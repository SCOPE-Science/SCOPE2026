# A sharp rim-edge screening transition for fastest mixing on a wheel with a hub leaf

## Finding
For each integer \(m\ge3\), attach one leaf to the hub of the wheel with rim cycle \(C_m\). Distribute a total conductance budget \(B>0\) among the spokes, rim edges, and leaf edge, allowing zero conductances. Among **all**, not necessarily symmetric, conductance assignments, the largest algebraic connectivity of the resulting weighted Laplacian is \(B/D_m\), where
\[
\delta_m=4\sin^2(\pi/m),\qquad k_m=1-\delta_m^{-1},
\]
\[
D_m=\begin{cases}
m+1-\dfrac{(m\sqrt{k_m}-1)^2}{m+2},&m=3,4,5,\\
m+1,&m\ge6.
\end{cases}
\]
The optimal invariant weights, normalized to produce algebraic connectivity one, are constant on each edge class and equal to
\[
(a_m,b_m,c_m)=
\begin{cases}
\left(\dfrac{2+k_m^{-1/2}}{m+2},\dfrac{1-a_m}{\delta_m},\dfrac{(m+1)a_m-1}{(m+2)a_m-2}\right),&3\le m\le5,\\
(1,0,1),&m\ge6.
\end{cases}
\]
Here \(a_m\) is the weight on each spoke, \(b_m\) on each rim edge, and \(c_m\) on the hub–leaf edge; the actual optimal weights under budget \(B\) are \(B(a_m,b_m,c_m)/D_m\). In the first branch \(k_m>m^{-2}\) and all three weights are positive. For every \(m\ge6\), **every** optimal conductance assignment, including asymmetric ones, has zero weight on **every** rim edge. Thus the ability of the rim to improve the optimal spectral gap disappears sharply between five and six rim vertices.

## Assumptions and scope
The underlying simple graph has vertex set \(\{o,\ell,v_1,\ldots,v_m\}\) and undirected edges \(ov_j\), \(v_jv_{j+1}\) (indices modulo \(m\)), and \(o\ell\); each edge has independently assignable nonnegative conductance. The Laplacian is \(L=\sum_e w_e(e_u-e_v)(e_u-e_v)^\mathsf T\), so its algebraic connectivity is the second-smallest eigenvalue \(\lambda_2(L)\). The objective is to maximize \(\lambda_2(L)\) subject to \(\sum_e w_e=B\), with no further lower or upper edge bounds. All statements hold for every integer \(m\ge3\) and real \(B>0\). The leaf attaches to the hub, not to a rim vertex. Disconnected weighted supports have zero spectral gap and cannot be optimal.

## Proof
**1. Symmetry reduction without assuming symmetric competitors.** For every mean-zero unit vector \(x\), the Rayleigh quotient \(x^\mathsf TL(w)x\) depends linearly on \(w\). Consequently \(w\mapsto\lambda_2(L(w))\), the minimum of these linear forms, is concave. Averaging any feasible weights under the dihedral automorphism group of the rim cannot decrease \(\lambda_2\) and preserves the budget. A maximizing allocation can therefore be chosen with one spoke weight \(a\), one rim weight \(b\), and one hub–leaf weight \(c\).

**2. Spectral decomposition.** On rim vectors of zero sum, with hub and leaf coordinates zero, the eigenvalues are \(a+4b\sin^2(\pi j/m)\), \(1\le j<m\). Their minimum is \(a+\delta_m b\). The orthogonal complementary space of vectors constant on the rim has one zero eigenvalue and two other eigenvalues \(\lambda_-\le\lambda_+\) solving
\[
\lambda^2-\bigl((m+1)a+2c\bigr)\lambda+(m+2)ac=0.
\]
Hence \(\lambda_2=\min\{a+\delta_m b,\lambda_-(a,c)\}\).

**3. Minimum budget to achieve unit gap.** Homogeneity reduces maximizing \(\lambda_2\) for budget \(B\) to minimizing the cost \(m(a+b)+c\) subject to \(\lambda_2\ge1\). The rim-mode condition is \(b\ge\max\{0,(1-a)/\delta_m\}\). The nonzero quotient-block eigenvalue condition requires \(a>2/(m+2)\) and
\[
c\ge f_m(a):=\frac{(m+1)a-1}{(m+2)a-2}.
\]
Indeed, as \(c\to\infty\), the smaller quotient-block eigenvalue increases towards \((m+2)a/2\). At \(c=f_m(a)\), the characteristic polynomial vanishes at \(1\), and its other root exceeds \(1\): when \(a\le1\), \(f_m(a)\ge1\), and when \(a>1\), the trace \((m+1)a+2f_m(a)\) exceeds \(2\). The eigenvalue is nondecreasing under increasing \(c\), so these conditions are also sufficient.

The exact minimum normalized budget is therefore
\[
\min_{a>2/(m+2)} S_m(a),\qquad
S_m(a)=ma+\frac{(m+1)a-1}{(m+2)a-2}+\frac{m}{\delta_m}\max\{0,1-a\}.
\]

**4. Unique scalar minimum and the transition.** The derivative of the rational term is \(-m/((m+2)a-2)^2\), and its second derivative is \(2m(m+2)/((m+2)a-2)^3>0\). For \(a\ge1\), the objective is strictly increasing because its derivative is \(m-m/((m+2)a-2)^2>0\). On \(2/(m+2)<a<1\),
\[
S_m'(a)=m\bigl(1-\delta_m^{-1}\bigr)-\frac{m}{((m+2)a-2)^2},
\]
which increases strictly from \(-\infty\). If \(m\ge6\), then \(\delta_m\le1\), and it remains negative through \(a=1\). The unique minimizer is \(a=1\), \(b=0\), \(c=f_m(1)=1\), of cost \(D_m=m+1\).

For \(m=3,4,5\), \(\delta_m>1\) and \(k_m=1-1/\delta_m>1/m^2\), so \(S_m'(1^-)>0\). There is exactly one critical point in the left interval,
\[
a_m=\frac{2+k_m^{-1/2}}{m+2}<1,
\]
which is the unique global minimizer. Taking \(b_m=(1-a_m)/\delta_m\) and \(c_m=f_m(a_m)\) gives the displayed positive weights. Direct substitution and \(k_m=1-\delta_m^{-1}\) simplify \(S_m(a_m)\) to \(D_m\).

**5. Return to unrestricted allocations and rigidity.** Concavity in step 1 proves that these symmetric optima are global over all edge weights. For \(m\ge6\), averaging any globally optimal weight assignment gives an invariant optimum. The unique invariant optimum has mean rim conductance zero. Every rim conductance of the original assignment was nonnegative, so each of those conductances must be zero as well. This proves the all-optimizer rim-screening statement. No assertion of uniqueness of all individual spoke/leaf weights is needed.

## Verification
A standalone standard-library script `verify.py` assembles weighted graph Laplacians directly, diagonalizes them independently of the derived reduced formula, compares the proposed optimal unit-gap normalization and selected random feasible competitors, and checks the explicit low-order identities. Run `python3 verify.py` from the directory containing the package. It reports 468 finite numerical comparisons, including sizes \(3\le m\le20\). These checks are supplementary: the proof above, not numerical sampling, establishes the theorem for all \(m\ge3\) and all real \(B>0\).

## Relationship to prior work
Sun, Boyd, Xiao, and Diaconis (2006) established the general continuous-time fastest-mixing/spectral-gap optimization formulation and its duality. Their general semidefinite framework does not give the above wheel-with-hub-leaf closed-form optimizer or the sharp rim-screening transition. Boyd, Diaconis, Parrilo, and Xiao (2007/2009) treated symmetry and the discrete-time fastest-mixing problem, including the unaugmented wheel, which differs in objective and graph structure. Berman and Förster (2005) studied algebraic connectivity under one pendant edge with changing weight, but not allocation across all edges under a fixed total budget. Thus the result is an explicit special-family solution, not a claim to invent spectral-gap optimization.

## Limitations
The result concerns one pendant leaf attached at the hub, nonnegative freely chosen conductances, and algebraic connectivity under a linear total-weight budget. It does not characterize all unrestricted optimal spoke weights for \(m\ge6\), impose strictly positive weights on every present edge, or treat a leaf attached to a rim vertex. Literature searches and source comparisons cannot establish universal priority; specialized prior coverage remains possible. The finite verification cases do not certify the infinite family by themselves.

## References
1. J. Sun, S. Boyd, L. Xiao, and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review **48** (2006), 681–699. https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf
2. S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955 (2007); SIAM J. Optimization **20** (2009), 792–819. https://arxiv.org/abs/0709.0955
3. A. Berman and K.-H. Förster, *Algebraic Connectivity of Trees with a Pendant Edge of Infinite Weight*, Electronic Journal of Linear Algebra **13** (2005). https://emis.de/ft/15363
