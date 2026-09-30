# Independent Audit — 2026/09/17/crossing-only-dengue-switching--e6abca835bbf

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `d29a622a2bb5cb93f16bd0b33ae0801f6733528a`
- Disposition: **PASSED**

## Correctness

**PASS** — The switch geometry follows directly from the published model equations. At I=kC with k<1, changing fogging adds only (0,0,0,-eta U,-eta V), whose I-normal component is zero, so both one-sided normal velocities are identical and ordinary attracting/escaping Filippov sliding is impossible. At I=C the recovery and mosquito-infection pieces match in value, so for k<1 the vector field is continuous; for k=1 the remaining fogging jump is again tangent. For a transversal event with identity reset, the standard saltation formula gives S=I+DeltaF n^T/phi. Because n^T DeltaF=0, the rank-one update squares to zero and has determinant one, so all event eigenvalues are one. The Floquet determinant conclusion follows from piecewise Liouville plus determinant-one saltations, and the equal relative U,V update makes the first-order infection fraction q=V/(U+V) continuous through the event. The record correctly excludes grazing/common-tangency points from the saltation claim.

## Originality

**PASS** — The Aldila et al. source explicitly lists a Filippov-based sliding-mode analysis of I=kC and I=C as future work. The submitted calculation resolves that model-specific question by showing that the sought ordinary sliding regions are structurally empty, and it adds the exact unipotent saltation/Floquet consequences. Standard Filippov and saltation theory provide the formulas, but the tangent-jump geometry and its consequences are specific to this threshold model and were not stated in the source or the located dengue-switching literature.

## Scientific value

**PASS** — The result closes an explicit analytical gap in the motivating model and prevents a misleading search for an ordinary sliding regime that cannot occur under its equations. The determinant-one shear and preserved mosquito infection-fraction perturbation also simplify variational/Floquet calculations for the periodic outbreaks already reported by the source paper. These are concrete reusable consequences despite the elementary algebra.

## Sources

- A Mathematical Model of Dengue Transmission Incorporating Hospital Capacity and Threshold-Based Fogging Interventions (Dipo Aldila; Joseph Páez Chávez; Aytül Gökçe; Thomas Götz; Burcu Gürbüz): https://arxiv.org/abs/2607.18140 — Primary model source; its conclusion explicitly names Filippov sliding analysis of I=kC and I=C as future work.
- Saltation Matrices: The Essential Tool for Linearizing Hybrid Dynamical Systems (Nathan J. Kong; J. J. Payne; Jiayi Zhu; Aaron M. Johnson): https://doi.org/10.1109/JPROC.2024.3440211 — Standard saltation-matrix framework used for transversal identity-reset events.

## Limitations

- The result excludes ordinary codimension-one Filippov sliding/escaping, not higher-order grazing or degenerate common tangencies.
- Saltation statements require nonzero crossing speed.
- No periodic-orbit existence, stability classification, or Hopf criticality is proved.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence. Open-access/preprint sources were checked first. Oxford Download was used only where version-specific or full-text source verification remained unavailable through the open-access retrieval path.
