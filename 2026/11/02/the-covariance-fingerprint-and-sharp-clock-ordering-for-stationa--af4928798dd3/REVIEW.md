# Review

## Correctness — PASS

The equilibrium size-biased interval and conditional uniform phase are specified rather than assumed from a fresh-reset initialization. Independent Brownian increments yield the covariance exactly, and one-sided derivatives at atoms recover the full tail. The finite-horizon double covariance integral gives the displayed strictly convex polynomial in renewal length; its strict Jensen inequality proves unique fixed-mean optimization. Tonelli and regular-variation integration justify the extended third-moment threshold and the three power-law cases. The Fourier formula follows by justified improper-transform integrations by parts. All boundary cases, the Poisson special case and stationary deterministic phase were checked. The separate self-contained checker completed 143 independent computational comparisons; correctness rests on the exact proof.

## Originality — PASS, with residual risks

The renewal-age framework and stationary spatial distributions are established in arXiv:2203.04046 and arXiv:2205.01613, and arXiv:2306.13621 already proves deterministic resetting minimizes the **one-time** stationary mean-square displacement. arXiv:1806.03435 establishes covariance and PSD for *Poisson* resetting. Those are excluded from the novelty claim. The current theorem addresses arbitrary iid strictly positive intervals, a *two-time* covariance that identifies the clock law and diffusivity, and the unique all-time-window variance minimizer, as well as the associated third-moment transition. Searches of mathematical research records and relevant literature identified nearby renewal age/residual results and reset-clock optimization for distinct cost functionals, not an evaluated theorem with equivalent coverage. A general regenerative-process covariance identification or convex-order inequality may imply portions of the result, and publication-priority uncertainty remains.

## Mathematical value — PASS

Non-Poissonian reset clocks occur naturally in experiments, and observational correlations are a meaningful alternative to fitting stationary spatial densities. The covariance fingerprint identifies exactly what can be inferred from ideal noiseless time correlations. The sharp every-window clock optimization is stronger than a stationary-width extremum and gives an explicit precision penalty for exponential resets; the second/third moment distinction identifies a previously unaddressed temporal averaging boundary. These are structurally motivated, physically interpretable quantitative questions, not arbitrary parameter substitutions.

## Scope and limitations

The claim is for equilibrium-stationary independent-excursion Brownian dynamics with iid positive intervals of finite first and second moment. It neither guarantees numerical stability of inverse covariance estimation nor extends to nonrenewal or incomplete resetting, nonlinear observables, or other particle models. Numerical checker tests support but do not prove the general result. Independent publication-priority validation is not performed.

Self-review: passed. Independent audit: not yet performed.
