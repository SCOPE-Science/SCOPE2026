# A sharp backup-edge price for fault-tolerant diffusion on book graphs

## Finding

Let \(m\ge 2\) be an integer and let \(G_m\) be the book graph consisting of two hubs \(A,B\), \(m\) other vertices \(v_1,\dots,v_m\), every edge \(Av_j,Bv_j\), and the common hub edge \(AB\). Fix an expenditure budget \(B_0>0\) and a relative price \(t>0\) on the common edge; each of the \(2m\) other edges has price one. For independently adjustable nonnegative edge conductances \(w\), write

\[
\mathcal{F}(w)=\min_{e\in E(G_m)}\lambda_2\bigl(L(w)-w_e(e_i-e_j)(e_i-e_j)^{\mathsf T}\bigr),
\qquad \sum_{e\ne AB}w_e+t w_{AB}\le B_0,
\]

where \(i,j\) are the endpoints of the deleted edge \(e\), \(L(w)\) is the combinatorial weighted Laplacian, and \(\lambda_2\) is its second-smallest eigenvalue, including zero if the surviving weighted network is disconnected. All conductances are fixed *before* an adversary removes one permissible edge; no reallocation occurs afterward.

Define \(u_m\in(0,1)\) as the unique root of

\[
 u^3+(2m-1)u^2+(m^2-m-1)u-1=0
\]

and define the positive critical price

\[
\boxed{\displaystyle
 t_c(m)=\frac{2m\,[1+(2m+1)u_m+2u_m^2]}{(1-u_m)[m^2-m-1+(4m-2)u_m+3u_m^2]}.}
\]

**Exact deletion/retention law.** Among all independently adjustable conductance assignments, a globally optimal assignment exists with a common spoke conductance \(a>0\) and hub-edge conductance \(b\ge0\). Its pair \((a,b)\) is unique among symmetry-invariant assignments. Moreover, **every** unrestricted global optimizer has the *same* hub-edge conductance \(b\), with

\[
\boxed{\quad b>0\ \Longleftrightarrow\ 0<t<t_c(m),\qquad
b=0\ \Longleftrightarrow\ t\ge t_c(m).\quad}
\]

The optimal value and the unique symmetry-invariant allocation are determined as follows. For \(r\ge0\), let \(f_m(r)\) be the unique root in \((0,2)\) of

\[
\begin{aligned}
P_m(z,r)={}&z^3-(2m+2+2r)z^2\\
&+[m^2+3m+(2m+5)r]z\\
&-m^2-m+2-(2m+4)r.
\end{aligned}
\]

Set \(r_*=0\) when \(t\ge t_c(m)\). When \(0<t<t_c(m)\), let \(r_*>0\) be the **unique** solution to

\[
(2m+t r_*)f_m'(r_*)=t f_m(r_*),
\qquad f_m'(r)=-\frac{\partial_rP_m(f_m(r),r)}{\partial_zP_m(f_m(r),r)}.
\]

Then

\[
\boxed{\displaystyle a=\frac{B_0}{2m+t r_*},\qquad
b=\frac{B_0 r_*}{2m+t r_*},\qquad
\max_w\mathcal F(w)=\frac{B_0 f_m(r_*)}{2m+t r_*}.}
\]

The critical price has the exact special value and large-book asymptotic

\[
\boxed{t_c(2)=3+2\sqrt 2,\qquad \lim_{m\to\infty}m t_c(m)=2.}
\]

A noteworthy contrast is that without an edge outage the corresponding budgeted spectral-gap problem has **zero** optimal hub-edge conductance for every \(t>0\), whereas under the single-outage criterion the hub edge is compulsory at every unrestricted optimum for \(t<t_c(m)\). Thus the optional edge is spectrally useless in the intact symmetric design but can be necessary for fault tolerance.

## Assumptions and scope

All graph edges are undirected, and the Laplacian counts each unordered edge exactly once. The two hubs connect individually to every page vertex, and the common edge connects the hubs. There are \(m+2\) vertices and \(2m+1\) permissible edges, including an edge whose chosen conductance may be zero. Conductances and costs are nonnegative and strictly positive, respectively, except permitted zero conductances. The deletion of one permissible edge is evaluated with all surviving conductances unchanged. The objective is continuous-time consensus/Markov diffusion spectral decay, *not* discrete-time second-largest eigenvalue modulus. The graph size, price and budget are quantified universally over \(m\ge2\), \(t>0\), \(B_0>0\).

The theorem determines the unrestricted optimal **value** and the compulsory/forbidden hub-edge conductance, and constructs the unique symmetric optimal design. It does not assert uniqueness of every individual spoke weight among arbitrary asymmetric unrestricted optima.

## Proof

**1. Symmetrization works for the adversarial objective.** For an edge \(e=\{i,j\}\), the surviving Laplacian is

\[
 L_{-e}(w)=\sum_{f\in E(G_m)\setminus\{e\}}w_f d_fd_f^{\mathsf T},
 \qquad d_f=e_{f^-}-e_{f^+}.
\]

For every \(w\ge0\), its second eigenvalue is the smallest eigenvalue of the restriction to the fixed subspace \(\mathbf1^\perp\), and hence is a concave function of \(w\). The minimum of finitely many concave functions is concave (its hypograph is the intersection of their hypographs); consequently \(\mathcal F\) is concave. It is invariant under permutations of the \(m\) page vertices and exchange of the two hubs. Averaging any feasible design over these automorphisms preserves its budget and cannot lower \(\mathcal F\). Compactness gives an optimum. Choosing every spoke positive gives strictly positive worst-outage gap because \(K_{2,m}\) remains connected after any one edge is removed when \(m\ge2\); therefore every maximizer exhausts the budget by positive homogeneity. Hence there is an optimal design with a shared spoke conductance \(a>0\), hub conductance \(b\ge0\), and \(2ma+tb=B_0\).

**2. The spoke outage always determines the symmetric worst case.** Put \(r=b/a\). Removing the common edge leaves the weighted complete bipartite graph \(K_{2,m}\), whose Laplacian has second eigenvalue \(2a\) for \(m\ge2\). Removing a spoke and dividing the Laplacian by \(a\) instead produces a single-degree-one page vertex. A test vector equal to \(1\) on that vertex and \(-1/(m+1)\) at every other vertex has Rayleigh quotient \((m+2)/(m+1)<2\). Thus a spoke outage is strictly worse than removal of the common edge.

After choosing the deleted spoke as \(Av_1\), the Laplacian for that outage splits into an eigenspace of eigenvalue \(2\), with multiplicity \(m-2\), and the invariant space spanned by the two hubs, \(v_1\), and the normalized sum of the remaining \(m-1\) pages. In this orthonormal basis the remaining \(4\times4\) block is

\[
Q_m(r)=\begin{pmatrix}
m-1+r&-r&0&-\sqrt{m-1}\\
-r&m+r&-1&-\sqrt{m-1}\\
0&-1&1&0\\
-\sqrt{m-1}&-\sqrt{m-1}&0&2
\end{pmatrix}.
\]

Direct determinant expansion gives \(\det(zI-Q_m(r))=zP_m(z,r)\). Here \(P_m(0,r)=-(m+2)(m+2r-1)<0\) and \(P_m(2,r)=(m-1)(m+2r-2)\ge0\). If all three positive roots lay below \(2\), their sum would be less than \(6\), contradicting \(\operatorname{tr}Q_m(r)=2m+2+2r\ge6\). Thus exactly one positive root lies below \(2\); the endpoint \((m,r)=(2,0)\) is checked directly, with roots \(2-\sqrt2,2,2+\sqrt2\). This uniquely determines \(f_m(r)\), which is simple and satisfies \(0<f_m(r)<2\). For symmetric conductances the worst-outage value is therefore \(a f_m(r)\).

**3. Strict increase and strict concavity of the root.** On the spoke-deleted graph, changing \(r\) adds \(rdd^{\mathsf T}\) with \(d=e_A-e_B\). Let \(v\perp\mathbf1\) be the normalized Fiedler eigenvector. Its two hub coordinates cannot agree: if they did, subtracting the two hub eigenvalue equations would force the lone page's coordinate equal to their common value, the lone page's own equation would force that value to zero, and the remaining page equations would force all coordinates to zero. Thus \(d^{\mathsf T}v\ne0\), and eigenvalue perturbation gives \(f_m'(r)=(d^{\mathsf T}v)^2>0\). Because \(f_m(r)\) is simple, the second-derivative formula in an orthonormal Laplacian eigenbasis gives

\[
f_m''(r)=2\sum_{j\ge3}\frac{|\langle v_j,dd^{\mathsf T}v\rangle|^2}{f_m(r)-\lambda_j}<0.
\]

The constant eigenvector contributes zero because \(d\perp\mathbf1\); at least one numerator in the sum is nonzero because \(d\) is not an eigenvector of the spoke-deleted Laplacian (its image has nonzero page coordinates). Hence the derivative is strictly decreasing for every finite \(r\ge0\). The bounded increasing function \(f_m\) satisfies \(f_m'(r)\to0\) and \(r f_m'(r)\to0\).

**4. Exact critical budget price and optimizer.** With \(r\ge0\), budget exhaustion forces \(a=B_0/(2m+tr)\). Hence maximizing the symmetric robust gap is the scalar problem

\[
\max_{r\ge0}\frac{B_0 f_m(r)}{2m+tr}.
\]

Its derivative has the sign of \(g_t(r)=(2m+tr)f_m'(r)-t f_m(r)\). By strict concavity,
\(g_t'(r)=(2m+tr)f_m''(r)<0\), and \(g_t(r)\to-t\lim_{s\to\infty}f_m(s)<0\). Therefore the unique symmetric optimum has \(r_*=0\) if and only if \(t\ge 2m f_m'(0)/f_m(0)\); otherwise it has exactly one positive root of \(g_t(r)=0\).

Let \(u=1-f_m(0)\). From \(P_m(1-u,0)=0\) one gets the stated cubic for \(u\), whose derivative is strictly positive for positive \(u\); its values at \(0\) and \(1\) have opposite signs. Direct implicit differentiation of \(P_m\) yields

\[
f_m'(0)=\frac{1+(2m+1)u+2u^2}{m^2-m-1+(4m-2)u+3u^2},
\]

proving the displayed critical-price formula. At \(m=2\), \(u=\sqrt2-1\), yielding \(t_c(2)=3+2\sqrt2\). Since the cubic gives \(u_m=m^{-2}+O(m^{-3})\), the same formula gives \(t_c(m)=2m^{-1}+O(m^{-2})\).

**5. The bridge conclusion holds for every unrestricted optimizer.** Symmetrization leaves the hub-edge weight unchanged because that edge is fixed by every graph automorphism. The symmetric optimizer is unique in the two variables \((a,b)\). Consequently averaging *any* unrestricted optimizer produces that same pair and forces its original hub-edge conductance to equal the displayed \(b\). This establishes both directions of the deletion/retention law without asserting uniqueness of unrestricted spoke allocations.

Finally, for the intact symmetric graph the page-difference eigenmodes have eigenvalue \(2a\); the remaining nonzero modes have eigenvalues \(m a+2b\) and \((m+2)a\), each at least \(2a\). Thus the intact spectral gap is exactly \(2a\), so its optimal bridge cost is always zero when \(t>0\). By the same averaging and fixed-edge argument, every unrestricted intact optimum also has zero hub-edge conductance.

## Verification

The standalone Python program `verify_bridge.py` constructs full Laplacians without calling the symbolic block representation, checks all candidate single-edge outages, independently evaluates the derived cubic and exact \(m=2\) price, and compares the analytic maximizer with scalar optimization and nonsymmetric feasible assignments. Executing it with Python, NumPy, SciPy and SymPy passed six explicit symbolic-identity assertions and \(1{,}295\) accumulated numerical/structural checks, including \(315\) direct spectral/outage comparisons and many differently priced asymmetric designs. The proof above—not finite experiments—establishes every quantified parameter claim.

For an illustrative unit budget, when \(m=3\) the critical price is approximately \(2.394885523\). At price \(t=1\) the unique symmetric optimum has \(a\approx0.1529777594\) on every spoke and \(b\approx0.0821334434\) on the hub edge. At price \(t=3\), every optimum has \(b=0\) and the symmetric optimum has \(a=1/6\).

## Relationship to prior work

Sun, Boyd, Xiao, and Diaconis (2006) formulated weighted algebraic-connectivity maximization under linear conductance expenditure as a convex semidefinite problem, with physical interpretations as heat or Markov diffusion. Their objective concerns the intact network, not the worst spectral gap across every single-edge outage. Boyd, Diaconis, Parrilo, and Xiao (2007 preprint; 2009 journal) give symmetry-based reductions and results for complete bipartite graphs and discrete-time fastest mixing. Their intact-graph calculations do not specify the present one-failure robust criterion on a book graph or its price threshold. Sydney, Scoglio, and Gruenbacher (2013) address selecting discrete edge rewirings to raise intact algebraic connectivity; that differs from continuous conductance allocation under an explicit one-edge adversary. The present contribution is the sharp all-parameter fault-tolerance price, characterization of the retained-edge conductance across all global optima, and the asymptotic price scale.

## Limitations

The theorem is restricted to a single adversarial edge deletion, linear conductance prices, two hubs, and identical spoke prices; it does not address multiple simultaneous failures, other page graphs, or heterogeneous spoke prices. It does not classify all unrestricted asymmetric spoke allocations. The originality comparison uses accessible published full text for the two foundational eigenvalue-optimization sources and bibliographic/abstract evidence for the edge-rewiring source. An unindexed equivalence in more general robust semidefinite network design remains a genuine risk and requires independent literature verification. Neither a numerical search nor absence of a keyword match proves universal originality.

## References

1. J. Sun, S. Boyd, L. Xiao, and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699, DOI: 10.1137/S0036144504443821. Electronic publication 2006-11-02; accessible author-hosted full text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf.
2. S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955 (first version 2007-09-06), later SIAM Journal on Optimization 20 (2009), 792–819. Accessible full text: https://ar5iv.labs.arxiv.org/html/0709.0955.
3. A. Sydney, C. Scoglio, and D. Gruenbacher, *Optimizing Algebraic Connectivity by Edge Rewiring*, Applied Mathematics and Computation 219 (2013), 5465–5479, DOI: 10.1016/j.amc.2012.11.002. The abstract and bibliographic record were compared; full text was unavailable in this review.
