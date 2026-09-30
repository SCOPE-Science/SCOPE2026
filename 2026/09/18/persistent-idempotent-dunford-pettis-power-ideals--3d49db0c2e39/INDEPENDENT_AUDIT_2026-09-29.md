# Independent audit — 2026-09-29

Record: `2026/09/18/persistent-idempotent-dunford-pettis-power-ideals--3d49db0c2e39`  
Assigned and audited source tree: `ce20ac0632ea44802011bafa7bee30789075b94d`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**independently_supported**. The synthesis is correct. Acuaviva supplies a Dunford–Pettis projection P on L^1[0,1] whose range Y has the Schur property but fails the Radon–Nikodým property. If P factored through ℓ^1, then the factor map restricted to Y would be bounded below because BA|_Y=I_Y, embedding Y isomorphically as a closed subspace of ℓ^1; this contradicts inheritance of the RNP. Hence P is Dunford–Pettis but nonrepresentable. Idempotence gives P=P^n in every closed n-fold Dunford–Pettis power. The standard complemented copy of ℓ^1 in L^1 gives the displayed n-factor representation of every representable operator, so G⊂I_n; ideality gives I_n⊂I_2, and Nasseri’s theorem gives I_2⊊D. Since P is identity on its infinite-dimensional range it is not strictly singular. The APB factorization through repeated P puts the entire generated ideal J_P in every power, and the quotient class P+G is a nonzero idempotent in every quotient power.

## Originality

**supported_synthesis**. Acuaviva’s and Nasseri’s September 2026 preprints provide the two independent ingredients: the non-RNP Schur projection and the Dunford–Pettis power-ideal framework. Nasseri’s public abstract proves the square ideal lies strictly between representable and Dunford–Pettis operators; the record’s common-idempotent conclusion is a synthesis of the two new inputs. Searches did not locate the persistent common-core statement. Classical representability/RNP facts are not claimed as new, and older Saab/Lewis–Stegall material is treated only as background.

## Scientific value

**meaningful_power_ideal_structure**. A single nonzero idempotent surviving every power is qualitatively stronger than separate nonvanishing of the powers: it supplies a common proper large ideal and shows the quotient is nonradical. This materially sharpens the structural picture while not resolving whether the power chain is strictly decreasing.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/persistent-idempotent-dunford-pettis-power-ideals--3d49db0c2e39
- https://arxiv.org/abs/2609.17283
- https://arxiv.org/abs/2609.18348
- https://doi.org/10.1016/0022-1236(73)90022-0
- https://doi.org/10.4153/CMB-1982-028-8

## Limitations

- The result does not prove that the closed power ideals are pairwise distinct.
- Its novelty is the 2026 synthesis; the representability/RNP and complemented-ℓ^1 ingredients are classical.
- The full text of Saab (1982) was not needed for the synthesis and was not claimed as independently inspected.
