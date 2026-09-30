# Independent Audit — Time-varying rates gauge away constant parameters in the Moose–Wolf inverse model

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `e3fca8185f54a55cde4a7693ec4039d18e0a8f86`  
**Audited current source tree:** `e3fca8185f54a55cde4a7693ec4039d18e0a8f86`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record path is unchanged from the dispatcher's source-check commit, so the audited tree is the assigned source tree. GitHub was used read-only. The dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASSED

PASS. Direct substitution verifies the gauge exactly. In the Holling model, replacing (a,b,c) by any nearby admissible (a',b',c') and setting alpha'(t)=alpha(t)+y(t)/(1-x(t)^4)[a'/(b'+x(t))-a/(b+x(t))] and delta'(t)=delta(t)+c'x(t)/(b'+x(t))-cx(t)/(b+x(t)) leaves both state derivatives unchanged wherever the displayed denominators are defined; the ratio-dependent formulas are identical with b y+x denominators. More decisively, c alone is always gaugeable through delta, without dividing by 1-x^4. The reconstruction formulas from an observed C1 trajectory follow by solving the two ODEs pointwise. On compact regular intervals, sufficiently small parameter perturbations preserve smoothness and strict positivity of a positive death-rate function. Thus unrestricted time-varying alpha and delta make the constant interaction parameters structurally nonidentifiable despite perfect continuous observation.

## Originality — PASSED

PASS, narrowly scoped. The source abstract explicitly describes a non-autonomous prey-predator inverse problem with temporally varying intrinsic growth and natural-death rates, simultaneous estimation of time-dependent and constant parameters, and a structural-identifiability analysis asserting identifiability. General unknown-input identifiability theory is prior art, so no novelty is assigned to the principle that arbitrary functions can mask constants. Targeted searches found no prior public source-specific gauge for these Moose–Wolf equations. The new content is the exact model-level counter-gauge and the resulting correction to the claimed structural-identifiability interpretation.

## Scientific value — PASSED

PASS. The gauge changes the status of the inverse problem at a foundational level: stable fitted constants can be consequences of architecture, regularization, or optimization bias rather than structural identifiability of the non-autonomous ODE itself. The record also identifies what independent information about alpha or delta would generically break parts of the gauge. This is useful as a correction while appropriately not claiming that the trained neural-network parameterization itself has been proved nonidentifiable.

## Independent checks

- Independently substituted the transformed rates into both archived state equations and verified exact cancellation of all parameter changes.
- Checked the c-only gauge separately; it proves nonidentifiability even at states where 1-x^4 vanishes.
- Checked the reconstruction formulas and the local preservation of rate regularity/positivity under small perturbations.
- Read the public source abstract, which explicitly states that the intended model is non-autonomous with time-varying intrinsic growth and natural-death rates, estimates both time-dependent and constant parameters, and performs structural identifiability to ensure identifiability.
- Ordinary open full-text retrieval did not expose the source body; authorized institutional retrieval was then attempted and returned no verified PDF. No claim is made to have read inaccessible source text.
- Compared with general time-varying-parameter/unknown-input identifiability literature so that the audit does not over-credit the general mechanism.
- Verified no files under the assigned record changed between the dispatcher source-check commit and current main, and verified both dated independent-audit files and FAILED_ATTEMPT.md are absent.

## Limitations

- The conclusion treats alpha(t) and delta(t) as unrestricted unknown functions of the stated regularity; a separately declared finite-dimensional neural-network class is a different identifiability problem.
- The full source paper remained inaccessible in this run after open-access and authorized-retrieval attempts, so the audit relies on its public abstract for the source's top-level identifiability claim and independently checks the archived equations/gauge.
- No claim is made about statistical identifiability under a prior, penalty, or fixed training algorithm.

## Evidence and references

- https://arxiv.org/abs/2609.20793
- https://arxiv.org/abs/2211.13507
- https://doi.org/10.1098/rsif.2019.0043
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/19/time-varying-rates-gauge-moose-wolf-parameters--525e2b442818

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
