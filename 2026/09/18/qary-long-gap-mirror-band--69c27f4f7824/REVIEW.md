# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The proof was checked against the two points where a q-ary argument can fail.

First, from a non-minimal codeword \(c\), an inclusion-minimal proper covered codeword \(u\) is indeed a minimal codeword, hence has weight at most \(n-k+1\). The long-gap assumption places that entire upper bound inside \([d,d+t]\), forcing \(\operatorname{wt}(u)=d\).

Second, on the \(d\) coordinates of \(u\), the ratios \(c_i/u_i\) take only \(q-1\) nonzero values. Pigeonhole therefore gives a scalar cancelling at least \(\lceil d/(q-1)\rceil\) coordinates. The resulting codeword is nonzero, lies in the same local gap window, and is consequently also minimum weight. The support union then has size at most \(2d\), contradicting the target weight.

The explicit \([5,2,2]_q\) family was recomputed directly. Its weight enumerator is
\[
1+(q-1)z^2+2(q-1)z^4+(q-1)(q-2)z^5.
\]
Thus it satisfies \(A_3=0\) and \(k=n-2d+1\) but has \(A_5>0\) for all \(q\ge3\), so it is a genuine counterexample to the unmodified q-ary analogue.

Finite verification independently enumerates representative counterexamples, the ratio-cancellation lemma, and all ternary linear subspaces up to length six.

## Originality

PASS, qualified to the best of our knowledge.

The motivating paper arXiv:2609.20344 was read through its theorem, q-ary discussion, conclusion, and references. It proves the binary mirror band and states that larger alphabets require extra conditions. Its MDS discussion does not supply a counterexample satisfying the local-gap hypothesis. It does not state the long-gap theorem or the \([5,2,2]_q\) family given here.

The residual-code paper arXiv:2509.03337 was inspected through its main bounds and excluded-weight criteria. Those results concern codewords below \(qd/(q-1)\) and do not state the local-gap-to-upper-band implication proved here.

External searches included exact and synonymous formulations involving q-ary mirror bands, vanishing partial weight distributions, minimal/non-minimal codewords, local weight gaps, and Ashikhmin--Barg arguments. No prior statement matching the theorem or explicit counterexample family was found.

The principal residual risk is the extreme recency of arXiv:2609.20344: a near-simultaneous note or a later revision may contain the same observation. Broader minimal-codeword literature may also contain an equivalent ratio-cancellation lemma, although the lemma alone would not constitute the stated weight-distribution theorem.

## Value

PASS.

The result resolves the precise ambiguity left by the motivating note's q-ary discussion in both directions. It shows that the binary theorem really does fail under the same hypotheses for every \(q\ge3\), rather than merely noting that its proof breaks. It also gives a positive q-ary replacement under a natural quantitative strengthening of the local-gap hypothesis, with an explicit alphabet-dependent cancellation term.

## Limitations

The q-ary theorem can be vacuous if the local gap is too short. No sharpness theorem is proved for the long-gap condition or the endpoint. The binary case remains strictly stronger because disjoint-support decomposition removes the extra hypothesis. No independent audit has been performed.
