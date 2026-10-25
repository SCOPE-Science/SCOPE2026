# Minimum silhouettes and exact angular shadow laws for odd regular bipyramids

## Finding

For every odd integer \(n\ge5\) and every height \(h>0\), the probability that the orthogonal planar shadow of a right regular \(n\)-gonal bipyramid has exactly four vertices under a uniform random viewing direction is
\[
\Pr(S_{n,h}=4)=\frac{2n}{\pi}\left[\arcsin q-\arcsin\!\left(q\cos\frac{\pi}{2n}\right)\right],\quad q=\frac{h}{\sqrt{h^2+\cos^2(\pi/n)}}.
\]
Every integer from \(4\) through \(n+2\) is attained with positive probability. At every fixed \(h>0\), as odd \(n\to\infty\),
\[
\Pr(S_{n,h}=4)=\frac{\pi h}{4n}+O_h(n^{-3}).
\]

For the pentagonal bipyramid, this combines with an exact classification to give all four shadow-size probabilities for arbitrary positive height. Put \(d=\pi/10\), \(c=\cos(\pi/5)\), \(q=h/\sqrt{h^2+c^2}\), \(g_j=\arcsin(q\sin(jd))\), and \(w=10/\pi\). Then
\[
\begin{aligned}
\Pr(S_{5,h}=4)&=w(g_5-g_4),\\
\Pr(S_{5,h}=5)&=1+w(2g_4-g_3-g_5-g_1),\\
\Pr(S_{5,h}=6)&=w(2g_1+2g_3-2g_2-g_4),\\
\Pr(S_{5,h}=7)&=w(2g_2-g_1-g_3).
\end{aligned}
\]
The seven-vertex probability in the last line was already available from the earlier maximum-shadow law; the distinct information here is the general minimum-shadow law, complete support, and the remaining probabilities. For the equilateral-face pentagonal bipyramid, \(h=(\sqrt5-1)/2\), these probabilities are approximately \(0.1173876921052801\), \(0.6069246263799069\), \(0.1877128511949624\), and \(0.0879748303198506\), respectively.

## Assumptions and scope

Take the convex hull of the \(n\) equatorial points \((\cos(2\pi j/n),\sin(2\pi j/n),0)\) for \(j=0,\ldots,n-1\) and the two poles \((0,0,\pm h)\). The base circumradius is normalized to one. The viewing direction is Haar-uniform on the unit sphere; the image is the orthogonal projection onto the perpendicular plane. Let \(S_{n,h}\) count vertices of the planar convex hull. Generic viewing directions are assumed in combinatorial sign classifications; nongeneric directions lie in a null set and do not affect probabilities. The theorem concerns odd \(n\ge5\) and strictly positive \(h\).

## Proof

**Contour-edge classification.** The outward normal of an upper or lower triangular facet over the equatorial edge with azimuthal midpoint \(\alpha_j=(2j+1)\pi/n\) has the same orientation as \((\cos\alpha_j,\sin\alpha_j,\pm c/h)\), where \(c=\cos(\pi/n)\). This follows by taking the cross product of two vectors along that facet. Reverse the unoriented viewing direction if necessary so that its last coordinate is positive, and write its horizontal direction as angle \(\phi\). For horizontal magnitude \(r\), define \(k=(c/h)|u_z|/r\) and \(\xi_j=\cos(\phi-\alpha_j)\). The corresponding upper and lower facets have dot-product signs given by \(\xi_j+k\) and \(\xi_j-k\). A silhouette edge occurs precisely when its two incident facet signs differ, except on the zero-measure boundaries. Each equatorial edge therefore contributes exactly one contour edge when \(|\xi_j|<k\). The upper polar fan and lower polar fan each contribute two contour edges if and only if at least one of their faces has each sign; these conditions are \(k<\max_j\xi_j\) and \(k<\max_j(-\xi_j)\). Consequently,
\[
S_{n,h}=\#\{j:|\xi_j|<k\}+2\mathbf1_{\{k<\max_j\xi_j\}}+2\mathbf1_{\{k<\max_j(-\xi_j)\}}.
\]
The two polar fans form cyclic contiguous sign blocks because \(\cos\) crosses a fixed level at most twice. This gives the two-versus-zero transition count, not one contour edge per incident triangle.

**Support and minimum.** For odd \(n\), the two largest among the generically distinct values \(|\xi_j|\) have opposite signs: their corresponding radial directions are respectively closest to \(\phi\) and to \(\phi+\pi\), with the nearest antipodal meshpoint strictly closer than the second nearest same-sign meshpoint. As \(k\) rises from zero to the smaller of these two maximal magnitudes, the number of magnitudes below \(k\) rises successively from zero to \(n-2\), while both polar indicators remain one. Thus each count \(4,5,\ldots,n+2\) occurs on a nonempty open set of directions. For the quadrilateral type, both indicators necessarily remain one and no magnitude is less than \(k\), equivalently \(k<\min_j|\xi_j|\). When a polar indicator disappears, at least \(n-1\) magnitudes have already been crossed, giving a count at least \(n\), so no further four-vertex intervals occur because \(n\ge5\).

The perpendiculars to the side-normal azimuths form a regular set modulo \(\pi\) with spacing \(\pi/n\). Hence their nearest azimuthal distance \(\delta\) is uniform in \([0,\pi/(2n)]\) and \(\min_j|\xi_j|=\sin\delta\). Independently, \(z=|u_z|\) is uniform on \([0,1]\). Writing \(a=h/c\), the inequality \(k<\sin\delta\) is equivalent to \(z<a\sin\delta/\sqrt{1+a^2\sin^2\delta}\). Therefore
\[
\Pr(S_{n,h}=4)=\frac{2n}{\pi}\int_0^{\pi/(2n)}\frac{a\sin\delta}{\sqrt{1+a^2\sin^2\delta}}\,d\delta.
\]
The substitution \(v=\cos\delta\) evaluates the integral exactly, using \(q=a/\sqrt{1+a^2}\), proving the displayed inverse-sine formula. Taylor's theorem at \(\delta=0\), together with \(c=1+O(n^{-2})\), proves \(\Pr(S_{n,h}=4)=\pi h/(4n)+O_h(n^{-3})\).

**Complete pentagonal law.** By fivefold rotational symmetry and reflection symmetry it suffices to take \(0<\phi<\pi/10\). The five magnitudes \(|\xi_j|\), descending, are \(a_1=\cos\phi\), \(a_2=\cos(\pi/5-\phi)\), \(a_3=\cos(\pi/5+\phi)\), \(a_4=\cos(2\pi/5-\phi)\), and \(a_5=\cos(2\pi/5+\phi)\). Their order is strict inside the interval, with the two largest of opposite sign. The count formula above gives the successive shadow sizes \(4,5,6,7,6,5\) on intervals cut at \(a_5,a_4,a_3,a_2,a_1\), with \(k\) increasing. For fixed \(\phi\), the Haar probability that \(k<a\) equals \(ha/\sqrt{c^2+h^2a^2}\). Its angular integral has primitive \(\arcsin(q\sin x)\) under the substitutions \(a=\cos x\). Integrating the six count intervals with the uniform reduced-azimuth density \(10/\pi\) and collecting terms gives the four displayed formulas. Direct algebra gives total probability one.

## Verification

The included self-contained Python program `verify_bipyramid_shadow.py` independently reconstructs three-dimensional vertices and all triangular facet signs, projects vertices to a uniformly oriented viewing plane, and computes a planar convex hull. It checks agreement of direct silhouettes with sign counts for several odd orders and heights; verifies the inverse-sine quadrilateral formula by independent spherical integration; checks the complete pentagonal distribution against direct Haar samples; and confirms the expected side count via exterior dihedral angles. Its finite experiments corroborate the proof rather than supplying an exhaustive infinite certificate.

## Relationship to prior work

The already established exact maximal-shadow probability for odd regular bipyramids gives \(\Pr(S_{n,h}=n+2)\), not the complementary minimum count or the complete pentagonal distribution. In particular its seven-vertex pentagonal formula is retained as prior work, not claimed to be discovered anew. Glisse and Lazard (2007) analyzed average silhouette complexity for polyhedra with geometrically constrained surfaces, and Glisse, Lazard, Michel, and Pouget (2016) treated random polytope silhouettes; neither provides the deterministic fixed-bipyramid angular distribution here. Black and Criado (2024) proved general expected-shadow bounds for fixed polytopes, not the displayed exact atoms. This comparison does not establish absolute historical priority.

## Limitations

The exact minimum formula and complete support theorem are restricted to odd regular bipyramids and Haar views. The remaining full distributions for odd \(n>5\) are not determined. The large-order estimate holds for fixed positive height and is not uniform for heights varying with \(n\). Existing specialists' literature may contain equivalent distribution formulas that were not recovered in the checked sources. Self-review is not independent validation.

## References

- Glisse and Lazard, *An Upper Bound on the Average Size of Silhouettes*, arXiv:cs/0702087, first posted 14 February 2007: https://arxiv.org/abs/cs/0702087.
- Glisse, Lazard, Michel, and Pouget, *Silhouette of a Random Polytope*, Journal of Computational Geometry 7(1), 2016: https://jocg.org/index.php/jocg/article/view/3009.
- Black and Criado, *Random Shadows of Fixed Polytopes*, arXiv:2406.06936, first posted 11 June 2024: https://arxiv.org/abs/2406.06936.
