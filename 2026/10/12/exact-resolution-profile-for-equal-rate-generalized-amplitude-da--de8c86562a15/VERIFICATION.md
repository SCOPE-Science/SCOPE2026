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

The claim is analytic. The following checks were performed on the packaged derivation.

1. The equal-rate generator sends \(I\mapsto0\), \(X\mapsto-\mu X\), \(Y\mapsto-\mu Y\), and \(Z\mapsto-2\mu Z\). Exponentiation therefore gives Pauli eigenvalues \(1,e^{-\mu s},e^{-\mu s},e^{-2\mu s}\).
2. Solving the Pauli-channel eigenvalue equations gives
\[
p_I=\frac{(1+e^{-\mu s})^2}{4},\quad
p_X=p_Y=\frac{1-e^{-2\mu s}}{4},\quad
p_Z=\frac{(1-e^{-\mu s})^2}{4}.
\]
Their sum is one and each is nonnegative.
3. The complete-positive order \(\mathcal N_s\succeq p_I\,\mathrm{id}\) gives \(D_A(\mathrm{id}\|\mathcal N_s)\le-\log_2p_I\). A maximally entangled input gives equality because the Choi state is Bell diagonal and assigns probability \(p_I\) to the null Bell state.
4. For \(g(x)=-\ln((1+e^{-x})/2)\), \(g(0)=0\) and \(g''(x)<0\) for \(x>0\). Hence \(g(x)/x\) decreases strictly, so the fixed-resolution supremum occurs at the shortest allowed interval.
5. The local expansion \(g(x)=x/2-x^2/8+x^4/192+O(x^6)\) yields the displayed correction to \(\Gamma_{s_{\min}}\).

The packaged script `artifacts/verify.py` independently checks the probability identities, Pauli eigenvalues, series coefficients, and representative monotonicity values. Finite numerical checks are not used to establish the universal theorem.

Scientific limits: the theorem assumes an identity null semigroup, exactly equal transition rates, a qubit, and the idealized adaptive-control model of arXiv:2610.03629v1. It proves an asymptotic exposure-time exponent, not an exact finite-time error probability.
