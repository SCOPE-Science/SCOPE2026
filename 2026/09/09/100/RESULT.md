\
# Reproducible numerical stability diagnostics for an individual Brill–Lindquist minimal-surface candidate (equal bare masses 1,1; separation 2)

## Context
In time-symmetric Brill–Lindquist initial data, marginally outer trapped surfaces are minimal surfaces and the MOTS stability operator is self-adjoint. Prior numerical-relativity work, including Pook-Kolb et al. (2019), already studies the MOTS stability parameter and stability spectrum in binary black-hole initial data, including Brill–Lindquist sequences. The purpose of this record is therefore a reproducible benchmark at one explicitly specified equal-mass parameter point, not a claim of the first stability computation for Brill–Lindquist data.

## Definitions
- Conformal factor
  \[
  \psi = 1 + \frac{1}{2d_1}+\frac{1}{2d_2},
  \]
  with punctures at \((\rho,z)=(0,+1),(0,-1)\), bare masses \(1,1\), separation \(2\), and \(g=\psi^4\delta\).
- ADM mass in these code units is \(m_{\rm ADM}=2\).
- The archived upper-puncture surface is represented by
  \(X(\lambda)=H(\lambda)\sin\lambda\),
  \(Z(\lambda)=1+H(\lambda)\cos\lambda\),
  sampled at \(N=800\) intervals, with an \(N=400\) companion.
- In the time-symmetric vacuum case, on an exact smooth MOTS the stability operator reduces to
  \[
  L_\Sigma=-\Delta_\Sigma+Q,\qquad
  Q=-(\operatorname{Ric}_g(n,n)+|A_g|^2).
  \]
  For such a fixed smooth surface, the principal eigenvalue obeys
  \(\min_\Sigma Q\le\lambda_1\le |{\Sigma}|^{-1}\int_\Sigma Q\,dA\).

## Numerical result
The archived finite-difference solve has an interior residual of approximately
\(3.9\times10^{-11}\) in the solver's discrete MOTS equation. On the sampled
\(N=800\) geometry, the archived verification reports
- \(H\in[0.382774,0.414862]\);
- sampled \(Q_{\min}\approx0.157901\);
- area-weighted sampled mean \(Q\approx0.159996\);
- area \(A\approx78.538913\).

An independent implementation of the same formulas at lower resolutions reproduced the same numerical regime:
- \(N=80\): \(Q_{\min}=0.157901658\), mean \(Q=0.159992234\);
- \(N=120\): \(Q_{\min}=0.157901641\), mean \(Q=0.159994474\).

Multiplying by \(m_{\rm ADM}^2=4\) gives the corresponding dimensionless scale near
\(0.632\)–\(0.640\).

These numbers are strong numerical evidence that the individual surface candidate is strictly stable. They are **not** a validated continuum enclosure for the principal eigenvalue of an exact MOTS.

## Why this is not a rigorous eigenvalue certificate
The archived program solves a finite-difference system and evaluates \(Q\) from sampled numerical derivatives. The small discrete residual does not by itself prove that a nearby exact minimal surface exists with a controlled \(C^2\) error. Likewise, the script's “Lipschitz gap” is estimated from grid derivatives rather than from an a priori continuum derivative bound, and the quadrature remainder is estimated from sampled second derivatives. Pole values are extrapolated rather than enclosed by a regularized interval argument.

Therefore the previously reported interval
\([0.157883,0.159998]\) (code units), or
\([0.631530,0.639991]\) after rescaling, should be interpreted only as a reproducible grid-based diagnostic interval, not as a mathematically validated enclosure for the exact continuum operator.

## Reproducibility
- `artifacts/stageF.py` regenerates the finite-difference candidate and sampled \(Q\) data.
- `artifacts/verify_certificate.py` replays the archived residual, sampled minimum/mean, area, and rescaling from `prof800.npy`.
- `prof400.npy` and `prof800.npy` provide the archived convergence pair.

The scripts use NumPy floating-point arithmetic and are suitable for numerical replay, not formal or interval certification.

## Literature context
- D. Pook-Kolb, O. Birnholtz, B. Krishnan, E. Schnetter, *Existence and stability of marginally trapped surfaces in black-hole spacetimes*, Phys. Rev. D 99, 064005 (2019), arXiv:1811.10405.
- L. Andersson, M. Mars, W. Simon, *Stability of marginally outer trapped surfaces and existence of marginally outer trapped tubes*, arXiv:0704.2889.
- X. Yu, *Blowup rate control for Jang's equation*, arXiv:1906.08841.
- Recent reviews of quasi-local horizons summarize Brill–Lindquist stability-spectrum calculations and their role in MOTS bifurcations.

## Limitations
This record does not prove global outermost status of the individual surface, does not prove a continuum lower bound for \(\lambda_1\), and does not establish a Jang-equation blow-up estimate for this numerical candidate. A rigorous certification would require, at minimum, an existence/error theorem (or validated numerics) for the exact minimal surface together with certified bounds for the coefficients and eigenvalue estimates.
