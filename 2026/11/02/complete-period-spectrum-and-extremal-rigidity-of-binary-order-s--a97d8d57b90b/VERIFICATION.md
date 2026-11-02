---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The complete finite certificate is `certificates/maximum_necklaces.txt`: 336 lexicographically minimal cyclic rotations of 36-bit words. Its SHA-256 is `e0838ac18297e49a77632d2017f8cee1d40359f65a6db4bec60bfab6b650432b`.

Run `python3 code/check.py` to enumerate every admissible order-seven cyclic class from all six-bit initial vertices without length pruning. It asserts the complete 29-entry nonzero period spectrum, total count 4788, optimal count 336, certificate equality, cyclic word validity, the common length-two/three profiles, balance, cyclic run count, and group-orbit counts. Actual run: 6,355,050 recursive states, `CHECK_OK` (record: `certificates/python-check-output.txt`).

Run `g++ -O2 -std=c++17 code/check_cpp.cpp -o check_cpp` followed by `./check_cpp certificates/maximum_necklaces.txt` to independently enumerate via the least-edge canonical root rule. Actual run: 766,602 states, `CHECK_CPP_OK`, identical 29-entry length spectrum and maximum certificate (record: `certificates/cpp-check-output.txt`). No third-party packages, external services or randomization are required. The two enumeration mechanisms share the mathematical de Bruijn reduction but have distinct rooting rules and implementations.

The exhaustion is an exact finite proof because every admissible cyclic word determines a closed trail of pairwise reversal-distinct seven-bit edges; both enumerators explore every permitted next edge without exclusions beyond the defining constraints. A shorter closed trail may be extended through the root; the software allows that extension. The checks establish nothing for orders other than seven. Literature priority and independent human validation remain separate from computational correctness.
