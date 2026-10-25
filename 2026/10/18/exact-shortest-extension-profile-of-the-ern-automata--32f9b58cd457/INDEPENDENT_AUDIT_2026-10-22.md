# Independent mathematical audit

## correctness

PASS

PASS: For n≥3, a cyclically shifts 0..n−1 and b maps 0→1 while fixing others; words act left-to-right. Telescoping the column-sum defect 1P_w−1 as a sum over b-letters followed by suffix matrices yields signed contributions s_{1·v}−s_{0·v}. For suffix length≤n−1 the pair images are either merged or the adjacent states h,h+1 modulo n, h equal to number of a letters; until the first cyclic 01 boundary r(S), every contribution of a word of length≤r is nonpositive. The word ba^r creates exactly one positive contribution. A length-(r+1) extending word must have initial b and a suffix with r copies of a, forcing the unique optimum ba^r. For d<n, initial no-01 binary prefix is 1^h0^{d−h}, with s_d=1 and n−d−1 free bits: d 2^{n−d−1} subsets; for d=n exactly the n−1 prefix-run sets. Fixed-cardinality binomial formula and mean follow by finite sums. Independent full subset-word enumeration for n=3..7 verified the minimum/uniqueness, histograms and moments. No inference to arbitrary automata.

## originality

PASS

PASS best of knowledge with explicit access risk: Berlinkov–Ferens–Szykuła 2018 classify preimage-problem complexity for general DFAs, not every subset of the particular Černý family. Miccinesi 2026 studies certificates for ≤n−1 short extending words and reportedly uses a Černý exceptional subset, but its arXiv text/PDF access failed; only abstract and indexed summary could be inspected, so it might contain an equivalent all-subset classification not excluded. Resultary produced family rank-compression and k-avoidance classifications, whose target quantifier differs from strict FIRST preimage enlargement. No positive evidence of a stronger published profile implies the full distribution and unique shortest words; priority remains provisional.

## value

PASS

PASS: for the foundational Černý automata, determining exact shortest preimage enlargements for every proper subset, including a full length and size-refined histogram and unique words, fills a natural gap between extremal examples and general complexity. The mean length asymptotically 3 against a worst case n captures nontrivial structural distribution, not an arbitrary tiny census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
