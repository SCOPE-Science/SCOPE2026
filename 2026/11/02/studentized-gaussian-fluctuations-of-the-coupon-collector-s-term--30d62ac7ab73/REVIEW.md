# Scientific review

## Correctness (C): PASS

The exact conditional law is reconstructed from independent rate-one Poisson processes and the unique maximal first-arrival time, including the independent truncated-positive Poisson counts of the other types. The conditional mean is \(1+(n-1)m/(e^m-1)\), and the conditional variance is \((n-1)p(m)(1-p(m))\). Uniform compact-window estimates give both the normal limit and an \(O_K((\log n)^{-1/2})\) conditional Kolmogorov bound. Joint asymptotic independence follows by tightness and uniform conditional characteristic functions. The independent merged-clock construction gives an exact \(L^2\) de-Poissonization identity; its error is negligible on the \(\sqrt{\log n}\) scale. The packaged standalone program independently checks 90 exact finite assertions, without treating them as infinite proofs.

## Originality (O): PASS, with residual historical risk

The nearest directly inspected works establish leading exponential asymptotics, stochastic ordering, and other features of the same sibling-collector model: Ilienko, arXiv:2002.00650 and 2026 publication, Theorems 1--3; Papanicolaou--Doumas, arXiv:2005.05270, the first sibling exponential limit; and Long, arXiv:2606.29635, Theorems 4--5. Their stated and inspected conclusions do not determine the centered \(\sqrt{\log n}\)-scale residual or its joint independent Gaussian/Gumbel limit. A leading-scale limit cannot by itself force a second-order conditional limit. The general Poisson and central-limit ingredients are classical and not attributed as novel. No implication-equivalent public claim was identified in the targeted searches, but broad older occupancy theory may contain a relevant equivalent formulation; definitive priority is not certified.

## Value (V): PASS

The central probabilistic issue is to separate a global extreme-value source of order-\(\log n\) variability from the remaining conditional occupancy noise. The theorem supplies a natural observable-time normalization that turns the residual into an asymptotically independent pivot; the exact conditional binomial law and uniform Gaussian bound explain precisely why this happens. This is a structural second-order extension of an established stochastic model and not a numerical recomputation or arbitrary parameter slice.

## Limits and sources

Only uniform iid sampling and the first sibling are covered. The exact conditional binomial statement concerns the Poisson embedding's physical stopping time, not the discrete stopping count. Primary scientific comparisons: Ilienko (arXiv:2002.00650; later doi:10.15559/26-VMSTA306); Papanicolaou and Doumas (arXiv:2005.05270); Doumas and Papanicolaou (arXiv:1412.4346); Long (arXiv:2606.29635). Holst's 1986 occupancy survey is a residual generality risk. Finite computation does not imply an infinite theorem.

Self-review: passed. Independent audit: not yet performed.
