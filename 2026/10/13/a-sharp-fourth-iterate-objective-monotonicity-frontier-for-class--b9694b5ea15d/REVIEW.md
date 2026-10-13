# Self-review

## Correctness
PASS. Diagonalization makes classical constant-step FISTA separable across SPD eigenmodes. The published recurrence gives
\[
p_1=1-q,
\qquad
p_2=(1-q)^2,
\]
\[
p_3=(1-q)^2(1-aq),
\qquad
p_4=(1-q)^3(1-cq).
\]
The inequality \(1<a<2\) proves the first three completed steps are objective-nonincreasing. The fourth-step difference factors exactly, and the ordering of its two roots gives one open violation band. Intersecting that band with \([1/\kappa,1]\) yields the sharp threshold
\[
\kappa_*=1.1810364530693856446\ldots.
\]
The packaged verifier independently reconstructs the constants and confirms the displayed \(\kappa=4/3\) spike.

## Originality
PASS. The original FISTA paper supplies the recurrence and global accelerated convergence rate, not this local stepwise threshold. The later monotone-FISTA work explicitly observes that ordinary FISTA need not have nonincreasing objective values, but gives no earliest-iterate or condition-number classification. Later worst-case FISTA work studies global cost-function bounds rather than this exact fourth-versus-third comparison.

Targeted searches using FISTA, fourth-iterate increase, condition-number monotonicity, scalar quadratic bands, and both numerical boundary constants found no implication-equivalent statement. The closest indexed exact-frontier results concern different algorithms such as exact-parameter Nesterov, Polyak, and Barzilai--Borwein methods.

## Value
PASS. The question is directly motivated by a known practical feature of ordinary FISTA and by the existence of monotone FISTA modifications. The result is a sharp natural boundary rather than an arbitrary example: it identifies the earliest possible objective increase, gives an exact universal conditioning threshold, and shows that a pronounced spike already occurs on a two-dimensional quadratic with condition number \(4/3\).

## Closest literature and limitations
The closest primary source is Beck--Teboulle's original FISTA paper; the closest monotonicity source is their later monotone-FISTA construction. Kim--Fessler provide a broader worst-case FISTA analysis, but direct full-body retrieval was incomplete in this run, which is retained as an originality risk. The theorem itself is limited to the original constant-step sequence on smooth SPD quadratics and only the comparison through the fourth completed iterate.

Self-review: passed. Independent audit: not yet performed.
