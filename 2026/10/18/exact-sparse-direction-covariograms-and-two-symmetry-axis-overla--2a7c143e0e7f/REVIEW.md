# Independent mathematical audit

## correctness

PASS

C_d={sum |x_i|<=1} has volume 2^d/d!, d>=3. Difference-body support k*t<=2 and signed-permutation invariance are exact. k=1 reduces to translated l1 ball radius 1-t/2; k=2 uses (u=x1+x2,v=x1-x2) square overlap of area 2(1-r)(1-r-t), followed by the l1-shell beta integral. k=3 base 3D lens gives 4/3-3t+3t²/2, and integrating over the remaining d-3 l1 coordinates gives A^(d-2)(A²+(d/2)aA+d(d-1)a²/12) with a=3t/2, A=1-a. Independent facet-halfspace convex-hull integration for d=3,t=13/100,k=1,2,3 gave measured/closed volumes 1.089867166666667,1.074798,0.968683333333333 (absolute discrepancies <=7e-16); this tests only samples. In d=3, put t=s/sqrt(k). The exact pair-difference quadratics have two roots strictly ordered s13=0.698560766..., s12=0.945467749..., while H2-H3 has negative discriminant, proving the three asserted strict rankings. No claim of arbitrary-direction extremality.

## originality

PASS

Explicit L1 cross-polytope k=1,2,3 fixed-axis covariogram polynomials and exact octahedral crossing locations are narrower in parameters but not implied by prior full-covariogram uniqueness or the rotationally averaged correlation. Resultary nearest hypercube record is an L-infinity rather than L1 body.

## value

PASS

The d-dimensional explicit sparse-axis overlap polynomials give reusable model benchmarks, and the unexpected two exact reversals distinguish three natural octahedral symmetry classes. This is a motivated geometric covariogram measurement, not a tiny numerical advantage or arbitrary shape slice; the all-d result is mathematically self-contained.

The dated certificate retains the supplied scientific assessment, sources and limitations.
