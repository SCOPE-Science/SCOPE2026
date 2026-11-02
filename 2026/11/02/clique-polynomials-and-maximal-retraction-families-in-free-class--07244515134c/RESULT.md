# Clique polynomials and maximal retraction families in free class-two Lie algebras

## Finding

Let \(F=\mathbb F_q\), let \(V\cong F^n\) with \(n\ge2\), and put \(W=\bigwedge^2_F V\), \(N=\binom n2\). On \(L=V\oplus W\) set \([v+w,v'+w']=v\wedge v'\); this is the free nilpotent Lie algebra of class two on \(n\) generators, including in characteristic two. An idempotent means a Lie-algebra endomorphism \(e\) satisfying \(e^2=e\).

For every \(k\ge0\), write \(\mathcal C_k=\{0,1\}^k\), with coordinatewise AND \(a\wedge_{\mathrm{bit}}b\). For a weak composition \(\mathbf n=(n_c)_{c\in\mathcal C_k}\) of \(n\), define
\[
w_c=\binom{n_c}{2}+\sum_{\substack{a<b\\ a\wedge_{\mathrm{bit}}b=c}}n_a n_b,
\qquad E(\mathbf n)=nN-\sum_c n_cw_c.
\]
Here \(a<b\) is any fixed total order on the binary patterns; the sum counts unordered pairs of **distinct** patterns once. Set \(g_j=|\operatorname{GL}_j(F)|=\prod_{h=0}^{j-1}(q^j-q^h)\), with \(g_0=1\). Then the number of ordered, pairwise-commuting \(k\)-tuples of idempotent Lie endomorphisms, **allowing repeated maps**, is
\[
\boxed{T_{n,k}=\sum_{\sum n_c=n}\frac{g_n}{\prod_c g_{n_c}}q^{E(\mathbf n)}.}\tag{1}
\]
Each summand also refines the joint linear ranks: if \(r_i=\sum_{c:c_i=1}n_c\), then the \(i\)-th map has rank \(r_i+\binom{r_i}{2}\). Multiplying the summand of (1) by \(\prod_{i=1}^k z_i^{r_i+\binom{r_i}{2}}\) gives the complete joint-rank enumerator. Thus (1) determines the whole clique polynomial via
\[
\boxed{c_j=\frac1{j!}\sum_{h=0}^j s(j,h)T_{n,h}\quad (0\le j\le2^n),}\tag{2}
\]
where \(c_j\) is the number of \(j\)-vertex cliques, \(c_0=1\), and \(s(j,h)\) denotes the signed Stirling numbers of the first kind.

All inclusion-maximal cliques have \(2^n\) vertices. They are exactly the Boolean families of all subset projections associated with an unordered decomposition of \(V\) into \(n\) lines, simultaneously conjugated by a single central shear. Their number is
\[
\boxed{M_{n,q}=q^{nN}\frac{g_n}{n!(q-1)^n}.}\tag{3}
\]
The tuple and maximal-family assertions (1)--(3), rather than the previously known classification of individual idempotent maps, are the contribution.

## Assumptions and scope

The assertions hold for every finite field \(F\) of order \(q\), including characteristic two, all integers \(n\ge2\), and every integer \(k\ge0\). The graph includes the zero and identity endomorphisms and all other idempotents; two **distinct** vertices are adjacent exactly when the endomorphisms commute. Equation (1) counts repetitions, while equation (2) removes them. The total order in the definition of \(w_c\) is an accounting convention only. For \(k=0\), the unique pattern has multiplicity \(n\) and (1) equals one. All exponents \(E(\mathbf n)\) are nonnegative integers.

## Proof

**Step 1: block form of a Lie endomorphism.** Any Lie endomorphism preserves \([L,L]=W\). Its quotient map on \(L/W=V\) is some \(A\in\operatorname{End}_F(V)\), and its remaining generator part is some \(B\in\operatorname{Hom}_F(V,W)\). Since \([v,v']=v\wedge v'\), the action on \(W\) is forced to be \(D=\bigwedge^2 A\). Conversely, every pair \((A,B)\) yields a Lie endomorphism with block matrix
\[
\Phi_{A,B}=\begin{pmatrix}A&0\\B&\bigwedge^2 A\end{pmatrix}
\quad\text{on}\quad V\oplus W.
\]
This uses only the alternating exterior product, so no characteristic restriction arises.

**Step 2: simultaneous shear lemma.** Suppose \(\Phi_1,\dots,\Phi_k\) commute and are idempotent. The induced maps \(A_i\) on \(V\) and restricted maps \(D_i=\bigwedge^2A_i\) on \(W\) are likewise commuting idempotents. Any finite family of commuting idempotent linear operators over any field admits a direct sum into common binary eigenspaces, since \(t(t-1)\) has distinct roots in every field. The short exact sequence \(0\to W\to L\to V\to0\) is therefore a sequence of modules for the product algebra \(F^{\mathcal C_k}\), and splits: on each joint eigenspace choose a linear complement to the subspace in \(W\). The resulting equivariant section of the quotient is of the form \(v\mapsto v+f(v)\), \(f\in\operatorname{Hom}_F(V,W)\).

Define the central shear \(S_f(v+w)=v+w+f(v)\). This is a Lie automorphism because it fixes every commutator. Equivariance gives simultaneously
\[
\Phi_i=S_f\begin{pmatrix}A_i&0\\0&D_i\end{pmatrix}S_f^{-1},
\qquad B_i=fA_i-D_if.
\tag{4}
\]
Conversely, every set of commuting idempotents \(A_i\) and every \(f\) define a commuting idempotent family (4).

**Step 3: count each color decomposition and its lifts.** For an ordered family \((A_i)\) put \(V=\bigoplus_{c\in\mathcal C_k}V_c\), \(n_c=\dim V_c\); \(A_i\) is identity on \(V_c\) iff bit \(c_i=1\). The number of ordered direct sum decompositions with this dimension vector is \(g_n/\prod_c g_{n_c}\). On the exterior square,
\[
W=\bigoplus_c W_c,\qquad
W_c=\bigwedge^2 V_c\ \oplus\!
\bigoplus_{\substack{a<b\\a\wedge_{\mathrm{bit}}b=c}}V_a\wedge V_b,
\]
and \(\dim W_c=w_c\). Two shears \(f,g\) yield the same ordered Lie-endomorphism tuple exactly when \((f-g)A_i=D_i(f-g)\) for every \(i\). Such differences are precisely the intertwiners \(\bigoplus_c\operatorname{Hom}_F(V_c,W_c)\), of dimension \(\sum_c n_cw_c\). Hence every ordered family \((A_i)\) lifts in exactly \(q^{nN-\sum_c n_cw_c}\) ways, proving (1). Formula (4) also implies that the rank of each \(\Phi_i\) is the rank of \(A_i\) plus the rank of \(\bigwedge^2 A_i\), establishing the joint-rank refinement.

**Step 4: clique inversion.** If \(S_j\) is the number of ordered pairwise commuting \(j\)-tuples of **distinct** idempotents, grouping an arbitrary ordered commuting \(k\)-tuple by equality of its entries yields \(T_{n,k}=\sum_{j=0}^k {k\brace j}S_j\). Stirling inversion gives \(S_j=\sum_{h=0}^j s(j,h)T_{n,h}\). Division by \(j!\) proves (2).

**Step 5: maximal commuting families.** Conjugate any commuting family by (4). If one nonzero joint eigenspace \(V_c\) has dimension greater than one, splitting it into a line and a complement gives a new nontrivial idempotent projection \(A\) commuting with every existing \(A_i\). Its induced \(\bigwedge^2A\) also commutes with all \(D_i\), so the new conjugated Lie retraction enlarges the family. Thus in a maximal family every nonzero \(V_c\) is a line. If any subset projection on these \(n\) lines is missing, it can again be adjoined; hence every maximal family equals the \(2^n\) subset maps conjugated by \(S_f\).

Conversely, an idempotent Lie map commuting with **every** subset projection must induce an idempotent \(A\) diagonal in the given line decomposition, hence one of the subset projections. In canonical coordinates let \(B\) be its central block. Commutation with the projection onto an individual line \(V_i\), whose exterior-square operator is zero, forces \(B|_{V_i}=0\) for each \(i\). Thus \(B=0\) and the family cannot be enlarged.

Finally the line decomposition is uniquely recoverable from the minimal nonzero quotient projections. For a fixed line decomposition, different shears \(S_f\) give different families: the central blocks of its individual-line projections are exactly \(f|_{V_i}\), recovering \(f\) on a basis. There are \(g_n/[n!(q-1)^n]\) unordered line decompositions and \(q^{nN}\) choices of \(f\), proving (3).

## Verification

The standalone script `verify.py` independently enumerates **all** Lie-endomorphism matrices in the indicated small fields by enumerating their images of generators and calculating their actions on exterior-square basis elements, rather than using the joint-eigenspace proof. It constructs the complete commuting graph, independently counts its vertices, edges and triangles, and checks these against (1) for arities one, two and three. It also directly enumerates maximal cliques for the two rank-two cases.

| \((n,q)\) | Idempotents | Ordered commuting pairs | Ordered commuting triples | Maximal cliques (directly checked) |
| --- | ---: | ---: | ---: | ---: |
| \((2,2)\) | 14 | 88 | 452 | 12 |
| \((2,3)\) | 38 | 292 | 1664 | 54 |
| \((3,2)\) | 1122 | 66532 | 1386792 | not enumerated |

The verifier prints `VERIFY_OK` after all checks. These are finite examples, not the proof of the all-parameter statements. Equations (1)--(3) are established above independently of enumeration.

## Relationship to prior work

Benito and Roldán-López (arXiv:1911.01897v1) describe derivations and automorphisms of free nilpotent Lie algebras via maps on free generators. Their homomorphism-extension and shear descriptions provide the structural starting point; the cited paper does not give the simultaneous commuting-retraction enumerator or maximal-clique classification. Cagliero and Rojas (arXiv:2006.04676v1) study minimal faithful representations of this same free two-step Lie algebra, a different invariant.

The single-idempotent rank and automorphism-conjugacy spectrum of the free class-two Lie algebra is known (earlier finite-field retraction classification, identifier `cb895a1f-3240-485e-833d-66f97c6d5267`). This finding does **not** re-claim that spectrum: its focus is the higher-arity commuting interaction, complete joint-rank refinement, and maximal Boolean families. Likewise, commuting-idempotent tuple enumerations for full matrix monoids do not count Lie algebra endomorphisms, since in (4) the exterior-square action is forced by the quotient map.

## Limitations

The formulas concern **free, two-step** nilpotent Lie algebras and the commutativity graph on **idempotent Lie endomorphisms**. They do not classify commuting arbitrary endomorphisms, nonfree two-step Lie algebras, or higher nilpotency classes. The formula for \(M_{n,q}\) counts embedded maximal cliques, not their automorphism orbits. Bibliographic checks may miss an equivalent result stated using retract semilattices or universal-algebra decompositions; publication priority is not asserted.

## References

1. P. Benito and J. Roldán-López, *Derivations and automorphisms of free nilpotent Lie algebras and their quotients*, first arXiv posting 2019-11-05, arXiv:1911.01897v1. https://arxiv.org/abs/1911.01897
2. L. Cagliero and N. Rojas, *Minimal faithful representations of the free 2-step nilpotent Lie algebra of the rank r*, first arXiv posting 2020-06-08, arXiv:2006.04676v1. https://arxiv.org/abs/2006.04676
3. *Idempotent conjugacy and rank spectrum for finite-field free class-two Lie algebras*, prior scientific record `cb895a1f-3240-485e-833d-66f97c6d5267` (individual retractions only).
