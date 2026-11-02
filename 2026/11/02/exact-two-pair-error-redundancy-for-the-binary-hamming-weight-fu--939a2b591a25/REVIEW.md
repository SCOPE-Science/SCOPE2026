# Scientific review

## Correctness — PASS

The statement includes cyclic pair-indexing, two-error separation \(d_{\mathrm{pair}}\ge5\), systematic normalization, the ordinary information-weight function, and the exceptional length-one case. The proof partitions all pairs of distinct-weight messages by the number of differing message positions, checks the exact suffix differences and identifies two new pair edges for the even two-flip and odd three-flip cases. The one-flip case produces four suffix edges plus a necessarily new message edge when \(k\ge2\). A last-coordinate argument excludes every suffix of length at most two even when nonlinear. The length-one bound is the blocklength bound. A standalone exhaustive program checks all different-weight message pairs through length eleven and the lower-bound configurations. Residual risk: human error in the proof is not ruled out by finite computation; no independently verified formal proof is claimed.

## Originality — PASS, qualified

The precise contribution is the optimal redundancy three and concrete four-periodic suffix for **ordinary message Hamming weight** with two cyclic symbol-pair errors. The 2025 Ge–Xu–Zhang–Zhang text treats ordinary weight but Hamming channel; the accessible 2025 Singh–Singh–Yaakobi text treats b-symbol weight in a symbol-read metric, not ordinary Hamming weight. The Xia–Liu–Chen and September 2026 Singh–Singh abstracts concern general pair function-correcting codes; their full texts were inaccessible, so coverage cannot be excluded from abstracts alone. Targeted semantic-record and literature searches found no statement whose hypotheses and conclusions imply this exact result. An implicit specialization of older general constructions is a material residual risk; independent historical priority verification is outstanding. The claim is accepted under the stated incomplete-access comparison, not as certified unique.

## Value — PASS

Determining the exact redundancy for a standard information invariant in the two-read-error regime is a natural coding-theoretic task. Three check bits independent of message length are both sufficient and necessary, with a nontrivial run/edge geometry argument. This result distinguishes ordinary Hamming weight from the overlapping-read weight studied in earlier bounds and gives a direct deployable encoder for function-only recovery. It does not purport to solve more general noisy data protection or high-error reconstruction.

Self-review: passed. Independent audit: not yet performed.
