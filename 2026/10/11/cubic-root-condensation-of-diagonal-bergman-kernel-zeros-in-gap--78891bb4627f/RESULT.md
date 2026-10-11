# Cubic-root condensation of diagonal Bergman-kernel zeros in gap-three Hartogs triangles

## Finding

Let \(k\geq0\) be an integer, \(r\in\{1,2\}\), \(n=3k+r\), and \(m=n+3\). Let \(Q_{m,n}(s)=s^{1-2n}P_{m,n}(s,s)\) be the normalized diagonal numerator in the Bergman kernel of the rational Hartogs triangle \(\mathbb H_{m/n}=\{(z_1,z_2):|z_1|^{m/n}<|z_2|<1\}\), with \(P_{m,n}\) normalized exactly as in Edholm--Mathew, Theorem 1.3. Then \(Q_{m,n}\) is a reciprocal sextic with six simple roots, none on \(|s|=1\). Precisely three lie in \(0<|s|<1\): one is real negative and two form a nonreal conjugate pair.

Write the interior roots \(\rho_k\in(-1,0)\), \(s_{+,k}\) with positive imaginary part, and \(s_{-,k}=\overline{s_{+,k}}\). For either fixed residue \(r\), the sharp boundary-condensation law is
\[
\rho_k\longrightarrow -2+\sqrt3,\qquad
s_{\pm,k}=e^{\pm 2\pi i/3}\left(1-\frac{\sqrt{2/3}}{k}+o(k^{-1})\right),\quad k\longrightarrow\infty.
\]
In particular \(\displaystyle\lim_{k\to\infty}n(1-|s_{\pm,k}|)=\sqrt6\); thus the pair of nonreal zero-product levels approaches the two primitive cube roots of unity at a quantified radial rate, while the third remains in the interior. The asymptotic is a statement for each of the two integer progressions independently, not a claim of uniformity in arbitrary rational slopes.

## Assumptions and scope

All integers are positive where required; \(n=3k+r\) ensures \(\gcd(m,n)=\gcd(3,n)=1\), including \(k=0\). The source's diagonal variable is the product \(s=z_1\overline w_1=z_2\overline w_2\), with \(0<|s|<1\). We classify zeros of the diagonal numerator \(Q_{m,n}\), not the entire zero variety of the two-variable Bergman kernel. Every diagonal root corresponds to a genuine kernel zero along the oblique punctured disk, because the denominator is nonzero there (Edholm--Mathew, Section 1.2.1).

## Proof

**Step 1: an explicit reciprocal sextic.** For \(m=n+3\), the paper's integers
\[
L(j)=\left\lceil\frac{1+n(j+1)}m\right\rceil,
\qquad \kappa(j)=m+n-1+nj-mL(j),\qquad0\le j\le m-2
\]
satisfy \(h(j):=j+1-L(j)=\lfloor(3j+2)/m\rfloor\), and \(\kappa(j)=m(h(j)+1)-4-3j\). On the three consecutive subintervals where \(h=0,1,2\), the index ranges are respectively
\[
\begin{array}{ll}
r=1:&[0,k],\ [k+1,2k+1],\ [2k+2,3k+2],\\
r=2:&[0,k],\ [k+1,2k+2],\ [2k+3,3k+3].
\end{array}
\]
Substitution into the four exact finite sums of Edholm--Mathew (equations 3.21b--e, with powers \(h,h+1,h+3,h+4\)) and the central term \(m^2s^3\) yields
\[
Q_{m,n}(s)=a(1+s^6)+b(s+s^5)+c(s^2+s^4)+d s^3.
\]
Here, for \(r=1\),
\[
\begin{aligned}
a&=\tfrac12(k+1)^2(k+2),\\
b&=(k+1)(3k^2+9k+7),\\
c&=(k+1)(6k^2+18k+13),\\
d&=8k^3+32k^2+45k+22;
\end{aligned}
\]
for \(r=2\),
\[
\begin{aligned}
a&=\tfrac12(k+1)(k+2)^2,\\
b&=(k+2)(3k^2+9k+7),\\
c&=(k+2)(6k^2+18k+13),\\
d&=8k^3+40k^2+69k+41.
\end{aligned}
\]
All four identities are direct evaluations of sums of quadratic expressions in \(j\) over the stated integer intervals. This derivation uses the source formula as a premise; it is not inferred from finitely many sampled polynomials.

**Step 2: exact location and simplicity.** Put \(u=s+s^{-1}\). Then
\[
Q_{m,n}(s)=s^3 R_k(u),\qquad
R_k(u)=a u^3+b u^2+(c-3a)u+d-2b.
\]
The discriminant of \(R_k\) is, for \(r=1\),
\[
-\frac{(k+1)^3(3k+4)^2}{4}
(18k^5+138k^4+490k^3+970k^2+1015k+431),
\]
and, for \(r=2\),
\[
-\frac{(k+2)^3(3k+5)^2}{4}
(18k^5+132k^4+454k^3+848k^2+811k+310).
\]
Both are strictly negative for every \(k\ge0\), so \(R_k\) has one simple real root and a simple nonreal conjugate pair. Moreover
\[
R_k(-2)=\begin{cases}
k^3+4k^2+10k+8,&r=1,\\
k^3+5k^2+13k+13,&r=2,
\end{cases}\qquad R_k(2)=m^3>0.
\]
Since \(a>0\) and \(R_k(u)\to-\infty\) as \(u\to-\infty\), its real root lies strictly below \(-2\). Each root \(u\ne\pm2\) yields exactly two distinct solutions of \(s^2-us+1=0\), reciprocal in modulus. If \(|s|=1\), then \(u=2\operatorname{Re}s\in[-2,2]\); none of the three \(u\)-roots lies there. Hence each \(u\)-root supplies precisely one simple interior \(s\)-root. For \(u<-2\) the interior solution is negative real, and for the two nonreal \(u\)-roots it is a nonreal conjugate pair. This proves the all-parameter part.

**Step 3: the radial scaling limit.** Divide \(R_k(u)\) by \(k^3\): in both progressions its coefficientwise limit is
\[
\tfrac12u^3+3u^2+\tfrac92u+2=\tfrac12(u+1)^2(u+4).
\]
Since the unique real root is below \(-2\), it converges to \(-4\), giving \(\rho_k\to -2+\sqrt3\). For the other roots make the *different*, local substitution \(u=-1+v/k\). Direct substitution into the explicit coefficients gives, uniformly for \(v\) in compact subsets of the complex plane,
\[
\frac{R_k(-1+v/k)}k\longrightarrow\frac32v^2+3.
\]
To see why no hidden term survives: the coefficient of \(v\) in \(R_k(v-1)\) is precisely \(-(k+1)\) for \(r=1\), respectively \(-(k+2)\) for \(r=2\); its constant term is \(3k+4\), respectively \(3k+5\); its quadratic coefficient is \((3/2)k^3+O(k^2)\), while its cubic coefficient is \(O(k^3)\). By the argument principle on small fixed circles about the two simple limiting zeros, the nonreal roots are
\[
u_{\pm,k}=-1\pm\frac{i\sqrt2}{k}+o(k^{-1}).
\]
The two inverse branches of \(s+s^{-1}\) at \(u=-1\) are the primitive cubic roots \(\zeta_\pm=e^{\pm2\pi i/3}\). Along the inward radial perturbation \(s=\zeta_\pm(1-\delta)\), differentiation gives \(u+1=\mp i\sqrt3\,\delta+O(\delta^2)\). Comparing imaginary first-order coefficients, and using that the real first-order coefficient of \(u+1\) vanishes, yields
\[
s_{\pm,k}=\zeta_\pm\left(1-\frac{\sqrt{2/3}}k+o(k^{-1})\right).
\]
Multiplication by \(n=3k+r\) gives \(n(1-|s_{\pm,k}|)\to\sqrt6\).

## Verification

The standalone standard-library script `verify_gap3_roots.py` independently calculates the diagonal polynomial from the source's integer \(L(j)\), \(\kappa(j)\) sums, checks the six coefficient formulas against 122 admissible integer pairs, and evaluates the exact cubic-discriminant identities and endpoint values using integers and rational numbers (610 assertions). Run `python3 verify_gap3_roots.py`. The code is a **finite consistency check**, not a proof that the identities hold for all \(k\); the derivation and discriminant factorizations above give the universal argument. The limit proof is analytic and does not rely on root-fitting numerics.

## Relationship to prior work

Edholm--Mathew (first public arXiv version 26 May 2025; later journal publication) introduce the exact polynomial and establish its palindromic symmetry, then handle gaps \(m-n=1\) and \(m-n=2\) analytically. Their Section 4 does not state the present sextic root-type classification or the sharp cube-root condensation law for gap three. A secondary mathematical problem index reports that the mere **unit-circle nonvanishing for gap three** has already been proved, without identifying the underlying proof; accordingly neither nonvanishing nor the count of three interior roots alone is claimed as new. The new assertion being compared is the exact negative-real/nonreal division and, centrally, the universal first-order radial coefficient \(\sqrt6\) for the two boundary-bound zero levels. Other diagonal-gap results are not assumed to imply this coefficient.

## Limitations

The polynomial zero classification is for the one-variable diagonal slice, not an exhaustive description of all Bergman-kernel zeros. The sharp asymptotic is as \(k\to\infty\) along the two coprime difference-three progressions. This result does not resolve the general unit-circle nonvanishing conjecture. Since a secondary index mentions a gap-three proof without linking it, undiscovered prior work could subsume portions of this result; independent audit remains necessary. The analytic argument depends on the normalization and numerator formula from Edholm--Mathew.

## References

1. L. D. Edholm and V. T. Mathew, *Arithmetic properties and zeros of the Bergman kernel on a class of quotient domains*, arXiv:2505.20489 (first public 26 May 2025), later *Mathematische Zeitschrift* 313, article 43 (2026), DOI 10.1007/s00209-026-04059-8; especially Theorem 1.3, equations (3.21), Theorem 1.5, Theorem 1.7 and Section 4.
2. MathDB, *Non-vanishing conjecture for the polynomials Q(m,n) on the unit circle*, problem 368572, accessed October 2026. Its unlinked progress assertion for gap three is treated as a prior-coverage warning, not proof of a first discovery.
