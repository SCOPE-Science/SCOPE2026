# The first quaternary row of Table 2 is not constacyclic as printed
## Finding

Debnath--Islam--Yadav--Prakash list in the first row of Table 2
\[
\ell=1,\qquad \lambda=\omega,\qquad (1,\omega,1,1,1),
\]
with classical parameters
\[
[10,6,4]_4,
\]
\(1\)-Galois hull dimension \(2\), and the almost-EAQMDS parameters
\[
[[10,4,4;2]]_4.
\]

For the printed coefficient tuple, the claimed constacyclic generator condition fails. With the natural constant-to-leading coefficient convention,
\[
g(x)=1+\omega x+x^2+x^3+x^4,
\]
and with \(\mathbb F_4=\mathbb F_2(\omega)\), \(\omega^2=\omega+1\), exact division gives
\[
(x^{10}-\omega)\bmod g(x)
=
1+\omega^2x+\omega x^3,
\]
which is nonzero. Reading the same tuple in the opposite coefficient order also gives a nonzero remainder:
\[
(x^{10}-\omega)\bmod
(x^4+\omega x^3+x^2+x+1)
=
\omega+\omega x+\omega^2x^2+\omega^2x^3.
\]

Thus neither conventional reading of the printed tuple defines the monic divisor of \(x^{10}-\omega\) required for an \(\omega\)-constacyclic code.

As a further consistency check, if the listed-order polynomial is treated simply as a length-\(10\) seed and its six unwrapped shifts are spanned over \(\mathbb F_4\), the resulting code has exact parameters
\[
[10,6,3]_4
\]
and Hermitian hull dimension \(0\). Its weight distribution is
\[
1+12z^3+57z^4+246z^5+645z^6+960z^7+1158z^8+798z^9+219z^{10}.
\]
This ordinary shift span is not asserted to be the authors' intended replacement code; it only demonstrates that the printed coefficients do not accidentally reproduce the advertised distance and hull data under the most direct linear interpretation.

Consequently the first row of Table 2, and the associated
\[
[[10,4,4;2]]_4
\]
EAQECC application, are not certified by the generator printed in that row.

## Assumptions and scope

The field convention is the one used in the paper:
\[
\mathbb F_4=\mathbb F_2(\omega),
\]
where \(\omega\) is primitive. Hence
\[
\omega^2=\omega+1,\qquad \omega^3=1.
\]

The claim is restricted to the first row of Table 2 as printed. It does not claim that no \([10,6,4]_4\) code with \(1\)-Galois hull dimension \(2\) exists, nor that an EAQECC with parameters \([[10,4,4;2]]_4\) is impossible by another construction.

The phrase “reverse coefficient convention” is included only to remove tuple-order ambiguity: the divisibility test fails in both directions.

## Proof

The paper's Theorem 2.1 states that a length-\(n\) \(\lambda\)-constacyclic code is an ideal in
\[
\mathbb F_q[x]/\langle x^n-\lambda\rangle
\]
and that its unique monic generator \(g(x)\) satisfies
\[
g(x)\mid x^n-\lambda.
\]

For the first Table 2 row,
\[
q=4,\qquad n=10,\qquad \lambda=\omega.
\]
Since the characteristic is two,
\[
x^{10}-\omega=x^{10}+\omega.
\]
Direct polynomial division of
\[
x^{10}+\omega
\]
by
\[
1+\omega x+x^2+x^3+x^4
\]
in \(\mathbb F_4[x]\) has remainder
\[
1+\omega^2x+\omega x^3.
\]
The remainder is nonzero, so the printed polynomial does not divide the constacyclic modulus.

If the tuple is instead read in reverse,
\[
g_{\mathrm{rev}}(x)=x^4+\omega x^3+x^2+x+1,
\]
then exact division gives the nonzero remainder
\[
\omega+\omega x+\omega^2x^2+\omega^2x^3.
\]
Thus coefficient order cannot repair the displayed row.

For the auxiliary ordinary shift-span check, form the six vectors corresponding to
\[
g(x),\,xg(x),\,\ldots,\,x^5g(x)
\]
without cyclic wrap. Their \(6\times10\) generator matrix has rank \(6\). Exhausting all
\[
4^6=4096
\]
linear combinations gives minimum distance \(3\) and the displayed weight enumerator.

For \(\ell=1\) over \(\mathbb F_4\), the Galois inner product is the Hermitian product
\[
\langle a,b\rangle_1=\sum_i a_i b_i^2.
\]
The Hermitian Gram matrix of the six shift rows has rank \(6\). Therefore the hull dimension is
\[
6-\operatorname{rank}(GG^\dagger)=0.
\]

## Verification

`artifacts/verify.py` uses only the Python standard library. It constructs \(\mathbb F_4\) as
\[
\mathbb F_2[\omega]/(\omega^2+\omega+1),
\]
performs both polynomial divisions exactly, and checks the two nonzero remainders.

It then constructs the six ordinary unwrapped shifts of the listed-order polynomial, verifies rank \(6\), enumerates all \(4096\) codewords, and checks minimum distance \(3\) and the complete weight distribution. Finally it forms the Hermitian Gram matrix and verifies rank \(6\), hence hull dimension \(0\).

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

The primary article itself supplies the decisive comparison. Its Theorem 2.1 requires the generator polynomial of a constacyclic code to divide the modulus \(x^n-\lambda\). Its Example 3.7 also works over the same field with \(n=10\) and \(\lambda=\omega\), explicitly factoring
\[
x^{10}-\omega
\]
before choosing a generator. Table 2 later labels the disputed row as an optimal constacyclic code and uses its distance and hull dimension to produce an almost-EAQMDS code.

Focused searches by DOI, title, exact classical parameters, exact quantum parameters, printed generator tuple, and correction-or-erratum terminology did not locate a public correction of this row. Searches for broader Galois-hull constructions found related families, but none supplies an implication that would make a non-divisor into a valid constacyclic generator.

The ordinary \([10,6,3]_4\) shift span is included only as a reproducibility check; the main contradiction is the exact divisibility failure against the paper's own generator criterion.

## Limitations

A typographical error in the printed tuple could explain the discrepancy. If the intended polynomial differs from the displayed coefficients, that intended code must be analyzed separately.

The result does not audit the other rows of Table 2 or the general small-hull existence theorems.

The absence of a public correction in the inspected sources is not a proof that no unpublished correction exists.

## References

1. Indibar Debnath, Habibul Islam, Shikha Yadav, and Om Prakash, *Study of small Galois hull dimensions of constacyclic codes*, Advances in Mathematics of Communications 22 (2026), 1--18, DOI 10.3934/amc.2025054.
2. M. M. Wilde and T. A. Brun, *Optimal entanglement formulas for entanglement-assisted quantum coding*, Physical Review A 77 (2008), 064302.
