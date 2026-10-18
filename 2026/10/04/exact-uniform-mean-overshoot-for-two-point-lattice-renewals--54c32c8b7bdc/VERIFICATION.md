---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: For t=b+u, b integer and 0<=u<1, crossing index is unchanged and R_t=R_b-u; only integer boundaries need maximizing. For integer 0<=b<m, conditioning on first long jump after j unit jumps gives e_b=sum_{j=0}^b p q^j(m+j-b)+q^{b+1}=m-b+q/p-q^{b+1}(m+q/p). Consecutive difference e_b-e_{b-1}=mu q^b-1, mu=q+pm, forces a unique or adjacent tied maximum at k=floor(log mu/(-log q)). Derivative of mu q^{m-1} in p proves k<=m-2. For b>=m, e_b=q e_{b-1}+p e_{b-m}; convexity prevents any later higher or tied maximum because the initial maximizers lie at one point or adjacent positions. Rare-long-jump scaling p=lambda/m gives (1/m)sup e_b ->1-log(1+lambda)/lambda, strictly less than lambda/(1+lambda) by (1+lambda)log(1+lambda)>lambda. Independent rational recurrence stress tests checked 715 parameter cases; infinite result is from induction.

## originality

PASS

Best-of-knowledge PASS: the classical Lorden and Carlsson–Nerman works give uniform moment inequalities, not an exact supremum/argmax for {1,m}; nearest Resultary records concern pairwise-dependent counterexamples and different stationary statistics. Older lattice-renewal literature remains a genuine alias risk.

## value

PASS

PASS: An exact sharp uniform renewal overshoot in the canonical {1,m} nontrivial lattice family and full maximizing boundary classification are natural refinements of Lorden’s general moment envelope. The rare-jump asymptotics quantifies a nontrivial persistent strict gap relevant to renewal/inventory tail bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
