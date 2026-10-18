---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For Z_G=Σ_{uv edge}[e_u,e_v], the unique central symmetry center has coordinate deg(v)/2=(N−n_i)/2. Every vertex corresponds to an acyclic orientation with coordinates indeg(v); its squared centered norm equals Σdeg(v)^2/4−Σ indeg(v)outdeg(v). A topological word counts the latter as one for every triple of distinct multipartite classes plus nonnegative interleaving triples (two vertices from one class straddling another class). Equality occurs exactly for contiguous class-block orders: k! distinct acyclic orientations. Symmetric polynomial simplification gives R²=(N³−Σn_i³)/12; central symmetry gives diameter 2R and uniqueness of the enclosing-ball center. Independent exhaustive all-acyclic-orientation enumeration (not reused topological-word code) checked seven small part profiles, exact R² and k! contacts. The symbolic interleaving argument, not finite sampling, proves every k and n_i.

## originality

PASS

Primary Padrol–Pilaud–Poullot establishes the standard graphical zonotope and acyclic orientation model but focuses deformation-cone geometry; Chapoton–Pilaud establishes graph joins/shuffles, not Euclidean circumspheres. A highly relevant separate published Resultary result on UNIVERSAL CONING gives D2(K1∨H)^2=D2(H)^2+m(m+1) and farthest-point cuts; that is a stronger statement for adjoining a single singleton part, but repeated coning cannot construct arbitrary multipartite blocks with n_i>1. It even explicitly cites complete multipartite cases as known. Therefore the complete arbitrary-part cubic-moment and k! contact theorem is not implied by that coning formula alone. Best-of-knowledge PASS with significant folklore/equivalent inequality risk.

## value

PASS

Complete multipartite graphs form a natural infinite iterated-graph-join/shuffle family. A closed Euclidean circumradius expressed by the third power sums of part sizes, plus an exact k! classification of extremal orientations, is a structural geometry theorem not merely a known vertex count; it specializes to both permutahedra and complete bipartite zonotopes and is useful in future optimization of graphical zonotopes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
