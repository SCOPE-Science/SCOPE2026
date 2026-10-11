# Independent mathematical audit

## correctness

PASS

Arbitrary antiderivative tests in x and y yield \(\mathbb E[y\mid x]=0\) and \(\mathbb E[z\mid y]=0\), hence the four zero first/mixed moments used in the proof. Stationarity of z then gives \(\mathbb E[xz]=-a\), while stationarity of xy gives \(\mathbb E[y^2]+\mathbb E[xz]=0\), so \(\mathbb E[y^2]=a\). Nonnegativity excludes a<0. At a=0, zero y square plus support invariance forces y=z=0, exactly the equilibrium line. For a>0, the variance/covariance formulas and Cauchy--Schwarz are immediate, and nonzero zero-mean y has both signs. The exact checker independently verifies all generator identities and the a=3/4 specialization.

## originality

PASS

The full foundational NE6 paper was inspected: it catalogs the flow at \(a=3/4\), reports Lyapunov/chaos data and a period-doubling route, but does not state the all-invariant-measure RMS/covariance law or the \(a=0\) recurrence boundary. The fractional-order follow-up changes the dynamical category. Targeted Resultary search returned related stationary laws for other systems but no NE6 equivalent.

## value

PASS

NE6 was introduced as a no-equilibrium chaotic flow at positive forcing. The exact law \(\mathbb E[y^2]=a\) converts that forcing into a sharp compact-recurrence boundary, completely classifies the critical parameter, and fixes the RMS amplitude and a covariance for every recurrent statistical state at positive a. That is a natural structural invariant of the source family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
