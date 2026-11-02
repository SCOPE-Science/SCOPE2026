# Scientific review of the multisink block-design capture law

## Correctness

**PASS.** The design identity \(BB^{\mathsf T}=(\rho-\lambda)I+\lambda\mathbf1\mathbf1^{\mathsf T}\) proves full row rank and establishes the exact bright space \(W\oplus B^{\mathsf T}W\) with dimension \(2(t+1)\). Strictly positive losses make every mode in that bright space decay; modes orthogonal to it have zero loss. Point probabilities follow from averaging the unmarked coordinates, while the block formula follows from the constant row-space leverage \(v/b\) minus the exact incidence variance \(u(s-u)/(s(\rho-\lambda))\). The proof includes the full nonsymmetric case. The attached checker has passed 244 marked-subset comparisons, 6,936 local values, 150 exact projector cases and 20 dissipative survival checks, with worst numerical projector error \(1.110\times10^{-15}\). Finite tests are corroboration, not a substitute for the analytical proof.

## Originality

**PASS, subject to historical-priority uncertainty.** The invariant-subspace transport method belongs to Novo et al. (arXiv:1412.7209), and spectral decomposition of symmetric incidence designs, including multiple marked sites in Hermitian search, belongs to Lugão and Portugal (arXiv:2310.14141). The latter full text was compared at its spectral theorem, multiple-marked derivations and conclusion: it studies finite-time coherent search, not absorptive dynamics, and it does not cover nonsymmetric designs or the blockwise capture formula. Razzoli et al. (arXiv:2011.13794) treat the single-trap efficiency framework. Previously calculated two-trap affine-plane cases do not imply the claimed general multisink, all-\(2\)-design theorem. Semantic comparisons with published mathematical results identified related design spectra and unrelated quantum transport, not a statement implying this formula. Search absence does not establish unique historical priority.

## Mathematical value

**PASS.** Exact sitewise absorption is physically meaningful: identical average efficiencies hide a geometric distinction between collinear and noncollinear triple absorbers in the Fano plane. The sharp upper bound \(v/b\) is an exact obstruction to full capture from block sites in every nonsymmetric design, even when the marked set nearly covers the point part. The formula is parameter-uniform over infinitely many balanced designs, and quantitatively separates sink-placement geometry from the universal bright-space dimension.

## Limitations and closest literature

The claim is restricted to uniform coherent hopping, at least three and fewer than all point absorbers, strictly positive absorption strengths and infinite-time single-excitation dynamics. It makes no statement about traps on block vertices, noisy evolution or time-to-capture. The multiple-marked Hermitian design-search result is a significant antecedent with a different observable and different generator; more specialized absorption literature could affect priority.

Self-review: passed. Independent audit: not yet performed.
