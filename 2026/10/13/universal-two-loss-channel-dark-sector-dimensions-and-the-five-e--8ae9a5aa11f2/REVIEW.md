# Independent mathematical audit

## correctness

PASS

Set y_ij=c_i c_j x_ij and r_i=d_i/c_i. Both lower-jump kernels become the two vertex-indexed edge-sum constraints Σ_{j≠i} y_ij=Σ_{j≠i} r_j y_ij=0. Annihilator vectors (α_i,β_i) obey α_i+α_j+β_i r_j+β_j r_i=0; using two distinct anchor ratios gives rank(B)=2n−4+rank(T), where each pair of ratios s,t contributes (1,s+t,st). At n≥5 the rank(T) dichotomy 2 (ratio multiplicity at least n−2) or 3 otherwise follows by choosing anchors and the Vandermonde determinant. For n=4 special equal-pair case rank(T)=1, otherwise 2. For h=1 the signless complete-graph incidence rank is n≥3. A separate rational Gaussian-elimination checker tested 510 integer-partition ratio patterns for n=2..9 and the explicit 5-emitter kernel vector; all matched. The stationary-state corollary requires only the stated scalar number Hamiltonian, no extra Lindblad terms.

## originality

PASS

Best-of-knowledge PASS for two-excitation simultaneous common kernel classification under two arbitrary nonzero weighted lowering profiles; previous papers on collective singlets and multilevel decay channels do not directly imply the full ratio-multiplicity formula. Plausible recent papers not fully read remain an explicit originality risk.

## value

PASS

Exactly classifies the protected two-excitation common dark space across the natural emitter number and spatial coupling multiplicity parameters, locating the generic five-emitter onset and exceptional four-emitter symmetry. Physically and algebraically motivated structural kernel theorem, not merely a sampled dimension table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
