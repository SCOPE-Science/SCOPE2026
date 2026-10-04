# Exact third-order union formula at the first multiple-overlap threshold for simplex-centred spherical caps
## Finding
Let \(n\ge4\). Choose vertices \(v_1,\ldots,v_{n+1}\in S^{n-1}\) of a regular simplex with
\[
\langle v_i,v_j\rangle=-\frac1n\qquad(i\ne j).
\]
For \(\theta\in(0,\pi/2]\), write \(C[v,\theta]=\{x\in S^{n-1}:\langle x,v\rangle\ge\cos\theta\}\), and let \(\sigma\) be normalized spherical measure. Define
\[
\beta_n=\frac12\arccos\!\left(-\frac1n\right),\qquad
\theta_{3,n}=\arccos\sqrt{\frac{n-2}{3n}},\qquad
\theta_{4,n}=\arccos\sqrt{\frac{n-3}{4n}}.
\]
Let \(A_n(\theta)\) and \(A_n(\theta,\beta_n)\) be the one-cap and equal two-cap intersection measures from Section 2.3 of Arman--Kaire--Prymak. For every \(\theta_{3,n}\le\theta\le\theta_{4,n}\),
\[
\sigma\!\left(\bigcup_{i=1}^{n+1}C[v_i,\theta]\right)
=(n+1)A_n(\theta)-\binom{n+1}{2}A_n(\theta,\beta_n)+\binom{n+1}{3}T_n(\theta),
\]
where \(T_n(\theta)\) is the common measure of an intersection of three caps.

Writing \(c=\cos\theta\), put
\[
\delta_n=\left(\frac{n+1}{n}\right)^2\frac{n-2}{n},
\]
\[
q_n(t_1,t_2,t_3)=\frac n{n+1}\sum_{i=1}^3t_i^2+\frac n{(n+1)(n-2)}\left(\sum_{i=1}^3t_i\right)^2,
\]
and
\[
D_n(c)=\{t\in\mathbb R^3:t_i\ge c\text{ for }i=1,2,3,\ q_n(t)<1\}.
\]
Then
\[
T_n(\theta)=\frac{\Gamma(n/2)}{\pi^{3/2}\Gamma((n-3)/2)\sqrt{\delta_n}}\int_{D_n(c)}(1-q_n(t))^{(n-5)/2}\,dt.
\]

For \(n\ge5\), put \(c_{3,n}=\sqrt{(n-2)/(3n)}\), \(p_n=(n+1)/2\), and
\[
K_n=\frac{\Gamma(n/2)\,3^{(n+1)/2}}{\pi^{3/2}\Gamma((n+3)/2)\sqrt{\delta_n}}\left(2\sqrt{\frac n{3(n-2)}}\right)^{(n-5)/2}.
\]
Then
\[
T_n(\theta)\sim K_n\bigl(c_{3,n}-\cos\theta\bigr)^{p_n}\qquad(\theta\downarrow\theta_{3,n}).
\]
Hence, if \(B_n^\triangle\) is the pairwise Bonferroni expression in the source,
\[
\sigma(C[S_n,\theta])-B_n^\triangle(\theta)\sim\binom{n+1}{3}K_n\sin(\theta_{3,n})^{p_n}(\theta-\theta_{3,n})^{p_n}.
\]

## Assumptions and scope
The exact union formula is for equal caps centred at the vertices of one regular simplex and only through the first interval in which triple overlaps occur while positive-measure quadruple overlaps do not. The exact integral is valid for \(n\ge4\). The onset asymptotic is asserted only for \(n\ge5\); the borderline \(n=4\) density has an integrable boundary singularity and is deliberately excluded from that asymptotic statement. No finite computation is used to infer the theorem.

## Proof
For any \(k\) chosen simplex vertices put \(s_k=\sum_{i=1}^k v_i\). The Gram relations give
\[
\|s_k\|^2=\frac{k(n-k+1)}n,\qquad \langle s_k,v_i\rangle=\frac{n-k+1}{n}.
\]
If \(x\in S^{n-1}\) lies in all \(k\) caps and \(c=\cos\theta\ge0\), then
\[
kc\le\langle x,s_k\rangle\le\|s_k\|,
\]
so \(c\le\sqrt{(n-k+1)/(kn)}\). Equality is attained by \(x=s_k/\|s_k\|\), and equality in both inequalities forces this point uniquely. Thus triple intersections first appear at \(\theta_{3,n}\), while positive-measure quadruple intersections do not appear before \(\theta_{4,n}\). Inclusion--exclusion therefore terminates after the triple term throughout the asserted interval; all pair intersections are congruent and all triple intersections are congruent.

Fix three vertices and let \(W=\operatorname{span}\{v_1,v_2,v_3\}\). For uniformly distributed \(x\in S^{n-1}\), the orthogonal projection \(z=P_Wx\) has density
\[
\frac{\Gamma(n/2)}{\pi^{3/2}\Gamma((n-3)/2)}(1-\|z\|^2)^{(n-5)/2}
\]
on the unit ball of \(W\). Put \(t_i=\langle z,v_i\rangle\). The Gram matrix is
\[
G=\frac{n+1}{n}I-\frac1nJ,
\]
with
\[
\det G=\delta_n,\qquad G^{-1}=\frac n{n+1}I+\frac n{(n+1)(n-2)}J.
\]
Hence \(\|z\|^2=t^{\mathsf T}G^{-1}t=q_n(t)\), and the map \(z\mapsto t\) has Jacobian \(\sqrt{\det G}\). The cap inequalities are exactly \(t_i\ge c\). Substitution proves the integral for \(T_n\).

For the onset law let \(d=c_{3,n}-\cos\theta\) and set
\[
t=c_{3,n}\mathbf1+d(y-\mathbf1).
\]
Because \(G^{-1}\mathbf1=(n/(n-2))\mathbf1\), one obtains exactly
\[
1-q_n(t)=2\sqrt{\frac n{3(n-2)}}\,d\left(3-\sum_{i=1}^3y_i\right)-d^2q_n(y-\mathbf1).
\]
The scaled domain converges to \(\Delta_3=\{y_i\ge0,\ \sum_i y_i<3\}\). For \(n\ge5\), the exponent \((n-5)/2\) is nonnegative, so dominated convergence applies directly. The remaining beta integral is
\[
\int_{\Delta_3}\left(3-\sum_i y_i\right)^{(n-5)/2}dy=3^{(n+1)/2}\frac{\Gamma((n-3)/2)}{\Gamma((n+3)/2)}.
\]
After cancellation this is exactly \(K_n\), with total power \(3+(n-5)/2=(n+1)/2\). Finally \(c_{3,n}-\cos\theta\sim\sin(\theta_{3,n})(\theta-\theta_{3,n})\), proving the angular deficit law.

## Verification
The proof uses exact regular-simplex Gram identities, the standard projection density of normalized spherical measure, finite inclusion--exclusion, and a beta integral. The accompanying `verify.py` checks the Gram inverse, determinant, triple and quadruple onset identities, exponent arithmetic, and beta-factor identity for dimensions \(4\) through \(40\). Those checks are supplementary; the theorem is analytic.

As a normalization cross-check, the same projection-density method in the two-vertex case reproduces the onset exponent obtained by expanding the two-cap integral of Arman--Kaire--Prymak. No numerical sampling is used as a proof step.

## Relationship to prior work
Arman--Kaire--Prymak derive an exact integral for two equal spherical caps and use second-order Bonferroni for caps centred at a regular simplex. They explicitly note that their pairwise expression is exact through \(\theta_{3,n}\) and then retain it only as a lower bound. The finding above supplies the missing triple-intersection term, making the union formula exact through the entire next regime up to \(\theta_{4,n}\), and gives the sharp first asymptotic of the lost mass.

Ben-David--Eiron--Simon computed the distance from the origin to centres of regular-simplex subsimplices, giving the same square-root radii that underlie these overlap thresholds. No novelty is claimed for the numerical threshold values themselves. Their result does not provide the triple-intersection measure, the exact next-regime union formula, or the onset coefficient.

## Limitations
The result does not optimize the illumination bounds of Arman--Kaire--Prymak and does not claim that inserting the triple term changes any published integer illumination number. Higher overlap regimes require four-fold and subsequent terms. The \(n=4\) triple integral is exact, but the onset asymptotic is not claimed there.

## References
1. A. Arman, J. S. Kaire, A. Prymak, “Hadwiger's conjecture for cap bodies,” arXiv:2510.25968. First public version: 29 October 2025. Sections 2.3--2.4.
2. S. Ben-David, N. Eiron, H. U. Simon, “The Computational Complexity of Densest Region Detection,” COLT 2000, Lemma 5.4.
