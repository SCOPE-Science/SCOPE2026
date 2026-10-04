# Same-model review

## Correctness
PASS. For any compactly supported invariant probability measure, applying the generator to arbitrary antiderivatives of continuous functions of \(z\) gives
\[
\mathbb E[x^2\mid z]=1.
\]
Stationarity of \(y^2\) gives \(\mathbb E[xy]=\mathbb E[y^2]\), hence
\[
\mathbb E[y^2]+\mathbb E[(x-y)^2]=1.
\]
The lower endpoint is impossible by stationarity of \(xy\). At the upper endpoint, support invariance reduces the measure to the two equilibrium atoms. If \(x^2=1\) almost surely, compact completeness similarly forces the support to those equilibria. Therefore any other invariant measure has a nonzero zero-mean defect \(x^2-1\) and must charge both signs, proving the cylinder crossing statement. The packaged exact-arithmetic checker verifies the critical polynomial identities.

Risk: the rigidity steps use the standard invariance of the support of an invariant measure under a continuous complete flow.

## Originality
PASS. The inspected same-object and same-family literature centers on discovery, equilibrium types, coexistence, bifurcation, Poincaré compactification, and integrability. Targeted published-finding corpus searches for Sprott C stationary moments, conditional laws, derivative-energy partitions, and the \(|x|=1\) recurrence barrier returned no same-object result implying the theorem.

Risk: two plausible analytical sources were not available as complete full text in this non-interactive run. Their abstracts and accessible metadata do not show coverage, but no whole-document noncoverage claim is made.

## Value
PASS. The theorem converts the forcing equation \(\dot z=1-x^2\) into a heightwise conditional law rather than only a global time average, couples it to the damped \(y\)-equation through an exact derivative-energy partition, and derives a sharp recurrence obstruction with a complete equality case. It applies to every compact invariant probability measure, not only numerically observed trajectories.

Same-model review: passed. Independent audit: not yet performed.
