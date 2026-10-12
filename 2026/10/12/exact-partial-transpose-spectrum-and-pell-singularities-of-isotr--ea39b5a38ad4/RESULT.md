# Exact partial-transpose spectrum and Pell singularities of isotropic spin-channel Choi states
## Finding
For every spin \(j\in\{1/2,1,3/2,\ldots\}\), let \(d=2j+1\) and let the isotropic spin channel be \(\Lambda_j(X)=[j(j+1)]^{-1}\sum_{a=1}^3 J_a XJ_a\). For its normalized Choi state \(C_j=(\operatorname{id}\otimes\Lambda_j)(|\Omega_d\rangle\langle\Omega_d|)\), the partial transpose has, on the total-spin \(L\) sector, the eigenvalue \[\lambda_L=\frac{(-1)^{2j-L}[L(L+1)-2j(j+1)]}{2(2j+1)j(j+1)},\qquad L=0,1,\ldots,2j,\] with multiplicity \(2L+1\). If \(k_j=\left\lceil(\sqrt{1+8j(j+1)}-1)/2\right\rceil\), then the Choi negativity is exactly \[\mathcal N(C_j)=\frac{k_j^2[4j(j+1)-k_j^2+1]}{4(2j+1)j(j+1)}-\frac12.\] Moreover, \(C_j^{T_2}\) is singular exactly when there is an integer \(L\) with \(L(L+1)=2j(j+1)\), equivalently when \(x=2L+1\) and \(y=2j+1\) solve the negative Pell equation \(x^2-2y^2=-1\). The first nontrivial singular spins are \(j=2,14,84\). The known binary statement that the channel is entanglement breaking only at \(j=1/2\) is prior work and is not claimed as new; the accepted contribution is the all-spin partial-transpose spectrum, the closed negativity law, and the Pell characterization of singular spins.

## Assumptions and scope
Fix a spin \(j\in\{1/2,1,3/2,\ldots\}\), let \(d=2j+1\), and let \(J_1,J_2,J_3\) be the Hermitian spin-\(j\) generators normalized by \(\sum_a J_a^2=j(j+1)I\). The channel is
\[
\Lambda_j(X)=\frac{1}{j(j+1)}\sum_{a=1}^3J_aXJ_a.
\]
This is the isotropic spin channel written by Alicki in Eq. (6) of arXiv:quant-ph/0402080. The Choi state is normalized with \(|\Omega_d\rangle=d^{-1/2}\sum_m|m,m\rangle\). Partial transpose is taken in the standard \(J_z\)-eigenbasis. The theorem concerns the Choi partial-transpose spectrum and its negativity; it does not claim a new binary entanglement-breaking classification.

## Proof
Write \(F\) for the swap operator on \(\mathcal H_j\otimes\mathcal H_j\). For a matrix \(A\), the vectorization identity
\[
(|A\rangle\rangle\langle\langle A|)^{T_2}=(A\otimes A^\dagger)F
\]
shows that \(C_j^{T_2}\) is unitarily equivalent, using the standard spin time-reversal intertwiner, to
\[
\frac{1}{(2j+1)j(j+1)}\left(\sum_{a=1}^3J_a\otimes J_a\right)F.
\]
The two factors commute. Under the Clebsch--Gordan decomposition
\[
\mathcal H_j\otimes\mathcal H_j=\bigoplus_{L=0}^{2j}\mathcal H_L,
\]
the spin-coupling operator satisfies
\[
\sum_aJ_a\otimes J_a=\frac12\left(J_{\rm tot}^2-2j(j+1)I\right),
\]
so its eigenvalue on \(\mathcal H_L\) is \([L(L+1)-2j(j+1)]/2\). Swap acts there by \((-1)^{2j-L}\). Multiplying these eigenvalues gives
\[
\lambda_L=\frac{(-1)^{2j-L}[L(L+1)-2j(j+1)]}{2(2j+1)j(j+1)}
\]
with multiplicity \(2L+1\), proving the spectrum.

For the negativity, let
\[
r_j=\frac{\sqrt{1+8j(j+1)}-1}{2},\qquad k_j=\lceil r_j\rceil,
\]
so that the strictly negative values of \(L(L+1)-2j(j+1)\) occur for \(0\le L\le k_j-1\), except that when \(r_j\) is integral the endpoint \(L=r_j\) is zero and is excluded automatically by the choice \(k_j=r_j\). The polynomial sum
\[
\sum_{L=0}^{m}(2L+1)[L(L+1)-2j(j+1)]
=(m+1)^2\left(\frac{m(m+2)}2-2j(j+1)\right)
\]
and the corresponding full sum at \(m=2j\), which is zero, give
\[
\|C_j^{T_2}\|_1=\frac{k_j^2[4j(j+1)-k_j^2+1]}{2(2j+1)j(j+1)}.
\]
Therefore \(\mathcal N(C_j)=(\|C_j^{T_2}\|_1-1)/2\), which is the stated closed formula.

Finally, a zero eigenvalue occurs exactly when \(L(L+1)=2j(j+1)\). Setting \(x=2L+1\) and \(y=2j+1\) turns this into
\[
x^2-2y^2=-1.
\]
Conversely every positive solution with \(j=(y-1)/2\ge1/2\) and \(L=(x-1)/2\le2j\) gives a zero sector. The nontrivial negative-Pell solutions begin \((x,y)=(7,5),(41,29),(239,169)\), yielding \(j=2,14,84\).

## Verification
The bundled `verify.py` independently constructs spin matrices, Kraus operators, normalized Choi matrices and partial transposes for \(j=1/2,1,3/2,2,5/2,3,7/2,4\), and compares their numerical spectra with the analytic sector formula. It also checks the closed negativity expression and searches the Pell singularity condition through \(j=500\). Its replay result is `VERIFY_OK spins=8 max_j=4 pell_first=2,14,84`. These finite checks are supplementary to the all-spin proof.

## Relationship to prior work
Alicki's arXiv:quant-ph/0402080 defines the same isotropic spin channel for general \(j\) and studies minimum output entropy, explicitly only solving the entropy problem for \(j=1/2\) and \(j=1\). Al Nuwairan's arXiv:1306.5321 develops Choi matrices of general irreducibly \(SU(2)\)-covariant EPOSIC channels as representation-theoretic projections, but the inspected full text does not state a partial-transpose or PPT spectrum. Filippov and Kuzhamuratova, arXiv:1803.02572, prove that the standard Landau--Streater channel is entanglement breaking exactly at \(j=1/2\), using an entanglement-annihilation argument for \(j\ge1\); that binary classification is prior and is not part of the novelty claim. Chang et al., arXiv:2105.00709, analyze PPT and entanglement breaking for low-dimensional irreducibly \(SU(2)\)-covariant families and include the qutrit Werner--Holevo/Landau--Streater special case, but explicitly restrict their qutrit-to-qutrit analysis to \(j=1\). Their arXiv record lists primary MSC 81P45. Karimipour, arXiv:2402.07700, explicitly distinguishes the standard high-spin \(SO(3)\) Landau--Streater channel from a different \(SO(d)\) generalization; the latter does not dominate the present all-spin \(SO(3)\) statement.

The spin-one specialization of the spectrum is already covered by the known qutrit Werner--Holevo formula, so the contribution is not the \(j=1\) case. The new content is the uniform all-spin sector formula, its exact closed negativity consequence, and the arithmetic characterization of exactly singular partial transposes.

## Limitations
The result concerns the normalized Choi state of this specific isotropic spin channel. It does not determine distillable entanglement, entanglement cost, or quantum capacity. Negativity is only one entanglement monotone, and the Pell singularities identify zero eigenvalues of the partial transpose rather than phase transitions of channel capacity. General \(SU(2)\) recoupling literature may encode equivalent spectral information in a different basis; focused searches and inspection of the most directly relevant channel papers did not locate this exact spectrum or the Pell characterization, but this remains the main residual originality risk.

## References
1. R. Alicki, *Isotropic quantum spin channels and additivity questions*, arXiv:quant-ph/0402080, first submitted 2004-02-12.
2. M. Al Nuwairan, *SU(2)-Irreducibly covariant and EPOSIC channels*, arXiv:1306.5321.
3. S. N. Filippov and K. V. Kuzhamuratova, *Quantum informational properties of the Landau--Streater channel*, arXiv:1803.02572.
4. E. Chang, J. Kim, H. Kwak, H. H. Lee, and S.-G. Youn, *Irreducibly SU(2)-covariant quantum channels of low rank*, arXiv:2105.00709; primary MSC 81P45.
5. V. Karimipour, *The noisy Landau--Streater (Werner--Holevo) channel in arbitrary dimensions*, arXiv:2402.07700.
