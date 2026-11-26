# Independent mathematical audit

## correctness

PASS

An independent coordinate reduction uses m=x+y/2, d=y, p=z-2y, and Q=a m^2+kappa d^2-epsilon. On the stated locus the map is (m+(p+Q)/2,-d+p+Q,-p-Q). If the second iterate returns, the m equation gives Q'=0 at the intermediate point; the d equation then gives p+Q=0, and the p equation gives Q=0 and hence p=0. Conversely on that ellipse the map reverses d, so only the two d=0 endpoints are fixed, and d>0 gives one representative per primitive cycle. The Jacobian product at d and -d has determinant one, trace 3+a^2 m^2-4 kappa^2 d^2, and a fixed tangent. Its characteristic polynomial is therefore the stated one with Delta=4ac m^2-4 kappa epsilon. The transverse trace 2+Delta crosses 2 inside the ellipse arc and is less than -2 somewhere precisely when kappa epsilon>1; equality at the lower boundary is attained at m=0 only. At Delta=0 the full polynomial is (lambda-1)^3; the double multiplicity is the transverse one. No Jordan or nonlinear claim is needed. Independent symbolic multiplication and five exact cases, including an equality case, passed (python3 /workspace/branches/recompute_frozen.py).

## originality

PASS

Exceptional nonisolated two-cycles, their tangent multiplier and the generic classification of volume-preserving spectra are not the novelty. On inspected evidence, the exact variation of the transverse polynomial along the positive-definite singular ellipse and the sharp coexistence threshold are distinct from the generic isolated-orbit formulas and the earlier line example.

## value

PASS

The threshold characterizes coexistence of three different linear spectra for the same map along its period-two family, not just how to obtain a desired spectrum by varying the map. This is useful precise information on the singular case excluded by the generic period-two formulas; the conclusion is about normal multipliers, not nonlinear orbital stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
