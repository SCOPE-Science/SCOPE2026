# Adjacency spectra and Pell-type integral orders of defect-one idempotent commuting graphs

## Finding

For a labeled set $X$ with $n\ge 2$ elements let $\Gamma_n$ be the graph on rank-$(n-1)$ idempotents of the full transformation monoid of $X$, with an edge between distinct maps that commute. For $n\ge3$ its adjacency characteristic polynomial is
\[
\det(\lambda I-A_n)=\bigl(\lambda-(n-2)^2\bigr)
\bigl(\lambda^2+(n-3)\lambda-(n-2)^2\bigr)^{n-1}
(\lambda-1)^{n(n-3)/2}(\lambda+1)^{(n-1)(n-2)/2}.
\]
The graph for $n=2$ is edgeless and has characteristic polynomial $\lambda^2$; the graph for $n=3$ consists of three disjoint edges. For $n\ge4$ the graph is connected and regular of degree $(n-2)^2$, with five distinct eigenvalues.

The graph is integral, meaning that its adjacency eigenvalues are integers, exactly when $5n^2-22n+25$ is a square. In particular there are infinitely many integral orders, including
\[
n_j=(L_{4j+3}+11)/5\qquad(j\ge0),
\]
where $L_0=2$, $L_1=1$ and $L_{m+2}=L_{m+1}+L_m$. Their first four values are $3,8,42,275$.

## Assumptions and graph model

The full transformation monoid consists of all maps $X\to X$. An idempotent fixes every element of its image; consequently one of rank $n-1$ is an elementary collapse $(a,b)$, with $a\ne b$, sending $a$ to $b$ and fixing every other point. Direct composition shows that two different collapses $(a,b),(c,d)$ commute if and only if $a\ne c$, $b\ne c$, and $d\ne a$: equal tails yield different values at that tail; if $b=c$ the maps disagree in the two orders at $a$, and if $d=a$ they disagree at $c$. If none of the conflicts occurs, each collapse fixes the other's head and has its own tail, so the compositions agree.

In the once-subdivided complete graph $S(K_n)$, $(a,b)$ corresponds to the edge from $a$ to the subdivision vertex on $\{a,b\}$. Two such edges form an induced matching precisely under the same three inequalities: the tails must be distinct and neither tail may be incident to the other edge's subdivision vertex. The clique counts are therefore the induced-matching counts in [1], not a contribution of the spectral result. In particular a nonempty clique corresponds to a map $f:T\to X\setminus T$ from its tail set, and is maximal exactly when $f$ is onto: otherwise an unused tail outside $T\cup f(T)$ can be mapped to a vertex of $f(T)$ to enlarge it. This gives $\binom nr(n-r)^r$ cliques of size $r\ge1$ and $\binom nr(n-r)!\left\{\begin{smallmatrix}r\\ n-r\end{smallmatrix}\right\}$ maximal cliques of that size, as in [1].

## Proof of the spectrum and integrality

Represent a vector on the vertices as an off-diagonal array $h(a,b)$ over $\mathbb Q$. Let $R_a=\sum_{b\ne a}h(a,b)$ and $C_a=\sum_{b\ne a}h(b,a)$ be the row and column sums, and $S=\sum_a R_a$ the total. The adjacency rule gives
\[
(A_nh)(a,b)=S-R_a-R_b-C_a+h(b,a).
\]
The constant arrays give eigenvalue $(n-2)^2$ by counting neighbors. Next consider $h(a,b)=u_a+v_b$ with $\sum_a u_a=\sum_a v_a=0$. Here $(R_a,C_a)=((n-1)u_a-v_a,(n-1)v_a-u_a)$, so the determinant $n(n-2)$ of the row/column-sum map on each coordinate is nonzero for $n\ge3$. Together with the constants these arrays map isomorphically onto the space of consistent sums $\sum R_a=\sum C_a$ (the two zero-mean parts plus a common mean). Thus the space splits as constants, zero-mean additive arrays, and the kernel of the row/column-sum map.

On the additive part the adjacency formula sends $(u,v)$ to
\[
\begin{pmatrix}-(n-2)&-(n-3)\\-(n-2)&1\end{pmatrix}
\begin{pmatrix}u\\v\end{pmatrix}.
\]
It acts in each of $n-1$ independent zero-mean directions, producing the quadratic factor. On the kernel, adjacency is transposition. Symmetric arrays with zero row sums correspond to the kernel of the unsigned vertex-edge incidence matrix of $K_n$. Its rank is $n$, since the only vector with $w_a+w_b=0$ for every edge is zero (use a triangle, then all the remaining vertices). Antisymmetric arrays correspond to the oriented incidence matrix, whose rank is $n-1$ since its left kernel consists of constants. Therefore the $+1$ and $-1$ multiplicities on this kernel are $\binom{n}{2}-n$ and $\binom{n}{2}-(n-1)$, respectively. This proves the factorization.

For $n\ge4$, evaluating the quadratic at $(n-2)^2,1,-1$ gives nonzero values, and the quadratic itself has positive discriminant. All five factors in the eigenvalue list then give different eigenvalues. The degree eigenvalue of a regular undirected graph has multiplicity equal to the number of components, so the graph is connected. The small cases follow from the rule: at $n=2$ no pair commutes, and at $n=3$ the graph is 1-regular on six vertices.

The quadratic discriminant is $D_n=(n-3)^2+4(n-2)^2=5n^2-22n+25$. When it is a square its square root has the parity of $n-3$, so the roots are integers; the converse follows from the difference of the roots. This also gives the correct criterion for $n=2$ separately, since $D_2=1$. Modulo 5 the Lucas sequence repeats $2,1,3,4$, so the stated orders $n_j$ are integers. For odd $m=4j+3$, the Lucas–Fibonacci identity $L_m^2-5F_m^2=-4$, with $F_0=0,F_1=1$, yields $5D_{n_j}=(5n_j-11)^2+4=L_m^2+4=5F_m^2$. The Lucas sequence is strictly increasing along these indices, proving infinitude.

## Verification

The accompanying standard-library `verify.py` constructs the graph using literal transformation compositions and verifies the characteristic polynomial for $2\le n\le6$ using exact integer traces and Newton identities. It also checks the known clique counts for $2\le n\le7$. The reported run ends with `VERIFY_OK_DEFECT_ONE_COMMUTING_SPECTRUM`. These bounded checks do not prove the uniform spectrum or its integral subfamily.

## Relationship to prior work and limitations

The induced-matching model in [1] gives the exact clique and maximal-clique classification under the identification above, not the adjacency diagonalization. The idempotent centralizer criterion of Araújo, Kinyon and Konieczny [2, Lemma 2.2] and the work of Cameron et al. [3, Theorem 2.12] on arc-generated semigroups are background for the action and the graph construction. The spectral claim pertains only to the induced graph on the specified rank class, not the full transformation commuting graph or its other rank classes. The discriminant criterion is exact; the Lucas subfamily is not claimed to exhaust the square solutions. The inspected prior statements do not give this adjacency spectrum; an equivalent treatment under another graph name remains possible.

## References

1. *A parity transition for optimal maximal induced matching reconfiguration* [title shortened], Resultary record [91acc585aff0](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-a-parity-transition-for-optimal-maximal-induced-matching-reconfi--91acc585aff0/RESULT.md), Finding and Proof §§1–2.
2. J. Araújo, M. Kinyon, and J. Konieczny, *Minimal Paths in the Commuting Graphs of Semigroups*, [arXiv:1003.2809](https://arxiv.org/abs/1003.2809), especially Lemma 2.2 and §6.
3. P. J. Cameron, A. Castillo-Ramírez, M. Gadouleau, and J. D. Mitchell, *Lengths of words in transformation semigroups generated by digraphs*, [arXiv:1602.00935](https://arxiv.org/abs/1602.00935), *Journal of Algebraic Combinatorics* 45 (2017), 149–170.
