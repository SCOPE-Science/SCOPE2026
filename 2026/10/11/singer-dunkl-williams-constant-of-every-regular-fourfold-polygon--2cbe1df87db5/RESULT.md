# Singer–Dunkl–Williams constant of every regular fourfold polygonal Banach plane
## Finding
For every integer \(n\ge1\), let \(X_{4n}\) be the real two-dimensional Banach space whose unit ball is a Euclidean regular \(4n\)-gon, up to linear isometry. Then the Dunkl--Williams constant related to Singer orthogonality satisfies
\[
DW_S(X_{4n})
=
1+\sec\!\left(\frac{\pi}{4n}\right).
\]
Equivalently, for
\[
D(X)
=
\inf\left\{
\inf_{\lambda\in\mathbb R}\|x+\lambda y\|:
x,y\in S_X,\ x\perp_I y
\right\},
\]
one has
\[
D(X_{4n})
=
\frac{2\cos(\pi/(4n))}
{1+\cos(\pi/(4n))}.
\]

Thus the square gives
\[
DW_S(X_4)=1+\sqrt2,
\]
while
\[
DW_S(X_{4n})\downarrow2
\]
as \(n\to\infty\).

## Assumptions and scope
All spaces are real. Normalize the regular \(N\)-gon, where
\[
N=4n,
\qquad
\alpha=\frac{\pi}{N},
\]
so that its Euclidean inradius is \(1\). Its outward unit facet normals occur at angles
\[
2j\alpha,
\qquad
j\in\mathbb Z.
\]
For an angle \(\theta\), let
\[
d(\theta)
=
\operatorname{dist}\!\left(\theta,2\alpha\mathbb Z\right)
\]
with the representative chosen so that
\[
0\le d(\theta)\le\alpha.
\]
The radial function of the unit circle is then
\[
R(\theta)=\sec d(\theta).
\]

The regular \(4n\)-gonal plane is a symmetric Minkowski plane with coordinate axes chosen along two perpendicular facet normals. Fu, Xie and Li quote the standard symmetric-plane fact that if
\[
x=ae_1+be_2\in S_X,
\]
then its unit isosceles-orthogonal partners are exactly
\[
\pm(-be_1+ae_2).
\]
They also prove
\[
D(X)DW_S(X)=2.
\]
It is therefore enough to compute \(D(X_{4n})\).

## Proof
Fix a unit vector in direction \(\theta\):
\[
x=R(\theta)(\cos\theta,\sin\theta).
\]
Because the polygon is invariant under a quarter-turn, the unit isosceles-orthogonal vector may be taken as
\[
y=R(\theta)(-\sin\theta,\cos\theta).
\]
Every unit isosceles-orthogonal pair is obtained this way, up to signs.

For \(\lambda\in\mathbb R\), put
\[
\delta=\arctan\lambda,
\qquad
-\frac{\pi}{2}<\delta<\frac{\pi}{2}.
\]
Then
\[
x+\lambda y
=
R(\theta)\sec\delta\,
(\cos(\theta+\delta),\sin(\theta+\delta)).
\]
Since a Euclidean unit vector in direction \(\psi\) has polygonal norm
\[
\cos d(\psi),
\]
we obtain
\[
\|x+\lambda y\|
=
\frac{\cos d(\theta+\delta)}
{\cos d(\theta)\cos\delta}.
\tag{1}
\]

By rotational symmetry, assume
\[
-\alpha\le\theta\le\alpha.
\]
Choose \(m\in\mathbb Z\) and
\[
-\alpha\le\varepsilon\le\alpha
\]
such that
\[
\theta+\delta=2m\alpha+\varepsilon.
\]
Then (1) becomes
\[
F(\theta,\varepsilon,m)
=
\frac{\cos\varepsilon}
{\cos\theta\,
\cos(2m\alpha+\varepsilon-\theta)}.
\tag{2}
\]
Only triples for which the last cosine corresponds to
\[
-\frac{\pi}{2}<2m\alpha+\varepsilon-\theta<\frac{\pi}{2}
\]
need be considered.

Set
\[
D_0=
\frac{2\cos\alpha}{1+\cos\alpha}.
\]
We prove that every value in (2) is at least \(D_0\).

First suppose \(m=0\). Write
\[
\delta=\varepsilon-\theta.
\]
If \(\theta\delta\le0\), then
\[
F
=
1-\tan\theta\tan\delta
\ge1
\ge D_0.
\]
If \(\theta\delta>0\), reversing both signs if necessary reduces to
\[
\theta\ge0,\qquad
\delta\ge0,\qquad
\theta+\delta\le\alpha.
\]
Put
\[
s=\theta+\delta.
\]
Using
\[
2\cos\theta\cos(s-\theta)
=
\cos s+\cos(2\theta-s)
\le
1+\cos s,
\]
we get
\[
F
=
\frac{\cos s}{\cos\theta\cos(s-\theta)}
\ge
\frac{2\cos s}{1+\cos s}
\ge
\frac{2\cos\alpha}{1+\cos\alpha}
=
D_0.
\tag{3}
\]
Equality in (3) is attained for
\[
\theta=\delta=\frac{\alpha}{2}.
\]

Now suppose \(m=1\); the case \(m=-1\) follows by changing all angles to their negatives. Put
\[
q=\varepsilon-\theta,
\qquad
\delta=2\alpha+q.
\]
If \(q\le0\), then for fixed \(q\) the function
\[
\frac{\cos(\theta+q)}{\cos\theta}
\]
is increasing in \(\theta\). The feasible minimum therefore occurs at
\[
\varepsilon=-\alpha,
\qquad
\theta=-\alpha-q.
\]
At that endpoint
\[
F
=
\frac{\cos\alpha}
{\cos\theta\cos(\alpha-\theta)}
\ge
\frac{2\cos\alpha}{1+\cos\alpha}
=
D_0,
\]
because
\[
2\cos\theta\cos(\alpha-\theta)
=
\cos\alpha+\cos(2\theta-\alpha)
\le
1+\cos\alpha.
\]

If \(q\ge0\), the same quotient is decreasing in \(\theta\), so the feasible minimum occurs at
\[
\varepsilon=\alpha,
\qquad
\theta=\alpha-q.
\]
Then
\[
2\cos(\alpha-q)\cos(2\alpha+q)
=
\cos3\alpha+\cos(\alpha+2q)
\le
1+\cos\alpha.
\]
Hence again
\[
F\ge D_0.
\]

Finally suppose \(|m|\ge2\). By sign symmetry take \(m\ge2\). The angle
\[
\delta=2m\alpha+\varepsilon-\theta
\]
satisfies
\[
\delta\ge2\alpha.
\]
Whenever such a case is feasible, \(\delta<\pi/2\), so
\[
F
\ge
\frac{\cos\alpha}{\cos2\alpha}.
\]
For \(\alpha<\pi/4\),
\[
\frac{\cos\alpha}{\cos2\alpha}
\ge
\frac{2\cos\alpha}{1+\cos\alpha},
\]
because
\[
1+\cos\alpha-2\cos2\alpha
=
(1-\cos\alpha)(4\cos\alpha+3)
\ge0.
\]
When \(\alpha=\pi/4\), no case with \(|m|\ge2\) is feasible.

Thus
\[
D(X_{4n})\ge D_0.
\]
The equality configuration
\[
\theta=\delta=\frac{\alpha}{2}
\]
in the \(m=0\) case proves the reverse inequality, so
\[
D(X_{4n})
=
\frac{2\cos\alpha}{1+\cos\alpha}.
\]
Fu--Xie--Li Proposition 2.1 gives
\[
D(X)DW_S(X)=2.
\]
Therefore
\[
DW_S(X_{4n})
=
\frac{2}{D(X_{4n})}
=
1+\sec\alpha
=
1+\sec\!\left(\frac{\pi}{4n}\right).
\]

## Verification
The proof above is analytic and handles the full continuum of directions and all integers \(n\ge1\).

The bundled `verify.py` independently reconstructs the inradius-one regular polygon norm for representative values
\[
N=4,8,12,16,20,28,40,64.
\]
For a fine deterministic angular grid it evaluates the exact formula (1), checks that no sampled value falls below
\[
\frac{2\cos(\pi/N)}{1+\cos(\pi/N)},
\]
and verifies the equality configuration
\[
\theta=\delta=\frac{\pi}{2N}
\]
to numerical precision. It also checks algebraically, using SymPy simplification, the trigonometric identities used in the endpoint argument.

These finite computations are reproducibility checks only. The universal lower bound and equality construction are established by the symbolic case analysis in the proof.

## Relationship to prior work
Fu, Xie and Li introduce \(DW_S(X)\), define Singer orthogonality, prove
\[
D(X)DW_S(X)=2,
\]
and derive an equivalent form for symmetric Minkowski planes. Their primary paper computes \(DW_S\) for \(\ell_p^2\), gives general bounds, and characterizes one affine-regular hexagonal Radon plane by an extremal value. The inspected full text does not state a regular \(4n\)-gonal formula or a regular-dodecagonal value.

The earlier survey by Alonso, Martini and Wu provides the orthogonality framework, including Singer and isosceles orthogonality, and was publicly dated 18 November 2022. The defining Filomat article is a 2023 publication; the inspected publisher/PDF metadata did not expose a reliable day-level public-release date, so no such day is asserted here.

Targeted public-research searches used the exact invariant notation, Singer-orthogonality aliases, regular-polygon and regular-dodecagon terms, the equivalent \(D(X)\) formulation, and the candidate secant formula. No covering statement was found. The closest indexed regular-polygon results concern unrelated invariants.

## Limitations
The formula is proved for regular polygons whose number of sides is divisible by \(4\). The argument uses quarter-turn symmetry essentially and does not claim a corresponding formula for regular polygons with
\[
N\equiv2\pmod4.
\]

The result concerns \(DW_S\), not the classical Dunkl--Williams constant \(DW\), the isosceles-restricted constant \(DW_I\), or the later Birkhoff-restricted constant \(DW_B\).

Bibliographic and semantic searches cannot prove absolute novelty. An equivalent formula under different notation for \(D(X)\) remains a residual risk, but no such statement was found in the inspected primary paper, the checked public records, or the local prior ledger.

## References
1. J. Alonso, H. Martini and S. Wu, “Orthogonality Types in Normed Linear Spaces,” in *Surveys in Geometry I*, pp. 97–170, Springer, 2022, doi:10.1007/978-3-030-86695-2_4. Public date: 18 November 2022.
2. Y. Fu, H. Xie and Y. Li, “The Dunkl-Williams constant related to the Singer orthogonality and red isosceles orthogonality in Banach spaces,” *Filomat* 37 (2023), no. 17, 5601–5622, doi:10.2298/FIL2317601F. Primary MSC 46B20.
