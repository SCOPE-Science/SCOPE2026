---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For a connected simple unicyclic graph, a nonzero principal Pfaffian of order 2ν(S) exists whenever the induced matching on its endpoints is unique. Distinct perfect matchings can differ only on the sole full even cycle. With the cycle fully supported, let a_v=ν(T_v−v), b_v=ν(T_v); b_v−a_v∈{0,1}. If every b_v=a_v, all maximum matchings stay off cycle-to-tree edges, their maximal Pfaffians share the same two-monomial even-cycle binomial Δ_C. If some b_v=a_v+1, a maximal matching using a cycle-to-tree edge yields a unique-monomial nonzero Pfaffian. Each exceptional support has exactly one in q−1 nonzero cycle-weight assignments satisfying Δ_C=0, and deleting one cycle matching edge gives a nonzero Pfaffian of order 2ν−2, so the drop is exactly two, including char2. Summing support counts proves R_G=H_G(q−1,z)+(q−1)^(ℓ−1) z^(ℓ/2−1)(1−z)∏_v Q_v(q−1,z) for even ℓ, and R_G=H_G for odd ℓ. O’Brien–Voll/Rossmann char rank conversion gives the ordinary character-degree formula for odd q only. Independent direct Gaussian elimination for a four-cycle with pendant length-two path gives q2 ranks [1,15,36,12], q3 [1,56,384,288], matching the factorized formula; not a universal proof.

## originality

PASS

Li–Yu (2014) classify fixed-sign real skew ranks for unicyclic oriented graphs, a genuinely close structural predecessor, but not all finite-field weight specializations or character multiplicities. The published Resultary forest, bare-cycle and cone results were materially read and represent proper graph families or distinct operations; none implies a general rooted-attachment product without matching-state analysis. Rossmann asks the general character-distribution question, O’Brien–Voll supplies conversion only. The factorized full-unicyclic histogram is distinct under inspected evidence, with historical Pfaffian-enumeration risk acknowledged.

## value

PASS

Unicyclic graphs are the next natural class beyond forests and cycles in Rossmann’s graphical-group enumeration question. A uniform factorized correction isolates an algebraic cycle-cancellation obstruction and computes every rank stratum/odd-field character-degree multiplicity for all rooted attachments. Exact classification over a natural infinite graph class has intrinsic combinatorial and representation-theoretic value; evaluation may remain exponential.

The dated certificate retains the supplied scientific assessment, sources and limitations.
