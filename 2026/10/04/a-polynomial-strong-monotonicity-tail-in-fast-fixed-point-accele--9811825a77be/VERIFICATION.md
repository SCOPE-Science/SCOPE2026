---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Specializing the stated FFP2 recurrence to \(T=0\) and \(G(x)=\lambda x\) gives the inspected scalar two-state recurrence. The package's source-bound replay uses \(t_0\ge\max\{r,((r-1)(2r-1)\eta)/((r-1)\eta-\nu),(r-1)/(r+1)\}\), so the proof's \(t_k\ge r\) requirement is satisfied. Positivity and \(0<q_k=x_k/z_k\le1\) follow inductively. The stable comparison \(q_{k+1}\le\theta q_k+\theta r/t_k\), \(\theta=(1-a)/(1-c)<1\), gives \(q_k=O(t_k^{-1})\). For \(p_k=t_kq_k\), the exact recurrence has \(p_{k+1}=(1-a)(p_k+r)+o(1)\), hence \(p_k\to r(1-a)/a\) and \(t_kh_k\to r/a\). The product update for \(z_k\) then has decrements \(\delta_k=s/t_k+o(t_k^{-1})\) with summable squared errors, yielding \(\log z_k=-s\log k+o(\log k)\), and therefore the two claimed iterate exponents and kth-root limit.

## originality

PASS

Fresh Resultary searches found no prior theorem giving the exact FFP2 scalar exponents or ratio limits. The primary preprint's accessible abstract advertises general accelerated/sublinear guarantees for distributed composite monotone inclusions, not a sharp strongly-monotone scalar asymptotic. Full primary text was unavailable through the lawful routes attempted, so no whole-document exclusion is claimed; that access limitation is retained as a residual risk. Nearby strongly-monotone methods use different recurrences and therefore do not imply the polynomial tail of this unmodified FFP2 run.

## value

PASS

A condition-number-one strongly convex scalar witness showing a parameter-dependent polynomial tail in an acceleration scheme is a meaningful algorithmic boundary: it separates the problem's strong monotonicity from the recurrence's actual rate and motivates restart or strong-monotonicity-aware modification. The exact exponents and ratio limits are more informative than a generic sublinear upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
