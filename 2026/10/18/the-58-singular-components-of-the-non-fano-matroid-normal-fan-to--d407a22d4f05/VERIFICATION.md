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

# Reproducible exact checks

Execute `python3 VERIFY.py` with SymPy installed. The program uses only the explicit seven-element input and exact rational/integer matrix operations. It has no data downloads, random parameters, floating-point assumptions, or external certificates.

The checker independently confirms the basis-exchange axiom and proper flat list; the 29 bases, 20 irredundant facets, and all 801 nonempty faces; their dimension distribution \((29,138,263,242,108,20,1)\); all 800 nontrivial normal cones are saturated in the integral lattice; the 278 nonsimplicial cones; their exact inclusion-maximal set of 58 faces; and the unique \(\pm1\) relation sizes identifying all generic affine determinantal cones. An additional integer check confirms that every alleged quadrilateral component comes from a lattice parallelogram. The run exits with `VERIFY_OK` on success.

The toric semigroup argument in `RESULT.md` converts the circuit sizes into Segre determinantal transverse models; this mathematical argument is not replaced by execution logs. The same finite enumeration does not determine the nonreduced Jacobian singular scheme, all nongeneric analytic types, or novelty with mathematical certainty. No independent audit has been performed.
