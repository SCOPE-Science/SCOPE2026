---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Courant–Fischer makes λ2 concave in edge rates; averaging the m−1 equal-priced leaves ensures symmetric maximizer. The symmetric star characteristic polynomial is X(X−u)^(m−2)[X²−(2w+mu)X+(m+1)wu]. Reparameterization z=λ−/u leads to derivative sign (m−1)[(m+1−2z)²−t z²], yielding threshold √t=m−1. Below threshold rates are all 1/(m−1+t). Above: h=√t, B=m t+2(m−1)(h+1), w=[m(h+1)−1]/(hB), u=(h+2)/B, gap=(m+1)/B. Global uniqueness beyond symmetric optimum uses Fiedler eigenvector equality for above threshold and orthogonal leaf-vs-exception PSD contrast vectors for below threshold. Independently computed numerical eigenvalues and budgets for (m,t)=(3,9),(5,5),(5,25),(7,36),(7,37), matching formula. Boundary zero-weight star disconnects. Source symbolic checker independently inspects these identities.

## originality

PASS

General fastest-mixing Markov-process SDP and graph-Laplacian concavity/symmetry reduction are known from Sun–Boyd–Xiao–Diaconis and Ghosh–Boyd; their inspected main worked examples do not supply this one-price star two-branch closed form and uniqueness over asymmetric weights. Resultary exact semantic search found no published equivalent; possibility of a specialized star formula under algebraic-connectivity design remains.

## value

PASS

Provides an exact all-size parametric optimizer for a natural asymmetric cost design on a canonical graph, including non-obvious square-price transition, positive exceptional edge for any finite cost, rigorous uniqueness and asymptotic gain; useful to analyze spectral-gap allocation beyond generic numerical SDP.

The dated certificate retains the supplied scientific assessment, sources and limitations.
