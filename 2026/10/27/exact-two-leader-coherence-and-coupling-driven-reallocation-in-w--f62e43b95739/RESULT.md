# Exact two-leader coherence and coupling-driven reallocation in weighted complete split networks

## Finding

Let \(p,q\ge2\) be integers. Form a connected weighted complete split network \(G_{p,q}(a,b)\) with a clique \(C\) of \(p\) vertices and an independent set \(U\) of \(q\) vertices. Every edge internal to \(C\) has conductance \(a>0\); every edge from \(C\) to \(U\) has conductance \(b>0\). Exactly two vertices are selected as noise-free leaders. For a leader set \(S\), put \(J(S)=\operatorname{tr}(L_{FF}^{-1})\), where \(F=V\setminus S\) and \(L_{FF}\) is the grounded weighted Laplacian. Lower \(J\) means lower normalized stationary follower variance.

Write \(t=a/b\). There are exactly three structural types of two-leader sets: CC (both in \(C\)), CU (one in each set), and UU (both in \(U\)). All choices within a type have identical \(J\); the exact values are \(b^{-1}J_{CC},b^{-1}J_{CU},b^{-1}J_{UU}\), where

\[
\begin{aligned}
J_{CC}&=\frac{p-3}{pt+q}+\frac{q-1}{p}+\frac{p+2t+q}{2(pt+q)},\\
J_{CU}&=\frac{p-2}{pt+q}+\frac{q-2}{p}+\frac{p+t+q}{pt+p+q-1},\\
J_{UU}&=\frac{p-1}{pt+q}+\frac{q-3}{p}+\frac{p+q}{2p}.
\end{aligned}
\]

Thus, for every \(p,q\ge2\) and every positive weight ratio, the complete set of optimal pairs consists precisely of the types attaining the minimum of these **three explicit rational functions**, including all ties. No further graph inversion or search over vertex pairs is required.

The peripheral-triad subfamily, \(q=3\), has a stronger *sharp phase theorem* for **every** \(p\ge2\):

1. If \(p=2\), let \(u=(1+\sqrt{33})/4\). CC is the unique optimal type for \(0<t<1/2\); UU is the unique optimal type for \(1/2<t<u\); CU is the unique optimal type for \(t>u\). At either boundary, exactly the neighboring two types tie.
2. If \(p=3\), CC and UU tie for \(0<t<v=(1+\sqrt{10})/3\); all three types tie at \(t=v\); and CU is the unique optimal type for \(t>v\).
3. If \(p\ge4\), let \(s_p=(p-1)/p\) and define

\[
 f_p(t)=2p^2t^2-(p^3+p^2-8p)t+p^3-3p^2-10p+12.
\]

There is exactly one root \(\rho_p>s_p\) of \(f_p\). UU is the unique optimal type for \(0<t<s_p\); CC is the unique optimal type for \(s_p<t<\rho_p\); and CU is the unique optimal type for \(t>\rho_p\). At each boundary only its adjacent types tie. Moreover,

\[
 \rho_p=\frac{p-1}{2}-\frac2p+O(p^{-2})\quad(p\to\infty).
\]

The corresponding numbers of leader pairs of types CC, CU, and UU are, respectively, \(\binom p2\), \(3p\), and \(3\) when \(q=3\). Boundary counts are sums of the tied type counts. The result is about the exact steady-state covariance objective, not transient convergence time or finite leader feedback gains.

## Assumptions and scope

All graphs are finite, undirected, and have the conductances just specified. The two leaders track a fixed reference without noise. Followers obey \(d x_F=-L_{FF}x_F\,dt+\sigma\,dW_F\), after subtracting that reference, where the independent Wiener inputs have equal intensity \(\sigma>0\). Since the graph is connected and at least one vertex is grounded, \(L_{FF}\) is positive definite. Its stationary covariance is \(\Sigma=(\sigma^2/2)L_{FF}^{-1}\). Thus minimizing total variance \(\operatorname{tr}\Sigma\) is equivalent to minimizing \(J(S)\). The equal-peripheral-edge model permits arbitrary positive \(a,b\); it does not address heterogeneous individual edge weights, directed graphs, or noise-corrupted leaders.

## Proof

Normalize \(b=1\), as a common conductance multiplier divides every inverse-trace objective by \(b\). Put \(B=pt+q\). If \(x\) clique vertices and \(y\) independent vertices remain followers, the grounded Laplacian is

\[
M_{x,y}=\begin{pmatrix}BI_x-t\mathbf1_x\mathbf1_x^{\mathsf T}&-\mathbf1_x\mathbf1_y^{\mathsf T}\\-\mathbf1_y\mathbf1_x^{\mathsf T}&pI_y\end{pmatrix}.
\]

The clique-contrast subspace has eigenvalue \(B\), and the independent-contrast subspace has eigenvalue \(p\). On vectors constant within each remaining type, the matrix is represented by

\[
H_{x,y}=\begin{pmatrix}B-tx&-y\\-x&p\end{pmatrix}.
\]

For \(x,y>0\), the trace of the inverse is therefore

\[
\operatorname{tr}(M_{x,y}^{-1})=\frac{x-1}{B}+\frac{y-1}{p}+\frac{B-tx+p}{p(B-tx)-xy}.
\]

For CC, CU, and UU respectively, \((x,y)=(p-2,q),(p-1,q-1),(p,q-2)\). Their reduced determinants are \(2B\), \(pt+p+q-1\), and \(2p\). Substitution gives exactly the three asserted rational functions. In boundary cases \(x=0\) or \(y=0\), direct inversion of the surviving block gives the same simplified expressions; this can also be seen by canceling the spurious contrast and quotient contributions. Every two-element leader set belongs to one of these three types under the automorphism group \(\mathfrak S_p\times\mathfrak S_q\). This proves the all-parameter classification by minimum.

For the sharper \(q=3\) statement, all denominators below are positive. Directly subtracting the three rational functions gives

\[
J_{CC}-J_{UU}=-\frac{(p-3)(pt-p+1)}{2p(pt+3)},
\]

\[
J_{UU}-J_{CU}=\frac{(p-1)g_p(t)}{2p(pt+3)(pt+p+2)},\quad
 g_p(t)=p^2t^2-p^2t+pt-p-6,
\]

and

\[
J_{CC}-J_{CU}=\frac{f_p(t)}{2p(pt+3)(pt+p+2)}.
\]

If \(p\ge4\), the first difference changes sign exactly at \(s_p\): UU beats CC below it, and CC beats UU above it. On \([0,s_p]\), the convex quadratic \(g_p\) has equal, negative endpoint values \(g_p(0)=g_p(s_p)=-(p+6)\). Convexity gives \(g_p(t)\le-(p+6)<0\) throughout that interval, so UU also beats CU there. At \(s_p\) the value \(f_p(s_p)=-(p-1)(p+6)<0\). Because \(f_p\) has positive leading coefficient, it has exactly one real root to the right of \(s_p\): existence follows from its positive limit at infinity, and uniqueness follows because \(f_p(s_p)<0\) lies strictly between its two distinct real roots. Hence CC beats CU until \(\rho_p\), and CU beats CC afterward. As CC already beats UU for \(t>s_p\), the three successive optimal types and all boundary ties follow.

When \(p=3\), \(J_{CC}=J_{UU}\) identically and \(f_3(t)=6(3t^2-2t-3)\), whose sole positive root is \(v\). When \(p=2\), exact simplifications are

\[
\begin{aligned}
J_{CC}-J_{UU}&=\frac{2t-1}{4(2t+3)},\\
J_{CC}-J_{CU}&=\frac{t-1}{2(t+2)},\\
J_{UU}-J_{CU}&=\frac{2t^2-t-4}{4(t+2)(2t+3)}.
\end{aligned}
\]

Their signs give the stated phases and strict boundary comparisons. Finally, solving the larger root of \(f_p\) by the quadratic formula and expanding the square root gives \(\rho_p=(p-1)/2-2/p+O(p^{-2})\); the exact radicand equals \(p^2(p^4-6p^3+9p^2+64p-32)\). No numerical extrapolation is used.

## Verification

Run `python verify.py` with SymPy installed. It checks four exact symbolic identities, compares the rational formulas with 420 independent grounded-matrix inverses over rational conductance ratios and small network sizes, and checks 17 additional exact phase-threshold identities. Expected output:

`VERIFY_OK 4 symbolic comparison identities; 420 exact direct grounded inverse comparisons; 17 exact threshold checks`

The proof above supplies the infinite-parameter argument; these finite evaluations are corroborative and cannot certify the universal quantifiers on their own.

## Relationship to prior work

Fitch and Leonard [1] derive joint-centrality criteria for noise-free leaders on general weighted networks and give exact optimal locations for paths and cycles. The present specialization solves the weighted complete-split all-pair objective and derives a coupling-dependent three-phase boundary that is not stated in their graph-specific results. Patterson, Yi and Zhang [2] establish general effective-resistance expressions and solve several classes including paths, cycles and trees, but not this weighted split family. Clark and collaborators [3] address a related leader-selection task with a different transient convergence-error criterion, rather than this stationary inverse-grounded-Laplacian objective. The phase inequalities and tie classifications here require comparisons beyond merely applying a generic joint-centrality formula.

## Limitations

Only two noise-free leaders, homogeneous conductance within each edge class, and independent equal-intensity follower disturbances are treated. For arbitrary peripheral size \(q\), the rational minimum classifies exact optimal leader types but a simplified list of contiguous coupling intervals is only proved for \(q=3\). The result does not assert novelty against inaccessible specialized literature or any independent certification; the mathematical argument and code are independently inspectable.

## References

[1] K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (initial public posting 2014-07-07), https://arxiv.org/abs/1407.1569.

[2] S. Patterson, Y. Yi, and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873 (initial public posting 2017-08-23), https://arxiv.org/abs/1708.06873.

[3] A. Clark, B. Alomair, L. Bushnell, and R. Poovendran, *Minimizing Convergence Error in Multi-Agent Systems via Leader Selection: A Supermodular Optimization Approach*, arXiv:1306.4949 (initial public posting 2013-06-20), https://arxiv.org/abs/1306.4949.
