# Exact heterogeneous action-budget region for finite actual-effectivity representations

## Finding
Fix an integer \(k\ge2\), a positive integer \(r\), and a vector of positive integer action-copy budgets \(\mathbf b=(b_1,\ldots,b_k)\). The following statements are equivalent.

**Universal realizability.** Every finite \(k\)-agent actual-effectivity neighbourhood frame satisfying Ciardelli's three game-representability conditions, at every world with exactly \(r\) reachable outcomes, has a deterministic concurrent-game realization on the same world set using precisely \(b_i\) distinct actions for **each** neighbourhood of agent \(i\). Different worlds may use different feasible budget vectors.

**Slice-capacity condition.** For every agent \(i\),
\[
\prod_{j\ne i}b_j\ge r.
\]
Equivalently, the exact universal action-copy budget region is
\[
\boxed{\prod_{i=1}^{k}b_i\,/\,\max_i b_i\ge r.}
\]
This is a complete **heterogeneous** budget tradeoff, not merely a bound on the maximum or a symmetric common copy number.

For example, with three agents and twelve reachable outcomes, the vector \((3,4,4)\) works universally: its complementary products are \(16,12,12\). The previously established symmetric construction instead uses \((4,4,4)\), and the vector \((3,4,4)\) reduces the first agent's actions for every one of its neighbourhoods.

## Assumptions and scope
Let \(W\) be a nonempty finite set of worlds and let the agents be indexed by \(\{1,\ldots,k\}\). At each world \(w\), each \(\Sigma_i(w)\) is a nonempty finite **set of nonempty subsets** of \(W\), satisfying:

1. **Common reachable range:** all \(\bigcup\Sigma_i(w)\) equal the same nonempty set \(R_w\subseteq W\).
2. **Independence:** every choice \(s_i\in\Sigma_i(w)\) has \(\bigcap_i s_i\ne\varnothing\).

Write \(r_w=|R_w|\). A deterministic concurrent game provides a nonempty finite action set \(\operatorname{Act}_i(w)\) for each agent and a single outcome \(o_w(t_1,\ldots,t_k)\in W\) for every joint action profile. The actual-effectivity neighbourhood of an action \(a\in\operatorname{Act}_i(w)\) is exactly the set of its outcomes across all completions of that action. A representation requires the resulting **set** of neighbourhoods to equal \(\Sigma_i(w)\) for each agent. We require precisely \(b_i\) distinct actions realizing each prescribed neighbourhood, so \(|\operatorname{Act}_i(w)|=b_i|\Sigma_i(w)|\).

The iff above has a universal quantifier over **all** admissible frames with the given range size. The capacity inequalities are not claimed necessary for a *particular* frame with several neighbourhoods or special structure.

## Proof
All constructions are local, so fix a world and abbreviate \(R=R_w\), \(|R|=r\), and \(\Sigma_i=\Sigma_i(w)\).

**Mixed-radix hyperplane lemma.** Let \(b_1,\ldots,b_k\ge1\). Pick a pivot \(p\) with \(b_p=\max_i b_i\) and form
\[
C=\prod_{j\ne p}\mathbb Z/b_j\mathbb Z,\qquad
H(t_1,\ldots,t_k)=\big((t_j-t_p)\bmod b_j\big)_{j\ne p}.
\]
The map \(H:\prod_i\{0,\ldots,b_i-1\}\to C\) is surjective on **every slice obtained by fixing one input coordinate**. To hit a requested \(d\in C\) when the pivot label \(t_p\) is fixed, set \(t_j\equiv d_j+t_p\pmod {b_j}\) for all other indices. If instead the label \(t_i\) is fixed with \(i\ne p\), choose \(t_p\in\{0,\ldots,b_p-1\}\) satisfying \(t_p\equiv t_i-d_i\pmod {b_i}\). This is possible because \(b_p\ge b_i\), so a complete system of residues modulo \(b_i\) appears among the first \(b_p\) integers. For the remaining indices choose \(t_j\equiv d_j+t_p\pmod{b_j}\). Hence the stated slice-surjectivity holds. Finally,
\[
|C|=\frac{\prod_i b_i}{\max_i b_i}=\min_i\prod_{j\ne i}b_j.
\]

**Sufficiency.** Suppose all complementary products are at least \(r\). By the lemma, \(|C|\ge r\); choose a surjection \(\pi:C\twoheadrightarrow R\). Give agent \(i\) the set of actions \(\Sigma_i\times\{0,\ldots,b_i-1\}\). For each tuple of chosen neighbourhoods \(\mathbf s=(s_1,\ldots,s_k)\), independence ensures the nonempty intersection \(I=\bigcap_i s_i\). Fix once and for all a fallback \(m(\mathbf s)\in I\), for example the least point in a fixed ordering of \(W\). For a joint action profile \(((s_1,t_1),\ldots,(s_k,t_k))\), set \(z=\pi(H(t_1,\ldots,t_k))\), and define the outcome to be \(z\) if \(z\in I\), otherwise \(m(\mathbf s)\).

Fix an action \((s_i,t_i)\) of agent \(i\). Every resulting outcome belongs to \(I\subseteq s_i\), so the action's outcome set is included in \(s_i\). Conversely, for any \(u\in s_i\), the common-range condition implies that each other agent \(j\) has some \(s_j\in\Sigma_j\) with \(u\in s_j\). The slice-surjectivity of \(H\) and surjectivity of \(\pi\) allow the other label coordinates to be selected, keeping \(t_i\) fixed, so that \(\pi(H(t))=u\). Then \(u\in I\), the first branch applies, and the joint outcome is \(u\). Thus the action's outcome set is exactly \(s_i\). This holds for every action, and the constructed action sets have exactly the asserted multiplicities. Perform the construction independently at every world to obtain a full game realization.

**Necessity for universal realizability.** Fix a set \(W=R\) with \(|R|=r\), and at **every** world stipulate \(\Sigma_i(w)=\{R\}\) for all agents. This is an admissible frame. In any representation using exactly \(b_i\) actions for agent \(i\), every action of agent \(i\) must realize all of \(R\), since it is the only prescribed neighbourhood. A fixed action of agent \(i\) has only \(\prod_{j\ne i}b_j\) completions, each yielding one deterministic outcome. Its outcome set can therefore have at most that many elements. To equal \(R\) requires \(\prod_{j\ne i}b_j\ge r\) for every \(i\). This proves necessity and the equivalence.

## Verification
The standalone standard-library script `verify.py` directly constructs the outcome tables and recomputes actual-effectivity neighbourhoods, without relying on the algebraic proof. It checks mixed-modulus slice surjectivity exhaustively for \(2\le k\le5\) and \(1\le b_i\le4\); it also reconstructs randomly sampled finite deterministic games, applies the budget construction, and compares resulting neighbourhood families exactly. The successful run reported `VERIFY_OK slices=15920 games=1152 action_profiles=305424 budgets=21760 strict_example=(3,4,4)`. All tested capacities and the strict asymmetric example agree with the theorem. Only the preceding argument proves the arbitrary finite-parameter assertion.

To reproduce: run `python3 verify.py` using Python 3 and its standard library. No input files or network are required.

## Relationship to prior work
Ciardelli's *Inquisitive Action Logic*, Theorem 2.2, proves qualitative representability under the two frame conditions above together with nonemptiness of each neighbourhood family. Its displayed construction pairs each prescribed neighbourhood with a state-sized auxiliary action label. It does not address the exact region of possibly different per-agent multiplicities.

The public finding *Sharp local-range compression for actual-effectivity representations* replaces the state-sized label by the local outcome-range size \(r\) and proves two-agent worst-case optimality. The public finding *Sharp root-size action realization for finite actual-effectivity frames* gives an optimal **uniform** copy number \(\lceil r^{1/(k-1)}\rceil\), using equal moduli across all agents. Its lower-bound argument records necessary complementary-product inequalities for a one-neighbourhood example, but does not provide a sufficient construction for **arbitrary unequal** vectors, or state a complete Pareto feasibility characterization. The mixed-modulus slice lemma supplies the additional nontrivial sufficiency step. Setting all \(b_i\) equal recovers the earlier theorem, whereas \((3,4,4)\) for twelve outcomes is genuinely outside its equal-budget construction.

Research on Latin hypercubes provides background for arrays with coordinate-wise coverage properties. We do not claim originality for the abstract combinatorial idea of such arrays; the contribution here is its exact match to the universal heterogeneous resource constraint for deterministic actual-effectivity representations.

## Limitations
The bound is exact **universally**, not the optimal resource vector for an individual frame. It assumes finite deterministic concurrent games, at least two agents, and that the actions are allocated in equal counts within each agent's neighbourhood class. It does not optimize total action count among representations allowing arbitrary heterogeneous repetitions within one agent, nor address nondeterministic games or coalitional powers. Equivalent formulations under hypergraph decompositions, mixed-level arrays, or older effectivity literature may exist; a literature search is not a proof of absolute priority.

## References
1. Ivano Ciardelli, *Inquisitive Action Logic*, arXiv:2606.31866, first posted 2026-06-30, Theorem 2.2.
2. *Sharp local-range compression for actual-effectivity representations*, public published-finding corpus record `4bce89f50bf5`, 2026-10-04.
3. *Sharp root-size action realization for finite actual-effectivity frames*, public published-finding corpus record `114a0e0912e6`, 2026-10-04.
4. Valentin Goranko and Wojciech Jamroga, *State and path coalition effectivity models of concurrent multi-player games*, Autonomous Agents and Multi-Agent Systems 30 (2016), DOI:10.1007/s10458-015-9294-4 (coalitional context).
