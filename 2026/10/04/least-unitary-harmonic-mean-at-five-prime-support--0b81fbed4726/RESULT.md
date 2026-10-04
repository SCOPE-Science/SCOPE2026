# Least unitary harmonic mean at five-prime support
## Finding
For a positive integer \(n\), write
\[
H^*(n)=\frac{n\,d^*(n)}{\sigma^*(n)}
      =2^{\omega(n)}\prod_{p^a\parallel n}\frac{p^a}{p^a+1},
\]
where \(d^*(n)\) and \(\sigma^*(n)\) are the number and sum of the unitary
divisors. A unitary harmonic number is an \(n\) for which \(H^*(n)\) is integral.

Among unitary harmonic numbers with
\[
\omega(n)=5,
\]
the least possible unitary harmonic mean is
\[
H^*(n)=13.
\]
The minimizers are exactly
\[
n=5460=2^2\cdot3\cdot5\cdot7\cdot13
\]
and
\[
n=8190=2\cdot3^2\cdot5\cdot7\cdot13.
\]

Equivalently,
\[
H^*(n)=13,\ \omega(n)=5
\quad\Longleftrightarrow\quad
n\in\{5460,8190\},
\]
and no five-prime-support unitary harmonic number has mean \(10\), \(11\), or \(12\).

## Assumptions and scope
The notation \(p^a\parallel n\) means that \(p^a\) is the exact prime-power
component of \(n\). The five such components are powers of five distinct primes.

Hagis and Lord proved
\[
\frac{2^{k+1}}{k+2}\le H^*(n)<2^k
\]
when \(n\) has \(k\) distinct prime factors, with equality on the left only in
their stated exceptional small cases. Thus for \(k=5\),
\[
H^*(n)>\frac{64}{7}.
\]
Because a unitary harmonic mean is integral, any five-prime-support example has
\[
H^*(n)\ge10.
\]
It is therefore enough to classify the four target means \(10\), \(11\), \(12\),
and \(13\).

The proof below is an exact finite reduction for those four targets. It does not
claim a classification of all unitary harmonic numbers with five distinct prime
factors.

## Proof
Fix an integer target \(h\in\{10,11,12,13\}\), and suppose
\[
H^*(n)=h,\qquad \omega(n)=5.
\]
Let the five exact prime-power components of \(n\), arranged in increasing
numerical order, be
\[
x_1<x_2<x_3<x_4<x_5.
\]
Their prime bases are pairwise distinct. Put
\[
f(x)=\frac{x}{x+1},\qquad T=\frac{h}{32}.
\]
Then the defining equation is
\[
\prod_{i=1}^{5} f(x_i)=T.
\]

Consider a stage at which a prefix \(x_1,\ldots,x_j\) has been chosen. Write
\[
P=\prod_{i=1}^{j}f(x_i)
\]
and let \(r=5-j\) components remain. If \(x\) is the next component, then every
remaining component is at least \(x\). Since \(f\) is strictly increasing,
\[
T
=P\prod_{\ell=1}^{r}f(y_\ell)
\ge P f(x)^r.
\]
Thus every possible next component satisfies the exact inequality
\[
P\left(\frac{x}{x+1}\right)^r\le T.
\]
Because \(P>T\) whenever at least one component remains, the left side increases
to \(P>T\) as \(x\) tends to infinity. Hence this inequality supplies a finite
upper bound for the next component. No floating-point approximation is needed:
after clearing denominators, it is an integer inequality.

At each stage one therefore enumerates only prime powers \(x\) in this finite
interval whose prime base has not already occurred. After four components have
been selected, the fifth component is not searched. If the prefix product is
\(P\), then
\[
P\frac{x_5}{x_5+1}=T
\]
forces
\[
x_5=\frac{T}{P-T}.
\]
This rational number must be an integer prime power, must exceed \(x_4\), and
must have a new prime base. These conditions are necessary and sufficient.

Applying this exhaustive recursion gives no solution for
\[
h=10,\qquad h=11,\qquad h=12,
\]
and exactly two component sets for \(h=13\):
\[
(2,5,7,9,13)
\]
and
\[
(3,4,5,7,13).
\]
Their products are respectively \(8190\) and \(5460\), and direct substitution
gives \(H^*(8190)=H^*(5460)=13\). Together with the lower bound
\(H^*(n)\ge10\), this proves both the minimum and the complete set of minimizers.

## Verification
The accompanying `verify.py` implements the preceding recursion using only
exact rational and integer arithmetic. It verifies the Hagis--Lord lower-bound
consequence for the four required target means, enumerates every admissible
prime-power branch, solves the last component exactly, checks that prime bases
are distinct, and substitutes every returned solution into the defining
product.

The replay reports zero solutions for \(h=10,11,12\) and exactly the two
factorizations above for \(h=13\). The computation is a finite exhaustive
certificate because the monotone inequality proved above supplies a finite
bound at every branch; it is not an empirical search cutoff.

## Relationship to prior work
Hagis and Lord introduced unitary harmonic numbers, proved finiteness for a
fixed number of distinct prime factors, established the lower bound used here,
and completely determined the cases with one, two, and three distinct prime
factors. Their 1975 article also tabulated all examples up to \(10^6\).

Wall later proved that there are exactly \(23\) unitary harmonic numbers with at
most four distinct prime factors. His bounded table through \(10^6\) contains
both \(5460\) and \(8190\), each with mean \(13\), and his paper describes the
same general strategy of successively bounding prime-power components. That
bounded table does not exclude larger five-prime-support numbers of means
\(10\), \(11\), or \(12\), nor does the at-most-four-prime classification do so.

OEIS A006086 records the unitary harmonic numbers and OEIS A006087 records their
unitary harmonic means. These databases display \(5460\) and \(8190\) with mean
\(13\), but their tabulated values do not constitute the unrestricted
five-prime-support extremal classification proved here.

## Limitations
This result identifies only the least mean at five-prime support and its
minimizers. It does not enumerate all unitary harmonic numbers with five
distinct prime factors, and it gives no assertion about the next attainable
mean after \(13\).

The literature comparison inspected the complete Hagis--Lord article, Wall's
full relevant classification and search method, the exact OEIS tables, and
modern literature on upper bounds. No equivalent five-prime-support extremal
theorem was found. A poorly indexed source could nevertheless contain the same
finite classification.

## References
1. P. Hagis, Jr. and G. Lord, "Unitary harmonic numbers", *Proceedings of the
   American Mathematical Society* 51 (1975), 1--7,
   DOI 10.1090/S0002-9939-1975-0369231-9. The paper records presentation to
   the Society on 25 January 1975 and gives primary 1970 MSC 10A20.
2. C. R. Wall, "Unitary harmonic numbers", *The Fibonacci Quarterly* 21
   (1983), 18--25, DOI 10.1080/00150517.1983.12429968.
3. T. Goto, "Upper Bounds for Unitary Perfect Numbers and Unitary Harmonic
   Numbers", *Rocky Mountain Journal of Mathematics* 37 (2007), 1557--1576,
   DOI 10.1216/rmjm/1194275935.
4. OEIS Foundation, A006086, "Unitary harmonic numbers".
5. OEIS Foundation, A006087, "Unitary harmonic means of the unitary harmonic
   numbers".
