# Independent mathematical audit

## correctness

PASS

At the critical parameter, use time γt and shift p=p_c+y. With β=n/(n−1) and λ=(2n−1)/(n−1), the two vector-field components are βiy and −λy−βy²−2(p_c+y)²i/(1−i). The common graph slope is a=−2p_c²/λ; solving the nullcline gives b_q=(−βa²−4p_c a−2p_c²)/λ, and solving invariance gives b_h=b_q−βa²/λ. Thus both positive trajectories have leading damping A=−βa, but the cubic coefficients are C=βb with different b. In the full system the transverse error obeys e′=(−λ+O(i)+O(e))e. In a small tube about the center graph this gives exponential decay, and i′≤β|e|i since the graph drift is nonpositive for small i≥0; the integrated bound i≤i(0)exp(const·|e(0)|) closes the small-tube argument for all sufficiently small positive initial states. For u=1/i, the error is O(u⁻²)+O(eu) in u′=A−C/u+error. Grönwall first gives u=O(1+t); positivity, local attraction and transverse decay then yield u∼At, followed by u=At+O(log t). Subtracting both the linear and logarithmic terms leaves an integrable derivative and finite constant. The same argument omits e on the nullcline reduction. Time rescaling alters the linear coefficient and constant, not −C/A. The nullcline and full linearization use the same p-root at i=0, hence the same threshold; the n=3 coefficient does not reverse sign, and the stated cubic numerator is positive and increasing for n≥4. Independent bounded symbolic replay: /workspace/branches/independent_replay.py, log_correction(); this checks coefficients, not the infinite-time limit.

## originality

PASS

The precise pair closure, critical parameter, nullcline and leading coefficient are inherited. The supported contribution is the exact difference between critical reciprocal-prevalence logarithms for the full and quasi-static systems, including the uniform-in-integer-degree sign reversal for n≥4. Neither generic normal-form theory nor the cited reduction supplies the exact comparison without the invariance calculation.

## value

PASS

The full and quasi-static ODEs have the same threshold and leading critical decay, yet for all n≥4 the reduction reverses the first logarithmic correction. The exact coefficient gap isolates a concrete limitation of the fast-nullcline approximation that cannot be seen from threshold or leading-order tests. This is a local benchmark for the deterministic closure, not a claim about stochastic network extinction or real pathogens.

The dated certificate retains the supplied scientific assessment, sources and limitations.
