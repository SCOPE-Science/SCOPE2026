# Independent mathematical audit

## correctness

PASS

The two poles are simple and positive. The surface resolvent numerator places its zero between the poles since the rate polynomial is negative at gamma/C_d; hence both exponential weights are positive. A rectangular pulse differentiates to a single impulse response before shutdown and a difference of translated responses afterward. This gives a unique surface maximum at shutdown and a deep derivative with the sign of (exp(b*tau)-1)/(exp(a*tau)-1)-exp((b-a)*t), initially positive at shutdown and crossing once. The resulting delay is the interval mean of tau/(exp(r*tau)-1) over the two rates. Its partial derivative in either endpoint is strictly negative, as seen by writing the mean on the fixed unit interval. Both generalized eigenvalues increase strictly with feedback and coupling and decrease strictly with either capacity: the derivatives are v_s^2, (v_s-v_d)^2, -r*v_s^2, and -r*v_d^2 for a C-normalized eigenvector. The coupling prevents either entry from vanishing, and a constant eigenvector would force r*v_d=0 by the deep equation. Pointwise differentiation of tau/(1-exp(-r*tau)) gives a derivative in (0,1), proving the duration claim as well. Independently replayed the example by bisection of the translated impulse derivative: python3 /workspace/checks/4_peak_example.py gives peak 22.2543875592 and delay 12.2543875592. This is illustrative only; the strict signs follow analytically. The supplied check and verification notes were inspected, not executed or treated as an attestation.

## originality

PASS

Accept the distinct simultaneous global comparative statics of the pulse peak delay in four separate physical coefficients, not the model, transfer functions, or elementary translated-impulse peak formula as independent advances. The strongest exact lag-function match concerns a serial two-rate response and is later by its record date; its available statement does not give the bidirectionally coupled heat-model parameter sensitivities. No positive evidence of prior coverage of the four-sign result was found in the bounded comparison. Primary-text limitations remain material to priority, not evidence of absence.

## value

PASS

Gives a usable direction-of-change theorem for how long deep warming continues after direct forcing stops, separately for both thermal capacities, leakage feedback and exchange, with no parameter tuning. The exact global directions are more informative than a representative time course or an unconstrained two-timescale fit. The result is limited to the specified linear two-layer pulse experiment, not a claim about emissions cessation or a calibrated climate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
