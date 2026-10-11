# Cofinite zero geometry on the balanced hypergeometric critical plane

## Finding
For \(a,b,c>0\), assume \(b+c=3a+\tfrac12\), and neither \(b-a\) nor \(c-a\) is a nonpositive integer. Set
\[
\Phi(z)={}_1F_2\!\left(\begin{matrix}a\ b,c\end{matrix};-z^2/4\right),\qquad R=\frac{\sqrt\pi\Gamma(a)}{\Gamma(b-a)\Gamma(c-a)}.
\]
When \(|R|\ne1\), every sufficiently large zero of \(\Phi\) in the right half-plane is simple, and the zeros form exactly two strings indexed by sufficiently large positive integers:
\[
z_{n,\pm}=w_{n,\pm}+\frac{d}{2w_{n,\pm}}+O(n^{-2}),\qquad w_{n,\pm}=2\pi n+\pi a\pm\theta,
\]
where \(\cos\theta=-R\) and
\[
d=(3a+b+c+1)(a-b-c-1)+4(bc+b+c)+\tfrac14.
\]
Any branch of \(\theta\) is permissible after reindexing the strings. The remaining large zeros in the left half-plane are their negatives because \(\Phi\) is even.

If \(|R|<1\), every sufficiently large zero is real and simple, and their number on \((0,x]\), counted with multiplicity, is \(x/\pi+O(1)\). If \(|R|>1\), every sufficiently large zero is nonreal and simple, only finitely many real zeros exist, and the modulus of the imaginary part of the asymptotic zeros tends to \(\operatorname{arcosh}|R|\). This is a transition in cofinite zero geometry, **not** a classification of every bounded zero or of the boundary \(|R|=1\).

## Assumptions and scope
The parameters are fixed positive reals subject to the displayed equality and exclusions. The hypergeometric series is entire and even. The gamma ratio is finite and nonzero under these hypotheses. The zero asymptotics hold as \(n\to+\infty\) for both signs with constants depending on the three parameters. For \(|R|>1\), choose any complex \(\theta\) with \(\cos\theta=-R\); its imaginary part has absolute value \(\operatorname{arcosh}|R|\).

## Proof
**Asymptotic reduction.** Formula (2.1) of Cho–Chung–Park [1], a sector-uniform large-argument expansion of \({}_1F_2\), has the algebraic exponent \(2a\) and oscillatory exponent \(\sigma=b+c-a-\tfrac12\). On the balanced plane they agree, \(\sigma=2a\). Multiply the expansion by \(\sqrt\pi\Gamma(a)(z/2)^{2a}/[\Gamma(b)\Gamma(c)]\), using the principal power in the right half-plane. Uniformly as \(|z|\to\infty\) there, it becomes
\[
G(z):=\frac{\sqrt\pi\Gamma(a)}{\Gamma(b)\Gamma(c)}(z/2)^{2a}\Phi(z)
=R+\cos(z-\pi a)+\frac{d}{2z}\sin(z-\pi a)+O\!\left(\frac{1+e^{|\operatorname{Im}z|}}{|z|^2}\right).
\]
In particular, with \(g(z)=R+\cos(z-\pi a)\), the difference \(G-g\) is \(O(e^{|\operatorname{Im}z|}/|z|)\), uniformly throughout the closed right half-plane outside a sufficiently large disk. The multiplier of \(\Phi\) is nonzero there.

**Global localization, not just detection.** For \(|R|\ne1\), the simple zeros of \(g\) are precisely \(2\pi k+\pi a\pm\theta\) for integers \(k\), and the two progressions are distinct. Choose a sufficiently small fixed radius \(\rho>0\) so the disks around distinct zeros are disjoint, and, in the nonreal case, avoid the real axis. Periodicity of \(g\), its absence of zeros outside these disks in a bounded-height fundamental strip, and its exponential growth as \(|\operatorname{Im}z|\to\infty\) imply a constant \(c_\rho>0\) such that
\[
|g(z)|\ge c_\rho e^{|\operatorname{Im}z|}
\]
outside these disks. Thus for large \(|z|\) the perturbation has modulus less than \(|g|\) there: no zeros of \(G\) occur outside the disks. On every sufficiently rightward disk boundary the same strict comparison and Rouché's theorem yield exactly one zero, counted with multiplicity. Hence it is simple, and the stated two strings exhaust every sufficiently large right-half-plane zero. Evenness covers the other half-plane. The bounded portion of the imaginary axis contains only finitely many zeros; the large portion lies in the zero-free complement of the disks.

**First correction.** If \(w=2\pi n+\pi a\pm\theta\), then \(\sin(w-\pi a)\ne0\). The unique zero \(z=w+\varepsilon\) has \(\varepsilon=O(1/n)\) from the simple-root lower bound and asymptotic equation. Taylor expansion gives
\[
0=-\sin(w-\pi a)\varepsilon+\frac{d}{2w}\sin(w-\pi a)+O(n^{-2}),
\]
so \(\varepsilon=d/(2w)+O(n^{-2})\).

**Reality dichotomy and counting.** If \(|R|<1\), select the real \(\theta\in(0,\pi)\). Each far-right disk is invariant under complex conjugation; since \(\Phi\) has real coefficients and the disk has one zero, the zero is real. Two simple zeros per period of length \(2\pi\) give the counting law. If \(|R|>1\), both root progressions have nonzero imaginary heights \(\pm\operatorname{arcosh}|R|\), and their disjoint far-right disks avoid the real line. Therefore all sufficiently large zeros are nonreal, with those limiting heights. The finitely many zeros in a bounded disk are not classified.

## Verification
On \((a,b,c)=(\tfrac12,\tfrac14,\tfrac74)\), the balanced equality holds and the gamma reflection identities yield \(R=-1/\sqrt2\) exactly, exhibiting the real-tail regime. To see the nonreal-tail regime is nonempty, fix \(a=\tfrac14\), let \(b\downarrow0\), and set \(c=\tfrac54-b\). Then \(R\to-\Gamma(\tfrac14)^2/[4\sqrt{2\pi}]\), whose absolute value exceeds one: the elementary bound \(\Gamma(\tfrac14)>\int_0^1t^{-3/4}(1-t)dt=16/5\) together with \(\pi<22/7\) proves it. By continuity, positive sufficiently small \(b\) give \(|R|>1\). Direct exact substitution at \((a,b,c)=(\tfrac14,\tfrac18,\tfrac98)\) gives \(d=-3/16\); these checks are illustrations, not substitutes for the infinite Rouché argument.

## Relationship to prior work
Cho–Chung–Park [1] prove their sector-uniform asymptotic (2.1), and their Proposition 5.1 compares strict regions on either side of the balance plane: it does not give a cofinite zero-string classification along equality. Their Theorem 7.1 gives global real-zero classifications for certain \(a=1\) parameters, which are stronger than the corresponding special cases here, but do not cover the all-positive-parameter two-regime statement. Zullo [2] treats Lommel-function zeros, including selected \(a=1\) hypergeometric specializations, without providing the stated general cofinite transition. The new assertion concerns exhaustion, simplicity, locations and off-axis heights of all sufficiently large zeros on the critical plane; the pre-existing leading asymptotic is credited rather than claimed as new.

## Limitations
The threshold \(|R|=1\) can have merging leading roots and is excluded. No claim is made about finitely many bounded zeros, Laguerre–Pólya membership in the general family, or results beyond positive parameters. Undiscovered equivalent zero-location arguments remain an originality risk.

## References
[1] Y.-K. Cho, S.-Y. Chung and Y. W. Park, *A sampling theorem of hypergeometric \({}_1F_2\) functions and the Laguerre-Pólya class*, Numerical Algorithms (first public 2025-07-05), DOI 10.1007/s11075-025-02158-x, especially equation (2.1), Proposition 5.1, Theorem 7.1.

[2] F. Zullo, *Integral representations and zeros of the Lommel function and the hypergeometric \({}_1F_2\) function*, Results in Mathematics 79 (2024), article 236; also arXiv:2312.00426.
