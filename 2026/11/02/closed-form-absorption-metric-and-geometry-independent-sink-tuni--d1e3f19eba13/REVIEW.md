# Independent mathematical audit

## correctness

PASS

No-jump generator A=i Ω T/2−κ E/2 has A+A†=−κ E and no eigenvector with zero first component on the open connected path; hence every eigenvalue has negative real part and the Lyapunov equation A†X+XA=−I has a unique positive solution X=integral e^(A†t)e^(At) dt. Explicit parity-dependent X_jk=(N+1−k)[j/κ+κ(j−1)/Ω²] for even gap, −i(N+1−k)/Ω for odd gap (j<=k), plus conjugate extension; affine second differences and right boundary s_(N+1)=0 establish entrywise commutator identity. This identifies mean for arbitrary density matrices. Diagonal E_j τ=(N+1−j)(j/κ+κ(j−1)/Ω²), strictly convex in κ for j>=2, gives κ_opt=Ω sqrt(j/(j−1)) independent of N and minimum 2(N+1−j)sqrt(j(j−1))/Ω. For j=1 mean N/κ monotone. Independent Python numpy recomputation of Lyapunov residual for N=2..8 and multiple positive Ω,κ passed; all-N is from exact recurrence.

## originality

PASS

General continuous-measurement hitting-time superoperator/inverse is prior work (Varbanov–Krovi–Brun 2008), as is semi-infinite endpoint Lindblad sink (Riberi 2026). The explicit finite N all-initial-state quadratic X and dimension-independent optimal κ for each j>=2 are not stated in inspected relevant prior texts. Prior inverse machinery does not mechanically determine the kernel without solving finite tridiagonal Lyapunov entries. Resultary query found no matching law.

## value

PASS

The mean quantum first-jump time is a natural absorption observable on coherent finite paths. Formula controls every initial state, including coherences, and gives an exact global absorber-strength tuning rule with a physically meaningful exceptional direct-sink case. Explicit all-N solution and Zeno-vs-weak-loss optimum are useful even though a general inverse representation is classical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
