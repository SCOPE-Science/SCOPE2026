# A sharp sampling-degeneracy transition for the terminal risk of stochastic proximal point iteration

## Finding

Consider the nonuniformly sampled stochastic proximal point algorithm, with its probability-dependent proximal scaling, on the canonical pair of strongly convex quadratics
\[
f_1(x)=x^2,\qquad f_2(x)=\tfrac12(x-1)^2,\qquad f(x)=\tfrac12(f_1(x)+f_2(x)).
\]
For each fixed \(\gamma>0\), independently select \(f_1\) with probability \(p\in(0,1)\) and \(f_2\) with probability \(1-p\), and apply the published SPPM-NS iteration. Let \(R(p,\gamma)\) denote the limiting mean-squared error relative to the minimizer \(x_\star=1/3\). A unique sharp threshold
\[
\gamma_\star=1.4333451253134435396\ldots
\]
is the positive root of
\[
100\gamma^5+5829\gamma^4-3240\gamma^3+2112\gamma^2-8064\gamma-8448=0.
\]
If \(0<\gamma<\gamma_\star\), the infimum of \(R(p,\gamma)\) on \(0<p<1\) is attained at an interior probability and is strictly less than \(1/9\). If \(\gamma=\gamma_\star\), the minimum equals \(1/9\) and is attained by at least one interior probability. If \(\gamma>\gamma_\star\), every legal interior probability has \(R(p,\gamma)>1/9\), whereas \(R(p,\gamma)\to1/9\) as \(p\uparrow1\). Thus, for all \(\gamma>\gamma_\star\), no strictly positive two-component sampling distribution minimizes the terminal risk: its infimum occurs only at the excluded, one-component limit. This statement concerns stationary risk, not the convergence-rate objective or finite-iteration performance.

## Assumptions and scope

Fix \(\gamma>0\), \(p\in(0,1)\), and any deterministic finite \(x_0\in\mathbb R\). At every iteration draw \(I_k\in\{1,2\}\) independently with probabilities \(p\) and \(1-p\), and set
\[
x_{k+1}=\operatorname{prox}_{\gamma/(2p_{I_k})f_{I_k}}(x_k),\qquad p_1=p,\quad p_2=1-p.
\]
The proximal convention is \(\operatorname{prox}_{\alpha h}(x)=\arg\min_y\{h(y)+\|y-x\|^2/(2\alpha)\}\). Define \(R(p,\gamma)=\lim_{k\to\infty}\mathbb E[(x_k-1/3)^2]\). The comparison value \(1/9\) is the limiting risk as \(p\uparrow1\); \(p=1\) itself is not an allowed sampling probability. Every expectation is over the independent choices, in exact real arithmetic.

## Proof

**1. Affine random dynamics and stationary moments.** Direct minimization of the two quadratic proximal objectives yields
\[
x_{k+1}=\begin{cases}q_1x_k,&I_k=1,\\ q_2x_k+1-q_2,&I_k=2,\end{cases}
\qquad q_1=\frac{p}{p+\gamma},\quad q_2=\frac{2(1-p)}{2(1-p)+\gamma}.
\]
Both \(q_1,q_2\) lie strictly between zero and one. The affine maps preserve \([0,1]\), and a coupling using identical random choices contracts any two trajectories by at most \(\max(q_1,q_2)^k\). Backward iteration from any point in \([0,1]\) therefore constructs a unique invariant probability law, and coupling implies convergence in law and in the first two moments from any finite deterministic start. In particular \(R\) exists.

Write \(d=1-q_2\), \(A=pq_1+(1-p)q_2\), \(B=(1-p)d\), \(C=pq_1^2+(1-p)q_2^2\), \(D=2(1-p)q_2d\), and \(E=(1-p)d^2\). The stationary first moment \(m\) and second moment \(s\) satisfy, by conditioning on \(I_k\),
\[
m=Am+B,\qquad s=Cs+Dm+E.
\]
Since \(A,C<1\), they are uniquely determined by
\[
m=\frac{B}{1-A},\qquad s=\frac{Dm+E}{1-C},\qquad R=s-\tfrac23m+\tfrac19.
\]
These equalities give an exact rational risk expression for all admissible \(p,\gamma\), with no stochastic approximation.

**2. The sign polynomial.** Set
\[
\begin{aligned}
F(p,\gamma)&=-\gamma^3+(-3p^2+8p-4)\gamma^2+9p^2(1-p)\gamma+12p^2(1-p)^2,\\
H(p,\gamma)&=\gamma^3+2(2-p)\gamma^2+3p(1-p)(4-p)\gamma+12p^2(1-p)^2.
\end{aligned}
\]
Substitution and common-denominator reduction of the moment equations gives the exact identity
\[
R(p,\gamma)-\frac19=-\frac{(1-p)(\gamma+p)F(p,\gamma)}{3(\gamma+3p(1-p))H(p,\gamma)}.
\]
All factors in the denominator and the prefactor are positive for \(\gamma>0\), \(0<p<1\). Hence \(R<1/9\), \(R=1/9\), or \(R>1/9\) according as \(F>0\), \(F=0\), or \(F<0\). The rational moment formulas also give \(\lim_{p\downarrow0}R=4/9\) and \(\lim_{p\uparrow1}R=1/9\).

**3. A single phase change.** At every fixed \(p\in(0,1)\), \(F\), regarded as a polynomial in positive \(\gamma\), has the descending coefficient signs of \((-1,c, +,+)\), where \(c\) may have either sign. By Descartes' rule, there is at most one positive root, counted with multiplicity. As \(F(p,0)>0\) and \(F(p,\gamma)\to-\infty\) with growing \(\gamma\), exactly one positive root \(g(p)\) exists, with \(F(p,\gamma)>0\) precisely when \(0<\gamma<g(p)\).

There is a nontrivial positive regime: \(F(4/5,1)=587/625>0\). Conversely, expanding \(F(p,2)\) in the degree-four Bernstein basis \(\binom4j p^j(1-p)^{4-j}\) gives the five coefficients
\[
-24,\quad-16,\quad-5,\quad-\frac32,\quad-4.
\]
Every basis function is nonnegative on \([0,1]\), so \(F(p,2)<0\) throughout that interval. Consequently the supremum \(g_\star=\sup_{0<p<1}g(p)\) lies strictly between \(1\) and \(2\). Take a sequence \(p_n\) for which \(g(p_n)\uparrow g_\star\). A subsequence converges to some \(\bar p\in[0,1]\); continuity of \(F\) gives \(F(\bar p,g_\star)=0\). But
\[
F(0,\gamma)=-\gamma^2(\gamma+4),\qquad F(1,\gamma)=\gamma^2(1-\gamma),
\]
both negative for \(\gamma>1\). Thus \(0<\bar p<1\). As \(F(p,g_\star)\le0\) for every interior \(p\), \(\bar p\) is an interior maximizer, hence
\[
F(\bar p,g_\star)=0,\qquad\partial_pF(\bar p,g_\star)=0.
\]
A direct exact polynomial resultant computation yields
\[
\operatorname{Res}_p(F,\partial_p F)=-324\gamma^4(3\gamma+2)^2P(\gamma),
\]
where \(P\) is the quintic in the finding. It follows that \(P(g_\star)=0\). For \(0<\gamma\le1\), bounding its positive monomials by \(100+5829+2112=8041<8448\) shows \(P(\gamma)<0\). For \(\gamma\ge1\), its derivative is
\[
P'(\gamma)=500\gamma^4+\gamma^2(23316\gamma-9720)+4224\gamma-8064>0,
\]
since the middle term is at least \(13596\) and the last two terms together cannot offset it (the final linear term is at least \(-3840\)). Finally \(P(1)=-11711\) and \(P(2)=54416\). Thus \(P\) has a unique positive root, so \(g_\star=\gamma_\star\).

If \(\gamma<\gamma_\star\), the definition of the supremum provides an interior \(p\) with \(F>0\), hence \(R<1/9\). Because the boundary risk limits are \(4/9\) and \(1/9\), continuity of \(R\) forces its global infimum to be attained at an interior point. At \(\gamma=\gamma_\star\), the constructed \(\bar p\) gives \(F=0\) and no other probability has \(F>0\), so the minimum \(1/9\) is attained. If \(\gamma>\gamma_\star\), every positive root \(g(p)\le\gamma_\star\), so \(F<0\) throughout \(0<p<1\), and \(R>1/9\). The limit \(p\uparrow1\) makes the infimum \(1/9\) but never attains it. This proves the classification.

## Verification

The standalone `verify.py` program (Python 3 with SymPy) checks the exact stationary-moment identity, the resultant factorization, both boundary formulas, the five rational Bernstein coefficients, the quintic's endpoint signs and derivative formula, and two rational-risk witnesses. It also iterates the exact first/second moment recurrences for 25 rational parameter pairs to verify convergence to the derived stationary expressions. Running `python verify.py` returns `PASS`. The proof above, not the finite checks or numerical root calculation, establishes the assertion for every real \(p\) and \(\gamma\) in scope.

As exact examples, \(R(4/5,1)=105400/1091241<1/9\). The rate-optimized probability \(p=2/3\) in the originating paper gives \(R(2/3,1)=2/21\) but \(R(2/3,2)=2/15>1/9\).

## Relationship to prior work

Richtárik, Sadiev, and Demidovich's 2024 preprint, Appendix B.3, Algorithm 3 and Theorem 3, specifies SPPM-NS and derives a linear convergence-to-neighborhood bound. Its sampling discussion distinguishes choices optimizing a guaranteed contraction rate or variance-bound term. That analysis provides the algorithm and the fixed-step context but not the exact stationary quadratic risk or the sharp transition between an attained interior minimum and an excluded one-component limit. Ryu and Boyd's 2017 stochastic proximal iteration manuscript analyzes general stochastic proximal mappings and their asymptotic and nonasymptotic convergence properties, not the two-curvature probability-dependent scaling and terminal-risk threshold here. Related coordinate-sampling, loopless variance reduction, and stochastic Polyak-step findings address different updates and objectives and do not imply the present quintic threshold.

## Limitations

The result uses exactly two specified one-dimensional strongly convex quadratics, independent sampling with positive probabilities, and a fixed positive proximal parameter. The classification is of the best **stationary** mean-squared error relative to the full-sum minimizer; it does not determine the exact interior minimizing probability when one exists, nor compare transient performance, computational cost, or general higher-dimensional stochastic objectives. A limiting probability of one is excluded by the method definition, and ignoring the other component can undermine finite-time learning or identification. The exact priority of the algebraic threshold in all related random-affine recurrence literature is not independently established.

## References

1. P. Richtárik, A. Sadiev, Y. Demidovich, *A Unified Theory of Stochastic Proximal Point Methods without Smoothness*, arXiv:2405.15941v1 (first public 24 May 2024), Appendix B.3, Algorithm 3 and Theorem 3. https://arxiv.org/pdf/2405.15941
2. E. K. Ryu and S. Boyd, *Stochastic Proximal Iteration: A Non-Asymptotic Improvement Upon Stochastic Gradient Descent*, manuscript (2017), Sections 2–5. https://web.stanford.edu/~boyd/papers/pdf/spi.pdf
