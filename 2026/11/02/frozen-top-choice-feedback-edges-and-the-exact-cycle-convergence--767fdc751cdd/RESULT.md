# Frozen top-choice feedback edges and the exact cycle convergence dichotomy

## Finding

**Theorem (a feedback-edge sufficient condition, exact on cycles).** Let \(G=(V,E)\) be any finite, simple, undirected acceptability graph with \(n=|V|\ge 1\). Each agent strictly ranks all adjacent agents above remaining unmatched. A matching is any set of vertex-disjoint acceptable edges. A blocking-pair move forms an edge \(\{u,v\}\notin M\) when both its endpoints strictly prefer each other to their current partners, simultaneously dissolving their previous matches.

Suppose \(F\subseteq E\) is a *feedback edge set* (\(G-F\) is a forest) and **each edge in \(F\) joins agents who rank one another first**. Then every sequence of blocking-pair moves starting at any matching is finite. More explicitly, writing \(f=|F|\), its length is at most
\[
(f+1)\left\lfloor\frac{n^3}{8}\right\rfloor+f.
\]

For the simple cycle \(C_n\), \(n\ge3\), this sufficient condition is **necessary for universal termination**: a blocking-pair improvement cycle exists if and only if every vertex prefers its clockwise neighbor to its counterclockwise neighbor, or every vertex has the reverse preference. Hence exactly two of the \(2^n\) strict local preference profiles are nonconvergent. Under independent uniformly random local rankings, the exact convergence probability is \(1-2^{1-n}\).

As a secondary consequence (not asserted as a new static-stability obstruction), a stable matching exists for every preference profile on an even cycle, while on an odd cycle it exists exactly for the \(2^n-2\) noncoherent profiles.

## Assumptions and scope

All preferences are strict, complete on each vertex's neighbors, and put being unmatched last. There are no transfers, capacities greater than one, or concurrent pair formation. Each move chooses one blocking edge and releases the former partners of its two endpoints, if any; the released partners become unmatched. No fairness or randomness assumption is made about move selection. **Convergence** means acyclicity of the finite directed graph of *all* matchings and blocking-pair transitions, equivalently termination of every infinite-attempt move sequence.

The polynomial bound uses the published forest-dynamics theorem of Fanelli and Moscardelli, whose Theorem 4 proves at most \(s^3/8\) blocking-pair moves on any forest with \(s\) vertices. The qualitative acyclicity argument below also supplies an independent direct derivation of the needed forest fact. The cycle claim ranges over **all** integers \(n\ge3\), including odd and even cycles.

## Proof

**Lemma 1 (forest obstruction to periodic blocking).** No directed cycle of blocking-pair moves can occur on a forest. Suppose a periodic orbit exists and repeat its finite sequence indefinitely. Some step breaks an existing matched pair by one member voluntarily joining a more preferred agent: otherwise the matching size could only grow, so an orbit could not return. Call such an event a *departure* \(x\to y\), meaning that \(x\) leaves its current partner \(y\) for a partner strictly preferred to \(y\).

Fix a departure \(x\to y\). Immediately afterward, \(x\)'s partner is strictly preferred to \(y\). Because the trajectory is periodic, \(x\) must again become matched with \(y\) before its next departure from \(y\). Somewhere in between, \(x\) must first lose a partner \(z\) whom \(x\) prefers to \(y\). This loss cannot be a voluntary switch by \(x\), since every voluntary switch strictly improves its partner. It must occur when \(z\) voluntarily leaves \(x\), giving another departure \(z\to x\). Since \(z\) is preferred by \(x\) to \(y\), we have \(z\ne y\). Repeating this implication among departures in the periodic orbit constructs an infinite nonbacktracking walk \(y,x,z,\ldots\) in the acceptability graph. Every nonbacktracking walk in a finite forest is finite, contradiction.

**Lemma 2 (frozen feedback edges).** If \(u\) and \(v\) rank one another first, then after they become partners neither can participate in a blocking-pair move. Therefore an edge \(e=\{u,v\}\) with this property can be formed at most once and is never destroyed. All feedback edges in \(F\) have this property. Partition any improvement trajectory into maximal consecutive stages containing no formation of a new edge in \(F\). During a stage, already-formed edges in \(F\) and their endpoints are frozen, and no other edge of \(F\) occurs in a matching or in a move. On the remaining vertices, every move therefore belongs to the forest \(G-F\). Lemma 1 forbids a periodic stage, proving termination because at most \(f\) stages can be separated by new feedback-edge formations.

For the quantitative bound, each forest stage has at most \(\lfloor n^3/8\rfloor\) moves, by Theorem 4 and its move-count corollary in Fanelli--Moscardelli (all surviving forests have at most \(n\) vertices). There are at most \(f+1\) stages and at most \(f\) formation moves. This proves the displayed upper bound.

**Lemma 3 (the two-cycle orientation dichotomy).** Label the vertices of \(C_n\) by \(0,\ldots,n-1\) modulo \(n\). Let \(s_i=+\) when vertex \(i\) prefers \(i+1\), and \(s_i=-\) when it prefers \(i-1\). The edge \(\{i,i+1\}\) joins mutual first choices exactly when \(s_i=+\) and \(s_{i+1}=-\). Any nonconstant cyclic binary word contains a \(+\) to \(-\) transition, so it has such an edge. Deleting that single edge of \(C_n\) leaves a path, and Lemma 2 yields convergence.

If all \(s_i=+\), let \(M_i=\{\{i,i+1\}\}\) be the matching with just one edge. The pair \(\{i+1,i+2\}\) blocks \(M_i\): vertex \(i+1\) prefers \(i+2\) to its partner \(i\), and vertex \(i+2\) is unmatched. Its formation produces \(M_{i+1}\). Thus \(M_0\to M_1\to\cdots\to M_{n-1}\to M_0\) is a strict improving cycle, valid also for \(n=3\). If all \(s_i=-\), the analogous move is \(M_i\to M_{i-1}\). These are precisely the two nonconvergent local preference assignments. Counting independent binary choices proves the probability formula.

**Static-stability consequence.** In the noncoherent cases, termination in a finite state space implies a terminal matching, which is stable. For even \(n\) under a coherent orientation, either alternating perfect matching is stable: on every unchosen edge one endpoint already has its first-choice partner. For odd \(n\), any matching leaves a vertex \(i\) unmatched. Its neighbor whose first choice is \(i\) is either unmatched or matched to its other (less preferred) neighbor; the pair blocks. Therefore the two coherent odd-cycle profiles admit no stable matching. This completes the proof.

## Verification

Run `python3 verify_cycles.py` with Python 3 and no third-party dependencies. It enumerates all strict binary local preference profiles for every \(3\le n\le10\), all legal matchings, and all improving transitions. A three-color depth-first search checks acyclicity, while checking terminal matchings validates the parity-dependent stability statement. Direct one-edge transition tests verify the explicit \(n\)-step countercycles. The executed check returned:

`VERIFY_OK profiles=2040 cycle_profiles=16 stable_profiles=2032 no_stable_profiles=8 directed_moves=824616`

This finite check does **not** establish the arbitrary-\(n\) theorem or the general feedback-edge condition; those follow from the proof above.

## Relationship to prior work

Fanelli and Moscardelli, *Approximately Stable Matching* (ECAI 2025; publisher's first verified online posting August 25, 2026), define these blocking-pair dynamics. Their Theorem 4 proves unconditional convergence on forest acceptability graphs, while Figure 1 gives a four-vertex cycle exhibiting nonconvergence. The theorem here gives a sufficient feedback-edge condition beyond forests, an **if-and-only-if classification for every simple cycle**, and a corresponding exact prevalence law. It does not claim the published four-vertex obstruction as new. Bredereck, Chen, Finnendahl, and Niedermeier (2020) analyze structurally restricted stable-roommates existence and explicitly use an odd directed top-choice cycle as a nonexistence obstruction; that static observation is acknowledged, while arbitrary-move convergence is the main distinction here. Diamantoudi, Miyagawa, and Xue (2004) establish existence of some path to stability when stable matchings exist, which is weaker than termination of every possible improvement path.

## Limitations

The result requires strict rankings, an undirected simple acceptability graph, and pairwise blocking moves. The feedback-edge condition is only **sufficient** on general graphs; the exact necessity statement applies only to a single simple cycle. The move-count bound is conservative and not claimed sharp. The randomized corollary assumes independent uniform preferences, not a population model. An alternative terminology or unindexed characterization of these dynamics may exist, and independent scientific validation remains to be performed.

## References

1. Angelo Fanelli and Luca Moscardelli, *Approximately Stable Matching*, ECAI 2025 proceedings, DOI: 10.3233/FAIA251234. Publicly available complete HTML at https://journals.sagepub.com/doi/10.3233/FAIA251234; publisher records first online publication as 2026-08-25. Theorem 4, Figure 1, Section 5.
2. Robert Bredereck, Jiehua Chen, Ugo Paavo Finnendahl, and Rolf Niedermeier, *Stable roommates with narcissistic, single-peaked, and single-crossing preferences*, Autonomous Agents and Multi-Agent Systems 34 (2020), article 53, DOI: 10.1007/s10458-020-09470-x; discussion of cyclic preferences in Proposition 9.
3. Effrosyni Diamantoudi, Eiichi Miyagawa, and Licun Xue, *Random paths to stability in the roommate problem*, Games and Economic Behavior 48 (2004), 18--28, DOI: 10.1016/j.geb.2003.05.003.
