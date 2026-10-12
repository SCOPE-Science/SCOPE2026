# Review of “All-stage extinction needs no auxiliary SIRS parameter inequalities”

## Correctness
PASS. Summing the model equations gives the exact scalar population balance used in the proof. The resulting upper envelope for \(S-S^0\) makes the subcritical first-stage decay explicit. At the critical threshold, the monotone rescaling has a finite limit; a hypothetical positive limit forces persistent disease-induced mortality, then a strictly negative population gap, and hence exponential decay of the same first-stage component. The feed-forward cascade and recovered compartment are stable linear equations driven by quantities already proved to vanish.

The proof assumes \(\delta_1>0\), as in the motivating paper's positive-parameter convention. The bundled checker reproduces the exact cancellation and factorization identities; the infinite-stage-count statement rests on the written induction/cascade argument, not finite enumeration.

## Originality
PASS. The motivating paper gives global all-initial-data DFE theorems only for two and three stages and attaches, respectively, an immunity-loss lower bound and Condition A. Its own simpler \(I_1\) argument is explicitly confined to the population-bounded region. The closest general matrix Lyapunov theorem has a source-model remainder proportional to \((S^0-S)I_1\), so it does not directly cover states above \(S^0\). Broader multistage theorems inspected use permanently removed or SIS architectures rather than the same SIRS return structure.

Residual literature risk remains because a delayed multi-group SIRS comparator was available only at abstract/metadata level, although its stated group-mixing object differs from the sequential-stage system.

## Value
PASS. The result removes the two source-specific auxiliary extinction conditions, proves convergence from arbitrary nonnegative initial populations, and extends the disease-free conclusion to any number of stages. This directly addresses the paper's observation that its sufficient conditions appear non-necessary and avoids symbolic Lyapunov coefficient growth on the DFE side.

## Closest literature and limitations
The closest sources are Somnic–Gasparyan–Rao (2026), Shuai–van den Driessche (2013), Guo–Li–Shuai (2012), Röst–Tekeli (2020), and Muroya–Kuniya–Enatsu (2015). The finding does not address the endemic equilibrium, later-stage infectivity, or the case \(\delta_1=0\). At \(\mathcal R_0=1\), it asserts global convergence but not Lyapunov stability.

Self-review: passed. Independent audit: not yet performed.
