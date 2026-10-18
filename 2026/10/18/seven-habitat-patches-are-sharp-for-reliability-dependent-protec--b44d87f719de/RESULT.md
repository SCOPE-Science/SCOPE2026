# Seven habitat patches are sharp for reliability-dependent protection-site switches

## Finding
Consider a tree-shaped network of \(n\geq2\) habitat patches. Exactly one selected patch \(v\) is protected and survives with certainty; every other patch survives independently with common probability \(p\in(0,1)\). Success is the event that **all surviving patches form one connected induced subgraph** (the protected patch makes the surviving set nonempty).

**Theorem.** Every tree with at most six vertices admits at least one fixed protection site maximizing success probability for **every** \(p\in(0,1)\). Exactly two of the eleven unlabeled seven-vertex trees lack such a fixed universally optimal site. Up to relabeling, their edge sets and optimal choices are as follows:

* \(A\): edges \(\{01,04,12,23,45,46\}\). Site 4 is uniquely optimal for \(0<p<1/2\); sites 0 and 4 tie for best at \(p=1/2\); site 0 is uniquely optimal for \(1/2<p<1\).
* \(B\): edges \(\{01,04,12,13,45,46\}\). Sites 1 and 4 tie for best for \(0<p<r\), where \(r=(3-\sqrt5)/2\); sites 0, 1 and 4 tie at \(p=r\); site 0 is uniquely optimal for \(r<p<1\).

Thus seven patches are the smallest connected habitat tree on which changing the common survival probability can force a change of protection location. Exactly two tree shapes attain this seven-vertex boundary. The claim is about **protection of one patch**, not design of the entire interaction graph.

## Assumptions and scope
The tree is finite, simple, undirected, and unweighted. Edges do not fail. Patches other than the chosen protected patch have independent identical Bernoulli survival indicators. The protected patch is permanently occupied. The event of interest is full connectivity of the surviving set, rather than survival of a particular path, total connected pairs, or expected surviving area. Statements hold for every real \(0<p<1\). Labels in the displayed edge sets are vertex labels 0 through 6.

For each \(v\), write \(R_v(p)\) for the probability of success when \(v\) is protected. The exact polynomial is
\[
R_v(p)=\sum_{\substack{S\subseteq V(T),\ v\in S\\T[S]\text{ connected}}}p^{|S|-1}(1-p)^{n-|S|}.
\]
This formula is a conditional, vertex-rooted version of the established residual node-connectedness reliability polynomial, not a new definition of node reliability.

## Proof
For every fixed survivor set containing the protected vertex, independence gives the probability \(p^{|S|-1}(1-p)^{n-|S|}\). Summing over precisely the connected sets proves the polynomial formula.

The universal claim through six patches is a finite exact classification. Every labeled tree of order \(n\) corresponds to a Prüfer word of length \(n-2\). The attached program `verify.py` generates all these words for each \(2\leq n\leq7\), reconstructs each tree, and groups trees by a canonical rooted-parenthesis code minimized over all choices of root. Equality of codes is equivalent to tree isomorphism. It obtains, respectively, \(1,1,2,3,6,11\) nonisomorphic trees. For each class, it enumerates all nonempty vertex subsets, tests induced connectivity, and constructs the exact integer-coefficient polynomial \(R_v\) for every vertex. A vertex is certified universally optimal when all its nonzero comparison polynomials \(R_v-R_u\) are positive throughout \((0,1)\); endpoint factors are removed and Sturm root counting plus an exact rational sign test proves those strict signs. Every tree of order at most six has such a vertex. Exactly nine of the eleven seven-vertex classes do; the remaining two classes are isomorphic to \(A\) and \(B\).

The two exceptional classes can be verified independently of the finite enumeration. For tree \(A\), direct connected-set counting gives
\[
R_0(p)-R_4(p)=p(1-p)^3(2p-1).
\]
For \(j\in\{1,2,3,5,6\}\), \(R_0-R_j\) is strictly positive throughout \((0,1)\); the corresponding factors are, in order,
\[
p^2(1-p)^3,\quad p^2(2-p)(1-p)^2,\quad p(1-p)(p^2-p+1),\quad p(1-p)(p^2-p+1)^2,\quad p(1-p)(p^2-p+1)^2.
\]
Likewise \(R_4-R_j\) is strictly positive throughout \((0,1)\): the factors are, respectively,
\[
p(1-p)^4,\quad p(1-p)^2(p^2-p+1),\quad p(2-p)(1-p)(2p^2-2p+1),\quad p(1-p)Q(p),\quad p(1-p)Q(p),
\]
where \(Q(p)=p^4-4p^3+8p^2-6p+2\). With \(t=1-p\), \(Q(p)=t^4+t^2+(1-t)^2>0\). Thus only vertices 0 and 4 can win, and their comparison establishes the switch at \(1/2\).

For tree \(B\), symmetry gives \(R_1=R_4\) and connected-set counting gives
\[
R_0(p)-R_1(p)=-p(1-p)^3(p^2-3p+1).
\]
For any leaf \(j\in\{2,3,5,6\}\),
\[
R_0-R_j=p(1-p)(p^2-p+1)>0,
\]
\[
R_1-R_j=p(1-p)H(p)>0,
\]
where \(H(p)=p^4-5p^3+9p^2-6p+2\). With \(t=1-p\), \(H(p)=t^4+t^3+(1-t)>0\). The only zero of \(p^2-3p+1\) in \((0,1)\) is \(r=(3-\sqrt5)/2\), proving the stated second switch and completeness of both optimizer descriptions.

## Verification
Run `python verify.py` with Python 3 and SymPy. It enumerates \(\sum_{n=2}^7 n^{n-2}\) labeled Prüfer codes, canonicalizes the trees, reconstructs all rooted reliability polynomials from induced-connected subsets, certifies the universal-site inequalities using exact Sturm root counts, identifies the two exceptional shapes, and checks their complete envelopes algebraically. Its final line is `PROTECTED_TREE_RELIABILITY_VERIFY_OK`. The code, including these assertions, is part of this package. No numerical grid or randomized test is used to establish the lower bound or the exact transitions.

## Relationship to prior work
Residual node-connectedness reliability and the connected-set polynomial are established notions. The 1993 study of Colbourn, Satyanarayana, Suffel, and Sutner develops algorithms for node reliability on trees and other restricted graph classes. Goldschmidt, Jaillet, and LaSota (1994) study which graph *topologies* are uniformly most reliable, rather than selecting a permanently surviving vertex of a *fixed* tree. Brown and Mol (2016) study the roots of the standard node-reliability polynomial; Mol's 2016 dissertation and Brown and Mol's 2017 analysis also address the shape and connected-subtree enumeration of unprotected node reliability. The new question keeps the tree fixed and compares the protection-site-specific conditional polynomials over all survival probabilities. A general reliability-computation algorithm does not itself state the sharp seven-vertex optimizer-switch classification.

## Limitations
The result does not cover arbitrary graphs, heterogeneous survival probabilities, multiple protected patches, dependent failures, imperfect edges, or optimization of a different landscape objective. The connection to conservation is a mathematical habitat-network interpretation; it is not an empirical prediction of ecological survival. A relevant 1993 tree-reliability algorithm paper could not be read in full, leaving residual bibliographic risk concerning an equivalent reformulation. The proof and computations have received only a self-review, not independent mathematical audit.

## References
1. J. I. Brown and L. Mol, *On the roots of the node reliability polynomial*, arXiv:1607.08496v1, first publicly submitted 2016-07-28; https://arxiv.org/abs/1607.08496.
2. C. J. Colbourn, A. Satyanarayana, C. Suffel and K. Sutner, *Computing residual connectedness reliability for restricted networks*, Discrete Applied Mathematics 44 (1993), 221–232, doi:10.1016/0166-218X(93)90233-E.
3. O. Goldschmidt, P. Jaillet and R. LaSota, *On reliability of graphs with node failures*, Networks 24 (1994), 251–259; https://web.mit.edu/~jaillet/www/general/networks-pj-94.pdf.
4. L. Mol, *On Connectedness and Graph Polynomials*, PhD dissertation, Dalhousie University (2016); https://central.bac-lac.gc.ca/.item?app=Library&id=TC-NSHD-71408&oclc_number=1033184059&op=pdf.
5. J. I. Brown and L. Mol, *The Shape of Node Reliability*, arXiv:1703.10573v1 (2017); https://arxiv.org/abs/1703.10573.
