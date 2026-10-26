# Complete stable locking staircase and two critical relaxation laws for an alternating Kuramoto ring

## Finding
For every integer \(m\ge3\), every \(a>0\), and every \(K>0\), consider the \(2m\)-node ring with alternating natural frequencies and equal attractive coupling,
\[
\dot\phi_j=(-1)^j a+K\{\sin(\phi_{j+1}-\phi_j)+\sin(\phi_{j-1}-\phi_j)\},\qquad j\in\mathbb Z/(2m\mathbb Z).
\]
A phase-locked state is an equilibrium in the zero-mean-frequency rotating frame; states are identified only under a common phase rotation. Call it **linearly asymptotically stable modulo rotation** when its symmetric Jacobian has one simple zero eigenvalue and all other eigenvalues are strictly negative.

**Complete classification:** Every such stable state has all nearest-neighbor phase differences in \((-\pi/2,\pi/2)\). There is precisely one stable phase class of winding number \(q\in\mathbb Z\) exactly when
\[
2|q|<m,\qquad K>K_q:=\frac{a}{1+\cos(2\pi q/m)}=\frac{a}{2\cos^2(\pi q/m)}.
\]
No other linearly asymptotically stable equilibria exist. The complete stable-state count is
\[
N_m(K,a)=\sum_{q\in\mathbb Z:\,2|q|<m}{\bf1}\{K>K_q\}.
\]
In particular, the first stable state appears strictly above \(K_0=a/2\); further stable states enter in opposite-winding pairs. As \(K\to\infty\), their number becomes \(m-1\) for even \(m\) and \(m\) for odd \(m\).

For each stable branch, put \(\vartheta=2\pi q/m\) and
\[
d=2\arcsin\!\left(\frac{a}{2K\cos(\vartheta/2)}\right),\qquad
\alpha=\frac{\vartheta+d}{2},\quad \beta=\frac{\vartheta-d}{2},\quad
u=K\cos\alpha,\quad v=K\cos\beta.
\]
Its even-to-odd edge increments are \(\beta\), and its odd-to-even increments are \(\alpha\). Both \(u\) and \(v\) are positive. The full Jacobian spectrum, including multiplicity, is
\[
\lambda_r^\pm=-(u+v)\pm\sqrt{u^2+v^2+2uv\cos(2\pi r/m)},\qquad r=0,\ldots,m-1.
\]
In particular, its positive spectral relaxation gap (the absolute value of the largest strictly negative eigenvalue) is exactly
\[
\gamma_q(K)=u+v-\sqrt{u^2+v^2+2uv\cos(2\pi/m)}.
\]
At the onset of the central winding branch and at every noncentral onset the gaps have **different sharp exponents**. Writing \(K=K_q(1+\varepsilon)\), \(\varepsilon\downarrow0\),
\[
\gamma_0(K)=\sqrt2\,a[1-\cos(\pi/m)]\sqrt\varepsilon+O(\varepsilon^{3/2}),
\]
and, for \(0<2|q|<m\),
\[
\gamma_q(K)=\frac{a[1-\cos(2\pi/m)]}{\sin(2\pi|q|/m)}\,\varepsilon+O(\varepsilon^2).
\]
The threshold configurations themselves have additional zero Jacobian eigenvalues and are not included in the linearly stable count. No claim about their nonlinear stability is made.

## Assumptions and scope
The coupling coefficient multiplying each neighbor sine is \(K\), not \(K/2\). The alternating frequencies have magnitude \(a\). Every vertex and edge is labeled, and only global phase rotations, not graph automorphisms, are identified. Winding number is the integer sum of the principal edge increments divided by \(2\pi\); it is used only after establishing that every stable edge is strictly acute. The theorem treats every real \(K>0\) and integer \(m\ge3\). Stability always means the spectrum of the linearization transverse to the global rotation orbit; it does not assert uniqueness of all equilibria or classify all unstable equilibria.

## Proof
**1. Alternating sine-flow reduction.** Let \(s_j=\sin(\phi_{j+1}-\phi_j)\). The equilibrium equations imply \(K(s_j-s_{j-1})=-(-1)^j a\). Hence all even \(s_j\) share one value and all odd \(s_j\) share another, with \(s_{\mathrm{odd}}-s_{\mathrm{even}}=a/K\). The total natural frequency is zero, so all frequency-locked states have common frequency zero.

**2. Negative or vanishing edge conductance cannot occur in a linearly asymptotically stable state.** The Jacobian is minus the weighted cycle Laplacian with signed edge conductances \(w_j=K\cos(\phi_{j+1}-\phi_j)\). Its quadratic form with sign reversed is \(Q(z)=\sum_j w_j(z_{j+1}-z_j)^2\). If at least two conductances are negative, choose a nonconstant vector constant on the two arcs cut by two negative edges: then \(Q(z)<0\). If one is negative and another is zero, cut at those edges to obtain the same conclusion. If exactly one conductance is negative, of magnitude \(c>0\), and all others are positive, the remaining path has resistance \(R=\sum_{j\ne j_*}1/w_j\). For prescribed unit voltage across the negative edge, the minimum quadratic form is \(R^{-1}-c\). Every other edge of the same parity has equal sine, and therefore has conductance \(+c\) if there is only one negative edge. There are \(m-1\) such edges. For \(m\ge3\), \(R\ge(m-1)/c>1/c\), making the minimum negative. Thus any negative edge implies a positive Jacobian eigenvalue. If no conductance is negative but at least one vanishes, every edge of its parity vanishes because its sine is \(\pm1\). These \(m\) missing edges disconnect the positive-conductance graph, producing more than one zero eigenvalue. A linearly asymptotically stable state must therefore have every edge conductance positive. Conversely, all-positive conductances yield a connected positive weighted Laplacian and exactly one zero eigenvalue.

**3. Winding solutions and exact thresholds.** Strict positivity of each cosine makes the principal inverse sine unique. Write the odd-edge angle as \(\alpha\) and even-edge angle as \(\beta\), each in \((-\pi/2,\pi/2)\). Their sum satisfies \(m(\alpha+\beta)=2\pi q\), so \(\vartheta=\alpha+\beta=2\pi q/m\) and \(2|q|<m\). Since \(\sin\alpha-\sin\beta=a/K>0\), one has \(d=\alpha-\beta>0\), necessarily \(0<d<\pi-|\vartheta|\). The sine identity gives
\[
\frac aK=2\cos(\vartheta/2)\sin(d/2).
\]
The right side is strictly increasing on that open interval from zero to \(2\cos^2(\vartheta/2)=1+\cos\vartheta\). Thus precisely one acute solution exists for each integer winding \(q\) if and only if \(K>K_q\), and none otherwise. Substituting the formula for \(d\) reconstructs it. Different integers have different winding numbers, and no other stable states are possible by Step 2. The count and eventual parity-dependent totals follow immediately.

**4. Spectrum.** Every stable equilibrium has alternating positive edge weights \(u=K\cos\alpha\) and \(v=K\cos\beta\). In an \(m\)-cell Bloch decomposition, the Jacobian matrix at Fourier phase \(t=2\pi r/m\) has diagonal entries \(-(u+v)\) and conjugate off-diagonal entries \(u+v e^{it}\) and \(u+v e^{-it}\). Diagonalization yields the claimed \(\lambda_r^\pm\). The unique zero mode is \(\lambda_0^+=0\). For positive \(u,v\), the second-largest eigenvalue occurs at \(r=1\) or \(r=m-1\), proving the relaxation formula.

**5. Critical exponents.** For \(q=0\), the edge conductances coincide exactly: \(u=v=\sqrt{K^2-a^2/4}\). Consequently \(\gamma_0=2\sqrt{K^2-a^2/4}\,[1-\cos(\pi/m)]\); inserting \(K=(a/2)(1+\varepsilon)\) gives the square-root expansion. For \(q\ne0\), put \(t=2\pi|q|/m\in(0,\pi)\). At the endpoint, exactly one parity of edges reaches angle magnitude \(\pi/2\), while the other has positive conductance \(K_q\sin t\). Writing \(d=\pi-t-\delta\), the sine identity gives \(\delta=2(1+\cos t)\varepsilon/\sin t+O(\varepsilon^2)\). The weaker edge conductance is \(a\varepsilon/\sin t+O(\varepsilon^2)\). Expanding the exact Bloch gap at that weak coupling yields the stated linear law. These expansions use \(m\) and \(q\) fixed as \(\varepsilon\downarrow0\).

## Verification
The accompanying `verify.py` constructs the exact-form branches for every allowable winding of each tested \(m\), calculates the nonlinear vector field and the full numerical Jacobian independently, and compares numerical eigenvalues with the Bloch formula. It also tests the critical scaling constants and the signed-resistance instability witness. Execution completed with `VERIFY_OK`, including 630 branch residual/spectrum tests across ring half-sizes from 3 through 16. These checks test finite instances only. The unrestricted conclusions follow from Steps 1–5, not extrapolation. Run with `python verify.py` in an environment with NumPy and SciPy installed.

## Relationship to prior work
Ochab and Góra, arXiv:0909.0043 (first posted 2009-08-31), developed winding-number and inverse-sine algorithms for locally coupled Kuramoto rings with general/random frequencies; their Section 4 presents an implicit winding test but not this exact alternating-frequency all-size stable-count formula or the two spectral critical exponents. Roy and Lahiri, arXiv:1103.4966 (2011-03-25), described generic ring equilibria including mixed inverse-sine branches and analyzed the general Jacobian; their Section III and IV furnish broader background but do not establish that every mixed branch is unstable for the present alternating family. Tilles, Cerdeira and Ferreira, arXiv:1108.3271 (2011-08-16), Section IV, explicitly analyze the **same** alternating-frequency family for arbitrary even ring size. In particular their equations (49a), (50a) and (51a) parametrize our acute alternating branches and contain the scalar branch equations and transcritical exchanges where strictly acute winding branches meet mixed-angle branches. For ten oscillators they report numerically the exchanges near \(K=0.764\) and \(K=5.236\), matching the present exact \(K_q\) values; the threshold values themselves are **not claimed as separate novelties**. Their Section IV also discusses stability exchanges in low-dimensional symmetry subspaces and says explicitly that these need not imply full-phase-space stability; after calculating full Jacobian behavior for states born at the first threshold, they describe exhaustive full-size stability classification as unresolved (around equations (47)–(51) and the discussion preceding Section V). The present contribution therefore is the proof that **no other mixed-sign edge branch is strictly stable in the full phase space for any ring size or coupling**, yielding an exact global stable-state staircase, **together with the full Bloch relaxation spectrum and distinct square-root versus linear critical gap laws**. It does not claim discovery of the alternating-frequency reduction, the existence of its winding branches, or the known branch equations and specific ten-node crossing thresholds. Standard Bloch theory for 2-periodic weighted graph Laplacians supplies a tool, not the new stability exclusion or coupling-dependent classification. The claimed contribution is the complete all-size *full-phase-space stability exclusion* and exact ensuing stable-state census plus the two distinct critical relaxation exponents. The inverse-sine branches, their existence cutoffs implicit in the 2011 paper, and the weighted Laplacian formalism are not claimed as new.

## Limitations
The result is restricted to even cycles with exactly alternating frequencies of equal magnitude and homogeneous positive nearest-neighbor coupling. It classifies only linearly asymptotically stable equilibria modulo common rotation; the unstable equilibrium census, basins of attraction, nonlinear stability of degenerate threshold equilibria, and general perturbations of detuning are not determined. Priority of a possible earlier all-size full-phase-space stability theorem or an earlier explicit spectral-gap calculation remains uncertain. Tilles et al. (2011), Section IV, already contain the alternating-frequency branch parametrization and sample coupling-crossing thresholds; these components are prior results rather than separate novelty claims. An older closely related article, arXiv:1102.3890, could not be inspected in full and remains a source-access risk. The exact global stability exclusion, consequent all-size strict-stability census, and the paired critical gap laws were not found in the inspected full-text results. The numerical verifier is corroboration, not a formal proof checker or independent scientific audit.

## References
1. J. Ochab and P. F. Góra, *Synchronization of Coupled Oscillators in a Local One-Dimensional Kuramoto Model*, arXiv:0909.0043v1 (2009-08-31), https://arxiv.org/abs/0909.0043.
2. T. K. Roy and A. Lahiri, *Synchronized oscillations on a Kuramoto ring and their entrainment under periodic driving*, arXiv:1103.4966v1 (2011-03-25), https://arxiv.org/abs/1103.4966.
3. P. F. C. Tilles, H. A. Cerdeira and F. F. Ferreira, *Local attractors, degeneracy and analyticity: symmetry effects on the locally coupled Kuramoto model*, arXiv:1108.3271v1 (2011-08-16), https://arxiv.org/abs/1108.3271.
4. P. F. C. Tilles, F. F. Ferreira and H. A. Cerdeira, *Multistable behavior above synchronization in a locally coupled Kuramoto model*, arXiv:1102.3890v1 (2011-02-18), https://arxiv.org/abs/1102.3890.
