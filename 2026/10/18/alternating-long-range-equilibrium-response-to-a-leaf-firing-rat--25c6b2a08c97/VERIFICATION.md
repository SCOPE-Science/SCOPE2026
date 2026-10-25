---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

From z_e=μ_e^α derive strictly convex potential α∑z_e^(1/α)-∑_v p_v log S_v, Hessian D_e δef +∑_{v incident both}w_v, D_e,w_v>0. Coercivity, nonzero S_v at minimizer and negative boundary one-sided derivatives give unique positive optimum and smoothness. Differentiating wrt leaf rate gives Hx=e_root/z_root; exact positive subtree Schur-complement C_e=D_e+w_child/(1+w_child Σ_child C_f^-1) and negative child transfer show strict sign alternation for every edge in a finite tree. Finite changes inherit strict derivative sign; α=0 is correctly excluded. Formula is derived, not inferred from saved numeric logs.

## originality

PASS

Qin's cited model establishes existence/uniqueness of an equilibrium, not sensitivity sign propagation. The new result determines every cross-edge derivative's sign and magnitude via a tree Green-vector elimination. Full Qin preprint inaccessible due authorization, named as priority risk; no clear stronger or equivalent comparison was found in actual Resultary searches.

## value

PASS

Strict alternating response to a single leaf firing rate in every finite tree, at all positive rates and 0<α<1, is a structural comparative-statics theorem for a natural weakly reinforced urn equilibrium; the exact positive cavity recursion is independently useful and nonlocal, not a textbook restatement of equilibrium uniqueness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
