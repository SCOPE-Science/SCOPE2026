# A sharp rim-price deletion transition for fastest diffusion on helm networks

## Finding

Let \(H_n\), for every integer \(n\ge5\), be the helm with central vertex \(o\), a rim cycle \(v_0,\ldots,v_{n-1}\), and private leaves \(u_j\) adjacent to \(v_j\). Independently choose nonnegative conductances on every edge, with price \(t>0\) per rim edge and unit price per spoke and private-leaf edge, under total expenditure \(B>0\). The objective is to maximize the weighted-Laplacian algebraic connectivity \(\lambda_2\), equivalently the decay exponent of the uniform-stationary symmetric continuous-time Markov diffusion.

Set
\[
\delta_n=2\bigl(1-\cos(2\pi/n)\bigr),\qquad \beta=t/\delta_n,
\]
\[
g(c)=2+\frac1{c-1},\qquad h_n(c)=\frac{2c-1}{(2n+1)c-(n+1)}\quad(c>1).
\]

**Low rim price.** If \(0<t<\delta_n\), let \(c_*\) be the unique real number \(>1\) satisfying
\[
1-\frac{\beta}{(c_*-1)^2}-\frac{1-\beta}{((2n+1)c_*-(n+1))^2}=0.
\]
Define \(a_*=h_n(c_*)\) and \(b_*=(g(c_*)-h_n(c_*))/\delta_n\). Both are strictly positive. Put \(C_*=n(a_*+tb_*+c_*)\). The global optimal gap is \(B/C_*\), attained by assigning the conductances \((B/C_*)a_*\), \((B/C_*)b_*\), \((B/C_*)c_*\) respectively to **every** spoke, rim edge, and private-leaf edge. This is the unique optimum **among dihedrally invariant allocations**; no uniqueness is asserted among all independently weighted allocations.

**High rim price.** If \(t>\delta_n\), the global optimal gap is exactly \(B/(5n)\), attained by rate \(3B/(5n)\) on every spoke, zero on every rim edge, and \(2B/(5n)\) on every private-leaf edge. This is again the unique dihedrally invariant optimum.

**Critical price.** At \(t=\delta_n\), the same optimal gap is \(B/(5n)\). All invariant optima have leaf rate \(2B/(5n)\); choosing any dimensionless \(a\in[3/(3n+1),3]\), their spoke and rim rates are respectively \((B/(5n))a\) and \((B/(5n))(3-a)/\delta_n\). Hence a genuine continuum of invariant optimal allocations connects a rim-positive graph to the rim-deleted graph.

In particular, \(\delta_n\sim4\pi^2/n^2\). When all edge prices equal \(1\), every \(n\ge7\) has an optimum that deletes the whole rim, \(n=6\) has the critical continuum, and \(n=5\) has strictly positive optimal rim conductance within the symmetric class. The optimization and its proof do not impose any symmetry on feasible allocations.

## Assumptions and scope

All conductances are finite and nonnegative, and the expenditure equation is imposed exactly. The optimum has positive spokes and pendant edges, so the attained graph is connected. The Laplacian is the unnormalized conductance Laplacian, with \(\lambda_2\) its second-smallest eigenvalue. There are exactly \(n\) edges in each of the three classes. Statements on uniqueness refer only to invariant allocations; the theorem proves global optimal **value and attainment** among unrestricted assignments. No discrete-time stochastic-matrix row-sum or holding-probability constraints are imposed.

## Proof

**1. Reduction without a symmetry assumption.** The Rayleigh representation
\[
\lambda_2(L)=\min_{x\perp\mathbf1,\,\lVert x\rVert=1}x^{\mathsf T}Lx
\]
shows that \(\lambda_2\) is concave in all edge conductances. Averaging any feasible allocation under the dihedral automorphisms of \(H_n\) preserves its total priced expenditure and cannot reduce \(\lambda_2\). Thus a globally optimal invariant allocation exists. Denote its spoke, rim and private-leaf conductances by \(a,b,c\), so its expenditure is \(n(a+tb+c)\).

**2. All potentially limiting eigenvalues.** Fourier decomposition in the rim index yields for each nonconstant mode \(k=1,\ldots,n-1\) the real symmetric block
\[
M_k=\begin{pmatrix}a+c+d_k b&-c\\-c&c\end{pmatrix},\qquad d_k=2\bigl(1-\cos(2\pi k/n)\bigr).
\]
The constant mode lies in the hub/rim/leaf quotient
\[
R=\begin{pmatrix}na&-na&0\\-a&a+c&-c\\0&-c&c\end{pmatrix},
\]
whose eigenvalues are zero and the two roots of
\[
z^2-\bigl((n+1)a+2c\bigr)z+(2n+1)ac=0.
\]
Since \(d_k\ge\delta_n\) and the blocks increase by positive-semidefinite rank-one changes as \(d_k\) increases, the smallest nonconstant eigenvalue occurs at \(d_k=\delta_n\). Therefore \(\lambda_2\ge1\) holds exactly when both \(M_1-I\) and the restriction of \(R-I\) to the two-dimensional space transverse to the all-ones vector are positive semidefinite.

**3. Exact unit-gap constraints.** The smallest eigenvalue of \(M_1\) is strictly below \(c\), so any unit-gap feasible allocation requires \(c>1\). The lower-right principal minor and determinant of \(M_1-I\) give
\[
a+\delta_n b\ge g(c)=\frac{2c-1}{c-1}.
\]
The radial quadratic is nonnegative at \(1\) with its larger root above \(1\) precisely when
\[
a\ge h_n(c)=\frac{2c-1}{(2n+1)c-(n+1)}.
\]
These two inequalities are also sufficient. For all \(n\ge5\) and \(c>1\), \(0<h_n(c)<g(c)\).

**4. Solve expenditure exactly.** By homogeneity, maximize gap at budget \(B\) by minimizing the expenditure needed to achieve unit gap. For fixed \(c>1\), minimize \(a+tb\) subject to \(a\ge h_n(c)\), \(a+\delta_n b\ge g(c)\), \(b\ge0\). If \(0<\beta<1\), the unique minimum is attained at \(a=h_n(c)\), \(b=(g(c)-h_n(c))/\delta_n>0\), with minimum \(\beta g(c)+(1-\beta)h_n(c)\). If \(\beta>1\), the unique minimum is \(a=g(c),b=0\). If \(\beta=1\), every \(a\in[h_n(c),g(c)]\) together with \(\delta_n b=g(c)-a\) minimizes.

For \(\beta<1\), the remaining one-variable objective
\[
F(c)=c+\beta g(c)+(1-\beta)h_n(c)
\]
is strictly convex because
\[
F''(c)=\frac{2\beta}{(c-1)^3}+\frac{2(1-\beta)(2n+1)}{((2n+1)c-(n+1))^3}>0.
\]
Its derivative runs from negative infinity as \(c\downarrow1\) to \(1\) as \(c\to\infty\), so it has the unique stated minimizer. When \(\beta\ge1\), the remaining objective \(c+g(c)=c+2+1/(c-1)\) has unique minimum at \(c=2\), equal to \(5\); the complete critical-price optimizer interval follows from \(g(2)=3\) and \(h_n(2)=3/(3n+1)\). Finally scale all unit-gap conductances by \(B/C_*\). Scaling proves the reported optimal \(\lambda_2\) and no allocation can exceed it.

**5. Equal-price size transition.** The elementary cosine inequalities yield \(\delta_5>1\), \(\delta_6=1\), and \(\delta_n<1\) for every \(n\ge7\). The expansion \(1-\cos u\sim u^2/2\) yields \(\delta_n\sim4\pi^2/n^2\).

## Verification

Run `python verify.py` with NumPy and SymPy. The script checks the radial characteristic polynomial and normalized inequalities symbolically, constructs the entire \((2n+1)\times(2n+1)\) Laplacian, recomputes its eigenvalues for graph sizes \(5\) through \(18\) at several relative prices, and tests asymmetric feasible competitors plus five explicit points of each critical-price continuum. The included finite calculations supplement, but do not replace, the analytic all-parameter proof.

## Relationship to prior work

Sun, Boyd, Xiao and Diaconis established the general convex fastest-mixing continuous-time Markov-process formulation and its dual [1]. The present contribution is a closed all-price phase diagram on the helm family, including a sharp rim-deletion threshold and its critical continuum, not the general convex formulation.

Jafarizadeh's analytic continuous-time consensus calculations include symmetric stars of length two [2, Sec. 5.3.3]. The rim-deleted branch here is consistent with that established star result; the new assertion concerns exactly when optional, differently priced rim links cease to improve the globally optimal rate, together with the low-price allocation. Results concerning the **discrete-time** second-largest-eigenvalue modulus are not equivalent, since they impose stochastic-row and holding constraints absent here.

## Limitations

The theorem does not classify all non-dihedrally invariant maximizing assignments, even though their best possible value is established. At zero rim price the problem has a different singular limiting interpretation; the theorem assumes strictly positive price. The proof addresses continuous-time Laplacian diffusion, not discrete-time fastest-mixing SLEM. The literature comparison cannot exclude equivalent treatments absent from the inspected sources or indexing.

## References

[1] J. Sun, S. Boyd, L. Xiao, and P. Diaconis, "The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem," *SIAM Review* 48(4), 681–699 (2006), DOI 10.1137/S0036144504443821, first verified public online date 2006-11-02; lawful author-hosted full text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf.

[2] S. Jafarizadeh, "Optimizing the Convergence Rate of the Continuous Time Quantum Consensus," arXiv:1509.05823v1 (2015-09-18), https://arxiv.org/abs/1509.05823.
