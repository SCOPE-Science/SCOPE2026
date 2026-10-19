# Scientific assessment

## Correctness — PASS

The stated theorem holds for every deterministic time \(t>0\) and spatial level \(x\). The proof reconstructs the occupation-density normalization and the killed/unrestricted Brownian resolvents, splits local-time increments before and after level hitting, integrates over the maximum threshold, and inverts explicit Laplace transforms. Reflection produces the span identity. Strict sign statements follow from positive Gaussian integrals and the exact origin value; no conclusion about uniqueness is taken from sample calculations. The `verify.py` standalone checks executed and passed, including independent integral representations and Laplace comparisons. The source identity at the origin is a boundary check, not a substitute for the nonzero-level argument.

## Originality — PASS (subject to historical uncertainty)

Pitman's directly inspected 1998 report gives the joint distribution of local time and the Brownian endpoint, plus bridge-local-time identities; the marked point/local-time covariance with full-time span and the positive far-field regime are not asserted in its inspected results. The inspected local-time chapters of Mörters–Peres provide background theory rather than this mixed expectation. Cox–Hobson–Obłój study local-time/terminal-state inequalities and a local martingale, not span covariance. Comparison with a published random-walk maximum/zero-return transform shows that its origin specialization does not state or imply the full arbitrary-spatial-level formula absent an additional spatial hitting calculation. Comparisons with related probability identities did not identify a directly covering theorem. Older or broader moment formulas may implicitly encompass this spatial profile; independent historical-priority assessment has not been performed.

## Mathematical value — PASS

Brownian span describes the spatial footprint of an entire trajectory; point local time describes occupation intensity at one spatial location. The theorem resolves their dependence as an exact deterministic function of the spatial level, including a countervailing negative-versus-positive covariance regime and a concrete positive region determined solely by the mean span. This is a motivated structural property of the Brownian occupation-density field, with a natural conservation check from the occupation-time formula. Neither a new general joint-distribution theorem nor a claim of unique crossing is needed for the exact spatial first-moment result to be informative.

## Limits and residual priority risk

The spatial crossing count is not classified; discrete approximations or finite numerical checks cannot certify it. Normalization and drift assumptions are essential. Historical sources concerning joint extremes and local time may imply formulas after unrecorded integration; the inspected sources do not resolve every possible historical route.

Self-review: passed. Independent audit: not yet performed.
