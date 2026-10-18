---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For integers free of prime (r+1) powers, factorwise monotonicity maximizes sigma(n)/n at first k primes with exponent r for given omega(n)=k. Mertens/PNT give restricted Gronwall limsup lambda_r=1/zeta(r+1), achieved by primorial powers P_k^r. The moving finite exponential B_c=e^gamma e^x P(Poisson(x)<=floor(x+c sqrt x)) tends to e^gamma loglog(n) Phi(c), yielding limsup lambda_r/Phi(c). At c_r=Phi^-1(lambda_r), the lattice Edgeworth expansion gives phi(c_r)/sqrt(x)*((4-c_r^2)/6 - fractional_phase)+O_r(1/x) on extremal powers; small phase mesh gives both signs if r<=4, while c_r>2 for r>=5 makes the bracket negative. Independent Poisson CDF checks at x=500,2000,10000 and exact numerical quantile signs for r=1..9 support the lattice coefficient/cutoff. The asymptotic uniformity and infinitely many phases use prime-number-theorem and local expansion, not numerical sampling.

## originality

PASS

Best-of-knowledge: Mishra–Sarkar’s public abstract establishes omega(n)-indexed Robin truncation; its full text was inaccessible through public and Oxford routes, so no whole-document noncoverage is claimed. The reviewed theorem supplies a far smaller moving Gaussian cutoff, rigorous lattice correction, and r=4/5 phase boundary not implied by the accessible statement. Priority uncertainty is material but alone does not negate O.

## value

PASS

A sharp unconditional fixed-exponent-class Gaussian truncation threshold and phase-sensitive critical behavior are meaningful arithmetic/probabilistic invariants. The transition exactly between maximal exponents four and five is a natural boundary and goes beyond the original omega(n)-indexed finite truncation; classical Gronwall, Mertens and Poisson asymptotics are credited ingredients. No universal boundary classification or explicit finite n cutoff is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
