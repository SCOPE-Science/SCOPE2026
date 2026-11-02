---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For positive q, detailed balance π_iP_ij=q_iq_j/(1-Σq_j²), and 2- and 3-step returns imply aperiodicity. The finite-state joint empirical flow rate J=ΣQ_ij log(Q_ij/(ν_iP_ij)) applies to balanced Q with zero diagonal. Necessity ν_i≤1/2 follows from outgoing flow; sufficiency via symmetric t_ij=(ν_i+ν_j-ν_k)/2=1/2-ν_k. Reversible P gives J(Q^T)=J(Q), so strict convexity forces unique symmetric minimizer; on 3 nodes symmetric row sums determine Q*_ij=t_ij. Substitution yields the displayed rate including boundary with xlogx convention; KL zero only at stationary π. Compact gap between unique optimum and other flows yields double-limit Gibbs conditioning for interior ν, R*_ij=t_ij/ν_i independent of q. Independently tested reversible stationary identities, balanced flow, and strict objective increase under nonzero cyclic circulation for 16 parameter combinations. Finite tests are not LDP proof.

## originality

PASS

Best-of-knowledge comparison by mathematical implication, using actual Resultary search, relevant primary source material, the assigned final claim, and explicit residual priorities. The contribution is limited to the exact special calculation/structural theorem; general underlying methods are credited.

## value

PASS

The complete explicit feasible triangle and evaluated rate surface quantify rare compositions of a natural mutation-spine Markov chain; a nontrivial and useful universality is that conditioned transition frequencies forget the original allele weights. Unlike merely restating level-2.5 LDP, the exact three-state entropy minimizer identifies the observable rare-event dynamics, with sharp interior and boundary scopes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
