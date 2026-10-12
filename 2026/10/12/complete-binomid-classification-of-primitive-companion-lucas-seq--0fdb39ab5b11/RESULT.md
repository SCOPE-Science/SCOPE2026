# Complete binomid classification of primitive companion Lucas sequences

## Finding
For coprime integer parameters \(P,Q\), with \(P\ne0\), consider the companion Lucas sequence \(V_0=2\), \(V_1=P\), \(V_{n+2}=PV_{n+1}-QV_n\). If its terms are all nonzero, form the generalized binomial coefficients
\[
{n\brack k}_{V}=\frac{V_nV_{n-1}\cdots V_{n-k+1}}{V_1V_2\cdots V_k}\qquad(0\le k\le n),
\]
with the empty product equal to \(1\). The sequence is **binomid** when all these rational numbers are integers. The complete classification is
\[
\boxed{V\text{ is binomid}\quad\Longleftrightarrow\quad (|P|,Q)\in\{(1,0),(1,1),(2,1)\}.}
\]
Every listed sequence is also a divisibility sequence: for all positive integers \(m,n\), \(m\mid n\) implies \(V_m\mid V_n\). In fact the absolute values of its terms are, respectively,
\[
|V_n|=1,\qquad |V_n|=\begin{cases}2&3\mid n,\\1&3\nmid n,\end{cases}\qquad |V_n|=2.
\]
All six choices of the sign of \(P\) are included. No claim is made about companion sequences with \(\gcd(P,Q)>1\), nor about general second-order recurrence initial conditions.

## Assumptions and scope
The parameters \(P,Q\) range over all integers satisfying \(P\ne0\) and \(\gcd(P,Q)=1\). Integrality and nonzero conditions refer to every positive index, not only the first tested indices. The definition of binomid follows the generalized factorial quotients introduced in the cited 2023 article. Multiplying every sequence term by one common nonzero integer does not change its generalized binomial coefficients; replacing \(P\) by \(-P\) changes each \(V_n\) by \((-1)^n\), which can only affect a coefficient by a sign.

## Proof
Write \(V_n=V_n(P,Q)\). If \(V\) is binomid, its coefficient \({2\brack1}_{V}=V_2/V_1\) is integral. Since \(V_2=P^2-2Q\), this yields \(P\mid2Q\). Coprimality forces \(|P|\mid2\), so \(|P|=1\) or \(2\). The identity \(V_n(-P,Q)=(-1)^nV_n(P,Q)\) allows us to take \(P>0\).

**Case \(P=1\).** Direct recurrence gives
\[
V_1=1,\quad V_2=1-2Q,\quad V_3=1-3Q,\quad V_4=1-4Q+2Q^2.
\]
The coefficient \({4\brack2}_V=V_4V_3/(V_2V_1)\) is integral. Because
\[
\gcd(V_2,V_3)=\gcd(1-2Q,Q)=1,
\]
we obtain \(V_2\mid V_4\). The identity \(V_4=V_2^2-2Q^2\) and \(\gcd(V_2,Q)=1\) imply \(V_2\mid2\). As \(V_2=1-2Q\) is odd, it follows that \(|1-2Q|=1\), whence \(Q\in\{0,1\}\).

**Case \(P=2\).** Coprimality makes \(Q\) odd. Every \(V_n\) is even, so let \(W_n=V_n/2\). This scaling leaves every generalized binomial coefficient unchanged. The recurrence gives
\[
W_1=1,\quad W_2=2-Q,\quad W_3=4-3Q,\quad W_4=8-8Q+Q^2.
\]
Here \(W_2\) is odd and \(\gcd(W_2,W_3)=\gcd(2-Q,2)=1\). Integrality of \({4\brack2}_{W}\) implies \(W_2\mid W_4\). Modulo \(W_2\), one has \(Q\equiv2\) and \(W_4\equiv-4\). Thus \(|2-Q|\mid4\); its oddness forces \(|2-Q|=1\), so \(Q=1\) or \(3\). The last possibility is ruled out at the third binomial level: for \(P=2,Q=3\), the normalized values are
\[
(W_1,W_2,W_3,W_4,W_5,W_6)=(1,-1,-5,-7,1,23),
\]
which give
\[
{6\brack3}_{W}=\frac{23\cdot1\cdot(-7)}{(-5)\cdot(-1)\cdot1}=-\frac{161}{5}\notin\mathbb Z.
\]
Consequently the only possible binomid pairs are the three listed. A separate necessity check for ordinary index divisibility gives the same list: divisibility forces \(V_1\mid V_2\) and \(V_2\mid V_4\), which are exactly the first two restrictions above (without needing the binomid hypothesis), so again only \(Q=0,1\) with \(|P|=1\), or \(Q=1,3\) with \(|P|=2\), survive. In the remaining \((P,Q)=(2,3)\) case, \(V_3=-10\) and \(V_6=46\), so \(V_3\nmid V_6\) even though \(3\mid6\). The negative-\(P\) case has the same divisibility status. Hence no excluded primitive companion is a divisibility sequence.

For sufficiency, \((P,Q)=(1,0)\) gives \(V_n=1\) for all positive \(n\), and \((2,1)\) gives \(V_n=2\). Both are trivially binomid and divisible. For \((1,1)\), the recurrence generates a six-periodic sequence
\[
(V_1,V_2,V_3,V_4,V_5,V_6)=(1,-1,-2,-1,1,2),
\]
and the next two terms repeat the first two, proving six-periodicity by the recurrence. Hence \(|V_n|=2\) exactly when \(3\mid n\). Every interval of \(k\) consecutive positive indices contains at least \(\lfloor k/3\rfloor\) multiples of \(3\), whereas \(1,\dots,k\) contains exactly that many. Therefore the exponent of \(2\) in every generalized binomial quotient is nonnegative, proving integrality, irrespective of signs. Divisibility follows because if \(3\mid m\) and \(m\mid n\), then \(3\mid n\); otherwise \(|V_m|=1\). The sign change \(P\mapsto-P\) preserves integrality and divisibility. This proves necessity and sufficiency for every parameter and index in the stated domain.

## Verification
The accompanying exact-rational Python verifier checks the three decisive coefficient positions \((n,k)=(2,1),(4,2),(6,3)\) throughout a finite coprime parameter box, and rechecks every generalized binomial coefficient through \(n=55\) for all six accepted sign choices. It also checks divisibility at those indices and the excluded normalized witness \(-161/5\). These finite computations are reproducibility tests; the unrestricted theorem is proved symbolically above.

## Relationship to prior work
D. B. Shapiro's *Divisibility Properties for Integer Sequences* (arXiv:2302.02243, first submitted February 4, 2023) defines binomid sequences, proves that the usual Lucas \(U\)-sequences with zero initial term are binomid at every level, and specifically asks which order-two recurrences with nonzero initial term are binomid and whether binomidness then implies divisibility (Section 4.4, Open Questions 27). The present classification treats the natural coprime-parameter companion \(V\)-family, whose initial term is \(2\), rather than the Lucas \(U\)-family. Shapiro's divisibility classifications do not themselves establish the necessity of binomidness in this family. The case \(Q=0\) is an elementary degenerate branch and is included for completeness, not claimed as a separate advance.

## Limitations
The result does not resolve Shapiro's question for all nonzero-initial-condition second-order recurrences, nor for nonprimitive companion pairs. The nearest indexed related mathematical records address different invariants of companion Lucas sequences, especially local realizability, rather than integral generalized factorial ratios. Equivalence with an unindexed prior special-family classification remains possible; no independent audit has been conducted.

## References
1. D. B. Shapiro, *Divisibility Properties for Integer Sequences*, arXiv:2302.02243v1 (2023), Sections 1, 4.3, 4.4 and Open Questions 27; publicly available author manuscript: https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/c/5162/files/2023/02/Divisibility_Properties.pdf.
2. A. Granville, *Classifying linear division sequences*, arXiv:2206.11823 (2022); relevant background on divisibility recurrences, not an asserted proof of the binomid classification.
