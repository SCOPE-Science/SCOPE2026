# Correlated two-qubit mixing in Erdős–Rényi graph states

## Finding
For a simple labeled graph \(G\) on \(n\ge4\) vertices, prepare the \(n\)-qubit graph state
\[
|G\rangle=\prod_{\{v,w\}\in E(G)}\operatorname{CZ}_{vw}|+\rangle^{\otimes n}.
\]
For each unordered pair \(S\subseteq V(G)\) of size two, put \(I_S=1\) if its reduced state is \(\rho_S=\mathbf1_4/4\), and \(I_S=0\) otherwise. Set
\[Y_n=\sum_{|S|=2}I_S,\qquad D_n=\binom n2-Y_n.\]
Suppose \(G\sim G(n,1/2)\), with independent equiprobable graph edges. Define
\[
t=2^{-(n-3)},\quad p=(1-t)(1-t/2),\quad
c_1=\frac{t(1-t)(1-t+t^2)}4,\quad
c_0=\frac{3t^2(5t^2-6t+3)}4.
\]
**Exact two-site covariance law.** For every \(n\ge4\) and every pair of distinct two-element subsets \(S,T\),
\[
\mathbb EI_S=p,\qquad
\operatorname{Cov}(I_S,I_T)=
\begin{cases}c_1,&|S\cap T|=1,\\c_0,&S\cap T=\varnothing.\end{cases}
\]
Both covariance expressions are strictly positive, including for disjoint vertex pairs. Hence
\[
\boxed{\mathbb EY_n=\binom n2p,\qquad
\operatorname{Var}(Y_n)=\binom n2p(1-p)+6\binom n3c_1+6\binom n4c_0.}
\]
Let \(Z_n\) denote the number of isolated vertices. In the limit \(n\to\infty\),
\[
\operatorname{Var}(Y_n)\sim2n^3 2^{-n},\qquad
\mathbb ED_n\sim6n^2 2^{-n},
\]
and more sharply
\[
\boxed{\mathbb E[(D_n-(n-1)Z_n)^2]
=\frac{n(n-1)t}{2}+O(n^4t^2).}
\]
Thus isolated vertices explain all of the leading-order variance of the deficient-marginal count, but only one third of its leading-order mean.

## Assumptions and scope
The graph is labeled, loopless, unweighted, undirected, and distributed as \(G(n,1/2)\): distinct undirected edges are mutually independent Bernoulli variables. The graph state is pure; two-qubit marginals are obtained by tracing out all other qubits. All expectations and variances refer to randomness over graphs, not to randomness over stabilizer operators or a within-state Pauli-weight distribution. Pair events refer to distinct two-element subsets. No independent-circuit-output claim is made.

## Proof
**Step 1: the quantum cut-rank criterion.** Write the adjacency matrix as \(\Gamma\) over \(\mathbb F_2\). Decompose computational basis configurations into \((s,r)\) across \(S\mid S^c\). The graph-state amplitude is \(2^{-n/2}\) times the phase \((-1)^{q_S(s)+q_R(r)+s^\top\Gamma_{S,S^c}r}\). In the partial trace, the matrix element between \(s\) and \(s'\) is proportional to \(\sum_r(-1)^{(s-s')^\top\Gamma_{S,S^c}r}\), and vanishes unless \((s-s')^\top\Gamma_{S,S^c}=0\). Therefore \(\rho_S=\mathbf1_4/4\) exactly when the binary \(2\times(n-2)\) cut matrix \(\Gamma_{S,S^c}\) has row rank two. Its rows are independent uniform binary vectors, giving
\[p=(1-2^{-(n-2)})(1-2^{-(n-3)})=(1-t/2)(1-t).\]

**Step 2: disjoint pairs.** By relabeling take \(S=\{1,2\}\) and \(T=\{3,4\}\). Let \(B\) be the shared random \(2\times2\) cross-edge matrix; its binary rank \(R\) equals \(0,1,2\) with probabilities \(1/16,9/16,6/16\), respectively. Conditional on \(B\), the two cut-rank events are independent, with the common success probability
\[
f_0=(1-u)(1-2u),\quad f_1=1-u,\quad f_2=1,\qquad u=2^{-(n-4)}=2t.
\]
The formulas follow by completing the column span of \(B\) with \(n-4\) fresh, uniformly random columns. The law of total covariance gives \(\operatorname{Cov}(I_S,I_T)=\operatorname{Var}(f_R)\); direct expansion with the above three rank probabilities gives exactly
\[c_0=3t^2(5t^2-6t+3)/4>0.\]

**Step 3: overlapping pairs.** By relabeling take \(S=\{1,2\}\), \(T=\{1,3\}\), and put \(L=V(G)\setminus\{1,2,3\}\). Let \(X\in\mathbb F_2^{n-3}\) be the edge vector from vertex one to \(L\). Denote by \(h\) the common edge \(\Gamma_{23}\), and by \(b,b'\) the edges \(\Gamma_{13},\Gamma_{12}\), respectively. The remaining vectors from vertices two and three to \(L\) are mutually independent and independent of \(X,h,b,b'\). Accordingly the two rank events are conditionally independent given \(X,h,b,b'\). Let \(q(X,h)\) be a rank-success probability averaged over its own \(b\). If \(X\ne0\), the second cut row is forbidden to equal either zero or the first row; checking the two possible values of \(h\) gives
\[q(X,0)=1-3t/2,\qquad q(X,1)=1-t/2.\]
If \(X=0\), the first row is nonzero with probability one half, and \(q(0,h)=(1-t)/2\) for either \(h\). Since \(\Pr(X=0)=t\) and \(h\) is uniform,
\[
\mathbb E(I_S I_T)=(1-t)\frac{(1-3t/2)^2+(1-t/2)^2}{2}
+t\frac{(1-t)^2}{4}.
\]
Subtracting \(p^2\) yields exactly \(c_1=t(1-t)(1-t+t^2)/4>0\).

**Step 4: enumeration and isolated-vertex fluctuation.** There are \(\binom n2\) pair events, \(3\binom n3\) unordered pairs of events intersecting in one vertex, and \(3\binom n4\) unordered pairs of disjoint events. The variance formula follows by multiplying off-diagonal covariances by two.

For the refined fluctuation statement, a given vertex is isolated with probability \(a=2^{-(n-1)}=t/4\), and two different vertices are simultaneously isolated with probability \(2a^2\). Consequently
\[
\mathbb EZ_n=na,\qquad \operatorname{Var}(Z_n)=na+n(n-2)a^2.
\]
Conditioning on a specified vertex being isolated, a two-site marginal is deficient surely if the vertex is in its pair. If the isolated vertex lies outside the pair, a zero cut-matrix column remains and rank two succeeds with probability \((1-t)(1-2t)\); hence the conditional deficiency probability is \(3t-2t^2\). Therefore
\[
\mathbb E(D_n Z_n)=\binom n2 a\bigl[2+(n-2)(3t-2t^2)\bigr].
\]
Insert this formula and the previous variances into
\[
\operatorname{Var}(D_n-(n-1)Z_n)=\operatorname{Var}(Y_n)+(n-1)^2\operatorname{Var}(Z_n)-2(n-1)\operatorname{Cov}(D_n,Z_n).
\]
Exact polynomial expansion in \(t\) gives \(\operatorname{Var}(D_n-(n-1)Z_n)=n(n-1)t/2+O(n^4t^2)\), while direct calculation gives
\[\mathbb E(D_n-(n-1)Z_n)=n(n-1)t(2-t)/4.\]
Squaring the latter adds only \(O(n^4t^2)\), proving the displayed mean-square formula. Finally \(t=8\cdot2^{-n}\), and the leading terms of the variance and deficiency mean are \(n(n-1)(n+1)t/4\) and \(3n(n-1)t/4\), respectively. Also \((n-1)\mathbb EZ_n\sim2n^2 2^{-n}\), exactly one third of \(\mathbb ED_n\) to leading order. This proves all assertions.

## Verification
Run the self-contained Python 3 standard-library program `verify.py`. It enumerates all labeled simple graphs on \(n=4,5,6\) vertices (64, 1024, and 32768 graphs), compares exact rational moments and both intersection-type covariances, and checks the isolated-vertex mixed moment. A separate direct-amplitude partial-trace implementation tests all 64 four-vertex graphs and 100 graphs each on five and six vertices, across every two-site marginal. The program prints `VERIFY_OK` on completion. These finite checks corroborate the identities at the tested sizes; the proof above establishes their all-size validity.

## Relationship to prior work
Zhang and Zhang (arXiv:2608.03102; first submitted 2026-08-04) connect graph descriptions of typical Clifford-circuit output states to the Erdős–Rényi ensemble and derive tripartite GHZ statistics. This work treats the **exact independent-edge graph ensemble** and a different joint statistic, the across-graph covariance of two-qubit maximal-mixing events; it does not assert their ensemble equivalence at finite circuit size.

Miller and collaborators (arXiv:2207.07665, J. Phys. A 56 (2023) 335303, Sections 2.1–2.2, 3.2 and Appendix E) establish general graph-state Shor–Laflamme relations including the leaf/twin contribution to the two-body sector, and compute mean/variance **within the Pauli-weight distribution** as well as a random-graph expectation of the distribution. Those are different from the joint graph-sample covariance of two distinct two-site marginal events derived here. Sudevan and Das (arXiv:2201.05622) construct graph states that are 2-uniform; their deterministic construction does not specify the random-ensemble joint covariance or its rare-event mechanism. Hein, Eisert, and Briegel established the underlying graph-state cut-entanglement structure. These foundational results are credited; no prior general cut-rank lemma is presented as new.

## Limitations
The law is specific to \(G(n,1/2)\), not arbitrary edge probabilities, correlated graph ensembles, finite-depth random Clifford circuits, or the joint distribution of all pair events. Positive pairwise covariance alone does not imply an arbitrary multivariate positive-association property. The leading-order isolated-vertex approximation describes fluctuations in mean square; it is not a claim that isolated vertices are the only cause of nonmaximally-mixed marginals. Related graph-theoretic twin-count identities could yield alternative derivations; bibliographic searches do not establish absolute priority. The computational check stops at six vertices and does not replace the all-size proof.

## References
1. Yu-Xuan Zhang and Yu-Xiang Zhang, *Typical Output States of Monitored Random Clifford Circuits: A Graph-Theoretic Approach*, arXiv:2608.03102 (first publicly posted 2026-08-04), https://arxiv.org/abs/2608.03102.
2. Daniel Miller, Daniel Loss, Ivano Tavernelli, Hermann Kampermann, Dagmar Bruß, and Nikolai Wyderka, *Shor-Laflamme distributions of graph states and noise robustness of entanglement*, J. Phys. A: Math. Theor. **56** (2023), 335303; arXiv:2207.07665, https://arxiv.org/abs/2207.07665.
3. Sowrabh Sudevan and Sourin Das, *N-qubit states with maximum entanglement across all bipartitions: A graph state approach*, arXiv:2201.05622, https://arxiv.org/abs/2201.05622.
4. M. Hein, J. Eisert, and H. J. Briegel, *Multiparty entanglement in graph states*, Phys. Rev. A **69** (2004), 062311, https://doi.org/10.1103/PhysRevA.69.062311.
