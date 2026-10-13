# Review of Pairwise metrics forget \(2^{n-1}-1-\binom n2\) orbit dimensions in the universal \(L_1\) diversity

## Correctness
PASS. Bryant--Nies--Tupper provide the two structural premises needed here: finite \\(L_1\\) diversities have unique cut-semidiversity decompositions, and their class has a separable universal ultrahomogeneous Fraïssé limit. Exact ultrahomogeneity turns equality of the induced finite labeled diversity into equality of ordered-tuple automorphism orbits. The forgetful map to pairwise distances is exactly the cut-incidence matrix. Its full row rank follows from \\(2e_{ij}=c_i+c_j-c_{ij}\\), yielding the claimed nullity by rank-nullity. Positivity makes the local fiber an open subset of the corresponding affine kernel translate. The verifier confirms these identities through eight labels and checks the explicit four-point family.

## Originality
PASS with substantial folklore risk. The number of cut rays \\(2^{n-1}-1\\), the \\(\\binom n2\\)-dimensional metric cut span, unique cut decomposition for \\(L_1\\) diversities, and the Fraïssé limit are all prior facts and are not claimed as new. Targeted published-finding corpus searches, exact-formula web searches, pairwise-distance/cut-semidiversity searches, and own-ledger checks did not locate the synthesis that identifies the cut-weight cone with ordered-tuple orbit parameters and computes the exact dimension of the metric fibers. Because the deduction is short once the ingredients are juxtaposed, an earlier uncatalogued formulation is plausible.

## Value
PASS. The result quantitatively explains how much higher-arity information the diversity structure retains beyond its metric reduct. It gives an exact exponential-versus-quadratic dimension gap, a sharp onset at arity four, and an explicit four-point kernel direction. This directly refines the model-theoretic contrast in the source between the ultrahomogeneous \\(L_1\\)-diversity limit and the failure of the finite \\(L_1\\)-metric class to have a Fraïssé limit.

## Closest literature and limitations
Bryant--Nies--Tupper (arXiv:1901.02122) is the closest source: it states unique cut decomposition, failure of uniqueness for metric cuts, and the universal ultrahomogeneous \\(L_1\\)-diversity theorem. Bryant--Tupper (arXiv:1312.5408) is the underlying cut-semidiversity source. Classical cut-cone references already imply the rank calculation. The retained claim is limited to injective labeled tuples and to the positive cut-weight stratum for the clean fiber-dimension statement.

Self-review: passed. Independent audit: not yet performed.
