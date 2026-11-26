# Independent mathematical audit

## correctness

PASS

Subtract the rear equilibrium level 1/a from both pressures under g_r=1, then multiply by γ. The rear equation has no constant source in these coordinates, and the front equation has source (1−h)κ0+hκ1, where κ0=γ(g_f−1), κ1=γ(g_f^s−a_s/a); output is the difference of the two scaled pressures. Thus choosing γ/c and fixing κ0,κ1 yields the stated positive rates and pressure map p↦cp+(1−c)/a for all 0<c<1. The resulting scaled initial states agree. The unstimulated matrix is stable and invertible (negative trace and determinant a[a+(1+r)d]>0), so both published day-1 equilibrium initializations map exactly. Position equality by integration persists across input switches, pressure carryover, and the daily position-only reset, and gives identical defined threshold crossing times. A different measured absolute pressure or an independently fixed initialization not preserved by the map is outside the conclusion. Differentiating the constant-output curve gives the stated nonzero null vector (γ>0), hence a singular positive-weight sensitivity information matrix when the sampled observation map is differentiable. Reconstructing the alternative from the invariants with exact fractions (independent_checks.py 4) gives 1009009/10000000, 6760153/561000, 2891/450000 within Table S3 bounds, with more than a hundredfold change in g_f. This example uses the displayed rounded Table S4 seed-308 row, not undisclosed full-precision coefficients, nor a new empirical fit. There is no claim that all six surviving combinations are identifiable.

## originality

PASS

The general use of state/output symmetries is prior art. The distinct supported result is the exact positive within-bound affine equivalence that survives the published rear normalization in this particular motion-only calibration, with its explicit six-combination normal form.

## value

PASS

The original seven rates are fitted and mechanistically interpreted using motion data. This interior positive ambiguity survives all admissible schedules and is large at a published fit, so more motion data alone will not resolve it. The explicit reduced coordinates can be used for fitting, and the gauge shows why a pressure-sensitive measurement may be needed to distinguish original rates. This is a structural inference result, not a claim that the model's forward predictions are wrong.

The dated certificate retains the supplied scientific assessment, sources and limitations.
