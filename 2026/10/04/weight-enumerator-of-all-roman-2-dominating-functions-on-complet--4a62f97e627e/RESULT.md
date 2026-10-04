# Weight enumerator of all Roman \(\{2\}\)-dominating functions on complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge2\), nonempty parts \(V_1,\ldots,V_r\), and \(N=\sum_i n_i\). A Roman \(\{2\}\)-dominating function is a map \(f:V(G)\to\{0,1,2\}\) such that every vertex labeled \(0\) has either a neighbor labeled \(2\) or two distinct neighbors labeled \(1\). Its weight is \(w(f)=\sum_{v\in V(G)}f(v)\). Define the all-function weight enumerator
\[
I_G(x)=\sum_{f}x^{w(f)},
\]
where the sum is over every Roman \(\{2\}\)-dominating function on \(G\).

For each part, put
\[
P_i=(1+x+x^2)^{n_i},\qquad U_i=(1+x)^{n_i},\qquad V_i=(x+x^2)^{n_i},\qquad C_i=(1+x)^{N-n_i}.
\]
Let \(s=|\{i:n_i=1\}|\) and
\[
c_2=|\{i:n_i=2\}|+\binom{s}{2}.
\]
For every integer \(t\) with \(3\le t\le N\), define
\[
q_t=\binom{N}{t}-\sum_{i:t<n_i}\binom{n_i}{t}-\sum_{i:t-1<n_i}\binom{n_i}{t-1}(N-n_i).
\]
Then
\[
\begin{aligned}
I_G(x)={}&(1+x+x^2)^N-(1+x)^N-\sum_i(P_i-U_i)C_i\\
&+\sum_i\Big[(V_i-x^{n_i})C_i+(P_i-U_i-V_i+x^{n_i})(C_i-1-(N-n_i)x)\Big]\\
&+c_2x^2+\sum_{t=3}^N q_t x^t.
\end{aligned}
\]

The coefficient of \(x^k\) is therefore exactly the number of Roman \(\{2\}\)-dominating functions of weight \(k\).

## Assumptions and scope
All graphs here are finite, simple, undirected, and connected. Complete multipartite means that vertices in different parts are adjacent and vertices in the same part are nonadjacent. Thus \(r\ge2\), each \(n_i\ge1\), and \(N\ge2\).

Write \(a_i,b_i,z_i\) for the numbers of vertices of \(V_i\) labeled \(1,2,0\), respectively, and put \(A=\sum_i a_i\), \(B=\sum_i b_i\). Since the open neighborhood of every vertex of \(V_i\) is exactly \(V(G)\setminus V_i\), a labeling is Roman \(\{2\}\)-dominating if and only if
\[
z_i>0\quad\Longrightarrow\quad (B-b_i\ge1)\ \text{or}\ (A-a_i\ge2)
\]
for every part \(i\). This local criterion is the structural core of the formula.

## Proof
Partition all labelings by the number of parts that contain a vertex labeled \(2\).

If label \(2\) occurs in at least two parts, then every zero-labeled vertex sees a label \(2\) outside its own part. Hence every such labeling is valid. The generating function for all labelings is \((1+x+x^2)^N\), the labelings with no \(2\) contribute \((1+x)^N\), and labelings whose \(2\)'s occur in exactly part \(i\) contribute
\[
(P_i-U_i)C_i.
\]
Therefore the contribution from at least two \(2\)-supporting parts is
\[
(1+x+x^2)^N-(1+x)^N-\sum_i(P_i-U_i)C_i.
\]

Now suppose label \(2\) occurs in exactly one part \(V_i\). Every zero outside \(V_i\) sees a \(2\). If \(V_i\) has no zero, its labels are only \(1\) and \(2\), with at least one \(2\), giving \((V_i-x^{n_i})C_i\). If \(V_i\) contains both a zero and a \(2\), its internal generating function is
\[
P_i-U_i-V_i+x^{n_i},
\]
and its zero vertices are defended exactly when there are at least two vertices labeled \(1\) outside \(V_i\). The latter choices contribute \(C_i-1-(N-n_i)x\). This gives the second sum in the theorem.

Finally suppose no vertex is labeled \(2\). Let \(S\) be the set of vertices labeled \(1\), with \(|S|=t\), and let \(a_i=|S\cap V_i|\). A zero in \(V_i\) is defended exactly when \(t-a_i\ge2\). For \(t=0\) or \(t=1\), no labeling is valid. For \(t=2\), every part that meets \(S\) must be completely selected; hence the valid choices are exactly one whole part of size \(2\), or two singleton parts, giving \(c_2\).

For \(t\ge3\), a \(t\)-set fails exactly when some non-full part contains at least \(t-1\) selected vertices. Such a failure has one of two mutually disjoint forms: all \(t\) selected vertices lie in a part with more than \(t\) vertices, or \(t-1\) selected vertices lie in a part with more than \(t-1\) vertices and the last selected vertex lies outside that part. These failures are mutually disjoint across parts when \(t\ge3\). Subtracting them from all \(\binom Nt\) choices gives \(q_t\). Adding the three disjoint regimes proves the formula.

## Verification
The accompanying `verify.py` independently builds every complete multipartite graph determined by an integer partition of each order \(2\le N\le10\). It enumerates all \(3^N\) labelings, checks the Roman \(\{2\}\)-domination definition vertex by vertex, forms the empirical weight enumerator, and compares every coefficient with the closed formula above. It also checks the local count criterion for every labeling. The replay covers 128 part-size profiles and 3,169,350 labelings and terminates with a `VERIFY_OK` line.

The finite replay is a stress test, not the proof for unbounded \(N\); the proof is the disjoint structural decomposition above.

## Relationship to prior work
Chellali, Haynes, Hedetniemi, and McRae introduced Roman \(\{2\}\)-domination and its minimum-weight parameter. A public bibliographic record gives the exact calendar date 2016-05-11, while another public record reports only the earlier month December 2015; no exact day for that earlier month-level record was verified here.

Padamutham and Palagiri determine the minimum Roman \(\{2\}\)-domination number of complete bipartite graphs: for \(K_{r,s}\) with \(r\le s\), it is \(2\), \(3\), or \(4\) according as \(r=1\), \(r=2\), or \(r\ge3\). Their full text then treats minimum-weight computation on chain and threshold graphs. This is scalar optimization coverage; it does not imply the all-function weight enumerator above.

The 2024 survey on Roman \(\{2\}\)-domination describes itself as a broad review of the published literature. Its special-class discussion records the same complete-bipartite minimum values and later variants such as reinforcement on complete multipartite graphs, but does not state an all-function weight enumerator. Searches under both “Roman \(\{2\}\)-domination” and its alias “Italian domination,” together with searches for polynomial, generating-function, enumeration, complete-bipartite, and complete-multipartite formulations, did not locate a stronger statement implying the displayed formula.

## Limitations
The theorem concerns ordinary Roman \(\{2\}\)-dominating functions, not perfect, total, restrained, independent, reinforcement, bondage, or strong variants. The result does not assert that the minimum Roman \(\{2\}\)-domination numbers already known for complete bipartite graphs are new.

The literature comparison cannot exclude poorly indexed theses, non-English sources, or material not surfaced by the searched databases. The dating evidence also contains an earlier month-only December 2015 record for the foundational article but no verified day for that record; 2016-05-11 is therefore used as the earliest exact calendar day verified in the inspected public sources, without inventing a 2015 day.

## References
1. M. Chellali, T. W. Haynes, S. T. Hedetniemi, and A. A. McRae, “Roman {2}-domination,” *Discrete Applied Mathematics* 204 (2016), 22–28. DOI: 10.1016/j.dam.2015.11.013.
2. C. Padamutham and V. S. R. Palagiri, “Complexity of Roman {2}-domination and the double Roman domination in graphs,” *AKCE International Journal of Graphs and Combinatorics* 17 (2020), 1081–1086. DOI: 10.1016/j.akcej.2020.01.005.
3. A. Almulhim, B. Al Subaiei, and S. R. Mondal, “Survey on Roman {2}-Domination,” *Mathematics* 12 (2024), 2771. DOI: 10.3390/math12172771.
