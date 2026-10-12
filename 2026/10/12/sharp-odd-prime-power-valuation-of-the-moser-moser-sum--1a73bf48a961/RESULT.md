# Sharp odd-prime-power valuation of the Moser–Moser sum
## Finding
For an odd prime \(p\), an integer \(r\ge 2\), and a positive integer \(a\) with \(p\nmid a\), define
\[
S_{p^r}(a)=\sum_{d\mid p^r}\varphi(d)^2\left(\frac{p^r}{d}\right)!d^{p^r/d}a^{p^r/d}.
\]
Then
\[
\nu_p\bigl(S_{p^r}(a)\bigr)=3r-2.
\]
Thus the classical Moser–Moser congruence, which gives divisibility by \(p^{2r}\), has the exact stronger modulus \(p^{3r-2}\) on every odd prime power of exponent at least two, provided \(p\nmid a\).

## Assumptions and scope
Here \(\varphi\) is Euler's totient and \(\nu_p\) is the \(p\)-adic valuation. The theorem concerns odd primes, exponents \(r\ge2\), and units \(a\) modulo \(p\). The restriction \(r\ge2\) is essential to the stated formula: the prime case is governed by the classical Wilson/Fermat cancellation. The prime \(2\) is excluded because additional equal-valuation terms can create different cancellation patterns.

## Proof
Write each divisor as \(d=p^j\), with \(0\le j\le r\), and denote the corresponding summand by \(T_j\).

For \(j=r\),
\[
T_r=\varphi(p^r)^2p^r a=p^{3r-2}(p-1)^2a,
\]
so \(\nu_p(T_r)=3r-2\).

For \(1\le j\le r-1\), put \(m=r-j\ge1\). Legendre's formula gives
\[
\nu_p((p^m)!)=\frac{p^m-1}{p-1},
\]
and therefore
\[
\nu_p(T_j)=2j-2+\frac{p^m-1}{p-1}+jp^m.
\]
Subtracting \(3r-2=3j+3m-2\) yields
\[
\nu_p(T_j)-(3r-2)
=j(p^m-1)+\frac{p^m-1}{p-1}-3m.
\]
If \(m=1\), this is \(j(p-1)-2\), which is nonnegative for every odd \(p\), with equality only when \(p=3\) and \(j=1\). If \(m\ge2\), the expression is minimized at \(p=3\) and \(j=1\), where it equals
\[
\frac32(3^m-1)-3m>0.
\]
Hence every intermediate summand has valuation strictly larger than \(3r-2\), except \(p=3,r=2,j=1\), where it has valuation exactly \(4\).

For \(j=0\),
\[
\nu_p(T_0)=\nu_p((p^r)!)=\frac{p^r-1}{p-1}.
\]
For \(p\ge5\), this is at least \(1+5(r-1)>3r-2\). For \(p=3\) and \(r\ge3\), it is at least \(1+3+9(r-2)>3r-2\). The only equality case is again \(p=3,r=2\).

Except at \(p=3,r=2\), the final summand \(T_r\) is therefore the unique summand of minimum \(p\)-adic valuation, so the valuation of the sum is exactly \(3r-2\).

It remains to treat \(p=3,r=2\). Dividing the three summands by \(3^4=81\) and reducing modulo \(3\) gives
\[
\frac{T_0}{81}\equiv a,
\qquad
\frac{T_1}{81}\equiv2a,
\qquad
\frac{T_2}{81}\equiv a
\pmod3,
\]
where Fermat's congruence gives \(a^3\equiv a^9\equiv a\pmod3\). Their sum is congruent to \(a\not\equiv0\pmod3\). Hence \(\nu_3(S_9(a))=4=3r-2\), completing the proof.

## Verification
The accompanying `verify.py` independently evaluates the defining sum exactly for a finite grid of odd prime powers and unit parameters, and separately checks the term-valuation inequalities over a larger finite grid. Its successful output is recorded in `verifier_output.txt`. These computations are regression checks only; the proof above is unbounded and does not rely on enumeration.

## Relationship to prior work
Chan, Chan, Chua, and Ku state the Moser–Moser congruence in the form \(S_n(a)\equiv0\pmod{n^2}\), give a new proof, and develop further congruences of the same modulus. Their proof explicitly establishes local divisibility by \(p^{2\alpha}\) when \(p^\alpha\parallel n\), but does not state an exact valuation on prime powers. Moser's original 1990 theorem establishes integrality after division by \(n^2\), and Evans gives a Burnside-based treatment of the \(a=1\) case. The present result instead determines the exact local order for every odd prime-power input of exponent at least two.

## Limitations
No claim is made here for \(p=2\), for \(r=1\), for parameters divisible by \(p\), or for integers having more than one prime divisor. The literature search did not locate an exact-prime-power valuation theorem for this sum, but absence from the searched sources is not a proof of exhaustive bibliographic novelty.

## References
1. H. H. Chan, S. H. Chan, T. G. Chua, and C. Y. Ku, “On theorems of Fermat, Wilson, and Gegenbauer,” *Canadian Mathematical Bulletin* 67 (2024), 304–317. DOI: 10.4153/S0008439523000723. Published online 2023-09-12.
2. W. O. J. Moser, “A (Modest) Generalization of the Theorems of Wilson and Fermat,” *Canadian Mathematical Bulletin* 33 (1990), 253–256. DOI: 10.4153/CMB-1990-040-6.
3. T. J. Evans, “On Some Generalizations of Fermat's, Lucas's and Wilson's Theorems,” arXiv:math/0510620, 2005; later *Ars Combinatoria* 79 (2006), 189–194.
