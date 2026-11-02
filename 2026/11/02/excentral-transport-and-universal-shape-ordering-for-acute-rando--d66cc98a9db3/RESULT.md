# Excentral transport and universal shape ordering for acute random cyclic triangles

## Finding

Let three points be sampled independently from uniform arclength on a Euclidean circle, and let \(\Theta=(\Theta_1,\Theta_2,\Theta_3)\) be the angles of their nondegenerate inscribed triangle in a fixed labeled order. Write \(X=\Theta/\pi\) and let \(\mathcal A\) denote the event that the triangle is acute. Then \(X\) is uniform on the open angle simplex
\[
\Delta=\{x\in(0,1)^3:x_1+x_2+x_3=1\},
\]
and the **complete conditional angle law** has the exact affine transport representation
\[
\boxed{\quad X\mid\mathcal A\ \stackrel{\mathrm d}=\ T(X),
\qquad (T(x))_i=\frac{1-x_i}{2}=\frac{x_j+x_k}{2}\quad
(\{i,j,k\}=\{1,2,3\}).\quad}
\]
The coupling is deterministic, not merely an equality of selected moments. Its image is the entire acute-angle simplex, and \(\mathbb P(\mathcal A)=1/4\).

The matrix of \(T\) has zeros on the diagonal and \(1/2\) off the diagonal. It is doubly stochastic. Consequently, \(T(x)\) is majorized by \(x\) for every \(x\in\Delta\), with equality up to permutation only for the equilateral angle vector \((1/3,1/3,1/3)\). **Simultaneously for every Borel, symmetric Schur-concave angle-shape functional** \(\Phi\),
\[
\Phi(T(X))\ge \Phi(X)\quad\text{almost surely},
\]
so the conditional score \(\Phi(X)\mid\mathcal A\) first-order stochastically dominates the unconditional score. The coupling inequality is strict almost surely for each strictly Schur-concave \(\Phi\).

Geometrically, \(T\) takes a triangle's three angles to the angles of its **excentral triangle** (the triangle joining its three excenters). Therefore the excentral shape of an unconditioned random inscribed triangle, normalized to the original circumradius, has exactly the same distribution of angles as the original random inscribed triangle conditioned to be acute.

In particular, compare triangles with the **same circumradius one**. The area, perimeter, and inradius each strictly increase almost surely under this joint coupling; hence their three acute-conditional distributions each stochastically dominate their unconditional distributions. If \(P\) is the unit-circumradius perimeter,
\[
\boxed{\ \mathbb E[P]=\frac{12}{\pi},\qquad
\mathbb E[P\mid\mathcal A]=\frac{48}{\pi^2},\qquad
\frac{\mathbb E[P\mid\mathcal A]}{\mathbb E[P]}=\frac4\pi.\ }
\]
Further, for the intrinsic normalized angular imbalance
\[
V(x)=\sum_{i=1}^3\left(x_i-\frac13\right)^2,
\]
there is an **exact full-law contraction**, not just a moment comparison:
\[
\boxed{\ V(X)\mid\mathcal A\ \stackrel{\mathrm d}=\ \frac14 V(X).\ }
\]
In particular, \(\mathbb E[V(X)]=1/6\) and \(\mathbb E[V(X)\mid\mathcal A]=1/24\).

## Assumptions and scope

The sample consists of exactly three independent arclength-uniform points on one circle. The circle's radius does not affect the angle law. Its chord triangle is nondegenerate with probability one. A triangle is *acute* when each of its three interior angles is strictly less than \(\pi/2\). Equality configurations have probability zero.

All shape comparisons use a common prescribed circumradius of one; without normalization, the ordinary excentral triangle has a different size and its raw perimeter or area is not the functional claimed here. The stochastic assertions concern the **distribution of shape or shape-derived functionals**; no equality is asserted between the distributions of the original spatial vertex triples, orientations, or positions. A symmetric \(\Phi\) is Schur-concave if \(u\prec v\) entails \(\Phi(u)\ge\Phi(v)\). For expectation comparisons, the expectations must exist; stochastic order itself requires only a Borel score.

## Proof

**1. Uniform angle simplex, with an explicit anchor.** Designate one of the three sampled points as an anchor \(P_0\), then rotate the circle so that \(P_0\) is at argument zero. The other two arguments remain independent uniform variables on \([0,2\pi)\). Let their increasing order statistics be \(0<U_{(1)}<U_{(2)}<2\pi\). The normalized clockwise gaps from the designated anchor are
\[
Z_1=\frac{U_{(1)}}{2\pi},\quad
Z_2=\frac{U_{(2)}-U_{(1)}}{2\pi},\quad
Z_3=1-\frac{U_{(2)}}{2\pi}.
\]
The ordered-pair density of \((U_{(1)},U_{(2)})\) is constant on its defining triangle. The displayed affine change of variables therefore gives density \(2\) to \((Z_1,Z_2)\) on \(\{z_1,z_2>0,z_1+z_2<1\}\), i.e. \(Z\sim\operatorname{Dirichlet}(1,1,1)\). By the inscribed-angle theorem the three interior angles, divided by \(\pi\), are \(Z_1,Z_2,Z_3\) in a fixed permuted order. Thus \(X\) is uniform on \(\Delta\). The *designated anchor* is essential: using the smallest absolute polar argument as the anchor would instead size-bias one gap and is not this argument.

**2. Exact conditional push-forward.** Acuteness is equivalent to \(X_i<1/2\) for each \(i\). Hence the acute region is
\[
D=\{x\in\Delta:x_i<1/2\text{ for }i=1,2,3\}.
\]
The affine mapping \(T\) sends the vertices of the closed simplex to the three vertices \((0,1/2,1/2)\) and its coordinate permutations. Conversely, for every \(y\in D\), the coordinates \(x_i=1-2y_i\) are positive and sum to one, with \(T(x)=y\); therefore \(T(\Delta)=D\). On the tangent plane \(\{v:\sum_i v_i=0\}\), \(T\) acts as scalar multiplication by \(-1/2\). Its two-dimensional absolute Jacobian is exactly \(1/4\). Thus \(\operatorname{area}(D)=\operatorname{area}(\Delta)/4\), proving the known acuteness probability \(1/4\), and the push-forward of uniform measure on \(\Delta\) is precisely uniform measure on \(D\). This is the asserted conditional law.

**3. Universal majorization and strictness.** The doubly stochastic matrix
\[
T=\frac12\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}
\]
is the average of the two nontrivial cyclic-permutation matrices. By the majorization criterion, \(T(x)\prec x\). One can see the comparison directly: every output coordinate is an average of two input coordinates, and the sum is conserved. The centered identity
\[
T(x)-\frac{\mathbf1}{3}=-\frac12\left(x-\frac{\mathbf1}{3}\right)
\]
implies \(V(T(x))=V(x)/4\). Thus \(T(x)\) cannot be a coordinate permutation of \(x\) unless \(x=(1/3,1/3,1/3)\). The defining implication of Schur concavity yields \(\Phi(T(x))\ge\Phi(x)\), and strict Schur concavity yields strict inequality at every nonequilateral vector. The equilateral vector has zero probability, proving the almost-sure and distributional claims. The identity for \(V\) also proves its complete conditional law.

**4. Excentral identification and concrete shape scores.** The classical excentral angle identity is \(\Theta_i^{\mathrm{exc}}=\pi/2-\Theta_i/2\), exactly \(\Theta^{\mathrm{exc}}/\pi=T(X)\). For a triangle of circumradius one and angles \(\theta_i=\pi x_i\), the area, perimeter, and inradius are respectively
\[
A(x)=2\prod_{i=1}^3\sin(\pi x_i),\qquad
P(x)=2\sum_{i=1}^3\sin(\pi x_i),\qquad
r(x)=4\prod_{i=1}^3\sin\left(\frac{\pi x_i}{2}\right).
\]
The functions \(t\mapsto\log\sin(\pi t)\), \(t\mapsto\sin(\pi t)\), and \(t\mapsto\log\sin(\pi t/2)\) are strictly concave on \((0,1)\). Hence these three positive symmetric shape scores are each strictly Schur-concave (apply the logarithm to either product). Their simultaneous strict coupling follows from Step 3. Crucially, the unit-circumradius normalization is imposed *after* forming the excentral shape.

**5. Exact perimeter and imbalance benchmarks.** For \(X\sim\operatorname{Dirichlet}(1,1,1)\), any coordinate has the \(\operatorname{Beta}(1,2)\) density \(2(1-t)\) on \((0,1)\). Therefore
\[
\mathbb E[P(X)]
=6\int_0^1 2(1-t)\sin(\pi t)\,dt=\frac{12}{\pi},
\]
whereas, since \(\sin(\pi(1-t)/2)=\cos(\pi t/2)\),
\[
\mathbb E[P(T(X))]
=6\int_0^1 2(1-t)\cos\left(\frac{\pi t}{2}\right)\,dt
=\frac{48}{\pi^2}.
\]
Finally \(\operatorname{Var}(X_i)=1/18\) for each coordinate, whence \(\mathbb E[V(X)]=3/18=1/6\), and Step 3 gives \(\mathbb E[V(T(X))]=1/24\). Every displayed equality has now been derived for the complete continuous law.

## Verification

The separately supplied `verification.py` computes the exact \(3\times3\) transport matrix, its doubly stochastic row and column sums, its determinant \(1/4\), and its three vertex images symbolically. It checks majorization and strict area/perimeter/inradius improvements over 17,296 positive rational simplex points. Using a fixed pseudorandom seed, it then compares the transported distribution with independent rejection sampling conditioned on acuteness (350,000 transported and approximately 350,000 accepted points), and verifies the acuteness probability and three shape-score marginals. The standalone checker prints `ALL_CHECKS_PASSED` when every diagnostic succeeds. These numerical tests are diagnostics, not a replacement for the exact change-of-variables and majorization proof.

Reproduction: execute `python verification.py` with Python 3, NumPy, SciPy, and SymPy installed. The proof uses only elementary order statistics, an affine Jacobian, majorization, and familiar trigonometric concavity.

## Relationship to prior work

Wendel's 1962 hemispherical-coverage theorem supplies the classical probability \(\mathbb P(\mathcal A)=1/4\) for three uniform circle points. Akopyan, Edelsbrunner, and Nikitenko (first public arXiv version July 15, 2020) explicitly recall this one-quarter result and investigate a distinct sphere-surface sampling scheme, for which the acute-triangle probability is one-half. Edelman and Strang study random triangle shapes from Gaussian coordinates and explicitly distinguish uniform angle-space sampling from uniform shape-space sampling. These results neither state the excentral push-forward identity for **uniform circle-point triangles** nor the consequent universal Schur-concave coupling.

A publicly indexed later study of finite regular-polygon triangles already treats conditional first and second area moments and their continuum limit. Those moment values are **not** offered here as new results. The asserted contribution is the explicit *complete conditional law*, deterministic excentral coupling, and its simultaneous first-order stochastic consequences for an entire class of shape scores, together with the complete angular-variance scaling. Similarity of marginal moments or of the one-quarter event probability does not, by itself, imply a coupling or stochastic ordering.

## Limitations

The statement is specific to exactly three independently arclength-uniform vertices of a circle. The conditional affine transport fails to be asserted for nonuniform angular distributions, independent points in a disk, the Gaussian-triangle shape measure, or independently sampled vertices on the two-sphere. It describes angles and scale-normalized functions of angles, not full point locations. Strictness excludes the equilateral vector, which has probability zero. A bounded literature and published-record search does not establish exhaustive historical priority; some relevant later indexed material could not be inspected in full. No independent mathematical review or external validation is claimed.

## References

1. J. G. Wendel, *A Problem in Geometric Probability*, Mathematica Scandinavica **11** (1962), 109–112. DOI: https://doi.org/10.7146/math.scand.a-10655.
2. A. Akopyan, H. Edelsbrunner and A. Nikitenko, *The Beauty of Random Polytopes Inscribed in the 2-sphere*, arXiv:2007.07783v1 (public July 15, 2020), especially pp. 4–6. https://arxiv.org/abs/2007.07783.
3. A. Edelman and G. Strang, *Random Triangle Theory with Geometry and Applications*, draft dated November 10, 2012, especially Section 3.6 on angle-space versus Gaussian shape-space laws. https://math.mit.edu/~edelman/homepage/papers/focm.pdf.
4. *Conditional area moments for center-containing regular-polygon triangles*, publicly indexed research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-conditional-area-moments-for-center-containing-regular-polygon-t--c4fde75045b5. Only the public indexed summary was accessible for this comparison; its full text was not verified.
