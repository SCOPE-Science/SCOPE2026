# The two pinched nonnormal fibers in an explicit degree-six del Pezzo fibration

## Finding
Let \(Q\subset\mathbf P^4_{\mathbf C}\) have homogeneous coordinates \([x_0:x_1:y_0:y_1:z]\) and equation \(x_0x_1+y_0y_1=z^2\). Set
\[
 C_x=Q\cap\{x_0=x_1=0\},\quad C_y=Q\cap\{y_0=y_1=0\},\quad X=\operatorname{Bl}_{C_x\sqcup C_y}Q.
\]
The two natural projections give degree-six del Pezzo fibrations \(\pi_x,\pi_y:X\to\mathbf P^1\). For **each** of them the complete singular-fiber locus consists of the two reduced points \([0:1]\) and \([1:0]\). Their fibers are reduced, irreducible, nonnormal surfaces. Each has normalization the Hirzebruch surface \(\mathbb F_2\), with one smooth rational double curve, ordinary two-branch normal crossings at its generic points, and exactly **two Whitney pinch points**.

The inverse image of the nonnormal double curve in \(\mathbb F_2\) is its negative section, of self-intersection \(-2\). Its restriction to that curve is the double cover \([a:b]\mapsto[a^2:b^2]\), branched at the two pinch points. Each singular fiber has complex topological Euler characteristic \(4\). Each other geometric fiber is a smooth degree-six del Pezzo surface of Euler characteristic \(6\), and \(e(X)=8\).

## Assumptions and scope
The base field is \(\mathbf C\). The total space is the **specific** smooth threefold obtained by blowing up the disjoint conics written above, not an arbitrary member of Mori–Mukai family No. 3-10. Fibers are scheme-theoretic geometric fibers. The phrase “ordinary two-branch normal crossing” is analytic/étale-local along the generic point of the double curve; it does not assert two globally separate components. The normalization map is not the identity over the double curve. The topological Euler characteristic uses ordinary topological Euler characteristic of compact complex algebraic surfaces.

## Proof
**1. General fibers and the only possible exceptional parameters.** By symmetry it suffices to study \(\pi_y=[y_0:y_1]\). The blowup of \(C_y\) resolves this rational pencil. For \([t:1]\) the corresponding hyperplane section of \(Q\) is the quadric in \(\mathbf P^3_{[x_0:x_1:y_1:z]}\)
\[
 Q_t:\quad x_0x_1+t y_1^2=z^2.
\]
For \(t\ne0\), it is a smooth quadric. The restriction of the \(C_x\)-blowup is the blowup at the two distinct points \(x_0=x_1=0,\ z=\pm\sqrt t\,y_1\), while \(C_y\) is a Cartier divisor in \(Q_t\), so blowing it up does not alter the fiber. Thus the fiber is a smooth degree-six del Pezzo surface, with Euler characteristic \(4+2=6\). In the second standard affine chart of the base the same argument exchanges \(y_0,y_1\). Therefore only \(0\) and \(\infty\) can be singular.

**2. The local surface at a special parameter.** At \([0:1]\), \(Q_0\) is the rank-three quadric cone \(x_0x_1=z^2\), with a unique vertex \(p=[0:0:0:1:0]\). Its intersection with \(C_x\) is the doubled vertex; \(C_y\subset Q_0\) is Cartier (it misses the vertex), so the \(C_y\)-blowup changes nothing on this fiber. Near \(p\), use \(y_1=1\), and eliminate \(y_0\) using \(y_0=z^2-x_0x_1\). Blowing up the ideal \((x_0,x_1)\) produces, on the chart \(x_0=u,\ x_1=uv\), the map
\[
 \pi_y=z^2-u^2v
\]
and the central-fiber equation
\[
 z^2=u^2v. \tag{1}
\]
On the second chart \(x_1=u',\ x_0=u'v'\) the same equation is \(z^2=u'^2v'\). Thus the fiber is reduced (equation (1) is squarefree) and locally irreducible, but nonnormal. Its singular locus in the first chart is precisely \(u=z=0\), and globally the two charts glue it into the exceptional \(\mathbf P^1\). Away from that exceptional curve, the blowup is an isomorphism to the smooth locus of the quadric cone. Therefore the displayed curve is the **entire** singular locus.

For \(v\ne0\) an analytic square root of \(v\) turns (1) into \((z-u\sqrt v)(z+u\sqrt v)=0\), a transverse double normal crossing. At \(v=0\), (1) is the standard Whitney pinch-point equation; the second chart contributes exactly one more, at \(v'=0\). These are distinct points of the exceptional \(\mathbf P^1\); no other singularity types occur.

**3. Explicit normalization and conductor.** In the first chart a normalization is
\[
 (u,w)\longmapsto (u,v=w^2,z=uw),
\]
with analogous coordinates \((u',w')\) on the opposite chart. On overlap,
\[
 w'=w^{-1},\qquad u'=uw^2.
\]
The last transition is the normal-bundle transition of degree \(-2\). More globally the minimal resolution \(\mathbb F_2\to Q_0\) has homogeneous local parametrization
\[
 [a:b],\ [\lambda:\mu]\longmapsto [x_0:x_1:y_1:z]=[\lambda a^2:\lambda b^2:\mu:\lambda ab],
\]
where the fiber homogeneous coordinates are interpreted in the standard twisted projective bundle. The rational blowup direction \([x_0:x_1]\) extends to \([a^2:b^2]\); hence the resolution lifts to a morphism from \(\mathbb F_2\) onto the fiber in \(X\). This map is an isomorphism off the exceptional curve and has finite fibers over that curve (the quadratic map on \(\mathbf P^1\)); being proper and quasi-finite, it is finite, so it is the normalization.

The exceptional section \(E\subset\mathbb F_2\) has \(E^2=-2\) and maps via \([a:b]\mapsto[a^2:b^2]\) onto the singular double curve. In local algebra, with \(A=\mathbf C[u,v,z]/(z^2-u^2v)\) and \(\overline A=\mathbf C[u,w]\) under \(z=uw,v=w^2\), the conductor is \((u,z)\subset A\) and its pullback is \((u)\subset\overline A\). The two branch points of this cover are precisely the two pinch points.

**4. Symmetry and Euler numbers.** The involution \(y_0\leftrightarrow y_1\) exchanges \(0\) and \(\infty\). The symmetry exchanging the \(x\)- and \(y\)-coordinate pairs exchanges the two fibrations. Thus the complete analysis holds for all four special fibers (two for each fibration).

Since normalization is bijective off the conductor, the additive Euler-characteristic relation is
\[
 e(S_{\rm special})=e(\mathbb F_2)-e(E)+e(\mathbf P^1)=4-2+2=4.
\]
Stratifying the base \(\mathbf P^1\) by \(\mathbf C^*\) and its two omitted points gives \(e(X)=e(\mathbf C^*)\,6+2\cdot4=8\). Independently, the smooth quadric threefold has Euler characteristic \(4\), and blowing up either smooth conic raises Euler characteristic by \(e(\mathbf P^1)=2\). Thus \(e(X)=4+2+2=8\), confirming the fiber computation.

## Verification
The accompanying standalone `verify.py` performs exact symbolic checks of the local equation, Jacobian singular-curve criterion, the normalization substitution, both blowup charts and their transition, and the Euler identities. The global normalization statement uses the finite birational geometry above; finite symbolic checks do **not** replace that argument. The pinched fibers are genuinely nonnormal even though their normalizations are smooth.

## Relationship to prior work
Gao's Example 7.15 (arXiv:2610.23024v1) specifies the blowup and analyzes smooth degree-six del Pezzo fibers and the quadratic parameter cover. In Proposition 7.16 it studies arithmetic exceptional loci supported on boundary divisors, but does not state the exact singular-fiber normalizations, conductor maps or pinch-point enumeration. Cheltsov–Thompson (arXiv:2309.12524v2) studies the K-moduli of threefolds in the same deformation family and conic-bundle geometry; the investigated relevant material does not identify the present special fiber calculation. Standard quadric-cone resolution and pinch-point theory are used, not presented as new.

## Limitations
The conclusion applies only to this explicit quadric and these two pencils. It does not classify singular fibers for arbitrary family No. 3-10 threefolds, determine stable reduction after base change, or prove an independent priority claim. The classification is a geometric calculation over \(\mathbf C\), not an assertion about integral arithmetic models or characteristic two.

## References
1. R. Gao, *The geometric exceptional set for Fano threefolds*, arXiv:2610.23024v1 (public October 16, 2026), Example 7.15 and Proposition 7.16. https://arxiv.org/html/2610.23024v1
2. I. Cheltsov and A. Thompson, *K-moduli of Fano threefolds in family 3.10*, arXiv:2309.12524v2. https://arxiv.org/abs/2309.12524
