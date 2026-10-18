# Review of joint span–crossing fluctuation theorem

## Correctness — PASS

The finite formulas follow from edge-indicator probabilities on uniform matchings and the conditional number of crossing partners of a prescribed chord. The external scalar crossing-variance identity is explicitly attributed to Flajolet and Noy. Crucially, the iid-endpoint representation converts crossings to an exact bounded order-two U-statistic and total span to another such U-statistic with expected absolute approximation error exactly \(n(n-1)/(2(2n-1))\). Hoeffding projection and the ordinary bivariate iid central limit theorem prove the limiting covariance matrix. Both projection integrals and all five stated finite moments were checked independently with exact rational computations for \(2\le n\le7\). The numerical check is finite evidence only; the general theorem follows from the proof.

## Originality — PASS (historical priority not independently established)

The closest primary study is Acan, arXiv:1501.01489v1, on the **same** chord diagrams, with **single-chord** span and crossing-degree information. The exact local conditional mean can already be deduced there; the present claim instead includes a full joint central limit theorem for sums over all chords and all crossing pairs, together with a positive-definite covariance and explicit residual Gaussian law. Flajolet and Noy provide the **scalar** crossing-count variance and Gaussian limit. No directly covering joint global span–crossing theorem was identified in the material inspected or in the searches recorded in the accompanying structured review. An unlocated specialization of a more general result remains a material historical risk; a failure to find it is not evidence of uniqueness.

## Value — PASS

The total shorter-arc span is a natural geometric aggregate, and crossing count is the edge count of the intersection graph. Their joint uncertainty cannot be inferred from their marginals. The exact asymptotic correlation \(\sqrt{15}/4\) and residual variance \(1/720\) reveal quantitatively that geometric spans explain \(15/16\) of intersection-count variance, while an independent noise direction remains. This is an informative structural fluctuation law, not just an isolated finite moment or an arbitrary slice.

## Scope and limits

The model is a uniform labeled cyclic perfect matching; no claim is made for conditioned or geometric-length-weighted matchings. Historical overlap checks are bounded and not an assertion of priority. The theorem is an asymptotic weak limit, with no claimed convergence rate. Independent verification of mathematical novelty and correctness remains outstanding.

Self-review: passed. Independent audit: not yet performed.
