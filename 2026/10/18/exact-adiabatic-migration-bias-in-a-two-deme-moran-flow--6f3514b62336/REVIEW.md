# Review of the exact adiabatic migration-bias theorem

## Correctness

**PASS.** The exact mean-field ODE is reconstructed from the published death–birth transition rates. For the frozen system, direct polynomial elimination gives \((x-y)[1-(1-m)(x+y)]=0\); the analytic attracting branch near \((1,0)\) has \(x\ne y\), forcing the exact mean \(1/[2(1-m)]\). A uniform negatively symmetric Jacobian on a small invariant rectangle proves existence, uniqueness, and local attraction of its forced periodic orbit. An \(O(q/T)\) tracking estimate and an elementary trigonometric integral prove the stated slow-season value and strict inequalities. Symbolic computations and representative finite-period integrations are reproduced by `verify.py`, not used as substitutes for the proof.

## Originality

**PASS, with residual risk.** The closest work is Masoumi, Kaveh, and Ejtehadi (arXiv:2610.08160v1; sections 2–4 and Appendices A–C), whose model and schedule are explicitly acknowledged. It reports numerical frequency shifts and discusses a peak-amplitude interpretation of long seasons, but does not derive the exact frozen-branch sum, exact adiabatic average, or positive equal-mean Jensen gap. Aubrée and coauthors (doi:10.1093/evolut/qpac067) analyze allele fixation in a pulsed mainland–island model, not this symmetric deterministic two-deme equilibrium. Focused mathematical-record searches and comparisons with accessible prior claims identified no covering result. Generic adiabatic tracking and Jensen's inequality are existing tools; the model-specific exact sum and its evolutionary comparison are the subject of this claim. Unindexed equivalent algebra or newer literature could still exist.

## Mathematical value

**PASS.** The motivating model explicitly compares seasonal and constant gene flow. This theorem provides an exact, nonperturbative expression in migration amplitude for the slow-season limit on a specified branch, and gives a strict counterexample to a universal contraction-to-neutrality interpretation when the baseline is matched by migration mean. It distinguishes three physically different baselines, while quantifying the first nonzero difference at order \(q^2\). This is a structural population-genetic conclusion, not a mere numerical observation.

## Limits of the assessment

The range of \(q\) is existentially small; finite population stochastic behavior and other parameter regimes are not assessed. Relevant mathematical literature outside the indexed and inspected sources could contain equivalent formulations. The analysis is not an independent scientific validation.

Self-review: passed. Independent audit: not yet performed.
