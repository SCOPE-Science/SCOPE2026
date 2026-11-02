# Review of the weight-two deletion-code theorem

## Correctness — PASS

A two-one word is uniquely parametrized by \((a,b)\) with the original ones at \(a,b+1\). Deletion of one yields the one-position outputs \(a,b\); deletion of zero yields at most three explicitly classified two-position outputs. For any correcting code with \(L\) adjacent-one words and \(E\) other words, disjoint one-position outputs force \(L+2E\le n-1\). Adjacent adjacent-one words also share a zero-deletion output, bounding \(L\le\lceil(n-1)/2\rceil\). The stated explicit code meets the resulting integer bound; its shadows are disjoint by parity and spacing. All endpoints, including \(n=2\), are covered. The shipped program recomputes literal deletion balls and small exact graph optima. The proof, not the finite program, establishes the all-length conclusion.

## Originality — PASS, with residual uncertainty

The most relevant reviewed primary work is Cullina–Kulkarni–Kiyavash (2012, arXiv:1211.4056; ISIT 2012), which solves the optimal-coloring problem on constant-weight one-deletion graphs and explicitly distinguishes chromatic number from independence number. The claim here is the exact independence number \(\alpha(L_{1,n,2})\), plus a matching all-length construction, not their coloring statement. No (2019, DOI:10.3390/e21121202) gives general independent-set and MILP upper-bound formulations for the unrestricted code; these do not imply the weight-two exact formula. Focused searches for the formula, its graph aliases, and its coding interpretation did not locate a covering assertion. Search absence is not novelty proof; an older or unindexed specialization remains possible. No independent literature audit has been performed.

## Value — PASS

The optimum capacity of the smallest nontrivial constant-composition binary deletion channel is a natural exact coding invariant. The result holds for every block length, gives an explicit optimal family, and proves an exact finite-length bound rather than re-computing isolated small tables. Its \(3n/4+O(1)\) leading size exhibits a notable departure from the roughly \(n/2\)-sized average fixed-weight residue classes of standard deletion-syndrome constructions. It supplies both a tractable tight combinatorial packing model and a reproducible benchmark for constrained deletion codes.

## Literature and limitations

Checked primary materials: A. No (2019), accessible publisher sections and conclusions (later full reload rate-limited); Cullina–Kulkarni–Kiyavash (2012), accessible arXiv full text and the relevant conference PDF theorem page. The exact claim may still be an implicit corollary or be stated elsewhere under different notation; no general nonbinary or unrestricted optimum follows. Independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
