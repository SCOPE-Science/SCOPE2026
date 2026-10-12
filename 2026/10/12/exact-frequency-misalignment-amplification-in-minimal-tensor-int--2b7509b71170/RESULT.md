# Exact frequency-misalignment amplification in minimal tensor interpolation

## Finding

In the smallest setting with a nontrivial frequency-coupling choice, rank-one common-index tensor adaptive randomized pivoting (T-ARP) followed by tensor discrete empirical interpolation (t-DEIM) has the **sharp** expected squared-error amplification

\[
K(t_1,t_2)=\max_{\ell=1,2}\left\{\frac{q}{t_\ell}+\frac{1-q}{1-t_\ell}\right\},\qquad q=\frac{t_1+t_2}{2}.
\]

Here the baseline is the squared error of the orthogonal t-product projection onto the prescribed tensor basis, and the maximum is taken over all targets with nonzero baseline error. For targets with equal squared residual energy at the two Fourier frequencies the ratio is exactly

\[
B(t_1,t_2)=2+\frac{(t_1-t_2)^2}{4}\left(\frac1{t_1t_2}+\frac1{(1-t_1)(1-t_2)}\right).
\]

Consequently \(K\ge B\ge2\), and the final equality occurs if and only if \(t_1=t_2\). In the anti-aligned family \(t_1=t\), \(t_2=1-t\), \(0<t\le1/2\), every nonzero residual target realizes

\[
K=B=\frac{1}{2t(1-t)},\quad \eta=\frac{1}{2t},\quad
\frac{K}{1+\eta}=\frac{1}{(1-t)(1+2t)}\longrightarrow1\quad(t\downarrow0).
\]

Thus the known \(1+\eta\) frequency-alignment guarantee for rank-one T-ARP is **asymptotically sharp even with no singular sampled tube**; unrestricted shared-index amplification is unbounded. Independent frequency-by-frequency leverage sampling instead gives factor exactly two for all targets with nonzero baseline error.

## Assumptions and scope

Use the real third-order t-product, with two coordinates, one basis column, and two third-mode entries: \(\mathcal V,\mathcal F\in\mathbb R^{2\times1\times2}\). The length-two Fourier transform is the sum/difference transformation; Parseval has factor \(1/2\). At Fourier frequency \(\ell\in\{1,2\}\), prescribe

\[
v_\ell=(\sqrt{t_\ell},\sqrt{1-t_\ell})^\mathsf T,\qquad
w_\ell=(-\sqrt{1-t_\ell},\sqrt{t_\ell})^\mathsf T,
\qquad 0<t_\ell<1.
\]

The physical real arrays are obtained by inverse two-point Fourier transform, so the construction is a genuine real t-product tensor, and \(\mathcal V^\mathsf T*\mathcal V\) is the tubal identity. Write the arbitrary real target as \(f_\ell=\alpha_\ell v_\ell+\beta_\ell w_\ell\) in the Fourier domain, where \(\alpha_\ell,\beta_\ell\in\mathbb R\), and assume \(\beta_1^2+\beta_2^2>0\). There is one T-ARP pivot, \(J\in\{1,2\}\), with probabilities \(\Pr(J=1)=q=(t_1+t_2)/2\) and \(\Pr(J=2)=1-q\); one common index is used at both frequencies. The interpolant is precisely

\[
\mathcal I_J\mathcal F=\mathcal V * (\mathcal E_J^\mathsf T*\mathcal V)^{-1}*\mathcal E_J^\mathsf T*\mathcal F.
\]

All sampled scalar Fourier basis entries are strictly positive, so both possible sample tubes are invertible. The expectation concerns this one randomized pivot, not numerical rounding or random targets.

## Proof

At frequency \(\ell\), orthogonality of \(v_\ell,w_\ell\) removes the in-basis component \(\alpha_\ell v_\ell\) from the interpolation residual. If coordinate one is selected, the remaining residual is

\[
\beta_\ell\left(w_\ell-\frac{(w_\ell)_1}{(v_\ell)_1}v_\ell\right),
\]

whose squared Euclidean norm, by the Pythagorean theorem, is \(\beta_\ell^2/t_\ell\). If coordinate two is selected, the corresponding squared norm is \(\beta_\ell^2/(1-t_\ell)\). Parseval therefore gives the exact equalities

\[
E_0:=\|\mathcal F-\mathcal V*\mathcal V^\mathsf T*\mathcal F\|_F^2
=\tfrac12(\beta_1^2+\beta_2^2),
\]

\[
\mathbb E\|\mathcal F-\mathcal I_J\mathcal F\|_F^2
=\frac12\sum_{\ell=1}^2\beta_\ell^2m_\ell,
\qquad m_\ell=\frac q{t_\ell}+\frac{1-q}{1-t_\ell}.
\]

Thus the error ratio is the convex combination \((\beta_1^2m_1+\beta_2^2m_2)/(\beta_1^2+\beta_2^2)\). Its exact supremum equals the larger of the two coefficients, attained by taking nonzero orthogonal residual at just that frequency. Equal nonzero squared residual energies give the arithmetic average \(B=(m_1+m_2)/2\). Direct simplification yields

\[
B-2=\frac{(t_1-t_2)^2}{4}\left(\frac1{t_1t_2}+\frac1{(1-t_1)(1-t_2)}\right),
\]

which is strictly positive exactly when the two frequency-leverage parameters differ. Under \(t_1=t\), \(t_2=1-t\), the sampling distribution is uniform, and both coefficients are \(1/(2t(1-t))\). The smallest frequency-alignment constant of Akdodshoev–Leplat–Ahmadi-Asl's Assumption 4.8 is \(\eta=\max_{j,\ell}q_j/p_j^{(\ell)}=1/(2t)\) for \(t\le1/2\). The displayed sharpness ratio follows by division and tends to one. The same basis with independently sampled coordinates at the two frequencies gives, at each frequency, squared-error coefficient \(t_\ell/t_\ell+(1-t_\ell)/(1-t_\ell)=2\); averaging by Parseval leaves factor two. All claims are exact for the stated open parameter domain; the excluded zero-leverage endpoints are not used.

## Verification

The included `verify.py` uses only the Python standard library. It checks 3,500 seeded exact-rational parameter pairs and residual mixtures; verifies the closed-form balance identity, alignment upper bound, and strict equality cases; reconstructs genuine real two-point inverse Fourier tensors using rational orthonormal vectors; and directly recomputes physical-domain interpolation energies for 300 exact-rational targets including arbitrary in-span components. It also checks the anti-aligned sharpness identities at several rational parameter values. Run `python3 verify.py`. These computations cross-check the finite algebra; the proof above establishes the unrestricted parameter statements.

## Relationship to prior work

Akdodshoev, Leplat, and Ahmadi-Asl [1] define common-index T-ARP and establish in Theorem 4.9 and Corollary 4.14 the expected rank-one t-DEIM squared-error bound \(1+\eta\) under frequency alignment. Their fully enumerated example demonstrates sharpness at perfect alignment, while the reported mildly misaligned example is less tight than the bound. The formulas here supply a **complete sharp minimal-frequency interpolation factor**, an explicit strict alignment defect, and a severely misaligned real family showing that the published \(1+\eta\) factor cannot generally be improved asymptotically. Their one-step projector identity underlies the calculation and is credited; this is not a claim to have invented T-ARP or the alignment condition.

Chellappa, Feng, and Benner [2] prove deterministic t-Q-DEIM interpolation error bounds in terms of inverse sampled-basis conditioning, not the common-index stochastic minimax quantity. Cortinovis and Kressner [3] and Epperly [4] analyze matrix adaptive randomized pivoting and its volume-sampling interpretation; these give the individual-frequency factor two, but without coupling the random sample across distinct Fourier bases.

## Limitations

The exact minimax classification is for rank-one real tensors with two coordinates and two frequencies, and its failure mode concerns **expected squared interpolatory error**, not a claim about tensor CUR approximation by orthogonal projection. No general higher-rank, multi-index, data-adaptive basis, or finite-precision extension is proved. Known inverse-basis conditioning can be large for either pivot, and published theory already records a frequency-alignment penalty; what is established here is the explicit sharp joint-frequency dependence and asymptotic necessity in this natural smallest setting. An unindexed mathematically equivalent leverage-mixture identity could exist; literature searching cannot certify novelty. Independent audit has not been performed.

## References

[1] A. Akdodshoev, V. Leplat, S. Ahmadi-Asl, *Adaptive Randomized Pivoting for Tensor Singular Value Decomposition Model*, arXiv:2606.26688, first public 2026-06-25, Algorithm 8, Assumption 4.8, Theorem 4.9, Corollary 4.14 and Section 5.

[2] S. Chellappa, L. Feng, P. Benner, *Discrete empirical interpolation in the tensor t-product framework*, arXiv:2410.14519, 2024, Section 3.

[3] A. Cortinovis, D. Kressner, *Adaptive randomized pivoting for column subset selection, DEIM, and low-rank approximation*, arXiv:2412.13992, 2024; SIAM J. Matrix Anal. Appl., 2026.

[4] E. N. Epperly, *Adaptive randomized pivoting and volume sampling*, arXiv:2510.02513, 2025, Theorems 3.2–3.3.
