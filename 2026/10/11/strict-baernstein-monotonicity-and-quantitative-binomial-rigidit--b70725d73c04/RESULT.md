# Strict Baernstein monotonicity and quantitative binomial rigidity

## Finding

Let \(n\ge1\), let \(p\) be a nonzero polynomial of degree \(n\) whose zeros all lie on \(\mathbb T\), and set
\[
Q_n(z)=1+z^n.
\]
For \(0<r<\infty\), define
\[
\Phi_p(r)
=
\log\frac{\|p\|_r}{\|Q_n\|_r}.
\]

The normalized norm ratio is strictly increasing unless \(p\) is a two-term extremal. Precisely,
\[
\Phi_p'(r)>0
\qquad(r>0)
\]
for every \(p\) not of the form
\[
p(z)=c(z^n-\omega),
\qquad
c\ne0,
\quad
|\omega|=1.
\]
For those binomials, \(\Phi_p\) is constant.

Consequently, whenever
\[
0\le s<t\le\infty,
\]
equality in Baernstein's comparison
\[
\frac{\|p\|_s}{\|Q_n\|_s}
\le
\frac{\|p\|_t}{\|Q_n\|_t}
\]
holds if and only if
\[
p(z)=c(z^n-\omega).
\]
Thus the extremizers exhibited in the 2026 proof are the complete equality family for every nontrivial pair of exponents.

There is also a quantitative form below exponent two. Normalize by rotation and scaling so that
\[
p(z)=1+a_1z+\cdots+a_{n-1}z^{n-1}+z^n.
\]
If \(p\ne1+z^n\), let
\[
m
=
\min\{1\le j\le n-1:a_j\ne0\}
\]
and let
\[
H_k=\sum_{j=1}^k\frac1j.
\]
Writing
\[
M_f(r)=\int_{\mathbb T}|f|^r\,dm,
\]
one has, for every \(0<r\le2\),
\[
\frac{M_p(r)}{M_{Q_n}(r)}\,\Phi_p'(r)
\ge
\frac{m(n-m)^2(H_{2m}-1)}
{n^3(2m-1)(r+2)}
|a_m|^2.
\]

## Assumptions and scope

The circle measure \(m\) is normalized Haar measure. For \(0<r<\infty\),
\[
\|f\|_r
=
\left(
\int_{\mathbb T}|f|^r\,dm
\right)^{1/r}.
\]
The endpoint conventions are Mahler measure at \(r=0\) and supremum norm at \(r=\infty\).

The primary 2026 theorem proves that \(\Phi_p\) is nondecreasing and states that the binomials above attain equality. The present result strengthens this to strict monotonicity away from the binomial orbit and supplies the displayed coefficient-sensitive derivative gap for \(0<r\le2\).

The quantitative coefficient \(|a_m|\) is taken after the standard self-inversive normalization. Different admissible choices of the normalizing rotation change \(a_m\) only by a unimodular factor, so its modulus is well defined.

## Proof

First apply the normalization used in the primary source. After multiplying by a nonzero scalar and rotating the variable, it is enough to consider
\[
p(z)
=
1+a_1z+\cdots+a_{n-1}z^{n-1}+z^n,
\qquad
p=p^*.
\]
Put
\[
\mathcal Dp(z)=zp'(z),
\qquad
q(z)=p(z)-\frac1n\mathcal Dp(z).
\]
Then
\[
q(z)
=
1+
\sum_{j=1}^{n-1}
\left(1-\frac jn\right)a_jz^j.
\]
In particular,
\[
q\text{ is constant}
\quad\Longleftrightarrow\quad
p(z)=1+z^n.
\]
The polar-derivative argument also gives that \(q\) has no zero in \(\mathbb D\), even when the boundary zeros of \(p\) have multiplicity.

Fix
\[
r=2a>0.
\]
Use the root-splitting approximation from the primary proof to choose normalized polynomials \(p_\nu\) with simple zeros on \(\mathbb T\) and
\[
p_\nu\longrightarrow p
\]
uniformly on the closed disk. Let \(q_\nu\) be their polar factors and define
\[
B_\nu=\frac{q_\nu^*}{q_\nu},
\qquad
g_\nu=q_\nu^a.
\]
For the simple-zero approximants, \(B_\nu\) is a finite Blaschke product with
\[
B_\nu(0)=0,
\qquad
|B_\nu(z)|\le|z|.
\]

The source's Hardy--Bergman identity is
\[
\mathcal P_{2a}(q_\nu,B_\nu)
=
\frac{M_{Q_n}(2a)}{an}
\int_{\mathbb D}
\operatorname{Re}H_a(B_\nu(z))
|g_\nu'(z)|^2\,dA(z),
\]
where
\[
\operatorname{Re}H_a(w)>0
\qquad(|w|<1).
\]
Its entropy decomposition and differentiation formula imply
\[
\Phi_{p_\nu}'(2a)
\ge
\frac{
\mathcal P_{2a}(q_\nu,B_\nu)
}
{2aM_{p_\nu}(2a)}.
\]

Assume now that \(p\ne1+z^n\). Then \(q\) is nonconstant. Because \(q\) is zero free in \(\mathbb D\), the normalized analytic power
\[
g=q^a
\]
is well defined there and \(g'\) is not identically zero. Choose a closed disk \(K\Subset\mathbb D\) on which
\[
|g'|\ge c>0.
\]
The normalized logarithms of \(q_\nu\) converge locally uniformly to that of \(q\), hence
\[
g_\nu'\longrightarrow g'
\]
uniformly on \(K\). Also \(|B_\nu(z)|\le|z|\), so all \(B_\nu(K)\) lie in one compact subdisk of \(\mathbb D\). The strict positivity and continuity of \(\operatorname{Re}H_a\) therefore give a constant \(h>0\) such that
\[
\operatorname{Re}H_a(B_\nu(z))\ge h
\]
on \(K\), for all sufficiently large \(\nu\). It follows that
\[
\mathcal P_{2a}(q_\nu,B_\nu)
\]
is bounded below by a positive constant independent of \(\nu\).

For fixed positive \(r\), both
\[
M_p(r)
=
\int|p|^r\,dm
\]
and
\[
M_p'(r)
=
\int|p|^r\log|p|\,dm
\]
are continuous under uniform convergence of polynomials: the function \(x^r\log x\), extended by zero at the origin, is continuous and bounded on every fixed compact interval. Hence the entropy derivative formula passes to the limit and gives
\[
\Phi_p'(r)>0
\]
for every \(r>0\).

This proves strict monotonicity whenever \(p\) is not binomial. For \(p=1+z^n\), the ratio is identically one. Undoing the normalization gives exactly
\[
c(z^n-\omega),
\qquad
c\ne0,
\quad
|\omega|=1.
\]
The endpoint cases follow by the continuity of \(\|p\|_r\) at \(r=0\) and \(r=\infty\), already established in the source. Thus every comparison with \(s<t\) is strict off the binomial family.

For the quantitative estimate, assume
\[
0<a\le1.
\]
The small-parameter kernel estimate in the primary proof gives
\[
\operatorname{Re}H_a(w)
\ge
\frac1{a+1}
\left(
1-
\sum_{k\ge1}
\frac{|w|^k}{k(k+1)}
\right).
\]
Since \(|B_\nu(z)|\le|z|\), define
\[
W_a(\rho)
=
\frac1{a+1}
\left(
1-
\sum_{k\ge1}
\frac{\rho^k}{k(k+1)}
\right)
\]
and obtain
\[
\operatorname{Re}H_a(B_\nu(z))
\ge
W_a(|z|).
\]
If
\[
g_\nu(z)=\sum_{j\ge0}c_{\nu,j}z^j,
\]
radial orthogonality yields
\[
\int_{\mathbb D}
W_a(|z|)|g_\nu'(z)|^2\,dA(z)
=
2\sum_{j\ge1}
j^2|c_{\nu,j}|^2
\int_0^1W_a(\rho)\rho^{2j-1}\,d\rho.
\]
For every integer \(m\ge1\), partial fractions give
\[
\sum_{k\ge1}
\frac1{k(k+1)(2m+k)}
=
\frac1{2m-1}
-
\frac{H_{2m}}{2m(2m-1)},
\]
so
\[
\int_0^1W_a(\rho)\rho^{2m-1}\,d\rho
=
\frac{H_{2m}-1}
{2m(2m-1)(a+1)}.
\]

If \(m\) is the first nonzero intermediate coefficient of the limiting polynomial, then
\[
q(z)
=
1+
\left(1-\frac mn\right)a_mz^m+O(z^{m+1}),
\]
and therefore
\[
g(z)=q(z)^a
=
1+
a\left(1-\frac mn\right)a_mz^m+O(z^{m+1}).
\]
Local convergence gives
\[
c_{\nu,m}
\longrightarrow
 a\left(1-\frac mn\right)a_m.
\]
Keeping only the \(j=m\) term in the radial integral, inserting the Hardy--Bergman identity, and using the nonnegative entropy term gives
\[
\frac{M_p(r)}{M_{Q_n}(r)}\Phi_p'(r)
\ge
\frac{m(n-m)^2(H_{2m}-1)}
{n^3(2m-1)(r+2)}|a_m|^2,
\]
with \(r=2a\). This proves the quantitative statement.

## Verification

The complete primary HTML text was checked at the self-inversive normalization, polar factor, entropy differentiation, Hardy--Bergman identity, strict kernel positivity, small-exponent kernel estimate, removal of multiple zeros, and endpoint passages.

The strictness argument uses the source's own simple-root approximants but adds a compact-interior lower bound that survives their limit whenever \(q\) is nonconstant. This avoids treating numerical strictness of an approximating sequence as proof.

The quantitative coefficient is checked independently from the radial integral. The packaged algebra checker verifies the relevant partial-fraction identity and the reduction of the coefficient constant to the displayed expression for symbolic \(m,n,r\). It also checks the polar-factor coefficient relation. The checker is an algebra audit only; the global positivity and approximation steps are established analytically above.

## Relationship to prior work

Zhang's 2026 paper proves Baernstein's quasi-norm monotonicity conjecture for all exponents and all multiplicities. It states that
\[
c(z^n-\omega)
\]
attains equality, but it does not claim that these are the only equality cases. Its all-exponent relative-entropy corollary likewise states attainment by the binomial family without an equality classification.

Lei and Zhang's earlier 2026 proof of the Agler--McCarthy entropy conjecture determines the equality cases at the single exponent \(r=2\): equality there forces the same binomial family. That result does not by itself state strict Baernstein monotonicity for every exponent, nor the coefficient-sensitive derivative gap above.

Agler and McCarthy's original formulation records Baernstein's norm-ratio conjecture and the binomial equality pattern for the associated entropy conjecture. It does not contain the all-exponent theorem or the strictness conclusion.

Earlier multiplier inequalities of Arestov and Pritsker cover sharp fixed-exponent or endpoint comparisons. As the primary 2026 paper notes, those methods can imply the \(s=0\) endpoint but do not compare two arbitrary positive exponents. Targeted searches for strict Baernstein monotonicity, complete equality cases, all-exponent entropy rigidity, and a quantitative coefficient gap did not locate a published statement equivalent to the finding here.

## Limitations

The explicit coefficient gap is proved only for
\[
0<r\le2,
\]
because it uses the source's elementary small-parameter kernel bound. Strict monotonicity and equality rigidity hold for every positive exponent.

The coefficient gap is expressed after the standard self-inversive normalization and in terms of the first nonzero intermediate coefficient. It is not asserted to be the optimal quantitative stability constant.

No claim is made about polynomials whose zeros leave the unit circle.

## References

1. T. Zhang, *Baernstein's Quasi-Norm Monotonicity Conjecture for Polynomials with Unimodular Zeros*, arXiv:2610.02009v1, 2026.
2. J. Lei and T. Zhang, *Proof of the Agler--McCarthy Entropy Conjecture*, arXiv:2605.03949, 2026.
3. J. Agler and J. E. McCarthy, *The Krzyż Conjecture and an Entropy Conjecture*, Journal d'Analyse Mathématique 144 (2021), 207--226. DOI: 10.1007/s11854-021-0178-z.
4. V. V. Arestov, *Integral inequalities for algebraic polynomials on the unit circle*, Mathematical Notes 48 (1990), 977--984. DOI: 10.1007/BF01139596.
5. I. E. Pritsker, *Inequalities for integral norms of polynomials via multipliers*, Mediterranean Journal of Mathematics 14 (2017), Article 109.
