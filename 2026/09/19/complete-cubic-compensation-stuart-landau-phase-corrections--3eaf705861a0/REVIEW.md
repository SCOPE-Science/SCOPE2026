# Same-model review

## Scientific claim reviewed

For the straight-isochrone three-oscillator Stuart–Landau system in arXiv:2609.20632v1, the resonant cubic monomial \(z_k^2\bar z_j\) supplies a pairwise second-harmonic phase channel that is absent from the paper's displayed enumeration of nonlinear pairwise cubic couplings. Once this channel and the other resonant cubic signatures are allowed with independent coefficients at strength \(O(\varepsilon^2)\), the entire explicit second-order phase correction in the source's Eq. (55) can be canceled exactly.

## Correctness

**PASS.**

The source gives the general first-order projection of a resonant cubic monomial,
\[
z_pz_q\bar z_r
\mapsto
\sin(\theta_p+\theta_q-\theta_r-\theta_j+\xi),
\]
for the equation of oscillator \(j\). Setting \(p=q=k\) and \(r=j\) gives
\[
z_k^2\bar z_j
\mapsto
\sin(2\theta_k-2\theta_j+\xi),
\]
which is a pairwise second harmonic and satisfies the same rotational resonance condition as the source's other cubic terms.

For straight isochrones, direct phase projection on \(z_m=Re^{i\theta_m}\) is
\[
R^{-1}\operatorname{Im}(e^{-i\theta_j}H_j).
\]
Applying this to the proposed \(H_j\) reproduces \(-f_j^{(2)}\) term by term. The symbolic artifact independently expands the source's Eq. (55), constructs the controller projection, and obtains an identically zero residual.

The order counting is consistent. The new controller is multiplied by \(\varepsilon^2\), so its first-order phase projection enters at \(O(\varepsilon^2)\), while mixed terms with the original \(O(\varepsilon)\) linear coupling first enter at \(O(\varepsilon^3)\). This is the same perturbative bookkeeping explicitly used by the source for a nonlinear coupling whose strength is chosen \(O(\varepsilon^2)\).

Potential failure modes were checked:

- The missing monomial is not equivalent to the two first-harmonic nonlinear pairwise cases listed by the source; its phase vector is \(-2e_j+2e_k\). It is admissible under the same rotational symmetry because \(z_k^2\bar z_j\mapsto e^{i\phi}z_k^2\bar z_j\) under a common phase rotation.
- Its coefficient can be complex, so one monomial spans both the shifted and unshifted second-harmonic components needed in Eq. (55).
- Constant and first-harmonic pieces of Eq. (55) are also cubic-realizable through terms already compatible with the source's general cubic formula.
- The claim is only second-order phase cancellation. It does not assert cancellation of amplitude corrections or higher perturbative orders.

## Originality

**PASS, to the best of our knowledge, with a narrow novelty claim and a substantial prior-design caveat.**

The primary source was inspected at the explicit second-order formula, cubic classification, and coupling-design sections. It states that every resonant cubic coupling has form \(z_pz_q\bar z_r\), then says that when only \(j,k\) occur, two nonlinear pairwise cases arise. The displayed list does not include \(z_k^2\bar z_j\), even though substitution into its own general formula gives a distinct second-harmonic phase signature. The source later describes its compensation as necessarily partial because its chosen physical-nonpairwise terms do not remove the additional pairwise and self-interaction corrections.

Searches for the source identifier/title together with second harmonic, cubic coupling, exact cancellation, phase design, and synonymous formulations found no public correction or source-specific complete cubic compensator. The current SCOPE archive was searched for the source identifier, Stuart–Landau, nonpairwise phase reduction, and second-order phase correction; no overlapping accepted record was found, and recent repository changes did not indicate an overlapping contribution.

Broad exact interaction design is prior art and is excluded from the novelty claim. Kori et al. (2008) give a general synchronization-engineering framework based on designed nonlinear feedback. More importantly, Namura, Muolo, and Nakao (Chaos 36, 023120, 2026; DOI 10.1063/5.0307452) state that optimal pairwise and higher-order interaction functions can be designed to realize prescribed higher-order Kuramoto dynamics for arbitrary smooth limit-cycle oscillators. The complete proof body of that paper was not fully inspected. This is a material residual risk for any broad claim that exact phase synthesis is new.

Accordingly, the novelty claim is restricted to two source-specific facts: (i) the missing \(z_k^2\bar z_j\) cubic phase class in the enumeration of arXiv:2609.20632v1, and (ii) the explicit proof that the source's complete Eq. (55), including its pairwise second harmonics, has a preimage inside the same simple resonant cubic polynomial class. Standard normal-form resonance, second harmonics, and general inverse phase design are not claimed as new.

## Value

**PASS.**

The correction changes the interpretation of the source's engineering limitation. Its specific two-type physical-nonpairwise controller with one strength parameter is necessarily partial, but resonant cubic coupling itself is not too small to cancel the full second-order correction. The omitted pairwise second-harmonic monomial is exactly the phase channel needed to close the cubic basis. The explicit compensator provides a directly testable design that makes the physical oscillator network agree with its first-order Kuramoto–Sakaguchi phase model through \(O(\varepsilon^2)\).

This is useful both as a correction to the cubic classification and as a sharper synchronization-engineering statement: the distinction is between a restricted controller family and the full resonant cubic family, not between physical and emergent corrections in principle.

## Limitations

The theorem is restricted to the source's explicit straight-isochrone, \(c=-1\), identical three-oscillator setting without self-coupling. It is a phase-reduction statement through second order and does not control \(O(\varepsilon^3)\) terms, amplitude observables, or finite-coupling global dynamics. General exact interaction synthesis is established prior art. The full proof body of Namura–Muolo–Nakao (2026) was not fully inspected and remains the main originality uncertainty for broader formulations.

Same-model review: passed. Independent audit: not yet performed.
