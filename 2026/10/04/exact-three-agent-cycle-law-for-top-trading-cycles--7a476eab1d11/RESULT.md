# Exact three-agent cycle law for top trading cycles
## Finding
Consider the classical Shapley--Scarf housing market with three agents. Agent \(i\) initially owns house \(i\), each agent has a strict ranking of all three houses, and the three rankings are sampled independently and uniformly from the six linear orders.

Use the parallel top-trading-cycles convention: in each round every remaining agent points to the owner of her favorite remaining house, every directed cycle in that round is executed simultaneously, and the participating agents and houses leave the market.

For a run of TTC, record in each round the multiset of cycle sizes. Over all
\[
6^3=216
\]
labeled preference profiles, the complete chronology law is:

\[
\begin{array}{c|r}
\text{cycle-size chronology} & \text{number of profiles}\\
\hline
((1,1,1)) & 8\\
((1,2)) & 24\\
((3)) & 16\\
((1,1),(1)) & 48\\
((2),(1)) & 48\\
((1),(1,1)) & 6\\
((1),(2)) & 30\\
((1),(1),(1)) & 36
\end{array}
\]

Thus the number of TTC rounds has distribution
\[
\Pr(R=1)=\frac29,\qquad
\Pr(R=2)=\frac{11}{18},\qquad
\Pr(R=3)=\frac16,
\]
and therefore
\[
\mathbb E[R]=\frac{35}{18}.
\]

The final trade volume is also exact. The number \(M\) of agents who receive a house different from their endowment satisfies
\[
\Pr(M=0)=\frac{49}{108},\qquad
\Pr(M=2)=\frac{17}{36},\qquad
\Pr(M=3)=\frac{2}{27}.
\]
There is no one-agent trade, so
\[
\Pr(M>0)=\frac{59}{108},
\qquad
\mathbb E[M]=\frac76.
\]

These are exact impartial-culture probabilities for the smallest housing market that can exhibit a genuine three-agent trading cycle.

## Assumptions and scope
There are exactly three agents and exactly three indivisible houses. Each agent initially owns one distinct house, and each agent demands exactly one house. Preferences are complete and strict.

The probability model is impartial culture: the six strict rankings of the three houses are independently equiprobable for each agent. The sample space therefore consists of \(216\) labeled profiles.

The chronology uses a parallel-round convention: all disjoint cycles present in the current directed graph are executed in the same round. This convention does not affect the final TTC allocation, but it does affect the reported round chronology when several disjoint cycles coexist.

A moved agent is one whose final TTC house differs from her initial endowment.

## Proof
Only the agents' first choices matter in the first round. Since each first choice is uniform over the three houses, there are
\[
3^3=27
\]
first-choice maps, each having exactly
\[
2^3=8
\]
full-ranking refinements obtained by ordering each agent's two lower-ranked houses.

View a first-choice map as a directed functional graph on the three owners. Its possibilities split into six types.

There is one identity map with three self-loops. Its eight refinements terminate immediately with chronology \(((1,1,1))\).

There are three maps consisting of one self-loop and one two-cycle. Their \(24\) refinements terminate immediately with chronology \(((1,2))\).

There are two three-cycles. Their \(16\) refinements terminate immediately with chronology \(((3))\).

There are six maps with two self-loops and one incoming tail. Their \(48\) refinements execute the two self-loops first and the remaining singleton second, giving \(((1,1),(1))\).

There are six maps with one two-cycle and one incoming tail but no self-loop. Their \(48\) refinements execute the two-cycle first and the remaining singleton second, giving \(((2),(1))\).

The remaining nine first-choice maps have exactly one self-loop and no two-cycle, accounting for \(72\) profiles. Three of these maps are stars: both other agents point directly to the fixed-point owner. After that owner exits, the two remaining second choices are independent binary choices. For each star map, the four lower-order refinements split as one profile producing two simultaneous self-loops, one producing a two-cycle, and two producing one self-loop followed by another. Across the three star maps and the irrelevant lower order of the fixed-point agent, this contributes
\[
6\text{ profiles of }((1),(1,1)),\quad
6\text{ profiles of }((1),(2)),\quad
12\text{ profiles of }((1),(1),(1)).
\]

The other six maps are chains: one agent points to the fixed-point owner and the third points to that agent. After the fixed point exits, the middle agent's next available choice is equally often her own house or the third agent's house. Across the \(48\) refinements this contributes
\[
24\text{ profiles of }((1),(2))
\]
and
\[
24\text{ profiles of }((1),(1),(1)).
\]

Combining the star and chain cases gives \(30\) profiles of \(((1),(2))\), \(36\) of \(((1),(1),(1))\), and \(6\) of \(((1),(1,1))\). Together with the other five first-round graph types, this proves the full eight-cell chronology table.

Summing the table by number of rounds gives counts \(48,132,36\), hence the stated round probabilities and expectation.

For trade volume, an agent moves exactly when she belongs to a nontrivial trading cycle at some stage. Exhaustive evaluation of the same \(216\) profiles gives \(98\) profiles with no movers, \(102\) with exactly two movers, and \(16\) with all three movers. The three-mover profiles are exactly the first-round three-cycles. Dividing by \(216\) gives the stated probabilities and
\[
\mathbb E[M]=\frac{2\cdot102+3\cdot16}{216}=\frac76.
\]

## Verification
The embedded `verify_ttc3_cycle_chronology.py` uses only the Python standard library and exact arithmetic.

It implements TTC in two independent ways. The first forms the functional graph from each agent to the current owner of her favorite remaining house. The second constructs the explicit bipartite directed graph with separate agent and house nodes. The two implementations must agree on both the final allocation and the entire parallel cycle chronology for every one of the \(216\) preference profiles.

The verifier also independently checks the \(27\)-map first-round taxonomy, the star/chain refinement split, the eight chronology counts, the trade-volume distribution, and the exact expectations.

Replay with:

`python3 verify_ttc3_cycle_chronology.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Shapley and Scarf introduced the indivisible-housing market and the trading-cycle idea in their foundational work on the core. Later characterization results established TTC as the canonical efficient, strategy-proof, individually rational rule under strict preferences.

Ekici's modern treatment makes the cycle structure explicit: TTC repeatedly identifies cycles of agents who own one another's favorite remaining objects, executes a cycle, removes its participants, and continues. That literature studies the mechanism axiomatically rather than giving the complete three-agent impartial-culture chronology above.

Che and Tercieux study random TTC dynamics in a different, two-sided matching environment with random preferences and object priorities. They derive a Markov description for the number assigned in each round. Their result strongly motivates round-by-round cycle statistics, but it does not cover the Shapley--Scarf endowment graph in which each house points deterministically to its owner.

Targeted searches using TTC/top-trading-cycles terminology, three-agent housing markets, impartial culture, cycle lengths, round counts, and the exact probabilities in this result did not locate an equivalent published table.

## Limitations
The theorem is only for three agents, strict preferences, one owned house per agent, and independent uniform preferences.

The cycle chronology uses simultaneous execution of all cycles in a round. A specification that deliberately executes one disjoint cycle at a time has the same final allocation but a different step count, so the chronology numbers should not be transferred to that convention.

The exact census was not found in the inspected literature, but an unindexed exercise, note, software table, or supplementary computation could contain the same finite distribution.

The foundational Shapley--Scarf publication was located with month-level dating rather than an exact public day. No day is inferred from that record; the metadata uses a later exact day-resolved public working-paper record in the same classical TTC literature.

## References
1. L. S. Shapley and H. Scarf, “On cores and indivisibility,” *Journal of Mathematical Economics* 1 (1974), 23–37. DOI: 10.1016/0304-4068(74)90033-0.
2. P. Jaramillo and V. Manjunath, “The Difference Indifference Makes in Strategy-Proof Allocation of Objects,” Documentos CEDE 8746, 2011; later *Journal of Economic Theory* 147 (2012), 1913–1946. RePEc:col:000089:008746.
3. Y.-K. Che and O. Tercieux, “An Analysis of Top Trading Cycles in Two-Sided Matching Markets,” Cowles Foundation Discussion Paper 2014, 2015.
4. Ö. Ekici, “Pair-efficient reallocation of indivisible objects,” *Theoretical Economics* 19 (2024), 551–564. DOI: 10.3982/TE5471.
