# No perfect powers in the dyadic-base generalized Woodall family
## Finding
For every pair of integers \(a,n\ge1\), put
\[
W_{a,n}=n(2^a)^n-1=n2^{an}-1.
\]
There are no integers \(y\ge2\) and \(k\ge2\) such that
\[
W_{a,n}=y^k.
\]
Thus every power-of-two-base generalized Woodall family is free of nontrivial perfect powers. In particular, the ordinary Woodall sequence, obtained at \(a=1\), contains no nontrivial perfect power.

## Assumptions and scope
A nontrivial perfect power means \(y^k\) with integers \(y\ge2\) and \(k\ge2\). The theorem treats the generalized Woodall expression \(nb^n-1\) only for dyadic bases \(b=2^a\). Some prime-search conventions impose \(n+2>b\); no such restriction is needed here.

No claim is made for bases with an odd prime factor. The proof uses essentially that every odd divisor of \(n2^{an}\) divides \(n\).

## Proof
Suppose
\[
n2^{an}-1=y^k
\]
with \(a,n\ge1\), \(y\ge2\), \(k\ge2\). The left side is odd, so \(y\) is odd.

If \(k\) is even, then \(y^k\equiv1\pmod8\). When \(an\ge3\),
\[
n2^{an}-1\equiv7\pmod8,
\]
a contradiction. The only pairs with \(an<3\) are
\[
(a,n)=(1,1),(2,1),(1,2),
\]
whose values are \(1,3,7\), none a nontrivial even power.

Now let \(k\ge3\) be odd. Factor
\[
y^k+1=(y+1)T,
\qquad
T=y^{k-1}-y^{k-2}+\cdots-y+1.
\]
Because \(y\) and \(k\) are odd, \(T\) is odd. Since
\[
(y+1)T=n2^{an},
\]
we have \(T\mid n\), hence \(T\le n\).

Also
\[
T=\frac{y^k+1}{y+1}
>
y^{k-1}\frac{y}{y+1}
\ge
\frac34y^{k-1},
\]
because \(y\ge3\). Therefore
\[
y^{k-1}<\frac{4n}{3}.
\]
If \(n=1\) or \(n=2\), then the odd divisor \(T\mid n\) forces \(T=1\), impossible because \(T>1\). Thus \(n\ge3\).

Since \(k/(k-1)\le3/2\),
\[
y^k<
\left(\frac{4n}{3}\right)^{k/(k-1)}
\le
\left(\frac{4n}{3}\right)^{3/2}.
\]
But
\[
n2^{an}-1\ge n2^n-1>n2^{n-1}.
\]
For \(n\ge3\),
\[
n2^{n-1}\ge\left(\frac{4n}{3}\right)^{3/2},
\]
because this is equivalent to
\[
2^{n-1}\ge\left(\frac43\right)^{3/2}\sqrt n,
\]
which holds at \(n=3\), and \(2^{n-1}/\sqrt n\) increases since the ratio of successive terms is \(2\sqrt{n/(n+1)}>1\). Thus
\[
n2^{an}-1>y^k,
\]
contradiction.

## Verification
The accompanying checker uses integer-only root arithmetic to test all \(1\le a\le6\), \(1\le n\le30\), verifies the complete low-\(an\) boundary for the modulo-\(8\) branch, and checks the key growth inequality for \(3\le n\le10000\). These computations are corroborative only; the theorem follows from the proof above.

## Relationship to prior work
Woodall numbers \(W_n=n2^n-1\) are classical. Luca and Shparlinski study pseudoprimality in the Cullen and Woodall sequences; their complete paper proves a pseudoprime-counting bound for Woodall numbers and contains no occurrence of “perfect power”. Its subject classifications include \(11B83\).

Azami and Uchiyama develop a primality-testing algorithm for ordinary Woodall numbers. This addresses primality rather than perfect-power values.

Generalized Woodall prime-search material uses the expression \(nb^n-1\). The result here isolates all dyadic bases \(b=2^a\) and proves a uniform perfect-power exclusion. The companion Cullen perfect-power classification does not imply this theorem: the sign is reversed, Cullen numbers have nontrivial square values, and the present theorem has the additional base parameter \(a\).

## Limitations
The argument does not extend directly to generalized Woodall bases with odd prime factors, because then the odd cofactor \((y^k+1)/(y+1)\) can divide the base rather than \(n\).

Keller’s classical article was available through abstract and classification records but its publisher PDF was inaccessible. The complete Luca–Shparlinski paper was inspected in full. Older Woodall sources found here had year-only or inconsistent exact-day metadata; the exact date used in metadata is the verified J-STAGE public release date of the Woodall primality-testing paper.

## References
1. F. Luca and I. E. Shparlinski, “Pseudoprime Cullen and Woodall numbers”, *Colloquium Mathematicum* 107 (2007), 35–43, DOI 10.4064/cm107-1-5.
2. K. Azami and S. Uchiyama, “Primality testing of Woodall numbers”, *JSIAM Letters* 6 (2014), 1–4, DOI 10.14495/jsiaml.6.1.
3. W. Keller, “New Cullen Primes”, *Mathematics of Computation* 64 (1995), 1733–1741.
4. PrimeGrid, “Generalized Cullen/Woodall Prime Search”, document defining generalized Woodall values as \(nb^n-1\).
