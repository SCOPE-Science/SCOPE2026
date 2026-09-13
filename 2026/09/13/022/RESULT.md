# Disproof of the T-uniform 1/N N-player to master limit (d = 2)

## Context

The target asks whether the symmetric N-player finite-state mean-field game
value converges to the master-equation solution with a constant C depending
only on d and the data but independent of both N >= 2 and T >= 1:

  sup_{t in [0,T]} |V^{N,1}(t,x,m^N) - U(t,x,m^N)| <= C/N.

Classical finite-state results (Cecchin-Pelino, Gomes-Mohr-Souza,
Cardaliaguet-Delarue-Lasry-Lions) prove O(1/N) convergence at each fixed T
with constants that grow in T. Whether the constant can be chosen uniform in
T >= 1 under Lasry-Lions monotonicity was the open two-sided question. This
record resolves it negatively with an explicit fixed-data counterexample
family in which the horizon T grows at fixed N = 2.

## Definitions

- States {1,2}, d = 2, simplex S_2 = {(m_1,m_2)}.
- Horizon [0,T], arbitrary T >= 1.
- Control: none. Each player jumps to the other state with constant rate 1.
  The rate set is the singleton {1} (compact, N-independent); running control
  cost is 0. The Hamiltonian is z -> z on the jump difference, convex and
  globally Lipschitz with constant 1.
- Couplings (N-independent): F(1,m) = m_1, F(2,m) = m_2 (i.e. F(x,m) = m_x),
  G = 0. F is 1-Lipschitz and strictly Lasry-Lions monotone:
  sum_x (F(x,m)-F(x,m'))(m_x-m'_x) = (m_1-m_1')^2+(m_2-m_2')^2 >= 0.
- V^{N,1}(t,x,m^N): expected cost of distinguished player 1 from state x and
  empirical distribution m^N under the Nash profile.
- U(t,x,m): classical solution of the finite-state master equation.

## Result

There is no finite C(d, data) independent of N >= 2 and T >= 1 satisfying the
T-uniform 1/N bound. Explicitly, with the fixed data above, N = 2, player 1
starting in state 1 and empirical m^N = (1/2,1/2):

  N * sup_{t in [0,T]} |V^{N,1}(t,1,m^N) - U(t,1,m^N)|
      = T/2 - (1 - e^{-4T})/8 >= T/2 - 1/8, for all T >= 1.

Hence for every candidate C, T = 2C+1 gives scaled error > C. The family has
fixed data, fixed N = 2, T -> infinity, satisfying the target's
growing-N-or-T clause.

## Proof / evidence

Master solution. With tau = T - t, delta = m_1 - 1/2,
phi(tau) = (1 - e^{-4 tau})/4:

  U(t,1,m) = tau/2 + delta phi(tau),
  U(t,2,m) = tau/2 - delta phi(tau).

This is smooth on [0,T] x S_2 with U(T,.,.) = 0. It satisfies the
uncontrolled backward master equation

  d_t U(x) + [U(3-x) - U(x)] + (1 - 2 m_1) d_{m_1} U(x) + F(x,m) = 0,

identically: e.g. for x = 1, d_t U_1 = -1/2 - delta e^{-4 tau},
U_2 - U_1 = -delta(1-e^{-4 tau})/2, b d_{m_1} U_1 = -delta(1-e^{-4 tau})/2,
F = 1/2 + delta, summing to 0 (x = 2 symmetric). Sympy certifies both
residuals are exactly 0.

Nash property. The singleton rate set admits exactly one strategy profile,
trivially a symmetric Nash equilibrium; V^{N,1} is therefore the unique
hence every symmetric Nash value.

Exact gap. The N chains are independent rate-1 two-state chains. With
p_1 the tagged-chain probability of state 1 and E[m^N_1] the mean empirical
frequency, independence gives E[1_{X^1=1} m^N_1] = p_1 E[m^N_1]
+ p_1(1-p_1)/N and the state-2 analogue, while E[m^N_1] equals the
deterministic mean-field flow m_1^{det}. The first terms reproduce the master
integrand, leaving integrand gap (2/N) p_1(1-p_1) >= 0. With
p_1(u) = (1+e^{-2u})/2, at N = 2 the gap is (1-e^{-4u})/4, integrating from
0 to T to V - U = T/4 - (1-e^{-4T})/16. Nonnegativity makes the t = 0 value a
lower bound for sup_t |V - U|, giving the headline. At fixed T the same
formula is O(1/N), consistent with classical fixed-horizon theory; only
T-uniformity fails via accumulated variance integral of Var(m^N_1).

Independent verification. output/artifacts/verify_disproof.py passes:
symbolic residuals 0, closed-form growth table (exceeds C = 10 at T = 21),
and Monte Carlo (N = 2, T = 3, 400k paths): V_mc = 2.18765 vs exact 2.18750.

## Limitations

The disproof uses a degenerate uncontrolled example with singleton rates, so
it refutes only the uniform-in-T claim as stated and leaves the classical
fixed-T 1/N bound intact. It is restricted to d = 2 and the stated couplings;
controlled settings and other couplings were not investigated.

## Reproducibility

Run `python3 output/artifacts/verify_disproof.py` (requires sympy, numpy).
It checks the master PDE symbolically, the closed-form scaled error, and the
Monte Carlo confirmation with seed 0.

## References

- Cecchin, Pelino, arXiv:1707.01819: finite-state N-player to MFG convergence
  via the master equation at fixed horizon.
- Cohen, Zell, arXiv:2204.05373: finite-state ergodic/discounted master
  equations (stationary infinite-horizon regime).
- Gomes, Mohr, Souza (2013): continuous-time finite-state MFG convergence.
- Bertucci, Cecchin (2024): discrete-to-continuous state master equations.
- Cardaliaguet, Delarue, Lasry, Lions (2019): master equation and fixed-T
  convergence with T-dependent constants.
