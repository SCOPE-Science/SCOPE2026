# An irreducible, nonprimitive degree-\(41\) trinomial with primitive constant term

## Finding
Let \(F=\mathbb F_{41}[u]/(u^2-3)\), \(\lambda=2+16u\), and
\[
f(X)=X^{41}+X+\lambda\in F[X].
\]
The element \(\lambda\) is primitive in \(F^\times\), and \(f\) is irreducible of degree \(41\), yet every root \(\alpha\) satisfies
\[
\alpha^{(41^{82}-1)/83}=1.
\]
Consequently \(f\) is **not** a primitive polynomial over \(F\). This explicitly contradicts the universal assertion of Conjecture 4.2 in Sharma, *Primitive Polynomials of the Form \(g(x)+\lambda\) over Finite Fields* (2026), which conjectures that \(X^p+X+\lambda\) is primitive over \(\mathbb F_{p^2}\) for every primitive \(\lambda\) and odd prime \(p\).

## Assumptions and scope
All calculations are in characteristic \(41\); \(3\) is a nonsquare in \(\mathbb F_{41}\). The word *primitive element* means a generator of the full multiplicative group of a finite field. A *primitive polynomial* is monic, irreducible, and has primitive roots in its degree extension. This result proves a concrete counterexample at \(p=41\), not a classification at other primes. The relevant article was first made publicly available on 2026-08-07 (UTC).

## Proof
**1. The coefficient is primitive.** Euler's criterion gives \(3^{20}\equiv-1\pmod {41}\), so the displayed quadratic quotient is a field of \(41^2=1681\) elements. The multiplicative-group order factors as
\[
1680=2^4\cdot3\cdot5\cdot7.
\]
Direct multiplication using \(u^2=3\) gives the following four exact powers:
\[
\begin{aligned}
\lambda^{840}&=40, &\lambda^{560}&=20+25u,\\
\lambda^{336}&=18, &\lambda^{240}&=15+26u.
\end{aligned}
\]
None is \(1\). Testing the prime divisors \(2,3,5,7\) of \(1680\) therefore proves \(\operatorname{ord}(\lambda)=1680\).

**2. The trinomial is irreducible.** Let \(\alpha\) be any zero of \(f\). The defining relation is \(\alpha^{41}=-\alpha-\lambda\). Applying the \(41\)-power Frobenius again gives
\[
\alpha^{41^2}=\alpha+\lambda-\lambda^{41}=\alpha+32u.
\]
Because \(32u\) is a nonzero element of \(F\), successive \(1681\)-power Frobenius maps send \(\alpha\) to \(\alpha+j(32u)\) for \(j=0,1,\ldots,40\). These are \(41\) distinct elements and the next is \(\alpha\); the degree of \(\alpha\) over \(F\) is therefore precisely \(41\). Since \(f\) has degree \(41\), it is irreducible.

**3. A multiplicative-order obstruction.** The prime \(83\) divides \(1681^{41}-1=41^{82}-1\), as \(1681\equiv21\pmod {83}\) and \(21^{41}\equiv1\pmod {83}\). Define
\[
E=\frac{41^{82}-1}{83}\in\mathbb Z.
\]
Eliminating \(u\) using \(u=-(\alpha^{41}+\alpha+2)/16\), we obtain the monic degree-\(82\) polynomial
\[
G(Z)=(Z^{41}+Z+2)^2-3\cdot16^2
 = Z^{82}+2Z^{42}+4Z^{41}+Z^2+4Z+15
 \quad\in\mathbb F_{41}[Z]
\]
with \(G(\alpha)=0\). Here the constant \(15\) is the reduction of \(4-3\cdot16^2\) modulo \(41\). The degree of \(\alpha\) over \(\mathbb F_{41}\) equals \(82\), since the element \(u\) belongs to \(\mathbb F_{41}(\alpha)\) and \([F(\alpha):F]=41\); thus \(G\) is its minimal polynomial over \(\mathbb F_{41}\).

Exact repeated-squaring in the polynomial quotient \(\mathbb F_{41}[Z]/(G)\) gives the finite identity
\[
Z^E\equiv1\pmod{G(Z)}.
\]
The files `verify_over_prime_field.py` and `verify_over_extension.py` implement this identity using distinct representations and independently check the coefficient's primitivity. Their algorithms are explicit exact modular arithmetic and need no external library. Consequently \(\alpha^E=1\), whereas a generator of \(\mathbb F_{41^{82}}^\times\) must have order \(41^{82}-1=83E\). The root \(\alpha\) is not primitive. Every other root is a Frobenius conjugate and has the same multiplicative order.

## Verification
Run `python3 verify_over_prime_field.py` and `python3 verify_over_extension.py` with Python 3. The first works over \(\mathbb F_{41}[Z]/(G)\), performing repeated multiplication and reduction by the displayed six-term polynomial. The second works over \(F[Z]/(f)\), representing field coefficients as integer pairs and reducing by \(Z^{41}+Z+\lambda\). Both return a `CERTIFICATE_OK` line. The first additionally prints the four primitivity tests and the exponent's bit length (\(433\)). Both check the divisor \(83\) and that the exact exponent's remainder is the unit element. Finite-field quotient identities are exhaustive calculations, not heuristic searches.

## Relationship to prior work
Sharma's arXiv:2608.07262v2, Section 4.2, formulates Conjecture 4.2 for **every** primitive \(\lambda\), and Table 6 reports small-prime computations through \(p=37\). The present example uses \(p=41\) and contradicts the conjecture despite the known irreducibility mechanism. Awasthi and Sharma's arXiv:1612.05367 discusses different *existence* conjectures for primitive polynomials and primitive transformation shift registers; existence for at least one coefficient does not imply primitivity for every coefficient. Searches of these documents, published-finding corpus research entries and indexed literature did not reveal the same \(p=41\) witness. That search result does not prove absolute novelty.

## Limitations
The result disproves the stated universal conjecture only; it does not determine whether another primitive \(\lambda\) at \(p=41\) yields a primitive polynomial, nor classify all failing coefficients or extension degrees. The exact modular-power calculation is accompanied by two replayable implementations but has not received independent external mathematical audit. Earlier unindexed examples remain possible.

## References
1. A. K. Sharma, *Primitive Polynomials of the Form \(g(x)+\lambda\) over Finite Fields: Non-Existence Results and Conjectures*, arXiv:2608.07262v2 (2026; first posted 2026-08-07), Section 4.2, Conjecture 4.2 and Table 6. https://arxiv.org/abs/2608.07262
2. A. Awasthi and R. K. Sharma, *Primitive transformation shift registers over finite fields*, arXiv:1612.05367 (2016), Sections 4 and 9. https://arxiv.org/abs/1612.05367
