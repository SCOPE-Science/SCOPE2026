# Exact transverse Hessian of the length-six Barker code

## Finding
Let \(\zeta=e^{i\pi/3}\) and
\[
b=(1,1,\zeta,-1,1,-\zeta).
\]
For a phase vector \(\theta=(\theta_0,\ldots,\theta_5)\), define the aperiodic autocorrelations and base energy by
\[
C_k(\theta)=\sum_{j=0}^{5-k}e^{i(\theta_{j+k}-\theta_j)},\qquad
E(\theta)=\sum_{k=1}^{5}|C_k(\theta)|^2.
\]
At
\[
\theta_*=(0,0,\pi/3,\pi,0,4\pi/3),
\]
one has \(E(\theta_*)=5\), \(\nabla E(\theta_*)=0\), and
\[
\operatorname{Hess}E(\theta_*)=
\begin{pmatrix}
4&-6&-1&2&3&-2\\
-6&10&0&-3&-4&3\\
-1&0&4&-2&-3&2\\
2&-3&-2&4&0&-1\\
3&-4&-3&0&10&-6\\
-2&3&2&-1&-6&4
\end{pmatrix}.
\]
The characteristic polynomial is
\[
\lambda^2(\lambda-1)(\lambda-5)(\lambda-9)(\lambda-21).
\]
The kernel is exactly
\[
\operatorname{span}\{(1,1,1,1,1,1),(0,1,2,3,4,5)\},
\]
which is the tangent space to the common-phase and linear-phase-modulation orbit. Therefore the Barker orbit is a strict local minimizer of \(E\) modulo those symmetries, and its exact transverse Hessian spectrum is \(\{1,5,9,21\}\).

Equivalently, for
\[
P_\theta(t)=\sum_{j=0}^{5}e^{i\theta_j}e^{ijt},
\]
with normalized Haar measure on the circle,
\[
\|P_\theta\|_4^4=36+2E(\theta).
\]
Thus \(\|P_{\theta_*}\|_4^4=46\), and the transverse Hessian spectrum of the fourth moment is \(\{2,10,18,42\}\).

## Assumptions and scope
All six coefficients have modulus one. The claim is local: it determines the complete second variation at the indicated Barker orbit and proves strict local minimality modulo the two continuous phase symmetries. It does not assert that \(E=5\) is the global minimum over all length-six unimodular sequences.

The phase symmetries are
\[
\theta_j\longmapsto \theta_j+\alpha+j\beta.
\]
They preserve every \(|C_k|\), so two Hessian zero modes are unavoidable.

## Proof
Write
\[
d_{j,k}=e_{j+k}-e_j\in\mathbb R^6,
\qquad
u_{j,k}=e^{i(\theta_{j+k}-\theta_j)}.
\]
For a fixed lag \(k\), put
\[
C_k=\sum_ju_{j,k},\qquad
A_k=\sum_ju_{j,k}d_{j,k},\qquad
B_k=\sum_ju_{j,k}d_{j,k}d_{j,k}^{\mathsf T}.
\]
Direct differentiation gives
\[
\nabla |C_k|^2=2\operatorname{Re}\!\left(iA_k\overline{C_k}\right)
\]
and
\[
\operatorname{Hess}|C_k|^2
=2\operatorname{Re}\!\left(-\overline{C_k}B_k+A_k\overline{A_k}^{\mathsf T}\right).
\]
At \(\theta_*\), all quantities lie in the Eisenstein-type ring \(\mathbb Z[\zeta]\), with \(\zeta^2-\zeta+1=0\). The five autocorrelations are
\[
-\tfrac12+\tfrac{\sqrt3}{2}i,\quad
\tfrac12+\tfrac{\sqrt3}{2}i,\quad
-1,\quad
\tfrac12-\tfrac{\sqrt3}{2}i,\quad
-\tfrac12-\tfrac{\sqrt3}{2}i,
\]
so every sidelobe has modulus one and \(E(\theta_*)=5\). Substitution into the derivative formula gives zero gradient and, after summing the five lag contributions, the displayed integer matrix \(H\).

The two vectors
\[
u=(1,1,1,1,1,1),\qquad v=(0,1,2,3,4,5)
\]
are annihilated by \(H\), as expected from the two exact symmetries. Exact determinant expansion gives
\[
\det(\lambda I-H)=\lambda^2(\lambda-1)(\lambda-5)(\lambda-9)(\lambda-21).
\]
Hence the kernel has dimension two and is exactly \(\operatorname{span}\{u,v\}\); every transverse eigenvalue is positive. The standard second-derivative test on a transverse slice therefore makes the whole symmetry orbit a strict local minimum. More precisely, if \(h\perp u,v\), then
\[
E(\theta_*+h)=5+\tfrac12 h^{\mathsf T}Hh+O(\|h\|^3),
\]
with sharp smallest transverse Hessian eigenvalue \(1\).

Finally, Parseval applied to \(P_\theta^2\) gives \(\|P_\theta\|_4^4=36+2E(\theta)\), yielding the fourth-moment formulation.

## Verification
The accompanying `verify.py` works with exact arithmetic in \(\mathbb Z[\zeta]\). It reconstructs all five sidelobes, checks the vanishing gradient conditions, reconstructs every entry of the Hessian from the differentiated correlation formula, verifies the two symmetry kernel vectors, and expands the characteristic polynomial by an exact permutation determinant. It then checks the factorization into \(\lambda^2(\lambda-1)(\lambda-5)(\lambda-9)(\lambda-21)\).

## Relationship to prior work
Zhang and Golomb proved that the generalized Barker sequence of length six is unique up to Barker-preserving transformations. Their proof is a global peak-sidelobe classification: it imposes \(|C_k|\le1\) and does not compute the base-energy Hessian or a second-variation spectrum.

Borwein and Ferguson study the base energy \(\sum |C_k|^2\) directly and use calculus-driven stochastic search for local minima. Their length-six table reports base energy \(5.000\), maximum sidelobe \(1.000\), and alphabet size \(6\); their discussion explicitly treats base-energy local minima as objects found by optimization. No Hessian or exact transverse curvature is given there.

Neuwirth's Fourier-extremal work provides the harmonic-analysis setting in which phase variation of trigonometric polynomials is studied systematically. Its primary classification is MSC 42A05. The present calculation concerns the fourth Fourier moment of a six-term unimodular polynomial rather than the maximum modulus of a trinomial.

## Limitations
This is a local theorem. It neither proves global optimality of base energy \(5\) among all length-six unimodular sequences nor classifies every base-energy critical point. The exact spectrum is for the standard Euclidean metric on phase coordinates; the positivity statement modulo the two symmetry directions is invariant, while numerical curvature values depend on that natural phase metric.

## References
1. Stefan Neuwirth, *The maximum modulus of a trigonometric trinomial*, arXiv:math/0703236, first submitted 2007-03-08; primary MSC 42A05.
2. Ning Zhang and Solomon W. Golomb, *Uniqueness of the generalized Barker sequence of length 6*, IEEE Transactions on Information Theory 36 (1990), 1167–1170, DOI: 10.1109/18.57221.
3. Peter Borwein and Ron Ferguson, *Polyphase Sequences With Low Autocorrelation*, IEEE Transactions on Information Theory 51 (2005), 1564–1567, DOI: 10.1109/TIT.2004.842778.
