# Endomorphism monoids and retraction rank spectra of repeated cyclic evolution algebras

## Finding

For each prime power \(q\) and positive integers \(\ell,r\), consider the evolution algebra \(E_{\ell,r}\) over \(\mathbb F_q\) defined below. Let \(g=\gcd(q-1,2^\ell-1)\) and \(h=\ell g\).

**Endomorphism normal form.** Each endomorphism is determined by independently assigning to each target cycle either zero or a source cycle together with an isomorphism between the two length-\(\ell\) cycle algebras. There are exactly \(h\) possible isomorphisms for each ordered pair of source and target cycles. Consequently
\[
\bigl|\operatorname{End}(E_{\ell,r})\bigr|=(1+rh)^r.
\]
This is a structural description of the entire endomorphism monoid, not only of its units.

**Retraction theorem.** Let \(N_{\ell,r,q}(k)\) be the number of algebra endomorphisms \(F\) with \(F\circ F=F\) and \(\dim_{\mathbb F_q}\operatorname{im}F=k\ell\). Then, for every integer \(0\le k\le r\),
\[
N_{\ell,r,q}(k)=\binom{r}{k}\bigl(1+kh\bigr)^{r-k}.
\]
No other ranks occur. The resulting polynomial is
\[
P_{\ell,r,q}(z)=\sum_{k=0}^{r}\binom{r}{k}(1+k\ell\gcd(q-1,2^\ell-1))^{r-k}z^{k\ell}.
\]
The image of every rank-\(k\ell\) retraction is itself isomorphic as an algebra to \(E_{\ell,k}\). The zero algebra is understood when \(k=0\).

## Assumptions and scope

An evolution algebra is a commutative, not necessarily associative algebra admitting a natural basis of mutually orthogonal distinct basis elements. Define
\[
E_{\ell,r}=\bigoplus_{a=1}^{r}\operatorname{span}_{\mathbb F_q}\{e_{a,i}:i\in\mathbb Z/\ell\mathbb Z\},
\]
with \(e_{a,i}^2=e_{a,i+1}\), indices taken modulo \(\ell\), and products of distinct natural basis elements equal to zero. An endomorphism is an \(\mathbb F_q\)-linear map preserving these products; it need not be unital (the algebra need not be unital). Rank is ordinary vector-space rank. An idempotent endomorphism means composition-idempotent, not an idempotent *element* of the algebra. Both \(\ell\) and \(r\) are at least one, including \(\ell=1\) and every field characteristic.

Every single cycle is simple: if an ideal contains a nonzero linear combination, multiplying by a basis vector with nonzero coefficient isolates a nonzero basis square, and its subsequent squares generate the entire cycle.

## Proof

**1. Orthogonality implies row sparsity.** Order the natural basis by target cycle and position, and write \(F(e_u)=\sum_v m_{v,u}e_v\). For distinct source indices \(u\ne w\), multiplicativity and \(e_ue_w=0\) give
\[
0=F(e_u)F(e_w)=\sum_v m_{v,u}m_{v,w}e_{\operatorname{next}(v)}.
\]
The successor map on the disjoint union of cycles is bijective. Its basis vectors are independent; hence \(m_{v,u}m_{v,w}=0\) for each target row \(v\). Since the coefficient ring is a field, every row contains at most one nonzero entry. Conversely, this row-sparsity ensures multiplicativity on products of distinct basis elements.

**2. Squaring forces whole-cycle labels.** Multiplicativity on squares says, for all target indices \(v\) and source indices \(u\),
\[
m_{\operatorname{next}(v),\operatorname{next}(u)}=m_{v,u}^{2}.
\]
If any row on target cycle \(a\) is nonzero, this relation forces every row on that cycle to be nonzero. After \(\ell\) steps, the source position returns to its initial position, since all source cycles have length exactly \(\ell\), and the coefficient must obey \(c^{2^\ell}=c\). Thus each active target cycle \(a\) is prescribed by a source-cycle index \(b\in\{1,\ldots,r\}\), a phase \(s\in\mathbb Z/\ell\mathbb Z\), and a scalar \(c\in\mathbb F_q^\times\) with
\[
c^{2^\ell-1}=1.
\]
Explicitly, the only nonzero coefficient on target row \((a,i)\) lies in source column \((b,i+s)\) and equals \(c^{2^i}\), where \(i\) is represented by \(0,\ldots,\ell-1\). All such choices satisfy the square and orthogonality equations. Since \(\mathbb F_q^\times\) is cyclic of order \(q-1\), the scalar equation has exactly \(g=\gcd(q-1,2^\ell-1)\) solutions. Therefore each target cycle has \(1+r\ell g=1+rh\) choices, proving the complete endomorphism count and the normal form. The \(h\) nonzero labels constitute the automorphism group \(G=\operatorname{Aut}(E_{\ell,1})\), whose identity corresponds to phase zero and scalar one.

**3. Composition-idempotence forces labelled roots.** View a nonzero target-cycle assignment as a labelled arrow \(a\to b\) (target \(a\), source \(b\)) with label in \(G\); zero assignments are zero arrows. On composing two maps, the source arrows are composed and the isomorphism labels multiplied (with the evident source-to-target orientation). A zero arrow remains zero. For any nonzero arrow \(a\to b\) in a composition-idempotent assignment, its second iterate has the same target, source and label. Therefore the arrow from \(b\) must be the loop \(b\to b\) with identity group label: equality of labels allows cancellation in \(G\). Call such vertices **roots**. Conversely, if every nonzero arrow points to a root, with every root labelled by the identity loop, then the resulting algebra endomorphism squares to itself.

**4. Rank and enumeration.** Choose the \(k\) roots in \(\binom rk\) ways. Each remaining target cycle either has zero assignment or points to one of the \(k\) roots with any of \(h\) labels; there are \(1+kh\) possibilities independently. Because each selected root supplies an identity block on its own source-cycle coordinates, these \(k\) source cycles contribute a total image rank of exactly \(k\ell\); the other source cycles do not contribute further columns. Moreover, the \(k\ell\) vectors \(F(e_{b,i})\) from the roots \(b\) constitute a natural basis of the image with the same square-successor relations and mutually zero mixed products. Hence the image is \(E_{\ell,k}\), and the stated coefficient formula and polynomial follow.

## Verification

The accompanying standalone `verify.py` constructs actual matrices over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), checks every product-preserving row-sparse matrix, calculates compositions and matrix ranks, and compares the full histograms with the symbolic formulas. It also checks *all* \(2^{16}=65536\) matrices of dimension four over \(\mathbb F_2\) with no row-sparsity restriction and recovers exactly 25 endomorphisms, of which the rank-\(0,2,4\) retraction multiplicities are \(1,6,1\). Other tested exact cases include \((\ell,r,q)=(2,2,4)\), with 169 endomorphisms and retraction multiplicities \(1,14,1\), and \((2,3,2)\), with 343 endomorphisms and multiplicities \(1,27,15,1\). Run with `python verify.py` using standard-library Python 3. The exhaustive tests are finite evidence; the argument above proves the formula for all parameters.

## Relationship to prior work

Narkuziyev studies permutation evolution algebras, their cycle decompositions and algebra *elements* satisfying the idempotent equation; this does not enumerate algebra endomorphisms that square to themselves under composition [1]. Sriwongsa and Zou establish structural descriptions of **invertible** homomorphisms and automorphism groups of perfect evolution algebras [2], while Wei and Zou count algebra **isomorphism classes** over finite fields [3]. The current theorem uses established monomial rigidity and the cyclic-scalar automorphism phenomenon as context; its subject is the full, generally noninvertible endomorphism monoid of repeated cycles and the exact rank distribution of its retractions. The automorphism count \(h\) alone does not imply the labelled-target independence or the root condition without the additional endomorphism analysis above.

## Limitations

This theorem addresses only direct sums of equal-length **unweighted** cyclic evolution algebras, not arbitrary weighted cycles, mixtures of lengths, or general perfect evolution algebras. It counts labelled algebra endomorphisms, not their equivalence classes under conjugation. A structurally equivalent formula in broader transformation-semigroup or categorical endomorphism literature has not been excluded exhaustively; the novelty comparison is limited to the sources examined. Computational tests cover finite examples and do not substitute for the proof.

## References

[1] B. A. Narkuziyev, *On absolute nilpotent and idempotent elements of an evolution algebra corresponding to permutations*, arXiv:1803.11415, initial public version 2018-03-30; related published version *Some remarks on evolution algebras corresponding to permutations*, Journal of Algebra and Its Applications (2022), DOI: 10.1142/S0219498822501122.

[2] S. Sriwongsa and Y. M. Zou, *On Automorphism Groups of Idempotent Evolution Algebras*, arXiv:2202.01333, especially Section 2 and Theorem 2.2.

[3] Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368 (2023-10-18), especially Theorem 1.1, Corollary 1.1 and Section 2.
