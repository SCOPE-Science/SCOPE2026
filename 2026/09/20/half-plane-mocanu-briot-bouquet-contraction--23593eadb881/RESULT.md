# A half-plane Briot–Bouquet contraction for bounded Mocanu variation

## Statement

Let \(\mathbb D=\{z:|z|<1\}\), let \(h\) be univalent on \(\mathbb D\), normalized by \(h(0)=1\), and suppose that \(h(\mathbb D)\) is an open half-plane. For \(\mu\ge1\), write
\[
\mathcal K_\mu(h)
=\{\mu q_1+(1-\mu)q_2:q_1\prec h,\ q_2\prec h\}.
\]
Let \(\beta\ne0\) and \(\gamma\in\mathbb C\) satisfy
\[
\operatorname{Re}(\beta h(z)+\gamma)\ge0
\qquad(z\in\mathbb D).
\]
If \(q\) is analytic on \(\mathbb D\), \(q(0)=1\), and
\[
P(z):=q(z)+\frac{zq'(z)}{\beta q(z)+\gamma}
\]
is analytic and belongs to \(\mathcal K_\mu(h)\), then
\[
\boxed{q\in\mathcal K_\mu(h).}
\]

Thus the nonlinear \(\beta\ne0\) implication posed in Dziok's Problem 1 is valid for every half-plane target and every bounded-variation parameter \(\mu\ge1\). Dziok's 2013 paper left the nonlinear case open; Dziok–Noor restated a more general two-target version in 2017 and again described the \(\beta\ne0\) case as open.

The result follows from a stronger norm contraction.

## Boundary-winding contraction lemma

Let \(Q\) be analytic on \(\mathbb D\), \(Q(0)=1\). Let \(a\in\mathbb C\) satisfy \(\operatorname{Re}a\ge0\), let \(c>0\), and assume that \(Q+a\) has no zero in \(\mathbb D\). Define
\[
R(z)=Q(z)+\frac1c\frac{zQ'(z)}{Q(z)+a}.
\]
Then for every \(0<r<1\),
\[
\boxed{
\int_0^{2\pi}|\operatorname{Re}Q(re^{it})|\,dt
\le
\int_0^{2\pi}|\operatorname{Re}R(re^{it})|\,dt.}
\]

This is the analytic mechanism behind the half-plane case.

## Proof of the contraction lemma

Put
\[
W=Q+a,\qquad \alpha=\operatorname{Re}a\ge0.
\]
Fix \(0<r<1\), write
\[
W(re^{it})=X(t)+iY(t),
\]
and choose a continuous argument \(\theta(t)=\arg W(re^{it})\). Because \(W\) is zero-free in the disk, its winding number around zero on every circle \(|z|=r\) is zero, so \(\theta\) can be chosen periodic. Moreover,
\[
\theta'(t)=\operatorname{Re}\frac{zW'(z)}{W(z)},\qquad z=re^{it}.
\]
Since \(\operatorname{Re}Q=X-\alpha\),
\[
\operatorname{Re}R=(X-\alpha)+\frac1c\theta'.
\]
Hence
\[
\int|\operatorname{Re}R|
\ge
\int \operatorname{sgn}(X-\alpha)\operatorname{Re}R
=
\int|X-\alpha|+\frac1cJ,
\]
where
\[
J=\int_0^{2\pi}\operatorname{sgn}(X(t)-\alpha)\,d\theta(t).
\]
It remains to show \(J\ge0\).

If \(\alpha=0\), then \(\operatorname{sgn}X=\operatorname{sgn}(\cos\theta)\). The \(2\pi\)-periodic function \(\operatorname{sgn}(\cos s)\) has mean zero and therefore has a periodic Lipschitz primitive \(\Phi\). Thus, by the chain rule for Lipschitz functions,
\[
J=\int_0^{2\pi}\Phi'(\theta(t))\theta'(t)\,dt
=\Phi(\theta(2\pi))-\Phi(\theta(0))=0.
\]

Now suppose \(\alpha>0\). For \(0<\varepsilon<\alpha\), choose a smooth nondecreasing function \(s_\varepsilon\) approximating \(\operatorname{sgn}\), with \(s_\varepsilon'\ge0\) supported in \((-\varepsilon,\varepsilon)\). On the disk \(|z|\le r\), the one-form \(d\arg W\) is smooth because \(W\ne0\). Stokes' theorem gives
\[
\begin{aligned}
J_\varepsilon
&:=\int_{|z|=r}s_\varepsilon(X-\alpha)\,d\arg W\\
&=\iint_{|z|<r}s_\varepsilon'(X-\alpha)\,dX\wedge d\arg W.
\end{aligned}
\]
In target coordinates,
\[
d\arg W=\frac{X\,dY-Y\,dX}{X^2+Y^2},
\qquad
dX\wedge d\arg W
=\frac{X}{|W|^2}\,dX\wedge dY.
\]
Since \(W\) is analytic,
\[
dX\wedge dY=|W'(z)|^2\,dx\wedge dy.
\]
Therefore
\[
J_\varepsilon
=
\iint_{|z|<r}
 s_\varepsilon'(X-\alpha)
 \frac{X|W'(z)|^2}{|W(z)|^2}\,dA(z).
\]
On the support of \(s_\varepsilon'\),
\(X>\alpha-\varepsilon>0\), so every integrand is nonnegative and
\(J_\varepsilon\ge0\). Letting \(\varepsilon\downarrow0\) gives \(J\ge0\) by dominated convergence on the boundary. This proves the contraction lemma.

## Reduction of the half-plane problem

Choose an affine map
\[
L(w)=\frac{w-B}{A},\qquad A\ne0,
\]
which maps the half-plane \(h(\mathbb D)\) onto the right half-plane
\(\{\operatorname{Re}\zeta>0\}\) and satisfies \(L(1)=1\). Thus
\[
h(\mathbb D)=B+A\{\operatorname{Re}\zeta>0\}.
\]
Set
\[
Q=L(q).
\]
Because affine maps preserve the defining signed convex combination,
\[
q\in\mathcal K_\mu(h)
\quad\Longleftrightarrow\quad
Q\in\mathcal K_\mu(h_0),
\qquad h_0(z)=\frac{1+z}{1-z}.
\]
For \(k=4\mu-2\), the classical Paatero–Pinchuk criterion used in Dziok's Corollary 1 is
\[
Q\in\mathcal K_\mu(h_0)
\quad\Longleftrightarrow\quad
\int_0^{2\pi}|\operatorname{Re}Q(re^{it})|\,dt\le k\pi
\quad(0<r<1).
\]

Write
\[
c=\beta A,\qquad \delta=\beta B+\gamma.
\]
The assumption
\[
\operatorname{Re}\{\beta(B+A\zeta)+\gamma\}\ge0
\qquad(\operatorname{Re}\zeta>0)
\]
forces \(c\) to be real: otherwise varying \(\operatorname{Im}\zeta\) would make the real part arbitrarily negative. It also forces \(c>0\), since \(\beta A\ne0\) and letting \(\operatorname{Re}\zeta\to\infty\) excludes \(c<0\). Finally \(\operatorname{Re}\delta\ge0\). Hence
\[
a:=\frac\delta c
\qquad\text{satisfies}\qquad
\operatorname{Re}a\ge0.
\]

The denominator transforms as
\[
\beta q+\gamma=c(Q+a).
\]
Because \(P\) is analytic, \(Q+a\) has no zero in \(\mathbb D\): a zero away from the origin would create a nonremovable simple pole in \(zQ'/(Q+a)\), while at the origin \(Q(0)+a=1+a\ne0\). Moreover
\[
L(P)
=Q+\frac1c\frac{zQ'}{Q+a}.
\]
Applying the contraction lemma on each circle gives
\[
\int_0^{2\pi}|\operatorname{Re}Q(re^{it})|\,dt
\le
\int_0^{2\pi}|\operatorname{Re}L(P)(re^{it})|\,dt.
\]
Since \(P\in\mathcal K_\mu(h)\), the right side is at most \(k\pi\). Therefore the Paatero–Pinchuk criterion gives \(Q\in\mathcal K_\mu(h_0)\), hence \(q\in\mathcal K_\mu(h)\).

## Relation to the published open problem

Dziok's 2013 Problem 1 asks for the nonlinear implication above for a general convex univalent target \(h\). The same paper notes that the linear case is covered by an earlier theorem, while the nonlinear case was open. The 2014 erratum changes assumptions in Lemma 1 and Theorem 3 only; it does not alter Problem 1. Dziok and Noor's 2017 paper poses a more general two-target version and explicitly says that the \(\beta\ne0\) case remains open and “seems to be false.” The theorem here proves a broad affirmative branch: every half-plane target, with no restriction on \(\mu\ge1\) beyond the bounded-variation setup.

## Originality check

Searches covered the exact 2013 and 2017 problem statements, the nonlinear expression
\(q+zq'/(\beta q+\gamma)\), bounded Mocanu variation, bounded boundary rotation, Briot–Bouquet differential subordination, half-plane targets, and later papers citing the same line of work. The 2015 Dziok paper on multivalent Mocanu functions contains a standard one-target differential-subordination lemma but no located statement of this \(L^1\) contraction or the half-plane \(\mathcal K_\mu\) conclusion. The 2020 bounded-Mocanu generalization cites both the 2013 and 2017 papers but no located source resolves this branch. No prior theorem equivalent to the boundary-winding contraction above was found. Originality is therefore claimed only to the best of our knowledge.

## Limitations

- The theorem does not settle Dziok's problem for arbitrary convex target domains.
- It does not settle the two-distinct-target version \(\mathcal K_\mu(h_1,h_2)\) posed by Dziok–Noor in 2017.
- The proof uses the affine geometry of a half-plane essentially; the \(L^1\) characterization is not invariant under a general conformal map of a convex domain.
- No exhaustive classification of equality in the contraction lemma is given.
- Literature under substantially different boundary-rotation or Hardy-space terminology may contain equivalent prior coverage not located by the search.

## References

1. J. Dziok, *Classes of functions associated with bounded Mocanu variation*, Journal of Inequalities and Applications 2013, 349. https://doi.org/10.1186/1029-242X-2013-349
2. J. Dziok, *Erratum to: Classes of functions associated with bounded Mocanu variation*, Journal of Inequalities and Applications 2014, 197. https://doi.org/10.1186/1029-242X-2014-197
3. J. Dziok and K. I. Noor, *Classes of analytic functions related to a combination of two convex functions*, Journal of Mathematical Inequalities 11 (2017), 413–427. https://doi.org/10.7153/jmi-11-35
4. J. Dziok, *Generalizations of multivalent Mocanu functions*, Applied Mathematics and Computation 269 (2015), 965–971. https://doi.org/10.1016/j.amc.2015.08.035
5. R. Aghalary and J. Kazemzadeh, *Generalization of functions of bounded Mocanu variation with respect to 2k-symmetric conjugate points*, Hacettepe Journal of Mathematics and Statistics 49 (2020), 1206–1215. https://doi.org/10.15672/hujms.466909
