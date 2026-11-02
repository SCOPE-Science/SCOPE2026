# Sharp heat-gradient amplification on balanced double stars

## Finding

For each integer \(m\ge 1\), let \(T_m\) be the unweighted tree with two adjacent hub vertices \(u,v\), each having precisely \(m\) pendant leaves. Thus \(T_m\) has \(2m+2\) vertices and graph diameter three. Let \(L=D-A\) be its combinatorial Laplacian, \(H_t=e^{-tL}\) its heat semigroup for every real \(t\ge0\), and \(\|f\|_{\mathrm{Lip}}=\max_{xy\in E(T_m)}|f(x)-f(y)|\).

Put
\[
\alpha_m=\frac{m+3-\sqrt{(m+3)^2-8}}2,\qquad
\beta_m=\frac{m+3+\sqrt{(m+3)^2-8}}2.
\]
Then the **exact attained seminorm operator modulus**, with constants factored out, is
\[
\boxed{\Lambda_m(t):=\sup_{\|f\|_{\mathrm{Lip}}>0}\frac{\|H_t f\|_{\mathrm{Lip}}}{\|f\|_{\mathrm{Lip}}}
=\frac{(\beta_m+2m-2)e^{-\alpha_m t}-(\alpha_m+2m-2)e^{-\beta_m t}}{\beta_m-\alpha_m}.}
\]
For \(t>0\), all nonconstant extremizers, up to addition of a constant and multiplication by a nonzero real scalar, are the single vertex pattern taking values \(2\) on all leaves at \(u\), \(1\) at \(u\), \(0\) at \(v\), and \(-1\) on all leaves at \(v\). In particular, the hub-to-hub edge is the unique norm-controlling edge orbit at every positive time.

For \(m=1\), \(\Lambda_1(t)<1\) at every \(t>0\). For every \(m\ge2\), \(\Lambda_m\) initially increases above one, has a unique global positive-time maximum at
\[
\boxed{t_m^*=\frac{1}{\beta_m-\alpha_m}\log\frac{\beta_m(\alpha_m+2m-2)}{\alpha_m(\beta_m+2m-2)},}
\]
and then tends strictly downward to zero. Over this entire family,
\[
\boxed{\sup_{m\ge1}\sup_{t\ge0}\Lambda_m(t)=3,}
\]
with no finite \(m,t\) attaining three; \(\Lambda_m(2\log(m)/m)\to3\) as \(m\to\infty\).

Equivalently, if \(p_t^x=H_t(x,\cdot)\) is the heat-kernel probability measure at vertex \(x\), then for the two hubs \(u,v\) and shortest-path Wasserstein distance, \(W_1(p_t^u,p_t^v)=\Lambda_m(t)\).

## Assumptions and scope

All vertices have counting measure, all edges have unit heat conductance and unit metric length, and the heat generator is \(L=D-A\), **not** the degree-normalized Laplacian. The integer \(m\) may be arbitrarily large but finite, and time is any real \(t\ge0\). Lipschitz seminorm zero means a constant function; the quotient is considered on functions modulo constants. At \(t=0\), the operator is the identity and every nonconstant function is an extremizer; the rigidity assertion is only for \(t>0\).

## Proof

**1. Edge gradients are independent coordinates.** Label the leaves \(u_1,\ldots,u_m\) and \(v_1,\ldots,v_m\) and orient the differences
\[
 g_i=f(u_i)-f(u),\quad h_i=f(v_i)-f(v),\quad c=f(u)-f(v),\quad G=\sum_i g_i,\quad K=\sum_i h_i.
\]
Because the underlying graph is a tree, arbitrary real values of these \(2m+1\) edge differences integrate uniquely to a vertex function up to constants. The input seminorm is therefore precisely the coordinate maximum norm. Under \(\dot f=-Lf\), direct subtraction of the vertex equations gives the exact autonomous gradient system
\[
\dot g_i=-g_i-G+c,\qquad \dot h_i=-h_i-K-c,\qquad \dot c=G-K-2c.
\]
Set \(S=G+K\) and \(D=G-K\). Then
\[
\dot S=-(m+1)S,\qquad
\begin{pmatrix}\dot D\\\dot c\end{pmatrix}
=\begin{pmatrix}-(m+1)&2m\\1&-2\end{pmatrix}
\begin{pmatrix}D\\c\end{pmatrix}.
\]
The characteristic polynomial of the negative of this two-dimensional generator is \(z^2-(m+3)z+2\); its positive roots satisfy \(0<\alpha_m<1<\beta_m\), \(\alpha_m\beta_m=2\), and \(\alpha_m+\beta_m=m+3\).

**2. Exact reduced heat coefficients.** In this proof abbreviate \(\alpha=\alpha_m\), \(\beta=\beta_m\), \(\delta=\beta-\alpha\), \(x=e^{-t}\), and \(r=e^{-(m+1)t}\). Define
\[
 b(t)=\frac{e^{-\alpha t}-e^{-\beta t}}\delta,\qquad
 a(t)=\frac{(\beta-2)e^{-\alpha t}+(2-\alpha)e^{-\beta t}}\delta,
\]
\[
 q(t)=\frac{(\beta-m-1)e^{-\alpha t}+(m+1-\alpha)e^{-\beta t}}\delta.
\]
Direct evaluation of the two-dimensional matrix exponential yields
\[
 D(t)=q(t)D(0)+2m b(t)c(0),\qquad c(t)=b(t)D(0)+a(t)c(0).
\]
For \(t>0\), \(b(t)>0\) and \(a(t)>0\), and the coefficients satisfy \(a(t)-q(t)=(m-1)b(t)\). Moreover, \(\dot q=-(m+1)q+2m b\) and \(q(0)=1\), hence
\[
 q(t)-r=2m\int_0^t e^{-(m+1)(t-s)}b(s)\,ds\ge0.
\]
(The inequality is strict for \(t>0\).)

**3. The hub gradient row.** Since the original gradients are independent, the exact induced coordinate-maximum norm is the largest absolute row sum of the gradient evolution matrix. The row for the hub edge is
\[
 c(t)=b(t)\sum_i g_i(0)-b(t)\sum_i h_i(0)+a(t)c(0).
\]
All \(2m+1\) coefficients are nonzero for \(t>0\), so its absolute row sum is
\[
 F_{\mathrm{hub}}(t)=a(t)+2m b(t)=q(t)+(3m-1)b(t).
\]
Substituting the definitions gives exactly the boxed formula for \(\Lambda_m(t)\), provided no leaf row is larger.

**4. Exact leaf row and strict comparison.** The sum and difference modes give
\[
 g_i(t)=xg_i(0)+C_G\sum_jg_j(0)+C_K\sum_jh_j(0)+b(t)c(0),
\]
where
\[
 C_G=\frac{r+q(t)-2x}{2m},\qquad C_K=\frac{r-q(t)}{2m}\le0.
\]
The coefficient of \(g_i(0)\) in its own row is
\(x+C_G=\frac{m-1}{m}x+\frac{r+q(t)}{2m}>0\). The absolute row sum of any leaf edge therefore equals
\[
 F_{\mathrm{leaf}}(t)=q(t)+b(t)+\frac{m-1}{m}\max\{0,\,2x-r-q(t)\}.
\]
We claim
\[
 2x-r-q(t)\le2m b(t)\qquad(t\ge0).
\]
To prove this, let \(w(t)=q(t)+2m b(t)\), \(z(t)=2e^{-t}-e^{-(m+1)t}\), and \(\mathcal D=\partial_t^2+(m+3)\partial_t+2\). Both \(w,z\) have initial value \(1\) and initial derivative \(m-1\). By the two-mode system, \(\mathcal D w=0\). Direct substitution gives \(\mathcal D z=-2m(e^{-t}-e^{-(m+1)t})\). The positive zero-initial-data Green kernel for \(\mathcal D\) is precisely \(b(t)\), hence
\[
 w(t)-z(t)=2m\int_0^t b(t-s)\big(e^{-s}-e^{-(m+1)s}\big)\,ds\ge0.
\]
This proves the claimed comparison. Consequently
\[
 F_{\mathrm{leaf}}(t)\le q(t)+(2m-1)b(t)
 < q(t)+(3m-1)b(t)=F_{\mathrm{hub}}(t)\quad(t>0).
\]
The strict inequality follows from \(m b(t)>0\). The other leaf row orbit has identical norm by symmetry. Thus the hub edge controls the entire operator norm at all \(t>0\); at zero every edge row has norm one.

**5. Rigidity of equality.** For positive \(t\), the controlling hub row has strictly positive coefficients on all \(g_i\) and on \(c\), and strictly negative coefficients on all \(h_i\). Equality in the coordinate-maximum norm inequality forces \(g_i=c=\sigma\) and \(h_i=-\sigma\) for the same nonzero scalar \(\sigma\). Integrating these edge differences produces exactly the displayed vertex pattern, up to a scalar and additive constant. Conversely that function attains the hub row norm; this proves sharpness and the complete classification.

**6. Phase transition and uniform sharp bound.** Write the proved norm as
\[
 \Lambda_m(t)=A_m e^{-\alpha t}-B_m e^{-\beta t},\quad
 A_m=\frac{\beta+2m-2}\delta,\quad B_m=\frac{\alpha+2m-2}\delta.
\]
Both coefficients are positive, \(A_m-B_m=1\), and \(\Lambda_m'(0)=2m-2\). If \(m=1\), the derivative is strictly negative for every positive time. If \(m\ge2\), the derivative changes sign exactly once, from positive to negative, at the displayed \(t_m^*\); since \(\Lambda_m(t)\to0\), this is its unique global maximum.

Since \(0<\alpha<1\) and \(\beta=m+3-\alpha\), one has \(3\delta-(\beta+2m-2)=8-5\alpha>0\), so \(A_m<3\) and hence \(\Lambda_m(t)<3\) for all finite \(m\) and \(t\). Finally, as \(m\to\infty\), \(\alpha\sim2/m\), \(\beta\sim m+3\), \(A_m\to3\), and \(B_m\to2\). At \(t_m=2\log(m)/m\), the first exponential tends to one and the second tends to zero, proving \(\Lambda_m(t_m)\to3\). This establishes the optimal but unattained family-wide supremum.

**7. Transport interpretation.** For each hub pair, Kantorovich--Rubinstein duality on the finite shortest-path metric identifies \(W_1(p_t^u,p_t^v)\) with the norm of the corresponding hub-gradient linear functional over unit-Lipschitz potentials. Step 3 computed that exact norm as \(\Lambda_m(t)\), with the extremizing potential from Step 5.

## Verification

The accompanying standalone program `check_bistar.py` uses the Python standard library. It directly constructs the full \((2m+1)\)-coordinate gradient generator and checks Taylor coefficients of the formulas through degree eight using exact integer/rational arithmetic for nine values of \(m\). It independently computes finite heat-kernel rows using continuous-time Markov uniformization, then evaluates the exact tree-cut formula for \(W_1\), comparing the hub and leaf edge types against the proposed formulas at 81 graph/time instances. It also checks the stated peak locations numerically for sampled values. Its verified output is:

```
CHECK_OK exact_taylor_orders=9 m_values=9 heat_row_transport_cases=81 checked_graph_families=balanced_double_stars
```

These finite tests are reproducibility checks, not a substitute for the all-parameter analytic proof in Steps 1--7. Run `python check_bistar.py` from the directory containing this document and the script.

## Relationship to prior work

Ollivier's 2007 work introduces the transport-contraction viewpoint for Markov processes. The 2017 semigroup theorem of Münch and Wojciechowski relates graph Ricci lower bounds to exponential Lipschitz estimates, but its general criterion does not supply this exact time-dependent nonexponential profile. Lu and Liu's 2012 double-starlike spectral work concerns graph determination by Laplacian spectra, not the graph-Lipschitz heat operator norm. Frank and Kovařík study heat kernels for differential operators on metric trees with one-dimensional edges; their operator and metric-measure model differ from the present finite combinatorial Laplacian. In particular, none of these inspected statements entails the explicit norm, positive-time extremizer rigidity or the limiting sharp amplification factor of three. Exact prior calculations outside the inspected and indexed literature remain possible.

## Limitations

The theorem is for the balanced, unweighted double-star family only, with combinatorial heat flow and vertexwise graph-Lipschitz seminorm. It does not establish a corresponding formula for unequal branch counts, weighted edges, degree-normalized heat flow, metric-graph differential heat flow, higher Wasserstein exponents, or arbitrary trees. Publication priority relative to unindexed work is not guaranteed.

## References

1. Yann Ollivier, *Ricci curvature of Markov chains on metric spaces*, first public arXiv posting 30 January 2007, arXiv:math/0701886, https://arxiv.org/abs/math/0701886.
2. Rupert L. Frank and Hynek Kovařík, *Heat kernels of metric trees and applications*, first public arXiv posting 31 August 2011, arXiv:1108.6145, https://arxiv.org/abs/1108.6145.
3. Pengli Lu and Xiaogang Liu, *Laplacian spectral characterization of some double starlike trees*, first public arXiv posting 28 May 2012, arXiv:1205.6027, https://arxiv.org/abs/1205.6027.
4. Florentin Münch and Radosław K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, first public arXiv posting 4 December 2017, arXiv:1712.00875, https://arxiv.org/abs/1712.00875.
