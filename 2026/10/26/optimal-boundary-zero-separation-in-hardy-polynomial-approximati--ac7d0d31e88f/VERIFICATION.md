---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed the residual problem: 1-r is divisible by the quadratic exactly when r has the two required evaluations, or the value and zero derivative at the double root. The residual degree bound N-1 then gives an admissible quotient of degree at most n. Inverting the two evaluation rows gives the stated formula with numerator 2(N-Re S_N); at the double root the Gram rows are 1 and k, giving 2(2N-1)/(N(N+1)). Dividing both expectation expressions by c^2 makes their integrands jointly continuous at c=0. The limiting divided denominator is strictly positive on any bounded c-interval (at zero it is Var(U)=1/12 and for c>0 the continuous uniform characteristic function has modulus less than one), so Riemann sums really give locally uniform convergence including collision. The geometric-sum estimate uses the shorter angle in [0,pi] and forces scaled cost 2 along unbounded-scale subsequences. The sign of F-2 is the negative of the sign of 4 sin(t)(t cos(t)-sin(t)), t=c/2: on (m*pi,m*pi+pi/2) tan(t)-t crosses from negative to positive exactly once for m>=1, while on the latter half the bracket stays negative. Direct differentiation gives F'/2=W/D^2 and W'=c^3 sin(c)-4(1-cos(c))^2. On (2pi,3pi), the ratio of the two positive terms is strictly increasing when the second is divided by the first: its log derivative is 3 cot(t)/2+tan(t)/2-3/c>0 by AM–GM. Thus W first increases and then decreases, and its opposite endpoint signs force exactly one zero. Later windows have F>=2-8pi/(16pi^2-4), strictly larger than F(5pi/2) by the displayed rational difference (the cubic numerator is positive from 3 onward). The escape estimate and compact-uniform convergence then force every minimizing angle sequence to converge in scaled units to the unique global optimum. Fresh local replay used modified Gram–Schmidt on the coefficient columns z^j f_theta and orthogonal projection of 1, testing n=0..11 at theta=0,1/16,7/16,1,2,pi: 72 comparisons, maximum absolute discrepancy 3.51e-14. Solving the derivative numerically at 55-digit working precision with seeds 7,8 gave 7.5403141895947861456 and error 1.7912691607609162356, not a root certificate. The package checker was inspected, not executed; the continuum conclusions rest on the proof.

## originality

PASS

Best-of-knowledge pass for the global limiting optimum, unique placement scale, and window analysis. The exact finite two-point Gram formula and repeated-root starting point are not new claims.

## value

PASS

The angle is a natural design variable rather than an arbitrary parameter slice. Separating the two fixed-node baselines from the smaller optimized cost shows that neither collision nor macroscopic separation is asymptotically best. The global proof locates the single relevant scale despite infinitely many competing windows and controls all optimal sequences, not just selected numerical examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
