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

Writing each zero-sum vertex coefficient alpha_x=u_i/n_i+v_x with zero within-part v sums gives exactly alpha^T D_p alpha = 2^p sum_i (1-1/n_i)u_i² -sum_i u_i² - 2^p sum_x v_x². This proves the iff via the Rayleigh maximum Lambda, strictness and the all-singleton Lambda=0 boundary. The compressed diagonal spectrum on H gives top eigenspace multiplicity k-1 when the maximal a_i repeats, and otherwise the unique secular root in (a2,a1), with multiplicity one. Schoenberg centered Gram B=-J D_p J/2 gives exact minimal affine dimension. For (m,2,..2) r>=3 the top eigenvalue ((r-1)(1-1/m)+1/2)/r exceeds every two-part maximum, and for K_{4,2,2,2} the block-sum vector (3,-1,-1,-1) at 2^p=3/2 gives 3/8 while all pairs have 2^p Lambda<=15/16. Independent rational quadratic-form checks agree; they do not prove all r,p.

## originality

PASS

Sánchez gives a general finite-metric negative-type criterion and bipartite calculations. Obata treats this exact complete multipartite graph family at fixed p=1, a substantial known slice that is fully credited; Robertson provides bipartite embeddings, and Das–Mohanty fixed p=2 squared-distance matrices. The variable-p part-size Rayleigh law, precise rank loss and pair-invisible collective failure are not explicit in the inspected statements, but elementary specialization of known tools remains a significant priority risk.

## value

PASS

The sharp generalized roundness and critical affine Euclidean rank for an infinite canonical graph class are motivated metric invariants. A concrete strict obstruction unseen in every two-part induced subgraph explains why local bipartite tests miss global Hilbert embeddability; it is more than an arbitrary numerical re-evaluation of fixed p=1 literature.

The dated certificate retains the supplied scientific assessment, sources and limitations.
