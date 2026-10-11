# Sharp interior recurrence boundary and cylinder-or-escape dichotomy in the ES9 flow

## Finding

For the ES9 circular-cylinder flow introduced by Jafari et al. [1], all real parameters \(a,b\) admit an exact classification of whether the open equilibrium-cylinder interior contains a nonempty compact invariant set. For \(a=0\) the answer is no, for every \(b\); for \(a\ne0\) it is yes **if and only if** \(b>1+a^{-2}\). In the exclusion range, every interior trajectory is complete in both time directions and obeys a global alternative: either its height \(z(t)\) tends to \(+\infty\) as \(t\to+\infty\), or its transverse radius tends to the equilibrium cylinder, \(x(t)^2+y(t)^2\to1\). In particular, no periodic orbit or nontrivial compact recurrent dynamics can remain strictly inside the cylinder in the exclusion range. The criterion is sharp because exactly two off-cylinder equilibria lie inside when \(a\ne0\) and \(b>1+a^{-2}\).

## Assumptions and scope

Let \(a,b\in\mathbb R\) and consider the polynomial differential equation on \(\mathbb R^3\):
\[
\begin{aligned}
\dot x&=f(y^2-axy),\\
\dot y&=f xz,\\
\dot z&=f(1-by^2),\\
f&=1-x^2-y^2.
\end{aligned}
\]
The interior \(\Omega=\{(x,y,z):x^2+y^2<1\}\) has \(f>0\). Every point on its boundary \(x^2+y^2=1\) is an equilibrium. A *compact invariant set inside* means a nonempty compact \(K\subset\Omega\) with \(\phi_t(K)=K\) for all \(t\in\mathbb R\), where \(\phi_t\) is the smooth flow restricted to \(\Omega\). The outside of the cylinder is not covered by the recurrence exclusion.

## Proof

**(1) Invariance and completeness.** Differentiating the cylinder factor gives
\[
\dot f=-2fxy(y-ax+z).
\]
Hence, along any finite-time trajectory, \(f(t)=f(0)\exp[-2\int_0^t xy(y-ax+z)\,ds]\), so the sign of \(f\) cannot change in finite time. Within \(\Omega\), \(|x|,|y|<1\) and \(0<f\le1\), giving \(|\dot z|\le1+|b|\). Thus \(z\) grows at most linearly on finite time intervals; the right-hand side remains bounded there. Polynomial local existence and continuation prove two-sided completeness and invariance of \(\Omega\), for every real \(a,b\).

**(2) A strict global Lyapunov identity.** When \(a\ne0\), put \(B=1+a^{-2}\) and \(\Phi=z+2a^{-2}x\). Direct differentiation and completing squares give the exact identity
\[
\boxed{\dot\Phi=f\bigl[f+(x-y/a)^2+(B-b)y^2\bigr].}
\]
For \(b\le B\), this yields \(\dot\Phi\ge f^2>0\) everywhere in \(\Omega\). In the exceptional case \(a=0\), choose instead \(\Phi_0=z+bx\); then \(\dot\Phi_0=f>0\) in \(\Omega\), for every real \(b\). There is no unstated positivity assumption on \(a\) or \(b\).

**(3) Absence of compact invariant interior dynamics.** Under either exclusion hypothesis, suppose \(K\subset\Omega\) were a nonempty compact invariant set. Since \(f\) is continuous and strictly positive on \(K\), it has a positive minimum \(\delta\). The corresponding \(\Phi\) (or \(\Phi_0\)) increases at least at rate \(\delta^2\) (or \(\delta\)) on every complete orbit in \(K\), contradicting boundedness of that function on \(K\). Consequently there is no such \(K\), and in particular no periodic trajectory contained in \(\Omega\).

**(4) Cylinder-or-escape alternative.** The appropriate Lyapunov function increases along every forward interior trajectory. If it diverges to \(+\infty\), then \(z(t)\to+\infty\), since \(|x(t)|<1\). Otherwise it has a finite limit; the identity gives \(\int_0^\infty f(t)^2\,dt<\infty\) (and, for \(a=0\), even \(\int_0^\infty f(t)\,dt<\infty\)). In this second case \(z\) is bounded, since the Lyapunov function is bounded and \(|x|<1\). The formula for \(\dot f\) in (1) then shows that \(f\) is uniformly continuous on \([0,\infty)\). A nonnegative uniformly continuous function with finite square integral tends to zero: otherwise uniform continuity provides infinitely many disjoint intervals on which its square integral is uniformly positive. Hence \(f(t)\to0\), or equivalently \(x(t)^2+y(t)^2\to1\).

**(5) Sharpness and all interior equilibria.** If \(a\ne0\) and \(b>B\), necessarily \(b>0\), and the two points
\[
E_\pm=\left(\pm\frac{1}{a\sqrt b},\;\pm\frac{1}{\sqrt b},\;0\right)
\]
are equilibria, with \(f(E_\pm)=1-B/b>0\); thus each singleton is a compact invariant subset of \(\Omega\). These are the only interior equilibria: \(\dot z=0\) there requires \(y^2=b^{-1}\); \(\dot x=0\) then gives \(x=y/a\), and \(\dot y=0\) gives \(z=0\). If \(a=0\), \(\dot x=0\) requires \(y=0\) while \(\dot z=f\ne0\), so no interior equilibria exist. At \(b=B\) the displayed points lie on, not inside, the equilibrium cylinder; the inequality in (2) remains strict throughout the open interior. This proves both directions, including the endpoint.

## Verification

The included `check_es9.py` is a standalone SymPy script verifying the differential identity for \(f\), both Lyapunov identities, and exact interior/endpoint equilibria for multiple positive and negative rational choices of \(a\). It is invoked with `python check_es9.py`; all assertions must pass. The sign arguments, compactness argument, completeness, and long-time limit are analytic proofs, not consequences of a finite symbolic or numerical test.

## Relationship to prior work

Jafari et al. [1, Table 1, case ES9] introduce this precise cylinder-factor system and give chaotic numerical behavior for the particular parameter values \(a=5\) and \(b=7\), including two isolated equilibria. Li et al. [2, Table 1, case ES9 and discussion] reuse the same core ES9 equations at these fixed parameters while varying the multiplier that creates equilibrium surfaces. Those sources describe the geometry and numerical chaotic regimes; neither inspected analysis derives the sharp all-real-parameter interior compact-invariance criterion, the displayed strict Lyapunov identity, or the cylinder-or-escape conclusion. The algebraic existence of interior equilibria alone would not exclude nonequilibrium compact dynamics below their appearance threshold. The new boundary and global alternative address that additional question.

## Limitations

The proof does not classify trajectories outside \(\Omega\), nor assert that a trajectory approaching the equilibrium cylinder converges to one particular point of it. For \(b>B\), the theorem guarantees compact invariant singletons, not periodic or chaotic motion. It does not establish any chaotic attractor at the cited numerical parameters. Historical priority outside the inspected primary documents and indexed mathematical records is not fully decidable from the available sources. The first verified public date for [1] is its explicitly dated online publication, 27 July 2016; an earlier undated manuscript cannot be excluded.

## References

[1] S. Jafari, J. C. Sprott, V.-T. Pham, C. Volos, and C. Li, “Simple chaotic 3D flows with surfaces of equilibria,” *Nonlinear Dynamics* 86 (2016), 1349–1358, DOI: 10.1007/s11071-016-2968-x; author-hosted full text: https://sprott.physics.wisc.edu/pubs/paper465.pdf.

[2] C. Li, Y. Peng, Z. Tao, J. C. Sprott, and S. Jafari, “Coexisting Infinite Equilibria and Chaos,” *International Journal of Bifurcation and Chaos* 31 (2021), 2130014, DOI: 10.1142/S0218127421300147; author-hosted full text: https://sprott.physics.wisc.edu/pubs/paper512.pdf.
