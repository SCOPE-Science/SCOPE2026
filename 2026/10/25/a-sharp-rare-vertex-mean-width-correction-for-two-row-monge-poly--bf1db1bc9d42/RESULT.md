# A sharp rare-vertex mean-width correction for two-row Monge polytopes

## Finding
Let \(n\ge3\), and let \(\mathcal M_{2,n}\) be the normalized two-row Monge polytope of nonnegative matrices \((u_j,v_j)_{1\le j\le n}\) with total entry sum one and \(u_j+v_{j+1}\le u_{j+1}+v_j\) for \(1\le j<n\). Equip its entry-sum-one affine hull with the inherited Frobenius metric. Let
\[
Q_n=\operatorname{conv}\left\{\frac{e_{1j}+e_{2j}}2:1\le j\le n\right\}\subset\mathcal M_{2,n}
\]
be the natural column-vertex simplex, and let \(w_H\) denote mean width calculated using the uniform unit sphere in the \((2n-1)\)-dimensional tangent hyperplane.

The column simplex supplies the entire leading mean width, but the remaining row-prefix and row-suffix vertices create a **strict, sharply quantified lower-order excess**:
\[
\boxed{\lim_{n\to\infty}n(\log n)^{3/4}\bigl[w_H(\mathcal M_{2,n})-w_H(Q_n)\bigr]=\sqrt2\,\pi^{1/4}.}
\]
In particular, \(w_H(\mathcal M_{2,n})\sim\sqrt{2\log n/n}\). The excess is positive for every \(n\ge3\), and the leading correction comes from exactly **two extreme row vertices**, not from the other \(2n-2\) row vertices.

More precisely, for \(G=(G_{ij})\in\mathbb R^{2n}\) with independent standard normal entries, let \(H_n=h_{\mathcal M_{2,n}}(G)\) and \(T_n=h_{Q_n}(G)\), and define the positive Gaussian quantile \(b_n\) by
\[
n\,\overline\Phi(\sqrt2 b_n)=1,
\]
where \(\Phi\) is the standard normal distribution function and \(\overline\Phi=1-\Phi\). Then
\[
\boxed{\lim_{n\to\infty}\sqrt n\,(\log n)^{3/4}\bigl(\mathbb E H_n-\mathbb E T_n\bigr)=\pi^{1/4},}
\]
and \(2b_n(H_n-b_n)\) converges in distribution to the standard Gumbel law \(\Pr(Z\le x)=\exp(-e^{-x})\). These limits concern Gaussian support in the entry coordinate space; translating the polytopes within their common affine hull does not change the mean-width claim.

## Assumptions and scope
The Gaussian entries are independent \(N(0,1)\); logarithms are natural. For \(K\) in the affine sum-one hyperplane, \(w_H(K)=\int_{S(H)}[h_K(\theta)+h_K(-\theta)]\,d\sigma_H(\theta)\), where \(H=\{z:\sum_{ij}z_{ij}=0\}\) and \(\sigma_H\) is its normalized spherical measure. The Gaussian support \(h_K(G)\) can be computed using independent ambient coordinates because the normal component shifts the support of all sum-one vertices by the same random constant. This shift has mean zero and cancels exactly in the difference of the two support functions. The source polytope is full-dimensional in its affine span; \(Q_n\) is lower-dimensional, but its mean width is well defined in \(H\). There is no claim about Euclidean volume, inballs, or a uniformly distributed point inside \(\mathcal M_{2,n}\).

## Proof
**1. Exact vertex support.** Erickson--Kretschmann, Proposition 5.1, characterizes the vertices of the normalized nonsymmetric Monge polytope. Specializing their description to two rows gives exactly the \(n\) column vertices \((e_{1j}+e_{2j})/2\), the \(n\) normalized top-row suffix indicators, and the \(n\) normalized bottom-row prefix indicators. Thus, writing
\[
Y_j=\frac{G_{1j}+G_{2j}}2,\qquad
A_k=\frac1k\sum_{j=n-k+1}^nG_{1j},\qquad
B_k=\frac1k\sum_{j=1}^kG_{2j},
\]
we have the **exact** identities
\[
T_n=\max_{1\le j\le n}Y_j,\qquad
H_n=\max\bigl\{T_n,A_1,\ldots,A_n,B_1,\ldots,B_n\bigr\}.
\]
The \(Y_j\) are independent \(N(0,1/2)\); each \(A_k,B_k\) has variance \(1/k\). In particular, \(A_1=G_{1n}\) and \(B_1=G_{21}\) are the only two row-normalized support variables having variance one.

**2. All longer row averages are negligible at the asserted scale.** Set \(R_n=\max_{2\le k\le n}\{A_k,B_k\}\), choose \(t_n=0.9b_n\), and recall \(b_n^2\sim\log n\). Using \((x-y)_+\le(x-t)_++(t-y)_+\),
\[
\mathbb E(R_n-T_n)_+\le\sum_{k=2}^n\bigl[\mathbb E(A_k-t_n)_++\mathbb E(B_k-t_n)_+\bigr]+\mathbb E(t_n-T_n)_+.
\]
Gaussian Mills bounds and \(A_k,B_k\sim N(0,1/k)\) give, uniformly for \(t_n\to\infty\),
\[
\sum_{k=2}^n\mathbb E(A_k-t_n)_++\mathbb E(B_k-t_n)_+
\le C\int_{t_n}^\infty\frac{e^{-u^2}}{u}\,du=O(e^{-t_n^2}/t_n^2)
=n^{-0.81+o(1)}.
\]
For \(T_n=\max_jY_j\), the lower-tail probability at \(t_n\) is \(\Phi(\sqrt2 t_n)^n\le\exp[-n^{0.19+o(1)}]\). Integrating this bound over a finite interval and applying a Gaussian tail bound further left yields \(\mathbb E(t_n-T_n)_+=o(n^{-K})\) for every fixed \(K\). Hence
\[
\mathbb E(R_n-T_n)_+=o\bigl(n^{-1/2}(\log n)^{-3/4}\bigr).
\]
It suffices to analyze \(\max\{T_n,A_1,B_1\}-T_n\).

**3. Remove two correlated columns.** Let \(T_n^{\circ}=\max_{2\le j\le n-1}Y_j\); it is independent of the two independent standard normals \(A_1\) and \(B_1\). For fixed \(a,b\), the map \(t\mapsto(\max\{a,b,t\}-t)\) is nonincreasing and one-Lipschitz. Since \(T_n\ge T_n^{\circ}\), the difference of the corresponding positive-part expectations is bounded by
\[
\mathbb ET_n-\mathbb ET_n^{\circ}=O((n b_n)^{-1}).
\]
The final estimate follows either by integrating \(\Phi(\sqrt2 t)^{n-2}[1-\Phi(\sqrt2t)^2]\), or directly by standard Gaussian-maxima quantile bounds. It is negligible at the target scale. Independence now gives the exact integral
\[
\mathbb E(\max\{A_1,B_1\}-T_n^{\circ})_+
=\int_{-\infty}^{\infty}\bigl(2\overline\Phi(t)-\overline\Phi(t)^2\bigr)\Phi(\sqrt2t)^{n-2}\,dt.
\]
The term containing \(\overline\Phi(t)^2\) is \(o(n^{-1/2}b_n^{-3/2})\), by the same quantile-window and Gaussian-tail estimates used next.

**4. A sharp boundary Laplace integral.** Define \(I_n=\int_{-\infty}^{\infty}\overline\Phi(t)\Phi(\sqrt2t)^{n-2}\,dt\). For fixed \(x\), write \(t=b_n+x/(2b_n)\). Gaussian Mills asymptotics and the defining quantile relation give
\[
\Phi(\sqrt2t)^{n-2}\longrightarrow e^{-e^{-x}},\quad
\overline\Phi(t)\sim\frac{e^{-b_n^2/2-x/2}}{\sqrt{2\pi}\,b_n},\quad
 e^{-b_n^2/2}\sim\frac{\sqrt2\,\pi^{1/4}b_n^{1/2}}{\sqrt n}.
\]
A uniform Mills-ratio domination on the upper side, and the superexponential lower tail of the Gaussian maximum on the lower side, justify dominated convergence after this change of variables. Consequently
\[
\begin{aligned}
I_n&\sim\frac{e^{-b_n^2/2}}{2\sqrt{2\pi}\,b_n^2}
\int_{-\infty}^{\infty}e^{-x/2-e^{-x}}\,dx\\
&=\frac{e^{-b_n^2/2}}{2\sqrt2\,b_n^2}
\sim\frac{\pi^{1/4}}{2\sqrt n\,b_n^{3/2}},
\end{aligned}
\]
where the integral equals \(\Gamma(1/2)=\sqrt\pi\). The two singleton vertices contribute \(2I_n\) to first order; steps 2--3 show that all remaining corrections are negligible. Since \(b_n/\sqrt{\log n}\to1\), this proves the stated Gaussian-support excess with constant \(\pi^{1/4}\).

**5. Intrinsic mean width and Gumbel law.** Let \(m_{2n-1}=\mathbb E\|Z_H\|\), for a standard Gaussian \(Z_H\) in the tangent space \(H\). Gaussian polar decomposition yields \(w_H(K)=2\mathbb Eh_K(G)/m_{2n-1}\) for any \(K\) of sum-one vertices, since the ambient normal component has zero expectation. Moreover \(m_{2n-1}\sim\sqrt{2n}\). Therefore the Gaussian-support excess from step 4 implies the boxed mean-width limit \(\sqrt2\pi^{1/4}\). Since \(\mathbb ET_n\sim b_n\sim\sqrt{\log n}\), the leading mean-width asymptotic follows. Finally, \(\Pr(T_n\le b_n+x/(2b_n))\to e^{-e^{-x}}\). At this threshold the union bound over the two variance-one vertices and over all longer averages is \(o(1)\), so \(H_n\) has the same Gumbel limit. Positivity of the width excess for finite \(n\) follows because the row singleton vertices lie outside the column simplex and each has a positive-probability open cone of uniquely exposed Gaussian directions.

## Verification
The standalone program `verify_monge_width.py` derives each random linear optimization problem from the full coordinate and adjacent Monge inequalities, solves it independently by SciPy/HiGHS, and compares the optimum with the \(3n\)-vertex support formula over 300 seeded random trials for \(3\le n\le12\). It also evaluates the one-dimensional rare-vertex integral at five exponentially increasing values of \(n\) and reports its slowly converging normalized values against the predicted \(\pi^{1/4}/2\) for a single boundary vertex. The successful run began `VERIFY_OK supports 300 LP comparisons`; the exact integral-normalization output is reproducible by running `python verify_monge_width.py` after installing the dependencies in `requirements.txt`. These finite checks do not prove any limiting theorem; the proof is analytic.

## Relationship to prior work
Erickson and Kretschmann, arXiv:2311.07522v2 (first available 2023-11-13), establish the precise vertex and facet structure of Monge polytopes and the exact normalized volume of the two-row case. Their vertex theorem directly supplies the three classes of Gaussian support variables in step 1; the source does not contain the asymptotic intrinsic mean-width gap, the exceptional-row-vertex correction constant, or the Gaussian support Gumbel limit. The later Erickson--Jones work, arXiv:2609.09508, addresses normalized volume and Ehrhart series by lattice-path methods. Its full text was not accessible in the literature check, and the comparison is limited to its public abstract.

A prior result on **uniformly distributed points inside** two-row Monge polytopes studies their Laplace-contrast profile and endpoint fluctuations; it does not determine Gaussian **support maxima over vertices** or mean width. Exact Frobenius inball formulas for rectangular Monge polytopes concern a different metric invariant and do not imply the above mean-width statement. Both distinctions concern distributions and mathematical implications, not merely titles. The probabilistic ingredients here use classical Gaussian maxima and Mills ratios; the assessed geometric contribution is the two-row Monge reduction and sharp lower-order rare-vertex width constant.

## Limitations
The theorem is for two-row normalized nonsymmetric Monge matrices and fixed independent standard Gaussian direction coordinates, not general \(p\times q\) aspect ratios or weighted costs. The Gumbel statement is about random Gaussian directional support, not a random point sampled uniformly in the polytope. The mean-width gap is relative to the column-vertex simplex in the same affine hull. The proof uses standard Gaussian tail estimates and is not an independent mathematical certification. A newer paper on the same object was accessible only at abstract level; equivalent formulas in less-indexed Gaussian-width literature remain a priority risk.

## References
- W. Q. Erickson and J. Kretschmann, *The structure and normalized volume of Monge polytopes*, arXiv:2311.07522v2, posted 2023-11-13, especially Proposition 5.1 and Theorems 5.3, 5.6; https://arxiv.org/html/2311.07522v2.
- W. Q. Erickson and N. B. Jones, *A lattice path model for the volume of the Monge polytope*, arXiv:2609.09508, posted 2026-09-08 (abstract inspected).
- Standard Gaussian maxima and Mills-ratio asymptotics are used in the proof; all constants required here are derived explicitly rather than imported from a numerical table.
