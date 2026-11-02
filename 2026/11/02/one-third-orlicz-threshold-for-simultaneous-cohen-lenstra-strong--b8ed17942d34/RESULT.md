# One-third Orlicz threshold for simultaneous Cohen–Lenstra strong laws

## Finding
Fix a prime \(\ell\), and let \(\mathcal G_\ell\) be the set of isomorphism classes of finite abelian \(\ell\)-groups. Equip it with the Cohen–Lenstra probability
\[
p_\ell(G)=\frac{c_\ell}{|\operatorname{Aut}G|},\qquad c_\ell=\prod_{j\ge1}(1-\ell^{-j}).
\]
For \(0<\beta<1\), define the convex Young function and its Luxemburg space by
\[
\Phi_\beta(t)=\int_0^t\exp\!\bigl((\log(e+s))^\beta\bigr)\,ds,\qquad
\|f\|_{\Phi_\beta}=\inf\left\{a>0:\sum_{G\in\mathcal G_\ell}p_\ell(G)\Phi_\beta(|f(G)|/a)\le1\right\}.
\]
Let \(G_1,G_2,\ldots\) be independent samples from \(p_\ell\). There is a phase boundary at exponent \(1/3\), with the endpoint excluded:

**Above the boundary:** for every \(1/3<\beta<1\), with probability one a *single* sample sequence satisfies
\[
\lim_{n\to\infty}\frac1n\sum_{i=1}^n f(G_i)
=\sum_Gp_\ell(G)f(G)
\quad\text{for every }f\in L^{\Phi_\beta}(p_\ell)\text{ simultaneously}.
\]
**Below the boundary:** for every \(0<\beta<1/3\), with probability one there is a (sample-dependent) **nonnegative** \(f\in L^{\Phi_\beta}(p_\ell)\) such that
\[
\sup_{n\ge1}\frac1n\sum_{i=1}^n f(G_i)=\infty,
\qquad \sum_Gp_\ell(G)f(G)<\infty.
\]
For each \(0<\beta<1\), the Orlicz space strictly contains \(\bigcup_{q>1}L^q(p_\ell)\). In particular the simultaneous strong law above \(1/3\) is strictly stronger than one obtained merely for all functions having some moment of order greater than one.

## Assumptions and scope
All groups are considered up to isomorphism; the trivial group is included. The prime \(\ell\) is fixed, and all random draws are *idealized independent samples* from the specified Cohen–Lenstra measure, not observed class groups of actual number fields. The statement is valid for real-valued or complex-valued functions. The assertion below the threshold is the negation of a **uniform, simultaneous** law: each individual integrable \(f\) still satisfies its usual scalar strong law almost surely. No claim is made at \(\beta=1/3\), nor about deterministic arithmetic sequences.

## Proof
**1. Exact criterion on any countable probability space.** Let \(X\) be countable, \(p_x>0\) with \(\sum_xp_x=1\), and \(\Phi\) a strictly increasing convex Young function with \(\Phi(t)\ge t\). Put \(B=L^\Phi(p)\) with the Luxemburg norm and \(w_x=\Phi^{-1}(1/p_x)\). For each \(f\in B\), the one-coordinate modular inequality gives
\[
|f(x)|\le w_x\|f\|_B.
\]
Every \(f\in B\) is integrable, since \(\Phi(t)\ge t\). Let \(\widehat p_n\) be the empirical measure of independent \(p\)-samples. If \(\sum_xp_xw_x<\infty\), ordinary scalar strong laws, first on every fixed coordinate and then on the integrable functions \(x\mapsto w_x\mathbf1_{x\notin F}\) for a nested exhaustion by finite sets \(F\), show
\[
\sum_xw_x|\widehat p_n(x)-p_x|\longrightarrow0\quad\text{almost surely}.
\]
Indeed, the finite-coordinate part tends to zero; the tail has limsup at most \(2\sum_{x\notin F}p_xw_x\), and this vanishes as \(F\) increases. Consequently
\[
\sup_{\|f\|_B\le1}\left|\sum_x(\widehat p_n(x)-p_x)f(x)\right|
\le \sum_xw_x|\widehat p_n(x)-p_x|\longrightarrow0.
\]
This is stronger than the asserted simultaneous pointwise convergence.

Conversely suppose \(\sum_xp_xw_x=\infty\). The independent random variables \(W_i=w_{X_i}\) have infinite mean. For each fixed positive integer \(M\), the tail-sum formula implies \(\sum_n\Pr(W_n>Mn)=\infty\). Independence and the second Borel–Cantelli lemma imply \(W_n>Mn\) infinitely often, simultaneously for all positive integers \(M\). Let \(T_n\in B^*\) be the positive empirical-average functional. Since the positive point-evaluation functional \(\delta_x:f\mapsto f(x)\) has exact dual norm \(\|\delta_x\|=w_x\) (attained by the one-coordinate indicator), positivity gives
\[
\|T_n\|_{B^*}\ge \frac{w_{X_n}}{n}.
\]
Thus \(\sup_n\|T_n\|=\infty\) almost surely. The uniform boundedness principle, applied pathwise to the Banach space \(B\), supplies \(f\in B\) with \(\sup_n|T_n(f)|=\infty\). Because each \(T_n\) is positive, replacing \(f\) by \(|f|\) yields a nonnegative function with \(\sup_n T_n(|f|)=\infty\). We have proved the exact criterion
\[
L^\Phi(p)\text{ is simultaneously strong-law admissible}
\iff \sum_xp_x\Phi^{-1}(1/p_x)<\infty.
\tag{1}
\]
No appeal to uncountably many separate almost-sure events occurs; both sides are decided by a common probability-one event.

**2. Inverting the particular Young function.** For fixed \(0<\beta<1\), integration over \([t/2,t]\) and monotonicity of the integrand give, as \(t\to\infty\),
\[
\log\Phi_\beta(t)=\log t+(\log t)^\beta+O(1).
\]
With \(t=\Phi_\beta^{-1}(y)\), it follows that \(\log t\sim\log y\) and hence
\[
\frac{\Phi_\beta^{-1}(y)}y
=\exp\bigl(-(1+o(1))(\log y)^\beta\bigr)\qquad(y\to\infty).
\tag{2}
\]
The little-oh depends on \(\beta\) but is uniform in the argument once that argument is sufficiently large.

**3. The automorphism-square statistic.** Write the isomorphism type as the partition \(\lambda\), with multiplicity \(m_i\) for cyclic factors of order \(\ell^i\). Let \(a_j=\sum_{i\ge j}m_i\) be the conjugate-column heights and set \(S(\lambda)=\sum_{j\ge1}a_j^2\). Counting endomorphisms and requiring invertibility on the diagonal multiplicity blocks over \(\mathbb F_\ell\) yields the classical exact formula
\[
|\operatorname{Aut}G_\lambda|
=\ell^{S(\lambda)}\prod_{i\ge1}\prod_{h=1}^{m_i}(1-\ell^{-h}).
\tag{3}
\]
Since \(\sum_i m_i=a_1\le\sqrt{S(\lambda)}\), each factor \((1-\ell^{-h})\) is at least \((1-\ell^{-1})\), and therefore
\[
S(\lambda)\log\ell+\sqrt{S(\lambda)}\log(1-\ell^{-1})
\le\log|\operatorname{Aut}G_\lambda|\le S(\lambda)\log\ell.
\tag{4}
\]
With \(c_\ell\) fixed, equations (2)–(4) imply positive constants \(b,B\) such that, for every type with sufficiently large \(S(\lambda)\),
\[
e^{-B S(\lambda)^\beta}\le
p_\ell(G_\lambda)\Phi_\beta^{-1}(1/p_\ell(G_\lambda))
\le e^{-b S(\lambda)^\beta}.
\tag{5}
\]

**4. The one-third threshold from partitions into squares.** In the multiset of conjugate-column heights \((a_j)_j\), denote by \(c_k\) the number of columns of height \(k\). The correspondence between partitions and these finite sequences \((c_k)_{k\ge1}\) is bijective and satisfies \(S(\lambda)=\sum_{k\ge1}k^2c_k\). Consequently
\[
\sum_\lambda e^{-tS(\lambda)}
=\prod_{k\ge1}(1-e^{-tk^2})^{-1},
\qquad
\log\sum_\lambda e^{-tS(\lambda)}
\le\frac{\sqrt\pi}{2}\zeta(3/2)t^{-1/2}.
\tag{6}
\]
The inequality follows from expanding the logarithm and bounding \(\sum_{k\ge1}e^{-tjk^2}\le\int_0^\infty e^{-tjx^2}\,dx\). If \(N(s)=\#\{\lambda:S(\lambda)\le s\}\), applying \(N(s)\le e^{ts}\sum_\lambda e^{-tS(\lambda)}\) with \(t\asymp s^{-2/3}\) yields
\[
N(s)\le \exp(C s^{1/3})\qquad(s\ge1)
\tag{7}
\]
for a constant \(C\). By (5) and (7), the series in (1) converges whenever \(\beta>1/3\).

For the reverse implication, for every integer \(m\ge1\) take all column multiplicity configurations with \(c_m=1\), with \(c_k\in\{0,1\}\) for \(1\le k<m\), and with \(c_k=0\) for \(k>m\). These are \(2^{m-1}\) distinct types, and different \(m\) produce disjoint sets. They all obey
\[
S(\lambda)\le\sum_{k=1}^m k^2\le m^3.
\]
The contribution of this disjoint family to (1) is at least \(2^{m-1}e^{-B m^{3\beta}}\) for all sufficiently large \(m\), by (5). If \(\beta<1/3\), these lower bounds do not even tend to zero. Hence (1) diverges, proving the negative half.

**5. Strict improvement over a positive-moment hypothesis.** Since \(\log\Phi_\beta(t)/\log t\to1\), for each \(q>1\) one has \(\Phi_\beta(t)\le C_q(1+t^q)\), so \(L^q(p_\ell)\subseteq L^{\Phi_\beta}(p_\ell)\). Let \(C_{\ell^n}\) be the cyclic group of order \(\ell^n\), and write \(L_n=\log(1/p_\ell(C_{\ell^n}))=n\log\ell+O_\ell(1)\). Define \(f(C_{\ell^n})=\exp(L_n-2L_n^\beta)\) for \(n\ge1\), and set \(f=0\) on all other types. By the defining integral of \(\Phi_\beta\),
\[
\sum_Gp_\ell(G)\Phi_\beta(|f(G)|)
\ll\sum_{n\ge1}e^{-c n^\beta}<\infty,
\]
so \(f\in L^{\Phi_\beta}\). But for every fixed \(q>1\), its \(q\)-th moment has terms of order \(\exp((q-1)L_n-2qL_n^\beta)\), which tend to infinity. Thus the same \(f\) belongs to none of the \(L^q\), proving strict containment.

## Verification
The supplied standalone script `VERIFY.py` checks equation (3) against exhaustive enumeration of all endomorphisms and automorphisms of the abelian groups of sufficiently small order for primes \(2\) and \(3\). It also checks the square-partition correspondence through weight \(23\) using two different enumerations. Run `python3 VERIFY.py` in a directory containing that file. The resulting record is `VERIFY_OK automorphism_formula_exact_cases=17 square_partition_weights=24 primes=2,3`. The general entropy bound, divergence construction and simultaneous almost-sure statement are proved above, not inferred from the finite script.

## Relationship to prior work
Bartel–Morgan (arXiv:2610.29880v1, 21 October 2026) introduced the present simultaneous or “promising” empirical-average test for Cohen–Lenstra distributions, proved the exact criterion \(\sum_xp(x)^{1-1/q}<\infty\) for the \(L^q\) classes (Theorem 1.2), and verified the needed power-mass bounds for finite abelian prime-power groups (Proposition 2.11). Their Corollary 1.3 covers \(\bigcup_{q>1}L^q\), but does not assert the Orlicz claims here. Bartel–Lenstra (2020, Section 7) established failure for the full integrable \(L^1\) class and formulated the motivating notion of reasonable functions. Mies (arXiv:2510.25408v1, 2025) studies sample estimation of an individual Orlicz norm; it does not assert simultaneous sample-average convergence for all functions in a Cohen–Lenstra Orlicz class. The present phase transition combines an exact Orlicz functional-analytic criterion with the \(S(\lambda)\)-weighted growth of finite abelian prime-power groups.

## Limitations
The exact endpoint \(\beta=1/3\) is deliberately left unresolved. The theorem is only about independent Cohen–Lenstra samples, not the class-group distribution of any concrete family of number fields. Although direct comparisons with accessible literature and searchable research records have found no equivalent phase boundary, independent priority assessment has not been performed, and unindexed empirical-process or partition-asymptotic results could contain equivalent formulations. Finite verification does not certify the infinite almost-sure claims.

## References
1. A. Bartel and A. Morgan, *On the notion of reasonable functions in Cohen–Lenstra type heuristics*, arXiv:2610.29880v1 (first public 2026-10-21), Theorem 1.2, Corollary 1.3, Proposition 2.11, https://arxiv.org/html/2610.29880v1.
2. A. Bartel and H. W. Lenstra Jr., *On class groups of random number fields*, Proceedings of the London Mathematical Society **121** (2020), 927–953, Section 7, DOI:10.1112/plms.12343.
3. F. Mies, *Empirical Orlicz norms*, arXiv:2510.25408v1 (2025), https://arxiv.org/html/2510.25408v1.
