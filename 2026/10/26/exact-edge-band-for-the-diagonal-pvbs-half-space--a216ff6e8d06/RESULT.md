# Exact edge band for the diagonal PVBS half-space

## Finding

For the single-species Product Vacua with Boundary States (PVBS) Hamiltonian on
\(D=\{(x,y)\in\mathbb Z^2:x+y\ge0\}\), with equal directional couplings
\(\lambda_1=\lambda_2=\lambda\in(0,1)\), the one-particle Bloch fiber at boundary
quasimomentum \(k\in[-\pi,\pi]\) has exactly one eigenvalue below its bulk band:
\[
E_{\mathrm{edge}}(k)=\frac{2\lambda^2}{1+\lambda^2}\sin^2\!\left(\frac{k}{2}\right).
\]
A corresponding fiber eigenfunction has amplitude
\[
\psi_k(x,y)=\bigl(\lambda\cos(k/2)\bigr)^{x+y}
             e^{ik(x-y)/2},\qquad x+y\ge0,
\]
with the endpoint \(|k|=\pi\) interpreted as a state supported on the boundary layer \(x+y=0\). The normal decay ratio is \(r(k)=\lambda\cos(k/2)\). The bottom of the bulk band in the same fiber is
\[
E_{\mathrm{bulk,min}}(k)=2-\frac{4\lambda\cos(k/2)}{1+\lambda^2},
\]
and the exact separation is
\[
E_{\mathrm{bulk,min}}(k)-E_{\mathrm{edge}}(k)
=\frac{2\bigl(1-\lambda\cos(k/2)\bigr)^2}{1+\lambda^2}>0.
\]
In particular, the edge band touches zero quadratically:
\[
E_{\mathrm{edge}}(k)=\frac{\lambda^2}{2(1+\lambda^2)}k^2+O(k^4)
\quad\text{as }k\to0.
\]
The fiber eigenvectors are square-summable in the inward normal coordinate but are Bloch waves, not square-summable states along the infinite boundary.

## Assumptions and scope

For an oriented nearest-neighbor edge \((z,z+e_j)\), the local interaction is
\[
h_{z,z+e_j}=|11\rangle\langle11|+|\phi_\lambda\rangle\langle\phi_\lambda|,
\qquad |\phi_\lambda\rangle=\frac{|01\rangle-\lambda|10\rangle}{\sqrt{1+\lambda^2}}.
\]
The half-space is \(D=\{(x,y):x+y\ge0\}\), the two directional parameters are equal, and \(0<\lambda<1\). The claim concerns only the one-particle sector and its direct-integral Bloch fibers along the primitive boundary translation \((1,-1)\). It does not classify the many-particle spectrum, perturbed models, other boundary slopes, or anisotropic couplings.

## Proof

In the one-particle sector the \(|11\rangle\langle11|\) term vanishes. If \(\psi(z)\) is the particle amplitude, each oriented edge contributes
\[
\frac{|\psi(z+e_j)-\lambda\psi(z)|^2}{1+\lambda^2}
\]
to the quadratic form. Set \(s=x+y\ge0\) and \(j=x\), and Fourier transform in \(j\) using \(\psi_{s,j}=e^{ikj}u_s\). The fiber operator is
\[
(H(k)u)_0=\frac{2\lambda^2}{1+\lambda^2}u_0
 -\frac{\lambda(1+e^{ik})}{1+\lambda^2}u_1,
\]
while, for \(s\ge1\),
\[
(H(k)u)_s=2u_s-\frac{\lambda}{1+\lambda^2}
 \bigl((1+e^{ik})u_{s+1}+(1+e^{-ik})u_{s-1}\bigr).
\]
The gauge change \(u_s=e^{-iks/2}v_s\) reduces this to the half-line Jacobi operator
\[
(H(k)v)_0=a v_0-bv_1,\qquad
(H(k)v)_s=2v_s-b(v_{s-1}+v_{s+1})\ (s\ge1),
\]
where \(a=2\lambda^2/(1+\lambda^2)\) and
\(b=2\lambda\cos(k/2)/(1+\lambda^2)\ge0\). For \(b>0\), the bulk recurrence for a decaying mode \(v_s=r^s\) gives
\[
E=2-b(r+r^{-1}),\qquad E=a-br.
\]
Equating the two expressions yields \(2-a=b/r\), hence
\[
r=\frac{b}{2-a}=\lambda\cos(k/2).
\]
Because \(0\le r<1\), this is the decaying root, and substitution into the boundary equation gives the stated \(E_{\mathrm{edge}}(k)\). Below the bulk band, the constant-coefficient second-order recurrence has only one decaying solution up to scale; the boundary equation fixes its ratio to this value, so there is no second eigenvalue below the band. At \(|k|=\pi\), \(b=0\): the boundary site has eigenvalue \(a\), while all interior sites have energy \(2\), so the same formula and uniqueness conclusion hold with the eigenvector supported at \(s=0\).

The bulk band is \([2-2b,2+2b]\). Direct subtraction gives
\[
(2-2b)-E_{\mathrm{edge}}(k)
=\frac{2(1-\lambda\cos(k/2))^2}{1+\lambda^2},
\]
which is strictly positive since \(\lambda<1\). Transforming back from \((s,j)\) gives the displayed amplitude \(\psi_k(x,y)\). Finally, the Taylor expansion \(\sin^2(k/2)=k^2/4+O(k^4)\) gives the quadratic edge coefficient. These steps prove the fiber statement; they do not turn a Bloch wave into a globally square-summable eigenvector along the infinite edge.

## Verification

The analytic proof reduces the claim to the boundary equation and the constant-coefficient bulk recurrence, including the separate endpoint case \(b=0\). The accompanying standard-library script checks the recurrence residuals, the exact separation identity, and positivity of the separation on a grid of parameter values. Those finite numerical checks are consistency checks only; the proof above establishes the statement for every \(k\in[-\pi,\pi]\) and \(\lambda\in(0,1)\).

## Relationship to prior work

Bachmann, Hamza, Nachtergaele, and Young analyze the same one-species PVBS model and prove gaplessness for the diagonal half-plane by constructing finite-diamond variational states whose Rayleigh quotients are of order \(L^{-2}\). Their paper also notes that PVBS excitations have a non-flat dispersion relation, but the inspected edge-state argument gives an upper-bound construction rather than the exact Bloch-fiber eigenvalue and normal profile stated here. Bishop, Nachtergaele, and Young classify gaplessness by half-space orientation and explicitly note that the finite-volume closing rate is not established in general; their stated bounds do not give this exact band or its separation from the bulk band. The present claim is narrower in model scope but sharper about the one-particle edge spectrum. The literature searches are not a proof of priority, and related work outside the inspected sources may contain an equivalent diagonalization.

## Limitations

The result applies only to equal couplings on the diagonal half-space with \(0<\lambda<1\). It does not establish the full many-particle spectrum, finite-diamond eigenvalue asymptotics with a matching lower bound, robustness under perturbations, or formulas for anisotropic couplings and other boundary orientations. The edge branch is a fiber eigenvalue; the corresponding plane wave is not globally in \(\ell^2(D)\) along the boundary.

## References

1. S. Bachmann, E. Hamza, B. Nachtergaele, and A. Young, *Product Vacua and Boundary State Models in d Dimensions*, arXiv:1410.0398v1 (first public version submitted 2014-10-01), *Journal of Statistical Physics* 160 (2015), 636–658.
2. M. Bishop, B. Nachtergaele, and A. Young, *Spectral Gap and Edge Excitations of d-dimensional PVBS models on half-spaces*, arXiv:1509.07550v1 (first public version submitted 2015-09-24), *Journal of Statistical Physics* 162 (2016), 1485–1521.
