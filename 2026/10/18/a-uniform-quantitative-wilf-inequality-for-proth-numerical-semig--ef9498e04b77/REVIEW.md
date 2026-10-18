# Scientific review

## Correctness — PASS

For every specified odd parameter, the primary Apéry theorem supplies \(N_{-j}=T(j)(M+1)+jM\) and the genus formula. The greedy coefficient restrictions give \(T(j)\le k+1\) since the top digit is at most one and among the lower digits at most one can be two. The final residue \(j=M\) yields \(c\ge M^2+1\). Substitution into \(e(c-g)-c\), using the independently established embedding dimension, produces the exact advertised polynomial lower bound. Its positivity follows from \(M\ge3\cdot2^n>4n+5\ge (k+1)(2k+1)/(k-1)\). Numerical shortest-path checks reconstructed 599039 distinct Apéry entries from 119 instances, along with genus, conductor, and Wilf margins. The infinite conclusion depends on the proof, not these tests.

## Originality — PASS within inspected sources

Theorem 6.1 of Srivastava–Thakkar (arXiv:2311.12462v1, 2023) proves Wilf only when \(m=2^r+1\), despite the breadth of its abstract. Liu–Xin–Ye–Yin (arXiv:2306.03459v4, 2025) provides stronger *structural* coverage: its Theorems 5.2–5.3 give exact Apéry and genus descriptions for all odd admissible \(m\). The present inequality depends on those descriptions and adds a direct quantitative Wilf margin for the full parameter range. This is a derived consequence, and possible prior implicit derivations or unindexed overlapping work are a meaningful residual originality risk. Existing Wilf sufficient conditions such as high embedding dimension or conductor at most three times the multiplicity do not cover the entire family as parameter sizes grow.

## Mathematical value — PASS

Wilf's conjecture remains open for general numerical semigroups. A published Proth-semigroup study proves the inequality only in the special \(2^r+1\) case. The explicit positive uniform lower bound settles the whole remaining odd-parameter Proth family and quantifies its Wilf margin without solving the full Frobenius maximization problem for each parameter. This is a motivated all-parameter arithmetic inequality, not merely a new numerical example. The argument is intentionally short because it leverages the published exact Apéry theorem; its status as a new consequence requires external scholarly scrutiny.

## Sources and limitations

Inspected: Srivastava–Thakkar, *The Frobenius Problem for the Proth Numbers*, arXiv:2311.12462v1, §§2,6; Liu–Xin–Ye–Yin, *On the Frobenius Number and Genus of a Collection of Semigroups Generalizing Repunit Numerical Semigroups*, arXiv:2306.03459v4, Proposition 2.7 and §5. The result excludes \(m=1\), depends on cited prior structural theorems, does not assert a sharp Wilf number or an exact all-parameter Frobenius formula, and may overlap a consequence not detected by indexed searches. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
