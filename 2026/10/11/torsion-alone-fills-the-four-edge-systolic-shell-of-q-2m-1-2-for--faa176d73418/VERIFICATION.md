---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The theorem itself is proved symbolically in `RESULT.md`. The standalone `verify.py` supplies independent checks of every local identity used in that proof and a broad finite sanity sweep.

For each \(m\) with \(4\le m\le20\), the program reconstructs the full cyclic complex from the published facet formula, checks the face and edge counts, confirms degree six, exhausts every graph triangle and simple four-cycle, and verifies
\[
\{\text{four-cycles}\}=U\sqcup V\sqcup W\sqcup R\sqcup S.
\]
It verifies that \(U,V,W\) are boundaries of explicit pairs of adjacent triangles and that the integral cocycle \(\alpha\) and mod-two cocycle \(\beta\) vanish on every face boundary. It then checks
\[
\alpha(R)=\alpha(S)=0,
\qquad
\beta(R)=\beta(S)=1,
\]
and confirms the translation orbit sizes \(4m+2\) and \(2m+1\).

The finite sweep is not used as a proof of the infinite parameter range; it is a replayable check of the formulas and case classification supporting the written all-parameter argument.

Exact successful output:

`VERIFY_OK theorem_family=Q_{2m+1,2} parameter_range=m>=4
proof_identities=A_faces+B_faces alpha_cocycle beta_cocycle R/S_detection
finite_exhaustive_sanity=m=4..20 triangles=faces quads=U|V|W|R|S
systole_length=4 minimizers=6m+3 all_unique_order2_class=yes
translation_orbits=4m+2,2m+1`
