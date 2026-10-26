# Supercritical flip onset and explicit eigenmode profile in finite Huygens paths

## Finding
For every finite unit-weight path of \(N+1\) phase oscillators, \(N\ge1\), a single, locally unique attracting prime-period-two orbit emerges immediately above the sharp step-size threshold at which the phase-opposition sink loses stability. The birth is supercritical and its spatial shape and critical multiplier are explicit.

Define \(\lambda_N=2+2\cos(\pi/(N+1))\), \(h_N=2/\lambda_N\), and \(v_i=(-1)^{i+1}\sqrt{2/(N+1)}\sin(i\pi/(N+1))\), for \(1\le i\le N\). Write \(S_N=\sum_i v_i^4\). For sufficiently small \(\delta=h-h_N>0\), the unique nearby genuine two-cycle consists of \(\pi\mathbf1\pm x_h\), where

\[
x_h=\sqrt{\frac{3\lambda_N\delta}{S_N}}\,v+O_N(\delta^{3/2}).
\]

The two-step Floquet multiplier corresponding to the highest Laplacian mode is \(1-4\lambda_N\delta+O_N(\delta^2)\); the other multipliers remain strictly inside the unit circle. The orbit is therefore asymptotically attracting. For \(N\ge2\), the leading shape can be written without eigenvector normalization:

\[
(x_h)_i=2(-1)^{i+1}\sqrt{\lambda_N\delta}\sin\left(\frac{i\pi}{N+1}\right)+O_N(\delta^{3/2}),\qquad 1\le i\le N.
\]

For \(N=1\), the corresponding amplitude is \((x_h)_1=\sqrt{6(h-1)}+O((h-1)^{3/2})\). Below \(h_N\), the strict Lyapunov theorem in [1] excludes nonfixed periodic points. This identifies a sharp no-periodic-orbit versus attracting-two-cycle transition.

## Assumptions and scope
The phase space is \(\mathbb T^N=(\mathbb R/2\pi\mathbb Z)^N\). The matrix \(K_N\) has entries \((K_N)_{ii}=2\), \((K_N)_{i,i+1}=(K_N)_{i+1,i}=-1\), and all other entries zero. The componentwise-sine map is

\[
G_h(z)=z+hK_N\sin z\pmod{2\pi},\qquad h>0.
\]

All claims above the threshold concern a sufficiently small neighborhood of \(\pi\mathbf1\) and a parameter interval \((h_N,h_N+\varepsilon_N)\) for some \(\varepsilon_N>0\) that may depend on \(N\). Convergence is ordinary discrete-time attraction of the two-cycle, not the neutral overall phase direction of the unreduced oscillator network. The branch sign is fixed by \(\langle x_h,v\rangle>0\); exchanging signs does not produce a different orbit.

## Proof
**1. Exact eigenstructure and the critical parameter.** The eigenvalues of \(K_N\) are \(\lambda_k=2-2\cos(k\pi/(N+1))\), \(1\le k\le N\), and are positive and distinct. The largest equals \(\lambda_N\), with normalized real eigenvector \(v\) as defined above. All the following local calculations use real representatives \(x=z-\pi\mathbf1\) near zero. Because \(\sin(\pi+x)=-\sin x\), the local map is the odd analytic map \(F_h(x)=x-hK_N\sin x\). Its derivative at zero is \(I-hK_N\). All eigenvalues lie strictly between \(-1\) and \(1\) when \(0<h<h_N\); at \(h_N\) exactly the leading eigenvalue reaches \(-1\) and all others remain strictly between \(-1\) and \(1\).

**2. Every nearby two-cycle is antipodal.** Suppose \(F_h(p+q)=p-q\) and \(F_h(p-q)=p+q\), with \(p,q\) sufficiently small. Adding the two identities yields \(\{F_h(p+q)+F_h(p-q)\}/2=p\). For fixed small \(q\), the left side minus \(p\) has derivative at \((p,q)=(0,0)\) equal to \(DF_h(0)-I=-hK_N\), which is invertible near \(h_N\). Since \(F_h\) is odd, \(p=0\) solves the summed equation for every \(q\). The implicit function theorem makes it the unique small solution. Thus a nearby two-cycle necessarily consists of \(\pm x\), with \(F_h(x)=-x\), equivalent to \(2x=hK_N\sin x\).

**3. Lyapunov–Schmidt equation and uniqueness.** Put \(\delta=h-h_N\). Let \(P=vv^{T}\) and \(Q=I-P\), and decompose \(x=sv+w\), \(w\perp v\). Define

\[
H(x,h)=2x-hK_N\sin x=(2I-hK_N)x+\frac h6K_Nx^{\circ3}+O(\|x\|^5),
\]

where \(x^{\circ3}\) means componentwise cubes. On \(v^\perp\), the derivative of \(QH\) with respect to \(w\) at \((0,h_N)\) is \(Q(2I-h_NK_N)|_{v^\perp}\), invertible because the top eigenvalue is simple. The analytic implicit function theorem therefore gives a unique odd analytic \(w(s,h)\), with \(w(s,h)=O(s^3)\) uniformly for \(h\) near \(h_N\). Note that the linear \(s\)-term vanishes in the \(Q\)-equation for all such \(h\) since \(QK_Nv=0\).

Take the scalar inner product with \(v\). Using symmetry of \(K_N\) and \(\langle v,K_Ny\rangle=\lambda_N\langle v,y\rangle\), obtain

\[
\langle v,H(sv+w,h)\rangle=s\left[-\lambda_N\delta+\frac{h\lambda_NS_N}{6}s^2+O(s^4)\right].
\]

The omitted term is analytic and uniform in \(h\); replacing \(h\) with \(h_N\) in the cubic coefficient adds \(O(\delta s^2)\). Since \(h_N\lambda_N=2\), the scalar equation for nonzero \(s\) has the form

\[
0=-\lambda_N\delta+\frac{S_N}{3}s^2+O(\delta s^2+s^4).
\]

Analytic oddness of \(w\) makes the bracket analytic in \(t=s^2\), and its derivative in \(t\) at zero is \(S_N/3>0\). The implicit function theorem gives exactly one small solution \(t(\delta)\), with

\[
t(\delta)=\frac{3\lambda_N}{S_N}\delta+O(\delta^2).
\]

For \(\delta>0\) it yields exactly \(s=\pm\sqrt{t(\delta)}\), the same two-cycle; for \(\delta\le0\) no small nonzero solutions arise. Because \(w=O(s^3)\), the amplitude formula follows. The one-cycle fixed-point equation near zero reduces to \(K_N\sin x=0\), hence its only solution is zero. This ensures prime temporal period two.

**4. Stability and the multiplier coefficient.** At the paired points \(\pm x\), the one-step derivative matrices coincide:

\[
DF_h(x)=DF_h(-x)=I-hK_ND_x,\qquad D_x=\operatorname{diag}(\cos x_i).
\]

Here \(D_x\) is positive definite for sufficiently small \(\delta\). Therefore \(K_ND_x\) is similar to the symmetric matrix \(D_x^{1/2}K_ND_x^{1/2}\). The eigenvalues are real and, for modes other than \(v\), remain in \((-1,1)\) by continuity from the distinct noncritical eigenvalues at \(\delta=0\).

The first-order shift of the simple critical eigenvalue can be computed by symmetric-matrix perturbation (equivalently by left and right eigenvectors at \(\delta=0\)). Expanding \(\cos x_i=1-x_i^2/2+O(\delta^2)\) and inserting \(x=sv+O(s^3)\) yields

\[
\begin{aligned}
\mu_{\mathrm{crit}}&=1-h\lambda_N+\frac{h\lambda_N}{2}\sum_i v_i^2x_i^2+O(\delta^2)\\
&=-1-\lambda_N\delta+\frac{h_N\lambda_N}{2}\frac{3\lambda_N\delta}{S_N}S_N+O(\delta^2)\\
&=-1+2\lambda_N\delta+O(\delta^2).
\end{aligned}
\]

For sufficiently small positive \(\delta\), every one-step multiplier has modulus less than one. Since \(DF_h(x)=DF_h(-x)\), the second-iterate derivative is \(DF_h(x)^2\), which is strictly contracting spectrally and has critical multiplier \(1-4\lambda_N\delta+O(\delta^2)\). Standard local stability of a hyperbolic periodic sink yields an open attracting basin.

**5. Spatial profile.** For \(N\ge2\), use \(\sum_{i=1}^N\sin^4(i\pi/(N+1))=3(N+1)/8\), giving \(S_N=3/[2(N+1)]\). (The identity fails for \(N=1\), which is why that case is separate.) Substitution into the normalized eigenvector formula gives the explicit componentwise amplitude. For \(N=1\), \(\lambda_1=2\), \(v_1=1\), \(S_1=1\), so \(h_1=1\) and \(x=\sqrt{6(h-1)}+O((h-1)^{3/2})\).

**6. Sharpness below threshold.** The strict-descent theorem in [1], Section 3 and the path computation in Section 5.2, show that \(V(z)=\sum_i\cos z_i\) decreases strictly along every nonfixed iteration for \(0<h<2/\lambda_N\). A periodic orbit of least period at least two is therefore impossible in that entire interval. The attracting orbit constructed above exists for every sufficiently small \(h-h_N>0\), proving the claimed sharp onset.

## Verification
The included standalone `verify.py` runs 30 finite numerical parameter cases: \(N=1,\ldots,10\) and three positive values of \(h-h_N\). It solves \(2x=hK_N\sin x\) by Newton iteration, verifies \(F_h(x)=-x\) by a separate map evaluation, checks the leading amplitude, and diagonalizes the similar symmetric Jacobian numerically. All 30 cases pass. Numerical computations neither establish the infinite-dimensional quantifiers nor replace the analytic proof.

## Relationship to prior work
Reference [1] derives the exact path map, its top eigenvalue, the strict Lyapunov interval \(0<h<2/\lambda_N\), and the Morse–Smale diffeomorphism interval \(0<h<1/\lambda_N\). The first two inputs are cited and are not new. The paper remarks that at larger steps discrete updates may acquire nontrivial periodic orbits; its results do not establish a supercritical flip branch, its local uniqueness, amplitude, or stability beyond \(2/\lambda_N\). References [2] and [3] study small-coupling diffeomorphisms of three-clock models, not this boundary. Reference [4] treats phase-twisted rings and the convergent range, not the path flip regime. The standard local implicit-function and spectral-perturbation machinery is classical; the explicit, all-path critical branch is the specific new claim.

## Limitations
The parameter width and neighborhood may depend on \(N\); no uniform-in-\(N\) branch radius is proved. Nothing is claimed about all attractors for large \(h\), or the full unreduced model's neutral common-phase direction. The cited published literature and searchable mathematical records do not establish historical uniqueness; priority across other terminology remains uncertain. 
## References
[1] Jorge Buescu, Emma D’Aniello, Henrique M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1 (first public 2026-10-07), https://arxiv.org/html/2610.10993v1.

[2] Jorge Buescu, Emma D’Aniello, Henrique M. Oliveira, *A Lyapunov function for a Synchronisation diffeomorphism of three clocks*, arXiv:2502.15371v1 (2025), https://arxiv.org/html/2502.15371v1.

[3] Jorge Buescu, Henrique M. Oliveira, *Lyapunov functions for Morse-Smale synchronisation diffeomorphisms*, arXiv:2503.13230v1 (2025), https://arxiv.org/html/2503.13230v1.

[4] Jorge Buescu, Henrique M. Oliveira, *Almost-global convergence to twisted states in discrete Huygens rings*, arXiv:2610.19953v1 (2026), https://arxiv.org/html/2610.19953v1.
