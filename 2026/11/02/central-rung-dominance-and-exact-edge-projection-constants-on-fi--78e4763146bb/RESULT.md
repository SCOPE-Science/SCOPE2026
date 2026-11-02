# Central-rung dominance and exact edge-projection constants on finite ladders

## Finding

For every integer \(n\ge 2\), let \(G_n=P_n\square K_2\) be the unit-conductance ladder with \(n\) rungs. Give its \(3n-2\) undirected edges arbitrary orientations, let \(B\) be the edge-by-vertex incidence matrix, and set \(L=B^{\mathsf T}B\). The orthogonal edge-gradient projection is
\[
\Pi_n=BL^+B^{\mathsf T}:\mathbb R^{3n-2}\longrightarrow\mathbb R^{3n-2}.
\]
Its induced \(\ell^\infty\)-operator norm \(M_n=\|\Pi_n\|_{\infty\to\infty}\) is given by the following **exact rational recurrences**, which involve only integer arithmetic.

Define four integer sequences by
\[
\begin{aligned}
&a_0=1,\quad a_1=2,\qquad b_0=0,\quad b_1=1,\\
&c_0=1,\quad c_1=3,\qquad s_0=1,\quad s_1=5,
\end{aligned}
\]
where each sequence \(t\) satisfies \(t_{m+2}=4t_{m+1}-t_m\). For \(m\ge1\),
\[
\boxed{M_{2m}=1+\frac{(2a_m-1)(a_m-1)}{3a_mb_m},\qquad
M_{2m+1}=1+\frac{2(c_m-1)}{s_m}.}
\]
For \(n\ge3\), **the maximizing rows are exactly the central rung rows**: one rung when \(n\) is odd, two when \(n\) is even. When \(n=2\), all four edge rows tie at \(M_2=3/2\). In every case, the sign vector of any maximizing row attains the induced norm.

The sharp amplification threshold is \(M_n>2\) **if and only if \(n\ge5\)**. Both parity subsequences increase strictly and stay below the sharp, unattained finite-ladder envelope
\[
\boxed{\sup_{n\ge2}M_n=1+\frac2{\sqrt3}}.
\]
More precisely, with \(\rho=2-\sqrt3\),
\[
M_n=1+\frac2{\sqrt3}-
\begin{cases}
2\sqrt2\,\rho^{n/2}+O(\rho^n),&n\text{ odd},\\
2\sqrt3\,\rho^{n/2}+O(\rho^n),&n\text{ even}.
\end{cases}
\]
The first values are \(M_2=3/2\), \(M_3=9/5\), \(M_4=27/14\), \(M_5=39/19\), and \(M_6=163/78\).

## Assumptions and scope

Vertices are \(t_1,\ldots,t_n\) on the top rail and \(b_1,\ldots,b_n\) on the bottom rail. Edges are the \(n\) rungs \(t_jb_j\) and the two sets of \(n-1\) consecutive rail edges. Every edge has conductance one. All spaces and operators are real. Orientation choices conjugate \(\Pi_n\) by a diagonal sign matrix and hence leave the induced maximum norm unchanged. The result is about the symmetric edge-space projection, not a vertex Laplacian inverse norm or a different current normalization.

Write \(H\) for the path Laplacian on \(\{1,\ldots,n\}\), with endpoint diagonal \(1\), interior diagonal \(2\), and neighboring entries \(-1\), and define \(G=(H+2I)^{-1}\). This positive Green matrix is only an intermediate object; the theorem concerns the full edge projection, including all rail rows and their comparison with the rung rows.

## Proof

**Step 1: Green matrix with both boundaries.** Put \(\gamma=\operatorname{arcosh}2\) and
\[
U_j=\cosh((j-\tfrac12)\gamma),\quad
V_j=\cosh((n+\tfrac12-j)\gamma),\quad
W=\sinh\gamma\,\sinh(n\gamma).
\]
The functions \(U\) and \(V\) solve the interior difference equation \(4v_j-v_{j-1}-v_{j+1}=0\), respectively satisfying the left and right endpoint equations. Their discrete Wronskian is \(W>0\). Thus the unique solution of \((H+2I)G=I\) is
\[
G_{ij}=\frac{U_{\min(i,j)}V_{\max(i,j)}}{W}.
\]
In particular, a column of \(G\) is positive, strictly increasing before its diagonal and strictly decreasing afterwards. For consecutive source positions \(k,k+1\), the difference \(d_j=G_{jk}-G_{j,k+1}\) is strictly positive and increasing for \(j\le k\), and strictly negative and increasing for \(j\ge k+1\). Also \(\sum_jG_{jk}=1/2\) and \(\sum_jd_j=0\), directly from summing the Green equations.

**Step 2: Every rung row.** Inject unit current from \(t_k\) to \(b_k\). Reflection antisymmetry makes the upper and lower potential arrays \(u\) and \(-u\), where \(u=Ge_k\). The rung-edge current magnitudes sum to \(2\sum_j u_j=1\). The two rail-current absolute sums together are
\(2\sum_{j=1}^{n-1}|u_j-u_{j+1}|=2(2u_k-u_1-u_n)\), because the Green column is unimodal. Consequently the **exact absolute row sum** of rung \(k\) is
\[
R_k=1+2(2G_{kk}-G_{1k}-G_{nk}).\tag{1}
\]

**Step 3: Every rail row is strictly below two.** Inject unit current from \(t_k\) to \(t_{k+1}\), where \(1\le k<n\). Write top and bottom potentials as \(s+v\) and \(s-v\). Then
\[
Hs=\tfrac12(e_k-e_{k+1}),\qquad
(H+2I)v=\tfrac12(e_k-e_{k+1}),\qquad v=d/2.
\]
The symmetric potential \(s\) is constant on either side of the cut and has jump \(1/2\) at \(k\). The signs and monotonicities in Step 1 show that at \(j\ne k\) the two rail-current absolute values sum to \(|d_j-d_{j+1}|\); at \(j=k\) their sum is exactly \(1\). For the latter, the positivity of \(d\) to the left and its negativity to the right give \(0<d_k-d_{k+1}<1\): indeed, summing \((H+2I)d=e_k-e_{k+1}\) through position \(k\) gives
\[
2\sum_{j\le k}d_j+(d_k-d_{k+1})=1.
\]
That identity also makes the sum of the rung-current magnitudes equal to \(1-(d_k-d_{k+1})\). The remaining rail-current magnitudes total \(d_k-d_1+d_n-d_{k+1}\). Hence the absolute row sum of either rail edge at position \(k\) is
\[
T_k=2-d_1+d_n
=2-(G_{1k}-G_{1,k+1})+(G_{nk}-G_{n,k+1})<2.\tag{2}
\]
This strict inequality holds for every \(n\ge2\) and every rail position.

**Step 4: Unique central rung maximizers.** Let \(A=\cosh(\gamma/2)=\sqrt{3/2}\), \(Y=\cosh(n\gamma/2)\), and \(z_k=\cosh((k-(n+1)/2)\gamma)\). The Green expression gives
\[
2G_{kk}-G_{1k}-G_{nk}
=\frac{\cosh(n\gamma)+2z_k^2-1-2AYz_k}{W}.\tag{3}
\]
For \(n>2\) and \(1\le k\le n\), one has \(1\le z_k\le\cosh((n-1)\gamma/2)\) and
\[
AY>2\cosh((n-1)\gamma/2),
\]
since \(\tanh(n\gamma/2)>\tanh\gamma=\sqrt3/2\) and \(\tanh(\gamma/2)=1/\sqrt3\). Thus the numerator in (3), viewed as a function of \(z\), has derivative \(4z-2AY<0\) over the entire allowed range. It is therefore maximized precisely when \(|k-(n+1)/2|\) is smallest. For \(n=2\) both rungs tie.

At these central positions, (1)–(3) simplify to
\[
R_{\mathrm{center}}=
\begin{cases}
\displaystyle 1+\frac{2(Y-A)}{\sqrt3\sinh(n\gamma/2)},&n\text{ odd},\\[6pt]
\displaystyle 1+\frac{(2Y-1)(Y-1)}{\sqrt3\,Y\sinh(n\gamma/2)},&n\text{ even}.
\end{cases}\tag{4}
\]
The odd expression is strictly increasing with \(Y\), because the derivative of \((Y-A)/\sqrt{Y^2-1}\) is \((AY-1)/(Y^2-1)^{3/2}>0\). The even expression is \(1+\frac2{\sqrt3}(1-1/(2Y))\sqrt{(Y-1)/(Y+1)}\), likewise strictly increasing with \(Y\). Both are strictly less than \(1+2/\sqrt3\). Moreover, \(R_{\mathrm{center}}=39/19>2\) at \(n=5\) and \(R_{\mathrm{center}}=163/78>2\) at \(n=6\), so every rung-central maximum for \(n\ge5\) strictly exceeds every rail row by (2). The remaining cases follow directly: at \(n=2\), all four rows equal \(3/2\); at \(n=3\), the central rung gives \(9/5\), while both rail rows give \(5/3\); at \(n=4\), the two central rungs give \(27/14\), while the largest rail row gives \(13/7\). This proves all maximizer statements.

**Step 5: Integer formulas and sharp asymptotics.** For \(n=2m\), \(\cosh(m\gamma)=a_m\), \(\sinh(m\gamma)=\sqrt3\,b_m\). For \(n=2m+1\), \(\cosh((m+\tfrac12)\gamma)=A c_m\), \(\sinh((m+\tfrac12)\gamma)=s_m/\sqrt2\). Each sequence obeys the stated recurrence because \(2\cosh\gamma=4\), with the displayed initial data. Substitution into (4) gives the rational formulas in the finding. Finally \(Y\sim\tfrac12e^{n\gamma/2}\). Expanding (4) at large \(Y\), and using \(e^{-\gamma}=2-\sqrt3\), yields the two parity-dependent exponential defects and the sharp limiting constant.

Since \(\Pi_n\) is a finite real matrix, its \(\ell^\infty\) norm is its largest absolute row sum. For any maximizing row, the input vector taking the sign of each entry in that row has maximum norm one and makes the output at that row equal the row sum. This proves attainment without any nonconstructive limiting input.

## Verification

The standalone `verify_ladder.py` uses only the Python standard library. It constructs the **grounded full-graph Laplacian independently** of the Green-function proof, inverts it over rational numbers, and forms every electrical transfer-current row for \(2\le n\le14\). It compares each absolute row sum against (1) or (2), checks the exact rational recurrence for the global maximum and the complete maximizing-edge classification, and checks symmetry and idempotence of the computed edge projection for \(2\le n\le9\). It additionally checks (4) numerically for \(2\le n\le30\). The execution returned `VERIFY_OK exact and hyperbolic checks: 4448`. These finite tests check implementation and algebra, not the all-\(n\) theorem, which is proved above.

## Relationship to prior work

Kelner and Maymounkov (arXiv:0909.2859, first posted 15 September 2009) formulate the electrical transfer projection \(\Pi\) and relate its induced norm to electrical routing in their Theorem 3.1. Their graph-general bounds do not provide the present exact finite-ladder constant or row-extremizer classification. Tan (2016, DOI below) derives current and resistance expressions for rectangular circuits with boundary conditions; currents and effective resistances alone do not give the absolute row sums and the sharp row-class comparison proved here.

The technical note *Exact finite-volume rung kernel and boundary-bulk split for weighted ladder spanning trees* (2026, identifier `647fc3f7ee8c`) explicitly obtains the rung-to-rung Green/transfer block on weighted ladders; that known kernel is **not** claimed as new here. Its theorem determines rung inclusion probabilities and their boundary/bulk limits, not the all-edge \(\ell^\infty\) norm, sharp rail-versus-rung competition, central-rung extremizers, rational recurrence, or parity-dependent convergence coefficient. Standard transfer-current identities support the derivation but do not by themselves evaluate these absolute maxima.

## Limitations

All conductances are exactly one, the network is a finite two-rail path ladder, and the norm is that of the real symmetric edge-gradient orthogonal projection. The theorem does not classify weighted ladders, ladders with periodic horizontal boundary conditions, wider strips, or the distinct \(\ell^1\)-to-\(\ell^1\) norm of the vertex pseudoinverse. The originality claim is limited to the complete sharp norm-and-extremizer result; related transfer kernels and resistance formulas were already known. Further specialized circuit literature could contain equivalent formulas not found in the inspected sources.

## References

1. J. Kelner and P. Maymounkov, *Electric routing and concurrent flow cutting*, arXiv:0909.2859 (v1, 15 September 2009), https://arxiv.org/abs/0909.2859.
2. Z.-Z. Tan, *Two-point resistance of an m × n resistor network with an arbitrary boundary and its application in RLC network*, Chinese Physics B 25 (2016), 050504, DOI: 10.1088/1674-1056/25/5/050504.
3. *Exact finite-volume rung kernel and boundary-bulk split for weighted ladder spanning trees* (2026), publicly available result identified by `647fc3f7ee8c`.
4. R. Burton and R. Pemantle, *Local characteristics, entropy and limit theorems for spanning trees and domino tilings via transfer-impedances*, Annals of Probability 21 (1993), 1329–1371, DOI: 10.1214/aop/1176989121.
