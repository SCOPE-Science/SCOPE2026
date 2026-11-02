# Exact minimum 1-limited domination and rigidity of Möbius ladders

## Finding

Let \(M_{2m}\), for an integer \(m\ge3\), be the Möbius ladder with vertices \(\mathbb Z/(2m)\), its cycle edges \(\{i,i+1\}\), and its antipodal edges \(\{i,i+m\}\). A set \(D\) is 1-limited dominating if every vertex outside \(D\) has a neighbor in \(D\) and every vertex inside \(D\) has at most one neighbor outside \(D\).

**Theorem.** For all \(m\ge3\),
\[
\gamma^{\mathrm L}_1(M_{2m})=
\begin{cases}m,&m\equiv0\pmod4,\\m+1,&m\not\equiv0\pmod4.\end{cases}
\]
The number of minimum sets on these fixed, labelled vertices is
\[
N_m=\begin{cases}
4,&m\equiv0\pmod4,\\
2m,&m\equiv2\pmod4,\\
3m,&m\text{ odd}.
\end{cases}
\]
Every minimum set is one of the following: when \(4\mid m\), a rotation of \((1100)^{m/2}\); when \(m\equiv2\pmod4\), any cyclic interval of \(m+1\) consecutive vertices; when \(m\) is odd, any such interval or any antipodally invariant set obtained from a minimum total dominating set of the \(m\)-cycle by selecting both vertices of each selected antipodal pair. There are exactly \(m\) members of the last family.

## Assumptions and scope

The graph is simple and cubic for every integer \(m\ge3\). Membership words index the \(2m\) vertices in their prescribed cyclic order; rotations are distinct labelled sets unless their words coincide. A total dominating set of a graph is one for which *every* vertex, including selected vertices, has a selected neighbor. Neither graph-automorphism orbits nor inclusion-minimal nonoptimum sets are counted.

## Proof

**1. Antipodal pair states.** Group vertices into the \(m\) antipodal pairs \(\{i,i+m\}\), with columns indexed cyclically by \(i\in\mathbb Z/m\). Mark a column \(A\) when both members belong to \(D\), \(Z\) when neither does, and \(P\) or \(Q\) when exactly one does (call the last two types *mixed*). The two horizontal edges from the last column to the first exchange the two row labels: the strip is twisted. Let \(a,z,p\) be the numbers of full, empty, and mixed columns. Then
\[
|D|=2a+p=m+a-z.
\]
A mixed column's selected vertex has its antipodal neighbor outside \(D\), so **both** cycle neighbors must be selected. In particular, a mixed column cannot touch a \(Z\) column; two adjacent mixed columns must select the same row after transportation along their common horizontal edges. If every column were mixed, this row would have to return to itself after the one row-exchanging twist, which is impossible. Hence every feasible configuration with mixed columns contains at least one \(A\) column.

An empty column cannot have empty columns on both sides: its two unselected vertices would lack selected neighbors. Thus every maximal run of \(Z\) columns has length at most two. Such a run cannot adjoin a mixed column, so both ends are flanked by \(A\) columns. Moreover, an \(A\) column adjoining a \(Z\) column must have its other neighboring column also of type \(A\): each selected vertex in the full column has its antipodal neighbor selected, but a neighboring \(Z\) supplies no selected cycle neighbor, and a mixed column would supply one on only one row. Hence each run of \(A\) columns adjoining \(Z\) has length at least two.

**2. The mixed–empty gap.** Suppose that both a mixed column and an empty column occur, and let \(r\) be the number of maximal \(Z\)-runs. There are at most \(2r\) empty columns. On the circular sequence of runs, with both mixed and empty types present and with no mixed–empty adjacency, there are at least \(r+1\) distinct \(A\)-runs adjoining an empty run. (Traverse all empty runs in their cyclic order; consecutive ones require an intervening \(A\)-run, and the nonempty complement containing mixed columns requires two distinct \(A\)-runs at its boundaries.) Each such full run has length at least two. Consequently,
\[
a\ge2(r+1),\qquad z\le2r,\qquad |D|=m+a-z\ge m+2.
\]
Thus no set of size at most \(m+1\) contains both mixed and empty columns.

**3. Mixed columns but no empty ones.** In this case \(z=0\) and \(a\ge1\), so \(|D|\ge m+1\). Equality forces exactly one \(A\) column and \(m-1\) consecutive mixed columns. The selected rows must agree along the mixed path; the twisted seam switches its row at the opposite side of the unique \(A\) column, so the two selected vertices in the \(A\) column each have one selected cycle neighbor. These configurations are feasible and are exactly the cyclic intervals containing \(m+1\) consecutive vertices on the \(2m\)-cycle. The position of the single full column (\(m\) choices) and the selected row in the mixed path (two choices) give exactly \(2m\) distinct sets.

**4. No mixed columns.** Here every column is \(A\) or \(Z\). The 1-limited conditions reduce exactly to requiring each \(A\) column to have an adjacent \(A\) column and each \(Z\) column to have an adjacent \(A\) column. Thus the length-\(m\) binary column word describes a total dominating set of \(C_m\), and \(|D|=2a\). If both column types occur, every run of ones has length at least two and every run of zeros has length at most two. The all-one word is feasible but too large to be optimal for \(m\ge3\).

Suppose there are \(r\) runs of ones, hence \(r\) runs of zeros. Then \(a\ge2r\), \(z\le2r\), so \(a\ge z\). Equality is possible only when every run of each kind has length exactly two, requiring \(4\mid m\). In that case the only minimum words are the four rotations of \((1100)^{m/4}\) in the column representation, which become the four rotations of \((1100)^{m/2}\) on the full vertex cycle. Each has \(a=z=m/2\), hence \(|D|=m\).

If \(m\equiv2\pmod4\), then a total-dominating column word cannot have \(a=z\), so \(a>z\). As \(|D|=2a\) is even and \(m\) is even, it follows that \(|D|\ge m+2\), strictly above the mixed optimum \(m+1\).

If \(m\) is odd, \(a-z\) is odd and nonnegative, hence at least one. The bound \(|D|\ge m+1\) is attained exactly when \(a-z=1\). The run inequalities then give
\[
1=a-z=(a-2r)+(2r-z),
\]
where both summands are nonnegative integers. Exactly one is one. Therefore the cyclic word has one unique run of length three among two-long one-runs, with all zero-runs two-long; or it has one unique zero-run of length one among two-long zero-runs, with all one-runs two-long. The first alternative applies when \(m\equiv1\pmod4\), and the second when \(m\equiv3\pmod4\). Each is one rotation orbit with a unique defect and hence contains exactly \(m\) different labelled column words. Each determines an antipodally invariant minimum set of the Möbius ladder.

**5. Exhaustion and counts.** Step 2 excludes mixed–empty configurations from minimum size. Step 3 lists all no-empty mixed minima. Step 4 lists and counts every pure-column minimum. For \(m\equiv0\pmod4\) only four pure-column sets have cardinality \(m\); for \(m\equiv2\pmod4\) only the \(2m\) consecutive-interval sets have cardinality \(m+1\); and for odd \(m\) the \(2m\) intervals and \(m\) antipodally invariant sets each have cardinality \(m+1\). Their families are disjoint because one contains mixed columns and the other does not. This proves all claims. \(\square\)

## Verification

The included standalone source `verify.cpp` independently constructs the Möbius-ladder adjacency lists, enumerates every candidate membership subset of size at most the theorem's claimed minimum for \(3\le m\le12\), and compares the complete set of optimal masks against a separate generator of the classified families. Compile using `g++ -O3 -std=c++17 -Wall -Wextra verify.cpp -o verify` and run `./verify`. The test examines 13,877,450 candidate masks and prints `VERIFY_OK` upon agreement. This finite experiment checks the formulas and several boundary cases but is not the all-parameter proof, which is the pair-run argument above.

## Relationship to prior work

Radić and Tepeh (2026) study 1-limited / \((1,2)\)-domination on cubic graphs and calculate the parameter on Goldberg snarks. Radić, Radić, and Tepeh (2026) give the general lower bound \(\gamma_1^{\mathrm L}(G)\ge|V(G)|/2\), a bipartite-cut structural lemma, and exact evaluations for two other snark families. Neither paper's inspected graph-family theorems state the complete Möbius-ladder optimum-set classification or multiplicities. In particular, the lower bound alone does not yield either the modulo-four exception or the family counts. The 2021 OEIS data on *ordinary* minimum dominating sets of Möbius ladders (A347559) concern a different constraint; likewise, data on inclusion-minimal *total* dominating sets (A303162) do not count 1-limited sets.

## Limitations

The result applies to the unmodified two-row Möbius ladder for \(m\ge3\), with labelled vertices. It does not count nonminimum 1-limited dominating sets, symmetry classes, or higher-width twisted ladders. A general historical-priority search cannot rule out an unlocated equivalent theorem under other graph terminology; prior work on matching cuts or \((1,2)\)-domination might furnish an alternative approach. Independent mathematical assessment has not been performed.

## References

1. G. Radić and A. Tepeh, *On 1-limited and (1,2)-domination in cubic graphs*, arXiv:2610.01796v1 (public October 1, 2026), https://arxiv.org/html/2610.01796v1.
2. G. Radić, G. Radić, and A. Tepeh, *Structural aspects of 1-limited domination in cubic graphs*, arXiv:2610.26259v1 (public October 19, 2026), https://arxiv.org/html/2610.26259v1.
3. OEIS A347559, *Number of minimum dominating sets in the n-Moebius ladder*, https://oeis.org/A347559 (different invariant).
4. OEIS A303162, *Number of minimal total dominating sets in the n-Moebius ladder*, https://oeis.org/A303162 (different invariant).
