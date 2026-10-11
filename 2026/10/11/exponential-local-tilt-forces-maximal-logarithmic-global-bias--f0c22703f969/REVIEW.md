# Review: Exponential local tilt forces maximal logarithmic global bias


## Correctness
PASS. The proof reconstructs the exact quantifiers and normalizations. Exponential tilt at discrepancy levels \\(k/2\\) produces staircase occupation ratio \\(e^{{(t/2)(k-\\ell)}}\\), so Theorem 1.25 gives pressure parameter \\(t/2\\). Proposition 8.9 gives \\(P_n'(0)=O(1)\\); Proposition 8.10 and Lemma 11.5 give \\(P_n''\\asymp n\\) uniformly on the bounded interval traversed by the convergent pressure parameters. The mean value theorem then forces the renormalized height to have fixed sign and linear magnitude. Theorem 4.5 transfers this to the continued-fraction sign sum, and Theorems 1.9--1.10 transfer it to the temporal central-limit centering. No experiment is substituted for proof.

## Originality
PASS. The closest source, arXiv:2609.33590v1, proves only the qualitative implication from local bias to global bias for general bounded type, while separately proving exponential tilt, pressure genericity, the twist formula, and the Beck centering formula. It does not state that nonzero exponential tilt forces eventual linear sign drift or maximal-order logarithmic centering. In the quadratic case a linear sign drift is already classical because the even continued fraction is eventually periodic; the new scope is the full bounded-type exponential-tilt class, including nonquadratic examples. The 2015 staircase paper was inspected for its quadratic-renormalizable central-limit and generic-point results and does not provide this arbitrary bounded-type implication.

## Value
PASS. The conclusion is a structural strengthening rather than a routine restatement: it separates the strength of exponential local bias from generic local/global bias, pins down the sign of the global displacement, and shows that the center reaches the largest order allowed by the general \\(O(\\log n)\\) theorem. This contrasts with the source's explicitly slower globally biased example and gives a quantitative hierarchy of bias mechanisms.

## Closest literature and limitations
The closest literature is Dolgopyat--Sarig (2026), which contains all required ingredients but states only qualitative local/global-bias implications, and Avila--Dolgopyat--Duryev--Sarig (2015), which treats a renormalizable quadratic setting. The result does not identify a limiting constant for \\(A_n/\\log n\\), and an equivalent formulation could exist in older literature under cocycle or pressure terminology.

Same-model review: passed. Independent audit: not yet performed.
