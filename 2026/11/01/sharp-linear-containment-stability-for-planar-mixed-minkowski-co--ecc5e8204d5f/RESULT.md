# Sharp linear containment stability for planar mixed Minkowski–covering equality

## Finding
For a full-dimensional origin-symmetric convex body \(K\subset\mathbb R^2\) and a full-rank lattice \(\Lambda\), the planar quotient mixed inequality admits a **sharp geometric stability estimate**. Fix any shortest nonzero lattice vector \(v\), let \(L=\mathbb R v\), and form a canonical inscribed parallelogram \(P\) from the central chord in direction \(v\) and any point at maximum perpendicular height. Set
\[
\varepsilon=\frac{\lambda_1(K,\Lambda)\,\rho_L\,\operatorname{area}(K)}{\det\Lambda}-1,
\qquad\rho_L=\mu(\pi_{L^\perp}K,\pi_{L^\perp}\Lambda).
\]
Then \(\varepsilon\ge0\) and
\[
\boxed{P\subseteq K\subseteq(1+2\varepsilon)P.}
\]
Equality \(\varepsilon=0\) holds exactly when \(K=P\). The coefficient \(2\) and the linear order are optimal for arbitrarily small positive deficits, and the estimate holds for **every** permissible choice of the extreme point defining \(P\). The origin is the dilation center.

## Assumptions and scope
Throughout, \(K\subset\mathbb R^2\) is compact, convex, full-dimensional, and satisfies \(K=-K\). The lattice \(\Lambda\) has rank two and determinant \(\det\Lambda>0\). A nonzero \(v\in\Lambda\) is chosen so that its Minkowski gauge equals \(\lambda_1(K,\Lambda)\). Put \(u=v/\|v\|_2\), and let \(a>0\) be the maximum scalar such that \(au\in K\), equivalently \(K\cap L=[-au,au]\). Choose a perpendicular unit vector \(n\) and write \(h=\max_{x\in K}\langle x,n\rangle>0\); choose **any** \(z\in K\) with \(\langle z,n\rangle=h\). Define
\[
P=\operatorname{conv}\{-au,au,-z,z\},\qquad\operatorname{area}(P)=2ah.
\]
The vector \(v\) is primitive in \(\Lambda\): otherwise a smaller positive lattice multiple would violate shortestness. Its perpendicular projected lattice therefore has spacing \(\det\Lambda/\|v\|_2\). The projected convex interval is \([-h,h]\,n\). The one-dimensional covering radius \(\rho_L\) is the smallest dilation of this projected interval whose translates by the projected lattice cover the perpendicular line.

## Proof
**1. Identify the exact deficit.** Along \(L\), the gauge of \(v\) is \(\|v\|_2/a\), hence
\[
\lambda_1(K,\Lambda)=\frac{\|v\|_2}{a}.
\]
Primitivity gives the perpendicular lattice spacing \(d=\det\Lambda/\|v\|_2\). Since the projected body is a centrally symmetric interval of radius \(h\), \(\rho_L=d/(2h)\). Thus
\[
\lambda_1\rho_L\frac{\operatorname{area}(K)}{\det\Lambda}
=\frac{\operatorname{area}(K)}{2ah}
=\frac{\operatorname{area}(K)}{\operatorname{area}(P)}.
\]
In particular \(\varepsilon=\operatorname{area}(K)/\operatorname{area}(P)-1\). Since the four vertices \(\pm au,\pm z\) lie in \(K\), convexity gives \(P\subseteq K\), so \(\varepsilon\ge0\).

**2. The sharp geometric lemma.** Let \(D=\operatorname{conv}\{(1,0),(0,1),(-1,0),(0,-1)\}\). Suppose \(D\subseteq H=-H\) for a planar convex body \(H\), and \(\operatorname{area}(H)=2(1+\eta)\). For any \(q=(q_1,q_2)\in H\), put \(s=|q_1|+|q_2|\). If \(s\le1\), then \(q\in D\). Otherwise take the edge of \(D\) between the two signed coordinate vertices corresponding to the signs of \(q_1,q_2\). The triangle with this edge as base and \(q\) as apex has area \((s-1)/2\) and lies in \(H\setminus\operatorname{int}D\). Its centrally opposite triangle also lies in \(H\setminus\operatorname{int}D\); the two triangles have disjoint interiors. Consequently
\[
2(1+\eta)=\operatorname{area}(H)\ge 2+(s-1),
\qquad s\le1+2\eta.
\]
This holds for every \(q\in H\); hence \(H\subseteq(1+2\eta)D\). (Signed coordinate vertices can be chosen arbitrarily when a coordinate is zero; the supporting edge still has the asserted area.)

**3. Transfer by an affine-linear map.** Since \(au,z\) are linearly independent, an invertible linear map sends \(P\) to \(D\). It sends \(K\) to an origin-symmetric convex body containing \(D\), preserving the area ratio and the centered dilation relation. Applying step 2 with \(\eta=\varepsilon\) gives \(K\subseteq(1+2\varepsilon)P\). The same proof holds for every choice of \(z\) at height \(h\).

**4. Rigidity.** If \(\varepsilon=0\), then \(P\subseteq K\) and the two full-dimensional convex bodies have equal area, forcing \(K=P\). The converse is immediate. In particular, all zero-deficit bodies are parallelograms with the chosen shortest-vector direction as one diagonal; no Euclidean-rectangular assumption is made.

**5. Sharpness at arbitrarily small deficit.** For \(0<t\le1\), with \(\Lambda=\mathbb Z^2\), set
\[
K_t=\operatorname{conv}\{(-1,0),(0,-1),(1,0),(0,1),(1,t),(-1,-t)\}.
\]
These are full-dimensional centrally symmetric hexagons. They lie in \([-1,1]^2\), contain \((1,0)\), and no proper dilation \(sK_t\) with \(s<1\) contains a nonzero integer lattice point; thus \(\lambda_1(K_t,\mathbb Z^2)=1\). With \(v=(1,0)\), \(z=(0,1)\), we have \(a=h=1\), \(\rho_L=1/2\), and \(P=D\). Elementary polygon area computation gives \(\operatorname{area}(K_t)=2+t\), so \(\varepsilon=t/2\). Yet \((1,t)\in K_t\) has \(P\)-gauge \(1+t=1+2\varepsilon\). Thus no factor \(1+c\varepsilon\) with \(c<2\) holds uniformly, including in the limit \(t\downarrow0\).

## Verification
The standalone Python 3 script `verify.py` implements rational-coordinate convex hulls, exact polygon area, central chords, and the induced parallelogram gauge without floating-point arithmetic. It passes **2,589 exact rational polygon checks**: 2,500 symmetric random polygons and 89 members of the explicit sharpness family. This is a reproducibility check, not a substitute for steps 1–5. Execute with `python verify.py` in a Python 3 environment; no third-party packages are needed.

## Relationship to prior work
Williams, *Mixed Minkowski-Covering Inequalities for Convex Bodies and Lattices* (2026), proves the general quotient-form inequality, including the case \(n=2,r=1\), and constructs a distinct exact-equality family. The present statement retains its lattice-selected direction but adds **sharp global containment by a specified inscribed parallelogram, with rigidity and an optimal linear coefficient**. The baseline nonnegative deficit is not claimed as new.

The classical Rogers–Shephard section-projection theorem supplies the corresponding planar area inequality and equality characterization, as recalled in Alonso-Gutiérrez et al. (2017). Those qualitative results do not themselves state the optimal dilation \(1+2\varepsilon\) for **each** chosen extremal point. The elementary geometric lemma above supplies the quantitative step. Böröczky’s 2005 stability study treats difference bodies, radial-mean bodies and simplex extremizers, rather than this centered parallelogram and quotient-covering deficit. Other historical formulations could still overlap; independent priority review has not been performed.

## Limitations
The theorem is planar, assumes central symmetry, and treats the selected quotient of one shortest lattice-vector direction. The coefficient does not claim optimality for **every fixed body**, nor an unrestricted higher-dimensional stability estimate. The proof shows sharp global containment, not a full classification of all positive-deficit equality configurations. The exact-rational checks are finite. Earlier equivalently formulated convex-body stability results remain a possible historical overlap.

## References
1. Aled Williams, *Mixed Minkowski-Covering Inequalities for Convex Bodies and Lattices*, arXiv:2606.06291v1 (first public 2026-06-04), https://arxiv.org/html/2606.06291v1 .
2. D. Alonso-Gutiérrez, S. Artstein-Avidan, B. González Merino, C. H. Jiménez and R. Villa, *Rogers-Shephard and local Loomis-Whitney type inequalities*, arXiv:1706.01499v2, https://arxiv.org/html/1706.01499v2 .
3. C. A. Rogers and G. C. Shephard, *Some extremal problems for convex bodies*, Mathematika 5 (1958), 93–102, DOI:10.1112/S0025579300001418.
4. K. J. Böröczky, *The stability of the Rogers-Shephard inequality and of some related inequalities*, Advances in Mathematics (2005), DOI:10.1016/j.aim.2003.11.015 (author-hosted full text examined: https://www.renyi.hu/~carlos/rogerstab.pdf).
