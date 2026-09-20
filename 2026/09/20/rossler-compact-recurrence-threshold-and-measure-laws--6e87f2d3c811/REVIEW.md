# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The core identities are exact consequences of invariance, not numerical fits. Direct differentiation gives
\[
\frac d{dt}\left(\frac{x^2+y^2}{2}+z\right)=ay^2+b-cz,
\]
while averaging \(\dot x\) and \(\dot y\) yields \(\langle y\rangle=-\langle z\rangle\) and \(\langle x\rangle=a\langle z\rangle\). Eliminating the second moment gives
\[
a\operatorname{Var}(y)=c m-a m^2-b,
\]
whose discriminant is \(c^2-4ab\) and whose exact root factorization is the stated variance-gap law. Independent symbolic expansion of all polynomial identities gives zero residual.

The compact-set implication was stress-tested separately. Every nonempty compact invariant set of a continuous flow supports an invariant probability measure, so the variance inequality rules out every compact invariant set when \(c^2<4ab\), not only periodic orbits. Conversely, an equilibrium exists whenever \(c^2\ge4ab\), proving the exact if-and-only-if threshold. A bounded forward trajectory would be global and have a nonempty compact invariant omega-limit set, so none can exist below threshold.

The positivity argument for \(z\) uses recurrence rather than an assumed positive initial condition. Since \(\dot z=b>0\) on \(z=0\), a trajectory can cross that plane only from negative to positive. A recurrent Birkhoff-generic point with negative \(z\) therefore cannot cross and would have nonpositive mean height, contradicting the strictly positive mean forced by the energy balance. The crossing plane has zero invariant measure because a trajectory meets it at most once. Regularizing \(\log z\) by \(\log(z+\varepsilon)\) then justifies the harmonic identity without assuming that the support stays a positive distance from \(z=0\).

At \(c^2=4ab\), zero variance makes \(y\) constant almost everywhere. Invariance forces the complete trajectory through almost every support point to keep this value, so \(\dot y=0\), hence \(x=am\); then \(\dot x=0\) forces \(z=m\). This proves uniqueness of the invariant measure. The statement for bounded forward trajectories is deliberately only weak convergence of empirical measures; no unsupported pointwise convergence claim is made.

## Originality

**PASS, to the best of our knowledge.** Searches covered Rössler/Rossler terminology together with compact invariant sets, bounded solutions, invariant measures, stationary/time averages, moments, covariance, no-equilibrium dynamics, hidden attractors, the discriminant \(c^2-4ab\), and synonymous formulations.

The strongest older overlap is Starkov--Starkov (2007). Its accessible abstract explicitly states that if the Rössler system has no equilibrium points then it has no periodic orbits, and it studies localization/nonexistence of compact invariant sets in specified half-spaces. That prior result is credited and the no-periodic statement is not claimed as new. The present theorem replaces periodicity by arbitrary compact invariant sets and bounded forward trajectories and supplies exact measure-wide mean, variance, covariance, and harmonic-mean laws. Because the full 2007 theorem statements were not accessible, that paper is a material residual coverage risk.

Bramburger--Fantuzzi (2024) is the most relevant measure-theoretic prior. Its general method uses invariant-measure Lie-derivative constraints and its Rössler example approximates a physical measure and unstable periodic-orbit measures from data. The inspected full Rössler section reports approximate low-degree moments but does not state the parameter-uniform identities or recurrence threshold here. This makes the individual generator identities conceptually standard; originality is assigned to their exact closed combination and global dynamical consequences, not to the general principle \(\int Lg\,d\mu=0\).

Cândido--Novaes--Valls (2020) and the 2026 Llibre--Szumiński preprint address local zero-Hopf periodic-orbit/tori bifurcations and non-integrability. Fowler--McGuinness (2023) treats the large-\(c\) asymptotic bursting regime. Igra's recent rigorous work proves chaotic and periodic dynamics under heteroclinic hypotheses with equilibria. No inspected source states the exact compact-recurrence equivalence, the variance-gap law, the harmonic defect law, or the unique compact invariant measure at the saddle-node equality.

## Value

**PASS.** The strongest conclusion is a sharp global structural obstruction: in the standard positive-parameter Rössler family, removing all equilibria by crossing \(c^2=4ab\) simultaneously removes every compact invariant set and every bounded forward orbit. Thus this classical family cannot realize an equilibrium-free hidden compact attractor in that parameter sector. At and above the threshold, the same argument yields exact statistics for every compact invariant measure rather than for one numerically selected attractor, including a variance-collapse law as the saddle-node closes and an exact relation between arithmetic and harmonic mean height.

## Scientific limitations

The theorem is restricted to \(a,b,c>0\). It does not classify the dynamics for \(c^2>4ab\). At equality it proves uniqueness of the compactly supported invariant probability measure and statistical convergence of bounded trajectories, not pointwise convergence of every bounded trajectory. The inaccessible full text of Starkov--Starkov (2007) is the principal originality uncertainty. Originality is therefore asserted only to the best of our knowledge.
