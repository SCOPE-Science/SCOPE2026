# Exact fixed two-burst unstable-deletion codes in \(S_6\)
## Finding
For permutation codes in \(S_6\) correcting a burst of exactly two unstable deletions, \(A_{\mathrm{PBUD}}(6,2)=12\). There are exactly \(67{,}163{,}560\) labeled maximum codes. For a maximum code, the number of distinct received permutations in \(S_4\) covered by its pairwise-disjoint descendant balls has distribution \(16:100,\ 17:3{,}240,\ 18:47{,}958,\ 19:415{,}120,\ 20:2{,}283{,}083,\ 21:8{,}134{,}400,\ 22:18{,}331{,}932,\ 23:23{,}922{,}912,\ 24:14{,}024{,}815\); hence exactly \(14{,}024{,}815\) maximum codes are perfect, meaning their exact-two-burst descendant balls partition all \(24\) permutations in \(S_4\).

An explicit perfect maximum code is
\[
\{123456,132465,152463,213654,342516,345162,362514,364251,563124,543216,615243,645213\}.
\]

## Assumptions and scope
For \(\pi=(\pi_1,\ldots,\pi_6)\in S_6\) and \(i\in\{1,2,3,4,5\}\), delete positions \(i,i+1\) and standardize the remaining four values by replacing them with their relative ranks in \(\{1,2,3,4\}\). Let \(B_2(\pi)\subseteq S_4\) be the set of distinct standardized results. A code \(C\subseteq S_6\) corrects a fixed burst of exactly two unstable deletions when \(B_2(\pi)\cap B_2(\sigma)=\varnothing\) for all distinct \(\pi,\sigma\in C\). This is the fixed-length unstable-burst model called \(2\)-PBUD in the cited literature; no claim is made here about the distinct model of bursts of at most two deletions.

The word “labeled” means that two subsets of \(S_6\) are counted separately unless they are literally equal; no quotient by coordinate, value, reversal, or other symmetries is taken. A maximum code is called perfect here exactly when the disjoint union \(\bigcup_{\pi\in C}B_2(\pi)\) equals all of \(S_4\).

## Proof
Enumerate the \(720\) permutations of \(S_6\) and the \(24\) possible received permutations of \(S_4\). Represent each descendant set \(B_2(\pi)\) by its \(24\)-bit incidence mask. There are \(610\) distinct masks. If a mask \(M\) occurs for \(\mu(M)\) permutations, at most one of those permutations can belong to a code, because two codewords with the same nonempty descendant mask collide. Once a mask is selected, it contributes \(\mu(M)\) independent labeled choices.

For an available output set \(U\subseteq S_4\), let \(F(U)\) be the largest number of mutually disjoint descendant masks whose union is contained in \(U\). Choose the least available received word \(b\in U\). Every packing counted by \(F(U)\) falls into exactly one of two cases: it leaves \(b\) uncovered, or it contains the unique selected mask \(M\) that covers \(b\). Hence
\[
F(U)=\max\left(F(U\setminus\{b\}),\ \max_{M\ni b,\ M\subseteq U}\left(1+F(U\setminus M)\right)\right),
\qquad F(\varnothing)=0.
\]
This recurrence is exhaustive because the selected masks are disjoint, so a packing that covers \(b\) has exactly one selected mask containing \(b\), while a packing that does not cover \(b\) belongs only to the first branch.

The same recurrence carries two exact annotations on every maximizing branch. First, the number of labeled realizations is multiplied by \(\mu(M)\) when \(M\) is selected and summed over tied maximizing branches. Second, a histogram records the total cardinality of the selected union, shifting its index by \(|M|\) on a selected-mask branch. Evaluating the recurrence on \(U=S_4\) gives maximum \(12\), total labeled maximum-code count \(67{,}163{,}560\), and the footprint histogram stated above. The histogram entries sum to \(67{,}163{,}560\); its \(24\)-footprint entry is \(14{,}024{,}815\), proving the perfect-code count.

The displayed code has \(12\) words. Direct reconstruction of its descendant masks shows that they are pairwise disjoint and their union has cardinality \(24\), so it is a perfect maximum witness.

## Verification
`verify.py` is a standalone Python-standard-library replay. It regenerates all \(720\) source permutations and all \(24\) received permutations, recomputes every standardized exact-two-burst descendant set, checks the mask multiplicities, evaluates the exhaustive recurrence, verifies the complete footprint histogram, and checks the explicit perfect witness. Its recorded output is in `verification_output.txt`; `CENSUS.json` records the expected exact totals and witness in machine-readable form.

The recurrence visits \(525{,}881\) reachable available-output states. This state count is descriptive only: correctness rests on the exhaustive recurrence above, not on a timeout, heuristic search, or sampled experiment.

## Relationship to prior work
Chee, Vu, and Zhang introduced the unstable burst-deletion model for permutations and constructed general families of such codes in the 2015 ISIT paper “Permutation Codes Correcting a Single Burst Deletion I: Unstable Deletions.” The expanded 2020 paper by Chee, Ling, Nguyen, Vu, Wei, and Zhang explicitly distinguishes exactly-\(s\) PBUD codes from at-most-\(s\) PBUD codes, defines \(A_{\mathrm{PBUD}}(n,s)\), and develops asymptotic bounds and constructions.

The inspected primary texts do not state the exact parameter \(A_{\mathrm{PBUD}}(6,2)\), an all-maximizer census, a footprint distribution, or a perfect-code count for this parameter. The 2020 general bounds and constructions therefore do not imply the finite classification above. Targeted searches under PBUD, UBD, “unstable burst deletion,” “permutation-invariant burst deletion,” the exact parameter \((6,2)\), and the numerical census values located no implication-equivalent published result.

## Limitations
The result concerns only fixed bursts of exactly two unstable deletions in \(S_6\). It does not determine the corresponding at-most-two-burst parameter, other lengths, other burst sizes, or equivalence classes under a symmetry group. The originality comparison cannot exclude an obscure or unindexed finite computation, thesis table, or unpublished census that was not discoverable in the inspected sources.

## References
1. Y. M. Chee, V. K. Vu, and X. Zhang, “Permutation Codes Correcting a Single Burst Deletion I: Unstable Deletions,” 2015 IEEE International Symposium on Information Theory, pp. 1741–1745. DOI: 10.1109/ISIT.2015.7282754.
2. Y. M. Chee, S. Ling, T. T. Nguyen, V. K. Vu, H. Wei, and X. Zhang, “Burst-Deletion-Correcting Codes for Permutations and Multipermutations,” IEEE Transactions on Information Theory 66(2), 957–969, 2020. DOI: 10.1109/TIT.2019.2933819.
