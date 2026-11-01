# Three even distance moments determine a triangle, with sharp cubic inverse stability

## Finding
Let \(T\) be any nondegenerate Euclidean triangle. Independently choose \(X,Y\) uniformly with respect to area on \(T\), and write \(D=\|X-Y\|\). Then the three numbers \(m_k=\mathbb E[D^{2k}]\), \(k=1,2,3\), determine \(T\) up to Euclidean congruence, including its size. Explicitly, if \(x,y,z\) are its three squared side lengths and \(e_1=x+y+z\), \(e_2=xy+xz+yz\), \(e_3=xyz\), then

\[
 m_1=\frac{e_1}{18},\qquad
 m_2=\frac{e_1^2-2e_2}{60},\qquad
 m_3=\frac{23e_1^3-62e_1e_2+20e_3}{4200}.
\]

The squared side lengths are therefore precisely the roots, including multiplicity, of

\[
 t^3-E_1t^2+E_2t-E_3=0,\qquad
 E_1=18m_1,\quad E_2=\frac{E_1^2-60m_2}{2},\quad
 E_3=210m_3-\frac{23}{20}E_1^3+\frac{31}{10}E_1E_2.
\]

Three is minimal among initial even-distance moments: the first two alone fail to distinguish some pairs of noncongruent, strictly nondegenerate triangles. Moreover, on every family with squared side lengths bounded above by a fixed \(B>0\), the reconstruction of the unordered squared-side multiset is uniformly Hölder continuous of exponent \(1/3\) in \((m_1,m_2,m_3)\). This exponent cannot be increased even in an arbitrarily small neighborhood of the equilateral triangle.

## Assumptions and scope
A triangle is nondegenerate when its area is positive and each strict triangle inequality holds. Uniformity means normalized two-dimensional Lebesgue measure on the triangle, with independent sampling and Euclidean distance. Squared side lengths are unordered, since the result identifies a triangle up to rigid motion and reflection, not an orientation or labeling. For the stability statement, compare two triangles whose squared side lengths lie in \([0,B]\), using \(\delta=\max_{1\le k\le3}|m_k-m_k'|\) and matching their three ordered squared sides. Constants depend on \(B\), not on the triangle shapes. The theorem makes no assertion about higher-dimensional simplices or nonuniform sampling.

## Proof
Choose vertices \(v_0=0,v_1,v_2\). Set \(x=\|v_1\|^2\), \(y=\|v_2\|^2\), \(z=\|v_1-v_2\|^2\). Uniform barycentric coordinates \((U_0,U_1,U_2)\) and \((V_0,V_1,V_2)\) of the two sampled points are independent \(\operatorname{Dirichlet}(1,1,1)\) vectors. Set \(A=U_1-V_1\) and \(B'=U_2-V_2\). By the Euclidean polarization identity,

\[
 D^2=xA^2+y(B')^2+(x+y-z)AB'.
\]

The exact Dirichlet moment formula for nonnegative integers \(p,q\) is

\[
 \mathbb E[U_1^pU_2^q]=\frac{2p!q!}{(p+q+2)!}.
\]

By independence and binomial expansion, for nonnegative integers \(p,q\),

\[
 H_{p,q}:=\mathbb E[A^p(B')^q]
 =\sum_{a=0}^{p}\sum_{b=0}^{q}(-1)^{p+q-a-b}
 {p\choose a}{q\choose b}
 \frac{2a!b!}{(a+b+2)!}
 \frac{2(p-a)!(q-b)!}{(p+q-a-b+2)!}.
\]

For \(k=1,2,3\), the multinomial theorem gives the finite identity

\[
 m_k=\sum_{i+j+h=k}\frac{k!}{i!j!h!}
 x^iy^j(x+y-z)^h H_{2i+h,2j+h}.
\]

Substituting the displayed factorial formula and collecting polynomial coefficients yields, exactly,

\[
 m_1=\frac{x+y+z}{18},\qquad
 m_2=\frac{x^2+y^2+z^2}{60},
\]
\[
 m_3=\frac{23(x^3+y^3+z^3)+7\sum_{\mathrm{sym}}x^2y-28xyz}{4200}.
\]

Here \(\sum_{\mathrm{sym}}x^2y\) is the sum of the six distinct permutations of the monomial. Newton identities yield the symmetric-polynomial forms in the Finding. All sums are finite and exact; the accompanying standard-library checker computes the expanded coefficient dictionaries over rational numbers and verifies these three polynomial equalities coefficient by coefficient. This establishes the identities for all Euclidean triangles, not merely a finite test set. Solving successively for \(e_1,e_2,e_3\) yields \(E_1,E_2,E_3\) above. Their monic cubic has the unordered squared side lengths as its full root multiset. Euclidean side-side-side congruence proves uniqueness.

To prove that two moments do not suffice, choose any \(0<r<1/10\) and consider two squared-side triples

\[
 (1+r,1-r/2,1-r/2),\qquad
 (1+r/2,1+r/2,1-r).
\]

Both triples give strict nondegenerate triangles. Each has \(e_1=3\) and \(e_2=3-3r^2/4\); the distinct \(e_3\)'s show that they are not congruent, although their \(m_1,m_2\) coincide. Indeed the two products differ in absolute value by \(r^3/2\), so their third distance moments differ by \(r^3/420\).

For uniform stability, fix \(B\) and consider two monic cubics reconstructed from bounded squared-side roots. Their elementary symmetric coefficients differ by at most \(C_B\delta\) because the displayed inverse map is polynomial and its arguments lie in a bounded interval. Therefore the two cubic polynomials differ by at most \(C_B'\delta\) throughout \(|t|\le B+1\) in the complex plane. If \(\delta\) is sufficiently small, surround the three roots of the first cubic by closed complex disks of radius \(\eta=(2C_B'\delta)^{1/3}\). On every boundary component of their union, the modulus of the first cubic is at least \(\eta^3\), strictly exceeding the polynomial perturbation. Rouché's theorem gives equal numbers of roots in each connected disk cluster. Every cluster has diameter at most \(6\eta\), because it contains at most three radius-\(\eta\) disks, joined by overlaps. Roots can thus be matched, with multiplicities, at distance at most \(6\eta\). For larger \(\delta\), enlarge the constant using the a priori root bound \(B\). Since the roots are real and nonnegative, this matching bounds the maximum distance of the ordered squared side lengths. Hence the uniform exponent is \(1/3\).

For sharpness, use the two explicit noncongruent triangles above as \(r\downarrow0\). Their first two moments agree, their third moments differ by exactly \(r^3/420\), while the maximum difference between their ordered squared-side triples equals \(r\). Both triangles tend to the same equilateral triangle. Thus no uniform inverse estimate with Hölder exponent strictly greater than \(1/3\) is possible near that triangle. This completes every part of the theorem.

## Verification
Run `python3 verify_triangle_moments.py` from the directory containing this document. The checker uses only the Python standard library, constructs each polynomial moment directly from the Dirichlet factorial sum, compares exact rational coefficient dictionaries against the three closed formulas, checks the inverse cubic coefficients on an unequal-sided strict triangle, and checks the nonidentifiability and cubic sharpness construction using rational arithmetic. It reports `ALL_CHECKS_PASSED`. The mathematical proof also establishes the global root-continuity estimate, which is not certified by finite numerical sampling.

## Relationship to prior work
The general mean-distance inequalities of Bonnet, Gusakova, Thäle and Zaporozhets (arXiv:2010.03351, publicly posted October 7, 2020) concern bounds for the first distance moment over general convex bodies, not finite-moment reconstruction of triangle side lengths. Bäsel (arXiv:2101.03815, January 11, 2021) gives distance-moment formulas for regular polygons, including their second and fourth distance moments, but does not address arbitrary-triangle reconstruction. Tong, Ahmadi and Pan (arXiv:1312.2498) derive forward distance distributions for arbitrary triangles; forward distribution formulas alone do not state that three specified moments suffice, nor their minimality or optimal inverse regularity. Pure, Durrani, Tong and Pan (DOI:10.1002/mma.7951) extend forward distance-density computations to arbitrary polygons. The 1982 Gates article (DOI:10.2307/3213843) reports reconstruction of triangles from odd random-*chord* moments, which are different observables from the three even *interior pair-distance* moments here. Its full text could not be inspected, and a previously known finite-moment equivalent remains a priority risk. Earlier width-based triangle reconstruction pertains to a different direction-random observable. The new assertion is the explicit minimal three-moment inverse law and its sharp \(1/3\) stability, not the general existence of forward distance-density calculations.

## Limitations
The theorem concerns exact population moments, not statistical sample-size requirements or noise-optimal estimators. The inverse Hölder bound is for squared side lengths, with an upper size bound; converting it to a uniform estimate on actual side lengths additionally requires a positive lower side-length bound. The optimum \(1/3\) exponent is a worst-case bound near equilateral triangles, not a claim that every triangle is equally ill-conditioned. The literature comparison cannot exclude an inaccessible older equivalent theorem. No independent mathematical audit has been performed.

## References
- G. Bonnet, A. Gusakova, C. Thäle, D. Zaporozhets, *Sharp inequalities for the mean distance of random points in convex bodies*, arXiv:2010.03351 (first public posting 2020-10-07), https://arxiv.org/abs/2010.03351.
- U. Bäsel, *The moments of the distance between two random points in a regular polygon*, arXiv:2101.03815 (first public posting 2021-01-11), https://arxiv.org/abs/2101.03815.
- F. Tong, M. Ahmadi, J. Pan, *Random Distances Associated with Arbitrary Triangles: A Systematic Approach between Two Random Points*, arXiv:1312.2498 (2013), https://arxiv.org/abs/1312.2498.
- R. Pure, S. Durrani, F. Tong, J. Pan, *Distance distribution between two random points in arbitrary polygons*, Mathematical Methods in the Applied Sciences 45 (2022), 2760–2775, https://doi.org/10.1002/mma.7951.
- J. Gates, *Recognition of triangles and quadrilaterals by chord length distribution*, Journal of Applied Probability 19 (1982), 873–879, https://doi.org/10.2307/3213843.
