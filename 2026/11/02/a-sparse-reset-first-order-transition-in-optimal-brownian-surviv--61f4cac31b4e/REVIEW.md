# Scientific review

## Correctness — PASS

For every fixed diffusion coefficient \(D>0\), near-reset weight \(c/L^2\), separation \(L>\max\{1,\sqrt c\}\), and initial position \(x>0\), the renewal kernel has a unique simple exponentially tilted pole that gives a true survival asymptotic with positive prefactor. A monotone parametrization by the positive pole momentum maps every reset rate to one optimization coordinate. Uniform two-chart expansions, an exhaustive sequence-compactness exclusion of intermediate scales, strict nondegenerate maxima, and a monotone branch height difference prove the asymptotic phase selection, the unique local coexistence weight, and its explicit \(L^{-2}\) correction. The standard-library checker performs 30,524 diagnostics including an independent substitution into the renewal pole condition. Finite tests are supporting checks, not substitutes for the renewal and asymptotic arguments. Risks: the key renewal theorem hypotheses, particularly the nonlattice finite-mean tilted kernel and directly Riemann integrable forcing, require the explicit conditions verified in the proof.

## Originality — PASS, qualified

The primary source arXiv:2311.11897 directly establishes the two-site survival transform; its optimized quantity is the **mean first-passage time**. The inspected full main text and arXiv:2401.01125 concern mean and fluctuation analyses, not maximization of the exponential survival tail under the sparse reset law \(c/L^2\). Actual published-record and literature searches for asymptotic survival optimization, the two competing scales and the specific critical constant returned no directly covering theorem. This is best-knowledge originality, not a claim of independently certified novelty. Residual risks include general defective renewal analyses or another unindexed distributed-resetting optimization theorem containing the same statement as an implicit corollary.

## Mathematical value — PASS

Optimizing the long-time survival exponent answers a different physical question from minimizing the average search time; the distinction is meaningful when rare late survivors determine reliability. The theorem identifies a parameter-independent critical sparsity coefficient, a genuinely macroscopic separation between optimal rates, exactly two global winners at a unique local coexistence weight, and the leading finite-distance shift. It resolves a naturally motivated limit of a published two-site resetting model rather than calculating a disconnected finite parameter slice. The result is limited to a two-point Poisson-reset Brownian half-line; other resetting geometries and finite observation times require separate work.

## Closest sources and unresolved risks

- Julián-Salgado, Dagdug and Boyer, arXiv:2311.11897, equations (2)–(6) and sections IV–V: shared renewal input; different objective and scaling.
- Méndez, Flaquer-Galmés and Campos, arXiv:2401.01125, sections II and V–VIII: broad related distributed-resetting mean-time and fluctuation results, not the present tail-exponent phase diagram.
- Evans, Majumdar and Schehr, arXiv:1910.07993: general restarting background; abstract-level comparison does not eliminate all possible general-theorem implications.

Self-review: passed. Independent audit: not yet performed.
