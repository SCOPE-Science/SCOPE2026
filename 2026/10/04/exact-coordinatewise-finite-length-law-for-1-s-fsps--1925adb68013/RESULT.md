# Exact coordinatewise finite-length law for ℓ1 S-FSPS
## Finding
Consider the composite projected-gradient specialization of S-FSPS in dimension \(n\ge1\) on the centered box
\[
S=\prod_{i=1}^n[-R_i,R_i],\qquad R_i>0,
\]
with \(A=I_n\), \(h\equiv0\), and \(g(u)=\|u\|_1\). Fix \(\chi>1\), initialize \(x^0\in S\) and \(z^0=0\), and let \((\gamma_k)_{k\ge0}\) be any positive nonincreasing sequence satisfying
\[
\gamma_k\to0,\qquad \sum_{k=0}^{\infty}\gamma_k=\infty.
\]
Then every nonzero coordinate keeps its initial sign and decreases in magnitude to zero, so \(x^k\to0\). More strongly,
\[
\sum_{k=0}^{\infty}\|x^{k+1}-x^k\|_1=\|x^0\|_1,
\]
and therefore
\[
\sum_{k=0}^{\infty}\|x^{k+1}-x^k\|_2\le \|x^0\|_1.
\]
Thus the Euclidean primal trajectory has finite length under every smoothing schedule allowed by the source's base conditions. In particular, power smoothing \(\gamma_k=(k+k_0)^{-\beta}\) has finite length for every \(0<\beta\le1\), including \(0<\beta\le1/2\), which is outside the source paper's general power-schedule range in Theorem 6.1.

## Assumptions and scope
The claim concerns equation (6.2) of arXiv:2609.28306v1 specialized to a separable \(\ell_1\) objective. The source defines
\[
\delta_k=\chi\left(L_{\nabla h}+\frac{\|A\|^2}{\gamma_k}\right).
\]
Here \(L_{\nabla h}=0\) and \(\|A\|=1\), so \(\delta_k=\chi/\gamma_k\). The initialization \(z^0=0\) gives \(x^1=x^0\). The box is centered at zero so a coordinatewise move toward zero remains feasible. No claim is made for arbitrary initial dual variables, nonseparable linear maps, nonmonotone smoothing, or summable smoothing sequences.

## Proof
For \(g(u)=\|u\|_1\), the Moreau-envelope gradient is coordinatewise:
\[
(\nabla g_\gamma(u))_i=\operatorname{clip}\!\left(\frac{u_i}{\gamma},[-1,1]\right).
\]
After the first dual update, equation (6.2) gives, for \(k\ge1\),
\[
z_i^k=\operatorname{clip}\!\left(\frac{x_i^k}{\gamma_{k-1}},[-1,1]\right),\qquad
x_i^{k+1}=x_i^k-\frac{\gamma_k}{\chi}z_i^k,
\]
provided the raw update stays in \(S\). We now show that it does.

Fix a coordinate with \(x_i^k>0\). If \(x_i^k>\gamma_{k-1}\), then \(z_i^k=1\) and
\[
0<x_i^k-\frac{\gamma_k}{\chi}<x_i^k,
\]
because \(\gamma_k\le\gamma_{k-1}<x_i^k\) and \(\chi>1\). If instead \(0<x_i^k\le\gamma_{k-1}\), then
\[
x_i^{k+1}=x_i^k\left(1-\frac{\gamma_k}{\chi\gamma_{k-1}}\right),
\]
whose multiplier belongs to \([1-1/\chi,1)\). The negative case is symmetric, and a zero coordinate remains zero. Hence every raw coordinate update lies between its current value and zero. It therefore remains inside its box interval, so the projection is inactive. Each nonzero coordinate preserves its sign and its magnitude is nonincreasing.

Let \(\ell_i=\lim_k|x_i^k|\). If \(\ell_i>0\), then eventually \(\gamma_{k-1}<\ell_i\le|x_i^k|\), so that coordinate stays in the outer regime and satisfies
\[
|x_i^{k+1}|=|x_i^k|-\frac{\gamma_k}{\chi}.
\]
The nonsummability of \((\gamma_k)\) would then force the nonnegative quantity \(|x_i^k|\) below zero, a contradiction. Thus every \(\ell_i=0\), proving \(x^k\to0\).

For each coordinate, sign preservation gives the finite telescoping identity
\[
\sum_{k=0}^{N}|x_i^{k+1}-x_i^k|=|x_i^0|-|x_i^{N+1}|.
\]
Summing over the finitely many coordinates and passing to the limit yields
\[
\sum_{k=0}^{\infty}\|x^{k+1}-x^k\|_1=\|x^0\|_1.
\]
Finally \(\|v\|_2\le\|v\|_1\) at every step, giving the Euclidean finite-length bound. Power schedules with \(0<\beta\le1\) satisfy all base smoothing assumptions, so the stated schedule extension follows.

## Verification
The proof is analytic and coordinatewise; no finite experiment is used as an infinite proof. The bundled verifier checks the recurrence, sign invariance, projection inactivity, exact finite \(\ell_1\)-telescoping identity, and Euclidean-length bound on several exact rational multidimensional schedules. The only infinite step is the explicit contradiction using the divergent tail \(\sum_k\gamma_k=\infty\).

## Relationship to prior work
Tao's arXiv:2609.28306v1 assumes the same base smoothing conditions \(\gamma_k\downarrow0\) and \(\sum_k\gamma_k=\infty\). Its Theorem 6.1 proves finite Euclidean primal length for definable composite problems under power schedules \(\gamma_k=(k+k_0)^{-\beta}\) with \(1/2<\beta\le1\); Corollary 5.5 shows the lifted-KL summability threshold is strictly above \(1/2\) for every finite lift exponent. The present result does not improve that general theorem. Instead, it identifies the canonical separable \(\ell_1\) box model as a class where direct coordinate order gives finite length for every base-admissible schedule, including all power exponents \(0<\beta\le1\).

The original S-FSPS framework, the 2020 variable-smoothing literature, and generic relaxed proximal-point theory explain the Moreau/proximal and soft-thresholding structure but do not state the exact coordinatewise path-length identity above. The 2026 counterexample paper shows that vanishing nonsummable smoothing alone does not imply whole-sequence convergence in general, so the separable order structure used here is essential rather than a generic consequence of the base assumptions.

## Limitations
The result applies to the centered-box, identity-map, separable \(\ell_1\) model with \(z^0=0\). It does not establish the same law for coupled linear maps, arbitrary convex feasible sets, arbitrary dual initialization, or general nonsmooth objectives. The exact identity is for accumulated \(\ell_1\) motion; Euclidean motion is bounded by it but need not equal it. A residual originality risk remains that an equivalent coordinatewise shrinkage identity occurs in specialized proximal literature not surfaced by the searches.

## References
1. Min Tao, *Whole-Sequence Convergence of Variable-Smoothing Full-Splitting Methods via a Lifted Kurdyka–Łojasiewicz Framework*, arXiv:2609.28306v1, 2026.
2. Radu Ioan Boţ, Guoyin Li, and Min Tao, *Full Splitting Algorithms for Fractional Programs with Structured Numerators and Denominators*, arXiv:2312.14341v2; SIAM Journal on Optimization 35 (2025), 2623–2653.
3. Radu Ioan Boţ and Axel Böhm, *Variable Smoothing for Convex Optimization Problems Using Stochastic Gradients*, Journal of Scientific Computing 85 (2020), article 33, DOI:10.1007/s10915-020-01332-8.
4. Guoyong Gu and Junfeng Yang, *A Unified and Tight Linear Convergence Analysis of the Relaxed Proximal Point Algorithm*, Journal of Industrial and Management Optimization 19 (2023), 3742–3749, DOI:10.3934/jimo.2022107.
5. Min Tao, *Failure of Whole-Sequence Convergence in Variable-Smoothing Full-Splitting Methods*, arXiv:2608.20859, 2026.
