# Same-model review

## Correctness
**PASS.** The proof checks the precise Hu--Ivaki definitions, quantifiers, normalization, and boundary case \(n=2\). Under \(A\in GL(n,\mathbb R)\), the codimension-one and codimension-two Jacobian formulas scale every facet mass and ridge conductance by \(|\det A|\), so the generalized Rayleigh form is affine invariant. On a box, all facet masses equal \(2^{n-1}\prod_k a_k\), all ridges between distinct coordinate directions have conductance \(2^{n-2}\prod_k a_k\), and the complete-graph variance identity yields the factor \(n\) exactly. The finite exact-rational checker is consistent with the algebra but is not used to promote a finite experiment into an all-dimensional proof.

## Originality
**PASS.** The closest primary source is Hu--Ivaki, arXiv:2609.21670v1. It defines the facet-network spectrum and, in Remark 1.2, says that a global minimizer with even multiplicity \(n-1\) is a parallelotope. That is a one-way shape consequence under additional minimizing assumptions; it neither gives \(\lambda_{1,e}=n\) for every parallelotope nor the stronger identity for every even facet function. Targeted searches for the parallelotope/cube/box aliases, the exact value, multiplicity, affine invariance, and full even spectrum found no covering public statement. Smooth unconditional-body and zonoid lower bounds do not imply the discrete equality. Residual risk remains because the source notes that further details may appear elsewhere.

## Value
**PASS.** Parallelotopes are the canonical family singled out by the source's extremal multiplicity discussion. Determining the entire even spectrum is a structural calibration of the newly introduced discrete operator, not a routine arbitrary parameter slice. It gives an exact equality benchmark and multiplicity for future extremal or stability work while making no unsupported characterization or minimization claim.

## Closest literature and limitations
The closest source is Y. Hu and M. N. Ivaki, *Centro-affine spectral geometry of polytopes*, arXiv:2609.21670v1. Broader smooth comparisons include their arXiv:2607.20223 and van Handel's smooth zonoid inequality. The present statement is limited to full-dimensional origin-symmetric parallelotopes with the published facet-network normalization and does not prove local/global minimality or a converse characterization.

Same-model review: passed. Independent audit: not yet performed.
