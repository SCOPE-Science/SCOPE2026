# A matched-edge weight resonance and the full actuator-set polynomial of bipartite networks

## Finding
For every integer \(n\ge3\), form two indexed vertex classes \(U=\{u_1,\dots,u_n\}\) and \(V=\{v_1,\dots,v_n\}\). Connect \(u_i\) and \(v_j\) with conductance \(b\ge0\) when \(i=j\), and conductance \(a>0\) otherwise; there are no edges within either class. Let \(L(a,b)\) be the ordinary weighted graph Laplacian and let \(T\) be a set of vertices, with one independent input at each selected vertex. Write \(\mathcal C_{a,b}(z)=\sum_{T\text{ controllable}}z^{|T|}\), where controllability refers to the entire \(2n\)-state system \(\dot x=-L(a,b)x+B_Tu\).

**Complete characterization.** If \(b\ne a\), the selection \(T\) is controllable if and only if it meets at least \(n-1\) of the \(n\) indexed pairs \(\{u_i,v_i\}\). If \(b=a\), it is controllable if and only if it contains at least \(n-1\) vertices of **each** of \(U\) and \(V\).

**Complete generating polynomials.** With \(q(z)=2z+z^2\),
\[
\mathcal C_{a,b}(z)=\begin{cases}
q(z)^n+nq(z)^{n-1},&b\ne a,\\
z^{2n-2}(z+n)^2,&b=a.
\end{cases}
\]
Consequently the minimum independent-actuator count and the number of minimum sets are, respectively,
\[
(\gamma,N_{\min})=\begin{cases}
(n-1,\,n2^{n-1}),&b\ne a,\\
(2n-2,\,n^2),&b=a.
\end{cases}
\]
For any \(a>0\), choosing positive \(b\ne a\) therefore requires only half as many actuators as \(b=a\), **without changing the unweighted support graph** \(K_{n,n}\). The resonance remains exact no matter how close \(b\) is to \(a\).

**Random-actuation reliability.** If each vertex is independently actuated with probability \(p\in[0,1]\), put \(r=p(2-p)\). The exact probabilities of controllability are
\[
\Pr(\mathrm{ctrl})=\begin{cases}
r^n+n(1-p)^2r^{n-1},&b\ne a,\\
\left[p^n+n(1-p)p^{n-1}\right]^2,&b=a.
\end{cases}
\]
For each fixed \(c\ge0\), in the nonresonant family with \(p_n=1-c/\sqrt n\), the probability converges to \(e^{-c^2}(1+c^2)\), whereas at resonance with \(p_n=1-c/n\), it converges to \(e^{-2c}(1+c)^2\). The associated high-reliability missing-actuator scales are thus \(n^{-1/2}\) and \(n^{-1}\), respectively.

## Assumptions and scope
Here \(n\) is any integer at least three, \(a\) is any strictly positive real number, and \(b\) is any nonnegative real number (including the matched-edge deletion \(b=0\)). Each actuator has a separate unconstrained real-valued input; a single common input is a different problem. All statements are for *exact*, infinite-precision controllability of the fixed weighted Laplacian; numerical conditioning near \(b=a\) is not asserted. No directed, signed, heterogeneous-index or independent-edge-perturbation version is claimed. For \(b>0\), the underlying simple graph is \(K_{n,n}\); when \(b=0\) it is the connected crown graph.

## Proof
Let \(J\) denote the \(n\)-square all-ones matrix and \(I\) the identity. Set \(d=(n-1)a+b\). In the order \(U,V\), the cross-adjacency block is \(M=aJ+(b-a)I\), and
\[
L=\begin{pmatrix}dI&-M\\-M&dI\end{pmatrix}.
\]
Put \(E=\{x\in\mathbb R^n:\sum_i x_i=0\}\), of dimension \(n-1\). Direct matrix multiplication gives the mutually orthogonal eigenspaces
\[
\begin{array}{c|c}
\text{eigenspace}&\text{eigenvalue}\\
\operatorname{span}\{(\mathbf1,\mathbf1)\}&0\\
\operatorname{span}\{(\mathbf1,-\mathbf1)\}&2d\\
\{(x,x):x\in E\}&na\\
\{(x,-x):x\in E\}&(n-2)a+2b.
\end{array}
\]
Their dimensions sum to \(2n\). Since \(n\ge3\), \(a>0\), \(b\ge0\), both standard-module eigenvalues lie strictly between \(0\) and \(2d\): explicitly \(2d-na=(n-2)a+2b>0\) and \(2d-[(n-2)a+2b]=na>0\). They are equal exactly if \(b=a\). There are no other eigenvalue coincidences.

By the symmetric Popov--Belevitch--Hautus criterion, \((-L,B_T)\) is controllable exactly when no nonzero eigenvector of \(L\) vanishes at every vertex in \(T\). The two constant-on-parts eigenvectors never vanish at a selected vertex. If \(b\ne a\), the other two eigenspaces are separate. A vector \((x,\pm x)\) vanishes on \(T\) precisely when \(x_i=0\) at each indexed pair touched by \(T\). If two pairs are untouched, a nonzero \(x\in E\) can be supported on those two indices by taking their coordinate difference. If at most one pair is untouched, the condition \(\sum_i x_i=0\) forces \(x=0\). This proves the first criterion.

At \(b=a\), the two \((n-1)\)-dimensional standard eigenspaces coalesce. Their sum is exactly \(E\oplus E\), consisting of all \((x,y)\) with \(\sum_i x_i=\sum_i y_i=0\). A nonzero vector here vanishes on \(T\) if and only if at least two vertices are unselected on one side: their coordinate difference provides one, and otherwise each side's zero-sum condition forces zero. This gives the second criterion.

For \(b\ne a\), any touched pair contributes the polynomial \(2z+z^2\) (either endpoint alone or both); all pairs must be touched except possibly one. Summing zero or one empty pair gives \(q(z)^n+nq(z)^{n-1}\). At \(b=a\), each side can omit zero or one vertex, giving \((z^n+n z^{n-1})^2\). Lowest-degree coefficients prove the minimum counts and multiplicities. These are exhaustive combinatorial counts, not asymptotic approximations.

For independent Bernoulli actuation, a pair is touched with probability \(r=1-(1-p)^2\). The nonresonant event has zero or one completely untouched pairs, giving \(r^n+n(1-r)r^{n-1}\). At resonance, each side has at most one unselected vertex; their independent probabilities multiply, giving the second expression. Under \(p_n=1-c/\sqrt n\), the number of empty pairs is asymptotically Poisson with mean \(c^2\), equivalently \((1-c^2/n)^n\to e^{-c^2}\). Under \(p_n=1-c/n\), the numbers of unselected vertices on the two sides converge to independent Poisson variables of mean \(c\). The displayed limits follow directly from the two exact formulas. For each fixed \(c\), these \(p_n\) lie in \([0,1]\) for all sufficiently large \(n\).

## Verification
The self-contained `verify.py` uses exact modular arithmetic to compute finite Kalman controllability ranks for every actuator subset on \(n=3,4\) and for reproducibly sampled subsets on \(n=5,6,7\), with both resonant and nonresonant integer conductances. It independently enumerates every subset on \(3\le n\le7\), checks the polynomial coefficients and verifies both reliability formulas at two rational sampling probabilities. Run `python3 verify.py` with Python 3 standard library; the expected output is `VERIFY_OK 2167 checks`. Exhaustive finite cases corroborate but do not replace the preceding general proof. Modular rank is exact for the displayed integer test instances and selected prime; it does not certify all real parameters. No symbolic formula is inferred from a finite experiment.

## Relationship to prior work
Parlangeli--Notarstefano (arXiv:1109.3556, 2011) give PBH-based exact leader tests for paths and cycles, not the matched-weight complete-bipartite family. Zhang--Camlibel--Cao (CDC/ECC 2011, DOI 10.1109/CDC.2011.6160658) study general and distance-regular graph leader sets; for multiple leaders their general conditions are separately necessary/sufficient, and their explicit network classifications are cycles and complete graphs. They do not state this all-set matched-edge classification or weight collision. Burgarth et al. (arXiv:1111.1475, 2011) and Monshizadeh--Zhang--Camlibel (arXiv:1403.4868, 2014) establish zero-forcing implications and strong structural controllability criteria, not a sharp fixed-two-weight Laplacian phase diagram.

In particular, for \(b>0\), the graph is \(K_{n,n}\), whose known ordinary zero-forcing number is \(2n-2\). Thus the resonant actuator minimum coincides with zero forcing, while for every unequal positive matched-edge weight the minimum is \(n-1\). The graph's zero-forcing number and the general PBH criterion are previous knowledge and are not claimed as new; only the complete weight-resolved classification, generating polynomial and resulting reliability transition are assessed here. At the boundary \(n=3, b=0\), this graph is the six-cycle, already within the path-and-cycle literature; no claim of novelty is attached to that special case. Existing published work on edge metric bases of crown graphs happens to yield \(n2^{n-1}\) selections in the deleted-matching case, but this is a different invariant and does not assert fixed-Laplacian controllability for positive matching weights.

## Limitations
The theorem concerns exact controllability and says nothing quantitative about the energy or conditioning of control near the coalescence \(b=a\). It requires identical nonmatching conductances and identical matched conductances; independently perturbed edges need not obey the same criterion. The result does not characterize single-input aggregate actuation, signed edges, arbitrary bipartite graphs, or finite-horizon Gramian magnitudes. Possible equivalent classifications in less searchable historical literature are not ruled out by database searches alone. Independent external proof assessment has not been performed.

## References
1. G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556, first posted 2011-09-16, https://arxiv.org/abs/1109.3556.
2. S. Zhang, M. K. Camlibel and M. Cao, *Controllability of Diffusively-Coupled Multi-Agent Systems with General and Distance Regular Coupling Topologies*, CDC/ECC 2011, DOI:10.1109/CDC.2011.6160658. Open full text: https://skoge.folk.ntnu.no/prost/proceedings/cdc-ecc-2011/data/papers/0872.pdf.
3. D. Burgarth, D. D'Alessandro, L. Hogben, S. Severini and M. Young, *Zero forcing, linear and quantum controllability for systems evolving on networks*, arXiv:1111.1475, first posted 2011-11-07, https://arxiv.org/abs/1111.1475.
4. N. Monshizadeh, S. Zhang and M. K. Camlibel, *Zero forcing sets and controllability of dynamical systems defined on graphs*, arXiv:1403.4868, first posted 2014-03-19, https://arxiv.org/abs/1403.4868.
