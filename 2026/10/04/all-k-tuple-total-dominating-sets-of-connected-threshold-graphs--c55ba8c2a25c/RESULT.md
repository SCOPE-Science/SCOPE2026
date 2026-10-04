# All \(k\)-tuple total dominating sets of connected threshold graphs
## Finding
Let \(G\) be a finite connected threshold graph of order \(N\ge2\). Use its canonical creation-block form
\[
0^{a_1}1^{b_1}\cdots 0^{a_p}1^{b_p},
\]
where every block size is positive. Let \(B_p\) denote the final \(1\)-block and put \(b=b_p\). For an integer \(k\ge1\), call \(S\subseteq V(G)\) a \(k\)-tuple total dominating set when every vertex has at least \(k\) neighbors in \(S\).

Then
\[
S\text{ is a }k\text{-tuple total dominating set}
\quad\Longleftrightarrow\quad
|S\cap B_p|\ge k\text{ and }|S|\ge k+1.
\]
Thus such sets exist exactly for \(1\le k\le b\), and their cardinality generating polynomial is
\[
T_k(G;x)=\sum_S x^{|S|}
=\left(\sum_{j=k}^b \binom{b}{j}x^j\right)(1+x)^{N-b}-\binom{b}{k}x^k.
\]
Every inclusion-minimal \(k\)-tuple total dominating set has size exactly \(k+1\). In particular,
\[
\gamma_{\times k,t}(G)=k+1,
\qquad
m_k(G)=\binom{b}{k}(N-b)+\binom{b}{k+1},
\]
where \(m_k(G)\) is the number of minimum \(k\)-tuple total dominating sets and the second binomial coefficient is understood as zero when \(k=b\).

A further consequence is a profile-collapse statement: the complete sequence of all polynomials \(T_k(G;x)\) is determined by only \(N\) and \(b\). Conversely, \(N\) is the largest possible degree in these polynomials and \(b\) is the largest \(k\) for which \(T_k(G;x)\neq0\), so the joint profile determines exactly that pair and no finer creation-block data.

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. The canonical threshold creation string starts with a nonempty \(0\)-block and ends with a nonempty \(1\)-block. Vertices are adjacent precisely when the later-created one is a \(1\)-vertex. The last \(0\)-block is therefore nonempty, every vertex in it has open neighborhood exactly \(B_p\), and every vertex in \(B_p\) is universal.

The parameter \(k\) is a positive integer. If \(k>b\), the last \(0\)-block contains a vertex of degree \(b<k\), so no \(k\)-tuple total dominating set exists. The theorem concerns unweighted all-cardinality enumeration, not the non-uniform total-vector-domination problem.

## Proof
Write \(t=|S\cap B_p|\). First suppose that \(S\) is a \(k\)-tuple total dominating set. A vertex in the last \(0\)-block has neighborhood exactly \(B_p\), hence it must have at least \(k\) selected neighbors there. Therefore \(t\ge k\). Also every selected vertex must itself have at least \(k\) selected neighbors and there are no loops, so necessarily \(|S|\ge k+1\).

Conversely suppose that \(t\ge k\) and \(|S|\ge k+1\). Every vertex outside \(B_p\) is adjacent to every vertex of \(B_p\), hence has at least \(t\ge k\) selected neighbors. An unselected vertex of \(B_p\) is adjacent to all \(t\) selected vertices of \(B_p\). A selected vertex \(v\in B_p\) is universal, so its selected neighbors are exactly \(S\setminus\{v\}\), of cardinality \(|S|-1\ge k\). Hence every vertex has at least \(k\) neighbors in \(S\), proving the characterization.

For the enumerator, first choose \(j\ge k\) vertices from the \(b\)-vertex block \(B_p\), then choose an arbitrary subset outside \(B_p\). This gives
\[
\left(\sum_{j=k}^b\binom{b}{j}x^j\right)(1+x)^{N-b}.
\]
The only counted sets violating \(|S|\ge k+1\) are the \(\binom{b}{k}\) sets consisting of exactly \(k\) vertices of \(B_p\), so subtracting \(\binom{b}{k}x^k\) gives the stated formula.

Every valid set has size at least \(k+1\). If \(t\ge k+1\), it contains a valid \((k+1)\)-subset entirely inside \(B_p\). If \(t=k\), then \(|S|\ge k+1\) supplies a vertex outside \(B_p\), and the \(k\) selected vertices of \(B_p\) together with that vertex form a valid \((k+1)\)-subset. Hence no larger valid set is inclusion-minimal, while every valid set of size \(k+1\) is automatically inclusion-minimal. Counting the two possibilities for a minimum set gives
\[
\binom{b}{k+1}+\binom{b}{k}(N-b).
\]
Finally, the displayed polynomial depends only on \(N\), \(b\), and \(k\). Conversely, \(b\) is the maximum feasible \(k\), and \(N\) is the graph order, proving the profile-collapse statement.

## Verification
The accompanying verifier constructs every connected threshold creation string of orders \(2\) through \(10\), tests every vertex subset against the definition for every \(k\), compares it with the two-condition characterization, compares every polynomial coefficient with the closed formula, and independently checks the inclusion-minimality statement. Its exact replay output is:

`VERIFY_OK graphs=511 subset_k_checks=3378744 coefficient_checks=47102 minimal_checks=344405 max_order=10`

This finite computation is a regression check. The infinite theorem is established by the proof above, not by enumeration.

## Relationship to prior work
Henning and Kazemi define \(k\)-tuple total domination, prove general structural facts about minimal \(k\)-tuple total dominating sets, and identify the problem with a \(k\)-transversal problem in the open-neighborhood hypergraph. Their 2010 paper also treats complete multipartite graphs, but not the threshold-graph all-set enumeration stated here.

Cicalese, Milanič, and Vaccaro place \(k\)-tuple total domination inside total vector domination. Their threshold-graph section records that minimum total vector domination is polynomial-time solvable on threshold graphs (indeed linear time through strongly chordal methods) while developing a separate exact algorithm for vector domination. This optimization coverage does not classify every feasible uniform \(k\)-tuple total dominating set, give the coefficient formula above, or imply the profile collapse.

Chiarelli and Milanič show that threshold graphs are hereditary total domishold for ordinary total domination. That concerns the \(k=1\) feasibility family through a separating weight function and does not cover uniform multiplicity \(k\ge2\) or the all-cardinality formula. Chaluvaraju and Chaitra introduce the ordinary total domination polynomial as a counting invariant and study general properties and graph operations; that work supplies enumerative context but not the threshold formula above.

## Limitations
The theorem is specific to connected threshold graphs and uniform open-neighborhood requirements. It does not solve non-uniform total vector domination, weighted counting, disconnected threshold graphs with isolated vertices, or \(k\)-tuple domination based on closed neighborhoods. Exhaustive verification reaches order \(10\) only and is not an infinite certificate. Search and full-text inspection did not reveal an equivalent published threshold-graph enumeration, but weak indexing or alternate terminology remains a bibliographic risk.

## References
1. M. A. Henning and A. P. Kazemi, “\(k\)-tuple total domination in graphs,” *Discrete Applied Mathematics* 158 (2010), 1006–1011. DOI: 10.1016/j.dam.2010.01.009.
2. F. Cicalese, M. Milanič, and U. Vaccaro, “On the approximability and exact algorithms for vector domination and related problems in graphs,” arXiv:1012.1529; later *Discrete Applied Mathematics* (2012).
3. N. Chiarelli and M. Milanič, “Total Domishold Graphs: a Generalization of Threshold Graphs, with Connections to Threshold Hypergraphs,” arXiv:1303.0944.
4. B. Chaluvaraju and V. Chaitra, “Total Domination Polynomial of A Graph,” *Journal of Informatics and Mathematical Sciences* 6 (2014), 87–92. DOI: 10.26713/jims.v6i2.256.
