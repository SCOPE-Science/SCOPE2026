# Scientific review

## Correctness — PASS

The density formula is obtained by convolution for \(X=aE_1+bE_2-(a+b)E_3\), including its continuous boundary cases. A derivative identity converts its apparent signed exponential difference to a strictly positive combination of exponential and exponential-times-linear kernels. Direct integration supplies positive weights for the Gamma factors \(2^{s/2}\Gamma(1+s/2)r^s\) and \((s+1)2^{s/2}\Gamma(1+s/2)r^s\). The trigamma-series lower bound proves positive logarithmic curvature for both factors for all real \(s\ge2\), and Hölder preserves log-convexity under the mixture. The variance-normalized moment lower bound in [1, Theorem 1], whose hypotheses are satisfied, yields strict monotonicity of the Gaussian-normalized norms. Boundary weights \(a=b\) and \(b=0\) are addressed by continuous limits. The embedded script independently checks 2,647 exact-rational and numerical assertions; numerical checks do not replace the continuum proof.

## Originality — PASS, with residual priority risk

The lead paper [1, Section 4.2] explicitly asks for the two-order Gaussian comparison and proposes the stronger moment-quotient log-convexity conjecture. Its existing one-order inequality is weaker, and its Gaussian-mixture argument covers paired opposite coefficients, not a genuinely asymmetric triple. The closest detailed treatment of centered three-exponential sums is [2, Proposition 5.3], which determines coefficient extrema at fixed moment order and gives a classical interpolation formula; its full mathematical comparisons do not yield a log-convexity assertion across orders. The negative-moment and \(L_1\)-normalized results in [3] have different comparison hypotheses. Literature and public-result searches did not identify a theorem covering the present claim. General analytic positivity mechanisms or earlier unindexed literature could still affect priority.

## Value — PASS

The full continuum \(2\le p<q\) is resolved for the first asymmetric finite-dimensional instance of a current explicit conjecture. The positive exponential/Gamma-moment decomposition gives a structural explanation of why normalized moments have positive curvature. This is more substantive than isolated finite experiments or a routine fixed-order bound and supplies a method for investigating larger sign-patterned sums.

## Limits

No conclusion is proved for four or more exponentials, nonzero-mean comparisons, powers below two, or general underlying distributions. Exact unindexed priority remains uncertain.

Self-review: passed. Independent audit: not yet performed.

## Sources

[1] https://arxiv.org/html/2602.03058v1 (Theorem 1, Section 4.2)

[2] https://arxiv.org/pdf/2512.12254 (Sections 2.5 and 5, Proposition 5.3)

[3] https://arxiv.org/pdf/2505.00944 (Theorems 1 and 2)
