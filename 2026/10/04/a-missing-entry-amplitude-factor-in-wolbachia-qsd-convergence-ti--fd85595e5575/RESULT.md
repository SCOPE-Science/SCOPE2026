# A missing entry-amplitude factor in Wolbachia QSD convergence times
## Finding
For the perfect-transmission household Wolbachia continuous-time Markov chain, write the transient generator in the source's class order as
\[
Q=\begin{pmatrix}Q_1&0&0\\0&Q_2&0\\Q_{31}&Q_{32}&Q_3\end{pmatrix},
\]
where \(\mathcal S_1\) is wildtype-only, \(\mathcal S_2\) is Wolbachia-only, and \(\mathcal S_3\) is mixed. Assume a mixed initial row distribution \(p_3\), simple Perron decay rates \(0<\alpha_1<\alpha_2<\alpha_3\), and left/right Perron vectors satisfying \(\ell_kQ_k=-\alpha_k\ell_k\), \(Q_ku_k=-\alpha_ku_k\), and \(\ell_ku_k=1\). Then the class masses satisfy
\[
M_k(t)=A_k e^{-\alpha_k t}+o(e^{-\alpha_k t}),\qquad
A_k=-p_3(Q_3+\alpha_k I)^{-1}Q_{3k}u_k(\ell_k\mathbf 1),\quad k\in\{1,2\}.
\]
Hence
\[
\frac{M_1(t)}{M_2(t)}=\frac{A_1}{A_2}e^{(\alpha_2-\alpha_1)t}(1+o(1)).
\]
With \(\rho=e^{\alpha_2-\alpha_1}\), an asymptotic \(K\)-fold crossing obeys
\[
t_K=\frac{\log K-\log(A_1/A_2)}{\log\rho}+o(1).
\]
The source's Table 5 uses \(\log K/\log\rho\) as the time until class \(\mathcal S_1\) has \(K\) times the mass of class \(\mathcal S_2\). That identification additionally requires \(A_1/A_2=1\) at leading order and neglect of faster modes; neither condition follows from the damping ratio alone.

## Assumptions and scope
The statement concerns the source's perfect-vertical-transmission architecture, in which the mixed class can enter either single-type class and neither single-type class can return to the mixed class. The initial distribution is supported on the mixed class, matching the source's displayed tutorial and larger-household trajectories. The ordering \(\alpha_3>\alpha_2>\alpha_1>0\) is the regime used for the source's QSD interpretation. The dominant eigenvalue of each single-type block is assumed simple, as follows from irreducibility of that communicating class. Conditioning on non-extinction does not change \(M_1/M_2\), because the common conditioning denominator cancels.

The claim does not assert a corrected numerical value for any Table 5 entry without reconstructing the source's full numerical generator. It identifies the missing source-specific amplitude and gives an exact formula for it.

## Proof
For \(k\in\{1,2\}\), variation of constants for the block-triangular chain gives
\[
p_k(t)=\int_0^t p_3e^{Q_3s}Q_{3k}e^{Q_k(t-s)}\,ds.
\]
Perron-Frobenius asymptotics inside class \(\mathcal S_k\) give
\[
e^{Q_k u}=e^{-\alpha_k u}u_k\ell_k+o(e^{-\alpha_k u})
\]
in operator norm on this finite state space. Because the mixed block decays strictly faster, \(Q_3+\alpha_kI\) is Hurwitz, so the tail of the convolution is integrable. Multiplying by the all-ones column yields
\[
M_k(t)=e^{-\alpha_k t}\left(\int_0^\infty p_3e^{(Q_3+\alpha_kI)s}Q_{3k}u_k\,ds\right)(\ell_k\mathbf1)+o(e^{-\alpha_k t}).
\]
Using \(\int_0^\infty e^{(Q_3+\alpha_kI)s}ds=-(Q_3+\alpha_kI)^{-1}\) gives the displayed \(A_k\). Positivity of the entry pathways and Perron vectors makes \(A_k>0\) when class \(\mathcal S_k\) is reachable. Dividing the two class-mass asymptotics proves the ratio and crossing formula.

To show that the prefactor is not determined by the spectral gap, consider transient states \(M,W,I\) and an absorbing state. Let \(M\) jump to \(W\) at rate \(r_1\), to \(I\) at rate \(r_2\), and let \(W\) and \(I\) die at rates \(\alpha_1\) and \(\alpha_2\), with \(r=r_1+r_2>\alpha_2>\alpha_1\). Starting from \(M\),
\[
P_W(t)=\frac{r_1}{r-\alpha_1}\left(e^{-\alpha_1t}-e^{-rt}\right),\qquad
P_I(t)=\frac{r_2}{r-\alpha_2}\left(e^{-\alpha_2t}-e^{-rt}\right).
\]
Thus
\[
\frac{P_W(t)}{P_I(t)}\sim
\frac{r_1(r-\alpha_2)}{r_2(r-\alpha_1)}e^{(\alpha_2-\alpha_1)t}.
\]
Holding \(r,\alpha_1,\alpha_2\) fixed keeps \(\rho\) fixed while changing \(r_1/r_2\) changes the prefactor continuously. Therefore no gap-only formula can determine the class-mass hitting time from a mixed start.

## Verification
The bundled checker evaluates the exact three-state formulas at \(\alpha_1=0.01\), \(\alpha_2=0.02\), \(r=1\), \(r_1=0.25\), \(r_2=0.75\). Here
\[
A_1/A_2=98/297\approx0.3299663.
\]
For \(K=10\), the gap-only value is about \(230.2585\) days, while the amplitude-adjusted crossing is about \(341.1350\) days. Direct bisection of the exact ratio gives the same crossing to the checker tolerance. The example is a proof witness, not a fit to the source's biological parameter set.

## Relationship to prior work
Barlow, Penington and Adams define the damping ratio as \(\rho=e^{\lambda_2-\lambda_1}\), describe it as a rate of convergence to the QSD, and in Appendix G explicitly retain modal coefficients \(c_i\) in the spectral expansion. Their Table 5 then reports \(\log K/\log\rho\) as the time until the wildtype-only class has \(K\) times the Wolbachia-only class mass. The formula above resolves those two statements by retaining the entry/eigenvector amplitude that the class-mass ratio needs.

Stott, Townley and Hodgson (2011) already emphasize in the broader matrix-population setting that a damping ratio is an asymptotic rate and ignores the initial population structure. That general warning does not give the reducible-CTMC entry formula above or identify the missing factor in this Wolbachia class-mass calculation. The present result should therefore be read as a source-specific structural correction, not as a claim that initial-condition sensitivity of damping-ratio heuristics is new in general.

## Limitations
The formula assumes the perfect-transmission block architecture and strict spectral ordering \(\alpha_3>\alpha_2>\alpha_1\). Resonance, repeated dominant eigenvalues, or zero reachability coefficients require separate asymptotics. The result does not recompute the source's full \(C=3\) or \(C=30\) generators, so it does not state how far any particular published number moves after inserting the true amplitude. It also does not challenge the source's QSD, invasion-probability, or expected-invasion-time calculations.

## References
Barlow, A., Penington, S., and Adams, B. *Analysis of a household-scale model for the invasion of Wolbachia into a resident mosquito population*. Journal of Mathematical Biology 92, 18 (2026). DOI: 10.1007/s00285-025-02332-8. First public preprint: arXiv:2502.12833v1, 2025-02-18.

Stott, I., Townley, S., and Hodgson, D. J. *A framework for studying transient dynamics of population projection matrix models*. Ecology Letters 14 (2011), 959–970. DOI: 10.1111/j.1461-0248.2011.01659.x.
