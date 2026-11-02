---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For 0<p<=1 the p-th quasi-triangle inequality on singular-value expansions bounds any input by its rank-one factors; testing rank-one factors gives equality. Orthogonal rotations reduce every masked rank-one xy* to B_(s,t)=[[sqrt(st),sqrt(s(1-t))],[sqrt((1-s)t),0]], whose singular-value squared sum is s+t-st and product sqrt(st(1-s)(1-t)). At fixed s+t increasing st decreases its largest singular value while strictly increasing a+b; since p<=1 the sum a^p+b^p strictly grows, attaining s=t. The k=sqrt(u/(4-3u)) derivative G(k)+H_p(k) has G decreasing and H_p strictly decreasing for p<1, with precisely one interior zero before 1/sqrt3; for p=1 it vanishes at 1/sqrt3. The formulas give the claimed sharp norm and extremizing rank-one projection; finite independent s,t tests and the p=1,1/2 endpoint algebra passed.

## originality

PASS

Best-of-knowledge originality for the full 0<p<1 sharp profile and optimizer, excluding qualitative boundedness and the trace-class endpoint as independent novelty. Actual primary theorem statements were compared by implication rather than numerical parameters alone.

## value

PASS

The three-one 2-by-2 cross is the smallest genuinely nontrivial Schur idempotent. Its exact sharp quasi-Schatten norm as a function of the exponent, its optimizer and trace-class endpoint supply a natural operator-ideal invariant omitted from qualitative support classifications. It is not merely verification that the pattern is bounded.

The dated certificate retains the supplied scientific assessment, sources and limitations.
