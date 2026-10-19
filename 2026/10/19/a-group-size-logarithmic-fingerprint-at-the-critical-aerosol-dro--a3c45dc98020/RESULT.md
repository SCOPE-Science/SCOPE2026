# A group-size logarithmic fingerprint at the critical aerosol–droplet SIS threshold

## Finding

Consider a family of epidemic mean-field models with two state variables: \(x(t)\) is the fraction of infected individuals and \(y(t)\) is the fraction of aerosol-contaminated environments. For every integer hyperedge size \(s\ge3\), define

\[
\dot x=\frac{x+y}{2}(1-x)-x,\qquad
\dot y=f_s(x)(1-y)-y,\qquad f_s(x)=\frac{\arctan(sx)}s.
\]

For every initial condition \((x(0),y(0))\in(0,1)^2\), the solution tends to the disease-free state, and there exists a real constant \(C_s=C_s(x(0),y(0))\) such that

\[
\boxed{\frac1{x(t)}=t+\frac{s^2}{9}\log t+C_s+o(1)}\qquad(t\to\infty).
\]

In particular, \(t x(t)\to1\) and \(y(t)/x(t)\to1\). Every member of this family has the same basic reproduction number \(\mathcal R_0=1\) and the same full disease-free Jacobian, with eigenvalues \(0\) and \(-3/2\). Nevertheless, if \(s,r\ge3\) are distinct, using any strictly interior initial conditions in the respective models gives

\[
\boxed{\lim_{t\to\infty}\frac{x_s(t)^{-1}-x_r(t)^{-1}}{\log t}=\frac{s^2-r^2}{9}}.
\]

Thus the first logarithmic correction to critical extinction distinguishes hyperedge size although the threshold, full linearization, and leading \(1/t\) extinction law do not.

## Assumptions and scope

This is an exact specialization of the regular \((2,s)\)-uniform-hypergraph mean-field system (3.3) in Nguyen and Porter [1], with the same saturating contamination law \(g(z)=\arctan z\). Set dyadic degree and environmental hyperdegree \(k_d=k_e=1\), dyadic and environmental infection rates \(\beta_d=\beta_e=1/2\), both recovery rates \(\gamma=\delta=1\), and environmental contamination coefficient \(\sigma=1/s\). These are positive permitted parameters. An underlying \((1,1)\)-regular \((2,s)\)-uniform hypergraph exists: partition \(2s\) vertices into two groups of size \(s\), add the two groups as the environmental hyperedges, and add any perfect matching as the dyadic edges. The theorem concerns the homogeneous deterministic mean-field equation, not a finite-vertex exact stochastic expectation.

The time variable is dimensionless after normalizing recovery rates to one. The logarithm is taken for \(t>0\) in those units. Constants in Landau notation may depend on the fixed integer \(s\) and on initial conditions; uniformity in growing \(s\) is not claimed.

The source's reproduction-number formula (3.4) gives \(\mathcal R_0=(\beta_d k_d/\gamma)+(\beta_e\sigma k_e s/(\gamma\delta))=1/2+1/2=1\). Direct differentiation gives the same matrix for all \(s\):
\[
J(0,0)=\begin{pmatrix}-1/2&1/2\\1&-1\end{pmatrix},\qquad \operatorname{spec}(J)=\{0,-3/2\}.
\]

## Proof

**1. Positive invariance and extinction.** The unit square is forward invariant: on \(x=0\) the first derivative is \(y/2\ge0\); on \(x=1\) it is \(-1\); on \(y=0\) the second derivative is \(f_s(x)\ge0\); and on \(y=1\) it is \(-1\). A strictly interior solution remains strictly interior by uniqueness and the boundary vector field. The function \(f_s\) obeys \(0\le f_s(x)\le x\) for \(x\ge0\). With \(V=x+y/2\), direct differentiation yields the exact identity
\[
\dot V=\frac{f_s(x)-x}{2}-\frac{x^2}{2}-\frac{[x+f_s(x)]y}{2}\le0.
\]
The set where \(\dot V=0\) in the closed unit square is contained in \(x=0\). Its only invariant point is the origin, because at \(x=0\) with \(y>0\) one has \(\dot x=y/2>0\). Compactness and LaSalle's invariance principle give \(x(t),y(t)\to0\).

**2. A slow-variation estimate.** The elementary integral estimate
\[
0\le x-f_s(x)=\frac1s\int_0^{sx}\frac{u^2}{1+u^2}\,du\le\frac{s^2x^3}{3}
\]
shows that on the unit square \(0\le-\dot V\le K_s V^2\) for a finite positive constant \(K_s\), for example \(K_s=5/2+s^2/6\). Hence \(V(t)^{-1}\le V(0)^{-1}+K_s t\), so \(V(t)\) cannot decay exponentially.

We use the following elementary exponentially stable forcing estimate. Suppose \(V\) is positive, nonincreasing, tends to zero, obeys \(\dot V\ge-KV^2\), and \(z'=-a(t)z+O(V^p)\) with \(a(t)\ge a_0>0\) for large \(t\), where \(p>0\). Then \(z=O(V^p)\). Indeed, split the variation-of-constants integral at \(t-L(t)\), where \(L(t)=(p+2)\log(1/V(t))/a_0\). The reciprocal bound implies \(L(t)=O(\log t)=o(t)\), and \(V(u)\le2V(t)\) for \(u\in[t-L(t),t]\) once \(t\) is large, because \(K L(t)V(t)\to0\). Thus the recent integral is \(O(V(t)^p)\); the earlier part and the homogeneous term are \(O(e^{-a_0 L(t)})=O(V(t)^{p+2})\). This proves the estimate.

**3. Transverse decay and the leading law.** Put \(d=y-x\) and \(h_s(x)=f_s(x)-x\). Exact subtraction gives
\[
\dot x=-x^2+\frac{1-x}{2}d,\qquad
\dot d=-\frac{3+x}{2}d+h_s(x)(1-x-d).
\]
Since \(h_s(x)=-s^2x^3/3+O(x^5)\), the forcing estimate with \(p=3\) yields \(d=O(V^3)\). From \(V=(3x+d)/2\), one has \(x\sim2V/3\) and hence \(d=O(x^3)\). Therefore \(\dot x=-x^2+O(x^3)\), or \((1/x)'=1+O(x)\). As \(x\to0\), Cesàro integration gives \(1/x(t)\sim t\), and consequently \(x(t)\sim1/t\) and \(y(t)/x(t)\to1\).

**4. The exact cubic coefficient.** Define \(A_s=-2s^2/9\) and \(z=d-A_sx^3\). Substitution in the two exact equations above, including \(\dot z=\dot d-3A_sx^2\dot x\), cancels all terms of order \(x^3\):
\[
-\frac32A_s-\frac{s^2}{3}=0.
\]
The remaining equation has the form \(\dot z=-[3/2+O(x)]z+O(x^4)\). Applying the same forcing estimate with \(p=4\) gives \(z=O(V^4)=O(x^4)\). It follows that
\[
d=-\frac{2s^2}{9}x^3+O(x^4),\qquad
\dot x=-x^2-\frac{s^2}{9}x^3+O(x^4).
\]
The cancellation of the quadratic transverse term and the explicit cubic coefficient are exact consequences of the saturating arctangent law and the matched rates; they are not inferred from a numerical fit.

**5. Integration and the finite constant.** Set \(u=1/x\). The preceding expansion implies
\[
\dot u=1+\frac{s^2}{9u}+O(u^{-2}).
\]
Since \(u\sim t\), integration first gives \(u=t+O(\log t)\). Substituting this estimate back gives
\[
\frac{d}{dt}\left[u-t-\frac{s^2}{9}\log t\right]
=O\left(\frac{\log t}{t^2}\right),
\]
which is integrable on every sufficiently late half-line. Thus the bracket converges to a finite \(C_s\), proving the expansion. Subtracting the expansions for two different fixed hyperedge sizes and dividing by \(\log t\) proves the stated size-comparison limit.

## Verification

The accompanying `verify.py` reproduces the exact Jacobian, weighted derivative identity, transformed equations, and cubic cancellation with symbolic mathematics. It also integrates three different fixed hyperedge sizes to two late but finite times and checks the stabilizing corrected reciprocal prevalence. Run `python verify.py` after installing packages from `requirements.txt`. Symbolic identities support specific proof steps; the limiting statement is proved by the analytical argument above, not by finite integration.

## Relationship to prior work

Nguyen and Porter [1], in their regular-hypergraph mean-field equation (3.3) and reproduction formula (3.4), supply precisely the two-channel model considered here. Their Theorem 3.3 handles \(\mathcal R_0<1\) and their endemic results treat \(\mathcal R_0>1\); the equality case and its explicit group-size-dependent reciprocal-prevalence logarithmic correction are not given in the inspected model and theorem sections. Their numerical discussion addresses hyperedge-size effects in other parameter regimes. The arctangent saturation and the reproduction-number formula are existing ingredients, not new claims here.

Jhun, Jo, and Kahng [2] analyze a simplicial SIS process on scale-free uniform hypergraphs using direct polyadic infection and stationary degree-distribution self-consistency. That model has no independently evolving contaminated-environment variable and does not imply the stated two-variable critical logarithmic coefficient by a matching specialization. The use of nonlinear normal forms or stable-mode reductions is classical; the claimed addition is the explicit, globally applicable coefficient \(s^2/9\) for this motivated, fixed-linearization group-size family, not a new general asymptotic technique.

## Limitations

The theorem concerns deterministic mean-field dynamics at the single critical parameter family specified above. It does not establish the same law for arbitrary transmission rates, heterogeneous hypergraphs, a finite stochastic epidemic, demographic noise, or group sizes that grow together with observation time. The additive constant \(C_s\) depends on initial conditions and is proved to exist but is not given in elementary closed form. Reproduction number and Jacobian alone do not identify group size in this family, but the result makes no claim of global parameter identifiability from finite, noisy observations. Independent verification and a comprehensive literature survey remain unperformed.

## References

[1] T. D. Nguyen and M. A. Porter, *A disease-spread model on hypergraphs with distinct droplet and aerosol transmission modes*, arXiv:2601.03563v1 (first public version 2026-01-07), https://arxiv.org/pdf/2601.03563. Relevant: §§2.2, 3.2 and equations (3.3)–(3.4).

[2] B. Jhun, M. Jo, and B. Kahng, *Simplicial SIS model in scale-free uniform hypergraph*, arXiv:1910.00375 (2019), https://arxiv.org/pdf/1910.00375. Relevant: mean-field system and stationary degree-dependent self-consistency.
