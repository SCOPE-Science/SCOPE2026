# Price-induced parity bifurcation for minimum-resistance two-hop rings

## Finding

For every integer \(n\ge5\), consider the simple undirected graph on \(\mathbb Z/n\mathbb Z\) with all first-neighbor edges \(\{i,i+1\}\) and second-neighbor edges \(\{i,i+2\}\). Each first-neighbor conductance costs one unit per unit weight; each second-neighbor conductance costs \(t>0\). Under total expenditure \(B>0\), choose independent nonnegative edge conductances to minimize the sum of effective resistances over all unordered vertex pairs, with disconnected networks assigned infinite cost.

Put
\[
 t_{\mathrm{high}}(n)=\frac{4(n-2)}{n+1},\qquad
 t_{\mathrm{low}}(n)=\frac{16}{n^2+7}\quad(n\text{ odd}).
\]
There is exactly one global optimizer. It has a common first-neighbor weight \(a\) and common second-neighbor weight \(b\), with \(n(a+tb)=B\), and its support has the following complete classification:

1. For every \(n\ge5\) and \(t\ge t_{\mathrm{high}}(n)\), \(a=B/n\) and \(b=0\).
2. For odd \(n\ge5\) and \(0<t\le t_{\mathrm{low}}(n)\), \(a=0\) and \(b=B/(nt)\).
3. In every other case, both \(a\) and \(b\) are strictly positive; this includes every even \(n\ge6\) whenever \(0<t<t_{\mathrm{high}}(n)\).

The values at both thresholds belong to the corresponding single-edge-class regions, and the optimizer is unique at equality. In the mixed region, \(b\) is the unique root inside \((0,B/(nt))\) of
\[
\sum_{k=1}^{n-1}\frac{s_k-t}{\mu_k[\,B/n+b(s_k-t)\,]^2}=0,
\quad \mu_k=4\sin^2(\pi k/n),\quad s_k=4\cos^2(\pi k/n),
\]
with \(a=B/n-tb\). Consequently, the cheap-shortcut sparsification threshold occurs only for odd cycles and is asymptotic to \(16/n^2\); the expensive-shortcut threshold exists for both parities and tends to \(4\).

## Assumptions and scope

All graph edges are undirected, each edge is counted once, and a length-two edge connects distinct vertices for every \(n\ge5\); each edge class contains exactly \(n\) edges. Prices and the budget are strictly positive and the edge weights may be zero. In particular, no prescribed positive lower bound is imposed on individual weights. The objective is
\[
 R_{\mathrm{tot}}(L)=\sum_{0\le i<j<n}(e_i-e_j)^\mathsf T L^\dagger(e_i-e_j)=n\operatorname{tr}(L^\dagger)
\]
for connected weighted Laplacians. For a disconnected weighted graph define \(R_{\mathrm{tot}}=+\infty\), rather than using a finite formal pseudoinverse trace disconnected from physical pairwise resistance. The graph is not restricted to circulant conductances when the optimization begins.

## Proof

**Global optimization and symmetry.** The effective-resistance objective is homogeneous of degree \(-1\) in positive uniform scaling of conductances. Hence a finite optimizer spends the entire budget, which is feasible by assigning positive weights to all first-neighbor edges. The price-constrained nonnegative polytope is compact. On approaching disconnection, a nonzero Laplacian eigenvalue tends to zero and the objective diverges, so a minimizer exists and is connected.

Let \(P=I-\mathbf1\mathbf1^\mathsf T/n\). On \(\mathbf1^\perp\), the Laplacian \(L\) is positive definite for every connected allocation, and the objective is \(n\operatorname{tr}(L|_{\mathbf1^\perp}^{-1})\). For every nonzero symmetric perturbation \(D\) in that subspace,
\[
\frac{d^2}{du^2}\operatorname{tr}(L+uD)^{-1}\Big|_{u=0}
 =2\operatorname{tr}(L^{-1}DL^{-1}DL^{-1})>0.
\]
Indeed, setting \(H=L^{-1/2}DL^{-1/2}\), the trace equals \(2\operatorname{tr}(L^{-1/2}H^2L^{-1/2})>0\). The edge-weight-to-Laplacian map is injective for a simple graph, because each off-diagonal edge entry records one weight, so the optimization is strictly convex in its edge weights on the connected domain. Every rotation of an optimizer is also optimal and preserves its price. Uniqueness therefore forces rotation invariance, yielding precisely the two class weights \(a,b\) and \(a+tb=c:=B/n\). Reflection invariance is automatic for these edge classes.

**Fourier reduction and convexity.** The nonzero Fourier eigenvalues of the first- and second-neighbor cycle Laplacians are, for \(1\le k<n\),
\[
\mu_k=4\sin^2(\pi k/n),\qquad \nu_k=4\sin^2(2\pi k/n)=\mu_k s_k,
\quad s_k=4\cos^2(\pi k/n).
\]
The minimized objective, apart from the positive constant factor \(n\), is
\[
\Phi(b)=\sum_{k=1}^{n-1}\frac{1}{\mu_k[\,c+b(s_k-t)\,]},
\qquad 0\le b\le c/t.
\]
If \(n\) is even, the right endpoint is disconnected and \(\Phi(b)\to+\infty\) there; if \(n\) is odd, the right endpoint is a connected second-neighbor cycle. In the connected interval,
\[
\Phi'(b)=-\sum_{k=1}^{n-1}\frac{s_k-t}{\mu_k[\,c+b(s_k-t)\,]^2},
\qquad
\Phi''(b)=2\sum_{k=1}^{n-1}\frac{(s_k-t)^2}{\mu_k[\,c+b(s_k-t)\,]^3}>0.
\]
Strictness holds since the \(s_k\) are not all equal for \(n\ge5\). Thus the signs of the two endpoint derivatives determine the complete phase diagram, and every interior stationary point is unique.

**First-neighbor endpoint.** The standard finite-cycle identity gives
\[
S_n:=\sum_{k=1}^{n-1}\frac1{\mu_k}=\frac{n^2-1}{12}.
\]
Since \(s_k=4-\mu_k\), one obtains
\[
\Phi'(0)=-c^{-2}\bigl[(4-t)S_n-(n-1)\bigr].
\]
It is nonnegative exactly when \(t\ge4-(n-1)/S_n=4(n-2)/(n+1)\). By strict convexity, this is necessary and sufficient for the all-first-neighbor optimizer.

**Second-neighbor endpoint, odd order.** When \(n\) is odd, multiplication by \(2\) permutes the nonzero residues, so \(\sum_{k=1}^{n-1}1/\nu_k=S_n\). At \(b=c/t\) the derivative is
\[
\Phi'(c/t)=-\frac{t^2}{c^2}\left[S_n-t T_n\right],
\qquad T_n:=\sum_{k=1}^{n-1}\frac{\mu_k}{\nu_k^2}.
\]
To evaluate \(T_n\), use the exact partial fractions
\[
\frac{\mu}{\nu^2} = \frac{1}{\mu(4-\mu)^2}
=\frac{1}{16\mu}+\frac{1}{16(4-\mu)}+\frac{1}{4(4-\mu)^2}.
\]
The well-known cosecant identity
\[
\sum_{k=0}^{n-1}\csc^2(x+k\pi/n)=n^2\csc^2(nx)
\]
by comparing its constant Laurent coefficients at \(x=0\) proves \(S_n=(n^2-1)/12\). For odd \(n\), translating the variable by \(\pi/2\) gives
\[
\sum_{k=0}^{n-1}\sec^2(x+k\pi/n)=n^2\sec^2(nx).
\]
Evaluating at \(x=0\) and taking two derivatives yields, after excluding the \(k=0\) summand,
\[
\sum_{k=1}^{n-1}\sec^2(k\pi/n)=n^2-1,\qquad
\sum_{k=1}^{n-1}\sec^4(k\pi/n)=\frac{n^4+2n^2-3}{3}.
\]
Substitution, using \(4-\mu_k=4\cos^2(\pi k/n)\), gives
\[
T_n=\frac{S_n}{16}+\frac{n^2-1}{64}+\frac{n^4+2n^2-3}{192}
=\frac{(n^2-1)(n^2+7)}{192}.
\]
Hence \(\Phi'(c/t)\le0\) exactly when \(t\le S_n/T_n=16/(n^2+7)\). Strict convexity proves the unique all-second-neighbor solution throughout that range. The two thresholds satisfy \(0<t_{\mathrm{low}}(n)<t_{\mathrm{high}}(n)\) for every odd \(n\ge5\), so the interior regime is nonempty.

**Even order and completeness.** If \(n\) is even, the second-neighbor-only support disconnects into two parity classes, and a Fourier mode has \(\nu_{n/2}=0\) but \(\mu_{n/2}=4\). As \(b\uparrow c/t\), the corresponding term in \(\Phi\) diverges. For \(t<t_{\mathrm{high}}(n)\), the derivative is strictly negative at zero and strictly positive near the right endpoint, so one unique interior optimum exists. For larger prices the zero endpoint is unique. This exhausts all orders, prices, and allocation patterns.

## Verification

The self-contained `CHECK.py` uses only Python 3 standard-library rational arithmetic for direct inverses of \(L+\mathbf1\mathbf1^\mathsf T/n\), exact boundary derivatives, and strict convexity finite differences, and compares independently evaluated Fourier sums to full-matrix traces. Run `python3 CHECK.py` in the directory containing this document. It reports 68 checks for \(5\le n\le11\); no floating-point experiment supplies the infinite-order proof. The exact identities, second-derivative positivity and connectivity arguments above are the universal certificates.

## Relationship to prior work

Ghosh, Boyd and Saberi (2006) introduced the general total-effective-resistance conductance allocation problem, its strict-convexity framework and optimality conditions. The convex design formulation and symmetry averaging are not claimed as new here. Chair (2014) computed resistance distances and the total resistance of the unit-weight \(C_n(1,2)\) and examined removal of all first-neighbor edges, including the known odd/even connectivity distinction. The Fourier diagonalization of a circulant and this parity graph fact are likewise prior work. Zhang and Yang (2006) gave general spectral expressions and several closed forms for unweighted circulants. The claim here concerns different optimization quantifiers: all independently adjustable nonnegative weights under a two-price budget, the unique globally optimal support, and exact two-sided cost transitions \(t_{\mathrm{low}},t_{\mathrm{high}}\). These do not follow solely by evaluating resistances of fixed unweighted networks.

## Limitations

The theorem is limited to the square of an undirected cycle, \(n\ge5\), with a constant cost per edge class and a linear budget. It does not classify other circulant step sets, higher-hop shortcuts, nonlinear cost schedules, edge-capacity constraints, or objectives such as spectral-gap maximization and spanning-tree count. The mixed-regime optimizer is characterized by a unique scalar root rather than a radical closed form. The proof establishes scientific correctness conditional on the stated model; an identical result may exist in unindexed literature, and no independent external audit is asserted.

## References

1. A. Ghosh, S. Boyd, and A. Saberi, “Minimizing Effective Resistance of a Graph,” Proceedings of the 17th International Symposium on Mathematical Theory of Networks and Systems, Kyoto, July 24–28, 2006, pp. 1185 ff. https://stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf .
2. N. Chair, “The effective resistance of the N-cycle graph with four nearest neighbors,” arXiv:1401.5628v1, 22 January 2014. https://arxiv.org/pdf/1401.5628 .
3. H. Zhang and Y. Yang, “Resistance distance and Kirchhoff index in circulant graphs,” *International Journal of Quantum Chemistry* **107** (2007), 330–339; first published 5 September 2006. https://doi.org/10.1002/qua.21068 .
