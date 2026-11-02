# Self-review

## Correctness — PASS
The proof starts from the exact omitted-neighbor count inside a clique fiber, which restricts every column to 0, 1, or \(m\) omissions. Domination and capacity exclude full triples, full–non-full–full, and singleton columns within cyclic distance two of full columns. The resulting run-gap inequality \(|S|\le mf+(n-f-2b-2)_+\) is optimized over all feasible numbers of full blocks and full columns. All equality cases are tracked; a separate no-full-column analysis identifies the only exceptions at \((3,3)\) and \((3,6)\). A constructive cyclic word gives equality, and a cyclic compositions count enumerates every optimum. Direct exhaustive graph checks and a separate column-state dynamic program independently match the claimed minima/counts in the stated finite ranges. Finite checks are not an unrestricted proof.

## Originality — PASS, qualified
The original definition, the cycle value, and the general Cartesian upper bound belong to Božović et al. (arXiv:2606.22422) and Tepeh (arXiv:2606.22428), respectively. The scalar equality is already implied by earlier general bounds for some special parameters and that part is not asserted as wholly novel. The inspected Cartesian-product paper's Section 4 treats rook, rectangular-grid, selected prism and hypercube situations, but does not establish the present complete \(K_m\square C_n\) family or count its optimizers. Neither the related more recent general-bounds abstract nor the searched mathematical record supplied an equivalent classification. The closest available historical result on 1-limited domination of \(C_n\square K_2\) concerns the excluded \(m=2\) factor and is not used to infer novelty. Residual risk remains from inaccessible or unindexed prior work, and from partial access to earlier historical ledgers.

## Value — PASS
The invariant is a capacity-constrained domination parameter whose Cartesian products are a focus of current research. This gives a sharp infinite two-parameter family beyond the cases explicitly solved in the originating product paper, with a rigid classification of *all* extremizers and a nonconstant four-periodic multiplicity \(4,n,n^2/4,n\). The exceptional whole-cycle-fiber minimizers have a precise structural boundary. These are natural exact invariants and equality structures, not arbitrary finite slices, renamings, or computation-only certificates.

## Limitations and risk
The scope is exactly ordinary \(K_m\square C_n\) for \(m,n\ge3\) and capacity one. General \(k\), arbitrary factors, nonminimum counts, and historical priority beyond inspected sources are not determined. No independent mathematical review or certification is claimed.

Self-review: passed. Independent audit: not yet performed.
