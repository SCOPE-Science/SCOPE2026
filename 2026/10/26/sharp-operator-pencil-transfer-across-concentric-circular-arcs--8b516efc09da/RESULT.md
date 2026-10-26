# Sharp operator-pencil transfer across concentric circular arcs

## Finding
Fix \(0<\theta<\varphi<\pi\). For arbitrary complex normed spaces \(X,Y\) and bounded operators \(A,B:X\to Y\), the **sharp dimension-free** constant in the degree-one pencil inequality is
\[
\boxed{\displaystyle\sup_{|t|\le\varphi}\|A+e^{it}B\|\le\frac{\sin(\varphi/2)}{\sin(\theta/2)}\sup_{|t|\le\theta}\|A+e^{it}B\|.}
\]
The coefficient is attained by \(A=-B\ne0\), including for complex scalars. In the scalar case, for nonzero \((a,b)\), equality holds precisely when \(a=-b\ne0\).

Let \(K_\psi=\{e^{it}:|t|\le\psi\}\) and \(E_\psi=\operatorname{span}_{\mathbb C}\{1,z\}\subset C(K_\psi)\), with the inherited minimal operator-space structure. The coefficient-preserving map
\[
J_{\theta,\varphi}:E_\theta\longrightarrow E_\varphi,\qquad a+bz\longmapsto a+bz
\]
has exact norm and completely bounded norm
\[
\boxed{\|J_{\theta,\varphi}\|=\|J_{\theta,\varphi}\|_{\mathrm{cb}}=\frac{\sin(\varphi/2)}{\sin(\theta/2)}}.
\]
The reverse coefficient map has both norms exactly one. The displayed factor is therefore the sharp distortion of this **specific marked** isomorphism. It is not asserted to be the unrestricted Banach--Mazur or complete Banach--Mazur distance.

## Assumptions and scope
The angles satisfy \(0<\theta<\varphi<\pi\); no degenerate singleton arc occurs. The operators may act between different complex normed spaces and need not be normal, compact, finite-dimensional, or even operators on a Hilbert space. Their operator norm is the standard induced norm. For arbitrary matrix levels, \(E_\psi\) inherits the matrix norm \(\|(C_{ij}+e^{it}D_{ij})\|_{M_n(C(K_\psi))}=\max_{|t|\le\psi}\|(C_{ij}+e^{it}D_{ij})\|_{M_n}\). The phrase "marked" refers to the distinguished ordered generators \(1,z\), which determine the map \(J\). A different linear change of basis is not optimized over.

## Proof
**1. Exact scalar arc profile.** Take \(a,b\in\mathbb C\). If either vanishes the arc suprema coincide and the claimed estimate follows. Otherwise put \(\alpha=|a|>0\), \(\beta=|b|>0\), and choose \(\delta\in\mathbb R/(2\pi\mathbb Z)\) so that \(a\) and \(be^{i\delta}\) have opposite phases. With \(d\in[0,\pi]\) the shortest circular angular distance between \(\delta\) and the arc midpoint \(0\), one has
\[
|a+be^{it}|^2=(\alpha-\beta)^2+4\alpha\beta\sin^2\!\left(\frac{t-\delta}{2}\right).
\]
For \(0<\psi<\pi\), the largest circular angular distance from \(\delta\) to a point in \([-\psi,\psi]\) is exactly \(\min\{\pi,d+\psi\}\): until the antipodal point becomes available, the more distant endpoint realizes it; after that, the arc contains an antipode. Consequently, writing
\[
H_\psi(d)=\sin^2\!\left(\frac{\min\{\pi,d+\psi\}}2\right),
\]
we have the **exact** profile
\[
M_\psi(a,b)^2:=\max_{|t|\le\psi}|a+be^{it}|^2=(\alpha-\beta)^2+4\alpha\beta H_\psi(d).
\]

**2. Sharp two-arc comparison.** Since \(\varphi>\theta\), we have \(H_\varphi(d)\ge H_\theta(d)>0\). For any \(c\ge0\) and \(q>0\),
\[
\frac{c+qH_\varphi(d)}{c+qH_\theta(d)}\le\frac{H_\varphi(d)}{H_\theta(d)}.
\]
We claim that the final ratio decreases strictly with \(d\) while it exceeds one. For \(0\le d<\pi-\varphi\), it equals
\[
\frac{\sin^2((d+\varphi)/2)}{\sin^2((d+\theta)/2)};
\]
its logarithmic derivative is \(\cot((d+\varphi)/2)-\cot((d+\theta)/2)<0\). For \(\pi-\varphi\le d<\pi-\theta\), its numerator is one and its denominator increases strictly. For \(d\ge\pi-\theta\), the ratio equals one. Thus its largest value occurs only at \(d=0\), and is \(\sin^2(\varphi/2)/\sin^2(\theta/2)\). Taking square roots proves the scalar inequality. Equality, because the coefficient is greater than one, forces \(\alpha=\beta\) and \(d=0\), equivalently \(a=-b\ne0\). Conversely such a pair attains the ratio because \(\max_{|t|\le\psi}|1-e^{it}|=2\sin(\psi/2)\).

**3. Operator pencil by dual scalarization.** For each unit vector \(x\in X\) and norm-one functional \(y^*\in Y^*\), apply the scalar inequality to \(a=y^*(Ax)\), \(b=y^*(Bx)\). Then
\[
\max_{|t|\le\varphi}|y^*((A+e^{it}B)x)|\le \frac{\sin(\varphi/2)}{\sin(\theta/2)}\sup_{|t|\le\theta}\|A+e^{it}B\|.
\]
Supremizing over \(x,y^*\), then over the outer arc, gives the operator claim by the complex Hahn--Banach norm formula. Its constant is sharp for \(A=-B\ne0\) on any nonzero normed space.

**4. Completely bounded arc transfer.** The scalar case identifies \(\|J_{\theta,\varphi}\|\). For any matrix size \(n\), take \(A,B\in M_n(\mathbb C)\) in step 3. The displayed operator-pencil inequality is precisely \(\|J_{\theta,\varphi}^{(n)}(A+Bz)\|\le K\|A+Bz\|\). Taking the supremum over sizes proves \(\|J\|_{\mathrm{cb}}\le K\), while scalar equality yields the reverse bound. Restriction from the larger arc to the smaller has cb norm one: it cannot increase any matrix supremum, and it fixes the constant function. This completes all assertions.

## Verification
The proof gives exact formulas for the scalar suprema and the worst phase; no numerical optimization establishes the infinite-dimensional result. The standalone `verify_arc_transfer.py` evaluates a deterministic family of random complex \(2\times2\) pencils at five angle pairs using finely sampled angular grids (405 checks including exact sharpness cases). The successful checks only corroborate the analytic argument, and a sampled grid is not an exhaustive certificate. The exact sharp witness \(A=-B\) is established symbolically, for every pair of eligible angles.

## Relationship to prior work
Ray's 2026 paper introduces the spaces \(E_\theta\), proves uniqueness of their operator-space structure and establishes that distinct arc angles yield non-isometric complex Banach planes. Ray's isometry classification does not determine the norm of the concrete coefficient-preserving comparison \(J_{\theta,\varphi}\). The exact optimal Hilbertian quadratic form for each individual arc (published in [2]) quantifies the distance from one \(E_\theta\) to a Hilbert plane, rather than the sharp norm of a **fixed** map between two different arcs. The broader Remez and Bernstein literature concerns polynomial control and derivatives on arcs; those results may supply an alternative route to this degree-one bound, but the inspected accessible source descriptions do not explicitly state the two-arc operator-pencil identity or its equality and completely bounded consequences. This is a claim of distinct mathematical content, not absolute bibliographic priority.

## Limitations
The exact distortion belongs to the **coefficient-preserving** map, not to an arbitrary isomorphism or the intrinsic Banach--Mazur metric; a change of basis can substantially reduce the distortion when an arc is very short. The operator-pencil estimate has degree one: no bound of this simple sine-ratio form is asserted for higher-degree polynomials. The full text of every older arc Remez paper was not compared, so a prior equivalent inequality under approximation-theory terminology remains a residual priority risk. The matrix-level result follows from scalar duality rather than introducing a new matrix extremum.

## References
[1] S. K. Ray, *Unique operator space structures on a family of two dimensional Banach spaces*, arXiv:2610.04608v1, first public 2026-10-03, https://arxiv.org/html/2610.04608v1.

[2] *The unique optimal Hilbertian metric for circular-arc function planes freezes at a semicircle*, published mathematical result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-unique-optimal-hilbertian-metric-for-circular-arc-function-p--c1c0ee781ccd.

[3] S. Kalmykov and B. Nagy, *Polynomial and rational inequalities on analytic Jordan arcs and domains*, Journal of Mathematical Analysis and Applications 430 (2015), 874--894, arXiv:1408.1601.

[4] P. Borwein and T. Erdélyi, *Sharp extensions of Bernstein's inequality to rational spaces*, Mathematika 43 (1996), 413--423, DOI:10.1112/S0025579300011876.
