# Independent mathematical audit

## correctness

PASS

The kernel calculation (RESULT.md, lines 43–52) gives reciprocal circles centered at s=(1−r²)^−1 of radius R(s); the angle covers every point since m−1 is positive, and the denominator cannot vanish. Recomputing R′ and R″ gives R′²+RR″<α² by the positive tail of the expansion of (1−1/s)^−2(β−1); with D=1−R′²−RR″, the two contact derivatives are D and R′D/sqrt(1−R′²). At height y>0 the right branch covers from s_0=R^−1(y) to infinity in abscissa, while the left branch has derivative with the sign of Y(s)−y. Thus an attained interior minimum gives the entire closed slice, or a decreasing left branch with unattained limit gives the open slice. At y=0 the minimum is s=1. At α=1, R=s−β+β(β−1)/(2s)+O(s^−2) gives the claimed threshold; even at equality the derivative is strictly negative at every finite admissible s. The envelope slope is sqrt(1−R′²)/R′ and strictly decreases. At s=1+t, X−1 is asymptotic to t and Y to αt^β, so inversion gives the stated cusp with its coefficient. At α<1 the expansions give X−(sqrt(1−α²)/α)Y=β+O(s^−1). Inversion gives the limiting angles (at α=1 the limit is vertical) and maps x=β to the claimed diameter circle except for the zero endpoint, which comes only from infinity. All conclusions follow analytically; checker.py was inspected as a finite floating-point diagnostic and not executed.

## originality

PASS

Credit the circle description and qualitative corner to prior results, including an exact specialization of Proposition 3.7. The distinct, verified contribution is the evaluated envelope with exact ownership at α=1, including the threshold, the sharp cusp law, and the far-field geometry. The closest earlier exact monomial range claim uses a wrong kernel factor and is not an equivalent result.

## value

PASS

The canonical monomial family tests the difference between a filled range, its closure and pointwise attainment. Knowing precisely where the left contact radius escapes at unit modulus, and hence which entire arcs (including endpoints) are missing after inversion, answers a question not settled by qualitative cusp or circle filling theorems. The cusp reads off the degree and modulus and the far-field description gives the limiting directions at zero. This is a useful complete range classification, not a resampling of the circles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
