# Independent mathematical audit

## correctness

PASS

The stable non-Hermitian no-jump generator K=-iJA-kappa P/2 has all eigenvalues in the open left half-plane: any eigenvector with zero decay at site 1 is zero by nearest-neighbor recurrence. The unique Hermitian solution T of K†T+TK=-I equals integrated survival. I independently verified the even/odd separation matrix ansatz and boundary row cancellation: diagonal T_ss=(N+1-s)(s/kappa+(s-1)kappa/(4J^2)); optimization by strict convexity and s=1 exception follow. Independently solved finite Lyapunov systems in Python for N=2..9 and J=.7,kappa=1.9, with errors under 1e-14; this numerics corroborates but does not prove the all-N statement.

## originality

PASS

The exact mean and size-free optimal sink rate are not supplied by inspected semi-infinite Lindblad walk, finite-array exceptional-point spectral classification, finite-ring traps, or projective-measurement hitting times. A generic Lyapunov inverse method is known, but its full path-specific explicit solution is the substantive evaluated result.

## value

PASS

Coherent transport through an absorbing quantum chain has the natural Zeno-versus-weak-sink tradeoff. A closed finite-size and all-site mean time, together with the surprising starting-site-only optimal loss rate, gives an exact benchmark for quantum absorption and transport, not a routine two-site numerical calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
