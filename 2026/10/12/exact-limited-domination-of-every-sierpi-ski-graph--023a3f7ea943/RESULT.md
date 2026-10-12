# Exact limited domination of every Sierpiński graph

## Finding

**Theorem.** For all integers \(n\ge 1\), \(m\ge 2\), and \(1\le k\le m-1\), the ordinary Sierpiński graph \(S(n,m)\) satisfies
\[
\boxed{\gamma_k^{\mathrm L}(S(n,m))=(m-k)m^{n-1}.}
\]
Here \(\gamma_k^{\mathrm L}\) is the minimum cardinality of a dominating set in which each selected vertex has at most \(k\) neighbors outside the set. This confirms Conjecture 12 of Božović, *On \(k\)-limited domination: complexity and Sierpiński graphs* (2026), for its entire stated parameter range. The proof supplies a uniform explicit optimal-set construction, not just the extremal number.

## Assumptions and scope

All graphs are finite, simple and undirected. For \(n\ge1\) and \(m\ge2\), the vertices of \(S(n,m)\) are words \(x_1\cdots x_n\) over \(\{0,\ldots,m-1\}\). Two distinct words \(u,v\) are adjacent if there is an index \(h\) such that their coordinates before \(h\) agree, their coordinates at \(h\) differ, and, after \(h\), every coordinate of \(u\) equals \(v_h\) while every coordinate of \(v\) equals \(u_h\). For a vertex set \(D\), domination means every vertex outside \(D\) has a neighbor in \(D\). It is \(k\)-limited if \(|N(u)\setminus D|\le k\) for each \(u\in D\).

The theorem concerns \(1\le k\le m-1\). The formula is not asserted for \(k\ge m\), and it makes no assertion about uniqueness or the total number of minimum sets.

## Proof

Put \(r=m-k\), so \(1\le r\le m-1\).

**1. A lower bound for a two-level block.** Suppose first that \(n\ge2\). Partition the vertices by their first \(n-2\) coordinates. Fix such a prefix \(p\), and let \(B_p\) be the \(m^2\) words \((p,i,j)\). For each \(i\in\{0,\ldots,m-1\}\), its **row clique** is \(C_{p,i}=\{(p,i,j):0\le j<m\}\), with \(m\) vertices. Let \(c_i=|D\cap C_{p,i}|\), where \(D\) is any \(k\)-limited dominating set of the *whole* \(S(n,m)\), not merely its induced block.

If \(c_i>0\), any selected vertex in that row has \(m-c_i\) unselected neighbors within the clique. The limitedness condition therefore gives \(c_i\ge m-k=r\).

At most one row of \(B_p\) can be empty. To see this, suppose rows \(i\) and \(j\) were both empty, with \(i\ne j\). The vertex \((p,i,j)\) has no selected neighbor in its row. Its **only** neighbor outside that row is \((p,j,i)\): any linking edge at an earlier coordinate requires the final two coordinates of the endpoint to be equal, whereas \(i\ne j\). The vertex \((p,j,i)\) is in the other empty row. Thus \((p,i,j)\) is undominated, a contradiction.

If no row is empty, \(\sum_i c_i\ge mr\). If row \(i\) alone is empty, then for every \(j\ne i\) the vertex \((p,i,j)\) must be dominated by its unique external neighbor \((p,j,i)\). Consequently \((p,j,i)\in D\). This selected vertex has the unselected neighbor \((p,i,j)\) across the two rows, *in addition* to its \(m-c_j\) unselected row neighbors. Hence \(m-c_j+1\le k\), so \(c_j\ge r+1\). We conclude
\[
\sum_i c_i\ge(m-1)(r+1)=mr+(m-1-r)=mr+(k-1)\ge mr.
\]
This argument remains valid even when vertices in \(B_p\) possess further links to other blocks, because the off-diagonal vertices \((p,i,j)\), \(i\ne j\), have no such earlier linking edge.

The \(m^{n-2}\) blocks \(B_p\) partition the graph, giving
\[
|D|\ge m^{n-2}\cdot mr=r m^{n-1}.
\]
For \(n=1\), the graph is \(K_m\); any nonempty \(k\)-limited dominating set has at least \(m-k=r\) vertices, so the same lower bound holds.

**2. A symmetric regular relation with uniform diagonal.** There is a symmetric relation \(R\subseteq\{0,\ldots,m-1\}^2\) such that every row has exactly \(r\) related elements and either all diagonal pairs belong to \(R\) or none do. We give an explicit construction with residues modulo \(m\):

- If \(m\) is odd and \(r\) is odd, include every diagonal pair, together with the offsets \(\pm1,\ldots,\pm(r-1)/2\).
- In all other cases omit all diagonal pairs. For even \(r\), use offsets \(\pm1,\ldots,\pm r/2\). For odd \(r\) (which then requires even \(m\)), use offsets \(\pm1,\ldots,\pm(r-1)/2\), plus the antipodal offset \(m/2\).

The stated ranges ensure that none of these offsets duplicate a residue or introduce an unwanted loop. Every row has degree exactly \(r\), the relation is symmetric, and its diagonal indicator is constant.

**3. Attaining the bound.** For \(n\ge2\), select a word exactly when its last two symbols are related:
\[
D=\{x_1\cdots x_n:(x_{n-1},x_n)\in R\}.
\]
Each row clique has exactly \(r\) selected vertices, so \(|D|=r m^{n-1}\). Since \(r\ge1\), every row clique contains a selected vertex and hence all vertices are dominated.

We verify the limitedness constraint for the additional links between row cliques. Such a link has first differing coordinate \(h<n\). If \(h=n-1\), its endpoints have last-two pairs \((a,b)\) and \((b,a)\). Symmetry of \(R\) ensures that either both endpoints or neither are selected. If \(h\le n-2\), the last-two pairs are \((b,b)\) and \((a,a)\), and the constant diagonal indicator gives the same conclusion. Therefore **no selected vertex has an unselected neighbor outside its row clique**. Every selected vertex has exactly \(m-r=k\) unselected neighbors within its row, so \(D\) is \(k\)-limited.

When \(n=1\), selecting any \(r\) vertices of \(K_m\) gives a \(k\)-limited dominating set. The construction and lower bound coincide for every admissible \(n,m,k\), completing the proof. \(\square\)

## Verification

The accompanying pure-Python script `verify.py` constructs the defining Sierpiński adjacency relation independently of the symmetric-relation construction. It checks that the explicit set dominates and meets the \(k\)-limited inequalities for 69 parameter profiles, verifies the linking-edge invariance, and independently exhausts all vertex subsets for 36 small profiles to confirm the exact minimum. Run `python3 verify.py`; the accompanying `verify_output.txt` is the actual recorded stdout. These finite tests supplement, and are not a substitute for, the universal proof above.

## Relationship to prior work

Božović's arXiv:2610.01584v1 (submitted 2026-10-01) defines the parameter and Sierpiński graphs, proves the formula for \(k=1\) and all \(m\), proves the remaining \(m=3,k=2\) case, and explicitly states the all-parameter formula above as **Conjecture 12** in Section 6. Those previously established cases are not presented as new. The new argument covers all \(m\ge2\), \(1\le k\le m-1\), and \(n\ge1\) simultaneously. Božović, Radić, Kovijanić-Vukićević, and Tepeh introduced \(k\)-limited domination and derived general bounds and graph-family examples (arXiv:2606.22422); their known general bounds do not state the Sierpiński conjecture's complete exact formula. The equivalent terminology \((0,k)\)-pitchfork domination is acknowledged, but does not itself imply the parameter values.

## Limitations

The result establishes the stated minimum cardinality and gives explicit attaining sets, but does not enumerate **all** attaining sets or analyze parameters outside the conjectured range. The independent exhaustive verification covers only the stated finite profiles. Unindexed or inaccessible pre-existing equivalent results cannot be ruled out by literature searches; no independent external audit is claimed.

## References

1. D. Božović, *On \(k\)-limited domination: complexity and Sierpiński graphs*, arXiv:2610.01584v1 (first public 2026-10-01), Section 5, Theorems 10–11 and Conjecture 12. https://arxiv.org/abs/2610.01584 ; full-text HTML https://arxiv.org/html/2610.01584v1 .
2. D. Božović, Ž. Kovijanić Vukićević, G. Radić, and A. Tepeh, *On \(k\)-limited domination in graphs*, arXiv:2606.22422 (first public 2026-06-21). https://arxiv.org/abs/2606.22422 .
3. A. Tepeh, *On \(k\)-limited domination: complexity and Cartesian products*, arXiv:2606.22428 (2026). https://arxiv.org/abs/2606.22428 .
