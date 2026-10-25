# Tilted-matching law and Gaussian section fluctuations of chainlink polytopes

## Finding

For an integer \(s\geq3\), real \(a_1,\ldots,a_s>0\), and \(0<\ell\leq\frac12\min_i a_i\), consider the full-dimensional chainlink polytope
\[
K(\mathbf a,\ell)=\{x\in\mathbb R^s:0\leq x_i\leq a_i,\;x_i-x_{i+1}\leq a_i-\ell\ (1\leq i\leq s)\},
\]
where indices are cyclic. Define its exponentially tilted volume by
\[
Z_{\mathbf a,\ell}(t)=\int_{K(\mathbf a,\ell)}\exp\!\left(t\sum_{i=1}^s x_i\right)\,dx,
\qquad t\in\mathbb R.
\]
Put \(M_i(t)=\int_0^{a_i}e^{tx}\,dx\) and
\[
B_i(t)=\frac{\ell^2}{2}e^{a_it}
\left(\frac{\sinh(\ell t/2)}{\ell t/2}\right)^2,
\]
with continuous values at \(t=0\). **The exact weighted cyclic-matching identity** is
\[
\boxed{Z_{\mathbf a,\ell}(t)=\operatorname{tr}\prod_{i=1}^s
\begin{pmatrix}M_i(t)&-B_i(t)\\1&0\end{pmatrix}.}
\tag{1}
\]
In particular, this gives the bilateral Laplace transform of the Euclidean hyperplane-section volume profile at every real tilt, not only its total volume.

For the *homogeneous* family \(K_s(r)=K((1,\ldots,1),r)\), with fixed \(0<r\leq1/2\), let \(X^{(s)}\) be uniformly distributed in \(K_s(r)\), and let \(S_s=\sum_{i=1}^s X_i^{(s)}\). Define
\[
m(t)=\begin{cases}(e^t-1)/t,&t\ne0,\\1,&t=0,\end{cases}
\qquad
u_r(t)=\frac12\left(\frac{\sinh(rt/2)}{\sinh(t/2)}\right)^2,
\]
where \(u_r(0)=r^2/2\), and put
\[
\lambda_\pm(u)=\frac{1\pm\sqrt{1-4u}}2,
\quad \delta_r=\sqrt{1-2r^2},
\quad \beta_\pm=\frac{1\pm\delta_r}{2}.
\]
The exact finite-dimensional moment-generating function is
\[
\boxed{\mathbb E e^{tS_s}=m(t)^s
\frac{\lambda_+(u_r(t))^s+\lambda_-(u_r(t))^s}
{\beta_+^s+\beta_-^s}.}
\tag{2}
\]
Furthermore, \(\mathbb E S_s=s/2\) exactly, and
\[
\boxed{\operatorname{Var}(S_s)=\frac{s}{12}+
\frac{s r^2(1-r^2)}{12\delta_r}
\frac{\beta_+^{s-1}-\beta_-^{s-1}}{\beta_+^s+\beta_-^s}.}
\tag{3}
\]
Consequently, with
\[
\sigma_r^2=\frac1{12}+
\frac{r^2(1-r^2)}{12\delta_r\beta_+}>\frac1{12},
\]
one has the **strictly enhanced section-mass fluctuations**
\[
\boxed{\frac{S_s-s/2}{\sqrt{s}}\ \Longrightarrow\ N(0,\sigma_r^2),
\qquad \frac{\operatorname{Var}(S_s)}s\longrightarrow\sigma_r^2.}
\tag{4}
\]
The variance baseline \(1/12\) is that of a uniformly sampled cube coordinate; imposing the nonzero cyclic link changes the macroscopic variance at leading order rather than merely in a lower-order term.

There is also a full large-deviation principle for \(S_s/s\), at speed \(s\), with good rate function
\[
\boxed{I_r(z)=\sup_{t\in\mathbb R}\{tz-\Lambda_r(t)\},\qquad
\Lambda_r(t)=\log m(t)+\log\frac{\lambda_+(u_r(t))}{\beta_+}.}
\tag{5}
\]
The rate is finite for \(z\in(0,1)\) and infinite outside the open unit interval.

## Assumptions and scope

Equation (1) holds for arbitrary positive real side lengths under \(s\geq3\) and \(2\ell\leq\min_i a_i\). Equations (2)--(5) concern only the homogeneous unit-side family with one fixed \(r\in(0,1/2]\) as \(s\to\infty\). The probability measure is normalized \(s\)-dimensional Euclidean volume, not counting measure on lattice points. The centered normal distribution in (4) is a weak limit; it is not a local central limit theorem.

If \(A_s(z)\) denotes the intrinsic \((s-1)\)-dimensional volume of the section of \(K_s(r)\) by \(\sum x_i=z\), the coarea formula gives the exact density of \(S_s\):
\[
 f_{S_s}(z)=\frac{A_s(z)}{\sqrt{s}\,\operatorname{Vol}_s(K_s(r))}.
\]
Thus the result describes fluctuations of the distribution of the same parallel sections that motivate the chainlink construction.

## Proof

**1. Weighted forbidden-region decomposition.** Let \(C=\prod_i[0,a_i]\). The only points removed from \(C\) are the events \(E_i=\{x\in C:x_i-x_{i+1}>a_i-\ell\}\). On \(E_i\), necessarily \(x_i>a_i-\ell\) and \(x_{i+1}<\ell\). If both \(E_i\) and \(E_{i+1}\) held, the same coordinate would satisfy \(x_{i+1}<\ell\) and \(x_{i+1}>a_{i+1}-\ell\geq\ell\), a contradiction. Consequently, a nonempty intersection of forbidden events is indexed by a matching of the cyclic graph on \(s\) vertices. Events in a matching involve disjoint pairs of coordinates, so the exponential product weight factors over occupied edges and unoccupied coordinates. The free-coordinate integral is \(M_i(t)\). For the edge from \(i\) to \(i+1\), substituting \(x_i=a_i-\ell+v\), \(0<v<\ell\), and \(0<x_{i+1}<v\), gives
\[
 \int_{E_i}\!e^{t(x_i+x_{i+1})}\,dx_i\,dx_{i+1}
 =e^{t(a_i-\ell)}\int_0^\ell e^{tv}\int_0^v e^{ty}\,dy\,dv
 =B_i(t).
\]
Inclusion--exclusion therefore produces the signed sum over cyclic matchings, assigning a factor \(-B_i(t)\) to each matched edge and \(M_j(t)\) to each unmatched vertex. Expanding the trace of the product of the displayed two-state matrices enumerates exactly those cyclic matchings: a transition between the two states occupies an edge and its next vertex, while a state-preserving transition contributes one free vertex. This establishes (1) for all real \(t\), including zero by continuity.

**2. Homogeneous diagonalization.** For equal side lengths one, the two-state matrix is constant. Its eigenvalues are \(m(t)\lambda_\pm(B(t)/m(t)^2)\). The hyperbolic-sine expressions for \(B(t)\) and \(m(t)\) simplify their ratio to \(u_r(t)\). Since \(0\leq u_r(t)\leq r^2/2\leq1/8\) on the real line, both eigenvalues are real and \(\lambda_+>\lambda_-\geq0\). Dividing the trace at tilt \(t\) by its value at zero proves (2).

**3. Mean, exact variance, and Gaussian limit.** The identity \(m(-t)=e^{-t}m(t)\) and evenness of \(u_r(t)\) imply \(\mathbb E e^{tS_s}=e^{st}\mathbb E e^{-tS_s}\). Hence \(\mathbb E S_s=s/2\). With \(\delta_r=\sqrt{1-2r^2}\), Taylor expansion at zero gives
\[
 \log m(t)=\frac t2+\frac{t^2}{24}+O(t^4),
 \qquad u_r(t)=\frac{r^2}{2}+\frac{r^2(r^2-1)}{24}t^2+O(t^4).
\]
Differentiating the logarithm of (2) twice and using \(d\lambda_\pm/du=\mp(1-4u)^{-1/2}\) yields (3). In particular, its extra term is positive for every \(s\geq3\). Since \(\beta_-/\beta_+<1\), dividing (3) by \(s\) yields \(\sigma_r^2\).

For fixed real \(h\), substitute \(t=h/\sqrt s\) into the centered logarithmic generating function. The eigenvalue ratio term is exponentially small uniformly near zero, and the remaining analytic Taylor expansion gives
\[
 \log\mathbb E\exp\!\left(h\frac{S_s-s/2}{\sqrt s}\right)
 \longrightarrow\frac{\sigma_r^2h^2}{2}.
\]
Convergence of moment-generating functions near the origin proves (4).

**4. Large deviations.** At every fixed real \(t\), taking the logarithm of (2) and dividing by \(s\) gives \(\Lambda_r(t)\). The term from the smaller eigenvalue vanishes uniformly exponentially, because its ratio to the larger is at most \(\beta_-/\beta_+<1\). The limiting logarithmic generating function is finite and real analytic on all of \(\mathbb R\). As \(t\to-\infty\), respectively \(+\infty\), its derivative tends to zero, respectively one, because \(u_r(t)\to0\) and \(\log m(t)\) has those slopes. Convexity follows from the finite-dimensional log-moment-generating functions; analyticity and \(\Lambda_r''(0)=\sigma_r^2>0\) force strict convexity. Consequently, every point in \((0,1)\) is exposed by some finite tilt, while the Legendre transform is infinite at the endpoints as well as outside \([0,1]\). The Gärtner--Ellis theorem gives the lower bound on open sets; the compact support \([0,1]\) gives exponential tightness and the matching upper bound for closed sets. This proves (5).

## Verification

Run `python checker.py` with Python 3. The standalone checker uses no nonstandard dependencies. It compares the two-state matrix trace against independent matching enumeration for 63 nonzero- and zero-tilt cases, against direct three-dimensional integration with explicit constraint inequalities for nine additional cases, against analytically differentiated finite-dimensional variances in 12 cases, and against the limiting variance expression in three cases. The recorded run completed all 87 comparisons and printed `CHECK_OK 87 direct algebra/numerical comparisons`. The finite calculations test implementation and boundary handling; they are not substitutes for the analytical derivation of (1)--(5).

## Relationship to prior work

Kantarcı Oğuz, Özel, and Ravichandran introduced chainlink polytopes and proved the **untilted** volume trace formula in Proposition 6.8 of their 2022 preprint. They also established Ehrhart-equivalence of complementary sections and studied symmetry and unimodality phenomena. Formula (1) uses their matching-decomposition insight, with full acknowledgment: neither the construction nor its unweighted volume trace is claimed as new. The candidate contribution is a tilted trace governing the complete continuous section-mass distribution and its exact variance, Gaussian limit, and large-deviation principle. Earlier work by Kantarcı Oğuz and Ravichandran concerns rank polynomials of circular fence posets; those combinatorial rank counts do not themselves provide the continuous-volume fluctuation law proved here.

## Limitations

The link bound \(2\ell\leq\min_i a_i\) is essential to the nonintersection of neighboring forbidden events. The homogeneous limit requires fixed \(r>0\) as dimension grows; neither a dimension-dependent vanishing link nor arbitrary inhomogeneous central limit behavior is established. The large-deviation principle does not determine local section-density asymptotics or Berry--Esseen rates. Prior published matching expansions make the proof method natural, and equivalent statements in weighted transfer-matrix or continuous hard-core models remain a bibliographic risk. The conclusions have not undergone independent mathematical validation.

## References

1. E. Kantarcı Oğuz, C. Y. Özel, and M. Ravichandran, *Chainlink Polytopes and Ehrhart-Equivalence*, arXiv:2211.08382, first submitted November 15, 2022, especially Proposition 6.8 and Section 4; https://arxiv.org/abs/2211.08382.
2. E. Kantarcı Oğuz and M. Ravichandran, *Rank Polynomials of Fence Posets Are Unimodal*, arXiv:2112.00518, first submitted December 1, 2021; https://arxiv.org/abs/2112.00518.
3. A. Dembo and O. Zeitouni, *Large Deviations Techniques and Applications*, for the standard Gärtner--Ellis theorem (only the classical theorem is invoked).
