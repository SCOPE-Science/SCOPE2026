# Review of the joint rank–hafnian Jordan spectrum

## Correctness

**PASS.** The algebra has the sixteen squarefree-monomial basis elements. The multiplication map by a homogeneous quadric shifts degree by two, so its rank is exactly \(2+\operatorname{rank}B(Q)\) for nonzero \(Q\), and the second-power rank is exactly \(\mathbf1_{H(Q)\ne0}\) in odd characteristic. The rank-two hollow symmetric matrices are classified by split hyperbolic factorization; the determinant and hafnian joint counts are obtained from a weighted ternary quadratic cone and its plane section. All seven multiplicities are disjoint, integral, positive, and sum to \(q^6\). The standalone code agrees over prime fields \(\mathbb F_3,\mathbb F_5,\mathbb F_7\), samples over \(\mathbb F_9\), and directly checks multiplication ranks.

## Originality

**PASS, subject to residual priority risk.** Lewis et al., *Matrices with restricted entries and \(q\)-analogues of permutations* (arXiv:1011.4539, Sections 3–4) counts symmetric zero-diagonal matrices by ordinary rank, a strictly coarser marginal than the simultaneous rank/hafnian stratification needed for the six nonzero Jordan types. Cook, *The Lefschetz properties of monomial complete intersections in positive characteristic* (arXiv:1111.4979, Sections 1–2) addresses linear Lefschetz multipliers, not this quadratic finite-field spectrum. Relevant Artinian Jordan-type research on other Hilbert functions and generators was also compared. No inspected source states these seven exact frequency formulas or their mod-three trichotomy, but an equivalent obscure prior treatment remains possible. These comparisons do not certify global novelty.

## Value

**PASS.** The result completely determines a natural invariant of homogeneous quadratic multiplication on the sixteen-dimensional cohomological squarefree algebra, instead of only the maximal-rank case. The arithmetic trichotomy is structural: it comes from the one-/two-/zero-line behavior of the binary cubic-root conic section and affects exact Jordan block frequencies. The claimed contribution is the motivated joint rank–hafnian distribution, not the previously known ordinary hollow-symmetric rank counts.

## Limits

The proof requires odd characteristic and a fixed four-variable square-zero monomial complete intersection. Arithmetic experiments in finitely many fields are independent consistency checks, not infinite proof. Literary priority is not exhaustively settled, and independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
