# Sharp distance-only envelopes for the planar modified Helmholtz Dirichlet profile
## Finding
Let \(\Omega\subset\mathbb R^2\) be a bounded convex domain, let \(\mu>0\), and let \(v_\mu\) be the solution of
\[
\Delta v_\mu-\mu^2v_\mu=0\quad\text{in }\Omega,
\qquad
v_\mu=1\quad\text{on }\partial\Omega.
\]
For \(x\in\Omega\), set \(d=\operatorname{dist}(x,\partial\Omega)\). Then
\[
e^{-\mu d}<v_\mu(x)\le \frac{1}{I_0(\mu d)}.
\]
Both functions of \(d\) are sharp over bounded convex planar domains. More precisely, for fixed \(\mu>0\) and \(d>0\),
\[
\inf_{(\Omega,x):\,\operatorname{dist}(x,\partial\Omega)=d}v_\mu^\Omega(x)
=e^{-\mu d},
\qquad
\sup_{(\Omega,x):\,\operatorname{dist}(x,\partial\Omega)=d}v_\mu^\Omega(x)
=\frac{1}{I_0(\mu d)}.
\]
The upper extremum is attained exactly when \(\Omega=B_d(x)\). The lower extremum is not attained by a bounded convex domain, but it is approached by tangent disks whose radii tend to infinity.

Equivalently, for the logarithmic profile \(w_\mu=-\mu^{-1}\log v_\mu\),
\[
\frac{1}{\mu}\log I_0(\mu d)\le w_\mu(x)<d.
\]

## Assumptions and scope
The domain is bounded and convex in the plane. The boundary-value problem is the one used by Nazarov; bounded convex domains fall within the Lipschitz setting of that theorem. The statement is pointwise and depends only on the distance \(d\) from the observation point to the boundary. It does not assert comparable sharp envelopes for nonconvex domains or for higher dimensions.

## Proof
For the upper bound, the open disk \(B_d(x)\) is contained in \(\Omega\). On that disk define
\[
b(z)=\frac{I_0(\mu|z-x|)}{I_0(\mu d)}.
\]
This is the radial solution of the same modified Helmholtz equation on \(B_d(x)\) with boundary value one. The maximum principle gives \(0<v_\mu\le1\) in \(\Omega\), hence \(v_\mu\le b\) on \(\partial B_d(x)\). Applying the maximum principle to \(b-v_\mu\) on the disk gives
\[
v_\mu(x)\le b(x)=\frac{1}{I_0(\mu d)}.
\]
If equality holds at \(x\), the strong maximum principle forces \(v_\mu=b\) throughout \(B_d(x)\). Hence \(v_\mu=1\) on all of \(\partial B_d(x)\). If \(\Omega\) properly contains \(B_d(x)\), some point of this circle lies in the interior of \(\Omega\), contradicting \(v_\mu<1\) at every interior point. Thus equality forces \(\Omega=B_d(x)\), and the disk plainly attains it.

For the lower bound, choose a nearest boundary point \(y\in\partial\Omega\). Convexity gives a supporting line at \(y\) whose inward unit normal points from \(y\) toward \(x\). Let \(s(z)\) be signed distance to that supporting line, positive on \(\Omega\). Then \(s(x)=d\) and
\[
\phi(z)=e^{-\mu s(z)}
\]
satisfies \(\Delta\phi-\mu^2\phi=0\). On \(\partial\Omega\), convexity gives \(s\ge0\), so \(\phi\le1=v_\mu\). Because \(\Omega\) is bounded, this boundary inequality is not equality everywhere. The strong maximum principle therefore yields \(v_\mu>\phi\) in \(\Omega\), and in particular
\[
v_\mu(x)>e^{-\mu d}.
\]

To prove sharpness of the lower envelope, take
\[
\Omega_R=B_R((0,R)),\qquad x=(0,d),\qquad R>d.
\]
Then \(\operatorname{dist}(x,\partial\Omega_R)=d\), and the radial formula gives
\[
v_\mu^{\Omega_R}(x)
=
\frac{I_0(\mu(R-d))}{I_0(\mu R)}.
\]
Using the standard asymptotic \(I_0(t)\sim e^t/\sqrt{2\pi t}\) as \(t\to\infty\),
\[
v_\mu^{\Omega_R}(x)\longrightarrow e^{-\mu d}.
\]
The strict lower inequality already proves that no bounded convex domain attains the infimum.

## Verification
The proof uses exact comparison solutions and the strong maximum principle. The upper comparison is the centered-disk Bessel profile; the lower comparison is the supporting-half-plane exponential profile. The extremizing sequence is explicit, and the only asymptotic input is the classical leading expansion of \(I_0\). No finite numerical experiment is used.

The equality analysis is also pointwise. Equality in the upper comparison forces equality of two solutions on the entire inscribed disk, which would put value one at an interior point unless the ambient domain is exactly that disk. The lower comparison is strict because a bounded convex domain cannot have its entire boundary on a single supporting line.

## Relationship to prior work
Nazarov proves that, for the same Dirichlet problem, the gradient inequality \(|\nabla v_\mu|\le\mu v_\mu\) characterizes convex planar domains and holds for every \(\mu>0\) in the convex case. His proof uses a supporting-half-plane exponential barrier and convexity of sublevel sets, but it does not state the sharp two-sided distance-only envelope above.

Kuznetsov's earlier work records the exact half-plane exponential solution, the exact disk Bessel solution, and Varadhan's large-parameter distance limit. Those ingredients identify the natural candidate extremals but do not state the optimization over all bounded convex domains or the unique upper equality case. Panharmonic/Yukawa potential literature gives explicit ball formulas and probabilistic representations; the inspected sources do not supply this convex-domain extremal statement.

## Limitations
Convexity is essential to the supporting-half-plane lower comparison. The theorem is planar; the corresponding higher-dimensional upper profile uses a different radial Bessel expression and is not claimed here. The literature search cannot exclude an equivalent elementary comparison theorem hidden in older potential-theory terminology.

## References
1. Alexander I. Nazarov, *On solutions of the modified Helmholtz equation in a planar domain*, arXiv:2609.06523v1, first public 2026-09-06.
2. Nikolay G. Kuznetsov, *The convexity of a planar domain via properties of solutions to the modified Helmholtz equation*, arXiv:2403.09382v2; Journal of Mathematical Sciences 281 (2024).
3. Antti Rasila and Tommi Sottinen, *Yukawa Potential, Panharmonic Measure and Brownian Motion*, Axioms 7 (2018), article 28, DOI:10.3390/axioms7020028.
