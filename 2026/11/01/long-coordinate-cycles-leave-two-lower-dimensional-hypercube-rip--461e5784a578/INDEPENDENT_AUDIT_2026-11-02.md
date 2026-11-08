# Independent mathematical audit

## correctness

PASS

PASS: This is an all-parameter statement k>=4,f>=0, n=k+f. A fixed point in any simplex has barycentric coefficients constant on each cyclic coordinate orbit; the admissible-orbit complex triangulates the actual geometric fixed locus, not just fixed vertices. For moving-block word weight w, average Hamming discrepancy over k cyclic shifts equals 2w(k-w)/k; orbit diameter <=2 plus zero-shift implies w(k-w)<=k-1. For k>=4 this excludes every 2<=w<=k-2, so only all-zero A, one-hot C, one-cold D, and all-one B orbits survive, for each fixed suffix y∈Q_f. Direct maximum cross-orbit distances yield only A_yA_z and B_yB_z for suffix distance <=2 and A_yC_z, B_yD_z for suffix distance <=1. All C_y are dominated by A_y, and D_y by B_y; the simultaneous contiguous simplicial retraction yields two components each exactly VR(Q_f;2), with stated commuting residual symmetries. For f=0..2 these components are contractible; for f>=3 the previously established Adamaszek–Adams hypercube theorem yields c_f spheres S³ in each. The k=3,f=0 boundary is a four-cycle, not two points. Independently enumerated all admissible moving orbits and pair compatibilities for (k,f)=(3,0),(4,0),(4,2),(4,3),(5,3),(6,2), verifying the sharp boundary and every claimed dominance inclusion; this checks but does not replace the all-k proof.

## originality

PASS

PASS best-of-knowledge: the Adamaszek–Adams theorem supplies the ambient smaller-cube Rips homotopy type and is explicitly credited; later hypercube symmetry work addresses representations of the ambient homology, not a geometric C_k fixed locus or its strong-collapse model. Exact orbit classification and residual-equivariant two-component deformation retraction are additional structural statements.

## value

PASS

PASS: Geometric fixed points of natural coordinate-permutation symmetries are meaningful equivariant homotopy invariants not determined by ordinary homology characters. The explicit orbit-space triangulation, sharp k>=4 threshold, two-component strong collapse and residual symmetry provide a reusable structural reduction for a family of arbitrarily large hypercubes. Known smaller-cube Rips sphere counts are correctly credited rather than presented as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
