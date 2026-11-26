# Independent mathematical audit

## correctness

PASS

Reassessed the corrected theorem, not the frozen inference. The source allows x_0=B, and every feasible x has first coordinate ≥1. Normalization cannot change a minimizing vertex or the sign of a stopping dot product. On R_-=[1,2]×[−5,−50/19], C is uniquely minimizing, with dot product ≤4−2500/19<0, and the clipping excess numerator is a(2−0.9a)+b(50−0.9b)>0 for 0≤a≤1 and 1000/19≤b≤55. Its clipped map sends the vertical endpoints to 1/2 and 50/19. On R_+=[1,2]×[1/2,50/19], A is uniquely minimizing, with dot product ≤−23. For b=50+v, the concave term b(50−0.9b) is decreasing here, hence is at least 50000/361, which exceeds the maximum 19/10 contribution of the horizontal subtractands. The clipped A-map sends the vertical endpoints to −91/20 and −50/19 in R_-, and both horizontal updates preserve [1,2]. Thus no positive tolerance can stop the invariant alternation. The two-step map is 0.81x+0.09C+0.1A, with fixed point (28/19,−50/19) and partner (29/19,50/19). Strict inequalities at both points and single-step factor 0.9 give local attraction as well as the specific convergence from B. The repair explicitly demonstrates the common face AC and its negative support and proves the scalar decay, so the corrected claim is consistent with Theorem 3.2. The reversed normal selects B and does not make AC a positive-support minimizing face.

## originality

PASS

The supported distinct claim is the exact nonterminating NSA trajectory with an attracting orbit and an all-positive-tolerance sign obstruction. It does not claim discovery of fixed-step oscillation generally or a counterexample to the source's conditional decay theorem. The strongest inspected primary result is compatible with, but does not yield, this behavior.

## value

PASS

Even after removing the false fixed-face inference, the explicit attracting orbit exposes a real operational limitation of the mathematical algorithm: it can fail to return a separator on a strictly separated triangle despite its exact face-distance decay. The construction distinguishes distance convergence from algorithmic success, with negative stopping values for every positive tolerance, rational replay and robustness to local perturbations near the orbit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
