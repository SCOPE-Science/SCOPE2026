# Cubic diameter tails and a two-contact transition on finite circular cones

## Finding

Let \(\mathcal C\) be the *closed lateral surface only* of a right circular cone of base radius \(b>0\), positive height \(h>0\), and slant length \(L=\sqrt{b^2+h^2}\). The base disk is not included. Choose \(X,Y\) independently from normalized surface-area measure on \(\mathcal C\), and let \(D\) be their shortest intrinsic surface distance. Put \(\kappa=b/L\in(0,1)\) and \(\alpha=\pi\kappa\).

**Theorem (diameter-contact and cubic-tail law).** The intrinsic diameter is
\[
M_\kappa=L\max\{1,2\sin(\alpha/2)\}.
\]
For every fixed \(0<\kappa<1\), as \(\varepsilon\downarrow0\),
\[
\Pr\{D>M_\kappa-\varepsilon\}=C(\kappa)\left(\frac{\varepsilon}{L}\right)^3+o(\varepsilon^3/L^3),
\]
with *three distinct and exact cases*
\[
C(\kappa)=
\begin{cases}
\dfrac{4\tan(\pi\kappa)}{3\pi\kappa},&0<\kappa<1/3,\\[5pt]
\dfrac{28}{\pi\sqrt3},&\kappa=1/3,\\[5pt]
\dfrac{2}{3\pi\kappa\sin^2(\pi\kappa/2)\cos(\pi\kappa/2)},&1/3<\kappa<1.
\end{cases}
\]
Below the threshold the diameter pairs join the apex to the rim; above it they join opposite rim points. At equality both geometrically disjoint families contribute to the tail coefficient. In physical dimensions the critical height-to-base-radius ratio is \(h/b=2\sqrt2\).

Additionally, at fixed \(L\) the distributions are strictly stochastically ordered by \(\kappa\): for \(0<\kappa_1<\kappa_2<1\) and \(0<t<M_{\kappa_2}\),
\[
\Pr\{D_{\kappa_1}\le t\}>\Pr\{D_{\kappa_2}\le t\}.
\]
Their squared-distance moment is
\[
\mathbb E[D^2]=L^2\left(1-\frac{8\sin(\pi\kappa)}{9\pi\kappa}\right).
\]

## Assumptions and scope

The surface is a compact two-dimensional metric cone, including its apex and rim but **excluding the filled-in base disk**. The two random points are independently sampled using the area element of the cone's lateral surface. Intrinsic distance means infimum of lengths of paths constrained to that surface, not the ambient Euclidean chord length. Parameters \(b,h\) are strictly positive. All endpoint asymptotics are for a *fixed* \(\kappa\in(0,1)\); they are not asserted uniform as \(\kappa\to0\), \(\kappa\to1\), or while \(\kappa\) moves with \(\varepsilon\).

## Proof

**1. Cone reduction and exact probability representation.** Unrolling the lateral surface produces a planar circular sector of radius \(L\) and total angle \(2\pi\kappa\), whose radial sides are identified. Equivalently, it is the truncated Euclidean metric cone over a circle of circumference \(2\pi\kappa\), with the standard cone distance formula [1]. If \(R,S\in[0,1]\) are the slant radii divided by \(L\), the area measure gives independent densities \(2r\,dr\) and \(2s\,ds\). Independent uniform azimuths yield a shorter unrolled angular separation \(\Delta\) uniform on \([0,\alpha]\), independent of \(R,S\). Since \(\alpha<\pi\), a straight segment in the smaller unrolled wedge realizes the shortest path, and
\[
\frac{D^2}{L^2}=R^2+S^2-2RS\cos\Delta.
\tag{1}
\]
There is no shorter apex route because the unfolded included angle is less than \(\pi\). This also supplies a reproducible exact integral for the entire distribution. For \(r,s>0\), define \(d_0=|r-s|\), \(d_1=\sqrt{r^2+s^2-2rs\cos\alpha}\), and
\[
G(t;r,s)=\begin{cases}
0,&t<d_0,\\
1,&t\ge d_1,\\
\alpha^{-1}\arccos\!\left((r^2+s^2-t^2)/(2rs)\right),&d_0\le t<d_1.
\end{cases}
\]
Then, for \(t\ge0\),
\[
\Pr\{D\le Lt\}=4\int_0^1\!\int_0^1 rs\,G(t;r,s)\,ds\,dr.
\tag{2}
\]
The null sets \(r=0\) and \(s=0\) do not affect this integral.

**2. Diameter and its competing contact families.** The squared expression in (1) is increasing in \(\Delta\in[0,\alpha]\). At \(\Delta=\alpha\) it is a strictly convex quadratic function of \((R,S)\) on the unit square. Its maximum therefore occurs at a corner. The corner values of \(D/L\) are \(0,1,1,2\sin(\alpha/2)\), respectively. The formula for \(M_\kappa\) follows. Strict convexity also excludes additional maximizing radius pairs: for \(\alpha<\pi/3\) these are precisely the two apex--rim ordered families; for \(\alpha>\pi/3\), precisely rim--rim pairs at \(\Delta=\alpha\); at equality both types maximize. The condition \(\alpha=\pi/3\) is equivalent to \(L=3b\) and hence \(h/b=2\sqrt2\).

**3. Upper tail when \(\alpha<\pi/3\).** Normalize \(L=1\) and write \(e=\varepsilon/L\). By compactness and strictness away from the maximizing sets, for small \(e\) the event \(D>1-e\) is contained in shrinking neighborhoods of \((R,S)=(0,1)\) and \((1,0)\). In the first such neighborhood set \(R=e u\) and \(S=1-e v\). Uniformly in \(\Delta\in[0,\alpha]\),
\[
\frac{1-D}{e}\longrightarrow v+u\cos\Delta.
\]
Here \(\cos\Delta\ge\cos\alpha>0\), so the event implies \(u,v\) remain uniformly bounded; rescaling and dominated convergence are valid. The joint law of \((R,S,\Delta)\) is \(4RS\,dR\,dS\,d\Delta/\alpha\). Accounting for both ordered apex--rim neighborhoods gives
\[
\lim_{e\downarrow0}e^{-3}\Pr\{D>1-e\}
=\frac8\alpha\int_0^\alpha\!\int_{\substack{u,v\ge0\\v+u\cos\delta<1}}u\,du\,dv\,d\delta
=\frac8{6\alpha}\int_0^\alpha\sec^2\delta\,d\delta
=\frac{4\tan\alpha}{3\alpha}.
\tag{3}
\]

**4. Upper tail when \(\alpha>\pi/3\).** Let \(m=2\sin(\alpha/2)>1\), \(a=\sin(\alpha/2)>0\), and \(c=\cos(\alpha/2)>0\). The only maximizing radial corner is \((1,1)\) with \(\Delta=\alpha\). Set \(R=1-eu\), \(S=1-ev\), and \(\Delta=\alpha-ew\). The first-order distance deficit is
\[
\frac{m-D}{e}\longrightarrow a(u+v)+cw.
\]
All three derivatives are strictly positive, justifying localization to \(u,v,w=O(1)\) by compactness. The density tends to \(4e^3/\alpha\), and the relevant three-dimensional simplex has volume \(1/(6a^2c)\). Hence
\[
\lim_{e\downarrow0}e^{-3}\Pr\{D>m-e\}
=\frac4\alpha\frac1{6a^2c}
=\frac2{3\alpha\sin^2(\alpha/2)\cos(\alpha/2)}.
\tag{4}
\]

**5. Critical coexistence.** At \(\alpha=\pi/3\), all three isolated radial maximizing corners remain separated, and equations (3) and (4) apply in their respective neighborhoods. Their limits add:
\[
\frac{4\sqrt3}{\pi}+\frac{16}{\pi\sqrt3}
=\frac{28}{\pi\sqrt3}.
\]
This yields the middle coefficient, which is *not* either one-sided limiting coefficient by itself.

**6. Order and moment.** Couple cone laws by using the same independent \(R,S\) and uniform \(U\in[0,1]\), taking \(\Delta=\pi\kappa U\). Since cosine strictly decreases on \((0,\pi)\), the resulting distance strictly increases almost surely with \(\kappa\). For any \(0<t<M_{\kappa_2}\), choose an *interior* triple \(0<R,S,U<1\) with \(D_{\kappa_2}>t\); such triples exist by continuity and the definition of the diameter. At that triple \(D_{\kappa_1}<D_{\kappa_2}\). Scale both radii by \(t/D_{\kappa_2}\), retaining the angle: the second distance then equals \(t\) while the first remains strictly below \(t\). Increasing the radial scaling slightly keeps both radii below one and yields \(D_{\kappa_1}<t<D_{\kappa_2}\) on an open set of positive probability. Thus strict stochastic inequality holds at every such \(t\). Finally, \(\mathbb E[R^2]=1/2\), \(\mathbb E[R]=2/3\), and \(\mathbb E[\cos\Delta]=\sin\alpha/\alpha\); averaging (1) proves the stated second moment.

## Verification

The local cubical volumes in (3) and (4) can be checked directly by elementary integration. An independent numerical routine in `checks/cone_tail_check.py` integrates one radial variable exactly, then uses Gauss--Legendre quadrature in the remaining radius and the angle. The observed ratios \(\Pr(D>M_\kappa-\varepsilon)/(\varepsilon/L)^3\) approach the derived constants for \(\kappa=0.2,1/3,0.6,0.85\), including at the coexistence point. Coupled Monte Carlo tests separately check stochastic ordering and the exact squared moment. See `checks/check_output.txt` for the actual finite numerical results. Finite quadrature and Monte Carlo are corroboration, not replacements for the proof.

## Relationship to prior work

Bacher and Sturm [1,2] give the general Euclidean metric-cone cosine distance and radial volume element; neither the cone metric nor the radial sampling law is claimed as new. Those known formulas give (1) after specializing to a circular link; the contribution here is the *evaluated rare-diameter probability*, its sharp cubic constants, the contact-family transition at \(\kappa=1/3\), and the additive critical amplitude. Existing literature on random Euclidean distances in plane polygons [3] uses a different underlying metric and sample space, so its formulas do not directly cover the lateral intrinsic metric. The derived moment and coupling are included as ancillary consequences, not represented as separate new discoveries.

## Limitations

The result does not concern the filled-in cone base, random points uniform in three-dimensional volume, ordinary ambient chord distance, or cones of zero height. The \(o(\varepsilon^3)\) remainder is pointwise in \(\kappa\) and not uniform near either degenerate endpoint or across a moving transition window. The classical cone-distance representation is established prior work; novelty of the specific cubic coefficients and critical coexistence remains subject to the possibility of less accessible historical treatments. No classification of noncircular cones is proved.

## References

[1] K. Bacher and K.-T. Sturm, *Ricci Bounds for Euclidean and Spherical Cones*, arXiv:1003.2114v1, first public 2010-03-10, https://arxiv.org/abs/1003.2114 . See §1.1 and Definition 2.1 for the cone cosine law and radial volume element.

[2] K. Bacher and K.-T. Sturm, *Ricci Bounds for Euclidean and Spherical Cones (revised/extended version)*, arXiv:1103.0197v1, first public 2011-03-01, https://arxiv.org/abs/1103.0197 . This is a later treatment of the same research, not an independent discovery.

[3] R. Pure, S. Durrani, F. Tong, and J. Pan, *Distance distribution between two random points in arbitrary polygons*, Math. Methods Appl. Sci. 45 (2022), 2760–2775, first online 2021-12-22, doi:10.1002/mma.7951. The planar-domain sampling setting is different.
