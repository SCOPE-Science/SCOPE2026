# Zero forcing polynomial of fan graphs
## Finding
For every integer \(m\ge3\), let
\[
F_m=K_1\vee P_m
\]
be the fan graph with universal hub \(h\) and path vertices \(v_1,\ldots,v_m\) in path order. For an initial set \(S\subseteq V(F_m)\), put
\[
R=S\cap\{v_1,\ldots,v_m\}.
\]
Then \(S\) is zero forcing exactly in the following two regimes.

If \(h\in S\), then \(S\) is zero forcing if and only if \(R\) contains an endpoint \(v_1\) or \(v_m\), or contains two consecutive path vertices.

If \(h\notin S\), then \(S\) is zero forcing if and only if at least one of the following holds:

1. \(\{v_1,v_2\}\subseteq R\);
2. \(\{v_{m-1},v_m\}\subseteq R\); or
3. \(\{v_i,v_{i+1},v_{i+2}\}\subseteq R\) for some \(1\le i\le m-2\).

Define
\[
Q_m(x)=\sum_{j\ge0}\binom{m-j-1}{j}x^j.
\]
For the four binary suffix states \(00,01,10,11\), put
\[
T(x)=
\begin{pmatrix}
1&x&0&0\\
0&0&1&x\\
1&x&0&0\\
0&0&1&0
\end{pmatrix},
\qquad
u(x)=\begin{pmatrix}1&x&x&0\end{pmatrix},
\qquad
w=\begin{pmatrix}1\\1\\1\\0\end{pmatrix},
\]
and
\[
A_m(x)=\nu(x)T(x)^{m-2}w.
\]
Then the complete zero forcing polynomial is
\[
\boxed{\mathcal Z(F_m;x)=(1+x)^{m+1}-xQ_m(x)-A_m(x).}
\]
Consequently,
\[
Z(F_m)=2,
\]
and there are exactly four minimum zero forcing sets:
\[
\{h,v_1\},\qquad \{h,v_m\},\qquad
\{v_1,v_2\},\qquad \{v_{m-1},v_m\}.
\]

## Assumptions and scope
All graphs are finite, simple, and undirected. A blue vertex with exactly one white neighbor may force that neighbor blue; an initial blue set is zero forcing when repeated legal forces eventually color every vertex blue. The theorem is stated for \(m\ge3\). The boundary \(m=2\) is \(F_2\cong K_3\), whose minimum zero forcing sets are the three two-vertex subsets.

The polynomial convention is
\[
\mathcal Z(G;x)=\sum_{k=1}^{|V(G)|}z(G;k)x^k,
\]
where \(z(G;k)\) is the number of zero forcing sets of cardinality \(k\). Binomial coefficients outside their ordinary nonnegative range are interpreted as zero. The scalar equality \(Z(F_m)=2\) is not the novelty claim; the retained content is the exact classification of every zero forcing set and the resulting all-cardinality enumerator.

## Proof
First suppose \(h\in S\). Once the hub is blue, a blue path vertex has exactly the same white path neighbors that it would have in the ordinary zero forcing process on \(P_m\). Thus every force available on the path remains available in the fan, and any zero forcing set of \(P_m\) clears the path while the hub stays blue.

Conversely, if \(R\) is not zero forcing on \(P_m\), then the path characterization gives that \(R\) contains neither endpoint and contains no adjacent selected vertices. Hence both \(v_1\) and \(v_m\) are white, so the hub has at least two white neighbors. Every selected internal path vertex has both path neighbors white. Therefore no blue vertex has exactly one white neighbor, and the fan process cannot even start. This proves the hub-selected criterion.

Now suppose \(h\notin S\). While the hub remains white, any blue path vertex already has the hub as a white neighbor. Such a vertex cannot force a path neighbor: if a path neighbor is white, then together with the hub it has at least two white neighbors. Therefore the first force, if one exists, must force \(h\).

An endpoint \(v_1\) can force \(h\) exactly when both \(v_1\) and \(v_2\) are blue, and symmetrically \(v_m\) can force \(h\) exactly when \(v_{m-1}\) and \(v_m\) are blue. An internal vertex \(v_{i+1}\) can force \(h\) exactly when \(v_i,v_{i+1},v_{i+2}\) are all blue. These are precisely the three listed patterns. If none occurs, there is no legal first force. If one occurs, the hub becomes blue; afterward the selected path vertices contain an endpoint or an adjacent pair, so they form a zero forcing set of \(P_m\) and the remaining path clears. This proves the hub-free criterion.

It remains to enumerate. Boyer et al.'s path criterion says that the nonforcing subsets of \(P_m\) are exactly the subsets that omit both endpoints and contain no adjacent vertices. Their weight enumerator is
\[
Q_m(x)=\sum_{j\ge0}\binom{m-j-1}{j}x^j.
\]
Hence the hub-selected zero forcing sets contribute
\[
x\bigl((1+x)^m-Q_m(x)\bigr).
\]

For a hub-free set, encode membership of \(v_1,\ldots,v_m\) by a binary word. The set fails exactly when the word does not begin with \(11\), does not end with \(11\), and contains no substring \(111\). Let \(A_m(x)\) be the weight enumerator of these failed words, where each selected vertex contributes a factor \(x\). With suffix states \(00,01,10,11\), the transition matrix is \(T(x)\). The first two bits may be \(00,01,10\) with weights \(1,x,x\), giving the row vector \(\nu(x)\); the final suffix may be \(00,01,10\), giving the column vector \(w\). Therefore
\[
A_m(x)=\nu(x)T(x)^{m-2}w.
\]
The hub-free zero forcing sets contribute \((1+x)^m-A_m(x)\). Adding both disjoint regimes gives
\[
\mathcal Z(F_m;x)
=x\bigl((1+x)^m-Q_m(x)\bigr)+(1+x)^m-A_m(x)
=(1+x)^{m+1}-xQ_m(x)-A_m(x).
\]
The coefficient of \(x^2\) is four for every \(m\ge3\), represented by the four sets displayed above, and no singleton satisfies either structural criterion. Thus \(Z(F_m)=2\) and the minimum-set count is four.

## Verification
The standalone verifier `verify_fan_zero_forcing.py` constructs \(F_m\), simulates the ordinary zero forcing rule on every subset for \(3\le m\le10\), checks the structural criterion subset by subset, independently evaluates the transfer recurrence for \(A_m(x)\), compares every coefficient of the claimed polynomial, and checks the minimum value and basis count.

A replay of the packaged verifier produced:

`VERIFY_OK m_range=3..10 subset_checks=4080 criterion_checks=4080 coefficient_checks=68 minimum_checks=16 max_order=11`

The finite computation corroborates the theorem but is not used as a proof of the infinite statement.

## Relationship to prior work
The foundational zero forcing paper introduced the standard color-change rule and the parameter \(Z(G)\). Its front matter records public availability on 2007-11-26 and AMS classification 05C50. Boyer et al. later introduced \(\mathcal Z(G;x)\) and proved that a path subset is nonforcing exactly when it omits both path endpoints and contains no adjacent selected vertices; that path result is used explicitly in the enumeration above.

The full text of Boyer et al. was inspected in its specific-family section and searched for the fan alias; it contains formulas for paths, cycles, complete graphs, complete multipartite graphs, wheels, and other families but no occurrence of “fan”. Its generic polynomial framework and path formula do not determine what changes after adding a universal vertex, especially in the hub-free regime.

Later literature on fan graphs found in the search concerns different questions. Hayat et al. study zero forcing for oriented fan graphs, where edge directions change the forcing rule. Kaudan, Taylor, and Narayan use generalized fan notation in a paper on the failed zero forcing number, a maximum nonforcing-set invariant. Neither statement implies the ordinary undirected all-set classification above.

## Limitations
The theorem is specific to the ordinary undirected fan \(K_1\vee P_m\) for \(m\ge3\). It does not claim a formula for generalized fans with several independent universal vertices, directed fans, positive semidefinite or skew zero forcing, propagation time, or failed zero forcing. The exhaustive computation stops at \(m=10\); only the proof establishes the infinite result. Literature searches cannot exclude a poorly indexed source using an uncommon alias, so global novelty is not claimed as formally certified.

## References
AIM Minimum Rank – Special Graphs Work Group. *Zero forcing sets and the minimum rank of graphs*. Linear Algebra and its Applications 428 (2008), 1628–1648. DOI:10.1016/j.laa.2007.10.009.

Kirk Boyer, Boris Brimkov, Sean English, Daniela Ferrero, Ariel Keller, Rachel Kirsch, Michael Phillips, Carolyn Reinhart. *The zero forcing polynomial of a graph*. arXiv:1801.08910v1; Discrete Applied Mathematics 258 (2019), 35–48.

Sakander Hayat, Hafiz Muhammad Afzal Siddiqui, Muhammad Imran, Hafiz Muhammad Ikhlaq, Jinde Cao. *On the zero forcing number and propagation time of oriented graphs*. AIMS Mathematics 6 (2021), 1833–1850. DOI:10.3934/math.2021111.

Chirag Kaudan, Rachel Taylor, Darren A. Narayan. *An Inverse Approach for Finding Graphs with a Failed Zero Forcing Number of k*. Mathematics 11 (2023), 4068. DOI:10.3390/math11194068.
