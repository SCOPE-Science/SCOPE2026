# Independent mathematical audit

## correctness

PASS

The 2026 Sene--Mansal primary PDF defines F3=(1-theta)omega E-(tau+mu)I, F4=theta rho E-(gamma+mu)A, F5=tau I+gamma A-mu R; thus the model requires A=A0+I^alpha F4 and R=R0+I^alpha F5. Their Eqs.(5.10)-(5.11) replace these by F3 and F4, repeated across the whole corrector weights in (5.15)-(5.16), while predictor (5.21) uses F4 for R. Independently recomputed rational witness theta=1/2,rho=2,gamma=mu=omega=tau=1,E0=1,I0=A0=R0=0 giving F3,F4,F5=(1/2,1,0). The fractional integral asymptotic for continuous g is I^alpha g(t)=g(0)t^alpha/Gamma(alpha+1)+o(t^alpha), so printed-versus-model equations differ by -1/2 and +1 times this factor for any 0<alpha<=1. A convergent scheme consistently implementing the printed fields cannot have claimed vanishing error for target A,R. No claims about missing code or figures.

## originality

PASS

The primary document itself supplies both the correct component definitions and repeatedly inconsistent printed predictor/corrector equations; this exact repeated shift is not an implication of Garrappa’s general correctly indexed system method. An earlier 2022 Sene chapter could contain a related mistake or warning, but its full text was not obtained. The source-specific contradiction was checked directly rather than inferred from title searches or old PASS.

## value

PASS

The defect changes the continuous equations approached by the printed numerical algorithm for two state components, yielding a nonzero leading-order mismatch even under mesh refinement. It therefore negates two printed convergence-error estimates and has concrete significance for reproducibility of epidemic-state simulations. A rational admissible witness and exact asymptotics distinguish this from a harmless isolated label typo.

The dated certificate retains the supplied scientific assessment, sources and limitations.
