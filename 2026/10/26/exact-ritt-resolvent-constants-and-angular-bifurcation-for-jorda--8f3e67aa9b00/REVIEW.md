# Independent mathematical audit

## correctness

PASS

The exterior-to-circle reduction follows by applying maximum modulus to the scalar matrix coefficients of (z−1)(zI−T_q)^−1; its limit at infinity is I, whereas its norm at −1 exceeds 1 for every q<1. Independently, for 0<q<1 put x=(1−q)/|z−q| on the circle and let b=(sqrt(4+x²)+x)/2 be the triangular singular norm. Since x=b−1/b, q times the squared boundary objective is b²(1−x²)=5/4−(b²−3/2)². As x increases through [(1−q)/(1+q),1], b increases, so the optimal point is the endpoint or x=1/sqrt(6), with the stated transition. The endpoint produces the first branch (also directly valid at q=0); the interior produces sqrt(5)/(2sqrt(q)) and |z−1|²=5(1−q)²/q. At the transition this distance squared is 4 and its derivative in q is −5(q_*^−2−1). Since 4−|e^{iθ}−1|² is asymptotic to (π−θ)², this gives both the exponent and the coefficient of angular splitting. Norm convergence T_q→I and the identity resolvent give the stated jump. The exact replay is the completed-square identity above together with the circle relation in RESULT.md lines 64–71; verify_ritt.py was inspected but not run, and its numerical samples are not the continuum proof.

## originality

PASS

Best of the retrieved evidence: the distinct claim is the optimal Euclidean Ritt constant on this specific path, including the change in boundary maximizers and the limiting jump. The same Jordan pencil and the general Ritt resolvent formalism are prior. The closest statements inspected neither evaluate this optimization nor imply the transition or the jump without a separate extremum calculation.

## value

PASS

The pencil is the straight norm-convergent path from the two-dimensional nilpotent Jordan contraction to I. Its exact resolvent norm is a meaningful sharpness benchmark, not just a sample value: the computation locates where the worst resolvent direction leaves −1, quantifies its angular motion, and gives an explicit failure of continuity at I within contractions. Useful as a finite-dimensional test for resolvent-constant estimates, without claiming a general higher-dimensional classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
