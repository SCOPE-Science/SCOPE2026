# Independent audit — 2026-09-29

Record: `2026/09/19/forced-colouring-polynomials-maximum-degree-two--889f7740a349`  
Assigned and audited source tree: `7495c9b4837d0eaea2369ed66961167ad2198c39`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **repaired**

## Correctness

**independently_supported**. The path and cycle formulas are correct. A definition-level independent enumeration through n=7 reproduces the path coefficient formula and the cycle coefficient formula of the earlier SCOPE theorem exactly. The two-recurrence cycle representation is algebraically equivalent to the closed coefficient count. The lambda=1, lambda=2 (including isolated components), and lambda>=4 branches follow from the forcing rule and multiplicativity, and independent enumeration confirms the stated minimum-domain values on small paths and cycles.

## Originality

**requires_provenance_repair**. The central novelty claim is contradicted by repository chronology. SCOPE record `2026/09/17/forced-three-colouring-max-degree-two--2226d8f07ffd` was committed at 2026-09-17 23:56:20 UTC and already states the exact path and cycle coefficient formulas and the maximum-degree-two lambda=3 classification. This assigned record was committed later, on 2026-09-19. Its genuinely additional value is narrower: an alternate root-of-unity/transfer-matrix derivation, the all-lambda packaging, the isolated-vertex lambda=2 consistency correction, and minimum-domain corollaries. The repair removes any separate first-discovery framing for the core formulas.

## Scientific value

**useful_refinement_after_provenance_repair**. After repair, the record remains useful as an alternate derivation and as a compact all-lambda treatment with exact forcing-domain consequences, but it is not a separate discovery of the core path/cycle formulas.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/commit/2bc43a7d60092cce0c0f86cebf225b20f6b40982
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/forced-colouring-polynomials-maximum-degree-two--889f7740a349
- https://arxiv.org/abs/2609.17108
- https://arxiv.org/abs/2406.15746

## Limitations

- The core lambda=3 path/cycle formulas were already present in an earlier SCOPE record.
- The theorem remains restricted to maximum degree two.
- The 2025 Springer chapter was not needed to resolve provenance because the earlier repository record is decisive.
