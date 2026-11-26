# Complete multipartite heat flow: the sharp endpoint coefficient and all active part sizes

## Finding

Let \(G=K_{m_1,\ldots,m_r}\) be a finite simple unweighted complete multipartite graph, with \(r\ge2\), positive integer part sizes \(m_i\), and \(n=\sum_i m_i\). Write \(S\) for the set of distinct part sizes. Let \(L=D-A\) be the combinatorial Laplacian, and \(H_t=e^{-tL}\). For real or complex functions with counting-measure norms and every \(t>0\),
\[
f_G(t):=\|\partial_t H_t\|_{\ell^\infty\to\ell^\infty}
=\|\partial_t H_t\|_{\ell^1\to\ell^1}
=\max_{m\in S} f_m(t),\qquad
f_m(t)=\frac{2(n-m)}m\big((m-1)e^{-(n-m)t}+e^{-nt}\big).
\]
Moreover,
\[
\sup_{t>0}t f_G(t)\le \frac{2(n-1)}{en}.
\]
Equality holds exactly when some part is a singleton, equivalently when the graph has a universal vertex, and then the unique maximizing time is \(1/n\).

For any two distinct sizes \(a<b\) in \(S\), their row norms cross at a unique positive time \(t_{a,b}\); \(f_a>f_b\) before that time and \(f_b>f_a\) after it. In the global maximum the sizes occur in strictly increasing order **without any omissions**: if \(S=\{m_1'<\cdots<m_k'\}\), the transitions are precisely at the \(k-1\) strictly increasing adjacent-size crossing times \(t_{m_i',m_{i+1}'}\). Between these times the maximizing size is unique; at a transition just the two neighboring sizes maximize. If \(k=1\) the unique size maximizes throughout.

The entire endpoint norm profile determines, and is determined by, the pair \((n,S)\). It need not determine the multiplicity of each size, or the Laplacian spectrum: \(K_{2,4,4,4,6}\) and \(K_{2,2,4,6,6}\) have the same profile and different spectra.

## Assumptions and scope

This uses the unnormalized Laplacian on the vertices, with unit edge weights and counting measure. It does not assert corresponding results for normalized Laplacians, weighted or directed graphs, or infinite graphs. A maximizing size is a size whose part vertices attain the largest absolute row sum of \(-L H_t\).

## Proof

**Decomposition and absolute row sums.** Put \(d_i=n-m_i\). Let \(I_i\) and \(J_i\) denote the identity and all-ones matrices on part \(i\), extended by zero elsewhere; let \(J\) denote the global all-ones matrix. The orthogonal projectors \(E_i=I_i-J_i/m_i\) project onto the within-part zero-sum functions; \(E_*=\sum_i J_i/m_i-J/n\) projects onto the partwise constant zero-sum functions. The Laplacian has eigenvalues \(d_i\) on the first spaces, \(n\) on the second, and zero on constants: indeed \(L=nI-J-\sum_i m_i E_i\). Hence
\[
L H_t=\sum_i d_i e^{-d_i t}E_i+n e^{-nt}E_*.
\]
For a vertex in a part of size \(m\), write \(d=n-m\), \(A=e^{-dt}\), \(B=e^{-nt}\). The diagonal entry is \(d((m-1)A+B)/m>0\), the other entries within the part equal \(d(B-A)/m\le0\), and those outside equal \(-B<0\). The row sum is zero, so its absolute row sum is twice the diagonal, namely \(f_m(t)\). The \(\ell^\infty\) induced norm is the maximum absolute row sum, and symmetry gives the same maximum absolute column sum for \(\ell^1\).

**Sharp time-scaled bound.** For every positive \(\lambda\), the function \(te^{-\lambda t}\) has its unique maximum \(1/(e\lambda)\) at \(t=1/\lambda\). Applying this to the two terms gives
\[
t f_m(t)\le \frac{2d}{em}\left(\frac{m-1}{d}+\frac1n\right)=\frac{2(n-1)}{en}.
\]
For \(m=1\) the only nonzero summand gives equality precisely at \(1/n\). For \(m>1\) the two positive terms peak at different times, so the bound is pointwise strict. The continuous finite maximum of the time-weighted rows tends to zero both as \(t\downarrow0\) and as \(t\to\infty\), so attains its positive maximum at a finite positive time. This proves strictness when no part is a singleton and uniqueness of the maximizing time otherwise.

**Individual crossings.** Divide the rows by \(2e^{-nt}\) and set \(h_m(t)=(n-m)(1+(m-1)e^{mt})/m\). The logarithmic derivative in time is zero for \(m=1\), and for \(m\ge2\) it is
\[
\partial_t\log h_m(t)=\frac{m(m-1)e^{mt}}{1+(m-1)e^{mt}}\in[m-1,m).
\]
For integer \(a<b\) this makes \(h_b/h_a\) strictly increasing. The ratio is less than one at zero because \(h_m(0)=n-m\), and tends to infinity at late times. This proves the unique crossing and its direction.

**Visibility of every size.** For this step extend \(m\) to real \(1\le m<n\), at a fixed \(t>0\). Write
\[
h_m(t)=(n-m)e^{mt}(1-g_t(m)),\qquad
g_t(m)=\frac{1-e^{-mt}}{m}=\int_0^t e^{-mu}\,du.
\]
Here \(0<g_t(m)<1\) and \(g_t''(m)=\int_0^t u^2 e^{-mu}\,du>0\). Thus \(\log(1-g_t)\) has strictly negative second derivative and \(\log h_m=\log(n-m)+mt+\log(1-g_t)\) is strictly concave in \(m\). If \(a<b<c\), then at the crossing \(t_{a,c}\) the middle row is strictly larger than the equal outer rows. The crossing directions give
\[
t_{a,b}<t_{a,c}<t_{b,c}.
\]
In particular successive adjacent-size crossings are strictly ordered. Between adjacent crossings for a given size (using zero and infinity at the ends), that size beats each other size: the crossing with any smaller size is no later than the preceding adjacent crossing, and the crossing with any larger size is no earlier than the following one, by the triple inequality. At an adjacent crossing the inequalities with all other sizes are strict by the same argument. This proves the asserted envelope description.

**What the profile determines.** Dependence on \((n,S)\) is immediate from the formula. To recover \(n\), use the last active row. If the graph is complete (all singleton parts), the profile is a single exponential of rate \(n\). Otherwise the late-time profile is a sum of two distinct exponentials with positive coefficients, and its larger rate is \(n\). These cases and rates can be distinguished from the exact tail: the slowest rate is \(-\lim_{t\to\infty}t^{-1}\log f_G(t)\), and multiplying by the compensating exponential and taking the limit gives its coefficient. After subtracting this term the tail is either zero or has the other rate, recoverable by the same limit. With \(n\) fixed, each size \(m\) is active on an open interval. If two graphs have equal profiles, shrink such an interval to avoid the other graph's finitely many transitions; their analytic row functions then agree on this subinterval, hence everywhere. Their values at zero are \(2(n-m)\), so the sizes coincide. Applying this to each graph recovers exactly \(S\).

Both example graphs have \(n=20\) and \(S=\{2,4,6\}\). Their eigenvalue \(18\) has multiplicity one and two, respectively, because each part of size two contributes one dimension to its eigenspace. The Laplacian spectra therefore differ.

## Verification and limitations

The analytical proofs of the row formula, time-scaled bound, visibility, and recovery above establish the statements for all admissible graphs. The supplementary `check.py` from the original package constructs the Laplacian directly and checks its exponential against the row formula on finite examples. It also tests crossing direction and the equal-profile, unequal-spectrum example. It uses NumPy and SciPy and is not a proof of universal statements; in particular visibility follows from strict concavity, not from numerical root comparisons.

General graph heat semigroup theory and the Laplacian spectra of blow-up graphs provide the setting and the spectral ingredient. The exact endpoint norm also requires the entrywise sign calculation, and the transition and recovery claims rely on the comparison of the size-indexed rows. There is no assertion of historical priority.

## References

1. M. Keller and D. Lenz, *Dirichlet forms and stochastic completeness of graphs and subgraphs*, arXiv:0904.2985. https://arxiv.org/abs/0904.2985
2. C. Oliveira, L. de Lima and V. Nikiforov, *Spectra of the blow-up graphs*, arXiv:1412.0319, Theorem 3. https://arxiv.org/abs/1412.0319
