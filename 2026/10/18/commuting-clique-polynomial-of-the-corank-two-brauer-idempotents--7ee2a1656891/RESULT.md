# Commuting-clique polynomial of the corank-two Brauer idempotents

## Finding

For every integer \(n\ge 2\), let \(B_n\) be the Brauer matching monoid on \(n\) upper and \(n\) lower labelled points. Multiplication concatenates diagrams and discards closed middle components. Let
\[
 E_n=\{e\in B_n:e^2=e,\ \operatorname{rank}(e)=n-2\}.
\]
Let \(P_n(z)\) count **unordered subsets**, including the empty subset, of distinct elements of \(E_n\) that commute pairwise, with \(z\) recording the subset size. Then
\[
 P_n(z)=\sum_{\substack{a,b\ge 0\\2a+3b\le n}}
 \frac{n!}{2^a a!\,b!\,(n-2a-3b)!}z^{a+b},
 \qquad
 \sum_{n\ge0}P_n(z)\frac{u^n}{n!}
 =\exp\!\left(u+\frac{zu^2}{2}+zu^3\right).
\]
For the generating series only, define \(P_0(z)=P_1(z)=1\). In particular, the maximal subset size is \(\lfloor n/2\rfloor\). The number of subsets attaining that size is
\[
 \begin{cases}
 \displaystyle \frac{n!}{2^k k!},&n=2k,\\[3pt]
 \displaystyle \frac{n!n}{2^k k!},&n=2k+1.
 \end{cases}
\]

The structural statement underlying all these formulas is: **two distinct corank-two idempotents commute if and only if their nonvertical supports are disjoint**. This gives the complete commuting-compatibility graph and not merely a count of individual idempotents.

## Assumptions and scope

Write the upper and lower point sets as \(\{1,\ldots,n\}\) and \(\{1',\ldots,n'\}\). A Brauer diagram is a perfect matching of their union, with multiplication by horizontal concatenation and deletion of components disjoint from the external boundaries. Its rank is the number of upper-to-lower matching edges (transversals).

For distinct labels \(a,b\), the **pair projection** \(p_{ab}\) has upper cup \(\{a,b\}\), lower cap \(\{a',b'\}\), and vertical transversals \(i\leftrightarrow i'\) at all other labels; its support is \(\{a,b\}\). For three distinct labels \(a,b,c\), the **triangle idempotent** \(t_{abc}\) has upper cup \(\{a,b\}\), lower cap \(\{b',c'\}\), transversal \(c\leftrightarrow a'\), and vertical transversals outside \(\{a,b,c\}\); its support is \(\{a,b,c\}\). Six different triangle idempotents occur on each unordered triple of labels.

We consider only monoid idempotents of rank exactly \(n-2\), not linear combinations of Brauer-algebra basis diagrams and not idempotents of other ranks. Disjoint support means set-theoretically disjoint subsets of the label set.

## Proof

**1. Exhaustion of the idempotents in the stratum.** Every diagram of rank \(n-2\) has exactly one upper cup \(I\), exactly one lower cap \(J\), each a two-element subset of labels, and a bijection between their respective \(n-2\) complements. If \(I\cap J=\varnothing\), diagram squaring joins the two independent middle cups and removes two transversals, so the square has rank \(n-4\) and the diagram cannot be idempotent. For \(I\cap J\ne\varnothing\), the middle cup--cap pairing connects every external transversal of the first diagram to a unique external transversal of the second. It thereby induces a fixed bijection \(\theta:J^c\longrightarrow I^c\) for this prescribed upper-cup/lower-cap pair. If a diagram has transversal bijection \(\sigma:I^c\longrightarrow J^c\), the square has transversal bijection \(\sigma\circ\theta\circ\sigma\) (using functional composition, from upper to lower). The equality \(\sigma\circ\theta\circ\sigma=\sigma\), with \(\sigma\) bijective, forces \(\sigma=\theta^{-1}\). Hence there is exactly one idempotent for every ordered pair \((I,J)\) with nonempty intersection. If \(I=J\) this is \(p_{ab}\), while if \(I=\{a,b\}\) and \(J=\{b,c\}\), it is \(t_{abc}\). Therefore there are \(\binom n2+6\binom n3\) distinct idempotents in the stratum; this individual-idempotent enumeration is antecedent literature and is not the new claim.

**2. Complete commutation criterion.** If two such idempotents have disjoint supports, their nonvertical matching edges occupy disjoint sets of labels. Every remaining strand is vertical. Concatenating in either order therefore produces exactly the same diagram, so the elements commute.

For the converse, any two distinct support sets of size two or three that intersect have union of cardinality at most five. Restriction of the two diagrams to this union, followed by the natural relabelling and vertical identity strands on any missing labels, preserves both possible products and their equality. Hence it suffices to check all distinct pairs of the above diagrams in \(B_5\). This is an **exact finite reduction valid for every \(n\)**, not an inference of an unbounded claim from samples. The exhaustive five-label certificate `verify_brauer_clique.py` implements matching concatenation from first principles, enumerates the 70 candidate idempotents, and compares both products for all \(\binom{70}{2}=2415\) distinct unordered pairs. Its complete support-size/intersection strata are:

| Support sizes | Intersection | Commuting | Number of pairs |
| --- | ---: | --- | ---: |
| 2 and 2 | 0 | yes | 15 |
| 2 and 2 | 1 | no | 30 |
| 2 and 3 | 0 | yes | 60 |
| 2 and 3 | 1 | no | 360 |
| 2 and 3 | 2 | no | 180 |
| 3 and 3 | 1 | no | 540 |
| 3 and 3 | 2 | no | 1080 |
| 3 and 3 | 3 | no | 150 |

The table totals 2415, exhausts every distinct candidate pair and has precisely 75 commuting pairs, all with disjoint supports. The certificate also verifies, independently by enumerating every perfect matching, that all corank-two idempotents of \(B_n\) are the claimed candidates for \(2\le n\le5\). The general exhaustion, however, rests on the bijection argument in step 1.

**3. Counting all commuting subsets.** By step 2, a commuting subset is uniquely a set of disjoint supported blocks, where each block is either an unordered pair carrying its unique projection or an unordered triple carrying one of six distinct triangle decorations. If there are \(a\) pair blocks and \(b\) triple blocks, then \(n-2a-3b\) labels are unused, and their number of decorated packings is
\[
 \frac{n!}{(2!)^a a!\,(3!)^b b!\,(n-2a-3b)!}\,6^b
 =\frac{n!}{2^a a!\,b!\,(n-2a-3b)!}.
\]
Such a subset contains \(a+b\) idempotents. Summing establishes the polynomial; the labelled exponential formula gives its exponential generating function.

**4. Maximum-sized subsets.** A subset of size \(k\) uses at least \(2k\) labels, so \(k\le\lfloor n/2\rfloor\), with equality attained using pair projections. For even \(n=2k\), all maximum subsets use \(k\) pairs, giving \(n!/(2^k k!)\). For odd \(n=2k+1\), either \(k\) pairs leave one unused label or \(k-1\) pairs accompany one decorated triple. Their sum is
\[
 \frac{n!}{2^k k!}+\frac{n!}{2^{k-1}(k-1)!}
 =\frac{n!n}{2^k k!}.
\]

## Verification

Run `python3 verify_brauer_clique.py` in the same directory as this document; only Python's standard library is needed. The code generates all matchings on up to ten endpoints, composes diagrams using union--find on three rows, checks idempotence, and independently validates each commuting pair in the complete five-label reduction. It then enumerates all disjoint-support commuting subsets for \(2\le n\le8\) without assuming the polynomial formula, and checks the resulting coefficient vectors against it.

The exact output ends with `VERIFY_OK_BRAUER_CORANK_TWO_CLIQUES`. The computed coefficient vectors for \(n=4,5,6\) are respectively \((1,30,3)\), \((1,70,75)\), and \((1,135,765,15)\). Both the exhaustive certificate and the proof of the universal five-label reduction are essential to step 2; finite checks by themselves would not settle the all-\(n\) statement.

## Relationship to prior work

Larsson (2006) and Dolinka--East--Evangelou--FitzGerald--Ham--Hyde--Loughlin (2014) study Brauer monoid idempotents and enumerate them in rank strata. Their individual-idempotent classifications and counts are acknowledged, including the corank-two count above. East--Gray (2014) study Graham--Houghton graphs and minimal idempotent generating sets for ideals of the Brauer and related monoids, a distinct generating-set invariant. Neither inspected primary source was found to give the exact pairwise commuting criterion or the all-size clique polynomial of a fixed Brauer rank stratum. An earlier result phrased as a classification of semilattices, commuting projection diagrams or decorated hypergraph packings could cover the same statement; no claim of exhaustive bibliographic uniqueness is made.

The planar Jones monoid is a proper submonoid of the Brauer monoid and admits a separate corank-two commuting-family analysis; the present decorated labelled-packing formula applies to the full **nonplanar** Brauer monoid and does not follow from the planar result.

## Limitations

The result concerns one fixed rank stratum and subsets of distinct idempotents, not tuples with repetition, products of those idempotents across rank strata, or all idempotents of \(B_n\). The formula is about diagram multiplication in the monoid, not the parameter-dependent multiplication in the Brauer algebra. The exact five-label certificate supplies a finite, reproducible local verification, while the unrestricted theorem depends on the proved support-reduction argument. The older Larsson thesis was accessible only at bibliographic/abstract level during the source comparison; an equivalent treatment there or elsewhere remains a specific literature-priority risk. Independent mathematical audit has not been performed.

## References

1. J. East and R. Gray, *Diagram monoids and Graham--Houghton graphs: Idempotents and generating sets of ideals*, first preprint 9 April 2014, arXiv:1404.2359, https://arxiv.org/abs/1404.2359 .
2. I. Dolinka, J. East, A. Evangelou, D. FitzGerald, N. Ham, J. Hyde and N. Loughlin, *Enumeration of idempotents in diagram semigroups and algebras*, first preprint 9 August 2014, arXiv:1408.2021, https://arxiv.org/abs/1408.2021 .
3. D. Larsson, *Combinatorics on Brauer-type semigroups*, Uppsala University Project Report 2006:3 (May 2006), https://www.diva-portal.org/smash/get/diva2%3A305049/FULLTEXT01.pdf .
