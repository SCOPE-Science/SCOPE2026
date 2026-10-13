# Sharp dimension-parity law for Hilbert–Schmidt coherence concentration

## Finding
Let \(d\ge2\) be an integer and let \(\Phi:M_d(\mathbb C)\to M_2(\mathbb C)\) be any completely positive trace-preserving (CPTP) map sending every diagonal density matrix to a diagonal density matrix, in the fixed input and output computational bases. Write \(\Delta\) for complete dephasing and \(C_2(\rho)=\|\rho-\Delta(\rho)\|_2\), where \(\|\cdot\|_2\) is the Hilbert–Schmidt norm. Then, for every input state \(\rho\),
\[
 C_2(\Phi(\rho))\le\sqrt{\lfloor d/2\rfloor}\, C_2(\rho).
\]
The constant is best possible **in every dimension**. In fact it is attained with a strictly incoherent channel and a full-rank input state. Equivalently, the supremum of the output-to-input coherence ratio over coherent states and all maximally incoherent \(d\)-to-qubit channels is exactly \(\sqrt{\lfloor d/2\rfloor}\). In particular, the sharp constant is \(1\) for dimensions \(2\) and \(3\), but exceeds \(1\) from dimension \(4\) onward, and is unbounded as \(d\to\infty\).

## Assumptions and scope
The input and output Hilbert spaces are \(\mathbb C^d\) and \(\mathbb C^2\), respectively. All states are positive semidefinite matrices of trace one. A maximally incoherent operation (MIO) means a CPTP map preserving the respective sets of diagonal density matrices. Strictly incoherent operations (SIO) admit Kraus operators for which both each operator and its adjoint map incoherent basis states to (possibly unnormalized) incoherent basis states. No postselection or condition on the Kraus rank is assumed in the upper bound. The ratio is taken only when \(C_2(\rho)>0\). The result concerns exactly the Hilbert–Schmidt norm of the off-diagonal part, not its square, the entrywise \(\ell_1\) norm, or a distance minimized over general diagonal states under another metric.

## Proof
**Spectral lemma.** If \(H\in M_d(\mathbb C)\) is Hermitian, \(\operatorname{Tr}H=0\), and \(-I\le H\le I\), then
\[
 \operatorname{Tr}H^2\le 2\lfloor d/2\rfloor.
\]
Indeed, the eigenvalues \(\lambda_j\) lie in \([-1,1]\) and sum to zero. Maximizing the convex function \(\sum_j\lambda_j^2\) over the polytope \(\{\lambda\in[-1,1]^d:\sum\lambda_j=0\}\) can be done at a vertex. At each vertex, at least \(d-1\) entries are \(\pm1\). If \(d=2m\), the remaining entry must also be \(\pm1\) and there are \(m\) of each sign. If \(d=2m+1\), the remaining entry is \(0\), with \(m\) entries of each sign. This proves the bound.

Now take the equatorial qubit observable \(\sigma_\theta=e^{-i\theta}|0\rangle\langle1|+e^{i\theta}|1\rangle\langle0|\). It has spectrum \(\{-1,+1\}\). Since \(\Phi\) preserves diagonal input states, the Heisenberg operator \(H_\theta=\Phi^*(\sigma_\theta)\) has zero diagonal, and hence trace zero. Since \(\Phi^*\) is unital and positive, \(-I\le H_\theta\le I\). Put \(X=\rho-\Delta_d(\rho)\), so that \(\|X\|_2=C_2(\rho)\). The diagonal state \(\Phi(\Delta_d(\rho))\) contributes nothing to \(\operatorname{Tr}[\sigma_\theta\Phi(\rho)]\). Hence the Hilbert–Schmidt Cauchy–Schwarz inequality and the spectral lemma yield
\[
 \begin{aligned}
 C_2(\Phi(\rho))
 &=\frac1{\sqrt2}\max_{\theta\in[0,2\pi)}
     \operatorname{Tr}[\sigma_\theta\Phi(\rho)]\\
 &=\frac1{\sqrt2}\max_\theta\operatorname{Tr}[H_\theta X]\\
 &\le\frac{\sqrt{2\lfloor d/2\rfloor}}{\sqrt2}\,\|X\|_2
 =\sqrt{\lfloor d/2\rfloor}\,C_2(\rho).
 \end{aligned}
\]
Here the first identity follows by writing the qubit's off-diagonal entry as \(z\): its coherence is \(\sqrt2|z|\), whereas the maximum expectation of \(\sigma_\theta\) is \(2|z|\).

**Attainment.** Put \(m=\lfloor d/2\rfloor\). For \(0\le j<m\), define a \(2\times d\) Kraus matrix
\[
 K_j=|0\rangle\langle2j|+|1\rangle\langle2j+1|.
\]
If \(d=2m+1\), add \(K_*=|0\rangle\langle2m|\). Then \(\sum K_j^*K_j=I_d\), including \(K_*\) when present. Each Kraus operator has at most one nonzero entry in each row and each column, so this is SIO, and therefore also MIO. Define
\[
 Z=\sum_{j=0}^{m-1}(|2j\rangle\langle2j+1|+|2j+1\rangle\langle2j|),\qquad
 \rho_\varepsilon=d^{-1}I_d+\varepsilon Z,
\]
with \(0<\varepsilon<1/d\). The eigenvalues are \(d^{-1}\pm\varepsilon\) in each two-dimensional block, plus \(d^{-1}\) for the singleton if \(d\) is odd; the input state is thus strictly positive. The output off-diagonal entry is \(m\varepsilon\). Consequently,
\[
 C_2(\rho_\varepsilon)=\varepsilon\sqrt{2m},\qquad
 C_2(\Phi(\rho_\varepsilon))=\sqrt2\,m\varepsilon,
\]
whose ratio equals \(\sqrt m\). This proves sharpness and the parity statement. \(\square\)

## Verification
The standalone `verify.py` checks the CPTP Kraus normalization, diagonal-state preservation, strict incoherence of individual Kraus matrices, full-rank input states, and equality of the two sides for every integer dimension from \(2\) through \(12\). It also exhaustively enumerates the eigenvalue-polytope vertices in those dimensions. Its successful execution prints `VERIFY_OK dimensions=11 exact_spectral_vertices=passed Kraus_completeness=passed full_rank_saturation=passed incoherent_marginals=passed`. Those computations only corroborate the argument: the vertex proof and dual-norm inequality establish the claims for all \(d\), without relying on a finite computation.

## Relationship to prior work
Cheng and Hall introduced the Hilbert–Schmidt off-diagonal norm as a candidate coherence monotone in arXiv:1508.03240, Sec. II C. Rana, Parashar and Lewenstein (arXiv:1511.01854, Sec. IV, Proposition 9) subsequently established nonmonotonicity of \(\ell_p\)- and Schatten-norm coherence; in particular their product-with-maximally-mixed-ancilla erasure produces the same **lower-bound mechanism** as the present even-dimensional construction. Thus the nonmonotonicity and the amplification examples are not claimed as new. The point proved here is a globally optimal, dimension-dependent **upper** bound for every MIO channel to a qubit, together with the exact odd/even dimension threshold and full-rank attainment by SIO. The known counterexample does not itself imply this global upper bound or the odd-dimensional optimal constant.

## Limitations
The result treats output dimension exactly two; no optimal constant for higher output dimensions is claimed. It establishes a sharp worst-case ratio, not a bound on the absolute amount of operationally useful coherence. The measure \(C_2\) is already known not to be a resource monotone in arbitrary dimensions. Priority relative to possible equivalent operator-norm results or unpublished formulations is not independently certified. The full text of Song and Tao's 2020 study was not obtained; its accessible abstract and first-page preview discuss coherence formulas and nonmonotonicity, but do not resolve the present exact optimization. The general proof does not require those sources as premises.

## References
1. S. Cheng and M. J. W. Hall, *Complementarity relations for quantum coherence*, arXiv:1508.03240 (first posted 2015-08-13), Sec. II C. https://arxiv.org/abs/1508.03240
2. S. Rana, P. Parashar and M. Lewenstein, *Trace-distance measure of coherence*, arXiv:1511.01854 (first posted 2015-11-05), Sec. IV, especially Proposition 9. https://arxiv.org/abs/1511.01854
3. E. Chitambar and G. Gour, *Critical Examination of Incoherent Operations and a Physically Consistent Resource Theory of Quantum Coherence*, arXiv:1602.06969 (2016), for the hierarchy of incoherent-operation classes. https://arxiv.org/abs/1602.06969
4. Y.-y. Song and Y.-h. Tao, *Notes on l2 Norm of Coherence*, International Journal of Theoretical Physics 59 (2020), 851–860, doi:10.1007/s10773-019-04371-6 (abstract and first-page preview examined only).
