# Independent mathematical audit

## correctness

PASS

The generator of dX=(Q-X)dt+sqrt(2)dW, dQ=(X-Q)dt/gamma+sqrt(2/gamma)dB with reset (X,Q)->(0,Q) at rate r>0 has Lyapunov drift LV=4-2(X-Q)^2-rX^2. Strictly positive quadratic damping gives a unique finite-second-moment stationary law by same-noise/same-jump contraction. Reconstructed all three stationary covariance equations and solved C=[[a,b],[b,b+1]], then K(t)=exp(At)C where A=[[-1-r,1],[1/gamma,-1/gamma]]. Difference K12-K21 equals -2/[gamma(r+2)+1] times a positive two-exponential divided difference, with exactly one positive-lag absolute maximum. Its first two right derivatives give s=r+1+1/gamma and inverse gamma^{-1}=-(s+1)d1/2, r=s-1-gamma^{-1}. Independently verified the probe-only (H(0),H'(0+)) inverse, calibration and positivity domain. Numerical independent 9 positive (r,gamma) settings x 3 lags; the proof not the grid covers all r,gamma,t>0.

## originality

PASS

Best-of-knowledge qualified originality: the exact published model/theorem comparisons below do not establish an earlier dominating theorem for the narrow stated new remainder. Related prior methods and components explicitly credited; uninspected specialized literature risks remain.

## value

PASS

An experimentally interpretable time-direction asymmetry and two separate structurally identifiable inverse maps for a physically motivated retained-bath resetting model; goes beyond the prior equal-time moment family and controls a concrete inverse problem under explicit scale calibration. It is not merely the general textbook matrix-exponential identity, since the exact nonrenewing reset covariance and injective formulas must be assembled.

The dated certificate retains the supplied scientific assessment, sources and limitations.
