# Three-step edge-parity extinction and a part-count Jordan law for even multipartite graphs

## Finding

For every integer \(r\ge2\) and even integers \(n_1,\ldots,n_r\ge2\), let \(G=K_{n_1,\ldots,n_r}\) be the complete multipartite graph. Its line graph \(L(G)\) has one vertex for each edge of \(G\), and adjacent vertices correspond to edges sharing an endpoint. Consider the synchronous binary rule \(x(t+1)=Fx(t)\), where \(F\) is the adjacency operator of \(L(G)\) over \(\mathbb F_2\), with no self-state included. Write
\[
N=\sum_{i=1}^r n_i,\qquad E=\sum_{i<j}n_i n_j,\qquad
c=r-1-\mathbf1_{\{r\text{ even}\}}.
\]
Then \(F^3=0\), and the complete nilpotent Jordan form of \(F\) has exactly
\[
\begin{aligned}
&c&&\text{blocks of length }3,\\
&N-2-2c&&\text{blocks of length }2,\\
&E-2N+4+c&&\text{blocks of length }1.
\end{aligned}
\]
In particular \(\operatorname{rank}F=N-2\), \(\operatorname{rank}F^2=c\), and \(\operatorname{rank}F^3=0\).

If \(H_t\) counts initial configurations whose trajectory is zero after at most \(t\) updates, the **exact extinction-depth census** is
\[
(H_0,H_1,H_2,H_3)=
\left(1,2^{E-N+2},2^{E-c},2^E\right).
\]
The sharp worst-case extinction depth equals two when \(r=2\) and three when \(r\ge3\). For \(r\ge3\), precisely \(1-2^{-c}\) of all initial configurations need all three updates. Thus the last-step fraction depends only on the number of parts; it is \(3/4\) for three or four parts, and \(15/16\) for five or six parts, regardless of their even sizes. For two parts the fraction requiring two steps is \(1-2^{-(N-2)}\).

## Assumptions and scope

The graph is finite, undirected, simple, and complete between distinct nonempty vertex classes, with no edges within a class. Each class has **even cardinality at least two**. The state consists of one bit per **edge of the underlying multipartite graph**, not one bit per original vertex. At every discrete step, each edge-site becomes the XOR of its incident neighboring edge-sites; the edge's own bit is excluded. Every rank, kernel and Jordan statement is over \(\mathbb F_2\). Extinction time for a given initial state is the least integer \(t\ge0\) for which its \(t\)-th iterate is zero. The zero configuration is the sole periodic state, by the established nilpotence. No assertion is made for odd-sized classes or nonbinary alphabets.

## Proof

**1. Incidence factorization.** Let \(B\) be the \(N\)-by-\(E\) unsigned incidence matrix, with one \(1\) at each endpoint of an edge. Each edge column has exactly two \(1\)'s. Therefore the diagonal of \(B^{\mathsf T}B\) vanishes modulo two; two distinct edge columns have inner product one exactly when their edges meet. Hence
\[
F=B^{\mathsf T}B.
\]
Also \(Q:=BB^{\mathsf T}=D+A_G\) over \(\mathbb F_2\), where \(D\) is the degree diagonal and \(A_G\) is the original graph's adjacency. Every vertex in part \(i\) has degree \(N-n_i\), which is even, so \(D=0\) and \(Q=A_G\).

**2. First rank.** Since \(G\) is connected, the columns of \(B\) span precisely the even-coordinate-sum subspace
\[
W=\{y\in\mathbb F_2^N:\sum_v y_v=0\},
\qquad \dim W=N-1.
\]
For completeness, a spanning tree's incidence columns span all pair differences, which in characteristic two are the vectors \(e_u+e_v\) generating \(W\). Moreover \(B^{\mathsf T}y=0\) says \(y_u+y_v=0\) for every edge, hence connectivity gives \(\ker B^{\mathsf T}=\langle\mathbf1_N\rangle\). Since \(N\) is even, \(\mathbf1_N\in W\). By rank-nullity on \(W\),
\[
\operatorname{rank}F=\dim B^{\mathsf T}(W)=N-2.
\]

**3. Second rank and the parity loss.** For \(y\in W\), let \(s_i=\sum_{v\in V_i}y_v\). Then \(\sum_i s_i=0\). At every vertex of part \(i\),
\[
(Qy)_v=\sum_{j\ne i}s_j=s_i.
\]
Every vector \((s_1,\ldots,s_r)\) of even total parity occurs from some \(y\in W\): choose a single representative vertex from each part and assign it bit \(s_i\). Consequently \(Q(W)\) is the \((r-1)\)-dimensional space of part-constant vectors with part values summing to zero. Its intersection with \(\ker B^{\mathsf T}=\langle\mathbf1_N\rangle\) is the whole one-dimensional line when \(r\) is even and is zero when \(r\) is odd. Using \(F^2=B^{\mathsf T}QB\) and surjectivity \(B:\mathbb F_2^E\twoheadrightarrow W\) gives
\[
\operatorname{rank}F^2=(r-1)-\mathbf1_{\{r\text{ even}\}}=c.
\]
This one-dimensional loss for an even number of parts produces the adjacent even/odd part-count plateaus.

**4. Nilpotence.** Because all \(n_i\) are even, any part-constant vector has sum zero on each part; thus \(Q\) annihilates every part-constant vector, in particular \(Q(W)\). Hence \(Q^2B=0\), so
\[
F^3=B^{\mathsf T}Q^2B=0.
\]

**5. Jordan blocks and state counts.** For a nilpotent operator of index at most three, let \(b_j\) be the multiplicity of Jordan blocks of size \(j\). Then \(\operatorname{rank}F^2=b_3\) and \(\operatorname{rank}F=b_2+2b_3\), while \(E=b_1+2b_2+3b_3\). Substituting the three proven ranks gives the stated \(b_3,b_2,b_1\), all nonnegative as they are actual Jordan multiplicities. Since \(\ker F^t\) has dimension \(E-\operatorname{rank}F^t\), its cardinality gives \(H_t\). When \(r=2\), \(c=0\) and \(N-2>0\), so \(F^2=0\ne F\); the sharp depth is two. When \(r\ge3\), \(c\ge2\), so \(F^2\ne0\) and the sharp depth is three. In that case the maximal-depth population is \(2^E-H_2\), yielding the announced fraction \(1-2^{-c}\). Every quantifier above ranges over all permitted part counts and sizes, not over a finite checked sample.

## Verification

A standalone Python 3 standard-library program, `verify.py`, independently constructs the adjacency matrix of the line graph directly from common endpoints, without using the incidence factorization. Binary Gaussian elimination establishes all predicted ranks and the zero third power on \(164\) ordered class-size profiles with two to six parts, each part having size \(2\), \(4\), or \(6\), and total order at most \(16\). This supplies \(492\) exact rank comparisons. The verifier also simulates every initial bit vector on six small line graphs, totaling \(12{,}816\) configurations, and checks their complete extinction-depth distributions. Run `python3 verify.py`. The recorded diagnostic is `LINE_GRAPH_EVEN_PARTS_VERIFY_OK graphs= 164 rank_checks= 492 exhaustive_graphs= 6 exhaustive_states= 12816`. These finite computations corroborate the implementation and examples, while the unrestricted theorem rests solely on Proof Steps 1–5.

## Relationship to prior work

The identity expressing line-graph adjacency as an incidence Gram matrix up to the degree-two diagonal is standard; for characteristic two the diagonal disappears. Abudayah, Alomari and Sander discuss incidence matrices and line graphs, but not these finite-field nilpotent Jordan blocks. Pasqualetti, Borra and Bullo study finite-field synchronous network dynamics and criteria for finite-time convergence, but do not calculate this line-graph family or its exact extinction-depth strata. Berman, Borer and Hungerbühler study Lights Out on graphs, which uses a different self-inclusive button-pushing operator and solves reachability rather than iterated zero-extinction. A published finite-field parity result for **the original** complete multipartite graph gives cycle counts for its vertex-update operator; its vertex state space and operator differ from the line-graph edge-update operator studied here. The present incidence-image restriction and the one-dimensional parity loss at even part count establish edge-space Jordan ranks and a last-step law not supplied by those comparisons. No assertion of comprehensive historical uniqueness is made.

## Limitations

This is a conditional classification restricted to even-sized multipartite classes, not a classification of all line graphs. It leverages elementary incidence theory, so an equivalent result could be implicit in historical graph-code or binary-rank literature not located here. In particular the classical incidence-Gram identity and the fact that the original complete multipartite binary adjacency has square zero in the all-even case are credited as ingredients, not claimed as discoveries. The exact multiplicities, part-count parity correction, and all-state extinction census are the evaluated claims. Exhaustive finite checks alone would not establish an infinite-family theorem; the proof addresses all class sizes independently.

## References

1. F. Pasqualetti, D. Borra, and F. Bullo, *Consensus Networks over Finite Fields*, arXiv:1301.4587v1, first publicly submitted 19 January 2013, Sections 3–5. https://arxiv.org/abs/1301.4587.
2. A. Abudayah, O. Alomari, and T. Sander, *Incidence matrices and line graphs of mixed graphs*, arXiv:2205.05375v1 (2022). https://arxiv.org/abs/2205.05375.
3. B. Berman, E. Borer, and L. Hungerbühler, *Lights Out on graphs*, arXiv:1903.06942v1 (2019), Sections 1 and 4. https://arxiv.org/abs/1903.06942.
4. *Sharp period-four census for complete multipartite parity automata*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-period-four-census-for-complete-multipartite-parity-automa--acea41c73be7/RESULT.md.
