# Exact three-way residue-class densities for the square-splitting Möbius function

## Finding

Let \(\mu\) be the classical Möbius function. Every positive integer has a unique representation
\[
n=u(n)v(n)^2,\qquad u(n)\text{ squarefree}.
\]
Following Talukdar and Saikia, define the square-splitting Möbius function
\[
f(n)=\mu(u(n))\mu(v(n)).
\]
Fix an integer \(q\ge1\) and any integer \(a\). If \(p^e\parallel q\), write \(h_e=\min(e,4)\), and define
\[
\kappa(q,a)=\frac{1}{q\zeta(4)}
\prod_{p^e\parallel q}
\frac{1-\mathbf1_{p^{h_e}\mid a}\,p^{h_e-4}}{1-p^{-4}},
\]
with the usual empty-product convention. The indicator is \(1\) when the divisibility condition holds and \(0\) otherwise.

For each \(\epsilon\in\{-1,0,+1\}\), put
\[
N_\epsilon(x;q,a)=\#\{1\le n\le x:\ n\equiv a\pmod q,\ f(n)=\epsilon\}.
\]
Then, as \(x\to\infty\) with \(q\) fixed,
\[
N_{+1}(x;q,a)=\frac{\kappa(q,a)}2x+o_q(x),\qquad
N_{-1}(x;q,a)=\frac{\kappa(q,a)}2x+o_q(x),
\]
and
\[
N_0(x;q,a)=\left(\frac1q-\kappa(q,a)\right)x+o_q(x).
\]
More precisely,
\[
N_{+1}(x;q,a)+N_{-1}(x;q,a)
=\kappa(q,a)x+O_q(x^{1/4}).
\]
The constant \(\kappa(q,a)\) is zero if and only if some prime satisfies \(p^4\mid\gcd(q,a)\); in that case \(f(n)=0\) identically on the progression. Otherwise \(\kappa(q,a)>0\), so the positive and negative values occur equally often asymptotically and each with positive density.

## Assumptions and scope

The modulus \(q\) is any **fixed** positive integer, and \(a\) may be a non-coprime residue. Densities are measured relative to **all** positive integers, so a complete residue class has density \(1/q\). The statement is unconditional, relying on the classical prime number theorem in fixed arithmetic progressions. No estimate uniform in growing \(q\), or quantitative error for the difference of the two signs, is asserted.

## Proof

**1. Prime powers and ordinary convolution.** The source's square-splitting formula yields
\[
f(p^j)=\begin{cases}
-1,&j=1,2,\\
+1,&j=3,\\
0,&j\ge4,
\end{cases}
\qquad f(1)=1.
\]
The Euler polynomial \(1-z-z^2+z^3=(1-z)(1-z^2)\) therefore gives the elementary identity
\[
f(n)=\sum_{d^2\mid n}\mu(d)\mu(n/d^2).
\tag{1}
\]
Also,
\[
f(n)^2=\mathbf1_{\text{no }p^4\mid n}
=\sum_{d^4\mid n}\mu(d).
\tag{2}
\]
Both identities follow prime by prime, including the case \(n=1\).

**2. The signed mean vanishes in every residue class.** The prime number theorem in arithmetic progressions says that for every fixed \(q\) and every invertible \(b\pmod q\),
\[
\sum_{\substack{m\le y\\m\equiv b\ (\mathrm{mod}\ q)}}\mu(m)=o_q(y).
\tag{3}
\]
For an invertible \(b\) and identity (1), necessarily \((d,q)=1\); hence
\[
\sum_{\substack{n\le x\\n\equiv b\ (\mathrm{mod}\ q)}}f(n)
=\sum_{\substack{d\le\sqrt x\\(d,q)=1}}\mu(d)
\sum_{\substack{m\le x/d^2\\m\equiv bd^{-2}\ (\mathrm{mod}\ q)}}\mu(m).
\]
Here \(d^{-2}\) is the inverse of \(d^2\pmod q\). For every fixed cut-off \(T\), the terms \(d\le T\) are \(o_q(x)\) by (3). In the tail \(d>T\), the absolute value is bounded by
\[
\sum_{d>T}\left\lfloor\frac{x}{d^2}\right\rfloor
\le x\sum_{d>T}d^{-2}=O(x/T).
\]
First let \(x\to\infty\) with \(T\) fixed, then \(T\to\infty\). We obtain the required \(o_q(x)\) estimate for every invertible class.

To treat an arbitrary (possibly noninvertible) class \(a\), consider only integers with \(f(n)\ne0\). By the first prime-power formula, every prime occurs to exponent at most \(3\). Write \(n=dm\), where \(d\) contains exactly the prime-power components of \(n\) at primes dividing \(q\), and \((m,q)=1\). There are only \(4^{\omega(q)}\) possible values of \(d\), and \(f(n)=f(d)f(m)\). For each such fixed \(d\), the congruence \(dm\equiv a\pmod q\) is a union of finitely many invertible residue classes for \(m\pmod q\), possibly an empty union. Applying the preceding invertible-class estimate with \(x/d\) in place of \(x\), then summing over the finitely many \(d\), proves
\[
\sum_{\substack{n\le x\\n\equiv a\ (\mathrm{mod}\ q)}}f(n)=o_q(x)
\tag{4}
\]
for **every** residue \(a\).

**3. Exact support density in arbitrary classes.** Identity (2) gives
\[
N_{+1}(x;q,a)+N_{-1}(x;q,a)
=\sum_{d\le x^{1/4}}\mu(d)\,
\#\{n\le x:n\equiv a\pmod q,\ d^4\mid n\}.
\]
Set \(g=\gcd(q,d^4)\). The two congruences admit a solution exactly when \(g\mid a\), and their solutions form one residue class modulo \(qd^4/g\). Therefore the inner count equals
\[
\mathbf1_{g\mid a}\frac{xg}{qd^4}+O(1).
\]
Summing the errors through \(d\le x^{1/4}\) gives \(O(x^{1/4})\). Extending the absolutely convergent main sum to all \(d\) costs at most
\[
\frac{x}{q}\sum_{d>x^{1/4}}\frac{\gcd(q,d^4)}{d^4}
=O_q(x^{1/4}).
\]
Thus the support count is \(\kappa(q,a)x+O_q(x^{1/4})\), where the Euler product of the main sum is
\[
\kappa(q,a)=\frac1q
\prod_{p\nmid q}(1-p^{-4})
\prod_{p^e\parallel q}\left(1-
\mathbf1_{p^{h_e}\mid a}\,p^{h_e-4}\right).
\tag{5}
\]
Extracting \(1/\zeta(4)=\prod_p(1-p^{-4})\) gives the stated expression. Each local factor in (5) is positive unless \(e\ge4\) and \(p^4\mid a\), precisely the vanishing criterion. In that case every integer in the class is divisible by \(p^4\) and hence has \(f(n)=0\).

**4. The sign classes.** Since \(f\in\{-1,0,1\}\), subtracting (4) from the support count gives twice the number of negative values, and adding gives twice the number of positive values. The complement of the support has density \(1/q-\kappa(q,a)\). These are the asserted three formulas.

## Verification

The included standard-library Python checker, `artifacts/verify.py`, reconstructs the classical Möbius values by linear sieve and evaluates \(f\) both from its prime-power rule and independently by the square-divisor convolution (1) for every \(n\le400000\). It checks the fourth-power-free identity (2) and verifies exact support counts in all \(146\) residue classes for \(q\in\{1,2,3,4,6,8,9,12,16,24,25,36\}\) by separate finite congruence counting. It also checks sample local Euler factors and structurally forbidden classes. The accompanying `artifacts/replay.txt` contains the actual output. This finite work does not replace the analytic proof of limits or the use of (3).

## Relationship to prior work

Talukdar and Saikia's *A Square–Splitting A-Convolution of Narkiewicz Type* establishes the exact prime-power formula and Euler series for \(f=\mu_\star\) in its Theorem 3, and computes the **unrestricted total support density** \(1/\zeta(4)\) in Theorem 11. It does not give separate positive/negative sign densities, nor arithmetic-progression densities, nor the classification of identically vanishing noncoprime classes; its conclusion explicitly raises related distributional questions.

The general fake-Möbius-function literature of Martin and Yip and of Saraeb analyzes oscillations or smoothed summatory functions at finer scales, but the inspected main theorems do not provide the present exact three-way fixed-progression classification. The current result combines the original source's local arithmetic with the prime number theorem in arithmetic progressions and exact fourth-power-free congruence counting.

## Limitations

The implied constants in \(O_q(\cdot)\) may depend on \(q\), and no uniformity for growing moduli is established. The signed discrepancy is shown only to be \(o_q(x)\); the result does not estimate its finer oscillations or obtain effective numerical rates. The proof uses classical deep input in the form of the prime number theorem in arithmetic progressions. General published methods and unindexed work remain possible sources of broader formulations.

## References

1. Champak Talukdar and Helen K. Saikia, *A Square–Splitting A-Convolution of Narkiewicz Type*, INTEGERS **26** (2026), article A56, published 2026-05-01, DOI: 10.5281/zenodo.19949682. Full text: https://math.colgate.edu/~integers/aa56/aa56.pdf.
2. Greg Martin and Chi Hoi Yip, *Oscillation results for the summatory functions of fake mu's*, arXiv:2411.06610, later Canadian Journal of Mathematics (2025 online).
3. Ali Saraeb, *Unimodular Fake Möbius Functions* (earlier version titled *Fake Mobius-type Functions on the Unit Circle*), arXiv:2512.18936.
4. Prime number theorem in arithmetic progressions, equivalently the zero-free line at real part one for Dirichlet \(L\)-functions (classical).
