---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Normalize an arbitrary nonzero real vector to sup norm one. Its signed active-set projective pattern lies in a ranked signed subset poset. If two patterns are comparable, a suitably signed small perturbation reduces one vector's norm strictly, contradicting directed Birkhoff–James orthogonality. Consequently a mutual-orthogonality clique injects into an antichain. A uniformly random coordinate permutation and independent signs generate a maximal chain hitting every rank-k projective pattern with probability 1/[C(n,k)2^(k-1)], proving the sharp LYM bound. For fixed k, all signed ternary support-k projective lines are pairwise mutually orthogonal, attaining it. Rank-size ratio 2(n-k)/(k+1) and binomial Stirling yield exact maximizing rank and asymptotic. Independently checked rank maxima n=1..16; checks are corroboration, not proof for arbitrary directions.

## originality

PASS

The published fixed-rank ternary-support family attains the lower bound but expressly does not claim global maximality; the 2021 symmetrized orthograph paper constructs only full-support sign families and general, weaker bounds. This record supplies the missing all-real-directions sharp upper bound by signed active patterns and LYM; related directed norm-recognition results do not force it.

## value

PASS

A canonical extremal invariant of a finite-dimensional real Banach-space orthogonality graph is determined exactly in every dimension with a matching geometric construction and a structural antichain proof. This nontrivially converts a previously constructive lower bound into a sharp universal theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
