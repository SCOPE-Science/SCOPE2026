# Exact cardinality recurrence for mapping spaces between finite weak orders

## Finding
Let \(P=A_1\oplus\cdots\oplus A_h\) and \(Q=B_1\oplus\cdots\oplus B_k\) be nonempty finite weak-order \(T_0\)-spaces, with \(|A_i|=r_i\ge1\) and \(|B_j|=q_j\ge1\). Put \(Q_0=0\) and \(Q_j=\sum_{t=1}^j q_t\). For \(r\ge1\) and \(x\ge0\), define
\[
a_j(r,x)=q_j\big((x+1)^r-x^r\big),\qquad
b_j(r,x)=(x+q_j)^r-x^r-a_j(r,x).
\]
Define two state counts \(S_j^{(i)}\) and \(M_j^{(i)}\): among order-preserving maps from the first \(i\) source levels, \(S_j^{(i)}\) counts those whose \(i\)-th source level has maximum occupied target level \(j\) and occupies exactly one point of \(B_j\), while \(M_j^{(i)}\) counts those occupying at least two points of \(B_j\). Initialize
\[
S_j^{(1)}=a_j(r_1,Q_{j-1}),\qquad M_j^{(1)}=b_j(r_1,Q_{j-1}).
\]
For \(i\ge2\) and \(1\le j\le k\), write \(x_{u,j}=Q_{j-1}-Q_u\) for \(u<j\). Then
\[
S_j^{(i)}=S_j^{(i-1)}+\sum_{u<j}\left(M_u^{(i-1)}a_j(r_i,x_{u,j})+S_u^{(i-1)}a_j(r_i,x_{u,j}+1)\right),
\]
\[
M_j^{(i)}=\sum_{u<j}\left(M_u^{(i-1)}b_j(r_i,x_{u,j})+S_u^{(i-1)}b_j(r_i,x_{u,j}+1)\right).
\]
Consequently,
\[
|\operatorname{Map}(P,Q)|=\sum_{j=1}^k\left(S_j^{(h)}+M_j^{(h)}\right).
\]
Thus the exact number of continuous maps between arbitrary finite weak orders is computed by \(2k\) transfer states and \(O(hk^2)\) integer-arithmetic transitions.

## Assumptions and scope
A finite weak order is written as an ordinal sum of nonempty antichains. Thus every point of \(A_i\) is below every point of \(A_{i'}\) when \(i<i'\), and distinct points within one level are incomparable; similarly for \(Q\). Finite \(T_0\)-spaces are regarded through their specialization orders, so continuous maps are exactly order-preserving maps. The theorem allows singleton levels and arbitrary heights \(h,k\ge1\).

The state \(S_j^{(i)}\) remembers that the image of the current source level has top target level \(j\) and uses exactly one point there. The state \(M_j^{(i)}\) remembers the same top level but at least two distinct top-level points. No other information about the image of earlier levels is needed.

## Proof
Fix an order-preserving map on the first \(i-1\) source levels and let \(u\) be the maximum target level occupied by \(A_{i-1}\). Every image of an earlier source level lies below every image of \(A_{i-1}\), so the allowed images of a point in \(A_i\) are exactly the common upper bounds of the image of \(A_{i-1}\).

If that image occupies at least two distinct points of \(B_u\), then no point of \(B_u\) is above both of them, because \(B_u\) is an antichain. Hence its common upper bounds are precisely the points in \(B_{u+1}\cup\cdots\cup B_k\).

If instead the image occupies exactly one point \(v\in B_u\) at its top level, then \(v\) itself is also a common upper bound, and the complete set of common upper bounds is
\[
\{v\}\cup B_{u+1}\cup\cdots\cup B_k.
\]
This proves that the pair consisting of the top occupied level and the singleton-versus-multiple flag is a sufficient transfer state.

Now fix a new top target level \(j>u\). If there are \(x\) allowed points strictly below \(B_j\), an arbitrary function from the \(r_i\)-point antichain \(A_i\) to those \(x\) points together with \(B_j\) is order-preserving relative to the previous prefix. The number whose top occupied level is \(j\) and that use exactly one distinct point of \(B_j\) is
\[
q_j\big((x+1)^{r_i}-x^{r_i}\big)=a_j(r_i,x):
\]
choose the unique top point, then use it at least once. The number that use at least two distinct points of \(B_j\) is the remaining
\[
(x+q_j)^{r_i}-x^{r_i}-a_j(r_i,x)=b_j(r_i,x).
\]

For a predecessor state \(M_u^{(i-1)}\), the allowed points below \(B_j\) are the levels strictly between \(u\) and \(j\), so their number is
\[
x_{u,j}=Q_{j-1}-Q_u.
\]
For a predecessor state \(S_u^{(i-1)}\), the unique point of \(B_u\) adds one more allowed point, giving \(x_{u,j}+1\). If the new maximum remains \(j=u\), this is possible only from \(S_j^{(i-1)}\), and every point of \(A_i\) must map to its distinguished point; this contributes exactly the carry term \(S_j^{(i-1)}\). Summing these mutually disjoint possibilities gives the displayed recurrence.

For \(i=1\), there is no lower-level constraint. Taking \(x=Q_{j-1}\) gives the initialization. Every map ends in exactly one state, so summing \(S_j^{(h)}+M_j^{(h)}\) over \(j\) gives \(|\operatorname{Map}(P,Q)|\).

## Verification
The accompanying `artifacts/verify.py` implements the recurrence independently of a brute-force enumerator of all functions. It checks every ordered pair of weak-order level compositions of total size at most four, for \(225\) source-target pairs, with zero mismatches. It also checks larger anchors:
\[
|\operatorname{Map}(W(2,2,2),W(2,2))|=44,\qquad
|\operatorname{Map}(W(2,2,2,2),W(2,2,2))|=738,
\]
and
\[
|\operatorname{Map}(W(3,2),W(2,3))|=143,\qquad
|\operatorname{Map}(W(2,1,2),W(1,2))|=17.
\]
These finite checks stress-test the formulas; the quantified theorem is established by the proof above, not by enumeration.

## Relationship to prior work
Barmak and Minian record the finite-space/order correspondence and the fact that a map between finite spaces is continuous exactly when it is order-preserving. Their work places this counting problem naturally in finite-space topology.

Pouzet and Zaguia describe finite weak orders as lexicographic sums of antichains (equivalently, complete multipartite orders) and study their endomorphisms in connection with perpendicular orders. The inspected structural results do not give a cardinality formula for all maps between two arbitrary weak orders or the two-state transfer recurrence above.

Published-record and literature searches were also made under the aliases “weak order”, “complete multipartite order”, “ordinal sum of antichains”, “order-preserving maps”, “endomorphism count”, and “mapping-space cardinality”. The closest located weak-order record concerns interval-endomorphism algebra dimensions rather than counts of order-preserving maps.

## Limitations
The recurrence counts the points of the finite mapping space; it does not determine its specialization order, beat-point core, homotopy type, component structure, or induced maps on homology. The arithmetic complexity statement counts transfer operations and treats integer exponentiation/arithmetic at the usual unit-operation level; bit complexity grows with the output integers. The originality comparison cannot exclude an equivalent recurrence hidden in unindexed enumeration literature.

## References
1. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156, first public version 2006-11-06; published in *Journal of Homotopy and Related Structures* 2 (2007), 127–140.
2. M. Pouzet and I. Zaguia, *Weak orders admitting a perpendicular linear order*, *Discrete Mathematics* 307 (2007), 97–107, DOI: 10.1016/j.disc.2006.05.038.
