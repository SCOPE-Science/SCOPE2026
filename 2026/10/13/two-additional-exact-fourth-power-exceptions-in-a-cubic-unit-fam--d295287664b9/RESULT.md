# Two additional exact fourth-power exceptions in a cubic-unit family
## Finding
For the cubic family \(K_b=\mathbb{Q}(\theta)\), where \(\theta\) is the unique real root of
\[
X^3-3bX-b^3,
\]
and
\[
\eta_b=((b+1)-\theta)^{-1}>1,
\]
the published square-exceptions \(b=5\) and \(b=96\) have exact positive-unit exponent \(4\).

Let \(\gamma_5\) be the real root greater than \(1\) of
\[
g_5(X)=X^3-3X^2-1,
\]
and let \(\gamma_{96}\) be the real root greater than \(1\) of
\[
g_{96}(X)=X^3-13X^2+X-1.
\]
Then
\[
\eta_5=\gamma_5^4,\qquad \eta_{96}=\gamma_{96}^4,
\]
and each \(\gamma_b\) is the fundamental unit of \(K_b\). Hence
\[
R_{K_5}=\frac14\log \eta_5,\qquad
R_{K_{96}}=\frac14\log \eta_{96}.
\]

## Assumptions and scope
The claim concerns only the two parameters \(b=5\) and \(b=96\). It does not classify all fourth powers in the Pell-parametrized square-exception set. The source establishes that these two parameters are square-exceptions and supplies the index formulas and Artin discriminant inequality used below.

For a monic cubic unit polynomial
\[
G(X)=X^3-DX^2+CX-1,
\]
write \(r_1,r_2,r_3\) for its roots. Newton's identities show that the monic polynomial with roots \(r_1^2,r_2^2,r_3^2\) is
\[
X^3-(D^2-2C)X^2+(C^2-2D)X-1.
\]
This squaring transform is used twice.

## Proof
For \(b=5\), take \((C,D)=(0,3)\). One squaring transform gives
\[
(A,B)=(C^2-2D,D^2-2C)=(-6,9).
\]
A second transform gives
\[
B^2-2A=93,\qquad A^2-2B=18.
\]
The source gives the minimal polynomial of \(\eta_b\) as
\[
H_b(X)=X^3-3(b^2+b+1)X^2+3(b+1)X-1.
\]
At \(b=5\), this is \(X^3-93X^2+18X-1\), exactly the polynomial obtained from \(g_5\) after two squarings. Since \(g_5(3)<0<g_5(4)\), its relevant real root satisfies \(3<\gamma_5<4\). Thus \(\gamma_5^4>1\) is the real root of \(H_5\), so \(\eta_5=\gamma_5^4\).

For \(b=96\), take \((C,D)=(1,13)\). The first transform gives
\[
(A,B)=(-25,167),
\]
and the second gives
\[
B^2-2A=27939,\qquad A^2-2B=291.
\]
These equal \(3(96^2+96+1)\) and \(3(96+1)\), respectively. Also \(g_{96}(12)<0<g_{96}(13)\), so \(12<\gamma_{96}<13\), and again the unique real root comparison gives \(\eta_{96}=\gamma_{96}^4\).

It remains to prove that the two fourth roots are fundamental. The source's prime-by-prime index formulas give
\[
[O_{K_5}:\mathbb{Z}[\theta]]=5\cdot11=55,
\]
because \(5\mid b\) to the first power and \(5^3-4=11^2\). Hence
\[
D_{K_5}=\frac{-27\cdot5^3(5^3-4)}{55^2}=-135.
\]
For \(b=96=2^5\cdot3\), one has
\[
96^3-4=2^2\cdot29^2\cdot263,
\]
and the same formulas give
\[
[O_{K_{96}}:\mathbb{Z}[\theta]]=2^7\cdot3^3\cdot29,
\]
so
\[
D_{K_{96}}=-2104.
\]

Suppose one of the units \(\gamma_b\) were not fundamental. Since the unit rank is one, \(\gamma_b=u^q\) for a unit \(u>1\) and a prime \(q\ge2\). Then \(u\le\gamma_b^{1/2}\). Artin's inequality from the source gives
\[
|D_{K_b}|\le4u^3+24\le4\gamma_b^{3/2}+24.
\]
For \(b=5\), \(\gamma_5<4\), so the right side is less than \(56\), contradicting \(|D_{K_5}|=135\). For \(b=96\), \(\gamma_{96}<13<16\), so \(\gamma_{96}^{3/2}<52\) and the right side is less than \(232\), contradicting \(|D_{K_{96}}|=2104\). Thus both \(\gamma_5\) and \(\gamma_{96}\) are fundamental, proving exact exponent \(4\).

## Verification
The standalone script `verify.py` uses exact integer arithmetic. It replays the two coefficient-squaring chains, the source's index formulas at the relevant primes, both field discriminants, the rational root brackets, irreducibility checks, and the integer inequalities sufficient for the Artin contradiction. Its recorded output is:

`VERIFY_OK cases=2 exact_fourth_powers=2 fundamental_units=2`

## Relationship to prior work
Kimura and Umemoto classify all parameters for which \(\eta_b\) is a square by a Pell equation. Their Theorem 5.2 explicitly lists \(5\) and \(96\) among the first positive square-exceptions, and the accompanying numerical statement says that the displayed examples have even order under a unit computation. The source does not give the exact exponents for \(b=5\) or \(b=96\). In Remark 5.6 it does give exact exponents for three different exceptional parameters, including the fourth-power identity at \(b=-75\), so the distinction between “square” and “exact fourth power” is already mathematically meaningful in the source's framework.

The present calculation supplies two additional exact fourth-power cases and proves that their fourth roots are the actual fundamental units, not merely units. Thus the source's general square-exception regulator bound \(R_{K_b}\le\tfrac12\log\eta_b\) sharpens at these two parameters to the exact quarter-log identities above.

## Limitations
No assertion is made that \(b=5\) and \(b=96\) are the only further fourth-power parameters. The proof is parameter-specific after the general coefficient-squaring identity. It uses the source's published index formulas and Artin inequality, but all substitutions and inequalities needed for these two parameters are replayed exactly in the included verifier.

## References
Iwao Kimura and Hikaru Umemoto, *On an infinite family of cubic fields with explicit fundamental units*, arXiv:2609.37389v1, 2026. Relevant parts: Proposition 2.1 and Lemma 2.2; Theorems 3.3 and 3.5; Lemma 4.1; Theorem 5.2 and Remark 5.6.
