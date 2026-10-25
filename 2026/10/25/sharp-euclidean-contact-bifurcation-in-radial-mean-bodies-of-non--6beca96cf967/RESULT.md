# Sharp Euclidean contact bifurcation in radial mean bodies of nonsquare rectangles

## Finding

Let \(K=[-a,a]\times[-b,b]\), with \(a>b>0\), let \(A=a/b>1\), and let \(R_pK\) denote the Gardner–Zhang radial mean body for any finite real \(p>-1\). Write \(r_p(K)\) and \(R_p^{\mathrm E}(K)\) for its centered Euclidean inradius and circumradius, respectively (the superscript distinguishes the radius from the mean-body operator). The exact smallest-radius directions are **always four strictly oblique directions**, whereas the largest-radius directions undergo a sharp phase change in both \(p\) and \(A\).

Define, for \(0\le q\le1\) and \(s,t>0\),
\[
\Phi_{s,t,p}(q)=2\sqrt{s^2+t^2q^2}\begin{cases}
\left(\frac{p+2-pq}{(p+1)(p+2)}\right)^{1/p},&p\ne0,\\
\exp(-1-q/2),&p=0.
\end{cases}
\]
Set
\[
q_{\min}(p,A)=\frac{p+2-\sqrt{(p+2)^2-4(p+1)A^{-2}}}{2(p+1)}\in(0,1).
\]
For every \(p>-1\) and \(A>1\),
\[
\boxed{r_p(K)=\Phi_{b,a,p}(q_{\min}(p,A)).}
\]
The four and only four contact directions of the centered inscribed Euclidean circle are
\[
\frac{(\pm aq_{\min}(p,A),\,\pm b)}{\sqrt{a^2q_{\min}(p,A)^2+b^2}}.
\]

For every \(-1<p\le2\), the enclosing radius is
\[
\boxed{R_p^{\mathrm E}(K)=\frac{2a}{(p+1)^{1/p}}},
\]
where the continuous \(p=0\) value is \(2a/e\); the only contact directions are the two long-side coordinate-axis directions \((\pm1,0)\).

For \(p>2\), put \(w_p(q)=1-pq/(p+2)\) and
\[
H_p(q)=\frac{q^2}{w_p(q)^{-2/p}-1},\qquad
E_p(q)=\frac{(2/p)(1-w_p(q))}{w_p(q)(1-w_p(q)^{2/p})}.
\]
There is exactly one \(q_*(p)\in(0,1)\) satisfying \(E_p(q_*(p))=2\), and the following threshold is finite, well defined and strictly larger than one:
\[
\boxed{A_*(p)=\sqrt{H_p(q_*(p))}>1.}
\]
For \(1<A<A_*(p)\), set
\[
q_{\max}(p,A)=\frac{p+2+\sqrt{(p+2)^2-4(p+1)A^2}}{2(p+1)}\in(0,1).
\]
Then
\[
\boxed{R_p^{\mathrm E}(K)=\Phi_{a,b,p}(q_{\max}(p,A))},
\]
with exactly four contact directions \((\pm a,\,\pm bq_{\max})/\sqrt{a^2+b^2q_{\max}^2}\).

At the unique transition \(A=A_*(p)\), the enclosing radius is \(2a/(p+1)^{1/p}\) and has **exactly six** contact directions: the two long axes and the four oblique directions with \(q=q_*(p)\). For \(A>A_*(p)\), only the two long axes remain, and the enclosing radius is again \(2a/(p+1)^{1/p}\). This is a discontinuous contact-direction transition: \(q_*(p)>0\) at equality.

For the exact quartic case \(p=4\), the threshold and transition angle parameter are radicals:
\[
\boxed{
q_*(4)=\frac{69-3\sqrt{17}}{64},\qquad
A_*(4)=\sqrt{\frac{963+459\sqrt{17}}{2048}}
=1.180800485353\ldots .}
\]
All assertions concern nonsquare rectangles \(a>b\); the square has additional symmetry and its known, different equality classes.

## Assumptions and scope

The radial mean body is defined by the exit-distance moment
\[
\rho_{R_pK}(u)^p=\frac{1}{|K|}\int_K\rho_{K-x}(u)^p\,dx,\quad p\ne0,
\]
where \(u\in S^1\) and \(\rho_{K-x}(u)=\sup\{t\ge0:x+tu\in K\}\). At \(p=0\) use the exponential of the average logarithm. The moments are finite precisely throughout the range needed here, \(p>-1\). By the convexity theorem for radial mean bodies, these are genuine centrally symmetric convex bodies also for negative \(p\). All Euclidean circles and radii are centered at the origin; by central symmetry the centered inradius is also the unrestricted maximal inscribed-circle radius (although an incenter need not generally be unique).

The claimed contact directions are all **unit** directions of radial equality with the centered inscribed or enclosing Euclidean circle. Independent \(\pm\) symbols produce four directions. Parameters \(p=0\) are always interpreted by continuous limits. No claim of an all-dimensional or nonrectangular optimization is made.

## Proof

**1. Exact reduction to two one-variable profiles.** If \(u=(u_1,u_2)\in S^1\), write \(h_1=|u_1|/(2a)\), \(h_2=|u_2|/(2b)\), and \(T=1/\max(h_1,h_2)\). The normalized covariogram satisfies
\[
\frac{|K\cap(K+tu)|}{|K|}=(1-h_1t)_+(1-h_2t)_+.
\]
The exit-distance random variable \(X_u=\rho_{K-Z}(u)\), for uniform \(Z\in K\), therefore has survival probability given by this covariogram, and its density on \([0,T]\) is \(h_1+h_2-2h_1h_2t\). Put \(q=\min(h_1,h_2)/\max(h_1,h_2)\) and \(z=t/T\). The rescaled density is \(1+q-2qz\), so for every \(p>-1\), \(p\ne0\),
\[
\mathbb E[X_u^p]=T^p\int_0^1z^p(1+q-2qz)\,dz
=T^p\frac{p+2-pq}{(p+1)(p+2)}.
\]
The logarithmic moment is \(\mathbb E[\log X_u]=\log T-1-q/2\). If \(h_1\ge h_2\), then \(T=2\sqrt{a^2+b^2q^2}\) and \(\rho_{R_pK}(u)=\Phi_{a,b,p}(q)\); if \(h_2\ge h_1\), then \(T=2\sqrt{b^2+a^2q^2}\) and \(\rho_{R_pK}(u)=\Phi_{b,a,p}(q)\). Both profiles traverse \(0\le q\le1\).

**2. Strict branch dominance.** For every \(0\le q<1\),
\[
\Phi_{a,b,p}(q)>\Phi_{b,a,p}(q),
\]
because \(a^2+b^2q^2>b^2+a^2q^2\), while the positive moment factor is identical. The profiles agree at \(q=1\). Consequently the global minimum comes from the second profile and the global maximum from the first; equality at their common endpoint causes no additional extremum whenever each strict optimum is attained elsewhere.

**3. The inradius has four oblique contacts for all \(p>-1\).** Differentiating the logarithm of either profile (with the \(p=0\) limit included) yields
\[
\frac{d}{dq}\log\Phi_{s,t,p}(q)
=\frac{t^2\bigl((p+2)q-(p+1)q^2\bigr)-s^2}
{(s^2+t^2q^2)(p+2-pq)}.
\]
The denominator is strictly positive. For \((s,t)=(b,a)\), the derivative numerator is negative at \(q=0\) and positive at \(q=1\). The concave quadratic crosses zero exactly once in \((0,1)\), at \(q=q_{\min}(p,A)\), and its second root lies above one. Thus this is the unique reduced minimizer and is strictly interior, giving exactly the four stated contact directions. Together with Step 2 this proves the global inradius classification.

**4. The axis dominates when \(p\le2\).** For \(p\le2\), the square profile \(\Phi_{1,1,p}(q)\) is maximized at \(q=0\) (with an additional endpoint tie at \(q=1\) when \(p=2\)). This follows directly from the derivative in Step 3: when \(p\le0\) the derivative is nonpositive; when \(0<p\le2\) its only interior critical point is a minimum, and the endpoint ratio
\[
\log\frac{\Phi_{1,1,p}(1)}{\Phi_{1,1,p}(0)}
=\frac{\log2}{2}-\frac{\log(1+p/2)}{p}
\]
is nonpositive, including its continuous limit at zero, since \(\log(1+x)/x\) decreases for \(x>-1\), \(x\ne0\). For \(a>b\) and \(q>0\), the strict bound \(\Phi_{a,b,p}(q)<a\Phi_{1,1,p}(q)\le a\Phi_{1,1,p}(0)=\Phi_{a,b,p}(0)\) proves unique axial maximizers. The formula for their radius follows from Step 1.

**5. A single sharp aspect-ratio threshold for \(p>2\).** In the long-coordinate-dominated branch,
\[
\frac{\Phi_{a,b,p}(q)}{\Phi_{a,b,p}(0)}
=\sqrt{1+\frac{q^2}{A^2}}\,w_p(q)^{1/p}.
\]
For \(0<q\le1\), this ratio is greater than one if and only if \(A^2<H_p(q)\). To locate the best competitor, write \(\alpha=2/p\in(0,1)\), \(w=1-pq/(p+2)\), and \(B(q)=w^{-\alpha}-1\). The logarithmic elasticity \(E(q)=qB'(q)/B(q)\) is precisely \(E_p(q)\), and
\[
\frac{H_p'(q)}{H_p(q)}=\frac{2-E_p(q)}{q}.
\]
The function \(E_p\) increases strictly: its logarithmic derivative with respect to \(w\) is negative exactly when
\[
w^{-\alpha}>1+\alpha(1-w),
\]
which holds strictly by convexity of \(w\mapsto w^{-\alpha}\) and its tangent at \(w=1\). Since \(w\) decreases with \(q\), \(E_p\) increases. Its limit at \(q\downarrow0\) equals one. At \(q=1\),
\[
E_p(1)=\frac{1}{1-(2/(p+2))^{2/p}}>2
\]
for \(p>2\): equivalently \(\log(1+p/2)/p<\log2/2\). Therefore \(E_p(q)=2\) has a unique solution \(q_*(p)\in(0,1)\), and \(H_p\) has a strict, unique interior maximum there. Moreover \(H_p(1)>1\), since the square's diagonal radius exceeds its axial radius for \(p>2\), as verified by the same endpoint ratio; hence \(A_*(p)>1\).

If \(A>A_*(p)\), the long axis is strictly better than all \(q>0\); if \(A=A_*(p)\), it ties exactly one oblique parameter \(q=q_*\); and if \(1<A<A_*(p)\), some oblique parameter strictly improves the axis. In the last regime, differentiating as in Step 3 shows that the only interior local maximum is the larger root of the quadratic \((p+2)q-(p+1)q^2=A^2\), namely \(q_{\max}(p,A)\). It belongs to \((0,1)\) because \(1<A<A_*\) forces the two roots to be real and \(q=1\) has derivative sign \(b^2-a^2<0\). That root is thus the unique reduced global maximum. At equality it coincides with \(q_*\). This proves all contact numbers and the discontinuous angular switch.

**6. Closed quartic radicals.** For \(p=4\), substitute \(z=\sqrt{1-2q/3}\) into the threshold envelope:
\[
H_4(q)=\frac94z(1-z)(1+z)^2.
\]
The derivative in \(z\) is proportional to \(-(z+1)(4z^2-z-1)\). On \(z\in[1/\sqrt3,1]\), its unique interior maximizer is \(z=(1+\sqrt{17})/8\). Substituting back gives \(q_*(4)=(69-3\sqrt{17})/64\) and \(H_4(q_*)=(963+459\sqrt{17})/2048\), proving the exact radical transition.

## Verification

The included standalone standard-library program `verify.py` recomputes the exit-distance moments from an independent density quadrature, compares the exact candidate extrema against dense angle sweeps for negative, zero, and positive values of \(p\), and verifies the quartic radicals with 60-digit decimal arithmetic. Run `python3 verify.py`. Successful output is `RADIAL_RECTANGLE_CHECKS_OK`. Finite grids and quadratures are consistency checks; the preceding derivative, elasticity and endpoint arguments prove the assertions for every real parameter in the stated ranges.

## Relationship to prior work

Gardner and Zhang introduced the radial mean bodies and their affine covariance. Langharst's 2026 proof of convexity for all \(p>-1\) justifies treating their negative-parameter members as centrally symmetric convex bodies. Langharst, Manui and Zvavitch give the cube's covariogram integral and axial/diagonal radial values (Proposition 34). The published result *A four-to-four contact transition in radial mean bodies of the square* completely classifies the **square** angular extrema, and those square equalities are expressly excluded from the present claim. Affine covariance of that square profile indeed determines every pointwise rectangular radial value, so deriving the profile in Step 1 is not in itself a novelty claim. The new result is the **two-parameter Euclidean optimization** after anisotropic affine distortion: an exact strict aspect-ratio threshold, six-way coexistence at it, uniqueness of all oblique contacts, and an exact quartic radical. Neither affine covariance nor the square's Euclidean extremizers alone supply that Euclidean contact classification because Euclidean circles are not preserved by anisotropic affine maps. Earlier work on dual quermassintegral inequalities treats integral quantities rather than the orientation-specific Euclidean extremizers here.

## Limitations

The result is specifically about axis-aligned nonsquare rectangles and the ordinary Euclidean metric (rotation or uniform scaling changes nothing). It does not provide a general phase classification for nonrectangular convex bodies, arbitrary norms, or dimensions above two. The radial formula and square extrema are known, and are not presented as new. A fully historical uniqueness certification is not possible: the original Gardner–Zhang paper was not accessible in full and older shape-specific extremization literature may exist. This does not affect the analytic proof but leaves a bounded priority risk. No independent audit has been performed.

## References

1. D. Langharst, *Convexity of Radial Mean Bodies via an Extension of Ball's Bodies*, arXiv:2603.14134, first posted 14 March 2026; Theorem 3 and Proposition 10, https://arxiv.org/abs/2603.14134.
2. D. Langharst, A. Manui, A. Zvavitch, *On the Fourier Mean Bodies of a Convex Body*, arXiv:2601.20117, first posted 27 January 2026, Section 3.3, Proposition 34, https://arxiv.org/html/2601.20117.
3. R. J. Gardner and G. Zhang, *Affine inequalities and radial mean bodies*, American Journal of Mathematics 120 (1998), 505–528, DOI 10.1353/ajm.1998.0021.
4. W. Wang and T. Zhang, *Inequalities for dual quermassintegrals of the radial p-th mean bodies*, Journal of Inequalities and Applications 2014, article 252, https://doi.org/10.1186/1029-242X-2014-252.
5. *A four-to-four contact transition in radial mean bodies of the square* (publicly available mathematical result, 2026); the square-only equality classification is used as an overlap comparator, not as a contribution of the present theorem.
