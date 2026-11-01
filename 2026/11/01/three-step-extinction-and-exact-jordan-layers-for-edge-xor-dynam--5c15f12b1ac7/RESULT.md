# Three-step extinction and exact Jordan layers for edge-XOR dynamics on Boolean cubes

## Finding
For each integer \(d\ge2\), write \(Q_d\) for the undirected Boolean hypercube and \(L(Q_d)\) for its line graph (two original edges are adjacent when they share an endpoint). Let \(q\) be a power of two. A configuration is a vector of elements of \(\mathbb F_q\) indexed by the edges of \(Q_d\); at every synchronous step an edge state is replaced by the sum of states on all *other* edges sharing either endpoint. Let \(T_d\) be that update matrix. Put \(N=2^d\), \(m=dN/2\), and \(J_j(0)\) for a size-\(j\) Jordan block at zero. The exact Jordan decomposition over \(\mathbb F_q\) is
\[
T_d\sim J_3(0)^{\oplus(N/2-2)}\oplus J_2(0)^{\oplus2}\oplus J_1(0)^{\oplus((d-3)N/2+2)}.
\]
The exponents are nonnegative for all specified \(d\); in particular when \(d=2\), the first and third multiplicities vanish. Every trajectory reaches zero by step three, sharply so when \(d\ge3\). The nilpotency index is two in the square case \(d=2\).

If \(H_d(x)\) denotes the least nonnegative integer \(t\) with \(T_d^t x=0\), and \(N_j\) counts all labelled configurations with \(H_d(x)=j\), then
\[
\begin{aligned}
N_0&=1,\\
N_1&=q^{(d-2)N/2+2}-1,\\
N_2&=q^{(d-1)N/2+2}-q^{(d-2)N/2+2},\\
N_3&=q^{dN/2}-q^{(d-1)N/2+2}.
\end{aligned}
\]
For uniform random initial states, the probability of requiring the full three steps is \(1-q^{2-N/2}\) when \(d\ge3\), tending to one with \(d\). For \(d=2\), \(N_3=0\).

## Assumptions and scope
All graphs are finite, simple, loopless, and undirected. The rule is strictly the synchronous, *open-neighborhood* sum over a finite field of characteristic two; including an edge's own state would be a different automaton. Each original cube edge labels one vertex of the line graph. The proofs concern all integer dimensions \(d\ge2\) and all finite characteristic-two fields, not just binary states.

## Proof
Let \(C\in\mathbb F_q^{N\times m}\) be the ordinary unoriented vertex-edge incidence matrix of \(Q_d\), one unit at each endpoint of each edge. Since distinct cube edges share at most one endpoint and every column of \(C\) has exactly two units, in characteristic two
\[
T_d=C^{\mathsf T}C,\qquad M=CC^{\mathsf T}=A_{Q_d}+(d\bmod2)I.
\]
The cube \(Q_d\) is connected, so \(\operatorname{im}C=W:=\{v\in\mathbb F_q^N:\sum_xv_x=0\}\) of dimension \(N-1\); also \(\ker C^{\mathsf T}=\langle\omega\rangle\), where \(\omega\) is the all-ones vertex vector. Note \(\omega\in W\), since \(N\) is even. Hence
\[
\operatorname{rank}T_d=\dim W-\dim(W\cap\ker C^{\mathsf T})=N-2.
\]

To calculate the second power, identify the vertex space with the group algebra \(R=\mathbb F_q[(\mathbb Z/2\mathbb Z)^d]\). Denote the commuting coordinate flips by \(g_i\) and set \(y_i=1+g_i\). Since \(y_i^2=0\), there is an algebra isomorphism
\[
R\cong\mathbb F_q[y_1,\ldots,y_d]/(y_1^2,\ldots,y_d^2).
\]
The operator \(M=A_{Q_d}+(d\bmod2)I\) is multiplication by \(s=y_1+\cdots+y_d\). Set \(z_1=s\) and \(z_i=y_i\) for \(2\le i\le d\). This invertible linear change of generators preserves the relations \(z_i^2=0\) (the square of every linear form vanishes in characteristic two). Consequently multiplication by \(z_1\) has both image and kernel equal to the ideal \((z_1)\), of dimension \(N/2\), and \(M^2=0\).

Under the group-algebra identification, \(W\) is the augmentation ideal: the elements whose coefficients in the group-element basis sum to zero. It is the ideal \((z_1,\ldots,z_d)\). In particular \(\ker M=(z_1)\subset W\), so
\[
\dim M(W)=\dim W-\dim\ker M=N/2-1.
\]
The all-ones vector is \(\omega=\prod_{i=1}^d(1+g_i)=\prod_{i=1}^d y_i=z_1z_2\cdots z_d\). For \(d\ge2\), the preimage \(z_2\cdots z_d\) lies in \(W\). Thus \(\omega\in M(W)\), and the one-dimensional kernel of \(C^{\mathsf T}\) survives inside that subspace. Therefore
\[
\operatorname{rank}(T_d^2)=\operatorname{rank}(C^{\mathsf T}MC)=\dim M(W)-1=N/2-2,
\quad T_d^3=C^{\mathsf T}M^2C=0.
\]
For a nilpotent matrix with Jordan-block multiplicities \(a_1,a_2,a_3\) in sizes one, two, three, respectively, \(\operatorname{rank}T^2=a_3\), \(\operatorname{rank}T=a_2+2a_3\), and \(m=a_1+2a_2+3a_3\). Substitution gives
\[
a_3=N/2-2,\quad a_2=2,\quad a_1=(d-3)N/2+2.
\]
This reconstructs the asserted Jordan form, including both boundary cases. The kernels of \(T_d\) and \(T_d^2\) have dimensions \((d-2)N/2+2\) and \((d-1)N/2+2\), respectively. Counting vectors in the successive kernels and taking differences gives all four exact relaxation-layer populations. Zero is the only periodic state because \(T_d\) is nilpotent.

Finally, the vertex adjacency operator is multiplication by \(g_1+\cdots+g_d\). Its square is \(dI\) since coordinate flips commute and each squares to identity. Thus the vertex rule is an involution when \(d\) is odd and is square-zero when \(d\) is even. This establishes the promised vertex-versus-edge comparison.

## Verification
The accompanying standalone Python checker constructs the cube edges, then forms the line-graph update in two different ways: directly from shared endpoints and from binary incidence neighborhoods. It compares individual updates, computes ranks of the first two powers over \(\mathbb F_2\) by explicit elimination, and verifies the third power is zero. For dimensions \(2\) through \(7\), all ranks match the formulas. For dimensions \(2\) and \(3\), every binary configuration is enumerated and classified by its first zero time. Larger dimensions use reproducibly seeded samples; they are not claimed as exhaustive. The theorem for all dimensions and all finite characteristic-two fields follows from the preceding proof, not from numerical extrapolation. Run with `python check_linecube.py`; the included `verification_output.txt` is an output record for the included program.

## Relationship to prior work
The matrix formulation of finite linear cellular automata and analysis of relaxation are classical; Tadaki (1993) studies rule-90 and rule-150 path automata, not the cube's line graph. Gadouleau and Richard (2015) establish that any connected undirected graph apart from a single edge *admits some* Boolean nilpotent update of class three. This is existential and does not establish nilpotence for the prescribed parity-neighbor rule, nor its Jordan structure or exact layer census. Binary adjacency-rank techniques and incidence matrices also appear in Buchanan and coauthors (2023), but they study odd biclique covers, not second powers of cube-line-graph adjacency or dynamical relaxation. The standard line-graph incidence identity and the first-rank step are not claimed to be new. The claimed contribution is the exact, dimension-uniform rank of the *second* iterate, the complete Jordan partition and the resulting explicit relaxation populations for this natural line-graph family.

## Limitations
The conclusion is specific to the open-neighbor sum in characteristic two, and does not classify nonlinear updates, odd-characteristic sums, or line graphs of arbitrary regular graphs. The inspected literature and research-record comparisons did not reveal an equivalent all-dimensional theorem, but historical equivalence in unindexed finite-field graph spectral work cannot be ruled out. Verification samples for dimensions above three do not constitute an exhaustive empirical proof.

## References
1. S. Tadaki, *Orbits in one-dimensional finite linear cellular automata*, initially public 14 May 1993, arXiv:cond-mat/9305012, https://arxiv.org/abs/cond-mat/9305012.
2. M. Gadouleau and A. Richard, *Simple dynamics on graphs*, initially public 16 March 2015, arXiv:1503.04688, https://www.i3s.unice.fr/~richard/PUBLICATIONS/JOURNALS/2015_Simple.pdf.
3. C. Buchanan et al., *Odd covers of graphs*, *Journal of Graph Theory* **104** (2023), 420–439, https://doi.org/10.1002/jgt.22970.
