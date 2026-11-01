# Sharp edgewise electrical projection norms and extremal multipartite networks

## Finding
Let \(G=K_{s_1,\ldots,s_r}\) be an unweighted complete multipartite graph, with \(r\ge2\), positive integer part sizes \(s_i\), and \(N=\sum_i s_i\ge2\). Orient its edges arbitrarily. Write \(B:\mathbb R^{V(G)}\to\mathbb R^{E(G)}\) for the edge-gradient matrix, \(L=B^{\mathsf T}B\), and \(P=BL^+B^{\mathsf T}\) for the orthogonal projection of edge signals onto edge gradients. Equip edge signals with the unweighted maximum norm.

Define
\[
F_N(s)=N+s-2-\frac{2(s-1)}{N-s},\quad 1\le s\le N-1.
\]
Then the exact, attained operator norm is
\[
\boxed{\|P\|_{\ell^\infty(E)\to\ell^\infty(E)}=
 \frac1N\max_{1\le i<j\le r}\bigl(F_N(s_i)+F_N(s_j)\bigr).}
\]
For a maximizing edge, an edge signal taking only \(-1\) and \(1\) attains the bound.

For each \(N\ge2\), let \(M_N\) be the largest such norm among all unweighted complete multipartite graphs with \(N\) vertices. Then
\[
\boxed{M_N=\begin{cases}
1,&N=2,\\
4/3,&N=3,\\
3/2,&N=4,\\
26/15,&N=5,\\
3-8/N+8/N^2,&N\ge6\text{ even},\\
3-8/(N+1),&N\ge7\text{ odd}.
\end{cases}}
\]
Up to permuting parts, the *complete list of maximizing graphs* is: \(K_{1,1}\) for \(N=2\); \(K_{1,1,1}\) for \(N=3\); \(K_{2,2},K_{2,1,1},K_{1,1,1,1}\) for \(N=4\); \(K_{2,2,1}\) for \(N=5\); \(K_{3,3}\) for \(N=6\); \(K_{4,3},K_{3,3,1}\) for \(N=7\); and only the balanced complete bipartite graph \(K_{\lfloor N/2\rfloor,\lceil N/2\rceil}\) for every \(N\ge8\). In particular, the sharp envelope increases to \(3\), but its five-vertex maximizer is tripartite rather than bipartite.

## Assumptions and scope
All graphs are finite, simple, connected, unweighted, and complete multipartite, with at least two nonempty parts. The norm is measured on the *entire* real edge-signal space, not just on already conservative or gradient edge signals. Edge orientations do not affect this norm, since changing them conjugates \(P\) by a diagonal sign matrix. The pseudoinverse \(L^+\) is the Moore–Penrose inverse on vertex space.

## Proof
**1. Laplacian decomposition.** For part \(i\), let \(d_i=N-s_i\). The vertex space decomposes orthogonally into global constants, the within-part zero-sum subspaces, and the subspace of partwise constants having global mean zero. The Laplacian acts by the scalar \(d_i\) on within-part contrasts for part \(i\) and by \(N\) on the last subspace. Consequently the potential of a unit dipole on an oriented edge from vertex \(a\) of part \(i\) to vertex \(b\) of part \(j\) can, up to an irrelevant global constant, be chosen to take four values:
\[
\phi(a)=\frac{N-1}{Nd_i},\qquad
\phi(x)=-\frac1{Nd_i}\quad (x\in i\setminus\{a\}),
\]
\[
\phi(b)=-\frac{N-1}{Nd_j},\qquad
\phi(y)=\frac1{Nd_j}\quad (y\in j\setminus\{b\}),
\]
with value zero on all other parts. Direct application of \(L\) gives \(L\phi=\mathbf e_a-\mathbf e_b\); therefore its edge differences constitute the corresponding column of \(P\).

**2. Absolute row sum.** Put \(A_i=(N-1)/(Nd_i)\) and \(C_i=1/(Nd_i)\), and similarly for \(j\). All edge differences with one endpoint in part \(i\) and one in part \(j\) have absolute values \(A_i+A_j\) once; \(A_i-C_j\) exactly \(s_j-1\) times; \(A_j-C_i\) exactly \(s_i-1\) times; and \(C_i+C_j\) exactly \((s_i-1)(s_j-1)\) times. The differences \(A_i-C_j\), \(A_j-C_i\) are nonnegative because \(1\le d_i,d_j\le N-1\). Let \(T=N-s_i-s_j\). Edges from part \(i\) or \(j\) to the other parts contribute respectively \(T(A_i+(s_i-1)C_i)\) and \(T(A_j+(s_j-1)C_j)\). Every edge between two untouched parts contributes zero. The total row sum simplifies to
\[
\frac{N^2-2N-s_i^2+2}{N(N-s_i)}+
\frac{N^2-2N-s_j^2+2}{N(N-s_j)}
=\frac{F_N(s_i)+F_N(s_j)}N.
\]
Since the induced maximum norm of a finite matrix is its largest absolute row sum, the stated formula follows. For a maximizing row \(e\), set the input on each edge \(f\) to the sign of \(P_{ef}\), choosing either sign if the entry is zero. The output on \(e\) is exactly that row sum.

**3. Optimal part sizes.** The discrete first difference is
\[
\Delta F_N(s)=F_N(s+1)-F_N(s)
=1-\frac{2(N-1)}{(N-s)(N-s-1)}
\quad(1\le s\le N-2).
\]
It decreases strictly with \(s\). Thus for each fixed sum \(h=s+t\le N\), \(F_N(s)+F_N(t)\) is maximized uniquely by the balanced pair (up to interchange). Its value is \(2F_N(k)\) when \(h=2k\), and \(F_N(k)+F_N(k+1)\) when \(h=2k+1\). The increases from total \(2k\) to \(2k+1\), and from \(2k+1\) to \(2k+2\), both equal \(\Delta F_N(k)\). These increases decrease in \(k\). At the final permitted step, they equal
\[
\Delta F_{2k}(k-1)=\frac{(k-1)(k-2)}{k(k+1)},\qquad
\Delta F_{2k+1}(k)=\frac{k-3}{k+1}.
\]
For even \(N\ge6\) and odd \(N\ge9\) they are strictly positive, so the best pair uses all vertices and is balanced, giving the displayed formulas. For \(N=7\), the last increment is zero, giving both \((3,3)\) with one remaining singleton part and \((3,4)\) with no remaining vertices. For \(N=5\), the increment is negative and the best pair is \((2,2)\), leaving exactly one singleton. The cases \(N=2,3,4\) follow from the same formula and its short sequence of part sizes. Strict discrete concavity rules out all other maximizing pairs and hence all other graph profiles.

## Verification
The standalone program `verify_electrical_multipartite.py` constructs the full oriented incidence matrix for every integer partition of \(2\le N\le9\) into at least two parts, solves an independently assembled reduced Laplacian exactly, and checks the maximum absolute projection row sum against the formula. It passed 87 such exact comparisons. It also enumerates all complete multipartite profiles on \(2\le N\le25\) using exact rational arithmetic and checks the sharp envelope and all maximizing profiles. Run with `python verify_electrical_multipartite.py`; requires SymPy. These computations are finite corroboration; the proof covers every admissible number and size of parts.

## Relationship to prior work
Electrical routing and graph-Laplacian projection operators occur in Kelner and Maymounkov, *Electric routing and concurrent flow cutting* (2009): their Theorem 3.1 controls routing congestion using a matrix projection norm, but does not give the complete multipartite row-norm or fixed-vertex extremal classification. Christiano, Kelner, Mądry, Spielman, and Teng, *Electrical Flows, Laplacian Systems, and Faster Approximation of Maximum Flow in Undirected Graphs* (2010), develop general electrical-flow algorithms rather than these exact projection norms. The previously established parallel-path formula covers \(K_{2,q}\), which consists of \(q\) two-edge terminal paths; no novelty is asserted for that subfamily alone. It does not cover \(K_{a,b}\) with \(a,b\ge3\), or multipartite graphs with three or more nontrivial parts. The full row-norm formula and global multipartite extremizer classification are the claims here.

## Limitations
The theorem does not cover edge conductances other than one, arbitrary graphs, directed Laplacians, complex edge signals with other norms, or the competitive ratio of electrical routing (which is not the same quantity as this projection norm). Prior literature under alternate names for transfer-current matrices may contain an equivalent formula; absence from the inspected sources is not an exhaustive priority guarantee.

## References
1. J. Kelner and P. Maymounkov, *Electric routing and concurrent flow cutting*, arXiv:0909.2859, first publicly posted 2009-09-15. See the definitions of graph gradient/divergence and Theorem 3.1 on electrical projection norm.
2. P. Christiano, J. Kelner, A. Mądry, D. Spielman and S.-H. Teng, *Electrical Flows, Laplacian Systems, and Faster Approximation of Maximum Flow in Undirected Graphs*, arXiv:1010.2921, first publicly posted 2010-10-14. See Section 2 on electrical flows.
