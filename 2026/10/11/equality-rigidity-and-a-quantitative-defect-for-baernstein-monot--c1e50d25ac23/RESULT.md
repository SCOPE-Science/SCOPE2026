# Equality rigidity and a quantitative defect for Baernstein monotonicity

## Finding

Let
\[
p
\]
be a nonzero polynomial of degree
\[
n\ge1
\]
whose zeros all lie on
\[
\mathbb T,
\]
and set
\[
Q_n(z)=1+z^n.
\]
For
\[
0\le r\le\infty,
\]
define
\[
F_p(r)
=
\log\frac{\|p\|_r}{\|Q_n\|_r},
\]
with the Mahler measure at
\[
r=0
\]
and the supremum norm at
\[
r=\infty.
\]

Then there is a complete equality dichotomy.

Either
\[
p(z)=c(\omega+z^n),
\qquad
c\ne0,
\qquad
|\omega|=1,
\]
in which case
\[
F_p
\]
is constant on the whole interval
\[
[0,\infty],
\]
or
\[
F_p
\]
is strictly increasing on
\[
[0,\infty].
\]

Equivalently, for every pair
\[
0\le s<t\le\infty,
\]
equality in Baernstein's sharp comparison
\[
\frac{\|p\|_s}{\|Q_n\|_s}
\le
\frac{\|p\|_t}{\|Q_n\|_t}
\]
holds if and only if the zeros of
\[
p
\]
form a regular
\[
n
\]
-gon.

For polynomials with simple unimodular zeros, the strictness can be quantified. Normalize as in the source:
\[
p(z)
=
1+a_1z+\cdots+a_{n-1}z^{n-1}+z^n
\]
and put
\[
q
=
p-\frac1n zp'.
\]
The source proves that
\[
q
\]
is zero-free on the closed disk. For
\[
r>0,
\]
take the analytic branch
\[
q(z)^{r/2}
=
\sum_{k\ge0}c_k(r)z^k
\]
with constant term
\[
1.
\]
Writing
\[
M_f(r)
=
\int_{\mathbb T}|f|^r\,dm,
\]
one has
\[
F_p'(r)
\ge
\frac{
2M_{Q_n}(r)
}{
n r^2(r+2)M_p(r)
}
\sum_{k\ge1}
\frac{k}{2k+1}
|c_k(r)|^2.
\]

The right-hand side is positive unless
\[
p(z)=1+z^n
\]
in the normalized coordinates. It therefore gives an explicit Hardy--Dirichlet defect behind the qualitative monotonicity theorem.

## Assumptions and scope

The first, global equality statement allows arbitrary multiplicities among the unimodular zeros.

The quantitative derivative estimate uses the simple-zero hypothesis because the source's polar factor is then zero-free on the closed disk and its quotient with the reflected factor is a finite Blaschke product.

The theorem does not assert that the displayed lower bound is the best possible quantitative stability coefficient. Its role is to give a universal, explicit, strictly positive defect away from the regular-polygon extremizer on the simple-root stratum.

The normalization by rotation and nonzero scalar multiplication preserves every ratio
\[
\|p\|_r/\|Q_n\|_r.
\]

## Proof

Zhang's theorem gives
\[
F_p(s)\le F_p(t)
\qquad
(0\le s\le t\le\infty).
\]

First consider equality rigidity for arbitrary root multiplicities.

For
\[
r>0,
\]
put
\[
M_p(r)
=
\int_{\mathbb T}|p|^r\,dm.
\]
The map
\[
r\longmapsto M_p(r)
\]
is real analytic on
\[
(0,\infty).
\]
Indeed, near a boundary zero of multiplicity
\[
m,
\]
the boundary modulus is comparable to
\[
|\theta-\theta_0|^m.
\]
On every compact subinterval of positive exponents, all differentiated parameter integrands are dominated by an integrable function of the form
\[
|\theta-\theta_0|^{m\varepsilon}
\bigl(1+|\log|\theta-\theta_0||^j\bigr).
\]
Thus parameter differentiation is locally dominated to every order. Since
\[
M_p(r)>0,
\]
both
\[
r^{-1}\log M_p(r)
\]
and
\[
F_p(r)
\]
are real analytic on
\[
(0,\infty).
\]

Suppose equality holds for some
\[
0\le s<t\le\infty.
\]
Monotonicity forces
\[
F_p
\]
to be constant on the interval between the two exponents. That interval contains a nonempty open subinterval of
\[
(0,\infty).
\]
Real analyticity therefore forces
\[
F_p
\]
to be constant on all of
\[
(0,\infty).
\]
In particular,
\[
F_p'(2)=0.
\]

Zhang's exponent-differentiation identity identifies
\[
4F_p'(2)
\]
with the difference between the relative entropies of the normalized
\[
|p|^2
\]
and
\[
|Q_n|^2
\]
densities. Hence equality of the derivatives at
\[
2
\]
is precisely equality in the homogeneous Agler--McCarthy entropy inequality. Lei and Zhang proved that equality there holds if and only if
\[
p(z)=c(\omega+z^n),
\qquad
c\ne0,
\qquad
|\omega|=1.
\]

Conversely, for such a binomial, a rotation of the circle and multiplication by
\[
c
\]
show that
\[
\|p\|_r
=
|c|\|Q_n\|_r
\]
for every exponent, including both endpoints. This proves the global dichotomy.

Now assume the roots are simple and use Zhang's normalized polar factorization. Let
\[
a=r/2,
\qquad
g=q^a,
\qquad
B=q^*/q.
\]
The source's boundary-to-area identity is
\[
\mathcal P_r(q,B)
=
\frac{M_{Q_n}(r)}{an}
\int_{\mathbb D}
\operatorname{Re}H_a(B(z))
|g'(z)|^2\,dA(z),
\]
and its kernel theorem gives
\[
\operatorname{Re}H_a(w)>0
\qquad
(w\in\mathbb D)
\]
with
\[
\operatorname{Re}H_a(0)
=
\frac1{a+1}.
\]

Apply Harnack's inequality to the positive harmonic function
\[
\operatorname{Re}H_a.
\]
Since the source also proves
\[
|B(z)|\le|z|,
\]
one obtains
\[
\operatorname{Re}H_a(B(z))
\ge
\frac1{a+1}
\frac{1-|B(z)|}{1+|B(z)|}
\ge
\frac1{2(a+1)}
(1-|z|).
\]
Therefore
\[
\mathcal P_r(q,B)
\ge
\frac{M_{Q_n}(r)}
{2an(a+1)}
\int_{\mathbb D}
(1-|z|)
|g'(z)|^2\,dA(z).
\]

For
\[
g(z)=\sum_{k\ge0}c_k(r)z^k
\]
and normalized area measure, orthogonality gives the exact radial identity
\[
\int_{\mathbb D}
(1-|z|)
|g'(z)|^2\,dA(z)
=
\sum_{k\ge1}
\frac{k}{2k+1}
|c_k(r)|^2.
\]

The source's entropy decomposition contains a nonnegative entropy term plus
\[
\frac{r}{M_p(r)}\mathcal P_r(q,B).
\]
Combining this decomposition with
\[
F_p'(r)
=
\frac{
\mathsf D(\rho_{p,r}\|m)
-
\mathsf D(\rho_{Q_n,r}\|m)
}{r^2}
\]
and
\[
a=r/2
\]
gives
\[
F_p'(r)
\ge
\frac{
2M_{Q_n}(r)
}{
n r^2(r+2)M_p(r)
}
\sum_{k\ge1}
\frac{k}{2k+1}
|c_k(r)|^2.
\]

If the sum vanishes, then
\[
q^{r/2}
\]
is constant, hence
\[
q
\]
is constant. Comparing coefficients in
\[
q=p-\frac1n zp'
\]
forces all intermediate coefficients of the normalized
\[
p
\]
to vanish. Thus
\[
p=1+z^n.
\]
The converse is immediate.

## Verification

The global equality argument was checked at all endpoint configurations. If equality occurs with
\[
s=0
\]
or
\[
t=\infty,
\]
monotonicity still makes
\[
F_p
\]
constant on a nonempty interval of finite positive exponents, so the analytic-continuation step applies unchanged.

The real-analyticity argument is local in the exponent and remains valid with repeated boundary zeros. A boundary zero of multiplicity
\[
m
\]
contributes the model factor
\[
|\theta-\theta_0|^{mr},
\]
whose parameter derivatives remain locally integrable for every fixed positive exponent.

For the quantitative estimate, the constants were replayed from the source identities:
\[
r=2a,
\]
the area identity contributes
\[
M_{Q_n}(r)/(an),
\]
Harnack contributes
\[
1/(2(a+1)),
\]
the entropy decomposition contributes
\[
r/M_p(r),
\]
and exponent differentiation contributes
\[
1/r^2.
\]
Their product is exactly
\[
\frac{
2M_{Q_n}(r)
}{
n r^2(r+2)M_p(r)
}.
\]

The radial integral was independently evaluated:
\[
2k^2
\int_0^1
(1-\rho)\rho^{2k-1}\,d\rho
=
\frac{k}{2k+1}.
\]

No finite experiment is used as proof.

## Relationship to prior work

Zhang proves the full Baernstein quasi-norm monotonicity conjecture for arbitrary unimodular-root multiplicities. The theorem is stated as nondecreasing, and the paper says that regular-polygon binomials attain equality. The inspected article does not state an if-and-only-if equality classification for two distinct exponents, and a full-text search finds no strict-monotonicity statement.

The same article proves the positive-kernel area identity used above. The quantitative inequality here is obtained by combining that identity with Harnack's inequality and an exact weighted Dirichlet coefficient calculation; the resulting explicit defect is not stated in the source.

Lei and Zhang previously proved the homogeneous Agler--McCarthy entropy inequality and classified its equality cases at exponent
\[
2.
\]
That result supplies the rigidity anchor used after real analyticity propagates an equality interval to exponent
\[
2.
\]
It does not itself compare arbitrary pairs of quasi-norm exponents or provide the all-exponent Hardy--Dirichlet defect.

Targeted searches for strict Baernstein monotonicity, equality cases for arbitrary exponent pairs, regular-polygon rigidity, and quantitative all-exponent defects did not locate an implication-equivalent published statement.

## Limitations

The quantitative derivative bound is asserted only for simple unimodular zeros. The global equality classification does allow repeated roots.

The displayed Hardy--Dirichlet defect is universal but is not claimed to be quantitatively optimal.

The theorem concerns the normalized circle integral means in Baernstein's problem; no stability estimate directly in terms of angular zero discrepancy is asserted.

The proof of the global equality classification uses the previously established equality theorem for the homogeneous entropy inequality at exponent
\[
2.
\]

## References

1. T. Zhang, *Baernstein's Quasi-Norm Monotonicity Conjecture for Polynomials with Unimodular Zeros*, arXiv:2610.02009v1, first posted 1 October 2026.
2. J. Lei and T. Zhang, *Proof of the Agler--McCarthy Entropy Conjecture*, arXiv:2605.03949v2, first posted 5 May 2026.
3. J. Agler and J. E. McCarthy, *The Krzyż Conjecture and an Entropy Conjecture*, Journal d'Analyse Mathématique 144 (2021), 207--226, DOI: 10.1007/s11854-021-0178-z.
