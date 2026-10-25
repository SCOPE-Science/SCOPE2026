# Scientific review: robust Hamiltonian-cycle equilibria

## Correctness — PASS

From the explicitly stated independent turnout semantics, the exact path formula gives a position-free payoff of \(\tau(1-Q_S)\) and distance penalty at most \(\Delta q_{\max}\). A full-cycle deviation necessarily loses at least \(\tau p_{\min}Q/q_{\max}\), whereas every non-full functional graph admits an improving cycle-to-cycle or cycle-to-in-tree redirection with the same minimum position-free gain. The strict diameter bound makes the sign robust. The three-voter condition follows by enumerating every unilateral action; the two-voter minimality statement is checked directly. The embedded standard-library checker passed 8,027 exact-rational assertions; it is a finite corroboration, not the proof.

## Originality — PASS, subject to historical-priority risk

Brill, Colley, George, Lisowski, Papasotiropoulos and Schmidt-Kraepelin, *Cycles in Liquid Democracy: A Game-Theoretic Justification* (COMSOC 2025 and arXiv:2607.12610), define the probabilistic game and prove structural cycle properties (Theorems 5 and 8) and path-level selection (Theorem 14). The inspected statements do not imply the present global if-and-only-if equilibrium classification, \((n-1)!\) count, heterogeneous probability robustness bound, or exact three-voter failure boundary. Classical functional digraph theory and independent-turnout products are credited as tools. Search comparisons include stochastic voting equilibria, delegation cycles, Hamiltonian cycles, spanning-cycle equilibria and aliases. Full 2025 proceedings manuscript and expanded 2026 article were read in relevant model, theorem and appendix sections. Related deterministic delegation and temporal delegation abstracts do not give a direct stochastic implication; they are residual historical search risks.

## Mathematical value — PASS

This is a complete equilibrium-structure theorem on a natural, explicitly quantified robustness region of the stochastic default-delegation game, valid with heterogeneous turnout; it rules out *all* disconnected or nonspanning equilibria and enumerates the survivors. The sharp three-voter counter-regime shows why mutual acceptability alone cannot replace the small-diameter hypothesis and gives an exact nonspanning-equilibrium boundary. The statement is stronger than graph-theoretic cycle existence and informs stability questions for default delegation. The general diameter constant is not claimed optimal, and independent audit remains outstanding.

## Limitations and closest literature

The 2025/2026 source gives weaker cycle/component restrictions; no absolute priority guarantee is possible. The three-voter threshold is exact for the nominated profile only; it does not classify all profiles. Other earlier formulations may exist. The theorem excludes restricted delegate menus, correlated turnout and variable tolerances.

Self-review: passed. Independent audit: not yet performed.
