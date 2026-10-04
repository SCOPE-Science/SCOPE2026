# Exact Gaussian timing-jitter law for the analytic perfect-state-transfer chain

## Finding

Consider the analytic \(N\)-site \(XX\) perfect-state-transfer chain
\[
J_n=\frac{\lambda}{2}\sqrt{n(N-n)},
\qquad
n=1,\ldots,N-1,
\qquad
\lambda>0.
\]
Its ideal endpoint-transfer time is
\[
t_0=\frac{\pi}{\lambda}.
\]

Model readout-clock uncertainty by
\[
T=t_0+\Xi,
\qquad
\Xi\sim\mathcal N(0,\sigma_t^2).
\]
Set
\[
m=N-1,
\qquad
s=\lambda\sigma_t.
\]
Then the exact mean endpoint occupation probability is
\[
\boxed{
\mathcal P_m(s)
=
4^{-m}
\left[
\binom{2m}{m}
+
2\sum_{k=1}^{m}
\binom{2m}{m-k}
e^{-k^2s^2/2}
\right].
}
\]

For every integer
\[
m\ge1,
\]
the function
\[
s\mapsto\mathcal P_m(s)
\]
is strictly decreasing on
\[
s>0,
\]
with
\[
\mathcal P_m(0)=1
\]
and
\[
\lim_{s\to\infty}\mathcal P_m(s)
=
4^{-m}\binom{2m}{m}.
\]

There are two different large-chain regimes.

On the natural high-fidelity scale
\[
s=\frac{c}{\sqrt m},
\qquad
c\ge0,
\]
one has the exact limiting profile
\[
\boxed{
\lim_{m\to\infty}
\mathcal P_m\left(\frac{c}{\sqrt m}\right)
=
\frac{1}{\sqrt{1+c^2/2}}.
}
\]

For any fixed
\[
s>0,
\]
the mean transfer probability instead has the asymptotic law
\[
\boxed{
\lim_{m\to\infty}
\sqrt m\,\mathcal P_m(s)
=
\frac{1}{\sqrt\pi}
\left(
1+2\sum_{k=1}^{\infty}e^{-k^2s^2/2}
\right).
}
\]
The parenthesis is the standard Jacobi theta series
\[
\vartheta_3\!\left(0,e^{-s^2/2}\right).
\]

Finally, fix a target
\[
\eta\in(0,1).
\]
For all sufficiently large \(m\), there is a unique
\[
s_{m,\eta}>0
\]
such that
\[
\mathcal P_m(s_{m,\eta})=\eta,
\]
and
\[
\boxed{
\sqrt m\,s_{m,\eta}
\longrightarrow
\sqrt{2(\eta^{-2}-1)}.
}
\]
In physical time units,
\[
\boxed{
\sigma_{t,\eta}
\sim
\frac{\sqrt{2(\eta^{-2}-1)}}{\lambda\sqrt{N-1}}.
}
\]

Thus the deterministic timing-window intuition for this chain sharpens, under Gaussian clock jitter, to an exact finite-size law, a universal \(1/\sqrt N\)-scale high-fidelity profile, and a distinct fixed-noise \(1/\sqrt N\) decay law with an explicit periodic-revival prefactor.

## Assumptions and scope

The system is the excitation-preserving \(XX\) chain in the one-excitation sector with the analytic couplings displayed above. The endpoint quantity is the probability that an excitation initially at site \(1\) is found at site \(N\) at readout.

The timing offset is Gaussian on the real line. Because the ideal transfer probability is periodic, the same expectation is obtained if one instead regards the phase error modulo the transfer period as a wrapped Gaussian.

The standard deviation
\[
\sigma_t
\]
is an external readout-clock uncertainty. Static coupling disorder, dephasing, amplitude damping, and correlated fabrication errors are not included.

The result concerns mean endpoint occupation probability. It is not a statement about worst-case timing error, arbitrary-state channel fidelity with additional phase corrections, or repeated-use memory effects.

## Proof

For this chain, the endpoint transfer amplitude is
\[
F(t)
=
\left[
-i\sin\left(\frac{\lambda t}{2}\right)
\right]^m,
\qquad
m=N-1.
\]
At
\[
t=t_0+\Xi
=
\frac{\pi}{\lambda}+\Xi,
\]
the transfer probability is therefore
\[
|F(t)|^2
=
\cos^{2m}\left(\frac{\lambda\Xi}{2}\right).
\]
Let
\[
X=\lambda\Xi.
\]
Then
\[
X\sim\mathcal N(0,s^2).
\]

The finite Fourier expansion
\[
\cos^{2m}\left(\frac{x}{2}\right)
=
4^{-m}
\left[
\binom{2m}{m}
+
2\sum_{k=1}^{m}
\binom{2m}{m-k}\cos(kx)
\right]
\]
and the Gaussian characteristic function
\[
\mathbb E[\cos(kX)]
=
e^{-k^2s^2/2}
\]
give the displayed exact formula for
\[
\mathcal P_m(s).
\]

Every nonconstant term in that finite sum has a positive coefficient and a factor
\[
e^{-k^2s^2/2}.
\]
Consequently
\[
\frac{d}{ds}\mathcal P_m(s)<0
\qquad
(s>0),
\]
which proves strict monotonicity. The endpoint values follow by setting
\[
s=0
\]
and by sending
\[
s\to\infty.
\]

For the high-fidelity scaling, write
\[
X=\frac{cZ}{\sqrt m},
\qquad
Z\sim\mathcal N(0,1).
\]
For every fixed real \(z\),
\[
2m\log\cos\left(\frac{cz}{2\sqrt m}\right)
\longrightarrow
-\frac{c^2z^2}{4}.
\]
Because the transfer probability is bounded by \(1\), dominated convergence yields
\[
\mathcal P_m\left(\frac{c}{\sqrt m}\right)
\longrightarrow
\mathbb E\left[e^{-c^2Z^2/4}\right]
=
\frac{1}{\sqrt{1+c^2/2}}.
\]

For fixed
\[
s>0,
\]
factor the central binomial coefficient:
\[
\mathcal P_m(s)
=
\frac{\binom{2m}{m}}{4^m}
\left[
1+
2\sum_{k=1}^{m}
R_{m,k}e^{-k^2s^2/2}
\right],
\]
where
\[
R_{m,k}
=
\frac{\binom{2m}{m-k}}{\binom{2m}{m}}
=
\prod_{j=1}^{k}
\frac{m-j+1}{m+j}.
\]
For each fixed \(k\),
\[
R_{m,k}\longrightarrow1,
\]
and
\[
0\le R_{m,k}\le1.
\]
Since
\[
\sum_{k\ge1}e^{-k^2s^2/2}<\infty,
\]
dominated convergence for the series gives
\[
1+
2\sum_{k=1}^{m}
R_{m,k}e^{-k^2s^2/2}
\longrightarrow
1+
2\sum_{k=1}^{\infty}e^{-k^2s^2/2}.
\]
The standard central-binomial asymptotic
\[
\frac{\binom{2m}{m}}{4^m}
\sim
\frac{1}{\sqrt{\pi m}}
\]
then proves the fixed-noise limit.

For the target-fidelity threshold, strict monotonicity gives uniqueness whenever
\[
4^{-m}\binom{2m}{m}<\eta<1.
\]
The left endpoint tends to zero, so this holds for all sufficiently large \(m\). The high-fidelity scaling limit is continuous and strictly decreasing in \(c\), hence inversion of the limit profile gives
\[
\sqrt m\,s_{m,\eta}
\longrightarrow
\sqrt{2(\eta^{-2}-1)}.
\]

## Verification

`verify_gaussian_timing.py` performs four independent numerical checks.

First, it constructs the finite single-excitation Hamiltonian directly for small chain sizes and evaluates its exponential by a power series, verifying the endpoint amplitude
\[
F(t)
=
\left[
-i\sin\left(\frac{\lambda t}{2}\right)
\right]^{N-1}.
\]

Second, it compares the finite binomial-exponential formula for
\[
\mathcal P_m(s)
\]
with direct Gaussian quadrature by composite Simpson integration.

Third, it checks the
\[
s=c/\sqrt m
\]
profile against increasing chain lengths and verifies convergence to
\[
(1+c^2/2)^{-1/2}.
\]

Fourth, it checks both the fixed-\(s\) theta-series constant and the asymptotic target-jitter threshold obtained by numerical inversion.

The finite replay supplements, rather than replaces, the analytic proof.

## Relationship to prior work

Christandl, Datta, Ekert, and Landahl give the engineered chain and the exact endpoint amplitude
\[
F(t)
=
\left[
-i\sin\left(\frac{\lambda t}{2}\right)
\right]^{N-1}.
\]
Their paper explicitly leaves other error sources untreated.

Kay later studies timing tolerance for perfect-state-transfer chains. In the analytic chain, the review identifies the \(J_x\) coupling pattern, the perfect transfer time, and the unusually broad timing peak; its timing-error discussion uses deterministic timing windows and local curvature. An earlier Kay paper likewise studies a deterministic offset from the ideal readout time and derives spectral robustness bounds.

Kirkland and, subsequently, Gordon, Kirkland, Li, Plosker, and Zhang develop sensitivity formulas and lower bounds for small deterministic readout-time perturbations on more general state-transfer graphs. The latter work does not use Gaussian, random, or averaged readout times.

The present claim is narrower in model but different in question: it integrates the exact analytic-chain transfer law against a Gaussian timing distribution and then determines the complete finite-size expression together with two sharp large-chain regimes. Targeted searches for Gaussian readout jitter, random timing errors, Krawtchouk-chain timing averages, central-binomial timing laws, and theta-function timing laws did not locate an equivalent statement.

A dissertation on state transfer in spin chains discusses deterministic high-fidelity timing windows for engineered spectra. Only searchable excerpts were available during this comparison, so an equivalent stochastic calculation elsewhere in that document remains a residual literature risk.

## Limitations

The Gaussian clock-error model is idealized. A physical readout system with hard truncation, non-Gaussian tails, drift, or correlated timing errors will generally have a different exact average.

The mean occupation probability can benefit from later periodic revivals when the Gaussian error becomes broad; this is why the fixed-\(s\) prefactor contains a theta series. If an experiment declares later readout periods invalid rather than equivalent, the error distribution should be truncated or conditioned and the formula changes.

The asymptotic target law concerns fixed
\[
\eta\in(0,1).
\]
Targets approaching \(1\) with chain length require a finer scaling analysis.

The result does not claim that the \(1/\sqrt N\) timing scale itself was previously unknown; deterministic timing-window analyses already motivate that scale. The new content is the exact Gaussian average, its universal limiting profile, the fixed-noise theta-series law, and the sharp stochastic target threshold.

## References

1. A. Kay, “A Review of Perfect State Transfer and its Application as a Constructive Tool,” arXiv:0903.4274, first submitted 25 March 2009; journal version: *International Journal of Quantum Information* 8 (2010), 641–676, DOI: 10.1142/S0219749910006514.
2. M. Christandl, N. Datta, A. Ekert, and A. J. Landahl, “Perfect state transfer in quantum spin networks,” arXiv:quant-ph/0309131; *Physical Review Letters* 92 (2004), 187902, DOI: 10.1103/PhysRevLett.92.187902.
3. A. Kay, “Perfect State Transfer: Beyond Nearest-Neighbor Couplings,” arXiv:quant-ph/0509065; *Physical Review A* 73 (2006), 032306, DOI: 10.1103/PhysRevA.73.032306.
4. S. Kirkland, “Sensitivity analysis of perfect state transfer in quantum spin networks,” *Linear Algebra and its Applications* 472 (2015), 1–30, DOI: 10.1016/j.laa.2015.01.013.
5. W. Gordon, S. Kirkland, C.-K. Li, S. Plosker, and X. Zhang, “Bounds on probability of state transfer with respect to readout time and edge weight,” arXiv:1510.05550; *Physical Review A* 93 (2016), 022309, DOI: 10.1103/PhysRevA.93.022309.
