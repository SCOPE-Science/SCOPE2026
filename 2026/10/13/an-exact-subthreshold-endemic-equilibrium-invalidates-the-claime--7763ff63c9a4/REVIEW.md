# Self-review

## Correctness

PASS. Direct exact substitution verifies the proposed positive endemic equilibrium in all five equations, gives
\[
R_0^2=\frac{9581}{10000}<1,
\]
and places the equilibrium inside the source's population bounds. Since an equilibrium trajectory cannot converge to a distinct disease-free equilibrium, the claimed global attractivity is false. The source's printed equation-(3.8) expression also evaluates to a strictly negative rational number at this equilibrium although the true orbital derivative must be zero.

## Originality

PASS. Subthreshold endemic equilibria under saturated treatment are known in other epidemic systems. The accepted result is narrower and source-specific: it gives an exact rational counterexample to this vector-host theorem and an exact failure point for the published Lyapunov calculation. Searches by source identity, theorem wording, backward-bifurcation aliases, and correction terminology, together with current and prior-ledger overlap checks, found no equivalent published diagnosis.

## Value

PASS. The theorem converts \(R_0<1\) into a global eradication claim. Showing that the model can remain exactly at a positive endemic equilibrium below that threshold materially changes the epidemiological interpretation, while the Lyapunov check identifies where the published proof cannot be correct.

## Closest literature and limitations

A 2019 saturated-treatment SIR analysis demonstrates the broader backward-bifurcation mechanism and uses a stricter global threshold; later network-SIS work also conditions subthreshold global stability on disease-free uniqueness. Those results use different state equations and do not supply this source-specific counterexample.

The present result does not classify the endemic equilibria or derive a sharp replacement global threshold.

Self-review: passed. Independent audit: not yet performed.
