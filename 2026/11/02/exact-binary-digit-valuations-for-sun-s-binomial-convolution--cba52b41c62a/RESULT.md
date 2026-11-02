# Exact binary-digit valuations for Sun's binomial convolution

## Finding
For every integer \(n\ge1\), let
\[
a_n=\binom{6n}{3n}\binom{3n}{n},\quad a_0=1,\qquad
T_n=\sum_{k=0}^{n}a_ka_{n-k}.
\]
Write \(s_2(m)\) for the number of ones in the binary expansion of the nonnegative integer \(m\). Then
\[
\boxed{\nu_2(T_n)=3s_2(n).}
\]
For the integer normalized by the Sun–Guo divisor,
\[
S_n=\frac{T_n}{(2n-1)\binom{3n}{n}},
\]
the equivalent exact formula is
\[
\boxed{\nu_2(S_n)=s_2(n)+s_2(3n).}
\]
In particular, these formulas apply at every positive index, including multiples of all powers of two.

## Assumptions and scope
The binomial coefficients have their usual integer meaning. The valuation \(\nu_2(m)\) is the exponent of two in a nonzero integer \(m\). The sums \(T_n\) are positive. The integrality of \(S_n\), already established by Guo, is also recovered for each checked finite instance but is *not* newly established by the valuation argument alone. All universal valuation statements concern positive integers \(n\), without a bound.

## Proof
Set \(A(z)=\sum_{n\ge0}a_nz^n\). The Pochhammer expression for its coefficients gives
\[
A(z)={}_2F_1\!\left(\frac16,\frac56;1;432z\right).
\]
The classical quadratic form of Clausen's hypergeometric identity states
\[
{}_2F_1(a,1-a;1;x)^2
={}_3F_2\!\left(\frac12,a,1-a;1,1;4x(1-x)\right).
\]
Because \((\tfrac12)_k(\tfrac16)_k(\tfrac56)_k\, (4\cdot432)^k/(k!)^3=a_k\binom{2k}{k}\), specialization at \(x=432z\) yields the identity of formal power series
\[
A(z)^2=\sum_{k\ge0}a_k\binom{2k}{k}z^k(1-432z)^k.
\]
Taking coefficients of \(z^n\) gives the exact finite alternative expression
\[
T_n=\sum_{k=\lceil n/2\rceil}^{n}
(-432)^{n-k}a_k\binom{2k}{k}\binom{k}{n-k}.\tag{1}
\]
Legendre's formula \(\nu_2(m!)=m-s_2(m)\), and invariance of digit sums under doubling, give
\[
\nu_2(a_k)=2s_2(k),\qquad
\nu_2\binom{2k}{k}=s_2(k).
\]
The last term \(k=n\) in (1) is \(a_n\binom{2n}{n}\), of valuation exactly \(3s_2(n)\). For any earlier term write \(j=n-k\ge1\). Since \(432=2^4\cdot27\), its valuation is at least \(4j+3s_2(k)\). The binary digit-sum inequality
\[
s_2(n)=s_2(k+j)\le s_2(k)+s_2(j)\le s_2(k)+j
\]
implies
\[
4j+3s_2(k)\ge 3s_2(n)+j>3s_2(n).
\]
Thus the term \(k=n\) has strictly smaller two-adic valuation than every other term in (1). The ultrametric inequality with a unique least-valuation summand proves \(\nu_2(T_n)=3s_2(n)\) without cancellation ambiguity.

Finally, \(2n-1\) is odd and another use of Legendre's formula gives
\[
\nu_2\binom{3n}{n}=2s_2(n)-s_2(3n).
\]
Subtracting the divisor valuation proves the asserted formula for \(\nu_2(S_n)\). Guo's theorem ensures \(S_n\) itself is an integer. This completes the proof.

## Verification
The accompanying standard-library script `verify.py` recomputes the original convolution, the transformed Clausen coefficient sum, the integral Sun–Guo quotient and both valuation predictions using exact integer arithmetic. On execution it returned `VERIFY_OK positive_indices=240 clausen_coefficients=241 normalized_quotients=240`. This is a finite cross-check, not the universal proof above. Run with `python3 verify.py`.

## Relationship to prior work
Sun introduced the normalized convolution and its divisibility questions. Guo proved the exact divisor \((2n-1)\binom{3n}{n}\) divides the convolution. Yang subsequently refined Guo's theorem with two-adic lower bounds for individually normalized summands, but those bounds do not determine the valuation of the entire convolution or the exact digit-sum formula here. The classical Clausen identity provides the alternative alternating expansion (1), whose unique lowest-valuation summand is the key extra mechanism. Relevant searched literature did not identify an already stated equivalent formula; broader implicit coverage by other hypergeometric methods remains possible.

## Limitations
No claim is made about odd-prime valuations, exact numerical quotient values, or asymptotic magnitudes. The argument determines the two-adic exponent of the full sum and normalized quotient, but it does not itself supply a new proof of the stronger integer divisibility result of Guo. Novelty is a same mathematical model literature assessment and not independent certification.

## References
- Z.-W. Sun, *Some new series for \(1/\pi\) and related congruences*, arXiv:1104.3856 (first public version 2011-04-19).
- V. J. W. Guo, *Proof of Sun's conjecture on the divisibility of certain binomial sums*, arXiv:1301.4877 (2013).
- Q.-H. Yang, *A refinement of Guo's theorem concerning divisibility properties of binomial coefficients*, Ars Combinatoria **135** (2017), 213–221.
- T. Clausen, *Ueber die Fälle, wenn die Reihe von der Form ...*, J. Reine Angew. Math. **3** (1828), Clausen's square identity for hypergeometric series.
