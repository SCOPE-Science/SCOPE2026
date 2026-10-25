# Three even distance moments reconstruct triangles with sharp cube-root stability

## Finding

Let \(T\) be any nondegenerate Euclidean triangle. If \(X,Y\) are independent points sampled uniformly by area from \(T\), write \(D=\|X-Y\|\) and \(M_{2j}=\mathbb E[D^{2j}]\). The three numbers \(M_2,M_4,M_6\) determine the unordered side lengths of \(T\), hence its congruence class. The first two determine its area already:

\[
\operatorname{area}(T)^2=\frac{81}{4}M_2^2-\frac{15}{2}M_4.
\tag{1}
\]

For the squared side lengths \(x=a^2,y=b^2,z=c^2\), put \(e_1=x+y+z\), \(e_2=xy+yz+zx\), and \(e_3=xyz\). They are recovered by

\[
\begin{aligned}
e_1&=18M_2,\\
e_2&=(e_1^2-60M_4)/2,\\
e_3&=(4200M_6-23e_1^3+62e_1e_2)/20.
\end{aligned}
\tag{2}
\]

The three squared side lengths are exactly the positive real roots, counted with multiplicity, of

\[
P(s)=s^3-e_1s^2+e_2s-e_3.
\tag{3}
\]

This is also a complete moment realizability test: a triple of real proposed moments comes from a nondegenerate triangle if and only if \(M_2>0\), the polynomial in (3) has three positive real roots counting multiplicity, and \(4e_2>e_1^2\). Among actual triangles, the sharp moment inequality is

\[
\frac95\leq \frac{M_4}{M_2^2}<\frac{27}{10},
\tag{4}
\]

with equality on the left precisely for equilateral triangles; the strict upper endpoint is approached by flattening triangles. The first two moments do not identify the side lengths, even locally around suitable scalene triangles.

There is a globally uniform inverse stability statement for shape. Normalize the squared sides to have sum one, sort them increasingly, and call the resulting triple \((q_1,q_2,q_3)\). If two triangles have normalized moment vectors \((u,v)=(M_4/M_2^2,M_6/M_2^3)\) and \((\widetilde u,\widetilde v)\), set \(\delta=\max\{|u-\widetilde u|,|v-\widetilde v|\}\). Then

\[
\boxed{\max_{1\leq i\leq3}|q_i-\widetilde q_i|\leq7\delta^{1/3}.}
\tag{5}
\]

The exponent \(1/3\) cannot be increased in any uniform estimate on a neighborhood of the equilateral triangle. The displayed constant is explicit, not claimed optimal.

## Assumptions and scope

The sampling measure is normalized two-dimensional Lebesgue area, not boundary length, a random-line chord process, or vertex sampling. The distance is ambient Euclidean distance. All three side lengths are strictly positive and obey strict triangle inequalities; repeated side lengths are allowed. Shapes are compared up to Euclidean isometry (including reflection), and normalized shape means division of squared side lengths by their sum. The stability statement is uniform over all positive-area triangles, with no lower bound on their minimum angle.

## Proof

**Exact moment lemma.** Write vertices as \(v_1,v_2,v_3\). The barycentric coordinates of each independent uniform point have the \(\operatorname{Dirichlet}(1,1,1)\) law. If \(\lambda,\mu\) are independent barycentric vectors and \(t_i=\lambda_i-\mu_i\), then \(\sum_i t_i=0\) and

\[
D^2=-x t_2t_3-y t_1t_3-z t_1t_2.
\tag{6}
\]

For any triple of nonnegative integers \(\alpha=(\alpha_1,\alpha_2,\alpha_3)\), the fundamental Dirichlet monomial identity is

\[
\mathbb E\prod_{i=1}^3\lambda_i^{\alpha_i}
=\frac{2\alpha_1!\alpha_2!\alpha_3!}{(\alpha_1+\alpha_2+\alpha_3+2)!}.
\tag{7}
\]

Expanding each \(t_i^{\alpha_i}\) by the binomial theorem, applying (7) separately to the two independent samples, and then expanding powers of (6) by the multinomial theorem gives the following coefficient table. In the symmetric monomial notation, \(\sum_{\mathrm{sym}}x^2y=x^2y+x^2z+xy^2+y^2z+xz^2+yz^2\):

\[
\begin{aligned}
M_2&=\frac{x+y+z}{18},\\
M_4&=\frac{x^2+y^2+z^2}{60},\\
M_6&=\frac{23(x^3+y^3+z^3)+7\sum_{\mathrm{sym}}x^2y-28xyz}{4200}\\
&=\frac{23e_1^3-62e_1e_2+20e_3}{4200}.
\end{aligned}
\tag{8}
\]

In particular the mixed \(xy\) coefficient in \(M_4\) vanishes. A fully exact independent implementation of the multinomial/Dirichlet calculation and coefficient comparison is provided in `check_triangle_moments.py`; it uses only rational arithmetic and the Python standard library. Formula (7), not the program output, is the mathematical justification of (8).

**Reconstruction, area, and feasibility.** The first and second lines of (8) recover \(e_1,e_2\); its third line recovers \(e_3\), proving (2) and the cubic (3). A polynomial's roots determine an unordered multiset, and three positive side lengths satisfying the triangle inequalities determine a triangle up to congruence.

Heron's identity written in squared-side variables is

\[
16\operatorname{area}(T)^2=4e_2-e_1^2.
\tag{9}
\]

Substitution of (2) into (9) gives (1). Conversely, if the reconstructed cubic has three positive real roots and \(4e_2>e_1^2\), the factorization

\[
4e_2-e_1^2=(a+b+c)(-a+b+c)(a-b+c)(a+b-c)
\tag{10}
\]

with \(a=\sqrt{x},b=\sqrt{y},c=\sqrt{z}\) implies all three strict triangle inequalities: of the last three factors, at most one can be nonpositive, and positivity of the product rules all such cases out. This proves the realizability test.

The inequality \(x^2+y^2+z^2\geq e_1^2/3\), with equality only at \(x=y=z\), gives the lower ratio in (4). The strict inequality \(4e_2>e_1^2\) gives \(x^2+y^2+z^2<e_1^2/2\) and hence the upper ratio. Degenerating nonzero-area triangles to collinear triples makes (9) tend to zero and achieves the upper endpoint as a limit.

**Why two moments are insufficient.** The noncongruent squared-side triples

\[
(x,y,z)=(1,2,3),\qquad
(\widetilde x,\widetilde y,\widetilde z)=(11/7,22/7,9/7)
\tag{11}
\]

both satisfy the strict triangle inequalities and have \(e_1=6\) and \(e_2=11\). They therefore have the same \(M_2=1/3\), \(M_4=7/30\), and area, but their sixth moments differ by exactly \(4/2401\). Indeed, fixing \(e_1,e_2\) fixes the intersection of a sphere with a plane in squared-side space; around a scalene triple there are arcs of positive, triangle-admissible triples that are not permutations. Thus two moments admit infinitely many distinct shapes, not merely the pair (11).

**Uniform stability.** For a triangle whose squared sides have sum one, express \(e_2,e_3\) in terms of the two scale-free observed moments:

\[
e_2=\frac12-\frac5{54}u,\qquad
e_3=\frac25-\frac{31}{108}u+\frac{35}{972}v.
\tag{12}
\]

For two such normalized triangles, let \(\varepsilon=\max\{|e_2-\widetilde e_2|,|e_3-\widetilde e_3|\}\). Equation (12) yields \(\varepsilon\leq(157/486)\delta\). Both monic cubics have identical quadratic coefficient \(-1\), and their difference at \(s\) has modulus at most \(\varepsilon(|s|+1)\).

When \(\varepsilon>0\), set \(r=(4\varepsilon)^{1/3}\). If \(r\leq1\), take the union of the three open complex disks of radius \(r\) centered at the three roots of the first cubic. On every boundary component, each root is at least distance \(r\), so the original cubic has modulus at least \(r^3=4\varepsilon\). Since all its roots lie in \([0,1]\), any point on that boundary has modulus at most \(1+r\); the polynomial perturbation has modulus at most \(\varepsilon(2+r)\leq3\varepsilon\). By Rouché's theorem, each connected disk-union component contains the same number of roots of the second cubic as of the first (with multiplicities). Any component contains at most three disks and has diameter at most \(6r\). Ordering the real roots therefore matches them within \(6r\). If \(r>1\), the bound is automatic because all normalized roots lie in \([0,1]\). Consequently

\[
\max_i|q_i-\widetilde q_i|\leq 6(4\varepsilon)^{1/3}
\leq 6(314/243)^{1/3}\delta^{1/3}<7\delta^{1/3},
\]

which proves (5).

**Sharpness of the stability exponent.** Let \(0<t<1/(2\sqrt3)\), and compare the two unordered normalized squared-side triples

\[
\begin{aligned}
Q_t&=(1/3+t,\ 1/3-t,\ 1/3),\\
\widetilde Q_t&=(1/3+t/\sqrt3,\ 1/3+t/\sqrt3,\ 1/3-2t/\sqrt3).
\end{aligned}
\tag{13}
\]

They define nondegenerate triangles by (9), have equal \(e_1=1\), equal \(e_2=1/3-t^2\), and hence equal \(u\). Their \(e_3\)'s differ by \(2t^3/(3\sqrt3)\), giving

\[
|v(Q_t)-v(\widetilde Q_t)|=\frac{648}{35\sqrt3}t^3,
\qquad
\max_i|q_i(Q_t)-q_i(\widetilde Q_t)|=\frac{t}{\sqrt3}.
\tag{14}
\]

No exponent greater than \(1/3\) is possible uniformly near the equilateral shape. This is a limit through positive-area triangles, not an appeal to numerical experiments.

## Verification

Execute `python3 check_triangle_moments.py` from the directory containing this document. The script reconstructs every monomial coefficient of \(M_2,M_4,M_6\) directly from (6) and (7) using exact rational arithmetic, compares these entire polynomials with (8), checks algebraic inversion and Heron's identity on five triangle configurations, and verifies the rational two-moment counterexample including the exact sixth-moment difference. These finite checks supplement rather than replace the universal derivation in the proof. The sharpness family and complex-root stability argument are analytic; neither is certified by sampling.

## Relationship to prior work

The classical random-chord and isotropic-correlation literature provides forward distributions for triangles. Ciccariello (2010) gives an isotropic correlation function, and Tong–Ahmadi–Pan (2013) provide the complete two-uniform-point distance distribution in arbitrary triangles. Reichenwallner (2017, Proposition 4) provides formulas for arbitrary moments of such random point-pair distances, used for a different monotonicity question. These forward formulas subsume the availability of moment evaluations, but do not themselves state the three-even-moment inverse, the two-moment area identity, the sharp failure of two-moment shape identification, or the optimal cube-root stability statement.

Gates (1982) established recognition of triangles by chord moments; the precise cited sufficient data \(\{I_0,I_1,I_5\}\) consist of chord-power functionals including perimeter and area. The present data are instead the three area-normalized point-pair moments proportional to \(\{I_5,I_7,I_9\}\), without a priori perimeter or area. Martirosyan–Sargsyan (2026) give a different chord-power recognition set \(\{I_0,I_1,I_2\}\). Neither cited sufficient-data set entails this three-even-moment reconstruction without further argument. The original Gates full text was not accessible for a decisive all-formulations priority check; independent literature verification remains appropriate.

## Limitations

This does not extend to arbitrary polygons or non-Euclidean distances. The exact forward moment evaluations, barycentric integration, Heron's identity, and generic perturbation-of-roots techniques are classical ingredients, not claimed independently new. The asserted contribution is their exact finite-moment inverse/area/stability combination for all triangles, with a sharp stability exponent; historical duplication cannot be ruled out, especially in the older chord-power literature. The numerical constant 7 in (5) is a proved convenient bound, not a sharp constant, and no stability of the unnormalized side lengths is claimed without control of the scale.

## References

1. S. Ciccariello, *The isotropic correlation function of plane figures: the triangle case*, arXiv:1006.1496v1 (first posted 8 June 2010), https://arxiv.org/abs/1006.1496.
2. F. Tong, M. Ahmadi, J. Pan, *Random Distances Associated with Arbitrary Triangles: A Systematic Approach between Two Random Points*, arXiv:1312.2498v1 (2013), https://arxiv.org/abs/1312.2498.
3. J. Gates, *Recognition of triangles and quadrilaterals by chord length distribution*, Journal of Applied Probability 19 (1982), 873–879, https://doi.org/10.2307/3213843.
4. B. Reichenwallner, *Moments of volumes of lower-dimensional random simplices are not monotone*, Monatshefte für Mathematik 186 (2018), 481–501; first arXiv posting 2017, https://arxiv.org/abs/1702.05943.
5. M. Martirosyan and R. Sargsyan, *A closed form for the chord-power integral \(I_2\) of a triangle*, arXiv:2605.24616 (2026), https://arxiv.org/abs/2605.24616.
