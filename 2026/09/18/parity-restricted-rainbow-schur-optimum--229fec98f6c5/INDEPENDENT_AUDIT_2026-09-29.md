# Independent audit — 2026-09-29

Record: `2026/09/18/parity-restricted-rainbow-schur-optimum--229fec98f6c5`  
Assigned and audited source tree: `e7f0cbd0c2fa2f69c1c44d0bf77847b29735e231`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**independently_reproduced**. The exact reduction and Bellman analysis reproduce independently. For n=2m, opposite-colored odd indices contribute 2a(m−a) ordered rainbow pairs with one odd summand, and the two-odd-summand pairs are exactly twice the cut of the threshold graph H_m with i+j≤m+1. Deleting vertices 1 and m gives H_{m−2}; separating the three membership cases for {1,m} yields the displayed recurrence for h_m(a). An independent exact-rational implementation matched this recurrence against brute-force fixed-cardinality cuts on small m and verified the claimed Bellman residual bound |Φ_m−B_m|≤1/2 for all m≤2000. The resulting uniform O(m) error reduces the asymptotic problem to maximizing G(x)=x(1−x)+H(x), whose only maximizers are 5/11 and 6/11 with value 9/22. The stated m/4 upper error and color-balance stability follow.

## Originality

**supported_qualified_current**. Hegde–Kumar–Pratibha establish the unrestricted 9/22 lower and 8/15 upper bounds and supply the parity-and-interval lower construction, but their public statement does not optimize over all arbitrary two-colorings of the odd integers with monochromatic evens. Targeted searches did not locate the fixed-cardinality threshold-graph reduction, its piecewise cut profile, or the parity-restricted stability theorem. The source is only days old, so the originality conclusion is necessarily narrow and subject to concurrent-work risk.

## Scientific value

**meaningful_partial_optimality**. The theorem rules out a large natural class of attempted improvements to the current 9/22 construction: any asymptotic improvement must abandon the monochromatic-even/two-colored-odd paradigm. The exact threshold-graph formulation and stability constraint are useful structural outputs while the unrestricted problem remains open.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/parity-restricted-rainbow-schur-optimum--229fec98f6c5
- https://arxiv.org/abs/2609.18474
- https://doi.org/10.37236/13554

## Limitations

- The theorem is restricted to the parity class in which the even integers use one color and all odds avoid that color.
- The stability statement constrains only the asymptotic odd-color balance, not a unique arrangement.
- The motivating lower-bound preprint is extremely recent, so an unindexed contemporaneous optimization cannot be excluded.
