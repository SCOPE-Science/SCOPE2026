# Scientific review of the strict-unimodality finding

## Correctness — PASS

For positive Poisson intensity and the stated two-atom jump law, the cumulant generator and true variance give the exact scalar objective. Its derivative numerator has coefficient sequence \(T_4=T_5=0\), \(T_6,T_7>0\), and \(T_n<0\) for every \(n\ge8\): the finitely many small coefficients are given exactly, while the infinite tail follows from a stated positive induction. Dividing by \(t^7\) yields a strictly decreasing function crossing zero once, proving the asserted full unimodality and uniqueness. The program verified the rational endpoint signs and its other tests passed. No finite enumeration substitutes for the all-index proof.

## Originality — PASS, subject to historical priority

Chen's arXiv:2610.00032v1 establishes the full variational framework and uses these same two masses and support points, but explicitly leaves the interior maximizer's uniqueness unproved in Section 7.2. The present claim adds a rigorous all-positive-argument shape theorem and an exact isolating interval, rather than merely reproducing the existing numerical estimate. Targeted comparisons against available mathematical research records and the source's actual theorem/section found no equivalent statement. A general earlier theorem on the uniqueness of maxima of moment-generating-function ratios might indirectly imply this special case and has not been ruled out universally.

## Mathematical value — PASS

Variance-exact sub-gamma bounds have a mathematically natural one-dimensional optimization, and the source's canonical bounded-jump example exhibits the nontrivial interior regime. Resolving uniqueness for exactly that published example establishes whether the reported sharp concentration scale has an unambiguous determining saddle point, not just a numerical candidate. Strict unimodality is stronger than the missing uniqueness fact. The claim intentionally does not overreach to arbitrary jump mixtures, nor assert a new general concentration theorem.

## Closest literature and limits

Closest direct source: Y. Chen, *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws*, arXiv:2610.00032v1 (2026), Theorem 3.1 and Section 7.2. General power-series sign arguments are classical and are used as proof technique rather than an independently new lemma. The scope is restricted to the two-atom jump law and strictly positive compound Poisson intensity; historical priority remains subject to further independent review.

Self-review: passed. Independent audit: not yet performed.
