# A squarefree theta bound for Clark–Ismail derivative positivity

**Same-model review: passed. Independent audit: not yet performed.**

## Result

Let
\[
f_n(x)=\frac{d^n}{dx^n}\left(\frac{x^n}{1-e^{-x}}\right),
\qquad n\in\mathbb N,\ x>0.
\]
Let \(\rho\in(0,1)\) be the unique root of
\[
\rho+\rho^2+\rho^3=1,
\]
and set
\[
a_*=-2\log \rho=1.218755726872012\ldots.
\]
Then
\[
\boxed{f_n(x)>0\quad\text{for every }n\in\mathbb N\text{ and every }x\ge a_*.}
\]

Since \(\rho>1/2\), this gives \(a_*<2\log 2\). Thus it strictly improves the explicit uniform interval \(x>2\log2\) stated in Castillo's 2025 correction, which restores the Al-Musallam–Bustoz bound after correcting the Hermite–Laguerre identity used in the 2024 paper.

This does not determine the optimal threshold
\[
\inf\{a>0:f_n(x)>0\text{ for all }n\in\mathbb N,\ x>a\}.
\]

## Context

Clark and Ismail introduced the positivity problem while studying complete monotonicity of functions involving the digamma function. Alzer, Berg, and Koumandos later showed that the associated global conjecture cannot hold for all derivative orders and posed the problem of determining a uniform positive threshold in \(x\). Al-Musallam and Bustoz proved positivity for \(x>2\log2\).

Castillo's 2024 paper claimed the stronger interval \(x>\log2\), but a 2025 correction identifies the Hermite–Laguerre formula used there as incorrect and restores the theorem \(x>2\log2\). The correction supplies the correct identity
\[
\frac{e^{y^2}}{\sqrt\pi}\int_{-\infty}^{\infty}
e^{-t^2}H_n(t)^2\cos(2yt)\,dt
=2^n n!L_n(2y^2).
\]
The argument below starts from this corrected identity.

## Proof

For each fixed \(x>0\), the geometric expansion of \((1-e^{-x})^{-1}\) and the Laguerre differentiation identity give
\[
f_n(x)=n!\sum_{j=0}^{\infty}e^{-jx}L_n(jx).
\]
Set
\[
q=e^{-x/2}\in(0,1).
\]
In the corrected Hermite–Laguerre identity, put \(y=\sqrt{jx/2}\). Then
\[
\int_{-\infty}^{\infty}e^{-t^2}H_n(t)^2
\cos(\sqrt{2jx}\,t)\,dt
=\sqrt\pi\,2^n n!\,q^jL_n(jx).
\]
Consequently
\[
n!e^{-jx}L_n(jx)
=\frac{q^j}{2^n\sqrt\pi}
\int_{-\infty}^{\infty}e^{-t^2}H_n(t)^2
\cos(\sqrt{2jx}\,t)\,dt.
\]
Since \(\sum_{j\ge0}q^j<\infty\) and
\(\int_{\mathbb R}e^{-t^2}H_n(t)^2\,dt<\infty\), absolute convergence permits interchange of the sum and integral:
\[
f_n(x)=\frac1{2^n\sqrt\pi}\int_{-\infty}^{\infty}
e^{-t^2}H_n(t)^2 K_q(\sqrt{2x}\,t)\,dt,
\]
where
\[
K_q(u)=\sum_{j=0}^{\infty}q^j\cos(\sqrt j\,u).
\]

It remains to give a uniform lower bound for \(K_q\). Every integer \(j\ge1\) has a unique representation
\[
j=d\,m^2
\]
with \(d\) squarefree and \(m\ge1\). Hence, by absolute convergence,
\[
K_q(u)
=1+\sum_{\substack{d\ge1\\d\ {\rm squarefree}}}
\sum_{m=1}^{\infty}q^{dm^2}\cos(m\sqrt d\,u).
\]
For fixed squarefree \(d\), set \(r=q^d\) and \(z=\sqrt d\,u/2\). Jacobi's theta function satisfies
\[
\theta_3(z,r)=1+2\sum_{m=1}^{\infty}r^{m^2}\cos(2mz).
\]
Jacobi's product formula gives, for \(0<r<1\),
\[
\theta_3(z,r)
=\prod_{k=1}^{\infty}(1-r^{2k})
\bigl(1+2r^{2k-1}\cos(2z)+r^{4k-2}\bigr).
\]
Each second factor is at least \((1-r^{2k-1})^2\), so
\[
\theta_3(z,r)\ge
\prod_{k=1}^{\infty}(1-r^{2k})(1-r^{2k-1})^2
=\theta_4(0,r).
\]
Equivalently,
\[
\sum_{m=1}^{\infty}r^{m^2}\cos(2mz)
\ge
\sum_{m=1}^{\infty}(-1)^m r^{m^2}.
\]
Applying this to every squarefree block and passing from finite partial sums by absolute convergence,
\[
K_q(u)\ge
1+\sum_{\substack{d\ge1\\d\ {\rm squarefree}}}
\sum_{m=1}^{\infty}(-1)^m q^{dm^2}.
\]

Under the unique factorization \(j=dm^2\) with \(d\) squarefree, \(m\) is even exactly when \(4\mid j\). Therefore the last double series equals
\[
1-\sum_{j=1}^{\infty}q^j
+2\sum_{k=1}^{\infty}q^{4k}
=
1-\frac{q}{1-q}+\frac{2q^4}{1-q^4}
=
\frac{1-q-q^2-q^3}{1-q^4}.
\]
Thus
\[
\boxed{
K_q(u)\ge \frac{1-q-q^2-q^3}{1-q^4}
\quad\text{for every }u\in\mathbb R.
}
\]

The polynomial \(q+q^2+q^3\) is strictly increasing on \((0,1)\). Hence if \(q\le\rho\), equivalently \(x\ge a_*\), the displayed lower bound is nonnegative. At the endpoint \(q=\rho\) the lower bound can vanish, so strict positivity of the integral needs one extra observation: \(K_q\) is continuous and
\[
K_q(0)=\sum_{j=0}^{\infty}q^j=\frac1{1-q}>0.
\]
Therefore \(K_q(u)>0\) on a neighborhood of \(u=0\). The polynomial \(H_n\) is not identically zero on any interval, so \(e^{-t^2}H_n(t)^2\) is positive on a subset of positive measure in the corresponding neighborhood of \(t=0\). Since the integrand is everywhere nonnegative and positive on a set of positive measure,
\[
f_n(x)>0.
\]
This proves the theorem, including \(x=a_*\).

Finally,
\[
\frac12+\frac14+\frac18<1,
\]
so the unique root satisfies \(\rho>1/2\), and therefore \(a_*=-2\log\rho<2\log2\).

## Why the squarefree grouping matters

A termwise estimate \(\cos(\sqrt j\,u)\ge-1\) loses all arithmetic structure among the frequencies. Grouping integers by squarefree kernel turns each family
\[
d,\,4d,\,9d,\,16d,\ldots
\]
into an exact one-dimensional theta series. Its global minimum is controlled by \(\theta_4(0,q^d)\). When the block minima are recombined, the sign is determined only by whether the square factor is even, which collapses the bound to the rational function
\[
\frac{1-q-q^2-q^3}{1-q^4}.
\]

## Limitations

- The constant \(a_*\) is a sufficient uniform threshold, not proved optimal.
- The argument does not determine the smallest derivative order for which positivity can fail below \(a_*\).
- The 2025 correction states that \(2\log2\) can be slightly refined by other Laguerre integral representations but does not provide a concrete bound there; an unpublished, differently phrased, or poorly indexed stronger bound may exist.
- The full text of Al-Musallam–Bustoz (2006) was not separately inspected; its \(2\log2\) theorem was checked through Castillo's 2025 correction and the 2024 article's literature discussion.

## References

1. W. E. Clark and M. E. H. Ismail, “Inequalities Involving Gamma and Psi Functions,” *Analysis and Applications* 1 (2003), 129–140. DOI: https://doi.org/10.1142/S0219530503000041
2. H. Alzer, C. Berg, and S. Koumandos, “On a conjecture of Clark and Ismail,” *Journal of Approximation Theory* 134 (2005), 102–113. DOI: https://doi.org/10.1016/j.jat.2004.02.008
3. F. Al-Musallam and J. Bustoz, “On a conjecture of W. E. Clark and M. E. H. Ismail,” *Ramanujan Journal* 11 (2006), 399–402.
4. K. Castillo, “On the positivity of a certain function related with the Digamma function,” *Ramanujan Journal* 63 (2024), 253–258. DOI: https://doi.org/10.1007/s11139-023-00759-5
5. K. Castillo, “Correction: On the positivity of a certain function related with the Digamma function,” *Ramanujan Journal* 66 (2025), article 70. DOI: https://doi.org/10.1007/s11139-025-01024-7
6. NIST Digital Library of Mathematical Functions, §20.5, equations 20.5.3–20.5.4, Jacobi theta product formulas: https://dlmf.nist.gov/20.5
