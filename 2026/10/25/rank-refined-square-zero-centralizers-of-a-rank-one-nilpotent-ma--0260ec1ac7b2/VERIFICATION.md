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
# Verification details

The associated `verification/verify.py` is a standalone Python 3 program. Invoke with `python3 verification/verify.py`. It enumerates matrices \(B\) directly, checks \(B^2=0\), enumerates every covector \(f\), vector \(g\), and scalar \(c\), checks the exact equations \(fB=Bg=f(g)=0\), and computes ordinary rank by elimination over each field. It compares every nonempty joint rank fiber with the symbolic Gaussian-binomial formula and raises an assertion if any differs.

Actual completed cases: \((q,b)=(2,1),(2,2),(2,3),(3,1),(3,2),(4,1),(4,2),(5,1)\). The fields include the extension field \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\). All completed with the success marker `COMMUTING_SQUARE_ZERO_RANK_FIBERS_OK`. The \(b=1\) cases serve as extra independent boundary comparisons, not part of the new scope \(b\ge2\).

For the in-scope cases, direct enumerations gave \(44,576,315,1264\) commuting square-zero matrices at \((q,b)=(2,2),(2,3),(3,2),(4,2)\), respectively, and the full rank-fiber table matched. The proof handles arbitrary prime powers and every \(b\ge2\); finite checking does not certify infinitely many instances. The scientific review here is internal self-review, not an independent audit.
