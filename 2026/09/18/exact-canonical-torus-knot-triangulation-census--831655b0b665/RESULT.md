# Exact canonical-size census for layered torus-knot triangulations

## Statement

Let \(T(P,Q)\) be a nontrivial positive-parameter torus-knot type with \(2\le P<Q\) and \(\gcd(P,Q)=1\). Lin and Spreer associate to it a canonical layered one-vertex triangulation of \(S^3\): Proposition 4.3 gives positive integers \(p,q,r,s\), unique up to swapping the two columns, with
\[
P=p+q,\qquad Q=r+s,\qquad |ps-qr|=1,
\]
and Corollary 4.4 makes the tetrahedron count the sum of the subtraction-Euclidean lengths of \((p,q)\) and \((r,s)\).

Write \(\ell(a,b)\) for the number of subtraction steps needed to take a coprime positive pair \((a,b)\) to \((1,1)\). Thus \(\ell(1,1)=0\), and define the two canonical component sizes by
\[
\{u,v\}=\{\ell(p,q),\ell(r,s)\}.
\]

**Theorem.** For every pair of integers \(0\le u<v\), exactly
\[
\boxed{2^u}
\]
positive-parameter torus-knot types have canonical component sizes \(\{u,v\}\).

Consequently, if \(a_n\) denotes the number of such torus-knot types whose Lin--Spreer canonical triangulation has exactly \(n\) tetrahedra, then
\[
\boxed{a_n=2^{\lceil n/2\rceil}-1\qquad(n\ge1).}
\]
Equivalently,
\[
\sum_{n\ge1}a_n z^n=\frac{z}{(1-z)(1-2z^2)}.
\]
The cumulative number \(A_N=\sum_{n\le N}a_n\) is
\[
\boxed{
A_{2m}=2^{m+2}-2m-4,
\qquad
A_{2m-1}=3\cdot2^m-2m-3.
}
\]
In particular,
\[
A_{17}=1515,\qquad A_{19}=3049.
\]
The latter recovers exactly the cutoff count reported by Lin--Spreer, but now as a closed formula valid at every cutoff.

Since canonical size is an upper bound for actual triangulation complexity, the result also gives the unconditional lower bound \(A_N\) on the number of positive torus-knot types of triangulation complexity at most \(N\). In particular their number grows at least exponentially with base \(\sqrt2\) in the complexity cutoff. If Lin--Spreer Conjecture 5.1 holds, the same formulas become the exact census by triangulation complexity within the positive torus-knot family.

## Proof

Choose, for every ordered coprime pair \((P,Q)\) with \(P,Q\ge2\), the column ordering in Proposition 4.3 for which the determinant is \(+1\). The canonical split is then equivalent to a positive unimodular matrix
\[
M=\begin{pmatrix}p&q\\ r&s\end{pmatrix},
\qquad p,q,r,s>0,
\qquad ps-qr=1,
\]
whose row sums are \((P,Q)\). Conversely every such matrix has coprime row sums, because any common divisor of \(p+q\) and \(r+s\) divides
\[
p(r+s)-(p+q)r=ps-qr=1.
\]
Thus positive determinant-one matrices encode the ordered canonical splits exactly.

We first describe a unique reduction on these matrices. Suppose \(q>p\). Then necessarily \(s>r\): if \(s\le r\), positivity gives \(qr>pr\ge ps\), contradicting \(ps-qr=1\). Similarly, \(q<p\) forces \(s<r\). The only equality cases are
\[
q=p\Longrightarrow p=q=1,\ s=r+1,
\]
and
\[
s=r\Longrightarrow r=s=1,\ p=q+1.
\]
Hence every non-boundary positive determinant-one matrix has one column strictly larger than the other in both coordinates.

If the second column is larger, subtract the first column:
\[
\begin{pmatrix}p&q\\r&s\end{pmatrix}
\longmapsto
\begin{pmatrix}p&q-p\\r&s-r\end{pmatrix};
\]
if the first column is larger, subtract the second. Positivity and determinant one are preserved. Moreover the subtraction-Euclidean identity applies simultaneously to both rows, so both row lengths decrease by exactly one. Repeating therefore ends uniquely at one of the boundary matrices
\[
B_k=\begin{pmatrix}1&1\\ k&k+1\end{pmatrix},
\qquad
B'_k=\begin{pmatrix}k+1&k\\1&1\end{pmatrix}
\qquad(k\ge1),
\]
whose ordered row-length pairs are \((0,k)\) and \((k,0)\), respectively. In particular, equal row lengths never occur.

The inverse operation is binary. From a positive determinant-one matrix with columns \(c_1,c_2\), the two children are
\[
[c_1,c_1+c_2]
\qquad\text{and}\qquad
[c_1+c_2,c_2].
\]
Both are again positive determinant-one matrices, they are distinct, and each increases both row lengths by one. The preceding dominance argument shows that every non-boundary matrix has exactly one parent, so these children form genuine rooted binary trees.

Fix \(0\le u<v\). Any matrix with ordered row lengths \((u,v)\) must reduce to the unique root \(B_{v-u}\), and it lies exactly \(u\) binary generations below that root. Therefore there are exactly
\[
2^u
\]
positive determinant-one matrices with ordered row lengths \((u,v)\).

Finally, passing from ordered parameter pairs to torus-knot types does not change this count. The symmetry \(T(P,Q)=T(Q,P)\) sends the matrix \(M\) to
\[
JMJ=
\begin{pmatrix}s&r\\q&p\end{pmatrix},
\qquad
J=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]
which preserves determinant one and swaps the two row lengths. Because \(P=Q\) is impossible for coprime \(P,Q\ge2\), each torus-knot type has exactly one representative whose ordered row lengths satisfy \(u<v\). Thus the number of knot types with unordered component sizes \(\{u,v\}\) is exactly \(2^u\).

For total canonical size \(n=u+v\), sum over \(0\le u<v\):
\[
a_n=\sum_{u=0}^{\lfloor(n-1)/2\rfloor}2^u
=2^{\lceil n/2\rceil}-1.
\]
The generating function and cumulative formulas follow by summing this geometric progression. This proves the theorem. \(\square\)

## Reproducibility

`artifacts/verify_counts.py` uses only exact integer arithmetic and the Python standard library. It builds the binary matrix trees through canonical size 19, checks determinant one, row Euclidean lengths, coprimality and deduplication of the resulting torus-knot parameter pairs, and verifies
\[
(a_1,\ldots,a_{19})=(1,1,3,3,7,7,15,15,31,31,63,63,127,127,255,255,511,511,1023),
\]
with cumulative counts \(A_{17}=1515\) and \(A_{19}=3049\). The script was executed successfully on the published source.

## Relation to prior literature

Lin--Spreer prove the unique positive split and identify the canonical tetrahedron count with the two subtraction-Euclidean lengths. They report at least 3,049 torus knots with triangulation complexity at most 19 and their companion notebook computes the cutoff counts recursively through the Stern--Brocot tree, including checks at 17 and 19. Their paper does not state the all-size formula above or the refined \(2^u\) count for prescribed component sizes.

The binary-tree behavior of nonnegative unimodular matrices is classical: Nathanson records the standard fact that the two elementary generators freely generate \(SL_2(\mathbb N_0)\), in its Calkin--Wilf/Stern--Brocot interpretation. The contribution here is the coupling of that binary ancestry with the *simultaneous pair of Euclidean row lengths* arising in the Lin--Spreer canonical split, which yields the refined knot census and its closed forms.

## Limitations

This result enumerates the canonical Lin--Spreer constructions; it does not prove Conjecture 5.1 that canonical size equals the true triangulation complexity of every torus knot. Hence \(A_N\) is an unconditional lower bound, not an exact count, for torus knots of actual triangulation complexity at most \(N\). Mirrors are not counted separately: the convention is the positive-parameter family \(T(P,Q)\) with \(2\le P<Q\), matching the motivating paper's census. The source preprint is very recent, so unpublished or not-yet-indexed parallel work remains a residual originality risk.

## References

1. Lezhi Lin and Jonathan Spreer, *Torus knots as loop-edges in three-sphere triangulations*, arXiv:2609.14200v1 (2026), especially Proposition 4.3, Corollary 4.4, Figure 6, and Conjecture 5.1. https://arxiv.org/abs/2609.14200
2. Lin--Spreer companion code and Figure 6 data. https://github.com/HimalayanRainstorm/TorusKnots
3. Melvyn B. Nathanson, *Free monoids and forests of rational numbers*, Discrete Applied Mathematics 216 (2017), 662--669, DOI 10.1016/j.dam.2015.07.011.
