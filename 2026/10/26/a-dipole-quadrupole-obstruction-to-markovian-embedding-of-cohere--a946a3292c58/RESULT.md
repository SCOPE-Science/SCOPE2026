# A dipole–quadrupole obstruction to Markovian embedding of coherent-spin measurements

## Finding
Let \(j\) be any positive integer or half-integer, and let \(P_\omega\) be the rank-one spin-\(j\) coherent-state projector in direction \(\omega\in S^2\). The nonselective coherent-spin measurement channel
\[
\mathcal M_j(X)=\frac{2j+1}{4\pi}\int_{S^2}\operatorname{tr}(P_\omega X)P_\omega\,d\omega
\]
is the time-one member of a time-homogeneous quantum Markov semigroup \(e^{t\mathcal L}\) with a finite-dimensional Gorini–Kossakowski–Sudarshan–Lindblad generator **if and only if** \(j=\frac12\). More generally, for every \(j\ge1\) it is impossible to have \(\mathcal M_j=e^{\tau\mathcal L}\) for any \(\tau>0\), even when \(\mathcal L\) is not required to be rotationally covariant.

Write \(n=2j\). The first two nontrivial multipole eigenvalues of \(\mathcal M_j\) are
\[
\lambda_1=\frac n{n+2},\qquad \lambda_2=\frac{n(n-1)}{(n+2)(n+3)}.
\]
The dimension-independent Markovian obstruction is strict:
\[
\lambda_1^3-\lambda_2=\frac{4n}{(n+2)^3(n+3)}>0\qquad(n\ge2).
\]
Its logarithmic size is \(\log(\lambda_1^3/\lambda_2)=\log(1+4/((n-1)(n+2)^2))=4n^{-3}+O(n^{-4})\). Thus discrete coherent-state monitoring has a non-Markovian signature at every higher spin, although the dipole–quadrupole discrepancy vanishes at a quantified semiclassical rate.

## Assumptions and scope
A *time-homogeneous Markovian embedding* means a norm-continuous, completely positive, trace-preserving semigroup \((e^{t\mathcal L})_{t\ge0}\) on the full \((2j+1)\)-dimensional matrix algebra, with constant GKSL generator \(\mathcal L\). No isotropy, detailed balance, locality, or preassigned Lindblad operators are assumed for a hypothetical embedding. The channel \(\mathcal M_j\) is finite-dimensional, trace preserving, unital, entanglement breaking, and SU(2)-covariant. Its eigenvalues on rank-\(L\) irreducible tensor operators, for \(0\le L\le 2j\), are the established coherent-state POVM coefficients
\[
\lambda_L=\frac{\binom{2j}{L}}{\binom{2j+L+1}{L}}.
\]
They are strictly positive and pairwise distinct. The claim concerns autonomous semigroups only; time-inhomogeneous GKSL evolutions, channels with ancillary memory, and approximate embeddings are not ruled out.

## Proof
**1. A universal completely-positive dipole–quadrupole facet.** Let \(j\ge1\), \(a=j(j+1)\), and \(V_L\) be the spin-\(L\) summand of the conjugation action on operators. Every SU(2)-covariant quantum channel \(\mathcal E\) acts by scalars \(u_L\) on \(V_L\). The SU(2)-covariant channel simplex has extreme channels indexed by integral \(k\in\{0,\ldots,2j\}\), with Kraus operators proportional to the rank-\(k\) normalized tensor operators \(T_{kq}\):
\[
\mathcal E_k(X)=\frac{2j+1}{2k+1}\sum_{q=-k}^{k}T_{kq}XT_{kq}^{\dagger}.
\]
The standard six-\(j\) recoupling formula gives their rank-\(L\) multipliers
\[
 u_L^{(k)}=(-1)^{2j+k+L}(2j+1)
 \begin{Bmatrix}j&j&k\\j&j&L\end{Bmatrix}.
\]
Writing \(s=k(k+1)\), the Racah formula at \(L=1,2\) reduces **exactly** to
\[
 u_1^{(k)}=1-\frac{s}{2a},\qquad
 u_2^{(k)}=1-\frac{3s}{2a}\left(1-\frac{s-2}{4a-3}\right).
\]
Consequently,
\[
 u_2^{(k)}-3u_1^{(k)}+2
   =\frac{3s(s-2)}{2a(4a-3)}\ge0.
\]
Indeed \(s\in\{0,2,6,12,\ldots\}\), and \(4a-3>0\) for \(j\ge1\). Convexity of the channel simplex proves the **universal covariant CPTP constraint**
\[
\boxed{u_2-3u_1+2\ge0.}\tag{1}
\]
Here \(u_1,u_2\) are real; negative values are permitted for individual channels.

**2. A constraint on every covariant Markov semigroup.** For any SU(2)-covariant GKSL generator \(\mathcal K\), its semigroup has real multipole scalars \(u_L(t)=e^{\eta_Lt}\), \(\eta_L\in\mathbb R\), with \(\eta_0=0\). Applying (1) to every \(t\ge0\), differentiating at \(t=0^+\), and noting equality there yields \(\eta_2-3\eta_1\ge0\). With decay rates \(\gamma_L=-\eta_L\), this is
\[
\boxed{\gamma_2\le3\gamma_1.}\tag{2}
\]
It follows in particular that \(u_2(t)\ge u_1(t)^3\) for all \(t\ge0\). This is a necessary inequality for **all** SU(2)-covariant Markovian semigroups, not just the familiar spin-component Lindbladian.

**3. Why a noncovariant generator cannot evade (2).** Suppose \(e^{\tau\mathcal L}=\mathcal M_j\) for a GKSL generator \(\mathcal L\) and some \(\tau>0\). Because every linear map commutes with its exponential, \(\mathcal L\mathcal M_j=\mathcal M_j\mathcal L\). The distinct eigenvalues \(\lambda_L>0\) therefore force \(\mathcal L\) to preserve each \(V_L\). Inside \(V_L\), choose a real basis of Hermitian spherical tensors, of real dimension \(2L+1\). A GKSL generator is Hermiticity preserving, so its restriction is a real matrix. Taking real determinants in \(e^{\tau\mathcal L}|_{V_L}=\lambda_L I\) yields, without any choice of logarithm branches,
\[
\operatorname{tr}_{\mathbb R}(\mathcal L|_{V_L})
       =\frac{2L+1}{\tau}\log\lambda_L.\tag{3}
\]
Average the generator over rotations:
\[
\overline{\mathcal L}=\int_{SU(2)}\mathcal U_g^{-1}\mathcal L\mathcal U_g\,dg,
\quad \mathcal U_g(X)=U_gXU_g^\dagger.
\]
Each conjugated generator is GKSL, and their finite-dimensional convex average is GKSL because the GKSL cone is convex and closed. The average is covariant. By real Schur irreducibility of \(V_L\), it acts there as \(\overline{\mathcal L}|_{V_L}=(\log\lambda_L/\tau)I\), using (3). Applying (2) now forces \(-\log\lambda_2\le-3\log\lambda_1\), or \(\lambda_2\ge\lambda_1^3\).

**4. Strict contradiction and qubit exception.** For \(n=2j\ge2\), the established spectrum gives
\[
\lambda_1^3-\lambda_2
=\frac{n^3}{(n+2)^3}-\frac{n(n-1)}{(n+2)(n+3)}
=\frac{4n}{(n+2)^3(n+3)}>0,
\]
contradicting (2). When \(j=\frac12\), only ranks zero and one occur and \(\lambda_1=1/3\). The isotropic GKSL generator
\[
\mathcal L_{1/2}(X)=-\frac{\log3}{2}\sum_{a=x,y,z}[J_a,[J_a,X]]
\]
has rank-one eigenvalue \(-\log3\), so \(e^{\mathcal L_{1/2}}=\mathcal M_{1/2}\). Thus the boundary at spin one-half is exact. The asymptotic logarithmic obstruction follows by expanding \(\log(1+4/((n-1)(n+2)^2))\). \(\square\)

## Verification
The companion standalone script `verify.py` independently evaluates the 6-\(j\) symbols and the two low-rank multipliers in exact rational arithmetic at multiple spin values, compares the exact channel-facet identities, and checks the strict coherent-POVM spectral inequality and large-spin asymptotic numerically. It prints assertion counts and exits nonzero on a disagreement. These finite checks corroborate recoupling arithmetic but do **not** replace the all-spin proof or its generator-twirling argument.

## Relationship to prior work
Brody, Graefe, and Melanathuru (arXiv:2605.02696v1, May 4, 2026), Sections III–IV, derive the coherent-spin channel, its complete multipole spectrum, and a mismatch with the **specific** angular-momentum-component Lindblad generator, displaying the spin-one ratio \(\log10/\log2>3\). These spectrum and comparator facts are prior work. The contribution here is the **universal** GKSL nonembeddability conclusion, including fully noncovariant hypothetical generators, proved by the CP facet and generator twirl. Rudnicki et al. (2026), Sections 4–5, and Aschieri–Ruba–Solovej (2024) establish the SU(2) covariant-channel simplex and recoupling framework; these are prior tools. Their inspected material was not found to contain this coherent-spin semigroup impossibility criterion. General channel-semigroup Markovianity is distinguished from divisibility of time-dependent channel families, as in Kattemölle–Gulácsi–Burkard (2026).

## Limitations
No claim is made about time-inhomogeneous generators, ancilla-assisted dilation, or approximate Markovian simulation; these can behave differently. The proof assumes finite spin and the exact isotropic coherent-state measure-and-prepare map. The novelty assessment is best-knowledge, not a priority certification; general covariant-semigroup classifications may contain abstract bounds implying some intermediate lemmas. The principal outcome is the rigorously established explicit nonembeddability of the specified measurement channel.

## References
1. D. C. Brody, E.-M. Graefe, R. Melanathuru, *Phase-space measurements and decoherence for angular momentum systems*, arXiv:2605.02696v1 (2026-05-04), especially equations (21), (27), (30)–(33). https://arxiv.org/abs/2605.02696
2. Ł. Rudnicki, A. Klimov, A. Muñoz, G. Leuchs, L. L. Sánchez-Soto, *SU(2)-Covariant Quantum Channels*, *Symmetry* **18** (2026), 1146, equations (26)–(38). https://doi.org/10.3390/sym18071146
3. T. Aschieri, B. Ruba, J. P. Solovej, *SU(2)-Equivariant Quantum Channels: Semiclassical Analysis*, *Communications in Mathematical Physics* **405** (2024), 298. https://doi.org/10.1007/s00220-024-05178-1
4. J. Kattemölle, B. Gulácsi, G. Burkard, *Non-Markovianity induced by Pauli twirling*, *npj Quantum Information* **12** (2026), 138. https://doi.org/10.1038/s41534-026-01345-5
