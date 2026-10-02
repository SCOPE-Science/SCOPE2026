# Independent scientific audit — SCOPE-20260913-051

Audited at: 2026-10-01T03:14:08.262218Z

Disposition: **passed**

## Correctness — PASS

For beta=2pi/3 the sector is strictly contained in its tangent half-plane, whose fractional mean curvature at the face point is zero. Subtraction leaves twice a positive absolutely convergent integral over the missing wedge. A radius-1/2 disk inside that wedge gives the stated uniform lower bound, and the axial integral contributes the positive cylinder factor. On a homogeneous stationary cone, a constant face Lagrange multiplier must scale like lambda^{-s} and hence be zero, so the positive curvature excludes stationarity.

## Originality — PASS

Cesaroni-Novaga prove the 120-degree cone for the standard full cluster energy and treat weighted energies only for strictly positive phase weights. The audited functional omits the exterior perimeter, corresponding to a degenerate zero exterior weight, so their theorem does not cover it. No source located states this two-chamber exclusion.

## Value — PASS

The result cleanly separates two superficially similar nonlocal functionals and shows that the classical/full-cluster 120-degree law fails for the two-chamber sum. This is a motivated boundary/counterexample with an explicit uniform curvature margin.

## Residual risks

- The true stationary angle for the two-chamber functional remains uncomputed.
- The theorem is restricted to s in [3/4,1), although positivity itself holds more broadly by the same half-plane subtraction.

## Sources inspected

- https://cvgmt.sns.it/media/doc/paper/4489/fractionalpartitions_revised.pdf — Full primary paper inspected; the weighted theory explicitly assumes c_i>0 and the standard cluster energy sums all phase perimeters.
- https://arxiv.org/abs/1910.03429 — Primary preprint metadata/abstract checked for the 120-degree full-cluster theorem.
