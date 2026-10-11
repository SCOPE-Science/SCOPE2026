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

For every Lipschitz observable \(f\), the source gives
\[
f-\int f\,d\mu_\alpha=c_f(\Phi-\alpha)+\widetilde f\circ\sigma-\widetilde f
\]
with
\[
|c_f|\le\frac{|f|_{\mathrm{Lip}}}{(1-\theta)^2},
\qquad
|\widetilde f|_{\mathrm{Lip}}\le\frac{\theta|f|_{\mathrm{Lip}}}{(1-\theta)^3}.
\]
The symbolic diameter is at most one. Sturmian balance gives \(|S_n(\Phi-\alpha)|<1\). Therefore the telescoped coboundary term contributes at most \(|\widetilde f|_{\mathrm{Lip}}\), and the total Birkhoff discrepancy is at most
\[
|f|_{\mathrm{Lip}}\left(\frac1{(1-\theta)^2}+\frac{\theta}{(1-\theta)^3}\right)
=\frac{|f|_{\mathrm{Lip}}}{(1-\theta)^3}.
\]
Dividing by \(n\) gives the empirical Wasserstein estimate.

For two empirical measures with the same number \(n\) of equally weighted atoms, optimal transport has a permutation optimizer, so its Wasserstein cost is exactly the matching pseudometric \(F_n\). The triangle inequality gives the stated upper bound.

For each \(n\), balance restricts the length-\(n\) digit counts to two adjacent integers. Their invariant mean is \(n\alpha\), which is not an integer, so both values occur and differ by one. The digit observable \(\Phi\) has Lipschitz seminorm one, and therefore its empirical averages provide the lower bound \(F_n\ge1/n\) for a suitable pair of orbit segments.

The proof is exact for every positive integer \(n\); no continued-fraction subsequence, finite enumeration, numerical experiment, or unproved limit transition is used. The multiplicative constants are valid but are not asserted to be sharp.
