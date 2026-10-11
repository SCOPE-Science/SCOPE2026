# Review

## Correctness
PASS. The exact vector field was read from the primary full text. On compact support inside \(0<x,y,z<1\), invariance permits averaging the Lie derivatives of \(\log x\), \(\log y\), and \(\log z\). The resulting three linear identities imply \(Y-X=cA/(c^2+ce+e^2)\), \(X-Z=eA/(c^2+ce+e^2)\), and \(X+Y+Z=(3+A)/(3+c-e)\). The strict sign \(A>0\) follows from \(\gamma>0\), compact interior support, and the Haar phase marginal. The symbolic checker independently replays the algebra. The same calculation over one full phase-locked period proves the periodic-orbit version.

## Originality
PASS. The exact Rodrigues paper was inspected at the model, parameter definitions, overview, and main theorem; in-document searches for species “mean” and “average” did not reveal this stationary mean-gap law. The full text of the earlier Afraimovich–Hsu–Lin periodically perturbed May–Leonard paper was also inspected; it studies a different additive forcing and return-map dynamics and does not imply the one-coordinate forcing defect or the ratio \((Y-X)/(X-Z)=c/e\). Targeted published-finding corpus searches for May–Leonard mean skew, species ordering, logarithmic balances, and the ratio \(c/e\) returned only structurally analogous balances in other systems. Targeted prior-result corpus searches for May–Leonard aliases and the source identifier found no overlapping statement. Search failure is not treated as a proof of uniqueness.

## Value
PASS. The source uses \(\delta=c/e\) as the strength of attraction of the May–Leonard network and studies periodic, quasiperiodic, and strange recurrent dynamics after forcing. The new law converts finite-amplitude recurrent population statistics into an exact observable of that same structural parameter: the two adjacent species-mean gaps have ratio exactly \(\delta\), while the forcing enforces the non-obvious ordering \(Y>X>Z\). This is a model-specific diagnostic that is independent of local linearization and does not rely on small-amplitude truncation.

## Closest literature and limitations
The closest literature comprises the exact source arXiv:2010.05776v1 / doi:10.1137/20M1335510 and the earlier periodically perturbed May–Leonard analysis doi:10.1142/S021812740100216X. Neither inspected full text states the claimed mean-skew ratio. The invariant-measure form is intentionally limited to compact support in the open unit cube; application to source SRB measures that accumulate on coordinate planes requires additional logarithmic-integrability work. No existence or stability theorem is asserted here.

Same-model review: passed. Independent audit: not yet performed.
