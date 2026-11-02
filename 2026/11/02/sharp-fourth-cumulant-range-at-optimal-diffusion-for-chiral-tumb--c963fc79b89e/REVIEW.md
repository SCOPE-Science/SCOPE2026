# Review of sharp fourth-cumulant range at optimal diffusion for chiral tumblers

## Correctness — PASS

The state space and angular Lévy–diffusion generator are specified for arbitrary symmetric probability measures, including atoms. The positive rotational diffusion gives compact resolvent and a spectral gap at the stationary eigenvalue. Analytic perturbation of the Feynman–Kac tilt rigorously identifies cumulants per unit time. The fourth-order Fourier recurrence is reconstructed explicitly through modes \(0,\pm1,\pm2\), including the eigenfunction normalization correction; it gives the displayed negative fourth-cumulant coefficient at \(D+\lambda(1-c_1)=\Omega\). A weighted probability measure with density proportional to \(1-\cos\eta\) proves the exact strict upper bound and lower equality case. SymPy identities, exact rational examples and independent high-precision finite Fourier eigenvalues agree with the formulas, without being used in place of the proof.

## Originality — PASS, qualified

Olsen–Löwen (arXiv:2405.14326, §§II.1–II.5) already derives the angular propagator, first Fourier-harmonic dependence of diffusivity, and optimal tumbling rate. These are credited. Villa-Torrealba et al. (arXiv:2002.02872, §III.2) computes partial-reorientation fourth moments with no intrinsic chirality, while another section treats reversal and angular diffusion; neither gives the combined intrinsically chiral plus continuous rotational-noise optimized class. Britton et al. (arXiv:2608.23519, §3.5) establishes higher-moment dependence on higher harmonics and a general moment framework; this overlaps the broad mechanism and could serve as an alternative starting point. The claimed new mathematical content is the strict-negative fourth-cumulant identity at the symmetric tumble diffusivity optimum together with the exact attainable global range, equality and nonattainment classifications. Relevant primary text and indexed finding searches did not reveal a directly covering theorem. Residual risk: a generic higher-moment formula could implicitly imply parts of the result, and publication priority is not independently established.

## Mathematical value — PASS

The 2024 universal maximum makes a whole family of control protocols indistinguishable by their diffusion coefficients. The new range identifies what a higher-order trajectory observable can nevertheless resolve, settles an all-distribution extrema problem, and gives sharp experimentally interpretable benchmarks and equality cases, rather than a single arbitrary numerical example. The upper boundary is strictly unattainable at finite control rate, an important distinction from optimization of diffusion alone. A single fourth cumulant cannot identify the full angular law, and no full finite-time distribution theorem is claimed.

## Reproducibility and limitations

Run `python verify.py` with SymPy and mpmath installed. The checker validates the symbolic perturbation formula and three independent tilted-spectrum examples. The global claims are proved in RESULT.md by exact algebra and measure inequalities. Tests cannot replace the infinite-dimensional spectral argument. Broader unpublished or unindexed literature and independent expert review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
