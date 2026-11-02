# The coefficient discriminant of weighted three-moment complete intersections is a subset-sum hyperplane arrangement

## Finding
Let \(k\) be algebraically closed with \(\operatorname{char}k=p\ge5\), and let \(n\ge6\). For \(\boldsymbol a=(a_1,\ldots,a_n)\in(k^*)^n\), let
\[
X_{\boldsymbol a}=V(F_1,F_2,F_3)\subset\mathbb P^{n-1}_k,
\qquad F_j=\sum_{i=1}^n a_ix_i^j\quad(j=1,2,3).
\]
For a nonempty set of coordinate indices \(S\), write \(A_S=\sum_{i\in S}a_i\) and let \(e_S\) be its zero-one incidence vector. The parameter discriminant, understood as the set of coefficients with a singular fiber, is exactly
\[
\mathscr D=\bigcup_{\varnothing\ne S\subseteq\{1,\ldots,n\}}
\{\boldsymbol a\in(k^*)^n:A_S=0\}.
\]
(The singleton hyperplanes have empty intersection with the coefficient torus.) This is a *set-theoretic* discriminant statement; no assertion about a scheme-theoretic discriminant multiplicity is made.

On the open parameter set \(W=A_{\{1,\ldots,n\}}\ne0\), the singular **subscheme** is the finite reduced scheme
\[
\operatorname{Sing}(X_{\boldsymbol a})
=\{[e_S]:\varnothing\ne S\subsetneq\{1,\ldots,n\},\ A_S=0\}.
\]
Every one of these points is an ordinary quadratic double point. Moreover \(X_{\boldsymbol a}\) is a geometrically integral normal complete intersection of multidegree \((1,2,3)\), degree \(6\), and dimension \(n-4\).

For \(2\le|S|\le n-1\), a general coefficient vector on \(A_S=0\), and on no other subset-sum hyperplane, has precisely one node, namely \([e_S]\). The generic fiber off the arrangement is smooth. When \(n=6\), a smooth fiber is a degree-six complete-intersection K3 surface, and a general single wall gives a one-node K3 degeneration.

## Assumptions and scope
All assertions are over the algebraic closure of a finite field of characteristic at least five, or over any algebraically closed field of that characteristic. The ambient scheme is defined by exactly the displayed three equations. The normality and exact singular-scheme statements require \(W\ne0\). The global discriminant set includes \(W=0\), where only singularity existence is asserted. A generic-wall coefficient avoids all other subset-sum hyperplanes; a wall indexed by a singleton is absent from \((k^*)^n\).

## Proof
**1. Jacobian-rank criterion.** The three rows of the affine Jacobian are \((a_i)\), \((2a_ix_i)\), and \((3a_ix_i^2)\). Since all weights and \(2,3\) are invertible, the Jacobian has rank below three precisely when the projective coordinates \(x_i\) take at most two distinct values. Indeed, columns corresponding to three distinct coordinate values form an invertible Vandermonde matrix, while any two-value configuration spans at most a two-dimensional column space.

**2. The subset-sum classification.** Suppose the coordinates assume two distinct values \(u\) on \(S\) and \(v\) on its nonempty complement \(T\), and set \(A=A_S\), \(B=A_T\). The defining equations become
\[
Au+Bv=Au^2+Bv^2=Au^3+Bv^3=0.
\]
If \(uv\ne0\), the first two equations and \(u\ne v\) force \(A=B=0\), hence \(W=0\). If exactly one value is nonzero, the sum of weights on its support must be zero, and conversely the corresponding projective indicator point satisfies all three equations and has Jacobian rank at most two. The all-equal nonzero case satisfies the equations precisely when \(W=0\), yielding the singular point \([1:\cdots:1]\). This proves the entire set-theoretic discriminant and, on \(W\ne0\), exhausts the singular support.

**3. Nondegenerate transverse quadratic form.** Fix a singular indicator point \([e_S]\) with \(A=0\) and \(B=W\ne0\). The differentials of \(F_1\) and \(F_2\) are linearly independent there, and their simultaneous kernel on the affine cone is
\[
\left\{(u_i)_{i\in S},(v_i)_{i\in T}:\sum_{i\in S}a_iu_i=0,
\ \sum_{i\in T}a_iv_i=0\right\}.
\]
The differential of \(G=F_3-\frac32F_2\) vanishes at the point. Its quadratic term on this kernel is
\[
\frac32\left(\sum_{i\in S}a_iu_i^2-\sum_{i\in T}a_iv_i^2\right).
\]
For the diagonal nondegenerate quadratic form \(q_S=\sum_{i\in S}a_iu_i^2\), the orthogonal complement of the hyperplane \(\sum_{i\in S}a_iu_i=0\) is spanned by the all-ones vector. Because \(A=0\), the restriction has precisely this one-dimensional radical; it is exactly the projective scaling direction, so its quotient is nondegenerate. On the \(T\)-block the analogous restriction is nondegenerate because its weighted total \(B\ne0\). After quotienting scaling, the complete quadratic form is therefore nondegenerate on a space of dimension \((|S|-2)+(|T|-1)=n-3\). The formal Morse lemma in odd characteristic gives the completed local equation \(z_1^2+\cdots+z_{n-3}^2=0\). Its Jacobian ideal is the maximal ideal, proving both the ordinary-double-point type and reducedness of the singular subscheme.

**4. Complete intersection and integrality.** Since \(n\ge6\), the intersection of three positive-degree hypersurfaces in \(\mathbb P^{n-1}\) is nonempty and every irreducible component has dimension at least \(n-4\). By Steps 1–2, when \(W\ne0\) the rank-deficient locus is finite. Thus each component has a point where the Jacobian has rank three, forcing dimension exactly \(n-4\). The three forms constitute a regular sequence, and the complete intersection is Cohen–Macaulay. It is generically smooth and hence reduced; because its singularities are isolated in dimension at least two, the conditions \(R_1\) and \(S_2\) imply normality. A positive-dimensional projective complete intersection is connected (equivalently, the Koszul resolution gives \(H^0(\mathcal O_X)=k\)); normal connected components cannot meet, so the fiber is irreducible. Its degree is \(1\cdot2\cdot3=6\).

**5. Generic walls and K3 surfaces.** Distinct proper nonempty index sets give distinct linear forms \(A_S\) over the coefficient field. For any \(S\) with \(|S|\ge2\) and proper complement, \(A_S=0\) meets the torus, and avoiding every other hyperplane is a nonempty Zariski-open condition. In that open set Step 2 gives exactly one indicator singular point and Step 3 makes it a node. When \(n=6\), eliminating the linear form leaves a \((2,3)\) complete intersection in \(\mathbb P^4\); adjunction and standard complete-intersection cohomology yield trivial canonical bundle and \(H^1(\mathcal O)=0\) in the smooth case, so it is a K3 surface.

## Verification
The standalone file `verification.py` exhaustively enumerates rational points and checks Jacobian ranks for three six-variable examples over the prime fields of cardinalities five and seven. It compares their singular supports to the independently calculated zero-sum subsets. All three checks pass and the program prints `VERIFY_OK`. These are finite consistency checks only; the proof above establishes the general family. Reproduce with `python3 verification.py` (Python 3 standard library).

## Relationship to prior work
Giménez–Gottig–Palacios–Pérez–Privitelli, *Power Sum Varieties over Finite Fields* (arXiv:2610.32056v1, October 23, 2026), study the geometry and normality of power-sum systems and obtain bounds on singular-locus dimension. Their displayed general projective normality conditions concern equal-coefficient power sums; they do not classify the coefficient-space discriminant, indicator singular points for arbitrary nonzero weights, or the generic single-node walls in this family. The preceding paper by Gottig–Pérez–Privitelli (arXiv:2401.06964v1) gives bounds and counting applications for systems of diagonal equations; its geometric results do not supply the weighted coefficient arrangement or these local analytic types. The specialized all-equal-weight characteristic-divisible situation is encompassed by the present formula, but that specialization is not the claimed novelty. The new assertion is the global coefficient discriminant and its nodal stratification, rather than a single coefficient vector.

## Limitations
This is a set-theoretic coefficient discriminant, not a calculation of its scheme-theoretic multiplicities or local intersection numbers where walls meet. The full-wall locus \(W=0\) is not classified by local singularity type here. No theorem is asserted in characteristic two or three, for vanishing weights, for more than three moment equations, or for the positive-characteristic behavior of K3 resolutions beyond the stated generic wall. A literature search cannot establish definitive historical priority; a general prior discriminant theory could contain an equivalent characterization. Independent audit has not been performed.

## References
1. N. Giménez, J. F. Gottig, M. Palacios, M. Pérez, M. Privitelli, *Power Sum Varieties over Finite Fields*, arXiv:2610.32056v1 (first posted October 23, 2026), https://arxiv.org/abs/2610.32056.
2. J. F. Gottig, M. Pérez, M. Privitelli, *An Approach to the Moments Subset Sum Problem Through Systems of Diagonal Equations over Finite Fields*, arXiv:2401.06964v1 (2024), https://arxiv.org/abs/2401.06964.
3. Standard results: Jacobian criterion; Serre normality criterion; Koszul cohomology of complete intersections; formal Morse lemma in characteristic different from two.
