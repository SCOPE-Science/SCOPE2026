# Sharp crossing-number envelope for canonical torus-knot component sizes

## Finding
For the canonical layered triangulation of a positive torus knot in the construction of Lin and Spreer, fix the two component sizes \(0\le u<v\), and write \(d=v-u\). Then the crossing number \(c\) satisfies the sharp bounds
\[
d(u+2)^2\le c\le F_{u+3}\bigl(dF_{u+3}+F_{u+2}-1\bigr),
\]
where \(F_0=0\), \(F_1=1\), and \(F_{j+1}=F_j+F_{j-1}\). The lower bound is attained uniquely by
\[
T\bigl(u+2,d(u+2)+1\bigr),
\]
and the upper bound is attained uniquely by
\[
T\bigl(F_{u+3},dF_{u+3}+F_{u+2}\bigr).
\]

Consequently, among all positive torus-knot types of a fixed total canonical size \(n=u+v\), the largest crossing number occurs for the most balanced admissible component sizes. For \(n\ge4\) the maximizer is unique. More explicitly, if \(n=2m-1\ge5\), it is \(T(F_{m+2},F_{m+3})\); if \(n=2m\ge4\), it is \(T(F_{m+2},F_{m+2}+F_{m+3})\). At \(n=3\) there is exactly one tie, between \(T(2,7)\) and \(T(3,5)\), both of crossing number \(12\).

## Assumptions and scope
The statement concerns the positive-parameter torus-knot family \(T(P,Q)\) with \(2\le P<Q\) and \(\gcd(P,Q)=1\), using the canonical split and layered-solid-torus construction of Lin--Spreer. The component size of a positive coprime pair is its subtraction-Euclidean distance to \((1,1)\), so total canonical size is the sum of the two component sizes. No claim is made that this canonical size always equals minimal triangulation complexity.

The argument also uses the determinant-one matrix description of the canonical split. For ordered component sizes \((u,v)\) with \(u<v\), the relevant positive determinant-one matrices form a depth-\(u\) binary tree above the boundary matrix
\[
B_d=\begin{pmatrix}1&1\\ d&d+1\end{pmatrix},\qquad d=v-u.
\]
This binary-tree parametrization is the same one underlying the exact component-size census already recorded in published-finding corpus.

## Proof
Let the two column-addition generators act on the right of \(B_d\). After exactly \(u\) additions, write
\[
W\binom11=\binom ab.
\]
Starting from \((1,1)\), each step sends \((a,b)\) to one of
\[
(a+b,b),\qquad (a,a+b).
\]
Every depth-\(u\) pair occurs exactly once. Multiplying \(B_dW\) by \((1,1)^T\) gives its two row sums, hence the torus-knot parameters
\[
P=a+b,\qquad Q=d(a+b)+b=dP+b.
\]
Because \(d\ge1\) and \(b\ge1\), one has \(Q>P\). The standard crossing-number formula for a torus knot therefore becomes
\[
c(T(P,Q))=P(Q-1)=P(dP+b-1).
\]

For the lower bound, each addition increases \(a+b\) by at least one, so after \(u\) steps
\[
P=a+b\ge u+2.
\]
Also \(b\ge1\). Hence
\[
c=P(dP+b-1)\ge dP^2\ge d(u+2)^2.
\]
Equality forces \(P=u+2\) and \(b=1\). The only depth-\(u\) pair with these two properties is \((a,b)=(u+1,1)\). Thus the lower extremizer is uniquely
\[
(P,Q)=\bigl(u+2,d(u+2)+1\bigr).
\]

For the upper bound, the elementary Fibonacci extremal property of the additive tree gives, at depth \(u\),
\[
a+b\le F_{u+3},\qquad a\le F_{u+2},\qquad b\le F_{u+2}.
\]
These bounds follow simultaneously by induction from the two child maps above. Equality in the sum bound occurs only for the two consecutive-Fibonacci orientations
\[
(F_{u+1},F_{u+2})\quad\text{and}\quad(F_{u+2},F_{u+1}).
\]
Since \(P(dP+b-1)\) is strictly increasing in both \(P\) and \(b\),
\[
c\le F_{u+3}\bigl(dF_{u+3}+F_{u+2}-1\bigr).
\]
The simultaneous maximizing pair is uniquely \((a,b)=(F_{u+1},F_{u+2})\), yielding
\[
(P,Q)=\bigl(F_{u+3},dF_{u+3}+F_{u+2}\bigr).
\]

It remains to maximize over component pairs with fixed total size \(n=u+v\). Put \(d=n-2u\), \(A=F_{u+3}\), and \(B=F_{u+2}\). The pairwise maximum is
\[
M_u=A(dA+B-1).
\]
A direct Fibonacci simplification gives
\[
M_{u+1}-M_u=-A^2+(2d-4)AB+(d-2)B^2-B.
\]
For \(d\ge4\) this is positive. For the final possible comparison, \(d=3\), write \(A=B+C\) with \(C=F_{u+1}\); the difference becomes
\[
2B^2-C^2-B,
\]
which is zero only for \(u=0\) and positive for \(u\ge1\). Therefore the maximum occurs at the largest admissible \(u=\lfloor(n-1)/2\rfloor\), uniquely except at \(n=3\). Substitution gives the stated odd- and even-size extremizers.

## Verification
The standalone script `artifacts/verify_crossing_envelope.py` uses exact integer arithmetic only. It independently generates the depth-\(u\) additive tree, reconstructs every corresponding torus-knot parameter pair, recomputes the canonical split and subtraction lengths, and checks both sharp formulas and uniqueness for \(0\le u\le12\), \(u<v\le14\). It also checks the fixed-total-size maximizers for \(1\le n\le24\). Its recorded successful output is:

`VERIFY_OK pairwise u<=12,v<=14 and global n<=24`

These finite checks are reproducibility evidence, not a substitute for the proof above.

## Relationship to prior work
Lin--Spreer prove existence and uniqueness of the positive split, identify the canonical tetrahedron count with two subtraction-Euclidean lengths, and emphasize the large gap between canonical triangulation size and crossing number. Their examples include both the linear family \(T(2,2k+1)\) and a consecutive-Fibonacci family with logarithmic canonical size relative to crossing number.

A prior published-finding corpus record gives the exact census of canonical component sizes: for each \(0\le u<v\), exactly \(2^u\) positive torus-knot types have component sizes \(\{u,v\}\). Its determinant-one binary-tree proof supplies the natural parametrization used here, but it does not state crossing-number bounds or identify crossing-number extremizers. The present result adds a sharp statistic on every one of those finite component-size fibers and then solves the fixed-total-size extremal problem.

Earlier work on converting triangulations to diagrams exhibits Fibonacci torus knots as a family with linearly many tetrahedra and exponentially growing crossing number. That establishes the qualitative phenomenon for one family; it does not give the exact fixed-component envelope above.

## Limitations
The bounds are for the Lin--Spreer canonical layered construction and its component-size statistic. They do not prove corresponding sharp bounds in terms of the minimal triangulation complexity of a torus knot, because equality between canonical size and minimal complexity remains conjectural in the motivating preprint. The motivating preprint is recent, so later or unindexed parallel work remains a residual originality risk.

## References
1. Lezhi Lin and Jonathan Spreer, *Torus knots as loop-edges in three-sphere triangulations*, arXiv:2609.14200v1 (2026), especially Proposition 4.3, Corollary 4.4, Example 4.5, Figure 6, and Conjecture 5.1. https://arxiv.org/abs/2609.14200
2. *Exact canonical-size census for layered torus-knot triangulations*, published-finding corpus record `2026/9/18/SCOPE-exact-canonical-torus-knot-triangulation-census--831655b0b665` (2026).
3. *Computing a Link Diagram From Its Exterior*, Theorem 9.1, full text at PubMed Central record PMC10771428.
4. Lin--Spreer companion source notebook, `tk_build_split.ipynb`. https://github.com/HimalayanRainstorm/TorusKnots
