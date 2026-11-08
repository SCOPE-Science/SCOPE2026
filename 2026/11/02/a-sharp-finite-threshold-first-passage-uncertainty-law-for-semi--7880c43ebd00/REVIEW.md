# Independent mathematical audit

## correctness

PASS

Reconstructed starting at a renewal epoch: Azuma bounds ensure finite E[N] for finite signed marks of positive stationary drift. Conditional variance decomposition with M=sum stopped edge means and V=sum stopped edge variances gives Var(H)=Var(M)+EV. For g_ij=v_ij-B mu_ij the centered Poisson equation (I-P)h=E_j[g_ij|i] gives E sum_{m<=N}g=E[h(J0)-h(JN)] by bounded-increment optional stopping. Hence exact identity VarH-B EH=Var(M)+E[h(J0)-h(JN)] and universal additive bound. At alpha=mu, overshoot U in [0,mu_max) forces VarM<=mu_max^2/4 and EH=k+O(1). For alpha=c mu+b_i-b_j, bounded endpoint potential again bounds M-k/c, giving same asymptotic coefficient; single-state renewal demonstrates sharpness. Separately reconstructed finite Poisson and crossing moments with 24 exact rational cases in independent_checks.py.

## originality

PASS

The finite-threshold weight-uniform first-passage inequality and exact corrector identity extend beyond the established fixed-time kinetic uncertainty bound. The main cited semi-Markov source identifies the first-passage analogue as a hypothesis, not a proved corollary. First-passage Markov and open-quantum results have different variables/assumptions and coefficients.

## value

PASS

Finite-threshold inequality with a sharp stationary constant, uniform over all positive-drift flux weights and initial states, closes a specific open semi-Markov first-passage uncertainty question and quantifies finite-level correction; the exact boundary term is mathematically motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
