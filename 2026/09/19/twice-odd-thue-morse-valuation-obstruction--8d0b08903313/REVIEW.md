# Review: explicit 2-adic obstructions for twice-odd Thue-Morse powers

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** Let `N=2^A` with `A>=2`, let `v` be odd, and put `m=2+Nv`. The proof is an exact 2-adic argument. It uses the known valuation theorem for coefficients of `T(x)^N`, the functional equation `T(x)=(1-x)T(x^2)`, the exact `m=2` recurrences, and elementary binomial arithmetic.

For `1<=i<N`, writing `[x^i]T(x)^(Nv)=r_i`, the proof establishes
`nu_2(r_i)=A-nu_2(i)`. The linear term from the odd power has this exact order, while every nonlinear convolution has at least one extra factor of 2. This prevents cancellation at the leading 2-adic order.

Comparing `T(x)^(2+Nv)` with `T(x)^2` then gives two bounds needed at the dyadic boundary. Below `N/2-1`, each coefficient difference has two spare powers of 2 relative to its `m=2` valuation. At `N/2-1`, all convolution summands have exact order `A`, and their number is odd, yielding the required nonzero endpoint correction modulo `2N`.

The final boundary coefficient is reduced to
`[x^(N-1)](1-x)^(Nv)T(x)^2`. Pairing the terms indexed by `k` and `N-k` modulo `4N`, together with `t_2(2h)=(-1)^h (mod 4)`, cancels every noncentral pair. The two unpaired terms give the stated congruence
`t_m(N-1)=N(v-1) (mod 4N)`.

At the same index, the binary digit-sum formula gives
`nu_2 binom(N(v+1),N-1)=A+nu_2(v+1)`. The two odd residue classes of `v` modulo 4 force opposite valuation inequalities, so equality is impossible.

The exact-integer verification independently recomputes the relevant coefficients for 112 `(A,v)` pairs with `2<=A<=8` and odd `1<=v<=31`, and for every odd `u` from 3 through 255. All checks pass. The computation is corroborative; the proof is complete without it.

## Originality

**PASS, to the best of our knowledge.** Zhao Shen's arXiv:2609.16966v1 states Conjecture 6.2 as an open necessary-and-sufficient criterion. In the layer `r=1`, that conjecture says that the all-index binomial valuation identity holds only for `m=2`. Shen proves the first excluded example `m=6`, but does not give the arbitrary twice-odd obstruction or the explicit witness index
`2^(nu_2(u-1)+1)-1`.

The earlier Gawron-Miska-Ulas work gives the exact power-of-two valuation theorem used here, but does not state the classification for all exponents `m=2u` with `u` odd. Ulas's later general paper on 2-adic valuations of powers of integer-coefficient series does not, in its available description, state this Thue-Morse boundary congruence.

Searches covered equivalent formulations involving `t_(2u)`, twice-odd exponents, exact binomial valuations, the boundary index `2^A-1`, and recent follow-up work on arXiv:2609.16966. No stronger theorem implying the result was located. No inaccessible source was identified whose title or available metadata specifically suggests the same result. The main residual risk is unindexed contemporaneous work because the motivating preprint is very recent.

## Value

**PASS.** The result settles the full infinite `r=1` layer of a newly stated necessary-and-sufficient conjecture. Every excluded exponent with exactly one factor of 2 receives a closed-form witness index, and the stronger modulo-`4N` congruence explains why the obstruction changes according to the odd parameter modulo 4. This is a uniform theorem, not a finite extension of the known `m=6` example.

## Limitations

The theorem settles only the `r=1` slice of Conjecture 6.2. It does not prove either direction for general `r>=2`, and it does not address the separate automatic-odd-parts conjecture. When `v=1 (mod 4)`, the boundary congruence gives a lower bound on the coefficient valuation rather than a complete formula. Originality remains to the best of our knowledge, with elevated residual uncertainty because the motivating preprint is recent. No independent validation or formal proof-assistant verification has been performed.
