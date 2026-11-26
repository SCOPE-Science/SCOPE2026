---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For algebraically closed k of prime characteristic p>=5, set y=t^(p+1), x=t^(p+2)u. The equation after dividing out t^((p+1)(p+2)) is u^(p+1)+1+lambda*t^(p^2-2p-5)*u^(p-1)=0. Its simple roots at t=0 lift. The orbit of x(t) under t->zeta*t has size p+1 by its leading exponent coprime to p+1; since the polynomial is monic of degree p+1 in x, this establishes irreducibility. In the Weierstrass basis 1,x,...,x^p over k[[y]], valuations are distinct modulo p+1, yielding semigroup <p+1,p+2> and delta p(p+1)/2. The coprime weighted initial Jacobian monomials x^p,y^(p+1) give mu=p(p+1). Writing M=x^(p-1)y^(p-1), the Jacobian relations give [f]=(5lambda/2)[M], and the maximal basis weight shows that (M) has basis M,yM. This gives the two Tjurina cases. For lambda nonzero the Frobenius induction keeps precisely the top monomial with exponent pair (p^e-1,p^e-1) at N=(p^e-1)/(p-1), killed by one more copy of f. At zero, f in (x^p,y^p) gives the upper bound p^(e-1)-1 on nu_e; at that degree the balanced binomial term is nonzero by Lucas and fits in the exponent box. Frobenius powers of the maximal ideal are preserved by local automorphisms, and units preserve ideal membership, so the distinct thresholds separate the p=5 strata. These exact arguments, not the finite script, cover all parameters.

## originality

PASS

Prior higher-weight threshold jumps and overlapping general threshold calculations are real. The supported distinct claim is the exact simultaneous branch, Jacobian/Tjurina and threshold calculation for this family, particularly separation at fixed mu=tau=30 in characteristic five, not a new general threshold method or the first threshold jump at fixed semigroup.

## value

PASS

The two strata answer a concrete invariant-detection question: even fixing the branch semigroup and both conventional local algebra lengths, the Frobenius invariant detects a difference. The single family explains exactly why that coincidence occurs at five and disappears at larger primes, rather than just recomputing a familiar diagonal threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
