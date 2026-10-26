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

# Reproducibility and verification

The standalone file `verify_double_subdivision.py` uses only the Python standard library. Execute `python3 verify_double_subdivision.py` from the directory containing that file; the script prints a summary and raises `AssertionError` if any test fails. The file `verification_output.txt` records a successful execution of the included script.

The script computes the proposed polynomial using inclusion-exclusion for edge covers and independent binomial-polynomial products for the two omitted-original cases. Separately, it constructs the graph from its explicit adjacency relation and checks every subset against the original closed-neighborhood double-domination criterion. For the seven parameter pairs \((2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4)\), every coefficient matched; altogether the oracle examined exactly \(1,755,392\) subsets. The minimum-size and minimum-count formula was additionally checked by integer arithmetic for 52 parameter pairs, with no floating-point approximations.

The smallest graphs provide the independent checks \(\mathcal D_{2,2}(z)=12z^6+8z^7+z^8\) and \(\mathcal D_{2,3}(z)=31z^8+34z^9+11z^{10}+z^{11}\).

These computations do not certify an infinite family by themselves. The proof in `RESULT.md` establishes necessity, sufficiency, disjointness, and enumeration for all integers \(2\le p\le q\). Independent validation has not been performed.
