# Complete purchaser-count spectrum for uniform sharing on balanced bipartite networks
## Finding
For every integer \(n\ge 2\), consider the complete bipartite network \(K_{n,n}\) with a uniform integer nomination capacity \(1\le k\le n\). Let \(\mathcal E(n,k)\) be the set of all numbers of purchasing agents across specialised pure Nash equilibria of the capacitated-sharing public-goods model, equivalently all cardinalities of \(D\)-sets in its DP-Nash subgraphs.

For \(k=n\),
\[
\mathcal E(n,n)=\{n\}.
\]
For \(1\le k<n\), define
\[
a(n,k)=\min\left\{2\left\lceil\frac{n}{k+1}\right\rceil,\quad 2\left\lceil\frac{n-1}{k+1}\right\rceil+1\right\}.
\]
Then the **complete attainable-cardinality spectrum** is
\[
\boxed{\mathcal E(n,k)=\{n\}\cup\{a(n,k),a(n,k)+1,\ldots,2(n-k)\}.}
\]
Every listed cardinality is attained and no other cardinality is possible. In particular, for every \(n\ge4\),
\[
\mathcal E(n,n-1)=\{2,n\},\qquad \mathcal E(n,n)=\{n\}.
\]
Thus a connected, \(n\)-regular interaction network can have two specialised equilibrium purchasing levels with an arbitrarily long *forbidden interval*, and raising everyone's sharing capacity by just one (from \(n-1\) to \(n\)) forces the minimum number of purchasers to jump from \(2\) to \(n\). The claim is about equilibrium purchaser counts, not about all preference-dependent welfare rankings.

## Assumptions and scope
The vertex set of \(G=K_{n,n}\) is partitioned into two independent sets \(L\) and \(R\) of \(n\) vertices each, with every cross-edge present. Every player has capacity \(k\), and in a DP-Nash subgraph the vertex set is partitioned into purchasers \(D\) and nonpurchasers \(P\). The subgraph contains only \(D\)-to-\(P\) edges. Every purchaser has **exactly** \(k\) incident subgraph edges (because the graph degree is \(n\ge k\)), and every nonpurchaser is incident to at least one such edge. Edges from \(D\) to \(P\) encode nominations by purchasing agents, so a purchaser never relies on a nomination from another purchaser. The initiating model proves that these objects induce specialised pure Nash equilibria with purchaser set \(D\). The formula classifies all possible such purchaser-set cardinalities; it does not presume a unique equilibrium.

## Proof
Set \(p=|D\cap L|\) and \(q=|D\cap R|\).

**One-sided purchaser sets.** If \(q=0\), an unpurchasing vertex in \(L\) would have no purchasing neighbour: all its neighbours lie in \(R\), which has no purchasers. Thus \(p=n\). Conversely, \((p,q)=(n,0)\) is feasible, because the \(n\) left purchasers each have \(n\) right nonpurchasers available, may each nominate \(k\) of them, and these nominations can cover all \(n\) right vertices. The case \((p,q)=(0,n)\) is symmetric. Hence all one-sided equilibria have \(n\) purchasers.

**Mixed purchaser sets.** Suppose \(p,q\ge1\). The right nonpurchaser set has size \(n-q\), so the \(p\) left purchasers can each nominate exactly \(k\) distinct right nonpurchasers while collectively covering all of them if and only if
\[
k\le n-q\quad\text{and}\quad pk\ge n-q.
\]
Indeed, necessity follows from the individual nomination limit and collective coverage. For sufficiency, label the \(r=n-q\) right nonpurchasers \(0,\ldots,r-1\), and give left purchaser indexed \(i\), for \(0\le i<p\), the \(k\) nominations
\[
(ik+j)\bmod r,\qquad j=0,\ldots,k-1.
\]
Since \(k\le r\), each purchaser selects distinct recipients. Since \(pk\ge r\), the consecutive integer list \(0,\ldots,pk-1\) covers all residues modulo \(r\). The reverse-direction nominations are independent and feasible exactly when \(k\le n-p\) and \(qk\ge n-p\).

Thus mixed purchaser sets exist exactly for the integer solutions
\[
1\le p,q\le n-k,\qquad kp+q\ge n,\qquad p+kq\ge n. \tag{1}
\]
With \(s=p+q\), the two final inequalities in (1) are jointly equivalent to
\[
s+(k-1)\min\{p,q\}\ge n.
\]
For fixed \(s\), if \(2\le s\le 2(n-k)\), the balanced choice \(p=\lceil s/2\rceil\), \(q=\lfloor s/2\rfloor\) obeys \(1\le p,q\le n-k\) and maximises \(\min\{p,q\}\). Consequently, a mixed purchaser set of size \(s\) exists **if and only if**
\[
2\le s\le 2(n-k),\qquad s+(k-1)\left\lfloor\frac{s}{2}\right\rfloor\ge n. \tag{2}
\]
The left-hand side of the final inequality in (2) increases strictly with \(s\). For even \(s=2h\), the condition is \((k+1)h\ge n\); for odd \(s=2h+1\), it is \((k+1)h+1\ge n\). Hence the first candidate size is precisely \(a(n,k)\), the minimum of the first feasible even and odd sizes displayed in the finding. The upper endpoint is itself feasible, because
\[
2(n-k)+(k-1)(n-k)=(k+1)(n-k)\ge n,
\]
where the last difference is \(k(n-k-1)\ge0\) for \(1\le k<n\). All integers from \(a(n,k)\) through \(2(n-k)\) therefore occur; none outside this interval can be mixed equilibrium counts. Adding the one-sided size \(n\) proves the formula for \(k<n\).

Finally, when \(k=n\), every purchaser must nominate all its neighbours, requiring all of them to be nonpurchasers. Thus purchasers cannot occupy both sides simultaneously, and the only feasible purchaser sets are \(L\) and \(R\), both of cardinality \(n\). This proves the remaining case. At \(k=n-1\), (2) allows only \(s=2\), establishing the two-point spectrum and the capacity-jump assertion.

## Verification
The standalone file `verify_spectrum.py` enumerates exact nomination subsets for every ordered buyer-partition count at \(2\le n\le8\), every \(1\le k\le n\), and computes the resulting feasible purchaser-count spectrum **without using inequality (1)**. It agrees with the closed formula in all \(35\) parameter pairs. This is a finite consistency check; the unrestricted theorem is proved by the explicit nomination construction and inequalities above.

To reproduce: run `python3 verify_spectrum.py` with a standard Python 3 interpreter. In particular the script independently finds purchaser counts \(\{2,4\}\) when \((n,k)=(4,3)\) and \(\{2,8\}\) when \((n,k)=(8,7)\).

## Relationship to prior work
Gerke, Gutin, Hwang and Neary introduced the underlying capacities-and-nominations public-goods model, and established the correspondence between its specialised equilibria and DP-Nash subgraphs. Their Appendix C derives general lower and upper bounds on the extreme purchaser counts and sharp bounds for complete **graphs**; their examples of efficiency loss under greater sharing capacity use other network structures. Neither the general bounds nor the complete-graph formulas entail the attainable purchaser-count spectrum on \(K_{n,n}\).

Gutin, Neary and Yeo studied the computational complexity of uniqueness for DP-Nash subgraphs and for purchaser sets, not this fixed-family cardinality classification. Deligkas, Gutin, Jones, Neary and Yeo established a maximum-matching formula for minimum purchasers when the capacity is one in a related directed setting. Thus no originality is asserted for the capacity-one minimum alone; the contribution is the exact **all-capacity, all-cardinality** spectrum, its forbidden intervals, and the sharp adjacent-capacity jump on regular bicliques.

Related published graph parameters, including released packing and \(k\)-limited domination on bipartite graphs, impose different neighborhood restrictions and do not directly classify exact-degree DP-Nash subgraphs.

## Limitations
The theorem concerns balanced complete bipartite networks with a uniform positive integer capacity and specialised pure equilibria. It does not classify unbalanced bicliques, nonuniform capacity vectors, arbitrary graphs, nonspecialised continuous-production equilibria, or welfare effects beyond purchaser counts. The theoretical proof is general in \(n\), while the computational check covers only \(n\le8\). An equivalent characterisation in older literature under a different name has not been ruled out by any exhaustive bibliographic theorem.

## References
1. S. Gerke, G. Gutin, S.-H. Hwang and P. Neary, “Public goods in networks with constraints on sharing,” arXiv:1905.01693; first public 5 May 2019; 2023 version, Definition 3, Theorem 1, Appendix C. https://arxiv.org/abs/1905.01693
2. G. Gutin, P. Neary and A. Yeo, “Exact capacitated domination: on the computational complexity of uniqueness,” arXiv:2003.07106; first public 16 March 2020. https://arxiv.org/abs/2003.07106
3. A. Deligkas, G. Gutin, M. Jones, P. Neary and A. Yeo, “Public Goods Games in Directed Networks with Constraints on Sharing,” arXiv:2511.11475v1, 14 November 2025, Theorem 9. https://arxiv.org/abs/2511.11475
