# Exponentially contracting paraboloid and complete bounded dynamics in Sprott G

## Finding

Consider Sprott's generalized case G flow
\[
\dot x=ax+bz,\qquad \dot y=xz-y,\qquad \dot z=-x+y,
\]
with real parameters \(a,b\). On the distinguished parameter plane \(a=-1/2\), all bounded dynamics can be classified exactly.

**Theorem.** Fix \(a=-1/2\).

1. For any \(b\ne0\), let \(H=y-x^2/(2b)\). Along every solution on its maximal interval,
   \[\dot H=-H,\qquad H(t)=H(0)e^{-t}.\]
   The polynomial coordinate transformation
   \[
   (x,y,z)\mapsto (x,v,h)=\bigl(x,-x/2+bz,\ y-x^2/(2b)\bigr)
   \]
   is a global diffeomorphism of \(\mathbb R^3\) and gives
   \[
   \dot x=v,\quad \dot v=-v/2-bx+x^2/2+bh,\quad \dot h=-h.
   \]
   Every bounded forward-complete orbit converges to one of exactly two equilibria:
   \[
   E_0=(0,0,0),\qquad E_b=(2b,2b,1).
   \]
   One equilibrium is a hyperbolic sink and the other a hyperbolic saddle of unstable dimension one. Specifically, \(E_0\) is the sink for \(b>0\), and \(E_b\) is the sink for \(b<0\).

2. Up to time translation there is exactly **one nonconstant bounded complete orbit**, a heteroclinic from the saddle to the sink on the invariant quadratic surface \(H=0\). Its exact energy dissipation is
   \[
   \int_{-\infty}^{\infty}\dot x(t)^2\,dt=\frac43|b|^3.
   \]
   Every nonempty compact **two-sided invariant** set is contained in the union of this orbit and its endpoints. Every compactly supported invariant probability measure is exactly a convex mixture of \(\delta_{E_0}\) and \(\delta_{E_b}\).

3. If \(b=0\), all forward solutions exist for all positive times, are bounded, and converge to some point of the equilibrium line \(L=\{(0,0,z):z\in\mathbb R\}\). Every bounded complete orbit is a constant equilibrium on \(L\), and compactly supported invariant probability measures are exactly the probability measures supported on compact subsets of \(L\).

Consequently, for every real \(b\) on \(a=-1/2\), no nonconstant periodic orbit or non-equilibrium compact recurrent dynamics exists. The phrase 'bounded complete' means defined and bounded for all \(t\in\mathbb R\); 'bounded forward-complete' means defined and bounded for \(t\ge0\).

## Assumptions and scope

The vector field is precisely the smooth polynomial system stated above. Both parameters are real; the theorem fixes \(a=-1/2\) and includes the singular case \(b=0\). No claim of global forward completeness is made for arbitrary initial data when \(b\ne0\); solutions may be unbounded or escape in finite time. Invariant compact sets mean two-sided invariant sets under the flow. Invariant measures have compact support.

## Proof

**1. Exact cancellation and conjugacy.** When \(b\ne0\), direct differentiation for general \(a\) gives
\[
\frac{d}{dt}\left(y-\frac{x^2}{2b}\right)
 =-\left(y-\frac{x^2}{2b}\right)-\frac{a+1/2}{b}x^2.
\]
Hence \(\dot H=-H\) at \(a=-1/2\). The inverse coordinate map is \(y=h+x^2/(2b)\), \(z=(v+x/2)/b\). Its Jacobian determinant is \(-b\ne0\). Differentiating \(v=-x/2+bz\) gives the displayed transformed system. In particular, any bounded complete orbit has \(h\equiv0\): otherwise \(h(t)=h(0)e^{-t}\) is unbounded as \(t\to-\infty\).

**2. Gradient-like planar limit.** On \(h=0\), define the potential and energy
\[
U_b(x)=\frac b2x^2-\frac16x^3,\qquad
\mathcal E=\frac12v^2+U_b(x).
\]
Then
\[
\ddot x+\frac12\dot x+U_b'(x)=0,\qquad
\dot{\mathcal E}=-\frac12v^2.
\]
The equilibria in the planar coordinates are \((x,v)=(0,0)\) and \((2b,0)\). Their planar linear characteristic polynomial is \(\lambda^2+\lambda/2+b-x_*\). Exactly one is a sink and the other a saddle, since their determinants are \(b\) and \(-b\). The additional transverse exponent is \(-1\), so this is also the three-dimensional classification.

**3. Bounded forward convergence for \(b\ne0\).** Along any bounded forward-complete trajectory define the same \(\mathcal E\), now allowing \(h\ne0\). The exact derivative is
\[
\dot{\mathcal E}=-\frac12v^2+bhv
\le -\frac14v^2+b^2h^2.
\]
As \(h(t)=h(0)e^{-t}\), its square is integrable. Since a bounded trajectory keeps \(\mathcal E\) bounded below, integration implies \(\int_0^\infty v(t)^2\,dt<\infty\). The equations bound \(\dot v\), so uniform continuity plus square integrability give \(v(t)\to0\). Differentiating once more,
\[\ddot v=-\dot v/2+(x-b)v-bh,\]
which is bounded; thus \(\dot v\) is uniformly continuous. A function tending to zero with uniformly continuous derivative has derivative tending to zero, hence \(\dot v(t)\to0\). Therefore
\[
\frac12x(t)(x(t)-2b)\to0.
\]
For fixed \(b\ne0\), the disjoint neighborhoods of its two roots and continuity of \(x(t)\) imply convergence to one root. The coordinate inverse and \(v,h\to0\) yield convergence to \(E_0\) or \(E_b\).

**4. Existence and uniqueness of the heteroclinic.** Let \(x_s\) denote the planar saddle coordinate (\(2b\) when \(b>0\), zero when \(b<0\)); let \(x_k\) denote the sink coordinate. In either case \(x_k<x_s\). The potential \(U_b\) has a local maximum at \(x_s\) and tends to \(+\infty\) as \(x\to-\infty\). The planar saddle has two one-dimensional unstable branches. Along either nonconstant branch, strict energy decrease from its past limit at the saddle gives \(\mathcal E(t)<U_b(x_s)\) for every finite time. The branch leaving toward \(x<x_s\) cannot cross \(x=x_s\), because that would require \(\mathcal E\ge U_b(x_s)\). On the half-line \(x<x_s\), the bound \(\mathcal E\le U_b(x_s)\), together with coercivity of \(U_b\) at minus infinity, bounds \(x\) and \(v\), hence the branch exists for all future times. Step 3 forces its limit to an equilibrium; energy below \(U_b(x_s)\) excludes the saddle, so it converges to the sink.

The right unstable branch, with \(x>x_s\), cannot cross back over \(x_s\), nor converge to the sink at \(x_k<x_s\); by Step 3 it cannot be bounded forward. Conversely, every bounded complete nonstationary orbit lies in \(h=0\). Its bounded alpha- and omega-limit sets are nonempty and invariant. Since \(\mathcal E\) tends to finite limits at both temporal ends and is constant on each corresponding limit set, \(\dot{\mathcal E}=-v^2/2\) forces each limit set to consist of equilibria. Each limit set is connected, so it consists of one equilibrium. Identical endpoints would force zero total energy loss, hence a constant orbit. The only distinct endpoint ordering compatible with strictly decreasing energy is saddle to sink. Thus every such orbit must be the unique left unstable branch, up to time translation.

**5. Exact dissipation and invariant measures.** The endpoint potentials are \(U_b(0)=0\) and \(U_b(2b)=2b^3/3\). Their difference in saddle-to-sink order is \(2|b|^3/3\). Integrating \(\dot{\mathcal E}=-v^2/2\) over the heteroclinic gives \(\int_{-\infty}^{\infty}v^2dt=4|b|^3/3\).

If \(\mu\) is a compactly supported invariant probability measure, flow invariance and \(h(t)=e^{-t}h(0)\) give \(\int h^2d\mu=e^{-2t}\int h^2d\mu\), so \(h=0\) almost surely. Integrating the energy derivative on that surface gives \(\int v^2d\mu=0\). Invariance then forces \(\dot v=0\) on its support, i.e., \(x\in\{0,2b\}\). Thus \(\mu\) is exactly a convex mixture of the two equilibrium atoms. Conversely each such mixture is invariant. The classification of compact two-sided invariant sets follows from the classification of bounded complete trajectories.

**6. Singular case \(b=0\).** Here \(x(t)=x(0)e^{-t/2}\). The remaining equations are \(\dot y=-y+x(t)z\) and \(\dot z=-x(t)+y\). Variation of constants gives
\[
y(t)=e^{-t}y(0)+\int_0^te^{-(t-s)}x(s)z(s)\,ds.
\]
Consequently, for every \(t\ge0\),
\[
|z(t)|\le |z(0)|+2|x(0)|+|y(0)|+\int_0^t|x(s)|\,|z(s)|\,ds.
\]
Gronwall's inequality and \(\int_0^\infty|x(s)|ds=2|x(0)|\) show that \(z\) is globally bounded; the linear equations then have global forward solutions. As \(xz\in L^1([0,\infty))\), the displayed convolution implies \(y\in L^1\), \(y\to0\), and \(z(t)\) converges to a finite limit. A bounded complete trajectory must have \(x\equiv0\) by backward exponential growth, then \(y\equiv0\) by the equation \(\dot y=-y\); therefore it is a point of \(L\). Flow invariance similarly forces any compactly supported invariant probability measure onto \(L\), and every such supported measure is invariant.

## Verification

The accompanying standalone symbolic checker `verify_sprott_g.py` verifies the exact Darboux identity for general parameters, the polynomial change of coordinates, its nonzero Jacobian for \(b\ne0\), the transformed equations, the energy identity, both equilibrium equations, the characteristic polynomials, and the exact endpoint potential difference. Running `python verify_sprott_g.py` with SymPy installed produces a single success message. The global convergence and heteroclinic uniqueness statements are established by the analytical inequalities and dynamical arguments above, not by finite experiments or the symbolic checker alone.

## Relationship to prior work

Sprott's 1994 work introduced case G with a chaotic parameter example and numerical spectral diagnostics. His 2013 parameter atlas explored equilibria, cycles, chaos, and escape primarily through parameter-plane numerical classification, but did not derive the exact quadratic-fiber contraction or a complete global bounded-orbit classification on \(a=-1/2\). A 2013 Shilnikov-theory survey tabulated equilibria and eigenvalues for Sprott G at \(a=1/2\), a different parameter regime. A 2021 full-text study of Sprott-system differential equivalences examined the chaotic regime for G near \((a,b)=(0.406,0.9)\); its jerk equivalence comparisons do not contain a theorem on the negative half-parameter plane here.

The present assertion is not the generic energy-dissipation principle alone: its content includes the particular polynomial cancellation selecting \(a=-1/2\), a global exact conjugacy, all-real-\(b\) bounded-complete classification, uniqueness of a selected connecting orbit, and a parameter-exact action. Analogous energy arguments for other flows do not imply these case-G-specific structural facts without the cancellation and its proof.

## Limitations

The theorem concerns only the parameter plane \(a=-1/2\); no global claim is made for neighboring \(a\). For \(b\ne0\), bounded-orbit convergence is conditional on forward completeness and boundedness, not a claim that all trajectories are bounded. The theorem does not determine basins of attraction or escape rates of unbounded solutions. The original model and mathematical methods are public, but unindexed equivalent negative-parameter analyses could affect historical priority. This is a mathematical proof with computational identity checks, not an independent external validation.

## References

1. J. C. Sprott, “Some simple chaotic flows,” *Physical Review E* **50**, R647–R650 (1994), doi:10.1103/PhysRevE.50.R647. First public date: 1994-08-01.
2. J. C. Sprott, “Dynamic Regions in Simple Chaotic Flows,” 2013, https://sprott.physics.wisc.edu/technote/regions.htm.
3. Eduardo M. A. M. Mendes, Claudia Lainscsek, Christophe Letellier, “Diffeomorphical equivalence vs topological equivalence among Sprott systems,” *Chaos* **31**, 083126 (2021), doi:10.1063/5.0058330.
4. Baoying Chen, “The Related Extension and Application of the Ši’lnikov Theorem,” *Journal of Applied Mathematics* (2013), doi:10.1155/2013/287123. The Sprott G comparison is at \(a=1/2\).
