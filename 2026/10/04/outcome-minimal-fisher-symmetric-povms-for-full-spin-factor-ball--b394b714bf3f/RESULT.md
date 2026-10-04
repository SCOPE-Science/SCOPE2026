# Outcome-minimal Fisher-symmetric POVMs for full spin-factor balls

## Finding
Let \(\gamma_1,\ldots,\gamma_d\) be Hermitian matrices on a \(D\)-dimensional Hilbert space satisfying
\[
\gamma_j\gamma_k+\gamma_k\gamma_j=2\delta_{jk}I,
\qquad \operatorname{Tr}(\gamma_j)=0,
\qquad \operatorname{Tr}(\gamma_j\gamma_k)=D\delta_{jk}.
\]
For the full spin-factor model
\[
\rho_\theta=\frac1D\left(I+\sum_{j=1}^d\theta_j\gamma_j\right),
\qquad \theta\in\mathbb R^d,\quad \|\theta\|<1,
\]
and every \(d\ge4\), there is, at every interior parameter \(\theta\), a single \((d+1)\)-outcome POVM whose classical Fisher matrix is exactly
\[
F_\theta=\frac1d J_\theta,
\qquad
J_\theta=(I-\theta\theta^{\mathsf T})^{-1}.
\]
Consequently the measurement attains the SLD-isotropic spin-factor optimum for weight \(W=J_\theta\), namely \(\operatorname{tr}(J_\theta V)=d^2\) for the efficient locally unbiased covariance \(V=F_\theta^{-1}\). Moreover \(d+1\) is the smallest possible number of positive-probability outcomes for any finite POVM attaining this full-rank Fisher matrix.

The construction is explicit. Put \(r=\|\theta\|\), choose a unit vector \(e\) with \(\theta=re\) (arbitrary \(e\) when \(r=0\)), and write
\[
\Delta=d+1-(d-1)r,
\quad
p_0=\frac{1+r}{\Delta},
\quad
p_1=\frac{1-r}{\Delta},
\quad
c=\frac{(d-1)r-1}{d}.
\]
Choose unit vectors \(u_1,\ldots,u_d\in e^\perp\) forming a regular simplex:
\[
\sum_{k=1}^d u_k=0,
\qquad
\sum_{k=1}^d u_ku_k^{\mathsf T}=\frac{d}{d-1}P_{e^\perp}.
\]
Set
\[
z_0=e,
\qquad
z_k=ce+\sqrt{1-c^2}\,u_k\quad(1\le k\le d),
\]
with probabilities \(p_0\) for \(z_0\) and \(p_1\) for each \(z_k\). These satisfy
\[
\sum_i p_i z_i=\theta,
\qquad
\sum_i p_i(z_i-\theta)(z_i-\theta)^{\mathsf T}=\frac{1-r^2}{d}I.
\]
Let
\[
B=\frac{J_\theta^{1/2}}{\sqrt{1-r^2}},
\qquad
\ell_i=B(z_i-\theta),
\qquad
b_i=p_i\ell_i,
\qquad
 a_i=p_i(1-\theta^{\mathsf T}\ell_i).
\]
Then the \(d+1\) effects
\[
M_i=a_iI+\sum_{j=1}^d(b_i)_j\gamma_j
\]
form the desired POVM.

For the five-parameter \(\Gamma^5\) example in the motivating paper, this is a six-outcome optimum at every interior point. The paper's generic realization of the same isotropic Fisher target randomizes five binary spectral measurements, producing ten labeled outcomes; the simplex construction therefore reaches the same local precision with the provably smallest outcome alphabet.

## Assumptions and scope
The model is the full affine spin-factor ball, not an arbitrary curved submodel. The parameter point is interior, \(\|\theta\|<1\), so \(J_\theta\) is positive definite. Outcome count means outcomes with strictly positive probability at the operating point; zero-probability outcomes can be deleted locally. The claim concerns a measurement designed for the chosen local point. It does not produce one parameter-independent POVM that is simultaneously optimal throughout the ball.

The originality claim is restricted to \(d\ge4\). Fisher-symmetric POVMs for arbitrary mixed qubit states, corresponding to the three-parameter Bloch ball, were already exhibited before the recent spin-factor work. Pure-state Fisher-symmetric measurements and collective universal constructions are also prior work and are not claimed here.

## Proof
First compute the SLD metric. For a tangent vector \(v\in\mathbb R^d\), write an SLD as \(L_v=aI+\gamma(b)\), where \(\gamma(b)=\sum_j b_j\gamma_j\). The equation
\[
\frac12\{\rho_\theta,L_v\}=\frac1D\gamma(v)
\]
reduces, using the Clifford anticommutation relations, to
\[
a+\theta^{\mathsf T}b=0,
\qquad
b+a\theta=v.
\]
Thus
\[
a=-\frac{\theta^{\mathsf T}v}{1-r^2},
\qquad
b=(I-\theta\theta^{\mathsf T})^{-1}v,
\]
and direct substitution gives
\[
J_\theta=(I-\theta\theta^{\mathsf T})^{-1}.
\]

Now verify the biased-simplex moments. The displayed values of \(p_0,p_1,c\), together with the regular-simplex identities, give
\[
p_0+dp_1=1,
\qquad
p_0+dp_1c=r.
\]
The transverse second moment is
\[
\frac{dp_1(1-c^2)}{d-1}=\frac{1-r^2}{d},
\]
and the axial second moment is
\[
p_0+dp_1c^2=r^2+\frac{1-r^2}{d}.
\]
Cross moments vanish because \(\sum_k u_k=0\). This proves the stated mean and covariance of the \(z_i\).

For every unit \(z_i\), the transformed score \(\ell_i=B(z_i-\theta)\) lies on the score boundary
\[
\|\ell_i\|=1-\theta^{\mathsf T}\ell_i.
\]
Indeed, with \(A=I-\theta\theta^{\mathsf T}=J_\theta^{-1}\), the identity
\[
z_i=\theta+\sqrt{1-r^2}\,A^{1/2}\ell_i
\]
and \(\|z_i\|=1\) imply
\[
\|\ell_i\|^2=(1-\theta^{\mathsf T}\ell_i)^2.
\]
The positive sign is forced by \(r<1\): the negative sign would give \(\theta^{\mathsf T}\ell_i=1+\|\ell_i\|>r\|\ell_i\|\), contradicting Cauchy--Schwarz.

Hence \(a_i=p_i\|\ell_i\|=\|b_i\|\), and the Clifford spectrum of \(a_iI+\gamma(b_i)\) is nonnegative. Also
\[
\sum_i b_i=\sum_i p_i\ell_i=0,
\qquad
\sum_i a_i=\sum_i p_i-\theta^{\mathsf T}\sum_i p_i\ell_i=1,
\]
so \(\sum_iM_i=I\). At the operating state,
\[
\operatorname{Tr}(\rho_\theta M_i)=a_i+\theta^{\mathsf T}b_i=p_i,
\]
and differentiation with respect to \(\theta\) gives gradient \(b_i\). Therefore
\[
F_\theta=\sum_i\frac{b_ib_i^{\mathsf T}}{p_i}
=\sum_i p_i\ell_i\ell_i^{\mathsf T}
=B\left(\frac{1-r^2}{d}I\right)B^{\mathsf T}
=\frac1dJ_\theta.
\]
Yamagata's spin-factor Fisher-region theorem says that after SLD normalization the attainable region is exactly the positive semidefinite trace-at-most-one cone. Its weighted optimum for \(W=J_\theta\) therefore has normalized Fisher matrix \(I/d\), which is precisely the matrix above.

Finally, let a finite measurement have \(m\) positive-probability outcomes with score vectors \(s_1,\ldots,s_m\). Every classical model satisfies
\[
\sum_{i=1}^m p_is_i=0.
\]
Thus the \(m\) score vectors have a nontrivial linear dependence, so their span has dimension at most \(m-1\). Because the Fisher matrix is \(\sum_i p_is_is_i^{\mathsf T}\), its rank is at most \(m-1\). An optimum with \(F_\theta=J_\theta/d\) has rank \(d\), forcing \(m\ge d+1\). The construction has exactly \(d+1\), so it is outcome-minimal.

## Verification
The accompanying `verify.py` uses exact rational arithmetic to check the biased-simplex normalization, mean, axial and transverse second-moment identities for multiple dimensions and interior rational radii. It also checks the resulting outcome-count comparison for the \(d=5\) example. These finite checks are regression tests only; the proof above is the general argument.

The source theorem used from Koichi Yamagata's 2026 spin-factor paper was checked at the statement and construction level: the attainable normalized Fisher region is \(\{K\succeq0:\operatorname{tr}K\le1\}\), the weighted optimum has normalized matrix proportional to the square root of the normalized weight, and the explicit generic implementation randomizes spectral measurements of SLD directions. The same paper's five-parameter \(\Gamma^5\) example uses the isotropic target \(K=I/5\).

## Relationship to prior work
Yamagata, *An attainable Gill--Massar-type bound for spin-factor models* (arXiv:2609.23020v1, first public 2026-09-19), proves the exact attainable Fisher region and gives a randomized-spectral-measurement realization. It does not state an exact minimum outcome count for the isotropic optimum or the biased-simplex compression above.

Yamagata, *Sufficient support size of measurements for quantum estimation* (arXiv:2604.21323v1), gives broad finite support-size upper bounds for optimal quantum measurements. Those bounds depend on Hilbert-space and parameter dimensions and do not imply the sharp \(d+1\) support size for this spin-factor optimum.

Li, Ferrie, Gross, Kalev, and Caves, *Fisher-Symmetric Informationally Complete Measurements for Pure States*, Phys. Rev. Lett. 116, 180402 (2016), treats pure-state local models and obtains the corresponding pure-state Fisher-symmetric constructions. Gross, Dangniam, and Caves' public 2015 presentation explicitly records Fisher-symmetric POVMs for arbitrary mixed qubits; that covers the \(d=3\) Bloch-ball specialization and is why the originality claim begins at \(d=4\). Zhu and Hayashi's 2018 universal Fisher-symmetry work concerns collective two-copy measurements and different universality requirements.

The exact claim here is therefore the arbitrary-interior, \(d\ge4\), full-spin-factor statement: the isotropic single-copy optimum always has a constructive \(d+1\)-outcome realization, and \(d+1\) is necessary.

## Limitations
No statement is made for boundary points \(\|\theta\|=1\), where the SLD metric becomes singular, or for curved submodels whose tangent space is a proper subspace of the full spin factor. The POVM depends on the unknown local point and would require localization/adaptation in an operational protocol. Outcome minimality is local and counts positive-probability outcomes; it does not minimize hardware settings, Naimark ancilla dimension, or global calibration cost. The construction's effects are generally not rank-one on the ambient Hilbert space, so it does not contradict broad support-size results that guarantee rank-one optimal POVMs with different outcome bounds.

## References
1. K. Yamagata, *An attainable Gill--Massar-type bound for spin-factor models*, arXiv:2609.23020v1 (2026).
2. K. Yamagata, *Sufficient support size of measurements for quantum estimation*, arXiv:2604.21323v1 (2026).
3. N. Li, C. Ferrie, J. A. Gross, A. Kalev, and C. M. Caves, *Fisher-Symmetric Informationally Complete Measurements for Pure States*, Phys. Rev. Lett. 116, 180402 (2016), arXiv:1507.06904.
4. H. Zhu and M. Hayashi, *Universally Fisher-Symmetric Informationally Complete Measurements*, Phys. Rev. Lett. 120, 030404 (2018), arXiv:1709.06112.
5. J. A. Gross, N. Dangniam, and C. M. Caves, *Fisher symmetry and the geometry of quantum states* (public presentation, 2015).
