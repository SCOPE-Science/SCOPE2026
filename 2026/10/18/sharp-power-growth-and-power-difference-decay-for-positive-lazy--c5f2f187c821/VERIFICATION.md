---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For fixed 1<p<infinity, 0<alpha<1/p and 0<delta<1, the weighted backward shift W has exact W^k e_j=(j/(j-k))^alpha e_{j-k} for k<j and zero otherwise, so norm ||W^k||=(k+1)^alpha. The positive p-absolutely Cesàro estimate follows from summing (j/(j-k))^{alpha p} over k<j and bounding j^{alpha p-1}sum_{i<=j}i^{-alpha p} <= (1-alpha p)^-1; convex-averaging preservation follows from Arnold Lemma 7.3. Weighted eigenvectors j^{-alpha}z^{j-1} for |z|<1 and spectral radius one give sigma(W)=closed disk; the affine spectrum of T contacts unit circle only at 1. Exactly, (T^n)_{ij}=(j/i)^alpha b_n(j-i), and (T^{n+1}-T^n)_{ij}=-delta(j/i)^alpha h_n(j-i), h_n(k)=b_n(k)-b_n(k-1). For Bin(n,delta), ||b_n||_1=1, ||b_n||_{p'}=O(n^{-1/(2p)}), ||h_n||_1=O(n^-1/2), ||h_n||_infty=O(n^-1), hence ||h_n||_{p'}=O(n^{-1+1/(2p')}). For output i>=sqrt(n), j/i=O(sqrt n) on kernel support; Young gives n^{alpha/2} and n^{(alpha-1)/2} upper bounds. On i<sqrt(n), Hölder bounds each row by C n^alpha i^{-alpha}||b/h||_{p'}, summing i^{-alpha p} gives the same upper rates precisely because alpha p<1. For lower bounds, take unit positive input supported on J_n=n delta+[2,3]sqrt n and evaluate on I_n=[1,1.5]sqrt n: b_n(k)>=c n^-1/2, h_n(k)<=-c n^-1 uniformly because the standardized deviations k-n delta are in a compact positive window, and (j/i)^alpha>=c n^{alpha/2}. Their signs are coherent and O(sqrt n) summands yield matching lower operator norm powers. Direct binomial witness computation at n=256 and 1024 (p=2,alpha=.3,delta=.4) gives stable positive normalized lower witnesses, a finite diagnostic only. This does not prove exact leading constants or the arbitrary positive-operator Katznelson–Tzafriri question.

## originality

PASS

The full Arnold 2026 paper gives the precise same shift and p-ACB constant (Example 3.2), the convex lazy-averaging p-ACB lemma (7.3), and a different ℓ1 counterexample (Proposition 7.1) to a general successive-power property. The full Abbar–Arnold–Coine 2026 preprint §3.3 Example 3.10 gives unaveraged weighted-shift power growth/ACB, not the binomially averaged reflexive consecutive-difference exponent. The Resultary finite-horizon worst-case result over all p-ACB operators does not imply this fixed shift’s matching upper/lower n^{(alpha-1)/2} law. Known ingredients are credited and only the new sharp two-sided reflexive lazy growth and decay laws assessed original.

## value

PASS

This natural concrete positive p-absolutely Cesàro bounded model sits next to the positive Katznelson–Tzafriri question. The new sharp exponents show an explicit divergence of ||T^n|| at n^{alpha/2} simultaneous with ||T^{n+1}-T^n|| decay at n^{(alpha-1)/2} for every reflexive exponent p and admissible alpha; both upper/lower orders are nontrivial. It is a motivated exact quantitative model fact, not a claim to solve the open arbitrary-operator question or a renaming of unaveraged shift growth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
