# Scientific review: finite-mixing parity threshold

## Correctness

**PASS.** The statement specifies every domain restriction: \(p\in(1/2,1)\), integer \(k\ge1\), \(r_i,a_i>0\), \(a_i\ge r_i-1\), and \(r_1r_2<1<(r_1+r_2)/2\). The exact power identity for the migration matrix leads to a two-dimensional Perron eigenvalue with trace \(\bar r(1+s)\) and determinant \(r_1r_2s\). Its strictly increasing dependence on the signed residual eigenvalue \(s=(-[2p-1])^k\) gives the sharp odd/even threshold. Global extinction (including equality) follows by linear domination or a strict left-Perron Lyapunov function. Global persistence as convergence to one positive fixed point follows from strong monotonicity, subhomogeneity, and lower/upper iterations. Exact-rational identity checks and a nonlinear iteration checker ran successfully. Computational tests are corroboration, not a replacement for the proof.

## Originality

**PASS under inspected-source evidence; not an exhaustive novelty certification.** The closest source is Bravo de la Parra and Sanz-Lorenzo (2021), which introduces the sequential fast-movement/slow-infection construction and gives limiting large-\(k\) results for SEIRS. It does not state a sharp all-\(k\) odd/even threshold for the rational two-patch map. Grumbach and collaborators (2023) give a much stronger census of equilibrium *population sizes* for two source patches with one dispersal step; their hypothesis \(r_i>1\) excludes the present mixed source–sink regime and their classification is not the same extinction implication. Continuous-time mobility literature does not capture negative subdominant mixing eigenvalues. The relevant two-stage SEIR mathematical record concerns different E/I migration matrices, not the present same-compartment repeated swap. A hidden equivalent finite-round result elsewhere remains possible.

## Value

**PASS.** The source's large-separation reduction cannot resolve finite migration-round behavior when the movement eigenvalue is negative. The exact all-integer phase diagram exhibits a structural reversal: odd finite mixing rounds can globally eradicate infection while every even count and the infinite-fast-mixing limit remain endemic. The cutoff works for arbitrary saturation strengths and includes the critical equality branch, so it is a natural, reusable boundary result rather than a numerical example or a purely local linear calculation.

## Closest literature and scope restrictions

The model is a phenomenological rational two-patch infection map and is not asserted to coincide with the full four-compartment SEIRS equations. The phenomenon requires over-exchange \(p>1/2\), balanced populations, fixed repeated movement, and heterogeneous patch gains straddling the invasion threshold; neither stochastic extinction nor unequal populations is covered. The 2024 continuous-time metapopulation paper and 2006 patch model were assessed only to the extent of accessible abstracts. No independent audit was performed.

Self-review: passed. Independent audit: not yet performed.
