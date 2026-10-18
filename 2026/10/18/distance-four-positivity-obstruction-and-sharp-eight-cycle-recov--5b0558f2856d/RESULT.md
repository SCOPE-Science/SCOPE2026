# Distance-four positivity obstruction and sharp eight-cycle recovery for the second-order Padé heat step

## Finding

Let \(G\) be a finite connected simple undirected graph, let \(L=D-A\) be its combinatorial Laplacian, and define the second-order \([0/2]\) Padé heat update
\[
T_G(h)=\bigl(I+hL+\tfrac12 h^2L^2\bigr)^{-1},\qquad h\geq0.
\]
This update is well-defined, symmetric, positive definite, and mass preserving at every step, but its entries need not be nonnegative. The following assertions hold.

**(1) Distance-four obstruction.** If \(G\) has graph diameter at least four, then for every pair of vertices \(u,v\) at graph distance exactly four,
\[
[T_G(h)]_{uv}=-\tfrac14(A^4)_{uv}h^4+O_G(h^5)<0
\]
for all sufficiently small positive \(h\). In particular, a small step cannot be guaranteed positivity preserving merely by symmetric diffusion, positive definiteness, and conservation.

**(2) Exact cycle-size boundary.** For the unweighted undirected cycle \(C_n\), \(3\leq n\leq7\), every entry of \(T_{C_n}(h)\) is strictly positive for every \(h>0\). For every \(n\geq8\), the update has negative entries for all sufficiently small positive \(h\), but is strictly entrywise positive for all sufficiently large \(h\).

**(3) Complete sharp recovery threshold at the first failing cycle.** On \(C_8\), the matrix \(T_{C_8}(h)\) is entrywise nonnegative **if and only if** \(h=0\) or \(h\geq h_8\), where \(h_8\approx0.213757965844620\) is the unique positive root of
\[
4h^4+22h^3+17h^2-1=0.
\]
At \(h=h_8\), the entries connecting antipodal vertices are zero and all other entries are positive; for \(h>h_8\), all entries are strictly positive. Thus the threshold is an exact, not merely sufficient, positivity cutoff.

## Assumptions and scope

Graphs are finite, connected, simple, undirected, and unweighted; the parameter \(h\) is any nonnegative real. The cycle \(C_n\) has its standard nearest-neighbor edges and \(n\ge3\). Entrywise nonnegative means every matrix entry is nonnegative, not merely that the matrix is positive semidefinite. The normalized combinatorial Laplacian convention is **not** used; scaling the edge conductances scales the step parameter accordingly. No claim is made that every graph of diameter at most three enjoys unconditional positivity, or that cycles longer than eight have a single global positivity cutoff.

## Proof

**Well-definedness and conservation.** All eigenvalues \(\lambda\) of \(L\) are nonnegative, and \(1+h\lambda+\tfrac12h^2\lambda^2>0\). Hence the inverse exists, is symmetric positive definite, and fixes the all-ones vector because \(L\mathbf1=0\). A connected graph has a simple zero eigenvalue, so spectral decomposition also shows \(T_G(h)\to\mathbf1\mathbf1^{\mathsf T}/|V(G)|\) entrywise as \(h\to\infty\). Eventual strict positivity is therefore a general spectral fact rather than a claim of novelty for the large-step regime.

**Distance-four coefficient.** With \(R(z)=(1-z+\tfrac12z^2)^{-1}\), multiplication by its quadratic denominator gives the exact Taylor coefficients
\[
R(z)=1+z+\tfrac12z^2+0z^3-\tfrac14z^4+O(z^5).
\]
For \(d_G(u,v)=4\), \((L^j)_{uv}=0\) for \(0\leq j<4\), because a product of fewer than four diagonal/edge factors cannot connect the pair. For \(j=4\), all contributing walks must consist of four off-diagonal steps, so \((L^4)_{uv}=(-1)^4(A^4)_{uv}=(A^4)_{uv}>0\); positivity follows from a length-four geodesic. Substituting \(z=-hL\) proves the displayed negative leading coefficient. For \(C_n\), a distance-four pair exists exactly when \(n\geq8\).

**Exact finite-cycle positivity certificates.** Label vertices modulo \(n\), and put \(t_{n,d}(h)=[T_{C_n}(h)]_{0d}\). Circulant symmetry makes \(t_{n,d}=t_{n,n-d}\). For each \(3\leq n\leq7\), direct polynomial multiplication of \(I+hL+\tfrac12h^2L^2\) with its adjugate yields rational forms \(t_{n,d}(h)=N_{n,d}(h)/D_n(h)\), with \(D_n\) and every \(N_{n,d}\) having nonnegative coefficients and, for \(h>0\), strictly positive values. Explicit common denominators and numerators for each distance \(0\leq d\leq\lfloor n/2\rfloor\) are recorded below; this is a finite exact-algebra certificate, not a numerical search.

For \(n=3\):
\[
\begin{aligned}
D_3&=9h^2+6h+2,\\
(N_{3,0},N_{3,1})&=(3h^2+2h+2,\ h(3h+2)).
\end{aligned}
\]
For \(n=4\):
\[
\begin{aligned}
D_4&=(2h^2+2h+1)(8h^2+4h+1),\\
N_{4,0}&=4h^4+6h^3+9h^2+4h+1,\\
N_{4,1}&=h(2h+1)(2h^2+2h+1),\\
N_{4,2}&=h^2(4h^2+6h+1).
\end{aligned}
\]
For \(n=5\):
\[
\begin{aligned}
D_5&=25h^4+50h^3+50h^2+20h+4,\\
N_{5,0}&=5h^4+10h^3+22h^2+12h+4,\\
N_{5,1}&=h(5h^3+10h^2+12h+4),\\
N_{5,2}&=h^2(5h^2+10h+2).
\end{aligned}
\]
For \(n=6\):
\[
\begin{aligned}
D_6&=(h^2+2h+2)(8h^2+4h+1)(9h^2+6h+2),\\
N_{6,0}&=12h^6+38h^5+115h^4+120h^3+76h^2+24h+4,\\
N_{6,1}&=2h(2h+1)(3h^4+8h^3+16h^2+8h+2),\\
N_{6,2}&=h^2(12h^4+38h^3+35h^2+16h+2),\\
N_{6,3}&=2h^4(2h+1)(3h+8).
\end{aligned}
\]
For \(n=7\):
\[
\begin{aligned}
D_7&=49h^6+196h^5+392h^4+364h^3+196h^2+56h+8,\\
N_{7,0}&=7h^6+28h^5+112h^4+140h^3+108h^2+40h+8,\\
N_{7,1}&=h(7h^5+28h^4+84h^3+84h^2+40h+8),\\
N_{7,2}&=h^2(7h^4+28h^3+42h^2+28h+4),\\
N_{7,3}&=7h^4(h^2+4h+2).
\end{aligned}
\]
Each polynomial identity can independently be checked by multiplying the circulant finite matrices. Since all displayed factors are strictly positive for \(h>0\), assertion (2) follows for \(n\le7\).

**Exact \(C_8\) cutoff.** For \(C_8\) write
\[
\begin{aligned}
U&=2h^2+2h+1,\\ V&=8h^2+4h+1,\\
W&=h^4+4h^3+8h^2+4h+1,\\ D_8&=2UVW.
\end{aligned}
\]
Direct inversion gives \(t_{8,d}=N_{8,d}/D_8\), where
\[
\begin{aligned}
N_{8,0}&=4h^8+22h^7+113h^6+208h^5+235h^4+156h^3+66h^2+16h+2,\\
N_{8,1}&=h(2h+1)U(h^4+4h^3+16h^2+8h+2),\\
N_{8,2}&=h^2(4h^2+6h+1)W,\\
N_{8,3}&=h^4(h+4)(2h+1)U,\\
N_{8,4}&=h^4(4h^4+22h^3+17h^2-1).
\end{aligned}
\]
The denominator and the numerators with \(d\le3\) are strictly positive whenever \(h>0\). The remaining sign is the sign of \(p(h)=4h^4+22h^3+17h^2-1\). Now \(p(0)=-1\), \(p(h)\to+\infty\), and \(p'(h)=16h^3+66h^2+34h>0\) for \(h>0\). Consequently exactly one positive root exists and the exact nonnegative step set is \(\{0\}\cup[h_8,\infty)\). The quoted decimal is a numerical approximation of this algebraic root, not its definition.

Finally, for every \(n\ge8\), the distance-four proof gives failure near \(h=0^+\), and the spectral limit gives eventual positivity. This completes the three assertions.

## Verification

The included standalone `artifacts/verify_pade02_cycles.py` builds the Laplacians and Padé matrices independently, performs symbolic inversion for all six cycle sizes, verifies the inverse and row-sum identities, checks cyclic and reversal symmetries, checks all positive-coefficient certificates, and reproduces the \(C_8\) exact numerator and root. It also checks the distance-four coefficient on an eight-vertex path. Execution with SymPy 1.14 produced 259 passed symbolic assertions. The finite checks establish the explicitly enumerated small-cycle factorization claims; the graph-family results follow analytically from the walk-length argument and spectral limit.

## Relationship to prior work

Positivity-preserving Padé damping for parabolic problems was studied by Wade, Khaliq, Siddique, and Yousuf (first published 29 September 2004), in the context of combinations of diagonal and positivity-preserving schemes. Padé discretizations and their possible failures to preserve positivity were investigated by Zappavigna, Colaneri, Kirkland, and Shorten (2010, 2012). Their examined arguments focus on diagonal Padé approximants and positive-system conditions, whereas the claim here concerns the \([0/2]\) approximation and exact signs on graph heat kernels. Existing literature on unconditional positivity of backward-Euler-filtered Crank–Nicolson likewise concerns a different rational map.

Itkin and Kazbek (2026) explicitly study the same \([0/2]\) Padé map and establish large-step positivity above a computable threshold for their class of eventually positive generators. This general eventual-positivity phenomenon is acknowledged as prior work, not presented as original. The claimed new content is the distance-four small-step obstruction with its sharp cycle-size boundary and, especially, the **exact algebraic threshold on \(C_8\)**; the available abstract of that recent paper does not settle whether these specialized results are already contained in its full text. An inaccessible full text is a residual originality risk.

The published eight-state Markov obstruction for the distinct fourth-order diagonal \([2/2]\) approximant treats a different rational function and a directed birth-chain witness. It does not imply the present \([0/2]\) cycle formulas merely from its eight-state count.

## Limitations

All assertions concern the completed rational update, not intermediate stage positivity, nonlinear PDE discretizations, or floating-point roundoff. The general distance-four result is a sufficient condition for small-step negativity, not a converse for arbitrary graphs. The complete global positivity set is given only for \(C_8\), not for every longer cycle. Eventual positivity is a known spectral phenomenon. The potential presence of an equivalent exact graph-specific threshold in unexamined recent literature cannot be excluded; independent review has not been undertaken.

## References

1. B. A. Wade, A. Q. M. Khaliq, M. Siddique, M. Yousuf, “Smoothing with positivity-preserving Padé schemes for parabolic problems with nonsmooth data,” *Numerical Methods for Partial Differential Equations* 21 (2005), 553–573; first published 29 September 2004. https://doi.org/10.1002/num.20039
2. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, “On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems,” MTNS 2010, July 2010; accessible repository full text deposited 15 October 2010. https://mural.maynoothuniversity.ie/id/eprint/2195/
3. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, “Essentially Negative News About Positive Systems,” Linear Algebra and its Applications 436 (2012), 3425–3442. https://doi.org/10.1016/j.laa.2011.12.021
4. A. Itkin, R. Kazbek, “Diagonal Frog meets ADI: trading matrix exponentials for rational maps in the Fokker–Planck equation,” arXiv:2608.22703, first posted 24 August 2026. https://arxiv.org/abs/2608.22703
5. Published research record, “Eight-state barrier for Markov positivity of the [2/2] Padé map,” https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab
6. Published research record, “Unconditional lattice positivity from backward-Euler-filtered Crank–Nicolson,” https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-backward-euler-filtered-cn-lattice-positivity--1f6f56bd0eac
