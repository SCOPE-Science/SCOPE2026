# A harmonic sharpening of the affine factorial perfect-power bound
## Finding
For every prime-power integer \(m\ge2\), Yudin's Appendix-A affine construction can be run with
\[
R=\left\lceil e^{m-\gamma}\right\rceil,
\qquad R_0=R+\pi(R),
\qquad K=1+(m-1)R_0,
\]
where \(\gamma\) is Euler's constant. It then produces distinct affine functions \(F_1,\ldots,F_N\), with positive leading coefficients, such that for every sufficiently large integer \(t\),
\[
\prod_{i=1}^N F_i(t)!
\]
is a perfect \(m\)-th power, and
\[
N\le m\bigl(1+(m-1)(R+\pi(R))\bigr).
\]
Hence, as \(m\to\infty\) through prime powers,
\[
N\le \bigl(e^{-\gamma}+o(1)\bigr)m(m-1)e^m.
\]
The coefficient \(e^{-\gamma}\) replaces the coefficient \(2\) in the explicit prime-power bound stated in Theorem A.1 of arXiv:2610.01899v1. Equivalently, the ratio of the two leading envelopes is \(e^{-\gamma}/2=0.2807297\ldots\).

Within the harmonic-number sufficient-condition relaxation of the same zero-sum proof, this leading constant is asymptotically optimal: if \(H_R=m-1+s+o(1)\) with fixed \(s>0\), the leading coefficient is \(e^{s-1-\gamma}/s\), uniquely minimized at \(s=1\).

## Assumptions and scope
The exponent \(m\) is a prime power. This is exactly the branch in which Olson's formula gives the Davenport constant
\[
D(C_m^r)=1+r(m-1).
\]
The construction, the row vectors, and the implication from a zero-sum subsequence to a product of distinct factorials are those of Appendix A of arXiv:2610.01899v1. Only its numerical parameter choice is changed.

Write
\[
H_R=\sum_{\ell=1}^R\frac1\ell.
\]
The proof uses the elementary strict inequality \(H_R>\log R+\gamma\) for every finite \(R\). The prime number theorem is used only for the displayed asymptotic \(\pi(R)=o(R)\), not for the finite bound.

No claim is made that the resulting \(N\) is the least possible number of factorials among all constructions, or even among all exact parameter choices in Appendix A. The optimality statement concerns only the leading envelope obtained from the harmonic-number sufficient condition described below.

## Proof
In Yudin's construction, for positive integers \(R,K\), the number of available row vectors is
\[
M_0=\sum_{\ell=1}^R\left(\left\lfloor\frac K\ell\right\rfloor+1\right),
\]
and they lie in \(C_m^r\) with
\[
r=K+R+\pi(R)=K+R_0.
\]
For prime-power \(m\), Olson's theorem gives
\[
D(C_m^r)=1+(m-1)(K+R_0).
\]
A zero-sum subsequence therefore exists as soon as \(M_0\ge D(C_m^r)\).

For every positive real \(x\), \(\lfloor x\rfloor+1>x\). Hence
\[
M_0>K H_R.
\]
The sequence \(H_n-\log n\) decreases strictly to \(\gamma\): indeed
\[
(H_{n+1}-\log(n+1))-(H_n-\log n)
=\frac1{n+1}-\log\left(1+\frac1n\right)<0,
\]
because \(\log(1+x)>x/(1+x)\) for \(x>0\). Thus
\[
H_R>\log R+\gamma.
\]
With \(R=\lceil e^{m-\gamma}\rceil\), one has \(\log R+\gamma\ge m\), and therefore \(H_R>m\).

Now choose \(K=1+(m-1)R_0\). Then
\[
1+(m-1)(K+R_0)=mK.
\]
Consequently
\[
M_0>K H_R>mK=D(C_m^r).
\]
The zero-sum step in Appendix A applies. Its selected row counts are multiples of \(m\), so the number \(N\) of selected factorials is a multiple of \(m\); in particular the construction gives
\[
N\le D(C_m^r)=mK
=m\bigl(1+(m-1)(R+\pi(R))\bigr).
\]
This proves the finite bound.

For the asymptotic, \(R=e^{m-\gamma}(1+o(1))\) and \(\pi(R)=o(R)\). Therefore
\[
m\bigl(1+(m-1)(R+\pi(R))\bigr)
=\bigl(e^{-\gamma}+o(1)\bigr)m(m-1)e^m.
\]

Finally, consider the same proof after replacing the exact row count by the sufficient lower bound \(M_0>K H_R\). Put \(H_R=m-1+s+o(1)\), with fixed \(s>0\). The sufficient inequality forces asymptotically \(K\gtrsim (m-1)R/s\), while
\[
R=e^{m-1-\gamma+s+o(1)}.
\]
The leading contribution to the Davenport threshold is then
\[
\frac{e^{s-1-\gamma}}s\,m(m-1)e^m.
\]
The function \(e^s/s\) has its unique minimum for \(s>0\) at \(s=1\), giving the coefficient \(e^{-\gamma}\). This proves the stated within-method asymptotic optimality.

## Verification
The accompanying `verify.py` independently evaluates the exact integer quantities \(R\), \(\pi(R)\), \(K\), \(D(C_m^r)\), and \(M_0\) for the prime powers
\[
2,3,4,5,7,8,9,11,13.
\]
For every sample it checks \(D(C_m^r)=mK\), \(M_0>D(C_m^r)\), and strict improvement over the source's stated bound. The replay output begins `VERIFY_OK samples=9 max_m=13`. These finite checks are consistency tests; the infinite statement follows from the proof above.

## Relationship to prior work
Yudin's Theorem A.1 proves the existence, for every \(m\ge2\), of a bounded affine family of distinct factorials whose product is an \(m\)-th power. In the prime-power branch it states
\[
N\le2m(m-1)\lceil e^m\rceil.
\]
Its proof already contains the row count \(M_0\), the dimension \(r=K+R+\pi(R)\), and Olson's exact Davenport constant. The present result uses those same ingredients but retains the Euler-constant term in the harmonic-number estimate and balances the proof parameters at \(H_R\approx m\).

Bérczes, Dujella, Hajdu, Saradha and Tijdeman study perfect powers formed from products of factorials, including products of distinct factorials with a fixed largest argument. Their Theorem 4.2 gives infinitely many perfect cubes using fewer than \(1.5\log n\) factors when the largest argument is \(n\). That problem has factor count growing with the largest argument, rather than a fixed affine family whose factor count depends only on \(m\), so it neither implies nor is implied by the bound above.

A separate prior result derived from the same recent source classifies four-factor affine square families. It concerns exact structural classification when \(m=2\) and \(N=4\); it does not bound the number of factors produced by Appendix A for general prime-power \(m\), and the present bound does not subsume that classification.

## Limitations
The explicit bound is proved only for prime-power \(m\), because it uses Olson's exact formula for \(D(C_m^r)\). It does not improve the general-composite branch of Theorem A.1. The construction is existential and retains the source's eventual-distinctness threshold for the affine arguments.

The coefficient \(e^{-\gamma}\) is optimal only for the harmonic-number sufficient-condition relaxation of this particular zero-sum parameter scheme. Using the exact floor sum \(M_0\), a sharper Davenport estimate in another group, or a different construction could lower the factor count further.

## References
1. F. Yudin, *Square products of factorials and a conjecture of Erdős and Graham*, arXiv:2610.01899v1, 1 October 2026. Primary MSC 11D85. See Appendix A, especially Theorem A.1 and its prime-power proof.
2. A. Bérczes, A. Dujella, L. Hajdu, N. Saradha, R. Tijdeman, *Products of factorials which are powers*, Acta Arith. 190 (2019), 339–350. See Section 4 and Theorem 4.2.
3. J. E. Olson, the Davenport-constant theorem for finite abelian \(p\)-groups used in Appendix A of reference 1.
