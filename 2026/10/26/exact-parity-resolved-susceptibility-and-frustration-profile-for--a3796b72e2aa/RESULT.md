# Exact parity-resolved susceptibility and frustration profile for the anti-voter Möbius ladder

## Finding
For the uniform anti-voter process on the Möbius ladder with \(2m\) spins and \(m\ge2\), write \(S_m=\sum_i\sigma_i\) for total spin. If \(m\) is odd, every stationary law has \(S_m=0\). If \(m\) is even, the unique stationary law satisfies
\[
\operatorname{Var}(S_m)=\frac{8m}{3m+2\sqrt3\,(1+q^m)/(1-q^m)},\qquad q=2-\sqrt3.
\]
On the even subsequence the variance increases strictly to \(8/3\); on the odd subsequence it vanishes identically. The even-case stationary correlation satisfies, uniformly for integers \(0\le d\le2m\),
\[
\mathbb E(\sigma_0\sigma_d)=(-1)^d\left(1-\frac{2\min(d,2m-d)}m\right)+O(m^{-1}).
\]
The expected numbers of equal-spin cycle edges and antipodal rungs converge respectively to \(4-2/\sqrt3\) and \(2/\sqrt3\). Thus the expected total number of frustrating edges approaches exactly four although the graph has \(3m\) edges.

## Assumptions and scope
Let \(G_m\) have vertices \(\mathbb Z/(2m)\), cycle edges \(\{i,i+1\}\) and rungs \(\{i,i+m\}\), with arithmetic modulo \(2m\). For \(m=2\), this is \(K_4\), and all three neighbors of every vertex are distinct. A configuration is \(\sigma\in\{-1,+1\}^{2m}\). Independently at rate one each vertex replaces its spin by minus that of one uniformly chosen neighbor. All observables refer to stationary probability measures on the finite continuous-time chain, not an infinite-volume Gibbs measure. Write \(C_d=\mathbb E(\sigma_i\sigma_{i+d})\); when \(m\) is even, this does not depend on \(i\) by stationary uniqueness and translation invariance.

## Proof
**Parity and stationarity.** The graph is bipartite exactly when \(m\) is odd. For odd \(m\), the two alternating configurations are absorbing. Under a gauge transformation reversing one partition, the chain becomes the ordinary finite voter model on a connected graph, whose only recurrent classes are the two consensus configurations. Thus any stationary law is supported on the two checkerboards and has \(S_m=0\). When \(m\) is even, the graph contains an odd cycle (the \(m\)-cycle comprising a rim path and one rung), so the signed anti-voter system is frustrated. The standard finite signed-voter duality, or elementary dual ancestral walks with odd closed loops, implies the Markov chain is ergodic; global spin reversal forces each stationary mean to vanish. Independently, the finite matrix test in the verification script confirms this uniqueness and the observable for small \(m\).

**Closed two-point equations.** Stationarity of the generator acting on \(\sigma_i\sigma_j\), for \(i\ne j\), yields
\[
3C_d+C_{d-1}+C_{d+1}+C_{d+m}=0\qquad(d\not\equiv0\pmod{2m}),\qquad C_0=1.
\]
Define \(A=3I+T+T^{-1}+T^m\) on periodic sequences of length \(2m\), with \(Tf(d)=f(d+1)\). Its Fourier eigenvalues are \(a_k=3+2\cos(\pi k/m)+(-1)^k\). For even \(m\), each \(a_k>0\): even \(k\) have eigenvalues at least two, while odd \(k\) have eigenvalues \(2+2\cos(\pi k/m)>0\) because \(k=m\) is then even. If \(G=A^{-1}\delta_0\), uniqueness of the correlation boundary-value problem gives \(C_d=G_d/G_0\), where
\[
G_d=\frac1{2m}\sum_{k=0}^{2m-1}\frac{e^{\pi i k d/m}}{3+2\cos(\pi k/m)+(-1)^k}.
\]
Since the constant Fourier eigenvalue is six, \(\sum_dG_d=1/6\). The spin-flip symmetry therefore gives
\[
\operatorname{Var}(S_m)=2m\sum_d C_d=\frac{m}{3G_0}.
\]

**Exact Fourier summation.** Split the Fourier indices into even and odd. For even \(m\), put \(q=2-\sqrt3\) and \(\delta=\min(d,2m-d)\). The odd-index Green contribution, the inverse of the antiperiodic one-dimensional discrete Laplacian, is exactly
\[
G_d^{\mathrm{odd}}=(-1)^d\left(\frac m8-\frac\delta4\right).
\]
Indeed it satisfies the second-difference equation away from the origin, is antiperiodic under translation by \(m\), and has the source jump demanded by the odd-frequency Fourier projection. The even-index contribution is the period-\(m\) massive Green function
\[
G_d^{\mathrm{even}}=\frac{(-q)^{\delta}+(-q)^{m-\delta}}{4\sqrt3(1-q^m)}.
\]
This follows by solving the recurrence \(4h_d+2h_{d-1}+2h_{d+1}=\delta_{0d}\) on the period-\(m\) ring, using characteristic roots \(-q\) and \(-q^{-1}\), and the factor \(1/2\) from retaining half the Fourier modes. In particular,
\[
G_0=\frac m8+\frac{1+q^m}{4\sqrt3(1-q^m)}.
\]
Substitution into \(m/(3G_0)\) proves the variance formula. For \(m\) even, \(q^m\) decreases, and so \(m^{-1}(1+q^m)/(1-q^m)\) strictly decreases; dividing the variance formula by \(m\) proves monotonicity and the limiting value \(8/3\).

**Macroscopic correlations and frustration.** The even-mode Green term is uniformly bounded independently of \(m,d\); meanwhile \(G_0=m/8+O(1)\). Dividing the odd-mode expression by \(G_0\) proves the displayed uniform tent-shaped correlation. More explicitly, at separation one,
\[
G_1=-m/8+1/2-2a_m,\qquad a_m=\frac{1+q^m}{4\sqrt3(1-q^m)},
\]
and at antipodal separation \(G_m=-m/8+a_m\). There are \(2m\) rim edges and \(m\) rungs. The expected equal-spin counts are therefore \(m(1+C_1)\) and \((m/2)(1+C_m)\). Direct substitution yields limits \(4-2/\sqrt3\) and \(2/\sqrt3\).

## Verification
The included `verify_antivoter_ladder.py` constructs the finite continuous-time generator directly on all configurations for \(m=2,4,6\), solves for stationarity, and compares the magnetization variance with the closed formula. It separately diagonalizes the circulant covariance operator numerically for \(m=2,4,6,8,10,100\). All tests passed with the stated tolerances. These finite checks are independent corroboration; the proof of arbitrary \(m\) is the Fourier and duality argument above. Run `python verify_antivoter_ladder.py` with NumPy and SciPy installed.

## Relationship to prior work
Aldous and Fill's anti-voter chapter provides the general dual random-walk formulation for stationary pair correlations and magnetization variance on finite graphs. Maillard and Mountford establish general signed-voter ergodic theory. The duality and the closed covariance recurrence are accordingly not claimed as new. The family-specific evaluated formula, the alternating zero-versus-nonzero variance, the uniform macroscopic correlation shape, and the finite frustration-edge limits require the explicit antiperiodic/massive Green-function summation performed here. The general duality does not state these evaluated Möbius-ladder expressions. A broader spectral theorem could still subsume these formulas as a specialization; historical priority has not been exhaustively established.

## Limitations
The statement assumes degree-three unweighted Möbius ladders, continuous-time uniform negative-copying dynamics, and stationary statistics. It does not give a transient law, mixing-time estimate, arbitrary signed graph formula beyond known dualities, or independent audit. The odd/even difference is particular to the rung connection of this graph family. The general theorem on signed-voter ergodicity is prior work.

## References
1. D. Aldous and J. Fill, *Reversible Markov Chains and Random Walks on Graphs*, chapter 14.4, “The antivoter model” (online draft, 1994), https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch14.S4.html .
2. G. Maillard and T. Mountford, “Ergodic behaviour of ‘signed voter models’,” *Annales de l'Institut Henri Poincaré, Probabilités et Statistiques* 49 (2013), DOI 10.1214/12-AIHP511; associated public preprint arXiv:0709.3468 (2007).
3. N. Gantert, M. Löwe and J. Steif, “The voter model with anti-voter bonds,” *Annales de l'Institut Henri Poincaré, Probabilités et Statistiques* 41 (2005), DOI 10.1016/j.anihpb.2004.03.007.
