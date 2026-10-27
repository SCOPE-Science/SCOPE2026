# Six people are sharp for vaccine-induced collateral infection in a time-varying SIR network

## Finding
In the discrete, one-round-infectious susceptible–infective–removed (SIR) model on an arbitrary fixed directed contact graph, suppose there is one initially infective vertex, one distinct vertex is vaccinated before transmission begins, and every directed edge has an arbitrary probability of transmitting in each calendar round. Contacts are independent across edges and rounds. The vaccinated and unvaccinated experiments use the same probabilities and differ only by removal of the vaccinated vertex at the beginning.

**Sharp population threshold.** For every graph on at most five vertices, every choice of seed, vaccine recipient and other target, and every such collection of calendar-time-dependent probabilities, vaccination cannot increase that target's probability of ever becoming infected. On a six-vertex directed graph, there is a choice of probabilities for which vaccination increases a different target's infection probability from zero to one. The strict effect persists for all probabilities in a nonempty open neighborhood in the unit cube, including a neighborhood of strictly interior values.

This is a statement about risk to an *unvaccinated third person*, not a claim that vaccination is generally harmful or that six is a threshold for total expected cases.

## Assumptions and scope
Fix a finite labelled vertex set of size \(n\), a directed simple graph without loops, a single infective seed \(s\), and a distinct vaccine recipient \(v\). All other people begin susceptible. In each round the currently infective individuals independently attempt each directed contact toward susceptible individuals; then they become permanently removed and newly infected individuals become infective in the next round. A given directed edge \((i,j)\) in calendar round \(t\) transmits with probability \(p_{ij,t}\in[0,1]\), which may vary arbitrarily with \(t\). Both experiments can be coupled by using the same Bernoulli contact variable for each directed edge and time. The vaccinated experiment begins with \(v\) removed; the comparison experiment begins with \(v\) susceptible.

## Proof
**Finite-state upper bound.** By relabelling, take seed 0 and vaccinated person 1. Every graph with at most five vertices embeds into the complete directed five-vertex graph by setting unused edge probabilities to zero; smaller populations embed by adding isolated vertices. Accordingly, it suffices to consider five vertices, with independently selectable binary directed contacts in every round.

Write a coupled state as \((I_U,R_U,I_V,R_V)\), the four bit sets of currently infective and removed vertices in the unvaccinated and vaccinated experiments. Susceptibles are complements of the unions. The initial state is \((\{0\},\varnothing,\{0\},\{1\})\). For a fixed susceptible target \(j\) in both experiments, put \(C=I_U\cap I_V\), \(A=I_U\setminus I_V\), and \(B=I_V\setminus I_U\). Exactly these paired next-infection outcomes are possible from a common edge-by-time contact configuration:

* \((0,0)\) always;
* \((1,0)\) exactly when \(A\ne\varnothing\);
* \((0,1)\) exactly when \(B\ne\varnothing\);
* \((1,1)\) exactly when \(C\ne\varnothing\) or both \(A,B\ne\varnothing\).

If \(j\) is susceptible in only one experiment, infection in that experiment is possible exactly when its current infective set is nonempty; otherwise only \((0,0)\) occurs. If \(j\) is susceptible in neither, only \((0,0)\) occurs. These rules are exhaustive: for an asymmetric outcome a source infective in only the specified experiment supplies a successful edge while all other incoming edges are unsuccessful; a common source or two disjoint sources supply simultaneous successes. Edges into different targets are disjoint, so all locally permitted target outcomes can be chosen together. The next state replaces infectives with removed vertices and adds the chosen new infectives. Thus these rules generate **every** pair of epidemic trajectories under every possible common edge-by-time contact history, without an approximation to probabilities.

The standalone `verify.py` enumerates the forward closure of this precisely defined finite-state transition relation. There are exactly 140 reachable paired states. In every terminal reachable state (both infective sets empty), every vertex other than 0 and 1 that was infected in the vaccinated experiment was also infected in the unvaccinated experiment. This is exhaustive finite verification: the complete state and transition sets are enumerated rather than sampled. Therefore the inclusion holds pathwise under the common-contact coupling. Taking probabilities proves the claimed monotonicity on at most five vertices.

**Six-vertex construction.** Use the directed edges \(0\to1\), \(0\to2\), \(1\to3\), \(2\to4\), \(4\to3\), \(3\to5\). Seed 0, vaccinate 1, and measure infection of target 5. Take certain successful contacts \((0,1)\), \((0,2)\) in round 0; \((1,3)\), \((2,4)\) in round 1; \((4,3)\) in round 2; and \((3,5)\) in round 3. Every other edge/round contact fails. Without vaccination, 3 becomes infective in round 2 and fails to transmit to 5; it has recovered by round 3. With vaccination, 3 instead becomes infective in round 3 through \(0\to2\to4\to3\), and infects 5. Thus the endpoint risks are respectively zero and one. Because final infection probabilities on a fixed finite graph are polynomials in the finitely many contact probabilities relevant before termination, the strict inequality persists under sufficiently small perturbations into \((0,1)\).

## Verification
Run `python3 verify.py` from the extracted finding directory. The code independently constructs the five-vertex universal coupled transition system, confirms its 140-state reachable closure and absence of adverse terminal states, simulates the deterministic six-person construction, and additionally finds a six-vertex adverse state by the same universal exhaustive method. The proof uses complete finite enumeration only for a finite cutoff and an exact explicit witness; no extrapolation from random trials is used.

## Relationship to prior work
Floyd, Kay and Shapiro (2007/2008) established monotonicity of vaccination for time-independent directed SIR contact probabilities, and explicitly discussed the possibility of collateral harm when contact probabilities depend on calendar time. Their accessible fourteen-page preprint supplies the conceptual starting point but does not establish this sharp five-versus-six population boundary. In particular, their time-independent monotonicity result cannot imply the present statement, whose upper bound allows arbitrary time variation. The present finding does not claim that the general possibility of time-dependent collateral harm is new.

## Limitations
The result assumes one initial seed, one prophylactically vaccinated vertex, one-round infectiousness, fixed population and graph, and independent directed edge-by-time contacts. It makes no assertion for multiple initial seeds, latent or heterogeneous infectious periods, adaptive transmission behavior, or realistic public-health benefit–risk balances. Research priority is provisional without an independent audit.

## References
1. W. Floyd, L. Kay, M. Shapiro, *Some Elementary Properties of SIR Networks or, Can I Get Sick because You Got Vaccinated?*, preprint dated 21 August 2007; *Bulletin of Mathematical Biology* 70 (2008), 713–727. DOI: 10.1007/s11538-007-9275-0. Full preprint: https://personal.math.vt.edu/floyd/research/papers/epidemics.pdf.
2. M. E. J. Newman, *Spread of epidemic disease on networks*, *Physical Review E* 66 (2002), 016128. DOI: 10.1103/PhysRevE.66.016128.
