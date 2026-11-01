# Scientific review

## Correctness — PASS

The statement specifies the finite-dimensional field, dimensions, norm-one hypothesis, normalized relative seminorm, and real-part pairing constraint. Compactness identifies the top singular subspace \(E=\ker(I-G^*G)\) and yields the exact formulas \(p_G(T)=\|T|_E\|\) and \(\nu_G(T)=w(U^*P_FT|_E)\). Every step in the proof has an explicit witness or inequality: the proper-range case uses a rank-one operator into \(F^\perp\), the full-range case is equivalent to coisometry and reduces to the classical sharp real/complex Hilbert numerical-index constants. Perturbations preserving another singular value one establish the discontinuity. Supplementary checks in `relative_index_check.py` pass 6,720 finite assertions; they are not a substitute for proof.

## Originality — PASS, best-knowledge

The source by Dey and Pal establishes finite-dimensional localization and a *necessary* partial-isometry condition for relative spear operators but neither the complete exact \(n_G^{(2)}\) values nor the dimension- and field-dependent coisometric classification and discontinuity. Kadets et al.'s classical \(n_G\) uses \(\|T\|\) instead of \(p_G(T)\), so its rectangular vanishing cannot imply this relative index. Their generating-operator work characterizes equality of relative and full norms, not a numerical-radius quotient. The closest published relative-seminorm result is about infinite-dimensional essential norms, with different domain and conclusion. The inspected full texts and mathematical-record searches returned no dominating claim. Possible older equivalent compression/relative-radius formulas remain a publication-priority risk; the top-singular localization itself is not claimed novel.

## Mathematical value — PASS

The original relative numerical index gives a natural quantitative refinement of the relative spear property. This theorem completely resolves it for the basic finite-dimensional real and complex Hilbert class, making the entire dependence on output dimension and coisometry explicit. In particular, it separates the old full-norm index from the relative seminorm index for rectangular coisometries and identifies a sharp discontinuity locus. It is a structural classification with a natural motivating gap, not a numerical coincidence or arbitrary slice. No general-Banach or infinite-dimensional conclusion follows.

## Limitations and closest sources

The classification is restricted to nonzero finite-dimensional Hilbert spaces. Its normalized seminorm is not assumed faithful. Most directly related are Dey–Pal (arXiv:2603.20796v1, Proposition 2.4 and Theorems 3.12–3.13), Kadets et al. (arXiv:1905.12257, classical full-norm index) and Kadets et al. (arXiv:2306.02645v1, generating operators). Historical mathematical-record comparisons cannot eliminate the possibility of earlier unindexed formulations. No independent validation or publication-priority certification has occurred.

Self-review: passed. Independent audit: not yet performed.
