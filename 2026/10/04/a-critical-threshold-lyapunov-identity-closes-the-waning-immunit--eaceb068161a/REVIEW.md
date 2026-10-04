# Same-model review

## Correctness

PASS. The proposed functional is differentiated directly from the source equations and yields the exact identity
\[
\dot{\mathcal L}=\beta(S-S_*)h+\zeta_1(\mathcal R_0-1)E.
\]
The feasible-set bound \(S\le S_*\) makes this nonpositive throughout the closed threshold. Its zero set is exactly \(E=A=V=0\), after which the downstream hospital/ICU/recovery cascade is stable. A separate estimate for \(S_*-S\) proves Lyapunov stability at the critical endpoint, so the result is global asymptotic stability, not attraction alone.

## Originality

PASS. The source's theorems state only the strict condition \(\mathcal R_0<1\), while the conclusion claims \(\mathcal R_0\le1\). Exact-source and critical-threshold searches found no published correction or proof for this seven-class model. Related SAIRS literature proves equality-case stability for different compartment structures and does not imply this functional or result.

## Value

PASS. The source presents the closed threshold as its eradication conclusion. Closing the nonhyperbolic equality case therefore resolves a genuine theorem-to-conclusion gap rather than extending a numerical example. The weighted functional is also simpler than a characteristic-root argument and rederives the strict-subthreshold result in the same proof.

## Closest literature and limitations

The primary source is Egbelowo, Munyakazi, and Hoang (2022), DOI 10.3934/math.2022871. Ottaviano, Sensi, and Sottile, arXiv:2202.02993 / DOI 10.1002/mma.9303, prove a related \(\mathcal R_0=1\) disease-free theorem for an unvaccinated multi-group SAIRS model, but its transition graph is not equivalent to the seven-class SARS-CoV-2 system.

The result is restricted to the source feasible region and does not give a sharp critical decay rate or settle global stability of the endemic equilibrium.

Same-model review: passed. Independent audit: not yet performed.
