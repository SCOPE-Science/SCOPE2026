# The smallest weak-reset quantum-walk absorption advantage occurs at detector separation eight

## Finding

For the centered discrete-time monitored quantum walk specified below, let \(M_L(r)\) be the mean number of steps until first detection at \(\pm L\), when a nondetected walker independently resets to its initial pure state with probability \(r\) after each failed step (no elapsed time charged to resetting). The complete exact table for the four smallest positive half-separations is

| \(L\) | \(\mathbb E T_L\) | \(\mathbb E T_L^2\) | \(\operatorname{Var}T_L\) | \(M_L'(0+)\) | classical \(M_{L,\mathrm{cl}}'(0+)\) |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 | 0 | 0 |
| 2 | 4 | 24 | 8 | 2 | 2 |
| 3 | 9 | 145 | 64 | 4 | 12 |
| 4 | 16 | 560 | 304 | -32 | 40 |

Consequently, detector half-separation \(L=4\), meaning detector separation eight lattice spacings, is the **smallest** size in this family for which every sufficiently small positive reset probability decreases the quantum mean first-detection time. At \(L=2,3\) every sufficiently small reset increases the mean, and at \(L=1\) the mean remains identically one. The classical comparison at \(L=4\) has strictly increasing mean for small reset rates.

## Assumptions and scope

Use positions \(x\in\mathbb Z\) and coin states \(+\) and \(-\). The coin and conditional shift are
\[
C=\frac1{\sqrt2}\begin{pmatrix}1&-1\\1&1\end{pmatrix},\qquad
S|x,\pm\rangle=|x\pm1,\pm\rangle,\qquad U=SC.
\]
One unit of time consists of applying \(U\), then measuring the two absorbing sites \(\pm L\) (both coin values). On a nondetection, delete the boundary amplitudes; before the next unit-time step, independently replace the conditional pure state by \(|0,+\rangle\) with probability \(r\), otherwise retain it. The measurement and reset are ideal, and all initial trials begin in \(|0,+\rangle\). The first-passage variable \(T_L\) refers to no resetting. We claim the exact four-size classification for \(L\in\{1,2,3,4\}\), and strict local consequences for sufficiently small \(r\ge0\). No conclusion about global resetting optimum is asserted.

## Proof

**Finite quantum survival channel.** Let \(\mathcal H_L\) be the span of \(|x,c\rangle\) with \(-L<x<L\). Denote by \(K_L=P_L U|_{\mathcal H_L}\) the interior compression of the one-step walk, and let \(\Phi_L(\rho)=K_L\rho K_L^\dagger\), with \(\rho_0=|0,+\rangle\langle0,+|\). The survival probability after \(t\) steps is \(s_t=\operatorname{Tr}\Phi_L^t(\rho_0)\). The finite survival operators calculated below give finite resolvents; because \(s_t\) decreases and the positive invariant sector contains no nonzero fixed point, \(s_t\to0\). Hence the tail-sum identities yield
\[
\mu_L=\mathbb E T_L=\operatorname{Tr}(I-\Phi_L)^{-1}\rho_0,\qquad
\nu_L=\mathbb E T_L^2=2\operatorname{Tr}(I-\Phi_L)^{-2}\rho_0-\mu_L.
\]
Here the inverse is on the parity-supported, real-symmetric density-matrix sector reached from \(\rho_0\). To see absorption is almost sure on this sector, a positive residual limiting survival density would be a nonzero fixed point of \(\Phi_L\), contradicting the certified invertibility of \(I-\Phi_L\) there.

**Exact finite certificates.** Write \(K_L=B_L/\sqrt2\). In the ordered basis \((x,c)\), the only nonzero entries of the integer matrix \(B_L\) are \(B_{(x+1,+),(x,+)}=1\), \(B_{(x-1,-),(x,+)}=1\), \(B_{(x+1,+),(x,-)}=-1\), and \(B_{(x-1,-),(x,-)}=1\), when source and target are interior. In the real symmetric matrix-unit basis \(E_{ij}+E_{ji}\) for \(i<j\) and \(E_{ii}\), retain only pairs of sites having the same position parity. The induced rational channel matrix \(A_L\) represents \(X\mapsto B_L X B_L^{\mathsf T}/2\). Its dimensions for \(L=1,2,3,4\) are exactly \(3,13,31,57\). With \(F_L=I-A_L\) and the coordinate vector \(e_L\) of \(\rho_0\), solve exactly
\[
F_Lv_L=e_L,\qquad F_Lw_L=v_L.
\]
For each of these four systems, the accompanying standalone program assembles every rational coefficient from the displayed formula, solves the systems using rational algebra, verifies both residuals *exactly*, and evaluates traces only from the diagonal matrix units. The resulting pairs \((\mu_L,\nu_L)\) are \((1,1),(4,24),(9,145),(16,560)\), giving variances \(0,8,64,304\). This finite algebra is exhaustive for the stated four sizes, rather than a floating-point experiment or an induction over all sizes.

**Restart renewal identity.** Let \(f_L(q)=\mathbb E[q^{T_L}]\), and let \(q=1-r\). A single attempt can end by successful detection after \(t\) steps with probability \(\Pr(T_L=t)q^{t-1}\), or reset following a failed detection. Its success probability is \(f_L(q)/q\), while the expected duration of one attempt is \([1-f_L(q)]/r\). Therefore the restarted mean is exactly
\[
M_L(r)=\frac{(1-r)[1-f_L(1-r)]}{r f_L(1-r)},\qquad r>0.
\]
Since the four finite channels have all moments finite, expansion at \(r=0\) gives
\[
M_L'(0+)=\frac{\mu_L^2-\mu_L-\operatorname{Var}(T_L)}2.
\]
Substitution yields derivatives \(0,2,4,-32\), proving the sharp weak-reset onset and the local strict signs. The value at \(L=1\) stays one because detection occurs after exactly one step, before any possible effective reset.

**Classical contrast.** The centered simple symmetric random walk on the same absorbing interval has first two exit-time moments \(\mu_{L,\mathrm{cl}}=L^2\) and \(\nu_{L,\mathrm{cl}}=(5L^4-2L^2)/3\), obtained by the first- and second-moment discrete Dirichlet recurrences. Its weak-reset derivative is \(L^2(L^2-1)/6\), hence \(40\) at \(L=4\). Independent rational finite matrices for the classical channel and both resolvent identities are also constructed by the accompanying verification program for every \(L\le4\).

## Verification

Run `python verify_variance.py` using SymPy. No network access or external data is needed. The program assembles the finite survival channel from the coin and shift, verifies both inverse-residual identities with exact rational arithmetic, checks the four rows and independently solves the classical Dirichlet systems. In addition, direct forward propagation for the quantum state was checked numerically through survival tails; these numerical checks support but do not replace the rational proof. The finite certificate is specifically for \(L=1,2,3,4\).

## Relationship to prior work

Wójcik [1], building on Chełminiak–Wójcik–Wójcik [2], develops the identical coined walk and an equivalent reset-before-next-step protocol, proves the mean first-detection time coincides with its classical counterpart without resetting, and supplies a full rational restarted mean at detector half-separation five (Appendix B). The quantum first-moment identity and general existence of resetting advantage are **not** claimed here. This result isolates the smallest width for the onset of improvement at infinitesimal reset strength by exact second-moment comparison, which is not stated by [1]. General finite-dimensional moment-resolvent methodology for absorbing quantum channels was also studied in [3]; the method itself is not asserted to be new.

## Limitations

The theorem classifies the derivative at zero reset probability, not whether large reset probabilities can improve a smaller-width walk. The results assume a fixed coin and localized coin preparation, symmetric perfectly absorbing detectors, ideal projective monitoring, and memoryless resetting after each nondetection. Only the four smallest positive integer half-separations are exhaustively certified; no all-width closed formula or different-coin statement is claimed. The full text of [3] and of [2] was not accessible in the comparison, leaving a specific priority risk for specialized small-width tables. Independent scientific validation remains outstanding.

## References

[1] J. Wójcik, *Revisiting quantum walk advantages: A mean hitting time perspective*, arXiv:2510.27377 (first posted October 31, 2025), https://arxiv.org/abs/2510.27377; published as *Re-examining quantum walk advantages*, Phys. Rev. E 113, 024135 (2026).

[2] P. Chełminiak, J. Wójcik and A. Wójcik, *Discrete-time walk on one-dimensional lattice under stochastic resetting: Advantage of quantum over classical scenario*, Phys. Rev. E 111, 044143 (2025), https://doi.org/10.1103/PhysRevE.111.044143.

[3] L. K. Moori and C. F. Lardizabal, *Mean and variance for the visit time of absorbing quantum walks and channels*, Int. J. Quantum Inf. 24, 2650005 (2026), https://doi.org/10.1142/S021974992650005X.
