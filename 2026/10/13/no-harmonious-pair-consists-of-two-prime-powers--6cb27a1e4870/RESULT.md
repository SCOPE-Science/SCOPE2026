# No harmonious pair consists of two prime powers
## Finding
Let \(\sigma(n)\) be the sum of the positive divisors of \(n\). A pair of positive integers \((x,y)\) is harmonious when
\[
\frac{x}{\sigma(x)}+\frac{y}{\sigma(y)}=1.
\]

There are no primes \(p,q\) and integers \(a,b\ge1\) such that
\[
x=p^a,\qquad y=q^b
\]
form a harmonious pair.

Equivalently, every harmonious pair has at least one member divisible by at least two distinct primes.

## Assumptions and scope
Prime powers here have positive exponent. The primes \(p\) and \(q\) are not assumed distinct at the outset.

The result concerns ordinary harmonious pairs defined using the usual divisor-sum function \(\sigma\). It does not concern cross-harmonious, unitary-harmonious, or other variants.

## Proof
Assume for contradiction that
\[
\frac{p^a}{\sigma(p^a)}+\frac{q^b}{\sigma(q^b)}=1.
\]
Set
\[
A=\sigma(p^a),\qquad B=\sigma(q^b),
\]
and
\[
U=A-p^a=\sigma(p^{a-1}),\qquad
V=B-q^b=\sigma(q^{b-1}).
\]
After multiplying the harmonious equation by \(AB\), one has
\[
p^aB+q^bA=AB.
\]
Using
\[
A=p^a+U,\qquad B=q^b+V
\]
and cancelling the common terms gives the exact factorization
\[
UV=p^a q^b.
\]
Thus
\[
\sigma(p^{a-1})\sigma(q^{b-1})=p^a q^b. \tag{1}
\]

For every prime \(r\) and integer \(t\ge0\),
\[
\sigma(r^t)=1+r+\cdots+r^t\equiv1\pmod r.
\]
Hence
\[
p\nmid U,\qquad q\nmid V.
\]

If \(p=q\), then neither \(U\) nor \(V\) is divisible by \(p\), contradicting (1), whose right side is divisible by \(p\). Therefore
\[
p\ne q.
\]

Equation (1) has no prime factors other than \(p\) and \(q\). Since \(p\nmid U\), every prime factor of \(U\) must be \(q\). Since \(q\nmid V\), every prime factor of \(V\) must be \(p\).

If \(a=1\), then \(U=1\), so the factor \(q^b\) on the right side of (1) would have to divide \(V\), contradicting \(q\nmid V\). Thus \(a\ge2\). Similarly \(b\ge2\). Consequently \(U,V>1\), and comparison of prime-adic valuations in (1) forces
\[
U=q^b,\qquad V=p^a.
\]
That is,
\[
\frac{p^a-1}{p-1}=q^b,\qquad
\frac{q^b-1}{q-1}=p^a. \tag{2}
\]

Substitute the first identity in (2) into the second:
\[
p^a
=
\frac{\frac{p^a-1}{p-1}-1}{q-1}
=
\frac{p(p^{a-1}-1)}{(p-1)(q-1)}.
\]
After division by \(p\),
\[
(p-1)(q-1)p^{a-1}=p^{a-1}-1. \tag{3}
\]
But
\[
(p-1)(q-1)\ge1,
\]
so the left side of (3) is at least \(p^{a-1}\), whereas the right side is strictly smaller than \(p^{a-1}\). This contradiction proves the theorem.

## Verification
The accompanying checker evaluates the defining harmonious equation exactly, with rational arithmetic, for all prime powers
\[
p^a,\ q^b
\]
with
\[
p,q\le97,\qquad 1\le a,b\le8.
\]
It finds no pair.

The checker independently verifies the algebraic factorization
\[
(\sigma(p^a)-p^a)(\sigma(q^b)-q^b)=p^a q^b
\]
whenever the harmonious equation is imposed symbolically through exact integer identities, and it checks the final inequality for the same finite grid.

These finite tests are corroborative only. The infinite statement follows from the valuation and size argument in the proof.

## Relationship to prior work
Kozek, Luca, Pollack, and Pomerance introduced the systematic study of harmonious pairs and proved that integers belonging to such pairs form a sparse set. Their paper defines harmonious pairs by the same equation used here, gives examples and asymptotic results, discusses a bound inherited from Borho in terms of the total number of prime factors, studies discordant numbers, and gives computational data.

The complete author manuscript of that paper was inspected section by section. Searches for “prime power” and “prime-power” encounter prime powers only inside the analytic proof machinery; no theorem or corollary excludes a harmonious pair whose two members are both prime powers. In particular, the Borho-type bound quoted there constrains the size of a pair in terms of the total prime-factor multiplicity but does not imply the present nonexistence statement.

The exact-sequence records A253535 and A253534 list the lesser and larger members of harmonious pairs and give the standard definition and examples. They do not state the prime-power exclusion.

A related result for the shape consisting of one power of two paired with a number having prime support \(\{2,q\}\) has genuine solutions when \(q\) is a suitable Mersenne prime. That result is not stronger than the theorem here because its second member is not a prime power.

## Limitations
The theorem excludes only the case in which both members individually have one-prime support. It does not classify harmonious pairs for which one member is a prime power and the other has two or more distinct prime factors.

The proof is elementary enough that an equivalent observation could exist in unindexed notes or recreational-number-theory literature. No such statement was found in the targeted named-family, formula-level, prime-power, and exact-sequence searches used for this review.

## References
1. M. Kozek, F. Luca, P. Pollack, and C. Pomerance, “Harmonious pairs”, *International Journal of Number Theory* 11 (2015), 1633–1651. DOI 10.1142/S1793042115400151.
2. OEIS Foundation, A253535, “Lesser member of a harmonious pair”, first recorded 3 January 2015.
3. OEIS Foundation, A253534, “Larger member of a harmonious pair”.
