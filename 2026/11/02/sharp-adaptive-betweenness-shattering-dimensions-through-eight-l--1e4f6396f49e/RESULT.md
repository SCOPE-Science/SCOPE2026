# Sharp adaptive betweenness-shattering dimensions through eight labels

## Finding
For an integer \(n\geq3\), let \(\mathcal B_n\) be the class of ternary betweenness predicates of strict total orders on \([n]\). A query \((a,b,c)\), with pairwise distinct labels and the endpoints \(a,c\) regarded as unordered, returns one if \(b\) is strictly between \(a\) and \(c\). The exact Littlestone dimensions are
\[
\bigl(\operatorname{Ldim}(\mathcal B_n)\bigr)_{n=3}^{8}=(1,3,5,7,10,13).
\]
For every \(n\geq3\) there is a general upper bound
\[
\operatorname{Ldim}(\mathcal B_n)\leq 1+\left\lfloor\log_2\!\left(\frac{n!}{6}\right)\right\rfloor,
\]
and equality holds for every \(3\leq n\leq8\). Thus \(n=6\) is the first size at which the ordinary \(\lfloor\log_2|\mathcal B_n|\rfloor\) cardinality bound is not attained: the values at \(n=6,7,8\) are respectively \(7,10,13\), rather than \(8,11,14\). The first static/adaptive separation occurs already at \(n=4\), since
\[
\bigl(\operatorname{VCdim}(\mathcal B_n)\bigr)_{n=3}^{6}=(1,2,4,6)
\]
and the corresponding adaptive values are \((1,3,5,7)\).

The exact input sizes, adaptive dimensions, and cardinality bounds are:

| \(n\) | Distinct betweenness concepts | VC dimension (where computed) | Littlestone dimension | Cardinality bound | Positive-root bound |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 3 | 3 | 1 | 1 | 1 | 1 |
| 4 | 12 | 2 | 3 | 3 | 3 |
| 5 | 60 | 4 | 5 | 5 | 5 |
| 6 | 360 | 6 | 7 | 8 | 7 |
| 7 | 2520 | not asserted | 10 | 11 | 10 |
| 8 | 20160 | not asserted | 13 | 14 | 13 |

## Assumptions and scope
All labels are distinct, every underlying order is strict and complete, and only Boolean betweenness questions on three distinct labels are permitted. The two orders obtained by reversing an ordering define the same concept; no pairwise direction queries are available. VC dimension refers to shattered *fixed sets of ternary questions* and Littlestone dimension to complete depth-uniform adaptive binary trees with ternary questions at internal vertices. The result is an exact finite-range classification and a general upper bound; it asserts no exact adaptive formula for \(n\geq9\), no static formula for \(n\geq7\), and no identification-query optimality assertion.

## Proof
**Concepts and one-third root counting.** A strict total order \(\pi\) determines the predicate
\[
B_\pi(a,b,c)=1\quad\Longleftrightarrow\quad
\pi^{-1}(a)<\pi^{-1}(b)<\pi^{-1}(c)
\ \text{or}\ 
\pi^{-1}(c)<\pi^{-1}(b)<\pi^{-1}(a).
\]
Its reversal has the same predicate. Conversely the complete betweenness predicate determines the order up to reversal (a standard fact, recorded by Courcelle). Thus there are exactly \(n!/2\) concepts. In the \(n!\) orders, each of three labels is the middle one in precisely one third of the relative orders; after quotienting by reversal, precisely \(n!/6\) concepts answer one to every fixed ternary question. In any complete adaptive-shattering tree of depth \(d\geq1\), the positive child of the root must support \(2^{d-1}\) distinct leaf concepts. Therefore \(2^{d-1}\leq n!/6\), which proves the stated all-order upper bound.

**Matching trees through eight.** `certificates.json` explicitly stores a complete binary tree and a compatible concept witness at every leaf for each of the six asserted depths. The deterministic query enumeration is as follows: for each increasing triple \(a<b<c\), list in order the three middle-label questions \((a,b,c)\), \((b,a,c)\), \((a,c,b)\). Enumerate permutations lexicographically and retain one per reversal pair, namely those whose first label is numerically smaller than the last. For a depth-\(d\) certificate, `node_queries` is the breadth-first heap array of \(2^d-1\) zero-based query indices. Heap node one is the root; the left child \(2i\) corresponds to answer one and the right child \(2i+1\) to answer zero. `leaf_permutation_indices` is the corresponding array of \(2^d\) lexicographic canonical-permutation indices, in heap leaf order. Directly evaluate all prescribed questions on the permutation at every leaf. `verify_certificate.py` does precisely this using a separate evaluator and verifies that the leaf witnesses are distinct. The successful output is in `verification_output.txt`. Because all \(2^d\) binary paths are thereby witnessed, the six lower bounds follow, and matching the universal upper bound gives the exact values.

**Static dimensions through six.** The verifier also performs complete backtracking over sets of distinct questions. For a candidate support \(S\), it partitions the concept set by the answer vector on \(S\). When adjoining a new question, a support can remain shattered only if that query splits every existing nonempty answer cell into two nonempty cells. The implementation visits every strictly increasing query-index sequence which passes this necessary-and-sufficient test; any rejected prefix cannot extend to a shattered set. It obtains maximum support sizes \(1,2,4,6\) for \(n=3,4,5,6\), with explicit witness supports printed in `verification_output.txt`. This establishes the claimed static dimensions, including that all smaller label counts have no static/adaptive gap.

**First thresholds.** For \(n=3,4,5\), the positive-root bound equals the ordinary cardinality bound and is attained by the certified trees. At \(n=6\), \(|\mathcal B_6|=360\) permits cardinality depth eight, but every query has only \(120<128\) positive concepts and therefore forbids depth eight. The certified depth-seven tree attains the stronger bound. The same comparison proves the strict one-level cardinality deficit at seven and eight labels. At four labels, the exhaustive static support bound two and the certified depth-three adaptive tree exhibit the first static/adaptive gap.

## Verification
With Python 3 and no third-party modules, run:

```text
python build_witnesses.py --out certificates_rebuilt.json
python verify_certificate.py certificates_rebuilt.json
python verify_certificate.py certificates.json
```

`build_witnesses.py` uses integer bitsets and a memoized, exhaustive depth-feasibility recurrence, pruning states with fewer than \(2^d\) surviving concepts. `verify_certificate.py` does **not** trust this search: it directly checks every leaf path against canonical permutations, counts the positive concepts for each question, checks the root upper bounds, and independently traverses the static shattering search through six labels. Rebuilding produces exactly the same certificate bytes. The six adaptive certificates have respectively \(2,8,32,128,1024,8192\) distinct leaf-permutation witnesses. The largest uses \(8191\) query-labeled internal nodes on \(20160\) distinct concepts. These are finite, complete certificates; no extrapolation supplies the all-order bound.

## Relationship to prior work
Courcelle's *Betweenness of partial orders* (arXiv:2004.09777, 2020) states the appropriate ternary betweenness definition and uniqueness of linear order up to reversal; its main results concern axiomatization and reconstruction, not adaptive or static learning dimensions. Manurangsi and Rubinstein's *Inapproximability of VC Dimension and Littlestone's Dimension* (arXiv:1705.09517, 2017) provides the exact definitions and generic dimension-computation setting, but no betweenness-specific values. Peters and Procaccia's *Preference Elicitation as Average-Case Sorting* (AAAI 2021) studies pairwise comparison queries and expected sorting-query counts under ranking distributions, which differ from ternary betweenness and complete worst-case shattering trees. Prior comparison-query results for permutations do not imply these ternary-query values merely because both arise from total orders; an atomic betweenness question is a Boolean combination of pairwise comparisons, and Littlestone dimension is query-language-sensitive. Ran Raz's permutation VC dimension uses the ability to realize all restrictions to a selected set of labels, rather than shattering fixed Boolean midpoint questions, so it is a distinct invariant. The literature comparisons establish absence of implication from these inspected sources, not an exhaustive priority guarantee.

## Limitations
The large lower bounds rely on the specified executable finite certificates and their verified interpretation, not on short symbolic constructions for arbitrary \(n\). No result for nine or more labels is claimed beyond the universal upper bound. No completeness claim is made for all historical literature; independent mathematical audit has not been performed. The 2017 generic hardness results alone neither imply nor contradict the finite values here. This result concerns mistake-tree depth, not optimal number of active queries needed to identify the unknown ordering.

## References
1. P. Manurangsi and A. Rubinstein, *Inapproximability of VC Dimension and Littlestone's Dimension*, arXiv:1705.09517, first public 2017-05-26; Proceedings of Machine Learning Research 65 (2017), 1432–1460. https://arxiv.org/abs/1705.09517
2. B. Courcelle, *Betweenness of partial orders*, arXiv:2004.09777, first public 2020-04-21; RAIRO Theoretical Informatics and Applications 54 (2020), article 7. https://arxiv.org/pdf/2004.09777
3. D. Peters and A. D. Procaccia, *Preference Elicitation as Average-Case Sorting*, AAAI 35 (2021), 5647–5655. https://ojs.aaai.org/index.php/AAAI/article/view/16709/16516
4. R. Raz, *VC-dimension of sets of permutations*, Combinatorica 20 (2000), 241–255. https://doi.org/10.1007/s004930070023
