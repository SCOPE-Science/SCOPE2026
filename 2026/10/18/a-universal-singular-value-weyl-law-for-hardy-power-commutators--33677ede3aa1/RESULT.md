# A universal singular-value Weyl law for Hardy power commutators

## Finding
Let \(H\) be the Hardy averaging operator on \(L^2(0,1)\): \((Hf)(x)=x^{-1}\int_0^x f(t)\,dt\). For \(\alpha>0\), write \(M_\alpha f(x)=x^\alpha f(x)\) and \(K_\alpha=HM_\alpha-M_\alpha H\). If singular values are arranged decreasingly, counting multiplicity and indexed from one, then
\[
\lim_{n\to\infty}n^2s_n(K_\alpha)=\frac4{\pi^2\alpha}.
\]
The operator is compact, quasinilpotent, and trace class with trace zero. Precisely, for every \(p>0\), \(K_\alpha\in\mathcal S_p\) if and only if \(p>1/2\); at the boundary \(K_\alpha\in\mathcal S_{1/2,\infty}\setminus\mathcal S_{1/2}\). Moreover,
\[
\|K_\alpha\|_{\mathcal S_2}^2=\frac{\alpha}{(1+\alpha)(1+2\alpha)}.
\]
Equivalently, for \(N_\alpha(t)=\#\{n:s_n(K_\alpha)>t\}\),
\[
\lim_{t\downarrow0}t^{1/2}N_\alpha(t)=\frac2{\pi\sqrt\alpha}.
\]

## Assumptions and scope
All spaces are complex Hilbert spaces with Lebesgue measure. The exponent \(\alpha\) is any fixed positive real number, including \(0<\alpha<1\); the limit is for fixed \(\alpha\) and is not asserted uniformly as \(\alpha\downarrow0\). We use the Schatten quasi-ideal \(\mathcal S_p\) also when \(0<p<1\). The weak ideal \(\mathcal S_{1/2,\infty}\) means \(\sup_{n\ge1} n^2s_n<\infty\). On \(0<t<x<1\), the integral kernel is
\[
 k_\alpha(x,t)=\frac{t^\alpha-x^\alpha}{x};
\]
elsewhere it is zero. Set \(\delta\in(0,1)\) arbitrarily and let \(J_{a,b}^2 f(x)=\int_a^x(x-t)f(t)\,dt\) on \(L^2(a,b)\).

## Proof
**1. Compactness and exact Hilbert--Schmidt norm.** Direct integration, first substituting \(t=xu\), yields
\[
\begin{aligned}
\|K_\alpha\|_{\mathcal S_2}^2
 &=\int_0^1\int_0^x\frac{(x^\alpha-t^\alpha)^2}{x^2}\,dt\,dx\\
 &=\frac1{2\alpha}\left(1-\frac2{\alpha+1}+\frac1{2\alpha+1}\right)
 =\frac{\alpha}{(\alpha+1)(2\alpha+1)}.
\end{aligned}
\]
This also proves boundedness and compactness. The formula is valid for every \(\alpha>0\).

**2. Regular second-order Volterra Weyl lemma.** Suppose \(0<a<b<\infty\), \(q\) is smooth on the closed triangle \(a\le t\le x\le b\), and \(h(x)=q(x,x)>0\). For
\[
(Tf)(x)=\int_a^x(x-t)q(x,t)f(t)\,dt,
\]
we have
\[
 \lim_{\tau\downarrow0}\tau^{1/2}N(T;\tau)
 =\frac1\pi\int_a^b\sqrt{h(x)}\,dx. \tag{1}
\]
Here \(N(T;\tau)=\#\{n:s_n(T)>\tau\}\).

First, Taylor expansion in the \(t\)-variable gives \(q(x,t)=h(x)+(x-t)r(x,t)\) with smooth \(r\); hence \(T=M_hJ_{a,b}^2+R\), where \(R\) has kernel \((x-t)^2r(x,t)\) on the lower triangle. Differentiation three times shows that \(R:L^2(a,b)\to H^3(a,b)\) continuously. The embedding \(H^3(a,b)\hookrightarrow L^2(a,b)\) has singular values \(O(n^{-3})\), thus \(s_n(R)=O(n^{-3})\). Ky Fan inequalities show that such a perturbation does not affect the coefficient of an existing \(n^{-2}\) singular-value asymptotic (take a discarded rank \(\lfloor\eta n\rfloor\), then let \(\eta\downarrow0\)).

For \(M_hJ^2\), partition \([a,b]\) into finitely many intervals \(I_j=[a_j,b_j]\). The operator differs from the orthogonal direct sum of the diagonal restrictions \(M_{h|_{I_j}}J_{I_j}^2\) by a finite-rank operator: across any two disjoint ordered intervals its kernel is \(h(x)(x-t)=xh(x)-t h(x)\), a sum of two separable terms. The finite rank does not change the coefficient. For the unweighted double-integration operator on an interval of length \(\ell\),
\[
 \lim_{n\to\infty}n^2s_n(J_I^2)=\frac{\ell^2}{\pi^2}. \tag{2}
\]
For completeness, \(J_I^2(J_I^2)^*\) has inverse fourth-derivative eigenproblem with conditions \(y(a)=y'(a)=y''(b)=y^{(3)}(b)=0\). Its positive frequency roots satisfy \(\cos(\kappa\ell)\cosh(\kappa\ell)=-1\) and are asymptotic to \((n-\tfrac12)\pi/\ell\), proving (2). If \(h_j^-\le h\le h_j^+\) on \(I_j\), the ideal property bounds the corresponding singular numbers between \(h_j^-s_n(J_{I_j}^2)\) and \(h_j^+s_n(J_{I_j}^2)\): indeed \(s_n(M_hA)\ge\|M_h^{-1}\|^{-1}s_n(A)\). Counting functions add under orthogonal direct sums. Thus the liminf and limsup of \(\tau^{1/2}N(M_hJ^2;\tau)\) lie between \(\pi^{-1}\sum_j|I_j|\sqrt{h_j^-}\) and \(\pi^{-1}\sum_j|I_j|\sqrt{h_j^+}\). Refinement and continuity give (1).

**3. Scaling recursion and an exact global constant.** Decompose \(L^2(0,1)=L^2(0,\delta)\oplus L^2(\delta,1)\). The lower-triangular block from input \((\delta,1)\) to output \((0,\delta)\) vanishes. The block from input \((0,\delta)\) to output \((\delta,1)\) has rank at most two, because its kernel is the sum of separable terms \(t^\alpha/x-x^{\alpha-1}\). Under unitary dilation from \((0,\delta)\) to \((0,1)\), the remaining upper-left block is exactly \(\delta^\alpha K_\alpha\). Write the lower-right block as \(K_{\alpha,\delta}\), the kernel restricted to \(\delta<t<x<1\). Therefore, modulo rank at most two,
\[
 K_\alpha\ \simeq\ \delta^\alpha K_\alpha\oplus K_{\alpha,\delta}. \tag{3}
\]
We have \(-k_\alpha(x,t)=(x-t)q_\alpha(x,t)\) with \(q_\alpha(x,x)=\alpha x^{\alpha-2}>0\). The regular lemma on \([\delta,1]\) gives
\[
 \lim_{\tau\downarrow0}\tau^{1/2}N(K_{\alpha,\delta};\tau)
 =L_\delta:=\frac1\pi\int_\delta^1\sqrt{\alpha x^{\alpha-2}}\,dx
 =\frac2{\pi\sqrt\alpha}(1-\delta^{\alpha/2}). \tag{4}
\]
For a rank-\(r\) perturbation, the singular-value counting functions differ by at most \(r\), by interlacing. Put \(\eta=\delta^\alpha\in(0,1)\). Equations (3)--(4) imply
\[
 N_\alpha(\tau)=N_\alpha(\tau/\eta)+N(K_{\alpha,\delta};\tau)+e(\tau),
 \qquad |e(\tau)|\le2. \tag{5}
\]
Iterate until \(\tau\eta^{-m}\ge\|K_\alpha\|\), with \(m=O(\log(1/\tau))\); the residual counting term is zero. On multiplying the sum of (5) by \(\sqrt\tau\), its error is \(O(\sqrt\tau\log(1/\tau))\to0\). For fixed \(j\), the \(j\)-th principal term tends to \(\eta^{j/2}L_\delta\); the boundedness of \(\sqrt z N(K_{\alpha,\delta};z)\) for all \(z>0\) gives a summable dominating geometric series. Dominated convergence therefore yields
\[
 \lim_{\tau\downarrow0}\sqrt\tau N_\alpha(\tau)
 =\frac{L_\delta}{1-\sqrt\eta}=\frac2{\pi\sqrt\alpha}, \tag{6}
\]
independently of \(\delta\). Monotone inversion of the counting asymptotic establishes \(\lim_{n\to\infty}n^2s_n(K_\alpha)=4/(\pi^2\alpha)\).

**4. Spectral and ideal consequences.** Since the singular sequence is asymptotic to a positive constant times \(n^{-2}\), its \(p\)-powers are summable exactly when \(2p>1\), and the stated weak critical membership follows. The operator is trace class. It has no nonzero eigenvalue: if \(K_\alpha f=\lambda f\) with \(\lambda\ne0\), choose \(\delta\) so that \(\delta^\alpha\|K_\alpha\|<|\lambda|\). The equation on \((0,\delta)\) forces \(f=0\) there; on \([\delta,1]\), the remaining integral equation is a bounded-kernel Volterra eigenvalue equation, which has only the zero solution by iterated-kernel factorial bounds. A compact operator with no nonzero eigenvalues is quasinilpotent. Lidskii's trace theorem then gives \(\operatorname{Tr}K_\alpha=0\).

## Verification
The accompanying standalone file `verify_hardy_commutator.py` uses exact rational arithmetic to test the kernel scaling identity, the rank-two cross-block decomposition and the analytic Hilbert--Schmidt integral for integer exponents. It is an algebraic regression test, not a substitute for the proof of the infinite-dimensional limit. The analytical boundary conditions, the regular Volterra lemma, the finite-rank recursion and the counting-function limit are given above, requiring no numerical truncation.

## Relationship to prior work
Gallardo-Gutiérrez, Partington and Ross (2025, arXiv:2501.14706v1) study invariant and related Hardy-operator structures, but their inspected complete manuscript does not supply this singular-value law for power-multiplier commutators. Belli, Gül, Ross and Siskakis (2026, arXiv:2604.19691) study a different weighted Cesàro integral operator and mention the classical Hardy average as comparison, not its present commutators. Earlier Volterra singular-number theory of Tuan and Gorenflo (1996) and Edmunds, Evans and Harris (1988) is especially relevant: the available abstract for the former gives asymptotics for weighted integral families, with its exact hypotheses and coverage not fully resolved. The full 1996 paper and the 1988 paper were not available for exhaustive theorem comparison. The result above provides a direct self-contained singular-endpoint analysis for the entire \(\alpha>0\) family; bibliographic uniqueness is not independently established.

## Limitations
The limit is for each fixed \(\alpha>0\), with no uniform error rate near \(\alpha=0\). In fact \(K_0=0\), so the limits in \(n\) and \(\alpha\) cannot be freely exchanged. Neither a complete singular-value formula at finite \(n\) nor sharp remainder bounds are proved. The general Volterra comparison requires independent full-text bibliographic follow-up; scientific provenance or originality is not independently certified.

## References
- E. A. Gallardo-Gutiérrez, J. R. Partington and W. T. Ross, *Hardy Operators: In the footsteps of Brown, Halmos, and Shields*, arXiv:2501.14706v1 (first posted 24 January 2025), https://arxiv.org/html/2501.14706v1.
- A. Belli, E. Gül, W. T. Ross and A. G. Siskakis, *The Cesàro operator on \(L^2(0,1)\)*, arXiv:2604.19691 (first posted 21 April 2026), https://arxiv.org/html/2604.19691v2.
- V. K. Tuan and R. Gorenflo, *Asymptotics of singular values of Volterra integral operators*, Numerical Functional Analysis and Optimization 17 (1996), 453–461, doi:10.1080/01630569608816704 (full text not inspected).
- D. E. Edmunds, W. D. Evans and D. J. Harris, *Approximation Numbers of Certain Volterra Integral Operators*, Journal of the London Mathematical Society 37 (1988), 471–489, doi:10.1112/jlms/s2-37.3.471 (full text not inspected).
