# An invasion-determinant threshold for two-resource, two-consumer communities

## Finding

A four-species antagonistic Lotka–Volterra community admits an exact, nonlocal exchange between coexistence and two alternative consumer-exclusion attractors. Consider two resources and two consumers obeying the exchange-symmetric equations below. Define the mismatch determinant
\[
Q=1-(a-b)(d-c).
\]
Provided the three biologically relevant equilibria are feasible, the coexistence equilibrium is a hyperbolic sink precisely for \(Q>0\), whereas for \(Q<0\) it is a saddle and **each** equilibrium with both resources and exactly one consumer is a hyperbolic sink. At \(Q=0\), these three points belong to an explicit continuous segment of equilibria; the transition is not the birth of a tiny-amplitude branch. The invasion exponent of either missing consumer is exactly \(Q\) times the resident consumer abundance.

For the natural one-parameter illustration with intrinsic rates \(r=m=3\), loss coefficients \(a=3,b=1\), gain coefficient \(c=1\), and variable \(1<d<2\), there are exactly nine nonnegative equilibria away from \(d=3/2\). Of these, the fully positive one is the only locally asymptotically stable equilibrium for \(d<3/2\); the two single-consumer, two-resource equilibria are the only locally asymptotically stable equilibria for \(d>3/2\). At the critical value, the relevant three equilibria form a positive stationary line segment.

## Assumptions and scope

All variables represent nonnegative abundances. For \(i\in\{1,2\}\) and \(j=3-i\), consider the autonomous continuous-time system
\[
\dot x_i=x_i(r-x_i-a y_i-b y_j),\qquad
\dot y_i=y_i(-m-y_i+c x_i+d x_j).
\]
Assume \(r,m>0\), \(a>b>0\), \(d>c>0\), and
\[
0<m<(c+d)r,\qquad
m>\frac{r((a-b)d-1)}{a}.
\]
The second lower inequality ensures that both resource abundances stay strictly positive at each single-consumer equilibrium. These hypotheses are sufficient for every equilibrium used in the theorem to be feasible. Define
\[
S=1+(a+b)(c+d),\quad T=1+ac+bd,\quad Q=1+(a-b)(c-d).
\]
Only equilibrium existence and *local* stability are claimed. The conclusions do not imply convergence of every positive trajectory to an equilibrium or give basin boundaries. The nonnegative orthant is forward invariant, and solutions are globally bounded since \(\dot x_i\le x_i(r-x_i)\), after which the two consumer equations admit scalar logistic upper bounds.

## Proof

**1. The three equilibria and exact missing-consumer invasion.** The symmetric positive equilibrium, in the coordinate order \((x_1,x_2,y_1,y_2)\), is
\[
E_*=(X,X,Y,Y),\quad
X=\frac{r+(a+b)m}{S},\quad
Y=\frac{(c+d)r-m}{S}.
\]
Write
\[
U=\frac{r(1-(a-b)d)+am}{T},\quad
V=\frac{r(1+(a-b)c)+bm}{T},\quad
W=\frac{(c+d)r-m}{T}.
\]
The single-consumer states are \(E_1=(U,V,W,0)\) and \(E_2=(V,U,0,W)\). Direct substitution into the per-capita equations verifies them. The assumptions give \(X,Y,U,V,W>0\). The missing consumer's linear invasion exponent at \(E_1\) is
\[
\lambda_{\mathrm{inv}}=-m+dU+cV=W\,[1+(a-b)(c-d)]=WQ;
\]
by symmetry the same holds at \(E_2\).

**2. The resident subcommunities are strictly stable.** At \(E_1\), the resident Jacobian in variables \((x_1,x_2,y_1)\) equals
\[
J_3=\begin{pmatrix}-U&0&-aU\\0&-V&-bV\\cW&dW&-W\end{pmatrix}.
\]
The positive definite diagonal matrix
\[
P=\operatorname{diag}\left(\frac{c}{aU},\frac{d}{bV},\frac1W\right)
\]
satisfies
\[
PJ_3+J_3^{\mathsf T}P=-2\operatorname{diag}\left(\frac ca,\frac db,1\right)<0.
\]
Consequently all resident eigenvalues have strictly negative real parts. Ordering the absent consumer last gives a block triangular full Jacobian with the additional eigenvalue \(WQ\). Both single-consumer states are hyperbolic sinks for \(Q<0\), and have exactly one unstable eigenvalue for \(Q>0\).

**3. The positive equilibrium changes stability with the same sign.** At \(E_*\), exchange symmetry separates the Jacobian into symmetric and antisymmetric two-dimensional blocks. Their common trace is \(-(X+Y)<0\). Their determinants are, respectively,
\[
XY\,[1+(a+b)(c+d)]=XYS>0,\qquad
XY\,[1+(a-b)(c-d)]=XYQ.
\]
The two-dimensional Hurwitz criterion proves \(E_*\) is a hyperbolic sink for \(Q>0\). If \(Q<0\), the antisymmetric block has one positive and one negative real eigenvalue, while the symmetric block is strictly stable: \(E_*\) is then a hyperbolic saddle with one unstable direction.

**4. The entire critical segment.** Suppose \(Q=0\). The four positive per-capita equilibrium equations have one-dimensional nullspace in the consumer-composition direction. Their full feasible solution is
\[
y_1=u,\quad y_2=2Y-u,\quad
x_1=r-2bY-(a-b)u,\quad
x_2=r-2aY+(a-b)u,
\quad 0\le u\le2Y.
\]
Its endpoints are \(E_2\) and \(E_1\); its midpoint is \(E_*\). Each resource coordinate is affine in \(u\) and positive at the endpoints, hence positive throughout. Since the equilibrium coefficient matrix has nullity exactly one at \(Q=0\), this is the complete family with both resources positive. Its existence precludes classifying the collision as an ordinary isolated hyperbolic bifurcation.

**5. Complete nonnegative equilibrium and attractor census for one parameter.** Set \(r=m=3\), \(a=3\), \(b=c=1\), \(1<d<2\). Then \(Q=3-2d\) and
\[
E_* =\left(\frac{15}{5+4d},\frac{15}{5+4d},\frac{3d}{5+4d},\frac{3d}{5+4d}\right),
\]
\[
E_1=\left(\frac{6(2-d)}{4+d},\frac{12}{4+d},\frac{3d}{4+d},0\right),
\quad
E_2=\left(\frac{12}{4+d},\frac{6(2-d)}{4+d},0,\frac{3d}{4+d}\right).
\]
For \(d\ne3/2\), the remaining six nonnegative equilibria are the origin, the resource-only axis points \((3,0,0,0)\) and \((0,3,0,0)\), the two-resource consumer-free point \((3,3,0,0)\), and the opposite-linked single-resource/single-consumer points
\[
F_1=\left(0,\frac6{1+d},\frac{3(d-1)}{1+d},0\right),\qquad
F_2=\left(\frac6{1+d},0,0,\frac{3(d-1)}{1+d}\right).
\]
This list is exhaustive by support enumeration. When both resources are absent, both consumers have negative per-capita growth. If just one resource is present, a consumer supported by its weaker \(c=1\) link cannot persist, since that resource cannot exceed \(3=m\). The remaining permitted two-species supports give \(F_1,F_2\). With both resources, each of the four consumer-support choices yields the resource-only point, \(E_1\), \(E_2\), or \(E_*\), except at the singular parameter \(d=3/2\) where the last three are replaced by a segment.

Every one of the six other isolated equilibria has a positive invasion eigenvalue: the origin and resource-axis points admit a missing growing resource; the resource-only point has consumer invasion \(3d>0\); each \(F_i\) has missing-resource invasion
\[
3-3\frac{3(d-1)}{1+d}=\frac{6(2-d)}{1+d}>0.
\]
Therefore only the attractors specified in the finding can be locally asymptotically stable. At \(d=3/2\), the exact stationary segment is
\[
\left(\frac{24}{11}-2u,\frac6{11}+2u,u,\frac9{11}-u\right),\quad0\le u\le\frac9{11}.
\]
The six remaining isolated equilibria remain unstable; the line's endpoint supports are the two former single-consumer states.

## Verification

Run `python3 verify.py` next to this document. This standard-library program checks all displayed equilibrium identities, the exact invasion factor, the three-dimensional Lyapunov matrix identity in 72 independent rational parameter cases, the complete nonnegative support census at two rational parameters on opposite sides of the threshold, and five exact points on the critical segment. At \(d=5/4\), \(Q=1/2\); at \(d=7/4\), \(Q=-1/2\). The script is a finite consistency check, not a proof of the all-parameter theorem; steps 1–5 give that proof.

## Relationship to prior work

Dopson and Emary (2023 preprint; 2024 journal article) investigate antagonistic bipartite ecological communities with generalized Lotka–Volterra equations, primarily in a large-species random-interaction regime. Their correlation convention in the studied ensemble imposes \(\gamma\ge0\), and they locate a multiple-attractor phase without a deterministic four-species consumer-invasion threshold or the nonisolated critical segment above. Here the positive numerical interaction coefficients have opposite within-pair ranking between resource damage and consumer benefit, a setting not addressed by their positive-correlation ensemble calculations.

Giraldo and Lee (2024) analyze multistability and degenerate bifurcations in empirical **mutualistic** plant-pollinator networks; their interguild signs, reciprocal coupling, parameterization and extinction scenarios differ from this antagonistic four-species classification. Livesay (2017 preprint, revised subsequently) and Hong and Pego (2021 preprint) give general results restricting simultaneous stability of nested Lotka–Volterra communities. Such principles are consistent with the present finding, but neither supplies the threshold \(Q=0\), the exact opposite-linked exclusion attractors, or the critical continuum and full nine-point census. These comparisons establish only noncoverage by the inspected results, not a claim of exhaustive priority.

## Limitations

The positive-equilibrium statement is local; no global convergence or basin partition is proved. The one-parameter census is specific to the stated coefficients and does not classify all boundary supports in the larger parameter family. A critical line of equilibria does not by itself imply that every point is attracting. The antagonistic loss/benefit preference inversion is an explicit model assumption rather than an inference about measured feeding networks. Independent literature and mathematical verification beyond the stated checks remain open.

## References

- M. Dopson and C. Emary, *The persistence of bipartite ecological communities with Lotka–Volterra dynamics*, arXiv:2307.14162 (first posted 2023-07-26); *Journal of Mathematical Biology* 89 (2024), Article 24, DOI 10.1007/s00285-024-02120-w.
- A. Giraldo and D.-S. Lee, *Bifurcations and multistability in empirical mutualistic networks*, arXiv:2406.06897v1 (2024-06-11).
- M. R. Livesay, *A Locally Stable Equilibria Criterion for the Generalized Lotka–Volterra*, arXiv:1709.00997 (first posted 2017-09-04).
- W. E. Hong and R. L. Pego, *Exclusion and multiplicity for stable communities in Lotka–Volterra systems*, arXiv:2102.00611 (first posted 2021-02-01).
