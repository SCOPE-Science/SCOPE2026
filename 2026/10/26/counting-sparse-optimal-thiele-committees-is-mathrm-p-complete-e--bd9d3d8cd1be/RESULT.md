# Counting sparse optimal Thiele committees is \(\#\mathrm{P}\)-complete even with known optimum score

## Finding
For any fixed rational scoring sequence \(u\) with \(u(0)=0\), \(u(1)=c>0\), \(u(2)<2c\), and \(u(3)<3c\), counting all optimal size-\(n\) Thiele committees is \(\#\mathrm{P}\)-complete even in approval elections in which every voter approves exactly three candidates and every candidate has exactly two approvers. More specifically, the instances arising from simple cubic bipartite graphs have an **explicitly known optimum** \(2nc\), and each winning committee is exactly a perfect matching. For Proportional Approval Voting (PAV), \(u(j)=H_j\) and \(c=1\).

## Assumptions and scope
Let \(n\ge3\), and let \(G=(L\sqcup R,E)\) be a finite **simple**, undirected, \(3\)-regular bipartite graph, with \(|L|=|R|=n\). Create one voter \(v_x\) for each \(x\in L\sqcup R\), and a distinct candidate \(c_e\) for each \(e\in E\). Voter \(v_x\) approves precisely the candidates \(c_e\) for edges incident to \(x\). Set the committee size to \(k=n\). Therefore there are \(2n\) voters and \(3n\) candidates, every voter has precisely three approvals, and every candidate has precisely two supporters. An admissible committee \(W\subseteq E\) has \(|W|=n\); define \(d_W(x)=|\{e\in W:x\in e}\}|\in\{0,1,2,3}\}\). Its Thiele score is
\[
\Phi_u(W)=\sum_{x\in L\sqcup R}u(d_W(x)).
\]
The fixed rule \(u:\{0,1,2,3}\}\to\mathbb Q\) obeys \(u(0)=0\), \(u(1)=c>0\), \(u(2)<2c\), and \(u(3)<3c\). No values beyond three are relevant. The counting problem concerns **all** optimal committees without tie-breaking. Inputs are finite and binary encoded.

## Proof
**1. Sharp score inequality.** For \(d\in\{0,1,2,3}\}\), the hypotheses imply
\[
 u(d)\le cd,\qquad u(d)=cd\iff d\in\{0,1}\}.
\]
Every selected candidate corresponds to an edge with exactly two endpoints. Double counting gives \(\sum_xd_W(x)=2|W|=2n\). Hence
\[
\Phi_u(W)\le c\sum_xd_W(x)=2nc.
\]
Equality holds precisely when no voter has two or three selected approved candidates. Since \(2n\) voters receive in total exactly \(2n\) selected approvals, this is equivalent to \(d_W(x)=1\) for **every** vertex. Thus equality occurs if and only if \(W\) is a perfect matching of \(G\).

**2. The bound is attained.** Every cubic bipartite graph has a perfect matching. To see this without assuming connectivity, for any \(S\subseteq L\), degree counting yields \(3|S|=e(S,N(S))\le3|N(S)|\), hence \(|N(S)|\ge|S|\). Hall's theorem provides a matching covering \(L\), and because the shores both contain \(n\) vertices, it covers \(R\) too. Its committee attains \(\Phi_u=2nc\). We have proved the exact equivalence
\[
 W\text{ is an optimal size-}n\text{ committee}\quad\Longleftrightarrow\quad W\text{ is a perfect matching of }G.
\]
The identification \(e\leftrightarrow c_e\) is one-to-one: no distinct graph matching produces the same committee.

**3. Counting complexity.** Given a simple cubic bipartite graph, the above election can be constructed in time polynomial in \(|V(G)|\), and the number of optimal committees is **exactly** the number of perfect matchings of that graph. Counting perfect matchings of simple cubic bipartite graphs is a classical \(\#\mathrm{P}\)-complete problem (Dagum and Luby, 1992), so this is a parsimonious hardness transformation. Conversely, in the stated rigid subclass, a nondeterministic polynomial-time counting machine guesses an \(n\)-element candidate set exactly once and accepts if and only if all \(2n\) voters have exactly one selected approved candidate; this is a polynomial-time test and counts exactly the optimal committees. Hence the restricted counting problem lies in \(\#\mathrm{P}\) and is \(\#\mathrm{P}\)-complete. A matching algorithm simultaneously finds an optimal committee in polynomial time. For general elections where each candidate has at most two supporters, polynomial-time Thiele winner determination is also known (Lassota and Sornat, 2026).

**4. PAV specialization.** PAV uses \(u(0)=0\), \(u(1)=1\), \(u(2)=3/2\), and \(u(3)=11/6\), so both strict inequalities are satisfied. Thus the optimal PAV score in each constructed instance is exactly \(2n\). For example, \(G=K_{3,3}\) gives \(6\) optimal size-\(3\) committees (one for each of its \(3!\) perfect matchings) among \(\binom{9}{3}=84\) committees.

## Verification
The included stand-alone program `CHECK.py` uses only the Python 3 standard library. Execute `python3 CHECK.py`. It exhaustively scores \(87,837\) committees arising from \(12\) simple cubic bipartite circulant graphs on \(6\) to \(12\) voters. It makes \(351,348\) exact-rational score evaluations under PAV and three additional rational rules meeting the theorem's inequalities. It independently counts perfect matchings by permutations of one bipartition, compares each score maximizer against the matching test, and checks the exact bound for every enumerated committee. The checks passed, including \(6\) winners for \(K_{3,3}\), \(13\) for \(5\)-by-\(5\) circulant examples and \(17\) or \(20\) for \(6\)-by-\(6\) examples. These finite checks do not establish the all-\(n\) result: the inequalities, Hall argument, and parsimonious correspondence above do.

## Relationship to prior work
Ai (2026) proves the unrestricted \(\#\cdot\mathrm{OptP}\)-completeness of counting PAV optima and explicitly identifies the effect of restrictions on approvals as a research direction. Its reduction does not establish the present simultaneously sparse \(2\)-supporter/\(3\)-approval subclass. Lassota and Sornat (2026) prove polynomial-time **winner determination** for at most two approvers per candidate but do not count ties. Janeczko and Faliszewski (2023) prove counting hardness for general Thiele rules and use the edge-candidate/vertex-voter encoding for **greedy** rules; that is close structurally but is not the exact-optimal PAV statement. The invoked hardness of enumerating cubic bipartite perfect matchings is due to Dagum and Luby (1992). In particular, the graph-to-election idea and the source counting problem are **not** claimed as new; the contribution is the exact sparse-optimum counting classification and direct winner-matching equivalence.

## Limitations
The reduction uses exact harmonic or other fixed rational Thiele scores and an input family with unbounded graph size. It does not prove hardness on planar cubic bipartite graphs (indeed planar perfect matchings have efficient counting algorithms), for a fixed committee size, or for rules violating the strict inequalities. The general \(\#\mathrm{P}\)-hardness assertion invokes the previously established graph-counting theorem rather than independently proving its source hardness. Earlier literature could contain this same elementary reduction implicitly or explicitly; historical priority is not certified. There is no independent scientific audit.

## References
1. Yizhou Ai, *The Complexity of Membership, Uniqueness, and Counting for Optimal Proportional Approval Voting Committees*, arXiv:2609.08884, first submitted 2026-09-08, https://arxiv.org/abs/2609.08884.
2. Alexandra Lassota and Krzysztof Sornat, *Algorithms for Structured Elections under Thiele Voting Rules*, AAAI 2026, DOI:10.1609/aaai.v40i20.38757, https://ojs.aaai.org/index.php/AAAI/article/view/38757/42719.
3. Łukasz Janeczko and Piotr Faliszewski, *Ties in Multiwinner Approval Voting*, arXiv:2305.01769, https://arxiv.org/abs/2305.01769.
4. Paul Dagum and Michael Luby, *Approximating the Permanent of Graphs with Large Factors*, Theoretical Computer Science 102(2):283–305 (1992), DOI:10.1016/0304-3975(92)90234-7.
5. Yoshio Okamoto and Ryuhei Uehara, *Counting the Number of Matchings in Chordal and Chordal Bipartite Graph Classes*, https://dopal.cs.uec.ac.jp/okamotoy/PDF/matchchordal.pdf (historical source-theorem corroboration).
