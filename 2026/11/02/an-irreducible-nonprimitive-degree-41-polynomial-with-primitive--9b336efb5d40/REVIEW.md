# Scientific review: primitive-constant polynomial counterexample

## Correctness — PASS

The field is well-defined because \(3^{20}\equiv40\pmod{41}\). Four explicit powers of \(\lambda=2+16w\) exclude every maximal proper subgroup of the cyclic group of order \(1680\), proving its primitivity. Iterating the \(1681\)-Frobenius adds the nonzero constant \(32w\) and gives \(41\) distinct conjugates, proving irreducibility without relying on a computer irreducibility test. Independent exact modular polynomial arithmetic then checks that the root's \((1681^{41}-1)/83\)-rd power is \(1\). Since \(83\) is prime and divides \(1681^{41}-1\), the root cannot generate the full multiplicative group. A separate finite enumeration checks all \(41^2\) constants and finds exactly \(64\) primitive coefficients with the specified order obstruction. The modular-exponent identity and the exhaustive count are exactly reproducible using the supplied code.

## Originality — PASS, qualified

Sharma's 2026 Conjecture 4.2 asserts universal primitivity in precisely this family. Its displayed numerical evidence ends at \(p=37\), whereas the verified counterexample is at \(p=41\). Proposition 4.1 proves only irreducibility and is fully compatible with this example. Searches for the specific conjecture, the \(41\)-degree polynomial, the order-\(83\) obstruction, and related Artin–Schreier formulations found no prior covering counterexample. Cohen's arbitrary-trace theorem establishes *existence* of a primitive element with a prescribed trace; it does not imply universal primitivity of this fixed polynomial family. A closely named Artin–Schreier research record addresses Goss's magic-index problem, not multiplicative order of this polynomial's roots. Full older cyclotomic literature was not comprehensively inspected; priority remains subject to that risk.

## Mathematical value — PASS

The counterexample settles the truth value of a specifically published, recent universal conjecture, not a routine special case or a small numerical refinement. Its characteristic is the next prime beyond the paper's tested range, and its fully irreducible polynomial isolates the failed assertion as primitivity rather than irreducibility. The exact \(64\)-of-\(384\) order-\(83\) obstruction count indicates that the failure is a significant natural stratum, not a single accidental coefficient. This does not resolve the paper's separate weaker existence conjecture.

## Closest literature and limitations

Primary comparison: Avnish K. Sharma, *Primitive Polynomials of the Form \(g(x)+\lambda\) over Finite Fields: Non-Existence Results and Conjectures*, arXiv:2608.07262, Proposition 4.1, Conjecture 4.2 and Table 6 (2026). Background: Stephen D. Cohen, *Primitive elements and polynomials with arbitrary trace*, Discrete Math. 83 (1990), 1–7. The enumeration counts only the specified order-\(83\) obstruction, not all possible nonprimitive cases, and no assertion is made about characteristics other than \(41\). Independent priority or mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
