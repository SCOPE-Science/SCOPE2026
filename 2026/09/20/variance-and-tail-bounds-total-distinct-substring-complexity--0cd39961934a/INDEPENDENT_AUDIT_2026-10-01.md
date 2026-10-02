# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260920-0cd39961934a`

## Correctness — PASS

The all-moment deficit estimate is valid: every pair of length-\(k\) windows matches with probability exactly \(d^{-k}\), including overlap; above \(\lfloor\log_d n\rfloor\), the deficit is bounded by collision pairs, and the \(q\)-moment plus Minkowski sum is geometric. Below the threshold the alphabet-size maximum gives a deterministic \(O(n)\) contribution. Optimizing Markov's inequality yields the stated exponential tail. The centered variance/concentration argument is also correct, but it is not originality-bearing here: the longest-repeat tail, typical-set Hamming Lipschitz bound, McShane extension, bounded-difference variance, and concentration steps agree with an earlier stronger nonuniform-iid theorem. The finite verifier correctly checks the collision and Lipschitz identities on small instances.

### Correctness sources

- assigned RESULT.md
- artifacts/verify_bounds.py
- https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-distinct-substring-complexity-concentration--a122573a5d02
- Godbole arXiv:2609.19409

### Correctness risks

- The variance scale is only an upper bound and is currently prior-covered in greater source generality.

## Originality — PASS

The centered theorem is covered by an earlier 2026-09-18 published finding, which treats arbitrary iid alphabets with atom bound \(p_*<1\) and proves essentially the same \(O(n\log^4 n)\) variance and \(\sqrt n\log^2 n\) concentration. The surviving originality is Theorem 1: an all-\(q\) \(O_d(qn)\) bound and exponential tail for the deficit from the exact deterministic maximum \(M_{n,d}\). Searches of the earlier concentration result, the later first-correction record, Godbole's primary paper, fixed-length subword work, and suffix-tree profile variance did not locate this exact deficit theorem.

### equivalent_formulations

Searches:
- Resultary: total distinct substring complexity variance concentration all lengths suffix array LCP random word
- Resultary: deficit from maximum distinct substrings all moments exponential tail
- Godbole arXiv:2609.19409

Evidence:
- The 2026-09-18 record is a stronger version of the centered variance/concentration clause.
- No inspected source states the \(\|M_{n,d}-D_n\|_q=O_d(qn)\) theorem or the resulting linear-scale exponential tail.

Reasoning:
Centered fluctuation about the mean and one-sided deficit from the exact combinatorial maximum are different functionals and were compared separately.

### broader_coverage

Searches:
- https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-distinct-substring-complexity-concentration--a122573a5d02
- 2026/9/19/SCOPE-random-word-distinct-substring-first-correction--022b2626ec5b
- Janson–Lonardi–Szpankowski 2004

Evidence:
- The earlier theorem dominates the centered part and the later mean-correction theorem controls expectation, but neither gives the all-moment deficit tail.

Reasoning:
Mean asymptotics and centered Lipschitz concentration do not mechanically imply a dimension-free exponential tail for the nonnegative maximum deficit.

### exact_database_or_table

Searches:
- current Resultary distinct-substring findings
- suffix-array/LCP additive-functional terminology

Evidence:
- No exact database/table of all deficit moments was found.

Reasoning:
The claim is probabilistic and uniform in \(n\), not a finite enumeration.

### claim_vs_prior_implication

Searches:
- claim-versus-prior concentration theorem

Evidence:
- The prior theorem has no deterministic maximum \(M_{n,d}\) and no collision-pair moment summation for \(M_{n,d}-D_n\).

Reasoning:
Theorem 1 is not a corollary of the prior centered concentration statement without additional structure; it remains a distinct contribution.

### source_inspections

- **Near-root-n concentration for random distinct-substring complexity** — https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-distinct-substring-complexity-concentration--a122573a5d02. Trigger: Exact semantic match for the centered theorem. Material read: Complete published RESULT.md. Method: Full theorem-and-proof implication comparison. Assessment: COVERS the centered variance/concentration part. Evidence: It proves the same logarithmic Lipschitz mechanism for the more general iid source class.
- **The Expected Number of Distinct Substrings in an Alphabet String** — https://arxiv.org/abs/2609.19409. Trigger: Primary paper posing the variance/concentration question and studying the same total statistic. Material read: Accessible primary abstract and open-question statement. Method: Primary scope comparison. Assessment: Background only; it studies expectation and poses variance/concentration as open. Evidence: The source asks whether variance can clarify concentration of the total distinct-substring count.
- **Assigned finite verifier** — artifacts/verify_bounds.py. Trigger: Collision and typical-set Lipschitz identities. Material read: Complete source. Method: Line-by-line inspection. Assessment: Correct corroboration. Evidence: It exhaustively checks overlapping equality probabilities, small deterministic maxima, and good-set Hamming jumps.

### checked_sources

- https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-distinct-substring-complexity-concentration--a122573a5d02
- https://arxiv.org/abs/2609.19409
- https://doi.org/10.1016/j.tcs.2004.06.023
- https://doi.org/10.3390/e22020207
- current Resultary deficit search

### residual_risks

- Older suffix-tree additive-functional literature could contain an equivalent maximum-deficit tail under different terminology.

## Scientific value — PASS

The surviving all-moment deficit theorem gives a strong finite-sample statement at the natural exact combinatorial maximum: the loss has linear scale with an exponential tail uniformly in word length for fixed alphabet size. This complements, rather than duplicates, the already-covered centered concentration theorem and is a reusable collision-count estimate.

### Value sources

- exact deterministic maximum
- collision-pair proof
- prior centered concentration theorem

### Value risks

- No optimal constant or matching lower tail is claimed.

## Limitations

- Independent uniform letters and fixed alphabet size for the deficit theorem.
- The centered variance/concentration theorem is prior-covered and is not counted as novel.
- No sharp variance asymptotic, CLT, or optimal concentration scale is obtained.
- Originality of the surviving deficit theorem is best-of-knowledge.

## Disposition

**PASSED**
