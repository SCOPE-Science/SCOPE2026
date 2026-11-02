---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

In a one-dimensional graph, a strong pair is arrow v→w precisely when w is its unique earlier neighbor. With only two nonneighbors per graph vertex, no pair can first occur after order position four, and the two missing edges rule out three simultaneous pairs. Independent exhaustive enumeration of all vertex orders for n=4..7 reconstructed exactly eight edge types per u∈U: {a_u,e_u},{a_u,f_u},{a_u,p},{a_u,q},{a_u,b_u},{a_u,c_u},{b_u,d_u},{c_u,d_u}; arrows u→v for distinct U-members are isolated. The connected core has 6k+2 vertices and 8k edges (including 2k leaves), so β1=2k−1, with k(k−1) isolated vertices; all H2 and higher vanish. The square loops span Z[U] and independent differences of p–a_u–q paths span augmentation ideal I_U integrally. Swapping leaves 1 and 2 reverses both types of cycles, so H1=ε⊗(Z[U]⊕I_U), while isolated ordered pairs are fixed under that involution and permuted by S_U, giving Htilde0=Z[U^(2)]. Proof for all n uses the order-position bound, not finite exhaustive computation. At n=4 the core is a single circle and no isolates, agreeing with known base example.

## originality

PASS

The exact n=4 triangle-with-leaf single-circle case and complete K_n zero-dimensional result are already in Knudson–Owens-White. The inspected source does not classify all K_n with two incident deleted edges, which for all n≥5 produces a disconnected graph and nontrivial integral symmetry modules. The theorem adds an exact infinite near-clique classification beyond the cited base case; literature under alternative filtration strong-Morse terminology remains an explicit risk.

## value

PASS

Deleting two incident edges is the first sharp perturbation of a clique that produces positive-dimensional homology for this natural filtration-matching construction. The result completely determines graph core, isolated components and exact integral automorphism representation for all n. It is a motivated infinite structural boundary, not a single arbitrary small graph census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
