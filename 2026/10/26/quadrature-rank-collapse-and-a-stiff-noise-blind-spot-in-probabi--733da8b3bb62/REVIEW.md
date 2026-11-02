# Independent mathematical audit

## correctness

PASS

For A=[[0,1],[0,-a]], H=(a,1) and v(s)=exp(As)B, direct exponentiation gives Hv(s)=1. Gaussian conditioning a positive quadrature covariance sum w_i v_i v_i^T with H therefore returns exactly κ² weighted variance of (1-e^{-as})/a, establishing P1=0 for any node and Pm>0 for positive distinct nodes m>=2. Explicit two-point Gauss rule gives κ²h a^{-2}e^{-ah}sinh²(ah/(2√3)). At fixed m>=2, smallest positive Gauss node determines exponential stiffness decay while the continuous integral variance is κ²/(2a³)(1+o(1)). Rank-one induction gives zero filtered covariance at EVERY mesh point from zero initial covariance and noiseless EKL H. For forced y’=-ay+t, y(0)=0, the midpoint conditional mean h(1-e^{-ah/2})/a exceeds exact h/a-(1-e^{-ah})/a² by e^{-ah/2}(2sinh(ah/2)-ah)/a²>0. Independent Gauss-quadrature numerical checks for m=1,2,3,5 and three positive (a,h) pairs verify finite formulas but do not prove limit.

## originality

PASS

The actual 2023 source introduces Gauss–Legendre square-root noise quadrature m=q, while its proof of exponential-trapezoidal equivalence uses exact covariance. The conditioned covariance rank-zero conclusion for that literal quadrature, the forced linear ODE false-certainty witness, and sharp fixed-order stiff limit are additional formulas not found in the inspected sections/appendix. General low-rank filtering warnings are prior but do not supply this particular ODE solver mechanism.

## value

PASS

A natural fixed-order discretization of a probabilistic ODE filter can report exactly zero mesh uncertainty while making strict error; for any fixed larger quadrature order its stiff variance scale is exponentially too small. This is a mathematically explicit, design-critical mechanism, not a generic numerical warning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
