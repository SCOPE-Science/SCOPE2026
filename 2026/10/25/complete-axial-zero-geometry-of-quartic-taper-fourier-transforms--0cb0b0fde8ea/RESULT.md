# Complete axial zero geometry of quartic-taper Fourier transforms

## Finding
For every real \(t>0\), define the entire Fourier transform
\[
F_t(z)=\int_{-1}^{1}(1-tx^4)e^{izx}\,dx\qquad(z\in\mathbb C).
\]
All its nonzero zeros are simple and lie on the union of the real and imaginary axes. For each integer \(n\ge1\), the interval \((n\pi,(n+1)\pi)\) contains exactly one positive real zero, and there are no other positive real zeros above \(\pi\). The remaining zeros, including multiplicities, have the following exhaustive classification.

* When \(0<t\le1\), there are no remaining zeros; in particular every zero is real.
* When \(1<t<5\), there is exactly one conjugate pair \(\pm iy_t\), with \(y_t>0\), and there is no real zero in \((0,\pi)\).
* When \(t=5\), the origin is a zero of multiplicity exactly two, and there are no other zeros in the open disk \(|z|<\pi\).
* When \(t>5\), there is exactly one positive real zero in \((0,\pi)\), its negative, and no imaginary zeros.

Every positive real zero in these intervals increases strictly as \(t\) increases. At the central transition,
\[
z_\pm(t)=\pm\sqrt{\frac{21}{20}(t-5)}\,(1+O(|t-5|)),
\]
where the square root takes imaginary values for \(t<5\). At the other transition, \(y_t\sim4/(t-1)\) as \(t\downarrow1\).

## Assumptions and scope
The parameter \(t\) is any finite positive real number. Zeros are counted with their complex multiplicities. All claims concern the entire transform of a possibly signed density on \([-1,1]\), not a probability characteristic function when the density changes sign. The Fourier convention is \(e^{izx}\); the evenness of the kernel makes the sign convention immaterial to the zero set.

## Proof
Set \(s(z)=\sin z/z\), continuously extended at zero. Differentiating its integral representation gives
\[
F_t(z)=2\bigl(s(z)-t s^{(4)}(z)\bigr).
\]
At \(z\ne0\), direct differentiation yields
\[
z^5s^{(4)}(z)=(z^4-12z^2+24)\sin z+(4z^3-24z)\cos z.
\]
Write \(a_n=n^2\pi^2\) and \(w=z^2\). The classical Mittag--Leffler identity
\[
z\cot z=1+2w\sum_{n\ge1}\frac1{w-a_n}
\]
and the Rayleigh identity \(\sum_{n\ge1}a_n^{-1}=1/6\) imply the exact meromorphic partial fraction expansion
\[
R(w):=\frac{s^{(4)}(\sqrt w)}{s(\sqrt w)}
=1+\sum_{n\ge1}\frac{c_n}{w-a_n},\qquad
c_n=8-\frac{48}{a_n}>0.
\]
The quotient is even in the chosen square root. The series converges locally uniformly away from its simple poles, as \(c_n\) is bounded and \(a_n\) grows quadratically. Here \(c_n>0\) follows from \(a_n\ge\pi^2>6\); this positivity is the decisive fourth-order feature.

For nonreal \(w\), the imaginary part satisfies
\[
\operatorname{Im}R(w)=-(\operatorname{Im}w)\sum_{n\ge1}
\frac{c_n}{|w-a_n|^2},
\]
which is nonzero. Hence \(R(w)=1/t\) forces \(w\) real, so \(z\) is real or purely imaginary. On every component of \(\mathbb R\setminus\{a_n\}\),
\[
R'(w)=-\sum_{n\ge1}\frac{c_n}{(w-a_n)^2}<0.
\]
On each interval \((a_n,a_{n+1})\), this function decreases continuously from \(+\infty\) to \(-\infty\), giving exactly one simple root of \(R(w)=1/t\). At the poles, \(s(z)=0\) but \(s^{(4)}(z)\ne0\), since \(c_n>0\); hence they never contribute roots of \(F_t\).

On \(( -\infty,a_1)\), \(R(w)\) decreases from its unattained limit \(1\) at \(-\infty\) to \(-\infty\) at \(a_1^-\). Moreover \(R(0)=s^{(4)}(0)/s(0)=1/5\). Comparing \(1/t\) with \(1\) and \(1/5\) yields the three central regimes and the critical parameter \(t=5\). When \(t=5\), the expansion
\[
F_t(z)=2\left(1-\frac t5+\left(-\frac16+\frac{t}{14}\right)z^2+O(z^4)\right)
\]
shows \(F_5(z)=\frac8{21}z^2+O(z^4)\), so the origin has multiplicity exactly two. Elsewhere each root is simple because \(R'(w)\ne0\) and \(w=z^2\) has nonzero derivative at \(z\ne0\).

Implicit differentiation of \(R(w_t)=1/t\) gives \(R'(w_t)w_t'=-1/t^2\), so \(w_t'>0\) and every positive real zero increases strictly. The expansion near the critical origin gives \(z^2=\frac{21}{20}(t-5)+O((t-5)^2)\). Finally, the hyperbolic form of the explicit derivative identity yields
\[
R(-y^2)=1-\frac4y+O(y^{-2})\qquad(y\to\infty),
\]
so the unique imaginary zero obeys \(y_t\sim4/(t-1)\) as \(t\downarrow1\). These arguments exhaust all entire zeros because poles of \(R\) are checked separately and all other zeros are equivalent to its level equation.

## Verification
The standalone `check.py` performs exact symbolic checks of the fourth derivative and local Taylor coefficients, independent numerical Fourier integration at twelve parameter-point pairs, nine convergent partial-fraction truncation checks, and monotone-bracket checks for thirty higher real roots, three imaginary pairs and two central real pairs. Run `python check.py` with `sympy` and `mpmath`. The recorded expected output is in `check_output.txt`. These finite numerical checks corroborate but do not replace the infinite proof above.

## Relationship to prior work
The Mittag--Leffler product and zero interlacing of sinc/Bessel functions are classical; the reference to Bessel derivative zeros by Baricz--Kokologiannaki--Pogány is a natural nearby treatment of derivatives, rather than a source of the quartic-window pencil theorem. Mercer's 1992 study treats variation with Bessel order of positive zeros of a fixed-coefficient Bessel combination. NIST DLMF §10.21 discusses Bessel and Dini zeros. The present assertion instead supplies the complete *complex* zero set for a degree-four weighted Fourier pencil and the sign-change/zero-mass phase boundaries, via an explicit positive-residue expansion specific to the fourth derivative. No assertion of exhaustive priority verification is made.

## Limitations
The conclusion holds for \(t>0\) and precisely the quartic window \(1-tx^4\); it does not classify arbitrary signed tapers or all higher even powers. The available literature comparison does not exclude an equivalent unlocated classical result, particularly within broader Fourier-critical-point or Bessel-function literature. Numerical checks alone cannot verify absence of zeros outside tested regions. No independent mathematical audit has been performed.

## References
1. Á. Baricz, C. G. Kokologiannaki, T. K. Pogány, *Zeros of Bessel function derivatives*, arXiv:1602.04295 (first public version, 2016-02-13), https://arxiv.org/abs/1602.04295 ; full text https://arxiv.org/html/1602.04295v2 .
2. A. McD. Mercer, *The zeros of \(az^2J_\nu''(z)+bzJ_\nu'(z)+cJ_\nu(z)\) as functions of order*, Int. J. Math. Math. Sci. 15 (1992), DOI:10.1155/S0161171292000395.
3. NIST Digital Library of Mathematical Functions, §10.21, https://dlmf.nist.gov/10.21 .
4. H. Ki and Y.-O. Kim, *On the number of nonreal zeros of real entire functions and the Fourier-Pólya conjecture*, Duke Math. J. (2000), DOI:10.1215/S0012-7094-00-10413-9 (abstract accessible; full-text comparison unresolved).
