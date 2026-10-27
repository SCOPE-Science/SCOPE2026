# Exact projection constant of the exterior-square Fourier block on symmetric groups

## Finding
For every integer \(n\ge4\), consider the real subspace \(X_n\subset\ell^\infty(S_n)\) consisting of all matrix coefficients of the irreducible symmetric-group representation indexed by \((n-2,1,1)\), with its inherited supremum norm. Its dimension is \(d_n^2\), where \(d_n=(n-1)(n-2)/2\). The **absolute Banach-space projection constant**, equal here to the smallest norm of any real-linear projection from \(\ell^\infty(S_n)\) onto \(X_n\), is
\[
\lambda(X_n)=(n-1)(n-2)\sum_{\substack{f,t\ge0\\f+2t\le n}}\left(t-\frac{(f-1)(f-2)}2\right)_+\frac{r_{n-f-2t}}{f!\,2^t t!},
\]
where \(u_+=\max\{u,0\}\) and \(r_m\) is the fraction of permutations of \(m\) letters having no fixed points and no 2-cycles (with \(r_0=1\)); equivalently \(r_m=[z^m]\exp(-z-z^2/2)/(1-z)\). The orthogonal Fourier projector is an optimal projection in the supremum norm, among **all** projections, not only invariant ones.

There is a dimension-free asymptotic constant
\[
\lim_{n\to\infty}\frac{\lambda(X_n)}{d_n}
=2e^{-3/2}\sum_{f,t\ge0}\frac{\left(t-\frac{(f-1)(f-2)}2\right)_+}{f!\,2^t t!}
\approx0.643322969593223.
\]
In particular, \(\lambda(X_n)\) grows quadratically with \(n\). The negative character support is exactly the strict threshold \(t>(f-1)(f-2)/2\), where \(f\) and \(t\) count fixed points and disjoint 2-cycles.

## Assumptions and scope
All spaces, functions, and linear projections are real. The group \(S_n\) acts on itself by left and right translation; \(X_n\) is the **full** regular-representation isotypic summand associated with the hook \((n-2,1,1)\), rather than the smaller exterior-square representation itself. Its dimension is the square of the character degree. The absolute projection constant of a finite-dimensional normed space is the supremum of its relative least projection norms over all isometric superspaces. The sequence \(r_m\) uses exact uniform counting and does not carry any probabilistic approximation in the finite formula.

## Proof
**1. Character and kernel.** Let \(V\) be the standard real \((n-1)\)-dimensional permutation representation (the zero-sum hyperplane). Its exterior square \(\bigwedge^2 V\) is the irreducible representation \((n-2,1,1)\), of dimension \(d_n\). Write \(F(g)\) for the number of fixed points and \(T(g)\) for the number of disjoint 2-cycles of \(g\in S_n\). The standard character is \(F(g)-1\), while \(F(g^2)=F(g)+2T(g)\). The exterior-square trace identity gives the exact character
\[
\chi(g)=\frac{(F(g)-1)^2-(F(g^2)-1)}2
=\frac{(F(g)-1)(F(g)-2)}2-T(g).
\]
Its value at the identity is \(d_n\); orthogonality to the trivial representation implies \(\sum_{g\in S_n}\chi(g)=0\). The orthogonal projector onto the full isotypic subspace is convolution by the central kernel \(k(g)=d_n\chi(g^{-1})/n!\). Each row of the convolution matrix is a translate of this kernel. Hence its exact supremum-operator norm is
\[
\|P_n\|_{\infty\to\infty}=\frac{d_n}{n!}\sum_{g\in S_n}|\chi(g)|
=\frac{2d_n}{n!}\sum_{g\in S_n}(-\chi(g))_+.
\]
The last equality uses the zero mean and holds for all \(n\ge4\); it does **not** assume that all negative character values equal \(-1\).

**2. Exact cycle counting.** There are exactly
\[
\frac{n!}{f!\,2^t t!\,(n-f-2t)!}\,R_{n-f-2t}
\]
permutations with exactly \(f\) fixed points and exactly \(t\) 2-cycles, where \(R_m=m!r_m\) counts permutations whose cycles all have length at least three. Choosing disjoint fixed points and ordered 2-cycle slots proves this expression. The exponential formula for permutations gives \(\sum_{m\ge0}r_m z^m=\exp(\sum_{j\ge3}z^j/j)=\exp(-z-z^2/2)/(1-z)\). Substitution into the preceding negative-mass identity yields exactly the finite sum in the finding and the stated sign-support threshold.

**3. Optimality among every linear projection.** The left and right regular translations act isometrically on \(\ell^\infty(S_n)\) and preserve \(X_n\). Given any projection \(Q\) onto \(X_n\), average its conjugates under the finite group \(S_n\times S_n\). The average is still a projection onto \(X_n\) and has norm at most \(\|Q\|\). It commutes with all left and right translations, so its convolution kernel is central. Every central convolution acts as one scalar on each irreducible isotypic block of the regular representation. Because the averaged projection is the identity on \(X_n\) and has range \(X_n\), these scalars are one on the \((n-2,1,1)\) block and zero on every other block; it therefore equals \(P_n\). Thus \(P_n\) minimizes the norm among all real-linear projections onto \(X_n\). Furthermore, for every isometric inclusion of \(X_n\) into a Banach space \(Y\), extend each coordinate evaluation functional \(X_n\to\mathbb R\) of norm at most one to \(Y\) using Hahn–Banach. These extensions form a contraction \(Y\to\ell^\infty(S_n)\) fixing \(X_n\), and composition with \(P_n\) is a projection from \(Y\) onto \(X_n\) of norm at most \(\|P_n\|\). Therefore the computed relative least projection norm equals the **absolute** projection constant.

**4. Limit.** The numbers of cycles of lengths one and two in a uniformly random permutation converge jointly to independent Poisson random variables \(F_\infty\) and \(T_\infty\) of respective means \(1\) and \(1/2\). This also follows directly from the finite joint probability formula in step 2 by fixing \(f,t\) and using \(r_{n-f-2t}\to e^{-3/2}\). For \(n\ge4\), \(\mathbb E[T]=1/2\) and \(\mathbb E[T(T-1)]=1/4\), so \(\mathbb E[T^2]=3/4\) uniformly. Since \(0\le (T-(F-1)(F-2)/2)_+\le T\), uniform square integrability controls the tails and justifies passing from the finite expectation to the infinite Poisson sum. Divide the exact norm by \(d_n\) to obtain the displayed limit. The double series is absolutely convergent; the numerical value follows by factorially convergent summation. \(\square\)

## Verification
The included standard-library script `verify_hook.py` computes the cycle-index norm independently from the finite \(r_m\)-sum, in exact rational arithmetic for \(4\le n\le12\). It also verifies character mean zero and second moment one for those dimensions, and checks the exact no-short-cycle recurrence. Its result is `VERIFY_OK rational_cycle_classes=4..12 sign_support_and_orthogonality_and_formula`. These finite computations are consistency checks, not substitutes for the all-dimensional character and counting proof.

## Relationship to prior work
Barvinok and Stephen (2001, §7.4 and Proposition 7.5) explicitly describe the skew-symmetric \((n-2,1,1)\) representation and the fixed-point/two-cycle character formula; **neither the character nor that representation is claimed as new**. Their theorem concerns quadratic-assignment value distributions rather than the negative character mass or a minimal \(\ell^\infty\) projection. The standard-block derangement formula for doubly transitive groups and the companion \((n-2,2)\) Fourier-block norm concern different isotypes. In particular, the companion character is negative precisely for one or two fixed points with zero 2-cycles; the exterior-square character here has an unbounded negative tail governed by a fixed-point-dependent threshold. General symmetry averaging of projections (Rudin's technique, discussed in Defant et al.) supplies a known tool for optimality, but not the exact norm or Poisson constant for this isotypic space.

## Limitations
The theorem concerns the full regular isotypic block, not functions on 2-subsets or matrices, and assumes real scalars and \(n\ge4\). It does not evaluate intermediate \(\ell^p\) operator norms, projection constants of incomplete matrix-coefficient subspaces, or all other irreducible partitions. The recurrence checks only finite small orders. An equivalent character-norm computation in older representation-theoretic tables remains a bibliographic risk; no claim of exhaustive novelty verification or independent audit is made.

## References
1. A. Barvinok and T. Stephen, *The distribution of values in the quadratic assignment problem*, arXiv:math/0104229v1, first public 2001-04-24, §7.4 and Proposition 7.5, https://arxiv.org/html/math/0104229v1.
2. D. Ellis, Y. Filmus and E. Friedgut, *A quasi-stability result for dictatorships in \(S_n\)*, arXiv:1209.5557v1, first public 2012-09-25, §2 (Fourier isotypic subspaces), https://arxiv.org/abs/1209.5557.
3. A. Defant, D. Galicer, M. Mansilla, M. Mastyło and S. Muro, *Projection constants for spaces of multivariate polynomials*, arXiv:2208.06467v1, §2.2 and Introduction (projection constants and averaging), https://arxiv.org/pdf/2208.06467.
4. *Derangement density controls the standard Fourier block of every doubly transitive action*, public mathematical research record (2026), distinct standard-representation isotype.
5. *Exact endpoint norms for the \((n-2,2)\) Fourier block of symmetric groups*, public mathematical research record (2026), distinct symmetric-square isotype.
