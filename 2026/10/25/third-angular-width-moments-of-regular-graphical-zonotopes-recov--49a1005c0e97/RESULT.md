# Third angular-width moments of regular graphical zonotopes recover graph triangles

## Finding
Let \(G\) be any finite connected simple graph on \(n\ge3\) vertices. Its centered graphical zonotope is
\[
 Z_G=\sum_{\{i,j\}\in E(G)}[-(e_i-e_j)/2,(e_i-e_j)/2]\subset\mathbf1^\perp.
\]
With \(U\) uniformly distributed on the unit sphere of \(\mathbf1^\perp\), define the intrinsic directional width
\[
 W_G=\sum_{\{i,j\}\in E(G)}|U_i-U_j|.
\]
Write \(m=|E(G)|\), \(w=\sum_{v}\binom{d_v}{2}\), \(s=\sum_v\binom{d_v}{3}\), \(t\) for the number of triangles, and
\[
 p=\sum_{\{u,v\}\in E(G)}(d_u-1)(d_v-1)-3t
\]
for the number of (unoriented) simple three-edge paths.

Let \(a=\sqrt{2/\pi}\), \(b=1/6+\sqrt3/\pi\), and \(c=b-a^2\). Put
\[
 F_P=(2/\pi)^{3/2}\left[1/\sqrt2+\arcsin(1/\sqrt3)-\frac14\arcsin(1/3)\right],
\]
\[
 F_S=(2/\pi)^{3/2}\left[1/\sqrt2+\frac94\arcsin(1/3)\right],\qquad F_T=3a/4,
\]
\[
 k_1=-a+2a^3,\quad k_2=a(1/4-2c),
\]
\[
 k_P=F_P-2ab+a^3,\quad k_S=F_S-3ab+2a^3,\quad k_T=F_T-3ab+2a^3.
\]
Then the **complete third-moment motif formula** is
\[
 \boxed{\mathbb E W_G^3=\frac{\Gamma((n-1)/2)}{\Gamma((n+2)/2)}\left[(ma)^3+3(ma)\{m(1-a^2)+2wc\}+mk_1+6wk_2+6(pk_P+sk_S+tk_T)\right].}
\]

In particular, for any two connected \(d\)-regular simple graphs \(G_1,G_2\) on the same \(n\) vertices, their first and second intrinsic width moments are equal, while
\[
 \boxed{\mathbb E W_{G_1}^3-\mathbb E W_{G_2}^3=6\delta\frac{\Gamma((n-1)/2)}{\Gamma((n+2)/2)}[t(G_1)-t(G_2)],}
\]
where \(\delta=k_T-3k_P=-0.076857861574849\ldots<0\). Consequently the third angular-width moment **strictly identifies the triangle count** within the class of connected regular graphs of a fixed order and degree. For example, \(K_{3,3}\) and the triangular prism have equal first and second width moments, yet the prism has a strictly smaller third moment.

## Assumptions and scope
The graph is finite, undirected, simple and connected, \(n\ge3\); regularity is needed only for the final triangle-recovery assertion. All edges have unit weights. Widths refer to intrinsic Euclidean directions in the \((n-1)\)-dimensional hyperplane, not coordinate directions in ambient \(\mathbb R^n\). Triangle counts are counts of unordered vertex triples inducing all three edges. The displayed formula is exact for **every** connected simple graph; no unproved limit passage or finite-order restriction is involved.

## Proof
**Gaussian-to-spherical normalization.** Let \(g_1,\ldots,g_n\) be independent standard Gaussians; set \(S=\sum_{\{i,j\}\in E}|g_i-g_j|/\sqrt2\). Orthogonally project \(g\) into \(\mathbf1^\perp\). Its length \(R\) is independent of its direction \(U\), \(R\sim\chi_{n-1}\), and \(S=RW_G/\sqrt2\). Therefore
\[
 \mathbb E W_G^3=\frac{\Gamma((n-1)/2)}{\Gamma((n+2)/2)}\mathbb E S^3,
\]
using \(\mathbb E R^3=2^{3/2}\Gamma((n+2)/2)/\Gamma((n-1)/2)\).

**One- and two-edge moments.** For a standardized difference \(X=|g_i-g_j|/\sqrt2\), \(\mathbb EX=a\), \(\mathbb EX^2=1\), \(\mathbb EX^3=2a\). Two edge differences are independent if their edges are vertex-disjoint; if the edges meet, their Gaussian correlation has magnitude \(1/2\). The centered bivariate-normal absolute-product formula gives \(\mathbb E XY=b\) in that case. Thus
\[
 \mathbb ES=ma,\qquad\operatorname{Var}(S)=m(1-a^2)+2wc.
\]
For a repeated variable and an adjacent edge variable, Gaussian conditioning gives \(\mathbb E X^2Y=a(1+1/4)\). Their mixed third cumulant is \(a(1/4-2c)=k_2\). The single-variable third cumulant is \(2a-3a+2a^3=k_1\).

**Distinct triples and exhaustive motif classification.** A joint cumulant vanishes whenever its three edge variables split into independent nonempty blocks. Accordingly, only three graph-theoretic three-edge motifs contribute: a three-edge path \(P_4\), a three-edge star \(K_{1,3}\), or a triangle \(C_3\). For the path, a suitable sign choice for standardized Gaussian differences gives correlation matrix with upper off-diagonals \((1/2,0,1/2)\); the star gives all off-diagonal correlations \(1/2\); the triangle gives the singular signed \((1/2,1/2,-1/2)\) matrix. Applying the trivariate centered-normal absolute-product integral, or its continuous singular limit, gives respectively the explicitly stated \(F_P,F_S,F_T\). For the path, two adjacent pairs have product moment \(b\) and the disjoint pair \(a^2\), hence third cumulant \(k_P=F_P-2ab+a^3\). The star and triangle have three adjacent pairs, hence \(k_S=F_S-3ab+2a^3\) and \(k_T=F_T-3ab+2a^3\). A simple path is uniquely determined by its middle edge and choices of one other incident edge at each endpoint, with three overcounts for every triangle; therefore \(p=\sum_{uv\in E}(d_u-1)(d_v-1)-3t\). The counts of stars and incident-edge pairs are respectively \(s\) and \(w\). In the ordered third cumulant expansion, each repeated-pair pattern has multiplicity six and each distinct three-edge set also multiplicity six. Therefore
\[
 \kappa_3(S)=mk_1+6wk_2+6(pk_P+sk_S+tk_T).
\]
The identity \(\mathbb ES^3=(\mathbb ES)^3+3(\mathbb ES)\operatorname{Var}S+\kappa_3(S)\) proves the boxed general formula.

**Regularity and sharp sign.** For \(d\)-regular graphs, \(m=nd/2\), \(w=n\binom d2\), \(s=n\binom d3\) and \(p=m(d-1)^2-3t\). All third-moment terms other than \(6t(k_T-3k_P)\) are consequently fixed by \(n,d\). The first two moments also depend only on \(m,w,n\), from the formulas above and the first two chi moments.

To prove \(\delta<0\) without relying on decimals, elementary simplification gives
\[
 \frac\delta a=\frac54+\frac{3\sqrt3-2-3\sqrt2-6\arcsin(1/\sqrt3)+(3/2)\arcsin(1/3)}\pi.
\]
Because \(\arcsin x>x\) for \(0<x<1\), while \(\arcsin x<x/\sqrt{1-x^2}\), it follows that
\[
 \frac\delta a<\frac{5\pi/4+\sqrt3-2-21/(4\sqrt2)}\pi<0.
\]
For the last strict inequality, use rational upper bounds \(\pi<22/7\), \(\sqrt3<97/56\), \(\sqrt2<99/70\). They bound the numerator by \(-95/1848\). Since \(a>0\), the claimed strict sign and injectivity follow.

## Verification
The self-contained Python checker `width_moment_checker.py` requires Python, NumPy and NetworkX and can be run with `python width_moment_checker.py`. It independently enumerates every connected unlabeled simple graph on \(3\) through \(6\) vertices (141 total), compares the closed motif census with a direct edge-by-edge trivariate Gaussian integration, checks a nonisomorphic regular-graph witness (triangular prism versus \(K_{3,3}\)), and performs a fixed-seed Gaussian Monte Carlo sanity check. Reported output: `VERIFY_OK connected_graphs= 141 delta= -0.076857861575 prism_minus_K33_exact= -0.922294338898 simulation= -1.0267011`. Numerical checks corroborate but are not substitutes for the all-graph cumulant proof or the explicit rational sign certificate.

## Relationship to prior work
The graphical-zonotope construction and graph-deformation framework are established in Padrol, Pilaud and Poullot [1], whose work also relates triangles to graph-theoretic deformation properties but does not establish this moment identity. General conversion between Gaussian homogeneous functionals and spherical mean-width moments is established in Kabluchko, Litvak and Zaporozhets [2]; their article calculates higher width moments of several regular polytopes, but does not give the graph-motif triangle recovery above. The necessary multivariate Gaussian absolute moments originate with Nabeya [3]. Existing width-variance formulas distinguish some graph degree sequences using only two-edge incidence counts; they cannot separate two fixed-order, fixed-degree regular graphs by triangle count. The new contribution is the **three-edge motif expansion, exact third-moment formula, and strictly invertible regular-graph triangle coefficient**, not the earlier Gaussian identities or basic zonotope definitions.

## Limitations
The exact triangle-recovery conclusion requires a common regular degree and graph order; for irregular graphs, degree-distribution and three-edge-path counts also influence the third moment. The results concern unit-weight graphical zonotopes and Euclidean angular width, not arbitrary weighted graph zonotopes or unrelated geometric moments. This is an analytical mathematical claim accompanied by finite diagnostic checks, not independently validated. Equivalent formulations in earlier literature on Gaussian graph total variation or third absolute moments cannot be categorically excluded solely by searches.

## References
1. A. Padrol, V. Pilaud and G. Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422v1 (24 November 2021), https://arxiv.org/abs/2111.12422.
2. Z. Kabluchko, A. Litvak and D. Zaporozhets, *Mean Width of Regular Polytopes and Expected Maxima of Correlated Gaussian Variables*, arXiv:1511.08479 (2015), https://arxiv.org/abs/1511.08479.
3. S. Nabeya, *Absolute Moments in 3-Dimensional Normal Distribution*, *Annals of the Institute of Statistical Mathematics* (1952), https://projecteuclid.org/journals/annals-of-the-institute-of-statistical-mathematics/volume-4/issue-1/Absolute-Moments-in-3-dimensional-Normal-Distribution/10.1007/BF02949720.full.
