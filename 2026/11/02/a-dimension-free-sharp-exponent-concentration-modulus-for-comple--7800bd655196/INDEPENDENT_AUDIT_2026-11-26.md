# Independent mathematical audit

## correctness

PASS

The frozen proof is correct: Schwarz–Pick and the even part control the mixed and pure discarded terms, respectively; a polytorus maximizer exists; the Cauchy bound e² along complex rotations yields H=2e⁴+4e², and two Taylor bounds plus real/imaginary sign selection give the claimed constant. The zero-deficit limit is legitimate. For the repair, independently checked the stronger prior-work specialization: at a norming polytorus point choose w_j=iε_j x_j to capture at least half the mixed linear norm, average at x±(sw+μv), and use the squared ball bound 1+s² and pure tail norm ≤δ. Then s||L_v||≤4δ+4s², optimizing at s=√δ and taking a limit when δ=0. The surviving three-coordinate obstruction is exact: on the tridisk torus the phase of z_3 aligns the two summands, and the remaining maximum is max(cosθ+2b sinθ)=√(1+4b²). Dividing the squared normalized discarded norm by δ_b gives 1+1/√(1+4b²)→2, excluding all p>1/2. For one retained coordinate, the mixed linear norm equals its value in modulus at the unit retained coordinate, so Schwarz–Pick plus the pure tail bound gives 3δ−δ². Finite tests are not the proof. The replacement checker verifies 100 exact Pythagorean instances; the original supplied checker was inspected, not run.

## originality

PASS

Final repaired finding only. The frozen originality assertion that the upper rate needs new work FAILS: the pre-limit proof of the prior theorem directly implies a strictly better constant, 8 instead of 8√(e⁴+2e²+1/2). Preserve the old finding as evidence but credit that upper bound as background. The repaired claim is the exact exponent obstruction with only three coordinates, together with the linear one-retained-coordinate contrast. The inspected prior concentration theorem and its optimality discussion do not supply this obstruction; the one-coordinate estimate itself uses standard Schwarz–Pick.

## value

PASS

The exact example sets a hard limit on every uniform deficit bound and identifies the minimal retained-coordinate geometry responsible: one retained coordinate permits an improved linear rate, whereas two retained and one discarded coordinate already saturate the uniform exponent. This is a motivated sharpness result for the pre-existing concentration theorem, not a weaker numerical rewrite of its upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
