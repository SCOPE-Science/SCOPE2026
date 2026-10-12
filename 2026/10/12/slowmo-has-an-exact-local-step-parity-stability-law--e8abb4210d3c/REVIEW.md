# Review

## Correctness

PASS. The source SlowMo equations reduce exactly to a second-order scalar recurrence after the tau-step SGD block is composed. The complete Jury criterion gives the necessary-and-sufficient condition \(0<\alpha(1-q)<2(1+\beta)\). For \(\alpha=1\), parity of \(\tau\) then yields the displayed exact thresholds and boundary eigenvalues.

Risk: outer-state stability does not bound the intermediate fast iterates inside a locally unstable block.

## Originality

PASS. The defining SlowMo paper contains the nested update and empirical hyperparameter analysis but no fixed-quadratic Schur region or parity law. The beta-zero slice is related to Lookahead and is treated as prior context. The positive-slow-momentum odd-period rescue interval is not implied by that slice, and focused published-record searches did not locate an equivalent SlowMo result.

Residual risk: an equivalent scalar calculation may exist in unindexed distributed-optimization notes.

## Value

PASS. The local-step count is a core communication parameter in SlowMo. The theorem gives a sharp structural distinction between odd and even synchronization periods and identifies exactly when persistent slow momentum can stabilize a fast SGD step that is individually unstable.

Self-review: passed. Independent audit: not yet performed.
