# Scientific review: exact cut-space projection constants of weighted multibranch diamonds

## Correctness — PASS

The theorem specifies a real weighted edge \(\ell_1\) space and an exact graph-gradient range. The proof identifies that range by equality of branch sums, averages every possible projection over actual ambient isometries preserving the range, and proves that the averaged projector fixes all independent branch-difference lines. The weighted matrix-column norm is computed explicitly for both edge types in every branch. A reciprocal-sum inequality gives a lower bound for *all* coefficient signs, and strictly positive coefficients attain equality. Jensen's strict convexity proves the rigid equal-weight upper extremum; a direct limit proves the unattained lower infimum. The one-defect derivative is an exact rational identity, not numerical inference.

The embedded `verify_exact.py` passed 120 separate rational instances, checking projection idempotence, range, basis fixing, all weighted column norms, and equality with the analytic lower bound. An independently formulated unconstrained (nonsymmetric) finite-dimensional projection linear program in `verify_lp.py` matched the theorem in 50 dimensions-and-weight instances within \(10^{-8}\). Such finite tests are corroborative only. The proof gives unrestricted quantifiers \(m\ge3\), \(r_i>0\), and real linear projections.

## Originality — PASS with stated residual risk

Dilworth–Kutzarova–Ostrovskii (2023), arXiv:2305.12582v1, §§1.1, 1.3, 1.6 and 2.1, supplies the cut/cycle definitions and weighted edge quotient but develops minimal projections chiefly onto **cycle** spaces, with explicit tori and Hamming results. The exact higher-codimensional weighted cut-space projection formula is not among the inspected results. Dilworth–Kutzarova–Ostrovskii (2018), arXiv:1807.03814v1, §5.1, explicitly discusses \(K_{2,m}\) multibranching diamonds but computes a **cycle-space** parameter \(2(m-1)/m\), as distinct from the cut-space constant \(2-1/m\) at equal weights. Classical Blatter–Cheney (1974) results concern hyperplane targets, whereas the present targets have codimension \(m-1\ge2\). General group averaging is explicitly credited as a method, not treated as an original lemma.

The mathematical-record searches also returned weighted Lipschitz-free space, complete bipartite Hilbert-distortion, cactus coordinate-projection, and other graph cut-projection results, but no statement implying this weighted family. A general subspace projection formula not exposed by accessible bibliographic records could subsume the result; the Blatter–Cheney full text was not inspected. Failed search alone is not used as a proof of novelty.

## Mathematical value — PASS

Complementability of graph cut and cycle spaces governs finite Lipschitz-free geometry and is treated as a structural Banach-space problem in the primary literature. The result solves an all-weight, infinite-dimension-family optimization over **every** linear projection, not just a selected orthogonal or symmetric projector. It also proves a sharp and rigid geometry-of-weights law: equal branches uniquely maximize the obstruction \(2-1/m\), while increasing one branch's length drives the exact minimum norm toward 1 at quantified order \(1/t\). The cut/cycle gap at equal weights is a substantive distinction for the same graph, not a reparameterization of an existing cycle-space value.

## Limitations

The paired edges of each branch must have equal lengths, and the result concerns ambient relative projections only. It does not compute minimal weighted cycle projections, arbitrary independently weighted edge projections, or projections of iterated diamonds. The full text of one older hyperplane reference was unavailable; possible equivalent general results remain an originality risk. Numerical testing does not certify the universal theorem, and independent scientific validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
