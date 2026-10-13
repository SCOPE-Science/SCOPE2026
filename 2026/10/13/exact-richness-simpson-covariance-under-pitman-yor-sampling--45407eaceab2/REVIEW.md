# Review
## Correctness
PASS. Conditioning on whether the first two labels share a block changes the state at time two from one block to two. The Pitman–Yor expected block-count recursion is affine, so the difference between those two conditional means evolves multiplicatively and gives the exact product \(R_n\). Exchangeability then converts the covariance with one pair indicator to covariance with pair homozygosity. Exact set-partition enumeration and independent recurrence replay agree with every displayed formula.

## Originality
PASS, with a specific older-moment-literature risk. The foundational full partition paper gives the model but contains no homozygosity or Simpson statement. A complete later paper on Ewens–Pitman restart and subsampling laws gives exact species-count moments but contains no homozygosity, Simpson, or covariance occurrence. A modern Ewens review discusses both \(K_n\) and Watterson homozygosity in a conditional testing framework but does not state this unconditional finite covariance.

The strongest residual risk is the inaccessible complete text of the 2000 Yamato–Sibuya paper on moments of Pitman sampling formula, plus older population-genetics work under alternative allele-frequency notation.

## Value
PASS. Richness and homozygosity are standard complementary summaries of a species sample. The theorem gives their exact finite dependence for the full Pitman–Yor family and identifies a simple conditional mechanism: one pair disagreement raises expected richness by exactly \(R_n\). In the Ewens case the resulting pair-diversity covariance is exactly independent of sample size, a structurally informative finite identity.

## Closest literature and limitations
The closest sources supply the full partition distribution, marginal richness moments, restart/subsampling laws, and the classical conditional homozygosity test. None of the inspected complete sources states the pair-conditioned richness gap or the displayed mixed covariance. The theorem is limited to the standard two-parameter partition rule and does not claim stochastic ordering or a complete joint law.

Self-review: passed. Independent audit: not yet performed.
