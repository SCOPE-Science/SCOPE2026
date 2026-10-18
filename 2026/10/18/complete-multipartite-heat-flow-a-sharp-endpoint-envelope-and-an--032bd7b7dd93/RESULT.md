# Complete multipartite heat flow: a sharp endpoint envelope and an ordered hub-to-bulk transition

## Finding

Let \(G=K_{m_1,\ldots,m_r}\) be any finite simple, unweighted, complete multipartite graph, with \(r\ge2\), positive integer part sizes \(m_i\), and \(n=\sum_i m_i\). Let \(L=D-A\) denote its **unnormalized** combinatorial Laplacian on counting-measure functions on the vertices, and \(H_t=e^{-tL}\). The following hold for every real \(t>0\), on both real and complex functions:

\[
\boxed{\ \|\partial_t H_t\|_{\ell^1\to\ell^1}
=\|\partial_t H_t\|_{\ell^\infty\to\ell^\infty}
=2\max_{1\le i\le r}\frac{n-m_i}{m_i}
\bigl((m_i-1)e^{-(n-m_i)t}+e^{-nt}\bigr).\ }
\]

The exact scale-invariant analyticity coefficient obeys
\[
\boxed{\ \sup_{t>0}t\|\partial_t H_t\|_{\ell^\infty\to\ell^\infty}
\le\frac{2(n-1)}{en},\ }
\]
with **equality if and only if some part has size one**, equivalently if the graph has a universal vertex. In every equality case the maximizing time is uniquely \(t=1/n\). In the absence of a singleton part, the inequality is strict.

For any two distinct available part sizes \(1\le a<b<n\), their respective row-norm expressions cross at exactly one positive time \(t_{a,b}\); the row belonging to size \(a\) dominates first and the size \(b\) row dominates thereafter. Consequently, as time grows, a maximizing part size never decreases. The global envelope experiences at most one fewer transition than the number of distinct part sizes; intermediate sizes may be skipped.

The full endpoint derivative-norm profile depends only on \(n\) and the **set of distinct part sizes**, not their multiplicities. Thus two nonisomorphic graphs, \(K_{2,4,4,4,6}\) and \(K_{2,2,4,6,6}\), have identical endpoint norm profiles for every time, even though their Laplacian spectra differ.

## Assumptions and scope

All graphs have at least two nonempty parts and therefore \(n\ge2\). The Laplacian uses one unit-conductance edge between every pair of vertices in different parts and no edges within a part. The norms are the unweighted, counting-measure \(\ell^1\) and \(\ell^\infty\) norms; no normalization by vertex degree occurs. The statements are not asserted for weighted, directed, normalized-Laplacian, or infinite graphs. A maximizing part size means a part size whose vertices achieve the maximum absolute row sum of \(-L H_t\).

## Proof

**Spectral decomposition.** For a part \(V_i\) of size \(m_i\), let \(J_i\) be the all-ones matrix on that block, extended by zero outside, and \(I_i\) the coordinate identity on the block. Write \(J\) for the global all-ones matrix and \(d_i=n-m_i\). The orthogonal projectors
\[
E_i=I_i-\frac{J_i}{m_i},\qquad
E_*=\sum_{i=1}^r\frac{J_i}{m_i}-\frac Jn,
\]
are pairwise orthogonal. On the range of \(E_i\), the Laplacian has eigenvalue \(d_i\); on the range of \(E_*\), eigenvalue \(n\); and on constants, eigenvalue zero. Thus
\[
L H_t=\sum_i d_i e^{-d_i t}E_i+n e^{-nt}E_*.
\]

**Exact absolute row sums.** Fix a vertex in part \(V_i\), and abbreviate \(m=m_i\), \(d=n-m\), \(a=e^{-dt}\), and \(b=e^{-nt}\). The corresponding row of \(L H_t\) has diagonal entry \(d((m-1)a+b)/m>0\); its \(m-1\) other entries within \(V_i\) are \(d(b-a)/m\le0\); and each of the \(d\) entries outside \(V_i\) equals \(-b<0\). Its absolute row sum is
\[
\frac d m\bigl((m-1)a+b\bigr)
+\frac{d(m-1)}m(a-b)+db
=\frac{2d}{m}\bigl((m-1)a+b\bigr).
\]
Every vertex has this form; hence the displayed operator-norm formula follows. The matrix is symmetric, giving equality of the \(\ell^1\) and \(\ell^\infty\) norms.

**Sharp universal coefficient and its equality cases.** For every \(\lambda>0\),
\[
\sup_{t>0} t e^{-\lambda t}=\frac1{e\lambda},
\]
attained uniquely when \(t=1/\lambda\). For a row from a size-\(m\) part,
\[
\begin{aligned}
t\frac{2d}{m}\bigl((m-1)e^{-dt}+e^{-nt}\bigr)
&\le \frac{2d}{em}\left(\frac{m-1}{d}+\frac1n\right)\\
&=\frac{2(n-1)}{en}.
\end{aligned}
\]
If \(m=1\), the first summand vanishes and the remaining rate is exactly \(n\); equality occurs precisely at \(t=1/n\). If \(m>1\), the two positive summands have distinct maximizing times \(1/d\ne1/n\); the inequality is strict at every \(t\). Since there are finitely many rows, each time-weighted row norm is continuous and tends to zero at both ends, so their maximum is strictly below the bound when all parts are larger than one. This also proves the unique maximizing time in the equality cases.

**Ordered pairwise crossings.** Suppress the common positive factor \(2e^{-nt}\) and put
\[
h_m(t)=\frac{n-m}{m}\left(1+(m-1)e^{mt}\right).
\]
For \(m\ge2\), its logarithmic derivative is
\[
\frac{d}{dt}\log h_m(t)
=\frac{m(m-1)e^{mt}}{1+(m-1)e^{mt}}\in[m-1,m),
\]
while the logarithmic derivative vanishes for \(m=1\). For every pair \(1\le a<b<n\) the logarithmic derivative of \(h_b/h_a\) is strictly positive. Also \(h_b(0)=n-b<n-a=h_a(0)\), while \(h_b(t)/h_a(t)\to\infty\) as \(t\to\infty\). There is therefore exactly one crossing. If a smaller size were to become a maximizer strictly after a larger one, the pairwise ratio monotonicity would be contradicted; hence the maximizing size is nondecreasing. Distinct sizes can each be entered at most once, giving the transition bound.

**Multiplicity blindness.** The norm formula maximizes over available values of \(m\), without using their multiplicities, once \(n\) is fixed. Both displayed graphs have \(n=20\) and distinct size set \(\{2,4,6\}\); thus their norm profiles agree identically. Their nonzero Laplacian eigenvalues include \(n-m\) with multiplicity \((m-1)\) per part of size \(m\), and \(n\) with multiplicity \(r-1\). The multiplicity of eigenvalue \(18\) is respectively one and two, proving their Laplacian spectra differ.

## Verification

The accompanying `check.py` constructs the unnormalized Laplacian matrices independently and evaluates \(L e^{-tL}\) using dense matrix exponentials. It checks the row formulas and endpoint norms for families of two- and three-part graphs with up to fourteen vertices, verifies the universal bound and pairwise crossing orientation, and confirms the exact profile coincidence and spectral discrepancy of the stated twenty-vertex examples. The program prints a passed-assertion count and requires NumPy and SciPy. It is supplementary numerical evidence; no finite computation is used to prove the statements for arbitrary part sizes or times.

## Relationship to prior work

Keller and Lenz (2009) establish the general finite- and infinite-graph heat semigroup framework, including the heat equation on \(\ell^\infty\). Oliveira, de Lima and Nikiforov (2014) analyze graph blow-up Laplacian spectra and eigenvectors. These underlying results provide context but, in their inspected discussions, do not give the complete multipartite **endpoint time-derivative row-norm envelope**, its optimal time-uniform coefficient and equality rigidity, or the multiplicity-blind spectral counterexample. In particular, eigenvalues alone do not determine the \(\ell^\infty\) row-sum norm. Related estimates for diagonal semigroups in \(\ell^2\) do not imply exact endpoint norms.

## Limitations

No claim is made of historical priority beyond the searched sources, nor of a universal bound for arbitrary graphs. The result is exact for this natural graph family only. The ordering theorem guarantees a monotone upper-envelope sequence but does **not** claim that every intermediate part size is visible as a global maximizer. The supplementary checker tests finitely many instances; independent mathematical and bibliographic validation remains outstanding.

## References

1. M. Keller and D. Lenz, *Dirichlet forms and stochastic completeness of graphs and subgraphs*, arXiv:0904.2985, first submitted 20 April 2009, especially the section on the heat equation on \(\ell^\infty\). https://arxiv.org/abs/0904.2985
2. C. Oliveira, L. de Lima and V. Nikiforov, *Spectra of the blow-up graphs*, arXiv:1412.0319, first submitted 1 December 2014, Theorem 3 and its proof. https://arxiv.org/abs/1412.0319
