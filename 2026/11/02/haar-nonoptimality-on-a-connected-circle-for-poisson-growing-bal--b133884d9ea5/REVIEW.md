# Independent mathematical audit

## correctness

PASS

Subtracting first arrival time leaves 0<=H<=1/2. Under antipodal placement, the opposite-arrival delay is Exp(1/2), giving H=min(1/2,1/4+W/2). For Haar, point void probability is e^(-u^2). Two points at 3/8 and 5/8 yield the exact union exponent J(u)=2u^2 up to 1/8, then u^2+u/4-1/64; inclusion-exclusion and the antipode bound give an integral lower bound. Alternating cubic/quadratic Taylor bounds evaluate it to 29716847/62914560 while H_antipodal<=181/384. Independent exact rational integration confirmed both strict gap values. Recoloring at most an expected 3/(2048) seeds before the first seed alone covers and bounding cover-time change by 1/2 proves the full-support result.

## originality

PASS

Aldous 2022 Section 7.1 explicitly asks whether Haar always minimizes the Poisson growing-ball mean on compact groups; it discusses a fixed-radius circle nonoptimality example but states the growing-ball case is unknown. The assessed unit-circle growing-ball inequality is not an implication of the fixed-radius coupon model or finite cyclic examples. Contemporary planar Johnson–Mehl asymptotics treat another spatial/rate limit.

## value

PASS

Provides a strictly certified counterexample on a connected homogeneous compact group to an explicit natural optimization question; full-support perturbation shows nonoptimality is not solely caused by choosing discrete seed locations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
