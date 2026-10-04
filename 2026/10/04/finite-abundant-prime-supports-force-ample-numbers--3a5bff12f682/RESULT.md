# Finite abundant prime supports force ample numbers

## Finding
Let \(a(n)\) be the recursive-divisor function
\[
a(1)=1,\qquad
a(n)=1+\sum_{\substack{d\mid n\\d<n}}a(d).
\]
Following Fink, call \(n\) ample when
\[
a(n)>n.
\]

For a finite nonempty set \(Q\) of primes, let
\[
\mathcal M_Q=\{n\ge1:\text{every prime divisor of }n\text{ lies in }Q\}.
\]
If
\[
\prod_{q\in Q}\frac{q}{q-1}>2,
\]
then \(\mathcal M_Q\) contains infinitely many ample integers.

As a consequence, for every positive integer \(k\), there are infinitely many ample integers divisible by none of the first \(k\) primes. This proves Fink's conjecture that such an ample integer exists for every \(k\).

## Assumptions and scope
The theorem uses only the defining recurrence for \(a(n)\), Fink's equivalent positive convolution expansion for the recursive-divisor function, and the classical divergence of the Euler product over the primes at \(s=1\).

The finite set \(Q\) need not consist of consecutive primes. The hypothesis
\[
\prod_{q\in Q}\frac{q}{q-1}>2
\]
is a sufficient condition, not asserted to be necessary, for \(Q\) to support an ample integer.

No effective bound is claimed for the least ample integer supported on a prescribed \(Q\), or for the least witness avoiding the first \(k\) primes.

## Proof
For a finite set \(Q\), define its Euler product
\[
Z_Q(s)=\sum_{n\in\mathcal M_Q}\frac1{n^s}
      =\prod_{q\in Q}\frac1{1-q^{-s}}
\]
for \(s>0\).

Fink's recursive identity can be written
\[
2a=\mathbf 1+\mathbf 1*a,
\]
where \(\mathbf 1(n)=1\) and \(*\) denotes Dirichlet convolution. Iterating gives the positive expansion
\[
a=\frac{\mathbf 1}{2}
+\frac{\mathbf 1*\mathbf 1}{2^2}
+\frac{\mathbf 1*\mathbf 1*\mathbf 1}{2^3}
+\cdots.
\]
This is also the \(x=0\) case of the series representation in Fink's later paper.

For \(s>0\) with
\[
Z_Q(s)<2,
\]
sum the expansion over \(\mathcal M_Q\) with weight \(n^{-s}\). Positivity permits termwise summation. If \(r\) factors have product in \(\mathcal M_Q\), then each factor itself lies in \(\mathcal M_Q\); hence the \(r\)-fold convolution contributes exactly \(Z_Q(s)^r\). Therefore
\[
A_Q(s):=\sum_{n\in\mathcal M_Q}\frac{a(n)}{n^s}
=\sum_{r\ge1}\frac{Z_Q(s)^r}{2^r}
=\frac{Z_Q(s)}{2-Z_Q(s)}.
\]

Now assume
\[
Z_Q(1)=\prod_{q\in Q}\frac{q}{q-1}>2.
\]
Because \(Q\) is finite, \(Z_Q(s)\) is continuous and strictly decreasing for \(s>0\), while
\[
\lim_{s\to\infty}Z_Q(s)=1.
\]
Thus there is a unique real number
\[
\alpha_Q>1
\]
such that
\[
Z_Q(\alpha_Q)=2.
\]

Suppose, for contradiction, that no integer in \(\mathcal M_Q\) is ample. Then
\[
a(n)\le n
\]
for all \(n\in\mathcal M_Q\). For every \(s>1\),
\[
A_Q(s)
\le
\sum_{n\in\mathcal M_Q}n^{1-s}
=
Z_Q(s-1).
\]
For \(s>\alpha_Q\), the exact formula above also gives
\[
A_Q(s)=\frac{Z_Q(s)}{2-Z_Q(s)}.
\]
As \(s\downarrow\alpha_Q\), the left side tends to \(+\infty\), because the denominator tends to \(0\) from above. The supposed upper bound tends instead to the finite number
\[
Z_Q(\alpha_Q-1),
\]
since \(\alpha_Q-1>0\) and \(Q\) is finite. This contradiction proves that some \(n\in\mathcal M_Q\) is ample.

There are in fact infinitely many such integers. Fink proved
\[
a(\ell n)\ge a(\ell)a(n)
\]
for all positive integers \(\ell,n\). Hence, if \(n\in\mathcal M_Q\) is ample, then for every \(r\ge1\),
\[
a(n^r)\ge a(n)^r>n^r.
\]
All powers \(n^r\) remain in \(\mathcal M_Q\), so the support \(Q\) contains infinitely many ample integers.

Finally fix a positive integer \(k\), and let \(p_k\) denote the \(k\)-th prime. The classical divergence of the Euler product at \(s=1\) implies
\[
\prod_{p>p_k}\frac{p}{p-1}=+\infty.
\]
After deleting the finitely many primes at most \(p_k\), a finite subproduct still eventually exceeds \(2\). Choose a finite set
\[
Q\subset\{p:p>p_k\}
\]
with
\[
\prod_{q\in Q}\frac{q}{q-1}>2.
\]
The first part supplies infinitely many ample integers whose prime factors all lie in \(Q\). None is divisible by any of the first \(k\) primes. This proves the conjecture.

## Verification
The accompanying `verify.py` checks several finite consequences of the proof.

For
\[
Q=\{3,5,7,11,13\},
\]
it verifies exactly that
\[
\prod_{q\in Q}\frac{q}{q-1}
=
\frac{1001}{384}>2.
\]
It independently evaluates \(a(n)\) by the defining recurrence on exponent vectors and confirms Fink's displayed odd ample example
\[
n=3^9 5^5 7^2 11 13=430996190625,
\]
for which
\[
a(n)=436791402496>n.
\]

The checker also numerically locates the unique root of
\[
Z_Q(s)=2
\]
and confirms the pole-versus-finite-bound behavior used in the proof on a nearby test point.

These computations are regression checks only. The existence theorem for every finite \(Q\) satisfying the Euler-product inequality, and the corollary for every \(k\), are proved analytically above.

## Relationship to prior work
Fink introduced ample numbers and stated as Conjecture 1 that there should exist ample numbers not divisible by the first \(k\) primes for every \(k\). The same paper proves the supermultiplicative inequality
\[
a(\ell n)\ge a(\ell)a(n)
\]
and notes that one witness for a given \(k\) automatically gives infinitely many.

Liyanage and Ranasinghe later described an approach toward the same conjecture based on explicit divisor-type formulas. Their 2022 conference abstract calls the work ongoing and does not state a proof for arbitrary \(k\).

Fink's 2023 paper gives the global Dirichlet series
\[
\sum_{n\ge1}\frac{a(n)}{n^s}
=
\frac{\zeta(s)}{2-\zeta(s)}
\]
and the positive convolution expansion used here. The new step is to restrict that expansion to the divisor-closed monoid generated by an arbitrary finite prime set \(Q\), producing
\[
A_Q(s)=\frac{Z_Q(s)}{2-Z_Q(s)},
\]
and then compare its finite-support pole with the hypothetical coefficientwise bound \(a(n)\le n\). That support-local argument yields the all-\(k\) conclusion.

A current problem database still listed Fink's conjecture as open at the time of the literature check. Targeted searches for the finite-support Euler-product criterion, for an all-\(k\) proof, and for an equivalent support-local Dirichlet-series argument did not locate a covering result.

## Limitations
The proof is existential. It does not give a practical upper bound for the smallest ample integer avoiding the first \(k\) primes, and it does not determine the minimal prime support satisfying the sufficient Euler-product condition.

The criterion
\[
\prod_{q\in Q}\frac{q}{q-1}>2
\]
may be stronger than necessary for a particular support \(Q\).

Literature non-detection cannot exclude an equivalent argument in an unindexed source.

## References
1. Thomas Fink, “Recursively abundant and recursively perfect numbers,” arXiv:2008.10398v1, first posted 24 August 2020. See Theorem 1, Corollary 1, and Conjecture 1.
2. T. M. A. Fink, “Properties of the recursive divisor function and the number of ordered factorizations,” arXiv:2307.09140v1, first posted 18 July 2023. See Theorems 1 and 2.
3. M. P. Liyanage and P. G. R. S. Ranasinghe, “An approach towards settling a conjecture on ample numbers,” Proceedings of the 9th Ruhuna International Science & Technology Conference, 19 January 2022, p. 41.
