# Same-model scientific review

## Correctness
PASS. The final claim is a theorem about one precisely defined statistic under an iid independent Gaussian null. The source definition of cross-HSIC and its jackknife studentizer was reconstructed algebraically to obtain
\[
T_n=\operatorname{sgn}(f_2)\frac{(n-2)C}{\sqrt{n(n-1)Q}}.
\]
The Gaussian residual directions are Haar on the centered sphere, giving the ratio representation through \(F(u,v)=P(u\circ v)\). The \(n=3\) calculation is exact. For \(n=4\), an exact rational Jacobian minor is nonzero. For \(n\ge5\), the quartic-root argument proves surjectivity at explicit reciprocal configurations. The submersion theorem then yields the stated tail lower bound and moment divergence. No experiment is used as an infinite proof.

Risk: the theorem intentionally does not claim a matching upper tail, an exact tail exponent, or finiteness below \(n-1\).

## Originality
PASS. The closest direct paper is Shekhar–Kim–Ramdas, which defines this statistic and proves asymptotic Gaussian validity; its inspected linear-kernel section and appendix reduce the statistic for asymptotic analysis but do not state the finite-sample Gaussian denominator geometry, the polynomial tail lower bound, or the infinite high moments. The broader cross-U-statistic paper of Kim–Ramdas concerns asymptotic dimension-agnostic inference. Targeted semantic and web searches for “Gaussian linear cross-HSIC finite-sample moment divergence jackknife denominator singularity,” “cross-HSIC heavy tails infinite third moment Gaussian,” “studentized cross U-statistic denominator zero high moments Gaussian independence,” and “linear-kernel cross-HSIC exact null distribution Gaussian half sample” returned no equivalent statement. The closest indexed record concerned dependence among jackknife pseudovalues rather than cross-HSIC tails.

Risk: classical Studentized-U and ratio-distribution literature is large, and an abstract theorem under different notation could imply part of the mechanism. The \(n=3\) arcsine law is correlation-like and is not claimed separately as the originality-bearing result.

## Value
PASS. The result identifies a concrete finite-sample boundary phenomenon in a statistic proposed specifically to obtain Gaussian calibration: at \(n=3\) it is bounded, whereas from \(n=4\) onward the jackknife denominator admits regular zeros that create polynomial tails and missing high moments even under the cleanest Gaussian null. This matters for understanding which moment-based finite-sample approximations can or cannot be transferred directly to the studentized statistic and supplies an explicit geometric diagnostic for self-normalized cross statistics.

Risk: the missing moments occur at orders growing with \(n\), so the theorem should not be read as evidence that the source asymptotic Gaussian calibration fails at practically large \(n\).

## Closest literature and limitations
The direct source is arXiv:2212.09108 / JMLR 24(369). The broader method source is arXiv:2011.05068 / Bernoulli 30(1). Studentized-U asymptotics were also checked at the level of the accessible primary abstract of arXiv:0906.5101. The result is limited to scalar linear kernels and an independent Gaussian null, and it supplies only a tail lower bound.

Same-model review: passed. Independent audit: not yet performed.
