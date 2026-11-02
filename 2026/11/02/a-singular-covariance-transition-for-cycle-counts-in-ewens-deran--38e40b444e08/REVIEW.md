# Scientific review: dependence transition in Ewens derangements

## Correctness — PASS

The cycle-weight exponential formula gives the normalizer and the joint factorial moments. The parity proof reconstructs the exact edges \(u=0,1\), uses the universally valid bound \(1/3\le d_k\le1/2\) for \(k\ge2\), and proves strict shrinking of the alternating ratios \(d_{k+s}/d_k\) without relying on computation. The standard analytic singularity expansion gives the second-order fixed-length covariance. A standalone standard-library verifier passed 2003 checks; finite enumeration was not used as an infinite proof. The detailed proof and domain appear in `RESULT.md`.

## Originality — PASS, with explicit residual historical risk

The complete exact mixed-moment formula is already a consequence of da Silva–Jamshidpey–Tavaré (2020), equation (6). It is not claimed novel. The narrower and substantive statement assessed here is the **strict alternating sign for all uniform derangements and all distinct cycle lengths**, its factorial amplitude, and the **universal parameter-dependent nonunit second-order sign**. Searches for these sign and rate results in research records, web-indexed literature and relevant primary texts found no express equivalent. Betz–Ueltschi–Velenik (2009) covers the general weighted-permutation framework and asymptotic cycle lengths, not this covariance transition in the inspected sections. The 2020 full-text treatment provides the moments and Poisson limit but not the all-size strict sign theorem or the \(n^{-2}\)/factorial dichotomy. A standard coefficient-extraction method could potentially lead to the nonunit part from those formulas; older literature may have made such an inference, and priority remains unconfirmed independently.

## Mathematical value — PASS

The cycle counts converge jointly to independent Poisson variables, so a first-order limit cannot describe their finite-sample dependence. The result distinguishes a robust sign and polynomial scale for nonunit Ewens parameters from a strict, unexpectedly alternating factorial dependence at the uniform parameter. The universal leading \(n^{-2}\) coefficient, independent of selected cycle lengths, and the exact parity law are natural complete classifications, rather than arbitrary computed cases. The theorem identifies a genuine singular boundary in a standard conditioned probabilistic-combinatorial model.

## Closest literature and limitations

Primary sources: Betz–Ueltschi–Velenik, arXiv:0908.2217v1 (2009), and da Silva–Jamshidpey–Tavaré, arXiv:2006.04840v1 (2020). The last source gives the previously known factorial moments, and the first develops the broader weighted-permutation framework. No independent research audit has occurred. All parameter-fixed asymptotics exclude nonuniform scaling and moving lengths.

Self-review: passed. Independent audit: not yet performed.
