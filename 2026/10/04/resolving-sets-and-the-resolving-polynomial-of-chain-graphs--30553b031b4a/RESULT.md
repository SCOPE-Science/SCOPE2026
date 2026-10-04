# Resolving sets and the resolving polynomial of chain graphs
## Finding
Let \(G\) be a finite connected chain graph with bipartition \(A\cup B\). Write the distinct open-neighborhood twin classes on the two sides as
\[
A_1,\ldots,A_p,\qquad B_1,\ldots,B_p,
\]
with \(\alpha_i=|A_i|\), \(\beta_i=|B_i|\), and the canonical nesting chosen so that a vertex of \(A_i\) is adjacent to a vertex of \(B_j\) exactly when \(j\le i\). For a set \(S\subseteq V(G)\), put \(T=V(G)\setminus S\).

Then \(S\) is a resolving set if and only if all of the following hold:

1. \(|T\cap A_i|\le 1\) and \(|T\cap B_i|\le 1\) for every \(i\).
2. Whenever \(i<j\) and \(T\cap A_i\ne\varnothing\), \(T\cap A_j\ne\varnothing\), at least one class \(B_k\) with \(i<k\le j\) meets \(S\).
3. Whenever \(i<j\) and \(T\cap B_i\ne\varnothing\), \(T\cap B_j\ne\varnothing\), at least one class \(A_k\) with \(i\le k<j\) meets \(S\).
4. \(S\ne\varnothing\).

Consequently all resolving sets, not only minimum ones, are counted by an exact four-state recurrence. Define the complement enumerator
\[
Q_G(y)=\sum_{S\text{ resolving}} y^{|V(G)\setminus S|}.
\]
Maintain four polynomials \(F_{a,b}\), where \(a,b\in\{0,1\}\), initially \(F_{0,0}=1\) and the other three are zero. At level \(i\), first process \(B_i\) and then \(A_i\). A state bit \(a=1\) means that an earlier omitted \(A\)-vertex is still waiting for a selected \(B\)-vertex in its distinguishing interval; \(b=1\) is the symmetric condition.

For \(B_i\), each term of state \((a,b)\) has two possible transitions:

- omit no vertex: weight \(1\), new state \((0,b)\);
- omit one vertex: weight \(\beta_i y\), allowed only if \(b=0\), with new state \((a,1)\) if \(\beta_i=1\) and \((0,1)\) if \(\beta_i\ge2\).

For \(A_i\), each term of state \((a,b)\) has two possible transitions:

- omit no vertex: weight \(1\), new state \((a,0)\);
- omit one vertex: weight \(\alpha_i y\), allowed only if \(a=0\), with new state \((1,b)\) if \(\alpha_i=1\) and \((1,0)\) if \(\alpha_i\ge2\).

After level \(p\), sum all four states. For the single exceptional graph \(K_2\), subtract \(y^2\), which is the empty landmark set. The resolving polynomial is then
\[
\Psi_G(x)=\sum_{S\text{ resolving}}x^{|S|}=x^{|V(G)|}Q_G(x^{-1}).
\]
In particular, if \(d=\deg Q_G\), then the metric dimension is \(|V(G)|-d\), and the coefficient of \(y^d\) in \(Q_G\) is the exact number of metric bases.

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. A resolving set means a landmark set whose distance vectors distinguish every pair of vertices. The canonical chain-graph decomposition used above has positive class sizes and no isolated vertices. The statement does not claim a formula for disconnected chain graphs.

The four-state recurrence counts labeled vertex subsets. The factor \(\alpha_i y\) or \(\beta_i y\) records the choice of which single vertex is omitted from a twin class. Coefficients are therefore exact counts of resolving sets by cardinality.

## Proof
For distinct vertices on the same bipartition side, the distance is \(2\). For \(a\in A_i\) and \(b\in B_j\), the distance is \(1\) when \(j\le i\) and \(3\) when \(j>i\).

Vertices in one class \(A_i\), or one class \(B_i\), are open-neighborhood twins. If two vertices of such a class both lie in \(T\), then every landmark outside that class has the same distance to them, while no landmark lies at either omitted vertex. Thus condition 1 is necessary.

Take omitted vertices \(u\in A_i\) and \(v\in A_j\) with \(i<j\). Every landmark on the \(A\)-side has distance \(2\) to both. A landmark in \(B_k\) distinguishes them exactly when \(i<k\le j\): it has distance \(3\) to \(u\) and \(1\) to \(v\). Therefore this pair is distinguished exactly when condition 2 holds. The same argument with the sides interchanged shows that two omitted vertices in \(B_i,B_j\) are distinguished exactly when condition 3 holds, because the distinguishing \(A\)-classes are precisely \(A_i,\ldots,A_{j-1}\).

Finally take one omitted vertex from each side. Every distance from a landmark on the same side as one omitted vertex is even, namely \(2\), while its distance to the omitted vertex on the opposite side is odd, namely \(1\) or \(3\). Hence any landmark distinguishes every omitted cross-side pair. Thus, once \(S\ne\varnothing\), conditions 1--3 are sufficient as well as necessary. Conditions 1--3 permit \(S=\varnothing\) only for \(K_2\), giving condition 4 and the stated correction.

It remains to justify the recurrence. After processing levels below \(i\), an omitted \(A_h\) can conflict with a later omitted \(A\)-vertex only when no selected vertex has appeared in \(B_{h+1},\ldots,B_{i-1}\). All such unresolved obligations are equivalent, so one bit \(a\) suffices. Selecting any vertex of \(B_i\) clears that obligation. Omitting the unique vertex of a singleton \(B_i\) does not clear it, while omitting one vertex from a class of size at least two leaves selected vertices in that class and therefore does clear it. A new omitted \(B_i\)-vertex is forbidden precisely when an unresolved earlier \(B\)-omission exists, because then condition 3 would already fail before \(A_i\) is processed. This is exactly the stated \(B_i\) transition. The \(A_i\) transition is symmetric. Hence the state recurrence is equivalent to conditions 1--3 and counts every allowed complement exactly once.

## Verification
The accompanying `verify_resolving_chain.py` constructs chain graphs from their twin-class sizes, computes all-pairs shortest-path distances, enumerates all vertex subsets, and independently checks the defining resolving-set condition against both the structural criterion and the four-state recurrence. Exhaustive replay covers every class-size vector with \(p\le4\), entries in \(\{1,2,3\}\), and total order at most \(10\).

Replay command: `python3 verify_resolving_chain.py`

The finite replay is corroborative only. The unrestricted statement follows from the distance analysis and state invariant proved above.

## Relationship to prior work
Fernau, Heggernes, van 't Hof, Meister, and Saei studied the metric dimension of chain graphs and gave a linear-time algorithm for the minimum size. The accessible abstract states an optimization result; it does not state an enumerator for all resolving sets. Bhat, Hanif, and Sudhakara later studied metric dimension and related variations for chain graphs, again with emphasis on metric-dimension values and transformations. Resolving polynomials are an established graph invariant: Ali, Salman, and Huang explicitly compute one for commuting graphs of dihedral groups.

The present statement refines the chain-graph minimum problem in a different direction: it characterizes every resolving set, identifies the exact interval obstructions caused by singleton twin classes, and counts all cardinalities through a four-state recurrence. The minimum size and number of metric bases are consequences of that full enumerator.

## Limitations
The full text of the 2015 chain-graph metric-dimension paper was not available through the lawful open-access routes inspected in this review, so there is residual bibliographic risk that an equivalent all-resolving-set characterization appears inside that paper despite not being advertised by its accessible abstract. A later chain-graph paper was located, but the accessible material centers on metric dimension and related variants rather than a resolving polynomial. The originality assessment therefore applies specifically to the all-resolving-set criterion and recurrence stated here, not to the previously studied metric-dimension minimum.

The verifier exhausts only finite instances through order \(10\); it is not an infinite proof. The recurrence is stated for connected chain graphs in canonical twin-class form.

## References
1. H. Fernau, P. Heggernes, P. van 't Hof, D. Meister, R. Saei, “Computing the metric dimension for chain graphs,” *Information Processing Letters* 115 (2015), 671–676. DOI: 10.1016/j.ipl.2015.04.006.
2. K. Arathi Bhat, S. Hanif, G. Sudhakara, “Metric dimension and its variations of chain graphs,” *Proceedings of the Jangjeon Mathematical Society* 24(3) (2021), 309–321. Public record: https://researcher.manipal.edu/en/publications/metric-dimension-and-its-variations-of-chain-graphs/ .
3. F. Ali, M. Salman, S. Huang, “On the Commuting Graph of Dihedral Group,” *Communications in Algebra* 44(6) (2016), 2389–2401. DOI: 10.1080/00927872.2015.1053488.
