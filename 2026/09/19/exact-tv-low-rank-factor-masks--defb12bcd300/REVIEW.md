# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The argument was checked at three levels.

First, conditioning on rank(U)=s gives the exact point probability by choosing the image s-subspace, requiring it to contain the target column space, and counting the q^{r-s} preimages of each target column. This yields the stated Gaussian-binomial formula.

Second, the likelihood ordering by target rank follows because, for each s shared by ranks d and d+1, the number of s-subspaces containing a fixed d-subspace is at least the number containing a fixed (d+1)-dimensional extension (strict unless s=k), while rank d has the additional positive s=d contribution. Hence the point mass is strictly decreasing in target rank.

Third, the sign change relative to the uniform law was checked explicitly. Full-row-rank targets have likelihood ratio p_{k,r}<1. For deficient targets, the rank-(k-1) contribution alone has likelihood ratio at least q^{n-r}p_{k-1,r}>1 under k<=r<n. Therefore no hidden deficit exists among deficient ranks, and summing the full-rank deficit gives exactly p_{k,n}(1-p_{k,r}).

The transfer to individual security uses the same uniform-input translation argument as the motivating paper: the joint-vs-product total variation for (A_T,X) equals the distance between R_T and uniform. Since R_T=U_TV with U_T uniform k-by-r, the product theorem applies directly. The asymptotic threshold follows from elementary product bounds.

The finite verifier exhaustively checked six small prime-field parameter sets and 322,377 factor pairs, including nontrivial k=2 cases, with exact rational arithmetic.

## Originality

**PASS, to the best of our knowledge.** The motivating preprint arXiv:2609.18876 proves only

d_TV <= 1-p_{k,r} <= q^{k-r}/(q-1)

for Low-Rank Factors. Its proof obtains the first inequality by conditioning on U_T having full row rank; it does not determine the signs of the remaining pointwise deviations or state the exact distance p_{k,n}(1-p_{k,r}).

Searches were performed for the motivating arXiv identifier and title together with exact total variation, product-of-random-matrices distributions, finite-field matrix products, rank distributions, low-rank masking, individual security, and equivalent p_{k,n}/p_{k,r} formulations. Standard literature on finite-field random-matrix rank and matrix factorization was also inspected. The older k-good-random-matrix literature concerns uniformity properties under multiplication by fixed full-rank matrices and does not supply this product-mask individual-security identity. No prior source located in this search states the exact total-variation formula or the iff rank-surplus threshold in the masking model.

The rank-conditioned point-mass formula is a short consequence of standard counting and may well be folklore in random finite-field matrix theory. Accordingly, novelty is not claimed for generic factorization counting in isolation. The originality claim is restricted to the exact TV identity in the Low-Rank Factors regime, the identification of the full-rank set as the entire TV deficit set, and the resulting sharp individual-security threshold. Because the motivating preprint is recent and the argument is concise once the sign structure is noticed, near-simultaneous or folklore priority risk remains material.

No inaccessible paper found in the targeted search produced concrete evidence of prior coverage. The main residual originality risk is uncatalogued folklore or a random-matrix-product result phrased without the privacy terminology.

## Value

**PASS.** The result converts an approximate achievability bound into an exact leakage law and matching converse. It shows that the published q^{k-r} security exponent is not merely an artifact of a union/coupling bound: it is the true scale. The iff criterion r-k->infinity is operationally informative, and the k=r example exhibits a constant leakage floor even as mask rank grows.

## Limitations

The theorem is specific to independent uniform factors and uniform inputs. It does not determine the exact TV leakage of rank-ball masks or arbitrary mask distributions, and it does not replace the motivating paper's maximal-correlation analysis. The published finite verification covers prime fields only; the proof itself applies to every prime-power field because it uses only finite-field subspace counts.
