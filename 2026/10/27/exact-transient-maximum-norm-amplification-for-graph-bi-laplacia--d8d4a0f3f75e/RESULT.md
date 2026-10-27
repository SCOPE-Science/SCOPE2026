# Exact transient maximum-norm amplification for graph bi-Laplacians on triangle-free strongly regular graphs

## Finding
Let \(G\) be any finite connected noncomplete triangle-free strongly regular graph with parameters \((v,k,0,\mu)\), where \(k\ge2\) and \(1\le\mu<k\). Let \(L=kI-A\) be the unnormalized combinatorial Laplacian and \(T(t)=\exp(-tL^2)\) on counting-measure \(\ell^\infty(V(G))\), for \(t\ge0\). Define
\[
\delta=\sqrt{\mu^2+4(k-\mu)},\quad r=(-\mu+\delta)/2,\quad s=(-\mu-\delta)/2,\quad a=(k-r)^2,\quad b=(k-s)^2,
\]
\[
h(t)=\frac{(k-s)e^{-at}-(k-r)e^{-bt}}{\delta}.
\]
Then \(0<a<b\), and the **sharp norm at every time** is
\[
\boxed{\|T(t)\|_{\ell^\infty\to\ell^\infty}=1+\frac{2(v-k-1)}v\max\{h(t)-1,0\}.}
\]
The norm is attained by signed-coordinate input vectors for every \(t\). There is a unique peak time
\[
\boxed{t_{\mathrm{peak}}=\frac{1}{b-a}\log\frac{(k-r)b}{(k-s)a}>0,}
\]
and a unique later positive threshold \(t_*>t_{\mathrm{peak}}\), determined by \(h(t_*)=1\). For \(0<t<t_*\), the norm is strictly greater than one; for \(t\ge t_*\), it equals one. At every \(t>t_*\), the matrix \(T(t)\) is entrywise strictly positive, whereas for \(0<t<t_*\) its nonedge entries are strictly negative and all its other entries are positive. At \(t=t_*\), exactly the nonedge entries vanish.

The peak norm is exactly \(1+\tfrac{2(v-k-1)}v[h(t_{\mathrm{peak}})-1]\). The short-time right derivative has the *degree-only* universal value
\[
\boxed{\left.\frac{d}{dt}\right|_{t=0+}\|T(t)\|_{\ell^\infty\to\ell^\infty}=2k(k-1),}
\]
independent of \(\mu\). The theorem includes the pentagon, Petersen graph, and Clebsch graph but deliberately excludes complete bipartite graphs (the \(\mu=k\) endpoint).

## Assumptions and scope
A strongly regular graph with parameters \((v,k,0,\mu)\) is a simple \(k\)-regular graph in which adjacent vertices have zero common neighbors and nonadjacent distinct vertices have \(\mu\) common neighbors. We assume \(1\le\mu<k\), so \(G\) is connected, noncomplete, nonbipartite, and has \(v=1+k+k(k-1)/\mu\). The operator acts on finite-dimensional real or complex coordinate spaces with counting measure. The matrix \(L^2\) is the square of the unnormalized Laplacian; the theorem does **not** concern \(e^{-tL}\) or normalized graph Laplacians. \(t_*\) is defined uniquely by a scalar equation and is not asserted to be an elementary expression.

## Proof
Write \(A\) for the adjacency matrix and \(J\) for the all-ones matrix. Counting length-two walks gives the exact identity
\[
A^2=(k-\mu)I-\mu A+\mu J.
\]
On the orthocomplement of the constant vector, adjacency eigenvalues must solve \(x^2+\mu x-(k-\mu)=0\), hence are \(r>0\) and \(s<0\), with \(\delta=r-s>0\). On constants, \(A=kI\) and \(L=0\). Therefore the spectral calculus on the three-dimensional adjacency algebra gives
\[
T(t)=\alpha(t)I+\beta(t)A+\gamma(t)J,
\]
\[
\alpha(t)=\frac{r e^{-bt}-s e^{-at}}\delta,\qquad
\beta(t)=\frac{e^{-at}-e^{-bt}}\delta,\qquad
\gamma(t)=\frac{1-\alpha(t)-k\beta(t)}v.
\]
Indeed the coefficients reproduce the eigenvalues \(1,e^{-at},e^{-bt}\) on the three eigenspaces, respectively. Since \(a<b\), \(\beta(t)>0\) whenever \(t>0\). Also \(0<\alpha(t)<1\): its numerator is a positive combination of the two numbers in \((0,1)\), with coefficients \(r/\delta\) and \(-s/\delta\) summing to one. The entries corresponding to neighboring vertices are
\[
\beta+\gamma=\frac{1-\alpha+(v-k)\beta}{v}>0.
\]
Every diagonal entry is strictly positive because \(T(t)\) is positive definite for every finite \(t\), its eigenvalues being strictly positive. The remaining entries, precisely those indexed by nonadjacent distinct vertices, all equal \(\gamma=(1-h)/v\), where \(h=\alpha+k\beta\) simplifies to the displayed function.

The rows of \(T(t)\) sum to one, since \(T(t)\mathbf 1=\mathbf1\). There are exactly \(v-k-1\) nonneighbors in each row. Therefore the absolute row sum equals one plus twice the total magnitude of negative entries, giving
\[
\sum_{y}|T(t)_{xy}|=1+2(v-k-1)\max\{-\gamma(t),0\}
=1+\frac{2(v-k-1)}v\max\{h(t)-1,0\}.
\]
This is independent of \(x\). Choosing \(f(y)=\mathrm{sgn}(T(t)_{xy})\) (an arbitrary sign at zero entries) attains the row sum, proving both sharpness and the formula for real and complex \(\ell^\infty\).

To determine the temporal profile, observe that \(h(0)=1\), \(\lim_{t\to\infty}h(t)=0\), and
\[
h'(t)=\frac{-(k-s)a e^{-at}+(k-r)b e^{-bt}}\delta.
\]
At time zero, the nonedge entries of \(-L^2\) equal \(-\mu\), by the two-walk identity: for nonadjacent vertices, \((L^2)_{xy}=(A^2)_{xy}=\mu\). Differentiating \(\gamma=(1-h)/v\) at zero yields \(h'(0)=v\mu>0\). Consequently the ratio \((k-r)b/((k-s)a)\) exceeds one. Dividing \(h'(t)\) by the positive factor \((k-s)a e^{-at}/\delta\) shows that its sign is the sign of \((k-r)b e^{-(b-a)t}/((k-s)a)-1\), a strictly decreasing function. Thus \(h\) increases strictly on \([0,t_{\mathrm{peak}}]\), decreases strictly afterward, and has the displayed unique peak. Since \(h(0)=1\), \(h(t_{\mathrm{peak}})>1\), and \(h(t)\to0\), continuity and strict decrease give exactly one \(t_*>t_{\mathrm{peak}}\) with \(h(t_*)=1\). This also establishes every asserted sign/positivity regime, attainment, and unique norm maximum.

Finally \(v-k-1=k(k-1)/\mu\) from the strongly regular vertex count. Differentiating the positive branch of the norm formula at \(t=0+\) gives
\[
\frac{2(v-k-1)}v h'(0)=2(v-k-1)\mu=2k(k-1),
\]
proving the universal initial slope. Nothing in this argument relies on finite numerical sampling.

## Verification
The included standalone `verify.py` uses only the Python standard library. Run `python verify.py` in the extracted files. It generates the cycle on five vertices, Petersen graph, and Clebsch graph; confirms all relevant adjacency-algebra identities exactly over integers, checks the graph-specific bi-Laplacian nonedge coefficients and degree-only short-time slope, and separately reconstructs the heat matrix at selected times from its eigenspace projectors. It reports 7,190 finite algebraic/numerical assertions passing. Decimal floating comparisons are explicitly restricted to finite examples and do not prove the general theorem; the analytical argument above supplies the all-graph proof.

## Relationship to prior work
The work of Keller and Lenz supplies the graph-Laplacian and heat-semigroup context, while Daners, Glück, and Kennedy develop general eventual positivity and discuss bi-Laplacians. A published general three-spectral-value result, *A three-spectral-value barrier for gaps in positivity times of self-adjoint semigroups*, already covers the **shape** of the positive-time set under a much broader spectral hypothesis. Hence the fact that there is only one positivity cutoff is **not** asserted to be novel by itself. The present result instead determines every sharp maximum-coordinate norm, the exact peak position and height, the sign pattern of all matrix entries, and the universal degree-only initial amplification coefficient for the particular family of triangle-free strongly regular graphs. Earlier complete multipartite and complete bipartite graph calculations concern different (or excluded) parameter classes. The general three-spectrum record was available as a scientific abstract/summary but its full text was not accessible for inspection; this limitation is relevant to final priority assessment.

## Limitations
The claim requires \(\mu<k\) and \(\lambda=0\): it does not cover all strongly regular graphs, arbitrary positive graph weights, or continuum bi-Laplacians. The positivity threshold is given implicitly; the result does not establish a new abstract three-spectral-level positivity theorem. Full historical novelty of the sharp norm formula remains subject to independent bibliographic verification; a matching specialized calculation under alternate terminology is possible. Independent mathematical review has not been performed.

## References
1. M. Keller and D. Lenz, *Unbounded Laplacians on Graphs: Basic Spectral Properties and the Heat Equation*, Mathematical Modelling of Natural Phenomena 5 (2010), 198–224, doi:10.1051/mmnp/20105409; arXiv:1101.2979.
2. D. Daners, J. Glück, and J. B. Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices*, first arXiv version 17 November 2015, arXiv:1511.05294, later J. Differential Equations 261 (2016), 2607–2649. Particularly the introduction and finite-dimensional analysis in Section 9.
3. *A three-spectral-value barrier for gaps in positivity times of self-adjoint semigroups*, published mathematical record (2026), identifier `da21753d4271`; the available record explicitly treats the positive-time-set shape for general three-spectral-value operators.
