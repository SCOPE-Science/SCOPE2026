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

# Reproducible checks

Run `python3 verify.py` with the standard Python 3 library. The checker independently constructs prime fields and quadratic extension fields, diagonal quadratic forms in dimensions three and four, all primitive idempotent parameters, and all ordered factor pairs. It compares the computed count at **every vector part** against the three-branch fiber theorem, compares all excluded graph points against the discriminant criterion, and checks that total pairs equal the square of the primitive-idempotent count.

The twenty complete configurations cover \(q=3,5,7,11\) in dimensions \(3,4\), with square and nonsquare determinant classes, and \(q=9,25\) in dimension \(3\), with both determinant classes. Expected terminal line: `VERIFY_OK 20 complete configurations`.

Illustrative checked images: the ternary split case over \(\mathbb F_3\) has \(19\) product-graph points rather than \(27\), the anisotropic ternary case over \(\mathbb F_5\) with diagonal coefficients \((1,1,2)\) has \(101\) of \(125\), and the analogous nonsplit example over \(\mathbb F_{25}\) has \(15001\) of \(15625\).

These finite computations test the explicit statement and its boundary but cannot establish it for all odd prime powers or dimensions. The mathematical proof derives the universal formulas by orthogonal-complement decomposition and quadratic Gauss-sum identities. No independent audit was performed.
