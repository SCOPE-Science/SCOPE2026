# Geometric-phase crossings of the maximal Gaussian localization eigenvalue on equilateral three-disk sets

## Finding

Let \(\mathcal F^2\) be the Bargmann--Fock space with Gaussian measure \(\pi^{-1}e^{-|z|^2}\,dA(z)\). Put \(\omega=e^{2\pi i/3}\) and, for \(R,\varepsilon>0\), let
\[
 \Omega_{R,\varepsilon}=\bigcup_{j=0}^2\{z\in\mathbb C:|z-R\omega^j|<\varepsilon\}.
\]
Let \(T_{R,\varepsilon}\) be the positive localization operator specified by
\[
 \langle T_{R,\varepsilon}f,f\rangle
   ={1\over\pi}\int_{\Omega_{R,\varepsilon}}|f(z)|^2e^{-|z|^2}\,dA(z),
 \qquad f\in\mathcal F^2.
\]
For every integer \(m\ge0\), define
\[
 R_m=\left({2(2m+1)\pi\over3\sqrt3}\right)^{1/2}.
\]
There exist \(\varepsilon_m>0\), a neighborhood \(I_m\) of \(R_m\), and, for all \(0<\varepsilon<\varepsilon_m\), a *unique* radius \(R_m(\varepsilon)\in I_m\) at which the two leading rotation-sector eigenvalue branches of \(T_{R,\varepsilon}\) coincide. The crossing is transverse, and
\[
 R_m(\varepsilon)=R_m+O_m(\varepsilon^2),\qquad
 \lambda_1(T_{R_m(\varepsilon),\varepsilon})
 =\lambda_2(T_{R_m(\varepsilon),\varepsilon})
 >\lambda_3(T_{R_m(\varepsilon),\varepsilon}).
\]
The maximal eigenvalue thus has **exact multiplicity two** for genuine unions of three disjoint open disks at infinitely many distinct, unbounded limiting triangle radii. Eigenvectors for the coincident eigenvalue belong to distinct characters of the threefold rotation. Here eigenvalues are counted with multiplicity and in nonincreasing order.

## Assumptions and scope

All assertions concern complex Bargmann--Fock space in one complex dimension, the normalization explicitly displayed above, and three *equal* Euclidean disks centered at the vertices of a centered equilateral triangle. For each fixed \(m\), the disks must be sufficiently small (depending on \(m\)); in particular \(\varepsilon_m\) may be chosen below \(\sqrt3R_m/4\). The result makes no assertion of a common disk-size threshold uniform in \(m\), and the local uniqueness is uniqueness only within the stated neighborhood \(I_m\). The family is a natural three-site, equal-area Gaussian time-frequency concentration model.

## Proof

**1. Coherent-state representation and operator-norm limit.** The normalized coherent vector at \(\zeta\in\mathbb C\) is
\[
 k_\zeta(w)=\exp(w\overline\zeta-|\zeta|^2/2),
 \qquad\|k_\zeta\|_{\mathcal F^2}=1.
\]
With \(P_\zeta=|k_\zeta\rangle\langle k_\zeta|\), the reproducing property implies the exact Bochner integral identity
\[
 T_{R,\varepsilon}={1\over\pi}\int_{\Omega_{R,\varepsilon}}P_z\,dA(z).
\]
It is a positive trace-class operator with trace \(3\varepsilon^2\) whenever the disks are disjoint. Therefore the normalized operator \(H_{R,\varepsilon}=\varepsilon^{-2}T_{R,\varepsilon}\) has trace \(3\). Changing variables inside each disk yields
\[
 H_{R,\varepsilon}=\sum_{j=0}^2{1\over\pi\varepsilon^2}
 \int_{|u|<\varepsilon}P_{R\omega^j+u}\,dA(u).
\]
The map \(\zeta\mapsto P_\zeta\) is smooth as an operator-valued map in both real coordinates, together with all real derivatives on compact subsets of \(\mathbb C\). The centered-disk linear moments vanish; Taylor's formula consequently proves, uniformly for \(R\) in any fixed compact subset of \((0,\infty)\),
\[
 H_{R,\varepsilon}=S_R+O(\varepsilon^2),\qquad
 {d\over dR}H_{R,\varepsilon}={d\over dR}S_R+O(\varepsilon^2)
 \quad\text{in operator norm},
\]
where \(S_R=\sum_{j=0}^2P_{R\omega^j}\). The differentiation estimate follows by applying the same Taylor argument to the first \(R\)-derivative of each projector. This is a \(C^1\) estimate, not only pointwise weak convergence.

**2. Exact finite-rank comparison spectrum.** Define \(\rho(R)=e^{-3R^2/2}\) and \(\vartheta(R)=\sqrt3R^2/2\). The coherent-vector overlap formula is
\[
 \langle k_\zeta,k_\eta\rangle
  =\exp\left(\eta\overline\zeta-\frac{|\zeta|^2+|\eta|^2}{2}\right).
\]
Thus the three-by-three Gram matrix for \(k_R,k_{R\omega},k_{R\omega^2}\) is Hermitian circulant: adjacent overlaps have modulus \(\rho\) and phase \(\pm\vartheta\). Its eigenvalues, also the three nonzero eigenvalues of \(S_R\), form exactly the multiset
\[
 g_\ell(R)=1+2\rho(R)\cos\left(\vartheta(R)-{2\pi\ell\over3}\right),
 \qquad \ell=0,1,2.
\]
The remaining spectrum of \(S_R\) equals zero. The coherent vectors at distinct points are linearly independent, hence each of these three numbers is strictly positive for \(R>0\).

At \(R=R_m\), \(\vartheta(R_m)=(2m+1)\pi/3\). Two distinct rotation sectors have the common maximal eigenvalue \(1+\rho_m\), and the third sector has eigenvalue \(1-2\rho_m\), where \(\rho_m=e^{-3R_m^2/2}\). The leading-to-third gap is exactly \(3\rho_m>0\). Since \(\vartheta'(R)=\sqrt3R\), differentiating the two crossing formulas gives the **nonzero derivative difference**
\[
 \left|{d\over dR}\bigl(g_{a_m}(R)-g_{b_m}(R)\bigr)\Big|_{R=R_m}\right|
   =6R_m\rho_m>0.
\]
The indices \(a_m\ne b_m\) identify two different one-dimensional characters of the threefold rotation.

**3. Persistence as an exact infinite-dimensional crossing.** The unitary action of rotation by \(2\pi/3\) splits \(\mathcal F^2\) orthogonally into three closed eigenspaces (equivalently, monomials with degrees congruent modulo \(3\)). Both \(S_R\) and the *actual* operator \(H_{R,\varepsilon}\) commute with this rotation, since the three-disk set is invariant. At the limiting crossing, in each leading sector the corresponding eigenvalue \(1+\rho_m\) is simple and isolated: all other eigenvalues of \(S_{R_m}\) in that sector are zero. By continuity and the positive \(3\rho_m\) gap to the third leading sector, one can choose a compact interval \(I_m\) centered at \(R_m\) where the two relevant sector-leading eigenvalues remain isolated from all other eigenvalues.

Standard isolated self-adjoint eigenvalue perturbation, applied within each invariant sector to the operator-norm \(C^1\) estimate above, yields two \(C^1\) sector branches \(h_{a_m}(R,\varepsilon)\) and \(h_{b_m}(R,\varepsilon)\) satisfying
\[
 h_{a_m}(R,\varepsilon)=g_{a_m}(R)+O_m(\varepsilon^2),\qquad
 h'_{a_m}(R,\varepsilon)=g'_{a_m}(R)+O_m(\varepsilon^2),
\]
and the analogous estimates for \(b_m\), uniformly on \(I_m\). After shrinking \(I_m\) if necessary, the derivative of their difference has fixed nonzero sign on \(I_m\). Since the limiting difference changes sign across \(R_m\), the intermediate-value theorem provides exactly one root \(R_m(\varepsilon)\in I_m\) for every sufficiently small positive \(\varepsilon\). The mean-value theorem and the \(O_m(\varepsilon^2)\) perturbation give \(R_m(\varepsilon)-R_m=O_m(\varepsilon^2)\). The spectral gap to the third sector and the rest of the spectrum persists by the norm estimate; therefore the common branch at the root is exactly the first and second eigenvalue, strictly above the third. Distinct rotation sectors prohibit an avoided crossing, and the derivative difference stays nonzero, proving transversality.

Finally, \(R_m\to\infty\) as \(m\to\infty\). Choosing \(\varepsilon_m\) also small enough that \(2\varepsilon_m<\sqrt3\inf I_m\) guarantees the three open disks are pairwise disjoint, so these are bona fide finite-area localization regions rather than point measures. The theorem follows.

## Verification

The proof is analytic and infinite-dimensional. The supplementary `triad_checker.py` independently constructs finite-section Fock Toeplitz matrices by Gaussian area quadrature and exploits the three rotation sectors. It checks three finite-disk top-sector crossings, for \(m=0,1,2\), and three independent small-disk-to-point-spectrum comparisons, all within printed tolerances. Execute `python triad_checker.py` with Python 3, NumPy, and SciPy. These finite calculations corroborate normalization and branch selection; they are **not** used to infer existence for arbitrarily large \(m\). The infinite family follows instead from the exact Gram formula and the uniform \(C^1\) operator perturbation argument for each fixed \(m\).

## Relationship to prior work

Nicola and Tilli prove the sharp Faber--Krahn principle for Gaussian short-time Fourier concentration: a single disk uniquely optimizes concentration at prescribed area. Gómez, Guerra, Ramos, and Tilli prove quantitative stability relative to the disk optimizer. These global concentration and stability results do not specify repeated coincidences of the leading localization eigenvalues for three widely separated equal disks. Bauer, Fulsche, and Rodríguez survey Fock Toeplitz operator classes and general operator-algebra questions; the inspected relevant sections do not contain this local three-disk top-eigenvalue crossing law. The coherent-state Gram identity and isolated-eigenvalue perturbation are established tools, but combining the nontrivial circulating phase, its infinitely many crossings, and symmetry-protected persistence in an actual infinite-dimensional disk localization operator supplies the present exact spectral statement. Priority outside the inspected sources remains open to further bibliographic checking.

## Limitations

The result concerns the equal-radius, exactly threefold symmetric configuration only. It does not give a disk-radius threshold uniform over all \(m\), prove crossings for any prescribed positive disk radius, provide a global classification of all crossings, or extend to general asymmetric configurations. The quantitative perturbation constants can deteriorate quickly as \(m\to\infty\), because the limiting spectral gap \(3\rho_m\) tends to zero. Numerical finite sections cannot certify the infinite-dimensional theorem by themselves. No independent mathematical audit has been performed.

## References

1. Fabio Nicola and Paolo Tilli, *The Faber--Krahn inequality for the Short-time Fourier transform*, arXiv:2106.03423 (first submitted 2021-06-07); *Inventiones Mathematicae* 230 (2022), 1--30. https://arxiv.org/abs/2106.03423
2. Jaime Gómez, André Guerra, João P. G. Ramos, and Paolo Tilli, *Stability of the Faber--Krahn inequality for the Short-time Fourier Transform*, arXiv:2307.09304 (first submitted 2023-07-18). https://arxiv.org/abs/2307.09304
3. Wolfram Bauer, Robert Fulsche, and Miguel Angel Rodríguez Rodríguez, *Operators in the Fock-Toeplitz algebra*, arXiv:2405.20792 (first submitted 2024-05-31). https://arxiv.org/abs/2405.20792
