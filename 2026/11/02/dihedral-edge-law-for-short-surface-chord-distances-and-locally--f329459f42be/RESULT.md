# Dihedral-edge law for short surface-chord distances and locally indistinguishable boxes

## Finding
Let \(P\subset\mathbb R^3\) be a full-dimensional convex polyhedron. Draw \(X,Y\) independently from normalized two-dimensional Hausdorff measure on its boundary, and put \(D=\|X-Y\|_2\). Write \(A=\mathcal H^2(\partial P)\), and for each polyhedral edge \(e\) let \(\ell_e>0\) and \(\theta_e\in(0,\pi)\) be its length and **interior** dihedral angle. Then
\[
A^2\Pr(D\le r)=\pi A r^2+\frac43\sum_e\ell_e\left(\frac{\pi-\theta_e}{\sin\theta_e}-1\right)r^3+O_P(r^4)\quad(r\downarrow0).
\]
The cubic coefficient is strictly positive and measures the geometric contribution of edges; it vanishes only in the formal flat-edge limit. This is a local exact asymptotic for a fixed polyhedron, not a claim of a uniform remainder over degenerating polyhedra.

For a rectangular box with side lengths \(a,b,c>0\), surface area \(A=2(ab+bc+ca)\), and \(h=\min(a,b,c)\), there is an **exact** local law for all \(r\in[0,h]\):
\[
A^2\Pr(D\le r)=\pi A r^2+\frac{8\pi-16}{3}(a+b+c)r^3+3(1-\pi)r^4.
\]
Consequently two rectangular boxes have the same CDF on a sufficiently small interval starting at zero if and only if their \(A\) and \(a+b+c\) agree. The noncongruent boxes with side-length triples \((1,2,3)\) and \((11/7,9/7,22/7)\) both have \(A=22\) and side sum \(6\), hence identical distance distributions at every \(r\in[0,1]\). Every box other than a cube additionally belongs locally to a continuous one-dimensional family of pairwise noncongruent boxes with identical short-distance CDFs.

## Assumptions and scope
A polyhedron has finitely many maximal planar polygonal faces and no nonmanifold boundary; convexity ensures that each edge is incident with exactly two distinct noncoplanar faces, with interior angle in \((0,\pi)\). The probability samples are independent **surface-area uniform** points on the boundary. Distances are ordinary Euclidean straight-line distances through ambient space, not geodesic distances along the surface. For boxes the sides are strictly positive; at the upper endpoint \(r=h\), the possible new opposite-face events have zero probability and the polynomial still applies.

## Proof
**1. Same-face pairs.** For one face \(Q\) of area \(B_Q\), perimeter \(L_Q\) and outward in-plane edge normals \(n_e\), the unnormalized measure of ordered pairs \((x,y)\in Q^2\) with \(\|x-y\|\le r\) is
\[
I_{QQ}(r)=\int_{\|w\|\le r}\operatorname{area}(Q\cap(Q+w))\,dw.
\]
The polygon translation covariogram has the direction-uniform local expansion
\[
\operatorname{area}(Q\cap(Q+w))=B_Q-\sum_{e\subset\partial Q}\ell_e\,(w\cdot n_e)_++O_Q(\|w\|^2).
\]
The error arises only within a fixed multiple of \(\|w\|\) of the finitely many vertices, so is bounded by a constant times \(\|w\|^2\). The disk integrals are \(\int_{\|w\|\le r}dw=\pi r^2\) and \(\int_{\|w\|\le r}(w\cdot n)_+dw=2r^3/3\). Therefore
\[
I_{QQ}(r)=\pi B_Qr^2-\tfrac23 L_Qr^3+O_Q(r^4).
\]
Summing over faces, \(\sum B_Q=A\) and \(\sum L_Q=2\sum_e\ell_e\), so the same-face cubic coefficient equals \(-4\sum_e\ell_e/3\).

**2. Face pairs sharing an edge.** Fix an edge of length \(\ell\) and interior dihedral angle \(\theta\). Away from its endpoints use orthonormal axial coordinate \(z\) and inward distances \(u,v\ge0\) along rays in the perpendicular section; the ray angle is \(\theta\). Points on the respective faces then have squared Euclidean separation
\[
(z-z')^2+u^2+v^2-2uv\cos\theta.
\]
The change of variables \(w=ue_1-ve_2\) has Jacobian \(\sin\theta\) and maps the first quadrant onto the planar cone of aperture \(\pi-\theta\). For one ordering of the two faces the coefficient of \(r^3\) per unit edge length is
\[
\frac2{\sin\theta}\int_{\substack{w\text{ in cone}\\\|w\|\le r}}\sqrt{r^2-\|w\|^2}\,dw
=\frac{2(\pi-\theta)}{3\sin\theta}r^3.
\]
The other ordering doubles it. Truncating longitudinal integration near the two endpoints changes the four-dimensional pair measure only by \(O_P(r^4)\), since all transverse variables are \(O_P(r)\). So this edge contributes \(4\ell(\pi-\theta)r^3/(3\sin\theta)+O_P(r^4)\).

**3. Remaining pairs.** Distinct faces meeting only at vertices give \(O_P(r^4)\): for distances \(\le r\) each point must lie within \(O_P(r)\) of a shared vertex, and each such face patch has area \(O_P(r^2)\). Disjoint closed nonincident faces have positive separation and contribute zero when \(r\) is sufficiently small. Combining steps 1–3 establishes the asymptotic. For \(x=\pi-\theta\in(0,\pi)\), \(x/\sin x>1\); hence each edge coefficient is positive.

**4. Exact box identity.** Every face is a rectangle with lengths \(u,v\). For \(r\le\min(u,v)\), its covariogram is exactly \((u-|w_1|)(v-|w_2|)\) throughout the integration disk, so
\[
I_{QQ}(r)=\pi uv\,r^2-\frac43(u+v)r^3+\frac12r^4.
\]
A pair of perpendicular adjacent rectangles of common edge length \(\ell\) and each width at least \(r\), with the two face orderings counted, contributes exactly
\[
2\int_{\substack{u,v\ge0\\u^2+v^2\le r^2}}\bigl[2\ell\sqrt{r^2-u^2-v^2}-(r^2-u^2-v^2)\bigr]du\,dv
=\frac{2\pi\ell}{3}r^3-\frac\pi4 r^4.
\]
This is exact for \(r\le h\), not asymptotic, because the longitudinal overlap length is \(\ell-|z-z'|\) and all face widths exceed the integration radius. Opposite faces cannot contribute at \(r<h\). Summing six rectangular same-face integrals and twelve adjacent-face integrals (four edges of each side length) yields \(\pi A r^2 +(8\pi-16)(a+b+c)r^3/3 +3(1-\pi)r^4\). Continuity extends it to \(r=h\).

**5. Inverse equivalence and continuum of collisions.** The leading coefficient of the normalized CDF is \(\pi/A\), so equality of germs determines \(A\). Given \(A\), its cubic coefficient \((8\pi-16)(a+b+c)/(3A^2)\), with \(8\pi-16>0\), determines the side sum. The converse follows from the exact polynomial. The displayed triples both have side sum \(6\) and pairwise-product sum \(11\), hence area \(22\). Their multisets differ, while both shortest sides are at least one. Lastly, at a noncubic triple the Jacobian of the map \((a,b,c)\mapsto(a+b+c,ab+bc+ca)\) has rank two: its gradient rows \((1,1,1)\) and \((b+c,a+c,a+b)\) are linearly independent. The implicit function theorem gives a local one-dimensional positive family with these invariants fixed. Quotienting by finite permutations still leaves continuously many noncongruent boxes; restricting to a common positive radius interval completes the claim.

## Verification
The proof is exact. Standalone `check_local.py` independently samples surface-uniform point pairs on four boxes using scrambled Sobol points and compares the exact CDF at multiple allowed radii; the absolute observed-vs-predicted deviations were less than \(1.6\times10^{-4}\) in those checks. It also evaluates the two noncongruent boxes' polynomial identity at eleven radii. Standalone `check_wedge.py` separately integrates the adjacent-face cone coefficient for four distinct interior angles and agrees within \(7\times10^{-7}\). Run `python check_local.py` and `python check_wedge.py` with NumPy/SciPy. Such finite numerical checks do not establish the general result; the analytic arguments above do.

## Relationship to prior work
The surface-point Euclidean distance histogram is the `D2` shape function investigated by Osada and colleagues (2001) and studied for engineering shapes by Rea and colleagues (2005). Rea and colleagues include sampled cube D2 curves and qualitative interpretation but, in their accessible full text, do not give the present general dihedral-edge coefficient, all-box local polynomial or inverse collision family. Mathai, Moschopoulos and Pederzoli (1999) derived detailed exact laws for a random point on each of two adjacent or opposite faces of a **unit cube**, with related formulas for random points in rectangles. Their pair-of-faces problems overlap and may subsume fixed cube special cases; those special cases are not claimed as new. The 1999 full text could not be retrieved for line-by-line comparison, so priority for any equivalent formula is unresolved. Ballani (2007) studies surface pair correlation in stationary **random Boolean sets** rather than fixed polyhedral chord histograms; Senesi and Lee (2015) study **volume-based** polyhedral scattering functions. A published result implying the general edge law or same-area/same-side-sum inverse collision would supersede the corresponding claims.

## Limitations
The expansion applies only for each fixed convex polyhedron as \(r\downarrow0\). Exact quartic behavior is established only for rectangular boxes and only up to the shortest side. The point-pair distribution is an ambient Euclidean chord distribution; it says nothing about intrinsic surface geodesics or volume-uniform sampling. Only local indistinguishability, not equality of full distance distributions, is established for the noncongruent boxes. Historical priority is qualified because the complete 1999 Mathai–Moschopoulos–Pederzoli paper and complete 2001 Osada paper were not obtained despite bounded attempts; independent literature review has not been performed.

## References
- R. Osada, T. Funkhouser, B. Chazelle, D. Dobkin, *Matching 3D Models with Shape Distributions*, Shape Modeling International (2001), DOI: `10.1109/SMA.2001.923386`.
- H. J. Rea, R. Sung, J. R. Corney, D. E. R. Clark, N. K. Taylor, *Interpreting Three-Dimensional Shape Distributions*, Proc. IMechE Part C **219** (2005), 553–566, DOI: `10.1243/095440605X31427` (first published 2005-06-01).
- A. M. Mathai, P. G. Moschopoulos, G. Pederzoli, *Distance between random points in a cube*, Statistica **59** (1999), 61–81, DOI: `10.6092/issn.1973-2201/1104`.
- J. Ballani, *Surface pair correlation function for stationary Boolean models*, Adv. Appl. Prob. (2007), DOI: `10.1239/aap/1175266466`.
- A. Senesi, B. Lee, *Scattering functions of polyhedra*, J. Appl. Cryst. **48** (2015), 565–577, DOI: `10.1107/S1600576715002964`.
