# A sharp dyadic phase transition in fifth-column Stirling differences

## Finding
Let \(S(m,5)\) denote the Stirling number of the second kind and let \(\nu_2(z)\) be the exponent of \(2\) dividing the nonzero integer \(z\). For every integer \(n\ge3\) and integer \(q\ge0\), put \(N=2^n\) and
\[
D_{n,q}=S\!\left(2^n(1+2^q),5\right)-S(2^n,5).
\]
Then \(D_{n,q}\ne0\) and its exact valuation is
\[
\nu_2(D_{n,q})=
\begin{cases}
n+q-1,&0\le q\le 2^n-n-2,\\
2^n-1,&q=2^n-n-1,\\
2^n-2,&q\ge2^n-n.
\end{cases}
\tag{1}
\]
In particular, the valuation grows linearly up to a single exceptional spike, then becomes constant under arbitrarily larger power-of-two shifts. One explicit instance is
\[
\nu_2\!\left(S(65552,5)-S(16,5)\right)=14.
\]

## Assumptions and scope
All quantities are ordinary integer Stirling numbers, with \(S(m,k)\) counting partitions of an \(m\)-element set into exactly \(k\) nonempty blocks. The quantifiers in (1) allow \(q\) to depend arbitrarily on \(n\); there is no uniform upper bound on either parameter. The base number \(2^n\) is at least \(8\), so both Stirling numbers in the difference are defined by the standard nonnegative combinatorial convention. The difference is positive, since \(S(m,5)\) is strictly increasing for \(m\ge5\).

## Proof
The standard inclusion-exclusion identity gives, for positive \(m\),
\[
120S(m,5)=5^m-5\cdot4^m+10\cdot3^m-10\cdot2^m+5.
\]
Write \(N=2^n\), \(H=2^{n+q}\), and \(A=120D_{n,q}\). Subtracting the two expressions yields exactly
\[
A=5^N(5^H-1)+10\cdot3^N(3^H-1)
   -10\cdot2^N(2^H-1)-5\cdot4^N(4^H-1).\tag{2}
\]
Because \(H\) is a power of two of exponent at least three, the elementary lifting-the-exponent identity yields
\[
\nu_2(5^H-1)=\nu_2(3^H-1)=n+q+2.
\]
The valuations of the four displayed summands in (2), in their order, are thus exactly
\[
n+q+2,\qquad n+q+3,\qquad N+1,\qquad 2N.\tag{3}
\]
The factors \(2^H-1\) and \(4^H-1\) are odd. Since \(n\ge3\), \(2N>N+3\).

Put \(q_*=N-n-1\), which is at least \(4\). If \(q<q_*\), then the first summand in (2) has strictly smaller valuation than each other summand, giving \(\nu_2(A)=n+q+2\). If \(q>q_*\), the third summand has strictly smaller valuation, giving \(\nu_2(A)=N+1\).

It remains to compute cancellation at the unique boundary \(q=q_*\). There \(H=2^{N-1}\). For every \(s\ge1\) one has the strengthened congruence
\[
\frac{5^{2^s}-1}{2^{s+2}}\equiv3\pmod4.\tag{4}
\]
Indeed the base case \(s=1\) is \((25-1)/8=3\), and squaring \(5^{2^s}\) carries the congruence to \(s+1\): if \(5^{2^s}=1+2^{s+2}u\) with \(u\equiv3\pmod4\), the next normalized quotient is \(u+2^{s+1}u^2\equiv u\pmod4\).

Dividing (2) by \(2^{N+1}\) and reducing modulo \(4\), the first summand is \(3\pmod4\) by (4) and \(5^N\equiv1\pmod4\); the second is \(2\pmod4\) by the exact valuation \(N+2\); the third is \(1\pmod4\), since \(-5(2^H-1)\equiv1\pmod4\); and the fourth vanishes. Hence
\[
A/2^{N+1}\equiv3+2+1=2\pmod4,
\]
so \(\nu_2(A)=N+2\) at the boundary. Finally, \(\nu_2(120)=3\), and subtracting three from the three cases for \(\nu_2(A)\) proves (1). \(\square\)

## Verification
The accompanying standalone `verify.py` uses modular exponentiation to check both sides of (1) without constructing enormous Stirling integers. It separately computes the fifth Stirling column from its defining recurrence for six small and boundary cases, including \((n,q)=(4,12)\), without using inclusion-exclusion. Exact modular arithmetic confirms \(119\) parameter pairs and six separate recurrence checks. These finite checks are corroboration; the infinite-parameter proof is the preceding valuation comparison and boundary congruence.

## Relationship to prior work
Zhao, Hong and Zhao, *Divisibility by 2 of Stirling numbers of the second kind and their differences*, initial arXiv submission September 27, 2012, Theorem 1.3, state for \(3\le k\le2^n\), \(k\) not one less than a power of two, and all positive \(a>b\), a difference valuation of \(n+\nu_2(a-b)-\lceil\log_2 k\rceil+s_2(k)+\delta(k)\). At \(k=5\) this reads \(n+\nu_2(a-b)-1\). Choosing \(a=1+2^q\), \(b=1\), equation (1) agrees only below the boundary and contradicts the *as-printed unrestricted quantifiers* above it: at \(n=4,q=12\) the printed expression is \(15\) but the exact valuation is \(14\). This observation does not contest asymptotic claims in which \(a,b\) are fixed while \(n\) increases.

The same authors' subsequent paper, *The 2-adic valuations of differences of Stirling numbers of the second kind* (arXiv:1407.8443), discusses finer and asymptotic variants, including excluded block counts. The finite-boundary law (1) gives a different uniform two-parameter description for \(k=5\). Standard inclusion-exclusion and lifting-the-exponent are classical components, not claimed new.

## Limitations
The exact law is proved for the fifth Stirling column and shifts \(2^n(1+2^q)\) from \(2^n\) with \(n\ge3\). It does not classify arbitrary \(a,b,k\) or dispute every restricted or eventually-in-\(n\) version of the earlier conjecture. A logically equivalent unlocated published result remains possible; the originality assessment depends on the cited statements and inspected material, not on a claim of exhaustive literature coverage. The accompanying checks are finite and not an independent mathematical audit.

## References
1. J. Zhao, S. Hong and W. Zhao, *Divisibility by 2 of Stirling numbers of the second kind and their differences*, arXiv:1209.6284 (first submitted 2012-09-27); *Journal of Number Theory* (2014), DOI: 10.1016/j.jnt.2014.01.005, especially Theorem 1.3.
2. W. Zhao, J. Zhao and S. Hong, *The 2-adic valuations of differences of Stirling numbers of the second kind*, arXiv:1407.8443 (first submitted 2014-07-31).
3. T. Lengyel, work on the \(2\)-adic valuations of Stirling-number differences and the motivating conjecture, cited in reference 1.
