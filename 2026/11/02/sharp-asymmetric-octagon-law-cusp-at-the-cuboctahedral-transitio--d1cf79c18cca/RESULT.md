# Sharp asymmetric octagon-law cusp at the cuboctahedral transition

## Finding

For \(1<t<3\), form the centered cube–octahedron intersection
\[
K_t=[-1,1]^3\cap\{x\in\mathbb R^3:\lVert x\rVert_1\le t\}.
\]
If a central plane is chosen with uniform unoriented normal, let \(N_t\) count the sides of its generic section. The cuboctahedron \(K_2\) is **the unique member of this interpolation whose central sections are almost surely octagons**.

The strength of this rigidity is quantified by an asymmetric cusp. As \(\varepsilon\downarrow0\),
\[
\begin{aligned}
\Pr(N_{2-\varepsilon}=6)&=\frac{2\sqrt3}{\pi}\varepsilon+O(\varepsilon^2),\\
\Pr(N_{2-\varepsilon}=10)&=\frac{6-2\sqrt3}{\pi}\varepsilon+O(\varepsilon^2),\\
\Pr(N_{2-\varepsilon}=8)&=1-\frac6\pi\varepsilon+O(\varepsilon^2).
\end{aligned}
\]
As \(\delta\downarrow0\),
\[
\begin{aligned}
\Pr(N_{2+\delta}=6)&=\frac{4\sqrt3}{\pi}\delta+O(\delta^2),\\
\Pr(N_{2+\delta}=10)&=\frac{6\sqrt2-4\sqrt3}{\pi}\delta+O(\delta^2),\\
\Pr(N_{2+\delta}=4)&=O(\delta^2),\\
\Pr(N_{2+\delta}=8)&=1-\frac{6\sqrt2}{\pi}\delta+O(\delta^2).
\end{aligned}
\]
The two octagon-loss slopes are unequal: \(6/\pi\) on the octahedral side and \(6\sqrt2/\pi\) on the cubic side.

## Assumptions and scope

The parameter \(t\) is fixed in \((1,3)\). The plane passes through the center and has a Haar-uniform normal on the sphere modulo antipodes. Exceptional normals passing through vertices or aligned with facet boundaries have probability zero. The theorem concerns the limit in which \(t\) approaches \(2\), not the limiting sampling size of a finite point cloud. The cube and octahedron endpoints are excluded.

## Proof

**1. Exact facet-crossing count.** A generic central-plane section of a three-polytope has one edge for each facet whose relative interior intersects the plane. By sign symmetry, assume the ordered absolute coordinates of the normal are \(x>y>z>0\). For each of the six coordinate facets of the truncated cube, there is a contribution of two if the corresponding coordinate of the normal is smaller than the maximum absolute tangential normal dot product on that facet. There are also eight facets supported by signed \(\ell_1\) inequalities. We can count these by testing their vertex dot-product extrema against zero. More explicitly, for \(t<2\) the relevant signed-facet vertices are sign variants of the six permutations of \((1,t-1,0)\); for \(t>2\) they are sign variants of the three permutations of \((1,1,t-2)\). Each facet is crossed exactly when these extrema have opposite signs. Thus the count is entirely elementary and finite; the accompanying checker evaluates this exact rule for arbitrary generic normals.

**2. The octahedral-side chamber formula.** Put \(t=2-\varepsilon\) and \(r=1-\varepsilon\). Exact evaluation of the 14 facet crossing conditions gives
\[
N_{2-\varepsilon}=4+2\mathbf1\{y<rx\}+2\mathbf1\{z<rx\}+2\mathbf1\{z>ry\}.
\]
At \(\varepsilon=0\), the first two indicators are one and the last is zero, so the result is eight. For small positive \(\varepsilon\), the change to six is caused by the band \(x-y\le\varepsilon x\); the change to ten is caused by \(y-z<\varepsilon y\). Their intersection, together with the exceptional band \(x-z\le\varepsilon x\), has spherical area \(O(\varepsilon^2)\), since both successive coordinate gaps must then be small. Therefore the six- and ten-sided probabilities agree up to \(O(\varepsilon^2)\) with the respective two single-band probabilities.

**3. The cubic-side chamber formula.** Put \(t=2+\delta\), \(0<\delta\ll1\). Exactly four cube-facet crossings persist, and the remaining pair occurs if \(x<y+\delta z\). Of the four octahedral-facet crossings present at \(\delta=0\), one opposite pair disappears on the band \(y-z\le\delta x\). The other pair persists away from the regions where \(\delta x\ge y+z\) or \(x-z\le\delta y\). Each of those regions has spherical area \(O(\delta^2)\): the first is a cap of angular radius proportional to \(\delta\) around a coordinate axis, and the second forces both successive gaps to be at most proportional to \(\delta\). Consequently, outside an \(O(\delta^2)\)-probability set,
\[
N_{2+\delta}=8+2\mathbf1\{x-y<\delta z\}-2\mathbf1\{y-z\le\delta x\}.
\]
The two indicated bands overlap only in a region of spherical area \(O(\delta^2)\), proving in particular that quadrilateral sections have probability \(O(\delta^2)\).

**4. Exact first-order spherical band areas.** The ordered-positive-normal chamber is one of \(48\) congruent spherical chambers, each carrying total sphere probability equal to its spherical area divided by \(4\pi\). Thus the conversion factor from a one-chamber band area to its Haar probability is \(12/\pi\). Along the tie \(x=y\), parameterize the unit sphere by
\[
(x,y,z)=(\cos\theta/\sqrt2,\cos\theta/\sqrt2,\sin\theta),\quad0\le\theta\le\arctan(1/\sqrt2).
\]
The spherical gradient norm of \(x-y\) at this tie is \(\sqrt2\). The widths of \(x-y<\varepsilon x\) and \(x-y<\delta z\) are respectively \(\varepsilon\cos\theta/2\) and \(\delta\sin\theta/\sqrt2\) to first order. Their band areas are
\[
\frac{\varepsilon}{2\sqrt3}+O(\varepsilon^2),\qquad
\frac{1-\sqrt{2/3}}{\sqrt2}\delta+O(\delta^2).
\]
Along the tie \(y=z\), parameterize by
\[
(x,y,z)=(\cos\theta,\sin\theta/\sqrt2,\sin\theta/\sqrt2),\quad0\le\theta\le\arctan\sqrt2.
\]
The widths of \(y-z<\varepsilon y\) and \(y-z<\delta x\) are \(\varepsilon\sin\theta/2\) and \(\delta\cos\theta/\sqrt2\). Their band areas are
\[
\frac{1-1/\sqrt3}{2}\varepsilon+O(\varepsilon^2),\qquad
\frac{\delta}{\sqrt3}+O(\delta^2).
\]
Multiplying by \(12/\pi\) yields all four positive leading coefficients in the finding. Disjointness to first order and total probability one give both octagon coefficients and show their sharpness.

**5. Exact uniqueness of the octagon-only member.** At \(t=2\) every generic normal yields eight section sides by the facet test. For each \(t<2\), choosing \(x\) and \(y\) sufficiently close and \(z\) sufficiently small produces a non-octagonal (six-sided) section on an open normal set. For each \(t>2\), choosing \(x\) and \(y\) sufficiently close and \(z\) sufficiently small produces a ten-sided section on an open normal set. Hence no other parameter has octagon probability one.

## Verification

The accompanying standalone `verify.py` enumerates the actual facet vertices and checks their crossing conditions against the chamber formula; it also samples Haar normals and compares near-transition frequencies against the four derived slopes. These are finite arithmetic/Monte Carlo probes only; the proof rests on the exact facet analysis and spherical band integrations above. Run `python verify.py` with a standard Python 3 interpreter.

## Relationship to prior work

Brandenburg, De Loera and Meroni (2023) develop general slicing-chamber methods and classify combinatorial structures of polytope slices. Berlow, Brandenburg, Meroni and Shankar (2021) develop intersection-body chambers of polytopes. These sources motivate direction-dependent combinatorial slicing, but the inspected treatments do not state the present one-parameter cuboctahedral rigidity or its two unequal exact one-sided slopes. Prior quantitative research on the same cube–cross-polytope family concerns other invariants, such as volume, illumination and Mahler products. A generic chamber decomposition by itself does not give the Haar measure of the changing bands. The contribution here is the complete first-order probability transition at the rectification point, not the well-known definition of the cuboctahedron.

## Limitations

The theorem computes sharp local asymptotics near \(t=2\), not the complete probability law for every \(1<t<3\). It assumes exact central Haar plane sampling and the canonical cube–octahedron intersection coordinates. The remainder terms are uniform for sufficiently small one-sided parameter deviations; no exact coefficients of the second-order terms are established. Historical-priority verification cannot be exhaustive, and no independent audit has been performed.

## References

1. M.-C. Brandenburg, J. A. De Loera and C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239, publicly posted 2023-04-27, https://arxiv.org/abs/2304.14239.
2. K. Berlow, M.-C. Brandenburg, C. Meroni and I. Shankar, *Intersection Bodies of Polytopes*, arXiv:2110.05996, publicly posted 2021-10-12, https://arxiv.org/abs/2110.05996.
3. F. Göring and M. Winter, *The Edge-transitive Polytopes that are not Vertex-transitive*, arXiv:2005.14285, publicly posted 2020-05-28, https://arxiv.org/abs/2005.14285.
