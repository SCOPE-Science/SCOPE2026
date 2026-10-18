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
# Reproducibility

Run `python3 check.py` with a standard Python 3 installation. It computes rational-valued reciprocal block sums directly from every integer in the relevant digit intervals for bases 2 through 6 and lengths 1 through 7, checks the exact harmonic definitions and block estimates, and encloses the infinitely long sum using a proved geometric tail inequality. All five bases passed these tests.

The proof does not rely on those finite samples. To verify the infinite statement by hand, confirm the fixed-initial-digits inequality for lengths at least 4, the finite exact decomposition at lengths 1–3, the telescope \(\sum_{a=1}^{b-1}(1/a-a/(a+1)^2)=1-1/b+\sum_{j=2}^b1/j^2\), and the four-term error decomposition. The bound \(\sum_{j\ge1}j^{-2}<7/4\) follows, for example, by the elementary estimate \(1+1/4+\sum_{j\ge3}1/[j(j-1)]=1+1/4+1/2=7/4\) with strict inequality for the last summands. Note that no computer enumeration of finitely many bases proves the limit as \(b\to\infty\).

The checked scope is integer bases \(b\ge2\), with no assertion that the displayed uniform constant is optimal. The original scientific article may have undiscovered equivalent refinements, and independent scholarly validation remains unperformed.
