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
# Verification procedure

With Python 3.10+ installed, execute `python verify_tame_bit.py` in a working directory containing all delivered artifacts; this requires only the Python standard library. It will exhaustively test all degree-2, degree-4, and degree-6 maps over the two-element field, calculate the exact ramification profile and two-sided projective orbits, and regenerate `tame_d6_pairs.txt`. The expected terminal summary is:

```
degree 2 all_maps 24 tame 0 profiles {}
degree 4 all_maps 384 tame 0 profiles {}
degree 6 all_maps 6144 tame 72 profiles {((1, 3), (1, 5), (2, 3)): 72}
degree 6: two disjoint orbits of size 36, representatives x/(x^6+x^3+1) and x/(x^6+x^5+x^3+1)
PASS
```

Execute `python verify_tame_sympy.py` with SymPy installed. It uses independent polynomial arithmetic for exhaustive degree-two and degree-four checks and for all 72 degree-six candidates in the certificate, yielding `INDEPENDENT SYMBOLIC PASS`. This second code does not perform a second complete search over all 6144 degree-six rational maps. The certificate has 72 distinct sorted two-integer rows and is regenerable from the primary code. All computations were completed with these files. The proof of the Hasse-jet criterion and the finite total search domain is presented in `RESULT.md`; the computation checks rather than replaces those arguments.

## Limits
These checks certify statements about rational maps defined over \(\mathbf F_2\); they do not test maps over arbitrary field extensions. No published mathematical claim of novelty can be inferred solely from successful programs.
