# Exact cubic-window GCDs of Pell numbers

## Finding

Let \(P_0=0\), \(P_1=1\), and \(P_{n+2}=2P_{n+1}+P_n\) for every integer \(n\geq0\). Let \(Q_0=Q_1=1\), \(Q_{n+2}=2Q_{n+1}+Q_n\). For every integer \(k\geq1\), write
\[
H_3(k)=\gcd_{n\geq0}\left(\sum_{j=0}^{k-1}P_{n+j}^{3}\right).
\]
Then \(H_3(k)=1\) for every odd \(k\). For every even \(k=2r\), with integer \(r\geq1\), put
\[
T_r=\begin{cases}P_r,&r\text{ even},\\ Q_r,&r\text{ odd}.\end{cases}
\]
The exact formula is
\[
\boxed{H_3(2r)=\frac{T_r}{7^{[3\mid r]}}\,3^{[4\mid r]}.}
\]
The bracketed expressions are indicator exponents, equal to one when their conditions hold and zero otherwise. In particular \(7\mid T_r\) if and only if \(3\mid r\), so the displayed quotient is always an integer. No asymptotic or upper-bound restriction on \(k\) is imposed.

## Assumptions and scope

All gcds are positive gcds of integer sets. The sliding windows begin at every nonnegative index, including the initial zero term. These are the classical Pell numbers and *associated* Pell numbers, with the latter normalized by \(Q_0=Q_1=1\). The assertion concerns cubes of Pell terms, not sums of unpowered terms, squares, arbitrary initial conditions, or cubes of associated Pell terms.

## Proof

**1. Basic Pell algebra.** Put \(M=\left(\begin{smallmatrix}0&1\\1&2\end{smallmatrix}\right)\). Matrix induction gives
\[
M^r=\begin{pmatrix}Q_r-P_r&P_r\\P_r&Q_r+P_r\end{pmatrix},\qquad
Q_r^2-2P_r^2=(-1)^r.
\]
The second identity gives \(\gcd(P_r,Q_r)=1\), and \(Q_r\) is always odd. Cassini's identity reads
\[
P_{k-1}P_{k+1}-P_k^2=(-1)^k.
\]
For \(k=2r\), let \(t=T_r\) and let \(w=Q_r\) when \(r\) is even, and \(w=P_r\) when \(r\) is odd. Squaring the first displayed matrix and using the norm identity gives
\[
M^{2r}=I+2tB,\qquad
B=\begin{cases}
\begin{pmatrix}2t-w&w\\w&2t+w\end{pmatrix},&r\text{ even},\\[3pt]
\begin{pmatrix}t-w&w\\w&t+w\end{pmatrix},&r\text{ odd}.
\end{cases}
\]
In both cases the entries of \(B\) have gcd one. In the even case this follows from the oddness of \(w\) and \(\gcd(t,w)=1\); in the odd case it follows immediately from \(\gcd(t,w)=1\). Thus the gcd of the four entries of \(M^{2r}-I\) is \(2t\).

**2. All possible prime divisors.** Set \(S_n(k)=\sum_{j=0}^{k-1}P_{n+j}^3\). If an odd prime \(\ell\) divides every \(S_n(k)\), subtracting two consecutive windows shows that \(\ell\mid P_k\), and then \(P_{k+1}^3\equiv1\pmod\ell\). Write \(a=P_{k+1}\pmod\ell\). As \(P_k\equiv0\pmod\ell\), Cassini gives \(a^2\equiv(-1)^k\pmod\ell\), while \(a^3\equiv1\pmod\ell\). If \(k\) is odd, these are inconsistent for odd \(\ell\), because their sixth powers would imply \(-1\equiv1\pmod\ell\). If \(k=2r\), they force \(a\equiv1\pmod\ell\). Consequently \(M^k\equiv I\pmod\ell\), and Step 1 forces \(\ell\mid t\).

Modulo two, \(P_n\equiv n\pmod2\). Every odd-length window family contains an odd sum, and therefore \(H_3(k)=1\) when \(k\) is odd. For an even length \(k=2r\), all windows have parity \(r\). Therefore a factor two in the gcd is possible only when \(r\) is even; in that case \(t=P_r\) is even.

**3. An integral cubic antidifference.** Define
\[
A(x,y)=-16x^3-3x^2y+9xy^2-2y^3.
\]
Direct expansion proves the polynomial identity
\[
A(y,x+2y)-A(x,y)=14x^3
\]
for arbitrary integers \(x,y\). If \(v_n=(P_n,P_{n+1})^{\mathsf T}\), telescoping gives
\[
14S_n(2r)=A(M^{2r}v_n)-A(v_n).
\]
Use the matrix \(B\) from Step 1, and define the integer polynomial
\[
\Phi(t,w;x,y)=\frac{A\big((I+2tB)(x,y)^{\mathsf T}\big)-A(x,y)}{2t}.
\]
The quotient is a polynomial with **integer coefficients**, because every coordinate increment is divisible by \(2t\); it is defined at \(t=0\) by this polynomial extension. It follows for every \(n\geq0\) that
\[
7S_n(2r)=t\,\Phi(t,w;P_n,P_{n+1}). \tag{1}
\]
At \(t=0\), both definitions of \(B\) become \(w\left(\begin{smallmatrix}-1&1\\1&1\end{smallmatrix}\right)\). Taking the first-order term in \(t\) yields the *polynomial congruence*
\[
\Phi(t,w;x,y)\equiv
3w(15x^3-9x^2y-xy^2+y^3)\pmod t.\tag{2}
\]
In particular, since \(v_0=(0,1)^{\mathsf T}\),
\[
\Phi(t,w;0,1)\equiv3w\pmod t.\tag{3}
\]
These congruences are literal integer-polynomial divisibilities, not assumptions about the invertibility of \(t\).

**4. Exact valuations away from three.** Identity (1) proves that \(t/\gcd(t,7)\) divides every window sum. Fix a prime \(\ell\mid t\) with \(\ell\ne3\). Since \(\gcd(t,w)=1\), (3) implies \(\ell\nmid\Phi(t,w;0,1)\). Hence (1) gives
\[
\nu_\ell(S_0(2r))=\nu_\ell(t)-[\ell=7].
\]
This is also the *lower* valuation bound for every \(S_n(2r)\) by (1), so the gcd has precisely that valuation. This covers \(\ell=2\) whenever \(2\mid t\). A prime not dividing \(t\) cannot divide the gcd by Step 2 (and its parity argument). Thus the only possible additional factor comes from three.

**5. The exact additional factor three.** When \(r\) is odd, \(t=Q_r\) is not divisible by three: the norm relation would require \(2w^2\equiv1\pmod3\) if \(t\equiv0\). When \(r\) is even, \(t=P_r\), and the recurrence modulo three has period eight with zeros precisely at multiples of four. Thus \(3\mid t\) if and only if \(4\mid r\).

Suppose \(4\mid r\). Since \(3\mid t\), congruence (2) shows that \(3\mid\Phi(t,w;P_n,P_{n+1})\) for **every** \(n\geq0\). Therefore \(3^{\nu_3(t)+1}\) divides every window sum. To prove sharpness, expand the explicit polynomial at \((x,y)=(0,1)\) using the even-\(r\) matrix:
\[
\Phi(t,w;0,1)=3w+t(18w^2-12)+t^2R(t,w),
\]
where \(R\) is an integer polynomial. If \(3\mid t\), the right side is congruent to \(3w\pmod9\). As \(3\nmid w\), the first window sum has precisely one power of three beyond those already present in \(t\). This establishes the factor \(3^{[4\mid r]}\).

**6. The factor seven.** The Pell recurrence modulo seven shows that \(P_n\) has period six and vanishes exactly for \(n\equiv0\pmod6\), whereas \(Q_n\) has period six and vanishes exactly for \(n\equiv3\pmod6\). Therefore \(7\mid T_r\) if and only if \(3\mid r\). Step 4 shows that the power of seven in the gcd is exactly one less than its power in \(T_r\). Together with Steps 2–5 this proves the displayed formula for every \(k\geq1\). \(\square\)

## Verification

Run `python3 verify.py` using Python 3 and the standard library. The output in `verification_output.txt` was reproduced from the exact source in this package. The tests independently compute \(\gcd(S_0(k),S_1(k),S_2(k),S_3(k))\) for every \(1\le k\le480\), check \(7200\) additional window divisibilities, verify the Pell matrix formula and the polynomial congruence, and test the fourth-order recurrence
\[
P_{n+4}^3=12P_{n+3}^3+30P_{n+2}^3-12P_{n+1}^3-P_n^3.
\]
That monic recurrence proves for every fixed \(k\) that the gcd of the first four windows is the infinite gcd. The finite checks are not used in place of the unrestricted proof above.

## Relationship to prior work

Mbirika, Schrader, and Spilker (2023), arXiv:2301.05758, explicitly define gcds of windows of arbitrary powers of Pell and related sequences. Their Theorems 15–19 concern first powers; their Section 6, Partial Result 29, gives squares for Pell and associated Pell sequences. They do not state the cubic Pell formula above. The same paper has primary MSC2020 classification 11B39. Anand and collaborators (arXiv:2407.12868, first released July 2024) study sums of *unpowered* consecutive Pell terms and fixed-multiple identities rather than gcds of cubic windows. The earlier Fibonacci cubic-window literature uses the recurrence with coefficient one, not the Pell coefficient two; its conclusions do not specialize to the displayed formula. This result is therefore a separate Pell-specific cubic classification, not a relabeling of an established Pell first-power or square-power identity.

## Limitations

The theorem is restricted to the classical Pell recurrence and cubic powers. It does not give a universal formula for all generalized Lucas sequences, for cubes of associated Pell numbers, or for fourth and higher powers. The literature comparison covers the primary works listed below and targeted searches, but an equivalent result in other or unindexed literature remains possible. All numerical verifications are finite checks; the infinite result rests on the polynomial and valuation proof.

## References

1. aBa Mbirika, Janee Schrader, Jürgen Spilker, *Pell and Associated Pell Braid Sequences as GCDs of Sums of k Consecutive Pell, Balancing, and Related Numbers*, Journal of Integer Sequences 26 (2023), Article 23.6.4. First arXiv version January 13, 2023, arXiv:2301.05758. Full text: https://cs.uwaterloo.ca/journals/JIS/VOL26/Mbirika/mbir5.pdf.
2. Navvye Anand et al., *Sum of Consecutive Terms of Pell and Related Sequences*, first arXiv version July 13, 2024, arXiv:2407.12868. https://arxiv.org/abs/2407.12868.
3. aBa Mbirika and Jürgen Spilker, *GCD of sums of k consecutive squares of generalized Fibonacci numbers*, Fibonacci Quarterly 60 (2022), 255–269, arXiv:2204.12626. https://arxiv.org/abs/2204.12626.
4. OEIS A000129 and A001333, classical Pell and associated Pell sequences; their term tables and recurrences provide numerical baseline checks. https://oeis.org/A000129 and https://oeis.org/A001333.
