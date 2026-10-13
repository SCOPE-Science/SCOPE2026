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
# Verification

The bundled `verify.py` uses exact `Fraction` arithmetic for all algebraic acceptance checks. It:

1. evaluates \(H(23/100)>0\) and \(H(6/25)<0\);
2. constructs a Sturm sequence and proves that \(H\) has exactly one real root in \((23/100,6/25)\);
3. substitutes the stated rational expression for \(\eta\), sets \(w=z(\eta-1)\), and verifies that the branch equation and tangency equation have numerators divisible by \(H\);
4. uses Sturm checks to certify \(\eta>24/5\) and \(w>1/2\) throughout the isolating interval, so the reconstructed solution is on the source's upper branch;
5. only then bisects the isolated root with high-precision decimal arithmetic to print the numerical value.

A clean replay prints:

`VERIFY_OK roots=1 z=0.2315850309344787997498601221579911665... theta=0.4812328240410028387300726699536883826...`

The finite decimal output is not used to prove uniqueness, branch membership, or the exact identities. The verification does not independently re-prove the source's Gibbs-measure phase-count theorem; it verifies the new exact algebraic identification conditional on the source's tangency characterization of the distinguished critical point.
