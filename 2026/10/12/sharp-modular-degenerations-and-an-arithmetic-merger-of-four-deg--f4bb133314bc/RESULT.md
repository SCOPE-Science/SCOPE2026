# Sharp modular degenerations and an arithmetic merger of four degree-seven conic–line arrangements

## Finding

Let \(H_i\) be the four reduced degree-seven divisors over \(\mathbb Q\) constructed from three conics and one of four bitangent lines in Amram–Bannai–Shirane–Sinichkin–Tokunaga [1]. For their fixed integral equations below, the complete singular-support degeneration spectrum in every characteristic \(p\ge7\) is as follows. At all other primes, each divisor has ten geometric singular points: four ordinary nodes, four ordinary two-branch contact-two points (tacnodes), and two ordinary triple points.

| Prime | Arrangement | Number of geometric singular points | Distinguishing incidence |
| --- | --- | ---: | --- |
| \(7\) | \(H_1,H_4\) | 6 each | The two special fibres coincide; a four-branch point has pairwise contacts \((2,2,2,1,1,1)\). |
| \(7\) | \(H_2,H_3\) | 9 each | A triple point has pairwise contact orders \((2,1,1)\). |
| \(11\) | \(H_1,H_3,H_4\) | 9 each | A triple point has pairwise contact orders \((3,1,1)\). |
| \(11\) | \(H_2\) | 8 | The same nonordinary triple point, and an additional line–conic contact-two point. |
| \(109\) | \(H_1\) | 9 | Two transverse line–conic intersections merge into contact two. |
| \(109\) | \(H_2,H_3,H_4\) | 10 each | Unchanged incidence. |

The lists of exceptional primes at least seven are **exactly** \(\{7,11,109\}\) for \(H_1\) and \(\{7,11\}\) for each of \(H_2,H_3,H_4\). In particular, \(H_1\) and \(H_4\), which lie in distinct complex realization-space components and form a Zariski pair [1], become **the same reduced divisor** modulo seven, not merely combinatorially equivalent.

For good primes, the singular-point splitting fields are \(\mathbb Q(\sqrt{109})\), \(\mathbb Q(\sqrt{-11})\), \(\mathbb Q\), and \(\mathbb Q\), respectively. Accordingly, if \(N_i(p)\) is the number of rational points in the geometric singular support of \(H_i\), then at every prime \(p\ge7\) other than \(7,11,109\),
\[
(N_1(p),N_2(p),N_3(p),N_4(p))=
\left(9+\left(\frac{109}{p}\right),\;9+\left(\frac{-11}{p}\right),\;10,\;10\right).
\]
Each of the four resulting vectors occurs at a set of primes of natural density \(1/4\). These splitting-field statements are direct arithmetic consequences of elimination polynomials already implicit in [1, Section 4.2]; the **new classification asserted here** is the sharp modular degeneration and incidence merger, not the mere existence of those elimination equations.

## Assumptions and scope

Work in \(\mathbb P^2\) with homogeneous coordinates \([T:X:Z]\). Define the integral quadratic forms
\[
\begin{aligned}
Q_1&=XZ-T^2,\\
Q_2&=X^2-10TX+25XZ-36Z^2,\\
Q_3&=4XZ-5T^2+8TZ-12Z^2,
\end{aligned}
\]
and the four integral linear forms
\[
\begin{aligned}
\ell_1&=25X-160T+256Z, & \ell_2&=X,\\
\ell_3&=X-10T+25Z, & \ell_4&=25X-90T+81Z.
\end{aligned}
\]
Let \(H_i=V(Q_1Q_2Q_3\ell_i)\), reduced after passage to an algebraically closed field of characteristic \(p\ge7\). There is no assertion for characteristics two, three, or five, for arbitrary changes of integral models, or for positive-characteristic complement topology. Singular points mean distinct points of the geometric reduced support, not the length of a Jacobian scheme. An ordinary node has two transverse branches; contact order \(m\) refers to local intersection multiplicity of two smooth branches.

The rational-point formula concerns the singular support as a reduced finite set over the prime field. The density assertion excludes finitely many exceptional primes, which do not affect natural density.

## Proof

**Smooth components and fixed conic intersections.** In the coordinate order \((T,X,Z)\), the Hessian determinants of the three quadratic forms are \(2\), \(7200\), and \(160\). Thus each conic is nonsingular in characteristic \(p\ge7\); the three conics are distinct, and so is any degree-one component. On the chart \(Z=1\), write \(t=T/Z\), \(x=X/Z\). The conic \(Q_1=0\) is \(x=t^2\), and direct substitution gives
\[
\begin{aligned}
Q_2(t,t^2,1)&=(t+1)(t-2)(t-3)(t-6),\\
Q_3(t,t^2,1)&=-(t-2)(t-6),\\
\operatorname{Res}_{x}(Q_2,Q_3)&=(t-2)(t-6)(5t-8)^2.
\end{aligned}
\]
The last resultant uses the displayed integral normalization of \(Q_3\). Its double root corresponds to the point \((t,x)=(8/5,3)\). The only other intersection of \(Q_1\) and \(Q_3\) is \([0:1:0]\): in coordinates \(u=T/X\), \(v=Z/X\), \(Q_1=v-u^2\), and substituting \(v=u^2\) into \(Q_3\) gives \(-u^2(1-2u)(1-6u)\), proving contact exactly two. Bézout's theorem shows these lists exhaust all conic–conic intersections with multiplicity.

Except in characteristic seven or eleven, their union has precisely six singular points: transverse \(Q_1\)-\(Q_2\) intersections at \((t,t^2)\) for \(t=-1,3\); ordinary triple points at \((2,4)\), \((6,36)\); a contact-two point of \(Q_1,Q_3\) at \([0:1:0]\); and a contact-two point of \(Q_2,Q_3\) at \((8/5,3)\). The first resultant has a repeated root modulo primes at least seven only when \(-1=6\) in characteristic seven. The final resultant has a collision of its double root with \(t=6\) precisely in characteristic eleven: \(5\cdot6-8=22\). The simple root at \(t=2\) stays distinct in every characteristic at least seven.

**The moving line.** Each line is of the form \(x=a_it+b_i\) on \(Z=1\), with
\[
(a_i,b_i)=\left(\frac{32}{5},-\frac{256}{25}\right),(0,0),(10,-25),\left(\frac{18}{5},-\frac{81}{25}\right).
\]
Substitution gives \(Q_1(t,a_it+b_i,1)=-(t-a_i/2)^2\). The \(Q_2\)-restrictions are \(-36(20t-57)^2/625\), \(-36\), \(-36\), and \(-36(20t-43)^2/625\), respectively. For the constant restrictions, the corresponding line meets \(Q_2\) twice at infinity; all four restrictions certify tangency of exactly order two for \(p\ge7\).

The four \(Q_3\)-restrictions are, in order,
\[
-\frac{125t^2-840t+1324}{25},\qquad
-5t^2+8t-12,\qquad
-(t-4)(5t-28),\qquad
-\frac{(5t-12)(25t-52)}{25}.
\]
Their discriminants are \(16\cdot109/25\), \(-16\cdot11\), \(64\), and \(64/25\). Hence the line meets \(Q_3\) in two distinct transverse points for every \(p\ge7\), except \(p=109\) for \(i=1\) and \(p=11\) for \(i=2\), where the intersection is one contact-two point.

It remains to exclude unlisted collisions. At the four \(Q_1\)-\(Q_2\) points \(t=-1,2,3,6\), the values of the integral line forms \(\ell_i\) are the rows
\[
(441,36,1,196),\quad(1,4,9,36),\quad(36,9,4,1),\quad(196,1,36,441).
\]
At \((8/5,3)\) the four values are \((75,3,12,12)\), and at \([0:1:0]\) they are \((25,1,1,25)\). In all characteristics \(p\ge7\) other than seven these are nonzero. Thus no line passes through an intersection of two conics in good characteristic, and its two conic tangency points cannot coincide with the intersections on \(Q_3\). The conic intersections and the line-restriction discriminants exhaust all possible pairwise intersections by Bézout, proving both the universal ten-point classification and the precise list of exceptional primes.

**Exceptional local structures.** In characteristic seven, the \(Q_1\)-\(Q_2\) roots \(t=-1\) and \(t=6\) coincide with multiplicity two. At their common point \((6,36)\), \(Q_1,Q_2\) have contact order two and \(Q_3\) is transverse to both. Also
\[
\ell_1-\ell_4=-70T+175Z,
\]
so \(\ell_1=\ell_4\) modulo seven. Both lines touch \(Q_1,Q_2\) at \((6,36)\), and each cuts \(Q_3\) transversely there. Thus \(H_1\) and \(H_4\) have identical reductions and the single four-branch point with six pairwise intersection multiplicities \((2,2,2,1,1,1)\). The other line–\(Q_3\) point is a node; altogether these two arrangements have six geometric singular points. For \(H_2,H_3\), the line avoids that nonordinary triple point, yielding nine geometric singular points each.

In characteristic eleven the \(Q_2\)-\(Q_3\) double intersection at \(t=8/5\) collides with the simple intersection at \(t=6\), making a triple contact of order three between \(Q_2,Q_3\), while \(Q_1\) is transverse to both. This leaves five conic-union singular points, and four new line-involving points for \(H_1,H_3,H_4\); for \(H_2\), its two transverse \(Q_3\) intersections additionally merge into a single contact-two point, leaving eight geometric singular points. In characteristic \(109\), none of the conic–conic incidences changes, but the two line–\(Q_3\) points on \(H_1\) coalesce into a contact-two point, leaving nine geometric singular points. Every claimed local multiplicity is the corresponding root multiplicity of the displayed restrictions, in smooth local coordinates.

**Arithmetic singular points.** Over \(\mathbb Q\), the six points of the three-conic union are rational, and the two tangency points on the added line are rational. The remaining two intersections with \(Q_3\) are controlled by the quadratics displayed above. Their discriminants show that the minimal splitting fields for all singular points are, respectively, \(\mathbb Q(\sqrt{109})\), \(\mathbb Q(\sqrt{-11})\), and two copies of \(\mathbb Q\). The Legendre-symbol formula follows by Frobenius fixed-point counting. Since \(109\) and \(-11\) generate distinct quadratic extensions, their compositum is biquadratic; the four possible sign pairs occur for sets of primes of natural density \(1/4\) by Chebotarev's density theorem. At the exceptional primes \((7,11,109)\), direct reduction of these same root polynomials and the conic incidence list gives the rational singular-point vectors \((6,7,9,6)\), \((7,8,9,9)\), and \((9,8,10,10)\), respectively.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It checks the polynomial elimination identities, smoothness determinants, all four conic–line restrictions and discriminants, collision-guard evaluations, and the characteristic-seven line equality. It also independently enumerates the rational singular support over \(26\) prime fields from seven through \(109\), comparing each ordinary prime with the Frobenius formula and reporting exceptional counts. It completed with `VERIFY_OK`.

The exact factor identities, local root multiplicities, nonzero Hessian determinants and Bézout arguments prove the assertions for all primes in the stated range. The sampled prime-field enumerations are additional checks, not an infinite-prime proof.

## Relationship to prior work

Amram–Bannai–Shirane–Sinichkin–Tokunaga [1] supply the four component equations and prove the two-component complex realization-space theorem and the Zariski-pair distinction. In Section 4.2 they explicitly calculate the line–third-conic elimination polynomials; hence the associated quadratic splitting fields can already be deduced from that work. The present result does not re-present those equations, complex singularity types or topological distinctions as new. It adds the sharp, uniform prime-characteristic singular-incidence classification for their fixed integral model, including a collision of distinct complex Zariski-pair representatives in characteristic seven and the two different degeneration mechanisms in characteristics eleven and \(109\).

Bannai–Tokunaga–Yorisaki [2] study other degree-seven conic–line realization spaces and new complex Zariski pairs; they do not establish this characteristic-dependent classification for the four explicitly fixed arrangements in [1]. General complex-arrangement results such as [3] do not entail the exact residue-characteristic merger. No global statement on preservation of the complex topology in finite characteristic is made.

## Limitations

Only characteristics at least seven and the specified integral equations are addressed. The singular-support census is not a calculation of a Jacobian scheme, local Tjurina numbers, an étale fundamental group, or a good integral moduli model. The cross-component coincidence in characteristic seven does not imply that the complex Zariski pair ceases to be topologically distinct. Prime-density statements are consequences of the explicit quadratic reductions, not a new general result on Chebotarev distribution. Other integer presentations can have different exceptional primes. Unindexed modular computations of these examples might exist.

## References

[1] M. Amram, S. Bannai, T. Shirane, U. Sinichkin, H. Tokunaga, *The realization space of a certain conic line arrangement of degree 7 and a π1-equivalent Zariski pair*, arXiv:2307.01736v1 (first public 2023-07-04), especially pp. 2–3, 13–15, 17–18. Primary MSC2020: 14H30.

[2] S. Bannai, H. Tokunaga, E. Yorisaki, *The realization spaces of certain conic-line arrangements of degree 7*, arXiv:2409.05011v1 (2024-09-08), especially Introduction and Theorem 0.1.

[3] P. Pokora, T. Szemberg, *Conic-line arrangements in the complex projective plane*, Discrete & Computational Geometry 69 (2023), 1121–1138, doi:10.1007/s00454-022-00397-6.
