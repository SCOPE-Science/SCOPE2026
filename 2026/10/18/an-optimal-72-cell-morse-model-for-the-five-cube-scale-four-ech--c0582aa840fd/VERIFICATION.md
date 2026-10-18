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

# Reproduction and limitations

The definition of the nerve, face encoding and deterministic matching appear in `RESULT.md` and `verify.cpp`. Running `g++ -O3 -std=c++17 verify.cpp -o verify && ./verify` gives the exact output in `verify_cpp_output.txt`. The program checks all face-poset cover edges and the complete directed acyclicity criterion; a Kahn traversal that misses one vertex triggers an assertion failure. Running `python fvector.py` gives `verify_python_output.txt` through a separately implemented submask enumeration. These are direct finite checks, not a sampled experiment, and each program was executed on the packaged source.

The CW homotopy and low-dimensional attaching-map deductions rely on Forman's theorem and the standard low-dimensional Hilton–Milnor decomposition, as detailed in `RESULT.md`. The independent homology computation of Adams–Shukla–Singh (Table 1, arXiv:2212.05871) gives the known ranks used only to prove minimality and not to certify graph acyclicity. No full homotopy classification can be claimed until the rank of \(Sq^2\) is independently determined. The inaccessible recent Biswas full text remains a documented novelty risk; all published comparisons were limited to actually accessible material.
