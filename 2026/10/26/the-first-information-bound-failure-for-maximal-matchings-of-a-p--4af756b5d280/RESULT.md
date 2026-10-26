# The first information-bound failure for maximal matchings of a path

## Finding

For each integer \(0\le m\le15\), let \(P_{m+1}\) be the path with \(m\) edges, indexed in order by \(1,\ldots,m\). Let \(\mathcal M_m\) be the Boolean concept class consisting of characteristic functions of **inclusion-maximal matchings** of this path, with the edges as query points. Put \(N_m=|\mathcal M_m|\). Then

\[
\operatorname{Ldim}(\mathcal M_m)=\lfloor\log_2 N_m\rfloor\quad(0\le m\le14),
\qquad
N_{15}=65,\quad\operatorname{Ldim}(\mathcal M_{15})=5<6=\lfloor\log_2 65\rfloor.
\]

Thus **15 edges (16 path vertices) is the smallest path size at which the cardinality upper bound on the optimal realizable online mistake count is not attained** for the concept class of inclusion-maximal matchings. This is a first-failure result, not a general dimension formula for longer paths.

The complete profile below specifies the finite claim. \(U_m=\lfloor\log_2 N_m\rfloor\).

| \(m\) | \(N_m\) | \(U_m\) | \(\operatorname{Ldim}\) |
|---:|---:|---:|---:|
| 0 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 |
| 2 | 2 | 1 | 1 |
| 3 | 2 | 1 | 1 |
| 4 | 3 | 1 | 1 |
| 5 | 4 | 2 | 2 |
| 6 | 5 | 2 | 2 |
| 7 | 7 | 2 | 2 |
| 8 | 9 | 3 | 3 |
| 9 | 12 | 3 | 3 |
| 10 | 16 | 4 | 4 |
| 11 | 21 | 4 | 4 |
| 12 | 28 | 4 | 4 |
| 13 | 37 | 5 | 5 |
| 14 | 49 | 5 | 5 |
| 15 | 65 | 6 | 5 |

## Assumptions and scope

A matching is a set of pairwise nonincident edges. It is **inclusion-maximal** if no further edge can be added while retaining the matching property; this is distinct from maximum-cardinality matching. Its indicator is a hypothesis on the \(m\)-edge ground set, and the unknown matching is fixed throughout the online game. Littlestone dimension is the largest depth of a complete binary decision tree whose internal nodes query edge membership, with every binary path realized by at least one fixed hypothesis. A singleton class has dimension zero. All vertices and edges are unweighted and unlabeled except for the stated edge order.

The result is finite and exhaustive for precisely \(0\le m\le15\). The checked base cases include the zero-edge path. Nothing is asserted about the first-failure status in a more general graph class or about the dimensions when \(m>15\).

## Proof

**1. Enumerating all maximal matchings.** Encode a matching as a binary word \(b_1\ldots b_m\) with \(b_i=1\) iff edge \(i\) is selected. Since successive edges meet, the word contains no `11`. Maximality is exactly the condition that every zero has a neighboring one, with only existing neighbors used at the endpoints. These conditions define the concept family without omissions or spurious hypotheses. For \(m\ge3\), the leftmost selected position is either 1 or 2: selecting 1 reduces the remainder to a maximal matching of the \((m-2)\)-edge suffix; selecting 2 reduces it to the \((m-3)\)-edge suffix. Thus

\[
N_m=N_{m-2}+N_{m-3}\quad(m\ge3),\qquad (N_0,N_1,N_2)=(1,1,2).
\]

This gives the displayed sizes and \(N_{15}=65\), independently of any shattering calculation.

**2. The cardinality upper bound.** A shattered tree of depth \(d\) has \(2^d\) root-to-leaf answer sequences, and a fixed hypothesis can realize at most one. Therefore \(\operatorname{Ldim}(\mathcal C)\le\lfloor\log_2|\mathcal C|\rfloor\) for every nonempty finite concept class. This proves the required upper bounds for \(m\le14\) and \(\operatorname{Ldim}(\mathcal M_{15})\le6\).

**3. Constructive lower bounds.** The accompanying `shattered_trees.json` gives an explicit complete shattered tree of depth \(U_m\) for each \(m\le14\), and a depth-five tree for \(m=15\). At every internal node, `query` is a 1-based edge index, with `zero` and `one` subtrees. At every leaf, `witness` is the integer bit mask of a maximal matching realizing the entire root-to-leaf answer sequence. The standalone `verify.py` validates the membership condition independently at every leaf, and `independent.cpp` separately computes all 16 dimensions using a different enumeration procedure and recursive minimax implementation. These finite certificates prove the lower bounds without induction beyond the stated range.

**4. Obstruction to depth six at 15 edges.** We use only necessary branch cardinalities, not an unverified assertion that a search returned no tree. A depth-six root requires at least 32 hypotheses on **each** answer branch. Direct counts from the binary-word characterization show that among the 15 possible first queries, only edge 4 and its reflected edge 12 have this property: each divides the 65 maximal matchings into 32 yes and 33 no. By path reflection it suffices to consider query 4.

Its 33-hypothesis `no` branch would have to shatter depth five. Such a branch first needs at least 16 hypotheses on both sides. A direct count over the 15 edge queries shows that **only** edge 12 can do this, giving 16 versus 17. The 17-hypothesis branch with edge 12 also absent would then need depth four. To continue, it needs a split of at least eight on both sides; **only** edge 8 gives such a split, of sizes 9 and 8. In each resulting version space, every edge query has a smaller side of size at most three. Consequently neither can shatter depth three, since even the first query of a depth-three tree requires four hypotheses on either side. Therefore the 17-class branch cannot shatter depth four, the 33-class branch cannot shatter depth five, and the original class cannot shatter depth six.

The exact branch-count assertions are independently and exhaustively recalculated in `verify.py`, using the complete explicitly listed family `maximal_matchings_15.txt` as a human-inspectable finite certificate. The printed `DEPTH_SIX_OBSTRUCTION` gives all candidate split locations at the three successive thresholds and checks that each last subgroup has maximum smaller-side size three. This proves \(\operatorname{Ldim}(\mathcal M_{15})\le5\). Together with the depth-five witness it proves equality. Since every smaller \(m\) attains its upper bound, 15 is the first failure.

## Verification

Run in one directory using standard tools:

```sh
python3 verify.py > python_output.txt
c++ -std=c++17 -O2 independent.cpp -o independent
./independent > cpp_output.txt
```

The supplied output files were produced by these commands. Python enumerates all \(2^m\) binary masks through \(m=15\), filters by the two exact matching conditions, evaluates the finite game recurrence and checks every supplied certificate leaf; the C++17 implementation independently enumerates conflict-free words recursively and applies a separate exact game recurrence on `std::bitset<128>`. The two implementations agree on every count and dimension. The Python final line is `ALL_CHECKS_PASS` and the C++ final line is `CPP_INDEPENDENT_PASS`. The count table, source files, explicit trees, and branch-count obstruction remain inside this package; no outside program or inaccessible path is needed.

## Relationship to prior work

Manurangsi, *Improved Inapproximability of VC Dimension and Littlestone's Dimension via (Unbalanced) Biclique*, first publicly posted November 2, 2022, studies exact/approximate computation of these dimensions for explicit general concept classes and their complexity. Its introduction and main results establish that general-dimensional computation is a nontrivial problem; its biclique reductions do **not** specify the maximal-matching path family or this first information-bound failure. The known Padovan recurrence for the number of maximal independent sets of a path gives the matching-count sequence via the line graph, but counting the hypotheses does not determine their adaptive shattering depth. Here the new assertion concerns the first nonattained bound, with explicit adaptive certificates and an obstruction for 15 edges. The restricted search and comparisons do not establish unconditional historical priority.

## Limitations

This is a finite first-failure theorem through 15 edges, not a formula or asymptotic claim for larger paths, nor a statement about all forests or all maximal matchings of arbitrary graphs. The branch-size obstruction uses exact finite counts that have independently reproducible exhaustive checks. Historical coverage beyond the inspected sources and database searches remains a priority risk.

## References

1. P. Manurangsi, *Improved Inapproximability of VC Dimension and Littlestone's Dimension via (Unbalanced) Biclique*, arXiv:2211.01443, first posted 2022-11-02; ITCS 2023, DOI: 10.4230/LIPIcs.ITCS.2023.85. https://arxiv.org/abs/2211.01443
2. Z. Füredi, *The number of maximal independent sets in connected graphs*, Journal of Graph Theory **11** (1987), 463–470, DOI: 10.1002/jgt.3190110403. https://doi.org/10.1002/jgt.3190110403 (general enumeration context, not an adaptive-dimension calculation).
3. M. Krivelevich, T. Mészáros, P. Michaeli, and C. Shikhelman, *Greedy maximal independent sets via local limits*, Random Structures & Algorithms **64** (2024), 986–1015, first published 2023-12-18, DOI: 10.1002/rsa.21200. https://doi.org/10.1002/rsa.21200 (greedy-MIS context rather than this exact online-shattering problem).
