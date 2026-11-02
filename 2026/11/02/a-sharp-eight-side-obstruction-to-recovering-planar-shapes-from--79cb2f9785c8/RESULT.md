# A sharp eight-side obstruction to recovering planar shapes from rotational width correlations

## Finding

For a plane convex body \(K\), let \(w_K(\theta)\) be its Euclidean projection width in direction \((\cos\theta,\sin\theta)\), and define its **unoriented rotational width correlation** by
\[
R_K(t)=\frac{1}{\pi}\int_0^\pi w_K(\theta)w_K(\theta+t)\,d\theta,\qquad t\in\mathbb R.
\]
The angular origin is unobserved. Congruence means equivalence under a Euclidean isometry, including a possible reflection.

**Theorem.** Among all full-dimensional, centrally symmetric, equilateral convex polygons with four or six sides, \(R_K\) determines \(K\) up to congruence. This is sharp in the number of sides: there are two noncongruent, centrally symmetric, equilateral convex octagons \(K_A,K_B\), each with all edges of length one, such that \(R_{K_A}(t)=R_{K_B}(t)\) for **every** real \(t\). They have the same area and perimeter,
\[
\operatorname{Per}(K_A)=\operatorname{Per}(K_B)=8,\qquad
\operatorname{Area}(K_A)=\operatorname{Area}(K_B)=\frac{3+\sqrt2+\sqrt3+\sqrt6}{2},
\]
but the single-direction third moments of width differ explicitly:
\[
\frac1\pi\int_0^\pi\bigl(w_{K_A}(\theta)^3-w_{K_B}(\theta)^3\bigr)\,d\theta
=\frac{11\sqrt2-3\sqrt6-8}{\pi}>0.
\]

The same two-point-correlation ambiguity occurs for **real-analytic strictly convex centrally symmetric bodies**, even for pairs arbitrarily close to a disk. A third-order, two-lag width correlation distinguishes the analytic pair at every smoothing scale.

A general auxiliary identity makes the area/perimeter coincidence structural rather than accidental: for every full-dimensional, centrally symmetric planar convex body, with correlation \(R=R_K\),
\[
\boxed{\ \operatorname{Area}(K)=\frac{\pi}{4}\bigl(R(0)+R''(0)\bigr),\qquad
\operatorname{Per}(K)=\pi\sqrt{\frac1\pi\int_0^\pi R(t)\,dt}.\ }
\]
In particular, any two such bodies with identical \(R\) automatically have equal area and perimeter.

## Assumptions and scope

The polygonal sharpness statement refers to **equilateral, centrally symmetric, full-dimensional** Euclidean polygons: the congruence statement for four or six sides is not asserted for arbitrary edge lengths or nonsymmetric polygons. Direction is unlabelled in the sense that one observes only the function of relative angle \(t\), not individual widths or their orientation. Degenerate line segments are not polygons in the theorem. All correlation averages use normalized Lebesgue measure \(d\theta/\pi\) over one period. The analytic examples are full-dimensional, strictly convex, centrally symmetric bodies with positive curvature and real-analytic support functions.

For construction, write \(u_a=(\cos(\pi a/12),\sin(\pi a/12))\) and set
\[
A=\{0,1,4,6\},\qquad B=\{0,1,3,7\},\qquad
K_S=\sum_{a\in S}[-u_a/2,u_a/2]\quad(S=A,B),
\]
where the sum is a Minkowski sum of unit segments. As all four unoriented directions are distinct, both bodies are genuine centrally symmetric eight-gons, with two unit edges parallel to each generator.

## Proof

### 1. Width correlations are a circular difference measurement

Any centrally symmetric equilateral \(2m\)-gon is a Minkowski sum of \(m\) unit segments whose unoriented generator angles \(\phi_1,\ldots,\phi_m\) are distinct modulo \(\pi\). Thus
\[
w(\theta)=\sum_{j=1}^m|\cos(\theta-\phi_j)|.
\]
With normalized period-\(\pi\) Fourier coefficients \(w_k=\pi^{-1}\int_0^\pi w(\theta)e^{-2ik\theta}\,d\theta\), the elementary Fourier expansion of \(|\cos|\) gives
\[
w_k=c_kF(k),\quad F(k)=\sum_{j=1}^m e^{-2ik\phi_j},\qquad
c_0=\frac2\pi,\quad c_k=\frac{2(-1)^{k+1}}{\pi(4k^2-1)}\ (k\ge1),\quad c_{-k}=c_k.
\]
Every coefficient \(c_k\) is nonzero. Parseval gives
\[
R(t)=\sum_{k\in\mathbb Z}c_k^2|F(k)|^2e^{2ikt}.
\]
Consequently, knowledge of \(R\) is precisely knowledge of the circular difference multiset \(\{\phi_i-\phi_j\pmod\pi:1\le i,j\le m\}\), counting multiplicities: the Fourier coefficients of this positive finite difference measure are \(|F(k)|^2\), and finite measures on a circle are determined by all their Fourier coefficients. The zeroth mode \(F(0)=m\) is fixed by the width mean, so the number of generators is itself determined when their lengths are one.

### 2. Three directions are rigid

For two distinct directions modulo \(\pi\), the difference multiset gives their circular separation up to replacing the separation by its complement; these yield congruent pairs under reflection. For three distinct directions, order them cyclically and let their positive successive gaps be \(g_1,g_2,g_3\), with \(g_1+g_2+g_3=\pi\). The multiset of off-diagonal directed differences is exactly
\[
\{g_1,g_2,g_3,\pi-g_1,\pi-g_2,\pi-g_3\}.
\]
A second positive gap triple with the same difference multiset must, after a permutation, choose each gap either as \(g_i\) or as \(\pi-g_i\). If exactly one gap is complemented and the sum remains \(\pi\), that gap is \(\pi/2\) and is unchanged. If exactly two are complemented, their original sum would be \(\pi\), impossible because the third gap is positive. If all three are complemented, their new sum would be \(2\pi\), not \(\pi\). Thus the unordered gap triple is forced. Any permutation of three successive gaps is induced by a rotation or reversal of a three-point cyclic configuration. This proves congruence rigidity through six sides, including coincident gap sizes.

### 3. The sharp octagonal pair

For \(A\) and \(B\), the six unordered circular interval classes \(\min(|a-b|,12-|a-b|)\) with \(a<b\) are exactly \(1,2,3,4,5,6\), each once. Therefore their complete directed difference multisets on the angular circle of circumference \(\pi\) coincide. Section 1 implies \(R_{K_A}=R_{K_B}\) identically, not merely at finitely many angles.

The ordered circular gaps of \(A\) are \((1,3,2,6)\) twelfths of \(\pi\), whereas those of \(B\) are \((1,2,4,5)\) twelfths. The unordered gap multisets are different, so no rotation or reflection can map the generator direction sets to one another. Their edge directions therefore prove the octagons are not congruent.

Every edge has length one, hence each perimeter is eight. The standard planar zonotope area formula, also obtained by adding the parallelogram swept out by each new segment, gives
\[
\operatorname{Area}(K_S)=\sum_{\{a,b\}\subset S}|\det(u_a,u_b)|
=\sum_{j=1}^6\sin\frac{j\pi}{12}=\frac{3+\sqrt2+\sqrt3+\sqrt6}{2}.
\]
The third width moment is computed without simulation: partition \([0,\pi]\) at the sign changes of the four cosine terms. In units \(\pi/12\), the breakpoints are \(0,6,7,10,12\) for \(A\) and \(0,1,6,7,9,12\) for \(B\). On each interval, the width is \(u\cos\theta+v\sin\theta\), where \(u=\sum_a s_a\cos(\pi a/12)\), \(v=\sum_a s_a\sin(\pi a/12)\), and \(s_a\) is the constant sign of the corresponding cosine. An explicit antiderivative of its cube is
\[
\mathcal P_{u,v}(\theta)=u^3\sin\theta-v^3\cos\theta
+(uv^2-u^3/3)\sin^3\theta+(v^3/3-u^2v)\cos^3\theta.
\]
Evaluation at those finite endpoints yields, exactly,
\[
\frac1\pi\int_0^\pi w_{K_A}^3=\frac{\sqrt6+3\sqrt3+9\sqrt2+109/3}{\pi},\qquad
\frac1\pi\int_0^\pi w_{K_B}^3=\frac{-6\sqrt2+9\sqrt3+12\sqrt6+133}{3\pi}.
\]
Subtraction gives the claimed positive difference. Strict positivity follows from \(11\sqrt2-3\sqrt6>8\), equivalently \(11-3\sqrt3>4\sqrt2\). Both sides of the latter are positive, and squaring reduces it to \(58>33\sqrt3\), which holds because \(58^2=3364>3267=3\cdot33^2\).

### 4. Correlation forces area and perimeter

For a centered centrally symmetric convex body, its support function is \(h(\theta)=w(\theta)/2\). The classical planar support-function identities (valid also for polygons by approximation or weak differentiation) are
\[
\operatorname{Per}(K)=\int_0^{2\pi}h(\theta)\,d\theta,\qquad
\operatorname{Area}(K)=\frac12\int_0^{2\pi}(h(\theta)^2-h'(\theta)^2)\,d\theta.
\]
Since \(R(0)=\pi^{-1}\int_0^\pi w^2\) and \(R''(0)=-\pi^{-1}\int_0^\pi(w')^2\), these formulas give \(\operatorname{Area}(K)=\pi(R(0)+R''(0))/4\). Averaging \(R(t)\) over one angular period gives the square of the mean width. Cauchy's perimeter formula gives the stated perimeter identity. The derivatives exist because widths of convex bodies are Lipschitz and hence have square-integrable weak derivatives; their squared Fourier coefficients have finite weighted sum.

### 5. Real-analytic strictly convex examples

Let \(P_t\) be the positive Poisson kernel on the angle circle of circumference \(\pi\), acting on Fourier mode \(e^{2ik\theta}\) by multiplication with \(e^{-|k|t}\), for any \(t>0\). Set \(h_{S,t}=P_t*(w_{K_S}/2)\), with convolution normalized by \(1/\pi\). This is the support function of a Minkowski average of rotated copies of \(K_S\). It is real analytic. The curvature-radius measure of a polygon is nonzero and positive; convolution with the everywhere-positive Poisson kernel yields \(h_{S,t}+h_{S,t}''>0\) at every angle, so the associated bodies are strictly convex with positive analytic curvature.

All width Fourier magnitudes of the two bodies remain equal after the common nonvanishing multiplier, hence their complete width correlations remain equal. Any congruence after smoothing would, by division of every Fourier mode by \(e^{-|k|t}\), give a congruence of the original octagons, which is impossible. As \(t\to\infty\), both supports tend uniformly to the same constant, so the ambiguous strictly convex bodies can be arbitrarily close to disks.

Their **third-order two-lag** correlation \(T_S(u,v)=\pi^{-1}\int_0^\pi w_S(\theta)w_S(\theta+u)w_S(\theta+v)\,d\theta\) remains different at every \(t>0\). To see this exactly, take the Fourier coefficient indexed by \((1,1)\). With \(\zeta=e^{-i\pi/6}\) and \(F_S(k)=\sum_{a\in S}\zeta^{ka}\), direct finite sums give
\[
F_A(1)^2F_A(-2)=-2\sqrt3-2i,\qquad
F_B(1)^2F_B(-2)=2\sqrt3-2i.
\]
Since \(c_1=2/(3\pi)\) and \(c_2=-2/(15\pi)\), the difference of the \((1,1)\) coefficients of \(T_A\) and \(T_B\) is
\[
\boxed{\ \widehat T_A(1,1)-\widehat T_B(1,1)=\frac{32\sqrt3}{135\pi^3}\ne0.\ }
\]
After Poisson smoothing this difference is multiplied by \(e^{-4t}\), so it remains nonzero for every finite \(t>0\). Thus the third-order statistic, unlike the complete second-order statistic, separates the example even in the real-analytic strictly convex class.

## Verification

The standalone file `verify.py` implements exact finite difference-multiset and dihedral-orbit checks, computes the area radical identity, checks the third-order Fourier coefficient, reproduces the cubic-width integrals from their piecewise trigonometric antiderivative, and compares the full width correlations at 17 relative angles by independent trapezoidal quadrature. It also checks all three-point cyclic configurations on several finite grids as a sanity test; that enumeration is **not** the proof of the continuous rigidity statement. Running `python verify.py --symbolic` adds exact radical evaluations with the optional SymPy library. The completed run produced `VERIFY_OK 3908 checks`.

The universality of the rigidity, the all-angle equality, and the real-analytic extension rests on the analytic proof above, not on finite tests. The symbols \(i\) in complex Fourier expressions denote the imaginary unit, not an extra geometric dimension.

## Relationship to prior work

The planar zonotope generator representation and determinant-volume formula are classical; Gover (2014) gives them explicitly. Homometric finite sets and the ambiguity of recovering a finite set from its difference multiset are established subjects, as described by Baake and Grimm (2006); the pair \(\{0,1,4,6\}\) and \(\{0,1,3,7\}\) is the known all-interval tetrachord pair, not newly discovered here. Bianchi, Gardner and Kiderlen (2010) analyze the **body covariogram**, which is not the rotational width correlation studied here: their Fourier transform concerns indicator functions of convex bodies, whereas this work concerns the one-dimensional Fourier power spectrum of widths. In particular, planar uniqueness results for the body covariogram do not imply uniqueness for this weaker/different width statistic.

The contribution here is the geometry-specific, sharp four/six versus eight side threshold under unit edges and central symmetry, an exact third-width-moment separation of the explicit octagons, the area/perimeter identities recovered solely from the rotational width correlation, and persistence of the obstruction among analytic strictly convex bodies with an explicit third-order spectral witness. No priority is claimed for the general principles of Fourier autocorrelation, homometry, zonotope area, or support-function reconstruction.

## Limitations

The side-count threshold is proved **only** for equilateral centrally symmetric polygons; it is not an assertion about all convex polygons or all weighted zonotopes. The third moment is shown to distinguish the particular exhibited octagons, not to reconstruct every possible zonotope. Smooth counterexamples are demonstrated in the plane, not in every dimension. Measurement noise, statistical estimation, and numerical stability are not analyzed. The literature comparison supports the exact stated contribution under current accessible sources but does not certify worldwide historical priority; related results may exist under different inverse-problem terminology.

## References

1. M. Baake and U. Grimm, *Homometric model sets and window covariograms*, first public arXiv version 2006-10-12, arXiv:math/0610411, https://arxiv.org/abs/math/0610411.
2. E. Gover, *Congruence and Metrical Invariants of Zonotopes*, first public arXiv version 2014-01-19, arXiv:1401.4749, https://arxiv.org/abs/1401.4749.
3. G. Bianchi, R. J. Gardner and M. Kiderlen, *Phase retrieval for characteristic functions of convex bodies and reconstruction from covariograms*, first public arXiv version 2010-03-23, arXiv:1003.4486, https://arxiv.org/abs/1003.4486.
4. The classical all-interval tetrachords \(\{0,1,4,6\}\) and \(\{0,1,3,7\}\), often called the Z-related four-note pair, are acknowledged as a known combinatorial construction; no specific first-public day is asserted for that earlier musical-set-theory observation.
