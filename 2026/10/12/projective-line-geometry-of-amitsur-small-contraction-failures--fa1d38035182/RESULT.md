# Projective-line geometry of Amitsur–Small contraction failures
## Finding
Let \(D\) be a noncommutative division ring finite-dimensional over its center \(F\), and suppose that \(D\) is not the Hamilton quaternion algebra over a real closed center. Then the splitting-field construction in Paran's 2026 classification can be chosen so that, for a maximal left ideal \(M\subset D[x,y]\) and its contraction
\[
J=M\cap D[x],
\]
the full interval of left ideals above \(J\) is completely determined.

There is a finite separable maximal subfield \(K/F\) and a simple left \(D[x]\)-module \(V\) such that
\[
D[x]/J\cong V\oplus V,
\qquad
\operatorname{End}_{D[x]}(V)\cong K.
\]
For every projective point \([a:b]\in\mathbf P^1(K)\), define
\[
W_{[a:b]}=\{(av,bv):v\in V\}\subset V\oplus V.
\]
Then the nonzero proper \(D[x]\)-submodules of \(D[x]/J\) are exactly the \(W_{[a:b]}\). Therefore the proper left ideals strictly containing \(J\) are exactly the ideals \(L_{[a:b]}\) obtained by pulling back these submodules, and every \(L_{[a:b]}\) is maximal. Moreover, for distinct projective points,
\[
L_{[a:b]}\cap L_{[c:d]}=J,
\qquad
L_{[a:b]}+L_{[c:d]}=D[x].
\]
Since \(K\) is infinite, \(J\) lies below infinitely many maximal left ideals. Equivalently, the interval \([J,D[x]]\) is isomorphic to the subspace lattice of \(K^2\): bottom element, one maximal overideal for each point of \(\mathbf P^1(K)\), and the top element.

## Assumptions and scope
The variables \(x,y\) are central. The division ring is assumed centrally finite and noncommutative. The exceptional positive case excluded from the claim is the Hamilton quaternion algebra over a real closed center, exactly as in the recent classification.

The field \(K\) is the separable maximal subfield chosen in the proof of the classification theorem. It is a finite separable splitting field of \(D\) and is not algebraically closed. The conclusion concerns the particular counterexample obtained from the paper's splitting-field construction; it does not assert that every possible nonmaximal contraction for \(D\) has the same interval.

## Proof
Paran's proof chooses a separable maximal subfield \(K\subset D\). Outside the Hamilton-over-real-closed case, this \(K\) is not algebraically closed and is a finite separable splitting field. Write \(K=F(\theta)\), choose a proper finite extension \(E=K(\alpha)\), and put
\[
A=D\otimes_F K.
\]
Because \(K\) splits \(D\), one has \(A\cong\operatorname{End}_K(V)\) for a simple left \(A\)-module \(V\) of dimension at least two over \(K\). Choose linearly independent \(u_1,u_2\in V\). The source constructs a maximal left ideal \(N\subset A\otimes_K E\) whose contraction satisfies
\[
A/(N\cap A)\cong V\oplus V.
\]
Its lifting lemma supplies a maximal left ideal \(M\subset D[x,y]\) and identifies
\[
D[x]/J\cong A/(N\cap A)\cong V\oplus V,
\qquad J=M\cap D[x],
\]
as left \(D[x]\)-modules. The action of \(D[x]\) on the right factors through a surjection \(D[x]\twoheadrightarrow A\). Hence its submodules are exactly the \(A\)-submodules.

Since \(A\cong\operatorname{End}_K(V)\), the commutant of the \(A\)-action on \(V\) is precisely the scalar field:
\[
\operatorname{End}_A(V)=K.
\]
The same equality holds for \(D[x]\)-endomorphisms because the action surjects onto \(A\).

Now let \(0\ne W\subsetneq V\oplus V\) be an \(A\)-submodule. The module \(V\oplus V\) is semisimple of composition length two, so \(W\cong V\). Choose an \(A\)-isomorphism \(\phi:V\to W\). Composing with the two coordinate projections gives two endomorphisms of \(V\), hence scalars \(a,b\in K\). They are not both zero, and
\[
\phi(v)=(av,bv).
\]
Thus \(W=W_{[a:b]}\), with the projective class \([a:b]\) uniquely determined. Conversely every \(W_{[a:b]}\) is visibly an \(A\)-submodule isomorphic to \(V\). This classifies all nonzero proper submodules.

Under the correspondence theorem, each \(W_{[a:b]}\) pulls back to a left ideal \(L_{[a:b]}\) with \(J\subsetneq L_{[a:b]}\subsetneq D[x]\). The quotient by \(W_{[a:b]}\) is again isomorphic to \(V\), so every \(L_{[a:b]}\) is maximal. Two distinct one-dimensional subspaces of \(K^2\) intersect trivially and span \(K^2\); therefore their corresponding submodules have intersection zero and sum \(V\oplus V\), which pulls back to the stated intersection and sum formulas for the ideals.

Finally, \(K\) is infinite. If the center \(F\) were finite, then the finite-dimensional division ring \(D\) would be finite and hence commutative by Wedderburn's little theorem, contrary to hypothesis. A finite extension of the infinite field \(F\) is infinite. Hence \(\mathbf P^1(K)\) is infinite.

## Verification
The infinite theorem follows from the source's exact module isomorphism and the elementary classification of submodules of two copies of a simple module whose endomorphism ring is a field. No finite computation is used to infer the theorem.

The bundled checker independently verifies the module-lattice step over \(A=M_2(\mathbb F_p)\) for \(p=2,3,5\). It enumerates every vector subspace of \(V\oplus V\), tests invariance under matrix-unit generators, and finds exactly \(p+1\) nonzero proper invariant subspaces, all of dimension two; distinct pairs are complementary. The output terminates with `VERIFY_OK`.

## Relationship to prior work
Paran's 2026 paper proves the complete centrally finite Amitsur--Small classification. Its Lemma 3.1 transports submodule structure through the polynomial-ring lifting, and Lemma 3.2 proves the decisive isomorphism \(A/(N\cap A)\cong V\oplus V\), recording composition length two. The main theorem states only that the contraction is nonmaximal. The paper does not state the projective-line parametrization of all overideals, and searches of its full text for projective or semisimple formulations found none.

Paran's 2024 precursor constructs explicit contractions generated by reducible one-variable polynomials and proves nonmaximality by exhibiting a strict containing left ideal. Chapman--Levin--Zaninelli's 2025/2026 cyclic-algebra paper reuses the Chapman--Paran criterion and likewise states nonmaximality, not the complete interval above the contraction. The earlier general semi-maximality result explains why contractions remain intersections of maximal left ideals, but it does not determine the number or geometry of those maximal overideals.

The 2025 Chapman--Paran article is the closest predecessor. Its public abstract and the exact statement of its Proposition 2.3 as reproduced in the cyclic-algebra paper were inspected; they concern existence of nonmaximal contractions. Full article text was not available for inspection, so a residual risk concerning an unindexed interval observation there is recorded in the review.

## Limitations
The result refines the specific splitting-field witnesses used in the centrally finite classification. It does not classify the overideal intervals of arbitrary Amitsur--Small counterexamples, nor does it address centrally infinite division rings. The projective-line structure is a consequence of the homogeneous semisimple quotient \(V\oplus V\); other counterexample constructions need not have that quotient.

The exact 2025 Chapman--Paran article could not be inspected in full. Its abstract and its central proposition as reproduced verbatim in later primary literature do not contain the present interval classification, but an uninspected remark remains a residual originality risk.

## References
1. E. Paran, “Characterization of the centrally finite Amitsur-Small division rings,” arXiv:2610.04317v1, 2026. Lemma 3.1, Lemma 3.2, Proposition 3.3, Theorem 1.1.
2. E. Paran, “On a problem of Amitsur and Small,” arXiv:2412.06230v1, 2024.
3. A. Chapman, I. Levin, M. Zaninelli, “Cyclic Division Algebras of Odd Prime Degree are never Amitsur-Small,” arXiv:2508.07451v2, 2026.
4. A. Chapman, E. Paran, “Amitsur-Small rings,” Journal of Algebra 679 (2025), 86–95, DOI 10.1016/j.jalgebra.2025.04.049.
