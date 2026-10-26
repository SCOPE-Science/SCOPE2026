# Unique rainfall reversal of two-zone curve-number aggregation bias

## Finding

Consider the Soil Conservation Service (SCS) curve-number event-runoff law with normalized curve number \(c\in(0,1]\), rainfall \(p\ge0\), and initial-abstraction fraction \(0<\lambda<1\):
\[
q_p(c)=\begin{cases}0,&p\le\lambda(1-c)/c,\\[3pt]
\dfrac{[p-\lambda(1-c)/c]^2}{p+(1-\lambda)(1-c)/c},&p>\lambda(1-c)/c.
\end{cases}
\]
The runoff and rainfall are in units of the standard potential-retention scale \(S_0\); in customary SCS units \(S_0=254\,\mathrm{mm}\) and \(c=\mathrm{CN}/100\).

**Theorem (one rainfall crossover).** For *every* \(0<x<y\le1\), area weight \(0<w<1\), and \(0<\lambda<1\), put \(z=wx+(1-w)y\) and
\[
\Delta(p)=wq_p(x)+(1-w)q_p(y)-q_p(z).
\]
There is a **unique** \(p_*>\lambda(1/y-1)\) such that
\[
\Delta(p)>0\quad(\lambda(1/y-1)<p<p_*),\qquad
\Delta(p_*)=0,\qquad
\Delta(p)<0\quad(p>p_*).
\]
For \(0\le p\le\lambda(1/y-1)\), both predictions are zero. The positive-root crossover is therefore nontrivial and globally unique, irrespective of the two curve numbers, their areas, and the abstraction fraction.

The threshold has a **sharp universal lower bound**
\[
p_*>\frac{1}{1+\lambda},\qquad
\inf_{x<y,\,0<w<1}p_*=\frac{1}{1+\lambda},
\]
whereas \(\sup p_*=+\infty\) over the same unrestricted parameter domain. These statements concern the mathematical model, not a physically feasible bound for real storms.

When both subareas produce runoff (\(p>\lambda(1/x-1)\)), the sign and the crossover are given by an **explicit cubic**. Set \(\gamma=1-\lambda\) and \(d_v(p)=vp+\gamma(1-v)\) for \(v\in\{x,y,z\}\). Then
\[
\Delta(p)=\frac{w(1-w)(y-x)^2}{\gamma xyz\,d_xd_yd_z}
\left[\lambda^2d_xd_yd_z-p^2(p-\gamma)xyz\right].
\]
The bracket has exactly one positive real zero; in the fully wet regime this zero is the crossing. If the crossing lies in the regime where the low-CN area is dry, its unique location instead solves the monotone scalar equation in the proof.

**Exact example (ordinary curve numbers).** At \(\lambda=1/5\), \(x=2/5\), \(y=1/2\), \(w=1/2\), the low-CN runoff onset is \(p=3/10\), and for \(p>3/10\)
\[
\Delta(p)=-\frac{13500p^3-12925p^2-1640p-528}{360(5p+4)(5p+6)(45p+44)}.
\]
The unique positive zero satisfies \(p_*\approx1.100145236813\), which corresponds to rainfall of about \(279.44\,\mathrm{mm}\) if \(S_0=254\,\mathrm{mm}\). In particular, \(\Delta(1)=59/117480>0\) and \(\Delta(2)=-13123/2701440<0\). A finite crossover can therefore lie above \(254\,\mathrm{mm}\), even for curve numbers 40 and 50.

## Assumptions and scope

Both subareas receive the *same* event-rainfall depth, obey the same fixed \(\lambda\), and are assigned area weights \(w\) and \(1-w\). Runoff from the two zones is area-averaged; the alternative prediction inserts the area-averaged CN into the same SCS equation. No travel-time routing, time-dependent moisture, measurement error, or spatially varying rainfall is considered. Curve numbers are strictly positive; the larger may equal 100. The theorem describes algebraic runoff predictions, not observed discharge or hydraulic peaks.

## Proof

**1. The runoff-onset stages.** Let \(s_v=(1-v)/v\) and \(a_v=\lambda s_v\). Since \(0<x<z<y\le1\), we have \(a_y<a_z<a_x\). For \(p\le a_y\), all three runoff responses vanish. For \(a_y<p\le a_z\), exactly the high-CN zone contributes and \(\Delta(p)=(1-w)q_p(y)>0\).

For \(a_z<p\le a_x\), the low-CN zone remains dry and
\[
\Delta(p)=q_p(y)\bigl[(1-w)-R(p)\bigr],\quad
R(p)=\frac{q_p(z)}{q_p(y)}
=\left(\frac{p-a_z}{p-a_y}\right)^2
\frac{p+\gamma s_y}{p+\gamma s_z}.
\]
Both factors in \(R\) are strictly increasing for \(p>a_z\): indeed \(a_z>a_y\) and \(s_z>s_y\). Thus \(R\) rises strictly from zero, and \(\Delta\) can cross zero **at most once** during this stage, necessarily from positive to negative.

**2. Exact fully wet factorization and root count.** If \(p>a_x\), write \(\beta=p-\gamma\). Algebraically,
\[
q_p(c)=\frac{[(p+\lambda)c-\lambda]^2}{c[\gamma+\beta c]},\qquad
\gamma+\beta c=cp+\gamma(1-c)>0.
\]
For \(\beta\ne0\), the partial fractions are
\[
q_p(c)=\frac{(p+\lambda)^2}{\beta}
+\frac{\lambda^2}{\gamma c}
-\frac{p^2}{\gamma\beta[\gamma+\beta c]}.
\]
The elementary weighted reciprocal identity
\[
\frac{w}{u}+\frac{1-w}{v}-\frac{1}{wu+(1-w)v}
=\frac{w(1-w)(u-v)^2}{uv[wu+(1-w)v]}
\]
then gives exactly the displayed factorization of \(\Delta\); the same identity holds at \(\beta=0\) by continuity.

For the cubic numerator \(B(p)=\lambda^2d_xd_yd_z-p^2(p-\gamma)xyz\), expand \(d_v=vp+\gamma(1-v)\). Its coefficient of \(p^3\) is \((\lambda^2-1)xyz<0\), its coefficient of \(p^2\) is
\[
\lambda^2\gamma[xy(1-z)+xz(1-y)+yz(1-x)]+\gamma xyz>0,
\]
and its lower-degree coefficients are nonnegative, with the coefficient of \(p\) strictly positive because \(x<y\). Therefore the descending coefficient sequence has **exactly one sign change**. By Descartes' rule of signs, \(B\) has at most one positive real root; since \(B(p)>0\) for sufficiently small \(p>0\) and \(B(p)<0\) for large \(p\), it has exactly one. Its sign switches only from positive to negative.

**3. Joining the stages.** The piecewise SCS runoff curve is continuous at each onset, so \(\Delta\) is continuous at \(a_z,a_x\). The first stage is strictly positive, the middle stage admits at most one positive-to-negative crossing, and the fully wet sign is controlled by a cubic with one positive-to-negative switch. Continuity precludes a second crossing at the boundary; because \(\Delta\) is negative at large \(p\), exactly one nontrivial crossover exists.

**4. Sharp lower bound.** In the active branch define \(s=(1-c)/c\) and \(d=p+\gamma s\). Two differentiations give
\[
\frac{\partial^2q_p(c)}{\partial c^2}
=\frac{2[\lambda^2d^3+p^2(\gamma-p)]}{\gamma c^3d^3}.
\]
For \(0<p\le(1+\lambda)^{-1}\), the numerator is increasing in \(s\ge0\), and at \(s=0\) is \(p^2\gamma[1-(1+\lambda)p]\ge0\). Across the runoff-onset boundary the function and its first derivative are continuous; hence \(q_p\) is convex on \((0,1]\), strictly so wherever it is positive apart from possible endpoints. Therefore \(\Delta(p)>0\) for any distinct \(x,y\) whenever runoff has begun and \(p\le(1+\lambda)^{-1}\). The lower bound is strict. Choosing \(x,y\uparrow1\) makes the unique inflection at \(c\approx1\) switch at \(p=(1+\lambda)^{-1}\); by continuity and the uniqueness already proved, the corresponding crossing tends to this bound, so the infimum is sharp.

**5. No universal upper bound.** Fix any large \(M>0\), let \(y=1\), take \(x>0\) sufficiently small, and then \(w<1\) sufficiently close to one so \(z=wx+(1-w)<\lambda/(M+\lambda)\). At \(p=M\), the low-CN and composite predictions vanish whereas the positive high-CN area contributes \((1-w)M>0\). Thus \(\Delta(M)>0\), implying \(p_*>M\). As \(M\) is arbitrary, the supremum is infinite.

## Verification

The file `verify.py` is a complete standalone Python 3 script using only the standard library. Run `python verify.py`. It checks the exact rational benchmark, the independent cubic-factorization formula at 2,400 pseudorandom parameter points, and 2,400 bisection-crossing configurations with 96,000 sign comparisons. The fixed seed is 20261024. The sign-change theorem, strict quantifiers and infimum/supremum statements rest on the symbolic proof, not on finite samples.

## Relationship to prior work

The event-runoff law and area-weighted/composite-CN procedures are established methods. Paudel, Nelson and Scharffenberg (2009), examined in its full nine-page public PDF, already analyze **the existence and practical significance of sign reversal** for distributed versus composite CN and report numerical crossing intervals. That qualitative reversal is explicitly not new. In particular, their equation-level model implies the present runoff law, but their numerical/range arguments do not establish the global two-zone *exactly-one-crossing theorem* for all positive CNs, weights, and \(\lambda\), or the exact cubic criterion and sharp absence of an unrestricted upper bound. Jena and coauthors (2012) compare distributed and composite estimates for hypothetical and field watersheds, reporting larger distributed runoff in their tested cases; their accessible abstract does not resolve the global exact two-zone classification. Bartlett and coauthors (2016) study a different probabilistic spatial-upscaling framework; its full text does not state the present exact theorem. The added mathematical point is a complete uniqueness and sharp-domain classification, not the familiar fact that nonlinear aggregation changes runoff.

## Limitations

One homogeneous rainfall depth, exactly two curve-number values, and area weighting are essential to the proof. The result does not claim one crossover for an arbitrary number of land-cover classes or under spatially nonuniform rainfall. For \(c\) near zero, extreme dimensionless rainfall may have no practical significance. The infinity statement describes model parameter space only. The original 2012 Jena paper was not fully available; its abstract and metadata were checked, leaving a historical-priority risk. Unidentified broader rational-aggregation theorems could cover parts of the algebra. There has been no physical calibration or empirical validation.

## References

- M. Paudel, E. J. Nelson, W. Scharffenberg, *Comparison of Lumped and Quasi-Distributed Clark Runoff Models Using the SCS Curve Number Equation*, Journal of Hydrologic Engineering **14** (2009), 1098–1106. DOI: 10.1061/(ASCE)HE.1943-5584.0000100. Public full-text copy: https://ce531.groups.et.byu.net/syllabus/notes/ModClarkCNPaper.pdf. Published online September 15, 2009.
- S. K. Jena, K. N. Tiwari, A. Pandey, S. K. Mishra, *RS and Geographical Information System–Based Evaluation of Distributed and Composite Curve Number Techniques*, Journal of Hydrologic Engineering **17** (2012), 1278–1286. DOI: 10.1061/(ASCE)HE.1943-5584.0000651. Full text not independently inspected.
- M. S. Bartlett, A. J. Parolari, J. J. McDonnell, A. Porporato, *Beyond the SCS-CN method: A theoretical framework for spatially lumped rainfall-runoff response*, Water Resources Research **52** (2016), 4608–4627. DOI: 10.1002/2015WR018439. Public full text: https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2015WR018439.
