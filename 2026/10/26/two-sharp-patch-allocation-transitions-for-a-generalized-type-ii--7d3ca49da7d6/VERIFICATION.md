---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Reconstructed f_p derivatives and unique inflection at u0=((p-1)/(p+1))^(1/p), endpoint one-sided strict maxima, stationary equality f_p(t)=f_p(N-t) in derivative form. Under t/N=(1-tanh z)/2, the off-center stationary point equation gives N=Qp(z)=2 cosh(z)[sinh((p-1)z/2)/sinh((p+1)z/2)]^(1/p). The explicit monotonicity inequality using G(s)=s coth(s), H(s)=G'(s), and H(s)/s decreasing ensures Qp strictly rises from Nloc to infinity for EVERY real p>1 (no integer restriction). This proves exact count and sign of critical points, including flat strict local minimum at Nloc. Comparing endpoint and center payoffs gives Nglob, the ordering Nloc<Nglob, and the tied maximizers. Expansion log(Qp/Nloc)=z^2/3+O_p(z^4) proves the exponent-independent square-root coefficient. Independent bounded checks 618 comparisons, supporting but not substituting for the analytic argument.

## originality

PASS

Hill sigmoidal response and global maximization of sums of sigmoids are established, notably Fazel–Chiang 2005 and Udell–Boyd 2014. The relevant primary section of Fazel–Chiang handles nonconcave rational utilities via semidefinite/sum-of-squares relaxations, not a closed-form theorem for two equal patches and all real p>1. The exact double threshold, complete stationary-point topology and universal square-root onset were not identified as quoted prior statements in actual literature comparisons. Qualified best-of-knowledge due to possibility of elementary previous two-patch derivations.

## value

PASS

The distinction between local and global optimality in the same motivated response objective, rigorously valid for every real Hill exponent and the universal onset coefficient, identifies a nontrivial allocation trap. Its value is a precise model-theoretic threshold, not an empirical ecological or population dynamics claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
