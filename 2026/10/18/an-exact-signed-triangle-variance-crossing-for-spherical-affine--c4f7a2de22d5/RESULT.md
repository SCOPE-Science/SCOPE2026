# An exact signed-triangle variance crossing for spherical affine-link graphs

## Finding
For integers \(n\ge3\), \(d\ge2\), real \(0<p<1\), and \(0<\delta<\min\{p,1-p\}\), let \(X_1,\dots,X_n\) be independent uniform unit vectors in \(\mathbb R^d\). Conditional on them, independent edges \(A_{ij}\in\{0,1\}\) have probabilities \(p+\delta\langle X_i,X_j\rangle\). Define the signed triangle statistic \(T_n=\sum_{i<j<k}(A_{ij}-p)(A_{ik}-p)(A_{jk}-p)\). Put \(s=p(1-p)\), \(c=1-2p\), and let \(T_n^{\mathrm{ER}}\) be the same statistic on independent Bernoulli-\(p\) edges. Then
\[
\mathbb E T_n=\binom n3\frac{\delta^3}{d^2},\qquad \operatorname{Var}(T_n^{\mathrm{ER}})=\binom n3 s^3,
\]
\[
\operatorname{Var}(T_n)=\binom n3\left(s^3+\frac{c^3\delta^3}{d^2}-\frac{\delta^6}{d^4}\right)+12\binom n4\left(\frac{s\delta^4}{d^3}-\frac{\delta^6}{d^4}\right).
\]
In particular the **variance-ordering difference** is exactly
\[
\operatorname{Var}(T_n)-\operatorname{Var}(T_n^{\mathrm{ER}})
=\binom n3\frac{\delta^3}{d^4}\Phi_n,\quad
\Phi_n=(1-2p)^3d^2+3(n-3)s\delta d-(3n-8)\delta^3.
\]
Moreover \(\Phi_{n+1}-\Phi_n=3\delta(sd-\delta^2)>0\). Hence the variance ordering reverses **at most once**, from the geometric graph having smaller variance to having larger variance, and every fixed parameter triple eventually has strictly larger geometric variance. The boundary is exactly the unique real crossing \(n_*=3+[\delta^3-(1-2p)^3d^2]/[3\delta(sd-\delta^2)]\); for each integer \(n\ge3\) the sign is that of \(n-n_*\). A concrete nondegenerate reversal is \(p=3/4\), \(\delta=1/8\), \(d=2\): \(\Phi_6=-25/256\) and \(\Phi_7=19/512\), so the geometric variance is smaller through six vertices and larger from seven vertices onwards.

## Assumptions and scope
All vectors are i.i.d. uniform on the Euclidean unit sphere, and conditional edges are independent. The strict inequality for \(\delta\) ensures that the conditional probabilities are strictly between zero and one. The Erdős–Rényi comparison uses the same marginal edge probability \(p\), not the same joint edge law. Binomial coefficients with top smaller than bottom are zero. The theorem holds for every finite \(n\ge3\), every integer dimension \(d\ge2\), and every specified admissible \(p,\delta\). The threshold describes variance of the **centered-edge product**, not variance of the uncentered triangle count.

## Proof
Put \(u_{ij}=\langle X_i,X_j\rangle\), \(Y_{ij}=A_{ij}-p\), and \(Z_{ijk}=Y_{ij}Y_{ik}Y_{jk}\). Conditional independence gives \(\mathbb E[Y_{ij}\mid X]=\delta u_{ij}\) and \(\mathbb E[Y_{ij}^2\mid X]=s+c\delta u_{ij}\). Rotational invariance gives \(\mathbb E X_i=0\), \(\mathbb E X_iX_i^{\mathsf T}=I_d/d\), and \(\mathbb E[u_{12}u_{23}u_{31}]=d^{-2}\). Consequently \(\mathbb E Z_{123}=\delta^3/d^2\).

In the expansion of \(\mathbb E[Z_{123}^2]\), all products of one or two distinct inner products vanish by conditioning on a vertex occurring only once; the cubic product has expectation \(d^{-2}\). Thus \(\mathbb E Z_{123}^2=s^3+c^3\delta^3/d^2\) and its variance is \(s^3+c^3\delta^3/d^2-\delta^6/d^4\).

For triangles \(123\) and \(124\), condition on \(X_1,X_2,Y_{12}\). Their remaining edges use disjoint randomness, and the conditional mean of each triangle is \(Y_{12}\delta^2u_{12}/d\). Therefore \(\mathbb E[Z_{123}Z_{124}]=\delta^4d^{-2}\mathbb E[Y_{12}^2u_{12}^2]\). Since \(\mathbb E u_{12}^2=1/d\), \(\mathbb E u_{12}^3=0\), this is \(s\delta^4/d^3\), giving covariance \(s\delta^4/d^3-\delta^6/d^4\). Disjoint triangles are independent; triangles sharing one vertex have zero covariance because conditional on their shared latent vector their data are independent and their conditional means are the same constant \(\delta^3/d^2\) by rotation invariance. There are \(\binom n3\) diagonal terms and \(12\binom n4\) ordered pairs of distinct triangles sharing one edge. Summing proves the displayed variance formula.

For independent Bernoulli edges, the diagonal variance is \(s^3\) and cross terms vanish because any distinct pair of triangles contains an edge that occurs exactly once and has centered expectation zero. Subtraction and \(12\binom n4/\binom n3=3(n-3)\) yield \(\Phi_n\). Its slope is strictly positive because \(d\ge2\) and \(\delta^2<\min\{p,1-p\}^2\le s<sd\). The positive slope implies the unique real root formula and the all-integer sign classification. Substituting the rational example yields the exact values indicated.

## Verification
A self-contained Python rational checker `verify.py` computes the formulas and independently enumerates uniform signed-coordinate latent vectors \(\{\pm e_1,\pm e_2\}\) in two dimensions. That finite distribution has the exact first-, second-, and odd-order tensor moments required in this proof, so for three and four vertices the checker matches the full model's first and second signed-triangle moments without Monte Carlo. The checker also verifies the exact slope and the six-to-seven sign change using rational arithmetic. Run `python verify.py` with Python 3.9 or later.

## Relationship to prior work
Huang and Li, *Detecting Random Geometric Graphs with General Kernel*, arXiv:2610.12765v1 (public 2026-10-08), analyze the same random-geometry-versus-Erdős–Rényi detection model. Their proof of the signed-triangle test bounds variance using diagonal terms and shared-edge covariance, but does not provide the present exact affine-link variance or the sample-size reversal classification. Mao, Wu and Xu, *Random geometric graphs with smooth kernels: sharp detection threshold and a spectral conjecture*, arXiv:2602.14998v1 (public 2026-02-16), derive a general signed-triangle mean and variance **bound**, and explicitly separate overlaps by shared vertices/edges. The present exact finite-parameter comparison is obtained by calculating all overlap contributions in the affine kernel, not by treating the cited upper bounds as equalities. All general signed-triangle methods and the underlying geometric graph model belong to this earlier literature.

## Limitations
This is an exact finite-sample variance classification for the affine spherical link only. It does not establish optimality of testing statistics, a central limit theorem, total variation detection thresholds, or analogous results for nonlinear kernels. This is not a claim of independent priority verification: a more general exact covariance theorem not identified in the comparisons could imply the formula, and the proof uses familiar conditioning and spherical-moment methods.

## References
1. Dong Huang and Shuangping Li, *Detecting Random Geometric Graphs with General Kernel*, arXiv:2610.12765v1, posted 2026-10-08, https://arxiv.org/abs/2610.12765.
2. Cheng Mao, Yihong Wu and Jiaming Xu, *Random geometric graphs with smooth kernels: sharp detection threshold and a spectral conjecture*, arXiv:2602.14998v1, posted 2026-02-16, https://arxiv.org/abs/2602.14998.
