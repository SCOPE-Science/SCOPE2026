# Sharp degree-four Fourier cutoff for constant 3-order width
## Finding
Let \(K\subset\mathbb R^2\) be a planar convex body with support function \(p(\theta)\) that is a real trigonometric polynomial of degree at most \(4\). Define the 3-order width
\[
w_3(\theta)=p(\theta)+p\left(\theta+\frac{2\pi}{3}\right)+p\left(\theta+\frac{4\pi}{3}\right).
\]
If \(w_3(\theta)\equiv\Lambda>0\), then
\[
A(K)\ge \frac{77\pi}{1053}\Lambda^2.
\]
The constant is sharp. Equality holds exactly, up to translation and rotation, for the body whose centered support function is
\[
p_*(\theta)=\frac{\Lambda}{3}\left(1+\frac{4\sqrt{190}}{117}\cos(2\theta)-\frac{4}{117}\cos(4\theta)\right).
\]

## Assumptions and scope
The statement concerns ordinary Euclidean planar convex bodies. The only spectral assumption is that the support function has Fourier degree at most \(4\). Translation contributes only first harmonics and therefore does not affect the area or \(w_3\). The class includes weakly convex boundaries for which the radius-of-curvature density can vanish at isolated normal directions. If one requires strictly positive radius of curvature, the displayed constant remains the sharp infimum but the equality body lies on the boundary of that stricter class.

The result is a finite-Fourier-mode theorem. It does not solve the unrestricted least-area problem for all bodies of constant 3-order width.

## Proof
Write the support function, after removing its translation terms, as
\[
p(\theta)=r+\operatorname{Re}\left(c_2e^{2i\theta}+c_4e^{4i\theta}\right).
\]
The constant 3-order-width condition annihilates every Fourier mode whose index is not divisible by \(3\), while constancy removes the nonzero multiples of \(3\). In degree at most \(4\), this leaves only the constant term, translation modes, and the \(2\)- and \(4\)-modes. Summing three rotated copies gives \(\Lambda=3r\).

For a support function, the radius-of-curvature density is
\[
\rho(\theta)=p(\theta)+p''(\theta)
=r-3\operatorname{Re}(c_2e^{2i\theta})-15\operatorname{Re}(c_4e^{4i\theta}),
\]
and convexity is equivalent here to \(\rho\ge0\). Blaschke's support-function area identity gives
\[
A(K)=\frac12\int_0^{2\pi}\left(p^2-(p')^2\right)d\theta
=\pi r^2-\frac{\pi}{2}\left(3|c_2|^2+15|c_4|^2\right).
\]

Set \(\phi=2\theta\) and normalize by \(r\). Then every admissible curvature density has the form
\[
\frac{\rho}{r}=1+2\operatorname{Re}\left(d_1e^{i\phi}+d_2e^{2i\phi}\right)\ge0.
\]
For completeness, the degree-two Fejer--Riesz factorization follows directly by multiplying this Laurent polynomial by \(z^2\): off-circle roots occur in reciprocal-conjugate pairs and unit-circle roots have even multiplicity, so one root from each pair can be selected to obtain
\[
1+2\operatorname{Re}\left(d_1e^{i\phi}+d_2e^{2i\phi}\right)
=|a+be^{i\phi}+ce^{2i\phi}|^2,
\]
with
\[
|a|^2+|b|^2+|c|^2=1,\qquad d_1=\overline a b+\overline b c,\qquad d_2=\overline a c.
\]
The area deficit is therefore governed by
\[
J=4\left(\frac{|d_1|^2}3+\frac{|d_2|^2}15\right),\qquad
A(K)=\pi r^2-\frac{\pi r^2}2J.
\]
Put \(x=|a|\), \(y=|b|\), and \(z=|c|\). The triangle inequality gives
\[
|d_1|\le y(x+z),\qquad |d_2|=xz,
\]
so
\[
J\le4\left(\frac{y^2(x+z)^2}3+\frac{x^2z^2}15\right).
\]
For fixed \(s=x^2+z^2\), write \(q=xz\). Since \(y^2=1-s\), the expression inside the outer factor \(4\) is
\[
\frac{(1-s)(s+2q)}3+\frac{q^2}15,
\]
which is increasing in \(q\ge0\). Hence its maximum at fixed \(s\) occurs when \(x=z\). Put \(x=z=\sqrt u\), so \(y^2=1-2u\) and \(0\le u\le1/2\). Then
\[
J\le\frac{80u-156u^2}15
=\frac{80}117-\frac{52}5\left(u-\frac{10}39\right)^2.
\]
Thus \(J\le80/117\), with equality exactly when \(u=10/39\), the two terms in \(d_1\) have the same phase, and the preceding fixed-sum inequalities are equalities. Consequently
\[
A(K)\ge\pi r^2\left(1-\frac12\frac{80}117\right)
=\frac{77\pi}117r^2
=\frac{77\pi}1053\Lambda^2.
\]

The equality phases satisfy the relation that allows a rotation to make the two relevant curvature harmonics real with compatible phase. After a further quarter-turn if necessary, the centered support is exactly \(p_*\) above. Its curvature density factors as
\[
p_*+p_*''
=\frac{\Lambda}3\left(1-\frac{4\sqrt{190}}39\cos(2\theta)+\frac{20}39\cos(4\theta)\right)
=\frac{40\Lambda}117\left(\cos(2\theta)-\frac{\sqrt{190}}20\right)^2,
\]
so it is a valid convex support function and attains equality.

## Verification
The bundled checker `verify.py` verifies the exact rational maximizer \(u=10/39\), the value \(J=80/117\), the area factor \(77/117\), the support/curvature coefficient relations, and numerically samples the root-of-unity cancellation and nonnegativity factorization. These computations are diagnostics; the proof above is exact and does not infer a global theorem from sampling.

## Relationship to prior work
Ou and Pan introduced \(w_k\), proved the support-Fourier characterization of constant \(k\)-order width, and explicitly asked which such convex curve has least area. Their support formula and area identity are exactly the starting point for the finite-mode reduction used here. Zhang and Yang later developed the radial dual of the Chernoff--Ou--Pan framework and obtained area bounds for constant radial \(k\)-order width; this is a different radial problem. Zhang's later constant-\(k\)-order-width paper is described as giving characterizations of that class rather than solving the least-area problem. Kwong's higher-order Chernoff theory gives stronger families of upper-type isoperimetric inequalities involving generalized width and curvature-center loci, not this sharp lower-area solution in the degree-four support class. A 2023 paper gives further Chernoff and reverse-Chernoff inequalities and stability results; no inspected statement yields the exact degree-four minimum or the extremizer above.

## Limitations
The unrestricted Ou--Pan least-area question remains outside this result. The equality body's curvature density vanishes at finitely many normal directions, so the equality case is not in the subclass with everywhere positive radius of curvature. A later or unindexed source could contain an equivalent finite-harmonic optimization; targeted searches and the inspected literature did not find one, but this is a residual originality risk.

## References
1. D. Zhang and Y. Yang, *The dual generalized Chernoff inequality for star-shaped curves*, Turkish Journal of Mathematics 40 (2016), 272--282, DOI 10.3906/mat-1504-12. The public article records accepted/published-online date 2015-06-19.
2. K. Ou and S. Pan, *Some remarks about closed convex curves*, Pacific Journal of Mathematics 248 (2010), 393--401, DOI 10.2140/pjm.2010.248.393.
3. D. Zhang, *A generalization of domains of constant width*, Beiträge zur Algebra und Geometrie 57 (2016), 259--270, DOI 10.1007/s13366-015-0252-8.
4. K.-K. Kwong, *A unified approach to higher order discrete and smooth isoperimetric inequalities*, arXiv:2111.13352v1.
5. J. Fang and Y. Yang, *Chernoff Type Inequalities Involving k-Order Width and Their Stability Properties*, Results in Mathematics 78 (2023), 101, DOI 10.1007/s00025-023-01889-4.
