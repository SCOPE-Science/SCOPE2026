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
# Exact verification record

The included `verify.py` executes with Python 3 and SymPy. It checks exact identities for all \(a\in\{-1,i,-i\}\), including the common-root exclusion and transversality resultants, the binary coordinate substitution, each required component swap/preservation identity, the antidiagonal lift of the union, the order-eight power relation, and the nonabelian order-sixteen projective relation. The expected final console line starts `VERIFY_OK:`.

The proof in `RESULT.md` is universal over \(\mathbb C\) for the three parameters. The script does not certify exhaustive group enumeration or the whole mathematical literature; completeness follows from the geometric forcing of a diagonal or antidiagonal binary matrix and exact coefficient comparisons. The checks are supplemental to the proof. Independent mathematical audit has not been performed.
