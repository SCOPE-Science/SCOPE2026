# Exact first-degree Hardy \(H^4\) approximants to geometric sums and a sharp boundary-root approach

## Finding
For each integer \(n\ge1\), put \(f_n(z)=\sum_{j=0}^{n}z^j\), and minimize \(\|1-qf_n\|_{H^4}\) over all complex polynomials \(q\) of degree at most one. The unique minimizer is
\[
q_n(z)=\frac{1+t_n}{2}+\frac{t_n-1}{2}z,
\]
where \(t_n\in(0,1)\) is the unique real zero in that interval of
\[
(16n^3+48n^2+32n+9)t^3-(36n^2+72n+27)t^2+(36n+27)t-9=0.
\]
It has a single zero, located at the real point
\[
\omega_n=\frac{1+t_n}{1-t_n}>1.
\]
If \(c_*\) is the unique real root of \(16c^3-36c^2+36c-9=0\), then
\[
\lim_{n\to\infty}nt_n=c_*=0.357498368378205\ldots,
\qquad
\lim_{n\to\infty}n(\omega_n-1)=2c_*=0.714996736756410\ldots.
\]
In particular, the zero-free radius greater than one cannot hold uniformly for all first-degree optimal approximants in \(H^4\): this explicit natural family has roots outside the closed unit disk that converge to the unit circle at an exact rate.

## Assumptions and scope
The space \(H^4\) is the classical Hardy space on the unit disk with \(\|g\|_{H^4}^4=\int_0^{2\pi}|g(e^{i\theta})|^4\,d\theta/(2\pi)\). The integer \(n\) ranges over all \(n\ge1\); complex coefficients of \(q\) are unrestricted, and the degree bound is exactly one. Here \(f_n\) is a polynomial with \(f_n(0)=1\). No statement about arbitrary \(H^4\) inputs or higher-degree approximants is made.

## Proof
**Uniqueness and two symmetries.** The map \(q\mapsto1-qf_n\) is affine and injective. Because \(L^4\) is strictly convex, \(\|1-qf_n\|_{H^4}\) is strictly convex in the complex coefficient pair. Coercivity on the finite-dimensional space gives a minimizer, which is therefore unique. Complex conjugation of coefficients preserves the objective because \(f_n\) is real-coefficient; hence the unique minimizer \(q(z)=a+bz\) has real \(a,b\).

Its residual has coefficients
\[
(1-a,\;\underbrace{-(a+b),\ldots,-(a+b)}_{n\text{ coefficients}},\;-b).
\]
Reversing this real coefficient vector preserves the \(H^4\) norm, since on the circle the reversed polynomial is \(z^{n+1}R(1/z)\) and the normalized integral is invariant under \(z\mapsto z^{-1}\). The reversed vector is another feasible residual, corresponding to \(q'(z)=(1+b)+(a-1)z\). By uniqueness, the endpoints agree: \(1-a=-b\), so \(a-b=1\). Write \(t=a+b\); this forces \(a=(1+t)/2\), \(b=(t-1)/2\), and \(s=(1-t)/2\). The residual becomes
\[
R_t(z)=s-t\sum_{j=1}^nz^j+sz^{n+1}.
\]

**Exact fourth moment.** For any real polynomial \(R(z)=\sum_{j=0}^{n+1}r_jz^j\), define aperiodic correlations \(A_d=\sum_{j=0}^{n+1-d}r_jr_{j+d}\). Fourier orthogonality gives the exact identity
\[
\|R\|_{H^4}^4=A_0^2+2\sum_{d=1}^{n+1}A_d^2.
\]
For \(R_t\), direct enumeration yields
\[
A_0=2s^2+nt^2,\qquad
A_d=(n-d)t^2-2st\quad(1\le d\le n),\qquad
A_{n+1}=s^2.
\]
Using \(\sum_{j=0}^{n-1}j=n(n-1)/2\) and \(\sum_{j=0}^{n-1}j^2=n(n-1)(2n-1)/6\), the exact objective is
\[
F_n(t)=6s^4+12ns^2t^2-4n(n-1)st^3+\frac{n(2n^2+1)}3t^4,
\qquad s=\frac{1-t}{2}.
\]
Its derivative satisfies
\[
6F_n'(t)=(16n^3+48n^2+32n+9)t^3-(36n^2+72n+27)t^2+(36n+27)t-9.
\]
The fourth-power norm \(F_n(t)\) is strictly convex by strict convexity of \(L^4\) and injectivity of \(t\mapsto R_t\). The derivative is negative at \(t=0\) and positive at \(t=1\), since \(6F_n'(0)=-9\) and \(6F_n'(1)=4n(4n^2+3n-1)>0\). Thus its unique minimizing point is precisely the stated \(t_n\in(0,1)\). Because every original minimizer lies on this invariant line, it is globally optimal among unrestricted complex linear \(q\). Its root is \(\omega_n=(1+t_n)/(1-t_n)>1\).

**Sharp large-degree limit.** Put \(t=c/n\) into the exact derivative polynomial. For fixed real \(c\),
\[
\lim_{n\to\infty}6F_n'(c/n)=P(c):=16c^3-36c^2+36c-9.
\]
The derivative \(P'(c)=48c^2-72c+36=12(4c^2-6c+3)>0\) for every real \(c\), because the quadratic discriminant is negative. Also \(P(0)=-9<0\) and \(P(1)=7>0\), so \(P\) has a unique real zero \(c_*\in(0,1)\). For any sufficiently small \(\varepsilon>0\), the derivative signs at \((c_*\pm\varepsilon)/n\) eventually agree with the signs of \(P(c_*\pm\varepsilon)\). Strict convexity therefore traps \(nt_n\) between these endpoints. Let \(\varepsilon\downarrow0\) to obtain \(nt_n\to c_*\). Finally \(n(\omega_n-1)=2nt_n/(1-t_n)\to2c_*\).

## Verification
The included standalone script `check.py` rederives the coefficient correlation formula by direct convolution, compares it with the closed quartic, checks derivative-root bracketing for several integers, and verifies the limiting constant. The proof above is analytic for all \(n\ge1\); finite computations are corroboration, not an infinite certificate. Coefficients and roots can be reproduced from the exact integer cubic without numerical integration.

## Relationship to prior work
Centner, Cheng, and Felder introduced and analyzed degree-zero and degree-one optimal polynomial approximants in classical Hardy \(H^p\), including a universal positive lower bound for the moduli of their roots for even \(p>2\) (Theorem 5.16 in arXiv:2305.16068). That theorem does not calculate the exact approximant for the growing geometric-sum family nor exclude a uniform root-radius bound strictly greater than one. Cheng and Felder (arXiv:2310.16010) develop additional Hardy-space properties without the present exact cubic or boundary rate. The new statement concerns a specific, canonical family, and proves that a universal bound stronger than one is impossible. It does *not* decide whether all such first-degree roots lie outside the open unit disk.

## Limitations
No all-input zero-exclusion theorem is claimed; roots for other \(H^4\) functions might occur inside the unit disk. Only degree-one approximants are treated. Existing literature could contain an equivalent family-specific computation under different terminology; further external historical checks are welcome. The proof has not been independently audited.

## References
1. R. Centner, R. Cheng, C. Felder, *Optimal Polynomial Approximants in \(H^p\)*, arXiv:2305.16068 (first public 2023-05-25), especially Theorem 5.16 and its discussion of zero locations.
2. R. Cheng, C. Felder, *More Properties of Optimal Polynomial Approximants in Hardy Spaces*, arXiv:2310.16010 (first public 2023-10-24).
