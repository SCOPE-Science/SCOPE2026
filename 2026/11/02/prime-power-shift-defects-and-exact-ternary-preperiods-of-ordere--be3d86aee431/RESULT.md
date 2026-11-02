# Prime-power shift defects and exact ternary preperiods of ordered Bell numbers

## Finding

Let \(S(n,j)\) denote the Stirling numbers of the second kind, with \(S(0,0)=1\). The ordered Bell (Fubini) numbers are
\[
F_n=\sum_{j=0}^{n}j!S(n,j),\qquad n\ge0.
\]
For an odd prime \(p\), an integer \(k\ge1\), and \(P=(p-1)p^{k-1}\), define the rational number
\[
R_{p,n}=2^{p-1}\sum_{j=0}^{n}\frac{j!S(n,j)}{(2^p-1)^{j+1}},\qquad n\ge0.
\]
All its denominators are prime to \(p\). The exact prime-power index-shift phase is
\[
\boxed{F_{n+P}-F_n\equiv-p^nR_{p,n}\pmod{p^k}\qquad(n\ge0).}
\]
Moreover, \(R_{p,n}\equiv F_n\pmod p\). In particular, whenever \(0\le n<k\) and \(p\nmid F_n\), the integer difference has exact valuation
\[
\nu_p(F_{n+P}-F_n)=n.
\]
For the least eventual preperiod \(s(p,k)\), define the finite set
\[
\mathcal B_{p,k}=\{n\in\mathbb Z:0\le n<k,\ n+\nu_p(R_{p,n})<k\}.
\]
It contains \(0\), and the exact onset is
\[
\boxed{s(p,k)=1+\max\mathcal B_{p,k}.}
\]
This computes the least preperiod from at most \(k\) rational Stirling sums, with no search through a full modular period. In the ternary case it simplifies to a complete closed classification:
\[
\boxed{s(3,k)=\begin{cases}1,&k=1,\\ k,&k\ge2\text{ even},\\ k-1,&k\ge3\text{ odd}.\end{cases}}
\]
The least eventual period \(P\) is a known result of prior work; the shift phase, finite sharp-onset criterion, and ternary parity law are the contributions asserted here.

## Assumptions and scope

The prime \(p\) is odd, \(k\ge1\), \(n\ge0\), and \(\nu_p\) is the ordinary valuation of nonzero rational numbers whose denominator is prime to \(p\). We use \(0^0=1\) when extracting the zeroth coefficient of a power sum. The least eventual preperiod of a sequence modulo \(p^k\) is the smallest \(s\ge0\) for which some positive integer period works for all indices \(n\ge s\). The theorem concerns scalar ordered Bell numbers, not coefficientwise ordered-Bell polynomials. No claim is made for \(p=2\).

## Proof

**1. Rational moment representation.** The classical exponential generating function and its geometric expansion near the origin are
\[
\sum_{n\ge0}F_n\frac{t^n}{n!}=\frac{1}{2-e^t}
=\frac12\sum_{a\ge0}2^{-a}e^{at}.
\]
Thus the rational power-sum generating function
\[
M_n(z)=\sum_{a\ge0}a^n z^a
=\sum_{j=0}^{n}j!S(n,j)\frac{z^j}{(1-z)^{j+1}}
\]
satisfies \(F_n=\frac12 M_n(1/2)\). The displayed series is interpreted as a rational function when congruences are evaluated; no infinite series is treated as convergent in the \(p\)-adic topology. Substitution \(z=2^{-p}\) gives
\[
\frac12M_n(2^{-p})=2^{p-1}\sum_{j=0}^{n}
\frac{j!S(n,j)}{(2^p-1)^{j+1}}=R_{p,n}.
\]
By Fermat's congruence, \(2^{p-1}\equiv1\pmod p\) and \(2^p-1\equiv1\pmod p\), whence \(R_{p,n}\equiv F_n\pmod p\).

**2. Universal shift defect.** Set \(q=p^k\), \(P=(p-1)p^{k-1}\). The inequality \(P\ge k\) holds for every odd prime and positive \(k\). Consider the formal rational function
\[
H(z)=M_{n+P}(z)-M_n(z)+p^n M_n(z^p).
\]
The coefficient of \(z^a\) for \(p\nmid a\) is \(a^n(a^P-1)\), divisible by \(q\) by Euler's theorem. For \(a=pb\), it is
\[
(pb)^n\big((pb)^P-1\big)+p^nb^n=(pb)^{n+P},
\]
which is divisible by \(q\) because \(P\ge k\). This also holds at \(a=0\) with the stated zeroth-power convention. Hence every Taylor coefficient of \(H(z)\) lies in \(q\mathbb Z\).

The rational function \(H\) has a denominator dividing
\((1-z)^{n+P+1}(1-z^p)^{n+1}\), which has constant term one and integer coefficients. Multiplying by this denominator shows that the numerator polynomial has every coefficient divisible by \(q\). At \(z=1/2\) the denominator is a \(p\)-adic unit, since \(p\) is odd and \(2^p-1\equiv1\pmod p\). Therefore \(H(1/2)\equiv0\pmod q\). Dividing by two gives
\[
F_{n+P}-F_n+p^nR_{p,n}\equiv0\pmod{p^k}.
\]
This is a congruence of exact rational expressions with \(p\)-integral denominators, not an inference from finite numerics.

**3. Exact onset.** Because \(R_{p,n}\) is \(p\)-integral, the shift by \(P\) is a period from every index \(n\ge k\). At each smaller \(n\), the congruence proves that this shift fails precisely when \(n+\nu_p(R_{p,n})<k\). The index zero always fails: \(R_{p,0}=2^{p-1}/(2^p-1)\) is a unit. Thus its exact onset is \(1+\max\mathcal B_{p,k}\).

To establish minimality among **all possible periods**, suppose a period \(d>0\) worked from an earlier index \(s\). For any \(n\ge s\), choose \(h\) so large that \(n+hd\ge k\). Then \(F_n\equiv F_{n+hd}\), while the known \(P\)-shift is valid from \(n+hd\), and the \(d\)-period again gives \(F_{n+P+hd}\equiv F_{n+P}\). Hence \(F_{n+P}\equiv F_n\) already at \(n\ge s\), contradicting the first failing index. The formula therefore computes the least eventual preperiod, not only the onset of a particular candidate shift.

**4. Ternary closure.** For \(n\ge1\), the terms \(j!S(n,j)\) with \(j\ge3\) vanish modulo three. Since \(S(n,1)=1\) and \(S(n,2)=2^{n-1}-1\),
\[
F_n\equiv1+2(2^{n-1}-1)=2^n-1\pmod3.
\]
Thus \(R_{3,n}\) is a ternary unit at every odd \(n\ge1\), and is divisible by three at every even \(n\ge2\). For even \(k\), the index \(k-1\) is odd and the defect has valuation exactly \(k-1\), so the least onset is \(k\). For odd \(k\ge3\), the defect vanishes at \(k-1\) but has valuation exactly \(k-2\) at the odd index \(k-2\); the least onset is \(k-1\). At \(k=1\), the defect at index zero is nonzero and the onset is one. These arguments prove the three branches for every exponent.

## Verification

The accompanying standalone script `verify_fubini.py` computes ordered Bell numbers in modular arithmetic using their independent binomial-block recurrence and computes \(R_{p,n}\) using Stirling-number rows. It checks 357 universal shift identities, 37 sharp valuation instances, and all ternary onset levels through exponent six, across 17 prime-power grids. It also compares two independent definitions of the first 15 ordered Bell numbers. Run using `python verify_fubini.py`; no external packages are needed.

## Relationship to prior work

The ordered Bell numbers and their last-digit periodicity were studied by Mező (2013), building on earlier work by Gross. Asgari and Jahangiri (2017) established related prime-power periods for distinguished-block Fubini sequences. Schreyer (2024) proved that the eventual period of the scalar Fubini sequence at odd modulus is the Carmichael function and gave the general onset upper bound. In the present case the known least period is \((p-1)p^{k-1}\) and the known upper bound is \(k\). Neither result by itself gives the exact scalar discrepancy at the preceding indices. Coefficientwise modular results on ordered-Bell polynomials also do not force the scalar specialization to attain the same preperiod: cancellation at the specialization is exactly what the ternary parity law detects.

The new statement is the explicit universal prime-power difference formula, the finite necessary-and-sufficient onset test, and the resulting complete three-adic onset classification. No prior result on general eventual periodicity is claimed as new.

## Limitations

The theorem is confined to odd primes. For arbitrary \(p\), the onset formula is finite and exact but involves valuations of explicit rational Stirling sums rather than a closed formula solely in \(p,k\). No claim is made about all terms in every residue class, the even prime, or the distribution of the ordered Bell residues. The literature comparison is not a proof of absolute historical priority. Independent validation has not been performed.

## References

1. I. Mező, *Periodicity of the last digits of some combinatorial sequences*, arXiv:1308.1637v1 (public 2013-08-07), https://arxiv.org/abs/1308.1637.
2. A. A. Asgari and M. Jahangiri, *On the periodicity problem of residual r-Fubini sequences*, arXiv:1701.07276 (public 2017-01-25), https://arxiv.org/abs/1701.07276.
3. B. Schreyer, *Rigged Horse Numbers and their Modular Periodicity*, arXiv:2409.03799 (public 2024-09-04), https://arxiv.org/abs/2409.03799.
