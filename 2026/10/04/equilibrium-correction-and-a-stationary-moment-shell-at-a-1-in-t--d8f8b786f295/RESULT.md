# Equilibrium correction and a stationary moment shell at \(a=1\) in the Ray–Ghosh flow
## Finding
Consider the Ray–Ghosh system at the distinguished slice \(a=1\):
\[
\dot x=-x+y+z,\qquad \dot y=xy-z,\qquad \dot z=-xz+y+b,\qquad b>0.
\]
Its divergence is the constant \(-1\). Define
\[
x_\pm=\frac{1\pm\sqrt{1+4b}}{2}.
\]
Then the source's equilibrium cubic factors as
\[
x^3-(b+1)x-b=(x+1)(x^2-x-b),
\]
but the factor \(x+1\) is spurious for equilibria: \(x=-1\) cannot satisfy the first two equilibrium equations. Thus the actual equilibrium \(x\)-coordinates are \(x_+\) and \(x_-\) when \(b\neq2\); at \(b=2\), \(x_-=-1\) is invalid and only \(x_+=2\) remains.

Moreover, every compactly supported invariant probability measure \(\mu\) satisfies
\[
\int \left(x-\frac12\right)^2\,d\mu=b+\frac14.
\]
Writing \(m=\int x\,d\mu\), this is equivalent to
\[
\operatorname{Var}_\mu(x)=(x_+-m)(m-x_-).
\]
Hence \(m\in[x_-,x_+]\). Equality at either endpoint forces an equilibrium-supported invariant measure. Therefore every non-equilibrium ergodic invariant measure satisfies \(x_-<m<x_+\), and it assigns positive mass both to \(x\in(x_-,x_+)\) and to \(x\notin[x_-,x_+]\). In particular, every nonconstant periodic orbit crosses at least one algebraic level \(x_-\) or \(x_+\). For \(b\neq2\), these are exactly the two equilibrium \(x\)-levels; at \(b=2\), the lower level \(x_-=-1\) is not an equilibrium.

## Assumptions and scope
The parameter assumptions are exactly \(a=1\) and \(b>0\). The invariant-measure statement assumes compact support, which is sufficient for integrating a polynomial Lie derivative against the measure. No existence of a non-equilibrium compact invariant measure is asserted. The strict mean and crossing statements apply to non-equilibrium ergodic invariant measures; a non-ergodic mixture of equilibrium measures is deliberately excluded. The periodic-orbit consequence applies only to nonconstant periodic trajectories.

## Proof
At an equilibrium, \(\dot y=0\) gives \(z=xy\), while \(\dot x=0\) gives \(y+z=x\). Hence
\[
y(1+x)=x.
\]
If \(x=-1\), the left side is \(0\) and the right side is \(-1\), a contradiction. Thus \(x\neq-1\), so
\[
y=\frac{x}{1+x},\qquad z=\frac{x^2}{1+x}.
\]
Substitution into \(\dot z=0\) at \(a=1\) yields the source cubic \(x^3-(b+1)x-b=0\), which factors as \((x+1)(x^2-x-b)\). Since \(x=-1\) has already been ruled out, the valid equilibrium coordinates solve \(x^2-x-b=0\), giving \(x_\pm\). The lower root equals \(-1\) exactly when \(b=2\), producing the stated exceptional count.

For the stationary law, set
\[
F(x,y,z)=x^2-2x-2y+2z.
\]
A direct Lie-derivative calculation along the \(a=1\) vector field gives
\[
\frac{dF}{dt}=-2(x^2-x-b).
\]
For any compactly supported invariant probability measure \(\mu\), invariance gives \(\int dF/dt\,d\mu=0\). Therefore
\[
\int x^2\,d\mu-\int x\,d\mu-b=0,
\]
which is exactly
\[
\int \left(x-\frac12\right)^2\,d\mu=b+\frac14.
\]
Since \(x_++x_-=1\) and \(x_+x_-=-b\),
\[
\operatorname{Var}_\mu(x)=m+b-m^2=(x_+-m)(m-x_-).
\]
Nonnegativity of variance implies \(m\in[x_-,x_+]\). If an endpoint occurs, the variance is zero and \(x\) is constant almost surely. An invariant trajectory with constant \(x=c\) must have \(\dot x=0\) and \(\ddot x=0\); for a root \(c\) of \(c^2-c-b=0\), these equations force \(y=c/(1+c)\) and \(z=c^2/(1+c)\), while \(c=-1\) is impossible. Hence endpoint equality is equilibrium-supported.

Finally let \(g(x)=x^2-x-b=(x-x_-)(x-x_+)\). The same identity gives \(\int g\,d\mu=0\). If a non-equilibrium ergodic invariant measure placed no mass on one sign of \(g\), the zero integral would force \(g=0\) almost surely. Continuity of trajectories would then force \(x\) to be constant at one root and hence the orbit to be an equilibrium, a contradiction. Thus both signs occur with positive measure. For a nonconstant periodic orbit the same argument uses the time average over one period; continuity then forces a crossing of \(g=0\), hence of \(x=x_-\) or \(x=x_+\). When \(b\neq2\), both are equilibrium levels; when \(b=2\), only \(x_+=2\) is an equilibrium and \(x_-=-1\) is merely the other zero of \(g\).

## Verification
The equilibrium reduction and Lie-derivative identity were independently replayed with exact polynomial arithmetic in the accompanying `verify_balance.py`. The script verifies the factorization
\[
x^3-(b+1)x-b=(x+1)(x^2-x-b)
\]
and the identity
\[
\nabla F\cdot(\dot x,\dot y,\dot z)=-2(x^2-x-b)
\]
coefficient by coefficient. The proof above, not the script output alone, supplies the invariant-measure and crossing arguments.

## Relationship to prior work
Ray and Ghosh introduce the system, write the equilibrium coordinates as \(y=x/(1+x)\) and \(z=x^2/(1+x)\), derive the cubic \(ax^3-(b+1)x-b=0\), and state a parameter region with three fixed points. On the singular slice \(a=1\), however, the cubic acquires the factor \(x+1\), exactly where those rational coordinate formulas are undefined. The direct equilibrium equations show that this root is extraneous. The source studies stability, Hopf bifurcation, period doubling, and chaos, but does not state the stationary moment shell above. Searches of the exact title, DOI, the singular slice \(a=1\), the factor \(x^2-x-b\), and invariant-measure/stationary-moment terminology did not locate a publication stating this correction or the same invariant-measure identity. Related records on stationary moment identities for other chaotic flows concern different vector fields and do not imply this result.

## Limitations
This result does not prove that a chaotic attractor, periodic orbit, or any other non-equilibrium compact invariant set exists at \(a=1\). It gives necessary restrictions on any such recurrent state. The originality search cannot exclude unindexed or inaccessible literature, and the claim is therefore limited to the explicit statement and comparisons documented in the review materials.

## References
1. A. Ray and D. Ghosh, “Another new chaotic system: bifurcation and chaos control,” arXiv:1911.11429v1, first public 26 November 2019.
2. A. Ray and D. Ghosh, “Another New Chaotic System: Bifurcation and Chaos Control,” *International Journal of Bifurcation and Chaos* 30(11), 2050161 (2020), doi:10.1142/S0218127420501618.
