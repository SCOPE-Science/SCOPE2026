# Scientific review of the square-root lifting law

## Correctness — PASS

The full statement is quantified for finite connected vertex-transitive base graphs, symmetry-invariant positive base-edge costs, integer leaf multiplicity and arbitrary feasible nonnegative conductances. The spectral gap is concave in edge weights, so averaging over automorphisms and private-leaf permutations yields an optimal uniform-leaf representative even when the competitor is asymmetric. The uniform-leaf block spectrum has lower branch determined by the base spectral gap; the branch is strictly increasing in that gap and lies below the leaf-difference eigenvalue. The definition of the base unit-budget optimum therefore gives a sharp cost constraint. A Schur complement and a strictly convex one-variable minimization prove the exact square-root formula and produce a feasible attaining allocation. Boundary zero-rate choices have zero gap. Critical identities were rederived symbolically, and numerical assembled-matrix checks cover vertex-transitive examples, including non-edge-transitive prisms. No finite check is substituted for the quantified proof.

## Originality — PASS, with bounded uncertainty

The closest continuous-time reference is Sun, Boyd, Xiao, and Diaconis (2006, DOI 10.1137/S0036144504443821), whose complete discussion provides the general semidefinite model, concavity and cycles but not an exact pendant-decoration lifting rule. Barik, Pati, and Sarma (2007, DOI 10.1137/050624029), especially Theorem 3.2, provides unweighted corona Laplacian spectra, but no class-cost-constrained global conductance optimization. Boyd, Diaconis, Parrilo, and Xiao (2009, DOI 10.1137/070689413) provides symmetry reductions for a discrete-time SLEM objective with different admissibility constraints. The present theorem supplies the quantitative budget transfer, positive square-root allocation, arbitrary leaf multiplicity, and non-edge-transitive core handling. Searches for equivalent statements and stronger results did not establish coverage, but specialized prior sources may be missed and literature search cannot prove absolute novelty.

## Value — PASS

The lifting theorem is a nontrivial exact composition law: a network with an arbitrary number of private leaves per vertex can be optimized from the original core's one scalar unit-budget spectral-gap value, without solving the larger semidefinite problem. It specifies the globally optimal cost split and private-leaf conductance, and carries every optimal base conductance profile forward. It applies even when different core-edge orbits require distinct costs and optimal weights, as shown by the explicit two-orbit prism family. The result is motivated by budgeted diffusion-network design and provides a reusable design rule rather than an arbitrary graph enumeration.

## Closest antecedents and boundaries

The explicit primal formula does not assert new general eigenvalue perturbation theory or an unrestricted optimizer-uniqueness classification. It depends on vertex transitivity and invariant cost coefficients, and treats the combinatorial continuous-time Laplacian. Prior works supply the general optimization framework, spectral ingredients and symmetrization methods; their combination requires an additional sharp scalar budget calculation to obtain the stated identity. The core constant is not universally evaluated for all graphs. Full specialist-literature exhaustion and independent auditing remain open.

Self-review: passed. Independent audit: not yet performed.
