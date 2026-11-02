# A sharp Eisenstein multiplicity band and spectral cusp for homogeneous Fourier shells on the three-torus

## Finding

Let \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\), with probability Haar measure. For each integer \(N\ge1\), define the analytic, total-degree \(N\) Fourier shell
\[
E_N=\operatorname{span}\bigl\{e^{i(k_1\theta_1+k_2\theta_2+k_3\theta_3)}:
 k_j\in\mathbb Z_{\ge0},\ k_1+k_2+k_3=N\bigr\}.
\]
The positive flat-torus Laplacian \(L_N=-\Delta_{\mathbb T^3}|_{E_N}\) has eigenvalue \(k_1^2+k_2^2+k_3^2\) on the indicated Fourier character.

**Sharp complete arithmetic band.** For every \(M\ge1\), set \(N=3M\), let \(a_M(m)\) be the multiplicity of \(3M^2+2m\), and define
\[
m_*(M)=\left\lceil\frac{3(M+1)^2}{4}\right\rceil.
\]
Let \(\chi_{-3}(d)\) be the real quadratic character modulo \(3\): it is \(1\) when \(d\equiv1\pmod3\), \(-1\) when \(d\equiv2\pmod3\), and \(0\) when \(3\mid d\). Then
\[
a_M(0)=1,\qquad
 a_M(m)=6\sum_{d\mid m}\chi_{-3}(d)
 \quad(1\le m<m_*(M)).
\]
At the very first excluded integer, this equality fails strictly:
\[
a_M\bigl(m_*(M)\bigr)<6\sum_{d\mid m_*(M)}\chi_{-3}(d).
\]
In particular, for each positive \(m<m_*(M)\), the eigenvalue is absent precisely when at least one prime congruent to \(2\) modulo \(3\) divides \(m\) to an odd power. Otherwise its multiplicity is
\[
6\prod_{\substack{p^e\parallel m\\p\equiv1\ (\mathrm{mod}\ 3)}}(e+1).
\]
The exceptional zero-frequency center has multiplicity one.

**A quantitative global spectral limit.** For every \(N\ge1\), form the probability measure
\[
\mu_N=\frac{1}{\binom{N+2}{2}}
\sum_{\substack{k\in\mathbb Z_{\ge0}^3\\k_1+k_2+k_3=N}}
\delta_{(k_1^2+k_2^2+k_3^2)/N^2}.
\]
There is an absolute constant \(C\) such that
\[
\sup_{s\in\mathbb R}\left|\mu_N(( -\infty,s])-F(s)\right|\le\frac{C}{N},
\]
where \(F\) is the distribution of \(s=t_1^2+t_2^2+t_3^2\) for a point chosen uniformly on the simplex \(t_j\ge0\), \(t_1+t_2+t_3=1\). Writing \(r=\sqrt{s-1/3}\) and \(h=1/\sqrt6\), its cumulative distribution is explicitly
\[
F(s)=\begin{cases}
0,&s\le1/3,\\[2pt]
\dfrac{2\pi}{\sqrt3}(s-1/3),&1/3<s\le1/2,\\[5pt]
\dfrac{2}{\sqrt3}\left[\pi r^2-3\bigl(r^2\arccos(h/r)-h\sqrt{r^2-h^2}\bigr)\right],&1/2<s<1,\\[5pt]
1,&s\ge1.
\end{cases}
\]
Its density \(f=F'\), extended by zero outside its support, is
\[
f(s)=\begin{cases}
\dfrac{2\pi}{\sqrt3},&1/3<s<1/2,\\[4pt]
\dfrac2{\sqrt3}\left[\pi-3\arccos\dfrac1{\sqrt{6(s-1/3)}}\right],&1/2<s<1,\\[4pt]
0,&s<1/3\text{ or }s>1.
\end{cases}
\]
The density is continuous through \(1/2\), but has a sharp, non-differentiable transition there:
\[
\lim_{\delta\downarrow0}
\frac{f(1/2)-f(1/2+\delta)}{\sqrt\delta}=6\sqrt2.
\]
The arithmetic cutoff approaches the same geometric transition: \((3M^2+2m_*(M))/(3M)^2\to1/2\).

## Assumptions and scope

The ambient torus is the standard flat three-torus with coordinates of period \(2\pi\); its Laplacian is \(\sum_{j=1}^3\partial_{\theta_j}^2\). The finite-dimensional Fourier shell uses nonnegative integer exponents, fixed **unweighted** total degree, and the orthonormal Fourier basis. Multiplicities include all ordered triples, not orbits modulo permutation. The exact divisor formula is asserted only when \(N\) is a multiple of three and strictly below the displayed threshold. The global distribution and its convergence rate hold for every positive integer \(N\), without divisibility restrictions.

## Proof

**1. Reduction to an Eisenstein norm.** For \(N=3M\), write the nonnegative frequency triple uniquely as
\[
(k_1,k_2,k_3)=(M+x,M+y,M-x-y)
\]
for integers \(x,y\) satisfying \(x\ge-M\), \(y\ge-M\), and \(x+y\le M\). Direct expansion gives
\[
k_1^2+k_2^2+k_3^2=3M^2+2Q(x,y),\qquad
Q(x,y)=x^2+xy+y^2.
\]
Without the three simplex inequalities, the number of representations of a positive integer \(m\) by \(Q\) is the classical Eisenstein norm count
\[
r_Q(m)=6\sum_{d\mid m}\chi_{-3}(d).
\]
For completeness, let \(\omega=e^{2\pi i/3}\). The quadratic form equals the field norm \(Q(x,y)=N(x-y\omega)\) in the Euclidean ring \(\mathbb Z[\omega]\), whose units have order six. A prime \(p\equiv1\pmod3\) splits into two nonassociate conjugate prime factors and contributes \(e+1\) possibilities at valuation \(e\). A prime \(p\equiv2\pmod3\) is inert, thus contributes zero possibilities at odd valuation and one at even valuation. The prime three ramifies, contributing one possibility at each valuation. Multiplying these choices and the six units gives both the divisor identity and the displayed prime-factor multiplicity. At \(m=0\), only \((x,y)=(0,0)\) occurs.

**2. Exact first clipping.** Put \(z=-x-y\), so \(x+y+z=0\) and
\[
2Q(x,y)=x^2+y^2+z^2.
\]
If any Eisenstein representation fails the simplex inequalities, at least one of \(x,y,z\) is \(\le-M-1\). By permutation symmetry take \(x\le-M-1\). Completing a square gives
\[
Q(x,y)=\left(y+\frac{x}{2}\right)^2+\frac{3x^2}{4},
\]
so for integral \(Q\),
\[
Q(x,y)\ge\left\lceil\frac{3(M+1)^2}{4}\right\rceil=m_*(M).
\]
Conversely choose \(x=-M-1\) and an integer \(y\) nearest to \((M+1)/2\). The completed-square identity gives \(Q(x,y)=m_*(M)\), but the first frequency is \(k_1=-1\), so this is an excluded unrestricted representation. Thus all representations at every smaller value survive, while at the threshold at least one is lost. This proves sharpness, not merely a sufficient radius estimate.

**3. Limit measure and quantitative error.** Identify the simplex with the equilateral triangle
\[
\mathcal S=\{t\in\mathbb R_{\ge0}^3:t_1+t_2+t_3=1\}
\]
of area \(\sqrt3/2\) in its affine plane, centered at \(b=(1/3,1/3,1/3)\). Since
\[
t_1^2+t_2^2+t_3^2=\frac13+|t-b|^2,
\]
the sublevel sets are precisely intersections of this triangle with centered disks. The inradius is \(h=1/\sqrt6\); the circumradius is \(\sqrt{2/3}\). For disks of radius \(r\le h\), the intersection area is \(\pi r^2\). For \(h<r<\sqrt{2/3}\), the three congruent circular caps outside the sides have disjoint interiors, each of area
\[
 r^2\arccos(h/r)-h\sqrt{r^2-h^2}.
\]
The normalized area therefore equals the asserted \(F(s)\). Differentiation gives \(f\). Using \(\arccos((1+6\delta)^{-1/2})=\sqrt{6\delta}+O(\delta^{3/2})\) proves the stated cusp limit.

To obtain the uniform convergence rate, parametrize the affine triangle by \((t_1,t_2)\), with \(t_3=1-t_1-t_2\). The \(N\)-th shell points are the mesh \((a/N,b/N)\), with \(a,b\ge0\), \(a+b\le N\), each carrying mass \(\binom{N+2}{2}^{-1}\). Every sublevel set is the intersection of a fixed triangle and an ellipse; it is convex, bounded, and has perimeter uniformly bounded over all \(s\). Associate a mesh square of side \(1/N\) with each grid point. Squares intersecting the boundary occupy area \(O(1/N)\), uniformly in \(s\), because a bounded-perimeter convex planar set has an \(\varepsilon\)-boundary neighborhood of area \(O(\varepsilon)\). The remaining squares reproduce its area exactly up to the lattice cell Jacobian, while \(\binom{N+2}{2}=N^2/2+O(N)\). Hence the discrete CDF and normalized area differ by at most \(C/N\), uniformly in \(s\). This also covers \(s\) outside the support, where both are \(0\) or \(1\).

## Verification

The accompanying standalone Python 3 checker uses only the standard library. From the included file directory, run `python checker.py`. It enumerates **every** eigenvalue multiplicity for \(N=3M\), \(1\le M\le35\), checks all values strictly below the exact clipping threshold against the divisor formula, and confirms strict loss at the first threshold. It additionally compares the spectral CDF with its analytic circular-cap formula at seven test values for each of \(N=300,600,1200\) and tests the one-sided cusp coefficient. The program reported `PASS 12252 exact or precision-tested assertions; all critical thresholds and density comparisons passed.` Finite enumeration is supplementary evidence, not a replacement for the unrestricted proof given above.

## Relationship to prior work

The Eisenstein norm representation formula is classical and **not claimed as a new identity**. Pinsky's equilateral-triangle eigenvalue work explicitly invokes the norm in the Eisenstein quadratic field. Rudnick and Wigman's full open manuscript analyzes the equilateral-triangle Robin spectrum and discusses quadratic-form Neumann spectral multiplicities. Their problems use eigenfunctions on a physical triangular domain, not the positive-frequency fixed-total-degree subspace of the flat three-torus, and do not directly give its first lost representation threshold or its whole-shell empirical eigenvalue density. Acosta Babb's 2023 open-access paper proves \(L^p\) convergence of Fourier series arising from Dirichlet eigenfunctions on planar triangles; its Sections 3–7 neither define this torus shell nor assert either displayed spectral statement. The arithmetic lemma and elementary circle–triangle geometry are separately familiar; the combined, quantitative spectral transition at the precise Hardy-shell cutoff is the contribution assessed here.

## Limitations

The exact arithmetic band is proven for total degrees divisible by three; no corresponding arithmetic formula is asserted for the other two residue classes. Above the first clipping threshold, unrestricted Eisenstein representation counts cannot simply be used. The CDF law concerns normalized eigenvalues under **uniform counting of Fourier characters**; it does not assert local gap statistics or convergence of individual eigenvalues. No extension to weighted monomials, other dimensions, or nonstandard Laplacians is claimed. Historical priority is provisional: the 1980 Pinsky full text was not accessible for complete inspection, though its public abstract concerns a different spectral problem. A general theorem on quadratic forms restricted to lattice simplices or an exact published formula for the squared Dirichlet-simplex norm could indirectly cover components of the result. Independent mathematical validation has not been carried out.

## References

1. R. L. Acosta Babb, *The \(L^p\) convergence of Fourier series on triangular domains*, Proceedings of the Edinburgh Mathematical Society **66** (2023), 453–474, published online 19 June 2023, DOI: `10.1017/S0013091523000226`.
2. Z. Rudnick and I. Wigman, *On the Robin spectrum for the equilateral triangle*, arXiv `2201.01117` (first public 4 January 2022); published in Journal of Physics A **55** (2022), 254004.
3. M. A. Pinsky, *The Eigenvalues of an Equilateral Triangle*, SIAM Journal on Mathematical Analysis **11** (1980), 819–827, DOI: `10.1137/0511073` (abstract and bibliographic details reviewed; full text not obtained).
