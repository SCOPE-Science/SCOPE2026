# A nilpotent cusp and exact algebraic approach at a quadratic scroll equilibrium collision

## Finding
For the quadratic three-dimensional flow
\[
\dot x=y(a-z),\qquad \dot y=z(x-b),\qquad \dot z=x(c+y)-dz,
\]
fix any real parameters \(a,b,c,d>0\) satisfying the natural equilibrium-collision relation \(ad=bc\). Its two nonzero equilibrium branches coalesce at \(E=(b,0,a)\). The merged equilibrium has a nonsemisimple double-zero eigenvalue and is a nilpotent cusp on each sufficiently smooth local center manifold. The cuspidal sector contains a forward-time incoming separatrix with \(y<0\), \(x>b\), and a backward-time outgoing separatrix with \(y<0\), \(x<b\), both tangent to the negative \(y\)-axis in the shifted center coordinates.

Every forward solution on the incoming separatrix satisfies the **exact physical-time limits**
\[
\boxed{\lim_{t\to\infty} t^2 y(t)=-\frac{6d}{ab},\quad
\lim_{t\to\infty} t^3(x(t)-b)=\frac{12d}{a^2b},\quad
\lim_{t\to\infty} t^2(z(t)-a)=-\frac6a.}
\]
The three coefficients are independent of the initial point on that separatrix. In particular the approach is algebraic despite the additional exponentially stable direction.

## Assumptions and scope
All four parameters are strictly positive and satisfy \(ad=bc\). Time is the original autonomous flow time. The claims are local near the nonzero equilibrium \(E\), on a fixed \(C^4\) center manifold; no claim is made about global basins or about arbitrary solutions in the full three-dimensional phase space. The incoming and outgoing curves are germs of trajectories, not assertions that all nearby trajectories converge to \(E\).

## Proof
**1. Collision and spectrum.** The equilibrium equations give the origin and the two standard nonzero branches
\[
E_2=\left(b,\frac{ad-bc}{b},a\right),\qquad
E_3=\left(b,0,\frac{bc}{d}\right).
\]
At \(ad=bc\), they coincide at \(E\); because \(b>0\), the origin is distinct. Put \(u=x-b\), \(v=y\), \(w=z-a\). The **exact** shifted system is
\[
\dot u=-vw,\qquad \dot v=(a+w)u,\qquad
\dot w=cu+bv+uv-dw.
\]
Its Jacobian is
\[
J=\begin{pmatrix}0&0&0\\a&0&0\\c&b&-d\end{pmatrix},
\quad \det(\lambda I-J)=\lambda^2(\lambda+d).
\]
The zero eigenspace is one-dimensional since \(a>0\), while the generalized center subspace is two-dimensional. Thus the zero block is nilpotent of size two and the remaining eigenvalue is \(-d<0\).

**2. Center-manifold jet.** By the smooth center-manifold theorem choose a local \(C^4\) invariant graph \(w=H(u,v)\), with \(H(0,0)=0\). Its first-order expansion is **not** obtained by simply setting \(\dot w=0\), because the center linearization is nilpotent. Instead invariance gives
\[
H(u,v)=\alpha u+\beta v+O((|u|+|v|)^2),\qquad
\beta=\frac bd>0,\quad \alpha=\frac{cd-ab}{d^2}.
\]
Indeed the linear invariance equation is \(a\beta u=cu+bv-d(\alpha u+\beta v)\). Restriction to this graph yields
\[
\dot u=-\beta v^2-\alpha uv+O((|u|+|v|)^3),\qquad
\dot v=a u+O((|u|+|v|)^2).
\]
Consequently, with \(X=v\), \(Y=a u+O(2)\), the leading nilpotent normal form is \(\dot X=Y\), \(\dot Y=-a\beta X^2+O(|XY|+Y^2)+O((|X|+|Y|)^3)\); the nonzero negative quadratic coefficient is the cusp condition. The next step constructs the two actual cuspidal separatrix curves rather than relying only on the classification label.

**3. Weighted blow-up and invariant curves.** In the negative-\(v\) half-plane make the exact weighted substitution
\[
v=-r^2,\qquad u=r^3q,\qquad r>0.
\]
For bounded \(q\), the center graph obeys \(H(r^3q,-r^2)=-\beta r^2+\alpha r^3q+O(r^4)\). Differentiating the blow-up and inserting the restricted equations gives, uniformly for bounded \(q\),
\[
\frac{dr}{dt}=-\frac a2r^2q+O(r^4),\qquad
\frac{dq}{dt}=r\left(\frac{3a}{2}q^2-\beta\right)+O(r^2).
\]
Introduce an increasing desingularized time \(s\) by \(ds/dt=r\). The vector field extends smoothly to \(r=0\) and becomes
\[
\frac{dr}{ds}=-\frac a2rq+O(r^3),\qquad
\frac{dq}{ds}=\frac{3a}{2}q^2-\beta+O(r).
\]
Write \(Q=\sqrt{2\beta/(3a)}>0\). On \(r=0\) there are exactly two fixed points \((0,Q)\) and \((0,-Q)\). Their eigenvalues in the radial and angular directions are respectively
\[
\left(-\frac{aQ}{2},3aQ\right),\qquad
\left(\frac{aQ}{2},-3aQ\right).
\]
Both are hyperbolic saddles. The local stable-manifold theorem gives a unique branch in \(r>0\) asymptotic to \((0,Q)\) as \(s\to+\infty\), of the form \(q=Q+O(r)\). The local unstable-manifold theorem gives a branch in \(r>0\) asymptotic to \((0,-Q)\) in reverse time. Blowing down yields the forward and backward cuspidal separatrix germs. Their signs are determined by \(u=r^3q\), \(v=-r^2\); they lie on opposite sides of \(u=0\). The standard nilpotent cusp local portrait follows from this negative-axis blow-up together with the nonzero quadratic normal-form coefficient. Only the existence and asymptotics of these germs are needed below.

**4. Exact decay along the incoming branch.** Along its forward orbit \(q\to Q\) and
\[
\dot r=-\frac{aQ}{2}r^2(1+o(1)).
\]
Hence \(d(1/r)/dt\to aQ/2\) and \(tr(t)\to 2/(aQ)\), with \(t\to\infty\) rather than a finite escape time. The substitutions \(v=-r^2\), \(u=r^3q\), and \(w=H(u,v)=-\beta r^2+o(r^2)\) give
\[
\begin{aligned}
\lim t^2v&=-\frac{4}{a^2Q^2}=-\frac{6d}{ab},\\
\lim t^3u&=\frac{8}{a^3Q^2}=\frac{12d}{a^2b},\\
\lim t^2w&=-\frac{4\beta}{a^2Q^2}=-\frac6a.
\end{aligned}
\]
These are exactly the three limits claimed. The time origin changes only lower-order terms.

## Verification
The standalone code `verify_cusp.py` uses exact symbolic algebra to check the Jordan polynomial, the correct center-plane tangent, the weighted-blow-up leading vector field, the two desingularized fixed points and their hyperbolic signs, and the three coefficient identities. Running `python verify_cusp.py` yields `CHECK_OK`. These algebraic checks are supplementary: the existence of the actual separatrix curves uses the smooth center-manifold and hyperbolic stable-manifold theorems, explicitly applied above.

## Relationship to prior work
Liu, Wu and Fu (2022, Equation (1) and Section 2) introduce the precise vector field and give the two equilibrium branches that coincide at \(ad=bc\), as well as the linear Jacobians. Their article is directed toward scroll attractors, parameter diagrams and synchronization; the available relevant source material does not establish the nonlinear cusp geometry or these physical-time limits. A later same-system weak-focus analysis treats the **disjoint** spectral region \(bc(bc-ad)>0\) with eigenvalues \(-d,\pm i\omega\); its center-manifold focal coefficients do not imply a result at the present zero-frequency collision \(ad=bc\). General nilpotent-singularity work describes techniques for center manifolds and degeneracies, but does not supply this flow's exact separatrix constants. Access limitations on the original full PDF remain an originality risk, as detailed in the scientific review.

## Limitations
The result asserts neither attraction of an open three-dimensional neighborhood nor global boundedness, stability of chaotic scrolls, periodic orbits, or dynamics off the collision surface. The center manifold is not globally unique, and no assertion of a unique algebraic trajectory in the full three-dimensional phase space is made. The leading coefficients apply to the specified incoming local separatrix only. A complete new-source full-PDF comparison was not possible; this is an originality-access caveat, not a proof step.

## References
1. M. Liu, Z. Wu and X. Fu, “Dynamical Analysis of a One- and Two-Scroll Chaotic System,” *Mathematics* **10** (2022), 4682. DOI: 10.3390/math10244682 (first public date 2022-12-09).
2. S. Song, J. Feng and Q. Wang, “The Center Conditions and Bifurcation of Limit Cycles at the Degenerate Singularity of a Three-Dimensional System,” *Journal of Applied Mathematics* (2014), 546243. DOI: 10.1155/2014/546243 (a different polynomial family).
3. C. Pessoa and L. Queiroz, “Nilpotent centers from analytical systems on center manifolds,” *Journal of Mathematical Analysis and Applications* **525** (2023), 127120. DOI: 10.1016/j.jmaa.2023.127120 (nilpotent-center theory, not this cusp).
