# Closed linear self-reproducing annular Hadamard algebras are finite block algebras

## Finding

Fix \(a>0\). Let \(X_a=\mathcal O(\Omega_a)\), where \(\Omega_a=\{z\in\mathbb C:e^{-a}<|z|<e^a\}\), equipped with uniform convergence on compact subsets. If \(c_n(f)\), \(n\in\mathbb Z\), denotes the Laurent coefficients, define the contour/Hadamard product by \(c_n(f\diamond g)=c_n(f)c_n(g)\).

**Classification theorem.** A nonempty, complex-linear, topologically closed subset \(V\subset X_a\) satisfies the **setwise** equality \(V\diamond V=V\) if and only if there is a finite family of pairwise disjoint, nonempty, finite sets \(E_1,\dots,E_r\subset\mathbb Z\) such that
\[
V=\left\{\sum_{j=1}^{r}\lambda_j P_{E_j}:\lambda_j\in\mathbb C\right\},\qquad P_E(z)=\sum_{n\in E}z^n.
\]
The empty family \(r=0\) describes \(V=\{0\}\). In particular, **every such closed linear self-reproducing family is finite-dimensional**. For nonzero \(V\), the block family is uniquely determined up to permutation, as the supports of the primitive idempotents intrinsic to \(V\).

## Assumptions and scope

The topology is the usual compact-open Fréchet topology on a **fixed reciprocal annulus**. Closure is essential. Linearity is over \(\mathbb C\), and self-reproduction means literal products, not a dense linear span of products. No assumption that \(V\) is an ideal in \(X_a\) or contains the ambient multiplication unit is made. The annulus contains the unit circle, and all Laurent indices (positive and negative) are allowed.

## Proof

**1. All elements extend through every larger reciprocal annulus.** As \(V\diamond V=V\), associativity implies \(V^{\diamond m}=V\) setwise for every integer \(m\ge1\). The standard Laurent coefficient estimate at the two circles of radii \(e^{\pm b}\), for \(0<b<a\), gives
\[
|c_n(f)|\le p_b(f)e^{-b|n|},\qquad p_b(f)=\sup_{e^{-b}\le|z|\le e^b}|f(z)|.
\]
If \(f=f_1\diamond\cdots\diamond f_m\), the coefficient product obeys
\[
|c_n(f)|\le \left(\prod_{k=1}^{m}p_b(f_k)\right)e^{-mb|n|}.
\]
Since \(b<a\) is arbitrary, this Laurent series converges normally on every compact subannulus of \(\Omega_{ma}\). The extensions from different \(m\) agree by identity on \(\Omega_a\); hence every \(f\in V\) has a unique extension to \(\mathbb C^*=\mathbb C\setminus\{0\}\). This also independently reconstructs the needed forward direction of Theorem 5.2 and Theorem 5.3 in [1].

**2. Closedness forces finite dimension.** Let \(T:V\to\mathcal O(\Omega_{2a})\) send \(f\) to its unique extension. Because \(V\) is a closed subspace of the Fréchet space \(X_a\), \(V\) is Fréchet. The graph of \(T\) is closed: if \(f_k\to f\) in \(V\) and \(Tf_k\to F\) in \(\mathcal O(\Omega_{2a})\), restriction to \(\Omega_a\) yields \(F|_{\Omega_a}=f\), so \(F=Tf\). The Fréchet closed graph theorem makes \(T\) continuous.

Fix any \(b_1\) with \(a<b_1<2a\). Continuity, using the increasing defining family of seminorms on \(V\), gives constants \(0<b_0<a\) and \(C>0\) for which
\[
p_{b_1}(Tf)\le C p_{b_0}(f)\qquad (f\in V).
\]
For every \(0<t<a\) we consequently have \(p_t(f)\le C p_{b_0}(f)\), since \(\Omega_t\subset\Omega_{b_1}\). Thus the single norm \(p_{b_0}\) generates the original Fréchet topology on \(V\), and the normed space \((V,p_{b_0})\) is complete.

Its closed unit ball has extensions bounded by \(C\) on the larger compact annulus of width \(b_1\). Montel's theorem (or Cauchy estimates and Arzelà–Ascoli) makes that ball relatively compact in the \(p_{b_0}\) norm. Completeness and closedness make it compact. The closed unit ball of an infinite-dimensional normed space cannot be compact (Riesz's lemma), so \(d=\dim_{\mathbb C}V<\infty\).

**3. Every finite-dimensional coefficient algebra decomposes into finite blocks.** Assume \(d>0\). Laurent coefficient functionals jointly separate points of \(V\). Linear algebra therefore provides finitely many indices \(n_1,\ldots,n_m\in\mathbb Z\) for which the map \(J:V\to\mathbb C^m\), \(J(f)=(c_{n_1}(f),\ldots,c_{n_m}(f))\), is injective. Discard any zero coordinate functional. Declare two of the remaining coordinates equivalent if their evaluations agree on every element of \(V\). There are \(r\) equivalence classes, with nonzero, pairwise distinct corresponding linear functionals.

A finite union of proper complex-linear hyperplanes cannot exhaust \(V\), so choose \(h\in V\) for which the values \(\lambda_1,\ldots,\lambda_r\) at the representative coordinates are nonzero and pairwise distinct. For each \(j\), the polynomial
\[
Q_j(t)=\frac{t}{\lambda_j}\prod_{k\ne j}\frac{t-\lambda_k}{\lambda_j-\lambda_k}
\]
has \(Q_j(0)=0\) and \(Q_j(\lambda_k)=\mathbf1_{j=k}\). Because \(V\) is closed under \(\diamond\) and \(Q_j\) has zero constant term, \(u_j=Q_j^{\diamond}(h)\), with ordinary polynomial powers interpreted as Hadamard powers, belongs to \(V\). On all selected coordinates, \(u_j\) equals the indicator of class \(j\). Injectivity of \(J\) now shows \(u_j\diamond u_j=u_j\), \(u_i\diamond u_j=0\) for \(i\ne j\), and that every \(f\in V\) is a linear combination of the \(u_j\), with the representative coordinate values as coefficients.

For an idempotent \(u_j\), each Laurent coefficient solves \(c_n(u_j)^2=c_n(u_j)\) and hence belongs to \(\{0,1\}\). The above two-sided Cauchy estimate implies \(c_n(u_j)\to0\) as \(|n|\to\infty\), so \(u_j=P_{E_j}\) for a finite, nonempty set \(E_j\). Orthogonality makes the supports pairwise disjoint. This proves the stated form. Since a product of copies of \(\mathbb C\) has a canonical family of primitive idempotents, the \(u_j\) and therefore the \(E_j\) are uniquely determined up to reordering.

**4. Converse and exact factorization.** For disjoint finite blocks, coefficientwise multiplication gives
\[
\left(\sum_j\lambda_jP_{E_j}\right)\diamond\left(\sum_j\mu_jP_{E_j}\right)=\sum_j\lambda_j\mu_j P_{E_j}.
\]
Every coefficient \(\lambda_j\) has a complex square root, so every vector is an actual square; hence \(V\diamond V=V\). This \(V\) is finite-dimensional and therefore closed in \(X_a\). The zero case is immediate. \(\square\)

## Verification

The argument is analytic and algebraic, with no numerical step or external computational certificate. Verification consists of: the explicit two-sided Laurent coefficient bound; the closed-graph condition for the extension operator; the continuous-seminorm bound on a wider annulus; compactness via Montel on a strictly smaller annulus; the zero-constant interpolation polynomial; and coordinatewise verification of idempotents, orthogonality, and square roots. The polynomial \(Q_j\) is well-defined because all selected \(\lambda_j\) are nonzero and distinct. The unique finite-block form includes the zero subspace, finite-dimensional non-ideal examples such as \(\operatorname{span}_{\mathbb C}\{z^2+z^4\}\), and block ideals as the singleton-block subclass.

## Relationship to prior work

Ben-Simon [1], Theorems 5.2–5.3, proves continuation of elements of any self-reproducing family and exhibits a **dense nonclosed infinite-dimensional** maximal family; Theorem 7.2 treats **uniformly bounded** self-reproducing sets, not nonzero complex-linear spaces (which are scalar-unbounded); Theorem 8.2 classifies finite-dimensional **ideals**, rather than the proper block subalgebras appearing here. The present result adds the closed-linear hypothesis, derives finite-dimensionality from continuation through the closed graph theorem and Montel compactness, and classifies every such algebra including all proper non-ideal blocks. Brück and Müller [2] study closed ideals in another Hadamard setting, with ambient-domain and ideal hypotheses distinct from the present claim. Render [3] systematically studies holomorphic Hadamard algebras; the available abstract alone cannot establish whether any uninspected theorem implies this specific classification.

## Limitations

This is solely a classification of closed **complex-linear** subspaces satisfying setwise self-reproduction on one annulus, not a classification of arbitrary nonlinear self-reproducing families, nonclosed linear algebras, or all closed subalgebras lacking factorization. It is not a claim that a closed ideal is finite-dimensional. In particular, the cited paper explicitly contains infinite-dimensional closed convolution ideals, but such ideals need not factor internally. Full text of the broad historical study [3] was unavailable in this investigation, leaving a limited residual priority/implication risk; this does not affect the self-contained proof. Independent examination remains outstanding.

## References

[1] Gabriel Ben-Simon, *Analytic Properties of Self-Reproducing Families under Contour Convolution*, arXiv:2610.19197v1, first posted 13 October 2026. https://arxiv.org/html/2610.19197v1

[2] Rainer Brück and Jürgen Müller, *Closed Ideals in a Convolution Algebra of Holomorphic Functions*, Canadian Journal of Mathematics 47 (1995), 915–928. https://doi.org/10.4153/CJM-1995-047-2

[3] Hermann Render, *Algebras of Holomorphic Functions with Hadamard Multiplication*, Studia Mathematica 118 (1996), 77–100. https://doi.org/10.4064/sm-118-1-77-100
