# An irreducible nonprimitive degree-\(41\) polynomial with primitive constant

## Finding

Let \(K=\mathbb F_{41}[w]/(w^2-3)\), with \(w^2=3\), and put \(\lambda=2+16w\). Then \(\lambda\) is primitive in \(K^\times\), and
\[
f(X)=X^{41}+X+\lambda\in K[X]
\]
is irreducible but **not primitive**. This is a counterexample to the universal claim in Conjecture 4.2 of Sharma [1], at the first prime after that paper's reported computational range.

More precisely, writing \(Q=41^2=1681\) and \(E=(Q^{41}-1)/83\), the class \(\alpha=X\bmod f\) satisfies the exact identity
\[
\alpha^E=1\quad\text{in }K[X]/(f),
\]
where \(83\) is prime and divides \(Q^{41}-1\). Hence the multiplicative order of \(\alpha\) is strictly less than \(Q^{41}-1\).

There are exactly \(384\) primitive constants in \(K\). A complete finite enumeration finds that **exactly \(64\)** of them have the specific order-\(83\) obstruction \(\alpha^E=1\). This counts that obstruction, not necessarily every way a polynomial in this family can fail to be primitive.

## Assumptions and scope

All arithmetic is exact, in characteristic \(41\). An element of \(K\) is represented uniquely as \(a+bw\) with \(0\le a,b<41\), and the multiplication rule is
\[
(a+bw)(c+dw)=(ac+3bd)+(ad+bc)w\pmod {41}.
\]
The degree-\(41\) polynomial is monic. A polynomial over \(K\) is *primitive* when it is irreducible and each of its roots has multiplicative order \(Q^{41}-1\) in the degree-\(41\) extension.

## Proof

**1. The coefficient field is a field.** The quadratic-character computation \(3^{20}\equiv-1\pmod{41}\) shows that \(3\) is not a square in \(\mathbb F_{41}\). Thus \(K\) is the field of \(1681\) elements.

**2. The constant is primitive.** Since \(Q-1=1680=2^4\cdot3\cdot5\cdot7\), it suffices to check that \(\lambda^{1680/\ell}\ne1\) for \(\ell=2,3,5,7\). Exact arithmetic gives
\[
\begin{array}{c|c}
\ell&\lambda^{1680/\ell}\\\hline
2&40\\
3&20+25w\\
5&18\\
7&15+26w
\end{array}
\]
None equals \(1\). The multiplicative order of \(\lambda\) is therefore precisely \(1680\).

**3. Irreducibility is proved independently of the order test.** For a root \(\alpha\) of \(f\), the defining equation yields \(\alpha^{41}=-\alpha-\lambda\). A further \(41\)-st power yields
\[
\alpha^{41^2}=\alpha+\lambda-\lambda^{41}.
\]
Since \(\lambda^{41}=2-16w\), the shift \(\delta=\lambda-\lambda^{41}=32w\) is nonzero and belongs to \(K\). Iteration gives \(\alpha^{Q^j}=\alpha+j\delta\) for all integers \(j\ge0\). In characteristic \(41\) the first \(41\) terms are pairwise distinct; hence \(\alpha\) has \(41\) distinct conjugates over \(K\). Its minimal polynomial is the monic polynomial \(f\) of degree \(41\), proving irreducibility.

**4. Exact nonprimitivity certificate.** The prime \(83\) divides \(Q^{41}-1\) because \(Q\equiv21\pmod{83}\) and \(21^{41}\equiv1\pmod{83}\). The standalone verifier implements polynomial multiplication in \(K[X]/(f)\) using the reduction \(X^{41}=-X-\lambda\). Binary exponentiation, with the exact integer exponent \(E=(1681^{41}-1)/83\), returns the constant polynomial \(1\), with all other \(40\) coefficients zero. This is the finite exact identity \(X^E\equiv1\pmod f\). Because \(f\) is irreducible and \(83>1\), the order of its root divides the proper factor \(E\) and cannot equal \(Q^{41}-1\).

**5. Enumeration of the specified obstruction.** In the finite field \(K\) there are \(\varphi(1680)=384\) generators. The companion enumeration visits all \(41^2\) coordinate pairs, rejects zero and tests each nonzero pair for primitivity against the four prime factors of \(1680\). For each primitive constant it then evaluates the same polynomial modular power using exact integer arithmetic. It finds \(384\) primitive constants and \(64\) satisfying the order-\(83\) identity, with no untested coordinate pairs. This is a finite exhaustive certificate for the count; the single explicit witness already suffices to refute the universal conjecture.

## Verification

Two executable source artifacts accompany the statement. With Python 3, run `python3 verify.py` for an independent implementation of field arithmetic, the four primitivity tests, the irreducibility hypotheses, and the exact polynomial modular exponentiation. It prints `VERIFY_OK` when each assertion holds. Separately, compile `census.cpp` using `g++ -O3 -std=c++17 census.cpp -o census` with the Boost multiprecision header available, then run `./census`. It prints `CENSUS_OK primitive_constants=384 order_83_obstructions=64` only if the exhaustive count matches both specified integers. A finite computation is used here as an *exact certificate of an explicit finite identity*, not as an inference from limited sampling to an unrestricted family.

## Relationship to prior work

Sharma [1], Section 4.2, Conjecture 4.2 states that \(X^p+X+\lambda\) is primitive over \(\mathbb F_{p^2}\) for **every** odd prime \(p\) and every primitive coefficient \(\lambda\). Its Remark 4.2 and Table 6 report supporting computation for \(3\le p\le37\). The present \(p=41\) example directly contradicts that universal assertion. Proposition 4.1 of [1] concerns *irreducibility*, which the example satisfies; it does not prove that the polynomial has a primitive root.

Cohen's prescribed-trace theorem [2] and related prescribed-coefficient existence results [3] give existence of some primitive elements or polynomials with specified data. Those existential statements do not imply that *every* polynomial in this fixed family with primitive constant is primitive. The counterexample does not refute the weaker *existence* Conjecture 4.1 of [1].

## Limitations

No claim is made that this is the least counterexample over all characteristics, nor that all \(384\) constants have been classified by every possible proper multiplicative order. The exact count \(64\) concerns the specified order-\(83\) test only. The conclusions are specific to \(p=41\). An unindexed independent computation or an implicit special case of older cyclotomic literature could establish earlier priority; the novelty comparison is not independent certification.

## References

[1] Avnish K. Sharma, *Primitive Polynomials of the Form \(g(x)+\lambda\) over Finite Fields: Non-Existence Results and Conjectures*, arXiv:2608.07262 (first posted 2026-08-07), Section 4.2, Proposition 4.1, Conjecture 4.2, Remark 4.2, Table 6. https://arxiv.org/abs/2608.07262

[2] Stephen D. Cohen, *Primitive elements and polynomials with arbitrary trace*, Discrete Mathematics 83 (1990), 1–7. DOI:10.1016/0012-365X(90)90215-4.

[3] Mateja Prešern, *Existence problems of primitive polynomials over finite fields*, PhD thesis, University of Glasgow (2007). https://theses.gla.ac.uk/50/
