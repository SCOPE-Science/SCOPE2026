# Exact four-agent random-serial-dictatorship ordinal-inefficiency census
## Finding
Consider the strict one-to-one random assignment problem with the same number \(n\) of agents and objects. Random serial dictatorship (RSD) chooses each of the \(n!\) priority orders uniformly and, in that order, assigns every agent her favorite remaining object.

For every strict profile with \(n\le 3\), the RSD random assignment is ordinally efficient. At \(n=4\), among all
\[
24^4=331{,}776
\]
labeled strict profiles, exactly
\[
68{,}976
\]
give an ordinally inefficient RSD assignment. Thus, under the uniform distribution on labeled profiles, the exact inefficiency probability is
\[
\frac{68{,}976}{331{,}776}=\frac{479}{2304}.
\]

Quotienting by independent relabeling of agents and objects gives exactly \(762\) profile classes. Of these, exactly \(153\) are RSD-inefficient and \(609\) are RSD-efficient. The inefficient classes have orbit-size distribution
\[
4\cdot72+3\cdot144+55\cdot288+91\cdot576=68{,}976.
\]

A further structural simplification holds at this first nontrivial size: every one of the \(153\) inefficient classes contains a directed \(2\)-cycle in the Bogomolnaia--Moulin ordinal relation. No genuinely longer minimal cycle is needed.

The minimum number of distinct preference orders in an inefficient four-agent profile is two. Exactly four symmetry classes attain this minimum, all with multiplicity pattern \(2+2\). Using objects \(a,b,c,d\), canonical representatives pair two copies of
\[
a\succ b\succ c\succ d
\]
with two copies of, respectively,
\[
a\succ b\succ d\succ c,\qquad
a\succ c\succ b\succ d,\qquad
b\succ a\succ c\succ d,\qquad
b\succ a\succ d\succ c.
\]
The third representative is the standard simplified four-agent example used by Manea.

## Assumptions and scope
Preferences are strict. There are \(n\) agents and \(n\) indivisible objects, each agent receives exactly one object, and every priority order in RSD has probability \(1/n!\).

For a random assignment \(\Pi\), define a directed relation on objects by
\[
x\mathrel{\triangleright_\Pi}y
\]
when some agent strictly prefers \(x\) to \(y\) and receives \(y\) with positive probability under \(\Pi\). Bogomolnaia and Moulin's criterion says that \(\Pi\) is ordinally efficient exactly when this relation is acyclic.

The symmetry quotient identifies profiles under arbitrary relabeling of agents and arbitrary relabeling of objects. It does not identify a profile with its preference reversal unless that reversal is induced by an object relabeling.

## Proof
The ordinal-efficiency criterion can be seen directly. If
\[
x_1\mathrel{\triangleright_\Pi}x_2\mathrel{\triangleright_\Pi}\cdots
\mathrel{\triangleright_\Pi}x_k\mathrel{\triangleright_\Pi}x_1,
\]
choose for every edge an agent witnessing that edge. Moving a sufficiently small common probability mass along the cycle, from each less-preferred received object to the corresponding more-preferred object, preserves every row sum and column sum and gives all involved agents a weak first-order stochastic improvement, with a strict improvement somewhere. Hence a cycle implies ordinal inefficiency.

Conversely, suppose another bistochastic assignment stochastically dominates \(\Pi\). For each agent, finite first-order stochastic dominance on a strict total order admits a monotone coupling: probability mass can be transported only from an object to an object weakly preferred to it. Summing the strict transports over agents gives a nonzero balanced directed flow on the finite object set, because both assignments have the same unit column sums. Every nonzero balanced finite directed flow contains a directed cycle. Every strict transport edge starts at an object that had positive probability under \(\Pi\), so that cycle lies in \(\triangleright_\Pi\). Therefore acyclicity is equivalent to ordinal efficiency.

It remains to make the finite count exhaustive.

For \(n=1,2,3\), the verifier enumerates every labeled profile and every priority order, constructs the positive-support RSD assignment, constructs \(\triangleright_\Pi\), and finds no cycle.

For \(n=4\), the first enumeration route runs over all
\[
\binom{24+4-1}{4}=17{,}550
\]
anonymous multisets of four strict rankings. Each multiset is weighted by the exact number of agent labelings. The \(24\) object relabelings are then applied explicitly, yielding \(762\) canonical symmetry classes. This route gives \(3{,}270\) inefficient anonymous multisets, total labeled weight \(68{,}976\), and \(153\) inefficient symmetry classes.

The second route independently runs over all \(24^4\) labeled profiles without using the anonymous quotient. It again gives exactly \(68{,}976\) inefficient profiles. On every one of the \(331{,}776\) profiles it separately tests whether the ordinal relation has any directed cycle and whether it has a reciprocal pair; the two predicates agree everywhere. This proves the four-agent \(2\)-cycle statement by exhaustive finite verification.

Finally, the quotient route records the multiplicity pattern of each inefficient class. The exact distribution is
\[
119\text{ classes of type }1+1+1+1,\qquad
30\text{ of type }2+1+1,\qquad
4\text{ of type }2+2.
\]
There are no inefficient classes using only one preference order, and the four \(2+2\) classes are precisely the representatives listed above.

## Verification
The embedded `verify_rsd4_ordinal_efficiency.py` is a standard-library-only exact verifier. It performs two exhaustive \(n=4\) enumerations: an anonymous-multiset/object-orbit computation with exact agent-label weights, and a direct labeled-profile computation over all \(331{,}776\) profiles.

It also reproduces the published four-agent witness with two agents ranking
\[
a\succ b\succ c\succ d
\]
and two ranking
\[
b\succ a\succ c\succ d.
\]
The resulting RSD rows are
\[
(5/12,1/12,1/4,1/4)
\]
for the first type and
\[
(1/12,5/12,1/4,1/4)
\]
for the second type, and the ordinal relation contains both \(a\triangleright b\) and \(b\triangleright a\).

Replay command:

`python3 verify_rsd4_ordinal_efficiency.py`

The expected first line is `VERIFY_OK`.

## Relationship to prior work
Bogomolnaia and Moulin introduced ordinal efficiency for random assignment, proved the acyclicity characterization, and showed that random priority/RSD need not be ordinally efficient. Their paper was published online on 29 March 2001 and gives a four-agent counterexample.

Manea later gave the simplified \(2+2\) four-agent example reproduced above and proved that, under uniformly distributed preferences, the fraction of profiles at which RSD is ordinally efficient tends to zero as the problem grows. Manea also proved that every ordinally inefficient RSD outcome admits an ordering-exchange contract that ordinally improves it.

Those results establish existence at four agents, a general characterization, and asymptotic prevalence. The inspected primary literature does not give the exact \(n=4\) labeled count \(68{,}976\), the \(153/762\) symmetry-class split, the orbit-size refinement, the fact that every four-agent failure already contains a \(2\)-cycle, or the four-class minimum-distinct-order classification.

## Limitations
This is a complete finite theorem for strict one-to-one assignment through four agents, not a formula for arbitrary \(n\). The \(2\)-cycle equivalence is asserted only at \(n=4\); longer minimal cycles may matter for larger problems.

The originality search cannot exclude an unindexed thesis, course note, software table, or supplementary data set containing the same finite census. The proof of the numerical statements is exhaustive computation, with two enumeration routes and exact integer arithmetic, rather than a closed symbolic counting formula.

## References
1. A. Bogomolnaia and H. Moulin, “A New Solution to the Random Assignment Problem,” *Journal of Economic Theory* 100 (2001), 295–328. DOI: 10.1006/jeth.2000.2710. Published online 29 March 2001.
2. M. Manea, “Random serial dictatorship and ordinally efficient contracts,” *International Journal of Game Theory* 36 (2008), 489–496. DOI: 10.1007/s00182-007-0088-z.
3. M. Manea, “Asymptotic ordinal inefficiency of random serial dictatorship,” *Theoretical Economics* 4 (2009), 165–197. Handle: 10419/150127.
