# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

For
\[
\dot x=-a(x+y),\qquad
\dot y=-kxz-y,\qquad
\dot z=gxy+d
\]
with \(a,k,g>0\), direct differentiation gives
\[
\frac{d}{dt}\left(y^2+\frac{k}{g}z^2\right)
=-2y^2+2\frac{k}{g}dz,
\]
\[
\frac{d}{dt}\left(z+\frac{g}{2a}x^2\right)
=d-gx^2,
\]
and
\[
(x^2)'=-2ax^2-2axy,\qquad
\dot x^2=a^2(x+y)^2.
\]
The symbolic verification artifact independently reduces every residual to zero.

The global-existence argument is valid because
\[
W'\le W+\frac{k}{g}d^2
\]
bounds \(y,z\) on finite intervals, after which the stable linear \(x\)-equation bounds \(x\).

For \(d<0\), the identity \(H'=d-gx^2\) gives \(z(t)\le H(0)+dt\), so \(z(t)\to-\infty\).

For \(d=0\), \(W'=-2y^2\) gives boundedness and \(y\in L^2\). The differential inequality
\[
(x^2)'\le-ax^2+ay^2
\]
gives \(x\in L^2\). Hence \(xy\in L^1\), so \(z\) converges. Bounded \(\dot y\) makes \(y\) uniformly continuous, and \(y\in L^2\) then implies \(y\to0\); stability of \(\dot x+ax=-ay\) gives \(x\to0\).

For bounded \(d>0\) trajectories, endpoint terms divided by \(T\) vanish in the exact balances, yielding
\[
A_T(x^2)\to d/g,\qquad A_T(xy)\to-d/g
\]
and
\[
A_T(z)-1/k-\frac{g}{kda^2}A_T(\dot x^2)\to0.
\]
The periodic-orbit formulas are exact specializations. For compactly supported invariant probability measures, integrating the same generator identities yields the stated measure formulas. Equality in the mean-\(z\) inequality forces \(x+y=0\) on the support; compact invariance then leaves only the two equilibria \(E_\pm\).

No regularity or boundary condition beyond the smooth autonomous ODE and the stated parameter signs is used.

## Originality

**PASS, to the best of our knowledge.**

The checked literature confirms the standard Burke–Shaw equations and chaotic parameter choices. Panchev, Spassova and Vitanov (2007) studied the Burke–Shaw family and explicitly mention parametric and temporal asymptotes in their abstract. A 2022 Lorenz-type-system review records the standard equations and equilibria. Shukla et al. (2026) analyze a torque decomposition and state in the abstract that all four torque types are needed to create chaos.

Searches for Burke–Shaw time averages, mean-square identities, forcing balance laws, global convergence at zero forcing, invariant-measure constraints, and equivalent formulations did not locate the theorem stated in RESULT.md. The novelty claim is therefore limited to the exact combined balance-law theorem and its consequences, not to the broad qualitative observation that external forcing is relevant to chaos.

### Principal residual prior-coverage risks

1. **Panchev, Spassova and Vitanov (2007), DOI 10.1016/j.chaos.2006.03.037.** The full text was not inspected. Its abstract says that temporal \(t\to\infty\) asymptotes are studied for both the generalized Lorenz and Burke–Shaw systems. It could contain a related asymptotic identity or special-case result. No accessible abstract or indexing text exposes the exact sign trichotomy or invariant-average formulas.
2. **Shukla et al. (2026), DOI 10.5890/DNC.2026.03.007.** The full text was not inspected. Its abstract overlaps the qualitative conclusion that the full torque structure, including external torque, is needed for chaos. No accessible abstract text exposes global convergence for \(d=0\), escape for \(d<0\), or the exact \(d>0\) long-time averages.

These access limitations leave a nonzero originality risk, but the available evidence does not provide concrete coverage of the theorem.

## Value

**PASS.**

The theorem converts the forcing term into an exact global organizing parameter. It rules out every bounded recurrent regime for negative forcing, proves convergence of every zero-forcing trajectory, and imposes exact moments on every bounded positive-forcing regime. In particular,
\[
\langle x^2\rangle=d/g
\]
is a parameter-exact diagnostic independent of \(a\) and \(k\), while
\[
\langle z\rangle\ge1/k
\]
has an exact nonnegative defect term. These formulas can be used both in qualitative analysis and as consistency checks for numerical attractors or periodic-orbit computations.

## Evidence checked

- S. Panchev, T. Spassova, N. K. Vitanov, *Chaos, Solitons & Fractals* 33 (2007), 1658–1671, DOI 10.1016/j.chaos.2006.03.037.
- “The fractional-order Lorenz-type systems: A review,” *Fractional Calculus and Applied Analysis* (2022), DOI 10.1007/s13540-022-00016-4.
- V. K. Shukla et al., *Discontinuity, Nonlinearity, and Complexity* 15(1) (2026), 99–107, DOI 10.5890/DNC.2026.03.007.
- Symbolic verification in `artifacts/verify_burke_shaw_balances.py` and its recorded output.
