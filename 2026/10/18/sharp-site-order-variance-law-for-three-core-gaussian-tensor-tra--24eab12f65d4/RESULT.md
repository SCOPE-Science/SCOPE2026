# Sharp site-order variance law for three-core Gaussian tensor-train trace estimation

## Finding
For a three-site real Gaussian tensor-train trace probe with integer bond dimension \(\chi\ge 1\), three nonzero positive-semidefinite local factors have a sharply optimal ordering: **put the factor with largest normalized squared Frobenius norm at the middle site.** The worst possible permutation-to-best-permutation variance ratio is at most \(\chi\), and this constant is the sharp supremum over all local dimensions and factors.

More exactly, for positive purities \(p,q,r\in[1/d,1]\) at the first, middle and last sites, define
\[
 V_\chi(p,q,r)=\frac{2(p+r)}{\chi}+\frac{4pr}{\chi^2}+\frac{2q}{\chi^2}[1+(\chi+1)p][1+(\chi+1)r].
\]
The variance of the unbiased single-probe trace estimator divided by the squared trace is exactly \(V_\chi(p,q,r)\). Given three purities \(a\ge b\ge c\), the minimum is \(V_\chi(b,a,c)\) and the maximum is \(V_\chi(a,c,b)\); reversal of the two end sites has no effect. The following bounds hold for *every* such triple:
\[
1\le\frac{V_\chi(a,c,b)}{V_\chi(b,a,c)}\le\chi.
\]
For \(\chi>1\), the upper inequality is strict at every finite local dimension; nevertheless it is optimal as a supremum when that dimension varies.

## Assumptions and scope
Fix integers \(d\ge2\), \(\chi\ge1\). For each physical index \(i,j,k\in\{1,\ldots,d\}\), independently sample standard real Gaussian vectors \(g_i,h_k\in\mathbb R^\chi\) and matrices \(M_j\in\mathbb R^{\chi\times\chi}\), with independent entries and independence among the three families. Define
\[
 \omega_{ijk}=\chi^{-1}g_i^{\mathsf T}M_jh_k.
\]
This is an isotropic three-core Gaussian tensor-train vector. Let \(D_1,D_2,D_3\) be arbitrary nonzero real symmetric positive-semidefinite \(d\times d\) matrices. Define \(t_j=\operatorname{tr}D_j>0\) and \(p_j=\operatorname{tr}(D_j^2)/t_j^2\). For each permutation \(\pi\) of \(\{1,2,3\}\), use the estimator \(X_\pi=\omega^{\mathsf T}(D_{\pi(1)}\otimes D_{\pi(2)}\otimes D_{\pi(3)})\omega\). All six target matrices have the same trace \(t_1t_2t_3\), spectrum and Frobenius norm. The Gaussian tensor-train distribution, however, distinguishes middle from endpoint sites whenever \(\chi>1\).

## Proof
**Unbiasedness and spectral reduction.** An application of Gaussian independence and \(\mathbb E[g_ig_{i'}^{\mathsf T}]=\delta_{ii'}I\) gives \(\mathbb E[\omega_{ijk}\omega_{i'j'k'}]=\delta_{ii'}\delta_{jj'}\delta_{kk'}\). Rotating the physical-index collections at any site by an orthogonal matrix preserves their joint standard-Gaussian law. Each symmetric factor can therefore be diagonalized without changing the estimator law. Let the diagonal weights at the first, middle and last sites be \(u_i,v_j,w_k\ge0\), respectively, and put \(t_u=\sum_i u_i\), \(s_u=\sum_i u_i^2\), analogously for \(v,w\).

**Exact variance.** Introduce random positive-semidefinite matrices \(G=\sum_i u_i g_ig_i^{\mathsf T}\) and \(H=\sum_k w_k h_kh_k^{\mathsf T}\). Conditional on \(G,H\), the independent middle Gaussian matrices give
\[
\mathbb E[X\mid G,H]=\chi^{-2}t_v\operatorname{tr}G\operatorname{tr}H,
\qquad
\operatorname{Var}(X\mid G,H)=2\chi^{-4}s_v\operatorname{tr}(G^2)\operatorname{tr}(H^2).
\]
The elementary Gaussian moments are
\[
\begin{aligned}
\mathbb E\operatorname{tr}G&=\chi t_u,\\
\mathbb E(\operatorname{tr}G)^2&=\chi^2t_u^2+2\chi s_u,\\
\mathbb E\operatorname{tr}(G^2)&=\chi t_u^2+\chi(\chi+1)s_u,
\end{aligned}
\]
with analogous identities for \(H\). Apply the law of total variance, the independence of \(G,H\), and divide by \((t_ut_vt_w)^2\). This yields exactly the displayed function \(V_\chi\), with \(p=s_u/t_u^2\), \(q=s_v/t_v^2\), \(r=s_w/t_w^2\).

**Optimal site.** Algebra yields the precise exchange law
\[
V_\chi(b,a,c)-V_\chi(a,b,c)=\frac{2(\chi-1)(a-b)(c-1)}{\chi^2}.
\]
Because \(0<c\le1\), moving a larger purity from an endpoint to the middle never increases variance. Repeated exchange proves the optimum; reversal symmetry proves the order of the endpoints is irrelevant. For \(\chi=1\), all site orderings coincide. For \(\chi>1\), equality between a swapped pair occurs when the exchanged purities tie or the other endpoint has purity one.

**Sharp universal amplification.** With \(a\ge b\ge c>0\), direct factorization gives
\[
\begin{aligned}
&\chi V_\chi(b,a,c)-V_\chi(a,c,b)\\
&=\frac{2(\chi-1)}{\chi^2}\bigl[abc(\chi+1)^2+ab(\chi+2)+ac(\chi+1)+bc+b\chi+c(\chi+1)\bigr]\ge0.
\end{aligned}
\]
This proves the universal factor \(\chi\). The square brackets are strictly positive when \(\chi>1\). To show sharpness, take one factor \(\operatorname{diag}(1,0,\ldots,0)\) and two factors \(I_d/d\), so \(a=1\) and \(b=c=1/d\). The ratio \(V_\chi(1,1/d,1/d)/V_\chi(1/d,1,1/d)\) tends to \(\chi\) as \(d\to\infty\). Thus no smaller uniform coefficient is possible.

## Verification
The standalone program `verify_order.py` performs 30,000 exact rational comparisons of the three site-order variances, the exchange identity, and the \(\chi\)-factor bound, over \(1\le\chi\le15\). It also directly simulates 140,000 independent Gaussian sketches per ordering at \(\chi=3\), \(d=4\), with distinct local purities, and tests the exact variance against independently generated samples. It evaluates near-sharp examples at increasing local dimensions. All its assertions passed. Finite computations supplement, but do not replace, the universal algebraic proof above.

## Relationship to prior work
Camaño, Epperly, Meyer and Tropp establish the Gaussian random-matrix-product-state construction and a full fourth-moment tensor, which in principle determines every fixed-observable variance. Bujanović, Kressner and Olić establish tensor-train Girard–Hutchinson moment and tail guarantees and discuss limitations of trace estimation. Their available full texts were checked for the three-site permutation optimization: neither states an optimal middle-site rule or a sharp universal permutation penalty. The exact fixed-target moment evaluation is therefore not claimed as an independent general theory; the claim here is the complete ordering inequality, its equality regime and its optimal amplification constant. This comparison cannot rule out a previously published equivalent rearrangement inequality in more general tensor probability literature.

## Limitations
The classification assumes independent *real standard-Gaussian* tensor-train cores, three sites, fixed common bond dimension, and nonzero positive-semidefinite local factors. It is a single-probe variance statement (independent averaging divides every variance by sample count). It does not claim an optimal permutation rule for higher tensor orders, indefinite or nonsymmetric local factors, complex cores, adaptive/non-Gaussian cores, or running-time improvements when changing a tensor network's mode ordering.

## References
1. C. Camaño, E. N. Epperly, R. A. Meyer and J. A. Tropp, *Linear algebra at exponential scale via tensor network dimension reduction*, arXiv:2606.15350v1 (first public version 2026-06-13), https://arxiv.org/html/2606.15350v1, especially Definition 1.1, §3.3, Theorem 4.3 and §4.5.
2. Z. Bujanović, D. Kressner and H. Olić, *Stochastic trace estimation with tensor train random vectors*, arXiv:2606.15679v1 (first public version 2026-06-14), https://arxiv.org/abs/2606.15679, especially Definition 1 and §§3–4.
