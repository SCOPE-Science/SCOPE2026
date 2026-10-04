# Exact degree-two discretized Carathéodory–Fejér extremals on every cyclic grid
## Finding
For each integer \(m\ge2\), define
\[
D_m=\sup\left\{\lambda\in\mathbb R:\exists c\in\mathbb R,\ 1+\lambda\cos(2\pi r/m)+c\cos(4\pi r/m)\ge0\ \text{for every }r\in\mathbb Z_m\right\}.
\]
Then \(D_2=D_3=+\infty\). For \(m\ge4\), set
\[
j=\left\lfloor\frac{3m}{8}\right\rfloor,\qquad k=\left\lceil\frac{3m}{8}\right\rceil,
\]
\[
u_m=\cos\left(\frac{2\pi k}{m}\right),\qquad v_m=\cos\left(\frac{2\pi j}{m}\right).
\]
The exact extremal value is
\[
D_m=-\frac{2(u_m+v_m)}{1+2u_mv_m}.
\]
When \(8\nmid m\), the extremizing coefficient is unique:
\[
c_m=\frac{1}{1+2u_mv_m},
\]
and the extremal sampled quadratic factors as
\[
1-c_m+D_mx+2c_mx^2=\frac{2(x-u_m)(x-v_m)}{1+2u_mv_m},\qquad x=\cos\left(\frac{2\pi r}{m}\right).
\]
When \(8\mid m\), the value reduces to \(D_m=\sqrt2\), attained by \(c=1/2\). Hence the finite cyclic sampling is lossless relative to the continuous degree-two problem exactly for \(8\mid m\); otherwise, for every finite nonaliased case \(m\ge4\), \(D_m>\sqrt2\).

## Assumptions and scope
The normalization fixes the constant Fourier coefficient to \(1\), allows a real first-harmonic coefficient \(\lambda\), and allows one real free coefficient at the second harmonic. Nonnegativity is imposed only at the \(m\)-th roots of unity. The aliased cases \(m=2,3\) are included explicitly. No statement is made here about additional harmonics, complex coefficients, or nonuniform sampling sets.

## Proof
Write \(x=\cos(2\pi r/m)\). Since \(\cos(4\pi r/m)=2x^2-1\), every candidate has the quadratic form
\[
q(x)=1+\lambda x+c(2x^2-1).
\]
For \(m=2\), choosing \(c=|\lambda|\) makes both sampled values nonnegative for arbitrary \(\lambda\), so \(D_2=+\infty\). For \(m=3\), the two sampled harmonics coincide, \(\cos(4\pi r/3)=\cos(2\pi r/3)\), so taking \(c=-\lambda\) gives the constant sampled value \(1\); hence \(D_3=+\infty\).

Assume \(m\ge4\), and let
\[
s=-\frac1{\sqrt2}=\cos\left(\frac{3\pi}{4}\right).
\]
If \(8\nmid m\), then \(j<3m/8<k=j+1\), so monotonicity of cosine on \([0,\pi]\) gives
\[
u_m<s<v_m.
\]
These are adjacent values of the sampled cosine grid around \(s\). Also \(1+2u_mv_m>0\): for \(m=4,5\) this is checked directly, while for \(m\ge6\) both \(u_m\) and \(v_m\) are nonpositive.

Set
\[
c_m=\frac1{1+2u_mv_m},\qquad D_m^*=-\frac{2(u_m+v_m)}{1+2u_mv_m}.
\]
A direct expansion gives
\[
q_*(x)=1-c_m+D_m^*x+2c_mx^2=\frac{2(x-u_m)(x-v_m)}{1+2u_mv_m}.
\]
No sampled cosine lies strictly between the adjacent values \(u_m\) and \(v_m\). Therefore \(q_*\) is nonnegative on the whole sampled grid, proving \(D_m\ge D_m^*\).

For the reverse inequality, let \(q\) be any feasible quadratic with first coefficient \(\lambda\). Put
\[
\alpha=1-2v_m^2>0,\qquad \beta=2u_m^2-1>0.
\]
The coefficient of \(c\) cancels in the positive combination \(\alpha q(u_m)+\beta q(v_m)\). Exact simplification yields
\[
0\le \alpha q(u_m)+\beta q(v_m)
=(u_m-v_m)\left(2(u_m+v_m)+\lambda(1+2u_mv_m)\right).
\]
Because \(u_m-v_m<0\) and \(1+2u_mv_m>0\), this forces \(\lambda\le D_m^*\). Thus \(D_m=D_m^*\). Equality in the positive combination requires \(q(u_m)=q(v_m)=0\); the two distinct roots then determine \(c=c_m\), proving uniqueness off the divisible-by-eight case.

If \(8\mid m\), the grid contains \(s\). At that point the second-harmonic factor vanishes:
\[
2s^2-1=0,
\]
so feasibility gives \(0\le q(s)=1-\lambda/\sqrt2\), hence \(\lambda\le\sqrt2\). Equality is attained by \(c=1/2\), for which
\[
q(x)=\left(x+\frac1{\sqrt2}\right)^2.
\]
The same one-point argument over the continuous circle proves that the continuous degree-two value is \(\sqrt2\). If \(8\nmid m\), this continuous extremizer is strictly positive at every sampled point; finiteness of the grid permits a small increase of \(\lambda\) while keeping \(c=1/2\), so \(D_m>\sqrt2\).

## Verification
The proof is analytic for all \(m\). The accompanying standard-library checker independently verifies, through \(m=5000\), the factorization, sampled feasibility, positivity of the two dual weights, equality of the dual upper bound with the claimed value, the divisible-by-eight cases, and the strict sampling gain off resonance. These finite checks are corroborative and are not used as a proof of the universal statement.

## Relationship to prior work
Kolountzakis and Révész introduced the discretized Carathéodory–Fejér quantity \(M_m(H)\), imposing nonnegativity only at the points \(r/m\), and related it to pointwise positive-definite extremal problems. Their framework also records aliasing phenomena and the inequality between discrete and continuous extremals. The present result evaluates their degree-two singleton case \(H=\{2\}\) on every cyclic grid, including the aliased orders, gives the exact off-resonance extremizer, and identifies the precise lossless-sampling arithmetic condition.

Krenedits and Révész later developed the same Carathéodory–Fejér-type reduction on locally compact Abelian groups. The inspected full texts provide the general reduction and classical continuous formulas but no exact all-\(m\) formula for \(M_m(\{2\})\) was located.

## Limitations
The originality comparison was concentrated on the two closest primary sources and targeted searches under discretized Carathéodory–Fejér, cyclic positive-definite, sampled nonnegative trigonometric polynomial, and finite-grid terminology. Older literature may encode the same two-variable linear program under interpolation or discrete positivity language not captured by those terms. The theorem concerns only the degree-two singleton harmonic and does not imply formulas for arbitrary frequency sets.

## References
1. M. N. Kolountzakis and S. Gy. Révész, “On pointwise estimates of positive definite functions with given support,” arXiv:math/0302193v1 (first public 2003-02-17); Canadian Journal of Mathematics 58 (2006), DOI 10.4153/CJM-2006-017-8.
2. S. Krenedits and S. Gy. Révész, “The Carathéodory-Fejér type extremal problem on locally compact Abelian groups,” arXiv:1304.0071v1 (first public 2013-03-30).
