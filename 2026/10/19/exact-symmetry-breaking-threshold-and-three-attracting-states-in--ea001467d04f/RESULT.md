# Exact symmetry-breaking threshold and three attracting states in a two-agent opinion–leadership model

## Finding
For the original opinion–leadership differential equations of Alutto, Zino, Johansson and Fontan (arXiv:2603.24381), restrict to two agents who listen only to each other and whose initial opinion anchors are opposite, \( (a,-a)\), with \(0<a\leq1\). Let \(\rho=\alpha/\beta>0\). The anchored vector field has exactly three nonzero equilibria if \(0<\rho\leq16\), and exactly five if \(\rho>16\). Together with the origin these give four or six equilibria in the admissible state cube, respectively. The opposed-opinion symmetric equilibrium is linearly unstable for \(\rho<16\), nonhyperbolic at \(\rho=16\), and locally exponentially attracting for \(\rho>16\). The two additional equilibria appearing for \(\rho>16\) are symmetry-broken and have opposite-sign opinions. At the exact admissible parameters \(a=1\), \(\alpha=1/4\), \(\beta=1/100\), exactly three of the five nonzero equilibria are locally exponentially attracting, and the other two are linearly unstable. Thus identical, opposed opinion anchors support a three-attractor phase portrait in the corresponding autonomous anchored vector field; no claim of global attraction or of basin intersection with every physically prescribed initial state is made.

## Assumptions and scope
Fix \(0<a\leq1\), \(\alpha,\beta>0\), and the row-stochastic interaction matrix \(W=\begin{pmatrix}0&1\\1&0\end{pmatrix}\). Fix the initial-opinion *anchors* \(x_1(0)=a\), \(x_2(0)=-a\) as the parameters entering the autonomous right-hand side. With opinion states \(X,Z\in[-a,a]\) and leadership states \(u,v\in[0,1]\), the resulting frozen-anchor dynamical system is
\[
\begin{aligned}
\dot X&=-(1-u)(X-Z)-u(X-a),\\
\dot Z&=(1-v)(X-Z)-v(Z+a),\\
\dot u&=\alpha(1-u)X^2-\beta u(X-Z)^2,\\
\dot v&=\alpha(1-v)Z^2-\beta v(X-Z)^2.
\end{aligned}
\]
The state cube is forward invariant. Equilibrium and local stability mean equilibrium and eigenvalues of this four-dimensional autonomous vector field **with those fixed anchors**. Actual model trajectories also obey the separate constraint that their opinion coordinates initially equal the anchors; the local phase portrait does not by itself establish which equilibrium basins intersect that constrained initial-data plane.

Let \(t=\sqrt\rho\). Define the symmetric equilibrium
\[
E_{\mathrm{pol}}=\left(\frac{a\rho}{\rho+8},-\frac{a\rho}{\rho+8},\frac\rho{\rho+4},\frac\rho{\rho+4}\right).
\]
For either admissible \(s>0\), set \(h(s)=\sqrt{s(4a-3s)}\) and define
\[
E_s^{\pm}=\left(\frac{s\pm h(s)}2,\frac{-s\pm h(s)}2,
\frac{s}{a-(-s\pm h(s))/2},\frac{s}{a+(s\pm h(s))/2}\right).
\]
There are always two same-sign-opinion equilibria \(E_{s_-}^{\pm}\), with \(s_-=at/(t+1)<a\). If \(t>4\), there are also two opposite-sign asymmetric equilibria \(E_{s_+}^{\pm}\), with \(s_+=at/(t-1)\in(a,4a/3)\). At \(t=4\), \(E_{s_+}^{+}=E_{s_+}^{-}=E_{\mathrm{pol}}\), so these are not two extra distinct equilibria. The signs label symmetry-related states, not stability.

## Proof
**1. Exhaustion of admissible equilibria.** At equilibrium put \(s=X-Z\). The first two equations imply
\[
s=u(a-Z)=v(a+X).
\]
Since \(a-Z\geq0\) and \(a+X\geq0\), one has \(s\geq0\). If \(s=0\), the leadership equations and the two anchors force \((X,Z,u,v)=(0,0,0,0)\): for a common nonzero opinion both leaderships would have to equal one, contradicting their distinct anchors. If \(s>0\), necessarily \(0<u,v<1\), \(|X|,|Z|<a\), and \(XZ\ne0\). In particular neither boundary-leadership state can be an unlisted equilibrium. Write \(p=X\) and \(q=-Z\); then \(p+q=s>0\). Eliminating \(u=s/(a+q)\) and \(v=s/(a+p)\) from the two leadership equations gives
\[
\alpha(a-p)p^2=\beta s^3=\alpha(a-q)q^2.
\]
The equality of the left and right cubic factors is precisely
\[
(p-q)\big(a(p+q)-(p^2+pq+q^2)\big)=0.
\]
If \(p=q\), then \(s=2p\) and \(\rho(a-p)=8p\); this yields exactly \(E_{\mathrm{pol}}\).

If \(p\ne q\), the factor in parentheses vanishes. Consequently \(pq=s(s-a)\) and the quadratic with roots \(p,q\) has discriminant \(s(4a-3s)\). Indeed, \(a-p=q^2/s\) because \(as=p^2+pq+q^2\), and therefore \((a-p)p^2=(pq)^2/s=s(a-s)^2\). Since \(\alpha(a-p)p^2=\beta s^3\), it follows that
\[
\rho=\frac{s^2}{(a-s)^2}.
\]
The branch \(s<a\) has the unique solution \(s_-=at/(t+1)\); its two roots have opposite signs, so \(X,Z\) have the same sign. The branch \(s>a\) has \(s_+=at/(t-1)\), and the discriminant is real precisely when \(t\geq4\). At \(t=4\) the two roots coincide and give the symmetric equilibrium. When \(t>4\), the two distinct roots are positive, giving opposite-sign opinions. Directly \(h(s)<2a-s\) for \(s\ne a\), so all the stated roots lie strictly inside the opinion cube. The rational formulas for \(u,v\) lie strictly between zero and one by the equilibrium identities. This exhausts every admissible equilibrium.

**2. Sharp symmetric stability boundary.** Let \(r=a\rho/(\rho+8)\) and \(y=\rho/(\rho+4)\). By exchange-and-negation symmetry the Jacobian at \(E_{\mathrm{pol}}\) decomposes into an invariant polarized sector and a transverse sector. The polarized sector has eigenvalues \(-(2-y)\) and \(-(\alpha+4\beta)r^2\), both negative. The transverse sector is the real matrix
\[
B=\begin{pmatrix}-y&a+r\\2\alpha(1-y)r&-(\alpha+4\beta)r^2\end{pmatrix}.
\]
Its trace is negative and its determinant simplifies exactly to
\[
\det B=\frac{\beta a^2\rho^2(\rho-16)}{(\rho+8)^2}.
\]
Thus for \(\rho<16\), \(B\) has a positive eigenvalue; at \(\rho=16\), it has a zero eigenvalue; and for \(\rho>16\), both transverse eigenvalues have negative real part. This proves the stated sharp linear-stability exchange (without asserting nonlinear stability at the degenerate equality).

**3. Three rigorously attracting states at one exact parameter point.** Put \(a=1\), \(\alpha=1/4\), \(\beta=1/100\), so \(\rho=25\). The symmetric state is \((25/33,-25/33,25/29,25/29)\). At each same-sign state the Jacobian has the *same* monic characteristic polynomial
\[
P_{\mathrm{same}}(z)=z^4+\frac{325}{144}z^3+\frac{2020873}{1264896}z^2+\frac{78161}{210816}z+\frac5{192}.
\]
All four coefficients are positive. The two remaining Routh–Hurwitz determinants for a monic quartic, in the conventional notation \(P=z^4+c_1z^3+c_2z^2+c_3z+c_4\), equal
\[
c_1c_2-c_3=\frac{589252621}{182145024}>0,
\]
\[
c_1c_2c_3-c_3^2-c_1^2c_4
=\frac{40962897209981}{38399085379584}>0.
\]
Therefore both same-sign equilibria are exponentially attracting. The characteristic polynomial at the symmetric state factors as
\[
P_{\mathrm{pol}}(z)=\frac{(29z+33)(4356z+725)(126324z^2+129925z+6525)}{15957752976},
\]
so it, too, is exponentially attracting. Finally, at each of the two opposite-sign asymmetric states,
\[
P_{\mathrm{cross}}(z)=z^4+\frac{145}{64}z^3+\frac{238993}{167936}z^2+\frac{12923}{83968}z-\frac5{512}.
\]
Since \(P_{\mathrm{cross}}(0)<0\) and \(P_{\mathrm{cross}}(z)\to+\infty\) as \(z\to+\infty\), each has a positive real eigenvalue and is unstable. The origin, whose behavior is not needed for the three-attractor claim, is the sole remaining equilibrium. All polynomial identities are exact and can be independently reproduced by the accompanying symbolic checker.

## Verification
Run `python verify.py` with Python 3 and SymPy. It reconstructs the vector field and its full four-by-four Jacobian, verifies the exact zero-residual formulas for all representative branches, rederives the three characteristic polynomials using algebraic number \(\sqrt5\), and checks the exact quartic Hurwitz inequalities. These finite symbolic checks corroborate the explicit-rational special case; the parameter-uniform equilibrium census and symmetric stability threshold follow from the algebraic proof above, not from finite sampling. In particular, a local attracting equilibrium does not automatically imply that the original, initial-anchor-constrained trajectory reaches it.

## Relationship to prior work
Alutto et al. (arXiv:2603.24381v1, Secs. 2–5) introduce precisely the quadratic-leadership model used here, derive implicit equilibrium equations and a conservative sufficient contraction condition, and state explicitly that their sufficient condition does not locate the exact stability boundary (Remark 4). Their three-node symmetry illustration does not classify the opposing two-agent case. The present classification uses their model but gives an exact sharp parameter threshold and a complete stationary-state census for that natural two-agent specialization. The same authors' later preprint arXiv:2606.05825 instead uses a *replicator* leadership law \(\dot y_i=y_i(1-y_i)(\rho_i x_i^2-(x_i-(Wx)_i)^2)\), which is not the quadratic birth–loss law studied here, so its equilibrium categories do not imply this census. Ataş–Demirci–Özemir (2021) study bifurcations with a different nonlinear, exponentially decaying interaction potential, not this evolving-leadership ODE. Classical Friedkin–Johnsen dynamics fix susceptibility and thus do not contain the present leadership feedback. Generic pitchfork theory supplies terminology, not this model-specific threshold or exact coexistence of attracting states.

## Limitations
The results classify only the precisely specified two-agent mutual-interaction network with opposed fixed anchors. The complete equilibrium census does not classify trajectories globally. Exponential attraction is proved for three points only at the exhibited exact parameter choice, not for both asymmetric same-sign branches at all parameter values. The symmetric threshold is a linearized result, and no center-manifold coefficient at equality is claimed. The two unstable asymmetric states need not be the only separatrices. The original model requires opinions at physical time zero to equal their anchors; no rigorous intersection between each local basin and that constrained initial-data plane is asserted. No empirical social-science prediction is inferred. Further literature could contain an equivalent reduction, and no independent external validation is asserted.

## References
1. M. Alutto, L. Zino, K. H. Johansson, A. Fontan, *On a Co-evolving Opinion-Leadership Model in Social Networks*, arXiv:2603.24381v1 (first posted 2026-03-25), https://arxiv.org/html/2603.24381v1.
2. M. Alutto, L. Zino, K. H. Johansson, A. Fontan, *On Leadership Emergence in Opinion Dynamics on Social Networks*, arXiv:2606.05825 (first posted 2026-06-04), https://arxiv.org/abs/2606.05825.
3. F. Ataş, A. Demirci, C. Özemir, *Bifurcation analysis of Friedkin–Johnsen and Hegselmann–Krause models with a nonlinear interaction potential*, Mathematics and Computers in Simulation **185** (2021), 676–686, doi:10.1016/j.matcom.2021.01.012. The complete article was not available for direct inspection.
