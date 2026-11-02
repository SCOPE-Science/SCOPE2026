# Scientific review — a square-root imbalance in near-census relative entropy

## Correctness — PASS

The claim is about the directed KL divergence between two **color-count** laws after drawing all but one of \(n\) balls, not the divergences between ordered sequence laws. The two-point hypergeometric distribution and the equality of the two relevant binomial probabilities give the finite-size identity exactly. Uniform factorial Stirling estimates in the interior, an explicit endpoint bound, and the unique global maximum of a limiting function localize every integer maximizer. The leading limiting function has vanishing quadratic but negative quartic curvature at balance; the next Stirling correction has positive quadratic curvature. Rescaling imbalance by \(\sqrt n\) yields \(f(x)=\frac43x^2-\frac83x^4\), whose only maximizers are \(x=\pm\frac12\) and whose maximum is \(1/6\). Lattice approximation proves both asserted limits for **every** maximizing sequence. The accompanying standard-library checker independently tests the exact probabilities and relative entropies; finite tests are not substituted for the analytic argument.

## Originality — PASS, subject to historical-priority limitations

Johnson, Gavalakis and Kontoyiannis, *Relative entropy bounds for sampling with and without replacement* (arXiv:2404.06632, first posted April 9, 2024; published in 2025) define the same hypergeometric-to-multinomial count divergence, and derive composition-sensitive bounds. Their principal finite-population theorem assumes a sample of size at most half the urn, while their fixed-fraction comparisons do not determine the near-census maximizer. Harremoës and Matúš, *Bounds on the information divergence for hypergeometric distributions* (arXiv:2002.03002; Kybernetika, 2020), derive general bounds and fixed-fraction asymptotics without resolving the optimized leave-one-out composition and its second-order gap. The identical finite divergence identity is a specialization of these probability laws and is not claimed independently novel; the claim requiring priority assessment is the asymptotic displacement and sharp improvement. Searches for this composition optimization, equivalent binomial modal-mass formulations, and available indexed results identified no theorem implying it. A hidden treatment of binomial modal saddle-point optimization remains possible; definitive priority requires a specialist literature review.

## Mathematical value — PASS

The choice of urn color composition is a natural parameter in approximation of sampling without replacement. Near a complete sample, the balanced configuration has a degenerate leading-order extremum. The theorem resolves where the worst binary composition lies at the finer square-root scale, and how much the relative entropy improves over balance. The positive \(1/(6n^2)\) effect is not presented as a large numerical improvement; its value is the structurally different extremizer at a meaningful limiting boundary and a sharp finite-size correction. The result concerns all sufficiently large population sizes, not an arbitrary numerical slice.

## Limitations and closest sources

The result treats exactly two nonempty colors and a sample leaving exactly one ball. It does not give an exact integer optimizer for each \(n\), does not address uniqueness, and does not settle arbitrary sample fractions or more colors. The complete source material discussed above was read in relevant sections, but historical priority is not exhaustively certified. Independent proof review has not occurred.

- Johnson, Gavalakis, Kontoyiannis, arXiv:2404.06632, https://arxiv.org/abs/2404.06632 .
- Harremoës, Matúš, arXiv:2002.03002, https://arxiv.org/abs/2002.03002 .

Self-review: passed. Independent audit: not yet performed.
