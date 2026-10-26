# Exact finite-radius descendant spheres for binary length-one reverse-complement duplication

## Finding
For a nonempty binary word \(x\) of length \(n\), let \(r\) be the number of equal letters at its beginning. At one step, choose any letter \(a\) in the current word and insert its binary complement \(\bar a\) immediately after it. Let \(D_t(x)\) be the **set of distinct words**, rather than insertion histories, obtainable in exactly \(t\) steps. For all integers \(n\ge1\) and \(t\ge0\),
\[
|D_t(x)|=\sum_{j=0}^{t}\binom{n+t-1}{j}-\sum_{j=0}^{t-1}\binom{n+t-r-1}{j}.
\]
The second sum is empty when \(t=0\). In particular this exact sphere size depends on the seed only through its length and initial constant-run length, regardless of all subsequent letters. A length-\(m\) binary word \(y\) is a descendant of \(x\) if and only if \(m\ge n\), \(y\) begins with the initial bit of \(x\), \(x\) is a scattered subsequence of \(y\), and the initial constant run of \(y\) is no longer than that of \(x\). The latter is an intermediate membership characterization; the principal enumerative contribution is the explicit distinct sphere-volume formula.

For \(t=1\), \(|D_1(x)|=n\), while \(|D_2(x)|=n(n+1)/2+r\). For \(t\ge2\) the sphere size is strictly increasing with \(r\) at fixed \(n,t\), so a constant seed maximizes it and a seed beginning with unequal letters minimizes it when \(n\ge2\). For any fixed nonempty \(x\),
\[
\lim_{t\to\infty}\frac{|D_t(x)|}{2^{n+t}}=\frac{1-2^{-r}}2.
\]

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), complementation interchanges the letters, and a duplication inserts the complement immediately to the right of a chosen original letter. The seed is nonempty, distinct output words are counted once regardless of generation paths, and the number of steps \(t\) is exact. No claim concerns duplication lengths exceeding one, larger alphabets, inverse parent multiplicities, or error-correcting code optima.

## Proof
**Reachability necessity.** Every insertion preserves the old word as a scattered subsequence and never changes its first letter. It cannot increase the initial homogeneous-run length: insertion in that run interrupts it, while insertion afterward leaves it unchanged.

**Reachability sufficiency.** Assume \(x\) is embedded in a longer word \(y\), their first letters agree, and \(r(y)\le r(x)\). Choose an embedding that uses *every* position of the first run of \(y\): its first \(r(y)\) target letters equal the first \(r(y)\) letters of \(x\), so moving those matches left is possible without harming subsequent matches. Within each later constant run of \(y\), move any matches to its rightmost positions, without changing their relative order or the matches in other runs.

At least one position in a run after the first is unmatched, since the first run is entirely matched and \(y\) is longer. Consider the rightmost run containing unmatched positions. By the right-justified convention its first letter is unmatched; this letter is different from its predecessor and can be deleted as the second member of a complementary adjacent pair. The preserved embedding remains an embedding in the shorter word. The only way deleting this first letter could increase the initial-run length is when it is the sole letter of the second run; its deletion then merges the first and third runs. As all later runs are completely matched (the chosen run was rightmost with unmatched letters), the first and third runs are both entirely matched into an initial constant run of \(x\). Their combined length is therefore at most \(r(x)\). Thus the shorter word still satisfies the first-run bound. Repeating removes all inserted letters and reaches \(x\). Inverting these deletions gives a sequence of permitted complement insertions, proving the criterion for every length.

**Exact enumeration.** For a fixed target word of length \(h\), the number of binary words of length \(m\) having it as a scattered subsequence is
\[
S(m,h)=\sum_{j=h}^{m}\binom mj,
\]
with \(S(m,0)=2^m\), \(S(m,h)=0\) for \(m<h\). Indeed, when scanning independent uniformly chosen bits, the greedy matching indicator for the next needed target bit is at every position an independent fair Bernoulli variable; greedy embedding succeeds precisely after at least \(h\) matches.

Write \(m=n+t\). Requiring a leading copy of the first letter of \(x\) and embedding the remaining \(n-1\) letters gives \(S(m-1,n-1)\) candidates. The forbidden candidates with initial run at least \(r+1\) all have their first \(r+1\) letters fixed to \(x_1\), and the first \(r\) of these embed the initial run of \(x\). If \(r<n\), the extra identical letter cannot match the next (opposite) seed letter, so the remaining \(n-r\) seed letters must occur in the suffix of length \(m-r-1\); if \(r=n\), that suffix is arbitrary and the same expression with empty target applies. There are exactly \(S(m-r-1,n-r)\) forbidden candidates when \(t\ge1\), and none when \(t=0\). Subtracting and using binomial symmetry gives the formula in the finding.

For \(t\ge2\), increasing \(r\) decreases the nonzero forbidden prefix-tail sum strictly, proving the sharp extremal claim. For fixed \(n\) and \(r\), each first sum equals \(2^{n+t-2}\) up to a polynomial in \(t\) of fixed degree, and each second sum equals \(2^{n+t-r-2}\) up to another fixed-degree polynomial. Division by \(2^{n+t}\) gives the asserted density.

## Verification
Run `python verify.py` with Python 3.9 or later and no external dependencies. The script independently generates each distinct exact-step descendant by direct insertion, and separately tests the subsequence/run criterion and the binomial formula for all binary seeds of lengths \(1\) through \(8\) and steps \(0\) through \(4\). A second exhaustive calculation checks the one-step inverse-deletion lemma for all admissible pairs with target length at most \(10\). Results: `RC1_DESCENDANTS_PASS seed_radius_cases=2550 candidate_targets=2708780`; `RC1_INVERSE_LEMMA_PASS admissible_pairs=84490`. These finite checks supplement, but do not replace, the all-length proof above.

## Relationship to prior work
Ben-Tolila and Schwartz (2021, arXiv:2112.11811v1) already characterize the **unbounded descendant language** by a concatenation of per-letter regular languages, and prove its full expressiveness for this binary channel. That structural language theorem is acknowledged, not claimed here as a new descendant-language description. The present theorem counts *distinct* descendants at **every exact finite radius**, eliminates the multiple-generation ambiguity of the language product, and proves the unexpected dependence on the initial run alone, sharp extrema, and limiting density. Yohananov and Schwartz (2023, arXiv:2312.00394v1) analyze coding capacity and common descendant cones; their common-descendant criterion and rate result do not give the stated exact per-seed finite-step counts. The binomial count of supersequences is standard and not claimed as original.

## Limitations
Originality is assessed against the inspected cited papers and searches, not guaranteed across all literature. An equivalent explicit sphere-volume identity might exist under a different insertion/channel terminology, and the earlier regular-language factorization logically determines the reachable set, although extracting an exact distinct finite-radius cardinality from its ambiguous concatenation is nontrivial. The code checks finite cases only. No independent mathematical audit has occurred.

## References
1. E. Ben-Tolila and M. Schwartz, *On the Reverse-Complement String-Duplication System*, arXiv:2112.11811v1 (first public version 2021-12-22), https://arxiv.org/abs/2112.11811.
2. L. Yohananov and M. Schwartz, *On the Coding Capacity of Reverse-Complement and Palindromic Duplication-Correcting Codes*, arXiv:2312.00394v1 (2023-12-01), https://arxiv.org/abs/2312.00394.
