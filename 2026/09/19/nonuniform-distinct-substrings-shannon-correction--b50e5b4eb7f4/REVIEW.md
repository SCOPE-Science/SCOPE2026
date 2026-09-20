# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof was checked separately at the occupancy, overlap, renewal, and concentration steps.

For the lower expectation bound, the only occurrence estimate used is the union bound \(\mathbb P(w\text{ occurs})\le\min(1,m_kp_w)\), so overlapping windows cannot invalidate it. For the upper bound, non-overlapping predecessors are independent of the current block. An overlapping equality at shift \(r<k\) forces a period-\(r\) word on \(k+r\) coordinates; grouping coordinates by residue class gives probability at most \(p_{\max}^k\), uniformly in \(r\). This makes the total overlap correction summable after multiplication by \(n\).

The renewal functions
\[
A(t)=\sum_k\mathbb E(1-e^{S_k-t})_+,
\qquad
B(t)=\sum_k\mathbb E\min(1,e^{t-S_k})
\]
both equal \(t/H+O(1)\): the renewal count has expectation \(t/H+O(1)\) by bounded overshoot and Wald's identity, while the exponential terms on either side of the threshold are uniformly bounded geometric sums because \(-\log p_{X_i}\) is bounded away from zero.

For the \(L^1\) statement, bounded-increment Hoeffding bounds control the short-length distinct-block contribution and the long-length repeat contribution. The proof uses expected one-sided excesses, not an unsupported inference from convergence in probability to \(L^1\).

A deterministic-seed suffix-automaton simulation was also run as a non-proof sanity check. It shows the predicted entropy-scale normalization for two nonuniform sources.

## Originality

**PASS, to the best of our knowledge.** The originality claim is deliberately narrower than the recent motivating preprint.

Janson, Lonardi and Szpankowski (2004) directly study the same all-length complexity index. Their paper was inspected: the general strongly mixing theorem gives a \(n(n+1)/2-O(n\log n)\) expectation, while the sharper coefficient and periodic expansion is explicitly stated for **unbiased memoryless sources**. Therefore the uniform specialization of the present theorem is prior art and is not claimed.

Ahmadi and Ward (2020) was inspected in full-text HTML. It explicitly distinguishes the all-length complexity index from the fixed-length \(k\)-subword complexity and analyzes the latter for nonuniform binary memoryless sources. Its transition ranges contain the Shannon threshold \((\log n)/H\), but no all-length \(n\log n/H\) correction or all-length \(L^1\) law was located.

Gheorghiciuc and Ward (2007) gives precise fixed-\(k\) expectation machinery, again not the summed all-length theorem stated here. Godbole (arXiv:2609.19409v1) mentions general probabilities in the setup but proves its displayed asymptotic bounds for equal letter probabilities and asks about concentration.

Residual risk remains in older terminology. The full text of Ivanko (2008) was not available for direct inspection here; an accessible 2009 exposition of that work uses uniform random words. Dębowski's entropy-from-subword-complexity chapter was identified and its abstract inspected, but its complete text was not checked line by line. Either could conceivably contain an equivalent nonuniform all-length statement. For that reason the claim is only “to the best of our knowledge,” not exhaustive priority.

## Value

**PASS.** The result identifies the exact first-order repeat deficit for arbitrary finite nonuniform i.i.d. sources. The coefficient is the inverse Shannon entropy rather than an alphabet-cardinality quantity, and the proof shows why overlap dependence does not change it. The \(L^1\) law also supplies a direct, if coarse, concentration statement for the all-length statistic.

## Limitations

- Fixed finite i.i.d. source only; no Markov/dependent-source extension is proved.
- At least two positive-probability symbols are required.
- The \(O(n)\) remainder is not resolved into a constant, oscillatory term, or smaller error.
- The fluctuation scale, variance, and limiting distribution of \(D_n\) are not determined.
- Full-text inspection was unavailable for the 2008 Ivanko article, and the Dębowski chapter was not inspected line by line.
