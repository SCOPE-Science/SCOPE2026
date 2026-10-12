# Exact \(7\)-adic orders and persistent residue classes for \(1+2^n+3^n\)

## Finding
For every integer \(n\ge1\), set \(S(n)=1+2^n+3^n\). Its exact \(7\)-adic valuation is
\[
\nu_7(S(n))=\begin{cases}
0,&n\not\equiv2,4\pmod6,\\
1+\nu_7(n),&n\equiv2\pmod6,\\
2+\nu_7(n)+\nu_7(n-1),&n\equiv4\pmod6.
\end{cases}
\]
Moreover, for every integer \(k\ge1\), the count
\[
R_k=\#\{0\le n<6\cdot7^{k-1}:\ 7^k\mid S(n)\}
\]
is exactly \(R_1=2\), \(R_2=8\), and \(R_k=15\) for all \(k\ge3\). The interval is a common period of both exponential terms modulo \(7^k\); its minimality is not needed.

## Assumptions and scope
The exponent \(n\) is a positive ordinary integer, and \(\nu_7(m)\) is the largest nonnegative integer \(e\) such that \(7^e\mid m\), defined here for nonzero ordinary integers \(m\). All occurrences of \(n\) and \(n-1\) inside valuations have nonzero arguments in the relevant residue cases. Auxiliary analytic arguments take values in \(\mathbb Z_7\). No assertion is made about other primes or about arbitrary sums of three exponentials.

## Proof
**Integral interpolation.** For \(t\in\mathbb Z_7\), define \(U(t)=64^t\) and \(V(t)=729^t\) by their convergent binomial expansions
\[
U(t)=\sum_{j\ge0}\binom tj63^j,\qquad
V(t)=\sum_{j\ge0}\binom tj728^j.
\]
These agree with integer powers at nonnegative integer arguments. Their coefficients in the ordinary monomial variable tend \(7\)-adically to zero, so they are restricted integral power series. In particular, divided differences of such series in two \(7\)-adic arguments remain integral.

For \(n=6t+r\) with \(r\in\{0,1,2,3,4,5\}\) and \(t\ge0\), write \(F_r(t)=1+2^rU(t)+3^rV(t)\). Reduction modulo \(7\) gives the values of \(1+2^r+3^r\), namely \(3,6,0,1,0,3\) for \(r=0,1,2,3,4,5\). Hence only \(r=2,4\) can give positive valuation.

**The class \(r=2\).** Set
\[
H_2(t)=\frac{F_2(t)}7=\frac{1+4U(t)+9V(t)}7.
\]
The constant term is \(2\); the linear coefficient is \((4\cdot63+9\cdot728)/7=972\equiv6\pmod7\). Every term of binomial degree at least \(2\) has ordinary monomial coefficients divisible by \(7\): the relevant bound is \(j-1-\nu_7(j!)\ge1\) for \(j\ge2\). Thus \(H_2\) is a restricted integral power series with
\[
H_2(t)\equiv2+6t=6(t-2)\pmod7.
\]
It has an exact zero at \(t=-1/3\in\mathbb Z_7\). Indeed, \(A=4U(-1/3)\) and \(B=9V(-1/3)\) satisfy \(A^3=B^3=1\), with \(A\equiv4\) and \(B\equiv2\pmod7\). They are the two distinct nontrivial cube roots of unity in \(\mathbb Z_7\), so \(A+B=-1\). Because the coefficient of \(t\) in the reduction of \(H_2\) is a unit, the divided difference of \(H_2(t)-H_2(-1/3)\) by \(t+1/3\) is a \(7\)-adic unit for every \(t\in\mathbb Z_7\). Consequently
\[
\nu_7(F_2(t))=1+\nu_7(t+1/3)=1+\nu_7(6t+2).
\]

**The class \(r=4\).** Set
\[
H_4(t)=\frac{F_4(t)}{49}=\frac{1+16U(t)+81V(t)}{49}.
\]
This is again a restricted integral power series: its constant is \(98/49=2\), its first coefficient is \((16\cdot63+81\cdot728)/49=1224\equiv6\pmod7\), and its binomial-degree-two coefficient is \((16\cdot63^2+81\cdot728^2)/49=877392\equiv5\pmod7\). Terms of binomial degree \(j\ge3\) have ordinary monomial coefficients divisible by \(7\), using \(j-2-\nu_7(j!)\ge1\). Therefore
\[
H_4(t)\equiv2+6t+5\binom t2\equiv2+6t^2
\equiv6(t-3)(t-4)\pmod7.
\]
Both roots are simple. Their exact \(7\)-adic lifts can be written explicitly:
\[
H_4(-1/2)=H_4(-2/3)=0.
\]
For the first equality, \(8\equiv1\pmod7\) and \(-27\equiv1\pmod7\), so \(U(-1/2)=1/8\) and \(V(-1/2)=-1/27\), giving \(F_4(-1/2)=1+2-3=0\). For the second, the elements \(C=16U(-2/3)\) and \(D=81V(-2/3)\) satisfy \(C^3=D^3=1\) and have distinct nontrivial residues \(2\) and \(4\) modulo \(7\); hence \(C+D=-1\). The two exact roots lie in the distinct residue classes \(-1/2\equiv3\) and \(-2/3\equiv4\pmod7\).

We use the elementary simple-root valuation principle: if a restricted integral power series reduces to a polynomial with distinct simple roots modulo \(7\), and each such root has a known zero in \(\mathbb Z_7\), then its valuation at any \(t\in\mathbb Z_7\) equals the sum of the valuations of the differences from those lifted zeros. To prove it, outside all root classes the series is a unit. Inside one root class, the quotient of the series difference by the argument difference is integral and reduces to the nonzero derivative at that root; all other root differences are units. Applying this principle yields
\[
\nu_7(H_4(t))=\nu_7(t+1/2)+\nu_7(t+2/3).
\]
As \(6t+4=n\), we have \(t+1/2=(n-1)/6\) and \(t+2/3=n/6\). Because \(6\) is a \(7\)-adic unit,
\[
\nu_7(F_4(t))=2+\nu_7(n-1)+\nu_7(n),
\]
completing the valuation formula.

**Counts in a common period.** Since \(64=1+63\) and \(729=1+728\) have \(7\)-adic distance exactly one from \(1\), lifting the exponent gives \(64^{7^{k-1}}\equiv729^{7^{k-1}}\equiv1\pmod{7^k}\). Thus \(L_k=6\cdot7^{k-1}\) is a common exponent period. For \(k=1\), the valid exponents are the two classes \(2,4\pmod6\), giving \(R_1=2\). For \(k=2\), class \(2\) contributes one exponent satisfying \(n\equiv0\pmod7\), whereas all seven exponents in class \(4\) contribute, giving \(R_2=8\). For \(k\ge3\), class \(2\) contributes one exponent modulo \(L_k\) satisfying \(n\equiv0\pmod{7^{k-1}}\). Class \(4\) contributes exactly fourteen: the condition is \(n\equiv0\) or \(1\pmod{7^{k-2}}\), and each class has seven lifts modulo \(7^{k-1}\). The conditions are combined uniquely with the fixed residue modulo \(6\) by the Chinese remainder theorem. Therefore \(R_k=1+14=15\) for all \(k\ge3\).

## Verification
Run `python3 verify.py` with Python 3 and no third-party packages. The standalone program evaluates the complete valuation formula for every exponent from \(1\) through \(5000\) using exact modular exponentiation, counts every root modulo \(7^k\) in the stated common period for \(1\le k\le5\), checks the published special family through ten indices, and checks the three critical binomial coefficients. The accompanying `verification_output.txt` records its actual successful execution. All finite checks supplement, rather than replace, the proof for arbitrary indices and prime-power levels.

## Relationship to prior work
Bayarmagnai and Delger (2022), Remark 10, identify the exceptional three-power sum and state \(\nu_7(S(4\cdot7^j))=j+2\) for nonnegative \(j\). That subfamily is already known and is not part of the claimed novelty. The present result supplies the complete valuation for every positive exponent, including the distinct branch involving \(\nu_7(n-1)\), and the exact stable count of fifteen solutions per common period at every level beyond the second. Their Theorem 1 gives a sufficient unboundedness criterion for general sums of powers but does not imply these particular exact valuations. Bell's work on \(p\)-adic valuations of polynomials and regular sequences is structurally related to the resulting valuation functions but does not specify these constants or exponent classes.

## Limitations
The theorem concerns only the indicated sum and the prime \(7\). It gives no analogous formula for other primes or other bases. The stable counts use a common period, without asserting minimality. Structural similarity to general results about \(p\)-adic exponential interpolation does not establish that the precise formula was absent from every other source.

## References
1. G. Bayarmagnai and S. Delger, “On the \(p\)-Adic Valuations of Sums of Powers of Integers,” *Journal of Integer Sequences* 25 (2022), Article 22.8.1, pp. 1–8; published October 7, 2022. https://cs.uwaterloo.ca/journals/JIS/VOL25/Bayarmagnai/bayar10.pdf
2. J. P. Bell, “\(p\)-adic valuations and \(k\)-regular sequences,” *Discrete Mathematics* 307 (2007), 3070–3075. DOI: 10.1016/j.disc.2007.03.009.
