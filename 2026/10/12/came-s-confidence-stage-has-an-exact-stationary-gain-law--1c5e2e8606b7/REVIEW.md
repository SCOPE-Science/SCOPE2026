# Review

## Correctness

PASS. Biregularity makes both row-column reconstructions scalar all-ones matrices. The source update clipping exactly removes the first-stage temporal bias, after which the momentum and confidence recurrences are one-dimensional and solvable in closed form. The embedded verifier directly replays the complete matrix recurrence.

Risk: the exact first-stage formula sets the source numerical regularizer \(\epsilon_1\) to zero.

## Originality

PASS. The CAME paper defines the residual-confidence mechanism and motivates larger steps when residuals are small, but the inspected full text does not give the stationary gain law, the exact \(\epsilon_2^{-1/2}\) limiting RMS, or the biregular density cancellation. Focused published-record searches did not locate an implication-equivalent result.

Residual risk: an equivalent calculation may exist in unindexed implementation notes.

## Value

PASS. The confidence stage is the defining distinction between CAME and Adafactor. The theorem gives a sharp boundary case for that mechanism: stationary consistency does not freeze the gain but drives it to the explicit regularization floor, while a natural class of sparse matrix patterns remains invisible to the global confidence RMS. This is a structural limitation and tuning diagnostic, not an arbitrary numerical example.

Self-review: passed. Independent audit: not yet performed.
