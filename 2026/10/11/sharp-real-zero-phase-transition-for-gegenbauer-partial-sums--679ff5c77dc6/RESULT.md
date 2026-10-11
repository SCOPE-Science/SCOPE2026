# Sharp real-zero phase transition for Gegenbauer partial sums

## Finding

For
\[
\alpha>0,
\]
define
\[
S_n^{(\alpha)}(z)
=
\sum_{k=0}^n C_k^{(\alpha)}(z),
\]
where \(C_k^{(\alpha)}\) is the Gegenbauer polynomial, and let
\[
R_n(\alpha)
\]
be the number of real zeros of \(S_n^{(\alpha)}\), counted with multiplicity.

There is a sharp phase transition at
\[
\alpha=1.
\]

For
\[
\alpha\ge1,
\]
the recent theorem of Tran and White states that all \(n\) zeros of \(S_n^{(\alpha)}\) lie in
\[
(-1,1)
\]
for all sufficiently large \(n\).

For every
\[
0<\alpha<1,
\]
the complementary behavior is
\[
\frac{R_n(\alpha)}{n}
\longrightarrow0.
\]

Thus the threshold is not merely a sufficient range for eventual real-rootedness. Below it, asymptotically almost every zero leaves the real axis.

## Assumptions and scope

The parameter is fixed while
\[
n\longrightarrow\infty.
\]
Zeros are counted with algebraic multiplicity.

The subcritical proof uses the standard uniform interior asymptotic for Gegenbauer polynomials for
\[
0<\alpha<1
\]
and the derivative identity
\[
\frac{d}{dz}S_n^{(\alpha)}(z)
=
2\alpha S_{n-1}^{(\alpha+1)}(z).
\]

The recent source proves both eventual real-rootedness and the arcsine zero-density law for the supercritical parameter
\[
\alpha+1>1.
\]

No assertion is made here about the exact number of real zeros for a fixed finite \(n\), nor about the detailed complex limiting zero measure when
\[
0<\alpha<1.
\]

## Proof

Fix
\[
0<\alpha<1.
\]

We first prove that \(S_n^{(\alpha)}\) is eventually positive on every compact subinterval of
\[
(-1,1).
\]

Write
\[
x=\cos\theta.
\]
For every fixed
\[
0<\varepsilon<\frac{\pi}{2},
\]
the standard ultraspherical asymptotic, uniformly for
\[
\varepsilon\le\theta\le\pi-\varepsilon,
\]
has the form
\[
C_k^{(\alpha)}(\cos\theta)
=
A_\alpha
\frac{(2\alpha)_k}{(\alpha+1)_k}
\frac{
\cos\!\left(
(k+\alpha)\theta-\frac{\alpha\pi}{2}
\right)
}{
(2\sin\theta)^\alpha
}
+
O_\varepsilon(k^{\alpha-2}),
\]
where
\[
A_\alpha>0
\]
depends only on \(\alpha\).

Set
\[
b_k
=
\frac{(2\alpha)_k}{(\alpha+1)_k}.
\]
Then
\[
b_k\asymp k^{\alpha-1},
\]
and
\[
\frac{b_{k+1}}{b_k}
=
\frac{k+2\alpha}{k+\alpha+1}
<
1
\]
because
\[
\alpha<1.
\]
Thus \(b_k\) decreases to zero.

The partial sums of
\[
e^{ik\theta}
\]
are uniformly bounded when
\[
\varepsilon\le\theta\le\pi-\varepsilon.
\]
Dirichlet summation therefore gives
\[
\sum_{k>n}
b_k e^{ik\theta}
=
O_\varepsilon(b_{n+1})
=
O_\varepsilon(n^{\alpha-1}).
\]
The summed error satisfies
\[
\sum_{k>n}k^{\alpha-2}
=
O(n^{\alpha-1}),
\]
since
\[
\alpha-2<-1.
\]
Consequently,
\[
\sum_{k>n}
C_k^{(\alpha)}(\cos\theta)
=
O_\varepsilon(n^{\alpha-1})
\]
uniformly in the same angular interval.

The ordinary series therefore converges uniformly on compact subsets of
\[
(-1,1).
\]
Its Abel sum is obtained from the Gegenbauer generating function:
\[
\sum_{k=0}^{\infty}
C_k^{(\alpha)}(x)t^k
=
(1-2xt+t^2)^{-\alpha}.
\]
Letting
\[
t\uparrow1
\]
gives
\[
\sum_{k=0}^{\infty}
C_k^{(\alpha)}(x)
=
(2-2x)^{-\alpha}.
\]
Hence, uniformly on every compact
\[
K\subset(-1,1),
\]
\[
S_n^{(\alpha)}(x)
=
(2-2x)^{-\alpha}
+
O_K(n^{\alpha-1}).
\]
The limiting function is strictly positive, so
\[
S_n^{(\alpha)}(x)>0
\]
on \(K\) for all sufficiently large \(n\).

Now use
\[
\left(S_n^{(\alpha)}\right)'
=
2\alpha S_{n-1}^{(\alpha+1)}.
\]
Because
\[
1<\alpha+1<2,
\]
the recent zero-distribution theorem implies that, for all sufficiently large \(n\), every zero of
\[
\left(S_n^{(\alpha)}\right)'
\]
lies in
\[
(-1,1),
\]
and the normalized derivative-zero counting measure converges to
\[
d\mu(x)
=
\frac{dx}{\pi\sqrt{1-x^2}}.
\]

Fix
\[
0<\delta<1.
\]
Let
\[
E_\delta
=
(-1,-1+\delta)\cup(1-\delta,1).
\]
The positivity just proved shows that, for large \(n\), every real zero of \(S_n^{(\alpha)}\) that lies in
\[
[-1,1]
\]
must belong to \(E_\delta\).

On either connected component of \(E_\delta\), Rolle's theorem, with multiplicities, bounds the number of real zeros of \(S_n^{(\alpha)}\) by the number of derivative zeros there plus one.

There are no real zeros for
\[
x\ge1.
\]
Indeed, for \(x>1\),
\[
1-2xt+t^2
=
(1-r_1t)(1-r_2t)
\]
with
\[
r_1,r_2>0,
\]
and each factor
\[
(1-r_jt)^{-\alpha}
\]
has strictly positive Taylor coefficients. Hence
\[
C_k^{(\alpha)}(x)>0
\]
and therefore
\[
S_n^{(\alpha)}(x)>0.
\]

On the other hand, the derivative has no zero on
\[
(-\infty,-1)
\]
for all sufficiently large \(n\), so \(S_n^{(\alpha)}\) is strictly monotone on that ray and has at most one real zero there.

Let
\[
N_{n-1}^{(\alpha+1)}(E_\delta)
\]
denote the number of zeros of \(S_{n-1}^{(\alpha+1)}\) in \(E_\delta\). We have
\[
R_n(\alpha)
\le
N_{n-1}^{(\alpha+1)}(E_\delta)+3.
\]
Therefore
\[
\limsup_{n\to\infty}
\frac{R_n(\alpha)}{n}
\le
\mu(E_\delta).
\]
Since the arcsine law has no atom at either endpoint,
\[
\mu(E_\delta)\longrightarrow0
\]
as
\[
\delta\downarrow0.
\]
It follows that
\[
\frac{R_n(\alpha)}{n}
\longrightarrow0.
\]

Together with the recent theorem for
\[
\alpha\ge1,
\]
this gives the sharp phase transition.

## Verification

The recent primary source was inspected through its definition of
\[
S_n^{(\alpha)},
\]
its generating-function identity, the derivative relation, the theorem asserting eventual real-rootedness for
\[
\alpha\ge1,
\]
and its proof of convergence of the normalized zero density to the arcsine law.

The subcritical asymptotic input was checked against the NIST Digital Library of Mathematical Functions, §18.15(ii). For fixed
\[
0<\alpha<1,
\]
its formula is uniform on angular intervals separated from
\[
0
\quad\text{and}\quad
\pi.
\]
The prefactor ratio in that formula is decreasing precisely because
\[
\alpha<1,
\]
so ordinary Dirichlet summation gives the required uniform tail bound.

The zero-count step uses only Rolle's theorem, positivity for
\[
x>1,
\]
and the source's all-real derivative theorem at parameter
\[
\alpha+1.
\]
No finite numerical experiment is used in the proof.

## Relationship to prior work

Tran and White prove the supercritical half of the transition: for
\[
\alpha\ge1,
\]
all zeros are eventually real and lie in
\[
(-1,1),
\]
with arcsine limiting density. Their paper illustrates nonreal zeros for the Legendre case
\[
\alpha=\frac12,
\]
but does not give a theorem for the full interval
\[
0<\alpha<1
\]
or an asymptotic count of real zeros there.

Classical Gegenbauer-sum positivity and zero-free results of Ruscheweyh, Gasper, Askey, and related authors concern differently normalized or weighted sums, frequently viewed as polynomials in an auxiliary generating variable. They do not imply a zero-count theorem for the unweighted polynomial
\[
z\longmapsto
\sum_{k=0}^n C_k^{(\alpha)}(z).
\]

The present result shows that the parameter
\[
\alpha=1
\]
is a genuine asymptotic zero-geometry boundary: the real-zero fraction jumps from
\[
0
\]
below the threshold to
\[
1
\]
at and above it.

## Limitations

For
\[
0<\alpha<1,
\]
the argument determines only the asymptotic fraction of real zeros. It does not give a sharp finite-\(n\) formula for \(R_n(\alpha)\).

The complex zero-counting measure below the threshold is not identified.

No rate is asserted for
\[
R_n(\alpha)=o(n).
\]
Obtaining one would require quantitative control of the boundary layers near
\[
-1
\quad\text{and}\quad
1.
\]

## References

1. K. Tran and R. White, *On zero distribution of the sum of Gegenbauer polynomials*, arXiv:2609.38669v1, 2026.
2. NIST Digital Library of Mathematical Functions, §18.15(ii), *Ultraspherical asymptotic approximations*, formula 18.15.10.
3. G. Szegő, *Orthogonal Polynomials*, 4th ed., American Mathematical Society, 1975, Theorem 8.21.11.
4. S. Ruscheweyh, *On the Kakeya–Eneström Theorem and Gegenbauer Polynomial Sums*, SIAM Journal on Mathematical Analysis 9 (1978), 682–686. DOI: 10.1137/0509049.
5. G. Gasper, *Positive Sums of the Classical Orthogonal Polynomials*, SIAM Journal on Mathematical Analysis 8 (1977), 423–447. DOI: 10.1137/0508032.
