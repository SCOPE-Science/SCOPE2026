# Sharp finite sampling of complex circular-arc function planes at every cardinality

## Finding
Let \(K_\theta=\{e^{it}:-\theta\le t\le\theta\}\), \(0<\theta<\pi\), and \(E_\theta=\operatorname{span}_{\mathbb C}\{1,z\}\subset C(K_\theta)\). For an ordered \(m\)-tuple \(T=(t_1,\ldots,t_m)\) of distinct arc angles define
\[
\mathcal K_\theta(T)=\sup_{(a,b)\ne(0,0)}\frac{\max_{|t|\le\theta}|a+e^{it}b|}{\max_j|a+e^{it_j}b|}.
\]
For every integer \(m\ge3\), let \(s=\sin(\theta/2)\) and let \(x=x_{\theta,m}\) be the unique number in \((0,\theta/2)\) satisfying
\[\sin x=s\cos\bigl(x/(m-1)\bigr).\]
Then
\[\boxed{\min_{|T|=m}\mathcal K_\theta(T)=C_{\theta,m}=\sec\bigl(x/(m-1)\bigr).}\]
The unique unordered minimizing set is the inset equiangular grid
\[\boxed{t_j=-2x+\frac{4x(j-1)}{m-1},\quad1\le j\le m.}\]
The same optimal constant and unique sampling grid apply simultaneously to matrix-valued or bounded-operator-valued affine pencils \(A+zB\) at **every** matrix size (including rectangular matrices):
\[\sup_{|t|\le\theta}\|A+e^{it}B\|\le C_{\theta,m}\max_j\|A+e^{it_j}B\|.\]
The sharp asymptotic and endpoint inset are
\[\lim_{m\to\infty}(m-1)^2(C_{\theta,m}-1)=\frac{\theta^2}{8},\qquad
\lim_{m\to\infty}(m-1)^2(\theta-2x)=\frac{\theta^2}{4}\tan(\theta/2).\]
For any target \(B>1\), the exact minimum number of points **subject to at least three points** is
\[\boxed{M_\theta(B)=1+\max\left\{2,\left\lceil\frac{\arcsin(s/B)}{\arccos(1/B)}\right\rceil\right\}.}\]
For clarity, this is a theorem for \(m\ge3\); the earlier-known two-node optimum is not asserted as new.

## Assumptions and scope
All arc angles are in radians; \(0<\theta<\pi\); knots are arbitrary distinct points on the specified **closed** arc, chosen nonadaptively; the function space consists of all complex affine degree-one polynomials restricted to the arc. The operator norm is the usual norm on bounded operators between arbitrary complex Hilbert spaces. Normalizations use an unscaled unit circle. The allowed nodes do not carry quadrature weights.

## Proof
**1. Scalar-phase reduction.** For scalars \(a,b\),
\[|a+e^{it}b|^2=|a|^2+|b|^2+2|ab|\cos(t-\delta),\]
for some phase \(\delta\). Write \(c=2|ab|/(|a|^2+|b|^2)\in[0,1]\). If the quotient of continuous and sampled squared norms is greater than one, it is increasing in \(c\), since the maximum sampled cosine is smaller than the maximum continuous cosine. If that quotient is one there is no loss. Thus the supremum always occurs at \(c=1\), equivalently \(|a|=|b|\), and equals
\[\max_{\delta\in[-\pi,\pi]}\frac{\max_{|t|\le\theta}|\cos((t-\delta)/2)|}{\max_j|\cos((t_j-\delta)/2)|}.\]
A zero denominator cannot occur for two distinct nodes on an arc shorter than a whole circle.

**2. Universal packing and antipodal obstructions.** Let \(L=t_1\), \(R=t_m\), \(c_0=(L+R)/2\), \(x=(R-L)/4\), and \(g=\max_j(t_{j+1}-t_j)\). The midpoint \(\delta\) of a largest gap lies on the full arc, so the numerator is one. Since the nodes all lie in an arc of angular length less than \(2\pi\), every sampled node is at circular angular distance at least \(g/2\) from that midpoint; hence \(\mathcal K_\theta(T)\ge\sec(g/4)\ge\sec(x/(m-1))\). At the phase opposite to the middle of the extreme nodes, \(\delta=c_0+\pi\pmod{2\pi}\), the largest sampled modulus is precisely \(\sin x\); the supremum along the target arc is at least \(s=\sin(\theta/2)\), with strict inequality when \(c_0\ne0\). Consequently
\[\mathcal K_\theta(T)\ge\max\{\sec(x/(m-1)),\ s/\sin x\},\quad 0<x\le\theta/2.\]
The first term grows strictly in \(x\); the second falls strictly. Their unique intersection lies in the open interval and solves the displayed equation, proving \(\mathcal K_\theta(T)\ge C_{\theta,m}\).

**3. Attainment by the inset grid.** Give the evenly spaced nodes the extremes \(-2x,2x\), and set their common gap \(h=4x/(m-1)\). By symmetry restrict the phase to \(\delta\in[0,\pi]\). If \(0\le\delta\le2x\), a sample is within \(h/2\) in angular distance, so the sampled denominator is at least \(\cos(h/4)\) and the numerator is at most one. If \(2x\le\delta\le\theta\), the nearest sample is the right endpoint; the ratio is at most \(\sec((\delta-2x)/2)\). If \(\theta\le\delta\le\pi\), numerator and sample maximum are \(\cos((\delta-\theta)/2)\) and \(\cos((\delta-2x)/2)\). Their quotient is increasing, since \(\theta>2x\), and its endpoint value is \(\sin(\theta/2)/\sin x\). The global grid constant is therefore exactly \(\max\{\sec(h/4),s/\sin x\}\), equal to \(C_{\theta,m}\) at the balancing root.

**4. Rigidity.** Any optimizer must attain equality in the universal lower bound. Strict monotonicity forces its span parameter to be precisely \(x_{\theta,m}\). A nonzero midpoint \(c_0\) strictly strengthens the antipodal bound, so the span center is zero. Finally, equality in the gap bound forces \(g=4x/(m-1)\), and because the sum of the \(m-1\) gaps is \(4x\), they must all be equal. This uniquely identifies the node set.

**5. All matrix levels.** For unit vectors \(u,v\) in source and target Hilbert spaces, the scalar coefficients \(a=\langle Au,v\rangle\), \(b=\langle Bu,v\rangle\) obey the preceding inequality; take suprema over \(u,v\). Scalar multiplication operators prove sharpness at each matrix level. Equivalently, the inverse of restriction to the optimal nodes has completely bounded norm \(C_{\theta,m}\) for the inherited minimal operator-space structures.

**6. Asymptotics and exact budget.** Set \(n=m-1\). The root identity implies \(x\to\theta/2\), \(\theta/2-x\sim \tan(\theta/2)(\theta/2)^2/(2n^2)\). Expand \(\sec(x/n)\) and multiply by \(n^2\) to obtain \(\theta^2/8\); twice the inset expansion yields \(\theta^2\tan(\theta/2)/4\). Finally, the lower-bound constraints for \(\mathcal K\le B\) require simultaneously \(x\ge\arcsin(s/B)\) and \(x\le n\arccos(1/B)\). The balanced grid achieves the threshold, yielding the exact ceiling formula. The restriction \(n\ge2\) enforces \(m\ge3\).

## Verification
The lower bound is independent of numerical optimization. A supplementary deterministic Python script `check_sampling.py` checks the root equation, closed-form constant and phase supremum on fine grids for multiple arc lengths and node counts. Such finite tests are illustrative; all quantified claims follow from the proof above. The boundary \(\theta=\pi\) is not included.

## Relationship to prior work
The operator-space context is supplied by S. K. Ray, *Unique operator space structures on a family of two dimensional Banach spaces* (2026), arXiv:2610.04608v1. Exact finite sampling is a natural question in the norm-discretization setting studied by Dai–Prymak (2026), arXiv:2610.07679v1; that work concerns multidimensional hyperbolic-cross polynomial spaces, not optimization of these arc pencils. Sommariva–Vianello (2018), arXiv:1802.01711v1, establish subperiodic trigonometric norming meshes with fixed nonsharp constants and O(degree) size, not the exact best cardinality-\(m\) design at degree one. The already-established exact **two-node** arc norming theorem is distinct and explicitly excluded from the new cardinality range. Prior work on best Hilbertian geometry of this family and on arc-extension norms concerns different invariants.

## Limitations
Only complex degree-one affine functions on a proper circular arc are treated; no claim is made for higher-degree subspaces, arbitrary parametrized curves, positive quadrature, numerical stability under noisy samples, or general noncommutative polynomial functions. Equivalence with scalar sampling relies on minimal operator-space norms. Completeness of publication-priority coverage is not independently established; a specialized earlier degree-one Remez/norming theorem may overlap.

## References
- S. K. Ray, *Unique operator space structures on a family of two dimensional Banach spaces*, arXiv:2610.04608v1 (first posted 2026-10-03).
- F. Dai and A. Prymak, *Sampling discretization of the uniform norm for hyperbolic-cross trigonometric polynomials*, arXiv:2610.07679v1 (2026-10-06).
- A. Sommariva and M. Vianello, *Discrete norming inequalities on sections of sphere, ball and torus*, arXiv:1802.01711v1 (2018-02-05).
