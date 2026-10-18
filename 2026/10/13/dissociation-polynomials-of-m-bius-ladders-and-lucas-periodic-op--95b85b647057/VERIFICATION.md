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

The 16 ordered rung-mask-pair states enforce for every occupied row-j vertex the exact neighbor-count inequality a_j+b_(1-j)+c_j<=1, including the row-flipped Möbius seam. The 41-transition matrix commutes with the row flip; its + and - eigenspaces have dimensions 10 and 6, so tr(F T^n)=tr(T_+^n)-tr(T_-^n). Independent exact symbolic determinants equal Q_+=1-(1+z)t-(z+2z^2)t^2+(z^3-z^2)t^3+z^4t^4 and Q_-=1+zt+z^2t^2. The formal log-determinant identity proves every n>=3 coefficient. Under t=u/z the top z^n term factors into (1-u^2)(1-u-u^2)(1-u)/(1-u^3) and gives Lucas_n+1+2[2|n]-3[3|n]; all coefficients of larger z-degree vanish by filtration. Independent separate graph adjacency enumeration for n=3..7 found all polynomial coefficients and matched transfer traces. Simple-graph domain excludes n<3. The complement equivalence to 3-path vertex covers follows from degree <=1.

## originality

PASS

No found prior exact all-order dissociation polynomial with Möbius flip and Lucas-periodic maximum-cover census. Grid enumerators use ordinary open boundaries; universal cubic bounds and maximal-set results are different statements. Best-of-knowledge novelty with explicit terminology risk.

## value

PASS

An entire natural nonorientable cubic graph family receives a closed dissociation polynomial rather than a scalar parameter; the twist is not covered by ordinary rectangular grid results. The Lucas-periodic top coefficient and bijection to minimum 3-path vertex covers are natural, exact structural data useful for subsequent extremal comparisons; no claim about arbitrary cubic graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
