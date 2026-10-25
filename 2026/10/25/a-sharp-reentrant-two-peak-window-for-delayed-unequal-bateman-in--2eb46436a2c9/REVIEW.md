# Scientific review: delayed unequal Bateman inputs

## Correctness — PASS

The result follows directly from the linear absorption/elimination equations by impulse-response superposition. For times strictly after the second input, the derivative is a difference of two positive exponentials (or an affine factor times one exponential in the coincident-rate limit), so it has one possible maximum. For the delay above the single-input peak time, a first maximum already occurs. The second appears precisely when the derivative jumps from a strictly negative left limit to a positive right limit, equivalent to \(m>Q(d)\). Equality has no second strict maximum. The derivative \(Q'(d)\) changes sign at the single point \(2t_0\). These identities give all parameters, delay boundaries, and the sharp maximum \(m_*\). The reproducible code checks 2,200 numerical cases; finite checks are not substituted for the analytic proof.

## Originality — PASS within inspected literature, residual risk

The Bateman kernel and dose-response superposition are established. The claimed addition is the sharp unequal-amplitude peak-count law and its reentrant delay regime. The fully inspected Sahin–Benet 2008 repeated-dosing work, Davies et al. 2010 multiple-peaking survey, and Grover–Benet 2011 work on multiple-dose pharmacokinetics provide background and related mechanisms but do not state this exact two-input, unequal-relative-amount threshold. Godfrey et al. 2011 addresses double peaks through compartmental absorption models; only the abstract was available, so its full mathematical coverage remains unresolved. More general exponential-mixture and variation-diminishing statements could imply the special theorem; no exhaustive novelty guarantee is made.

## Mathematical value — PASS

The result classifies an observable nonmonotonic model phenomenon: delaying a relatively weak second input first allows two strict peaks, then fuses them into one, then resolves two again. The exactly computed critical relative amount and equality boundaries separate three practical idealized response regimes, and are valid for distinct as well as repeated rate constants. The conclusion is structural and not a mere numerical peak calculation.

## Scope and limitations

This is a mathematical property of the simplest linear first-order kinetic response to two ideal impulses. It says nothing about minimum peak prominence, pharmacodynamic effects, toxicity, patient-specific scheduling, nonlinear metabolism, or whether the features would be resolvable in clinical samples. Equivalent coverage in literature not accessible in full is possible. No independent review has been carried out.

Self-review: passed. Independent audit: not yet performed.
