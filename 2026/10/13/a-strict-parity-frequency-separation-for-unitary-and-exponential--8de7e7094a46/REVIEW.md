# Scientific review: parity-frequency separation

## Correctness — PASS
The proof addresses every positive integer by separating the conditional odd and even populations and using exact multiplicative prime-power formulas. For odd inputs, the indicated \(18058\) finite valuation vectors have ratio greater than one (or are the all-zero vector), while squarefree prime factors above \(19\) cannot decrease the ratio. A convergent squarefree-tail Euler product gives the certified conditional lower frequency. The exceptional input \(1\) has density zero. The exact rational lower bound exceeds \(17/20\).

For even inputs, the \(32591\) selected finite valuation vectors have ratio strictly below \(11/12\) before primes above \(19\) are included. A uniform \(100\)-th-moment estimate for the remaining prime-factor product excludes all but less than \(1/70\) of each selected cylinder from being guaranteed strict failures. Exact rational finite products and a convergent large-prime remainder bound establish the inequality over arbitrarily large inputs. The resulting conditional failure frequency exceeds \(897/3500>1/4\). The attached standard-library checker recomputes all exact rational components. Neither finite enumeration alone nor sampled ratios are treated as infinite proofs.

## Originality — PASS, residual risk acknowledged
Trudgian's 2013 paper directly poses the overall density question and supplies a squarefree lower bound, but not conditional odd/even estimates. The published \(0.753659844\ldots\) bound is an overall lower frequency, not a parity separation; the logical information in one unconditional average cannot force either conditional bound. The numerical counts in OEIS A322446 are finite experiments. Related exponential-divisor mean-value and inequality papers treat different claims. Targeted published-finding corpus searches for the comparison, parity, conditional densities and aliases did not retrieve a covering result. An unindexed proof or a stronger theorem whose implication has not been recognized remains possible; no formal global novelty certification is asserted.

## Value — PASS
The original literature requests information on how often the inequality holds; the new result proves a strict difference exceeding ten percentage points between odd and even asymptotic frequencies. The phenomenon is not implied by existing overall-density bounds. The parity contrast is structural and applies over an unrestricted infinite domain, with separate exact certificates for both sides. It is meaningful without determining either exact conditional density or the full overall density.

## Limitations
The constants \(17/20\) and \(3/4\) are certified bounds, not claimed optimal. The proof does not establish existence or formulas for the separate limiting frequencies; it bounds their lower and upper limits. Any inaccessible or unindexed stronger published result is an originality risk.

Self-review: passed. Independent audit: not yet performed.
