# Isolated triad-triplet oscillations leak outside finite Fourier support

## Result

The time-dependent seven-mode "isolated triad triplet" solution in arXiv:2609.20710v1 is an exact solution of the seven-mode system written there as Eq. (42), but in general it is **not** an exact solution of the full inviscid Navier--Stokes (Euler) equation. The obstruction is nonlinear Fourier leakage: modes belonging to different legs of the isolated triplet form additional Euler triads that are absent from Eq. (42), and these generate modes outside the seven-mode set immediately.

For the paper's explicit example
\[
g=10/7,\qquad h=8/5,\qquad \sigma_g=\sigma_h=-1,\qquad k=s_k=1,\qquad A=0.1,
\]
choose the planar realization of Eq. (14)
\[
1+g^{-1}e^{-i\alpha}+he^{i\beta}=0,
\]
with
\[
\alpha=0.700863354157635,\qquad \beta=2.855574876316264.
\]
The seven wavevectors may be represented by
\[
\begin{aligned}
K&=1, &P&=g^{-1}e^{-i\alpha}, &Q&=he^{i\beta},\\
K_h&=h^{-1}e^{-i\beta}, &P_h&=(gh)^{-1}e^{-i(\alpha+\beta)},\\
K_g&=ge^{i\alpha}, &Q_g&=ghe^{i(\alpha+\beta)}.
\end{aligned}
\]
They contain the three intended triads
\[
K+P+Q=0,\qquad K+K_h+P_h=0,\qquad K+K_g+Q_g=0.
\]

Now take one mode from the middle triad and one from the large triad, namely \(P\) and \(Q_g\). They form the additional triad
\[
K_{\rm ext}+P+Q_g=0,
\qquad
K_{\rm ext}=-(P+Q_g),
\]
where
\[
K_{\rm ext}=1.556836734693878+1.372668410498753\,i,
\qquad
|K_{\rm ext}|=2.075562377687905.
\]
This wavevector is not one of the seven retained modes (nor its negative); its distance from the signed retained support is about \(0.64807407\).

The paper's helicities give
\[
s_P=-1,\qquad s_{Q_g}=+1.
\]
Using the paper's own helical interaction coefficient, Eq. (5), with \(K_{\rm ext}\) as the middle leg, the two possible output-helicity channels have
\[
Q_+=0.396114511389982,
\qquad
Q_-=0.052996797414140,
\]
and therefore interaction coefficients
\[
C_+=-1.182684755435803,
\qquad
C_-=-0.158233295136504.
\]
At \(t=0\), Eq. (43) gives
\[
\overline{u_P(0)}\,\overline{u_{Q_g}(0)}
=A^2h^{-1/3}=0.008549879733383.
\]
Hence the full Euler equation forces the absent mode immediately:
\[
\boxed{
\partial_t u^{+}_{K_{\rm ext}}(0)=-0.010111812421482\ne0,
\qquad
\partial_t u^{-}_{K_{\rm ext}}(0)=-0.001352875643234\ne0.
}
\]
After real-valued completion of the Fourier field, \((-P,-Q_g)\) is the unique retained unordered pair summing to \(K_{\rm ext}\), so this leakage cannot be cancelled by another retained pair.

Thus the seven-mode subspace is not invariant under the Euler quadratic nonlinearity. Eq. (42) is a finite triad-network truncation: solving it exactly does not by itself produce an exact solution of the full Euler PDE.

## Structural obstruction from known theory

Kishimoto and Yoneda proved a complete classification of real-valued three-dimensional Euler solutions supported on finitely many Fourier modes: every such solution is time-independent; the only possibilities are stationary two-dimensional-like flows and Beltrami flows (with the precise planar cases described in their theorem). Their theorem allows arbitrary real frequencies, not only lattice Fourier modes. Therefore any genuinely time-periodic, real-valued, finite-mode Euler field of the type asserted in arXiv:2609.20710v1 is already excluded by this classification.

The explicit leakage computation above is source-specific and stronger for diagnosis: it identifies a concrete missing interaction in the paper's displayed numerical example rather than relying only on the abstract classification theorem.

## Scope of the correction

This does **not** invalidate the exact solution of the reduced seven-mode ODE itself, nor the use of triad triplets as diagnostics or shell/network models. It corrects the stronger claim that the isolated seven-mode oscillation is an exact nonlinear solution of the full inviscid Navier--Stokes equation, and therefore also the suggestion that this finite-mode oscillation can directly serve as an exact-PDE benchmark.

The paper's infinite-chain/fractal constructions are logically separate. The present argument addresses the isolated finite triplet of Sec. IV.2 and its finite Fourier reconstruction in Eqs. (42)--(43), (51)--(52), and the finite Fourier reconstruction displayed immediately after Eq. (50).

## Reproducibility

`artifacts/verify_external_mode_leakage.py` reconstructs the source geometry, verifies the three intended affine triads, constructs the missing cross-triplet wavevector, checks uniqueness of its generating retained pair after real completion, and evaluates the paper's Eq. (5) interaction coefficient for both output helicities. `artifacts/verification_output.txt` records the resulting numerical values.

## References

1. Ö. D. Gürcan, L. Manfredini, P. Morel, *Solutions of the Navier-Stokes Equation Through Affine Transformations: The Triad Triplet*, arXiv:2609.20710v1 (2026). https://arxiv.org/abs/2609.20710
2. N. Kishimoto, T. Yoneda, *Characterization of three-dimensional Euler flows supported on finitely many Fourier modes*, arXiv:2110.08039; J. Evol. Equ. 22 (2022), DOI: 10.1007/s00021-022-00703-5. https://arxiv.org/abs/2110.08039
