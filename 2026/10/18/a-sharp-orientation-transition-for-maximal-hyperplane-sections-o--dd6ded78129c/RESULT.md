# A sharp orientation transition for maximal hyperplane sections of Euclidean ball prisms

## Finding

For every integer \(d\ge4\) and \(h>0\), define the centered Euclidean ball prism
\[
Z_{d,h}=\{(x,z)\in\mathbb R^{d-1}\times\mathbb R:\|x\|_2\le1,\ |z|\le h\}.
\]
Let \(\kappa_j=\pi^{j/2}/\Gamma(1+j/2)\), the volume of the unit \(j\)-ball, and put \(\alpha=(d-2)/2\). Define, for \(0<k<1\),
\[
J_\alpha(k)=\int_0^k(1-t^2)^\alpha\,dt,
\qquad
M_\alpha(k)=\frac{J_\alpha(k)-k(1-k^2)^\alpha}{k^3(1-k^2)^\alpha}.
\]
Then \(M_\alpha\) increases strictly from \((d-2)/3\) to \(+\infty\). In particular there is a sharp height
\[
h_c(d)=\sqrt{\frac3{d-2}}
\]
with this **complete global maximal-section classification, including affine hyperplanes**:

* If \(h\ge h_c(d)\), the maximum \((d-1)\)-volume equals \(2h\kappa_{d-2}\), and the only maximizing hyperplanes are the central planes parallel to the prism axis (the ball-normal direction is arbitrary).
* If \(0<h<h_c(d)\), there is a unique \(k_*=k_*(d,h)\in(0,1)\) satisfying \(h^2M_\alpha(k_*)=1\). Every maximizing plane passes through the origin and its unit normal makes an angle \(\theta_*\in(0,\pi/2)\) with the prism axis, where \(\tan\theta_*=h/k_*\). The maximum equals
\[
2\kappa_{d-2}\frac{\sqrt{h^2+k_*^2}}{k_*}J_\alpha(k_*).
\]
The arbitrary azimuthal direction and reversal of a normal are the only degeneracies in this classification. As \(h\uparrow h_c(d)\) from below,
\[
k_*^2\sim\frac5{d+1}\left(1-\frac{h^2}{h_c(d)^2}\right).
\]
Thus the oblique optimum reaches the vertical-plane orientation through a sharp square-root transition.

In dimension \(d=4\), the value becomes elementary:
\[
\boxed{\max_H\operatorname{vol}_3(Z_{4,h}\cap H)=
\begin{cases}
\dfrac{4\pi}{3}\left(1+\dfrac{h^2}{3}\right)^{3/2},&0<h\le\sqrt{3/2},\\[4pt]
2\pi h,&h\ge\sqrt{3/2}.
\end{cases}}
\]
For \(0<h<\sqrt{3/2}\), the unique optimal truncated-ball parameter is \(k_*=\sqrt{1-2h^2/3}\). The first branch and its strict oblique equality classification are not part of the previously established three-dimensional result.

## Assumptions and scope

The dimensions are integers \(d\ge4\), the Euclidean radius of the base ball is exactly one, and \(h>0\) is the **half-height**. Sections and their volumes use induced Euclidean \((d-1)\)-dimensional measure. The maximum ranges over every affine hyperplane of \(\mathbb R^d\), including central, translated, and supporting planes. The base ball's rotational symmetry permits its first coordinate to be selected along the horizontal component of a plane normal. The angle \(\theta\) lies in \([0,\pi/2]\): \(\theta=0\) means a horizontal plane, \(\theta=\pi/2\) a plane containing the cylinder axis. The parameter \(k=h\cot\theta\) is understood by limits at both endpoints. No assertion is made here about products involving two or more interval factors, non-Euclidean bases, or dimensions \(d=2,3\).

## Proof

**1. Reduction to central sections.** For any fixed unit normal \(u\), Brunn's concavity theorem says that the function assigning the \((d-1)\)-st root of the volume of \(Z_{d,h}\cap\{y:\langle y,u\rangle=s\}\) to the offset \(s\) is concave on its support interval. Central symmetry of \(Z_{d,h}\) makes this function even. Hence its maximum over offsets occurs at \(s=0\). After identifying the maximizing central normals below, strictness in each of their translated section profiles shows that an affine maximizer must itself be central; see step 5.

**2. Exact all-orientation section profile.** Write a unit normal as \(u=(\sin\theta\,e_1,\cos\theta)\), where the last coordinate is axial. For \(0<\theta<\pi/2\), the central plane is the graph \(z=-\tan\theta\,x_1\). The graph Jacobian is \(\sec\theta\), and the allowed horizontal ball coordinates satisfy \(|x_1|\le h\cot\theta=k\). At fixed \(x_1=t\), the remaining section is a \((d-2)\)-ball with volume \(\kappa_{d-2}(1-t^2)^\alpha\). Thus
\[
A_{d,h}(k):=\operatorname{vol}_{d-1}(Z_{d,h}\cap u^\perp)=
\begin{cases}
2\kappa_{d-2}\dfrac{\sqrt{h^2+k^2}}{k}J_\alpha(k),&0<k\le1,\\[5pt]
\kappa_{d-1}\dfrac{\sqrt{h^2+k^2}}{k},&k\ge1.
\end{cases}
\]
The integral identity \(2\kappa_{d-2}J_\alpha(1)=\kappa_{d-1}\) ensures continuity at \(k=1\). Taking the two endpoint limits gives \(A_{d,h}(0)=2h\kappa_{d-2}\) and \(A_{d,h}(\infty)=\kappa_{d-1}\). For \(k\ge1\), the profile is strictly decreasing in \(k\), because \(\sqrt{h^2+k^2}/k=\sqrt{1+h^2/k^2}\) strictly decreases. Therefore no global maximizer has \(k>1\), and the horizontal plane cannot maximize.

**3. A strict monotonicity lemma.** Put \(f_\alpha(k)=(1-k^2)^\alpha\). Direct differentiation of the first profile, with a positive factor removed, shows
\[
\operatorname{sgn}A'_{d,h}(k)=
\operatorname{sgn}\left(k^3 f_\alpha(k)-h^2\big[J_\alpha(k)-kf_\alpha(k)\big]\right)
=\operatorname{sgn}\big[1-h^2M_\alpha(k)\big].
\]
Integration by parts yields
\[
J_\alpha(k)-kf_\alpha(k)=2\alpha\int_0^kt^2(1-t^2)^{\alpha-1}\,dt,
\]
and hence, substituting \(t=ks\),
\[
M_\alpha(k)=2\alpha\int_0^1s^2
\frac{(1-k^2s^2)^{\alpha-1}}{(1-k^2)^\alpha}\,ds.
\]
For fixed \(0<s<1\), the derivative of the logarithm of the positive integrand factor with respect to \(q=k^2\) is
\[
\frac{\alpha}{1-q}-\frac{(\alpha-1)s^2}{1-qs^2}
=\frac{\alpha(1-s^2)+s^2(1-q)}{(1-q)(1-qs^2)}>0.
\]
Since \(\alpha\ge1\), strict positivity holds uniformly pointwise on the open parameter range. Integration gives strict monotonicity of \(M_\alpha\). Dominated convergence at zero yields
\[
M_\alpha(0+)=2\alpha\int_0^1s^2\,ds=\frac{2\alpha}{3}=\frac{d-2}{3}.
\]
The numerator \(J_\alpha(k)-k f_\alpha(k)\) tends to \(J_\alpha(1)>0\), whereas its denominator \(k^3f_\alpha(k)\) tends to zero as \(k\uparrow1\). Therefore \(M_\alpha(k)\to+\infty\).

**4. Sharp maximization and rigidity.** If \(h^2\ge3/(d-2)\), then \(h^2M_\alpha(k)>1\) for every \(k>0\); consequently \(A_{d,h}\) decreases strictly from its vertical-plane value \(2h\kappa_{d-2}\) to its horizontal-plane value. If \(0<h^2<3/(d-2)\), strict monotonicity and both endpoint limits imply a unique solution \(k_*\in(0,1)\) of \(h^2M_\alpha(k_*)=1\). The derivative is positive on \((0,k_*)\) and negative on \((k_*,1)\), and the branch \(k\ge1\) is also strictly decreasing. Thus \(k_*\) gives the unique global maximizing inclination. Rotational symmetry and normal reversal characterize all central equality directions, and the angle conversion is \(\tan\theta_*=h/k_*\).

**5. Strict affine equality.** For an oblique direction, translating the hyperplane changes the graph into \(z=c-\tan\theta\,x_1\). Up to its constant Jacobian, its section volume is the integral of the strictly even-decreasing function \(t\mapsto\kappa_{d-2}(1-t^2)_+^\alpha\) over a fixed-length interval \([a-k,a+k]\), centered at \(a=c/\tan\theta\). For the maximizing oblique directions \(k=k_*<1\), this integral is strictly maximal at \(a=0\). For a vertical-plane maximizer, translating the plane to \(x_1=a\) yields the exactly smaller volume \(2h\kappa_{d-2}(1-a^2)^\alpha\) for every \(a\ne0\) with \(|a|<1\), and zero beyond. Brunn's inequality excludes every other affine direction from exceeding its central companion. All maximizing affine planes therefore pass through the origin.

**6. Elementary four-dimensional formula and onset.** For \(d=4\), \(\alpha=1\), \(J_1(k)=k-k^3/3\), and
\[
M_1(k)=\frac{2}{3(1-k^2)}.
\]
Solving \(h^2M_1(k_*)=1\) gives \(k_*^2=1-2h^2/3\). Substitution into the section profile yields the stated \((4\pi/3)(1+h^2/3)^{3/2}\) expression; at \(h_c=\sqrt{3/2}\), both formulas equal \(2\pi h_c\). Finally, Taylor expansion at \(k=0\) gives
\[
M_\alpha(k)=\frac{d-2}{3}\left(1+\frac{d+1}{5}k^2+O(k^4)\right).
\]
Insert \(h^2M_\alpha(k_*)=1\) and let \(h\uparrow h_c\) to obtain the displayed square-root transition law. This completes the proof for every integer \(d\ge4\).

## Verification

The standalone Python 3 file `check_sections.py` uses only the standard library. It independently integrates the geometric section profile via Simpson quadrature, numerically maximizes that profile by a golden-section search, tests dimensions \(4,5,6,9,20\) at five distinct height ratios around the critical height (520 comparisons), checks the exact four-dimensional expression, and checks the limiting transition location. Running `python3 check_sections.py` produced:

```text
EUCLIDEAN_CYLINDER_SECTION_CHECK_OK comparisons= 520
dimensions= (4, 5, 6, 9, 20) height_ratios= (0.3, 0.8, 0.99, 1, 1.1)
critical_halfheight_squared=3/(d-2); four_dimensional_profile_checked
```

These finite numerical tests are supplementary checks, not an infinite-dimensional proof; steps 1–6 provide the exact argument.

## Relationship to prior work

Dirksen's *Hyperplane Sections of Cylinders* [1, Theorem 1] supplies a general Fourier–Bessel expression for central sections of products of cubes and Euclidean balls. Its sharp Theorem 3 gives the **three-dimensional** \(1\)-interval/\(2\)-ball height transition; this case is deliberately excluded here. Theorem 2 of [1] assumes **more than one interval factor and more than one ball dimension**, and cannot by itself determine the present \(1\)-interval/\((d-1)\)-ball maximum for \(d\ge4\). Our elementary strip-volume identity agrees with [1]'s general integral formula, but the strict all-dimensional maximal-orientation phase law, exact threshold \(h_c(d)\), uniqueness, and explicit four-dimensional profile are additional statements not supplied there.

The 2013 study of Brzeziński [2] considers section-volume estimates for related products of Euclidean balls; the accessible abstract alone is insufficient to establish the absence of an equivalent result in its full text. Meyer's broader maximal-section paper [3] concerns general necessary geometry of extrema, rather than this explicit familywise sharp orientation law; only its accessible abstract was checked. A separate published result on the intersection body of a smooth prism [4] identifies polar axial facets and their regularity, not which central-section direction maximizes radial volume, nor the dimension-dependent threshold. The algebraic profile and statement-level implication were compared explicitly. Older general slicing literature can still pose a historical-priority risk; no claim of exhaustive historical exclusion or independent certification is made.

## Limitations

The theorem depends on a Euclidean ball cross-section, one interval factor, and a centered symmetric product. The high-dimensional threshold is for \(d\ge4\), not a newly claimed solution of the previously published \(d=3\) case. It does not classify volumes for arbitrary nonsymmetric bodies, multiple interval factors, or general noncentral sections except for the uniqueness of maximizing offsets. The implicit root defining the oblique maximum need not be elementary for other dimensions. The precise historical priority of the general-dimensional statement has not been independently established.

## References

[1] H. Dirksen, *Hyperplane Sections of Cylinders*, arXiv:1602.07854v1 (first public 2016-02-25), especially Theorems 1–3 and §3, https://arxiv.org/abs/1602.07854; published *Colloquium Mathematicum* 147 (2017), 145–164, https://doi.org/10.4064/cm6909-5-2016.

[2] P. Brzeziński, *Volume estimates for sections of certain convex bodies* (2013), abstract-level literature comparison; full-text implication unresolved.

[3] M. Meyer, *Maximal hyperplane sections of convex bodies* (1999), abstract-level literature comparison; full-text implication unresolved.

[4] *Polar axial facets and sharp contact regularity of intersection bodies of smooth prisms* (published open research record), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-polar-axial-facets-and-sharp-contact-regularity-of-intersection--8b975c5e3727, full RESULT.md inspected.
