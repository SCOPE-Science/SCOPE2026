# Restrained Roman domination polynomial of complete multipartite graphs

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), partite classes \(V_1,\ldots,V_r\), and \(N=\sum_i n_i\). A restrained Roman dominating function is a map \(f:V(G)\to\{0,1,2\}\) in which every vertex labeled \(0\) has both a neighbor labeled \(2\) and a neighbor labeled \(0\).

For each part write
\[
z_i=|V_i\cap f^{-1}(0)|,\qquad t_i=|V_i\cap f^{-1}(2)|,
\]
and put \(Z=\sum_i z_i\) and \(T=\sum_i t_i\). Then \(f\) is restrained Roman dominating if and only if
\[
z_i>0\quad\Longrightarrow\quad Z-z_i>0\ \text{ and }\ T-t_i>0
\]
for every \(i\).

This characterization gives the complete weight enumerator
\[
R_{rR}(G;x)=\sum_f x^{\sum_{v\in V(G)}f(v)}.
\]
For \(i\in[r]\), define
\[
A_i(x)=(1+x+x^2)^{n_i}-(x+x^2)^{n_i},\qquad
C_i(x)=(1+x)^{n_i}-x^{n_i},\qquad
P_i(x)=(x+x^2)^{n_i}.
\]
For \(Q\subseteq[r]\) with \(|Q|\ge2\), define
\[
T_Q(x)=\prod_{i\in Q}A_i(x)\prod_{i\notin Q}P_i(x),
\]
\[
B_{Q,i}(x)=A_i(x)\prod_{j\in Q\setminus\{i\}}C_j(x)\prod_{j\notin Q}x^{n_j}
\quad(i\in Q),
\]
and
\[
C_Q(x)=\prod_{i\in Q}C_i(x)\prod_{j\notin Q}x^{n_j}.
\]
Then
\[
R_{rR}(G;x)
=(x+x^2)^N+
\sum_{\substack{Q\subseteq[r]\\|Q|\ge2}}
\left(T_Q(x)-\sum_{i\in Q}B_{Q,i}(x)+(|Q|-1)C_Q(x)\right).
\]

As a coefficient-level corollary, if \(m=\min_i n_i\), then
\[
\gamma_{rR}(G)=
\begin{cases}
N,&r=2\text{ and }m=1,\\
4,&r=2\text{ and }m\ge2,\\
\min\{4,m+1\},&r\ge3.
\end{cases}
\]

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. Every part has positive size and \(r\ge2\). The polynomial counts all restrained Roman dominating functions by weight, not only minimum functions. The scalar minimum formula is included as a consequence of the all-function classification and is not used as evidence for originality.

## Proof
A vertex in \(V_i\) is adjacent precisely to the vertices outside \(V_i\). Hence a zero-labeled vertex in \(V_i\) has a zero-labeled neighbor exactly when \(Z-z_i>0\), and it has a 2-labeled neighbor exactly when \(T-t_i>0\). This proves the stated characterization.

For the polynomial, first consider labelings with no zeros. Every vertex is labeled \(1\) or \(2\), giving \((x+x^2)^N\).

Now fix the set \(Q\) of parts that contain at least one zero. The zero-neighbor condition forces \(|Q|\ge2\). Ignoring the 2-neighbor condition, the weight enumerator for labelings with zero-support exactly \(Q\) is \(T_Q(x)\): a part in \(Q\) has at least one zero, while a part outside \(Q\) has no zero.

For \(i\in Q\), let \(E_i\) be the bad event that no vertex labeled \(2\) lies outside \(V_i\). Its enumerator is \(B_{Q,i}(x)\). If \(i\ne j\) are in \(Q\), then \(E_i\cap E_j\) forces the complete absence of label \(2\), because a 2-label would have to lie simultaneously in two disjoint parts. Thus every intersection of at least two distinct bad events has the same enumerator \(C_Q(x)\). Inclusion-exclusion therefore gives
\[
T_Q(x)-\sum_{i\in Q}B_{Q,i}(x)+(|Q|-1)C_Q(x),
\]
because \(\sum_{k=2}^{|Q|}(-1)^k\binom{|Q|}{k}=|Q|-1\). Summing over \(Q\) proves the polynomial formula.

For the minimum, suppose first that \(r=2\). If one part is a singleton and any zero occurs, zeros must occur in both parts, but the singleton would then have to be simultaneously labeled \(0\) and \(2\); hence no zero is possible and the minimum is \(N\). If both parts have size at least two, any zero-containing function needs a 2-label in each part, so weight at least \(4\), attained by choosing one 2-label in each part and labeling every other vertex \(0\).

Now let \(r\ge3\) and \(m=\min_i n_i\). If \(m=1\), label the singleton vertex \(2\) and every other vertex \(0\), giving weight \(2\). If \(m=2\), label one vertex of a smallest part \(2\), its mate \(1\), and all vertices outside that part \(0\), giving weight \(3\); weight \(2\) is impossible because a zero in the 2-label's part would have no 2-neighbor outside it. If \(m\ge3\), choose one 2-labeled vertex in each of two different parts and label all other vertices \(0\), giving weight \(4\); weight at most \(3\) cannot provide a 2-label outside the part of a forced zero sharing the part of the first 2-label. These cases give \(\min\{4,m+1\}\).

## Verification
The accompanying `verify.py` constructs every nondecreasing complete-multipartite profile of order at most \(9\) with at least two parts. It enumerates every labeling in \(\{0,1,2\}^N\), tests the defining neighborhood conditions directly, compares them with the part-count characterization, independently accumulates the weight histogram, evaluates the closed polynomial formula coefficient by coefficient, and compares the minimum weight with the stated piecewise formula. This finite census is a regression check; the proof above establishes the unrestricted theorem.

## Relationship to prior work
Pushpam and Padmapriea introduced restrained Roman domination in *Transactions on Combinatorics* 4(1) (2015), 1--17, DOI 10.22108/TOC.2015.4395. The indexed abstract gives the same local definition used here and states that the paper initiates the parameter. Later work of Siahpour, Abdollahzadeh Ahangar, and Sheikholeslami studies Nordhaus--Gaddum behavior and graphs with large restrained Roman domination number (DOI 10.1007/s40840-020-00965-0). Padamutham studies complexity on chordal, bipartite, bounded-treewidth, and threshold graphs (DOI 10.1142/S1793830922500963). Ivanović gives a general mixed-integer formulation; its bibliographic classification records MSC 05C69.

The literature and published-record searches recorded in `AUDIT.json` did not identify an arbitrary complete-multipartite all-function characterization or a weight enumerator. The closest prior results concern the scalar parameter, general bounds, or algorithms. The founding full text was not available through the lawful publisher route inspected during this review, so an unindexed family-specific statement there remains a residual bibliographic risk; this does not alter the direct proof.

## Limitations
The claim is restricted to connected complete multipartite graphs. The polynomial counts functions by total Roman weight only; it does not refine simultaneously by the numbers of labels \(0\), \(1\), and \(2\). No claim is made that the scalar minimum formula alone is new. The originality assessment is based on the named searches and inspected accessible materials and is not a proof of absence from all literature.

## References
1. P. Roushini Leely Pushpam and S. Padmapriea, “Restrained Roman domination in graphs,” *Transactions on Combinatorics* 4(1) (2015), 1--17. DOI: 10.22108/TOC.2015.4395.
2. F. Siahpour, H. Abdollahzadeh Ahangar, and S. M. Sheikholeslami, “Some Progress on the Restrained Roman Domination,” *Bulletin of the Malaysian Mathematical Sciences Society*. DOI: 10.1007/s40840-020-00965-0.
3. C. Padamutham, “Complexity aspects of restrained Roman domination in graphs,” *Discrete Mathematics, Algorithms and Applications*. DOI: 10.1142/S1793830922500963.
4. M. Ivanović, “A mixed integer linear programming formulation for restrained Roman domination problem,” 2018; bibliographic record MaRDI Q4682585.
