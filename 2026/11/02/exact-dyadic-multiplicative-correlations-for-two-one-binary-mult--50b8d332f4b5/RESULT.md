# Exact dyadic multiplicative correlations for two-one binary multipliers

## Finding
For integers \(k\ge2\) and \(r\ge0\), write \(s_2(n)\) for binary digit sum, \(\tau(n)=(-1)^{s_2(n)}\), and
\[
C_{k,r}=\sum_{n=0}^{2^r-1}\tau(n)\tau((2^k+1)n).
\]
Then the full ordinary generating function in the dyadic exponent is
\[
\boxed{\sum_{r\ge0}C_{k,r}z^r=1+\frac{2z^{k+2}}{(1-z)(1-z^k+2z^{k+1})}.}
\]
In particular, \(C_{k,0}=1\), \(C_{k,r}=0\) for every \(1\le r\le k+1\), and \(C_{k,k+2}=2\). All subsequent terms obey the order-\(k+2\) recurrence
\[
C_{k,r+k+2}=C_{k,r+k+1}+C_{k,r+2}-3C_{k,r+1}+2C_{k,r},\qquad r\ge0.
\]
The strength is a uniform exact formula for the *infinite family* of multipliers with two ones separated by an arbitrary positive gap of at least two positions. This determines the first nontrivial dyadic correlation level and every later level, not only a limiting average.

## Assumptions and scope
Here \(k\) is any integer at least two, \(r\) is any nonnegative integer, and the sums are over ordinary nonnegative integers. No limiting assumption is imposed. The previously known single instance \(k=1\) (multiplier three) is not included in the new claim. The theorem does not concern all odd multipliers, non-dyadic cutoffs, or weighted correlations.

## Proof
Fix \(k\ge2\), and put \(m=2^k+1\). To multiply a binary input by \(m\) reading low bits first, take a carry \(c\in\{0,1,\ldots,m-1\}\) and input bit \(b\in\{0,1\}\). The next carry is \(d=\lfloor(c+mb)/2\rfloor\). Since \(m\) is odd, the output bit is congruent to \(c+b\pmod2\); the product of the input sign and output sign is therefore \((-1)^c\), independent of \(b\). Define the integer matrix
\[
M_{c,d}=(-1)^c\left(\mathbf 1_{\{d=\lfloor c/2\rfloor\}}+\mathbf 1_{\{d=\lfloor(c+m)/2\rfloor\}}\right).
\]
Let \(e_c\) denote the row basis vector at state \(c\), let \(R_j=e_0M^j\), and let the column vector \(v\) have \(v_c=\tau(c)\). The final carry is the high part of the product, so concatenating its binary bits with the low output bits yields exactly
\[
C_{k,r}=R_r v.
\]
For \(0\le j\le k\), multiplication by \(m\) has no overlap between the two shifted copies of any \(n<2^j\). Thus \(mn=n+2^kn\), the first \(j\) output bits are the bits of \(n\), the carry after reading those bits is \(2^{k-j}n\), and the cumulative signed weight is \(\tau(n)^2=1\). Therefore the exact row vector is
\[
R_j=\sum_{a=0}^{2^j-1}e_{a2^{k-j}},\qquad 0\le j\le k.
\]
In particular, \(R_k=\sum_{a=0}^{2^k-1}e_a\). For each state \(a\), applying the transition produces the two states \(\lfloor a/2\rfloor\) and \(\lfloor(a+m)/2\rfloor\), both with coefficient \((-1)^a\). Pairing consecutive even and odd \(a\) cancels every internal state. The two uncancelled endpoints give
\[
R_{k+1}=e_{2^{k-1}}-e_{2^k}.
\]
Both carry indices here are even when \(k\ge2\). One more matrix multiplication therefore gives
\[
R_{k+2}=e_{2^{k-2}}+e_{3\cdot2^{k-2}}-e_{2^{k-1}}-e_{2^k}.
\]
From the explicit rows \(R_0,R_1,R_2\) one checks **as exact vector equality**, not just after evaluation against \(v\),
\[
R_{k+2}-R_{k+1}-R_2+3R_1-2R_0=0.
\]
Right-multiplying by \(M^r v\) establishes the claimed recurrence for every \(r\ge0\). Moreover \(R_0v=1\); for \(1\le j\le k\), \(R_jv=\sum_{a<2^j}\tau(a)=0\), since multiplication by a power of two does not change binary digit sum. The explicit two final rows give \(R_{k+1}v=0\) and \(R_{k+2}v=2\), using \(\tau(2^i)=-1\) and \(\tau(3\cdot2^i)=1\). Hence the initial sequence is \(1,0,\ldots,0,2\), with exactly \(k+1\) zeros. Multiplying the recurrence by powers of the formal indeterminate \(z\) gives the characteristic denominator
\[
D_k(z)=1-z-z^k+3z^{k+1}-2z^{k+2}=(1-z)(1-z^k+2z^{k+1}).
\]
Because the initial values are \(C_{k,0}=1\), \(C_{k,1}=\cdots=C_{k,k+1}=0\), \(C_{k,k+2}=2\), direct coefficient comparison gives
\[
D_k(z)\sum_{r\ge0}C_{k,r}z^r=D_k(z)+2z^{k+2}.
\]
Dividing as formal power series yields the boxed formula above.

## Verification
The accompanying standalone `verify.py` directly enumerates the binary-parity products for eight multipliers, \(2\le k\le9\), and 14 dyadic prefix lengths for each. Independently, it constructs and checks the signed carry rows and the vector identity for each tested parameter, then tests the recurrence. These finite computations detect arithmetic and indexing errors; the symbolic proof above proves all allowed parameters and infinitely many prefix lengths.

## Relationship to prior work
Shallit, *Rarefied Thue-Morse Sums Via Automata Theory and Logic* (arXiv:2302.09436), studies the single marginal \(\sum\tau(bn+j)\), rather than the mixed dilation correlation \(\sum\tau(n)\tau(mn)\). Baake and Coons, *Correlations of the Thue--Morse sequence* (arXiv:2209.07102), study translation-invariant shift correlations in the Thue--Morse system; the offset is held fixed rather than multiplied by \(n\). Winterhof, *Pseudorandom binary sequences: quality measures and number-theoretic constructions* (arXiv:2305.11486), surveys correlation measures and digit sequences but does not supply this family-level exact dyadic identity. Morgenbesser, Shallit, and Stoll, *Thue-Morse at Multiples of an Integer* (arXiv:1009.5357), analyze the parity at integer multiples, not the mixed two-factor dyadic generating function. A previously recorded calculation addresses the special multiplier three; that case is explicitly outside this theorem. Transfer-matrix methods themselves are standard and are not claimed as new.

## Limitations
The statement is about \(k\ge2\) and full dyadic prefixes only. There is no claim of novelty of the underlying carry-automaton formalism; earlier implicit deductions from more general correlation results are a bibliographic risk. The proof has not received independent validation. The finite tests are consistency checks, not a surrogate for proof.

## References
1. M. Baake and M. Coons, *Correlations of the Thue--Morse sequence*, arXiv:2209.07102 (first public September 15, 2022).
2. J. Shallit, *Rarefied Thue-Morse Sums Via Automata Theory and Logic*, arXiv:2302.09436 (first public February 18, 2023).
3. A. Winterhof, *Pseudorandom binary sequences: quality measures and number-theoretic constructions*, arXiv:2305.11486 (first public May 19, 2023).
4. J. F. Morgenbesser, J. Shallit and T. Stoll, *Thue-Morse at Multiples of an Integer*, arXiv:1009.5357 (2010).
