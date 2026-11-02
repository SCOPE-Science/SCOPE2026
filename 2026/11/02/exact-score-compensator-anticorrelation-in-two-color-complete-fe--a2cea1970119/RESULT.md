# Exact score–compensator anticorrelation in two-color complete-feedback card guessing

## Finding

Consider a uniformly shuffled deck containing exactly \(m\) red and \(m\) black cards, for each integer \(m\geq1\). Before each reveal, the player guesses the currently more numerous color, choosing by an independent fair coin on ties. Let \(T_m\) count correct guesses, \(S_m\) be the predictable sum of conditional probabilities of a correct guess, and \(M_m=T_m-S_m\) be the terminal martingale. Then

\[
\lim_{m\to\infty}\frac{\operatorname{Var}(S_m)}m
=2\log 2-\frac12-\frac\pi4>0,
\qquad
\lim_{m\to\infty}\frac{\operatorname{Cov}(S_m,M_m)}m
=\frac12-\log 2<0.
\]

Moreover, with \(H_j=\sum_{k=1}^j1/k\), the martingale variance has the **exact finite-deck** value

\[
\mathbb E[M_m^2]=\frac m2-\frac{m}{2(2m-1)}(H_{2m}-1).
\]

Consequently the Pearson correlation of the predictable score and its martingale residual tends to

\[
\frac{\frac12-\log2}{\sqrt{\frac12\big(2\log2-\frac12-\frac\pi4\big)}}
=-0.859935683747\ldots.
\]

The negative covariance is of the same linear order as both marginal variances; in particular the score fluctuations cannot be reconstructed by adding their separate variances.

## Assumptions and scope

Only uniformly randomized balanced two-color decks and the above complete-feedback greedy strategy are considered. Independent randomized tie guesses are included in the score's probability space. At every reveal \(k\), with \(2m-k+1\) cards remaining, \(\mathcal F_{k-1}\) contains the revealed cards and past tie randomization; \(p_k=\mathbb P(\text{guess at }k\text{ is correct}\mid\mathcal F_{k-1})\). Then \(S_m=\sum_{k=1}^{2m}p_k\), and \(M_m=\sum_{k=1}^{2m}(\mathbf1_{\text{correct at }k}-p_k)\) is a square-integrable martingale terminal value. All limits keep two card types fixed and send the common multiplicity to infinity. The cited source already identifies the weak Brownian-bridge limit of the compensator; the explicit second moment, variance and covariance are the additions assessed here.

## Proof

**1. Exact reverse-path identity.** Read the deck from its bottom, and write \(D_t\) for red count minus black count among its final \(t\) cards, \(1\leq t\leq2m\). This is a symmetric simple-walk bridge with exactly \(m\) increments of each sign. The optimal conditional success probability with \(t\) cards left is

\[
p_t=\frac12+\frac{|D_t|}{2t}.
\]

Hence the predictable sum obeys, pathwise,

\[
S_m=m+\frac12\sum_{t=1}^{2m}\frac{|D_t|}{t}.
\tag{1}
\]

Sampling without replacement gives \(\mathbb E D_t^2=t(2m-t)/(2m-1)\). Martingale orthogonality and \(p_t(1-p_t)=1/4-D_t^2/(4t^2)\) yield

\[
\mathbb E M_m^2
=\frac m2-\frac1{4(2m-1)}\sum_{t=1}^{2m}\frac{2m-t}{t}
=\frac m2-\frac{m}{2(2m-1)}(H_{2m}-1).
\tag{2}
\]

In particular \(\mathbb E M_m^2/m\to1/2\).

**2. Second-moment convergence.** The invariance principle for symmetric finite-population bridges gives \(D_{\lfloor2mu\rfloor}/\sqrt{2m}\Rightarrow B(u)\) in the continuous-path topology after linear interpolation, where \(B\) is a standard Brownian bridge. Thus (1), truncated to \(u\geq\varepsilon>0\), converges to the corresponding Riemann integral. This extends to \(\varepsilon=0\) in \(L^2\)-controlled approximation: hypergeometric sampling without replacement is sub-Gaussian, so for each fixed \(q\geq1\), \(\|D_t\|_q\leq C_q\sqrt t\). Minkowski's inequality gives

\[
\left\|\frac1{2\sqrt m}\sum_{t\leq2m\varepsilon}\frac{|D_t|}{t}\right\|_q
\leq\frac{C_q}{2\sqrt m}\sum_{t\leq2m\varepsilon}t^{-1/2}
\leq C_q'\sqrt\varepsilon+O_q(m^{-1/2}).
\]

The entire normalized expression has a uniformly bounded fourth moment (choose \(q=4\)). The truncated invariance principle, endpoint control and uniform integrability of squares establish convergence of the first two moments to those of

\[
A=\frac1{\sqrt2}\int_0^1\frac{|B(u)|}{u}\,du.
\tag{3}
\]

The first moment equals \(\mathbb EA=\sqrt\pi/2\), by \(\mathbb E|B(u)|=\sqrt{2u(1-u)/\pi}\) and a beta integral.

**3. Exact bridge second moment.** The standard Brownian bridge has the time-change representation \(B(u)\overset d=(1-u)W_{u/(1-u)}\), with \(W\) standard Brownian motion. Consequently, setting \(I=\sqrt2 A\),

\[
I\overset d=\int_0^\infty\frac{|W_x|}{x(1+x)^2}\,dx.
\]

For \(0<x\leq y\), the bivariate centered Gaussian absolute-moment identity gives

\[
\mathbb E[|W_xW_y|]=\frac2\pi\left[\sqrt{x(y-x)}+x\arcsin\sqrt{x/y}\right].
\]

Apply Tonelli and the change \(x=uy\). Writing

\[
J(u)=\int_0^\infty\frac{dy}{(1+y)^2(1+uy)^2},
\]

we obtain

\[
\mathbb E I^2=\frac4\pi\int_0^1
\left[\sqrt{\frac{1-u}{u}}+\arcsin\sqrt u\right]J(u)\,du.
\tag{4}
\]

Both terms can be evaluated exactly by interchanging the nonnegative integrals. The elementary trigonometric substitution \(u=\sin^2\theta\) gives

\[
\int_0^1\sqrt{\frac{1-u}{u}}\,J(u)\,du
=\frac\pi2\int_0^\infty(1+y)^{-5/2}\,dy=\frac\pi3.
\]

Integration by parts with the same substitution gives, for \(y>0\),

\[
\int_0^1\frac{\arcsin\sqrt u}{(1+yu)^2}\,du
=\frac\pi{2y}\left[(1+y)^{-1/2}-(1+y)^{-1}\right].
\]

Putting \(z=\sqrt{1+y}\) and then \(v=1/z\) gives

\[
\int_0^1\arcsin\sqrt u\,J(u)\,du
=\pi\int_0^1\frac{v^4}{1+v}\,dv
=\pi\left(\log2-\frac7{12}\right).
\]

It follows from (4) that \(\mathbb E I^2=4\log2-1\), and hence

\[
\mathbb E A^2=2\log2-\frac12,
\qquad
\operatorname{Var}(A)=2\log2-\frac12-\frac\pi4.
\tag{5}
\]

By Step 2, this is the limit of \(\operatorname{Var}(S_m)/m\).

**4. Joint covariance.** Kuba and Panholzer's established two-type score moment asymptotics give \(\mathbb E(T_m-m)/\sqrt m\to\sqrt\pi/2\) and \(\mathbb E(T_m-m)^2/m\to1\), so \(\operatorname{Var}(T_m)/m\to1-\pi/4\). Since \(T_m=S_m+M_m\), the exact identity

\[
2\operatorname{Cov}(S_m,M_m)
=\operatorname{Var}(T_m)-\operatorname{Var}(S_m)-\mathbb EM_m^2
\]

and (2),(5) yield \(\operatorname{Cov}(S_m,M_m)/m\to1/2-\log2\). Division by the two limiting marginal standard deviations gives the asserted correlation.

## Verification

The standalone script `verify_moments.py` enumerates every balanced deck for multiplicities \(1\leq m\leq8\) using exact rational arithmetic, averages independent tie coins analytically, and checks the exact martingale-variance formula and variance decomposition. It also compares independent numerical integrations of the two terms in (4) with the derived elementary values. Run with `python verify_moments.py`; its reproducible output is in `verification_output.txt`. Finite enumeration and numerical quadrature do not prove the asymptotic theorem; Steps 1–4 give the analytic proof.

## Relationship to prior work

Dey and Manthripragada (2026, arXiv:2610.17479v1) prove the general complete-feedback score limit framework, including the fixed-type weak Brownian-bridge compensator functional (their Proposition 1.4). Their stated fixed-type result identifies the law in functional form, not the evaluated second moment or the associated score–martingale covariance. Kuba and Panholzer (2023, arXiv:2303.04609v1, Theorem 9) determine all fixed-order asymptotic moments of the two-color optimal score, which are used here rather than claimed anew. The exact elementary evaluation (5), the finite-deck martingale variance (2), and the nonzero normalized anticovariance are the new asserted combination. The derivation uses the standard Gaussian absolute-moment identity; it does not claim that identity as new.

## Limitations

No assertion is made for unequal initial multiplicities, more than two colors, or nonlinear tie-breaking strategies. The first-public date and primary classification refer to the motivating 2026 probability preprint, not the older supporting paper. A broad Brownian-functional identity or a previously unnoticed appendix computation could cover the elementary constant; relevant literature and indexed mathematical records were searched, but absence from search results is not a novelty proof. The analysis is reviewed here but not independently validated.

## References

1. P. S. Dey and J. M. Manthripragada, *Limit Theorems for the Complete Feedback Card Guessing Game*, arXiv:2610.17479v1 (first posted 2026-10-12), https://arxiv.org/abs/2610.17479.
2. M. Kuba and A. Panholzer, *On Card Guessing with Two Types of Cards*, arXiv:2303.04609v1 (first posted 2023-03-08), https://arxiv.org/abs/2303.04609.
3. P. Diaconis and R. Graham, *The analysis of sequential experiments with feedback to subjects*, Annals of Statistics 9 (1981), 3–23; foundational greedy-feedback analysis, as cited in References 1–2.
