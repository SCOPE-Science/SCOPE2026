# Exact three-point Fourier uncertainty on every cyclic group
## Finding
For every integer \(N\ge 3\), define
\[
q_N=\min\{d\ge 3:d\mid N\}.
\]
If \(f:\mathbb Z_N\to\mathbb C\) has exactly three nonzero values, then
\[
|\operatorname{supp}\widehat f|\ge \frac{N(q_N-2)}{q_N}.
\]
The bound is sharp for every \(N\). Equivalently, among the \(N\)-th roots of unity, a Laurent polynomial with exactly three nonzero coefficients and three distinct exponent classes modulo \(N\) has at most \(2N/q_N\) zeros, and this maximum is attained.

## Assumptions and scope
The Fourier transform is the unnormalized cyclic transform
\[
\widehat f(k)=\sum_{x\in\mathbb Z_N}f(x)e^{-2\pi i kx/N}.
\]
The hypothesis is exact support size three: all three coefficients are nonzero and the three support points are distinct modulo \(N\). No assertion is made here for larger exact support sizes.

## Proof
Write a translated support as \(\{0,a,b}\). First remove a common divisor. Put \(g=\gcd(N,a,b)\), \(N=gM\), \(a=ga'\), and \(b=gb'\). Then \(\widehat f(k)\) depends only on \(k\bmod M\), so every Fourier zero for the induced three-point function on \(\mathbb Z_M\) lifts to exactly \(g\) zeros on \(\mathbb Z_N\). Moreover \(q_M\ge q_N\). It therefore suffices to prove the bound when \(\gcd(N,a,b)=1\).

There are three cases.

If \(3\mid N\), then \(q_N=3\). The classical product uncertainty inequality gives \(3|\operatorname{supp}\widehat f|\ge N\), which is exactly the stated bound.

Assume \(3\nmid N\) and \(4\mid N\), so \(q_N=4\). Primitive support means that \(a\) and \(b\) are not both even. For
\[
P(z)=c_0+c_1z^a+c_2z^b
\]
split the even and odd exponent terms as \(P(z)=E(z^2)+zO(z^2)\). Both parity parts are present, and because there are only three monomials one of \(E\) or \(O\) is a single nonzero monomial. Hence \(P(z)=P(-z)=0\) is impossible: adding and subtracting would force both parity parts to vanish, contradicting the singleton monomial. Pairing the \(N\)-th roots as \(\{z,-z}\) therefore gives at most \(N/2\) zeros, so \(|\operatorname{supp}\widehat f|\ge N/2\).

Finally suppose \(q_N=p\ge5\). Then \(3\nmid N\) and \(4\nmid N\). If \(N\) is odd, the consecutive divisors around support size three are \(1\) and \(p\). Meshulam's divisor-interpolation inequality gives directly
\[
|\operatorname{supp}\widehat f|\ge \frac{N(1+p-3)}{p}=\frac{N(p-2)}{p}.
\]
If \(N=2m\) with \(m\) odd, identify \(\mathbb Z_N\cong\mathbb Z_2\times\mathbb Z_m\). Primitive support meets both parity fibers, so one fiber contains two support points and the other one. Write the corresponding functions on \(\mathbb Z_m\) as \(f_0,f_1\), and their transforms as \(A,B\), with one of \(f_0,f_1\) one-sparse and the other two-sparse. For the two characters \(\varepsilon\in\mathbb Z_2\),
\[
\widehat f(\varepsilon,\eta)=A(\eta)+(-1)^\varepsilon B(\eta).
\]
For each \(\varepsilon\), this is the Fourier transform on \(\mathbb Z_m\) of a nonzero function supported on at most three points. Since the least divisor of \(m\) above one is \(p\), Meshulam's bound implies at most \(2m/p\) zeros in that parity-frequency fiber. Thus the total number of zeros is at most \(4m/p=2N/p\), proving the lower bound.

For sharpness, let \(h=N/q_N\) and use support \(\{0,h,2h}\). Choose two distinct \(q_N\)-th roots \(\alpha,\beta\) with \(\alpha+\beta\ne0\), for example \(1\) and \(e^{2\pi i/q_N}\), and coefficients from
\[
(t-\alpha)(t-\beta)=t^2-(\alpha+\beta)t+\alpha\beta.
\]
All three coefficients are nonzero. As frequency varies, \(t\) runs through the \(q_N\)-th roots equally often, and exactly the two values \(\alpha,\beta\) vanish. Hence there are exactly \(2N/q_N\) Fourier zeros.

## Verification
The accompanying `verify_mu3_cyclic.py` uses only integer arithmetic. For every \(3\le N\le36\), it exhausts all normalized three-point supports \(\{0,a,b}\). After shifting a putative zero to frequency zero, every nondegenerate second zero determines the coefficient kernel; a third zero is then equivalent to a \(3\times3\) Fourier minor vanishing. The script tests that determinant exactly by reducing its six-term root-of-unity expression modulo the cyclotomic polynomial \(\Phi_N\). Row-equivalent frequency classes are handled separately. The run checks 7,140 normalized supports, 168,000 nondegenerate pair kernels, and 4,950,750 exact cyclotomic determinant tests, and returns `VERIFY_OK`.

## Relationship to prior work
Meshulam's uncertainty inequality gives the sharp divisor-interpolation lower bound for a prescribed support cardinality in many divisor regimes, but for even \(N\) with \(N\equiv2\pmod4\) its support-three bound is weaker than the formula above. Bonami and Ghobber distinguish exact-support equality cases from the monotone Meshulam function and treat prime-square and two-prime families; they explicitly note the difficulty of extending their analysis to arbitrary prime factorizations. Delvaux and Van Barel relate rank-deficient Fourier submatrices to finite-group uncertainty and give extensive prime-power/Kronecker constructions. The present result instead gives the exact support-three minimum for every cyclic order, including arbitrary composite \(N\).

## Limitations
The theorem is specific to exact support size three and does not classify all extremizing coefficient/support configurations. The literature search did not locate an equivalent all-order formula, but a differently phrased or poorly indexed prior statement remains a residual originality risk.

## References
Roy Meshulam, *An uncertainty inequality for finite abelian groups*, arXiv:math/0312407, first posted 2003-12-22.

Aline Bonami and Saifallah Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, arXiv:1003.5060, first posted 2010-03-26.

Steven Delvaux and Marc Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, Linear Algebra and its Applications 426 (2007), 349-367, DOI 10.1016/j.laa.2007.05.009.
