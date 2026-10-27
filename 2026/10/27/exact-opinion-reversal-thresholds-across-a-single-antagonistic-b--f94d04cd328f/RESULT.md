# Exact opinion-reversal thresholds across a single antagonistic bridge

## Finding

Consider two nonempty connected cooperative communities joined by one antagonistic edge of variable strength \(t>0\). In a signed Friedkin–Johnsen equilibrium, suppose every agent has the *same innate opinion* \(+1\), while positive anchoring strengths and within-community friendly edge weights may vary. Then the signs of all expressed opinions admit exact thresholds determined only by two effective anchoring strengths and two positive-community Green functions. In particular, a negative expressed opinion occurs for some finite \(t\) **if and only if** the two effective anchoring strengths differ; a sign reversal occurs only on the side with the smaller effective anchoring strength. The vertices with negative expressed opinions form a connected set containing that side's bridge endpoint and grow monotonically with \(t\).

Specifically, let \(a\) and \(b\) be the endpoints of the negative bridge in communities \(U\) and \(W\), respectively. Let \(K_U,K_W\) be diagonal matrices with strictly positive anchoring coefficients, and let \(L_U,L_W\) be their positive-weight graph Laplacians. Put

\[
M_U=K_U+L_U,\qquad M_W=K_W+L_W,\qquad G_U=M_U^{-1},\qquad G_W=M_W^{-1},
\]
\[
A=\frac{1}{(G_U)_{aa}},\qquad B=\frac{1}{(G_W)_{bb}},\qquad
h_i=\frac{(G_U)_{ia}}{(G_U)_{aa}},\qquad g_j=\frac{(G_W)_{jb}}{(G_W)_{bb}}.
\]

All the quantities \(A,B,h_i,g_j\) are positive, and \(0<h_i\le1\), \(0<g_j\le1\), with \(h_a=g_b=1\). The equilibrium \(z(t)\) is exactly

\[
z_i(t)=1-\frac{2tB h_i}{AB+t(A+B)}\quad (i\in U),\qquad
z_j(t)=1-\frac{2tA g_j}{AB+t(A+B)}\quad (j\in W).
\]

For \(i\in U\), write \(C_i=2Bh_i-(A+B)\). If \(C_i\le0\), then \(z_i(t)>0\) for every finite \(t>0\). If \(C_i>0\), then

\[
z_i(t)\begin{cases}>0&t<AB/C_i,\\=0&t=AB/C_i,\\<0&t>AB/C_i.\end{cases}
\]

The right-side criterion is identical with \(C_j'=2Ag_j-(A+B)\). The first reversal, if any, is at the weakly anchored bridge endpoint, at the sharp threshold

\[
t_* = \frac{AB}{|A-B|}\qquad(A\ne B).
\]

When \(A=B\), all expressed opinions stay strictly positive for every finite \(t\). The reversal set at each \(t\) is either empty or a single rooted connected subgraph; on the other community it is always empty. This statement holds for arbitrary finite connected within-community graphs, including graphs with cycles.

## Assumptions and scope

Let \(G=(V,E)\) be a finite undirected graph whose removal of the single negative edge \(\{a,b\}\) leaves precisely two connected components \(U\) and \(W\). All edges within those components are cooperative, with fixed positive symmetric weights \(c_{ij}\). The negative bridge has signed adjacency weight \(-t\), with \(t>0\). Every node \(i\) has anchoring coefficient \(k_i>0\) and innate opinion \(s_i=1\). There are no other negative edges. The signed Laplacian \(L_\pm(t)\) has the usual positive-edge quadratic energy \(c_{ij}(x_i-x_j)^2\) and negative-edge energy \(t(x_a+x_b)^2\). The unique equilibrium solves

\[
(K+L_\pm(t))z(t)=K\mathbf1,\qquad K=\operatorname{diag}(k_i).
\]

This is a deterministic equilibrium statement, not a statement about individual transient trajectories or stochastic opinion formation. A sign reversal means a strictly negative *expressed* equilibrium opinion despite every innate opinion being \(+1\). Threshold equality means the indicated opinion is zero, not negative.

## Proof

**1. Positive definiteness and reduction.** Define the strictly convex quadratic energy

\[
\mathcal E(x)=\frac12\sum_{i\in V}k_i(x_i-1)^2+
\frac12\sum_{\{i,j\}\in E\setminus\{\{a,b\}\}}c_{ij}(x_i-x_j)^2+
\frac t2(x_a+x_b)^2.
\]

Its Hessian is \(K+L_\pm(t)\succ0\), because every \(k_i>0\) and all edge terms are nonnegative. Its unique minimizer is the stated equilibrium.

On \(U\), constrain \(x_a=u\) and minimize the internal community energy. Since \(M_U\mathbf1=K_U\mathbf1\), the displacement \(f=x-\mathbf1\) satisfies \((M_Uf)_i=0\) for all \(i\ne a\), and \(f_a=u-1\). The vector \(G_Ue_a/(G_U)_{aa}\) is the unique solution of this Dirichlet problem with endpoint value \(1\). Thus the constrained minimizer is \(x_i=1+h_i(u-1)\). The minimized community energy is \(A(u-1)^2/2\): indeed, \(M_Uf=(u-1)e_a/(G_U)_{aa}\) and \(f^{\mathsf T}M_Uf=(u-1)^2/(G_U)_{aa}\). The same argument on \(W\) gives \(x_j=1+g_j(v-1)\) and energy \(B(v-1)^2/2\).

Hence the full minimization is exactly the two-variable strictly convex problem

\[
\min_{u,v}\left\{\frac A2(u-1)^2+\frac B2(v-1)^2+\frac t2(u+v)^2\right\}.
\]

**2. Exact endpoint response.** Its two first-order equations are \(A(u-1)+t(u+v)=0\) and \(B(v-1)+t(u+v)=0\). Solving gives, with \(\Delta=AB+t(A+B)>0\),

\[
u=\frac{AB+t(A-B)}{\Delta},\qquad v=\frac{AB+t(B-A)}{\Delta},
\]

and substituting in the harmonic extensions gives the exact formulas in the finding.

**3. Positivity of the Green profiles.** Each \(M_U\) is an irreducible, strictly diagonally dominant \(M\)-matrix because the friendly component is connected and \(k_i>0\). Alternatively, its inverse is the convergent nonnegative Neumann series obtained by splitting its positive diagonal from its nonpositive off-diagonal entries; connectivity makes every inverse entry strictly positive. Thus \(h_i>0\). At a nonroot vertex, the harmonic equation reads

\[
h_i=\frac{\sum_{j\sim i}c_{ij}h_j}{k_i+\sum_{j\sim i}c_{ij}}.
\]

The positive killing term \(k_i\) and the maximum principle imply \(h_i<1\) for \(i\ne a\), with \(h_a=1\). The same holds for \(g\).

**4. Sharp sign and connectedness classification.** Multiplying the exact formula for \(z_i\) by \(\Delta>0\) gives \(\Delta z_i=AB-t[2Bh_i-(A+B)]\), yielding the threshold alternatives in the finding. Since \(h_i\le1\), a positive left threshold coefficient requires \(B>A\), while a positive right coefficient requires \(A>B\). Hence not both sides can contain negative nodes, and any reversal first occurs at the endpoint with \(h_a=1\) or \(g_b=1\), at \(t_*=AB/|A-B|\). All coordinates strictly decrease as functions of \(t>0\), so the negative set is nested as hostility strengthens.

Finally, let a left vertex have \(h_i>\eta>0\). If \(i\ne a\), the displayed harmonic averaging identity guarantees an adjacent vertex with a **strictly larger** \(h\)-value; otherwise the average would be strictly smaller than \(h_i\), a contradiction. Repeatedly following strictly increasing values on the finite connected community reaches the only exceptional vertex \(a\). Every intermediate vertex stays above \(\eta\). Consequently every strict superlevel set of \(h\) is connected and contains \(a\), and similarly for \(g\). At fixed \(t\), the negative-opinion set is exactly one such superlevel set on the weaker side, proving rooted connectedness. No tree assumption is used.

## Verification

The standalone `verify.py` uses exact rational Gaussian elimination, independent of the reduced-form derivation, to solve full signed equilibrium systems. It checks the analytic formulas, strict positivity of harmonic profiles, exact sign thresholds, the one-side-only restriction, and connectedness of negative-opinion vertices on \(650\) deterministic pseudorandom instances with connected cooperative components of up to four nodes each, seven antagonistic strengths per instance, and six exact benchmark checks: **4,556 cases passed**. Run `python3 verify.py` using only the Python standard library. This finite test is a consistency check and is not a substitute for the proof.

An explicit three-agent path demonstrates two distinct sign-change strengths. The positive edge joins vertices \(c\) and \(a\) with weight \(1\); the sole negative bridge joins \(a\) and \(b\) with weight \(t\); the anchoring coefficients are \(k_c=1/10\), \(k_a=1\), \(k_b=4\). Every innate opinion is \(+1\). Here \(A=12/11\), \(B=4\), \(h_a=1\), and \(h_c=10/11\). In order \((c,a,b)\),

\[
(z_c,z_a,z_b)=\left(\frac{48-24t}{48+56t},\frac{48-32t}{48+56t},\frac{48+32t}{48+56t}\right).
\]

Thus the bridge endpoint \(a\) crosses zero at \(t=3/2\), then \(c\) crosses at \(t=2\), while \(b\) remains positive. At \(t=3\), the equilibrium is \((-1/9,-2/9,2/3)\).

The phenomenon needs no heterogeneity in anchoring coefficients: take the three-node path with a negative edge \(a-b\), a positive edge \(b-c\) of strength \(1\), and \(k_a=k_b=k_c=1\). Then \(A=1\), \(B=3/2\), and the first reversal occurs exactly at \(t=3\). At \(t=4\), the equilibrium in order \((a,b,c)\) is \((-1/23,7/23,15/23)\). Here the imbalance is entirely structural: the positive network behind \(b\) changes its effective anchoring.

## Relationship to prior work

Xu, Hu, Wu, and Liu (2020) established an equilibrium inverse formula for signed social trust networks and investigated maximizing aggregate opinion by manipulating initial or expressed opinions. Zhou, Sun, Xu, Li, and Zhang (2024) studied the signed Friedkin–Johnsen model, signed-walk representations, aggregate disagreement and polarization quantities, fast solvers, and opinion seeding. Both papers supply relevant equilibrium formalism, including inverse matrices whose evaluation can in principle resolve any fixed instance. Neither inspected work states the present *all-network if-and-only-if hostility threshold*, the effective-anchoring criterion \(A\ne B\) with unanimous innate opinions, or the nested connected sign-reversal footprint of a single antagonistic bridge. These conclusions require an additional two-community Dirichlet reduction and maximum-principle analysis; they are not claimed as a new equilibrium formula for general signed networks. A more recent study of fairness-aware seeding in weighted signed networks addresses a different intervention (changing innate opinions) and is noted as a publication-priority comparison, with access limitations recorded separately.

## Limitations

The result requires one negative **bridge**, no other hostile edges, strictly positive anchoring at every node, positive undirected within-community ties, and unanimous innate opinion \(+1\). Without the bridge decomposition or with multiple negative ties, the sign geometry may be different. The theorem does not characterize sign reversals from arbitrary innate profiles, finite-time convergence rates, or directed networks. Standard Schur-complement and maximum-principle machinery is central to its proof, so the claim of originality is specifically the synthesized sharp sign-footprint classification, not those background tools. Independent scientific audit has not been performed.

## References

1. P. Xu, W. Hu, J. Wu, and W. Liu, *Opinion Maximization in Social Trust Networks*, IJCAI 2020, arXiv:2006.10961v1 (first publicly posted 2020-06-19), https://arxiv.org/abs/2006.10961.
2. X. Zhou, H. Sun, W. Xu, W. Li, and Z. Zhang, *Friedkin-Johnsen Model for Opinion Dynamics on Signed Graphs*, arXiv:2407.10680v1 (first publicly posted 2024-07-15), https://arxiv.org/abs/2407.10680.
3. Z. Lu et al., *Fairness-Aware Opinion Seeding in Undirected Signed Friedkin–Johnsen Networks*, Mathematics 14(19), 3478 (2026), https://doi.org/10.3390/math14193478. Used solely for later-literature comparison.
