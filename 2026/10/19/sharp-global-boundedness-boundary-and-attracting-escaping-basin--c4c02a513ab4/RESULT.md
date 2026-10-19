# Sharp global boundedness boundary and attracting–escaping basin coexistence in a two-cell spiking map

## Finding

For the two-cell hyperbolic-tangent map of Buscarino, Famoso and Fortuna at their fixed coupling and bias parameters, the Euler-step parameter has an **exact global boundedness boundary** at \(T=2\). For every \(\alpha>0\), every forward orbit is bounded and there is a compact absorbing set when \(0<T\le 2\). For every \(T>2\), an explicit nonempty open exterior region consists entirely of exponentially escaping orbits, for every \(\alpha>0\). The endpoint \(T=2\) belongs to the bounded regime despite its neutral affine part.

More precisely, writing \(X_n=(u_n,v_n)\) and using the maximum norm, an initial condition with
\[
\|X_0\|_\infty>\frac{3T}{T-2},\qquad T>2,
\]
has a nonzero escape amplitude \(L=L(X_0,T,\alpha)\) such that
\[
\lim_{n\to\infty}[-(T-1)]^{-n}X_n=L,\qquad
\|L\|_\infty\ge\|X_0\|_\infty-\frac{3T}{T-2}>0,
\]
and in fact
\[
\big\|X_n-[-(T-1)]^nL\big\|_\infty\le\frac{3T}{T-2}\quad(n\ge0).
\]
Thus the escaping trajectories have exact logarithmic growth rate \(\log(T-1)\) and alternating leading direction.

The exterior escape basin need not exhaust phase space. At the explicit parameters \(T=9/4\), \(\alpha=1/4\), there is a **unique fixed point** \(X_*\) with \(\|X_*\|_\infty\le12/13\). Every point of the nonempty square \(X_*+[-1/13,1/13]^2\) converges geometrically to \(X_*\), with contraction factor at most \(469/512\) in the maximum norm. In the same map every initial condition with \(\|X_0\|_\infty>27\) escapes exponentially. An attracting equilibrium therefore coexists with a nonempty open escape basin beyond the sharp global boundedness boundary.

## Assumptions and scope

The deterministic, real-valued map is
\[
\begin{aligned}
u_{n+1}&=(1-T)u_n+T\left(\frac{17}{10}\tanh(\alpha u_n)-\tanh(\alpha v_n)-\frac3{10}\right),\\
v_{n+1}&=(1-T)v_n+T\left(\tanh(\alpha u_n)+\frac{17}{10}\tanh(\alpha v_n)+\frac3{10}\right).
\end{aligned}
\]
The parameters satisfy \(T>0\) and \(\alpha>0\), with no restriction on \(X_0\in\mathbb R^2\). This is the source map's deterministic Euler discretization with \(\mu=0.7\), \(s=1\), \(i_1=-0.3\) and \(i_2=0.3\). The variables \(u_n,v_n\) are real, with no clipping, noise or finite-precision arithmetic.

Set
\[
A=\begin{pmatrix}17/10&-1\\1&17/10\end{pmatrix},\qquad
b=\begin{pmatrix}-3/10\\3/10\end{pmatrix},\qquad
\Phi_\alpha(X)=\begin{pmatrix}\tanh(\alpha u)\\\tanh(\alpha v)\end{pmatrix},
\]
and \(H(X)=A\Phi_\alpha(X)+b\), so \(F_{T,\alpha}(X)=(1-T)X+TH(X)\). Every component of \(H\) has magnitude at most \(3\).

A *compact absorbing set* means a fixed compact subset of \(\mathbb R^2\) that contains all sufficiently late iterates of every forward trajectory, with the entry time allowed to depend on the initial condition. For \(T>2\), *escaping* means \(\|X_n\|_\infty\to\infty\).

## Proof

**1. Steps strictly below two.** When \(0<T<2\), put \(\rho=|1-T|<1\). The uniform forcing bound gives
\[
\|X_{n+1}\|_\infty\le\rho\|X_n\|_\infty+3T.
\]
Iteration shows that for every \(\epsilon>0\), the square of radius \(3T/(1-\rho)+\epsilon\) is absorbing and forward invariant. This proves global boundedness for all \(0<T<2\).

**2. The neutral endpoint.** For \(T=2\), we have \(F(X)=-X+2H(X)\), so \(|F_j(X)+X_j|\le6\). In the second iterate the fixed bias cancels exactly:
\[
F^2(X)-X=2A\big(\Phi_\alpha(F(X))-\Phi_\alpha(X)\big).
\]
Fix \(\theta=9/10\), \(\tau=\operatorname{arctanh}(\theta)=\tfrac12\log19\), and \(R=11+\tau/\alpha\). Suppose a coordinate \(X_j\) has \(|X_j|\ge R\). Then \(F_j(X)\) has the opposite sign, with \(|F_j(X)|\ge|X_j|-6>\tau/\alpha\). Thus \(\tanh(\alpha F_j(X))-\tanh(\alpha X_j)\) points strictly inward and has absolute value at least \(2\theta=9/5\). The other coordinate's hyperbolic-tangent difference has absolute value at most \(2\).

Because the diagonal coefficient of \(A\) is \(17/10\), while the off-diagonal magnitude is \(1\), the inward signed two-step displacement satisfies
\[
\operatorname{sgn}(X_j)\big(F^2_j(X)-X_j\big)
\le-4\frac{17}{10}\frac9{10}+4=-\frac{53}{25}.
\]
For every \(X\), regardless of coordinate size,
\[
\big|F^2_j(X)-X_j\big|\le4\left(\frac{17}{10}+1\right)=\frac{54}{5}<R.
\]
Hence a coordinate of magnitude at least \(R\) cannot change sign in two steps and its magnitude drops by at least \(53/25\); a coordinate of magnitude below \(R\) has next two-step magnitude at most \(R+54/5\). It follows independently for the two coordinates that \(F^2\) has the absorbing, forward-invariant square of radius \(R+54/5\). Writing \(B\) for that square, we have \(F^2(B)\subseteq B\). Consequently \(B\cup F(B)\) is compact, forward invariant under \(F\), and absorbing; it lies inside the square of radius \(R+54/5+6\). In particular, every orbit is bounded at the marginal step \(T=2\).

**3. Supercritical escape and exact rate.** For \(T>2\), set \(q=T-1>1\). The reverse triangle inequality gives
\[
\|F_{T,\alpha}(X)\|_\infty\ge q\|X\|_\infty-3T.
\]
Let \(r_*=3T/(q-1)=3T/(T-2)\). If \(r_0=\|X_0\|_\infty>r_*\), induction yields
\[
\|X_n\|_\infty\ge r_*+q^n(r_0-r_*).
\]
To sharpen this into an asymptotic law, let \(Z_n=(-q)^{-n}X_n\). Then
\[
Z_{n+1}-Z_n=T(-q)^{-n-1}H(X_n),
\]
and the increments are absolutely summable. Its limit \(L\) therefore exists and satisfies
\[
\|L-X_0\|_\infty\le3T\sum_{n\ge0}q^{-n-1}=r_*.
\]
Our strict exterior assumption makes \(L\ne0\). The tail bound is \(\|L-Z_n\|_\infty\le r_*q^{-n}\), proving the displayed uniform error and the exact escape rate.

**4. Coexistence at explicit parameters.** Set \(\alpha=1/4\), \(T=9/4\). The fixed-point equation is \(X=H(X)\), independent of \(T\). Because \(|\tanh a-\tanh b|\le|a-b|\), the maximum-norm Lipschitz constant of \(H\) is at most
\[
\frac14\left(\frac{17}{10}+1\right)=\frac{27}{40}<1.
\]
The Banach fixed-point theorem gives a unique \(X_*\in\mathbb R^2\). The fixed-point equation implies \(\|X_*\|_\infty\le(3/10)/(1-27/40)=12/13\).

For any \(X\in[-1,1]^2\), let \(D(X)\) be diagonal with entries \(d_j=\tfrac14\operatorname{sech}^2(X_j/4)\). Since \(|\tanh t|\le|t|\),
\[
\frac{15}{64}\le d_j\le\frac14.
\]
The Jacobian \(DF(X)=-\tfrac54I+\tfrac94 A D(X)\) consequently has diagonal entries between \(-181/512\) and \(-47/160\), and off-diagonal entries of absolute value at most \(9/16\). Its induced maximum-norm operator norm is thus bounded by
\[
\|DF(X)\|_{\infty\to\infty}\le\frac{181}{512}+\frac9{16}=\frac{469}{512}<1.
\]
The square \(Q=X_*+[-1/13,1/13]^2\) lies inside \([-1,1]^2\). Along each segment joining \(X_*\) to \(X\in Q\), the Jacobian bound applies. The mean-value inequality gives \(\|F(X)-X_*\|_\infty\le(469/512)\|X-X_*\|_\infty\). Thus \(Q\) is forward invariant and every point in it converges geometrically to the unique fixed point. The supercritical escape radius at the same parameters is \(3(9/4)/(9/4-2)=27\), so the exterior open set \(\|X_0\|_\infty>27\) escapes. This completes the proof.

## Verification

The standalone accompanying `verify.py` checks the exact rational inequalities \(53/25>0\), \(54/5<11\), \(27/40<1\), and \(469/512<1\); it reproduces the exact exterior radius \(27\). It also computes the fixed point by contraction, tests the contraction bound on sampled points of its explicit invariant square, checks the supercritical escape inequality along finite orbits, and compares two large-iteration values of the alternating escape amplitude. The computations are supplementary diagnostics; none is used to substitute for the infinite-quantifier proof above. Running `python3 verify.py` requires only Python's standard library.

## Relationship to prior work

Buscarino, Famoso and Fortuna (2023) introduced this map and analyzed fixed points, finite-initial-condition bifurcation plots, spiking, intermittency, noise effects, and hardware implementation. Their numerical examples include steps exceeding \(2\), but the article does not establish the global boundedness boundary, the critical two-step absorbing mechanism, or the explicit coexistence of an attraction basin with an external escape basin. Their equilibrium stability analysis is local; local stability alone cannot imply all-orbit boundedness. The elementary bounded-forcing recursion covers the strict subcritical and supercritical inequalities but becomes inconclusive at \(T=2\); the endpoint proof depends on the original system's saturating odd nonlinearity and strictly dominant diagonal coupling. No assertion of exhaustive historical priority is made.

## Limitations

The result is about the deterministic real map, not its finite-word hardware implementation or noise-driven version. It neither classifies all bounded attractors nor determines the full boundary of each supercritical escape basin. The explicit exterior radius is sufficient, not claimed to be the smallest escaping radius; \(T=2\) is sharp only as the *all-initial-condition boundedness* threshold. For \(T>2\), some trajectories may remain bounded, and no claim of uniform chaos or convergence of every orbit is made. The size of the proved absorbing region at the endpoint depends on \(\alpha\) and becomes large as \(\alpha\downarrow0\).

## References

1. A. Buscarino, C. Famoso, L. Fortuna, “Bifurcations in a new two-cell spiking map: a numerical and experimental study,” *Nonlinear Dynamics* **111** (2023), 20361–20375. First published online 27 September 2023. DOI: 10.1007/s11071-023-08897-7. Full text: https://link.springer.com/article/10.1007/s11071-023-08897-7
