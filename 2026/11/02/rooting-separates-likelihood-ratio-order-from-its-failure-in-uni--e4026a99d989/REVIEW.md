# Independent mathematical audit

## correctness

PASS

Choosing the s-1 nonroots in the marked tree, its Cayley tree, and the residual forest on n-s vertices with k-1 fixed roots gives the displayed classical mass formula, including the upper endpoint where the residual factor is 1. Cancellation gives the adjacent ratio C(n,k)*(1+(k-1)/(n-k-s+1)), strictly increasing on common support. The added upper endpoint and the k=1,n point-mass laws give the full cross-product order; transitivity gives all pairs. At each claimed threshold there is a strictly positive cross-product difference between size 1 of the law with more roots and the upper endpoint of the law with fewer roots; summing cross-products across the threshold gives strict tail dominance. Exchangeability gives mean n/k and ordered quantile coupling gives the exact W1 difference. Size bias multiplies each ratio by the positive constant k/(k+1), so it preserves the order. In the unrooted case, the conditioning formula uses the residual counts F(n-s,k-1). The labeled EGF and Lagrange coefficient give the claimed F(m,2), with m=2,3 checked separately. Normalizations cancel at s=1,2; the obstruction reduces to comparing 2(n-1)^2/((n-2)(n+5)) and 2(n-2)^2/((n-3)(n+4)). Their quotient is the displayed 1+positive term for n>=5, and is 1 for n=4, where the rest of the relevant support comparisons are valid. All other adjacent cases at n<=4 have a degenerate endpoint. Own exact set-partition enumeration with Cayley weights (branches/audit3.py, audit3.out) corroborates all rooted pairs and the unrooted boundary on n=2..9; at n=5 the unrooted size-1 and size-2 counts are (16,12) vs (15,12), before normalization. The original script is not relied on for exhaustiveness; its finite tail check is non-strict, while strictness follows analytically as above. No claim of unrooted stochastic-order failure is present.

## originality

PASS

The underlying joint rooted distribution, one-root mass and resulting moment are classical. The rooted likelihood-ratio strengthening is a short calculation from them, and its size-biased form is immediate once proved, so these should not be treated as new forest enumeration or independently substantial results. The surviving contribution is the sharp comparison of the two uniform sampling conventions: the strict rooted order together with the exact, persistent reverse step for unrooted forests, starting at n=5. The inspected joint law, stochastic coupling, enumerator total positivity and same-day unrooted two-component result do not give that comparison. This is a bounded originality judgment, strongest for the ensemble contrast and all-order obstruction.

## value

PASS

Rooting is an intrinsic modeling choice for labeled forests, and likelihood-ratio order is substantially stronger than ordinary tail ordering. The exact reversal in the first nondegenerate unrooted comparison provides a reusable sharp boundary: it occurs for every n>=5, at the same two smallest sizes, yet never for n<=4. This excludes a general monotone-likelihood-ratio argument for the unrooted model without pretending to refute unrooted stochastic monotonicity. The valued contribution is the structural rooted/unrooted contrast, not the routine size-bias or transport corollaries in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
