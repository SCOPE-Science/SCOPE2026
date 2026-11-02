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

Represent a plane by a rank-two 2×n basis matrix; each adjacent determinant vanishes iff neighboring nonzero vertex columns occupy the same projective line. For support S with c components the number of rank-two ordered matrices is (q-1)^|S|((q+1)^c-(q+1)); subtract zero-support correction and divide by |GL_2(q)|. The cyclic occupancy transfer has characteristic polynomial lambda^2-(1+w)lambda-qw and a correction qw^n for all occupied; eigenvalue dominance near w=q-1 yields quasi-powers and a CLT with the claimed nonzero variance coefficient. Independent canonical-RREF enumeration for q=2 n=4,5,6 and q=3 n=4 matched direct induced-component predictions; independent symbolic derivatives for q=2,3,5,9 matched mu and sigma². Group equivalence is restricted to odd prime fields and subgroups containing G'.

## originality

PASS

Qiao’s 2024 paper (full primary PDF, Theorem 1.2, Lemma 2.3 and detailed Section 2 proof inspected) already supplies the global finite polynomial existence and componentwise rank-condition enumeration, so UNREFINED rank-two counts are not original. Qiao does not state the cyclic two-state support-refined distribution, explicit fixed-field Gaussian support CLT, its constants or golden-ratio high-field limit. A published SCOPE result on character degree enumeration of cycle graphical groups counts a different invariant. Classical finite-state transfer/quasi-power methods cover the methodology, but do not document the specialized statement as presented.

## value

PASS

The support size is a natural, presentation-relative statistic of abelian subgroups in the first nontrivial quotient dimension; dimension one is always isotropic. A complete exact distribution and typical-density/variance CLT for all cycle lengths and fixed finite fields capture structural subgroup behavior absent from unrefined counts. It is more than a lookup and does not claim arbitrary abelian subgroups or uniform growing-q limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
