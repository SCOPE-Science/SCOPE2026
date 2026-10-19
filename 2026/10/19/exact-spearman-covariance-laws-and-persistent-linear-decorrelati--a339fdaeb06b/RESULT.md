# Exact Spearman covariance laws and persistent linear decorrelation in shuffled full-branch maps

## Finding

Fix integers \(m\ge2\) and \(N\ge m\), a branch-orientation vector \(\varepsilon=(\varepsilon_1,\ldots,\varepsilon_m)\in\{-1,+1\}^m\), and a permutation \(\pi\) of \(\{1,\ldots,N\}\). Define the signed branch sum \(S=\sum_{j=1}^m\varepsilon_j\). For the stationary interval map \(g_\pi=\sigma_\pi\circ f_\varepsilon\) defined below, let \(C_\pi=\operatorname{Cov}(X_0,X_1)\), with \(X_0\) uniform on the unit interval and \(X_{k+1}=g_\pi(X_k)\). If
\[
a_j=j-\frac{N+1}{2},\qquad
r_\pi=\frac{12}{N(N^2-1)}\sum_{j=1}^N a_j a_{\pi(j)},
\]
then the **exact dynamical rank-covariance identity** is
\[
\boxed{ C_\pi=\frac{S}{12m^2N^2}\bigl[1+(N^2-1)r_\pi\bigr]. }
\]
The number \(r_\pi\) is the usual Spearman rank correlation of the rank sequences \((1,\ldots,N)\) and \((\pi(1),\ldots,\pi(N))\). No independence or asymptotic approximation is used in this identity.

For \(\pi\) sampled uniformly from all \(N!\) permutations, its exact ensemble moments are
\[
\boxed{\mathbb E_\pi C_\pi=\frac{S}{12m^2N^2},\qquad
\operatorname{Var}_\pi(C_\pi)
=\frac{S^2(N^2-1)^2}{144m^4N^4(N-1)}.}
\]
The distribution is symmetric around its mean. When \(S\ne0\), the exact standardized statistic is
\[
\frac{C_\pi-\mathbb E_\pi C_\pi}
{\sqrt{\operatorname{Var}_\pi(C_\pi)}}
=\operatorname{sgn}(S)\sqrt{N-1}\,r_\pi,
\]
and has Kolmogorov distance \(O(N^{-1/2})\) from standard normal as \(N\to\infty\) for fixed \(m\) and fixed \(\varepsilon\); in particular
\[
\sqrt N\,C_\pi\ \Longrightarrow\
\mathcal N\!\left(0,\frac{S^2}{144m^4}\right).
\]
All constants in this asymptotic assertion may depend on fixed \(m\) and \(\varepsilon\). The rank-statistic normal approximation itself is classical; the new object is its exact realization by the dynamical observable.

There is also an **all-future rigidity classification**: the following are equivalent.

1. \(S=0\).
2. For **every** \(N\ge m\), every equal-cell permutation \(\pi\), every integer \(k\ge1\), and every bounded measurable \(\psi:[0,1]\to\mathbb R\),
\[
\boxed{\operatorname{Cov}\bigl(X_0,\psi(X_k)\bigr)=0.}
\]

Thus balanced orientations force exact linear orthogonality of the initial coordinate to every bounded observable of every future state, independently of the output-cell permutation. This is **not** independence of the states and does not say that arbitrary functions of the initial coordinate are uncorrelated with the future.

## Assumptions and scope

On the \(j\)-th equal branch \(I_j=[(j-1)/m,j/m)\), for \(1\le j\le m\), define the full-branch map
\[
f_\varepsilon(x)=
\begin{cases}
mx-(j-1),&\varepsilon_j=+1,\\
j-mx,&\varepsilon_j=-1.
\end{cases}
\]
On the \(i\)-th equal output cell \(J_i=[(i-1)/N,i/N)\), define the orientation-preserving interval exchange
\[
\sigma_\pi(y)=y+\frac{\pi(i)-i}{N}.
\]
Endpoints are identified by arbitrary consistent conventions, which do not affect Lebesgue probabilities or covariance identities. Both \(f_\varepsilon\) and \(\sigma_\pi\) preserve Lebesgue probability, hence so does \(g_\pi\). All stated probabilities and moments under \(X_0\) use this canonical stationary law, not a claim of uniqueness or mixing. The permutation ensemble, when specified, is uniform on the symmetric group and separate from the stationary initial distribution.

## Proof

**Step 1: exact conditional barycenter of the inverse branches.** Set \(Y=f_\varepsilon(X_0)\). The map has \(m\) inverse branches of common Jacobian \(1/m\), so conditional on \(Y=y\), the branch label is uniform on \(\{1,\ldots,m\}\) for Lebesgue-a.e. \(y\). The inverse of the \(j\)-th branch is \((j-1+y)/m\) if \(\varepsilon_j=+1\) and \((j-y)/m\) if \(\varepsilon_j=-1\). Averaging these inverse coordinates gives the exact affine identity
\[
\boxed{\mathbb E\bigl[X_0-\tfrac12\mid Y=y\bigr]
=\frac{S}{m^2}\bigl(y-\tfrac12\bigr).}
\]
One way to check the additive constant is to evaluate at \(y=1/2\): the mean of the branch midpoints \((j-1/2)/m\) is \(1/2\); the derivative in \(y\) is the average inverse slope \(S/m^2\). This argument treats every sign vector, including odd \(m\) for which \(S\ne0\).

**Step 2: covariance identity and all-future orthogonality.** Stationarity gives \(\mathbb EX_k=1/2\). Because \(X_1=\sigma_\pi(Y)\), the tower property gives
\[
C_\pi=\frac{S}{m^2}\int_0^1
\bigl(y-\tfrac12\bigr)\bigl(\sigma_\pi(y)-\tfrac12\bigr)\,dy.
\]
Write \(y=(i-1+t)/N\) for \(0\le t<1\) inside \(J_i\), so \(\sigma_\pi(y)=(\pi(i)-1+t)/N\). With \(a_i=i-(N+1)/2\), both centered coordinates equal \((a_i+t-1/2)/N\) and \((a_{\pi(i)}+t-1/2)/N\). Integrating \(t\) over \([0,1]\) and summing cells yields
\[
\int_0^1\bigl(y-\tfrac12\bigr)
\bigl(\sigma_\pi(y)-\tfrac12\bigr)\,dy
=\frac{1}{N^3}\sum_{i=1}^N a_i a_{\pi(i)}+\frac{1}{12N^2}.
\]
Substituting the definition of \(r_\pi\) proves the boxed formula. For \(k\ge1\), \(X_k\) is a measurable function of \(Y\), namely \(g_\pi^{k-1}(\sigma_\pi(Y))\). Thus if \(S=0\), the conditional barycenter formula forces \(\operatorname{Cov}(X_0,\psi(X_k))=0\) for every bounded measurable \(\psi\). Conversely, if this universal orthogonality holds, choose \(N=m\), the identity permutation, \(k=1\), and \(\psi(x)=x\). Since \(\sigma_\pi\) is then the identity, the covariance equals \(S/(12m^2)\); it can vanish only if \(S=0\). This establishes both quantifiers in the equivalence.

**Step 3: exact ensemble mean, variance, and symmetry.** Let \(Q_\pi=\sum_i a_i a_{\pi(i)}\). As \(\sum_i a_i=0\) and \(\sum_i a_i^2=N(N^2-1)/12\), permutation sampling gives
\[
\mathbb E_\pi Q_\pi=0,
\quad \operatorname{Var}_\pi(Q_\pi)
=\frac{(\sum_i a_i^2)^2}{N-1}.
\]
For completeness, \(\mathbb E[a_{\pi(i)}^2]=(\sum_j a_j^2)/N\) and \(\mathbb E[a_{\pi(i)}a_{\pi(j)}]=-(\sum_l a_l^2)/(N(N-1))\) for \(i\ne j\); expanding \(Q_\pi^2\) gives the formula. The reversal \(\pi^*(i)=N+1-\pi(i)\) is a bijection on the symmetric group and sends \(Q_\pi\) to \(-Q_\pi\). Applying the affine covariance identity proves the displayed exact moments and symmetry. The rearrangement inequality gives the two exact extremal values \(S/(12m^2)\) at the identity permutation and \(S(2-N^2)/(12m^2N^2)\) at the rank reversal; the maximum and minimum are the larger and smaller of these values. For \(S\ne0\), the maximum absolute magnitude is \(|S|/(12m^2)\), uniquely attained at the identity permutation (including \(N=2\), where the second magnitude is zero). The entire finite support, not necessarily a full real interval, is the image of the discrete Spearman support under the boxed affine transformation.

**Step 4: Gaussian fluctuations.** The statistic \(Q_\pi\) is the classical centered two-rank permutation sum. Its variance is \(\sigma_N^2=[N(N^2-1)/12]^2/(N-1)\). Apply the deterministic-array specialization of the Chen–Fang combinatorial central limit theorem to \(c_{ij}=a_i a_j/\sigma_N\), whose row and column means vanish and which has \(\max_{ij}|c_{ij}|=O(N^{-1/2})\). Its Kolmogorov bound is at most \((451/N)\sum_{i,j}|c_{ij}|^3=O(N^{-1/2})\), since the sum has \(N^2\) entries. This proves the standardized bound. Since \(\mathbb E C_\pi=O(N^{-2})\) and \(N\operatorname{Var}(C_\pi)\to S^2/(144m^4)\) for fixed nonzero \(S\), the final weak limit follows by Slutsky's theorem. If \(S=0\), every \(C_\pi\) vanishes exactly and the Gaussian statement is intentionally excluded.

## Verification

The standalone `verify.py` performs a second, exact rational calculation of \(\operatorname{Cov}(X_0,X_1)\) by integrating each composition branch and output-cell intersection directly, independently of the conditional-barycenter derivation. It exhausts every orientation and output permutation for \((m,N)=(2,2),(2,3),(3,3),(3,4),(4,4),(4,5)\), altogether 2,576 cases, and verifies exact moment formulas for every orientation when \(N\le5\). These finite calculations are regression checks only. Steps 1–4 establish the universal and asymptotic statements.

## Relationship to prior work

Byott–Lin–Zhang (2014), the motivating treatment of the same mixed-orientation branch family under equal-cell permutations, analyzes transfer-operator and topological mixing properties; it provides the objects and context but not the above affine rank-covariance distribution or the balanced all-future identity in its inspected results. Byott–Holland–Zhang (2012) studies the related all-increasing stretch-and-fold family and spectral mixing, so it does not determine the signed-orientation classification. The Spearman statistic, rearrangement bounds, and permutation combinatorial central limit theorem are classical and are *not* presented as new standalone probability results; Chen–Fang's published theorem is invoked in Step 4. The contribution claimed here is the exact, sign-sensitive dynamical reduction, its uniform-shuffle consequences, and the all-future linear-orthogonality criterion.

## Limitations

The orthogonality assertion concerns the **linear initial coordinate** and arbitrary bounded observables of a **single future state**, not independence of past and future sigma-fields or vanishing nonlinear temporal correlations. No global classification of transfer spectral gaps, invariant-measure uniqueness, or mixing speed is asserted. The Gaussian limit averages **uniformly over permutations** for fixed orientation and fixed branch count; it is not a central limit theorem for time averages under one fixed map. The source comparison was bounded to accessible papers and searchable records, so unindexed earlier statements or hidden stronger implications remain a historical-priority risk.

## References

1. Nigel P. Byott, Congping Lin, Yiwei Zhang, *On the mixing properties of piecewise expanding maps under composition with permutations, II: Maps of non-constant orientation*, arXiv:1405.0481v1 (first public 2014-05-02).
2. Nigel P. Byott, Mark Holland, Yiwei Zhang, *On the mixing properties of piecewise expanding maps under composition with permutations*, arXiv:1203.5145v1 (2012).
3. Louis H. Y. Chen, Xiao Fang, *On the error bound in a combinatorial central limit theorem*, arXiv:1111.3159 (2011), Theorem 1.1.
