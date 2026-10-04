# The dimension-two finite-field case of the nilpotent-free duality conjecture

## Finding
Let \(F\) be a finite field. There is a three-dimensional subspace \(W\leq M_2(F)\) whose only nilpotent element is \(0\). Since
\[
3=2^2-\binom{2}{2},
\]
this proves the \(n=2\) case of Conjecture 8 in Wigderson's recent matrix-space duality paper.

More explicitly, let \(K/F\) be the quadratic extension and let \(\sigma\) be its nontrivial \(F\)-automorphism. For \(a\in K\), write \(L_a\) for multiplication by \(a\) on the two-dimensional \(F\)-space \(K\), and put
\[
U=\{L_a\circ\sigma:a\in K\}\subseteq\operatorname{End}_F(K)\cong M_2(F).
\]
Then \(\dim_F U=2\), every nonzero element of \(U\) is invertible, and \(U\) lies in the trace-zero hyperplane. Hence, if \(E\in M_2(F)\) has \(\operatorname{tr}(E)=1\), then
\[
W=U\oplus FE
\]
has dimension three and contains no nonzero nilpotent matrix.

## Assumptions and scope
The proof applies to every field admitting a separable quadratic extension; finite fields satisfy this because \(\mathbb F_{q^2}/\mathbb F_q\) is separable. The stated consequence is only the \(n=2\) case of the conjecture. No claim is made for \(n\geq3\), nor for the stronger Atkinson-type problems discussed in the source.

## Proof
The map \(a\mapsto L_a\circ\sigma\) is \(F\)-linear and injective: if \(a\neq0\), then both \(L_a\) and \(\sigma\) are invertible. Therefore \(U\) is two-dimensional and every nonzero element of \(U\) is invertible.

Fix \(a\in K\) and set \(T=L_a\circ\sigma\). Since \(\sigma^2=1\),
\[
T^2=L_{a\sigma(a)}=N_{K/F}(a)I.
\]
If \(a\neq0\), then \(T\) is not scalar. Indeed, if \(L_a\circ\sigma=cI\), applying both sides to \(1\) gives \(a=c\in F^\times\), and cancellation would force \(\sigma=1\), a contradiction. Cayley--Hamilton in dimension two gives
\[
T^2-\operatorname{tr}(T)T+\det(T)I=0.
\]
Combining this with \(T^2=N_{K/F}(a)I\) yields a linear relation between \(I\) and \(T\). Because these are linearly independent for \(a\neq0\), its \(T\)-coefficient must vanish, so \(\operatorname{tr}(T)=0\). The same conclusion is immediate for \(a=0\). Thus \(U\subseteq\ker(\operatorname{tr})\).

Choose a coordinate basis of \(K\) over \(F\) and let \(E\) be the projection onto the first coordinate, so \(\operatorname{tr}(E)=1\). Therefore \(E\notin U\), and \(W=U\oplus FE\) has dimension three. If \(X=u+cE\in W\) is nilpotent, then \(\operatorname{tr}(X)=0\). Since \(\operatorname{tr}(u)=0\) and \(\operatorname{tr}(E)=1\), this forces \(c=0\). Thus \(X=u\in U\). A nonzero element of \(U\) is invertible, so it cannot be nilpotent. Hence \(X=0\).

## Verification
The proof is characteristic-free once a separable quadratic extension is available. For a concrete coordinate check, when \(q\) is odd choose a nonsquare \(d\in\mathbb F_q\); one obtains
\[
U=\left\{\begin{pmatrix}x&-dy\\y&-x\end{pmatrix}:x,y\in\mathbb F_q\right\},
\]
whose nonzero determinants are protected by anisotropy of \(x^2-dy^2\). In characteristic two, choose \(d\) so that \(X^2+X+d\) is irreducible; then
\[
U=\left\{\begin{pmatrix}x&x+dy\\y&x\end{pmatrix}:x,y\in\mathbb F_q\right\}.
\]
The accompanying checker exhausts every element of \(W\) for \(q=2,3,4,5,7,11,13\) and verifies that the simultaneous equations \(\operatorname{tr}(X)=0\) and \(\det(X)=0\), which characterize nilpotence for \(2\times2\) matrices, have only the zero solution inside \(W\). The finite computation is a sanity check; the proof above establishes the result for all finite fields.

## Relationship to prior work
Wigderson's arXiv:2609.29177v1 states the Gerstenhaber--Serezhkin nilpotent-space bound and asks in Conjecture 8 whether, over every finite field, there is a complementary matrix space of dimension \(n^2-\binom{n}{2}\) containing no nonzero nilpotent. The paper explicitly says that such a construction is unclear over finite fields. Its Proposition 9 constructs \(n\)-dimensional totally nonsingular spaces from degree-\(n\) field extensions; for \(n=2\), that gives dimension two, whereas Conjecture 8 requires dimension three. The present construction uses the same quadratic extension but twists multiplication by the nontrivial Galois automorphism to place a two-dimensional invertible subspace inside the trace-zero hyperplane, allowing one further trace-transverse dimension.

Searches for the exact \(2\times2\) finite-field statement, nilpotent-free three-dimensional matrix spaces, and equivalent formulations did not locate a statement implying this construction. The closest located records concerned anisotropic adjoint forms, double-transvection commutators, and rank-three fooling-set matrices; none gives a three-dimensional nilpotent-free subspace of \(M_2(\mathbb F_q)\). This is evidence against direct coverage, not an exhaustive proof of novelty.

## Limitations
The result settles only the first nontrivial dimension \(n=2\). It does not provide a pattern for \(n\geq3\). A residual bibliographic risk remains that an equivalent \(2\times2\) observation appears in older matrix-space or quadratic-form literature under different terminology. The accompanying finite computations do not replace the general proof.

## References
1. Yuval Wigderson, *Duality for matrix space questions*, arXiv:2609.29177v1, submitted 2026-09-24.
2. Murray Gerstenhaber, *On nilalgebras and linear varieties of nilpotent matrices. I*, American Journal of Mathematics 80 (1958), 614--622.
3. V. N. Serezhkin, *Linear transformations preserving nilpotency* (1985), cited in arXiv:2609.29177v1 for the arbitrary-field nilpotent-space theorem.
