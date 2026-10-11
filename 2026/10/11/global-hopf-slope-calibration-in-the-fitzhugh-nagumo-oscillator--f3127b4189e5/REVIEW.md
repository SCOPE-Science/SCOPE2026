# Same-model review

## Correctness
PASS. Eliminating the recovery variable produces an exact Liénard equation. The state energy
\[
\mathcal E
=
\frac12\dot v^2
+
\varepsilon
\left[
\frac{1-b}{2}v^2
+
\frac{b}{12}v^4
+
(a-bI)v
\right]
\]
has derivative
\[
\dot{\mathcal E}
=
(1-\varepsilon b-v^2)\dot v^2.
\]
Stationarity gives the accepted balance. Non-equilibrium support has positive \(\dot v^2\)-energy, yielding the speed-weighted RMS identity and the necessary threshold \(\varepsilon b<1\). The two conditional nullcline laws follow independently from arbitrary one-variable antiderivative tests.

Risk: the recurrence theorem is intentionally restricted to compactly supported invariant probability measures.

## Originality
PASS. The strongest prior FHN sources inspected concern Lyapunov stability regions, Hopf/canard bifurcation, limit-cycle multiplicity, singular Hopf analysis, and broad model reviews. Direct searches for the weighted trace balance, \(v^2\dot v^2\), invariant measures, and the \(\varepsilon b<1\) stationary threshold found no same-object implication. The closest indexed structural analogue is a distinct third-order Goodwin oscillator theorem.

Risk: the complete 2004 Lyapunov-functional paper and complete 2009 planar-dynamics paper were not searchable in the inspected route and remain the principal residual originality risks.

## Value
PASS. The result ties the model's local Hopf trace exactly to finite-amplitude recurrent statistics: every non-equilibrium compact stationary state has speed-weighted mean square voltage \(1-\varepsilon b\). This produces a sharp parameter obstruction to recurrence and a model-native diagnostic for periodic or stationary numerical data.

Same-model review: passed. Independent audit: not yet performed.
