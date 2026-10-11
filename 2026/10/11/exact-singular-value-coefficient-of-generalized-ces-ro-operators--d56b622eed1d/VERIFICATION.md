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

# Verification of the singular-value asymptotic

The proof uses an exact finite-band decomposition and classical Hilbert-space singular-number inequalities. Its load-bearing comparisons are: a trace-class within-block diagonal defect (the \(\sum_{k\ge1} k^{-2}\) bound); rank at most \(m\) per boundary with weak count coefficient at most \(mM/B\); the exact direct-sum count of blocks \(Q_B/(kB)\); a rank-at-most-\(m\) replacement of \(Q_B\) by a circulant; and an ideal inequality bounding the discarded analytic-symbol tail by \(\delta_m/n\). Sending the block size to infinity before the perturbation tolerance, and sending the polynomial degree to infinity before that tolerance in the Wiener extension, avoids an unsupported exchange of limits.

Independent endpoint check: at \(t=0\), \(C_0=D\) and \(s_n(C_0)=1/n\). For two interior parameters, the northwest \(240\)-square sections were assembled by \(C_t[n,j]=t^{n-j}/(n+1)\) when \(j\le n\), zero otherwise, and full numerical singular values computed. At \(t=0.3\), the elliptic coefficient is \(1.023715546376166\), versus \(n s_n\) approximately \(1.02370\), \(1.02371\), \(1.02371\) at \(n=20,40,75\). At \(t=0.7\), the corresponding coefficient is \(1.175005293105528\), versus \(1.17487\), \(1.17497\), \(1.17499\). The end of the finite singular spectrum has a truncation boundary layer, so these finite checks have no role in proving the infinite limit.

The symbols are normalized against the standard orthonormal Fourier basis, with angular integration divided by \(2\pi\). Singular indices start at \(n=1\), while matrix coordinates start at \(0\). The theorem holds for the real representation because complexification preserves singular values of a real Hilbert-space matrix. The noncompact endpoint \(t=1\), general nonabsolutely summable Toeplitz symbols, and sharper remainder terms are unproved.
