---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The real Hilbert–Schmidt dissipation identity forces peripheral eigenoperators to commute with each positively weighted rank-one projector. They are block diagonal with diagonal even block C. The commutator with the hopping Hamiltonian is off-diagonal, excluding nonzero imaginary eigenvalues. At zero, the two hopping block equations give [C,TT†]=0; off-diagonal entries of TT† at distance two connect the even words, forcing C scalar (automatic for d=1). The odd block differs from the same scalar by an arbitrary operator supported on ker T on both sides. Norm contraction excludes a Jordan block at zero. The adjoint generator reverses the Hamiltonian sign and has the same kernel, so the limiting spectral projection is indeed Hilbert–Schmidt orthogonal, giving the stated all-state formula including dark coherences. Complementary Walsh zero modes pair to give one odd-supported mode per pair in even d, and none in odd d. Even translations make the odd-site dark weight constant, so its square yields the 2/(πd) term by Stirling; the bright term is exponentially small. A direct d=2 check gives T all ones, rank(D)=1, odd-site return 1/3. The uploaded numerical checker was inspected, not run; the exact limit and asymptotic are proved analytically and do not establish a relaxation rate uniform in d.

## originality

PASS

The supported contribution is the explicit trace-preserving stationary algebra, convergence and return law for individually monitored even vertices. General Lindblad structure, the Walsh spectrum and the overlapping dark multiplicity and localized dark weight are not independent originality claims. The strongest inspected halfcube result is for absorption, not trace-preserving dephasing; the bright block and fixed-point calculation are material differences. This is a best-of-knowledge assessment, not a priority certificate.

## value

PASS

The explicit full limit distinguishes dark coherence retention from ordinary mixing, and predicts an order-1/d return where an exponentially small return might be expected on 2^d vertices. It also settles all initial states and arbitrary positive site strengths in the specified model without relying on uniform rates. This is informative without any claim about relaxation time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
