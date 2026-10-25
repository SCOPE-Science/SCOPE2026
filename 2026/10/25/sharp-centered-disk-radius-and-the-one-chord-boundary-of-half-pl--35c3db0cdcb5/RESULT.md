# Sharp centered-disk radius and the one-chord boundary of half-plane translation numerical ranges

## Finding

Let \(\alpha>-1\), let \(\mathbb C_+=\{w:\operatorname{Re}w>0\}\), and equip the weighted Bergman Hilbert space \(\mathcal A^2_\alpha(\mathbb C_+)\) with the norm
\[
 \|f\|_\alpha^2=\int_{\mathbb C_+}|f(x+iy)|^2x^\alpha\,dx\,dy.
\]
For \(b=u+iv\) with \(u>0\) and \(v\ne0\), consider the bounded translation-composition operator \(T_bf(w)=f(w+b)\). Set
\[
 k=\frac{u}{|v|},\quad \phi=\arctan k,\quad c=(1+k^2)^{-1/2}.
\]
There is exactly one \(\Theta_k\in(3\pi/2,2\pi)\) satisfying
\[
 \cos\Theta_k=c\exp[-k(\Theta_k-\phi)].\tag{1}
\]
Write \(x_k=\Theta_k-\phi\) and \(S_k(x)=\exp(-kx+ix)\). The closure of the numerical range of \(T_b\), up to conjugation when \(v>0\), is the compact convex region bounded by **exactly one spiral arc and exactly one straight chord**:
\[
 \partial\overline{W(T_b)}
 = S_k([0,x_k])\ \cup\ [S_k(x_k),1]\qquad (v<0),\tag{2}
\]
with the complex conjugate of this set when \(v>0\). The numerical range is precisely the **interior** of this compact region, so no boundary point is attained by a unit vector. Its sharp origin-centered inradius (the supremum of radii of centered open disks contained in \(W(T_b)\)) is
\[
 \boxed{\ \rho(k)=\cos\Theta_k
 =\frac{\exp(-kx_k)}{\sqrt{1+k^2}}\ }.\tag{3}
\]
This dimensionless radius is independent of \(\alpha\) and of the magnitude of \(b\); it depends only on \(u/|v|\). Its two extreme-pitch laws are
\[
 \rho(k)=1-2\pi k+O(k^{3/2})\quad(k\downarrow0),\qquad
 \rho(k)\sim\frac{e^{-1}}{k}e^{-\pi k}\quad(k\to\infty).\tag{4}
\]

## Assumptions and scope

The Hilbert-space weight parameter is any real \(\alpha>-1\); the translation has strictly positive real part and nonzero imaginary part. Numerical ranges use \(W(T)=\{\langle Tf,f\rangle:\|f\|=1\}\). The geometric boundary and radius concern the closure of this convex numerical range; equality on its boundary is not attained. The statements do not concern arbitrary affine symbols, weighted translations, or non-Hilbert spaces. Positive real translations have a different degenerate interval numerical range, while purely imaginary translations lead to an open unit disk; these limiting cases are not part of the main theorem.

## Proof

**1. Spectral reduction.** The Paley--Wiener--Laplace isometry for half-plane weighted Bergman spaces identifies \(\mathcal A^2_\alpha(\mathbb C_+)\) with \(L^2((0,\infty),d\mu_\alpha)\), where \(d\mu_\alpha\) has a strictly positive density on \((0,\infty)\). Under this identification, \(T_b\) becomes multiplication by \(e^{-bt}\). Consequently its numerical range consists exactly of integrals of \(e^{-bt}\) against absolutely continuous probability measures on \((0,\infty)\). The change of variable \(x=|v|t\) and complex conjugation where necessary reduce the closed numerical range to
\[
 K_k=\operatorname{conv}\big(\{S_k(x):x\ge0\}\cup\{0\}\big).
\]
(The extra limit point \(0\) makes the displayed set compact; it is in the convex hull already once convex closure is taken.) This also proves independence of \(\alpha\).

**2. All supporting directions, not just sampled directions.** For \(0\le\theta\le2\pi\), its support function is
\[
 h_k(\theta)=\max_{x\ge0}e^{-kx}\cos(x-\theta).
\]
An interior positive local maximum can occur only when \(x=\theta-\phi+2\pi j\) for an integer \(j\), in which case its value is \(c e^{-kx}\). Later admissible maxima are smaller by the factor \(e^{-2\pi k}\). Comparison with the endpoint \(x=0\) therefore yields the **exact global formula**
\[
 h_k(\theta)=
 \begin{cases}
 \cos\theta,&0\le\theta<\phi,\\
 \max\{\cos\theta,\ c e^{-k(\theta-\phi)}\},&\phi\le\theta\le2\pi.
 \end{cases}\tag{5}
\]
The first branch is valid because \(\cos\theta\ge c\) and every admissible interior maximum is at most \(c\) for \(0\le\theta<\phi\). At \(\theta=\phi\), the two displayed candidates coincide at the same parameter \(x=0\).

For \(\phi<\theta<\pi/2\), the derivative of \(\log(c e^{-k(\theta-\phi)})-\log\cos\theta\) is \(\tan\theta-k>0\), starting from equality at \(\theta=\phi\). For \(\pi/2\le\theta\le3\pi/2\), the cosine is nonpositive. Thus the exponential strictly dominates over the entire interval \(\phi<\theta\le3\pi/2\). On \((3\pi/2,2\pi)\), \(\cos\theta\) strictly increases from zero to one while the exponential strictly decreases from a positive value to less than one. They meet at exactly one \(\Theta_k\), yielding (1). Hence the exposed support points, in increasing angular order, consist of the endpoint \(1\), the smooth arc \(S_k(x)\) for \(0<x<x_k\), and the endpoint again; precisely at \(\Theta_k\) there is a supporting segment joining \(1\) to \(S_k(x_k)\). This proves (2), and excludes any later turn of the spiral from the boundary.

**3. The exact inradius and openness.** For \(\phi\le\theta\le\Theta_k\) the support function is \(c e^{-k(\theta-\phi)}\), strictly decreasing; on \([\Theta_k,2\pi]\) it is \(\cos\theta\), strictly increasing. On \([0,\phi]\) it decreases from one to \(c>h_k(\Theta_k)\). Therefore the global minimum of \(h_k\) equals \(h_k(\Theta_k)=\cos\Theta_k>0\), which is the radius of the largest origin-centered disk in \(K_k\). For any supporting direction, the maximizing multiplier parameters form a finite set (one point, or two points at \(\Theta_k\)). Because the spectral measure is nonatomic, an expectation against a probability density cannot attain such a boundary support value. Conversely, every interior point of \(K_k\) is a convex combination of averages of \(S_k\) over finitely many short intervals of positive length: approximate vertices of a polygon enclosing the point by these interval averages, then use positive probability mixtures. Thus \(W(T_b)=\operatorname{int}K_k\); all disks of radius less than (3) are contained in \(W(T_b)\), while no disk of greater radius is contained.

**4. Extreme-pitch limits.** Put \(\varepsilon=2\pi-\Theta_k\). As \(k\downarrow0\), (1) implies \(\varepsilon\to0\), and logarithms of (1) give
\[
 \log\cos\varepsilon=-\tfrac12\log(1+k^2)-k(2\pi-\varepsilon-\arctan k).
\]
It follows that \(\varepsilon^2=4\pi k+O(k^{3/2})\), so \(\rho(k)=\cos\varepsilon=1-2\pi k+O(k^{3/2})\). For \(k\to\infty\), (1) forces \(\Theta_k=3\pi/2+\varepsilon_k\) with \(\varepsilon_k=O(e^{-\pi k}/k)\); using \(\phi=\pi/2-1/k+O(k^{-3})\) and \(c=k^{-1}(1+O(k^{-2}))\) in (1) yields \(\rho(k)\sim e^{-1}k^{-1}e^{-\pi k}\). This proves (4).

## Verification

The standalone `verify_spiral.py` evaluates the unique supporting-direction crossing by bisection, independently maximizes the original angular support over a dense spectral grid, and checks numerical consistency of (1)--(5) for six positive pitch ratios. The analytical proof is global and does not depend on any finite grid, plotting convention, or numerical tolerance. Execute using Python 3 with `python verify_spiral.py` from the extracted package directory.

## Relationship to prior work

The **convex-hull-of-a-spiral description is prior work, not the new claim**. Chacón--Chacón (2005), Theorem 5.13, states the spiral convex-hull numerical-range form on half-plane Hardy space, based on the normal multiplier model; its Theorem 5.5 treats related Dirichlet compression. Bourdon--Shapiro (2000/2002) identifies winding spectral curves and origin inclusion for associated disk symbols. Blois (2026) supplies the weighted half-plane Bergman setting and the precise Laplace model while studying cyclicity instead of quantitative numerical-range geometry. The added results here are the **unique finite cut-off and tangent chord**, the **explicit sharp centered-disk radius**, the **absence of attained boundary values for the weighted half-plane model**, and the **two precise pitch limits**. They require the global support optimization beyond the literature's qualitative convex-hull statement.

## Limitations

The theorem gives a one-parameter transcendental characterization, not an elementary closed expression for the tangent angle. It does not classify composition operators induced by general affine symbols or the numerical range on disk Hardy/Bergman spaces after a nonunitary change of model. The older Hardy-space spiral convex-hull result strictly limits the new contribution: merely recognizing the hull would not be original.

## References

1. A. Blois, *Cyclic phenomena for composition operators on weighted Bergman spaces*, arXiv:2606.10999 (first public June 9, 2026), especially Section 2 and the Laplace representation. https://arxiv.org/abs/2606.10999
2. G. A. Chacón and G. R. Chacón, *Some properties of composition operators on the Dirichlet space*, Acta Math. Univ. Comenianae 74 (2005), 259–272, especially Theorems 5.5, 5.11, 5.13. https://www.kurims.kyoto-u.ac.jp/EMIS/journals/AMUC/_vol-74/_no_2/_chacon/chacon.pdf
3. P. S. Bourdon and J. H. Shapiro, *What is the numerical range of a composition operator?*, Integral Equations Operator Theory 44 (2002), 410–441; relevant discussion of parabolic spirals in Section 6. https://users.math.msu.edu/users/shapiro/pubvit/downloads/whatis/whatis.pdf
