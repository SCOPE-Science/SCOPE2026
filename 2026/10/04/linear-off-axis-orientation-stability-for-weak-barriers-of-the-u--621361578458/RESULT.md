# Linear off-axis orientation stability for weak barriers of the unit cube
## Finding
For every integer \(n\ge 3\), let \(Q_n=[-1/2,1/2]^n\), let \(B\) be an \((n-1)\)-dimensional rectifiable weak barrier for \(Q_n\), and let \(\mu=S^*(B,\cdot)\) be its orientation measure. Write
\[
\delta=S(B)-n\ge0.
\]
For \(0<\beta<\pi/4\), let
\[
J_\beta=\{v\in S^{n-1}:\angle(v,\pm e_i)>\beta\text{ for every }i\}.
\]
Then
\[
S^*(B,J_\beta)
\le
\frac{(\sqrt n+1)^2}{\sin^2\beta\,\cos^2\beta}\,\delta.
\]
Thus the orientation mass whose normals stay a fixed positive angle away from all cube facet normals is controlled linearly by the Jones deficit. Every rectifiable barrier is a weak barrier, so the same estimate applies to rectifiable barriers.

## Assumptions and scope
The cube has side length one and is centered at the origin. The surface area convention is the one for which \(S^*(B,S^{n-1})=2S(B)\). A weak barrier is understood through projection multiplicities: for every unit vector \(u\), its total projected \((n-1)\)-area is at least the projected \((n-1)\)-area of \(Q_n\). The estimate is asserted for \(n\ge3\) because the planar unit-square case already has a sharper linear estimate in the literature.

The constant above is explicit but is not claimed to be optimal in either \(n\) or \(\beta\). No assertion is made about existence of barriers whose area approaches Jones' bound.

## Proof
By the weak-barrier projection inequality and the coarea representation of the orientation measure,
\[
\frac12\int_{S^{n-1}}|\langle u,v\rangle|\,\mu(\mathrm dv)
\ge
\mathcal H^{n-1}(Q_n|u^\perp)
\qquad (u\in S^{n-1}).
\]
The surface area measure of the unit cube has one unit atom at each \(\pm e_i\), so Cauchy's projection formula gives
\[
\mathcal H^{n-1}(Q_n|u^\perp)=\sum_{i=1}^n|u_i|.
\]
For a sign vector \(s\in\{\pm1\}^n\), take \(u_s=s/\sqrt n\). The preceding inequality becomes
\[
\int_{S^{n-1}}|\langle s,v\rangle|\,\mu(\mathrm dv)\ge2n.
\]
Average this over all sign vectors and define
\[
\Phi(v)=2^{-n}\sum_{s\in\{\pm1\}^n}|\langle s,v\rangle|
       =\mathbb E_\varepsilon\left|\sum_{i=1}^n\varepsilon_i v_i\right|.
\]
For \(v\in S^{n-1}\), the Rademacher sum \(X=\sum_i\varepsilon_i v_i\) satisfies \(\mathbb E X^2=1\), hence \(\Phi(v)\le1\). Since \(\mu(S^{n-1})=2S(B)=2n+2\delta\), the averaged projection inequalities yield
\[
\int_{S^{n-1}}(1-\Phi(v))\,\mu(\mathrm dv)\le2\delta. \tag{1}
\]

Set \(q(v)=\sum_i v_i^4\). The exact fourth-moment identity is
\[
\mathbb E X^4=3-2q(v),
\]
so
\[
\mathbb E(X^2-1)^2=2(1-q(v)).
\]
Also \(|X|\le\|v\|_1\le\sqrt n\), and therefore
\[
(X^2-1)^2=(|X|-1)^2(|X|+1)^2
\le(\sqrt n+1)^2(|X|-1)^2.
\]
Taking expectations and using
\[
\mathbb E(|X|-1)^2=2(1-\Phi(v))
\]
gives the pointwise deficit estimate
\[
1-\Phi(v)\ge\frac{1-q(v)}{(\sqrt n+1)^2}. \tag{2}
\]

Now let \(v\in J_\beta\), and put \(c=\cos\beta\). Then \(|v_i|<c\) for every \(i\). With \(a_i=v_i^2\), we have \(a_i\ge0\), \(\sum_i a_i=1\), and \(a_i\le c^2\). Because \(0<\beta<\pi/4\), one has \(c^2>1/2\). By transferring mass toward larger coordinates, the convex quantity \(\sum_i a_i^2\) is maximized under these constraints by the vector with entries \(c^2\), \(1-c^2\), and zeros. Hence
\[
q(v)\le c^4+(1-c^2)^2,
\]
and therefore
\[
1-q(v)\ge2c^2(1-c^2)=2\sin^2\beta\,\cos^2\beta. \tag{3}
\]
Combining (2) and (3), every \(v\in J_\beta\) obeys
\[
1-\Phi(v)\ge
\frac{2\sin^2\beta\,\cos^2\beta}{(\sqrt n+1)^2}.
\]
Integrating this lower bound over \(J_\beta\) and applying (1) gives
\[
\frac{2\sin^2\beta\,\cos^2\beta}{(\sqrt n+1)^2}\,\mu(J_\beta)
\le2\delta,
\]
which is the claimed estimate.

## Verification
The proof is analytic and uses only the weak-barrier projection inequality, the unit-cube projection formula, elementary Rademacher moments, and a finite-dimensional convex maximization. The accompanying script `artifacts/verify.py` independently checks the exact second- and fourth-moment identities by exhaustive sign enumeration for many integer coefficient vectors and checks the derived pointwise inequalities on a deterministic grid. These computations are consistency checks; they are not substituted for the universal proof above.

## Relationship to prior work
Kiderlen introduced the higher-dimensional weak-barrier framework and proved a general stability theorem. For polytopes, Corollary 1.4 gives an off-facet-normal estimate with Jones-deficit exponent
\[
\frac{2(n+1)}{n(n+4)}-\varepsilon,
\]
with a constant depending on additional parameters. The same paper specializes the discussion to the centered unit cube and explicitly notes that the exponent can be improved; it quotes a direct linear estimate only in dimension two. The present result supplies a linear estimate for the natural cube orientation defect in every dimension \(n\ge3\), with an explicit constant, by exploiting all diagonal sign directions simultaneously.

Steinerberger's earlier stability theorem is planar, and his special unit-square proposition is also planar. Kiderlen and Pausinger's subsequent lower-bound work concerns the planar unit square and unit disc. Recent stability results for Khintchine-type inequalities concern different moment regimes and do not state this weak-barrier consequence.

## Limitations
The coefficient \((\sqrt n+1)^2/(\sin^2\beta\cos^2\beta)\) is obtained from the crude uniform bound \(|X|\le\sqrt n\) and is unlikely to be sharp. The result controls orientation mass only; it does not incorporate the spatial placement of the barrier patches and therefore does not itself improve the best known lower bound for the minimum barrier area of the cube. It also does not settle the optimal quantitative stability law for general convex bodies.

## References
1. Markus Kiderlen, *Stability for barriers of n-dimensional convex bodies with surface area close to Jones' bound*, arXiv:2605.13449, first public version 13 May 2026.
2. Stefan Steinerberger, *A Stability Version of the Jones Opaque Set Inequality*, arXiv:2501.01004, 2025.
3. Markus Kiderlen and Florian Pausinger, *Explicit lower bounds for opaque sets of unit square and unit disc*, arXiv:2509.08842, 2025.
4. Ángel Chávez and Sam Sheng, *Stability of Khintchine-type inequalities via log-monotonicity*, arXiv:2606.19313, 2026.
