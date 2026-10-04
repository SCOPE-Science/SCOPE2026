# Exact sign-aware graph-specific tuning for homogeneous distributed gradient tracking

## Finding
For homogeneous scalar quadratic local costs, the exact constant-step tuning of the source distributed gradient-tracking dynamics depends only on the largest positive and most-negative nontrivial consensus eigenvalues, but it depends on their signs asymmetrically. Write
\[
p=\max\{\lambda_2,0\},\qquad n=\max\{-\lambda_N,0\}.
\]
Then the unique optimal normalized common stepsize is
\[
\beta_*=1-r_*,\qquad
r_*=\max\left\{\sqrt p,\frac{\sqrt{n(4+5n)}-n}2\right\}.
\]
The attained asymptotic factor is exactly \(r_*\). In particular, a negative spectral endpoint of magnitude \(n\) contributes the smaller obstruction \((\sqrt{n(4+5n)}-n)/2\), not \(\sqrt n\).

## Assumptions and scope
Let \(W\) be a connected symmetric doubly stochastic consensus matrix with eigenvalues \(1=\lambda_1>\lambda_2\ge\cdots\ge\lambda_N>-1\). Each local cost is a scalar quadratic with the same curvature \(\bar h>0\). The common physical stepsize is \(\alpha>0\), and \(\beta=\alpha\bar h\) is the normalized stepsize. The statement concerns the exact-arithmetic linear dynamics and asymptotic spectral radius of the homogeneous reduced system \(A_0(\beta)\).

The MSC2020 code \(65K05\) is used because the claim is an exact numerical mathematical-programming parameter design for an iterative optimization method; MSC2020 describes \(65K05\) as numerical mathematical programming methods.

## Proof
The source diagonalizes the homogeneous-curvature dynamics and factors the characteristic polynomial as
\[
\det(zI-A_0(\beta))=(z-1+\beta)\prod_{i=2}^N P_{\lambda_i}(z;\beta),
\qquad
P_\lambda(z;\beta)=(z-\lambda)^2+\beta\lambda(z-1).
\]
For fixed \(0<\beta<2\), the source proves that the modal root radius decreases with \(\lambda\) on the negative interval and increases with \(\lambda\) on the positive interval. Hence the exact spectral radius over the *actual* finite spectrum is
\[
\rho(A_0(\beta))=
\max\{|1-\beta|,R_+(\beta,p),R_-(\beta,n)\},
\]
where a missing-sign branch is interpreted as zero and
\[
R_+(\beta,p)=\frac{p(2-\beta)+\sqrt{\beta p\,[4(1-p)+\beta p]}}2,
\qquad
R_-(\beta,n)=\sqrt{n(n+\beta)}.
\]
For \(0<\beta\le1\), \(1-\beta\) is strictly decreasing while every nonzero endpoint term is strictly increasing. At \(\beta\downarrow0\), both endpoint terms are below \(1-\beta\). Therefore the unique minimizer is the first intersection of \(1-\beta\) with either endpoint branch.

For the positive branch, substituting \(z=1-\beta\) in \(P_p\) yields the source intersection
\[
\beta_+=1-\sqrt p,
\qquad 1-\beta_+=\sqrt p.
\]
For the negative branch, solve
\[
(1-\beta)^2=n(n+\beta).
\]
The root in \((0,1]\) is
\[
\beta_-=1+\frac n2-\frac12\sqrt{n(4+5n)},
\]
so
\[
1-\beta_-=\frac{\sqrt{n(4+5n)}-n}2.
\]
Consequently \(\beta_*=\min\{\beta_+,\beta_-\}\), which is the stated formula. For \(1<\beta<2\), the endpoint radii are increasing, and for \(\beta\ge2\), \(|1-\beta|\ge1\); neither range can improve the minimum. Uniqueness follows from the strict monotonicity of the active crossing, including the complete-graph limit \(p=n=0\), where \(\rho(A_0(\beta))=|1-\beta|\) and \(\beta_*=1\).

Finally, for \(0<n<1\),
\[
\frac{\sqrt{n(4+5n)}-n}2<\sqrt n,
\]
because after dividing by \(\sqrt n\) and rearranging, the inequality is equivalent to \(n<1\). Thus a negative-dominant graph can be tuned strictly faster than the sign-blind \(\sqrt n\) surrogate suggests.

## Verification
The bundled `verify_sign_aware_dgt.py` independently constructs the roots of \(P_\lambda\), checks the closed-form optimizer against dense one-dimensional minimization over hundreds of \((p,n)\) pairs, verifies the branch-intersection identities, and checks a negative-only two-agent example. The script is supplementary; the proof above is algebraic and does not depend on floating-point experiments.

A concrete negative-only example is
\[
W=\begin{pmatrix}0.2&0.8\0.8&0.2\end{pmatrix},
\]
whose nontrivial eigenvalue is \(-0.6\). Here \(p=0\), \(n=0.6\), the exact optimizer is approximately \(0.2753049234\), and the exact optimal factor is approximately \(0.7246950766\). The sign-blind prescription \(1-\sqrt{0.6}\approx0.2254033308\) instead has factor \(\sqrt{0.6}\approx0.7745966692\).

## Relationship to prior work
Wang et al., arXiv:2608.03548v1, derive the homogeneous factorization, prove the endpoint monotonicity, and solve the closed-form regime under \(\lambda_2\ge|\lambda_N|\), obtaining \(\beta_*=1-\sqrt\sigma\). They explicitly note that the exact graph-specific optimizer may depend on the full spectrum and use a sign-blind essential spectral radius \(\sigma\) for their certified surrogate. The present result keeps their exact homogeneous modal factors but minimizes them over the actual signed spectral endpoints, producing the negative-endpoint branch and the exact switching condition.

Tian, Chai, and Xu, arXiv:2607.23601v1, derive exact *worst-case* rates for DIGing and AugDGM over function/network classes parameterized by a connectivity magnitude. Their accessible abstract and detailed public review describe a \(\sigma\)-parameterized worst-case problem rather than this fixed-graph signed-endpoint formula. Their arXiv full text could not be retrieved during this check, so this remains a residual comparison risk.

Tian, Chai, and Xu, arXiv:2607.25463v1, optimize parameters for DIGing on unweighted least squares by graph-frequency decomposition. That paper concerns DIGing rather than the adapt-then-combine DGT dynamics analyzed here. Nedić et al., arXiv:1609.05877v1, establish geometric convergence for ATC-DIGing with uncoordinated stepsizes but do not, in the inspected abstract, state this signed-endpoint optimizer.

Targeted semantic searches in published-finding corpus and general literature searches for ATC-DIGing/AugDGM, homogeneous quadratics, negative consensus eigenvalues, signed spectral endpoints, and the closed form \(\sqrt{n(4+5n)}\) found no implication-equivalent statement.

## Limitations
The theorem is restricted to uniform scalar curvatures and a common constant stepsize. It does not cover curvature heterogeneity, time-varying graphs, directed/non-symmetric mixing, vector-valued local quadratics with noncommuting Hessians, or uncoordinated steps. The originality check could not inspect the full text of arXiv:2607.23601 or arXiv:2607.25463 during this run; their abstracts and an accessible technical review were checked, so an equivalent formula hidden in inaccessible full text remains a stated risk. Search non-retrieval is not treated as proof of priority.

## References
1. Y. Wang, L. Ballotta, R. Carli, A. Iannelli, X. Cao, and L. Schenato, “Adaptive Stepsizes With Certified Convergence in Distributed Gradient Tracking With Quadratic Costs,” arXiv:2608.03548v1, 4 August 2026.
2. Q. Tian, L. Chai, and J. Xu, “Exact Worst-case Convergence Rates of Distributed Gradient Tracking Methods,” arXiv:2607.23601v1, 26 July 2026.
3. Q. Tian, L. Chai, and J. Xu, “Optimal Parameter Design for DIGing on Minimizing Unweighted Sum of Squares,” arXiv:2607.25463v1, 28 July 2026.
4. A. Nedić, A. Olshevsky, W. Shi, and C. A. Uribe, “Geometrically Convergent Distributed Optimization with Uncoordinated Step-Sizes,” arXiv:1609.05877v1, 19 September 2016.
5. MSC2020 database, \(65K05\): numerical mathematical programming methods.
