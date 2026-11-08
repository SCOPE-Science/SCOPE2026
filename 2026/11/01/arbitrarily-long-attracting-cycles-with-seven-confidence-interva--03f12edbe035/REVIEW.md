# Independent mathematical audit

## correctness

PASS

For each p>=2, Q=2^p-1, c=1/(4Q), orbit positions x0=1/Q and xj=2^(p-j)/Q (j>=1) are all distinct. The symmetric confidence set consists of [-c,c] and up to three positive bands and their negatives: I1 around the range 2/Q to 2^(p-2)/Q for p>=3, I2 around 2^(p-1)/Q, I3 around (Q-1)/Q; for p=2, I2 and I3 coincide and I1 is omitted. Their integer/Q offsets have strict margin c for intended trust and >=3c for excluded trust. At x0 the moving agent trusts stubborn opinion 1 only, giving R(x)=(x+1)/2; at the other orbit positions it trusts stubborn 0 only, giving L(x)=x/2. R followed by p-1 halvings forms a least-period-p cycle. A nonempty open c/2-neighborhood follows the same itinerary, errors halve at every step and return multiplier is 2^(-p); hence attraction is genuine, not a fragile point cycle. With <=2 agents, reciprocal averaging reaches consensus or a one-stubborn distance strictly contracts upon any nontrivial step, so no nonconstant cycle; the three-agent count is minimal. Independently checked exact rational transitions/trust/perturbations for representative p including 2..59,120,200. Those finite instances do not prove the universal p theorem; the symbolic integer separation does. Endpoints of confidence bands depend on p.

## originality

PASS

Zabarianska–Proskurnikov (2024) already constructs a period-three orbit with three agents and two distinct stubborn agents. The assessed contribution is the explicit all-p, <=7 symmetric-component construction with attracting open basin and minimal agent count; this is not implied by one period-three example. Piecewise contraction bounds on number of orbits do not bound period length of one orbit.

## value

PASS

Unbounded attracting least period with a constant three agents and seven confidence components isolates a genuine dynamical-complexity threshold left open by a single known period-three example. A robust open attraction basin and a least-agent proof give conceptual force. This theorem does not claim one fixed confidence set simultaneously has all periods, nor global attraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
