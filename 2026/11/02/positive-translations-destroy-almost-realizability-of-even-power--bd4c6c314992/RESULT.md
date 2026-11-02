# Positive translations destroy almost-realizability of even-power Fibonacci samples

## Finding

Let \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). For integers \(h\ge0\) and \(k\ge1\), consider the sequence

\[
a_n=F_{(n+h)^{2k}}\qquad(n\ge1).
\]

**Theorem.** This sequence is almost realizable if and only if \(h=0\). At \(h=0\), the smallest positive integer multiplier making it realizable is \(5\). For every \(h\ge1\), no positive integer multiplier makes it realizable. More precisely, for any fixed \(M\ge1\), the prime-index Dold condition fails for infinitely many primes \(p\equiv2,3\pmod5\):

\[
p\nmid M\bigl(F_{(p+h)^{2k}}-F_{(1+h)^{2k}}\bigr).
\]

The new negative assertion is powered by the exact congruence, for each odd prime \(p\equiv2,3\pmod5\),

\[
F_{(p+h)^{2k}}\equiv F_{(h-1)^{2k}}\pmod p\qquad(h\ge1,k\ge1).
\]

## Assumptions and scope

A nonnegative integer sequence \((a_n)_{n\ge1}\) is *realizable* when there exists a self-map of a set with exactly \(a_n\) points fixed by its \(n\)-th iterate for every \(n\ge1\). It is *almost realizable* when \((Ma_n)_{n\ge1}\) is realizable for some fixed positive integer \(M\). The necessary Dold condition at a prime \(p\) is \(p\mid M(a_p-a_1)\); no sign-condition argument can overcome a failure of this congruence. The exponents and translations in this theorem are integers, with \(k\ge1\), \(h\ge0\); the indexing always begins at \(n=1\). The positive unshifted case is a theorem of Moss and Ward, not an independently discovered construction here.

## Proof

**1. Frobenius calculation.** Put

\[
Q=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
\]

Then \(Q^2=Q+I\), \(Q^{-1}=Q-I\), and the upper-right entry of \(Q^t\) is \(F_t\) for every \(t\ge0\). For any odd prime \(p\equiv2,3\pmod5\), the polynomial \(X^2-X-1\) is irreducible over \(\mathbf F_p\) because its discriminant \(5\) is a quadratic nonresidue. Its roots in \(\mathbf F_{p^2}\) are exchanged by Frobenius and sum to \(1\). Applying the polynomial functional calculus to \(Q\) therefore gives

\[
Q^p=I-Q=-Q^{-1},\qquad Q^{p^2}=Q\pmod p.
\]

These are matrix congruences. Their extension to all nonnegative integers \(j\) is \(Q^{p^j}\equiv Q\) for even \(j\), and \(Q^{p^j}\equiv-Q^{-1}\) for odd \(j\).

**2. Even powers and translation.** Expand the exponent exactly:

\[
(p+h)^{2k}=\sum_{j=0}^{2k}\binom{2k}{j}h^{2k-j}p^j.
\]

Let \(E\) and \(O\) denote the sums of the integer coefficients in this expansion with even and odd \(j\), respectively. For odd \(j\), the integer \(\binom{2k}{j}\) is even: its equality to \(\tfrac{2k}{j}\binom{2k-1}{j-1}\) proves that an odd \(j\) divides the even numerator \(2k\binom{2k-1}{j-1}\), leaving an even quotient. Thus \(O\) is even. The matrix Frobenius identities imply

\[
Q^{(p+h)^{2k}}\equiv(-1)^OQ^{E-O}
=Q^{(h-1)^{2k}}\pmod p,
\]

because \(E-O\) is the binomial evaluation at \(p=-1\). The upper-right entries yield the announced Fibonacci congruence for all \(h\ge1\).

**3. An unbounded collection of Dold obstructions.** Fix \(h\ge1\) and \(k\ge1\). The positive integer

\[
\Delta_{h,k}=F_{(h+1)^{2k}}-F_{(h-1)^{2k}}
\]

is nonzero: for \(h=1\) it compares \(F_{2^{2k}}>0\) with \(F_0=0\), while for \(h\ge2\) the indices are strictly ordered and lie in the range of strictly increasing Fibonacci numbers (except the smallest lower index \(1\), which is still smaller). Thus for each odd prime \(p\equiv2,3\pmod5\),

\[
a_p-a_1\equiv-\Delta_{h,k}\pmod p.
\]

Dirichlet's theorem supplies infinitely many primes in either reduced residue class modulo five. Given any fixed \(M\ge1\), only finitely many such primes divide the nonzero integer \(M\Delta_{h,k}\). At every other such prime, \(p\nmid M(a_p-a_1)\). Consequently no fixed multiplier can satisfy even the prime-index Dold conditions; the sequence is not almost realizable when \(h\ge1\).

**4. Sharp unshifted boundary.** For \(h=0\), Moss and Ward's Corollary 3 proves that \((5F_{n^{2k}})_{n\ge1}\) is realizable for all \(k\ge1\). To see that five is necessary, use \(n=5\): the Fibonacci sequence modulo five has period \(20\), so \(F_{5^{2k}}\equiv0\pmod5\), whereas \(F_1=1\). (Equivalently apply their Lemma 6 repeatedly.) Hence the Dold condition for multiplier \(M\) forces \(5\mid M\). The least such positive integer is \(M=5\), which works by the cited theorem. This completes the classification.

## Verification

The standalone `verify.py` checks the matrix Frobenius congruences for inert primes, the even-binomial parity identity, the Fibonacci shift congruence by independent modular methods, the positivity of selected \(\Delta_{h,k}\), and the necessity of the factor five in the unshifted cases. Run `python3 verify.py`. All these computations are finite consistency checks; the proof for infinitely many primes depends instead on the matrix identities and Dirichlet's theorem.

## Relationship to prior work

Moss and Ward [1], first posted on 26 November 2020, proved the unshifted almost-realizability result, including the multiplier five, and obstruction for odd powers. Their inspected article explicitly treats monomial samples, not arbitrary positive translations of those monomials. Luca and Ward [2] prove broad sufficiency for monomial time changes of linear recurrences, not almost-realizability for shifted powers. Jaidee, Moss and Ward [3] classify polynomials preserving realizability for **all** starting realizable sequences; this universal-property result does not decide the particular Fibonacci sequence after multiplication by an arbitrary constant. OEIS A054783 [4] tabulates unshifted square-index Fibonacci numbers, but is not a translated-power no-repair theorem. The present result is the complete translation dichotomy for the Fibonacci even-power family. Searches did not identify a covering statement; undiscovered equivalent literature remains possible.

## Limitations

The result classifies only the family \(F_{(n+h)^{2k}}\) with nonnegative integral translations and even positive power exponents. It does not claim a corresponding classification for arbitrary integral polynomials, arbitrary recurrence sequences, or negative shifts. It relies on the published positive theorem for \(h=0\) and Dirichlet's theorem for the infinite prime supply. A finite computational check is not an independent verification of the proof or of bibliographic priority.

## References

[1] P. Moss and T. Ward, *Fibonacci along even powers is (almost) realizable*, arXiv:2011.13068v1 (26 November 2020), Theorem 2 and Corollary 3. https://arxiv.org/html/2011.13068v1

[2] F. Luca and T. Ward, *On (almost) realizable subsequences of linearly recurrent sequences*, arXiv:2204.02711 (first version 6 April 2022), Theorem 1. https://arxiv.org/abs/2204.02711

[3] S. Jaidee, P. Moss and T. Ward, *Time-changes preserving zeta functions*, arXiv:1809.09199 (first version 24 September 2018), Theorem 5. https://arxiv.org/abs/1809.09199

[4] OEIS A054783, *\((n^2)\)-th Fibonacci number*. https://oeis.org/A054783
