# Independent audit — 2026-09-30 UTC

Record: `2026/09/20/single-commutators-cstar-quotients-finite-von-neumann--0347171537ea`  
Assigned and audited source tree: `735dbcf37795103544e4e5b358ea1d173572f9f3`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `f43878bf0203edde5ca0650213c50ffad924c072`  
Disposition: **passed**

## Correctness

**independently_supported**. The quotient theorem is correct. Generalized Dixmier averaging sends every closed ideal J of a finite von Neumann algebra into itself, so the center-valued trace descends. If q(x) is central, every unitary conjugate differs from x by J, hence the norm-Dixmier limit T_M(x) does too; thus Z(M/J)=q(Z(M)). For a zero descended central component, x-T_M(x) is a lift with zero center-valued trace and Wang’s uniform theorem makes it one commutator before passing to the quotient. This identifies the single-commutator set with ker Tbar, giving closed linearity and the exact distance formula. The 2K general quotient estimate and K reduced-product estimate follow from lift minimization and coordinatewise rescaling as stated.

## Originality

**qualified_supported_recent_quotient_consequence**. Wang’s September 2026 preprint proves the uniform one-commutator theorem inside finite von Neumann algebras; Takesaki and the broader Dixmier/center-quotient literature provide classical quotient structure. Current searches did not locate the exact arbitrary norm-closed-ideal consequence that every zero descended central-trace class is itself a single commutator, nor the reduced-product/matrix-corona metric package. Novelty is therefore restricted to this quotient-level consequence and quantitative packaging, not to center lifting itself.

## Scientific value

**meaningful_operator_algebra_extension**. The result transports a new finite-von-Neumann commutator theorem through arbitrary C*-quotients and yields exact metric and corona statements, including positive nonzero commutator projections in the matrix corona.

## Independent checks

- Reconstructed ideal invariance and center lifting from norm Dixmier averaging.
- Checked the lift x-T_M(x) and distance identity.
- Checked the reduced-product quotient norm and coordinate rescaling argument.

## Literature and evidence checked

- https://arxiv.org/abs/2609.16932
- https://doi.org/10.2140/pjm.1971.36.827
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/single-commutators-cstar-quotients-finite-von-neumann--0347171537ea

## Limitations

- Finite von Neumann algebras only.
- The factor 2 in the general quotient commutator-cost bound is not shown optimal.
- Some nonquantitative quotient formulation could exist in older Dixmier-property literature.
