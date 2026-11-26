# Independent mathematical audit

## correctness

PASS

The theorem survives unchanged; the complete corrected RESULT.md in /workspace/repairs/3 fixes the material misattribution of the general finite-gain criterion and noise-free path results and describes the coefficient checks accurately. Re-audit of the surviving result: L plus the two positive pins is positive definite by its quadratic form, and the stationary covariance is half the inverse. Grounding gives a middle resistance (x+s)(d−x+s)/(d+2s) at x and a tail resistance equal to distance plus the leader resistance. Summing shows the only fixed-gap placement dependence is the sum of the two quadratic tail lengths; moving one unit from the longer to the shorter improves it unless the gap in tail lengths is at most one. In /workspace/branches/replay_3.py, direct resistance summation and selected exact grounded matrix inverses agree; positive quadratic certificates exclude 1,2,2,4,5,6,5,6 gaps, respectively, for n=3,…,10. The remaining pair differences give strictly increasing transitions at five and nine, and the stated four phases and isolated ties at ten. For n=5m the smooth derivative numerator at gains 1 and 2 has one positive zero in (3m,3m+1), by its signs and Descartes' rule. The exact odd-tail correction is 1/4; the zero-correction gaps 3m−1 and 3m+1 bound all gaps farther out by strict monotonicity. Independently reconstructed rational gaps strictly select 3m+1 at gain one and 3m at gain two for every m≥2. Balancing gives exactly the listed sets, with all ties retained. The finite checks cover all relevant small orders, while the family conclusion follows from symbolic inequalities rather than sampled sizes.

## originality

PASS

General two-noisy-leader objectives and prior noise-free path placements are acknowledged. The distinctive claims supported here are the exact all-positive-gain P10 diagram with proof of the first possible decrease and the all-m fixed-gain reversal on P_(5m), not the formulation of the general placement problem or the first indexed observation of any reentrant example.

## value

PASS

The result challenges monotone gain-separation intuition in a common finite-gain consensus problem. It identifies the smallest counterexample, resolves every positive-gain tie there, and shows the decrease persists at fixed gains in arbitrarily large paths, rather than being an isolated finite anomaly or an effect visible only after rescaling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
