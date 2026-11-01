# One pendant edge preserves majority equilibria but creates Fibonacci-many oscillations

## Finding
Let \(G_n\), for each integer \(n\ge3\), be the labelled graph formed by adding a single pendant vertex \(p\) adjacent to vertex \(0\) of the cycle \(C_n\). Under simultaneous binary strict-neighbor-majority dynamics with self-retention on ties, define \(H_n\) to be the number of fixed configurations and \(N_n\) to be the number of primitive period-two temporal orbits. Distinct labelled states are counted separately; only the two time phases of each primitive orbit are identified. Then
\[
H_n=L_n+2\cos(\pi n/3),\qquad
N_n=F_{n-2}-q_{n-3}+\mathbf1_{2\mid n},
\]
where \(F_0=0\), \(F_1=1\), \(F_{j+2}=F_{j+1}+F_j\), \(L_0=2\), \(L_1=1\), \(L_{j+2}=L_{j+1}+L_j\), and \(q_j\) is the six-periodic integer sequence \((1,1,0,-1,-1,0)\) indexed by \(j\bmod6\). The cosine term is always an integer.

Adding the pendant vertex leaves the fixed-point count **exactly equal** to that of the unperturbed cycle \(C_n\), but creates precisely \(F_{n-2}-q_{n-3}\) additional primitive two-cycles. For every odd \(n\ge5\), the original cycle has no primitive two-cycle whereas \(G_n\) has at least two. The additional count is asymptotic to \(\varphi^{n-2}/\sqrt5\), with \(\varphi=(1+\sqrt5)/2\). Every forward trajectory eventually becomes fixed or two-periodic, so this is the complete temporal recurrent-orbit census.

## Assumptions and scope
A configuration is \(x\in\{0,1\}^{n+1}\), with cycle bits \(x_0,\ldots,x_{n-1}\) in cyclic order and pendant bit \(x_p\). For every vertex \(i\), its next bit is one if strictly more than half its neighbors presently have bit one, zero if strictly fewer than half have bit one, and its old bit if exactly half do. All vertices update synchronously. There are no self-loops in \(G_n\). For counting periodic orbits, graph automorphisms and color complementation are not identified. Only the temporal exchange of the two states in a genuine period-two orbit is factored out.

## Proof
**1. Period restriction.** Write spins as \(s_i(t)=2x_i(t)-1\in\{-1,1\}\). Let \(W\) be the symmetric adjacency matrix with an added diagonal entry \(W_{ii}=1\) precisely at degree-two vertices (the cycle vertices other than \(0\)); its other diagonal entries are zero. A tie-retaining majority update is exactly
\(s_i(t+1)=\operatorname{sgn}(\sum_j W_{ij}s_j(t))\), and each field is a nonzero odd integer. Define \(\Phi_t=\sum_{i,j}W_{ij}s_i(t+1)s_j(t)\). Symmetry gives
\[
\Phi_t-\Phi_{t-1}
=\sum_i\bigl(s_i(t+1)-s_i(t-1)\bigr)\sum_jW_{ij}s_j(t)\ge0.
\]
Each nonzero summand is strictly positive, since \(s_i(t+1)\) has the sign of its nonzero field. The integer \(\Phi_t\) is bounded, so eventually all its increments vanish, forcing \(s_i(t+1)=s_i(t-1)\) for every vertex. Thus every orbit enters a fixed point or a primitive two-cycle.

**2. All two-cycle flip sets.** A degree-two cycle vertex that changes bit in a genuine two-cycle must see both neighbors of the opposite bit at that phase, and the same holds at the other phase. Both neighbors therefore change bit. Since vertices \(1,\ldots,n-1\) form a connected path of degree-two cycle vertices, flipping even one forces the whole cycle to flip. Such a cycle must alternate in space, hence requires even \(n\); its pendant vertex is the time-delayed root, so it also flips. There are exactly two complementary alternating states, constituting **one** primitive temporal orbit.

If none of the degree-two cycle vertices flips, the root and leaf must both flip in a genuine two-cycle (otherwise the leaf, which copies the root one step later, also stays fixed). The leaf must be opposite to the root at each phase. With the two rim-neighbor bits fixed, the degree-three root flips in both directions exactly when those two bits differ. Each fixed interior cycle vertex is stable at both phases exactly when it has at least one fixed neighbor of its own bit. Consequently the length-\(n-1\) word \(x_1\cdots x_{n-1}\) must have opposite endpoints, with every maximal constant-bit run of length at least two. Conversely each such word produces exactly one primitive temporal two-cycle (the root and leaf are opposite and reverse on each step), and these exhaust the remaining cases.

**3. Counting the new two-cycles.** Let \(a_\ell\) count binary words of length \(\ell\) having opposite endpoint bits and all constant-bit runs of length at least two. Such words have \(2r\ge2\) constant runs and two possible initial bits. With \(\ell\) total symbols and each run length at least two,
\[
a_\ell=2\sum_{r\ge1}\binom{\ell-2r-1}{2r-1},
\]
where out-of-range binomial coefficients vanish. A run has ordinary generating function \(R(z)=z^2/(1-z)\). Thus
\[
\sum_{\ell\ge0}a_\ell z^\ell
=\frac{2R(z)^2}{1-R(z)^2}
=\frac{z^2}{1-z-z^2}-\frac{z^2}{1-z+z^2}.
\]
The two coefficient sequences on the right are Fibonacci numbers and the six-periodic \(q\)-sequence, respectively, giving \(a_{n-1}=F_{n-2}-q_{n-3}\). Including the unique all-flipping orbit for even \(n\) yields the asserted \(N_n\).

**4. Counting equilibria.** In a fixed configuration the leaf must equal the root. The root consequently remains fixed exactly when at least one of its two cycle neighbors shares its bit. All other rim vertices are fixed exactly when at least one of their cycle neighbors shares their bit. Thus fixed configurations correspond bijectively to cyclic binary words with no isolated singleton run, exactly as on the bare cycle. Use pair states ordered \(00,01,10,11\) and transitions \((a,b)\mapsto(b,c)\) unless \(a=c\ne b\). The transition matrix is
\[
M=\begin{pmatrix}1&1&0&0\\0&0&0&1\\1&0&0&0\\0&0&1&1\end{pmatrix}.
\]
The count is \(\operatorname{tr}(M^n)\). Direct determinant expansion gives
\(\det(\lambda I-M)=(\lambda^2-\lambda-1)(\lambda^2-\lambda+1)\). Its four roots are the two Fibonacci–Lucas roots and \(e^{\pm i\pi/3}\), so the trace is \(L_n+2\cos(\pi n/3)\), as claimed.

## Verification
The included standard-library Python program `verify.py` directly simulates all \(2^{n+1}\) configurations for every \(3\le n\le17\), independently counting fixed states and primitive two-cycles via a two-step return test. It compares the results to the closed expressions, the independent run-composition sum, and the four-state transfer trace. It also checks every period-two flip set and its stated geometry for \(3\le n\le13\), and verifies the two algebraic representations for \(3\le n\le100\). Reproduce with `python3 verify.py`; `verification_output.txt` is the output from a successful execution. The finite tests corroborate, and do not substitute for, the preceding infinite-family proof.

For \(n=3,4,5,6,7,8,9,10\), the primitive two-cycle counts are respectively \(0,1,2,5,6,9,12,21\). For the same values, the fixed-state counts are \(2,6,12,20,30,46,74,122\).

## Relationship to prior work
The classical finite symmetric-threshold period-two theorem of Goles and Olivos guarantees eventual periods at most two but does not itself supply this graph-specific counting formula. Benjamini, Chan, O'Donnell, Tamuz and Tan formulate the same tie-retaining majority rule, credit the finite-graph period-two property, and study probabilistic and infinite-graph convergence rather than the present one-leaf recurrent census. The unperturbed-cycle fixed-state count is a known local-word count; novelty is claimed only for the combined pendant-edge invariance, complete flip-set classification, and exact new-orbit law.

## Limitations
The statement concerns one pendant edge, synchronous updates, the specified tie convention, and **recurrent** states. It does not compute transient times or basin sizes, nor does it cover more than one pendant edge, weighted updates, or asynchronous schedules. Although relevant literature was inspected, historical equivalence in differently named threshold-automata treatments cannot be ruled out. The 1980 Goles–Olivos note was available at the abstract/bibliographic level, not as full text.

## References
1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189. DOI: https://doi.org/10.1016/0012-365X(80)90121-1. Bibliographic record and abstract were consulted.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, first posted 2014-05-11, https://arxiv.org/html/1405.2486v1. Full accessible text was examined, especially the introduction and the cited finite-graph theorem.
