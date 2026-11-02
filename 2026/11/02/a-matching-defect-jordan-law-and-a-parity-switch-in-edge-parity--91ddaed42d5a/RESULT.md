# A matching-defect Jordan law and a parity switch in edge-parity networks

## Finding

Let \(n\ge3\), \(0\le k\le\lfloor n/2\rfloor\), and let \(G_{n,k}\) be the complete graph on \(n\) labelled vertices with an arbitrary matching of \(k\) edges deleted. Write \(E=\binom n2-k\). For any finite field \(\mathbb F_q\) of characteristic two, put one field value on each remaining edge and update it synchronously to the sum of the values on the *other* edges sharing an endpoint. Thus the update matrix \(F\) is the loopless adjacency matrix of \(L(G_{n,k})\), over \(\mathbb F_q\).

**Complete Jordan classification.** For odd \(n\), the Jordan form is
\[
F\sim J_1(0)^{\oplus(E-n+1)}\oplus J_2(1)^{\oplus k}\oplus J_1(1)^{\oplus(n-1-2k)}.
\]
In particular \(F^3=F\): every state is periodic after at most one update, with eventual period one or two. Exactly \(q^{n-1-k}\) states are fixed, and there are exactly
\[
\frac{q^{n-1}-q^{n-1-k}}{2}
\]
primitive two-cycle orbits. Each fixed point has an attraction basin of cardinality \(q^{E-n+1}\), and each primitive two-cycle has a basin of cardinality \(2q^{E-n+1}\). The fractions of uniformly random starting states that eventually enter periods one and two are respectively \(q^{-k}\) and \(1-q^{-k}\). Initially periodic states number \(q^{n-1}\), and the other \(q^E-q^{n-1}\) states first become periodic after one update.

For even \(n=2m\ge4\), define
\[
r_{n,k}=\begin{cases}
k,&0\le k<m,\\
m-1-\mathbf1_{\{m\text{ even}\}},&k=m.
\end{cases}
\]
Then
\[
F\sim J_3(0)^{\oplus r_{n,k}}\oplus
J_2(0)^{\oplus(n-2-2r_{n,k})}\oplus
J_1(0)^{\oplus(E-2n+4+r_{n,k})}.
\]
Every state reaches zero within at most three updates: \(F^3=0\). The exact numbers first reaching zero at times \(0,1,2,3\) are, in order,
\[
1,\qquad q^{E-n+2}-1,\qquad
q^{E-r_{n,k}}-q^{E-n+2},\qquad q^E-q^{E-r_{n,k}}.
\]
The maximum is three except when \(k=0\) or \((n,k)=(4,2)\), in which case it is two.

**A nonmonotone final deletion.** For even \(n=2m\), the rank of the second iterate is \(k\) throughout \(0\le k<m\). Deleting the final disjoint edge changes this rank from \(m-1\) to \(m-2\) when \(m\) is even, but leaves it at \(m-1\) when \(m\) is odd. Thus, at every order divisible by four, adding the last matching defect *reduces* the number of independent three-step relaxation modes. At odd graph orders, by contrast, a single matching defect already creates nontrivial period-two orbits.

## Assumptions and scope

All graphs are finite, simple, undirected, and labelled. The graph \(G_{n,k}\) is connected for the stated parameter range, including the smallest boundary examples. The local rule excludes the edge's own current state: no self-loop is used in the line graph. The field cardinality \(q\) is an arbitrary positive power of two; the matrix and its Jordan forms are interpreted over that field, not over the real numbers. An attraction basin includes the periodic states themselves. An initial state first reaches its periodic orbit at time \(T=0\) precisely when it is periodic already. \(J_s(\lambda)\) denotes a single size-\(s\) Jordan block with eigenvalue \(\lambda\). Graphs arising from different choices of the deleted matching are isomorphic, so all counts are independent of that choice.

## Proof

**Incidence reduction.** Let \(B\) be the unoriented vertex-edge incidence matrix of \(G_{n,k}\), with \(n\) rows and \(E\) columns, over \(\mathbb F_q\). Every column has exactly two ones. Two different columns have inner product one exactly when their edges meet. Consequently
\[
F=B^{\mathsf T}B,\qquad H=BB^{\mathsf T}=D+A_G,
\]
where \(D\) is the degree-parity diagonal matrix and \(A_G\) the adjacency matrix of \(G_{n,k}\). Since \(G_{n,k}\) is connected, \(B\) has rank \(n-1\), its image is
\[
W=\{z\in\mathbb F_q^n:\sum_i z_i=0\},
\]
and \(\ker B^{\mathsf T}=\langle\mathbf1\rangle\). For every integer \(j\ge1\),
\[
F^j=B^{\mathsf T}H^{j-1}B.
\]

Label the deleted edges as \((0,1),(2,3),\ldots,(2k-2,2k-1)\). In characteristic two, removing an edge adds its adjacency indicator. Writing \(J\) for the all-ones vertex matrix, the root adjacency matrix is \(A_G=J+I+P\), where \(P\) is adjacency of the deleted matching. Since \(Jz=0\) for every \(z\in W\), only \(H\vert_W\) matters.

**Odd order.** When \(n\) is odd, matched vertices have odd degree \(n-2\) and unmatched vertices even degree \(n-1\). Hence on \(W\), the matrix \(H\) is the permutation \(R\) that swaps the two coordinates of each deleted pair and fixes each unpaired coordinate. In particular \(R^2=I\), proving \(F^3=F\). Because \(\sum_i\mathbf1_i=1\ne0\) for odd \(n\), \(B^{\mathsf T}\) is injective on \(W\). It therefore identifies \(\operatorname{im}F=B^{\mathsf T}W\), of dimension \(n-1\), with the involution \(R\vert_W\).

On each paired coordinate block, \(I+R\) maps \((s,t)\) to \((s+t,s+t)\); it vanishes on unmatched vertices. There is at least one unmatched vertex because \(n\) is odd. Therefore, for arbitrary prescribed pair sums, one can choose an unmatched coordinate to enforce the single even-sum constraint defining \(W\). Thus \(\operatorname{rank}((I+R)\vert_W)=k\), and \((I+R)^2=0\). The involution has exactly \(k\) size-two Jordan blocks at eigenvalue one and \(n-1-2k\) size-one blocks there. The identity \(F^3=F\) makes the zero-primary component semisimple, of dimension \(E-n+1\). This proves the odd-order Jordan form.

All periodic states are precisely \(\operatorname{im}F\), with \(q^{n-1}\) elements. The fixed subspace has dimension \(n-1-k\). Subtracting fixed configurations and dividing by two gives the primitive two-cycle orbit count. The map \(F:\mathbb F_q^E\to\operatorname{im}F\) is surjective, and each fiber has \(q^{E-n+1}\) elements. Its restriction to its image is invertible, so each recurrent phase has this same number of initial predecessors. The basin and first-entry formulas follow.

**Even order.** When \(n=2m\) is even, matched vertices have even degree \(n-2\), while unmatched vertices have odd degree \(n-1\). On \(W\), the matrix \(H\) is the linear operator \(R\) whose matched-pair blocks are the two-by-two all-ones matrix and whose unmatched-coordinate blocks vanish. Thus \(R^2=0\) and \(F^3=0\). Because \(\mathbf1\in W\) now, the map \(B^{\mathsf T}\vert_W\) has a one-dimensional kernel; hence \(\operatorname{rank}F=n-2\).

For a vector in \(W\), let \(t_i\) be the sum of its two coordinates on the \(i\)-th deleted pair. The image \(RW\) consists of vectors having value \(t_i\) at both ends of that pair and zero at all unmatched vertices. If \(k<m\), at least two unmatched vertices remain. One of their values may be chosen to enforce \(\sum z_i=0\), so all \(k\) pair sums are independent. Consequently \(\dim RW=k\), and \(\mathbf1\notin RW\) because it is nonzero on the unmatched coordinates. Thus \(\operatorname{rank}F^2=k\).

If \(k=m\), there are no unmatched vertices; membership in \(W\) enforces \(\sum_{i=1}^m t_i=0\). Therefore \(\dim RW=m-1\). The constant vector \(\mathbf1\) lies in \(RW\) if and only if \(m\) is even. Since \(\ker B^{\mathsf T}\vert_W=\langle\mathbf1\rangle\), it follows that \(\operatorname{rank}F^2=m-1-\mathbf1_{\{m\text{ even}\}}\). This proves the second-iterate rank formula.

For a nilpotent linear operator of index at most three with ranks \(\operatorname{rank}F=n-2\), \(\operatorname{rank}F^2=r_{n,k}\), the numbers of size-three, size-two and size-one Jordan blocks are respectively \(r_{n,k}\), \(n-2-2r_{n,k}\), and \(E-2n+4+r_{n,k}\). Finally, \(\ker F\subseteq\ker F^2\subseteq\ker F^3\) have cardinalities \(q^{E-n+2}\), \(q^{E-r_{n,k}}\), and \(q^E\); their successive differences give the first-zero-entry distribution. A three-step state exists exactly when \(r_{n,k}>0\), establishing the sharpness exceptions and the final-deletion discontinuity. This completes the proof.

## Verification

Two standalone executable verifiers accompany this result. `rank_verifier.py` computes the actual binary adjacency matrices, their first three powers, and Gaussian-elimination ranks for all \(77\) parameter pairs with \(3\le n\le16\). It also checks \(\operatorname{rank}(F+F^2)=k\) at odd orders. `independent_enumeration.cpp` independently constructs the graph adjacency and evolves all \(3{,}995{,}516\) binary initial states over \(16\) graph instances with \(3\le n\le7\). It verifies the exact eventual-period and first-entry counts. The included outputs record successful executions. Both programs verify examples and identities for finite parameters; the proof above covers all \(n\), all allowed \(k\), and every finite field of characteristic two.

For reproduction, run `python3 rank_verifier.py` and compile `independent_enumeration.cpp` with a C++17 compiler using optimization, then execute the resulting program. No third-party package is required.

## Relationship to prior work

The incidence identity and its connection to line graphs are classical. Davis, Domke and Garner analyzed ordinary (real) adjacency ranks of line graphs of regular graphs, including complete and cocktail-party graphs; that is not a characteristic-two Jordan census, and their regular root family does not cover all partial-matching deletions. Abudayah, Alomari and Sander examine incidence-line-graph identities and mixed orientations, not the present finite-field dynamics. Ciandrini and collaborators study synchronous XOR Boolean networks and general linear attractor behavior, without the parameter-dependent Jordan forms on these particular line graphs. These known results motivate and supply background, not the explicit formulas above.

Other exact edge-parity classifications on Boolean cubes and Hamming-product line graphs share the update rule but treat different root graph families. Their conclusions do not imply the matching-deletion parameter law: the rank drop at a perfect matching depends on how the deleted pairs intersect the even-coordinate subspace. No claim is made that the general incidence method or the general linear-fiber formula is new.

## Limitations

The theorem concerns synchronous edge-neighbor sums over characteristic-two fields only. It does not cover real-valued adjacency dynamics, nonlinear threshold rules, arbitrary edge-deletion sets, asynchronous updates, or graphs with loops. The exact classification is proved algebraically without external formal certification. Exhaustive finite checks alone do not prove the infinite-family conclusion. Historical-priority searches can miss unindexed or inaccessible equivalent classifications, and the absence of such a match is not itself a proof of priority.

## References

1. G. J. Davis, G. S. Domke and C. R. Garner, Jr., “Ranks of Line Graphs of Regular Graphs,” *Journal of Combinatorial Mathematics and Combinatorial Computing* **49** (2004), 113–128. Publisher record: https://combinatorialpress.com/jcmcc-articles/volume-049/ranks-of-line-graphs-of-regular-graphs/ (listed publication date 2004-05-31); accessible PDF at the publisher.
2. L. Ciandrini, C. Maffi, A. Motta, B. Bassetti and M. Cosentino Lagomarsino, “Feedback topology and XOR-dynamics in Boolean networks with varying input structure,” arXiv:0809.1526v1 (2008-09-09), https://arxiv.org/abs/0809.1526.
3. M. Abudayah, O. Alomari and T. Sander, “Incidence matrices and line graphs of mixed graphs,” arXiv:2205.05375v1 (2022-05-11), https://arxiv.org/html/2205.05375v1.
