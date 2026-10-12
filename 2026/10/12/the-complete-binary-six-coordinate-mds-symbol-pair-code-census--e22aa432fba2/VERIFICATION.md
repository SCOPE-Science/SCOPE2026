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

# Reproducible verification

The mathematical domain is exactly all subsets of size sixteen of the 64 binary length-six words, each tested with cyclic symbol-pair distance at least four. The known sharp Singleton upper bound is re-established by puncturing any adjacent two positions.

Use `g++ -O2 -std=c++17 pair6_enum.cpp -o pair6_enum` and run `./pair6_enum`; the output must begin with `# nodes 391978 solutions 76`. Every following line must match the data lines of `pair6_codes.txt` in the same order.

Run `python3 pair6_verify.py` in the directory containing `pair6_codes.txt`. This independent exact-cover enumerator checks 96 erasure-projection constraints, visits 685 nodes, finds the identical 76 catalogs, verifies every pair-distance directly, tests binary-affinity by translated XOR closure and reconstructs all five isometry orbits. It prints `EXACT_COVER_OK words=64 conditions=96 nodes=685`, `COUNT=76 AFFINE=44 NONAFFINE=32 ORBITS=5`, and the five sorted orbit representatives.

The two algorithms have separate search spaces (all distance-four cliques versus 96-column exact covers) and different completeness arguments. Finite exhaustive search here suffices because all possible binary length-six words are explicitly enumerated. No sampling, extrapolation, separate external audit, or cryptographic verification is claimed. Arithmetic uses exact integers only.
