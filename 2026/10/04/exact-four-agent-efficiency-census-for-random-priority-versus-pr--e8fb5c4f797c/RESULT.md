# Exact four-agent efficiency census for random priority versus probabilistic serial
## Finding
Consider the balanced random-assignment problem with four agents and four unit objects, complete strict preferences, random priority (uniform random serial dictatorship), and probabilistic serial.

There are
\[
(4!)^4=24^4=331776
\]
labeled strict-preference profiles. They split into exactly four classes:
\[
\begin{array}{c|r|c}
\text{class} & \text{profiles} & \text{probability}\\ \hline
RP=PS & 72288 & 251/1152\\
RP\neq PS,\ RP\text{ ordinally efficient} & 190512 & 147/256\\
RP\text{ ordinally inefficient, }PS\not\succ_{SD}RP & 57312 & 199/1152\\
PS\succ_{SD}RP & 11664 & 9/256
\end{array}
\]
where \(PS\succ_{SD}RP\) means that every agent weakly stochastically prefers her probabilistic-serial lottery to her random-priority lottery and at least one agent strictly prefers it.

Consequently, random priority is ordinally inefficient on exactly
\[
68976
\]
profiles, with probability
\[
\frac{479}{2304},
\]
whereas probabilistic serial directly stochastically dominates random priority on exactly
\[
11664
\]
profiles, with probability
\[
\frac{9}{256}.
\]
Therefore direct probabilistic-serial domination explains exactly
\[
\frac{11664}{68976}=\frac{81}{479}
\]
of the four-agent ordinal inefficiency of random priority. Most ordinally inefficient random-priority profiles are not repaired by probabilistic serial through direct stochastic domination; they require some other ordinal improvement.

The foundational comparison establishes that this direct-domination configuration cannot occur with two or three agents. Hence four agents are the first balanced market size where probabilistic serial can stochastically dominate random priority.

## Assumptions and scope
There are exactly four agents and four objects. Every agent has a complete strict ranking of the objects.

Random priority draws one of the \(4!=24\) priority orders uniformly and applies serial dictatorship.

Probabilistic serial lets all agents consume their most-preferred currently available object at equal unit speed until every agent has consumed one unit in total.

Stochastic dominance is evaluated separately at each agent's reported strict ranking. A random assignment is ordinally efficient when no feasible random assignment weakly stochastically improves every agent and strictly improves at least one.

## Proof
The complete profile domain has \(24^4=331776\) elements.

For each profile, the random-priority assignment is computed by enumerating all \(24\) priority orders and counting the deterministic serial-dictatorship assignments. Probabilistic serial is computed exactly with rational arithmetic by advancing from one object-exhaustion event to the next.

Ordinal efficiency of random priority is tested with the Bogomolnaia-Moulin acyclicity criterion. Given an assignment \(P\), put a directed relation from object \(a\) to object \(b\) whenever some agent receives positive probability of \(b\) and strictly prefers \(a\) to \(b\). Their lemma states that \(P\) is ordinally efficient if and only if this relation is acyclic.

For every profile, the verifier first checks whether the two probability matrices are equal. If not, it checks whether probabilistic serial stochastically dominates random priority by comparing cumulative probabilities on every upper contour set of every agent. It independently computes whether random priority is ordinally efficient from the object relation.

The exact resulting counts are
\[
72288,\quad190512,\quad57312,\quad11664
\]
in the four classes stated above.

These classes are exhaustive. Probabilistic serial is ordinally efficient at every profile, so a distinct random-priority assignment cannot stochastically dominate it. Therefore, whenever the assignments are distinct and probabilistic serial does not dominate random priority, the two assignments are incomparable by stochastic dominance.

Summing the two ordinally inefficient classes gives
\[
57312+11664=68976.
\]
The exact reductions are
\[
\frac{68976}{331776}=\frac{479}{2304},
\qquad
\frac{11664}{331776}=\frac{9}{256},
\qquad
\frac{11664}{68976}=\frac{81}{479}.
\]

## Verification
The embedded `verify_rsd_ps_four_agents.py` uses only the Python standard library and exact rational arithmetic.

It exhausts all \(331776\) labeled four-agent profiles. For every profile it:
- averages the \(24\) deterministic serial-dictatorship outcomes exactly;
- executes probabilistic serial by exact exhaustion events;
- tests the Bogomolnaia-Moulin object relation for acyclicity;
- checks equality of the two assignments;
- checks stochastic dominance by all rank cutoffs.

The replay returns the exact four-class histogram and the three reduced fractions stated in the finding.

Run:

`python3 verify_rsd_ps_four_agents.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Bogomolnaia and Moulin introduced probabilistic serial and compared it systematically with random priority. They prove that probabilistic serial is ordinally efficient, give the acyclicity characterization used here, show that with two agents the mechanisms coincide, and completely describe the three-agent disagreement profiles. They also give a four-agent example in which probabilistic serial stochastically dominates random priority, establishing that direct dominance becomes possible at four agents.

Che and Kojima later prove an asymptotic equivalence result: in large replicated markets, random-priority and probabilistic-serial assignments converge to one another.

The present result is a finite exact complement at the first market size where direct dominance is possible. It measures the whole four-agent domain, distinguishes ordinal inefficiency from direct probabilistic-serial domination, and shows that only \(81/479\) of random-priority's four-agent ordinal inefficiency is captured by direct domination from probabilistic serial.

## Limitations
The classification is exact only for the balanced four-agent, four-object model with complete strict preferences and uniform random priority.

It does not classify larger markets, weak preferences, unequal numbers of agents and objects, quotas, priorities at objects, or strategic reports.

The originality search did not locate the exact counts or fractions reported here. An unindexed computation, lecture note, thesis, or supplementary file could contain the same four-agent census.

## References
1. A. Bogomolnaia and H. Moulin, “A New Solution to the Random Assignment Problem,” *Journal of Economic Theory* 100 (2001), 295–328. DOI: 10.1006/jeth.2000.2710. Published online 29 March 2001.
2. Y.-K. Che and F. Kojima, “Asymptotic Equivalence of Probabilistic Serial and Random Priority Mechanisms,” *Econometrica* 78 (2010), 1625–1672. DOI: 10.3982/ECTA8354. First published 12 October 2010.
