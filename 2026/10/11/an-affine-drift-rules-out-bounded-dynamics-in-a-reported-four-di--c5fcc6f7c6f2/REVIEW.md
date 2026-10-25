# Scientific review

## Correctness
**PASS.** For the printed system
\[
\dot x=-x-4y,\quad\dot y=x+z^2+aw,\quad\dot z=1+x,\quad\dot w=-by,
\]
let \(F=w-\tfrac b4(x+z)\). Then \(\dot x+\dot z=1-4y\), hence \(\dot F=-by-\tfrac b4(1-4y)=-b/4\). If \(b\ne0\), no forward-complete orbit remains bounded. A compact positively invariant set, a periodic orbit, a compact attractor or a compactly supported invariant probability measure would contradict the drift. The argument is independent of \(a\) and does not establish global forward existence. The excluded case \(b=0\) admits equilibria, for example \((-1,1/4,1,0)\).

## Originality
**PASS, best-of-knowledge.** The complete defining 2021 article was compared at the equations, numerical evidence, and conclusions. It presents the same autonomous vector field but does not state the constant affine drift; indeed its bounded hidden-attractor interpretation is incompatible with it. The 2023 full-text network-control example reproduces the exact four equations and assumes bounded node coordinates, without stating the obstruction. The 2022 same-authors follow-up is described as having a nontrivial equilibrium, distinguishing it from the present nonzero-\(b\) system; only its abstract and bibliographic data were accessible, so complete noncoverage is not asserted. Searches also considered exact-equation corrections, affine coboundaries, global monotone observables, and closely related Sprott flows. None established dominating prior coverage. A differently indexed correction remains possible.

## Mathematical value
**PASS.** This corrects a global dynamical interpretation in a published and subsequently reused concrete system. Negative divergence or the absence of equilibria does not itself rule out chaotic attractors; the affine drift does. Despite the elementary cancellation, the all-parameter exclusion of compact invariant dynamics directly addresses a substantive model-validation problem.

## Scope and evidence
The conclusion is for the exact printed autonomous ODE with any real \(a\) and \(b\ne0\). It does not classify finite-time escape versus asymptotic unboundedness, the \(b=0\) dynamics, numerical integrations, a modified follow-up model, or controlled network systems. The algebraic identity was independently checked with exact symbolic arithmetic; finite numerical trajectories are not required. No formal verification or external expert attestation is claimed.

References: Al-hayali–Al-Azzawi, *J. Phys.: Conf. Ser.* 1879 (2021), 032031, doi:10.1088/1742-6596/1879/3/032031; Al-Azzawi–Al-Hayali, *Archives of Control Sciences* 32 (2022), 37–56, doi:10.24425/acs.2022.140863; Liang–Deng–Zhang, *Mathematics* 11 (2023), 3543, doi:10.3390/math11163543.
