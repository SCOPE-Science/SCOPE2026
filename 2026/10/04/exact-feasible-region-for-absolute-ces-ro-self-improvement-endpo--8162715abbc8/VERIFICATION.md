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

The focal full text was checked at the definitions, Theorem 3.1, Example 3.2, and Remark 3.3. The source verifies the universal threshold and the two extreme examples at fixed optimal \(p\)-Cesàro constant.

For the new realization, the parameter choice \(\beta=p/Q\) gives weighted-shift constant \(K_Q=1/(1-\beta)=Q/(Q-p)\). The inequality \(Q\ge pK/(K-1)\) is algebraically equivalent to \(K_Q\le K\). Endpoint failure is exact because the normalized \(Q\)-orbit average of \(e_j\) is \(\sum_{{\ell=1}}^j1/\ell\).

The square-zero block has \(\lVert S_K\rVert^p=2K-1\), hence its worst normalized \(p\)-orbit sum occurs at length two and equals \(K\). On the \(\ell^p\)-direct sum, \(p\)-orbit sums add exactly, so the optimal constant is \(K\). For \(q\ge p\), the inequality \((a^p+b^p)^{{q/p}}\le2^{{q/p-1}}(a^q+b^q)\) transfers finite \(q\)-Cesàro bounds across the two summands, while the invariant weighted-shift summand transfers failure at \(Q\). This proves the claimed exact feasible region without computational extrapolation.

The literature comparison used the full arXiv HTML of arXiv:2610.00271v1, current indexed material for arXiv:2609.24601v1, publisher HTML for DOI:10.1016/j.jmaa.2020.124035, targeted semantic searches, and the previously indexed finding set for statement-level overlap. A differently phrased older direct-sum observation remains the principal originality risk.
