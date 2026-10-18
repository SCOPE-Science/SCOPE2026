# Exact mixed-volume lifting and sharp difference-body bounds for convex pyramids

## Finding
Let \(d\ge2\), let \(B\subset\mathbb R^{d-1}\) be any compact convex set with nonempty interior, and let
\[P=\operatorname{conv}\big((B,0),(p,h)\big)\subset\mathbb R^d,\qquad p\in\mathbb R^{d-1},\quad h>0.\]
Write \(m=d-1\), \(A=\operatorname{vol}_{m}(B)\), and
\[M_j=V_m(\underbrace{B,\ldots,B}_{m-j},\underbrace{-B,\ldots,-B}_{j}),\qquad 0\le j\le m,\]
where \(V_m\) is the standard mixed volume, normalized by \(V_m(K,\ldots,K)=\operatorname{vol}_m(K)\), and put \(M_{-1}=M_d=0\). For every \(s\ge0\),
\[\boxed{\frac{\operatorname{vol}_d(P+s(-P))}{\operatorname{vol}_d(P)}=\sum_{k=0}^{d}\binom dk\frac{M_{k-1}+M_k}{A}s^k.}\]
Thus the complete unbalanced difference-body volume polynomial of an arbitrarily oblique pyramid is determined by the reflected mixed-volume data of its base. In particular,
\[\boxed{\frac{V_d(P[d-k],(-P)[k])}{\operatorname{vol}_d(P)}=\frac{M_{k-1}+M_k}{A},\quad 1\le k\le d-1.}\]
The identity gives a **sharp pointwise lower envelope** for every \(s\ge0\):
\[\boxed{\frac{\operatorname{vol}_d(P+s(-P))}{\operatorname{vol}_d(P)}\ge 2(1+s)^d-1-s^d.}\]
For each \(s>0\), equality holds if and only if \(B\) is centrally symmetric (up to translation). At \(s=0\), both sides are \(1\) for every base.

For the ordinary difference body this specializes to the complete sharp spectrum
\[\boxed{2(2^d-1)\ \le\ \frac{\operatorname{vol}_d(P-P)}{\operatorname{vol}_d(P)}\ \le\ \binom{2d}{d}.}\]
Lower equality holds exactly for centrally symmetric bases, and upper equality exactly for simplex bases. For \(d\ge3\) **every** value in the closed interval is attained; when \(d=2\), both endpoints coincide at \(6\). The upper endpoint and its equality criterion are the classical Rogers–Shephard theorem, not claimed as new.

In dimension \(3\), put \(q=\operatorname{area}(B-B)/\operatorname{area}(B)\). Every convex pyramid over the plane has the explicit complete profile
\[\boxed{\frac{\operatorname{vol}_3(P+s(-P))}{\operatorname{vol}_3(P)}=1+\frac{3q}{2}(s+s^2)+s^3,\qquad 4\le q\le6.}\]
In particular, its normalized ordinary difference-body volume is exactly \(2+3q\), running sharply from \(14\) to \(20\), with equality bases as above. The polynomial applies to arbitrary convex (not necessarily polygonal) bases and apex offsets.

## Assumptions and scope
Convex bodies are full dimensional in their ambient affine spaces. The vertical height \(h\) is positive, but the horizontal apex location \(p\) is completely unrestricted. All volumes are Euclidean Lebesgue measures. Minkowski operations are \(X+Y=\{x+y:x\in X,y\in Y\}\), \(-X=\{-x:x\in X\}\), and \(sX=\{sx:x\in X\}\) for \(s\ge0\). The mixed volume \(V_d(P[d-k],(-P)[k])\) has \(d-k\) arguments equal to \(P\) and \(k\) equal to \(-P\). No smoothness or polyhedral assumptions on the base are required.

## Proof
**1. Exact horizontal slices.** Translate the pyramid so that \(0\in B\); this does not change any volume ratios because \(P+s(-P)\) merely translates. Parameterize the height of points in \(P\) by \(a\in[0,1]\), with horizontal slice \((1-a)B+ap\) at height \(ah\). A point in \(P+s(-P)\) at dimensionless height \(u=a-sb\), where \(a,b\in[0,1]\), belongs to the horizontal set
\[(1-a)B+s(1-b)(-B)+up.\]
For \(0\le u\le1\), the feasible minimum \(b=0\) (thus \(a=u\)) maximizes both nonnegative coefficients of \(B\) and \(-B\). As \(0\in B\), every other feasible slice lies inside that one. Hence the entire horizontal slice equals
\[(1-u)B+s(-B)+up.\]
For \(-s\le u\le0\), the minimum feasible \(b=-u/s\) (when \(s>0\)), with \(a=0\), gives the entire slice
\[B+(s+u)(-B)+up.\]
The case \(s=0\) is immediate by continuity. Translation by \(up\) disappears from volumes. Fubini therefore gives the *exact* integral identity
\[\operatorname{vol}_d(P+s(-P))=h\left(\int_0^1\operatorname{vol}_m((1-u)B+s(-B))\,du+\int_0^s\operatorname{vol}_m(B+t(-B))\,dt\right).\]
On the other hand, the pyramid volume is \(\operatorname{vol}_d(P)=hA/d\). This simultaneously proves independence of altitude and apex placement.

**2. Mixed-volume coefficients.** Minkowski's polynomial theorem states
\[\operatorname{vol}_m(\alpha B+\beta(-B))=\sum_{j=0}^{m}\binom mj M_j\alpha^{m-j}\beta^j\quad(\alpha,\beta\ge0).\]
Integrating each term in the two exact slices yields
\[\frac{\operatorname{vol}_d(P+s(-P))}{\operatorname{vol}_d(P)}=\frac{d}{A}\sum_{j=0}^{m}\binom mj M_j\left(\frac{s^j}{m-j+1}+\frac{s^{j+1}}{j+1}\right).\]
Use \(d\binom{d-1}{k}/(d-k)=\binom dk\) and \(d\binom{d-1}{k-1}/k=\binom dk\) to collect the coefficient at every power \(s^k\). This proves the boxed polynomial with \(M_{-1}=M_d=0\). Comparing with Minkowski's *dimension-\(d\)* volume polynomial identifies every stated mixed-volume quotient.

**3. Sharp lower bound and equality.** For \(m\ge1\), the Brunn–Minkowski inequality applied to \(B\) and \(-B\), both of volume \(A\), yields
\[\operatorname{vol}_m(\alpha B+\beta(-B))\ge A(\alpha+\beta)^m\quad(\alpha,\beta\ge0).\]
Inserting this inequality into the exact two-slice formula proves
\[\frac{\operatorname{vol}_d(P+s(-P))}{\operatorname{vol}_d(P)}\ge d\int_0^1(1-u+s)^{d-1}du+d\int_0^s(1+t)^{d-1}dt=2(1+s)^d-1-s^d.\]
If \(B\) is centrally symmetric, its reflection is a translate of itself; all Brunn–Minkowski inequalities used become equalities. Conversely for any \(s>0\), equality of integrals forces equality in Brunn–Minkowski for two positive coefficients on an interval. Equal-volume convex bodies \(B\) and \(-B\) can be homothetic only as translates; equivalently \(B\) is centrally symmetric. In dimension \(m=1\), every interval is centrally symmetric, so the equivalence remains valid.

**4. Sharp upper bound, range, and the three-dimensional case.** Rogers–Shephard's classical inequality in ambient dimension \(d\) gives \(\operatorname{vol}_d(P-P)\le\binom{2d}{d}\operatorname{vol}_d(P)\), with equality if and only if the pyramid is a simplex, equivalently its base is a simplex. Set \(s=1\) in the lower inequality for the other endpoint. The ratio depends continuously on the base in the Hausdorff metric. For \(d\ge3\), Minkowski-interpolate between any centrally symmetric convex base and a simplex base in \(\mathbb R^{d-1}\). Continuity and the two sharp endpoints give every intermediate ratio; there is no assertion of strict monotonicity along the interpolation. For \(d=2\) all bases are intervals and both endpoints equal \(6\).

When \(d=3\), the reflected planar mixed areas satisfy \(M_0=M_2=A\) and \(\operatorname{area}(B-B)=2A+2M_1\). Thus \((M_0+M_1)/A=(M_1+M_2)/A=q/2\); the complete cubic formula follows. The planar Brunn–Minkowski lower bound gives \(q\ge4\) with equality only for centrally symmetric bases; planar Rogers–Shephard gives \(q\le6\) with equality only for triangles. This completes all cases. \(\square\)

## Verification
The standalone file `check_pyramidal_difference.py` independently computes planar convex hull areas using rational shoelace arithmetic and convex-hull volumes in three and four dimensions with SciPy. It tests five unrelated polygonal bases with oblique apices, their entire cubic coefficient prediction at five nontrivial scale values, and four-dimensional tetrahedral and cubical bases at several scales. It also verifies sharp endpoint ratios \(14,20,30,70\). The observed maximum errors meet floating-point tolerances stated in the code. The computations are finite cross-checks; the proof above establishes the assertions for arbitrary dimensions and arbitrary convex bases.

Run: `python check_pyramidal_difference.py`. Requires Python 3, NumPy and SciPy.

## Relationship to prior work
The classical Rogers–Shephard upper inequality and equality cases (1957), the Brunn–Minkowski inequality, and Minkowski's mixed-volume polynomial are pre-existing results explicitly used in the proof. Artstein-Avidan, Einhorn, Florentin and Ostrover (first publicly available 9 August 2014) study general mixed-volume inequalities and the Godbersen conjecture. Artstein-Avidan and Putterman (2024) investigate unbalanced difference bodies. Kotrbatý and Mouamine (2026) establish stronger general mixed-volume upper bounds. Those upper estimates are not presented as novel here. The contribution under assessment is the exact dimension-reducing adjacent-mixed-volume lifting identity for *every convex pyramid*, its sharp base-symmetric lower envelope, and the resulting complete pyramid-family difference-volume spectrum. The inspected primary full texts did not state that specific lifting identity. Their general inequalities do not themselves specify the dependence on the lower-dimensional base's reflected mixed volumes.

## Limitations
Historical novelty has not been independently confirmed against every older convex-geometric monograph or Rogers–Shephard-era construction; rediscovery remains possible. No claim is made of a new general Rogers–Shephard inequality, a proof of any formerly open Godbersen inequality, or a full characterization of arbitrary non-pyramidal convex bodies. The exact lifting identity requires the geometric object to be a genuine pyramid, although the base can be arbitrary. Computational tests do not replace the analytic proof.

## References
1. C. A. Rogers and G. C. Shephard, *The difference body of a convex body*, Arch. Math. 8 (1957), 220–233. Classical difference-body inequality and equality cases; cited through inspected primary literature, rather than represented as newly established.
2. S. Artstein-Avidan, K. Einhorn, D. Y. Florentin, Y. Ostrover, *On Godbersen's Conjecture*, arXiv:1408.2135v1 (first public 2014-08-09). https://arxiv.org/abs/1408.2135
3. S. Artstein-Avidan and E. Putterman, *On unbalanced difference bodies and Godbersen's conjecture*, arXiv:2412.05308v1 (2024). https://arxiv.org/abs/2412.05308
4. J. Kotrbatý and M. A. Mouamine, *Godbersen's conjecture and the L_p–Rogers–Shephard inequality*, arXiv:2607.20387v1 (2026). https://arxiv.org/abs/2607.20387
