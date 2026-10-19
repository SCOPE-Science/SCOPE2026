# Higher-power complete mappings and the complete-regularity barrier

## Finding
Let \(S\) be a nonempty finite semigroup and let \(k\ge2\) be an integer. A **\(k\)-complete mapping** is a permutation \(\alpha:S\to S\) for which \(\theta:S\to S\), defined by \(\theta(x)=x(\alpha(x))^k\), is also a permutation.

**Theorem.** The following statements hold.

1. **Complete-regularity obstruction.** If \(S\) has a \(k\)-complete mapping for any \(k\ge2\), then every element of \(S\) belongs to a subgroup of \(S\); equivalently, \(S\) is completely regular.
2. **Full even-power classification.** For every even \(k\ge2\), \(S\) admits a \(k\)-complete mapping **if and only if** \(S\) is completely regular. In fact, writing \(E\) for the least common multiple of the exponents of all maximal subgroups, one can select an integer \(a\ge1\) such that \(\gcd(a,E)=\gcd(1+ka,E)=1\), and \(\alpha(x)=x^a\) is a witness.
3. **Exact inverse-semigroup reduction.** For any \(k\ge2\), a finite inverse semigroup \(S\) admits a \(k\)-complete mapping if and only if it is a Clifford semigroup (a semilattice of groups) and each constituent maximal subgroup admits a \(k\)-complete mapping. In that case every \(k\)-complete mapping preserves every maximal subgroup, and restrictions to these groups may be chosen independently.
4. **Explicit abelian-maximal-subgroup criterion.** If all maximal subgroups of the finite inverse semigroup \(S\) are abelian, it has a \(k\)-complete mapping exactly when it is Clifford and either \(k\) is even, or **each** constituent maximal subgroup has trivial or noncyclic Sylow \(2\)-subgroup. Thus for odd \(k\ge3\), the subgroup condition is identical to the familiar existence condition for ordinary complete mappings of finite abelian groups, but non-Clifford inverse semigroups are always excluded.

The theorem applies to all finite semigroups in clauses 1–2 and to all finite inverse semigroups in clauses 3–4, without identity assumptions. It concerns existence and structural preservation, not the number of permutations in arbitrary nonabelian groups.

## Assumptions and scope
For a finite semigroup \(S\), define the Green preorder \(s\le_{\mathcal J}t\) by inclusion of principal two-sided ideals \(S^1sS^1\subseteq S^1tS^1\), and write \(s\mathrel{\mathcal J}t\) for equality. The maximal subgroups are the group \(\mathcal H\)-classes. A completely regular semigroup is a union of these groups. A Clifford semigroup is an inverse semigroup that is a union of groups, equivalently a semilattice of groups.

The exponent \(E\) of the family of maximal subgroups means the least common multiple of their individual exponents (including the trivial group exponent \(1\)); this is finite. The Sylow \(2\)-subgroup of an odd-order group is trivial. Powers \(x^a\) are taken in the semigroup multiplication, which restricts to ordinary group powers whenever \(x\) belongs to one of its subgroups.

## Proof
**Step 1: the two permutations preserve Green \(\mathcal J\)-classes.** For every \(x\in S\), since \(\theta(x)=x(\alpha(x))^k\), both \(\theta(x)\le_{\mathcal J}x\) and \(\theta(x)\le_{\mathcal J}\alpha(x)\). Because \(\theta\) is a permutation of the finite set \(S\), iterate these inequalities around any cycle of \(\theta\): each becomes an equality of \(\mathcal J\)-classes. Hence \(\theta(x)\mathrel{\mathcal J}x\) for every \(x\). Therefore \(x\le_{\mathcal J}\alpha(x)\). Iterating this last inequality around the cycles of the permutation \(\alpha\) shows \(x\mathrel{\mathcal J}\alpha(x)\) for all \(x\) as well.

**Step 2: every square remains in its \(\mathcal J\)-class.** In the chain
\[\theta(x)\le_{\mathcal J}(\alpha(x))^k\le_{\mathcal J}(\alpha(x))^2\le_{\mathcal J}\alpha(x),\]
the endpoints are \(\mathcal J\)-equivalent by Step 1. Thus \((\alpha(x))^2\mathrel{\mathcal J}\alpha(x)\). Since \(\alpha\) is onto, every \(s\in S\) satisfies \(s^2\mathrel{\mathcal J}s\).

**Step 3: a finite-semigroup group-class lemma.** If \(s^2\mathrel{\mathcal J}s\) in a finite semigroup, then \(s\) lies in a subgroup. Here is a justification via the standard principal-factor description. The \(\mathcal J\)-class of \(s\) is regular (an element whose square stays in the class cannot belong to a null principal factor). Its principal factor is a completely \(0\)-simple Rees matrix semigroup \(\mathcal M^0(G;I,\Lambda,P)\). Write the image of \(s\) as \((i,g,\lambda)\). Its square stays nonzero precisely when \(P_{\lambda i}\ne0\); then its \(\mathcal H\)-class \(\{(i,h,\lambda):h\in G\}\) is a group, and the corresponding \(\mathcal H\)-class containing \(s\) in the original semigroup is a group. Thus \(S\) is completely regular, proving clause 1.

**Step 4: even powers and explicit witnesses.** Suppose now \(S\) is completely regular and \(k\) is even. For every prime \(p\mid E\), choose \(a_p\) modulo \(p\) avoiding \(0\) and, if \(p\nmid k\), avoiding \(-k^{-1}\). Such a choice always exists: for odd \(p\) at most two residues are excluded, while for \(p=2\) the residue \(a_p=1\) is admissible because \(k\) is even. The Chinese remainder theorem yields \(a\ge1\) such that \(a\) and \(1+ka\) are units modulo every prime factor of \(E\). Therefore each power map \(x\mapsto x^a\) and \(x\mapsto x^{1+ka}\) is a permutation on every maximal subgroup. Since these subgroups partition \(S\), both maps are permutations of \(S\). Within the maximal subgroup containing \(x\),
\[x(\alpha(x))^k=x(x^a)^k=x^{1+ka}.\]
This proves clause 2. The same construction works without an evenness restriction when \(E\) is odd.

**Step 5: finite inverse semigroups.** For inverse \(S\), Step 3 gives exactly the Clifford property. In a Clifford semigroup, distinct constituent maximal subgroups are exactly distinct \(\mathcal J\)-classes: its idempotents form a semilattice, and \(S^1eS^1\) is determined by the semilattice ideal below \(e\). By Step 1, each \(k\)-complete map \(\alpha\) preserves each maximal subgroup; so does \(\theta\). The restrictions are therefore \(k\)-complete group mappings. Conversely, a choice of such a map on each maximal subgroup has a disjoint-union permutation \(\alpha\), and \(x\) and \(\alpha(x)\) lie in the same group, so the associated \(\theta\) is also the disjoint union of group permutations. This proves clause 3, including independent restriction choices.

**Step 6: finite abelian groups for odd powers.** Let \(A\) be a finite abelian group and \(k\) odd. Write \(A=A_2\times A_{\mathrm{odd}}\). If \(A_2\) is trivial or noncyclic, the classical abelian Hall–Paige existence theorem supplies an ordinary complete mapping \(\beta:A_2\to A_2\) (including the trivial group). The power map \(u\mapsto u^k\) is bijective on \(A_2\), because \(k\) is odd, so choose \(\alpha_2(u)=(\beta(u))^{k^{-1}}\), where the inverse exponent is taken modulo the exponent of \(A_2\). Then \(u(\alpha_2(u))^k=u\beta(u)\) is a permutation. For \(A_{\mathrm{odd}}\), Step 4's CRT construction supplies a power map for every integer \(k\); combining maps componentwise gives a \(k\)-complete mapping of \(A\).

Conversely, if \(A_2\) is nontrivial cyclic, the product \(P=\prod_{u\in A}u\) of all elements is the unique nontrivial involution. For any permutations \(\alpha\) and \(\theta\) satisfying the \(k\)-complete identity, commutativity gives
\[P=\prod_{u\in A}\theta(u)=\Big(\prod_{u\in A}u\Big)\Big(\prod_{u\in A}\alpha(u)\Big)^k=P^{k+1}.\]
Therefore \(P^k=1\), impossible for odd \(k\). Combining necessity and sufficiency with Step 5 proves clause 4.

## Verification
The bundled `verify.py` exhaustively enumerates all permutations for 42 concrete finite semigroup/exponent combinations, independently tests the defining \(k\)-complete condition, and checks existence against the asserted classification in cyclic groups, two abelian-product groups, group-with-zero Clifford examples, Brandt matrix units, the symmetric inverse semigroup on two points, rectangular and left-zero bands, and a nilpotent pair. The verifier also confirms that the two-by-two Brandt inverse semigroup admits an ordinary \(1\)-complete mapping but no \(2\)-complete mapping. Execute using `python3 verify.py`. The recorded result is `VERIFY_OK 42 exhaustive semigroup/exponent tests; Brandt k=1 contrast`.

These exhaustive small examples are sanity checks only; the universal statements rest on Steps 1–6 and the classical finite-semigroup principal-factor theorem and abelian Hall–Paige theorem.

## Relationship to prior work
Araújo, Bentz, Cameron, Hendrey and Kinyon, *Complete Mappings of Semigroups*, Definition 15.1 and Problem 15.8, explicitly introduce \(k\)-complete mappings and ask for their existence classification in finite semigroups, Clifford semigroups and inverse semigroups. Their Theorem 10.1 classifies **ordinary** \(k=1\) complete mappings of finite inverse semigroups, allowing some non-Clifford examples; their Theorem 11.2 shows that an **involutive ordinary** complete mapping forces complete regularity. These do not imply the present all-permutation, every-even-\(k\) characterization or the \(k\ge2\) inverse-semigroup groupwise reduction. Their classical Hall–Paige citations supply the pre-existing group-theoretic input in Step 6. The ordinary mapping and Hall–Paige antecedents are not claimed as novel.

The semilattice-of-groups equivalence for Clifford semigroups is standard; its recent categorical reformulation by Caviglia, Faul, Manuell and Mesiti has no stated power-complete-mapping result. The new content is the Green-class power obstruction and its sharp parity-dependent existence consequences.

## Limitations
For odd \(k\), the theorem **does not** classify arbitrary noncommutative maximal groups or all completely regular non-inverse semigroups; the exact reduction in clause 3 leaves their group \(k\)-complete mapping problem as a genuine separate question. It does not count the number of mappings except structurally as a product of independent groupwise choices in Clifford semigroups. The group criterion in clause 4 uses the established Hall–Paige theorem, not an independent reproof of that result. Equivalent but unindexed older results cannot be completely excluded.

## References
1. J. Araújo, W. Bentz, P. J. Cameron, K. Hendrey, M. Kinyon, *Complete Mappings of Semigroups*, arXiv:2608.25092 (first posted 2026-08-25), especially Theorems 10.1 and 11.2, Definition 15.1 and Problem 15.8. https://arxiv.org/abs/2608.25092
2. J. N. Bray, Q. Cai, P. J. Cameron, P. Spiga and H. Zhang, *The Hall–Paige conjecture, and synchronization for affine and diagonal groups*, J. Algebra 545 (2020), 27–42, DOI:10.1016/j.jalgebra.2019.02.025.
3. E. Caviglia, P. F. Faul, G. Manuell, L. Mesiti, *Clifford semigroups and the monoidal Grothendieck construction*, arXiv:2607.12944 (2026), structural context only. https://arxiv.org/abs/2607.12944
