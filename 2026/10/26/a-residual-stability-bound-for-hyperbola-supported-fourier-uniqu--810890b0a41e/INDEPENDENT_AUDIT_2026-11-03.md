# Independent mathematical audit

## correctness

PASS

Verified the actual six-file Git tree by recomputing the Git tree SHA from all six frozen blob IDs. Reconstructed the sampling lemma: on intervals l_n≤L, convexity gives ||If||²≤L Σ|s_n|²; lower gap δ gives ||(If)′||²=Σ|s_{n+1}−s_n|²/l_n≤4δ^−1Σ|s_n|²; Poincare–Wirtinger on f−If and triangle inequality yield equation (1) with C(L,δ)=√L+2L/(π√δ). Since tφ∈L2 automatically, the continuous representative φhat has L2 derivative with ||φhat′||2=π||ψ||2; applying the lemma at B with ℓ2 residual proves φhat∈L2 and hence tψ∈L2. Then apply it to ψhat at A, obtaining u≤αv+C_A R_A and v≤βu+C_B R_B for u=||ψ||2,v=||tψ||2; solving the 2×2 system gives exactly both formulas, since 1−αβ>0. Change of variables gives ||tφ||2=||ψ||2 and ||φ||2=||tψ||2; unitary 2^−1/2 Fourier normalization gives ||fhat′||2=π||tf||2. This is a universal analytic proof; no finite test, stored log or VERIFY_OK is used as a substitute. Exact criticality, sharpness, general H0 distributional representative and endpoint are bounded as stated.

## originality

PASS

Best-of-knowledge: the 2024 Radchenko–Ramos Theorem 2 and §4.2 prove exact-zero H0 uniqueness for the same gap product, by a two-sided Poincare–Wirtinger contraction, but do not state a finite additive bound in both nonzero ℓ2 sample residuals. The new theorem adds a normed linear interpolation lemma for nonzero data, an automatic H0→weighted-L2 regularity upgrade, and explicit two-axis constants. The 2011 hyperbola HUP and 2022 finite periodic NUDFT work do not give this nonuniform reciprocal-transform residual estimate. Its method is very close to known techniques; search cannot certify absolute priority.

## value

PASS

The natural observation problem is noisy Fourier recovery of a density on a hyperbola from two separated nonuniform arms. Exact uniqueness of H0 functions gives no quantitative conditioning under nonzero measurement errors. This result provides a concrete two-channel ℓ2 residual-to-L2 stability inequality in an infinite-dimensional class, with explicit sensitivity to both upper and lower gaps and the subcritical margin 1−αβ, and proves a nontrivial automatic weighted-L2 regularity upgrade from the data. A future stability/inverse-problem analysis can use precisely this estimate; it is not valued for a new uniqueness threshold, optimal constants, formal verification or code. The proof is short and leverages standard interpolation, narrowing but not removing its independent utility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
