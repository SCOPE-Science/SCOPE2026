# Sharp \(L^2\)-to-\(L^4\) norm for four consecutive characters
## Finding
For \(c=(c_0,c_1,c_2,c_3)\in\mathbb C^4\), define
\[
P_c(t)=c_0+c_1e^{2\pi i t}+c_2e^{4\pi i t}+c_3e^{6\pi i t},\qquad t\in\mathbb T=\mathbb R/\mathbb Z,
\]
where \(\mathbb T\) has normalized Haar measure. Let \(\rho\) be the unique positive solution of
\[
\rho^3+3\rho^2-3\rho-3=0.
\]
Then the exact norm of the four-character extension map from the four-dimensional coefficient space to \(L^4(\mathbb T)\) is
\[
\mathsf C_4=
\left(\frac{3\rho^4+4\rho^3+12\rho^2+3}{2(1+\rho^2)^2}\right)^{1/4}
=1.294588535436489\ldots .
\]
Equivalently, \(K=\mathsf C_4^4\) is the largest real root of
\[
208K^3-1224K^2+2268K-1323=0,
\]
namely \(K=2.808840165474397\ldots\).

All nonzero extremizers are exactly
\[
(c_0,c_1,c_2,c_3)=\lambda\,(1,\rho e^{i\beta},\rho e^{2i\beta},e^{3i\beta}),
\]
with \(\lambda\in\mathbb C\setminus\{0\}\) and \(\beta\in\mathbb R\). Thus the two inner frequencies have modulus \(\rho\) times the two outer frequencies, and the coefficient phases form an arithmetic progression.

## Assumptions and scope
The statement is for the continuous torus with normalized Haar measure and for the four consecutive characters indexed from \(0\) through \(3\). Translation of the frequency set and multiplication of all frequencies by a nonzero integer do not change the continuous-torus norm, so the same constant holds for every four-term integer arithmetic progression. No claim is made here for finite cyclic sampling, for non-arithmetic four-point spectra, or for exponents other than \(4\).

## Proof
Parseval applied to \(P_c^2\) gives
\[
\begin{aligned}
\|P_c\|_4^4={}&|c_0^2|^2+|2c_0c_1|^2+|c_1^2+2c_0c_2|^2\\
&+|2c_0c_3+2c_1c_2|^2+|c_2^2+2c_1c_3|^2\\
&+|2c_2c_3|^2+|c_3^2|^2.
\end{aligned}
\]
Write \(a=|c_0|\), \(b=|c_1|\), \(c=|c_2|\), \(d=|c_3|\), and
\[
S=a^2+b^2+c^2+d^2.
\]
Maximizing each collision term over phases by the triangle inequality yields
\[
\|P_c\|_4^4\le
2S^2-(a^4+b^4+c^4+d^4)+4ab^2c+8abcd+4bc^2d.
\]
Set
\[
A=a^2+d^2,\qquad B=b^2+c^2,
\]
so \(A+B=S\). The elementary bounds
\[
a^4+d^4\ge\frac{A^2}2,\qquad b^4+c^4\ge\frac{B^2}2,
\]
\[
bc\le\frac B2,\qquad ad\le\frac A2,
\]
and Cauchy--Schwarz,
\[
ab+cd\le\sqrt{AB},
\]
give
\[
4bc(ab+2ad+cd)\le 2B\sqrt{AB}+2AB.
\]
Consequently
\[
\|P_c\|_4^4\le
2S^2-\frac{A^2+B^2}2+2AB+2B\sqrt{AB}.
\]
After homogeneity sets \(S=1\), put \(r=\sqrt{B/A}\). The right-hand side becomes
\[
h(r)=\frac{3r^4+4r^3+12r^2+3}{2(1+r^2)^2},\qquad r\ge0.
\]
A direct differentiation gives
\[
h'(r)=-\frac{2r(r^3+3r^2-3r-3)}{(1+r^2)^3}.
\]
The cubic \(q(r)=r^3+3r^2-3r-3\) has exactly one positive root \(\rho\): it is negative at \(0\), its only positive critical point lies at \(\sqrt2-1\) where it is still negative, and it then increases to \(+\infty\). Hence \(h\) increases on \((0,\rho)\) and decreases on \((\rho,\infty)\), so its global maximum is \(h(\rho)\). Eliminating \(\rho\) from \(q(\rho)=0\) and \(K=h(\rho)\) yields
\[
208K^3-1224K^2+2268K-1323=0.
\]
The other two real roots are smaller, so the stated root is the sharp fourth power of the norm.

Every inequality above is an equality when \(a=d\), \(b=c\), and \(b/a=\rho\). Conversely, equality at the interior maximum forces these modulus relations. Equality in the three triangle inequalities for the pair-sum collision fibers forces
\[
2\arg c_1\equiv\arg c_0+\arg c_2,
\qquad
2\arg c_2\equiv\arg c_1+\arg c_3
\pmod{2\pi},
\]
so the four phases are affine-linear. This gives precisely the stated extremizer family.

## Verification
The standalone script `verify.py` independently evaluates the exact fourth-moment formula, locates the positive cubic root by bisection, checks the defining cubic for \(K\), verifies the extremizing coefficient pattern, and stress-tests random complex coefficient vectors against the sharp bound. The numerical checks corroborate the analytic proof; they are not used to infer the universal inequality.

The equal-modulus arithmetic-progression maximum from the phase-only problem is \(44\), so after \(\ell^2\)-normalization its fourth-power ratio is \(44/16=11/4=2.75\). The present unrestricted coefficient maximum is \(2.808840165474397\ldots\), showing that amplitude redistribution is genuinely necessary.

## Relationship to prior work
Neuwirth's 1997 work on metric unconditionality in Fourier analysis makes explicit the key even-exponent mechanism: for even \(p\), the \(L^p\) norm is a polynomial expression in Fourier coefficients obtained from Parseval applied to \(f^{p/2}\). That framework explains why additive relations govern \(L^4\) norms, but it does not give the sharp four-consecutive-character optimization or its extremizers.

A later work of Neuwirth studies exactly the same four consecutive frequencies, but for the Fourier-analytic Sidon constant, i.e. coefficient \(\ell^1\) mass under an \(L^\infty\) constraint. That is a different norm problem and does not imply the present \(L^2\)-to-\(L^4\) constant. Nearby phase-only fourth-moment results restrict all coefficient moduli to be equal; their arithmetic-progression endpoint is strictly below the unrestricted optimum above.

## Limitations
This result does not classify arbitrary four-point frequency sets, finite cyclic analogues, or other exponents. The literature comparison found no implication-equivalent exact constant, but an older finite-degree Nikolskii or finite autoconvolution calculation under different terminology remains a residual originality risk. The theorem itself is independent of numerical experimentation.

## References
1. Stefan Neuwirth, *Metric unconditionality and Fourier analysis*, arXiv:math/9707211, first public version 1997-07-28; MSC 42A55, 46B28, 46B04.
2. Stefan Neuwirth, *On the (Fourier analytic) Sidon constant of the four-frequency set indexed from \(0\) through \(3\)*, arXiv:2603.28229, 2026.
