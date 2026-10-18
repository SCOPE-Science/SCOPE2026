# Review of the three-inclusion-order sampling separation theorem

## Correctness — PASS

The complete finite-population statement is proved by six analytical steps: independent affine differences for each set of at most three distinct points; the exact incidence count; factorization of the quadratic Boolean Walsh transform into \(m\) four-term sums; the resulting exactly two-point hyperplane total; finite-population mean and variance identities; and the standard hypergeometric central limit theorem together with Portmanteau to obtain maximal total-variation distance. All ranges, parameters, and variance normalizations are explicit. The hypergeometric mean \(N/4+\sqrt N/4\) and variance \(N/16\) imply the stated standardized variance exactly. An executed pure-standard-library verification program checked every Walsh coefficient and affine block at sizes \(N=16,64,256\), and all subsets of sizes one through three at \(N=16\). Its finite scope is not misrepresented as a proof of the limit.

## Originality — PASS, qualified

The closest primary source is Chen, arXiv:2610.09168v1. Chen constructs an order-two counterexample and expressly poses every fixed higher inclusion order as a conjectural problem; its general block-design inclusion identity is acknowledged as a known ingredient. The additional source on triplewise-independent summands, arXiv:2104.02292, concerns random-variable sequences, not fixed-size survey-sampling designs with SRSWOR-matched probabilities. Classical affine Hadamard three-designs and quadratic Boolean bent functions provide ingredients but, in the inspected material, do not assert this joint survey-sampling asymptotic separation. Mathematical-record searches for the exact combination, higher-order aliases, three-wise matching, and Fourier/bent formulations did not identify an equal or stronger theorem. Remaining priority risk: an older design-theoretic or sampling-theoretic source could combine these classical ingredients into an equivalent unpublished or unindexed example. No literature search is a proof of absolute uniqueness.

## Value — PASS

The construction resolves the first unproved case, \(r=3\), of an explicitly formulated 2026 survey-sampling question about which finite-order inclusion probabilities can transfer normal asymptotics. It is substantive because every distinct triple has exactly the correct joint inclusion probability, all outcomes are deterministic and uniformly bounded, and the two sampling laws still become maximally separated in total variation, not merely weakly different. The construction yields a transparent analytic obstruction for variance-matched survey estimates. It does not settle \(r\ge4\), characterize all such designs, or provide a general finite-population CLT.

## Principal sources and risks

Chen, *Low-Order Inclusion Probabilities Do Not Determine Asymptotic Normality*, arXiv:2610.09168v1, especially Sections 1–2, 4, 6 (order two and the higher-order conjecture). Boglioni Beaulieu, Lafaye de Micheaux and Ouimet, *Counterexamples to the classical central limit theorem for triplewise independent random variables having a common arbitrary margin*, arXiv:2104.02292 (triplewise independent but not the present fixed-size design). The affine Hadamard three-design and the bent Walsh spectrum are standard. The general hypergeometric central limit theorem supplies the sole non-elementary asymptotic step; the remaining proof is exact finite algebra and combinatorics.

Self-review: passed. Independent audit: not yet performed.
