# Global entropy stabilization of the Rössler flow with nonpositive feedback

## Finding
Consider the classical three-dimensional Rössler vector field
\[
\dot x=-y-z,\qquad \dot y=x+ay,\qquad \dot z=b+z(x-c).
\]
**Theorem.** For every fixed triple \((a,b,c)\in\mathbb R^3\) with \(a\le0\), \(b>0\), and \(c>0\), write \(p\) for the unique positive solution of
\[
ap^2-cp+b=0
\]
and put \(E=(ap,-p,p)\). The point \(E\) is the unique equilibrium in \(z\ge0\). Every solution with arbitrary real initial \(x(0),y(0)\) and \(z(0)\ge0\) exists for all forward times, lies in \(z>0\) for every positive time, and converges to \(E\).

For \(z>0\), the nonnegative entropy-energy function
\[
V(x,y,z)=\frac{(x-ap)^2+(y+p)^2}{2}+z-p-p\log(z/p)
\]
has the **exact** dissipation law
\[
\frac{dV}{dt}=a(y+p)^2-\frac{(c-ap)(z-p)^2}{z}.
\]
In particular, for every trajectory starting at \(z(0)>0\),
\[
\int_0^\infty\left[-a(y(t)+p)^2+\frac{(c-ap)(z(t)-p)^2}{z(t)}\right]dt=V(x(0),y(0),z(0)).
\]
The only nonempty compact **two-sided invariant** subset of \(z>0\) is \(\{E\}\); the only compactly supported invariant Borel probability measure there is \(\delta_E\). Thus nonconstant periodic or chaotic compact recurrent dynamics are impossible throughout this entire parameter regime.

## Assumptions and scope
All three parameters are time-independent real numbers; the hypotheses are \(a\le0\), \(b,c>0\). The vector field is taken exactly as displayed, with no coordinate or time rescaling. The state domain for the Lyapunov function is the open half-space \(\{(x,y,z):z>0\}\); initial states with \(z=0\) enter it immediately. Claims of convergence concern forward time only. Compact invariant sets mean sets invariant under the flow for all positive and negative times with the complete orbits remaining inside the set. "Strict-invariance Lyapunov" means that the largest forward-invariant subset of the zero-derivative locus is one equilibrium; its derivative need not be pointwise strictly negative at other points.

For \(a<0\), the polynomial \(q(s)=as^2-cs+b\) is strictly decreasing on \(s\ge0\), starts positive and tends to \(-\infty\). For \(a=0\), its unique positive zero is \(p=b/c\). Hence \(p\) exists and is unique, and \(c-ap\ge c>0\).

## Proof
**Equilibrium and positivity.** An equilibrium must satisfy \(y=-z\), \(x=az\), and \(b+z(az-c)=0\). At \(z=0\), the last equation becomes \(b=0\), which is excluded. By the preceding uniqueness argument, \(E\) is the sole equilibrium in \(z\ge0\). Along any local solution the scalar third equation has the integrating-factor identity
\[
z(t)=\exp\!\left(\int_0^t[x(u)-c]du\right)\!\left[z(0)+b\int_0^t\exp\!\left(-\int_0^s[x(u)-c]du\right)ds\right].
\]
For \(z(0)\ge0\), the right-hand side is positive whenever \(t>0\) lies in the interval of existence; if \(z(0)>0\), it is positive already at \(t=0\).

**Exact energy cancellation.** Introduce \(X=x-ap\), \(Y=y+p\), and \(Z=z-p\). The equilibrium identity \(b=cp-ap^2\) gives
\[
\dot X=-Y-Z,\qquad \dot Y=X+aY,\qquad
\dot z=zX+(ap-c)(z-p).
\]
Differentiate \(V=(X^2+Y^2)/2+z-p-p\log(z/p)\):
\[
\dot V=X(-Y-Z)+Y(X+aY)+\left(1-\frac pz\right)[zX+(ap-c)Z]
=aY^2+(ap-c)\frac{Z^2}{z}.
\]
The mixed terms cancel *identically*. Since \(a\le0\), \(c-ap>0\), and \(z>0\), the derivative is nonpositive. Moreover, \(s-1-\log s\ge0\) for all \(s>0\), with equality only for \(s=1\), so \(V\ge0\) and its sole zero is \(E\).

**Properness and global existence.** For each fixed \(p>0\), the function \(z-p-p\log(z/p)\) tends to \(+\infty\) both as \(z\downarrow0\) and \(z\to+\infty\). Consequently the sublevel sets \(\{z>0:V\le M\}\) are compact subsets of \(\mathbb R^2\times(0,\infty)\). A solution with \(z(0)>0\) remains in its initial sublevel, cannot encounter the boundary or blow up in finite forward time, and therefore exists globally. When \(z(0)=0\), first use the positivity formula on a short interval to select any sufficiently small positive time and then apply the same argument from that time onward. This also establishes forward completeness for boundary initial data.

**LaSalle at and below the damping boundary.** For \(a<0\), the zero-derivative locus consists of \(Y=0\) and \(z=p\). Along a trajectory staying there, \(\dot Y=X\), so \(X=0\); thus its largest invariant subset is \(E\). At \(a=0\), the derivative vanishes precisely on \(z=p\), without requiring \(Y=0\). But maintaining \(z=p\) implies \(0=\dot z=pX\), hence \(X=0\); then \(0=\dot X=-Y\), hence \(Y=0\). Again only \(E\) is invariant. LaSalle's invariance principle on each compact sublevel now implies convergence of every positive-height trajectory to \(E\), and the boundary case follows by starting at any positive time. Because \(V\) is positive definite, this also establishes Lyapunov stability and global asymptotic stability relative to \(z>0\).

**Exact total dissipation and compact dynamics.** Integrate the derivative identity from \(0\) to \(T\) for positive initial height, then let \(T\to\infty\). Since the orbit converges to \(E\), \(V(T)\to0\), giving the asserted integral equality. If \(K\subset\{z>0\}\) is nonempty, compact and two-sided invariant, choose a point at which \(V\) attains its maximum \(M\) on \(K\). Every backward iterate stays in \(K\), yet nonincrease along forward orbits forces its value to be at least \(M\), hence exactly \(M\). The backward orbit therefore lies in the zero-derivative locus; the preceding invariance calculation forces the maximizing point to be \(E\) and \(M=0\). Thus \(K=\{E\}\). Finally, if \(\nu\) is a compactly supported invariant probability measure in the open half-space, invariance and boundedness on its compact support give \(\int\dot V\,d\nu=0\); nonpositivity of \(\dot V\) and invariance force \(\nu\) to be supported on \(E\). Therefore \(\nu=\delta_E\).

## Verification
The attached standalone SymPy checker `check_identity.py` reconstructs the unshifted vector field and equilibrium, verifies the translated equations, and proves algebraically that the difference between \(\dot V\) and the proposed dissipation expression equals \((ap^2-cp+b)(z-p)/z\), which vanishes exactly under the equilibrium equation. Its output is `PASS` when these exact identities hold. It also checks several parameter examples for sign and root selection. The quantified positivity, properness, invariance and convergence arguments above are analytic proofs, not consequences of finite spot tests or numerical simulation.

## Relationship to prior work
Rössler's original 1976 two-page paper introduced the now-classical vector field at the positive-feedback example \((a,b,c)=(0.2,0.2,5.7)\) and discussed folded chaotic trajectories; it explicitly raised analysis of monostable variants as a natural next problem. Barrio, Blesa, Dena and Serrano (2011) study equilibrium and Hopf bifurcations and state positive parameter assumptions in their introduction. Genesio, Innocenti and Gualdani (2008) pursue harmonic-balance predictions of periodic-orbit bifurcations. Fowler and McGuinness (2023) develop a large-\(c\) asymptotic treatment with positive feedback. These results do not provide the exact entropy dissipation identity and the all-initial-data global convergence theorem on \(a\le0\) as stated here. Two located research summaries concerning compact Rössler recurrence and conditional stationary flux explicitly restrict their statements to positive parameters and thus do not imply this closed nonpositive-feedback result. This comparison is not a proof of universal priority; the full texts of all later bifurcation studies were not uniformly available.

## Limitations
The result is restricted to \(b,c>0\), \(a\le0\), and initial \(z\ge0\). It says nothing about trajectories launched in \(z<0\), the parameters \(a>0\), or the degenerate boundary \(b=0\) or \(c=0\). It gives no uniform global convergence rate or bifurcation classification at positive feedback. The exact dissipation integral requires strictly positive initial height; for boundary initial data it applies after any positive time. A bibliographic search can miss equivalent unindexed arguments, and an inaccessible primary text remains a historical priority risk; no external independent audit has been performed.

## References
1. O. E. Rössler, *An Equation for Continuous Chaos*, Physics Letters A **57** (1976), 397–398; DOI: `10.1016/0375-9601(76)90101-8`. Full original two-page text: https://www.cfm.brown.edu/people/dobrush/am34/tutorial/AN-EQUATION-FOR-CONTINUOUS-CHAOS_ROSSLER.pdf (dated 12 July 1976).
2. R. Barrio, F. Blesa, A. Dena and S. Serrano, *Qualitative and numerical analysis of the Rössler model: Bifurcations of equilibria*, Computers & Mathematics with Applications **62** (2011), 4140–4150; DOI: `10.1016/j.camwa.2011.09.064`.
3. R. Genesio, G. Innocenti and F. Gualdani, *A global qualitative view of bifurcations and dynamics in the Rössler system*, Physics Letters A **372** (2008), 1799–1809; DOI: `10.1016/j.physleta.2007.10.063`.
4. A. C. Fowler and M. J. McGuinness, *Bursting solutions of the Rössler equations*, ANZIAM Journal (2023); DOI: `10.1017/S144618112300010X`.
