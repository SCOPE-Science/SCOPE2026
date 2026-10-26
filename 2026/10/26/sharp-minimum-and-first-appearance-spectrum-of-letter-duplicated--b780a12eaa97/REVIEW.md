# Scientific review

## Correctness — PASS
The claim uses the precise run-length-at-least-two definition from the cited literature, with the empty optimum normalized to zero. Two simultaneous pigeonhole inductions prove the lower bounds for even and odd target lengths without assuming that all alphabet symbols occur. Greedy embedding in the periodic word yields the exact earliest-last-position formula, and the sharp lower envelope at every target length matches those bounds. Uniqueness of maximal run decompositions then yields the formal bivariate geometric series without counting embeddings more than once. The independent checker confirms 67,752 finite source-word cases and a separate first-appearance recurrence through prefix degree eighty. The proof, not the experiments, establishes all quantified cases, including \(q\ge2\), \(n=0\), and the borderline remainder \(s=q\).

## Originality — PASS
The two directly relevant primary articles [1,2] define the same admissible subsequences and prove per-input algorithms and variants. Their inspected definitions, main results, algorithms and discussion do not supply the all-input extremal value or a complete first-appearance generating function for distinct LDS words. The prior authors distinguish the longest run subsequence problem by a different admissibility rule. Exact-statement, equivalent-expression, alphabet-size, cyclic-source and run-count searches did not locate an implication that covers these two results. The no-match outcome is evidence of incomplete overlap, not a proof that an equivalent result cannot exist elsewhere. Remaining risk: unindexed enumeration work may already state the same rational series or worst-case value under another name.

## Mathematical value — PASS
Longest duplicated-letter subsequences provide a natural measure of how many repeated-letter blocks can be recovered after deletions. An exact uniform worst-case guarantee is a structural complement to a linear-time per-instance algorithm: it identifies the sharp attainable value for every length and every alphabet size, including a periodic infinite witness. The additional bivariate formula counts all admissible *distinct* output patterns on this witness, refining the extremal statement with a complete, reproducible spectrum. The result is neither an isolated small-case computation nor a restatement of algorithmic complexity.

## Scope and risks
The generating function counts distinct LDS words and first appearances, not embedding multiplicities. Other minimizers are not classified; extension to run lengths greater than two is not claimed. An independent mathematics audit and a comprehensive bibliographic uniqueness guarantee are not available.

## References
[1] Lai, Liyanage, Zhu, Zou, arXiv:2112.05725; CPM 2022, DOI 10.4230/LIPIcs.CPM.2022.7.
[2] Lai, Liyanage, Zhu, Zou, Acta Informatica (2024), DOI 10.1007/s00236-024-00459-7.

Self-review: passed. Independent audit: not yet performed.
