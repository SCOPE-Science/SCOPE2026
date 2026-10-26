# The first factorial information-bound failure for comparison shattering of permutations

## Finding

For each integer \(1\le n\le7\), let \(\mathcal H_n\) consist of the \(n!\) Boolean comparison concepts arising from all strict total orders on \([n]\). Its instance domain is \(X_n=\{\{a,b\}:1\le a<b\le n\}\); the concept for a permutation \(\pi\), written as an ordered list of the labels, answers \(1\) to \(\{a,b\}\) precisely when \(a\) precedes \(b\) in \(\pi\).

The exact deterministic Littlestone dimensions are

\[
(\operatorname{Ldim}(\mathcal H_1),\ldots,\operatorname{Ldim}(\mathcal H_7))
=(0,1,2,4,6,9,11).
\]

In particular, the usual hypothesis-count bound \(\operatorname{Ldim}(\mathcal H_n)\le\lfloor\log_2(n!)\rfloor\) is attained for every \(1\le n\le6\), but **fails for the first time at seven labels**:

\[
\operatorname{Ldim}(\mathcal H_7)=11<12=\lfloor\log_2(7!)\rfloor.
\]

For comparison, \(\operatorname{VCdim}(\mathcal H_n)=n-1\) for every \(n\ge1\). The stated Littlestone profile is restricted to \(n\le7\), whereas the VC-dimension identity holds for all \(n\).

## Assumptions and scope

All labels are distinct; orders are strict and total; queries ask only the relative order of two specified labels. A complete binary query tree of depth \(d\) is shattered when every binary response path is consistent with at least one total order. The Littlestone dimension is the maximum such \(d\). In particular, this is not the depth of a comparison-sorting algorithm, where all leaves must uniquely identify the input.

For a strict partial order \(P\) on \([n]\), write \(\mathcal L(P)\) for its set of linear extensions and \(\lambda(P)=|\mathcal L(P)|\). The unresolved query pairs are exactly the pairs incomparable in \(P\). These notions also specify an entirely finite proof certificate for the seven-label upper bound.

## Proof

**Step 1: General upper bound.** The \(2^d\) root-to-leaf paths of a shattered depth-\(d\) binary query tree require \(2^d\) different total orders. Therefore \(2^d\le n!\). This establishes the claimed dimensions as upper bounds for \(1\le n\le6\), once matching witnesses are supplied.

**Step 2: Exact branching recurrence.** Let \(B(P,d)\) mean that the total orders extending \(P\) shatter a full tree of depth \(d\). Then \(B(P,0)\) always holds for any consistent \(P\), and for \(d\ge1\),

\[
B(P,d)\iff\exists\{a,b\}\text{ incomparable in }P:\quad
 B(\operatorname{tc}(P\cup\{a<b\}),d-1)\ \land\
 B(\operatorname{tc}(P\cup\{b<a\}),d-1).
\]

Here \(\operatorname{tc}\) is transitive closure. In either branch the candidate concepts are precisely the linear extensions of the indicated new partial order, so induction proves the recurrence without any statistical or extrapolation assumption. If \(\lambda(P)<2^d\), the state cannot support depth \(d\); that pruning test is logically one-sided and exact.

The count \(\lambda(P)\) is computed from the predecessor sets \(\operatorname{pred}_P(v)\). If \(S\subseteq[n]\) has been placed in the order prefix, put

\[
F_P(S)=\begin{cases}
1,&S=[n],\\
\displaystyle\sum_{v\notin S:\,\operatorname{pred}_P(v)\subseteq S}
F_P(S\cup\{v\}),&S\ne[n].
\end{cases}
\qquad \lambda(P)=F_P(\varnothing).
\]

Every linear extension has a unique next available minimum vertex, so this count is exact. The attached `verify_posets.py` enumerates all possible unresolved pairs, maintains their strict transitive closures, and memoizes the recurrence on the resulting finite posets and target depths. It returns

\[
B(\varnothing,11)=\mathrm{true},\qquad
B(\{1<2\},11)=\mathrm{false},\qquad
B(\varnothing,12)=\mathrm{false}
\]

for \(n=7\). In fact, every root query in the empty seven-label order has its two branches isomorphic (by relabeling) to the extensions of \(\{1<2\}\). Consequently, the failed depth-eleven half-class is already sufficient to rule out depth twelve in the entire class. The second program, `verify_bitsets.py`, independently enumerates all \(5040\) permutations and all \(21\) query pairs, computes the exact Boolean split recurrence on permutation subsets, and reaches the same result. The attached scripts are the reproducible, exhaustive finite part of this proof, not a sample of states.

**Step 3: Matching lower bounds.** The file `comparison_certificates.json` contains explicit complete binary shattered query trees for every \(1\le n\le7\) at the respective claimed depths. Each internal node specifies one unordered label pair. Each leaf supplies the lexicographic index of a distinct permutation consistent with all comparisons on its path. The verifier reconstructs all permutations and checks every certificate path directly, including all \(2048\) leaves of the depth-eleven seven-label tree and all \(512\) leaves of the depth-nine six-label tree. Thus \(\operatorname{Ldim}(\mathcal H_7)\ge11\), and the hypothesis-count upper bounds for \(n\le6\) are attained. Step 2 proves the remaining upper bound, completing the profile.

**Step 4: Static VC dimension.** Associate to a set of comparison queries its simple undirected graph on the \(n\) labels. A set of queries is VC-shattered exactly when **every orientation of its edges** is extendible to a strict total order. This holds for a forest, because each orientation is an acyclic digraph and hence has a topological sort. If the graph contains an undirected cycle, orient that cycle cyclically: no strict total order can realize the resulting responses. Thus the shattered query sets are exactly forests, and their maximum size is \(n-1\).

## Verification

Run the two independently organized finite verifiers using only the Python standard library:

```sh
python verify_bitsets.py comparison_certificates.json
python verify_posets.py
```

The first verifier works with explicit subsets of lexicographically ordered permutations and also checks the supplied full positive certificates. The second works with transitively closed predecessor masks and independently counts linear extensions by recursion over all vertex subsets. The successful replay output, preserved in `verification_output.txt`, terminates with `BITSET_ALL_CHECKS_PASS` and `POSET_ALL_CHECKS_PASS`. Each test is finite and exhaustive over precisely the specified state space. No result for eight or more labels follows from these computations.

## Relationship to prior work

The concept class is the realizable, noiseless comparison version of learning a ranking. Jia, Wang, Guo and Wang (2021), *PairRank: Online Pairwise Learning to Rank by Divide-and-Conquer* (arXiv:2103.00368), analyze pairwise noisy-feedback ranking and regret, not complete shattered trees for all total orders. Filmus, Hanneke, Mehalel and Moran (2023), *Optimal Prediction Using Expert Advice and Randomized Littlestone Dimension* (arXiv:2302.13849), provide general relations between Littlestone dimension and online mistake bounds, but do not determine the comparison-class values for \(n=1,\ldots,7\). The present finite comparison calculation is not an implication of the hypothesis-count bound alone: that bound overestimates the seven-label dimension by one.

## Limitations

The classification is finite, through seven labels; no formula, asymptotic bound sharper than the cardinality bound, or monotonic failure claim is established for larger \(n\). The nonexistence proof at seven labels depends on the transparent exhaustive finite recurrence implemented in the two accompanying programs. Direct inspection of all historical comparison-learning literature has not been possible; a previously published equivalent calculation under sorting or finite model-theoretic terminology would affect priority. The paper establishes neither independent external verification nor any stronger claim than the displayed equalities.

## References

1. Y. Jia, H. Wang, S. Guo and H. Wang, *PairRank: Online Pairwise Learning to Rank by Divide-and-Conquer*, arXiv:2103.00368, first publicly posted 28 February 2021. https://arxiv.org/abs/2103.00368
2. Y. Filmus, S. Hanneke, I. Mehalel and S. Moran, *Optimal Prediction Using Expert Advice and Randomized Littlestone Dimension*, arXiv:2302.13849, first publicly posted 27 February 2023. https://arxiv.org/abs/2302.13849
