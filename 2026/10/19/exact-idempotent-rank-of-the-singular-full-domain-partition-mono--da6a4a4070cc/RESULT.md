# Exact idempotent rank of the singular full-domain partition monoid

## Finding

**Theorem.** Let \(n\ge3\). In the partition monoid \(\mathcal P_n\) on \([n]\sqcup[n]'\), let \(\mathcal P_n^{\mathrm{fd}}\) be the submonoid of partitions in which every upper vertex lies in a block meeting the lower row. Set \(I_n=\mathcal P_n^{\mathrm{fd}}\setminus\mathcal S_n\). Then
\[
\operatorname{idrank}(I_n)=2\binom{n}{2}=n(n-1).
\]
Moreover, if \(D\) is any strongly connected tournament on \([n]\), a minimum idempotent generating set is
\[
\{e_{ij}:1\le i<j\le n\}\ \cup\
\{t_{i\to j}:i\to j\text{ is an arc of }D\}.
\]
For \(n=2\), \(\operatorname{idrank}(I_2)=3\).

## Assumptions and scope

Diagram multiplication identifies the lower row of the left partition with the upper row of the right partition and retains only the exterior rows after taking connected components. The *rank* of a partition is its number of transversal blocks (blocks meeting both rows). All elements in \(\mathcal P_n^{\mathrm{fd}}\) have full upper domain, and their only rank-\(n\) elements are permutations.

For distinct \(i,j\), write \(e_{ij}\) for the equivalence projection having a transversal block \(\{i,j,i',j'\}\) and transversal pairs \(\{k,k'\}\) elsewhere. Write \(t_{i\to j}\) for the transformation diagram of the idempotent map sending \(i\) to \(j\) and fixing every other vertex; it has the top pair \(\{i,j\}\), discrete lower-row equivalence and one lower singleton. A generating set of \(I_n\) means semigroup generation (nonempty products); the rank excludes adding the ambient identity.

## Proof

**Rank-\(n-1\) classification.** Let \(a\in\mathcal P_n^{\mathrm{fd}}\) have rank \(n-1\). Its upper partition has exactly one two-element class \(P=\{i,j\}\), and every other upper class is a singleton. There are \(n-1\) transversal blocks containing the \(n\) lower vertices, so precisely two possibilities occur: the extra lower vertex either lies in one of those transversal blocks, or constitutes a lower-only singleton. In the latter case the lower row is discrete, and the partition is a rank-\(n-1\) transformation; its idempotents are exactly the two maps \(t_{i\to j}\) and \(t_{j\to i}\). In the former case the partition has a unique two-element lower class \(Q\). Idempotence preserves rank, requiring \(P=Q\): if they differed, gluing the two diagrams would merge distinct transversal blocks and decrease the rank. With \(P=Q\), the diagram induces a permutation of the \(n-1\) transversal blocks. Its square equals itself only when that permutation is the identity, giving precisely \(e_{ij}\). Consequently the entire rank-\(n-1\) idempotent layer is
\[
\{e_{ij},t_{i\to j},t_{j\to i}:1\le i<j\le n\}.
\]

**Lower bound.** The rank of a product of full-domain partitions is at most the rank of each factor. To express a target of rank \(n-1\) as a product of singular idempotents, every factor must therefore belong to the layer just classified. If a product of rank-\(n-1\) factors retains rank \(n-1\), its lower-row equivalence equals that of its rightmost factor: the only way to add identifications between distinct lower transversal blocks would lower the rank, while lower-only singletons of the final factor cannot become joined. Since \(e_{ij}\) is the sole rank-\(n-1\) idempotent with its particular nontrivial lower equivalence, each \(e_{ij}\) must itself be a generator. This forces at least \(\binom{n}{2}\) generators.

Fix now an unordered pair \(P=\{i,j\}\). Both \(t_{i\to j}\) and \(t_{j\to i}\) have top kernel \(P\). A rank-preserving product has the top kernel of its first factor: any additional merging of distinct upper transversal blocks would lower rank. Hence a product representing \(t_{i\to j}\) must begin with a generator from \(\{e_{ij},t_{i\to j},t_{j\to i}\}\). Suppose neither of the two transformations occurs in the generating set. The first factor is then \(e_{ij}\). For any rank-\(n-1\) factor \(b\), the product \(e_{ij}b\) retains rank \(n-1\) only if the upper kernel of \(b\) is also \(P\); otherwise the gluing joins two formerly distinct transversal blocks. Under the supposition the only available factor with that kernel is \(e_{ij}\), and \(e_{ij}^2=e_{ij}\). Thus no rank-preserving word starting at \(e_{ij}\) can reach either transformation. This contradiction forces at least one of \(t_{i\to j}\) and \(t_{j\to i}\) for each pair. These required generators are distinct from the \(e_{ij}\)'s, yielding the bound \(2\binom{n}{2}\).

**Matching upper bound.** By Howie's idempotent-generation theorem for singular transformations, the defect-one transformation idempotents oriented along any strongly connected tournament generate \(\operatorname{Sing}(\mathcal T_n)\) for \(n\ge3\). Such tournaments exist in every size \(n\ge3\): start with a directed triangle and repeatedly insert a vertex receiving one arc from, and sending one arc into, the old strongly connected tournament, orienting the remaining new arcs arbitrarily. The equivalence projections \(e_{ij}\) generate the finite join semilattice \(\mathcal E_n\) of equivalence partitions, with the empty product interpreted as its identity. By Carroll–East–Fresacher, Proposition 6.6,
\[
I_n=\operatorname{Sing}(\mathcal T_n)\,\mathcal E_n.
\]
When the semilattice factor is the identity, the product already belongs to the semigroup generated by the chosen transformations; otherwise it is a nonempty product of the chosen projections. Thus the proposed \(2\binom{n}{2}\) idempotents generate all of \(I_n\), proving equality.

For \(n=2\), precisely three full-domain partitions are singular, and their multiplication satisfies \(ab=b\) for every pair of these three elements. Each is idempotent and no one is generated by the others in a right-zero semigroup; hence the idempotent rank is \(3\). \(\square\)

## Verification

A standalone Python 3 checker accompanies this statement. It represents partition diagrams by canonical restricted-growth tuples, implements three-row diagram multiplication using disjoint-set unions, enumerates all full-domain diagrams of rank \(n-1\), determines their actual idempotents, and computes the generated rank-\(n-1\) subsemigroup for explicit strong-tournament generator sets. It confirms for \(n=3,4,5\) that the rank-\(n-1\) layer has respectively \(36,360,3600\) elements, that exactly \(9,18,30\) of them are idempotent, and that the proposed \(6,12,20\) generators produce the whole layer. It also verifies the three-element right-zero multiplication for \(n=2\). These are **finite checks**; the infinite-family claim follows from the mathematical argument and cited structural theorems, not the experiments.

Reproduce from a directory containing the embedded `check_idrank.py` file using `python3 check_idrank.py`. Expected final line: `CHECKER_OK`.

## Relationship to prior work

East and Gray (2020 preprint, revised 2021), Section 4.5, asked whether singular full-domain partitions are idempotent generated and requested ranks and idempotent ranks of their proper ideals. Carroll, East, and Fresacher (2025), Theorem 3.16, established idempotent generation and supplied the full set of \(3\binom{n}{2}\) rank-\(n-1\) idempotents as generators, while Proposition 6.6 proved the singular-transformation/equivalence factorization. Those results imply an upper bound but do not state the exact minimum \(2\binom{n}{2}\), which follows here from a separate rank-preserving obstruction plus the tournament reduction. Howie's 1978 theorem supplies the classical transformation-semigroup component; the full transformation monoid is not the full-domain partition monoid. East–Gray (2017) studies the full partition monoid, which is a different ambient semigroup.

## Limitations

Only the largest proper ideal \(I_n\) is treated; smaller rank ideals and complete classification/counting of *all* minimum generating sets are not claimed. The argument uses the published factorization and classical strong-tournament generation theorem. The two full-domain source papers were inspected in accessible complete HTML form; Howie's original 1978 publisher-hosted full text was not accessible here, so its theorem was cross-checked against published abstracts and secondary descriptions. Unindexed equivalent prior work cannot be excluded by search alone.

## References

1. J. East and R. D. Gray, *Ehresmann theory and partition monoids*, arXiv:2011.00663 (first public 2020-11-02), Section 4.5: https://arxiv.org/html/2011.00663v2.
2. L. Carroll, J. East, and M. Fresacher, *Presentations for semigroups of full-domain partitions*, arXiv:2507.05497 (first public 2025-07-07), Theorem 3.16 and Proposition 6.6: https://arxiv.org/html/2507.05497v1.
3. J. M. Howie, *Idempotent generators in finite full transformation semigroups*, Proc. Roy. Soc. Edinburgh A **81** (1978), 317–323, DOI:10.1017/S0308210500010647.
4. J. East and R. D. Gray, *Diagram monoids and Graham–Houghton graphs: idempotents and generating sets of ideals*, J. Combin. Theory A **146** (2017), 63–128, DOI:10.1016/j.jcta.2016.09.001.
