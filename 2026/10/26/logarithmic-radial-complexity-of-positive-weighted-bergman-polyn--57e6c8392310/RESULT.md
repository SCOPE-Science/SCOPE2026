# Logarithmic radial complexity of positive weighted Bergman polynomial sampling

## Finding
Fix a real weight parameter \(\alpha>-1\), write \(\beta=\alpha+1>0\), and let \(\mathcal P_N\) denote the complex polynomials of degree at most the integer \(N\ge1\). The normalized weighted Bergman norm is
\[
\|P\|_{\alpha}^{2}=\frac{\alpha+1}{\pi}\int_{|z|<1}|P(z)|^2(1-|z|^2)^\alpha\,dA(z).
\]
Suppose arbitrary finitely many sites \(z_\nu\) in the closed unit disk have positive weights \(w_\nu>0\) and satisfy, with fixed \(0<A\le B<\infty\),
\[
A\|P\|_\alpha^2\le\sum_\nu w_\nu|P(z_\nu)|^2\le B\|P\|_\alpha^2\qquad(P\in\mathcal P_N).
\]
Let \(r\) be the number of distinct values of \(|z_\nu|\). With \(H_\beta\) and \(T_\beta\) explicitly defined in the proof, necessarily
\[
r\ge\frac{A}{e\,2^\beta H_\beta T_\beta B}\bigl(\lfloor\log_2N\rfloor+1\bigr).
\]
Conversely, an explicitly specified sampler with exactly \(J=\lceil\log_2(2(N+1))\rceil\) radii has positive weights and obeys
\[
A_\beta\|P\|_\alpha^2\le \mathcal Q_N(P)\le\|P\|_\alpha^2,
\qquad A_\beta=\frac{1-2^{-\beta}}{2\cdot4^\beta H_\beta}>0.
\]
In particular, under degree-independent positive frame bounds, the optimal distinct-radius growth order is \(\Theta_\alpha(\log(N+1))\). This is a statement about radial levels, not a claim of minimum total sample count or optimal numeric frame constants.

## Assumptions and scope
The samples may have arbitrary angular locations, repetitions, weights, and dependence on \(N\); only strict positivity and the displayed frame bounds are required. The lower theorem remains true if sampling on the boundary is allowed. For the construction, all points lie strictly inside the unit disk. There is no assumption of radial symmetry on an arbitrary competing sampler.

With \(P(z)=\sum_{k=0}^N a_kz^k\), orthogonality gives
\[
\|P\|_\alpha^2=\sum_{k=0}^N M_k|a_k|^2,\qquad
M_k=\beta\int_0^1t^k(1-t)^{\beta-1}\,dt
=\frac{\Gamma(\beta+1)\Gamma(k+1)}{\Gamma(k+\beta+1)}.
\]
Define
\[
H_\beta=\max\{1,2^\beta\Gamma(\beta+1)\}.
\]
The moment comparison used below is
\[
e^{-1}(k+1)^{-\beta}\le M_k\le H_\beta(k+1)^{-\beta}\quad(k\ge0).
\]

## Proof
**1. Moment comparison.** Substitute \(u=1-t\) into the beta integral. On \(0\le u\le1/(k+1)\), the factor \((1-u)^k\) is at least \((k/(k+1))^k\ge e^{-1}\), with the case \(k=0\) interpreted directly. This proves the lower estimate. For \(k\ge1\), \((1-u)^k\le e^{-ku}\), hence \(M_k\le\Gamma(\beta+1)k^{-\beta}\le2^\beta\Gamma(\beta+1)(k+1)^{-\beta}\). The case \(k=0\) gives \(M_0=1\).

**2. Dyadic exponential-peak lemma.** Put \(n_s=2^s\) for integers \(0\le s\le J_0\), \(J_0=\lfloor\log_2N\rfloor\). For all \(x\ge0\),
\[
\sum_{s=0}^{J_0}n_s^\beta e^{-xn_s}\le T_\beta\max_{0\le s\le J_0}n_s^\beta e^{-xn_s},
\]
where the following fully explicit constant is finite for every \(\beta>0\):
\[
T_\beta=\max\left\{
\frac1{1-(2/e)^\beta},\quad
\frac{e^\beta}{1-2^{-\beta}},\quad
\frac{e^{2\beta}}{1-2^{-\beta}}+
\frac{(2/e)^\beta}{1-(2/e^2)^\beta}
\right\}.
\]
Here is a proof with all endpoint cases. If \(x\ge\beta\), successive terms have ratio at most \((2/e)^\beta<1\). If \(x2^{J_0}<\beta\), the sum is at most \(2^{J_0\beta}/(1-2^{-\beta})\), while its last term is at least \(e^{-\beta}2^{J_0\beta}\). Otherwise \(0<x<\beta\) and there is a first index \(s_0\) with \(x2^{s_0}\ge\beta\); writing \(y=x2^{s_0}\), one has \(\beta\le y<2\beta\). The sum through \(s_0\) is bounded by \(e^{2\beta}/(1-2^{-\beta})\) times the term at \(s_0\). The succeeding terms, relative to that term, are at most \(2^{r\beta}e^{-\beta(2^r-1)}\), \(r\ge1\); the first is \((2/e)^\beta\) and later successive ratios are at most \((2/e^2)^\beta\). This gives the claimed tail bound. The case \(x=0\) is in the second case.

**3. Positive lower bound for radial levels.** Group the given sites by their distinct squared radii \(t_j=|z_\nu|^2\in[0,1]\), and let \(W_j\) be the sum of their positive weights. Testing the frame inequalities on \(P(z)=z^{n_s}\) gives
\[
A\le\sum_{j=1}^r W_jL_s(t_j)\le B,
\qquad L_s(t)=\frac{t^{n_s}}{M_{n_s}}.
\]
By the moment estimates, with \(h_s(t)=n_s^\beta t^{n_s}\),
\[
\frac{h_s(t)}{H_\beta}\le L_s(t)\le e\,2^\beta h_s(t).
\]
Applying Step 2 with \(x=-\log t\), and handling \(t=0\) separately (every \(L_s(0)=0\)), yields
\[
\sum_{s=0}^{J_0}L_s(t)\le e\,2^\beta H_\beta T_\beta\max_s L_s(t).
\]
For every fixed radius, positivity and the upper frame bound imply \(W_jL_s(t_j)\le B\) individually for each \(s\); hence \(W_j\max_sL_s(t_j)\le B\). Summing the lower inequalities over \(s\) now gives
\[
A(J_0+1)\le\sum_{j=1}^rW_j\sum_{s=0}^{J_0}L_s(t_j)
\le rBe\,2^\beta H_\beta T_\beta.
\]
This proves the lower bound without any angular-symmetry assumption.

**4. Matching explicit construction.** Set \(J=\lceil\log_2(2(N+1))\rceil\) and, for \(1\le j\le J\), choose \(t_j=1-2^{-j}\) and \(\rho_j=\sqrt{t_j}\). Let
\[
w_j=\begin{cases}
2^{-j\beta}-2^{-(j+1)\beta},&j<J,\\
2^{-J\beta},&j=J.
\end{cases}
\]
At each radius choose the \(N+1\) sites
\[
z_{j,m}=\rho_j\exp(2\pi i m/(N+1)),\qquad m=0,\ldots,N,
\]
with individual positive weights \(w_j/(N+1)\). Define \(\mathcal Q_N(P)\) as the resulting weighted sum of \(|P|^2\). Root-of-unity orthogonality (no nonzero difference of exponents between \(0\) and \(N\) is divisible by \(N+1\)) gives the exact diagonal form
\[
\mathcal Q_N(P)=\sum_{k=0}^N S_k|a_k|^2,
\qquad S_k=\sum_{j=1}^Jw_jt_j^k.
\]
Write \(d\mu_\beta(t)=\beta(1-t)^{\beta-1}dt\). For \(j<J\), \(w_j=\mu_\beta([t_j,t_{j+1}])\); and \(w_J=\mu_\beta([t_J,1])\). Because \(t\mapsto t^k\) is increasing, \(S_k\le\int_{1/2}^1t^k d\mu_\beta(t)\le M_k\).

For the reverse bound, take \(j_0=\lceil\log_2(2(k+1))\rceil\le J\) and \(x=2^{-j_0}\). Then \(1/[4(k+1)]<x\le1/[2(k+1)]\). Bernoulli's inequality gives \((1-x)^k\ge1-kx\ge1/2\); moreover \(w_{j_0}\ge(1-2^{-\beta})x^\beta\), whether or not \(j_0=J\). Therefore
\[
S_k\ge w_{j_0}(1-x)^k
\ge\frac{1-2^{-\beta}}{2\cdot4^\beta}(k+1)^{-\beta}
\ge A_\beta M_k.
\]
The diagonal form establishes the claimed frame bounds, completing the proof.

## Verification
The standalone Python checker `check.py` computes all monomial eigenvalues for 60 combinations of \(\beta\in\{1/2,1,2,4\}\) and \(1\le N\le512\), replays exact-rational monomial comparisons for integer parameters, tests the angular orthogonality criterion, and stress-tests the dyadic lemma over representative scales. The retained `check_output.txt` records 17,469 successful finite assertions. The all-parameter theorem follows analytically from Steps 1–4, not from those finite checks. Both checker files are included beside this report in the self-contained package.

## Relationship to prior work
Gröchenig and Ortega-Cerdà's 2020 preprint (later Journal of Geometric Analysis, 2021) analyzes degree-uniform Marcinkiewicz–Zygmund sampling for Bergman and Hardy polynomials, reproducing-kernel weights, and limits of sampling families. Its Theorems 1.1, 2.9–2.11 describe sampling conditions and geometry but do not state the minimum number of distinct radii for arbitrary positive weighted point schemes or the matching dyadic-circle construction. The later Fock-space paper develops a related sampling framework for Gaussian moments; its conclusions concern a different radial measure. Our distinction is the exact logarithmic radial-level growth forced by beta moments of weighted Bergman monomials, even with freely chosen angular sites and positive weights. McLean (2016) gives positive exponential-sum approximations to reciprocal powers over intervals with logarithmically many nodes, so a generic positive upper construction is already anticipated by approximation theory. The present conclusion concerns the matching *necessity* of logarithmically many physical radii under entirely arbitrary positive Bergman polynomial samplers, without symmetry assumptions. An unstated deduction from older power-law approximation lower bounds remains an originality risk.

## Limitations
The proof does not determine a sharp multiplicative constant in front of \(\log N\), an exact minimum number of radii for each \(N\), or the optimal total number of sites. Positivity of the sampling weights is essential to the lower-bound argument; the theorem makes no claim for signed or complex quadrature weights. The frame constants in the constructive upper bound may be small when \(\alpha\) is large, but are uniform in degree for each fixed weight parameter. Independent scientific validation and exhaustive historical literature verification have not been performed.

## References
1. K. Gröchenig and J. Ortega-Cerdà, *Marcinkiewicz–Zygmund Inequalities for Polynomials in Bergman and Hardy Spaces*, arXiv:2005.14176 (first version 2020-05-28); J. Geom. Anal. 31 (2021), 7595–7619. https://arxiv.org/abs/2005.14176 ; https://doi.org/10.1007/s12220-020-00599-5 .
2. K. Gröchenig and J. Ortega-Cerdà, *Marcinkiewicz–Zygmund inequalities for polynomials in Fock space*, Math. Z. 302 (2022), 1409–1428. https://doi.org/10.1007/s00209-022-03087-4 .
3. W. McLean, *Exponential Sum Approximations for t^{-beta}*, arXiv:1606.00123 (2016). https://arxiv.org/abs/1606.00123 .
