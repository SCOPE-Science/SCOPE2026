# Normal-subgroup labelings classify diagonal relations of finite group–semilattice products

## Finding
Let \(Y\) be a finite meet-semilattice with greatest element \(1\), let \(G\) be any finite group, and equip \(S=Y\times G\) with multiplication \((y,g)(z,h)=(y\wedge z,gh)\). A *diagonal subsemigroup* of \(S\) is a subsemigroup of \(S\times S\) containing every pair \((s,s)\), for \(s\in S\). Write \(\mathcal N(G)\) for the inclusion-ordered lattice of normal subgroups of \(G\).

**Classification.** Every diagonal subsemigroup is uniquely of the form
\[
R(A,N)=\{((a,g),(b,h)):(a,b)\in A,\ gh^{-1}\in N_{a,b}\},
\]
where \(A\subseteq Y\times Y\) is meet-closed and contains the diagonal of \(Y\), and \(N:A\to\mathcal N(G)\) is order-reversing: \((a,b)\le(c,d)\) implies \(N_{c,d}\le N_{a,b}\). Inclusion of such relations is exactly inclusion of supports together with inclusion of their normal-subgroup labels on the smaller support. In particular, the inclusion lattice of diagonal subsemigroups of \(Y\times G\) depends on \(G\) only through its normal-subgroup lattice.

**Congruences.** Every congruence is uniquely specified by a semilattice congruence \(\theta\) on \(Y\) and an order-reversing map \(M:Y/\theta\to\mathcal N(G)\), through
\[
((a,g),(b,h))\in R_{\theta,M}\quad\Longleftrightarrow\quad
 a\mathrel\theta b\ \text{and}\ gh^{-1}\in M_{[a]}.
\]
Consequently, with \(\operatorname{Anti}(P,L)\) denoting order-reversing maps of finite posets,
\[
|\operatorname{Diag}(Y\times G)|=
\sum_{A\in\operatorname{Diag}(Y)}
 |\operatorname{Anti}(A,\mathcal N(G))|,
\qquad
|\operatorname{Cong}(Y\times G)|=
\sum_{\theta\in\operatorname{Cong}(Y)}
 |\operatorname{Anti}(Y/\theta,\mathcal N(G))|.
\]
These are **equalities**, not just lower or upper bounds.

**Prime-normal-lattice specialization.** Let \(C_n=\{0,\ldots,n-1\}\) under minimum, \(n\ge1\), and let \(G\) be any nontrivial finite simple group (abelian or nonabelian). Its two-element normal-subgroup lattice turns each labeling into a downset \(B\) of \(A\), including the empty downset. Put
\[
D_n=\sum_{A\in\operatorname{Diag}(C_n)}
 \#\{B\subseteq A:B\text{ is a downset in }A\}.
\]
Then \(D_n\) is the exact number of diagonal subsemigroups, independent of the isomorphism type and order of \(G\), and
\[
|\operatorname{Cong}(C_n\times G)|=(n+3)2^{n-2},
\qquad \chi(C_n\times G)=\frac{(n+3)2^{n-2}}{D_n}.
\]
The congruence formula is an integer also at \(n=1\), where it equals \(2\). The first exact diagonal counts are
\[
(D_1,D_2,D_3,D_4,D_5)=(2,17,337,12152,696076).
\]
Moreover, because \(|\operatorname{Diag}(C_n)|=(n!)^2\),
\[
D_n\ge(n+1)(n!)^2,
\qquad
\chi(C_n\times G)\le
\frac{n+3}{2(n+1)}\,\chi(C_n).
\]
This explicitly sharpens the general Clifford-semigroup comparison for every \(n\ge2\).

## Assumptions and scope
All semilattices and groups in the theorem are finite, and \(Y\) has a top element. The group need not be abelian or simple in the classification and congruence formulas. Simplicity is imposed only in the explicit downset and numerical specialization. The order on \(Y\times Y\) is coordinatewise, with meet taken coordinatewise. An order-reversing label satisfies \(x\le y\Rightarrow N_y\subseteq N_x\). An empty downset is permitted. For the normalized coefficient, \(\chi(T)=|\operatorname{Cong}(T)|/|\operatorname{Diag}(T)|\).

## Proof
**1. Fibers over the semilattice square.** Project any diagonal subsemigroup \(R\subseteq S\times S\) to \(Y\times Y\). Its nonempty fiber-support \(A\) contains the diagonal and is meet-closed. For \(u=(a,b)\in A\), let \(H_u\subseteq G\times G\) be its group-coordinate fiber. Since \(u\wedge u=u\), the fiber is a nonempty finite subsemigroup of the finite group \(G\times G\), hence a subgroup: positive powers supply identities and inverses. Because \(Y\) has a top element, multiplying by the diagonal elements \(((1,t),(1,t))\) of \(S\times S\) preserves this fiber. In particular, starting from the identity of \(H_u\) gives \((t,t)\in H_u\) for every \(t\in G\). Hence \(H_u\) is a subgroup containing the diagonal subgroup \(\Delta_G\).

**2. Normal-subgroup coordinates.** Every subgroup \(H\) of \(G\times G\) containing \(\Delta_G\) has the unique form
\[
H_N=\{(g,h):gh^{-1}\in N\}
\]
for a normal subgroup \(N\triangleleft G\). Indeed, define \(N=\{g:(g,1_G)\in H\}\); conjugation by diagonal elements makes \(N\) normal, and right multiplication by \((h^{-1},h^{-1})\) proves the displayed description. Applying this correspondence to each nonempty fiber gives unique labels \(N_u\in\mathcal N(G)\).

**3. Necessity and sufficiency of antitonicity.** If \(u\le v\) in \(A\), multiply any member of fiber \(H_v\) by \((1_G,1_G)\in H_u\). Its group coordinates remain unchanged, while its semilattice coordinate becomes \(u\), so \(H_v\subseteq H_u\), equivalently \(N_v\subseteq N_u\). Conversely, suppose \(A\) is meet-closed and the normal-subgroup labels are antitone. For \((g,h)\in H_{N_u}\) and \((s,t)\in H_{N_v}\), the difference of their product is
\[
(gs)(ht)^{-1}=g(st^{-1})g^{-1}(gh^{-1}).
\]
Both factors lie in \(N_{u\wedge v}\), because it contains \(N_u,N_v\) and they are normal. Thus the product lies in fiber \(H_{N_{u\wedge v}}\). Diagonal elements are present since every diagonal semilattice cell belongs to \(A\) and every normal subgroup contains \(1_G\). This proves the exact classification and also its stated inclusion order.

**4. Congruences.** Let \(R\) now be an equivalence relation as well as a diagonal subsemigroup. Define \(a\mathrel\theta b\) precisely when \(((a,1_G),(b,1_G))\in R\). This is a semilattice congruence. If a pair \(((a,g),(b,h))\) belongs to \(R\), raise it to a common positive multiple of the finite orders of \(g\) and \(h\): the result is \(((a,1_G),(b,1_G))\), so every semilattice pair in the support already belongs to \(\theta\). Thus the support is exactly \(\theta\). For \(a\mathrel\theta b\), multiplication of \(((a,1_G),(b,1_G))\) by diagonal elements \(((1,t),(1,t))\) shows \(((a,t),(b,t))\in R\). Transitivity, together with the within-fiber subgroup relations, forces \(N_{a,a}=N_{b,b}\): the pairs \(((a,g),(b,g))\) and \(((b,h),(a,h))\) transport each within-level relation between levels \(a\) and \(b\). The same transports show \(N_{a,b}=N_{a,a}\) whenever \(a\mathrel\theta b\), since a related cross-level pair \(((a,g),(b,h))\) is equivalent by transitivity to \(((a,g),(a,h))\). Thus all labels over one \(\theta\)-class equal a single normal subgroup \(M_{[a]}\). Equivalently, applying the normal-subgroup fiber description directly gives
\[
((a,g),(b,h))\in R\iff a\mathrel\theta b
\text{ and }gh^{-1}\in M_{[a]}.
\]
Antitonicity of \(N\) descends to the quotient semilattice \(Y/\theta\): whenever \([a]\le[b]\), the representatives \(a\wedge b\) and \(b\) are comparable, and \(a\wedge b\mathrel\theta a\). Conversely, this formula for any \((\theta,M)\) is reflexive, symmetric, transitive and multiplicatively compatible (use normality and antitonicity as in Step 3). It is uniquely recoverable from \(R\). Summing over supports or congruence traces proves the two counting formulas. An isomorphism of normal-subgroup lattices transports labels and preserves inclusion and congruence counts.

**5. The chain and a simple group.** When \(G\) is nontrivial finite simple, the only labels are \(\{1_G\}\) and \(G\). The cells labeled \(G\) form exactly a downset \(B\) of \(A\). Thus the diagonal count is \(D_n\). A semilattice congruence on the chain is an interval partition into \(k\) blocks, with \(\binom{n-1}{k-1}\) choices. There are precisely \(k+1\) antitone two-valued labels on its quotient chain. Hence
\[
|\operatorname{Cong}(C_n\times G)|
=\sum_{k=1}^{n}\binom{n-1}{k-1}(k+1)
=(n+3)2^{n-2}.
\]

For completeness, every \(A\in\operatorname{Diag}(C_n)\) is specified uniquely by independent integers \(0\le a_i,b_i\le n-1-i\), for \(0\le i<n\), where \(a_{n-1}=b_{n-1}=0\): its off-diagonal upper pairs are \((i,i+j)\) for \(1\le j\le a_i\), and its lower pairs are \((i+j,i)\) for \(1\le j\le b_i\). Meeting an off-diagonal pair with a diagonal pair forces the indicated initial segment, and direct examination of upper–upper, lower–lower, and mixed products proves the converse. Hence there are \(\prod_{i=0}^{n-1}(n-i)^2=(n!)^2\) possible supports.

An exact finite algorithm for \(D_n\), without enumerating relations on \(S\times S\), is to sum the number of distinct intersections \(A\cap D(t)\), where \(A\) ranges over these prefix-coded supports and
\[
D(t)=\{(i,j):0\le j<t_i\},\qquad
n\ge t_0\ge t_1\ge\cdots\ge t_{n-1}\ge0.
\]
Every downset of \(A\) equals one of these intersections, because downsets of an induced finite subposet extend to downsets of the ambient grid. Counting distinct intersections produces the five listed values, reproduced by `verify.py`.

Finally, for each support \(A\), the intersections with the \(n+1\) grid downsets \(\{(i,j):i,j\le k\}\), \(-1\le k<n\), are pairwise different: the diagonal points \((k,k)\) distinguish them. Therefore \(A\) has at least \(n+1\) downsets, giving \(D_n\ge(n+1)(n!)^2\). Combining this with the preceding congruence formula and \(\chi(C_n)=2^{n-1}/(n!)^2\) yields the displayed strict quantitative bound.

## Verification
Run `python3 verify.py` using only the Python standard library. It independently generates all prefix-coded semilattice supports and intersects them with ambient grid downsets for \(n=1,2,3,4,5\), obtaining \(D_n=2,17,337,12152,696076\). It exhaustively tests all \(4096\) reflexive relations on the four-element semigroup \(C_2\times C_2\); checks all possible diagonal/group-full fiber assignments in \(C_3\times C_2\) by direct multiplication; enumerates equivalence partitions for congruences over chains and the four-element diamond semilattice; and independently enumerates the diagonal-containing subgroups of \(S_3\times S_3\) before checking all fibers over the two-chain. The last test gives \(46\) diagonal subsemigroups, consistent with a three-element chain of normal subgroups. The executable ends with `VERIFY_OK`. Computations check finite instances only; the arbitrary finite \(Y,G\) theorem is established by Steps 1–4.

## Relationship to prior work
Barber and Ruškuc (arXiv:2602.17286, first posted February 19, 2026) introduce and study the DSC coefficient. Their Section 4 treats Clifford semigroups, constructs an **injective** family of diagonal subsemigroups indexed by subgroup kernels and semilattice traces, expressly notes that this family is not exhaustive in general, and proves \(\chi(S)\le\chi(Y)\). The theorem above supplies an **exhaustive** classification for the distinct natural case of **constant group fibers with identity connecting homomorphisms**, an exact normal-lattice formula, and quantitative strictness for nontrivial simple groups over chains. For a simple-group fiber on a chain, the Section 4 construction contributes \((n+1)(n!)^2\) members; the exact new count is strictly larger for \(n\ge2\), beginning \(17>12\) at \(n=2\).

The earlier Barber–Ruškuc paper (arXiv:2504.02428) establishes the general finite-group DSC baseline, but neither an exhaustive Clifford direct-product labeling theorem nor these counts. Classical normal-subgroup and semilattice-congruence correspondences form ingredients of the proof, not separate claims of novelty. The chain-only support count \((n!)^2\) is an elementary input; the added subgroup-valued fibers are essential for the result about group–semilattice products.

## Limitations
The proof requires a finite group (so a nonempty fiber subsemigroup becomes a subgroup) and a greatest element in the semilattice (so every nonempty fiber receives all group diagonals). It does not assert the same classification for arbitrary Clifford semigroups with nonidentity connecting homomorphisms, or for infinite nonperiodic groups or semilattices without a top. The formula \(D_n\) is an explicit finite combinatorial sum; no simple closed product or asymptotic equivalent for \(D_n\) is claimed. Historical priority is not independently certified; an older equivalent theorem under subgroup-valued relation or strong-semilattice terminology remains possible.

## References
1. C. Barber and N. Ruškuc, *Comparing Numbers of Diagonal Subsemigroups and Congruences for Semigroups*, arXiv:2602.17286v1 (first public posting 2026-02-19), especially Section 4, Lemma 4.1 and Theorem 4.2. https://arxiv.org/abs/2602.17286
2. C. Barber and N. Ruškuc, *Semigroup Congruences and Subsemigroups of the Direct Square*, arXiv:2504.02428v1 (2025-04-03), especially Proposition 1.2 and the finite-group observations. https://arxiv.org/abs/2504.02428
