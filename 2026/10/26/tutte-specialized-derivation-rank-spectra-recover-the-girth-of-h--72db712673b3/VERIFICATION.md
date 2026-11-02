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

I checked the entire algebraic derivation parametrization, including characteristic two and disconnected/isolated vertices. Since a height-two incidence algebra has J^2=0, idempotent Leibniz identities force D(h)=sum_e x_e(h_v-h_u)f_e and D(f_e)=lambda_e f_e, with two freely independent field parameters per edge. Relative to diagonal L plus radical J the operator row matrix is [B_x | Lambda]. If S denotes nonzero lambda edges and B denotes zero-lambda edges with nonzero x, then rank D=|S|+rank(incidence(B))=|S|+|V|-c(B) over every field. Counting (x,lambda) choices yields the stated Tutte specialization. Subtracting the forest baseline termwise shows only cyclic B contribute, and the smallest possible rank g-1 arises exactly for full shortest g-cycles; coefficient c_g(q-1)^g is positive. Formula for unicyclic G follows by adjoining arbitrary forest-edge subsets. Independently computed q=2 four-cycle spectrum (1,12,54,109,80), q=3 (1,32,384,2064,4080) and several graph identities; source verify_derivation_rank.py genuinely solves all Leibniz equations in its finite prime-field checks. Neither source logs nor bounded instances were substituted for the universal proof.

## originality

PASS

Best-of-knowledge PASS for the distribution of ranks of ALL linear derivations, including outer derivations, and the girth recovery from its first cyclic coefficient. Krylov–Tuganbaev and Fornaroli–Khrypchenko provide prior derivation decomposition, and Tutte/graphic-matroid identities are classical. The neighboring published inner-derivation/element-centralizer enumerator differs on cyclic graphs and only covers the forest limit. A general weighted matroid-state-sum theorem could still imply this formula, hence residual historical priority is explicit.

## value

PASS

The theorem assigns a natural operator-rank distribution to every height-two incidence algebra and relates it to graphic-matroid invariants. Recovering girth and number of shortest cycles from the histogram gives interpretable structural information; the full spectrum is not equivalent to a routine parameter dimension computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
