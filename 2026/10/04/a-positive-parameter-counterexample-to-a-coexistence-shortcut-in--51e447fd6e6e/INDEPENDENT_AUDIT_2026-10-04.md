# Independent mathematical audit

## correctness

PASS

The publisher PDF was read through the coexistence derivation and Theorem 3.1. The source itself derives the admissible interval \((L_0,U)\) with \(L_0=\max\{0,L\}\), but its theorem statement uses the sign test at \(L\) and then states the weak-Allee shortcut. For the assigned positive parameter tuple, exact arithmetic gives \(C_1=21/10\), \(C_2=-1\), \(L=-11/10\), \(L_0=0\), \(U=9/10\), and \(f(u)=-u^2-u/5-341/100\). Hence \(f(u)<0\) for every \(u>0\), so there is no admissible positive coexistence root despite satisfying \(r>\beta_1\eta\), \(\gamma_1>\beta_2\), and \(\beta<C_1\). The source proof itself switches to \(f(L_0)f(U)<0\), confirming the precise endpoint mismatch.

## originality

PASS

The full relevant primary text was obtained and inspected. It contains the inconsistency targeted by the finding: equation (3.3) defines \(L_0=\max\{0,L\}\); Theorem 3.1(a) states its premise using \(f(L)f(U)<0\) and says the weak-Allee inequalities imply it; the proof instead uses \(f(L_0)f(U)<0\). Fresh Resultary searches found no published correction or exact counterexample for this model. The explicit all-positive parameter witness is therefore original to the best of current evidence.

## value

PASS

Positive coexistence is a prerequisite for the source's subsequent stability and bifurcation analysis. An exact positive-parameter counterexample shows that the printed ecological shortcut can assert a coexistence equilibrium that does not exist and identifies the precise mathematical correction: use the actual admissible lower endpoint \(L_0\). That is a substantive correction, not a cosmetic typo.

The dated certificate retains the supplied scientific assessment, sources and limitations.
