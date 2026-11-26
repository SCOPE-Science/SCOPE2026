# Independent mathematical audit

## correctness

PASS

The LCM identity and prime-power ranks give the stated max transition: a positive b injects 2 into the two-adic exponent and reduces the old b by one, a positive a injects 1 into the three-adic exponent, and positive d injects 3 into the two-adic exponent while dropping by one. In particular z(7)=8 and v_7(F_8)=1. The fifth-prime exponent is invariant. After two steps with d≥2 the three exponents are max(2,a−2j,3·1_{j≤d}), max(1,b−j), and max(0,d−j) for j≥2; substitution propagates the formula, including the step after the last 7 disappears. The first fixed time is the maximum of the three coordinate deadlines. With d=1, the lone delay is (0,b,1)→(3,0,0)→(1,1,0)→(2,1,0) for b≤1; otherwise (a_1,b_1)≥(3,1) and the fixed point is not reached at step one. For d=0 outside the eight listed small states, step one gives the stable quadrant a≥2,b≥1 with decrements clipped to 2 and 1. Direct transition in the eight states reproduces the table and the two fixed-point families. At t≥5 at least one of b≥t+1, a≥2t+1, d≥t−1 is necessary; at t=5 both competing pure powers exceed 3^(t+1), and the ratios increase thereafter. The pure power of 3 has exactly height t; any extra factor loses uniqueness of the minimum only by increasing the input, so there is exactly one minimizer. Independent direct modular rank iteration for every 7-smooth input up to 3^9 covered 425 trajectories and verified heights and endpoints, including minima for t=5–8 (python3 /workspace/review_checks.py). Supplied code was inspected, not executed; finite checks are not the proof.

## originality

PASS

Credit the known prime-power and LCM identities, fixed-point classification, global convergence, and large powers-of-two heights. The strongest catalogue match also gives the full five-smooth slice (d=0), but it neither includes the 7-coordinate nor yields the restricted least-input theorem without controlling the new competitors. The supported distinct contribution is the exact extension through all echelons of the 7-adic exponent, its boundary delay, and the resulting minimum theorem on the full 7-smooth stratum.

## value

PASS

The naturally closed 7-smooth domain beyond five-smooth inputs exhibits a new mechanism: the disappearing 7-part pins the two-adic coordinate above its stationary level, and the last 7 can induce a transient on small states. The exact mixed-height law exposes where that mechanism determines the full stopping time and determines whether adding the new prime can beat the old pure-power-of-three witnesses. This supplies usable exact orbit and extremal information across the whole domain, not a tabulation of selected inputs or a global minimum claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
