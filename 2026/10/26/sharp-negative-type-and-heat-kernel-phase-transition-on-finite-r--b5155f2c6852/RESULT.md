# Sharp negative type and heat-kernel phase transition on finite rank-two Grassmannians

## Finding

Let \(q\ge2\) be a prime power, \(n\ge4\) an integer, and \(X=\operatorname{Gr}_q(2,n)\) the set of two-dimensional linear subspaces of \(\mathbb F_q^n\). Endow \(X\) with the Grassmann-graph shortest-path metric
\[
d(U,V)=2-\dim_{\mathbb F_q}(U\cap V)\in\{0,1,2\}.
\]
Write
\[
m=\frac{q^n-1}{q-1},\qquad N=\binom{n}{2}_q=\frac{(q^n-1)(q^{n-1}-1)}{(q^2-1)(q-1)},\qquad p_*=\log_2(1+q^{-1}).
\]

**Sharp negative type and Euclidean snowflake dimension.** For every \(p>0\), the distance-power matrix \(D_p=[d(U,V)^p]_{U,V\in X}\) is conditionally negative semidefinite (CND) if and only if \(p\le p_*\). It is strictly CND (negative on every nonzero coefficient vector whose entries sum to zero) exactly when \(0<p<p_*\). At the critical exponent the centered Euclidean Gram matrix \(-\tfrac12 H D_{p_*}H\), where \(H=I-N^{-1}\mathbf1\mathbf1^\top\), has rank \(m-1\); for \(0<p<p_*\) its rank is \(N-1\). Consequently the least Euclidean dimension for an isometric embedding of the snowflaked metric \((X,d^{p/2})\), meaning squared Euclidean distances equal \(d^p\), is respectively \(m-1\) at \(p=p_*\) and \(N-1\) below it. A canonical critical embedding sends \(U\) to the normalized indicator \(h_U/\sqrt{2q}\in\mathbb R^m\) of its \(q+1\) projective points.

**Exact heat-kernel admissibility.** Given \(p>0\) and \(a\ge0\), let
\[
K_{a,p}(U,V)=\exp(-a\,d(U,V)^p),\qquad b=2^p.
\]
If \(p\le p_*\), every \(a\ge0\) gives a positive-semidefinite kernel, strictly positive definite whenever \(a>0\). If \(p>p_*\), let \(\rho_{q,p}\) be the unique root in \((0,1)\) of
\[
1-(q+1)t+qt^{2^p}=0.
\]
Then \(K_{a,p}\) is positive semidefinite **exactly** when \(a=0\) or \(a\ge-\log\rho_{q,p}\), and is strictly positive definite exactly when \(a>-\log\rho_{q,p}\). At \(a=0\) its rank is \(1\); at the nonzero transition \(a=-\log\rho_{q,p}\) its rank is \(m\). In particular, for the unsnowflaked distance exponent \(p=1\), the admissible range simplifies to \(a=0\) or \(a\ge\log q\), and the nontrivial boundary has rank \(m\). These statements hold for every prime power and every \(n\ge4\), with no limit or genericity hypotheses.

## Assumptions and scope

All scalar matrices and positive-definiteness tests are over \(\mathbb R\). A symmetric function \(D\) is CND when \(\sum_{U,V}c_Uc_V D(U,V)\le0\) for every real \(c\) with \(\sum_Uc_U=0\); it is strictly CND when equality forces \(c=0\). Positive (semi)definiteness of a kernel on the finite set \(X\) refers to its complete \(N\times N\) Gram matrix; positive definiteness on all smaller configurations follows by taking principal submatrices. \(\binom{n}{2}_q\) denotes the Gaussian binomial coefficient shown above. The parameter \(a=0\) is included; formally \(a=+\infty\) yields the identity kernel but is not a finite parameter.

## Proof

**1. The incidence spectrum.** Set \(r=(q^{n-1}-1)/(q-1)\). Let \(B\) be the \(m\times N\) zero-one matrix recording projective-point membership in two-subspaces: \(B_{P,U}=1\) if \(P\subset U\). Every two-subspace contains \(q+1\) projective points; every point lies in exactly \(r\) two-subspaces; two distinct points span a unique two-subspace. Therefore
\[
BB^\top=(r-1)I_m+J_m,\qquad B^\top B=(q+1)I_N+A,
\]
where \(J\) denotes the all-ones matrix and \(A_{UV}=1\) precisely when \(\dim(U\cap V)=1\). Since \(r>1\), the first matrix is positive definite and \(\operatorname{rank}B=m\). The constant vectors of the domain and codomain correspond via \(B\). Their orthogonal complements consequently decompose \(\mathbb R^N=V_0\oplus V_1\oplus V_2\), with dimensions \(1\), \(m-1\), \(N-m\); these are, respectively, the constants, \(\operatorname{im}B^\top\cap\mathbf1^\perp\), and \(\ker B\). The three eigenvalues of \(A\) are
\[
k=(q+1)(r-1),\qquad \theta_1=r-q-2,\qquad \theta_2=-(q+1).
\]
Here \(\theta_1=q^2+q^3+\cdots+q^{n-2}-1>0\) since \(n\ge4\). The point-disjoint relation is \(J-I-A\). The three blocks exhaust the spectrum, without an appeal to a classification table.

**2. Sharp negative type.** Put \(b=2^p>1\). Because distances are exactly \(0,1,2\),
\[
D_p=bJ-bI+(1-b)A.
\]
On \(V_1\) and \(V_2\), the respective eigenvalues are
\[
\mu_1=-b+(1-b)(r-q-2)<0,\qquad
\mu_2=(q+1)-qb.
\]
The entire zero-sum subspace is \(V_1\oplus V_2\). Thus \(D_p\) is CND exactly when \(b\le(q+1)/q\), and is strictly CND exactly when \(b<(q+1)/q\). The centering matrix \(H\) acts as the identity on these blocks and zero on constants. The centered Euclidean Gram matrix \(-\tfrac12 HD_pH\) therefore has the asserted ranks. Every Euclidean realization with squared distances \(D_p\) has this centered Gram matrix, so its rank is the minimal ambient Euclidean dimension after translation.

At the critical power \(b=(q+1)/q\), the projective-point indicator columns \(h_U\) of \(B\) satisfy
\[
\left\|\frac{h_U-h_V}{\sqrt{2q}}\right\|^2
=\begin{cases}0&d(U,V)=0,\\1&d(U,V)=1,\\(q+1)/q&d(U,V)=2.\end{cases}
\]
Their coordinate sums are all \(q+1\), so the image lies in an affine hyperplane; its affine span has dimension \(m-1\) by the rank of the centered Gram matrix.

**3. Complete exponential-kernel spectrum.** For finite \(a\ge0\), set \(t=e^{-a}\in(0,1]\). The Gram matrix equals
\[
K_{a,p}=(1-t^b)I+(t-t^b)A+t^bJ.
\]
Its eigenvalues on the three blocks are
\[
\begin{aligned}
\lambda_0&=1+k t+(N-1-k)t^b,\\
\lambda_1&=1-t^b+\theta_1(t-t^b),\\
\lambda_2&=1-(q+1)t+qt^b.
\end{aligned}
\]
The first two are strictly positive for \(0\le t<1\), since \(k\ge0\), \(N-1-k\ge0\), \(\theta_1>0\), and \(0\le t^b\le t\le1\). At \(t=1\), \(\lambda_0=N\) and \(\lambda_1=\lambda_2=0\). It remains to classify \(f_b(t)=\lambda_2\) for \(0<t<1\). For \(b\le1+1/q\),
\[
f_b'(t)=-(q+1)+qb\,t^{b-1}<0\quad (0<t<1),
\]
so \(f_b(t)>f_b(1)=0\). For \(b>1+1/q\), strict convexity, \(f_b(0)=1\), \(f_b(1)=0\), \(f'_b(0)=-(q+1)<0\), and \(f'_b(1)>0\) imply that exactly one root \(\rho_{q,p}\) occurs in \((0,1)\); the sign is positive before that root and negative between it and \(1\). This proves all positive-semidefinite, strictness, and rank assertions. For \(p=1\), the polynomial factors as \(f_2(t)=(1-t)(1-qt)\), giving \(\rho_{q,1}=q^{-1}\).

## Verification

The accompanying `verify.py` reconstructs projective points and two-subspaces over \(\mathbb F_2\) and \(\mathbb F_3\) by row-reduced bases; it checks the incidence identities, intersection graph degrees, critical rational distance representation, and spectral formulas for the cases \((q,n)=(2,4),(2,5),(3,4)\). These have respectively \((m,N)=(15,35),(31,155),(40,130)\), and all exact tests pass. Run `python3 verify.py` in the directory containing the script. The script is finite diagnostic evidence only; the preceding proof establishes arbitrary prime powers and dimensions analytically.

## Relationship to prior work

Sánchez (2011) develops finite-metric methods for supremal negative type and calculates complete bipartite graph examples; Murugan (2011) gives a general determinant criterion for vertex-transitive graph metrics and examines Hamming cubes. Those broad methods make diameter-two spectral approaches natural, but the inspected works do not state the finite-field rank-two Grassmannian threshold, the sharp drop in Euclidean embedding dimension, or the three-branch exponential-kernel phase diagram. Harandi and collaborators (2014) study positive-definite kernels on real, continuous Grassmann manifolds with projection/angle geometry, rather than the finite-field graph path metric here. The incidence spectral ingredients are classical and the argument deliberately exposes that dependence; newness of the complete stated classification is assessed only against the sources checked, not claimed as a global priority certificate.

## Limitations

The theorem covers only two-dimensional subspaces and \(n\ge4\); it does not assert the same threshold for higher-rank Grassmann graphs or continuous real Grassmannians. Literature comparison was bounded: an unindexed formulation using the classical Grassmann graph adjacency spectrum together with generic negative-type criteria may already imply the same result. The finite checker is not an independent validation and does not replace the analytic proof. No independent audit has been performed.

## References

1. Stephen Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451 (first public version 2011-08-02), https://arxiv.org/abs/1108.0451.
2. Mathav Kishore Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657 (first public version 2011-12-23), https://arxiv.org/abs/1112.5657.
3. Mehrtash T. Harandi et al., *Expanding the Family of Grassmannian Kernels: An Embedding Perspective*, arXiv:1407.1123 (first public version 2014-07-04), https://arxiv.org/abs/1407.1123.
