# Sharp characteristic-five p-rank stratification of genus-five Humbert curves

## Finding

For every algebraically closed field \(k\) of characteristic \(5\), the \(5\)-rank of the Jacobian of a smooth genus-five Humbert curve is **exactly one of** \(3,4,5\), and every value occurs. The lower bound \(f(C)\ge3\) is sharp. There is exactly one unordered five-branch-point configuration, up to projective equivalence, attaining \(f(C)=3\):
\[
 B=\{\infty,0,1,u,v\},\qquad u^2-u+1=v^2-v+1=0,\quad u\ne v.
\]
Over characteristic \(5\) these two roots are distinct, and satisfy \(u+v=uv=1\). At this configuration precisely two of the five natural elliptic quotients are supersingular. No smooth genus-five Humbert curve in characteristic \(5\) has supersingular Jacobian.

## Assumptions and scope

Let \(k\) be algebraically closed of characteristic \(5\). A *generalized Fermat curve of type \((2,4)\)* here means a smooth connected projective curve \(C\) with a faithful action of \(G\cong(\mathbb Z/2\mathbb Z)^4\) such that the quotient \(C/G\cong\mathbb P^1\) has exactly five distinct tame branch points, each of ramification index \(2\); the five inertia classes have their unique relation that their sum is zero. This is the usual smooth diagonal-three-quadrics Humbert model. The characteristic is not \(2\), so the cover is tame. Riemann–Hurwitz yields \(2g(C)-2=16(-2)+5\cdot8=8\), hence \(g(C)=5\).

The \(5\)-rank \(f(C)\) is defined by \(\#J(C)[5](k)=5^{f(C)}\). The claim is geometric over \(k\), not a claim about rational-point counts over a fixed finite field, nor about singular reductions of non-smooth diagonal models.

## Proof

**1. Five elliptic double quotients and an isogeny.** Let \(B=\{b_1,\ldots,b_5\}\) be the branch set and \(g_i\in G\) its inertia elements, with \(\sum_i g_i=0\). For each \(i\), there is a character \(\chi_i:G\to\{\pm1\}\) equal to \(+1\) at \(g_i\) and \(-1\) at all four remaining generators; the assignment is compatible with the relation because it has four negative signs. The double quotient \(E_i=C/\ker(\chi_i)\to\mathbb P^1\) is branched at precisely \(B\setminus\{b_i\}\), so \(E_i\) has genus one. Write \(\pi_i:C\to E_i\), of degree \(8\).

The homomorphisms \(\Psi=\sum_i\pi_i^*:\prod_i J(E_i)\to J(C)\) and \(\Phi=(\pi_{i*})_i:J(C)\to\prod_i J(E_i)\) obey \(\pi_{i*}\pi_i^*=[8]\). For \(i\ne j\), select \(h\in\ker\chi_j\) with \(\chi_i(h)=-1\). On pullbacks from \(E_j\), \(h\) acts trivially; on \(J(E_i)\), its induced deck involution acts as \([-1]\). Thus \(\pi_{i*}\pi_j^*=-\pi_{i*}\pi_j^*\). Since homomorphisms between abelian varieties have no nonzero torsion, \(\pi_{i*}\pi_j^*=0\). Consequently \(\Phi\Psi=[8]\). The kernel of \(\Psi\) is finite, and since its source and target both have dimension \(5\), \(\Psi\) is an isogeny. Its kernel is annihilated by \(8\), hence of order prime to \(5\). This constructs the decomposition in characteristic \(5\) directly, without transferring a complex-analytic argument. In particular,
\[
 f(C)=\sum_{i=1}^{5}f(E_i)=5-\#\{i:E_i\text{ is supersingular}\}.
\]

**2. Legendre Hasse invariant.** For four distinct points, choose projective coordinates taking three to \(\infty,0,1\) and the fourth to \(t\notin\{0,1\}\). The double cover is the Legendre elliptic curve \(y^2=x(x-1)(x-t)\). Its Hasse invariant in characteristic \(5\) is proportional to the coefficient of \(x^4\) in \([x(x-1)(x-t)]^2\), namely
\[
 H(t)=t^2+4t+1=t^2-t+1.
\]
It is supersingular exactly when \(H(t)=0\). The discriminant of \(H\) is \(-3=2\), nonzero in characteristic \(5\). Its two roots \(u,v\) satisfy \(u+v=uv=1\).

**3. No three elliptic quotients can be supersingular.** Suppose two distinct four-point subsets of \(B\) yield supersingular elliptic quotients. They share exactly three branch points. Send the common three to \(\infty,0,1\), and call the remaining two \(u,v\). The two supersingularity conditions read \(H(u)=H(v)=0\). Since the points are distinct, \(u,v\) are precisely the two roots, hence \(u+v=uv=1\). For the three other four-subsets (deleting, respectively, \(1,0,\infty\)), the Hasse equations after multiplication by nonzero denominators are
\[
 \begin{aligned}
 Q_1&=u^2-uv+v^2,\\
 Q_0&=(u-1)^2-(u-1)(v-1)+(v-1)^2,\\
 Q_\infty&=v^2(u-1)^2-uv(u-1)(v-1)+u^2(v-1)^2.
 \end{aligned}
\]
Substituting \(u+v=uv=1\) gives \(Q_1=Q_0=Q_\infty=-2=3\ne0\) in \(k\). Thus *none* of the other three elliptic curves is supersingular. The number of supersingular factors is at most \(2\), proving \(f(C)\ge3\).

**4. Sharpness and full spectrum.** Choosing \(u,v\) as the two roots produces a smooth five-point branch configuration (all five points are distinct) with exactly two supersingular elliptic quotients, hence \(f(C)=3\). Conversely any \(f(C)=3\) configuration has two such quotients and normalizes to this same unordered branch set, proving its uniqueness up to \(\operatorname{PGL}_2(k)\).

For a rank-\(4\) example, let \(u\) be either root of \(H\) and take \(v=2\). The five Hasse numerators for the five omitted branch points are \(0,3,3-u,2-2u,2u+1\), up to the order convention. All four values after the first are nonzero because neither root equals \(1,2,3\). Hence there is exactly one supersingular quotient and \(f(C)=4\). For a rank-\(5\) example take \(u=2,v=3\): the five Hasse numerators are \(3,2,2,3,3\), all nonzero. Thus \(f(C)=5\). Together the rank spectrum is \(\{3,4,5\}\).

## Verification

The standalone Python 3 program `checker.py`, needing no external dependencies, implements \(\mathbb F_{25}=\mathbb F_5[t]/(t^2-2)\). It checks the two roots of \(H\), the exact five-numerator conditions at the rank-\(3\), rank-\(4\), and rank-\(5\) witnesses, and exhausts ordered valid pairs \((u,v)\in\mathbb F_{25}^2\) to confirm that no sampled configuration has more than two supersingular elliptic quotients. Run `python3 checker.py`. The universal bound is proved by the symbolic argument in Step 3, not by this finite enumeration.

## Relationship to prior work

Hidalgo–Kontogeorgis–Leyton-Álvarez–Paramantzoglou, arXiv:1409.3063 (first public version 2014-09-10), establish the general type \((k,n)\) description in arbitrary tame characteristic. Carvacho–Hidalgo–Quispe, arXiv:1507.02903 (first public version 2015-07-10), Section 5.1/Theorem 5.1, establish the five-elliptic isogeny for the complex family. The present characteristic-\(5\) proof of the isogeny is given explicitly; the claimed addition is the **sharp global rank bound, complete attainable spectrum, and unique minimal-rank branch configuration**, which are not consequences of the isogeny decomposition without the branch-point compatibility calculation.

Related later geometric descriptions (Auffarth–Lucchini Arteche–Rojas, arXiv:1905.12690; Karagiannis, DOI 10.1093/qmath/haae064) treat decompositions or canonical representations. No equivalent sharp characteristic-\(5\) rank stratification was found in the inspected material; coverage of every historical or later treatment is not guaranteed.

## Limitations

The assertion concerns the smooth type \((2,4)\) Humbert locus, not arbitrary smooth genus-five curves, singular boundary fibres, other primes, or the full Newton polygon of every nonordinary member. Existence and uniqueness of the minimum refer to geometric branch configurations over an algebraically closed field. The decomposition does not claim a polarization-preserving isomorphism. The theorem has only the documented self-review, not independent validation; historical overlap remains possible.

## References

- R. A. Hidalgo, A. Kontogeorgis, M. Leyton-Álvarez, P. Paramantzoglou, *Automorphisms of Generalized Fermat curves*, arXiv:1409.3063, version 1 dated 2014-09-10, https://arxiv.org/abs/1409.3063.
- M. Carvacho, R. A. Hidalgo, S. Quispe, *Isogenous decomposition of the Jacobian of generalized Fermat curves*, arXiv:1507.02903, version 1 dated 2015-07-10, especially §5.1 and Theorem 5.1, https://arxiv.org/html/1507.02903v1.
- R. Auffarth, G. Lucchini Arteche, A. Rojas, *A decomposition of the Jacobian of a Humbert-Edge curve*, arXiv:1905.12690, https://arxiv.org/abs/1905.12690.
- K. Karagiannis, *Representations on canonical models of generalized Fermat curves and their syzygies*, Quarterly Journal of Mathematics 76 (2025), 95–107, DOI:10.1093/qmath/haae064.
