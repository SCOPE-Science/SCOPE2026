# Exact mean-square periodic error for arithmetic-progression denumerants

## Finding
For every odd positive integer \(a\) and every positive integer \(d\) with \(\gcd(a,d)=1\), put \(b=a+d\), \(c=a+2d\), and \(L=abc\). Let \(R(t)\) count nonnegative integral solutions of \(ax+by+cz=t\), and define its canonical quadratic polynomial part by
\[
P(t)=\frac{t^2+(a+b+c)t}{2abc}+\frac{a^2+b^2+c^2+3ab+3ac+3bc}{12abc}.
\]
Then the following **exact** mean-square identity holds:
\[
\boxed{\frac1L\sum_{t=0}^{L-1}\bigl(R(t)-P(t)\bigr)^2
=\frac{a^4+70a^2-71}{2880a^2}
+\frac{b^4+10b^2-11}{720b^2}
+\frac{c^4+70c^2-71}{2880c^2}.}
\]
The residual is periodic with period dividing \(L\), has mean zero on a complete period, and the displayed expression is therefore its exact variance. In particular, when \(d\) is fixed and \(a\) tends to infinity through odd integers coprime to \(d\), the variance is \(a^2/480+O_d(a)\), so its root mean square is \(a/\sqrt{480}+O_d(1)\).

## Assumptions and scope
The integers \(a\ge1\) and \(d\ge1\) satisfy \(a\equiv1\pmod2\) and \(\gcd(a,d)=1\). These hypotheses make \(a,b,c\) pairwise coprime: \(\gcd(a,c)=\gcd(a,2d)=1\) and the other pairwise gcds equal one. Summands \(x,y,z\) are ordered coordinate counts in \(\mathbb Z_{\ge0}^3\), not positive solutions or unordered partitions. The exact mean is over all residues \(0\le t<L\). The case \(a=1\) is included; root sums over modulus one are empty.

## Proof
**Polynomial contribution.** The ordinary generating function is
\[
G(z)=\sum_{t\ge0}R(t)z^t=\frac1{(1-z^a)(1-z^b)(1-z^c)}.
\]
Near \(z=1\), use the expansions of each reciprocal factor in powers of \(1-z\) through the constant term. The coefficient of \(z^t\) from the pole at one is precisely \(P(t)\) as stated. Because \(a,b,c\) are pairwise coprime, all other poles are *simple*, located at nontrivial roots of unity of one and only one of the three moduli.

**Three orthogonal waves.** For each \(m\in\{a,b,c\}\), let \(u_m,v_m\) be the other two denominations, reduced modulo \(m\), and \(\zeta_m=\exp(2\pi i/m)\). Simple partial fractions at the nontrivial \(m\)-th roots give the exact identity for all nonnegative integers \(t\):
\[
R(t)-P(t)=\sum_{m\in\{a,b,c\}}F_m(t),\qquad
F_m(t)=\frac1m\sum_{j=1}^{m-1}\frac{\zeta_m^{-jt}}{(1-\zeta_m^{u_mj})(1-\zeta_m^{v_mj})}.
\]
Every \(F_m\) has mean zero on its modulus. Its nonzero Fourier frequencies on \(\mathbb Z/L\mathbb Z\) are of the form \(jL/m\), for \(1\le j<m\). For two different pairwise coprime moduli, these sets do not intersect modulo \(L\). Orthogonality thus eliminates every cross term in the period average of the squared (real) residual. Parseval yields
\[
\frac1L\sum_{t=0}^{L-1}(R(t)-P(t))^2
=\sum_{m\in\{a,b,c\}}\frac1{16m^2}\sum_{j=1}^{m-1}
\csc^2\!\left(\frac{\pi u_mj}{m}\right)
\csc^2\!\left(\frac{\pi v_mj}{m}\right).
\]
Because \(\gcd(d,m)=1\), reindexing \(j\) by \(dj\) modulo \(m\) converts the outer waves, at moduli \(a\) and \(c\), to the pair of residues \((1,2)\) (up to signs), and the middle wave, at modulus \(b\), to \((1,1)\). The moduli \(a,c\) are odd, so the doubled residues are invertible.

**Evaluation of the finite trigonometric sums.** For every integer \(m\ge1\) (empty sums when \(m=1\)), the standard cotangent multiplication identity
\[
\sum_{j=0}^{m-1}\csc^2\!\left(x+\frac{j\pi}{m}\right)=m^2\csc^2(mx)
\]
implies, on expanding at \(x=0\),
\[
\sum_{j=1}^{m-1}\csc^2\!\left(\frac{j\pi}{m}\right)=\frac{m^2-1}{3},\qquad
\sum_{j=1}^{m-1}\csc^4\!\left(\frac{j\pi}{m}\right)=\frac{m^4+10m^2-11}{45}.
\]
For the second identity, differentiate the displayed multiplication identity twice, subtract the singular \(j=0\) term, and use \(\frac{d^2}{dx^2}\csc^2x=6\csc^4x-4\csc^2x\). Hence the middle contribution is \((m^4+10m^2-11)/(720m^2)\).

For odd \(m\), the corresponding odd cosine multiplication identity gives
\[
\sum_{j=1}^{m-1}\sec^2\!\left(\frac{j\pi}{m}\right)=m^2-1.
\]
The elementary pointwise identity
\[
\csc^2x\,\csc^2(2x)=\tfrac14(\csc^4x+\csc^2x+\sec^2x)
\]
therefore yields
\[
\sum_{j=1}^{m-1}\csc^2\!\left(\frac{j\pi}{m}\right)
\csc^2\!\left(\frac{2j\pi}{m}\right)=\frac{m^4+70m^2-71}{180}.
\]
Multiplication by \(1/(16m^2)\) gives each outer contribution \((m^4+70m^2-71)/(2880m^2)\). Adding the three wave variances proves the boxed identity. Expanding the three rational expressions for fixed \(d\) gives the stated asymptotic.

## Verification
The accompanying `verify.py` independently obtains every coefficient \(R(t)\) for \(0\le t<L\) by the three successive unbounded-coin recurrences, evaluates \(P(t)\) using exact fractions, checks that the residuals sum to zero, and directly computes their average square. It verifies the closed expression without using root-of-unity, Fourier, or trigonometric identities. All 66 configurations with odd \(1\le a\le15\), \(1\le d\le10\), \(\gcd(a,d)=1\), and \(abc\le12000\) agree exactly; see the certificate produced by running `python3 verify.py`. These finite tests check implementations, not the infinite claim.

## Relationship to prior work
Aldrich, Gulbrandsen and Keddy study the three-variable restricted partition function and give period-\(abc\) upper/lower quasipolynomial bounds; their Theorem C does not determine the mean-square error of the canonical polynomial part. Kiran develops the general polynomial/periodic Sylvester-wave decomposition, providing the natural machinery underlying the proof, but no closed arithmetic-progression RMS evaluation was located in the inspected wave results. Komatsu and Ying examine the same arithmetic-progression triple through generalized Frobenius numbers, Apéry sets, genera and Sylvester sums; those are different invariants, and do not give the stated period-averaged square. Lisoněk studies pointwise approximations rather than this exact mean square. The key additional specialization here is the orthogonality of three separate wave moduli followed by explicit evaluation of a doubled-angle mixed cosecant moment.

## Limitations
The formula assumes pairwise coprime denominators of the precise three-term arithmetic progression form. Even initial terms permit shared roots between the first and third factors, introducing different pole orders, and are not covered. No claim is made for four or more denominations, or for the exact optimal pointwise approximation error. The underlying harmonic tools and special trigonometric moments are classical; an earlier unlocated deduction or implicit equivalent from a general Fourier-Dedekind identity remains a possible originality risk.

## References
1. M. Aldrich, D. Gulbrandsen and C. Keddy, *Enumerating Integral Points on Triangles in* \(\mathbb R^3\), arXiv:2610.20899, first version October 14, 2026, https://arxiv.org/abs/2610.20899.
2. N. Uday Kiran, *An Algebraic Approach to q-Partial Fractions and Sylvester Denumerants*, arXiv:2104.10989, https://arxiv.org/html/2104.10989v3.
3. T. Komatsu and H. Ying, *The Frobenius Number for Sequences of Arithmetic Progressions Associated with Number of Solutions*, arXiv:2206.13052, https://arxiv.org/abs/2206.13052.
4. P. Lisoněk, *Denumerants and Their Approximations*, Journal of Combinatorial Mathematics and Combinatorial Computing 18 (1995), https://combinatorialpress.com/article/jcmcc/Volume%2018/vol-18-paper%2021.pdf.
