# D-optimal slab concentration for biharmonic Bergman modes: a quartic-to-logarithmic crossover

## Finding

Let \(\Pi=\{x+iy\in\mathbb C:y>0\}\), and let \(\mathcal B_2(\Pi)\) be the complex Hilbert space of square-integrable biharmonic functions on \(\Pi\): \(\Delta^2f=0\), with the unweighted planar area norm. For \(0<a<b<\infty\), let \(T_{a,b}\) be the orthogonal compression of multiplication by \(\mathbf 1_{\{a<y<b\}}\) to \(\mathcal B_2(\Pi)\). Under Fourier transform in \(x\), every nonzero horizontal frequency \(\xi\) has a two-dimensional biharmonic fiber. Write \(\rho=|\xi|\), \(t=2\rho\), \(z=t(b-a)\), and \(c=(a+b)/(b-a)>1\).

In an explicit orthonormal Fourier--Laguerre basis the concentration matrix is
\[
M_{a,b}(\rho)=e^{-at}Q(at)-e^{-bt}Q(bt),\qquad
Q(s)=\begin{pmatrix}1&-s\\-s&1+s^2\end{pmatrix}.
\]
In particular the product of its two positive eigenvalues is
\[
D_{a,b}(\rho)=\det M_{a,b}(\rho)
=e^{-cz}g(z),\qquad g(z)=2(\cosh z-1)-z^2>0.
\]
The trace is \(e^{-at}(2+a^2t^2)-e^{-bt}(2+b^2t^2)\), so the two eigenvalues are determined exactly by trace and determinant.

The D-optimal joint concentration \(D_*(a,b)=\sup_{\rho>0}D_{a,b}(\rho)\) is attained at **exactly one** positive frequency \(\rho_*\). The dimensionless maximizer \(z_*=2\rho_*(b-a)\) is the unique solution of
\[
\frac{2(\sinh z_*-z_*)}{2(\cosh z_*-1)-z_*^2}
=\frac{a+b}{b-a}.
\]
As a slab becomes thin relative to its height (\((b-a)/(a+b)\to0\)),
\[
D_*(a,b)\sim\frac{64}{3e^4}
\left(\frac{b-a}{a+b}\right)^4,
\qquad \rho_*\sim\frac{2}{a+b}.
\]
For a slab approaching the boundary, set \(\varepsilon=2a/(b-a)\to0^+\) and \(L=\log(1/\varepsilon)\). Then
\[
z_*=L+2\log L+o(1),\qquad
1-D_*(a,b)\sim\varepsilon L.
\]
At the endpoint \(a=0<b\), \(\sup_{\rho>0}D_{0,b}(\rho)=1\), but the supremum is not attained by any finite frequency.

## Assumptions and scope

All functions are complex-valued; \(\Delta=\partial_x^2+\partial_y^2\). Frequencies \(\xi=0\) are ignored as a null set in the Fourier direct integral. The symbol \(\mathbf 1_{\{a<y<b\}}\) is a bounded orthogonal-coordinate slab indicator. No finite-rank or trace-class claim is made for the global operator \(T_{a,b}\), which acts on an infinite-horizontal-measure domain. The determinant throughout refers to a **two-dimensional Fourier fiber**, not a Fredholm determinant of the full operator. The thin-slab and boundary limits are separate asymptotic regimes; their error terms are with respect to the indicated dimensionless ratio.

## Proof

**1. Fourier fibers and orthonormalization.** Taking the unitary Fourier transform in \(x\) converts \(\Delta^2f=0\) into \((\partial_y^2-\rho^2)^2\widehat f(\xi,y)=0\) for almost every \(\xi\ne0\). Square-integrability in the upper half-plane excludes both growing exponential solutions. Thus the complete fiber is \(\{(A+By)e^{-\rho y}:A,B\in\mathbb C\}\). For \(t=2\rho\), put \(v=ty\). The two fiber functions \(\psi_0(y)=\sqrt t\,e^{-\rho y}\) and \(\psi_1(y)=\sqrt t\,(1-ty)e^{-\rho y}\) are orthonormal because
\[
\int_0^\infty e^{-v}\,dv=1,\quad
\int_0^\infty (1-v)e^{-v}\,dv=0,\quad
\int_0^\infty(1-v)^2e^{-v}\,dv=1.
\]
Plancherel and the direct-integral decomposition justify the reduction to the \(2\times2\) Gram matrix of these functions restricted to \(a<y<b\).

**2. Exact spectral data.** Direct integration gives
\[
\int_s^\infty e^{-v}
\begin{pmatrix}1&1-v\\1-v&(1-v)^2\end{pmatrix}dv
=e^{-s}Q(s).
\]
Subtracting two tails gives the displayed \(M_{a,b}(\rho)\). Its determinant expands using \(\det Q(s)=1\) and the cross identity
\[
\operatorname{tr}(\operatorname{adj}Q(x)Q(y))=2+(x-y)^2.
\]
This yields \(\det M=e^{-at-bt}[2(\cosh((b-a)t)-1)-(b-a)^2t^2]\). Strictly positive definiteness follows because \(1\) and \(1-v\) remain linearly independent on every nontrivial interval; strict inequality \(M<I\) follows by the same argument on its nonempty complement. Consequently both eigenvalues lie strictly between zero and one.

**3. Unique maximum.** Set \(g(z)=2(\cosh z-1)-z^2=4\sinh^2(z/2)-z^2>0\). Then \(g(z)\sim z^4/12\) at zero and \(g(z)\sim e^z\) at infinity. Its logarithmic derivative
\[
H(z)=\frac{g'(z)}{g(z)}
=\frac{2(\sinh z-z)}{g(z)}
\]
is strictly decreasing. Indeed, a direct identity gives
\[
g'(z)^2-g(z)g''(z)
=2\bigl[z^2(\cosh z+1)-4z\sinh z+4(\cosh z-1)\bigr]
=4\sum_{k=3}^\infty\frac{(2k-1)(k-2)}{(2k)!}z^{2k}>0.
\]
Thus \(H'(z)<0\). Moreover \(H(z)\sim4/z\) at zero, \(H(z)\to1\) at infinity, and \(H(z)>1\) for every finite \(z>0\): the last assertion follows from \(g'(z)-g(z)=z^2-2z+2(1-e^{-z})>0\), whose derivative is positive and which vanishes at zero. Since \(c>1\), the equation \(H(z)=c\) has one solution. The derivative of \(e^{-cz}g(z)\) has sign \(H(z)-c\), while the determinant vanishes at both endpoints. This proves uniqueness and global optimality.

**4. Thin slab.** For \(c\to\infty\), \(H(z)=4/z+O(z)\) forces \(z_*=4/c+O(c^{-3})\). With \(g(z)=z^4/12+O(z^6)\),
\[
D_*=e^{-cz_*}g(z_*)\sim e^{-4}\frac{4^4}{12c^4}
=\frac{64}{3e^4c^4}.
\]
Also \(\rho_*=z_*/[2(b-a)]\sim2/(a+b)\).

**5. Boundary approach.** Put \(c=1+\varepsilon\). The optimum tends to infinity and its defining equation can be rewritten as
\[
\varepsilon=
\frac{z_*^2-2z_*+2-2e^{-z_*}}
{2(\cosh z_*-1)-z_*^2}
=z_*^2e^{-z_*}(1+o(1)).
\]
Taking logarithms first gives \(z_*/L\to1\), then substituting back yields \(z_*=L+2\log L+o(1)\). Next,
\[
D_*=e^{-\varepsilon z_*}
\bigl[1-(2+z_*^2)e^{-z_*}+e^{-2z_*}\bigr].
\]
The first loss is \(\varepsilon z_*\), whereas the bracket's loss is \(O(\varepsilon)\). Hence \(1-D_*\sim\varepsilon z_*\sim\varepsilon L\). If \(a=0\), the matrix is the increasing partial Gram integral \(\int_0^{bt}e^{-v}(1,1-v)^\top(1,1-v)\,dv\); its eigenvalues strictly increase toward one, so the determinant increases strictly toward one but never reaches it.

## Verification

The self-contained Python 3 file `checker.py` compares 120 independently integrated matrix entries with the closed formulas, checks determinant identities, numerical strict maxima and both asymptotic regimes. The complete extracted checker produced 387 supplementary finite assertions without failure. These finite checks are diagnostic: positivity, uniqueness and both limiting statements are proved above, not inferred from computation.

## Relationship to prior work

Pessoa and Santos provide the unweighted polyharmonic Bergman decomposition and Fourier/Laguerre framework on the upper half-plane. Bradík's 2023 work studies harmonic (order-one) Bergman kernels and the vertical Berezin transform, rather than the two-mode biharmonic slab compression. Neither work supplies the exact slab fiber determinant, its unique D-optimal frequency, or the thin-slab quartic and boundary logarithmic asymptotics in the accessible material. The earlier Fourier/Laguerre model is used and fully credited; it is not claimed as new. An inaccessible portion of the Pessoa--Santos paper and potentially unindexed specialized localization literature remain historical-priority risks.

## Limitations

The theorem is unweighted and two-dimensional, with fourth-order harmonic equation \(\Delta^2f=0\), positive finite slab thickness, and the determinant criterion. It does not optimize the smallest individual fiber eigenvalue, does not give global spectral multiplicity/trace formulas, and does not assert a corresponding result for higher polyharmonic order or weighted half-spaces. Independent mathematical audit and independent validation have not been performed.

## References

1. L. V. Pessoa and A. Moura Santos, *Polyharmonic Bergman spaces and Bargmann type transforms*, Journal of Mathematical Analysis and Applications 449 (2017), 619--641. DOI: 10.1016/j.jmaa.2016.12.034.
2. J. Bradík, *Harmonic Berezin transform on half-space with vertical weights*, arXiv:2310.17562, first posted 2023-10-26.
3. MSC2020 classification, 31A30: biharmonic and polyharmonic equations and functions in two dimensions.
