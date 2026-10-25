---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Exact two-point counting-measure example H=H0=C^2, k=diag(1,0), f(1)=g(1)=e1 and f(2)=g(2)=e2 is Parseval/Bessel. For every h=(a,b), both 2020 journal scalar tests equal |a|^2=||kh||^2 while T_fT_g*=I != k (witness e2). Direct independent SymPy matrix arithmetic verified k*(I-k)=0 and e2 contradiction. In arbitrary COMPLEX Hilbert spaces with bounded Bessel maps, polarization of <(M-k)h,kh>=0 gives k*(M-k)=0, equivalent to P_{closure R(k)} M=k; the second test analogously gives k(N-k*)=0. In particular R(M) subset closure R(k), or onto(k), makes the first test sufficient; the corresponding dual condition applies to N. The 2019 preprint theorem ALREADY assumes onto(k) and onto(k*) and is NOT contradicted; the false unconditional theorem is the 2020 journal version. Source files result/proof/verification/review/slogan/metadata/audit fully inspected, all six Git blob identities and complete tree matched. No numerical experiment replaces the operator proof.

## originality

PASS

Best-of-knowledge original correction to the unconditional scalar-equivalence assertions printed in the 2020 journal Theorem 3.2; the 2019 PREPRINT version of the SAME authors’ Theorem 3.2 explicitly requires k onto in (i) and k* onto in (ii), so it is NOT refuted by a rank-one projection. The 2020 journal Theorem 3.2 removed these conditions and is refuted. Complex polarization and the onto repair are classical; the source-specific counterexample and exact projected-reconstruction diagnosis are the assessable contribution, not a newly discovered surjectivity theorem. No indexed correction of the 2020 journal theorem was found in the actual searches. Nonindexed errata remain possible.

## value

PASS

The 2020 published theorem purports to replace full continuous K-dual reconstruction by two scalar norm identities. A transparent C² Parseval example falsifies both unconditional statements and proves exactly which reconstruction component is invisible, so it is a motivated correction with direct implications for selecting continuous K-duals. Although complex polarization and the onto special case were already known (indeed the 2019 preprint stated onto), the journal introduced a broader false theorem. Demonstrating its false positives, and the exact projected statement that remains valid, is an independently useful source-specific repair rather than an arbitrary tiny or mechanical parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
