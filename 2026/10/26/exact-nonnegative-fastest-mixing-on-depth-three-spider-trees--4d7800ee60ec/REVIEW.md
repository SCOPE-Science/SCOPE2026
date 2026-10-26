# Scientific review: nonnegative fastest mixing on depth-three spiders

## Correctness — PASS

The domain is every integer \(k\geq3\), over every symmetric nonnegative stochastic transition matrix on the indicated tree. Automorphism averaging applies because the SLEM is an operator norm of an affine matrix map. The invariant Laplacian decomposes into a radial \(4\times4\) block and \(k-1\) copies of a \(3\times3\) arm-contrast block. Interlacing gives a global lower bound through the least contrast eigenvalue. The exact positive vector \((a,a+1,a+2)\) produces the Rayleigh certificate \(xa^2+y+z\leq a^2/k+1\); equality and the eigenvector equation give the unique invariant optimal edge probabilities. A fully factored radial characteristic polynomial puts the entire nontrivial spectrum within \([\gamma_k,2-\gamma_k]\), with \(\gamma_k\) attained. These algebraic steps establish the infinite-family optimum and invariant uniqueness. Symbolic identities, reduced-spectrum checks, and independently assembled Laplacians reproduced from the package pass, but finite checks are not the universal proof.

## Originality — PASS with residual risk

The graph family itself is strongly represented in prior literature, making statement-level comparisons essential. Boyd–Diaconis–Parrilo–Xiao (arXiv:0709.0955) supply the general FMMC symmetry and SDP machinery, but not the stated radical optimum for this family. Jafarizadeh–Jamalipour (arXiv:1001.4278) prove an unconstrained consensus optimum on the *same* symmetric-star topology. Their center transition weight \(2/(k+2)\) would yield central holding probability \((2-k)/(k+2)<0\) for every \(k\geq3\), and hence their optimum is infeasible for the entrywise nonnegative Markov problem addressed here. Jafarizadeh (DOI:10.1109/TSIPN.2020.2964211; arXiv:2501.02421) discusses Markov-feasible symmetric stars: the explicit arbitrary-depth formula in sections 6.6 and 7.3 requires \(k\pi_1\leq2\pi_0\), which fails under uniform stationary weights for \(k\geq3\). The all-parameter result in section 7.2.1 is for depth two, while the depth-three special case in 7.2.2 retains assumptions not satisfied by this family. The closest accessible published mathematical record on lazy random walks on spiders concerns mixing bounds for fixed weights, not fastest-mixing design. Thus the present conclusion is not established as a corollary of the closest inspected specific theorems. Residual risk: another branch of the 2020 framework or specialized literature could contain an equivalent boundary-case derivation; absence of a search hit does not prove absolute novelty.

## Value — PASS

The Markov positivity constraint is substantive: on exactly the same tree, an unconstrained fast consensus solution assigns a negative holding probability at the hub. The exact constrained solution exhibits an active hub constraint, distinct interior edge probabilities, a closed-form spectral-gap law for every number of arms, and a proof identifying which spectral mode limits mixing. This is a natural, infinite-family network-design problem; it is not a renamed known optimum. The edge weights and sharp rate supply benchmark instances for constrained consensus/Markov design. The finding is self-contained even without a broader theory of arbitrary arm lengths.

## Scope and outstanding validation

No assertion is made about uniqueness of general nonsymmetric minimizers, variation in stationary measure, or total-variation mixing-time minimization. The closest relevant literature and residual overlap risks remain recorded in `AUDIT.json` and `RESULT.md`. Independent reproduction of the mathematical argument and the originality comparison remains outstanding.

Self-review: passed. Independent audit: not yet performed.
