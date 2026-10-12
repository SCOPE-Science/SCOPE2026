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

The proof is symbolic. For \(1\le j\le r-1\) with \(m=r-j\), the exact term valuation is
\[
2j-2+\frac{p^m-1}{p-1}+jp^m,
\]
and its excess over \(3r-2\) is
\[
j(p^m-1)+\frac{p^m-1}{p-1}-3m.
\]
This excess is positive except for \(p=3,r=2,j=1\). The factorial-only term also lies strictly above the target except at \(p=3,r=2\). The terminal term has valuation exactly \(3r-2\). In the exceptional case, the three normalized terms modulo \(3\) are \(a,2a,a\), so their sum is \(a\not\equiv0\pmod3\).

`verify.py` checks the exact defining sum on a finite grid and checks the valuation inequalities on a wider finite grid. `verifier_output.txt` records the replay result. These computations do not replace the all-parameter proof.
