# Review of logarithmic critical return asymptotics

## Correctness

The scale-product formula gives transience because \(\rho_x\sim Kx^{-2\beta-1}(\log x)^{-2d}\) is summable. The exact hitting-probability ratio yields the h-transformed drift \((1/2-\beta)/x-d/(x\log x)+O(1/(x\log^2 x))\). Alexander's first-return theorem applies with \(\delta=2\beta-1>-1\) and gives the conditional first-return mass. A local defective-renewal theorem then transfers that mass to the original transient return probability, with the positive factor \((1-r)^{-2}\). The moment threshold follows from the logarithmic integral test.

## Originality

Lo, Menshikov, and Wade (2022) explicitly exclude the critical equality and note the absence, to their knowledge, of a transient-chain local-return estimate. Alexander (2009) treats the recurrent reflecting chain obtained after the h-transform, not the original transient chain. The logarithmic coefficient and defective-renewal transfer are made explicit here. Searches by source, aliases, critical parameters, and local-return formulation produced no exact match. The result is a synthesis of known methods, so independent priority remains unverified.

## Value

The local asymptotic \(P_0(X_{2n}=0)\sim Cn^{-\beta-1}(\log n)^{-2d}\) resolves the critical return-moment boundary at logarithmic precision. It identifies the exact threshold \(d=1/2\), including divergence at equality, and shows why the leading Lamperti drift alone is insufficient to decide the boundary.

## Limitations

The result is restricted to nearest-neighbour chains with the displayed second-order drift expansion. It does not establish the analogous statement for bounded jumps larger than one. The local-renewal transfer uses a standard regularly varying local-subexponential result. Independent priority review and independent audit have not been performed.

Self-review: passed. Independent audit: not yet performed.
