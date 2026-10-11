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

The proof was checked against the focal paper's exact normalization. The critical ground state is \(h(x)=\|x\|_p^{-(n-\alpha)/2}\), and the coefficient multiplying the double integral is \(C_{n,\alpha}/2\). For distinct shells \(S_k,S_\ell\), direct substitution of the shell measures, ground-state values and ultrametric distance gives
\[
\iint_{S_k\times S_\ell}
\frac{h(x)h(y)}{\|x-y\|_p^{n+\alpha}}\,dx\,dy
=(1-p^{-n})^2p^{-(n+\alpha)|k-\ell|/2}.
\]
The factor \(1/2\) disappears after summing the two ordered orientations of each distinct shell pair.

For the Hardy mass, \(\|x\|_p^{-\alpha}h(x)^2=\|x\|_p^{-n}\), and multiplication by \(|S_k|=(1-p^{-n})p^{-nk}\) gives the constant shell contribution \(1-p^{-n}\).

The sequence inequalities were checked symbolically. For support length \(2N+1\) with zero extension, the exact first path eigenvalue is
\[
\lambda_N=4\sin^2\!\left(\frac{\pi}{4N+4}\right).
\]
The chosen sine profile attains that nearest-neighbor Rayleigh quotient. For every positive integer \(m\), telescoping and Cauchy--Schwarz give \(D_m\le m^2D_1\), and the convergent geometric moment is
\[
\sum_{m\ge1}m^2r^m=\frac{r(1+r)}{(1-r)^3}.
\]
These identities yield the stated two-sided bounds without numerical approximation.

The verification establishes only the radial finite-annulus theorem stated in the finding. It does not certify an exact closed form for the best multiplicative constant, a nonradial extension, or a nonlinear \(L^q\) analogue.
