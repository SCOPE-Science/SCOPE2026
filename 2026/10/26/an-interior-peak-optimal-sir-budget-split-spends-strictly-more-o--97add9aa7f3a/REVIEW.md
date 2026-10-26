# Scientific review

## Correctness — PASS
For \(S_0,I_0>0\), the final-size function has exactly one physical root and strictly positive derivative with the reproduction ratio. The exact identity \(Q'/Q=(g_*-yh)/(1-y)\), with \(0<y<1\), gives a global sign after the reproduction-ratio optimum. The uniform large-transmission bound and the rational-exponential example prove the all-treatment result without numerical minimization. The peak comparison is explicitly limited to initially growing epidemics for every allocation; the flat-peak regime is not misclassified. `check.py` corroborates the formula with 522 checks; analytic arguments, rather than the finite grid, establish global conclusions.

## Originality — PASS (provisional priority)
The exact two-program response functions and the peak-optimal split are in Maity et al. (arXiv:2302.00960v1), notably Section 3.2 and Appendix B. The present claim changes the objective to total infectious person-time under a budget that changes recovery; Maity's peak formula alone does not impose the optimizer ordering or the high-transmission boundary policy. Sereno et al. (arXiv:2111.05652) give the known area-under-infections/final-size relationship with fixed time normalization, but do not optimize a constant split that changes recovery. Bolzoni et al. (arXiv:1706.04447) treat time-optimal and unconstrained single-control strategies rather than this simultaneous static two-control budget. Related optimization theory and unpublished formulations may subsume part of this observation. Priority is not independently certified.

## Value — PASS
The two measures correspond to distinct epidemic resource questions: maximal simultaneous infections versus integrated infectious exposure or bed-days under a model-specific interpretation. The strict comparative statics hold across all positive initial states and positive intervention coefficients, while the high-transmission theorem and a fully bounded example demonstrate a complete shift from an interior peak-optimal mix to all-treatment for integrated burden. The value rests on the structured objective divergence, not on rederiving the classical SIR final-size formula.

## Residual limitations
No time-dependent controls, age structure, susceptible replenishment, stochastic extinction, financial utility, or real-world optimal treatment recommendation are established. The total person-time minimizer need not be unique in the general parameter regime, and prior-art coverage beyond the inspected papers remains possible.

Self-review: passed. Independent audit: not yet performed.
