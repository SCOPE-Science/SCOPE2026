# Independent mathematical audit

## correctness

PASS

Algorithm 1 of arXiv:2602.05893v1 initializes w₋₁=√varsigma and uses the minimum-norm convex-hull gradient with its current square included in w₀². Zero lies in the hull exactly on [−c,c], and outside to the right the closest gradient to zero is λy. Consequently the first multiplier of y=x₀−c is 1−1/√(r+y²), including the exact endpoint hit at r+y²=1. For 0<r<1 the derivative of the positive crossing depth is r/(r+y²)^(3/2)−1, strictly decreasing for y>0 and changing sign once inside (0,√(1−r)). This gives y*=r^(1/3)√(1−r^(1/3)) and depth (1−r^(1/3))^(3/2). The width test is δ≤2c, with equality captured at the far endpoint, and reflection proves the left-start result. For example, λ=1, varsigma=27/64, y*=3/8 gives depth 1/8: c=1/32 jumps from 13/32 to −3/32, whereas c=1/16 lands exactly on −c. If w₀>λ then the right-side distances decrease and stay positive as wₖ is nondecreasing. The upper bound wₖ²≤varsigma+λ²(k+1)y₀² makes the sum of λ/wₖ diverge; the log-product estimate forces the distance to zero. When r≥1 there is no crossing basin for y>0, not a separate real-valued width formula. The bundled script exists at artifacts/verify_pareto_capture.py; its finite checks were read, not executed. Its r=1,2 noncrossing checks use startup values outside the paper's range with λ=1, but the recurrence is still defined there and the same r values are realizable with admissible startup after rescaling λ. The analytical proof uses the stated scope and does not rely on those tests.

## originality

PASS

The algorithm and Pareto interval are known inputs. The distinct result is a sharp parameter-dependent threshold separating guaranteed first-crossing capture from possible complete skipping of a nontrivial Pareto interval, with the complementary no-crossing outcome. Neither the inspected algorithm nor the closest same-family and overshoot records give that comparison.

## value

PASS

The width is an intrinsic parameter of an elementary connected Pareto set for a named line-search-free method. The sharp law separates a guaranteed selection event from a strict skip of every Pareto point in one iterate, which criticality-rate estimates do not address. It also distinguishes finite entry from same-side convergence to a particular endpoint. The exact witness and equality case make the threshold useful for checking algorithm behavior, rather than merely showing an isolated overshoot.

The dated certificate retains the supplied scientific assessment, sources and limitations.
