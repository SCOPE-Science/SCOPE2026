# Review

## Correctness

PASS. Ordinary duplicate contractions are mutually reversible by insertion. Kihara's hierarchy recursion gives \(61\) normalized \(\Sigma_4\) patterns and \(61\) normalized \(\Pi_4\) patterns, with no level-at-most-\(4\) normalized word of length \(8\); prepending never lowers the level, so the finite universe is exhaustive. The proved subsequence normal form exactly captures the absorption rewrite preorder. Exhausting it gives \(37\) mutual classes on each side. The packaged checker reproduces the source's \(17\) normalized \(\Sigma_3\) patterns and returns `VERIFY_OK`. Observation 2.22 then gives the semantic upper bounds.

## Originality

PASS. The primary paper defines absorption and solves the lower-level classification but leaves the fourth-level semantic counts open. Its publicly accessible 2026 journal-version manuscript retains the open question, and the August 2026 open-problem collection repeats it. Candidate-specific searches for fourth-level mutual absorption, the normalized count \(61\), and the quotient count \(37\) found no equivalent statement. The nearest indexed fourth-level item concerns ordinary four-block undecidability and has no implication for this realizability-theoretic quotient.

## Value

PASS. This is a complete classification of a natural invariant supplied by the primary source at exactly the first hierarchy level where the semantic classification is open. It reduces the fourth-level search to \(37\) syntactic cases and gives an explicit uniform upper bound for the open semantic counts. The exact rewrite normal form and cutoff are reusable for future separation arguments.

## Closest literature and limitations

The closest source is Kihara's arXiv:2410.15795 / 2026 *Journal of Mathematical Logic* paper, especially Definitions 2.3 and 2.6, Observations 2.17 and 2.22, Proposition 2.9, and Section 5. The 2026 *Open Problems in Mathematical Logic* collection independently confirms the fourth-level questions.

The result proves no many-one or di-many-one separation between distinct absorption classes and no general reducibility algorithm.

Self-review: passed. Independent audit: not yet performed.
