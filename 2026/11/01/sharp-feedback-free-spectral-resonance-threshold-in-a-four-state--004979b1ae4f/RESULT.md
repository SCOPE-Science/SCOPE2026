# Sharp feedback-free spectral resonance threshold in a four-state cyclic promoter

## Finding

**Theorem.** In the stationary four-state, equal-rate directed cyclic promoter model specified below, the two-sided centered mRNA power spectral density has precisely one strict positive-frequency maximum (with a symmetric negative-frequency maximum) if and only if
\[
\gamma^2>4a^2+\frac{32a^3}{3\beta}.
\]
In that regime frequency zero is a strict local minimum and the positive-frequency maximum is global on nonnegative frequencies. At equality or below, the spectrum strictly decreases on all positive frequencies, attaining its global maximum at zero. This is an exact statement about the stationary Markov-modulated immigration–death process, not a diffusion or large-copy-number approximation.

As a boundary comparison, equal-rate unidirectional cycles of two or three promoter states, with transcription from just one state, have strictly decreasing mRNA spectra for all positive parameter values. Moreover, an arbitrary finite reversible promoter coupled to the same immigration–death mechanism cannot have a positive off-center spectral maximum. Hence four states are the minimal homogeneous directed-cycle size capable of this feedback-free spectral resonance.

## Assumptions and scope

Let \(Z_t\in\{0,1,2,3\}\) be a continuous-time Markov chain with transitions \(j\to j+1\pmod 4\) at common rate \(a>0\), independent of the transcript population. Each transition occurs with exponential waiting time. The stationary distribution is uniform. Conditionally on \(Z_t=0\), mRNA molecules are created at Poisson rate \(\beta>0\); no transcript is created in other promoter states. Each present transcript is independently removed at rate \(\gamma>0\). Let \(Y_t\in\mathbb N_0\) be the transcript count under the unique stationary joint law. There is no transcriptional feedback, no translation, no cell division, and no burst production.

Use the Fourier normalization
\[
S_Y(\omega)=\int_{-\infty}^{\infty}e^{-i\omega t}\operatorname{Cov}(Y_t,Y_0)\,dt,
\qquad\omega\in\mathbb R.
\]
The chain has stationary mean \(\mathbb E Y_t=\beta/(4\gamma)\) and a finite covariance integral. A peak is a strict local maximum of this continuous spectrum, and zero frequency is counted separately from its symmetric positive/negative pair.

## Proof

**1. The promoter autocovariance.** Write \(H_t=\mathbf1_{\{Z_t=0\}}\). The four eigenvalues of the directed-cycle generator are \(0,-2a,-a+ia,-a-ia\). Fourier diagonalization of the uniform cycle gives, for every real time \(t\),
\[
\operatorname{Cov}(H_t,H_0)
=\frac18e^{-a|t|}\cos(at)+\frac1{16}e^{-2a|t|}.
\]
At time zero the right-hand side is \(3/16\), the Bernoulli variance at stationary success probability \(1/4\). Fourier transformation (using the stated normalization) gives
\[
S_H(\omega)=\frac{a(\omega^4+3a^2\omega^2+6a^4)}
{2(\omega^2+4a^2)(\omega^4+4a^4)}.
\]
This expression is positive for every real frequency, although the promoter autocovariance has an oscillatory component.

**2. Exact mRNA spectrum.** Conditional on the entire promoter path, immigration events are Poisson and surviving transcript lifetimes are independent exponential random variables. The mean immigration rate is \(\bar\beta=\beta/4\). Decompose the covariance into the contribution from shared surviving molecules and the contribution from promoter-driven fluctuations in the conditional intensity. Fourier transformation of their corresponding convolution kernels gives the exact identity
\[
S_Y(\omega)=\frac{2\bar\beta+\beta^2 S_H(\omega)}
{\gamma^2+\omega^2}
=\frac{\beta/2+\beta^2 S_H(\omega)}{\gamma^2+\omega^2}.
\]
In particular the intrinsic transcript shot-noise contribution is not omitted. This standard transfer identity can also be established directly by generator moment equations, as independently checked in the accompanying program.

**3. Strict spectral shape.** Introduce the dimensionless positive parameters and nonnegative squared frequency
\[
b=\frac\beta a,\qquad g=\frac\gamma a,\qquad x=\frac{\omega^2}{a^2}.
\]
By the preceding formulas,
\[
aS_Y(a\sqrt x)=\frac{b}{2}\,
\frac{1+b(x^2+3x+6)/[(x+4)(x^2+4)]}{g^2+x}.
\]
Differentiating the right-hand side with respect to \(x\) yields exactly
\[
\frac{d}{dx}\bigl[aS_Y(a\sqrt x)\bigr]
=-\frac{bQ(x)}{2(g^2+x)^2(x+4)^2(x^2+4)^2},
\]
where the polynomial is
\[
\begin{aligned}
Q(x)={}&x^6+(8+2b)x^5+(24+13b+bg^2)x^4\\
&+(64+48b+6bg^2)x^3+(144+68b+26bg^2)x^2\\
&+(128+48b+16bg^2)x+256+96b-24bg^2.
\end{aligned}
\]
Every nonconstant coefficient is strictly positive; hence \(Q\) is strictly increasing on \([0,\infty)\), with \(Q(x)\to\infty\). Since the denominator is positive, if \(Q(0)\ge0\), the derivative is strictly negative for all \(x>0\). If \(Q(0)<0\), there is exactly one positive root \(x_*\) of \(Q\), with spectrum strictly increasing up to \(x_*\), strictly decreasing afterwards, and approaching zero as \(x\to\infty\). Thus \(\omega_*=a\sqrt{x_*}\) is the unique positive-frequency maximum, and frequency zero is a strict local minimum. The inequality \(Q(0)<0\) reduces to \(g^2>4+32/(3b)\), equivalent to the announced dimensional threshold. Equality is included in the strictly decreasing branch for positive frequencies.

**4. Minimal-cycle comparison.** For the equal-rate directed two-state cycle, \(S_H(\omega)=a/(4a^2+\omega^2)\). For the equal-rate directed three-state cycle,
\[
S_H(\omega)=\frac{2a(\omega^2+3a^2)}
{3(\omega^4+3a^2\omega^2+9a^4)}.
\]
Each is decreasing as a function of \(\omega^2\ge0\) (for the three-state case the derivative numerator is proportional to \(-\omega^2(\omega^2+6a^2)\)). Since the exact mRNA transfer divides a positive constant plus a nonincreasing spectrum by the strictly increasing \(\gamma^2+\omega^2\), neither case admits an off-center maximum. A single fixed promoter state yields the decreasing Poisson immigration–death spectrum.

Finally, for any finite irreducible *reversible* promoter and real state-dependent rate function \(h\), its centered covariance has a representation \(\sum_{k\ge1}c_k e^{-\lambda_k|t|}\) with \(c_k\ge0\) and \(\lambda_k>0\), by self-adjoint spectral decomposition in stationary weighted \(L^2\). The promoter-rate spectrum is the nonnegative Lorentzian sum \(\sum_k2c_k\lambda_k/(\lambda_k^2+\omega^2)\). The nonzero mean transcript-production shot noise ensures the associated mRNA spectrum is strictly decreasing for positive frequency. This completes the comparison.

## Verification

The accompanying standalone `checker.py` requires only the Python standard library: execute `python3 checker.py`. It checks 48 exact rational instances of the differentiated polynomial identity, compares 600 random independently computed full generator/moment resolvent spectra with the Fourier transfer spectra across two to six promoter states, tests 240 explicit two additional promoter harmonic formulas, and checks four threshold examples. It reports 892 successful checks and a maximal relative discrepancy below \(2\times10^{-14}\) on the specified seeded sample. These are finite corroborations; the root count and all-parameter threshold follow from the sign proof above.

For \(a=1\), \(\beta=8\), and \(\gamma=8\), the unique positive maximum is \(\omega_*\simeq0.7779563871383612\) and \(S_Y(\omega_*)/S_Y(0)\simeq1.0538456991606762\).

## Relationship to prior work

Warren, Tănase-Nicola and ten Wolde (2005) derive exact biochemical noise spectra for linear reaction systems. Rieckh and Tkačik (2013) analyze promoter-state architectures, including a three-state cycling motif, and give the general mRNA-spectrum filtering relation: that general identity is **prior work**, not part of the present originality claim. The new claim here is the complete four-state no-feedback shape threshold, the uniqueness of its positive-frequency maximum, and the minimal equal-rate cycle comparison. Jia, Qian and Zhang (2019) study spectral onset under feedback in a different two-state hybrid gene-expression model; that conclusion does not imply the four-state feedback-free criterion. Jia and Grima (2021) derive more general frequency-domain formulas with cell-lineage effects; general spectral resolvents could algebraically reproduce the current calculation, but a full exact phase diagram for this four-state promoter is not identified in the examined material. No uniqueness in the entire literature is claimed.

## Limitations

The four-state threshold assumes strictly positive rates, a homogeneous unidirectional four-cycle, a single active promoter state, single-molecule Poisson transcription, and first-order decay. It does not classify arbitrary nonreversible promoter generators, heterogeneously directed or bidirectional cycles, bursty production, or protein spectra. The "minimal" statement refers only to homogeneous directed cycles and reversible generators, not every possible network with three states. Nonzero-frequency spectral maxima are not proofs of deterministic limit cycles or experimentally resolvable oscillations. Historical priority remains subject to independent literature review.

## References

1. P. B. Warren, S. Tănase-Nicola, and P. R. ten Wolde, *Exact results for noise power spectra in linear biochemical reaction networks*, arXiv:q-bio/0512041v1, first posted 2005-12-23, https://arxiv.org/html/q-bio/0512041v1.
2. G. Rieckh and G. Tkačik, *Noise and information transmission in promoters with multiple internal states*, arXiv:1307.8075v1, first posted 2013-07-30, https://arxiv.org/abs/1307.8075.
3. C. Jia, H. Qian, and M. Q. Zhang, *Exact power spectrum in a minimal hybrid model of stochastic gene expression oscillations*, arXiv:1909.09769v1, 2019-09-21, https://arxiv.org/abs/1909.09769 (comparison literature only).
4. C. Jia and R. Grima, *Frequency Domain Analysis of Fluctuations of mRNA and Protein Copy Numbers within a Cell Lineage*, Physical Review X 11, 021032 (2021), https://doi.org/10.1103/PhysRevX.11.021032 (comparison literature only).
