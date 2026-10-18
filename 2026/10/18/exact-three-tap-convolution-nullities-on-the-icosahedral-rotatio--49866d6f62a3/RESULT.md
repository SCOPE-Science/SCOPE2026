# Exact three-tap convolution nullities on the icosahedral rotation group

## Finding

Let \(G=\mathrm A_5\), regarded as the orientation-preserving rotation group of the regular icosahedron. For every three-element subset \(S\subset G\), define the unit-coefficient left-convolution operator on complex functions on \(G\) by
\[
 (T_Sf)(g)=\sum_{s\in S}f(s^{-1}g).
\]
Its complex nullity admits the complete intrinsic classification below. This is a classification of **all** \(\binom{60}{3}=34{,}220\) supports, not only generating supports, with no assumed inverse closure of \(S\).

For any ordering \(S=\{x,y,z\}\), write \(a=x^{-1}y\), \(b=x^{-1}z\), and define \(H_S=\langle a,b\rangle\). Its order does not depend on the ordering. Write \(\tau(S)\) for the sorted three-element multiset of orders of \(x^{-1}y\), \(x^{-1}z\), and \(y^{-1}z\). The 24 five-cycles of \(G\) split into two \(G\)-conjugacy classes of size twelve, each invariant under inversion. If \(\tau(S)=(3,5,5)\), let \(\epsilon(S)=\mathrm{same}\) if the two order-five pair quotients belong to the same one of these classes, and \(\mathrm{different}\) otherwise. The choice of orientation of each quotient and the naming of the two classes are immaterial. The symbol — below means this flag is not needed.

| \(\tau(S)\) | \(|H_S|\) | \(\epsilon(S)\) | \(\dim_{\mathbb C}\ker T_S\) | Number of supports |
|:--:|--:|:--:|--:|--:|
| \((2,2,2)\) | 4 | — | 0 | 300 |
| \((2,2,3)\) | 6 | — | 20 | 1,800 |
| \((2,2,5)\) | 10 | — | 0 | 3,600 |
| \((2,3,3)\) | 12 | — | 0 | 3,600 |
| \((2,3,5)\) | 60 | — | 0 | 7,200 |
| \((2,5,5)\) | 60 | — | 5 | 3,600 |
| \((3,3,3)\) | 3 | — | 40 | 200 |
| \((3,3,3)\) | 12 | — | 10 | 1,200 |
| \((3,3,5)\) | 60 | — | 0 | 3,600 |
| \((3,5,5)\) | 60 | different | 4 | 3,600 |
| \((3,5,5)\) | 60 | same | 10 | 3,600 |
| \((5,5,5)\) | 5 | — | 0 | 720 |
| \((5,5,5)\) | 60 | — | 4 | 1,200 |

Consequently, the nullity distribution, with the number of supports at nullity \(0,4,5,10,20,40\), is respectively
\[
 (19{,}020,\ 4{,}800,\ 3{,}600,\ 4{,}800,\ 1{,}800,\ 200).
\]
Precisely \(15{,}200\) supports are singular. The maximum nullity is \(40\), attained precisely at the \(200\) cosets of the ten order-three subgroups. The three pairwise quotient orders alone do **not** suffice for the complete rank classification: the subgroup order disambiguates \((3,3,3)\) and \((5,5,5)\), and the split five-cycle conjugacy-class flag disambiguates \((3,5,5)\).

## Assumptions and scope

All computations take place in the exact finite group of even permutations of five symbols; its identity is \(e\). A support is an **unordered set of three distinct elements**. The operator is the unweighted (each coefficient one) left-convolution operator on the 60-dimensional complex group algebra; this classification is not asserted for weighted supports, multisets, or other groups. Matrix ranks over \(\mathbb Q\) equal those over \(\mathbb C\) because all entries are integers. The conjugacy-class distinction applies solely to five-cycles in \(\mathrm A_5\), not to conjugacy under \(\mathrm S_5\), which merges the two classes.

## Proof

**1. Reduction to 1,711 finite cases.** For each \(S=\{x,y,z\}\), left translate its three elements by \(x^{-1}\) to obtain \(\{e,a,b\}\). Left multiplication of the support is implemented by an invertible left-regular translation, so it preserves \(\ker T_S\)'s dimension. There are exactly \(\binom{59}{2}=1{,}711\) distinct unordered choices \(\{a,b\}\subset G\setminus\{e\}\). Conversely, each original support has exactly three choices of distinguished element. Hence an invariant count of \(c\) normalized pairs corresponds to \(60c/3=20c\) unrestricted supports, even when the support has a nontrivial translation stabilizer.

**2. Exact group and invariants.** Represent permutations as five-entry arrays and define \((pq)(i)=p(q(i))\). Enumerate lexicographically all permutations of five symbols, retaining exactly those with even inversion parity. There are 60. Form the full 60-by-60 multiplication table and the inverse and element-order tables by integer operations. Element orders have multiplicities \(1,15,20,24\) for \(1,2,3,5\). The conjugates \(cuc^{-1}\) of one order-five element \(u\) form a twelve-element class; its complement among order-five elements is the other class. Both are closed under inversion (also explicitly verified). For a normalized support \(\{e,a,b\}\), the signature is the sorted triple of orders of \(a,b,a^{-1}b\); the generated subgroup's order is found by repeatedly multiplying the already-reached elements on the right by \(a\) and \(b\). Finite closure under these generators equals their generated subgroup. For the split flag, compare the class memberships of the two order-five elements of \(\{a,b,a^{-1}b\}\). The checker also verifies equality of all three invariant keys obtained by anchoring at each original support element.

**3. Exact operator matrix and ranks.** In the standard basis \(\{\delta_g:g\in G\}\), the operator for normalized support \(\{e,a,b\}\) has the integer matrix
\[
 M_{r,c}=[r=c]+[r=ac]+[r=bc],\qquad r,c\in G,
\]
where brackets are Kronecker indicators. This follows immediately by applying \(T_S\) to the point-mass function \(\delta_c\). The supplied `check_a5.py` forms this matrix for each of the 1,711 normalized supports and performs ordinary row-echelon Gaussian elimination entirely over \(\mathbb Q\), using exact `Fraction` numerators and denominators. A pivot is selected if and only if its current rational entry is nonzero. Row swaps, nonzero pivot divisions, and subtraction of pivot-row multiples preserve rank. Thus the returned pivot count is *exactly* the rank over \(\mathbb Q\) and hence \(\mathbb C\). Subtracting from 60 gives the exact nullity, without floating-point or modular-rank assumptions.

**4. Exhaustiveness and count certificate.** The finite loop iterates over all \(\binom{59}{2}\) index pairs. For every case it asserts that the invariant key belongs to exactly one of the thirteen displayed rows, that the exact nullity equals that row's prediction, and that all three anchor choices give the same key. The normalized counts for the table, in row order, are
\[
 (15,90,180,180,360,180,10,60,180,180,180,36,60),
\]
which sum to 1,711. Multiplying each by 20 gives the displayed 34,220-support census. Summing by nullity gives the distribution. Since a support with signature \((3,3,3)\) generating a subgroup of order three is exactly a coset of an order-three cyclic subgroup, the row of nullity 40 identifies all extremizers. There are ten such subgroups (20 elements of order three, two per subgroup), each with twenty left cosets, giving 200 extremizers. This completes the finite proof of the classification and its consequences.

The exact executable is an essential finite-case proof certificate: the mathematical assertion does not rely on uninspected logs or on a statistical sample. All inputs, loops, matrix arithmetic, and assertions occur inside the supplied stand-alone code.

## Verification

Run `python3 check_a5.py` with Python 3 standard library. The program terminates successfully with `PASS: all 1,711 normalized supports checked over Q; 13 types; 34,220 total.` A successful run checks all thirteen predicted nullities, the complete counts, inversion-stability of the five-cycle class, anchor invariance, and the aggregate singularity/extremal census. The computation takes seconds on an ordinary desktop and uses no downloads, random inputs, floating-point approximations, or external packages. All exact arithmetic uses Python integers and `fractions.Fraction`; the verifier checks the finite domain exhaustively.

## Relationship to prior work

Arezoomand and Taeri establish general block-characteristic-polynomial methods for finite Cayley digraphs, including nonabelian regular representations [1]. That framework explains why Fourier or regular-matrix methods apply, but the source's inspected general formulas do not themselves present the thirteen A5 intrinsic support types, the split five-cycle distinction, or this numerical nullity census. Siemons and Zalesski study singularity for **normal**, conjugacy-invariant Cayley connection sets in finite simple groups [2]; generic unweighted three-element supports in this theorem are not normal, so their character-sum criterion does not decide this classification. Liu and Zhou survey Cayley spectral results including alternating groups and normal connection sets [3], but the inspected sections do not give this exact census. Fang, Lu, Wang and Xu [4] analyze automorphism groups and normality of low-valency Cayley digraphs for finite simple groups; their publicly readable author-uploaded full text gives no eigenvalue, rank or spectral census and does not supply this classification. Xu and Xu [5] study normality and arc transitivity of low-valency Cayley graphs on A5, a highly relevant same-group source whose full text was unavailable for comparison; no claim of a full-text exclusion is made.

This theorem is about nullities of all unweighted three-element left-convolution matrices and the exact data needed to distinguish them. The basic group representation and Cayley adjacency approaches are prior methods and not asserted as new.

## Limitations

The certificate is a finite exhaustive exact-arithmetic proof for one natural finite simple group, not a symbolic formula for all nonabelian simple groups. The result does not classify weighted convolutions or nonzero eigenvalues. The proof's reproducibility depends on executing or independently checking the supplied transparent finite enumeration; the script itself is not an independent mathematical audit. The relevant 2004 low-valency A5 symmetry paper [5] was compared through its available abstract, not its full text, and an equivalent spectral census in older literature cannot be entirely excluded. Independent publication priority and independent mathematical verification have not been established.

## References

[1] M. Arezoomand and B. Taeri, *On the characteristic polynomial of n-Cayley digraphs*, Electronic Journal of Combinatorics 20(3) (2013), P57, publicly dated 2013-10-07, DOI 10.37236/3105. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i3p57/pdf/

[2] J. Siemons and A. Zalesski, *Remarks on singular Cayley graphs and vanishing elements of simple groups* (2018), arXiv:1804.01204. https://arxiv.org/pdf/1804.01204

[3] X. Liu and S. Zhou, *Eigenvalues of Cayley graphs: a survey* (2022), https://www.combinatorics.org/ojs/index.php/eljc/article/download/v29i2p9/pdf/

[4] X.-G. Fang, Z.-P. Lu, J. Wang and M.-Y. Xu, *Cayley Digraphs of Finite Simple Groups with Small Out-Valency*, Communications in Algebra 32 (2004), 1201–1211, DOI 10.1081/AGB-120027974 (author-uploaded full text reviewed).

[5] M. Xu and S. Xu, *Symmetry properties of Cayley graphs of small valencies on the alternating group A5*, Science in China Series A: Mathematics 47 (2004), 593–604, DOI 10.1360/03ys0065 (abstract accessible; full text not inspected).
