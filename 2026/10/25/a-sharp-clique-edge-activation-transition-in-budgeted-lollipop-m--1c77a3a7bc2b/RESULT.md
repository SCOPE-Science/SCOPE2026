# A sharp clique-edge activation transition in budgeted lollipop mixing

## Finding

**Theorem (exact continuous-time lollipop optimum).** Let \(k\ge2\) be an integer and let \(G_k\) have vertices \(u_1,\ldots,u_k,h,v,z\). Its edges are all pairs in the clique \(\{u_1,\ldots,u_k,h\}\), the bridge \(hv\), and the terminal edge \(vz\). Give every edge a nonnegative symmetric continuous-time rate, with total rate budget \(B>0\). For the weighted Laplacian \(L\), write \(\lambda_2(L)\) for the second-smallest eigenvalue. Put

\[
 d_k=\begin{cases}1,&2\le k\le3,\\[2pt]\sqrt{\frac{k+1}{2k}},&k\ge4,\end{cases}\qquad
 V_k=\frac{k(8+6d_k)+6+k^2(1-d_k^2)}{k+3}.
\]

Then the exact optimum over all rates is \(\max\lambda_2(L)=B/V_k\). **The maximizing rate allocation is unique.** In units of \(B/V_k\), every spoke \(hu_i\) has rate
\[
 a_k=\frac{3(d_k+1)}{(k+3)d_k},
\]
 every clique edge \(u_i u_j\), \(i\ne j\), has rate
\[
 c_k=\begin{cases}0,&2\le k\le3,\\[2pt]\frac{kd_k-3}{k(k+3)d_k},&k\ge4,\end{cases}
\]
 the bridge \(hv\) has rate \(b_k=[2kd_k+3(k+1)]/(k+3)\), and the terminal edge \(vz\) has rate \(e_k=[kd_k+2k+3]/(k+3)\). Consequently **every** optimum discards all \(\binom{k}{2}\) edges between peripheral clique vertices when \(k=2,3\), whereas **every** such edge receives strictly positive rate for all \(k\ge4\). The optimal spectral-gap multiplicity is one for \(k=2\) and exactly \(k\) for every \(k\ge3\).

## Assumptions and scope

The vertices have uniform stationary mass and edges have unrestricted nonnegative transition *rates*, not discrete-time probabilities or vertexwise rate caps. Rates are normalized by \(\sum_{\{i,j\}\in E(G_k)}w_{ij}=B\). The underlying allowed graph is fixed, although an allowed edge may optimally receive zero weight. Only integers \(k\ge2\) and budgets \(B>0\) are claimed. The construction is sometimes called a clique-with-two-vertex-tail or kite/lollipop graph; terminology alone does not specify the rate optimization.

## Proof

**1. Universal geometric upper bound.** It suffices by homogeneity to minimize \(\sum w_{ij}\) subject to \(\lambda_2(L)\ge1\). For vectors \(X_i\) in an arbitrary Euclidean space, centered so that \(\sum_i X_i=0\), suppose all edge distances obey \(\|X_i-X_j\|^2\le1\). Then the Rayleigh inequality \(L\succeq I-\mathbf1\mathbf1^\top/(k+3)\) gives
\[
 \sum_i\|X_i\|^2\le\sum_{\{i,j\}}w_{ij}\|X_i-X_j\|^2\le\sum_{\{i,j\}}w_{ij}.
\]
 Let \(P=k^{-1}\sum_{i=1}^kX_{u_i}\), \(t=k^{-1}\sum_i\|X_{u_i}-P\|^2\), and \(N=k+3\). The identities
\[
 \sum_{i<j}\|X_{u_i}-X_{u_j}\|^2=k^2t,
 \quad \frac1k\sum_i\|X_{u_i}-X_h\|^2=t+\|P-X_h\|^2
\]
 imply \(0\le t\le(k-1)/(2k)\) and \(\|P-X_h\|\le\sqrt{1-t}=:d\). From the two remaining length bounds, \(\|P-X_v\|\le d+1\), \(\|P-X_z\|\le d+2\), \(\|X_h-X_z\|\le2\). Applying the weighted variance identity to masses \(k,1,1,1\), with the peripheral internal scatter \(kt\), yields
\[
 \begin{split}
 \sum_i\|X_i\|^2
 &=kt+\frac{k\bigl(\|P-X_h\|^2+\|P-X_v\|^2+\|P-X_z\|^2\bigr)+\|X_h-X_v\|^2+\|X_h-X_z\|^2+\|X_v-X_z\|^2}{N}\\
 &\le \frac{k\bigl(8+6\sqrt{1-t}\bigr)+6+k^2t}{N}=:F_k(t).
 \end{split}
\]
 Its derivative is \(F_k'(t)=k(k-3/\sqrt{1-t})/N\). For \(k\le3\) it is nonpositive throughout the permitted interval and the maximum is at \(t=0\); for \(k\ge4\) it is positive throughout since \(k\sqrt{(k+1)/(2k)}>3\), and the maximum is at \(t=(k-1)/(2k)\). Hence every feasible rate allocation with \(\lambda_2\ge1\) has budget at least \(V_k\).

**2. An attainable embedding.** For \(k\le3\), take all peripheral vectors equal to \(0\) on a line, with \(X_h=d_k\), \(X_v=d_k+1\), \(X_z=d_k+2\). For \(k\ge4\), in an orthogonal coordinate space let \(X_{u_i}=(e_i-k^{-1}\mathbf1)/\sqrt2\), \(i=1,\ldots,k\), and place \(X_h,X_v,X_z\) at \(d_k,d_k+1,d_k+2\) times a unit vector orthogonal to their span. Center the whole configuration. All allowed edge lengths are \(1\) except that peripheral-to-peripheral lengths are \(0\) for \(k\le3\). Its variance is exactly \(V_k\), so the bound is geometrically sharp.

**3. An explicit optimal Laplacian (self-contained positive-semidefinite certificate).** Write \(d=d_k\), \(N=k+3\), and prescribe the four rates \(a=a_k,b=b_k,c=c_k,e=e_k\) in the theorem, at spectral-gap-one normalization. The rates are nonnegative: when \(k\ge4\), \(kd=\sqrt{k(k+1)/2}>3\). Also \(a+kc=1\) for \(k\ge4\), and \(a\ge1\) for \(k=2,3\).

For an arbitrary real vertex function, decompose its peripheral values into their mean \(P\) and zero-sum fluctuations. The associated Laplacian energy is
\[
 (a+kc)\sum_{i=1}^k(x_{u_i}-P)^2+ka(P-x_h)^2+b(x_h-x_v)^2+e(x_v-x_z)^2.
\]
 Its centered squared norm is \(\sum_i(x_{u_i}-P)^2\) plus the weighted variance of the four points \((P,x_h,x_v,x_z)\) with masses \((k,1,1,1)\). In edge-increment coordinates \(q_1=x_h-P\), \(q_2=x_v-x_h\), \(q_3=x_z-x_v\), the difference between axial energy and axial squared norm is \(q^\top Mq\), where
\[
 M=\operatorname{diag}(ka,b,e)-\frac1N
 \begin{pmatrix}3k&2k&k\\2k&2k+2&k+1\\k&k+1&k+2\end{pmatrix}.
\]
 Direct substitution gives \(M(d,1,1)^\top=0\), while its three off-diagonal entries are respectively \(-2k/N,-k/N,-(k+1)/N\). For every real triple \(q\), the exact ground-state identity
\[
 q^\top Mq=\frac{2kd}{N}\left(\frac{q_1}{d}-q_2\right)^2+\frac{kd}{N}\left(\frac{q_1}{d}-q_3\right)^2+\frac{k+1}{N}(q_2-q_3)^2\ge0
\]
 proves that the quotient part has eigenvalues at least \(1\) off the constants, with equality precisely for increments proportional to \((d,1,1)\). The fluctuation part has coefficient \(a+kc\ge1\); therefore \(L\succeq I-\mathbf1\mathbf1^\top/N\). Equality is attained by the nonconstant axial vector, so \(\lambda_2(L)=1\). Its multiplicity is \(1\) if \(k=2\), and \(1+(k-1)=k\) if \(k\ge3\).

Finally, either evaluate the displayed rates or use the embedding's edge-tightness and the eigenvector identities to obtain \(ka+\binom{k}{2}c+b+e=V_k\). Thus the lower bound on the budget is attained; scaling all rates by \(B/V_k\) proves the optimum for every \(B>0\).

**4. Uniqueness.** Let another budget-\(V_k\) allocation satisfy \(\lambda_2\ge1\). Apply the inequality in step 1 to the specific maximizing embedding in step 2. Equality of its endpoints forces every embedding coordinate, after centering, to be a unit-eigenvalue vector for that allocation; it also forces zero weight on any edge shorter than one. For \(k\le3\) the peripheral-clique edges have distance zero and hence rate zero. The axial eigenvector's equations at each peripheral vertex, at \(h\), at \(v\), and at \(z\) separately force precisely \(a,b,e\).

For \(k\ge4\), the peripheral simplex-coordinate vectors span the entire zero-sum peripheral subspace. Their eigenvector equations at \(h\) require all \(h-u_i\) rates to coincide; their equations on peripheral vertices require the restriction of the peripheral Laplacian block to the zero-sum space to be the identity, which forces every \(u_i-u_j\) rate to equal \((1-a)/k\). The axial eigenvector then fixes \(a,b,e\), yielding \(c=(1-a)/k\) exactly. No other allocation is optimal. Scaling preserves uniqueness.

## Verification

The embedded standalone `verify.py` constructs the full weighted Laplacian, recomputes the total budget, evaluates its eigenvalues, and checks the claimed gap and multiplicity for each integer \(2\le k\le60\). All 59 tested values passed at numerical tolerance \(10^{-11}\). This is a finite reproducibility test, not the proof of the all-parameter statements. The proof is the geometric bound and the explicit semidefinite identity above.

## Relationship to prior work

Sun, Boyd, Xiao, and Diaconis (2006) formulate the continuous-time fastest-mixing Markov process as rate-budget spectral-gap optimization and its maximum-variance embedding dual; their examples cover paths, cycles, and a small six-vertex graph, but do not state this lollipop family optimum or the clique-edge activation. Richter and Rocha (2014 preprint) give a complete optimization for **double-broom trees**, which lacks the full peripheral clique constraints and hence does not imply the rate reallocation here. Jafarizadeh's clique-lifted **discrete-time** lollipop optimization concerns stochastic transition probabilities and second-largest eigenvalue modulus under vertexwise feasibility; it does not assert this total-continuous-rate-budget Laplacian optimum. Li, Guo, and Shiu study the **unweighted** kite graph's algebraic connectivity as an extremal graph among fixed-clique-number graphs, not optimal variable conductances. These contrasts are comparisons of statements and constraints, not mere title differences.

## Limitations

The result concerns continuous-time symmetric rates with uniform stationary distribution and a global sum budget, for the specific two-vertex-tail graph, and makes no prediction for longer pendant paths, general clique-chain graphs, discrete-time SLEM minimization, or fixed per-node rates. A potentially relevant 2002 paper by Kirkland and Pati on vertex connectivity and absolute algebraic connectivity was identified by abstract but not obtained in full text; stronger prior coverage there cannot be excluded.

## References

1. J. Sun, S. Boyd, L. Xiao, and P. Diaconis, “The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem,” *SIAM Review* **48** (2006), 681–699. DOI: `10.1137/S0036144504443821`. Full text: `https://stanford.edu/~boyd/papers/pdf/fmmp.pdf` (public 2006-11-02).
2. S. Richter and I. Rocha, “Absolute Algebraic Connectivity of Double Brooms,” Chemnitz preprint, 2014, `https://www.tu-chemnitz.de/mathematik/preprint/2014/PREPRINT_10.pdf`.
3. S. Jafarizadeh, “Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs,” `https://arxiv.org/abs/2501.02421`; accessible earlier full-text version at `https://www.researchgate.net/profile/Saber-Jafarizadeh/publication/338414306_Fastest_Mixing_Reversible_Markov_Chain_Clique_Lifted_Graphs_and_Subgraphs/links/649049d795bbbe0c6edab526/Fastest-Mixing-Reversible-Markov-Chain-Clique-Lifted-Graphs-and-Subgraphs.pdf`.
4. J. Li, J.-M. Guo, and W. C. Shiu, “The minimum algebraic connectivity of graphs with a given clique number,” full-text preprint `https://shiu1958.github.io/PDF/p1170-final.pdf`.
5. S. Kirkland and S. Pati, “On Vertex Connectivity and Absolute Algebraic Connectivity for Graphs,” *Linear and Multilinear Algebra* (2002), DOI: `10.1080/03081080290025453` (abstract consulted; full text unavailable).
