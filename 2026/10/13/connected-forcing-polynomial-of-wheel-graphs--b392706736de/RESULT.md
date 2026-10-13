# Connected-forcing polynomial of wheel graphs
## Finding
For every integer \(n\ge4\), define the wheel \(W_n=K_1\vee C_n\), where the rim is \(C_n\) and the unique vertex outside the rim is the hub \(h\). For each integer \(j\), let \(z_c(W_n;j)\) be the number of connected zero forcing sets of cardinality \(j\), and define
\[
\mathcal C_n(x)=\sum_j z_c(W_n;j)x^j.
\]
A set \(S\subseteq V(W_n)\) is connected forcing if and only if exactly one of the following applicable descriptions holds:

1. \(h\in S\), and \(S\cap V(C_n)\) is not an independent set of the rim cycle; equivalently, it contains an edge of \(C_n\).
2. \(h\notin S\), \(S\) induces a connected subgraph of \(C_n\), and \(|S|\ge3\).

Let
\[
I(C_n;x)=\sum_{k=0}^{\lfloor n/2\rfloor}i_{n,k}x^k
\]
be the independence polynomial of the rim cycle. Here \(i_{n,0}=1\), and for \(1\le k\le\lfloor n/2\rfloor\),
\[
i_{n,k}=\frac{n}{n-k}\binom{n-k}{k}.
\]
Then
\[
\mathcal C_n(x)=x\big((1+x)^n-I(C_n;x)\big)+n\sum_{j=3}^{n-1}x^j+x^n.
\]
Equivalently, for \(1\le j\le n+1\),
\[
z_c(W_n;j)=\binom{n}{j-1}-i_{n,j-1}+n\mathbf 1_{\{3\le j\le n-1\}}+\mathbf 1_{\{j=n\}},
\]
where \(i_{n,k}=0\) outside \(0\le k\le\lfloor n/2\rfloor\). In particular,
\[
Z_c(W_n)=3,\qquad z_c(W_n;3)=2n,
\]
and the total number of connected forcing sets is
\[
2^n-I(C_n;1)+n(n-3)+1.
\]
If \(F_0=0\) and \(F_1=1\) are the Fibonacci initial values, then \(I(C_n;1)=F_{n-1}+F_{n+1}\), so the total can also be written as
\[
2^n-F_{n-1}-F_{n+1}+n(n-3)+1.
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. The zero forcing rule is the standard color-change rule: a blue vertex with exactly one white neighbor forces that neighbor blue. A connected forcing set is a zero forcing set whose induced subgraph is connected. The notation \(W_n\) in this result uses rim order \(n\), so \(|V(W_n)|=n+1\); this convention is stated explicitly because some literature indexes wheels by total order.

The result is an all-cardinality classification. The finite computation supplied with the package is a consistency check for small wheels and is not used as an infinite proof.

## Proof
Write the rim vertices cyclically as \(v_0,\ldots,v_{n-1}\).

First suppose \(h\in S\), and put \(R=S\cap V(C_n)\). Connectivity is automatic. If \(R\) contains adjacent rim vertices, choose a maximal cyclic run of blue rim vertices containing an adjacent pair. If the whole rim is already blue there is nothing to prove. Otherwise an endpoint of that run has the hub and its inward rim neighbor blue and has exactly one white neighbor, namely the next rim vertex outside the run. It forces that vertex. Repeating this boundary force grows the run until the entire rim is blue. Hence \(S\) is zero forcing.

Conversely, suppose \(R\) is independent. Every blue rim vertex then has both rim neighbors white. Since an independent set in \(C_n\), with \(n\ge4\), has size at most \(\lfloor n/2\rfloor\), the blue hub has at least two white rim neighbors. Thus no blue vertex can make the first force, so \(S\) is not zero forcing. This proves the first case.

Now suppose \(h\notin S\). Since \(S\) is required to be connected and lies entirely on the rim, either \(S=V(C_n)\) or \(S\) is a consecutive rim arc. If \(|S|\ge3\), choose an internal vertex of such an arc; when the whole rim is selected choose any rim vertex. That vertex has both rim neighbors blue and the hub white, so it forces the hub. If the rim is not already entirely blue, the now-blue hub leaves an endpoint of the selected rim arc with exactly one white neighbor, and boundary forcing propagates around the rim. Thus every connected rim set of size at least three is forcing.

If instead \(|S|=1\), the sole blue rim vertex has three white neighbors. If \(|S|=2\), connectivity makes the two selected rim vertices adjacent, and each has two white neighbors: the hub and its outer rim neighbor. No first force is possible. This proves the second case.

For enumeration with the hub selected, the admissible rim traces are exactly all rim subsets except independent sets, giving
\[
x\big((1+x)^n-I(C_n;x)\big).
\]
Without the hub, every proper connected rim subset of size \(j\) is a cyclic interval, of which there are exactly \(n\) for each \(3\le j\le n-1\), while the full rim contributes one set of size \(n\). This gives the remaining two terms in \(\mathcal C_n(x)\).

For completeness, the coefficient of \(x^k\) in \(I(C_n;x)\) can be counted directly. For \(k\ge1\), mark one chosen rim vertex in an independent \(k\)-set. Starting at the marked vertex, the \(k\) positive gaps of unchosen vertices around the cycle sum to \(n-k\), so there are \(\binom{n-k-1}{k-1}\) gap compositions and \(n\) choices for the marked starting vertex. Each independent set is counted once for each of its \(k\) possible marks. Hence
\[
i_{n,k}=\frac{n}{k}\binom{n-k-1}{k-1}=\frac{n}{n-k}\binom{n-k}{k}.
\]
The minimum-size and total-count formulas follow by taking the coefficient of \(x^3\) and evaluating \(\mathcal C_n(1)\), respectively.

## Verification
The accompanying checker constructs \(W_n\) directly, tests every vertex subset for induced connectivity and the standard zero forcing rule, compares those outcomes with the two-case classification, and compares the full cardinality distribution with the closed formula. It exhaustively checks rim orders \(4\le n\le11\). The analytic proof above establishes the result for every \(n\ge4\); the computation is only a finite cross-check.

## Relationship to prior work
Connected forcing was introduced in 2016. The full text of Brimkov and Davila's introduction paper develops the parameter and several graph families but does not treat wheels. Brimkov's 2016 complexity paper likewise develops structural results and exact connected forcing numbers for unicyclic, cactus, and block-graph families; its full text has no occurrence of “wheel.”

Brimkov, Davila, and Schuerger later introduced the cardinality notation \(z_c(G;i)\) and explicitly studied counts of connected forcing sets. Their wheel proposition proves that wheels are connected-forcing dense and that their connected forcing number is \(3\), exhibiting hub-plus-adjacent-rim minimum sets. It does not classify all wheel connected forcing sets, count the second rim-only class of minimum sets, or give the all-cardinality enumerator. Their general extremal-size formulas determine only a few top coefficients for arbitrary graphs, not the wheel polynomial above.

Thus the scalar equality \(Z_c(W_n)=3\) is treated as prior work. The contribution here is the complete two-regime structural classification and the resulting exact all-cardinality enumerator, including the exact minimum-set count \(2n\).

## Limitations
The result is specific to wheels in the rim-order convention \(W_n=K_1\vee C_n\). It does not claim an analogous formula for arbitrary cones or joins. The literature comparison found no prior all-cardinality wheel enumeration, but an obscure or poorly indexed source could still exist. The supplied checker covers only \(4\le n\le11\) and cannot replace the all-orders proof.

## References
B. Brimkov and R. Davila, “Characterizations of the Connected Forcing Number of a Graph,” arXiv:1604.00740, first submitted 2016-04-04.

B. Brimkov, “Complexity and Computation of Connected Zero Forcing,” arXiv:1607.00658, first submitted 2016-07-03. The arXiv record lists MSC 05C15.

R. Davila, M. A. Henning, C. Magnant, and R. Pepper, “Bounds on the Connected Forcing Number of a Graph,” Graphs and Combinatorics 34 (2018), 1159–1174, DOI: 10.1007/s00373-018-1957-x. The published front matter lists MSC 05C69 and 05C50.

B. Brimkov, R. Davila, and H. Schuerger, “Connected forcing density and related problems,” arXiv:2507.11194, first submitted 2025-07-15.
