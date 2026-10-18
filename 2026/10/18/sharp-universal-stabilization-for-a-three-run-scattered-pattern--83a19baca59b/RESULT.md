# Sharp universal stabilization for a three-run scattered-pattern frequency

## Finding
For integers \(s,t,k\ge1\), let \(p=0^s1 0^t\) and let \(B_{s,t}(n,k)\) count binary words of length \(n\) with exactly \(k\) occurrences of \(p\) as an order-preserving, not necessarily contiguous, subsequence. Write \(d=s+t-1\). For each integer \(A\) in \([s+t,s+t+k-1]\) define \(w_{A,i}=\binom{i}{s}\binom{A-i}{t}\) for \(s\le i\le A-t\), and let \(\mathcal C_A(k)\) be the finite set of nonnegative integer vectors \((c_i)_{i=s}^{A-t}\) with \(\sum_i w_{A,i}c_i=k\). Put \(h(c)=\sum_i c_i\) and \(M(A,c)=A+h(c)\). Then the **entire length enumerator** is
\[
\sum_{n\ge0}B_{s,t}(n,k)z^n
=\frac{1}{(1-z)^{s+t}}\sum_{A=s+t}^{s+t+k-1}z^A\,[u^k]\prod_{i=s}^{A-t}\frac{1}{1-zu^{w_{A,i}}}
=\frac{\sum_{A,c\in\mathcal C_A(k)}z^{M(A,c)}}{(1-z)^{s+t}}.
\]
(The last sum means \(A\) in the indicated interval and \(c\in\mathcal C_A(k)\).) Define the ordinary degree-\(d\) polynomial
\[
P_{s,t,k}(x)=\sum_{A,c\in\mathcal C_A(k)}\binom{x-M(A,c)+d}{d},\qquad
\binom{y}{d}=\frac{y(y-1)\cdots(y-d+1)}{d!}
\]
for arbitrary \(y\), including negative integers. Then **for every integer \(n\ge k+1\)** one has \(B_{s,t}(n,k)=P_{s,t,k}(n)\), independently of the sizes of the two outer runs. The threshold is **sharp for every choice of the three positive parameters**:
\[
P_{s,t,k}(k)-B_{s,t}(k,k)
=(-1)^{s+t-1}\Big(1+\mathbf1_{k\ge2}(\mathbf1_{s=1}+\mathbf1_{t=1})\Big)\ne0.
\]
The polynomial degree is exactly \(s+t-1\), with positive leading coefficient \(\big(\sum_A|\mathcal C_A(k)|\big)/(s+t-1)!\).

## Assumptions and scope
All three integers \(s,t,k\) are positive. Only the binary alphabet is considered, and distinct embeddings of the fixed pattern in the same word are counted separately. The enumeration includes the empty input word at \(n=0\), with zero counted words because \(k>0\). The polynomial extension of \(\binom{y}{d}\) is different from the ordinary combinatorial binomial \(\binom{m}{d}=0\) for \(m<d\) when \(m\) is nonnegative. No assertion is made for frequency \(k=0\) or for patterns with a different number of alternating runs.

## Proof
**Gap formula.** A binary word with \(A\) zeroes has a unique representation \(1^{b_0}0 1^{b_1}0\cdots 0 1^{b_A}\), where all \(b_i\ge0\). A one from gap \(i\) has exactly \(i\) earlier and \(A-i\) later zeroes; selecting \(s\) earlier zeroes and \(t\) later zeroes yields \(w_{A,i}=\binom{i}{s}\binom{A-i}{t}\) embeddings of \(p\). The total number is \(\sum_i w_{A,i}b_i\). Exactly \(s+t\) gaps have weight zero: the first \(s\) and the final \(t\). Therefore, after fixing \(A\) and the active vector \(c\), the inactive gap counts are independent and contribute \((1-z)^{-(s+t)}\), while the active gaps contribute the product displayed in the finding.

**Finite range of zero counts.** If a word has positive frequency, it has \(A\ge s+t\) zeroes and at least one active one. Set \(u=A-s-t+1\ge1\). For the active gap \(i=s+j\), where \(0\le j<u\),
\[
 w_{A,s+j}=\binom{s+j}{s}\binom{t+u-1-j}{t}
 \ge (j+1)(u-j)\ge u.
\]
Consequently, if the total frequency is \(k\), then \(u\le k\), proving \(A\le s+t+k-1\). This proves the finite rational generating function without any asymptotic hypothesis.

**Bound on the numerator support.** Write \(h=\sum_i c_i\ge1\). The same weight inequality gives \(uh\le k\). Since \((u-1)(h-1)\ge0\), we also have \(u+h\le uh+1\le k+1\). Thus every numerator exponent satisfies
\[
M(A,c)=s+t-1+u+h\le s+t+k.
\]
Its contribution to the length-\(n\) coefficient is \(\binom{n-M+d}{d}\) if \(n\ge M\), and zero otherwise, by the binomial series for \((1-z)^{-(d+1)}\). If \(n\ge k+1\), the upper argument satisfies \(n-M+d\ge0\). Whenever \(n<M\), this argument lies in \(\{0,\ldots,d-1\}\), making the generalized binomial polynomial zero as required. Every summand therefore agrees with its polynomial continuation for all \(n\ge k+1\).

**Sharpness and exact jump.** At \(n=k\), only terms attaining the maximum exponent \(M=s+t+k\) can differ from their combinatorial coefficients: their binomial upper argument is \(-1\), and \(\binom{-1}{d}=(-1)^d\). Equality in the bound on \(M\) requires \(uh=k\) and \((u-1)(h-1)=0\). If \(u=1\), then the unique active gap has weight one and contains \(h=k\) ones; this always yields one extremal numerator term. If \(h=1\), then \(u=k\) and exactly one active gap has weight \(k\). For \(k\ge2\), an interior gap has weight at least \((j+1)(k-j)>k\) for \(1\le j\le k-2\). The initial active gap has weight \(\binom{t+k-1}{t}\), equal to \(k\) precisely when \(t=1\); the last has weight \(\binom{s+k-1}{s}\), equal to \(k\) precisely when \(s=1\). These are distinct for \(k\ge2\). For \(k=1\), the \(h=1\) case is the same as the already counted \(u=1\) case. The number of maximum-exponent summands is consequently \(1+\mathbf1_{k\ge2}(\mathbf1_{s=1}+\mathbf1_{t=1})\), proving the claimed nonzero jump.

**Exact degree.** All numerator coefficients are nonnegative integers. There is at least one summand, namely the \(A=s+t\) configuration with \(c_s=k\), so the coefficient of \(x^d\) in \(P\) is strictly positive and equal to the total number of enumerated active configurations divided by \(d!\). This concludes the proof.

## Verification
The included standalone Python checker builds the finite numerator independently from all active-gap solutions and enumerates all binary words of lengths \(0\) through \(12\). It verifies exact occurrence counts and generating-function coefficients for \(1\le s,t\le3\) and \(1\le k\le6\) (702 parameter-length cases), together with nonzero sharp-threshold discrepancies in 54 parameter triples. Its direct subsequence counter is a right-to-left dynamic program distinct from the gap-weight enumerator. Finite checks corroborate but do not replace the above proof.

## Relationship to prior work
Menon and Singh, *Subsequence frequency in binary words* (first public June 2023), give explicit frequency counts for \(k\le4\) and study maxima for patterns of at most three runs. The present assertion for \(k\le4\) must not be counted separately as novel. Bruda, *Enumerating binary words restricted by subsequence frequency* (first public June 30, 2026), proves eventual polynomiality for all \(k>0\) and patterns of at least two runs, with a degree bound and a sufficient equality condition. Because the present three-run pattern has an internal singleton, its polynomial degree was already implied by Bruda. The distinct assertions here are the explicit finite coefficient formula for **every** \(k\), the universal **sharp** onset \(n=k+1\), and the exact discrepancy at \(n=k\). Bruda's inspected general theorem and proofs do not state that threshold or discrepancy. The formulas do not follow from an asymptotic eventual-polynomial claim alone.

## Limitations
The theorem is confined to patterns with a single middle symbol and positive frequency. The original polynomial-degree claim is not new; it is included solely for completeness of the enumerator. A differently expressed weighted-gap identity in other literature could dominate the explicit formula or its cutoff; current literature comparisons do not prove global uniqueness. Exhaustive computation was only through length \(12\); all infinite assertions depend on the mathematical argument. No independent scientific validation has been performed.

## References
- Glenn Bruda, *Enumerating binary words restricted by subsequence frequency*, arXiv:2607.02578, first submitted 2026-06-30, https://arxiv.org/abs/2607.02578.
- Krishna Menon and Anurag Singh, *Subsequence frequency in binary words*, arXiv:2306.07870, first submitted 2023-06-13, https://arxiv.org/abs/2306.07870.
- Mathematical Reviews MSC2020, 68R15, *Combinatorics on words*, https://mathscinet.ams.org/msc/msc2020.html?btn=Current&t=68R15.
