---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Reflexive modules are second syzygies (Enomoto), and every second syzygy is projective for gl.dim A<=1, so ref A=proj A. For any simple right S, if projective it embeds as a direct summand of regular A and Hom(S,A)≠0. If nonprojective its minimal resolution 0→P1→P0→S→0 has nonzero projective P1; assuming Ext^1(S,A)=0 makes Hom(P0,A)→Hom(P1,A) surjective. Extending coordinates of a split embedding P1→A^m gives h:P0→A^m with hj equal to that embedding and a retraction P0→P1, which splits the resolution, contradiction. Hence each simple index belongs to I_ref(A), satisfying both hypotheses of Enomoto Theorem 5.5. Passage to basic Morita representative preserves heredity. This proves for all finite-dimensional hereditary k-algebras over arbitrary fields; no finite examples used as infinite proof.

## originality

PASS

The 2026 full Enomoto paper supplies the general criterion and one hereditary three-vertex example, but the relevant inspected theorem and examples do not assert the uniform all-hereditary conclusion. The nonprojective-simple splitting lemma supplies the missing input. Resultary searches on reflexive equivalence and full I_ref turned up no broader direct coverage; short-corollary priority risk is recorded.

## value

PASS

Hereditary finite-dimensional algebras constitute a central representation-theoretic class. Proving the newly introduced reflexive equivalence collapses to ordinary Morita equivalence on the entire class is a natural, useful rigidity boundary beyond a single small example; it does not claim the same for gl.dim=2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
