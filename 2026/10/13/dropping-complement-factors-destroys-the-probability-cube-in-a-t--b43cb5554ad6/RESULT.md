# Dropping complement factors destroys the probability cube in a tripartite replicator model
## Finding
The binary-population replicator construction in Su and Long implies complement factors that are later deleted. From
\[
\pi_g=x\pi_{gs}+(1-x)\pi_{gw},
\]
the paper's Eq. (7) satisfies
\[
\dot x=x(\pi_{gs}-\pi_g)=x(1-x)(\pi_{gs}-\pi_{gw}).
\]
Likewise, the victim coordinate has the factor \(y(1-y)\), and the paper's Eq. (17) explicitly writes \(z(1-z)\) for the risk-neutral new-media coordinate. Eqs. (19)–(21) are obtained by declaring the complement factors nonnegative and deleting them. That deletion is not dynamically valid at the boundary.

With the source's baseline values \(B_g=3\), \(C_g=2.5\), and \(C_{\mathrm{weak}}=1.5\), evaluate Eq. (19) at \((x,y,z)=(1,0,1)\). All terms multiplied by \(yz\) or \(1-z\) vanish, so
\[
\dot x=B_g-C_g+C_{\mathrm{weak}}=3-2.5+1.5=2.
\]
Hence a solution initialized at that probability-cube boundary has \(x(t)=1+2t+o(t)\), and therefore \(x(t)>1\) for all sufficiently small positive \(t\). The unreduced replicator equation instead has \(\dot x=0\) whenever \(x=1\).

Therefore the simplified drift used in Eqs. (19)–(24) does not globally define strategy-probability dynamics on \([0,1]^3\). Restoring the complement factors (or explicitly replacing the model by a different state-space dynamics) is necessary before boundary stability and probability-valued simulations can be interpreted as replicator dynamics.

## Assumptions and scope
The claim uses the payoff averaging and government replicator definition printed in Eqs. (4)–(7), the stated interpretation \(x,y,z\in[0,1]\) as strategy probabilities, the simplification statement preceding Eqs. (19)–(21), and the baseline parameter values in Table 3. It needs no assumption about the ambiguous typography of the later Brownian term: the deterministic drift already violates the state space when the stochastic perturbation is switched off. The claim is about boundary dynamics and forward invariance. It does not claim that every interior zero of the payoff-difference brackets moves when complement factors are restored.

## Proof
For any binary population with first-strategy frequency \(x\), payoffs \(u_1,u_2\), and average payoff \(\bar u=xu_1+(1-x)u_2\), the replicator definition gives
\[
\dot x=x(u_1-\bar u)=x(1-x)(u_1-u_2).
\]
Applying this identity to the source's government Eqs. (4)–(7) yields the missing factor \(1-x\) exactly. Applying it to Eqs. (8)–(11) yields \(y(1-y)\). For new media, Eq. (17) itself displays \(z(1-z)\). Nonnegativity of these factors in the interior permits some sign comparisons, but it does not permit deleting them from a differential equation because they vanish on the upper faces.

For the explicit witness, substitute \(x=1,y=0,z=1\) in Eq. (19). Its subsidy term contains \(yz=0\), and its fine term contains \(1-z=0\). The remaining coefficient is \(B_g-C_g+C_{\mathrm{weak}}\). Table 3 gives \(3-2.5+1.5=2\), so the vector field points strictly outward at the face \(x=1\). Continuity then gives \(x(t)=1+2t+o(t)\). In the unreduced replicator equation, the same point has the factor \(1-x=0\), hence zero normal component. This proves the state-space failure of the simplified system.

## Verification
The bundled checker verifies the binary-payoff identity symbolically and the exact baseline boundary value \(2\). The proof does not infer an infinite statement from numerical sampling: the boundary identity is algebraic, and one exact source-parameter point suffices to disprove forward invariance of the cube for Eqs. (19)–(21).

## Relationship to prior work
The motivating article itself supplies both sides of the comparison: its payoff averages and initial replicator definitions imply the complement factors, while its later simplification deletes them on the stated ground that they are nonnegative. A recent tripartite evolutionary-game paper in *Mathematics* retains the standard \(x(1-x)\), \(y(1-y)\), and \(z(1-z)\) factors in all three coordinates, and an earlier public-health tripartite model does the same. Those sources support the standard probability-preserving formulation but do not state the source-specific boundary counterexample above. published-finding corpus searches for the DOI, complement-factor deletion, boundary invariance, and the explicit equation context returned no record covering this correction.

## Limitations
The finding is source-specific. It does not determine all consequences of restoring the factors, does not reconstruct the paper's entire risk-adjusted stochastic model, and does not claim that all interior equilibria disappear. Interior payoff-difference zeros can coincide between the unreduced and reduced vector fields. The proved failure is global probability-cube invariance and the associated boundary dynamics of the simplified system.

## References
1. J. Su and J. Long, “Tripartite stochastic evolutionary game and its evolutionary stability under emergencies,” *Journal of Dynamics and Games*, early access 31 July 2026, DOI 10.3934/jdg.2026051.
2. “Tripartite Evolutionary Game Model and Stability Analysis for Collaborative Innovation in Traditional Energy Enterprises,” *Mathematics* 14 (2026), article 1968, DOI 10.3390/math14111968.
3. Z. Xu, “Tripartite Evolutionary Game Model for Public Health Emergencies,” *Discrete Dynamics in Nature and Society* (2021), article 6693597, DOI 10.1155/2021/6693597.
