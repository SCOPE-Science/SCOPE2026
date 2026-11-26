# Four-cycle control of the endpoint commutator of two conditional expectations

## Finding
Let \(G=(U\sqcup V,E)\) be a nonempty finite simple \(d\)-regular bipartite graph, with \(d\ge2\), and put uniform probability measure on its edges. Let \(P\) and \(Q\) be conditional expectation onto the \(U\)- and \(V\)-endpoints, respectively. For an edge \(e\), let \(c_4(e)\) count the simple unoriented four-cycles containing it, and set \(c_*=\min_{e\in E}c_4(e)\). For \(C=PQ-QP\),
\[
\|C\|_{\infty\to\infty}=\|C\|_{1\to1}=\frac{2((d-1)^2-c_*)}{d^2}.
\]
The \(L^\infty\) norm is attained by a sign-valued input; the \(L^1\) norm is attained by an input supported on one edge, and need not be attained by a sign-valued input. The sharp upper bound at fixed \(d\) is \(2(1-1/d)^2\), with equality exactly when some edge lies in no four-cycle. The commutator vanishes exactly when every component is \(K_{d,d}\).

For the point-line incidence graph of a finite projective plane of prime-power order \(q\ge2\), the same commutator has
\[
\|C_q\|_{1\to1}=\|C_q\|_{\infty\to\infty}=\frac{2q^2}{(q+1)^2},\qquad
\|C_q\|_{2\to2}=\frac{\sqrt{q(q^2+q+1)}}{(q+1)^2}.
\]
Thus the endpoint norms tend to \(2\), while the Hilbert norm tends to zero at order \(q^{-1/2}\).

## Assumptions and scope
Both sides of the graph have common degree \(d\); the graph need not be connected. Each edge has mass \(1/|E|\), so induced \(L^1\) and \(L^\infty\) norms are the usual absolute column- and row-sum norms. An edge sign function takes values in \(\{-1,1\}\) on every edge. No weighted or irregular extension is asserted.

## Proof
**Endpoint norms.** For an output edge \(e=(u,v)\) and an input edge \(f=(a,b)\), expanding the two averages gives
\[
C_{ef}=d^{-2}\big(\mathbf1_{b\in N(u)}-\mathbf1_{a\in N(v)}\big).
\]
Swapping \(e\) and \(f\) negates this entry. The two indicated sets of input edges each have size \(d^2\). Their intersection consists of the edges from \(N(v)\) to \(N(u)\). Of these, \(2d-1\) are incident with \(u\) or \(v\), and each of the rest closes exactly one simple four-cycle through \(e\), and conversely. Thus the absolute row sum is \(2(d^2-2d+1-c_4(e))/d^2\). The maximum gives the \(L^\infty\) norm and, by skew-symmetry, the \(L^1\) norm. Taking the signs of a maximizing row, with arbitrary signs where it is zero, attains the \(L^\infty\) norm. A point mass at a maximizing column attains the \(L^1\) operator norm after normalization.

For the distinction, take the ordinary six-cycle with its alternating bipartition and label the edges \(e_j\) in cyclic order, \(j\bmod 6\). Row \(j\) of \(4C\) has a \(+1\) and a \(-1\) on the two edges \(e_{j-2},e_{j+2}\) and zeros elsewhere, so \(\lvert(Cf)(e_j)\rvert=\lvert f(e_{j-2})-f(e_{j+2})\rvert/4\). Within each parity class of three indices, at most two of the three pairwise sign differences can be nonzero. Hence any sign input has \(\|f\|_1=1\) and \(\|Cf\|_1\le 1/3<1/2=\|C\|_{1\to1}\).

**Equality and sharpness.** For each edge, \(c_4(e)\le (d-1)^2\), since a four-cycle is fixed by the choice of a second neighbor at each endpoint. Upper equality occurs just when \(c_*=0\). For each \(d\), choose a prime \(q\ge d-1\) and the projective plane over \(\mathbb F_q\). Its incidence graph has degree \(q+1\) and no four-cycles. Hall's theorem, iterated on the residual regular bipartite graph, gives a partition of its edges into \(q+1\) perfect matchings. The union of any \(d\) of these is an admissible graph with no four-cycles. If \(C=0\), then all edges satisfy \(c_4(e)=(d-1)^2\), so for any edge \((u,v)\) the bipartite graph between \(N(v)\) and \(N(u)\) is complete. Every one of those vertices already has degree \(d\) within these two sets, giving a whole connected component \(K_{d,d}\). The converse follows from the row formula.

**Hilbert norm for projective planes.** Let \(A\) be the point-line incidence matrix, with \(q^2+q+1\) rows and columns and common row and column sum \(d=q+1\). Since two distinct points have just one common line, \(AA^{\mathsf T}=qI+J\). The cross-Gram matrix of the two endpoint subspaces in normalized indicator bases is \(A/d\). Its singular value 1 is the shared constant direction; on the complements all singular values are \(s=\sqrt q/(q+1)\). A pair of corresponding principal unit vectors spans a two-dimensional block, in which the two projections have matrices \(\operatorname{diag}(1,0)\) and \(ww^{\mathsf T}\) with \(w=(s,\sqrt{1-s^2})^{\mathsf T}\). Their commutator has norm \(s\sqrt{1-s^2}\); the shared and remaining orthogonal directions contribute zero. Substitution gives the claimed exact Hilbert norm. The incidence graph has no four-cycles, giving the endpoint norm and both limits.

## Verification
The accompanying `verify.py` checks the integer-scaled row-sum identity on eight examples, checks the entries against explicit matrix composition when there are at most 60 edges, and checks the projective-plane incidence Gram identity for prime orders 2, 3 and 5. The finite checks supplement, but do not establish, the universal theorem or the sign-input distinction; the six-cycle calculation above proves that distinction directly.

## Relationship to prior work and limitations
The two-projection Hilbert calculation and incidence Gram identity use classical tools. Walters addresses Hilbert-space commutator bounds and anticommutator norms; Abiad–Dalfó–Fiol characterize regularity properties of bipartite graphs algebraically. The claim here is the exact graph-dependent endpoint norm and sharp equality cases, together with an explicit same-operator separation from the Hilbert norm. No priority certification, classification of all separating graph families, or claim about nonuniform edge measures is made.

## References
- A. Abiad, C. Dalfó and M. A. Fiol, *Algebraic characterizations of regularity properties in bipartite graphs*, https://arxiv.org/abs/1205.5913.
- S. Walters, *Anticommutator Norm Formula for Projection Operators*, https://arxiv.org/abs/1604.00699.
- P. R. Halmos, *Two subspaces*, Trans. Amer. Math. Soc. 144 (1969), 381–389.
