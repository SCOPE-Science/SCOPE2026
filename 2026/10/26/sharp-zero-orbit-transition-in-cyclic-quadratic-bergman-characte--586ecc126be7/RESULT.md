# Sharp zero-orbit transition in cyclic quadratic Bergman character kernels

## Finding

For the order-\(q\) rotation character \(r\) of the quadratic-weighted Bergman space of the unit disk, with integers \(q\ge2\) and \(0\le r<q\), the number \(N(q,r)\) of distinct nonzero rotation orbits of *attainable* kernel zeros is

\[
N(q,r)=\begin{cases}
0,&(q,r)=(2,1),\\
1,&(q,r)\ne(2,1),\quad q\le2r+4,\\
2,&q\ge2r+5.
\end{cases}
\]

Every such orbit comprises exactly \(q\) simple zero products \(t=z\overline w\) inside the unit disk. In the borderline case \(q=2r+4\), a further \(q\) roots of the kernel numerator lie on the unattainable boundary \(|t|=1\); these do not count. The exceptional case \((q,r)=(2,1)\) has only boundary numerator zeros. When \(r>0\), there is also a forced zero at \(t=0\) of multiplicity \(r\), excluded from \(N(q,r)\). The complete space has zero-free Bergman kernel, whereas its cyclic character sectors exhibit an exact one-to-two zero-orbit transition.

## Assumptions and scope

Let \(A^2_2(\mathbb D)\) be the Hilbert space of holomorphic functions on \(\mathbb D\) with norm
\[
\|f\|^2=\frac3\pi\int_{|z|<1}|f(z)|^2(1-|z|^2)^2\,dA(z).
\]
For \(q\ge2\), \(0\le r<q\), let \(A_{q,r}\) be the closed subspace spanned by monomials \(z^{qj+r}\), \(j\ge0\). Its evaluation kernel is \(K_{q,r}\). For \(z,w\in\mathbb D\) put \(t=z\bar w\), so \(|t|<1\). Every \(t\in\mathbb D\) is attainable, for instance using \(z=\sqrt{|t|}\), \(w=\overline t/\sqrt{|t|}\) when \(t\ne0\). The cyclic action on nonzero products is \(t\mapsto e^{2\pi i/q}t\).

## Proof

**1. Exact numerator.** Normalized monomials have reproducing coefficients \(\binom{n+3}{3}\); hence
\[
K_{q,r}(z,w)=\frac{t^r}{6}\sum_{j=0}^{\infty}(qj+r+1)(qj+r+2)(qj+r+3)t^{qj}
=\frac{t^r P_{q,r}(t^q)}{6(1-t^q)^4}.
\]
Write \(s=t^q\). The cubic numerator \(P_{q,r}(s)=c_0+c_1s+c_2s^2+c_3s^3\) has
\[
\begin{aligned}
c_0&=(r+1)(r+2)(r+3),\\
c_1&=q^3+3q^2r+6q^2+3qr^2+12qr+11q-3r^3-18r^2-33r-18,\\
c_2&=4q^3-6qr^2-24qr-22q+3r^3+18r^2+33r+18,\\
c_3&=(q-r-1)(q-r-2)(q-r-3).
\end{aligned}
\]
Using \(\sum_{j\ge0}j^k s^j\) for \(0\le k\le3\) gives these identities directly, including cases where the degree drops. Two important exact evaluations are
\[
P_{q,r}(1)=6q^3,
\qquad P_{q,r}(-1)=2(q-2r-4)\big(q^2+2qr+4q-2r^2-8r-6\big).
\]

**2. Simple negative roots.** For completeness, one can prove the needed reality and simplicity without a numerical root computation. Set
\[
F_m(s)=\sum_{j\ge0}\prod_{k=1}^{m}(qj+r+k)s^j=\frac{Q_m(s)}{(1-s)^{m+1}},\quad Q_0=1.
\]
Differentiation gives the recurrence
\[
Q_{m+1}=qs(1-s)Q'_m+\big((r+m+1)(1-s)+q(m+1)s\big)Q_m.
\]
For \(m\in\{0,1,2,3\}\), all coefficients of \(Q_m\) are nonnegative with positive constant and leading coefficients. To see this exactly, write \(u=r+1\ge1\), \(d=q-r-1\ge0\). Then \(Q_1=(u, d)\), \(Q_2=(u(u+1), d^2+4du+d+u(u-1),d(d-1))\), and the coefficients of \(Q_3\), in increasing order, are
\[
\begin{aligned}
&u(u+1)(u+2),\\
&d^3+6d^2u+3d^2+12du^2+12du+2d+4u(u-1)(u+1),\\
&d(d-1)(4d+12u+4)+6du^2+u(u-1)(u-2),\\
&d(d-1)(d-2).
\end{aligned}
\]
These are nonnegative for integer \(u\ge1\), \(d\ge0\). Suppose \(Q_m\) has simple negative roots. At each such root \(x\), the recurrence gives \(Q_{m+1}(x)=qx(1-x)Q'_m(x)\), which has the opposite sign to \(Q'_m(x)\); these signs alternate between the roots. There is another sign change from the largest negative root to \(0\), because \(Q_{m+1}(0)>0\). These furnish at least \(\deg Q_m\) distinct simple negative roots of \(Q_{m+1}\). If its degree rises by one, the positive leading coefficient gives the additional negative root to the left of the smallest previous root. No more roots are possible by degree. The base \(Q_0=1\) starts the induction. Consequently, every root of \(P_{q,r}=Q_3\) is distinct, strictly negative. The general real-rootedness context is also classical in Veronese-transform theory; the contribution here is the ensuing *unit-disk root count* for these kernels.

**3. Counting negative roots in \((-1,0)\).** Put \(u=r+1\) and \(d=q-r-1\) as above. The second factor of \(P(-1)\) becomes
\[
B=d^2+4du+2d+u(u-2),
\]
which is strictly positive except when \((q,r)=(2,1)\); in that case \(P(s)=24(1+s)\). Thus for all other pairs the sign of \(P(-1)\) equals the sign of \(q-2r-4\).

If \(q\le2r+3\), then \(P(-1)<0<P(0)\). There is an odd number of zeros in \((-1,0)\). There cannot be three: if the polynomial is cubic, the product of their moduli is \(c_0/c_3>1\), since \(d\le r+2\). Hence precisely one root lies in \((-1,0)\). If the polynomial has smaller degree, the same conclusion is immediate from its maximum possible degree and endpoint sign.

If \(q\ge2r+5\), then \(P(-1)>0\) and \(c_3>c_0>0\) because \(d\ge r+4\). The number of negative roots in \((-1,0)\) is even. It cannot be zero, as that would give \(c_0/c_3\ge1\), contrary to \(c_0/c_3<1\). Since \(P\) is cubic with three distinct negative roots and \(P(-1)\ne0\), exactly two lie in \((-1,0)\).

At \(q=2r+4\), \(c_3=c_0\) and \(P(-1)=0\). Simplicity yields precisely one other root in \((-1,0)\): indeed \(P\) is reciprocal and factors as \((1+s)\big(c_0s^2+(c_1-c_0)s+c_0\big)\); the remaining distinct negative roots are reciprocal and lie on opposite sides of \(-1\). For \((q,r)=(2,1)\) there is only the boundary root \(-1\). Finally each \(s\in(-1,0)\) has exactly \(q\) distinct \(q\)-th roots of modulus below one; these are simple zeros of \(K_{q,r}\) away from the forced factor \(t^r\). No other interior zeros exist.

## Verification

The standalone file `verify_cyclic_bergman.py` symbolically reconstructs \(P_{q,r}\), checks the endpoint factors, and verifies the first nine Hilbert-series coefficients for all \(1770\) pairs \(2\le q\le60\), \(0\le r<q\), totaling \(15930\) coefficient checks. Exact algebraic Sturm counts confirm the predicted interior and boundary zeros and simplicity for all these pairs. Its output is provided in `verification_cyclic_bergman.txt`. The proof above, not this finite sweep, establishes the unbounded statement.

## Relationship to prior work

Ross and Thomas (2009) study weighted Bergman kernels on orbifolds, including cyclic character constructions and averaging. Their inspected discussion does not classify the zero orbits of the present explicit disk character sectors. Zeytuncu (2010) studies weighted disk Bergman kernel zeros for different radial weights, not these cyclic projections. Jochemko (2016) proves substantially more general real-rootedness results for Veronese numerators; that **prior result covers negative-real root location** and is not claimed as new here. What is classified here is whether those roots satisfy \(|s|<1\), yielding the exact threshold and the attainable orbit counts. Park (2016) studies zeros on other Reinhardt geometries. An older equivalent table or a specialization of broader results might establish the sharp orbit count; independent priority review remains appropriate.

## Limitations

The theorem concerns the integer quadratic-weight exponent \(2\), one-complex-variable disk character spaces, and scalar reproducing kernels. It does not classify other weights, mixed character kernels, or kernel zeros for arbitrary orbifold geometries. The negative-real-root property itself is substantially anticipated by Veronese real-rootedness results. Historical publication priority of the sharp one-to-two *attainable zero-orbit* threshold remains qualified; no independent mathematical audit has been performed.

## References

1. J. Ross and R. P. Thomas, *Weighted Bergman kernels on orbifolds*, arXiv:0907.5215 (first posted 2009-07-30).
2. Y. E. Zeytuncu, *Weighted Bergman Projections and Kernels: Lp Regularity and Zeros*, arXiv:1009.2806 (2010).
3. K. Jochemko, *On the real-rootedness of the Veronese construction for rational formal power series*, arXiv:1602.09139 (2016).
4. J. Park, *The Zeros of the Bergman Kernel for Some Reinhardt Domains*, Journal of Function Spaces (2016), DOI:10.1155/2016/3856096.
