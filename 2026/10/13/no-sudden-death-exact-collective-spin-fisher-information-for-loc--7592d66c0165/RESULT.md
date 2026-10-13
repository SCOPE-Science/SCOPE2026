# No sudden death: exact collective-spin Fisher information for locally decohered W states

## Finding
For every integer \(N\ge2\) and channel strength \(0\le p\le1\), the largest quantum Fisher information for a collective spin rotation *after* independent phase damping or amplitude damping of the pure one-excitation state \(|W_N\rangle\) is, respectively,
\[
F_{\mathrm{PD}}(N,p)=N+2(N-1)(1-p)^2,
\qquad F_{\mathrm{AD}}(N,p)=N(1-2p)^2+2(N-1)(1-p).
\]
Here \(F\) is **total** Fisher information, and \(F/N\) is the per-qubit convention. Every transverse spin axis is optimal; the longitudinal Fisher information is zero. Both functions are continuous through \(p=0\). Contrary to the zero-Fisher-information prediction in equations (9) and (11) of the motivating 2014 paper, neither channel has Fisher-information sudden death: phase damping retains the strictly super-shot-noise value \(F>N\) whenever \(p<1\), while amplitude damping has \(F>0\) throughout the closed channel-strength interval.

For amplitude damping, quantum enhancement \(F>N\) holds exactly for \(0\le p<(N-1)/(2N)\); equality also occurs at \(p=1\). Its unique global minimum is at \(p=(3N-1)/(4N)\), with value \((3N+1)(N-1)/(4N)>0\).

## Assumptions and scope
Fix \(N\ge2\) and \(p\in[0,1]\), and use the qubit basis \(|0\rangle,|1\rangle\). Write \(|\Omega\rangle=|0\rangle^{\otimes N}\), and let \(|e_j\rangle\) have an excitation at site \(j\) only. Put \(|W_N\rangle=N^{-1/2}\sum_{j=1}^N|e_j\rangle\). The phase-damping channel has one-qubit Kraus operators \(\sqrt{1-p}I\), \(\sqrt p|0\rangle\langle0|\), and \(\sqrt p|1\rangle\langle1|\); the amplitude-damping channel has \(|0\rangle\langle0|+\sqrt{1-p}|1\rangle\langle1|\) and \(\sqrt p|0\rangle\langle1|\). Apply the chosen channel independently to all sites, then encode an angle by \(\rho_\theta=e^{-i\theta J_{\boldsymbol u}}\rho e^{i\theta J_{\boldsymbol u}}\), with \(J_{\boldsymbol u}=\frac12\sum_{j=1}^N\boldsymbol u\cdot\boldsymbol\sigma^{(j)}\) and \(\|\boldsymbol u\|=1\). The quantum Fisher information is the symmetric-logarithmic-derivative Fisher information of this family, maximized over \(\boldsymbol u\). It is **not** Fisher information for estimating the noise strength \(p\), nor for rotating the input before noise.

## Proof
Let \(P_1=\sum_j|e_j\rangle\langle e_j|\). Direct Kraus multiplication gives the exact output states
\[
\rho_{\mathrm{PD}}=q|W_N\rangle\langle W_N|+(1-q)P_1/N,\qquad q=(1-p)^2,
\]
\[
\rho_{\mathrm{AD}}=(1-p)|W_N\rangle\langle W_N|+p|\Omega\rangle\langle\Omega|.
\]
Use the spectral formula \(F(\rho,J)=2\sum_{i,j:\lambda_i+\lambda_j>0}(\lambda_i-\lambda_j)^2|\langle i|J|j\rangle|^2/(\lambda_i+\lambda_j)\), where eigenvectors with zero eigenvalue are **included**. Omitting support-to-kernel transitions discards a positive, generally dominant contribution.

For phase damping, every positive-eigenvalue vector lies in the single-excitation sector. The operator \(J_x=\frac12\sum_j\sigma_x^{(j)}\) sends this sector to the zero- or two-excitation sectors. Consequently all matrix elements of \(J_x\) within the support vanish, so the complete spectral formula collapses to \(F(\rho_{\mathrm{PD}},J_x)=4\operatorname{tr}(\rho_{\mathrm{PD}}J_x^2)\). Expanding \(4J_x^2=NI+2\sum_{i<j}\sigma_x^{(i)}\sigma_x^{(j)}\) yields \(4\langle W_N|J_x^2|W_N\rangle=3N-2\) and \(4\operatorname{tr}(P_1J_x^2/N)=N\). Linearity gives \(F_{\mathrm{PD}}=N+2(N-1)q\).

For amplitude damping, the nonzero spectral weights are \(p\) on \(|\Omega\rangle\) and \(1-p\) on \(|W_N\rangle\) (zero weights at the endpoints are permitted). The generator obeys
\[
J_x|\Omega\rangle=\frac{\sqrt N}{2}|W_N\rangle,\qquad
J_x|W_N\rangle=\frac{\sqrt N}{2}|\Omega\rangle+\sqrt{\frac{N-1}{2}}|D_N^{(2)}\rangle,
\]
where \(|D_N^{(2)}\rangle\) is the normalized uniform two-excitation Dicke vector. The only active spectral transitions are between vacuum and \(W\), carrying weight \((p-(1-p))^2/(p+1-p)\), and from \(W\) to the zero-weight two-excitation sector, carrying weight \(1-p\). The spectral formula therefore yields exactly \(N(1-2p)^2+2(N-1)(1-p)\), including \(p=0\) and \(p=1\).

Both density operators are invariant under rotations about the \(z\)-axis, and commute with \(J_z\). Thus \(F(\rho,J_z)=0\); covariance under axial rotations forces equal transverse diagonal metric entries and no transverse mixing. Every transverse direction realizes the displayed global maximum. Finally, \(F_{\mathrm{AD}}-N=2(1-p)(N-1-2Np)\), and completing the square gives the minimum and shot-noise threshold stated above. These steps prove the theorem for the full infinite family, not merely small instances.

## Verification
Run `python3 artifacts/verify.py` after installing NumPy from `requirements.txt`. The verifier builds the full \(2^N\)-dimensional matrices, diagonalizes the density operators including their zero eigenvalues, computes Fisher information for all three spin axes, and compares every value with both closed forms for \(2\le N\le6\) and nine values of \(p\), including both endpoints. It separately constructs direct tensor-product Kraus maps for \(2\le N\le4\) and five strengths to check the state reduction. Expected terminal message: `VERIFY_OK full_spectrum_axis_cases=270 Kraus_outputs=30 N=2..6 p=9 both_channels`. These finite tests corroborate, and do not replace, the analytic argument.

## Relationship to prior work
Özaydın's arXiv:1403.2376v1 (2014), equations (9) and (11), analyzes precisely these independent local channels and rotation generators for \(N=3\), but reports discontinuous zero/near-zero Fisher information. The expressions here instead give, for \(N=3\), \(F_{\mathrm{PD}}/3=1+4(1-p)^2/3\) and \(F_{\mathrm{AD}}/3=(1-2p)^2+4(1-p)/3\). In particular, at \(p=1/2\) their positive values are \(4/3\) and \(2/3\). The likely algebraic cause of the earlier discrepancy is omission of the spectral transitions to zero-eigenvalue sectors, rather than a discontinuity of the physical state.

Liu, Jing, Zhong and Wang (arXiv:1312.6910v1) and Liu, Xiong, Song and Wang (arXiv:1401.3154v1) independently develop general rank-deficient Fisher-information methods, including exactly the support-to-kernel terms used here, but do not evaluate the present two noisy \(W_N\) families. Özaydın, Altıntaş, Yeşilyurt, Bugu and Erol (2015) compare a genuine three-qubit W state to a reduced W-like state in these channels, primarily through plotted values; no all-size correct closed expressions are given. Erol (arXiv:1704.07367) plots noisy three-qubit W/GHZ superpositions and may implicitly contain the pure-W endpoint, but does not state the present full-parameter infinite family. Zhao, Zhang and Yang (2018) analyze spin Fisher information for three- and five-qubit \(W\)/GHZ **superpositions** in the same noise channels and report nonzero phase-damping robustness. That is significant conceptual antecedence and may contain low-dimensional special cases; the explicit all-\(N\) closed forms, exact amplitude minimum, and direct comparison to the published discontinuities remain the particular claim assessed here.

## Limitations
This is a correction of a specific metrological observable, not a claim about phase estimation under every possible encoding, estimation of the channel parameter, or all definitions of noisy metrological advantage. It does not treat depolarization, correlated noise, arbitrary input states, or channel noise following phase encoding. Mathematical validity follows from the stated Kraus and generator conventions; the suggested diagnosis of the prior paper's algebra is an interpretation, not a reconstruction of its unpublished calculations. An unlocated broader exact formula or a full special-case formula in later literature may reduce publication novelty; independent literature-priority assessment is outstanding.

## References
1. F. Özaydın, *Quantum Fisher Information of W States in Decoherence Channels*, arXiv:1403.2376v1 (10 March 2014); published as *Phase damping destroys quantum Fisher information of W states*, Physics Letters A 378 (2014), 3161–3164, DOI: 10.1016/j.physleta.2014.08.035. https://arxiv.org/pdf/1403.2376
2. J. Liu, X. Jing, W. Zhong and X. Wang, *Quantum Fisher information for density matrices with arbitrary ranks*, arXiv:1312.6910v1 (2013). https://arxiv.org/pdf/1312.6910
3. J. Liu, H.-N. Xiong, F. Song and X. Wang, *Fidelity susceptibility and quantum Fisher information for density operators with arbitrary ranks*, arXiv:1401.3154v1 (2014). https://arxiv.org/pdf/1401.3154
4. F. Özaydın, A. A. Altıntaş, C. Yeşilyurt, S. Bugu and V. Erol, *Quantum Fisher Information of Bipartitions of W States*, Acta Physica Polonica A 127 (2015), 1233–1235, DOI: 10.12693/APhysPolA.127.1233. https://www.researchgate.net/publication/281190019_Quantum_Fisher_Information_of_Bipartitions_of_W_States
5. V. Erol, *Quantum Fisher Information of W and GHZ State Superposition Under Decoherence*, arXiv:1704.07367 (2017). https://arxiv.org/pdf/1704.07367
6. J.-L. Zhao, Y.-D. Zhang and M. Yang, *Influence of noise on tripartite quantum probe state*, Acta Physica Sinica 67 (2018), 140302, DOI: 10.7498/aps.67.20180040. https://wulixb.iphy.ac.cn/cn/article/pdf/preview/10.7498/aps.67.20180040.pdf
