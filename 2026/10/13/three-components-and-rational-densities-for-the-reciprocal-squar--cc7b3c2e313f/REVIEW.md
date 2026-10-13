# Review of the cube-free reciprocal-square divisor-range theorem

## Correctness — PASS

The domain is exactly the cube-free positive integers, with prime exponents \(0,1,2\). Multiplicativity and absolute convergence identify its closure with infinite products of three local options. The essential tail-filling lemma is not assumed: the proof establishes all seven prime-local rational inequalities below \(29\), then uses Nagura's prime-interval theorem and the elementary bound \(\log(1+x+x^2)\ge x\) for larger primes. The three-option interval-covering argument is constructive and takes a convergent limit. An exact nine-interval reduction then follows, with every overlap and both separating gaps verified by rational estimates using Archimedes' bounds for \(\pi\). Independent density calculations from cube-free local exponent weights sum to one. The standalone checker reproduces all finite rational certificates from its actual source file. No finite computation is mistaken for the infinite prime bound or the closure proof.

## Originality — PASS, with residual literature risk

Defant's 2015 restricted-domain paper (arXiv:1507.02663) introduces the exact domain parameter and asks for the number of component intervals; its theorems give connectedness thresholds but no component count or endpoint and density data for exponent cutoff two at reciprocal-square weight. Sanna's 2015 paper (arXiv:1507.08091) gives three intervals and densities for the unrestricted prime exponents, not for the cube-free subset; an unrestricted union of three intervals does not imply the subset fills three intervals. The cube-free endpoints \(9720/(91\pi^4)\), \(120/\pi^4\), and \(315/(2\pi^4)\), and its conditional densities, are distinct from Sanna's. Zubrilina (arXiv:1711.02871) and Achenjang–Berger (arXiv:1808.07550) likewise work with unrestricted integer domains. The prior squarefree restriction has a different component partition; a published unitary reciprocal-square result uses different prime-local factors. Bibliographic and semantic alias searches found no statement that covers the asserted cube-free equality. An unindexed exact calculation could still exist, and search absence is not proof of novelty.

## Mathematical value — PASS

The 2015 restricted-domain paper specifically asks for exact component counts for exponent cutoffs, a natural topological invariant of an arithmetic-function range. The cutoff two is the first nonsquarefree restriction, and the theorem determines not only the component number but every endpoint and the exact conditional distribution across its components. That it retains the unrestricted three-component count despite smaller maximal Euler factors is a mathematically interpretable stability fact, and the independent tail-filling proof explains why no additional gaps appear. This is a complete natural case, not an arbitrary small numerical bound or merely a finite enumeration. It does not solve the general cutoff-parameter problem.

## Sources and limitations

Primary literature inspected: Defant, *On the Density of Ranges of Generalized Divisor Functions with Restricted Domains* (2015); Sanna, *On the closure of the image of the generalized divisor function* (2015); and later unrestricted-range studies of Zubrilina (2017) and Achenjang–Berger (2018). The prime-gap input is Nagura (1952). Finite rational computations verify only the stated exact comparisons. The global statement uses a classical published prime-interval theorem and standard Euler products. The novelty assessment is not a guarantee against inaccessible or unindexed prior work.

Self-review: passed. Independent audit: not yet performed.
