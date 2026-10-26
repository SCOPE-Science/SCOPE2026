# Reentrant mRNA spectral resonance with purely real relaxation modes in a two-stage feedback circuit

## Finding

For a natural two-species transcription--translation birth--death model, increasing a *negative* transcription-feedback gain creates and then destroys a strictly positive-frequency global maximum of the stationary **mRNA** power spectral density (PSD), although the deterministic linearization retains two distinct real negative eigenvalues throughout both transitions. The **protein** PSD is strictly decreasing at all nonnegative frequencies over the entire real-eigenvalue regime. The two feedback thresholds are exactly the first two positive roots of the cubic
\[
P(q)=2q^3-91q^2+220q-10,
\]
namely \(q_1=0.046341956618\ldots\) and \(q_2=2.512597182950\ldots\). This spectral reentrance occurs for \(q_1<q<q_2\) and for no other \(0\leq q<81/4\). The phenomenon is robust in the sense that small simultaneous changes to the fixed positive reaction-rate parameters preserve at least a low-pass/band-pass/low-pass sequence at three fixed feedback values; the exact cubic thresholds refer only to the normalized rates below.

## Assumptions and scope

Let \(V\) be a system-size parameter. Denote mRNA and protein concentrations by \(m=M/V\) and \(p=N/V\). Consider the continuous-time chemical jump process with four channels, concentration changes of magnitude \(V^{-1}\), and propensities (in the order mRNA birth, mRNA degradation, protein birth, protein degradation)
\[
V\,10\exp[-(q/10)(p-1)],\qquad V\,10m,\qquad V\,m,\qquad V\,p.
\]
Here the dimensionless feedback slope \(q\geq0\), the mRNA turnover rate is ten times the protein turnover rate, and other fixed rates have been normalized to one. The smooth transcription response is strictly positive and decreases in protein concentration for \(q>0\). The unique positive deterministic fixed point is \((m,p)=(1,1)\). The theorem concerns the **stationary linear-noise (Gaussian/Ornstein--Uhlenbeck) approximation** around this fixed point, equivalently the weak-noise limit of the system-size expansion; no claim is made that the finite-\(V\) jump-process PSD equals the displayed formula.

Write \(\xi=(\xi_m,\xi_p)^\top\) for the scaled Gaussian concentration fluctuations. Their stationary dynamics are \(d\xi=K_q\xi\,dt+\sqrt{D}\,dW\), with
\[
K_q=\begin{pmatrix}-10&-q\\1&-1\end{pmatrix},\qquad D=\begin{pmatrix}20&0\\0&2\end{pmatrix}.
\]
The two-sided stationary spectral-density matrix is the Fourier transform of the covariance, with no extra \(2\pi\) factor in the spectral definition:
\[
S(\omega)=(K_q-i\omega I)^{-1}D\bigl[(K_q-i\omega I)^{-1}\bigr]^\dagger.
\]
A *band-pass maximum* means a strict global maximum at a frequency \(\omega_*>0\) on the half-line \(\omega\geq0\). This definition does not mean that the deterministic orbit oscillates, nor does it quantify spectral peak sharpness.

## Proof

**1. Stable real relaxation.** Linearizing the mean-field equations \(\dot m=10e^{-(q/10)(p-1)}-10m\) and \(\dot p=m-p\) yields the stated \(K_q\). Its eigenvalues are
\[
\lambda_{\pm}=\frac{-11\pm\sqrt{81-4q}}2.
\]
For all \(0\leq q<81/4\), both eigenvalues are strictly negative, distinct and real. The deterministic fixed point is globally unique on the positive quadrant since the first nullcline decreases in \(p\) while the second is \(m=p\). A stationary OU distribution exists uniquely for these gains.

**2. Exact two observable spectra.** The inverse resolvent has first row proportional to \((-1-i\omega,q)\) and second row proportional to \((-1,-10-i\omega)\), with determinant \((10+q-\omega^2)+11i\omega\). Therefore
\[
S_{mm}(\omega)=\frac{20(1+\omega^2)+2q^2}{(10+q-\omega^2)^2+121\omega^2},
\qquad
S_{pp}(\omega)=\frac{220+2\omega^2}{(10+q-\omega^2)^2+121\omega^2}.
\]
The underlying noise intensities \(20\) and \(2\) are sums of steady production and removal reaction propensities; no cross-noise is assumed because each elementary reaction changes one species.

**3. Complete mRNA maximum classification.** Put \(x=\omega^2\geq0\), \(u=1+q^2/10\), \(B=101-2q\), and \(c=10+q\). Then
\[
S_{mm}(\sqrt{x})=\frac{20(x+u)}{F_q(x)},\qquad F_q(x)=x^2+Bx+c^2=(c-x)^2+121x>0.
\]
Direct differentiation gives
\[
\frac{dS_{mm}(\sqrt{x})}{dx}
=\frac{20}{F_q(x)^2}\left(\frac{P(q)}{10}-2ux-x^2\right),
\qquad P(q)=2q^3-91q^2+220q-10.
\]
The bracket is strictly decreasing for \(x\geq0\). If \(P(q)\leq0\), the spectrum strictly decreases for every \(x>0\), and its maximum is at zero. If \(P(q)>0\), it first increases and then decreases, with its *unique* positive maximizer
\[
x_*(q)=-u+\sqrt{u^2+P(q)/10},\qquad\omega_*(q)=\sqrt{x_*(q)}.
\]
Since the spectrum tends to zero as \(x\to\infty\), this is a global, not merely a local, maximum.

**4. Precisely two thresholds before the eigenvalue collision.** The derivative \(P'(q)=6q^2-182q+220\) has its first zero \(q_-=(91-\sqrt{6961})/6\in(1,5)\) and its second zero \(q_+=(91+\sqrt{6961})/6>81/4\). Thus \(P\) increases until \(q_-\) and decreases throughout \([q_-,81/4]\). The exact signs \(P(0)=-10\), \(P(1)=121\), and \(P(5)=-935\) show that there are exactly two roots in \([0,81/4)\), one in \((0,1)\) and one in \((1,5)\). Their numerical values stated above are approximations to these algebraically specified roots.

**5. The protein spectrum never develops a positive-frequency peak in this regime.** Its derivative with respect to \(x\) has the sign of
\[
q^2+240q-11010-220x-x^2.
\]
For \(0\leq q<81/4\), the constant term is at most \((81/4)^2+240(81/4)-11010<0\). Hence \(S_{pp}(\omega)\) strictly decreases for \(\omega>0\), despite the mRNA resonance window.

**6. Robustness, not a numerological isolated slice.** The physically relevant inequalities are strict at \(q=0,1,5\): the mRNA initial spectral derivatives are respectively negative, positive, negative, the two eigenvalues are distinct and negative, and the protein initial spectral derivatives are negative. Linear-noise spectral matrices, eigenvalues and their initial spectral derivatives depend continuously on the local reaction-rate parameters. Consequently the same three-phase pattern at these three feedback values persists under sufficiently small rate perturbations that preserve the single-species birth--death noise structure, positive fixed points and smooth negative feedback. This does not assert that the perturbed family still has exactly two crossings without additional control.

## Verification

The standalone file `verify_spectrum.py` uses symbolic matrix inversion to reconstruct both PSDs from \(K_q\) and \(D\), checks the differentiated polynomial identities exactly, verifies the turning-point and root inequalities, and independently evaluates the original complex resolvent at nine feedback strengths and eight frequencies each (72 matrix evaluations). It also compares the global mRNA maximum with a 5,000-point frequency-square grid. Run with Python, NumPy and SymPy:

```bash
python verify_spectrum.py
```

These are finite computational checks supplementing, not replacing, the exact algebraic proof above. The displayed asymptotic limit concerns the Gaussian system-size expansion; no finite-volume numerical simulation or all-volume error estimate is claimed.

## Relationship to prior work

Aslyamov, Ptaszyński and Esposito (arXiv:2510.17587v1, first public October 20, 2025) derive the general stationary Gaussian resolvent PSD and its negative-feedback gene-regulatory application, emphasizing full-matrix responses and zero-frequency noise. The formula in Step 2 follows from their generic resolvent and is not itself claimed as a new PSD method. The present specific result is the **complete reentrant global finite-frequency phase diagram with two exact feedback boundaries in a minimal two-species model, while all deterministic eigenvalues stay real and the protein spectrum remains low-pass**. Their accessible primary text, including the gene-network section and appendix, does not explicitly state or classify this reentrance.

Gupta and Khammash (2022) explicitly study a **two-species negative-feedback network** in their Eq. (40), give the exact **protein/output** PSD, and prove a necessary-and-sufficient global positive-frequency peak criterion in Eq. (41) and Supplementary Proposition S4.1. Under the present rates their output formula gives the protein PSD here (up to an overall positive factor). **Consequently the protein low-pass conclusion is a previously implied corollary, not separately claimed as new**. Their published output-spectrum criterion does not determine the **mRNA/controller** reentrant band-pass window and two cubic thresholds with fixed mean concentrations. The same paper additionally studies antithetic integral-feedback regulators. Joo and Chauhan (arXiv:1408.4782) already document noise-induced spectral peaks despite real deterministic eigenvalues in three-species biochemical networks; such peaks *by themselves* are prior art. The distinguishing content here is the **two-species nonmonotone feedback window, exact two-threshold global classification and same mathematical model observable contrast**, not the general idea of noise-induced resonances.

## Limitations

This is a theorem for the **stationary Gaussian linear-noise approximation**, not an exact finite-system stochastic spectral theorem or proof of a coherent oscillatory trajectory. The two numerical thresholds depend on the specified dimensionless reaction-rate ratios and chosen one-parameter transcription curve, although the qualitative three-phase witness is open under small rate changes. The theorem neither gives a universal criterion for all feedback kinetics nor extends the protein low-pass statement beyond the distinct-real-eigenvalue range. General spectral theory could implicitly imply the algebraic calculation, and further expert originality assessment is warranted.

## References

1. T. Aslyamov, K. Ptaszyński and M. Esposito, *Macroscopic fluctuation-response theory and its use for gene regulatory networks*, arXiv:2510.17587v1 (October 20, 2025), especially Eqs. (2), (6), (25)--(33) and appendix; subsequently Phys. Rev. Lett. 136, 067102 (2026). https://arxiv.org/abs/2510.17587
2. A. Gupta and M. Khammash, *Frequency spectra and the color of cellular noise*, Nature Communications 13, 4305 (2022). https://doi.org/10.1038/s41467-022-31263-x
3. J. Joo and S. Chauhan, *Design principles of noise-induced oscillation in biochemical reaction networks: II. Coupled positive and negative feedback loops*, arXiv:1408.4782v1 (August 20, 2014). https://arxiv.org/abs/1408.4782
