# Independent Audit — Sharp certified-domination gap for connected graphs

**Audit date:** 2026-09-30 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `5022039798b1d7e29d46e971d8d0335a51d8a183`  
**Audited current source tree:** `5022039798b1d7e29d46e971d8d0335a51d8a183`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record path has no changes from the assignment snapshot, so the audited tree equals the assigned source tree. GitHub was used read-only. The UTC-dated independent-audit files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. The factor-two equality argument is sound. Starting from the standard bound γ_cer≤γ+|S1|≤2γ, equality forces a minimum leaf-free dominating set D to consist entirely of half-shadowed weak supports. Each such support then has exactly one outside neighbor, its private leaf, and domination forces all outside vertices to be exactly these leaves; hence the graph is a corona. The converse is immediate. The fixed-order gap follows from γ≤floor(n/2), γ_cer≤2γ, and the impossibility γ_cer=n-1. For odd extremality, γ=m-1 would force the impossible odd-order corona, so γ=m and γ_cer=n-2, where the known connected characterization yields a diadem. Independent exhaustive Graph Atlas checks through order seven reproduced every stated maximum and found no mismatch with the corona/diadem equality families.

## Originality — PASS

PASS, narrowly scoped. Dettlaff et al. introduced certified domination, proved γ_cer≤2γ, and characterized connected graphs with very large certified domination numbers including the corona/diadem structures. The 2019 equality paper concerns γ_cer=γ and related parameters. Targeted searches did not locate the converse factor-two equality theorem γ_cer=2γ iff corona or the exact fixed-order maximum of γ_cer-γ with its parity-dependent extremal classification. All underlying certified-domination bounds and known n/n-2 characterizations receive no novelty credit.

## Scientific value — PASS

PASS. The theorem closes a natural extremal question for the gap between two established domination parameters and identifies exactly when the standard factor-two estimate is tight. The parity split and corona/diadem classifications make the result structural rather than merely numerical.

## Independent checks

- Reproved the equality case in the standard γ_cer≤γ+|S1|≤2γ argument.
- Checked that equality forces exactly one private leaf per minimum-dominating-set vertex, hence a corona.
- Re-derived the odd-order obstruction from γ_cer≠n-1 and the factor-two equality theorem.
- Exhaustively computed γ and γ_cer for every connected Graph Atlas graph through order seven; maxima were n/2 for even n and (n-3)/2 for odd n.
- Checked all small equality graphs against generated corona and diadem families; no mismatch was found.
- Compared with the original certified-domination paper and the 2019 equal-domination paper; no factor-two converse or fixed-order gap theorem was located.
- GitHub comparison found no changes under the assigned record path; both dated audit files are absent and VERIFICATION.md retains the verified blob SHA.

## Limitations

- The theorem is for finite simple connected graphs.
- The 2025 tree-equality paper is related but addresses γ_cer=γ rather than the factor-two equality; no broader claim is made about every later certified-domination variant.
- Originality is restricted to the exact factor-two converse and fixed-order gap classification, not the prior corona/diadem large-γ_cer characterizations.

## Evidence and references

- https://arxiv.org/abs/1606.03257
- https://doi.org/10.1016/j.akcej.2018.09.004
- https://doi.org/10.7494/OpMath.2019.39.6.815
- https://doi.org/10.1007/s13226-025-00907-1
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/20/sharp-certified-domination-gap-connected-graphs--83a8e57e9984

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
