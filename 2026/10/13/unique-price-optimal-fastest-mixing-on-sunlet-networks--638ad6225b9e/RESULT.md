# Unique price-optimal fastest mixing on sunlet networks

## Finding

**Theorem.** Let \(n\ge 3\) be an integer and \(t>0\). On the sunlet graph \(S_n=C_n\odot K_1\), assign nonnegative individual conductances \(a_j\) to the pendant edges and \(b_j\) to the edges of the base cycle, indexed by \(j\in\mathbb Z/n\mathbb Z\). Pendant conductance has unit price \(t\), cycle conductance unit price \(1\); require
\[
 t\sum_{j=0}^{n-1}a_j+\sum_{j=0}^{n-1}b_j=1.
\]
Let \(L\) be the ordinary symmetric weighted graph Laplacian on all \(2n\) vertices, with increasing eigenvalues starting at zero. Put
\[
 \mu_n=4\sin^2(\pi/n),\quad
 \chi_n=\sqrt{\mu_n t},\quad
 R_n(t)=\frac{\mu_n}{n\bigl(2+\mu_n t+2\sqrt{\mu_n t}\bigr)}.
\]
The exact optimum over **all individual edge allocations** is
\[
 \max\lambda_2(L)=R_n(t),
\]
and the **unique** maximizing allocation is
\[
 \boxed{\ a_j^*=R_n(t)\bigl(1+\chi_n^{-1}\bigr),\qquad
 b_j^*=\frac{R_n(t)}{\mu_n}(2+\chi_n)
 \quad\text{for every }j.\ }
\]
Every edge receives strictly positive conductance for every finite \(n\ge3\) and \(t>0\); there is no price-induced edge-deletion transition.

At each fixed \(t>0\), the asymptotic laws are
\[
 \lim_{n\to\infty}n^3R_n(t)=2\pi^2,\qquad
 \lim_{n\to\infty}n^2a_j^*=\frac{\pi}{\sqrt t},\qquad
 \lim_{n\to\infty}nb_j^*=1.
\]
If \(t=\rho n^2\) with fixed \(\rho>0\), there is a distinct price-size crossover:
\[
 \lim_{n\to\infty} n^3R_n(\rho n^2)
 =\frac{4\pi^2}{2+4\pi^2\rho+4\pi\sqrt\rho}.
\]

## Assumptions and scope

The vertices are cyclic vertices \(u_j\) and their distinct pendant leaves \(v_j\). The \(n\) cycle edges are \(u_ju_{j+1}\), and the \(n\) pendant edges are \(u_jv_j\), indices modulo \(n\). All rates are symmetric, and the stationary law of the continuous-time chain with generator \(-L\) is uniform when connected. The objective is the second-smallest eigenvalue of **the unnormalized Laplacian**, not the discrete-time second-largest eigenvalue modulus or a normalized-Laplacian gap. Edge prices are fixed within the two indicated orbits but decision variables are wholly unrestricted across individual edges. The budget is an equality; because the optimum is positive, using an inequality instead gives equality by scaling.

## Proof

**1. Cyclic reduction without assuming uniqueness.** The variational formula
\[
 \lambda_2(L)=\min_{z\perp\mathbf 1,\,\|z\|=1}\sum_{pq\in E}w_{pq}(z_p-z_q)^2
\]
shows that \(\lambda_2\) is concave in all edge weights. Averaging any allocation over the rotation group preserves expenditure and cannot decrease the gap. Therefore some globally optimal allocation has the two constant weights \(a_j=a\) and \(b_j=b\). Neither \(a=0\) nor \(b=0\) can attain a positive gap, because the graph then disconnects.

**2. Exact Fourier spectrum.** Set \(\mu_k=4\sin^2(\pi k/n)\). On Fourier mode \(k\), the Laplacian acts on cyclic and leaf amplitudes through
\[
 M_k=\begin{pmatrix}a+b\mu_k&-a\\-a&a\end{pmatrix}.
\]
For \(k=0\) its eigenvalues are \(0\) and \(2a\). For nonzero \(k\), the smaller eigenvalue is
\[
 h(a,b,\mu_k)=a+\frac{b\mu_k}{2}
 -\sqrt{a^2+\left(\frac{b\mu_k}{2}\right)^2}.
\]
For positive \(a,b\), this expression is positive, strictly increasing in \(\mu_k\), and less than \(a\). As the least nonzero \(\mu_k\) equals \(\mu_n\), and \(2a>a\), it follows that \(\lambda_2=h(a,b,\mu_n)\). Its real eigenspace is exactly the two-dimensional cosine/sine first-harmonic space.

**3. Sharp price bound.** Write \(x=a\), \(y=\mu_n b/2\), and \(r=h(a,b,\mu_n)>0\). The equality \(r=x+y-\sqrt{x^2+y^2}\) is equivalent to
\[
 x>r,\qquad y>r,\qquad (x-r)(y-r)=\frac{r^2}{2}.
\]
More generally, requiring a spectral gap at least \(r\) amounts to the last equality with \(\ge\) in place of \(=\). Arithmetic-geometric mean, with equality conditions, gives
\[
 ta+b=tx+\frac{2y}{\mu_n}
 \ge r\left(t+\frac2{\mu_n}+2\sqrt{\frac t{\mu_n}}\right),
\]
with equality precisely when
\[
 x=r\left(1+\frac1{\sqrt{\mu_n t}}\right),\qquad
 y=r\left(1+\frac{\sqrt{\mu_n t}}2\right).
\]
The budget \(n(ta+b)=1\) consequently gives \(r\le R_n(t)\); equality yields exactly the announced \(a^*,b^*\), which are feasible. Thus the **symmetric** optimum is unique.

**4. Rigidity against asymmetric allocations.** Let an arbitrary feasible allocation attain the global gap \(R=R_n(t)\). Its rotational average is the unique symmetric optimum just found. Let \(z^{(c)}\) and \(z^{(s)}\) be real cosine and sine first-harmonic eigenvectors of the averaged Laplacian for eigenvalue \(R\). For every rotation of the original allocation, the Rayleigh quotient of either vector is at least \(R\). Their average is exactly \(R\). Hence the Rayleigh quotient for each rotation, including the identity, equals \(R\); both vectors are eigenvectors of the original Laplacian.

Write their two coordinates at cyclic vertex \(u_j\) as \(U(\cos j\theta,\sin j\theta)\), and at leaf \(v_j\) as \(V(\cos j\theta,\sin j\theta)\), where \(\theta=2\pi/n\). Both \(U\) and \(V-U\) are nonzero, by the positive-eigenvalue equations for \(M_1\). The leaf equations for the two eigenvectors force \(a_j=a^*\) at every leaf (the sine and cosine never vanish simultaneously). Subtracting the already-satisfied symmetric cyclic-vertex equations then gives, with \(q_j=(\cos j\theta,\sin j\theta)\),
\[
 (b_{j-1}-b^*)(q_j-q_{j-1})
 +(b_j-b^*)(q_j-q_{j+1})=0.
\]
The two chord vectors are linearly independent: their oriented determinant equals \(-2(1-\cos\theta)\sin\theta\ne0\) for \(n\ge3\). Thus \(b_{j-1}=b_j=b^*\) for every \(j\). The individual allocation is therefore the announced one, proving **global uniqueness**.

**5. Scaling limits.** Since \(\mu_n=4\pi^2n^{-2}+O(n^{-4})\), direct substitution into the exact formulas proves all stated limits, including the crossover with \(\mu_n t\to4\pi^2\rho\). No numerical or finite-size extrapolation is needed.

## Verification

Run `python3 verify_sunlet.py` with the Python standard library. It checks \(168\) exact-rational budget, characteristic-equation, and equality-certificate identities, independently diagonalizes \(36\) complete weighted Laplacians, and compares \(1080\) nonsymmetric feasible allocations. The obtained line is:

`VERIFY_OK 168 exact rational identities; 36 optimized full Laplacian eigenspectra; 1080 nonsymmetric feasible comparisons; max absolute gap error 2.776e-16`

Finite checks are supplementary. The universal theorem follows from the concavity, Fourier, inequality, and rigidity arguments above.

## Relationship to prior work

The semidefinite-programming formulation and geometric dual of optimal algebraic connectivity are classical; Göring–Helmberg–Wappler and Sun–Boyd–Xiao–Diaconis establish general optimization frameworks, not this price-resolved sunlet formula. The sunlet is a graph corona; Liu–Shao derive fixed-weight **normalized** and **signless** corona spectra, rather than the ordinary-Laplacian global cost-allocation optimum. Du–Zhu–Gao–Li derive a weighted-corona ordinary-Laplacian characteristic polynomial and study coherence, but do not optimize the Fiedler eigenvalue under prices; their conclusion explicitly leaves general weighted-corona Laplacian spectra for future study. Wan and coauthors give structural edge-design results, especially for trees, but the sunlet is unicyclic and has a two-dimensional optimal Fiedler eigenspace. The present statement provides the explicit arbitrary-price optimum and a uniqueness theorem against all nonsymmetric edge assignments. General convex programmability and already-known fixed-weight spectra are not claimed as new. No search can exclude every unindexed or unpublished equivalent specialization.

## Limitations

The result treats a sunlet with exactly one leaf per cycle vertex and identical within-orbit prices, uniform stationary masses, symmetric continuous-time rates, and a linear total-expenditure budget. It does not cover nonuniform vertex masses, node-dependent prices, arbitrary corona attachments, normalized-Laplacian optimization, or discrete-time fastest-mixing chains. The self-review is not an independent peer review; historical equivalence remains a residual possibility.

## References

1. C. Göring, C. Helmberg, M. Wappler, *Embedded in the Shadow of the Separator*, Optimization Online, first public posting 2005-09-02. https://optimization-online.org/wp-content/uploads/2005/09/1202.pdf
2. J. Sun, S. Boyd, L. Xiao, P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699. https://doi.org/10.1137/S0036144504443821 ; lawful public text https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf
3. Y. Wan, S. Roy, X. Wang, A. Saberi, T. Yang, M. Xue, B. Malek, *On the Structure of Graph Edge Designs that Optimize the Algebraic Connectivity*, 47th IEEE Conference on Decision and Control (2008). https://doi.org/10.1109/CDC.2008.4738734
4. H. Liu, Y. Shao, *Two Kinds of Laplacian Spectra and Degree Kirchhoff Index of the Weighted Corona Networks*, Journal of Mathematics (2022). https://doi.org/10.1155/2022/6884839
5. W. Du, J. Zhu, H. Gao, X. Li, *Consensus analysis of the weighted corona networks*, Frontiers in Physics 10 (2022), 948247. https://doi.org/10.3389/fphy.2022.948247 ; open-access text https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2022.948247/pdf
