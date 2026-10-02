# Review status

Independent audit completed on 2026-10-01 UTC.

Disposition: **passed**.

## Correctness — PASS

For a one-bit flip, the exact objective gap reduces to a quadratic column-norm term plus a Gaussian inner product. Conditional on the common noise vector, the channel columns are independent, so the improvement indicators are iid Bernoulli. Uniform chi-square concentration for both the noise norm and a fresh column norm is strong enough on the \(1/N\) tail scale because \(N^{-1/4}\log N\to0\). Mills’ ratio gives \(NQ(\sqrt{2\log N-\log\log N+c})\to e^{-c/2}/(2\sqrt{\pi})\), and the conditional binomial law therefore converges to Poisson. Each gap changes sign at most once as \(\rho\) increases, so the zero-count probability gives the Gumbel threshold. The minimax lower bound follows from the uniform-prior MAP argument.

## Originality — PASS

Papailiopoulos states a one-bit ML converse only below \(2\log N-\log\log N-s_N\) for diverging \(s_N\), while the audited claim resolves the constant window and its limiting count law. Hu–Lu’s Poisson/Gumbel theorem concerns errors of the box-relaxation decoder, a different statistic and threshold. Resultary did not surface an earlier SCOPE claim implying this exact Hamming-one Poisson law.

## Value — PASS

The exact constant-width transition and limiting law sharpen a natural first-order ML threshold obstruction and quantify the probability of local instability precisely where the motivating result leaves a lower-order gap. The result also cleanly separates what one-bit competitors explain from what any unresolved multi-bit obstruction must supply.

## Sources and residual risk

Assigned package and both committed simulation files inspected from the frozen Git tree.; Papailiopoulos abstract inspected; full text unavailable after lawful attempts.; Hu–Lu abstract/bibliographic record inspected.

Residual risk: Near-simultaneous or folklore derivations remain possible because the conditional-independence proof is short and the motivating preprint is very recent..

The dated independent-audit files contain the structured claim-versus-prior comparison and full evidence record.
