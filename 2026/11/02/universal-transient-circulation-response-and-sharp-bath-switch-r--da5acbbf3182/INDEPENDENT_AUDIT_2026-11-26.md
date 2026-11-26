# Independent mathematical audit

## correctness

PASS

The conclusion survives; the frozen proof's Gaussian-tail justification for arbitrary initial laws does not. Convolution smooths a heavy-tailed initial law but need not give it Gaussian tails. The complete revised proof in repairs/5/RESULT.md convolves a nonsingular Gaussian with the independently transported initial law and controls the weighted L¹ gradient by the Gaussian's first weighted gradient norm and the initial first moment. This proves Fubini and exact crossed-derivative cancellation, with finite drift moment by the second moment. The resulting quadratic functional of the raw moments cancels every coupling except its own trace decay and the signed bath difference. The linear solution gives the unique stationary preparation and the value of Q(0). Multiplication by sign(c) and the positive Green kernel give the lower envelope and force saturation almost everywhere before the optimal zero; positive constant baths attain it even when c<0 in the original sign convention. The source checker tests 2,100 finite comparisons, not arbitrary-measurable or heavy-tailed inputs; the justification for those inputs is analytic, not based on a rerun of the checker.

## originality

PASS

On inspected evidence the distinctive claim is the fixed-trap bath-driven circulation mode paired with its sharp constrained first zero. Constant-bath covariance machinery already makes the constant-bath one-mode calculation a linear projection, and stationary torque is explicitly known; neither is claimed as a new general mechanism. The time-dependent bath difference and first-zero objective are not the controlled-trap full-state problem. No inspected statement gives the combined result. The proof repair changes no formula or hypothesized protocol.

## value

PASS

The selected output is the physical torque-related circulation moment, not an arbitrary eigenprojection chosen to produce a scalar ODE. The resulting sharp, experimentally interpretable swap time is independent of temperature scale and of coupling and anisotropy at a given trace; the comparison also rules out any faster protocol under the same difference bound and identifies the necessary equality control. This is a motivated exact consequence for a natural intervention, not a new claim about generic covariance evolution or a numerical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
