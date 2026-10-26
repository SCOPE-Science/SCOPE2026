# Sharp fourth-moment rigidity and an exact defect identity for the five-point planar Fourier cross

## Finding
Let \(z,w\in\mathbb T\), and let \(dm\) denote probability-normalized Haar measure on \(\mathbb T^2\). For any complex coefficients \(a,b,c,d,e\), put
\[
P(z,w)=a+bz+cz^{-1}+dw+ew^{-1},\qquad
S=|a|^2+|b|^2+|c|^2+|d|^2+|e|^2.
\]
Then the **exact sharp** fourth-moment bound is
\[
\boxed{\int_{\mathbb T^2}|P|^4\,dm\le\frac{27}{11}S^2.}
\]
For \(S>0\), equality holds precisely for
\[
\boxed{(a,b,c,d,e)=\lambda\bigl(\sqrt3,\sqrt2e^{i\theta},\sqrt2e^{-i\theta},
\sqrt2e^{i\phi},\sqrt2e^{-i\phi}\bigr),}
\]
where \(\lambda\in\mathbb C\setminus\{0\}\) and \(\theta,\phi\in\mathbb R\). In particular, the zero-frequency coefficient has squared magnitude three halves of each of the four first-neighbor coefficients, and all maximizing coefficient phases are affine on the frequency lattice.

There is also an **exact global stability identity**. Normalize \(S=1\), writing the coefficients as \(\alpha,\beta,\gamma,\delta,\varepsilon\). Define
\[
A=|\alpha|^2,\quad x=|\beta|^2+|\gamma|^2,\quad
y=|\delta|^2+|\varepsilon|^2,\quad s=x+y,
\]
\[
q=|\beta\gamma|,\quad t=|\delta\varepsilon|,\quad
h=\frac{x}{2}-q,\quad v=\frac{y}{2}-t,
\]
and let \(M(\alpha,\beta,\gamma,\delta,\varepsilon)\) be the fourth moment of the associated five-mode polynomial. Define the phase deficit
\[
\Pi=M(|\alpha|,|\beta|,|\gamma|,|\delta|,|\varepsilon|)
-M(\alpha,\beta,\gamma,\delta,\varepsilon)\ge0.
\]
Then, with no missing error term,
\[
\boxed{
\begin{aligned}
\frac{27}{11}-M(\alpha,\beta,\gamma,\delta,\varepsilon)
={}&\frac{11}{4}\left(s-\frac8{11}\right)^2
+\frac34(x-y)^2\\
&+2\left[2A(h+v)+h\left(\frac x2+q\right)
+v\left(\frac y2+t\right)+xy-4qt\right]+\Pi.
\end{aligned}}
\]
Every term on the right is nonnegative. The identity measures the spectral-shell imbalance, horizontal-versus-vertical imbalance, opposite-arm imbalance, and phase frustration separately. In particular,
\[
\frac{27}{11}-M\ge
\frac{11}{4}\left(s-\frac8{11}\right)^2+\frac34(x-y)^2.
\]
The same theorem, including the sharp constant, complete equality classification, and exact stability identity, holds for probability-normalized Fourier averages over \(\mathbb Z_N\times\mathbb Z_M\) whenever \(N,M\ge5\), where \(z,w\) range over the corresponding roots of unity.

## Assumptions and scope
The Fourier support is the radius-one Lee cross \(\{(0,0),(1,0),(-1,0),(0,1),(0,-1)\}\). All five coefficients are unrestricted complex numbers. There is no reality, equal-modulus, or positivity hypothesis. The coefficient norm is the unweighted Euclidean norm, and all Haar measures are probability-normalized. The cyclic size restrictions are **necessary for the stated nonaliasing proof**, not asserted to be the precise best possible sizes. Finite grids with smaller cyclic orders are not covered. The two-torus case has no frequency aliasing.

## Proof
**1. Exact autocorrelation expansion.** By character orthogonality,
\[
\int|P|^4\,dm=\sum_{(j,k)\in\mathbb Z^2}|R_{j,k}|^2,
\quad R_{j,k}=\sum_{u-v=(j,k)}c_u\overline{c_v},
\]
where the nonzero frequency coefficients \(c_u\) are \(a,b,c,d,e\) at the five cross frequencies. With \(S=\sum|c_u|^2\), the nontrivial positive-difference representatives are
\[
\begin{aligned}
R_{1,0}&=b\bar a+a\bar c,&R_{0,1}&=d\bar a+a\bar e,\\
R_{2,0}&=b\bar c,&R_{0,2}&=d\bar e,\\
R_{1,1}&=b\bar e+d\bar c,&R_{1,-1}&=b\bar d+e\bar c.
\end{aligned}
\]
Their negatives are complex conjugates. Thus
\[
\begin{aligned}
M(a,b,c,d,e)={}&S^2+2\bigl(|b\bar a+a\bar c|^2
+|d\bar a+a\bar e|^2+|b\bar c|^2+|d\bar e|^2\\
&\qquad+|b\bar e+d\bar c|^2+|b\bar d+e\bar c|^2\bigr).
\end{aligned}
\tag{1}
\]
Equation (1) holds for all complex coefficients, including zeros. It also follows independently by computing the squared norm of the ordered pair-sum convolution.

**2. Phase majorization.** Apply the triangle inequality to the four two-term sums in (1). The resulting moment is exactly \(M(|a|,|b|,|c|,|d|,|e|)\), and the difference is \(S^2\Pi\ge0\). More explicitly, each two-term complex sum \(U+V\) contributes the nonnegative deficit
\[
2\bigl((|U|+|V|)^2-|U+V|^2\bigr)
=4\bigl(|U||V|-\operatorname{Re}(U\bar V)\bigr).
\]
The four pairs \((U,V)\) are \((b\bar a,a\bar c)\), \((d\bar a,a\bar e)\), \((b\bar e,d\bar c)\), and \((b\bar d,e\bar c)\), with normalized coefficients understood for \(\Pi\).

**3. Magnitude reduction.** For \(S=1\), use \(A,x,y,s,q,t\) as defined above. Formula (1) for nonnegative coefficients becomes
\[
M_{\rm mag}=1+2\bigl[A(s+2q+2t)+q^2+t^2+xy+4qt\bigr].
\tag{2}
\]
Here \(A=1-s\), \(0\le s\le1\), and AM--GM gives \(0\le q\le x/2\), \(0\le t\le y/2\). Every summand in (2) that depends on \(q,t\) is nondecreasing in either argument; replacing them by \(x/2,y/2\) can only increase the moment. The resulting expression is
\[
M_{\rm mag}\le1+2\left[2s(1-s)+\frac{s^2}{4}+\frac32xy\right].
\tag{3}
\]
Since \(xy\le s^2/4\),
\[
M_{\rm mag}\le1+4s-\frac{11}{4}s^2
=\frac{27}{11}-\frac{11}{4}\left(s-\frac8{11}\right)^2
\le\frac{27}{11}.
\]
This proves the claimed universal constant without numerical optimization or an unproved inequality.

**4. Exact stability identity.** Keep track of every previous difference. Write \(h=x/2-q\) and \(v=y/2-t\). The exact difference between the square brackets of (3) and (2) is
\[
D=2A(h+v)+h\left(\frac x2+q\right)+v\left(\frac y2+t\right)+xy-4qt.
\]
All four summands are nonnegative: \(A,h,v\ge0\) and \(4qt\le xy\). Also \(s^2/4-xy=(x-y)^2/4\). Combining these two differences with the phase deficit and the completed-square identity yields exactly the boxed stability formula. The derivation is algebraic, with no limiting argument or hidden positivity assumption.

**5. Necessity and sufficiency of equality.** For equality, both visible squares in the stability identity vanish: \(s=8/11\) and \(x=y=4/11\). As \(A=3/11>0\), the \(2A(h+v)\) term forces \(h=v=0\), hence \(|\beta|=|\gamma|=|\delta|=|\varepsilon|=\sqrt{2/11}\). Equality of the first two complex triangle inequalities, with the now nonzero central coefficient, forces
\[
\arg\beta+\arg\gamma\equiv2\arg\alpha,
\qquad\arg\delta+\arg\varepsilon\equiv2\arg\alpha
\pmod{2\pi}.
\]
These relations also align the two cross-frequency sums; they are equivalent to the two free affine frequencies \(\theta,\phi\) in the displayed equality family. Every listed vector makes all steps exact and gives the fourth-moment ratio \(27/11\). No other nonzero vector can attain the bound.

**6. Finite grids.** The frequencies involved in all autocorrelations have coordinate differences between \(-2\) and \(2\). For \(N,M\ge5\), their residue pairs are distinct, so discrete Fourier orthogonality gives exactly the same formula (1). All subsequent steps and all equality conditions therefore apply unchanged.

## Verification
The standalone `artifacts/verify.py` uses independent ordered pair-sum convolution and difference autocorrelation calculations, without implementing the optimization proof as an assumed inequality. It performs 6,700 deterministic assertions: 1,500 independent pairs of complex-convolution checks, 1,500 sharp-bound tests, 1,500 normalized exact-defect tests, 1,500 phase-majorization tests, 300 exact-integer sharp inequalities, 180 finite-product Fourier-grid comparisons, and 220 exact-family checks. Execute from the artifact root using `python artifacts/verify.py`; only the Python standard library is required. Finite tests corroborate the fully written universal proof but do not replace it.

## Relationship to prior work
González-Riquelme and Oliveira e Silva (2024, arXiv:2405.16647) develop sharp finite-field Fourier extension and a convolution formulation of even moments. Their complete theorems concern paraboloids, hyperbolic paraboloids and higher-dimensional cones; they do not state a sharp inequality for the five-frequency Lee cross on the continuous torus or on large rectangular cyclic grids. Their main formulas differ both in support and normalizations. Iosevich et al. (2018, arXiv:1806.11387) investigate extension on finite-field zero-radius spheres, not this unrestricted sharp five-mode norm-and-stability classification.

The published result *Sharp fourth-moment extension and one-axis rigidity for finite abelian crosses* treats the **full union of two order-\(n\) coordinate subgroups** in a finite group, with \(2n-1\) frequencies and a sharp extremizer on one complete axis. At \(n\ge5\), its substantially larger frequency space gives only a loose bound for the present five-point subspace and does not imply the precise \(27/11\) constant or the mixed-axis equality family. Its order-three example has the same five-point **residue support** but aliases opposite-difference frequencies and yields the different all-one ratio \(77/25\); the continuous all-one ratio here is \(61/25\).

The published result *Sharp fourth-moment extension and nine phase-rigid optimizers on the ternary split cone* optimizes on the **same five residues modulo three**, but extra mod-three collisions produce a different sharp constant and discrete phase rigidity; it cannot imply the nonaliased continuous and order-at-least-five theorem. The published *Sharp fourth moments for a five-point Ferrers Fourier spectrum* treats \(\{(0,0),(1,0),(2,0),(0,1),(1,1)\}\), which has a boundary nonvertex point rather than the interior center of the present diamond. These supports are not affinely lattice-equivalent, and its algebraic sharp constant \(2.646915\ldots\) differs from \(27/11\). Unlike these results, the present theorem additionally supplies a global exact nonnegative defect decomposition.

## Limitations
The classification is proved only at the fourth moment for this five-point support (and its nonaliasing cyclic realizations). It is not a theorem for all Lee crosses, arbitrary extra frequencies, or small cyclic orders, nor does it assert a minimal optimal metric distance to the optimizer orbit. It supplies an exact coefficient-space stability certificate and two explicit coercive lower bounds, not a sharp stability constant in a prescribed quotient-space distance. Although the closest source statements and actual database searches were compared at the level of their implications, an older unindexed equivalent \(\Lambda(4)\) extremal or multidimensional filter-autocorrelation formula remains a bibliographic risk. No independent audit is asserted.

## References
1. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1, first publicly posted 2024-05-26, https://arxiv.org/abs/2405.16647.
2. A. Iosevich, D. Koh, S. Lee, T. Pham, and C.-Y. Shen, *On restriction estimates for the zero radius sphere over finite fields*, arXiv:1806.11387v1, first publicly posted 2018-06-29, https://arxiv.org/abs/1806.11387.
3. *Sharp fourth-moment extension and one-axis rigidity for finite abelian crosses*, published research record, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-extension-and-one-axis-rigidity-for-finite-a--5b31463115dc.
4. *Sharp fourth-moment extension and nine phase-rigid optimizers on the ternary split cone*, published research record, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-extension-and-nine-phase-rigid-optimizers-on--d65b0e8eea36.
5. *Sharp fourth moments for a five-point Ferrers Fourier spectrum*, published research record, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moments-for-a-five-point-ferrers-fourier-spectrum--bb5fd3f72396.
