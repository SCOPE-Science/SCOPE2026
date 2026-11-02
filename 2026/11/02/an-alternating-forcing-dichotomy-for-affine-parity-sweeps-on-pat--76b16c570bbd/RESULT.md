# An alternating forcing dichotomy for affine parity sweeps on paths

## Finding

For every integer \(n\ge2\), every finite field \(\mathbb F_q\) of characteristic two, every vector of offsets \(b=(b_1,\ldots,b_n)\in\mathbb F_q^n\), and **every permutation** prescribing one sequential update of each vertex of the path \(P_n\), there is an exact and schedule-independent census of the periodic orbits.

At vertex \(i\), replace its current state by its state plus its currently available neighbors' states plus \(b_i\), with all additions in \(\mathbb F_q\). Let \(F\) denote the completed sweep, put \(N=n+1\), and set
\[
\eta=\begin{cases}
0,&n\text{ even or }\sum_{i\text{ odd}}b_i=0,\\
1,&n\text{ odd and }\sum_{i\text{ odd}}b_i\ne0.
\end{cases}
\]
Here the sum uses **one-based indices**. For every integer \(t\ge1\), let \(g=\gcd(t,N)\) and \(L=N/g\). Then
\[
\boxed{\#\operatorname{Fix}(F^t)=
\begin{cases}
q^g,&\eta=0\text{ and }L\text{ even},\\
q^{g-1},&L\text{ odd},\\
0,&\eta=1\text{ and }L\text{ even}.
\end{cases}}
\]
In particular, \(F^N=\mathrm{id}\), and \(N\) is its exact permutation order. Every state is periodic from time zero. The number of distinct primitive \(d\)-cycles, for each positive divisor \(d\mid N\), is
\[
\boxed{C_d=\frac1d\sum_{e\mid d}\mu(d/e)\,\#\operatorname{Fix}(F^e).}
\]
No other primitive periods occur.

When \(\eta=0\), every positive divisor of \(N\) is realized as a primitive period, **except period two when \(N\equiv2\pmod4\)**. When \(\eta=1\), the primitive periods are **exactly** the divisors \(d\) of \(N\) for which \(N/d\) is odd. In particular, if \(N\) is a power of two and \(\eta=1\), every one of the \(q^n\) configurations has primitive period \(N\), and there are precisely \(q^n/N\) cycles.

## Assumptions and scope

The graph is the undirected path on labeled vertices \(1,\ldots,n\), with no wraparound, with \(n\ge2\). Each sweep updates every vertex once in any fixed permutation order; the same order and same offsets are used in every subsequent sweep. The field has cardinality \(q=2^h\), \(h\ge1\). There are no simultaneous updates and no changes of the order between sweeps. Write absent endpoint-neighbor states as zero. The state space is \(\mathbb F_q^n\); the local map at vertex \(i\) is
\[
U_i(x)_i=x_i+x_{i-1}+x_{i+1}+b_i,\qquad
U_i(x)_j=x_j\ (j\ne i),
\]
where \(x_0=x_{n+1}=0\) is boundary notation only. This is a finite-state discrete-time dynamical system; primitive period refers to the number of **whole sweeps**.

## Proof

**1. Turn local updates into affine coordinate swaps.** Let \(e_0,\ldots,e_n\) be the standard basis of \(\mathbb F_q^{N}\), put \(\alpha_i=e_{i-1}+e_i\), and define
\[
H_0=\left\{u\in\mathbb F_q^N:\sum_{j=0}^n u_j=0\right\},\qquad
\Phi(x)=\sum_{i=1}^n x_i\alpha_i.
\]
The \(n\) vectors \(\alpha_i\) are independent and belong to the \(n\)-dimensional subspace \(H_0\); therefore \(\Phi\) is a linear isomorphism onto \(H_0\). Let \(s_i\) swap coordinates \(i-1\) and \(i\). The two swapped entries in \(\Phi(x)\) differ (equivalently, sum in characteristic two) by \(x_{i-1}+x_{i+1}\). Direct substitution gives
\[
\Phi\circ U_i\circ\Phi^{-1}(u)=s_i u+b_i\alpha_i.
\]
This remains valid at the endpoints. Thus the full sweep becomes an affine map \(u\mapsto Pu+t_0\) on \(H_0\), where \(P\) is a product of the \(n\) adjacent transpositions \(s_i\), each used once, and \(t_0\in H_0\).

**2. Every schedule gives one long cycle.** The adjacent transpositions correspond to the edges of the \((n+1)\)-vertex path. The product of transpositions along all edges of a tree, each once in any order, is a single cycle on its vertices: deleting a leaf shows inductively that the transposition incident to that leaf inserts its label into the unique cycle on the remaining tree. Consequently, \(P\) is a permutation of all \(N\) coordinates consisting of one \(N\)-cycle. All possible schedules are conjugate as coordinate permutations.

**3. Reduce offsets to an affine hyperplane.** For a permutation \(P\) consisting of one \(N\)-cycle, \(\ker(I+P)\) is the one-dimensional constant-vector space and \(\operatorname{im}(I+P)=H_0\). As \(t_0\in H_0\), choose \(v\in\mathbb F_q^N\) with \(t_0=(I+P)v\). Translation by \(v\) conjugates the sweep to the pure coordinate permutation \(P\) acting on the affine hyperplane
\[
H_c=\left\{z\in\mathbb F_q^N:\sum_{j=0}^n z_j=c\right\},\qquad c=\sum_{j=0}^n v_j.
\]
If \(N\) is odd, every \(H_c\) contains a constant vector fixed by \(P\), so the sweep has a fixed point. When \(N\) is even, the condition that \(P\) have a fixed point in \(H_c\) is exactly \(c=0\), since all constant vectors then have coordinate sum zero.

**4. Identify the affine obstruction from the original path.** A fixed configuration of the full sweep must remain unchanged at every individual vertex update, because each coordinate is updated exactly once. Hence the fixed-point equation is
\[
A(P_n)x=b,
\]
where \(A(P_n)\) is the usual neighbor-adjacency matrix. Its determinant recurrence gives determinant one for even \(n\) and zero for odd \(n\) in characteristic two. For odd \(n\), its kernel is exactly the span of \((1,0,1,0,\ldots,1)\). By symmetry of \(A(P_n)\), the system is solvable exactly when \(\sum_{i\text{ odd}}b_i=0\). Thus the affine hyperplane parameter \(c\) is zero precisely when \(\eta=0\) in the even-\(N\) case; for odd \(N\), the fixed-point census is independent of \(c\) regardless.

**5. Count all fixed points of every power.** A vector fixed by \(P^t\) has one freely chosen field value on each of the \(g=\gcd(t,N)\) coordinate cycles, each of common length \(L=N/g\). The constraint defining \(H_c\) is \(L\sum_{j=1}^{g}a_j=c\). In characteristic two, if \(L\) is even this constraint holds for all \(q^g\) choices when \(c=0\) and for none when \(c\ne0\). If \(L\) is odd, it has exactly \(q^{g-1}\) solutions for every \(c\). This proves the boxed fixed-count formula for every positive \(t\), in both cases. Taking \(t=N\) gives all \(q^n\) states fixed. Möbius inversion of fixed-point populations proves the orbit formula.

**6. Show sharp primitive-period support and exact order.** A configuration of period \(d\mid N\) is a length-\(d\) word repeated \(N/d\) times. In \(H_0\), a primitive word of length \(d\ge3\) with two adjacent nonzero entries equal to one has zero coordinate sum and hence is allowed if the repetition factor is odd; if the factor is even, the primitive word with one nonzero entry is allowed. Period one is always represented by zero. At \(d=2\), a primitive two-word has distinct entries and nonzero sum, so it is forbidden exactly when the repetition factor is odd. For \(H_c\) with \(c\ne0\), a repeated word can have total sum \(c\) only when the repetition factor is odd, and then the primitive word with one entry \(c\) realizes every eligible \(d\). This proves both support assertions. Since \(N\ge3\), a primitive length-\(N\) word exists in either case, so the global order is exactly \(N\).

## Verification

Run `python3 verify.py` using Python 3 with the standard library. The script implements each original local update and an independent representation by affine adjacent-coordinate swaps, and checks the exact fixed-point formulas and the full-period identity. It exhaustively tests all offsets and all update permutations at \((n,q)=(2,2),(3,2),(4,2),(5,2),(2,4),(3,4)\), totaling 4,696 offset/order cases and 154,528 evaluated initial states. It additionally checks 936 seeded tests of the local conjugacy and \(N\)-sweep identity over sizes up to 40. The recorded output appears in `verify_output.txt`. These finite checks support the implementation but do not substitute for the preceding proof for arbitrary \(n,q\).

## Relationship to prior work

Macauley, McCammond and Mortveit develop the dynamics-group framework for asynchronously updated Boolean cellular automata on **cycles**. Defant gives an exact affine cycle-orbit classification for invertible rule-150/105 sequential dynamics over \(\mathbb F_2\) with its stated schedule. Chen and Reidys give a general closed matrix representation for arbitrary linear sequential dynamical systems. Those results provide context and important established methods, including classical Coxeter-element ideas; they do not state the path-specific arbitrary-schedule affine-hyperplane fixed-point formula with the alternating forcing obstruction above. The underlying identification of type-\(A\) Coxeter elements with long cycles is classical, not claimed as a new group-theoretic fact.

## Limitations

The result assumes characteristic two, a path (not a cycle), a fixed permutation order repeated each sweep, and fixed vertex offsets. It does not cover general graphs, arbitrary repeated-vertex schedules, changing offsets, or nonlinear update rules. The claim of originality is limited to the combined exact affine path census and its forcing/period-support dichotomy; general linear-system methods and cycle-graph phenomena are acknowledged as known. No independent external mathematical review is claimed.

## References

1. M. Macauley, J. McCammond, and H. S. Mortveit, *Dynamics Groups of Asynchronous Cellular Automata*, arXiv:0808.1238, first submitted 2008-08-08; Journal of Algebraic Combinatorics 33 (2011), 31–55.
2. C. Defant, *Flexible Toggles and Symmetric Invertible Asynchronous Elementary Cellular Automata*, arXiv:1511.06966, first submitted 2015-11-22; Discrete Mathematics 341 (2018), 2363–2378.
3. R. X. F. Chen and C. M. Reidys, *Linear Sequential Dynamical Systems, Incidence Algebras, and Möbius Functions*, arXiv:1510.04930, first submitted 2015-10-16; Linear Algebra and its Applications 553 (2018), 270–291.
