# Independent audit — 2026-09-30

Record: `2026/09/19/nonpairwise-synchrony-interference-stuart-landau--c23725ab572f`  
Assigned and audited source tree: `a7407221d78bfcd4f979d96f7db606e0f268377d`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `2294c7f8abbbee7d129d727da25d754dd73a139b`  
Disposition: **passed**

## Correctness

**independently_supported**. The synchrony Jacobian formulas check directly from the displayed mixed phase reduction. Differentiating the unit-weight pairwise first-order term, the source second-order term, and the asymmetric physical nonpairwise term at full synchrony gives zero row sum and the double transverse eigenvalue -3ε cosρ-(9ε²/(2a))sin²ρ-3η cosξ. Solving its zero condition gives the stated boundary branch, and with η=qε² the expansion around ρ=π/2 has coefficient 3/(2a)+q cosξ and no ε² term. For the engineered coupling, direct differentiation gives the additional +6η sin²ρ transverse contribution. Substitution of the source harmonic-matching choice η=ε²/(4a) leaves -3ε cosρ-3ε² sin²ρ/a, while η=3ε²/(4a) cancels the entire second-order synchrony correction and leaves exactly -3ε cosρ in the truncated phase model.

## Originality

**qualified_source_specific_refinement**. Higher-order phase reduction and the second-order pairwise synchrony correction are prior work, and the Muolo–Nakao–Bick preprint already develops physical versus emergent nonpairwise interactions and coupling design. Its public statement does not give the closed PN–EN transverse interference law or distinguish the source's harmonic-cancellation strength from the three-times-larger strength that exactly neutralizes the second-order synchrony boundary. Current targeted searches did not locate those source-specific formulas. The contribution is therefore a local-stability calculation and design refinement, not a new general theory of higher-order synchronization.

## Scientific value

**useful_exact_design_diagnostic**. The result makes the interference of physical and emergent nonpairwise terms transparent at the most important coherent state and shows that cancelling selected harmonics is not the same objective as cancelling their net transverse Jacobian. The exact neutralizing strength is practically interpretable within the source's second-order model, while the record correctly avoids extrapolating it to the full finite-coupling system.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/nonpairwise-synchrony-interference-stuart-landau--c23725ab572f
- https://arxiv.org/abs/2609.20632
- https://doi.org/10.1007/s00332-024-10053-3
- https://arxiv.org/abs/2606.04904
## Limitations

- The exact cancellation holds only in the displayed mixed-order phase reduction and omits O(ε³), O(εη), and O(η²) terms.
- Only local transverse stability of full synchrony is addressed, not basin geometry or other attractors.
- The pairwise second-order correction and general higher-order reduction machinery are prior work.
- The motivating preprint is extremely recent, so parallel source-specific calculations may not yet be indexed.
