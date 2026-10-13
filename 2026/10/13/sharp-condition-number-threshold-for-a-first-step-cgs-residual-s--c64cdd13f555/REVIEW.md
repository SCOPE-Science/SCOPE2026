# Self-review

## Correctness
PASS. The first standard CGS residual is exactly
\[
r_1=(I-\alpha_0A)^2r_0,
\qquad
\alpha_0=\frac{r_0^{\mathsf T}r_0}{r_0^{\mathsf T}Ar_0}.
\]
For SPD \(A\), spectral decomposition turns the squared residual ratio into a normalized fourth central moment. Convexity at fixed mean pushes the extremal spectral measure to the two interval endpoints. The resulting one-variable rational function is therefore an exact sharp envelope, not an estimate.

The envelope is strictly increasing in \(\kappa\). The threshold polynomial has exactly one root greater than one because its reciprocal reduction \(Q(y)\), after \(y=z+2\), has exactly one sign change and changes sign on \([2,\infty)\). The finalized checker verifies the exact rational witness, the polynomial reduction and isolating interval, and the stationary/elimination identities.

## Originality
PASS. The classical literature identifies CGS as a squared-polynomial method and explicitly describes wild residual-norm oscillations. The inspected statements do not quantify the sharp first-step SPD amplification, identify the endpoint spectral extremizer, give the threshold \(\kappa_*=3.442815869257\ldots\), or derive its \(\kappa^{3/2}\) asymptotic severity.

Database and primary-literature searches covered direct and equivalent formulations, including squared BiCG polynomial, first residual, residual amplification/spike, SPD/positive definite, condition number, endpoint spectra, and the numerical threshold. The closest retrieved records concern different iterative methods and do not imply the claim. The principal residual risk is uninspected older full text using a different moment-inequality formulation.

## Value
PASS. The result turns the long-known qualitative warning about CGS oscillations into a sharp safety frontier and exact worst-case law. It shows that nonnormality is unnecessary: a two-dimensional SPD diagonal problem already produces a first-step spike immediately above a modest condition number. This is useful for interpreting residual histories and for deciding when a smoothing variant such as TFQMR or BiCGSTAB is justified even on nominally benign spectra.

## Closest literature and limitations
Sonneveld's foundational paper introduces CGS; Freund's TFQMR paper explicitly calls out wild residual oscillations; Aihara's full-text product-method treatment states the exact squared residual-polynomial identity. None of the inspected statements provides the new sharp first-step envelope. The theorem is limited to exact arithmetic, the first unpreconditioned CGS step, standard shadow residual, and SPD matrices.

Self-review: passed. Independent audit: not yet performed.
