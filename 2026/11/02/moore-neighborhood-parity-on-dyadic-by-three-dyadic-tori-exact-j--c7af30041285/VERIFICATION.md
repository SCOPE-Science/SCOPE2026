---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Over characteristic two the eight-neighbor rule is multiplication by F=(1+x+x^−1)(1+y+y^−1)+1, with its central term cancelled, on K[x±,y±]/(x^M−1,y^(3d)−1). The y-polynomial factors as (y+1)^d(y²+y+1)^d with coprime components. On the y=1 primary component, writing s=x+x^−1=u²/(1+u) and t=y+y^−1=v²/(1+v) gives a rank-four free truncated-polynomial module, while the invertible triangular substitution z=s+(1+s)t yields c=2 min(M,d) nilpotent blocks of size L=max(M,d)/2; d=1 separately yields two J_(M/2)(0). On the cyclotomic component, w=1+y+y^−1 is nilpotent with B free rank two over K[w]/w^d, and the unit 1+s rescales it to give exactly 2M unipotent J_d(1) blocks. Block nullities give exact first entry times and fixed point differences give all power-of-two primitive periods and their joint product populations. Independently assembled binary adjacency matrices for 4×3 and 4×6 and reproduced the nilpotent kernel dimensions [0,2,4] and [0,4,8] respectively. This cannot replace the CRT and module proof for all M,d and q.

## originality

PASS

Zaidenberg 2006 develops broad prime-characteristic lattice-convolution and semisimple primary methods, and Martin–Odlyzko–Wolfram 1984 is broad cellular-automaton algebra; neither inspected material supplies the exact eight-neighbor double-cyclotomic Jordan form. Omirov–Redjepov–Usmonov 2024 treats Moore CA with different boundary conditions. The specific two-sector ground-field Jordan and joint orbit census were not identified as previously published; incomplete historical full-text access remains risk.

## value

PASS

The eight-neighbor Moore parity rule is a canonical local cellular automaton. The theorem describes its entire finite dynamic—not merely its characteristic polynomial—over all dyadic-by-three-dyadic periodic tori, including exact transient length, order of periodic subsystem and number of states/orbits in each (entry time, primitive period) class. Primary-factor resonance yields a surprising coexistence of large nilpotent and unipotent sectors and is structurally motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
