# Eight taxa are the sharp threshold for survival-dependent phylogenetic protection

## Finding

**Theorem (sharp first change and its unique eight-taxon shape).** Let \(T\) be a rooted non-plane full binary phylogenetic tree with \(n\ge 2\) leaves; every edge has length one. Each leaf independently survives with common probability \(p\in(0,1)\), except that a single chosen leaf \(x\) is guaranteed to survive. Let \(G_T(x;p)\) be the increase in expected **rooted** phylogenetic diversity, relative to the same model in which no leaf is guaranteed survival. Then:

1. If \(2\le n\le7\), at least one leaf maximizes \(G_T(x;p)\) for **every** \(p\in(0,1)\).
2. Among the \(23\) nonisomorphic rooted full binary tree shapes with eight leaves, exactly one has no leaf that remains optimal at every \(p\). Up to unordered child exchanges, this tree is

   ```text
   (((), ((), ())), ((), (((), ()), ((), ()))))
   ```

   with \( () \) a leaf and \((A,B)\) an internal vertex with child subtrees \(A,B\). Two leaves in its three-leaf child clade have ancestry-clade sizes \((3,2,1)\); four leaves in its five-leaf child clade have sizes \((5,4,2,1)\). Precisely the former two are optimal when
   \[p>\frac{3-\sqrt5}{2},\]
   and precisely the latter four are optimal when
   \[0<p<\frac{3-\sqrt5}{2}.\]
   All six are optimal at equality, and the other two leaves are never optimal in the open parameter interval.

Consequently eight is the least leaf number permitting the identity of a best single-taxon protector to depend on the common background survival probability, *purely through unit-edge rooted tree topology*.

## Assumptions and scope

A rooted full binary tree means every internal vertex has exactly two children; the two children are unordered. Tips are the only taxa and are labeled only to specify a choice; isomorphisms ignore labels and preserve the root. Every branch has exactly unit length (not a molecular-clock constraint). No branch length or extinction rate heterogeneity is allowed. For a surviving set \(S\) of taxa, rooted phylogenetic diversity \(\operatorname{PD}_T(S)\) is the number of edges in the minimal rooted subtree connecting all of \(S\) to the root; \(\operatorname{PD}_T(\varnothing)=0\). Exactly one surviving leaf is guaranteed under intervention. The benefit \(G_T(x;p)\) is the unconditional expected increase of rooted PD from protecting \(x\), relative to independent survival with no protection. Optimal means globally maximal among all leaves, allowing ties. The parameter range is the entire continuum \(0<p<1\).

## Proof

Write \(q=1-p\). For a leaf \(x\), each edge \(e\) on its root path subtends a clade with \(m_e\) leaves. Without protection, \(e\) is represented by surviving taxa if and only if at least one of the \(m_e\) descendants survives. Protecting \(x\) changes this event only if all \(m_e\) descendants would otherwise fail. This has probability \(q^{m_e}\). Edges not on the root path of \(x\) do not change. By linearity of expectation,

\[
G_T(x;p)=\sum_{e\text{ on root--}x\text{ path}}q^{m_e}.
\]

This is the rooted HEDGE marginal formula specialized to a shared extinction probability and unit edge lengths; the probabilistic edge identity itself is not claimed as new.

Let \(c_k(x)\) denote the number of path edges whose descendant clade has size \(k\), for \(1\le k\le n-1\), and let \(C_j(x)=\sum_{k=1}^jc_k(x)\). If for some leaf \(x\) and every leaf \(y\) one has \(C_j(x)\ge C_j(y)\) for each \(1\le j\le n-1\), then \(x\) is optimal for every \(q\in(0,1)\). Indeed, writing \(d_k=c_k(x)-c_k(y)\) and \(D_j=\sum_{k=1}^jd_k\), summation by parts gives

\[
G_T(x;p)-G_T(y;p)
=(1-q)\sum_{j=1}^{n-2}D_jq^j+D_{n-1}q^{n-1}\ge0.
\]

The following complete finite classification proves the minimum-size and uniqueness statements. Unordered rooted full binary shapes are constructed recursively: the single leaf is \( () \); for \(n\ge2\), take every \((A,B)\) with \(|A|+|B|=n\), \(|A|\le|B|\), and if sizes tie require \(A\le B\) in lexicographic canonical encoding. Every binary root splits uniquely into two smaller rooted binary shapes, and this normalization removes exactly the interchange symmetry; hence the construction is exhaustive and duplicate-free. For every generated shape, recursively list every tip and the sizes of the child clades encountered from its root to that tip, build its vector \((c_1,\ldots,c_{n-1})\), and test the cumulative inequalities against all other tips using integer arithmetic.

| Number of leaves | Number of shapes | Shapes without a cumulatively dominating leaf |
| ---: | ---: | ---: |
| 2 | 1 | 0 |
| 3 | 1 | 0 |
| 4 | 2 | 0 |
| 5 | 3 | 0 |
| 6 | 6 | 0 |
| 7 | 11 | 0 |
| 8 | 23 | 1 |

The sole eight-leaf shape lacking such a leaf has the exact encoding displayed in the theorem. These are complete finite computations with an inspectable executable enumerator supplied as `verify.py`, not a sample of possible trees. The exhaustive recurrence, canonicality rule, integer tests, and the complete count output suffice to reproduce the finite certificate.

For this exceptional shape, exactly four distinct root-to-tip clade-size profiles occur:

\[
(3,1),\quad(3,2,1),\quad(5,1),\quad(5,4,2,1).
\]

The \((3,2,1)\) profile strictly dominates \((3,1)\), and \((5,4,2,1)\) strictly dominates \((5,1)\). Hence only the two longer profiles can maximize. Their benefits are, respectively,

\[
L(q)=q+q^2+q^3,\qquad R(q)=q+q^2+q^4+q^5.
\]

Their exact difference factors as

\[
R(q)-L(q)=q^3(q^2+q-1).
\]

The strictly increasing quadratic \(q^2+q-1\) has exactly one root in \((0,1)\), at \(q_*=(\sqrt5-1)/2\). For \(q<q_*\), the two left-clade cherry leaves uniquely maximize; for \(q>q_*\), the four right-clade quartet leaves uniquely maximize. Replacing \(q=1-p\) yields the survival thresholds and tie case in the theorem. All seven-or-fewer shapes already have a universal best leaf, and all other eight-leaf shapes do too by cumulative dominance, completing the proof.

## Verification

The accompanying standard-library `verify.py` constructs every unordered rooted full binary shape with \(2\) through \(8\) leaves by an exhaustive recursive split and canonical child ordering. It calculates the full cumulative-dominance census and checks the unique exceptional encoding and the four exact clade-size profiles. A structurally separate check enumerates all \(2^7\) survival subsets of the *other* seven taxa for each of the eight candidate leaves at extinction probabilities \(q=1/4,1/2,3/4\). Exact rational subset enumeration agrees with the path-profile formula, including the exact signed differences \(-11/1024\), \(-1/32\), and \(135/1024\). Running `python verify.py` reproduces the byte-identical one-line JSON `certificate.json` (followed by a line feed). The certificate verifies finite enumeration and representative independent identities; the polynomial factorization and summation-by-parts argument justify statements for the full continuum.

## Relationship to prior work

Hartmann and Steel (2006) introduced broad Noah's Ark conservation optimization methods involving expected phylogenetic diversity and investment. Steel, Mimoto and Mooers (2007) derive the general rooted HED formula and the extinction-weighted HEDGE conservation benefit, including the edgewise probability identity used here. Martyn and colleagues (2012) give linear-time algorithms for HED indices on arbitrary much larger weighted trees, and demonstrate empirically that extinction assumptions alter species priorities. These sources cover the *method of evaluating a leaf* but do not, in material inspected, report the exact least number of **unit-edge rooted full binary** tips for a changing global optimizer, the uniqueness of its exceptional eight-tip shape, or its golden-ratio threshold. The present contribution is only that discrete sharp classification, not the established expected-PD formula, HED concept, or generalized conservation algorithm. A complete reading of Hartmann and Steel (2006) was unavailable; see limitations.

## Limitations

The model deliberately uses a normalized unit edge length, which need not give equal root-to-tip distances, and is not asserted to represent a time-calibrated phylogeny. Arbitrary unequal lengths, nonbinary trees, correlated losses, taxon-specific risks, multiple protection decisions, nonrooted PD, and conservation costs beyond a single identical intervention are outside scope. The seven/eight-taxon classification is exact within these hypotheses, not a universal statement about all phylogenies. The originality comparison is best-knowledge rather than proof of uniqueness across all publications; a mathematically equivalent classification in older conservation-index literature remains a residual bibliographic possibility. Independent scientific audit has not been carried out.

## References

1. Hartmann, K. and Steel, M. (2006), “Maximizing Phylogenetic Diversity in Biodiversity Conservation: Greedy Solutions to the Noah's Ark Problem,” *Systematic Biology* **55**, 644–651, published 2006-08-01, https://doi.org/10.1080/10635150600873876 .
2. Steel, M., Mimoto, A. and Mooers, A. Ø. (2007), “Hedging Our Bets: The Expected Contribution of Species to Future Phylogenetic Diversity,” *Evolutionary Bioinformatics* **3**, 237–244, published 2007-09-25, https://doi.org/10.1177/117693430700300024 ; full text https://pmc.ncbi.nlm.nih.gov/articles/PMC2684137/ .
3. Martyn, I., Kuhn, T. S., Mooers, A. Ø., Moulton, V. and Spillner, A. (2012), “Computing evolutionary distinctiveness indices in large scale analysis,” *Algorithms for Molecular Biology* **7**, article 6, published 2012-04-13, https://doi.org/10.1186/1748-7188-7-6 .
