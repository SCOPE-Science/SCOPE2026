# Independent mathematical audit

## correctness

PASS

For y=cos(theta) the cost is h(y)=(arccos y)^2. The identity h(1-v)=4 arcsin(sqrt(v/2))^2 gives an analytic power series at v=0; substitution in (1-y^2)h''-yh'=2 yields c_1=2 and c_(j+1)/c_j=j^2/((j+1)(2j+1)). This gives the stated c_N and bounds (-1)^N h^(N) below by N!c_N on the open interval. The monic Hermite nodal product is 2^(1-N)(T_N-s_N), including the single endpoint y=1 for odd N. Multiplying by the derivative sign gives exactly 2^(1-N)(1-s_N T_N). Continuity handles the endpoints. The polynomial integrates identically for the two measures by the degree bound; the centered grid has angles 2π(j-(N-1)/2)/N for j=0,...,N-1 and the stated second moment. A zero deficit forces support on the grid and discrete Fourier inversion forces equal weights. On writing rho for distance to the grid, 1-s_N cos(N theta) >= 2N^2 rho^2/π^2, yielding the claimed second bound. Nearest-node projection costs E[rho], bounds the k-th mode of the projected measure by k E[rho], and discrete inversion gives total variation at most N(N-1)E[rho]/4; moving this unmatched mass costs at most π times that amount. The symmetric small shifts do not cross the cut, have deficit h^2 and W1 exactly h by the generating coupling and the distance-to-grid test. The real-line consequence follows by the pointwise nearest-representative inequality, with equality forcing the canonical representatives. These proofs cover arbitrary admissible Borel probability measures and every N>=3; the reviewed frozen checker is finite diagnostic evidence only and was not executed.

## originality

PASS

Pass for the combined geodesic-energy result, specifically the explicit Nth-mode coercivity and sharp-order transport from that energy deficit for an arbitrary circle measure with a block of vanishing moments. Classical Hermite and Gaussian/Gauss–Radau methods and the existence of square-root stability in different moment problems are not new. No inspected comparison subsumes the distinct contribution.

## value

PASS

For the natural moment problem of cancelling the first several harmonics while minimizing angular spread, the theorem gives quantitative rigidity for arbitrary measures, not just an exact quadrature rule or discrete extremizer. It controls concentration and the redistribution of mass explicitly, and a feasible shift family verifies that improving the transport power for fixed N is impossible. This is useful despite rapidly growing, non-optimal constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
