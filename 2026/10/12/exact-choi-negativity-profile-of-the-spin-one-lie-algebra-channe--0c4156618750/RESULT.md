# Exact Choi-negativity profile of the spin-one Lie-algebra channel

## Finding

Consider the spin-one \(\mathfrak{su}(2)\) channel introduced in the Lie-algebra-channel family of Ritter. In a Cartesian spin-one basis it is
\[
\mathcal E_p(X)
=(1-p)X+\frac p2\big(\operatorname{Tr}(X)I-X^{\mathsf T}\big),
\qquad 0\le p\le1.
\]
The endpoint \(p=1\) is the qutrit Werner-Holevo, equivalently Landau-Streater, channel.

Let
\[
|\Phi_3\rangle=\frac1{\sqrt3}\sum_{j=0}^2|jj\rangle,
\qquad
J_p=(\operatorname{id}\otimes\mathcal E_p)
(|\Phi_3\rangle\langle\Phi_3|)
\]
be the normalized Choi state. Then the partial transpose has the complete spectrum
\[
\boxed{
\operatorname{spec}(J_p^{T_2})=
\left\{
\left(\frac{2-p}6\right)^{\times5},
\left(\frac{3p-2}6\right)^{\times3},
\left(\frac{1-2p}3\right)^{\times1}
\right\}.
}
\]
Consequently its negativity is exactly
\[
\boxed{
\mathcal N(J_p)=
\begin{cases}
1-\dfrac{3p}2,&0\le p\le\dfrac12,\\[4pt]
\dfrac{4-5p}6,&\dfrac12\le p\le\dfrac23,\\[4pt]
\dfrac{2p-1}3,&\dfrac23\le p\le1.
\end{cases}
}
\]
For every \(p\in[0,1]\), at least one eigenvalue of \(J_p^{T_2}\) is negative. Thus the channel is never PPT and, in particular, never entanglement breaking on its full physical interpolation from the identity channel to the qutrit Werner-Holevo channel.

The profile is nonmonotone. It decreases from
\[
\mathcal N(J_0)=1
\]
to the unique minimum
\[
\boxed{\mathcal N(J_{2/3})=\frac19},
\]
and then increases to
\[
\mathcal N(J_1)=\frac13.
\]
The minimum occurs exactly at Ritter's physical critical value \(p=2/3\), where the source's rank-two symmetric-tensor sector is erased. Thus the source's strongest one-sector decoherence point is not a PPT transition: it is the point of least Choi negativity, after which Choi entanglement revives as the channel approaches the Werner-Holevo endpoint.

## Assumptions and scope

The parameter is restricted to the completely positive trace-preserving range \(0\le p\le1\) used in the source. The spin is exactly one, so the system dimension is three.

The Choi state is normalized to unit trace. Negativity means
\[
\mathcal N(\rho)=\frac{\|\rho^{T_2}\|_1-1}2.
\]
The statement concerns Choi-state entanglement and the PPT/entanglement-breaking property of the channel. It does not assert a formula for quantum capacity, private capacity, degradability, or entanglement transmission of arbitrary input states.

The equivalence between the spin-one Landau-Streater endpoint and the qutrit Werner-Holevo channel is basis dependent at the matrix-form level but unitary at the channel level; Choi partial-transpose eigenvalues and negativity are invariant under the corresponding local unitary changes of basis.

## Proof

Let \(F\) be the swap operator on \(\mathbb C^3\otimes\mathbb C^3\), and let
\[
P_\Phi=|\Phi_3\rangle\langle\Phi_3|.
\]
In the Cartesian spin-one representation the angular-momentum matrices satisfy
\[
(J_a)_{bc}=-i\varepsilon_{abc},
\]
so contraction of two Levi-Civita tensors gives, for every \(3\times3\) matrix \(X\),
\[
\sum_{a=1}^3J_aXJ_a
=\operatorname{Tr}(X)I-X^{\mathsf T}.
\]
Since the spin-one Casimir is \(2I\), Ritter's channel is therefore the displayed interpolation
\[
\mathcal E_p(X)
=(1-p)X+\frac p2\big(\operatorname{Tr}(X)I-X^{\mathsf T}\big).
\]

The normalized Choi state of the identity channel is \(P_\Phi\). The normalized Choi state of
\[
X\longmapsto\frac12\big(\operatorname{Tr}(X)I-X^{\mathsf T}\big)
\]
is
\[
\frac16(I-F).
\]
Hence
\[
J_p=(1-p)P_\Phi+\frac p6(I-F).
\]
Partial transposition on the second subsystem uses
\[
P_\Phi^{T_2}=\frac13F,
\qquad
F^{T_2}=3P_\Phi,
\]
and gives
\[
J_p^{T_2}
=\frac{1-p}3F+\frac p6(I-3P_\Phi).
\]

Now decompose \(\mathbb C^3\otimes\mathbb C^3\) orthogonally into three invariant pieces:
\[
\mathcal H_- = \operatorname{ran}\frac{I-F}2,
\qquad \dim\mathcal H_-=3,
\]
\[
\mathbb C|\Phi_3\rangle,
\qquad \dim=1,
\]
and
\[
\mathcal H_+^0
=\operatorname{ran}\left(\frac{I+F}2-P_\Phi\right),
\qquad \dim\mathcal H_+^0=5.
\]
On these spaces, respectively, \((F,P_\Phi)\) acts as
\[
(-1,0),\qquad(1,1),\qquad(1,0).
\]
Substitution gives the three eigenvalues
\[
\frac{3p-2}6,
\qquad
\frac{1-2p}3,
\qquad
\frac{2-p}6
\]
with multiplicities \(3,1,5\), proving the spectral formula.

The last eigenvalue is positive throughout \(0\le p\le1\). The antisymmetric eigenvalue is negative exactly for \(p<2/3\), while the maximally-entangled-line eigenvalue is negative exactly for \(p>1/2\). These two negativity intervals overlap, so no physical \(p\) makes the partial transpose positive. Summing the absolute values of the negative eigenvalues yields the stated three-piece formula.

Each piece is affine. Its slopes are respectively
\[
-\frac32,
\qquad
-\frac56,
\qquad
\frac23.
\]
Therefore the unique global minimum occurs at the common breakpoint \(p=2/3\), where the value is \(1/9\).

## Verification

The accompanying `verify_choi_negativity.py` uses exact rational arithmetic. It constructs the normalized Choi matrix directly from the channel action on matrix units, performs the second-system partial transpose, and verifies its equality to
\[
\frac{1-p}3F+\frac p6(I-3P_\Phi)
\]
as an affine polynomial in \(p\).

It then constructs the three orthogonal projectors above, checks their ranks \(3,1,5\), verifies the exact spectral decomposition, and checks the piecewise negativity at rational points in all three parameter intervals. The recorded replay output is `VERIFY_OK`.

The computation is supplementary. The proof of the spectrum, NPT property, and global minimum is analytic for the entire continuum \(0\le p\le1\).

## Relationship to prior work

Ritter's 2005 paper defines the spin-one Lie-algebra channel, derives its tensor-sector action, identifies \(p=2/3\) as the only physical critical value in its convex-sector analysis, and records the equivalence of the \(p=1\) endpoint with the Werner-Holevo channel. It does not analyze the Choi partial-transpose spectrum or Choi negativity across \(p\).

Filippov and Kuzhamuratova later analyze the Landau-Streater endpoint and show, among other properties, that the spin-one endpoint is not entanglement breaking. This covers an endpoint consequence but not the interpolation or its exact Choi-negativity profile.

Roofeh and Karimipour study exactly the same qutrit interpolation
\[
\Lambda_x=(1-x)\operatorname{id}+x\Lambda_1
\]
in 2023--2024, including covariance, degradability, and capacity bounds. Their inspected full text defines the family and uses Choi matrices in a capacity bound, but searches of the full text for PPT, separability, entanglement breaking, partial-transpose negativity, and negativity did not locate the spectrum or the piecewise formula proved here.

Zhu and Wang's 2026 work proves that the special point \(p=1/2\) is not PPT while establishing a substantially deeper zero-capacity result. Thus NPT at \(p=1/2\) is prior coverage and is not claimed as new here. The present claim is the full \(p\)-dependent spectrum, exact negativity law, all-parameter NPT conclusion, and identification of \(p=2/3\) as the unique Choi-negativity minimum.

## Limitations

The result is specific to the spin-one, three-dimensional interpolation. It does not establish an analogous law for higher-spin Landau-Streater channels or higher-dimensional generalized Werner-Holevo channels.

NPT of the Choi state rules out entanglement breaking, but it does not by itself determine quantum or private capacity. In particular, the recent \(p=1/2\) result shows that NPT can coexist with zero quantum and private capacity.

The literature comparison cannot exclude every differently named equivalent formulation. The closest exact-family paper and the recent \(p=1/2\) NPT paper were inspected explicitly, and the latter is recorded as partial prior coverage.

## References

1. W. G. Ritter, “Quantum Channels and Representation Theory,” arXiv:quant-ph/0502153; J. Math. Phys. 46, 082103 (2005), DOI: 10.1063/1.1945768.
2. S. N. Filippov and K. V. Kuzhamuratova, “Quantum informational properties of the Landau-Streater channel,” arXiv:1803.02572; J. Math. Phys. 60, 042202 (2019), DOI: 10.1063/1.5037700.
3. S. Roofeh and V. Karimipour, “The noisy Werner-Holevo channel and its properties,” arXiv:2310.15353; Phys. Rev. A 109, 052620 (2024), DOI: 10.1103/PhysRevA.109.052620.
4. C. Zhu and X. Wang, “Quantum Incapacity beyond No-Cloning and PPT Mechanisms,” arXiv:2607.24693 (2026).
5. M. Horodecki, P. W. Shor, and M. B. Ruskai, “Entanglement Breaking Channels,” Rev. Math. Phys. 15, 629–641 (2003), DOI: 10.1142/S0129055X03001709.
