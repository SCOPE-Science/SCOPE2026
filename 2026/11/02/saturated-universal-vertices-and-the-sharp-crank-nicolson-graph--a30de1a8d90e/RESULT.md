# Saturated universal vertices and the sharp Crank–Nicolson graph positivity frontier

## Finding
For an arbitrary connected weighted undirected graph with \(N\ge3\) vertices and conductances \(0\le w_{ij}\le c\), where \(c>0\) and \(w_{ij}=w_{ji}\), let \(L\) be the weighted Laplacian and
\[
C(h)=\bigl(I+\tfrac h2L\bigr)^{-1}\bigl(I-\tfrac h2L\bigr).
\]
There is a unique finite sharp horizon \(h_*(G)\) such that \(C(h)\) is entrywise nonnegative precisely for \(0\le h\le h_*(G)\). It satisfies
\[
\boxed{h_*(G)\ge \frac{2}{c(N-2)}.}
\]
**Equality holds if and only if** some vertex has conductance exactly \(c\) to *every* other vertex. At the universal bound \(h_0=2/[c(N-2)]\), the zero diagonal entries of \(C(h_0)\) are precisely those saturated universal vertices; all off-diagonal entries are strictly positive. In particular, arbitrary additional edges away from one saturated universal vertex leave the exact positivity horizon unchanged.

The following sharp quantitative reserve holds at the universal bound. If \(d_i=\sum_{j\ne i}w_{ij}\) denotes weighted degree, then
\[
\boxed{C(h_0)_{ii}\ge
\frac{N-2}{2c(N-1)^2}\bigl((N-1)c-d_i\bigr).}
\]
A positive weighted-degree deficit therefore certifies a strictly positive diagonal margin.

For a uniform-conductance complete multipartite graph \(K_{n_1,\ldots,n_k}\), with \(k\ge2\), positive part sizes, \(N=\sum_i n_i\ge3\), all cross-part conductances \(c\), and \(a=\min_i n_i\), the *entire* sharp horizon is
\[
\boxed{h_*(K_{n_1,\ldots,n_k})=
\frac{a+\sqrt{a^2+4(N-a)(N-2)}}{c(N-a)(N-2)}.}
\]
Exactly the vertices in minimum-size parts first reach zero diagonal at this horizon. In particular, for fixed \(N\), the sharp horizon depends only on \(a\), not on the other part sizes or their number. It is strictly increasing in \(a\). For a fixed number \(k\) of parts, its minimum is attained by every partition containing a singleton part, and its maximum by precisely the partitions whose smallest part has size \(\lfloor N/k\rfloor\). The complete graph, the unit-weight star, and all complete split graphs with at least one singleton part share the identical horizon \(2/[c(N-2)]\).

## Assumptions and scope
The graph is undirected, finite, connected, and weighted, with one symmetric nonnegative conductance per unordered pair; zero means the edge is absent. The parameter \(c>0\) is an upper bound on every pair conductance, *not* a total-conductance or weighted-degree budget. The matrix \(L\) is the combinatorial weighted Laplacian: \(L_{ii}=\sum_{j\ne i}w_{ij}\), \(L_{ij}=-w_{ij}\) for \(i\ne j\). The update is applied to nonnegative column states, or to row probabilities by symmetry. Entrywise nonnegativity means preservation of every nonnegative initial vector; it is stronger than stability and independent of stage-level positivity. The main theorem assumes \(N\ge3\). When \(N=2\), the connected symmetric two-state problem is unconditionally end-step positive and no finite horizon exists.

## Proof
**1. Diagonal reduction and unique crossing.** Put \(s=h/2\) and \(R_s=(I+sL)^{-1}\). The Cayley identity gives \(C(h)=2R_s-I\). Since \(-L\) is an irreducible Markov generator, for \(s>0\)
\[
R_s=\int_0^\infty e^{-u}e^{-usL}\,du
\]
is strictly positive entrywise and has row sums one. Thus the only possible negative entries in \(C(h)\) are diagonal entries, and \(C(h)\ge0\) if and only if \((R_s)_{ii}\ge1/2\) for every \(i\). In an orthonormal eigenbasis of \(L\), the spectral projection onto constants contributes \(1/N\) to every return diagonal. Therefore
\[
(R_s)_{ii}=\frac1N+\sum_{\lambda_j>0}\frac{|u_j(i)|^2}{1+s\lambda_j},
\]
which decreases strictly from \(1\) to \(1/N<1/2\), because the total weight of the positive-eigenvalue terms is \(1-1/N\). Each diagonal consequently crosses \(1/2\) exactly once. The smallest crossing is the finite horizon; no later return to positivity is possible.

**2. Comparison against the saturated complete graph.** Define \(L_c=c(NI-\mathbf1\mathbf1^{\mathsf T})\), the Laplacian of the complete graph with every conductance \(c\). Then
\[
D=L_c-L=\sum_{i<j}(c-w_{ij})(e_i-e_j)(e_i-e_j)^{\mathsf T}\succeq0.
\]
Set \(A_c=I+sL_c\), \(A_G=I+sL=A_c-sD\), and \(x_c=A_c^{-1}e_i\). The strictly concave quadratic variational identity
\[
e_i^{\mathsf T}A_G^{-1}e_i=\max_x\bigl(2e_i^{\mathsf T}x-x^{\mathsf T}A_Gx\bigr)
\]
gives
\[
(R_s)_{ii}\ge (A_c^{-1})_{ii}+s x_c^{\mathsf T}Dx_c.
\]
The complete-graph resolvent is explicit:
\[
x_c=\frac1N\mathbf1+\frac{1}{1+sNc}\left(e_i-\frac1N\mathbf1\right),\qquad
(A_c^{-1})_{ii}=\frac{1+sc}{1+sNc}.
\]
Since \(D\mathbf1=0\),
\[
x_c^{\mathsf T}Dx_c=\frac{\sum_{j\ne i}(c-w_{ij})}{(1+sNc)^2}.
\]
Consequently, for every \(s\ge0\),
\[
C(2s)_{ii}\ge\frac{1-sc(N-2)}{1+sNc}
+\frac{2s\sum_{j\ne i}(c-w_{ij})}{(1+sNc)^2}.
\]
At \(s_0=1/[c(N-2)]\) this reduces to the claimed degree-deficit reserve and proves nonnegativity of all diagonals. The variational inequality is an equality if and only if \(x_c\) is also the unique maximizer for \(A_G\), equivalently \(Dx_c=0\). For \(s>0\), this is equivalent to \(De_i=0\), equivalently \(c-w_{ij}=0\) for every \(j\ne i\). Hence the diagonal of the update is zero at \(h_0=2s_0\) exactly at saturated universal vertices. If none exist, finitely many strictly positive diagonals persist on a nonzero interval beyond \(h_0\). If one exists, its strictly decreasing resolvent diagonal becomes negative immediately after \(h_0\). This establishes the necessary-and-sufficient equality classification.

**3. Exact complete-multipartite return law.** In a complete multipartite graph with unit cross-part conductance (scale back by \(c\) afterwards), the orthogonal Laplacian eigenspaces are: constants with eigenvalue \(0\); vectors constant on each part and globally zero-sum with eigenvalue \(N\); and, for each part of size \(b\), vectors supported there and summing to zero, with eigenvalue \(N-b\). For a vertex in a part of size \(b\), the diagonal orthogonal-projector weights onto these subspaces are respectively \(1/N\), \(1/b-1/N\), and \(1-1/b\). Writing \(x=sc\), its exact return diagonal is
\[
r_b(x)=\frac1N+\frac{1-1/b}{1+(N-b)x}+\frac{1/b-1/N}{1+Nx}.
\]
Direct subtraction for any admissible part sizes \(b_1,b_2\) yields
\[
r_{b_1}(x)-r_{b_2}(x)=
\frac{x(b_1-b_2)[1+(N-1)x]}{[1+Nx][1+(N-b_1)x][1+(N-b_2)x]}.
\]
Therefore the smallest parts always attain the minimum return diagonal for every \(x>0\), irrespective of the other part sizes. Finally,
\[
2r_b(x)-1=
\frac{1+bx-(N-b)(N-2)x^2}
{[1+(N-b)x][1+Nx]}.
\]
For \(N\ge3\), the numerator has exactly one positive root,
\[
x_b=\frac{b+\sqrt{b^2+4(N-b)(N-2)}}{2(N-b)(N-2)}.
\]
Choosing \(b=a\) and using \(h=2x/c\) gives the announced formula, and strict ordering shows precisely which diagonals vanish. The same ordering implies strict increase of the horizon in the smallest part size. The fixed-\(N\), fixed-\(k\) extremal partition statements follow from \(1\le a\le\lfloor N/k\rfloor\).

## Verification
The attached `verify.py` uses only Python's standard library and rational Gauss–Jordan inversion. With a fixed random seed it checks 456 independently weighted connected graphs on 3–8 vertices, including 28 cases with at least one saturated universal vertex, against the **exact** critical universal step. It tests all 12,616 off-diagonal entries, stochastic row sums, the characterization of every zero diagonal, and immediate post-frontier negativity in the saturated cases.

The same program independently enumerates all 86 unordered multipartite partitions on 3–9 vertices (with at least two parts). For each one it constructs the full graph Laplacian, uses exact integer-square-root rational enclosures of the claimed algebraic critical step, and confirms the crossing direction and all 270 predicted minimum-part zero-diagonal locations. Numerical or finite exact tests do not replace the infinite-family analytical proof above. Replay with `python verify.py`; the expected concluding line starts `VERIFICATION_OK`.

## Relationship to prior work
Crank and Nicolson introduced the trapezoidal time discretization; Horváth analyzed positivity conditions for general Runge–Kutta discretizations and positively invariant cones. Fallat and Tsatsomeros proved the general matrix-Cayley identity used here and investigated \(M\)-matrix positivity classes. A published return-resolvent result for reversible Markov chains already states the general diagonal test and the exact saturated-complete-graph threshold \(2/[c(N-2)]\); neither observation is claimed here as original. Klee and Stamps recapitulate the known complete-multipartite Laplacian spectrum, likewise not claimed as new.

The assessed additions are (i) the sharp lower envelope over **all independently weighted graphs with pair conductances capped by \(c\)**, including the complete equality characterization and quantitative degree-deficit reserve, and (ii) the exact multipartite threshold and the smallest-part universality for arbitrary part profiles. The general return-diagonal criterion and known spectra provide important starting ingredients but do not themselves state those equality classes or the profile-invariance formula. A specialized previous derivation may exist; no publication-priority guarantee is made.

## Limitations
The conductance cap is a pairwise upper bound, not a total-resource constraint. The multipartite closed formula requires equal cross-part conductances. The classification concerns end-step entrywise positivity, not positive internal stages, nonlinear invariance, convergence order, or finite-precision guarantees. The case \(N=2\) is excluded from the finite-horizon statement. General graph horizons beyond the universal lower bound are not given in closed form. The fixed-step sharpness statements are analytic; numerical checks are finite corroboration only. The full text of a relevant general positive-cone discretization source was not accessible, leaving a prior-coverage risk.

## References
1. J. Crank and P. Nicolson, *A practical method for numerical evaluation of solutions of partial differential equations of the heat-conduction type*, Proc. Cambridge Philosophical Society 43 (1947), 50–67, DOI: 10.1017/S0305004100023197.
2. Z. Horváth, *Positively invariant cones of dynamical systems under Runge–Kutta and Rosenbrock-type discretization*, Proceedings in Applied Mathematics and Mechanics 4 (2004), 688–689, DOI: 10.1002/pamm.200410325. First published online 2004-12-27.
3. S. M. Fallat and M. J. Tsatsomeros, *On the Cayley transform of positivity classes of matrices*, Electronic Journal of Linear Algebra 9 (2002), 190–196, DOI: 10.13001/1081-3810.1086.
4. S. Klee and M. T. Stamps, *Eigenvalues of graph Laplacians via rank-one perturbations*, arXiv:2008.01669v1 (2020), Proposition 6, on complete-multipartite Laplacian spectra.
5. *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains*, publicly available mathematical research record, October 2026, identifier `d475df91cd2a` (published-finding corpus/2026 repository, 2026/10/4).
6. D. J. Duffy, *A Critique of the Crank Nicolson Scheme: Strengths and Weaknesses for Financial Instrument Pricing*, Wilmott magazine (2004), pp. 68–76.
