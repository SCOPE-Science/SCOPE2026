# One forbidden hypersimplex vertex: exact asymmetry and a simplex of centers

## Finding
Let \(k,\ell\ge3\), \(n=k+\ell\), and \(H\subset[n]\) have \(|H|=k\). Delete exactly the vertex \(\mathbf1_H\) from the standard hypersimplex, retaining
\[
P_{k,\ell}(H)=\operatorname{conv}\{\mathbf1_B:B\subset[n],\ |B|=k,\ B\ne H\}.
\]
Put \(m=\min\{k,\ell\}\) and \(M=\max\{k,\ell\}\). For Minkowski asymmetry in the affine hull,
\[
s(P)=\min_{c\in P}\inf\{s\ge1:-(P-c)\subseteq s(P-c)\},
\]
the exact value is
\[
\boxed{s(P_{k,\ell}(H))=\max\left\{\frac M m,\frac m{m-1}\right\}=\begin{cases}
\dfrac m{m-1},&|k-\ell|\le1,\\
\dfrac M m,&|k-\ell|\ge2.
\end{cases}}
\]
Relative to the undeleted hypersimplex, the asymmetry increase is exactly \(1/(m-1)\) when \(k=\ell\), exactly \(1/[m(m-1)]\) when \(|k-\ell|=1\), and zero otherwise.

All minimizing centers are classified as follows, with \(J=[n]\setminus H\):

1. If \(|k-\ell|\ge2\), the **unique** center is \(c=(k/n)\mathbf1\).
2. If \(k=\ell=m\), the **unique** center has \(c_i=(m-1)/(2m-1)\) on \(H\) and \(c_j=m/(2m-1)\) on \(J\).
3. If \(k=m\) and \(\ell=m+1\), the **entire** center set is
\[
\boxed{c_i=\frac{m-1}{2m-1}\ (i\in H),\qquad
c_j=\frac{m-1+\theta_j}{2m-1}\ (j\in J),\quad
\theta_j\ge0,\ \sum_{j\in J}\theta_j=1.}
\]
4. If \(k=m+1\) and \(\ell=m\), the **entire** center set is
\[
\boxed{c_i=\frac{m-\theta_i}{2m-1}\ (i\in H),\quad
\theta_i\ge0,\ \sum_{i\in H}\theta_i=1,\qquad
c_j=\frac m{2m-1}\ (j\in J).}
\]
Thus the minimizing-center locus is a simplex of affine dimension \(m\) **if and only if** rank and corank differ by one; in every other parameter regime it is a point. In particular, the loss of a single basis does not change the asymmetry for rank--corank gap at least two, while the near-balanced case simultaneously increases asymmetry and creates an \(m\)-dimensional family of centers.

## Assumptions and scope
The integers satisfy \(k,\ell\ge3\), so both rank and corank are at least three. The ambient affine hull is \(x([n])=k\), of dimension \(n-1\). The expression is affine-invariant Minkowski asymmetry, **not** Euclidean inradius, Minkowski addition, or a mean-width invariant. A *center* means any point attaining the displayed minimizing asymmetry; uniqueness refers to all such points in the affine hull. For the rank-two or corank-two cases, published general rank-two matroid results already apply; they are not part of the novelty asserted here.

## Proof
**1. The exact halfspace representation.** Write \(x(A)=\sum_{i\in A}x_i\). The hypersimplex is \(\Delta_{n,k}=\{x\in[0,1]^n:x([n])=k\}\). Its edges exchange exactly one selected and one unselected coordinate, so \(x(H)\) changes by at most one along any edge. Intersecting with the integral cut \(x(H)\le k-1\) therefore creates no new vertices: a crossing edge ends on the cut at an already existing vertex. Only \(\mathbf1_H\) violates it. Hence
\[
\boxed{P_{k,\ell}(H)=\{x\in[0,1]^n:x([n])=k,\ x(H)\le k-1\}.}\tag{1}
\]
The polytope is full-dimensional in its displayed affine hyperplane, since the cut removes a nonempty proper vertex corner of the full-dimensional hypersimplex. Its geometry is independent of the particular labels in \(H\).

**2. Exact reflected containment.** For \(s\ge1\), \(-(P-c)\subseteq s(P-c)\) is equivalent to \(((s+1)c-x)/s\in P\) for every \(x\in P\). By (1), the coordinate inequalities require
\[
1\le z_i\le s,\qquad z=(s+1)c,\qquad z([n])=k(s+1).\tag{2}
\]
Indeed every coordinate takes both values zero and one somewhere in \(P\) because \(k,\ell\ge3\). The cut inequality requires
\[
z(H)\le s(k-1)+\min_{x\in P}x(H)
=s(k-1)+\max\{0,k-\ell\}.\tag{3}
\]
The minimum is attained by a surviving basis containing as many elements of \(J\) as possible. Conversely (2)--(3) ensure that every reflected point lies in the halfspace description (1). Thus they are **necessary and sufficient**, with no symmetry restriction on \(c\).

**3. Sharp lower bounds.** Put \(a=\max\{0,k-\ell\}\). Summing the lower and upper bounds in (2) yields \(s\ge\ell/k\) and \(s\ge k/\ell\). Since \(z(H)\ge k\), (3) yields
\[
s\ge\frac{k-a}{k-1}=\frac{m}{k-1}.
\]
Since \(z(J)\le\ell s\), combining the sum in (2) with (3) yields
\[
s\ge\frac{k-a}{\ell-1}=\frac{m}{\ell-1}.
\]
The maximum of these four obstructions is exactly \(\max\{M/m,m/(m-1)\}\). For integral \(m\ge3\), \(M/m\ge m/(m-1)\) whenever \(M\ge m+2\), whereas \(M/m<m/(m-1)\) for \(M=m\) or \(m+1\).

**4. Attainment and exhaustive center classification.** If \(M\ge m+2\), set \(s=M/m\). When \(k<\ell\), every coordinate of \(z\) must be one, because \(z([n])=n\) and each \(z_i\ge1\). When \(k>\ell\), every coordinate of \(z\) must equal \(s\), because \(z([n])=ns\) and each \(z_i\le s\). These vectors satisfy (3) by the lower bound already proved, yielding exactly the uniform center and proving uniqueness.

For \(k=\ell=m\), set \(s=m/(m-1)\). Equations (2)--(3) force \(z_i=1\) on \(H\); the total sum then forces \(z_j=s\) on \(J\). This gives the displayed unique center.

For \(k=m\), \(\ell=m+1\), (3) again forces \(z_i=1\) on \(H\). The remaining block obeys \(1\le z_j\le s\) and \(z(J)=ms\). Subtracting one from each of its \(m+1\) coordinates leaves total \(s-1\). Consequently \(z_j=1+(s-1)\theta_j\) with \(\theta_j\ge0\), \(\sum\theta_j=1\), and all such parameters satisfy (2)--(3). Division by \(s+1\) gives the first simplex formula.

For \(k=m+1\), \(\ell=m\), (3) and (2) force \(z_j=s\) on \(J\). The remaining block has \(m+1\) coordinates, each at most \(s\), with total \((m+1)s-(s-1)\); hence \(z_i=s-(s-1)\theta_i\) with \(\theta_i\ge0\), \(\sum\theta_i=1\). Division by \(s+1\) gives the second formula. There are exactly \(m+1\) affinely independent parameter vertices in either case, so the center locus is an \(m\)-simplex. This proves both attainment and the **complete** classification.

## Verification
The included standalone `verify.py` is a standard-library-only exact-rational finite checker. It enumerates all surviving basis vertices for every \(3\le k,\ell\le8\), constructs all predicted Minkowski-center vertices and their barycenter, and checks that every reflected basis vertex lies in (1). It also tests the four analytic lower bounds and the center-locus dimension predictions. Its run produced **36 dimension profiles, 48,164 surviving basis vertices, 212,798 exact reflected-vertex checks, and ten nonunique-center profiles**, all passing.

Separately, full numerical linear programs in the rescaled variables \((z,s)\), without imposing block symmetry, matched the formula for every \(3\le k,\ell\le10\) (64 parameter profiles). These checks are corroboration only: the all-dimensional proof is Steps 1--4 above.

## Relationship to prior work
Pineda-Villavicencio and Schröter develop the matroid-base-polytope framework and polytope reconstruction from basis-exchange graphs; the source's verified primary MSC2020 is 52B11. Ferroni establishes the circuit-hyperplane relaxation geometry and the associated matroid-polytope split, but studies Ehrhart polynomials and lattice points. Ferroni and Schröter extend valuation formulas for matroid polytopes; Minkowski asymmetry is not one of their evaluated invariants. Den Hertog, Pauphilet and Soali provide a **general robust linear program** for Minkowski centers of polyhedra. Our Step 2 is a concrete specialization of that method; neither their general optimization formulation nor the cited matroid papers state the present rank--corank law or the complete simplex-of-centers transition.

An existing full classification of Minkowski centers of **rank-two matroid base polytopes** covers rank two and, by complement duality, corank two. Both regimes are deliberately excluded. A result for panhandle matroid base polytopes concerns the opposite cell of the hypersimplex split, whose bases meet a distinguished block in at least \(k-1\) places, rather than the present complement in which \(x(H)\le k-1\); their polytope vertex sets and asymmetry problems differ. These statements do not imply the classification above for all rank and corank at least three.

## Limitations
Only deletion of **one** hypersimplex vertex is classified; arbitrary collections of forbidden bases, general sparse-paving matroids, and Euclidean center invariants are not covered. The result is an exact structural theorem about Minkowski centers, not a theorem on Ehrhart coefficients or volume. Finite checks cannot replace the proof. The relevant available sources do not state an equivalent theorem, but bibliographic priority cannot be guaranteed without an exhaustive independent literature review. No independent mathematical audit has been conducted.

## References
1. G. Pineda-Villavicencio and B. Schröter, *Reconstructibility of matroid polytopes*, arXiv:2010.10227 (first posted 2020-10-20; primary MSC2020 52B11), https://arxiv.org/abs/2010.10227 .
2. L. Ferroni, *On the Ehrhart Polynomial of Minimal Matroids*, arXiv:2003.02679 (first posted 2020-03-05), especially Section 5 and Proposition 5.3, https://arxiv.org/abs/2003.02679 .
3. L. Ferroni and B. Schröter, *Valuative invariants for large classes of matroids*, arXiv:2208.04893 (first posted 2022-08-09), https://arxiv.org/abs/2208.04893 .
4. D. den Hertog, J. Pauphilet, and M. Y. Soali, *Minkowski Centers via Robust Optimization: Computation and Applications*, preprint posted 2022, Proposition 4, https://optimization-online.org/2022/01/8768/ .
5. *Minkowski asymmetry and all centers of rank-two matroid base polytopes*, published mathematical result, identifier `a659b650d983`, rank-two scope and proof inspected.
