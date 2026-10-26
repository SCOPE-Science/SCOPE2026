# Complete fifth-order binary universal-cycle deletion spectrum

## Finding

Let \(\mathcal A=\{0,1\}\), and let \(F\subseteq\mathcal A^5\) be a set of exactly \(s\) distinct forbidden length-five words, where \(0\le s\le32\). A *universal cycle* for \(\mathcal A^5\setminus F\) is a circular word of length \(32-s\ge5\) whose cyclic factors of length five are precisely the surviving words, each occurring once. Write \(c_s\) for the number of forbidden sets having a universal cycle. Then

\[
 \Pr_F(\text{universal cycle})=\frac{c_s}{\binom{32}{s}},\qquad 0\le s\le32,
\]

with the convention that \(c_s=0\) for \(s>27\). The *entire exact spectrum* of \(c_s\), indexed by \(s=0,1,\ldots,32\), is

\[
(1,2,2,4,8,14,26,38,56,86,126,166,199,230,254,250,240,204,168,130,98,68,51,30,20,12,9,6,0,0,0,0,0).
\]

For each value of \(s\), the following table also gives \(b_s\), the number of deletion sets whose corresponding directed graph is balanced (Eulerian degree condition), independently of its connectivity.

| Deleted words \(s\) | Universal-cycle sets \(c_s\) | Balanced sets \(b_s\) |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 2 | 2 |
| 2 | 2 | 2 |
| 3 | 4 | 4 |
| 4 | 8 | 8 |
| 5 | 14 | 16 |
| 6 | 26 | 30 |
| 7 | 38 | 46 |
| 8 | 56 | 72 |
| 9 | 86 | 118 |
| 10 | 126 | 190 |
| 11 | 166 | 276 |
| 12 | 199 | 358 |
| 13 | 230 | 454 |
| 14 | 254 | 582 |
| 15 | 250 | 734 |
| 16 | 240 | 814 |
| 17 | 204 | 734 |
| 18 | 168 | 582 |
| 19 | 130 | 454 |
| 20 | 98 | 358 |
| 21 | 68 | 276 |
| 22 | 51 | 190 |
| 23 | 30 | 118 |
| 24 | 20 | 72 |
| 25 | 12 | 46 |
| 26 | 9 | 30 |
| 27 | 6 | 16 |
| 28 | 0 | 8 |
| 29 | 0 | 4 |
| 30 | 0 | 2 |
| 31 | 0 | 2 |
| 32 | 0 | 1 |

In particular, exactly \(6600\) of the \(2^{32}\) possible forbidden subsets satisfy balance; not all such subsets admit a universal cycle. At \(s=5\), for example, \(16\) sets satisfy balance but only \(14\) have a universal cycle. At \(s=27\), the six valid sets are the complements of the six primitive binary necklaces of length five, each viewed as a set of five successive cyclic length-five factors.

## Assumptions and scope

The alphabet is fixed and labeled binary. The order is exactly five, not arbitrary order; every forbidden set of a given cardinality is equally likely. Circular words are not quotiented by alphabet complementation or reversal; the count is of forbidden *sets*, not of how many distinct universal cycles each set may admit. A universal cycle is required to have at least five positions, as in the motivating counting convention. This restriction explains zero entries after \(s=27\), even if fewer than five remaining edges form a shorter directed circuit.

## Proof

**Graph criterion.** Consider the order-four binary de Bruijn digraph \(G\) with vertices all sixteen binary strings of length four. For each five-bit word \(e=e_1e_2e_3e_4e_5\), there is a directed edge from its first four bits to its final four bits. After deleting exactly the edges indexed by \(F\), a cyclic Eulerian traversal of all remaining edges exists exactly when (i) every active vertex has equal indegree and outdegree, (ii) all vertices incident to surviving edges lie in one weakly connected component, and (iii) at least five edges remain. These are precisely the required universal-cycle conditions, by reading one appended bit per traversed edge. For a balanced directed graph, weak connectivity on the nonisolated vertices is equivalent to existence of an Eulerian circuit. This remains correct in the presence of the two loops.

**Exhaustive, bounded certificate.** Fix an ordering of the thirty-two five-bit edges by binary integer value \(0\) through \(31\). Encode a deletion set by a bit vector \(z\in\{0,1\}^{32}\). Its integer degree-balance equations imply the sixteen incidence equations over \(\mathbb F_2\). The incidence matrix of the underlying connected graph has rank \(15\) over \(\mathbb F_2\); its nullspace therefore has dimension \(17\). Gauss elimination constructs an explicit nullspace basis. The program `verify_parity.py` visits all \(2^{17}=131072\) nullspace vectors, selects exactly those satisfying every *integer* indegree-outdegree equation, and applies the preceding Eulerian connectivity criterion. This visits every possible balanced deletion set exactly once; it does not assert that parity alone implies balance. It yields precisely the thirty-three \(b_s\) and \(c_s\) values in the table.

**Independent complete enumeration.** The separately implemented `verify_mitm.py` partitions the thirty-two edge indices into two sets of sixteen. For every subset of each half it computes the entire signed divergence vector of the sixteen vertices. Two halves give a balanced deletion exactly when their divergence vectors sum to zero. The second program joins all such pairs, uses an independently implemented disjoint-set connectivity check, and obtains the same complete thirty-three coefficients, including exactly \(6600\) balanced candidates. Because every \(32\)-edge subset has exactly one half-and-half representation, this is an independent exhaustive proof of the finite enumeration. The code uses exact integers and contains the expected coefficients, which are recomputed and asserted upon execution.

## Verification

Run `python3 verify_parity.py` and `python3 verify_mitm.py` from a folder containing the two bundled scripts; neither needs third-party dependencies or external files. The first prints `PARITY_ORDER5_UNIVERSAL_CYCLE_PASS basis=17 balanced=6600`, and the second prints `MITM_ORDER5_UNIVERSAL_CYCLE_PASS 6600 balanced` followed by the full coefficient vectors. Both programs were executed on the accompanying source files and agreed coefficient-for-coefficient. The first exhausts a \(17\)-dimensional parity kernel; the second independently exhausts and matches all pairs of \(16\)-edge-half signatures. The graph criterion is proved above, not inferred from sample outputs.

The output concerns existence, not the number of different Eulerian circuits for each retained edge set. The nullspace enumeration deliberately discards parity-valid but integer-unbalanced sets, and the weak-connectivity test disregards isolated vertices. No extrapolation to other orders or alphabets follows.

## Relationship to prior work

Chen, Kitaev, and Sun (initial public preprint 2019; journal 2020) formulated the exact probabilities \(P_c(n,k,s)\), computed binary values for orders two, three, and four (their Tables 1–3), gave exact arbitrary-order answers for one or two deletions, and provided general lower bounds for larger deletion counts. Theorem 5 specifically supplies lower bounds for the binary case of order at least five, rather than this complete order-five coefficient spectrum. The current table therefore addresses the first binary order absent from their finite tables, for every deletion cardinality. The standard Eulerian-circuit/de Bruijn correspondence is used, not claimed as new. The 2019/2020 paper and its reference list were inspected in full-text form; the finite table is the additional enumerative result.

## Limitations

This is an exact, finite fifth-order result. It does not establish an order-uniform formula, an arbitrary-alphabet analogue, or an exact universal-*word* (linear) spectrum. Counts arise from two explicitly complete finite enumerations, rather than a closed-form expression for the coefficients. An independently published equivalent table may exist under circuit-subgraph or edge-deletion terminology and would supersede any originality assertion. The computations can be repeated using the two self-contained bundled programs.

## References

1. H. Z. Q. Chen, S. Kitaev, and B. Y. Sun, *On the probability of existence of a universal cycle or a universal word for a set of words*, arXiv:1908.01116 (first public 2019-08-03); journal version *Lower Bounds, and Exact Enumeration in Particular Cases, for the Probability of Existence of a Universal Cycle or a Universal Word for a Set of Words*, *Mathematics* 8 (2020), 778, DOI:10.3390/math8050778. Lawful open-access full text at https://strathprints.strath.ac.uk/72338/1/Chen_etal_Mathematics_2020_Lower_bounds_and_exact_enumeration_in_particular_cases.pdf .
2. N. G. de Bruijn and T. van Aardenne-Ehrenfest, classical circuit enumeration correspondence; standard Eulerian circuit criterion as used in Reference 1, Section 1.
