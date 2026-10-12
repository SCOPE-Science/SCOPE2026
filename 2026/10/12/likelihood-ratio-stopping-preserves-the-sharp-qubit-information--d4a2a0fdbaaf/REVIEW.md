# Self-review

## Correctness — PASS
The proof reconstructs the stopped quantum instrument rather than inferring it only from classical decision probabilities. The first-hit error is the exact gambler's-ruin value \(p_m=p^m/(p^m+(1-p)^m)\). More importantly, every stopped path reaching the same score boundary has a Kraus product proportional to the same positive diagonal operator; this makes each coarse-grained terminal map rank one and fixes the effective Kraus pair uniquely from its two eigenstate probabilities. The coherence, disturbance, and mean-duration formulas then follow directly. Exact-rational recurrence checks in `verify.py` agree with the formulas for multiple nontrivial parameter values and thresholds.

## Originality — PASS
The direct 2006 source supplies the one-shot sharp inequalities and diagonal equality family. The 2007 adaptive-QND paper supplies repeated Bayesian likelihood updates and likelihood-ratio stopping in experiment. Targeted searches by source identifier, adaptive-QND aliases, Kraus composition, sequential probability-ratio terminology, and the explicit odds-power form did not locate an implication-equivalent theorem connecting these ingredients. Later sequential-testing literature is broader but does not, from the inspected material, supply this exact discrete stopped-instrument closure. Residual risk remains that an equivalent result exists under other weak-measurement or filtering terminology.

## Value — PASS
The exact closure says that an experimentally natural adaptive operation—repeat until enough evidence accumulates—preserves the sharp quantum information-disturbance/decoherence frontier for this extremal instrument. It also gives the explicit renormalization \(p\mapsto p_m\) and exact expected number of elementary measurements, making the statement useful for comparing measurement strength and repetition cost. This is more than a routine restatement of gambler's ruin because the decisive quantum step is the rank-one coarse-graining of infinitely many stopped Kraus histories.

## Closest literature and limitations
Janssens is the closest mathematical source because it defines the figures of merit and the extremal instrument. Hume, Rosenband, and Wineland are the closest operational source because they use repeated QND readout with real-time Bayesian likelihood-ratio stopping. The theorem is restricted to the symmetric commuting diagonal qubit model and symmetric integer score thresholds; nonideal state changes or asymmetric likelihood increments are outside scope.

Self-review: passed. Independent audit: not yet performed.
