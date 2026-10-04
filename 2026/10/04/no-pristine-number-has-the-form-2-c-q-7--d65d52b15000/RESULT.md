# No pristine number has the form \(2^c q^7\)

## Finding
Let \(a(n)\) be the recursive divisor function, defined by \(a(1)=1\) and
\[
a(n)=1+\sum_{\substack{d\mid n\\d<n}}a(d).
\]
Following Fink, call \(n\) pristine when \(a(n)=n\).

There is no pristine integer of the form
\[
2^c q^7
\]
with \(c\ge1\) and \(q\) an odd prime.

Fink's exact formula gives
\[
a(2^c q^7)
=
2^c\sum_{i=0}^{7}\binom{7}{i}\binom{c+i}{i},
\]
so pristineness is equivalent to
\[
q^7=F_7(c):=\sum_{i=0}^{7}\binom{7}{i}\binom{c+i}{i}.
\]
The argument below reduces every possible solution to the finite interval \(1\le c\le5032\), and exact enumeration on that interval finds no seventh power at all.

## Assumptions and scope
The source paper proves the corresponding nonexistence for odd exponents \(3\) and \(5\), proves that for each odd \(d\) there are at most \(d-1\) pristine numbers of the form \(2^c q^d\), and asks whether there are none for every odd \(d\). The present result settles only the next open exponent \(d=7\).

The primary source first appeared publicly as arXiv:2008.10398v1 on 24 August 2020. No assertion is made here about odd exponents \(d\ge9\).

## Proof
A direct expansion and factorization gives
\[
F_7(c)=\frac{(c+8)G(c)}{5040},
\]
where
\[
G(c)=c^6+69c^5+1681c^4+17667c^3+79318c^2+143184c+80640.
\]
Moreover,
\[
G(-8)=-147456=-2^{14}3^2.
\]
Since \(G(c)\equiv G(-8)\pmod{c+8}\),
\[
\gcd(c+8,G(c))\mid147456.
\]

Assume that
\[
q^7=F_7(c)
\]
for an odd prime \(q\). Then
\[
(c+8)G(c)=5040q^7.
\]

First suppose \(q\ge11\). Then \(q\nmid5040\) and \(q\nmid147456\). Hence \(q\) cannot divide both \(c+8\) and \(G(c)\). Because \(q^7\) divides their product, the whole factor \(q^7\) must divide exactly one of them.

The final summand in the definition of \(F_7(c)\) yields
\[
q^7=F_7(c)>\binom{c+7}{7}>\frac{c^7}{5040}.
\]
Since \(4^7>5040\), it follows that
\[
c<4q.
\]
Thus, for \(q\ge11\),
\[
c+8<4q+8<q^7.
\]
Consequently \(q^7\nmid c+8\), so
\[
q^7\mid G(c).
\]
Because \(G(c)>0\) for \(c\ge1\),
\[
G(c)\ge q^7.
\]
Using \((c+8)G(c)=5040q^7\), this gives
\[
c+8\le5040,
\]
hence
\[
c\le5032.
\]

For the remaining odd primes \(q\in\{3,5,7\}\), the already proved bound \(c<4q\) gives \(c<28\), so again \(c\le5032\).

Therefore every possible solution lies in
\[
1\le c\le5032.
\]
The accompanying exact-arithmetic verifier evaluates \(F_7(c)\) throughout this interval and tests whether it is an integer seventh power. There are no such values. Hence no pristine number has the form \(2^c q^7\).

## Verification
The accompanying `verify.py` independently reconstructs \(F_7(c)\) from the binomial sum, checks the displayed polynomial factorization coefficient-by-coefficient using integer arithmetic, verifies
\[
G(-8)=-147456
\]
and
\[
4^7>5040,
\]
and then exhaustively checks every integer \(1\le c\le5032\) for a seventh-power value of \(F_7(c)\). It prints `VERIFY_OK` only if all checks succeed.

The finite computation is used only after the proof has established the unconditional cutoff \(c\le5032\).

## Relationship to prior work
Fink derived the formula
\[
a(2^c q^d)=2^c\sum_{i=0}^{d}\binom{d}{i}\binom{c+i}{i},
\]
used it to exclude \(d=3\) and \(d=5\), and proved that for every odd \(d\) there are at most \(d-1\) pristine numbers of this two-prime form. The paper then explicitly asks whether the true number is always zero.

The present proof sharpens that general finite-count bound from “at most six” to “none” in the first untreated case \(d=7\). Targeted searches using the paper title, the term “pristine,” the exponent \(7\), and the equivalent binomial equation did not locate a prior proof of this case.

## Limitations
This does not resolve Fink's question for all odd exponents. Literature non-detection is not a proof that no unindexed observation of the \(d=7\) case exists.

The exact enumeration checks the rigorously bounded interval only; it is not being used as evidence about unbounded \(c\).

## References
1. Thomas Fink, “Recursively abundant and recursively perfect numbers,” arXiv:2008.10398v1, 24 August 2020.
