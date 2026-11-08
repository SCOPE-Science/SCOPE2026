# A hub-induced period-eight parity transition for reversible waves on Boolean cubes

## Finding

Let \(d\ge3\), let \(q=2^f\) for an integer \(f\ge1\), let \(Q_d\) be the \(d\)-dimensional Boolean cube, and add a single vertex adjacent to every cube vertex. Call the resulting graph \(G_d=K_1\vee Q_d\), put \(N=2^d\), and let \(A\) be its loopless adjacency matrix over \(\mathbb F_q\). On two successive configurations \(u,v\in\mathbb F_q^{N+1}\), consider the reversible wave
\[
T(u,v)=(Au+v,u).
\]
Write \(P_j(d,q)\) for the number of **configurations**, not orbit classes, with least temporal period exactly \(j\), starting immediately.

For **even** \(d\ge4\), precisely the four primitive periods \(1,2,4,8\) occur, and
\[
\begin{aligned}
P_1&=q^{N/2+1},\\
P_2&=q^{N+2}-q^{N/2+1},\\
P_4&=q^{2N}-q^{N+2},\\
P_8&=q^{2N+2}-q^{2N}.
\end{aligned}
\]
The global order of the permutation \(T\) is exactly \(8\).

For **odd** \(d\ge3\), precisely the four primitive periods \(1,2,3,6\) occur, and
\[
\begin{aligned}
P_1&=q,\\
P_2&=q^2-q,\\
P_3&=q^{N+1}-q,\\
P_6&=q^{2N+2}-q^{N+1}-q^2+q.
\end{aligned}
\]
The global permutation order is exactly \(6\). All other \(P_j\) vanish. The number of distinct temporal orbits of length \(j\) is \(P_j/j\). In particular, a single universal vertex doubles the largest possible period for even-dimensional cubes (from \(4\) to \(8\)), whereas the corresponding odd-dimensional maximum remains \(6\).

## Assumptions and scope

The graph is finite, undirected, simple, and labelled: cube vertices are \(\{0,1\}^d\), with edges between strings differing in exactly one coordinate; the additional apex is joined to every cube vertex. Each vertex state lies in the finite field \(\mathbb F_{2^f}\), with no loops or self-coupling. The time step is the same deterministic linear map at every integer time. Addition and matrix arithmetic have characteristic two. The conclusions hold simultaneously for all integers \(d\ge3\), all \(f\ge1\), and every pair of initial configurations \(u,v\).

The low-dimensional graph \(G_2\) is a wheel over a four-cycle and satisfies the even-case formulas, but it is excluded from the stated family to isolate genuinely higher-dimensional cubes. At \(d=1\), the odd-case exponent for period three is different; that case is not included.

## Proof

**1. Hypercube rank lemma.** Write \(S_j\) for translation by the \(j\)-th coordinate unit on functions on \(\{0,1\}^d\), and put
\[
R=\sum_{j=1}^d(S_j+I),\qquad B=\sum_{j=1}^d S_j.
\]
In characteristic two, the commuting operators \(S_j+I\) square to zero, so \(R^2=0\) and \(B=R+(d\bmod 2)I\). The regular representation of the group algebra is
\[
\mathbb F_q[y_1,\ldots,y_d]/(y_1^2,\ldots,y_d^2),
\]
where \(y_j\) acts as \(S_j+I\). The invertible linear change \(z_1=y_1+\cdots+y_d,\ z_j=y_j\) for \(j\ge2\) preserves the relations \(z_j^2=0\). Consequently, \(R\) acts as multiplication by \(z_1\), proving
\[
\operatorname{rank}R=N/2,\quad \dim\ker R=N/2.
\]
Let \(e\) be the all-one column of length \(N\), and set \(J=ee^{\mathsf T}\). The all-one vector corresponds to \(y_1\cdots y_d\) applied to a coordinate delta, so \(e\in\operatorname{im}R\): explicitly, \(g=(S_2+I)\cdots(S_d+I)\delta_0\) satisfies \(Rg=e\). For \(d\ge2\) the coordinate sum \(e^{\mathsf T}g=0\). By symmetry of \(R\), \(e^{\mathsf T}k=0\) for every \(k\in\ker R\). We also have \(e^{\mathsf T}e=N=0\) in the field.

**2. Adjacency at the apex.** Relative to cube coordinates and the apex,
\[
A=\begin{pmatrix}B&e\\ e^{\mathsf T}&0\end{pmatrix}.
\]
If \(d\) is even, \(B=R\), \(Be=0\), and
\[
A^2=\begin{pmatrix}J&0\\0&0\end{pmatrix}\ne0,\qquad A^3=0.
\]
The equation \(A(x,a)=0\) is \(Rx=ae\) and \(e^{\mathsf T}x=0\). Every solution is \(x=ag+k\) with \(k\in\ker R\), and the second equation holds automatically, proving
\[
\dim\ker A=N/2+1,\qquad \operatorname{rank}A^2=1.
\]

If \(d\) is odd, \(B=I+R\) and \(B^2=I\), with \(Be=e\). Direct multiplication shows
\[
A^3=A,\quad A^4=A^2.
\]
Because \(B\) is invertible, \(A(x,a)=0\) holds exactly when \(x=ae\); hence \(\dim\ker A=1\). The equation \((A+I)(x,a)=0\) becomes \(Rx=ae\), \(e^{\mathsf T}x+a=0\). Expressing \(x=ag+k\) as above forces \(a=0\), giving \(\dim\ker(A+I)=N/2\). Moreover \(A^2\) is an idempotent of rank \(N\), so
\[
\mathbb F_q^{N+1}=K\oplus E,\quad K=\ker A,\quad E=\operatorname{im}A^2,
\]
with \(\dim K=1\), \(\dim E=N\). On \(K\), \(A=0\); on \(E\), \(A^2=I\), and \(A+I\) has nullity \(N/2\).

**3. Fixed-point spaces of the wave.** The inverse \(T^{-1}(u,v)=(v,u+Av)\) exists on every field. Matrix multiplication yields
\[
T^2=\begin{pmatrix}A^2+I&A\\A&I\end{pmatrix}.
\]
Thus \(\operatorname{Fix}(T)\) is parametrized by \(u=v\in\ker A\); and \(\operatorname{Fix}(T^2)\) is parametrized by \(u,v\in\ker A\).

For even \(d\), the identities \(A^3=0\) and \(A^2\ne0\) imply
\[
T^4=I+\operatorname{diag}(A^2,A^2),\qquad T^8=I.
\]
Consequently the dimensions of the fixed spaces of \(T,T^2,T^4,T^8\), in that order, are
\[
N/2+1,\quad N+2,\quad 2N,\quad 2N+2.
\]
The last fixed space is the whole phase space, while \(T^4\ne I\).

For odd \(d\), the invariant phase space splits into \(K^2\oplus E^2\). On \(K^2\), \(T\) swaps coordinates and has fixed-space dimension one at odd times, two at even times. On \(E^2\), the block equation \(T^2+\operatorname{diag}(A,A)T+I=0\) and \(A^2=I\) imply
\[
T^3=\operatorname{diag}(A,A),\qquad T^6=I.
\]
All eigenvalues of \(T\) on \(E^2\), over an algebraic closure, are nontrivial cube roots of unity (the scalar reduction of the equation is \(\lambda^2+\lambda+1=0\)); hence \(T^t-I\) is invertible on \(E^2\) whenever \(3\nmid t\). When \(3\mid t\) but \(2\nmid t\), its fixed space on \(E^2\) has dimension \(2\dim\ker(A+I)=N\). When \(6\mid t\), all \(2N\) dimensions are fixed. In particular, the fixed-space dimensions for \(T,T^2,T^3,T^6\) are
\[
1,\quad2,\quad N+1,\quad2N+2.
\]
The order is exactly six.

**4. Primitive-period census.** A linear fixed subspace of dimension \(r\) over \(\mathbb F_q\) contains \(q^r\) vectors. In each parity case all primitive periods divide the stated global order. Successive subtraction over the divisibility poset of \(1,2,4,8\), respectively \(1,2,3,6\), gives exactly the displayed formulas. The top-period counts are positive, so the orders are sharp.

**5. Comparison with the unmodified cube.** On \(Q_d\) without the apex, \(B^2=0\) when \(d\) is even and \(B^2=I\) when odd. The same wave calculation gives global order \(4\) for even \(d\) and \(6\) for odd \(d\). Thus the even-dimensional period doubling comes specifically from the apex contribution \(J\ne0\) to \(A^2\), not from any change in the local rule.

## Verification

Standalone checks are provided in `check_ranks.py` and `check_states.py`. Run with a standard Python 3 interpreter. `check_ranks.py` constructs the graph adjacency over \(\mathbb F_2\), computes full matrix powers of the wave independently, and checks fixed-space nullities at all iterates \(1,\ldots,24\) for dimensions \(2\) through \(6\) (120 exact matrix comparisons). Since all matrix coefficients belong to \(\mathbb F_2\), these ranks remain unchanged over every field extension \(\mathbb F_{2^f}\). `check_states.py` independently simulates all \(263168\) two-layer binary configurations on the cone graphs of dimensions \(2\) and \(3\), detecting each configuration's least period and matching the closed formulas. Full command output is in the corresponding `.out` files. These finite checks are evidence for, but not substitutes for, the arbitrary-dimensional proof above.

## Relationship to prior work

Macfarlane (2004) studies one-dimensional reversible second-order linear cellular automata and converts them into first-order matrix automata, with principal results concerning the evolving weights of configurations from selected seeds. Steeb and Hardy (2007) explicitly describe time-reversible cellular automata obtained from a two-level wave rule on one-dimensional lattices. Vlasov (2014) considers spatial two-dimensional reversible second-order systems and derives support-weight recurrences. These establish the reversible-wave setting but do not supply the apex-cube Jordan-rank argument or the complete primitive-period census here.

An earlier cycle/wheel-graph wave calculation applies to a cone over a four-cycle, which is the excluded \(d=2\) boundary, not to cones over higher-dimensional cubes. Hypercube first-order parity dynamics and Cartesian-product wave systems concern different update maps or graph classes. The new result is the all-dimensional apex-induced transition and complete orbit count, rather than reversibility itself.

## Limitations

The theorem is restricted to characteristic two and the open-neighbor sum rule. It does not address nonlinear excitation, noisy dynamics, positive characteristic other than two, or cones over general Cayley graphs. No claim of absolute priority is made: unindexed mathematically equivalent results might exist. The proof is an ordinary finite-dimensional algebraic argument; its checks do not constitute independent review.

## References

1. A. J. Macfarlane, *Linear reversible second-order cellular automata and their first-order matrix equivalents*, Journal of Physics A 37 (2004), 10791–10814. DOI: 10.1088/0305-4470/37/45/006. First public journal date: 2004-10-28. Accessible manuscript: https://citeseerx.ist.psu.edu/document?doi=f3921158b9871d8db8d16cde33822fabde049a6b&repid=rep1&type=pdf
2. W.-H. Steeb and Y. Hardy, *One-Dimensional Cellular Automata, Conservation Laws and Partial Differential Equations*, Zeitschrift für Naturforschung A 62 (2007), 569–572. DOI: 10.1515/zna-2007-10-1103. https://www.degruyter.com/document/doi/10.1515/zna-2007-10-1103/html
3. A. Yu. Vlasov, *On number of nonzero cells in some two-dimensional reversible second-order cellular automata* (first arXiv version 2014-07-24), arXiv:1407.6553. https://arxiv.org/abs/1407.6553
