# A Morse–Bott saddle circle at the exact locking threshold of an alternating four-oscillator ring

## Finding
For the nearest-neighbor four-cycle Kuramoto flow with alternating frequencies \((a,-a,a,-a)\), \(a>0\), and equal edge coupling \(K/2>0\), the entire set of phase-locked configurations, modulo simultaneous rotation of all phases, has the following sharp classification.

If \(0<K<a\) it is empty. If \(K=a\) it is a single point, at which the full Jacobian is zero. If \(K>a\) it is the disjoint union of one hyperbolic sink, one hyperbolic source, and one smooth embedded circle of equilibria. The circle is normally hyperbolic of saddle type, with one positive and one negative transverse eigenvalue at every point.

For \(K>a\) the sink has quotient eigenvalues \(-Kc,-Kc,-2Kc\), and the source has \(Kc,Kc,2Kc\), where \(c=\sqrt{1-a^2/K^2}\). At a point of the circle with flow parameter \(s\in[2a/K-1,1]\), the quotient eigenvalues are
\[
0,\qquad \pm K\sqrt{2-(s-2a/K)^2-s^2}.
\]
The positive transverse eigenvalue attains every value in the **sharp** interval
\[
\left[2\sqrt{a(K-a)},\ \sqrt{2(K^2-a^2)}\right].
\]
Thus a nonisolated one-dimensional family of saddles coexists with a unique attracting locked state for **every** coupling above the exact threshold.

## Assumptions and scope
Index the vertices by \(j\in\mathbb Z/4\mathbb Z\), let \(a>0\), \(K>0\), and consider
\[
\dot\theta_j=(-1)^j a+\frac K2\left(\sin(\theta_{j+1}-\theta_j)+\sin(\theta_{j-1}-\theta_j)\right).
\]
Here \(\theta\in(\mathbb R/2\pi\mathbb Z)^4\). An equilibrium is a locked configuration; the mean frequency is zero. Only the diagonal common-rotation action \(\theta\mapsto\theta+(t,t,t,t)\) is quotiented. No spatial relabeling or other graph symmetry is quotiented, so distinct fixed points and circle points are counted separately. The eigenvalues reported are those on the resulting three-dimensional smooth quotient. All stability assertions for \(K>a\) are local orbital assertions relative to uniform phase rotation. At \(K=a\) only complete *linear* degeneracy is asserted.

## Proof
**1. Reduction to alternating edge flows.** Put \(d_j=\theta_{j+1}-\theta_j\pmod{2\pi}\) and \(b_j=\sin d_j\). Then an equilibrium satisfies
\[
0=(-1)^j a+\frac K2(b_j-b_{j-1}),\qquad
\sum_{j=0}^3d_j\equiv0\pmod{2\pi}.
\]
Consequently, for some real \(s\),
\[
b_0=b_2=s-2a/K,\qquad b_1=b_3=s,
\]
with precisely \(2a/K-1\le s\le1\). The interval is empty if \(K<a\), a singleton if \(K=a\), and has nonempty interior if \(K>a\). A tuple of four edge angles whose sum is an integer multiple of \(2\pi\) determines exactly one configuration modulo uniform phase, so this reduction has no missing gauge freedom.

**2. Complete branch and topology census.** Assume \(K>a\) and define \(\alpha(s)=\arcsin(s-2a/K)\), \(\beta(s)=\arcsin s\), taking values in \([ -\pi/2,\pi/2]\). Each even edge has angle either \(\alpha\) or \(\pi-\alpha\), each odd edge either \(\beta\) or \(\pi-\beta\). For each pair of opposite edges, the sum is either twice the principal angle, twice its supplementary angle, or exactly \(\pi\) when one of each is taken. If both pairs use principal choices, closure requires \(\alpha+\beta=0\) (because \(-\pi<\alpha+\beta<\pi\)), and hence \(s=a/K\). This yields the unique isolated principal solution with edge tuple \(( -\gamma,\gamma,-\gamma,\gamma)\), where \(\gamma=\arcsin(a/K)\). If both pairs are supplementary, the same equation gives the unique isolated complementary solution \((\pi+\gamma,\pi-\gamma,\pi+\gamma,\pi-\gamma)\).

If one opposite pair is principal on both edges and the other supplementary on both edges, closure would force \(\alpha-\beta\equiv0\pmod\pi\), impossible for interior \(s\) because \(-\pi<\alpha-\beta<0\). If both opposite pairs use one principal and one supplementary angle, their total sum is exactly \(2\pi\), regardless of \(s\). These are four smooth open arcs indexed by the independent choices of which even and which odd edge is supplementary. At the left endpoint \(s=2a/K-1\), the two even-edge options coincide, joining the arcs in pairs; at the right endpoint \(s=1\), the odd-edge options coincide, joining them in the other pairing. Mixed/same choices can occur only at these endpoints and represent the same existing endpoint configurations. The resulting four-edge cycle of arcs is a connected embedded circle. Smoothness at the joins follows by using the even-edge angle, respectively odd-edge angle, as local coordinate: the other sine has magnitude strictly less than one, so its angle is smoothly determined. This proves that the list is exhaustive.

When \(K=a\), the only permissible flow is \(s=1\); both even differences equal \(-\pi/2\) and both odd differences equal \(\pi/2\) modulo \(2\pi\). There is exactly one quotient equilibrium and every edge cosine vanishes.

**3. Jacobian and transverse Morse–Bott type.** For an equilibrium with edge cosines \(w_j=\cos d_j\), let \(L(w)\) be the weighted cycle Laplacian \(L_{jj}=w_{j-1}+w_j\), \(L_{j,j+1}=-w_j\) and \(L_{j,j-1}=-w_{j-1}\). The Jacobian is \(-K L(w)/2\). At the principal solution all weights equal \(c=\sqrt{1-a^2/K^2}\), so the full eigenvalues are \(0,-Kc,-Kc,-2Kc\). At the complementary solution all weights equal \(-c\), so they are \(0,Kc,Kc,2Kc\). The zero eigenvalue in both cases corresponds only to common rotation.

On every mixed/mixed arc, the weights can be written \((x,y,-x,-y)\) with \(x^2=1-(s-2a/K)^2\) and \(y^2=1-s^2\). The characteristic polynomial of \(L\) is **exactly**
\[
\det(zI-L)=z^2\bigl(z^2-4(x^2+y^2)\bigr).
\]
Thus the full Jacobian has eigenvalues \(0,0,\pm K\sqrt{x^2+y^2}\). One zero is the uniform rotation direction and the other is tangent to the circle. Since \(a/K\in(0,1)\), the two cosines cannot vanish simultaneously, so the normal eigenvalues are nonzero and have opposite signs everywhere. The circle is a normally hyperbolic equilibrium manifold of saddle type.

The square of the positive transverse exponent is \(K^2[2-(s-2a/K)^2-s^2]\), a concave quadratic on \([2a/K-1,1]\). Its maximum is achieved at \(s=a/K\) and is \(2(K^2-a^2)\); its equal endpoint minima are \(4a(K-a)\). Continuity gives exactly the claimed sharp interval.

## Verification
The included `verify.py` runs a symbolic SymPy characteristic-polynomial identity and reconstructs all sixteen inverse-sine branches for six independent values of \(K/a>1\), verifying four interior circle branches, both isolated solutions, the sine-balance equations, winding closure, and the exact normal-exponent bounds at thirty interior parameters. It independently checks the unique critical configuration and verifies the complete zero Jacobian at \(K=a\). Execute `python verify.py` with a Python 3 interpreter and SymPy installed. The numerical branch samples corroborate, but do not replace, the universal branch exhaustion in the proof; the symbolic determinant is exact.

## Relationship to prior work
Roy and Lahiri (2011) formulate the same nearest-neighbor Kuramoto ring and derive a general one-parameter inverse-sine approach to locked solutions, but focus on broad branch analysis and a worked three-node example rather than this exact four-node alternating-frequency equilibrium topology. Mehta et al. (2014) use algebraic methods to study equilibria and stability on general graphs. Delabays, Coletta and Jacquod (2015) develop circulation-flow methods and stable-locking bounds on single cycles, treating at most one large angle as relevant for stable equilibria; they do not state the alternating four-cycle's *full* nonisolated saddle family and its transverse spectrum in the relevant sections inspected. Sclosa (2021) studies completely degenerate Kuramoto equilibria; the isolated threshold configuration here fits that general framework, but the global three-piece equilibrium set above threshold is a separate statement.

## Limitations
This classification holds only for the four-cycle, equal edge coupling, exactly alternating frequencies, and positive \(a,K\). It does not assert persistence of the equilibrium circle under generic perturbation; such a symmetry-dependent continuum can split. The single equilibrium at threshold is fully linearly degenerate, so this statement alone does not determine its nonlinear stability. Local normal spectra do not classify global attraction basins or transient dynamics. Earlier unindexed special-case calculations could affect historical priority.

## References
1. T. K. Roy and A. Lahiri, *Synchronized oscillations on a Kuramoto ring and their entrainment under periodic driving*, arXiv:1103.4966v1 (2011-03-25), especially equations (1), (7)–(10), and the stability matrix (11).
2. D. Mehta, N. S. Daleo, F. Dörfler and J. D. Hauenstein, *Algebraic Geometrization of the Kuramoto Model: Equilibria and Stability Analysis*, arXiv:1412.0666v1 (2014-12-01).
3. R. Delabays, T. Coletta and P. Jacquod, *Multistability of Phase-Locking and Topological Winding Numbers in Locally Coupled Kuramoto Models on Single-Loop Networks*, arXiv:1512.04266v1 (2015-12-14), sections III–IV.
4. D. Sclosa, *Completely Degenerate Equilibria of the Kuramoto Model on Networks*, arXiv:2112.12034v1 (2021-12-22), example of the four-cycle and nonzero-frequency degeneracy.
