# Review of the joint de Bruijn balance spectrum

## Correctness — PASS

The finite state space is exhaustively covered: every Euler tour fixes the unique all-zero edge and induces one of the \(2^{16}\) local pairings. Independently, unused-edge depth-first search generates exactly the same \(2048\) rooted cycles. Direct enumeration of every circular interval agrees with the prefix-walk discrepancy formula for each cycle; independent Parikh-set and sliding-extrema calculations agree on the peak Abelian complexity for each. The eight-cell histogram and the reversal/complementation orbit counts are direct integer tallies with complete coverage and consistent totals. `verify.py` implements and reruns the proof without third-party dependencies.

## Originality — PASS against checked sources, subject to residual risk

Richomme–Saari–Zamboni (arXiv:0911.2914v1) provides general Abelian-complexity theory rather than de Bruijn-specific joint counts. Gabrić–Sawada (arXiv:2005.01638) examines selected de Bruijn constructions and lists whole-family discrepancy distributions as future work; its tables do not determine the eight joint counts. Álvarez–Becher–Mereb–Pajor–Soto (arXiv:2407.17367v1) gives the all-order minimum discrepancy but not the number attaining it or the Abelian-peak joint spectrum. The debruijnsequence.org properties tables concern selected constructions. Semantic record searches and accessible historical claim comparisons revealed no dominating equivalent statement. Residual risk: earlier unindexed exhaustive computations or unpublished supplements could already report some entries; no external historical uniqueness certificate is claimed.

## Mathematical value — PASS

This is a complete finite classification directly motivated by prior discrepancy research, which explicitly asks for distributions over all de Bruijn cycles. Pairing discrepancy with peak Abelian complexity quantifies a distinct aspect of local balance and reveals that peak Abelian complexity does not determine circular discrepancy. Exact extremal multiplicities and symmetry-orbit frequencies provide a reproducible base case for understanding population distributions beyond selected constructions. The result is valuable as a natural finite benchmark, without pretending to resolve the higher-order problem.

Self-review: passed. Independent audit: not yet performed.
