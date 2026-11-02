# A two-orbit rigidity theorem for strongly pseudoperfect prime squares

## Finding

For an integer \(n\ge 2\), a *complement orbit* is the set \(\{d,n/d\}\), where \(d\mid n\). This orbit is a singleton when \(d^2=n\). An *omission* is a set of complement orbits whose union of divisors has sum \(\sigma(n)-2n\). Such an omission is equivalent to a strongly pseudoperfect representation: the complementary set of divisors is closed under \(d\mapsto n/d\) and has sum \(2n\).

**Theorem.** Let \(a\ge1\) be an integer and let \(p\ge3\) be an odd prime. For \(n=2^a p^2\), an omission consisting of at most two complement orbits exists **if and only if** \(n=36\). For \(n=36\), the unique such omission consists of the orbit \(\{4,9\}\) and the singleton orbit \(\{6\}\). In particular, there are no zero-orbit or one-orbit omissions anywhere in the family. For every other \(n\) in the family, any strongly pseudoperfect representation (if one exists) omits at least three complement orbits.

The exceptional representation retains the divisors \(\{1,2,3,12,18,36\}\), whose sum is \(72\).

## Assumptions and scope

All divisors are positive, and distinct complementary divisors are counted once each in a two-element orbit. A square-root orbit is counted once, not twice. This distinction matters for even \(a\). The theorem covers exactly the two-prime-support family \(2^a p^2\), with \(a\ge1\) and \(p\) an odd prime, and bounds the number of **orbits** omitted, not the number of individual divisors omitted. It does not assert that every number in this family is strongly pseudoperfect.

## Proof

Put \(A=2^a\), \(B=2A-1\) and
\[
T=\sigma(Ap^2)-2Ap^2=B(p+1)-p^2.
\]
The integer \(T\) is odd, since \(B(p^2+p+1)\) is odd. The three complement orbits containing an odd divisor have weights (sums of their distinct elements)
\[
w_1=1+Ap^2,\qquad w_2=(A+1)p,\qquad w_3=A+p^2.
\]
All other orbits have even weights. They are of two types:

- Outer orbits of weight \(U+Vp^2\), with \(U=2^i\), \(V=2^{a-i}\), \(1\le i\le a-1\), and \(UV=A\). Here \(U,V\ge2\).
- Middle orbits of weight \(pM\). For a two-element orbit \(M=U+V\), where \(U,V\ge2\) are powers of two and \(UV=A\). The only remaining possibility is the singleton middle orbit, available when \(a\) is even, with \(M=\sqrt A\).

Consequently a one-orbit omission must be one of the three odd-weight orbits; a two-orbit omission must contain exactly one odd-weight orbit and one even-weight orbit.

**Excluding the first odd orbit.** For every \(p\ge3\),
\[
w_1-T=A(p^2-2p-2)+(p^2+p+2)>0.
\]
Thus the orbit \(\{1,Ap^2\}\) cannot be omitted in an omission of one or two orbits.

**Excluding all single-orbit omissions.** The equation \(T=w_2\) gives \(p^2-(A-2)p-B=0\). Hence \(q=B/p\) is a positive odd integer with \(pq=B\) and \(p-q=A-2\). For \(q\ge3\), \(pq=q(q+A-2)\ge3(A+1)>B\); for \(q=1\), the equality would imply \(p=B=2A-1\) and \(p-q=2A-2\ne A-2\), a contradiction. The equation \(T=w_3\) gives \(2p^2-Bp-(A-1)=0\). Then \(p\mid A-1\), so \(k=(A-1)/p\ge1\), and \(2p=B+k\ge2A\), contrary to \(p\le A-1\). The parity of \(T\) also excludes zero omissions.

**Odd orbit \(w_2\), even middle orbit.** Equating \(T=w_2+pM\) gives
\[
p^2-(A-2-M)p-B=0,\qquad q=B/p\in\mathbb Z_{>0},\qquad p-q=A-2-M.
\]
If \(a\ge4\), then \(M\le A/2+2\). If \(q\ge5\), this implies \(p=q+A-2-M\ge A/2+1\) and \(pq\ge(5/2)A+5>B\). Thus \(q=1\) or \(q=3\). The case \(q=1\) is impossible because \(p-q=2A-2>A-2-M\). The case \(q=3\) forces \(3M=A+4\). For a two-element middle orbit, \((U-3)(V-3)=5\), forcing \(\{U,V\}=\{4,8\}\). This gives \(A=32\) and \(p=B/3=21\), not a prime. For the singleton orbit, \(M=\sqrt A\) would satisfy \(M^2-3M+4=0\), impossible. When \(a=2\), the only even middle orbit is the singleton \(M=2\), giving \(p^2=7\). When \(a=3\), the only possible middle weight has \(M=6\), giving \(p^2=15\). When \(a=1\) there is no even middle orbit.

**Odd orbit \(w_3\), even middle orbit.** Equating \(T=w_3+pM\) gives
\[
2p^2-(B-M)p-(A-1)=0.
\]
Thus \(k=(A-1)/p\) is a positive integer and
\[
M=2(k-1)p+k+1.
\]
For \(k\ge2\), the right side exceeds \(A=kp+1\), whereas a middle-orbit parameter satisfies \(M\le A\). Thus \(k=1\) and \(M=2\). A two-element middle orbit has \(M\ge4\). For a singleton, \(\sqrt A=2\) gives \(A=4\), \(a=2\), and \(p=A-1=3\). This is the asserted exceptional configuration.

**Odd orbit \(w_2\), even outer orbit.** Write \(A=UV\) with \(U,V\) powers of two at least \(2\). The equation \(T=w_2+U+Vp^2\) becomes
\[
(V+1)p^2-(A-2)p-(2A-U-1)=0.
\]
Consequently \(k=(2A-U-1)/p\) is a positive **odd** integer satisfying
\[
F(k):=k^2+(A-2)k-(V+1)(2A-U-1)=0.
\]
If \(U\ge2V\), direct substitution gives
\[
F(2V-1)=U(1-2V)+4V^2-7V+4\le4-5V<0,
\quad F(2V+1)=U+4V^2+V>0.
\]
The polynomial is strictly increasing for positive arguments, so the sole possible integer root is \(2V\), which is even. If \(U\le V\) and \(U\ge4\), evaluate the original quadratic \(G\) in \(p\):
\[
G(U)=U^2-2UV+3U+1<0,
\qquad G(U+2)=U^2+7U+4V+9>0.
\]
The positive integer root, if any, must be \(p=U+1\). Then \((U-1)V=U^2+5U+4\), so \(U-1\mid10\). Since \(U\ge4\) is a power of two, this is impossible. For \(U=2\), \(G(3)=18-V\ne0\) because \(V\) is a power of two, while \(G(p)=V(p^2-2p-4)+(p^2+2p+3)>0\) for every odd \(p\ge5\). The dichotomy \(U\ge2V\) or \(U\le V\) exhausts powers of two.

**Odd orbit \(w_3\), even outer orbit.** The equation \(T=w_3+U+Vp^2\) becomes
\[
(V+2)p^2-Bp-(A-U-1)=0.
\]
Put \(k=(A-U-1)/p\), a positive odd integer; then
\[
F(k):=k^2+Bk-(V+2)(A-U-1)=0.
\]
When \(V=2\), the original quadratic implies \(4p=4U-1+k\), hence \(p\ge U\); yet \(p\mid U-1\), a contradiction. When \(4\le V\le4U\),
\[
F(V/2-1)=\frac{V^2-2V+16-U(12V-8)}4<0,
\qquad F(V/2+1)=\frac{(V+2)(4U+V+4)}4>0.
\]
The sole possible integer root is \(V/2\), which is even, contrary to \(k\) odd. Finally, when \(V>4U\), the powers-of-two condition gives \(V\ge8U\). Writing \(G\) for the original quadratic in \(p\),
\[
G(2U-1)=8U^2-3UV-5U+V+2<0,\qquad
G(2U+1)=8U^2+UV+11U+V+4>0.
\]
If \(V=8U\), then \(G(2U)=3U+1>0\); if \(V\ge16U\), then \(G(2U)=8U^2-UV+3U+1<0\). Hence in either case the unique positive root lies strictly between consecutive integers. No integral \(p\) exists.

These cases exhaust all omissions containing at most two orbits. For \(a=2\), \(p=3\), the omitted weights \(4+9=13\) and \(6\) sum to \(19=\sigma(36)-72\), producing the claimed omission. All other cases are excluded, so it is unique. \(\square\)

## Verification

The standalone `verify.py` independently enumerates divisor orbits and their weights by integer arithmetic. It compares all omissions of cardinality zero, one or two against the theorem across a finite grid of exponent and prime parameters, including the singleton orbit for square \(n\). The script does not assume the case-by-case proof. Execute `python3 verify.py`; see `VERIFICATION.md` for the scope and limits.

## Relationship to prior work

Wang and Zelinsky, *Strongly Pseudoperfect Numbers* (first posted 2026-09-28; arXiv:2609.36068), study complementary divisor omissions, prove a one-pair classification for \(3\cdot2^a p\), and investigate sparse omissions. They list the exceptional representation of \(36\) but do not state this uniform two-orbit classification for \(2^a p^2\). Their formulation makes counting complement orbits a natural invariant.

Aryan, Madhavani, Parikh, Slattery and Zelinsky, *On 2-Near Perfect Numbers* (arXiv:2310.01305), classify two omitted **individual divisors** in the \(2^a p^2\) family, without the same requirement of complement closure. Their classification is not a classification of at most two complement **orbits**, which can comprise three or four individual divisors. Earlier work on \(2^a p\) concerns a different odd-prime exponent. The OEIS entry A334405 records \(36\) as strongly pseudoperfect, but does not supply the asserted universal uniqueness result.

## Limitations

This result determines only the low-orbit boundary for \(2^a p^2\). It does not classify all strongly pseudoperfect members of this family, all possible larger omission sets, or numbers with other odd-prime exponents. An equivalent low-orbit classification might exist in literature not reached by the searches described in `REVIEW.md`; no exhaustive priority certification is claimed. Finite computation is corroboration, not a substitute for the unrestricted proof. Independent audit has not been performed.

## References

1. Audrey Wang and Joshua Zelinsky, *Strongly Pseudoperfect Numbers*, arXiv:2609.36068 (first posted 2026-09-28), https://arxiv.org/abs/2609.36068; full text https://arxiv.org/html/2609.36068.
2. Vedant Aryan, Dev Madhavani, Savan Parikh, Ingrid Slattery, Joshua Zelinsky, *On 2-Near Perfect Numbers*, arXiv:2310.01305 (2023), https://arxiv.org/abs/2310.01305.
3. OEIS A334405, *Strongly pseudoperfect numbers*, https://oeis.org/A334405.
