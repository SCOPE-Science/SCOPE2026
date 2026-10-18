# Negative cubic correction at the double zero of the distinct-prime parity Dirichlet series

## Finding

Let \(\omega(n)\) count the distinct prime divisors of a positive integer, with \(\omega(1)=0\), and let \(D(s)=\sum_{n\ge1}(-1)^{\omega(n)}n^{-s}\) for \(\Re(s)>1\). Define

\[
C_2=\prod_{p>2}\left(1-\frac{1}{(p-1)^2}\right),\qquad
S=2\sum_{p>2}\frac{\log p}{(p-1)(p-2)},
\]

where both products/sums are over primes and \(\gamma\) is Euler's constant. The function \(D\) has a holomorphic continuation near \(s=1\), satisfying

\[
D(1+t)=4C_2(\log2)t^2+
4C_2(\log2)\left(S-\gamma-\tfrac52\log2\right)t^3+O(t^4).
\]

In particular, the exact third derivative is

\[
D^{(3)}(1)=24C_2\log2\left(S-\gamma-\tfrac52\log2\right)<0.
\]

Consequently \(\frac{D(1+t)}{t^2}\) approaches \(4C_2\log2\) strictly from **below** as positive real \(t\) tends to zero. This gives the first nonzero correction to the previously determined quadratic term.

## Assumptions and scope

The definitions concern ordinary prime factors, with no multiplicities in \(\omega(n)\). All logarithms are natural. \(C_2\) is the conventional Hardy–Littlewood twin-prime singular product, not twice that product. The Taylor variable \(t\) is complex and sufficiently close to zero; the strict-sign and below-the-limit conclusions concern real \(t>0\) tending to zero. The theorem is analytic and unconditional; it makes no claim about the existence, density, or distribution of twin primes.

## Proof

For \(\Re(s)>1\), multiplicativity gives

\[
D(s)=\prod_p\frac{1-2p^{-s}}{1-p^{-s}}=
\frac{1-2^{1-s}}{(1-2^{-s})^2}\frac{G(s)}{\zeta(s)},
\quad
G(s)=\prod_{p>2}\frac{1-2p^{-s}}{(1-p^{-s})^2}.
\]

Each logarithm of a factor of \(G(s)\) is \(O(p^{-2\Re(s)})\) locally uniformly when \(\Re(s)>\frac12\), away from finitely many zero points; hence \(G\) is holomorphic near \(1\), and its product there is positive. At \(s=1\),

\[
G(1)=\prod_{p>2}\frac{p(p-2)}{(p-1)^2}=C_2>0.
\]

Termwise logarithmic differentiation is valid near \(1\), giving

\[
\frac{G'(1)}{G(1)}
=\sum_{p>2}
\left(\frac{2p^{-1}\log p}{1-2p^{-1}}
-\frac{2p^{-1}\log p}{1-p^{-1}}\right)
=2\sum_{p>2}\frac{\log p}{(p-1)(p-2)}
=S.
\]

The prime sum converges absolutely by comparison with \(\sum_{n\ge3}(\log n)/n^2\). Put \(L=\log2\). The analytic expansions at \(s=1+t\) are

\[
\frac{1-2^{-t}}{(1-2^{-1-t})^2}
=4Lt-10L^2t^2+O(t^3),
\qquad
\frac1{\zeta(1+t)}=t-\gamma t^2+O(t^3),
\]

and \(G(1+t)=C_2(1+St+O(t^2))\). Their product establishes the asserted cubic expansion and exact third derivative.

It remains to prove the strict sign without relying on finite computation as a proxy for the prime sum. Set \(f(x)=2\log x/((x-1)(x-2))\). For real \(x\ge19\), \(f\) is positive and decreasing, so

\[
\sum_{\substack{p>19\\p\text{ prime}}}f(p)
\le\sum_{n=20}^{\infty}f(n)
\le\int_{19}^{\infty}f(x)\,dx.
\]

Since \((x-1)(x-2)\ge(x-2)^2\) and \(\log x\le\log(x-2)+2/(x-2)\) for \(x\ge19\),

\[
\int_{19}^{\infty}f(x)\,dx
\le\frac{2(\log17+1)}{17}+\frac2{17^2}.
\]

For the seven primes \(3,5,7,11,13,17,19\), the strict rational upper bounds

\[
\begin{array}{c|ccccccc}
p&3&5&7&11&13&17&19\\
\hline
\log p<&11/10&161/100&39/20&12/5&257/100&71/25&59/20
\end{array}
\]

follow by evaluating lower partial sums of \(e^r=\sum_{k\ge0}r^k/k!\) at the displayed rational bounds \(r\). Substituting these bounds yields the *rational* inequality

\[
S<
\sum_{p\in\{3,5,7,11,13,17,19\}}\frac{2r_p}{(p-1)(p-2)}
+\frac{2(r_{17}+1)}{17}+\frac2{17^2}
<\frac{13}{6}.
\]

On the other hand \(\gamma>\frac12\), since the monotone sequence \(\sum_{k=1}^{n}1/k-\log(n+1)\) tends to \(\gamma\), and its value at \(n=6\) is \(49/20-\log7>1/2\). Also \(\log2=2\sum_{j\ge0}((2j+1)3^{2j+1})^{-1}>2/3\). Therefore

\[
\gamma+\tfrac52\log2>\frac12+\tfrac52\frac23=\frac{13}{6}>S.
\]

All other factors in the expression for \(D^{(3)}(1)\) are positive. Thus \(D^{(3)}(1)<0\). Dividing the Taylor expansion by \(t^2\) gives a strictly negative first correction for sufficiently small real \(t>0\), proving the final assertion.

## Verification

The standalone `CHECK.py` implements the exact rational upper bounds on \(\log p\) using finite positive Taylor sums of the exponential, checks the resulting strict rational inequality \(S<13/6\), and independently compares a finite odd-prime Euler product's numerical logarithmic derivative with its termwise expression. Run `python3 CHECK.py` using only the Python standard library. The finite Euler-product numerical check is diagnostic only; the analytic majorant proves the infinite bound.

## Relationship to prior work

Álvarez Cruz and Álvarez Gutiérrez, *Regularization of a Divergent Arithmetic Product via the Asymptotic Monoid: The Case of \((-1)^{\omega(n)}\)*, arXiv:2610.13658v1 (first posted 2026-10-09), Proposition 6.3 and Corollary 6.6, establish \(D''(1)=8C_2\log2\) and the quadratic term. The present result starts from the same Dirichlet series and derives the exact **next** coefficient, including a global strict sign proved by an independent inequality for a prime logarithmic sum. The earlier second-derivative statement alone does not determine this sign, and the inspected original article does not state the cubic coefficient or sign.

## Limitations

This is a local expansion at \(s=1\), not an evaluation of the separately defined regularized arithmetic product. It does not improve analytic continuation across the natural boundary \(\Re(s)=0\), and it gives no new prime-pair theorem. It does not prove global monotonicity of \(D(1+t)/t^2\) away from zero. Publication priority remains subject to independent bibliographic checking beyond the inspected primary paper and indexed searches.

## References

1. A. Álvarez Cruz and E. A. Álvarez Gutiérrez, *Regularization of a Divergent Arithmetic Product via the Asymptotic Monoid: The Case of \((-1)^{\omega(n)}\)*, arXiv:2610.13658v1 (2026-10-09), especially §§6.1–6.3, Proposition 6.3 and Corollary 6.6. https://arxiv.org/pdf/2610.13658
2. Classical Laurent expansion of the Riemann zeta function at \(s=1\), \(\zeta(1+t)=t^{-1}+\gamma+O(t)\).
