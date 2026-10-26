# A sharp positivity transition for fractional graph heat on complete multipartite networks

## Finding
For any finite connected complete multipartite graph that is not complete, the fractional heat operators \(T_\alpha(t)=\exp(-tL^\alpha)\) change their positivity behavior exactly at \(\alpha=1\). They are entrywise strictly positive for every \(t>0\) if \(0<\alpha\leq1\); if \(\alpha>1\), they have negative entries at every sufficiently small positive time but become entrywise nonnegative permanently at one explicitly determined finite time. The exact sharp \(\ell^1\) and \(\ell^\infty\) norms and their global transient maxima are given below. Close to \(\alpha=1\), the positivity delay is linear in \(\alpha-1\), whereas the peak norm excess is quadratic; both leading coefficients are explicit in the part sizes.

Write \(G=K_{n_1,\ldots,n_r}\), where \(r\ge2\), \(n_i\ge1\), \(N=\sum_i n_i\), and some \(n_i\ge2\). Put \(u_i=n_i/N\), \(q_i=1-u_i\), and \(s=N^\alpha t\). Define
\[
H_i(\alpha,s)=u_i+q_i e^{-s}-e^{-q_i^\alpha s}.
\]
For \(\alpha>1\) and \(n_i\ge2\), \(H_i(\alpha,s)\) has a unique positive zero \(s_i^{\mathrm{end}}\), and
\[
\boxed{\tau_\alpha=N^{-\alpha}\max_{i:n_i\ge2}s_i^{\mathrm{end}}.}
\]
Entrywise nonnegativity holds exactly for \(t=0\) and \(t\ge\tau_\alpha\); it is strict for \(t>\tau_\alpha\). At all times, putting \([y]_+=\max\{y,0\}\),
\[
\boxed{\|T_\alpha(t)\|_{\ell^1\to\ell^1}=\|T_\alpha(t)\|_{\ell^\infty\to\ell^\infty}
=1+2\max_{i:n_i\ge2}\left(1-\frac1{n_i}\right)[-H_i(\alpha,N^\alpha t)]_+.}
\]
For \(\alpha>1\), the unique maximum of the \(i\)-th contribution occurs at
\[
\vartheta_i=\frac1{N^\alpha}\frac{(\alpha-1)(-\log q_i)}{1-q_i^\alpha},
\]
with \(E_i=\exp(-q_i^\alpha N^\alpha\vartheta_i)-u_i-q_i\exp(-N^\alpha\vartheta_i)>0\). Thus the sharp global peak is
\[
\boxed{\sup_{t\ge0}\|T_\alpha(t)\|_{\ell^\infty\to\ell^\infty}
=1+2\max_{i:n_i\ge2}\left(1-\frac1{n_i}\right)E_i.}
\]
Every displayed operator norm is attained by a sign choice on one corresponding matrix row (or column). Different parts may compete for the global time maximizer, so no uniqueness of the maximizing time is asserted.

For this fixed graph, as \(\varepsilon=\alpha-1\downarrow0\), set
\[
A_G=\frac2N\max_{i:n_i\ge2}\frac{-\log q_i}{u_i},\qquad
B_G=\max_{i:n_i\ge2}\left(1-\frac1{n_i}\right)\frac{q_i(\log q_i)^2}{u_i}.
\]
Then \(A_G,B_G>0\) and
\[
\boxed{\tau_{1+\varepsilon}=A_G\varepsilon+O_G(\varepsilon^2),\qquad
\sup_{t\ge0}\|T_{1+\varepsilon}(t)\|_{\infty\to\infty}
=1+B_G\varepsilon^2+O_G(\varepsilon^3).}
\]
For each non-singleton part, its individual positivity-ending time is asymptotically twice its own peak time. The maximum in \(A_G\) is attained precisely at the largest non-singleton part sizes, because \(-\log(1-u)/u\) is strictly increasing for \(0<u<1\).

## Assumptions and scope
All edges have unit weight. The Laplacian is the unnormalized positive semidefinite combinatorial matrix \(L=D-A\), and \(L^\alpha\) is defined by the nonnegative spectral functional calculus, with the zero eigenvalue raised to any positive power interpreted as zero. All norms use counting measure on vertices, without degree normalization. The graph is connected and noncomplete: \(r\ge2\), at least one \(n_i\ge2\). These definitions and conclusions hold for every real \(\alpha>0\) and \(t\ge0\), and the asymptotic formulas keep the graph fixed while \(\alpha\downarrow1\) from above. No assertion is made about an arbitrary graph or a directed or normalized Laplacian.

## Proof
Let \(J\) denote the all-ones matrix, and let \(J_i\) denote the all-ones matrix on part \(i\), extended by zero outside that part; similarly \(I_i\) is the identity restricted to part \(i\). The orthogonal decomposition into constant vectors, part-constant vectors of global mean zero, and within-part mean-zero vectors diagonalizes \(L\): the eigenvalues are respectively \(0\), \(N\), and \(N-n_i=Nq_i\). Consequently,
\[
T_\alpha(t)=\frac JN+e^{-N^\alpha t}\left(\sum_i\frac{J_i}{n_i}-\frac JN\right)
+\sum_i e^{-(N-n_i)^\alpha t}\left(I_i-\frac{J_i}{n_i}\right).
\]
The entries between different parts equal \((1-e^{-s})/N\), strictly positive for \(t>0\). Distinct vertices in part \(i\) have matrix entry \(H_i(\alpha,s)/n_i\). The diagonal entry in that part equals \(H_i(\alpha,s)/n_i+e^{-q_i^\alpha s}>0\); the latter is also evident from the spectral sum of nonnegative squares. Every row sums to one, and the kernel is symmetric. Therefore its maximum absolute row sum (and column sum) is exactly \(1+2\max_i (n_i-1)[-H_i/n_i]_+\). Choosing input signs equal to the signs of an attaining row gives the sharp \(\ell^\infty\) norm, and symmetry gives the sharp \(\ell^1\) norm.

For \(\alpha\le1\), \(q_i^\alpha\ge q_i\). Strict convexity of the exponential gives \(u_i+q_i e^{-s}>e^{-q_i s}\ge e^{-q_i^\alpha s}\) for \(s>0\). Thus every entry is strictly positive. For \(\alpha>1\), put \(a_i=q_i^\alpha<q_i\), and multiply \(H_i\) by \(e^{a_i s}\):
\[
e^{a_i s}H_i(\alpha,s)=u_i e^{a_i s}+q_i e^{-(1-a_i)s}-1.
\]
This function is strictly convex, equals zero at \(s=0\), has derivative \(a_i-q_i<0\) there, and diverges to \(+\infty\). It therefore has exactly one positive zero, being negative before and positive after it. The maximum of \(-H_i\) is found by differentiating \(e^{-a_i s}-u_i-q_i e^{-s}\); its derivative changes sign once at \(s=(\log(q_i/a_i))/(1-a_i)\). This proves the finite-time and peak formulas, including the asserted sign pattern.

Finally write \(\varepsilon=\alpha-1\) and \(\delta_i=q_i-q_i^{1+\varepsilon}=-\varepsilon q_i\log q_i+O(\varepsilon^2)\). The positive root is \(O(\varepsilon)\), and Taylor expansion of the equality \(H_i=0\), after dividing by its nonzero root, gives
\[
s_i^{\mathrm{end}}=\frac{2\delta_i}{q_i u_i}+O(\varepsilon^2)
=\frac{-2\log q_i}{u_i}\varepsilon+O(\varepsilon^2).
\]
The peak satisfies \(s_i^{\mathrm{peak}}=\delta_i/(q_i u_i)+O(\varepsilon^2)\), and its excess is \(E_i=\delta_i^2/(2q_i u_i)+O(\varepsilon^3)=\varepsilon^2 q_i(\log q_i)^2/(2u_i)+O(\varepsilon^3)\). Since the graph has finitely many parts and \(N^{-(1+\varepsilon)}=N^{-1}(1+O(\varepsilon))\), taking the finite maxima gives exactly \(A_G\) and \(B_G\). The derivative of \(-\log(1-u)/u\) has numerator \(u/(1-u)+\log(1-u)>0\) (by elementary integration), proving the final largest-part statement.

## Verification
The accompanying `checker.py` reconstructs the combinatorial Laplacian directly, diagonalizes it numerically, and independently compares \(\exp(-tL^\alpha)\) with the three-eigenspace block formula on a large sample of balanced and unbalanced complete multipartite graphs. It compares entrywise values, row sums, exact-row formulas, positivity regimes, computed threshold and peak times, and near-critical coefficients. It completed 11,556 assertions successfully using NumPy and SciPy. Numerical tests do not prove any infinite-parameter statement; those follow from the preceding spectral and analytic arguments. Reproduce using `python checker.py` with NumPy and SciPy available.

## Relationship to prior work
Riascos and Mateos (2014/2015) develop fractional graph diffusion by spectral powers and study \(0<\alpha<1\), especially random walks on rings; the full accessible 2015 manuscript does not supply an \(\alpha>1\) positivity cutoff or a critical-onset law for complete multipartite graphs. Daners, Glück, and Kennedy (2015) give general qualitative eventual-positivity criteria for semigroups, which do not supply these exact graph-dependent times, endpoint norms, or the linear/quadratic singular onset. Previously established special formulas for squared-Laplacian heat on complete bipartite graphs are recovered at \(\alpha=2\), \(r=2\); those special-case formulas are not claimed here as new. A published theorem about positivity intervals with at most three spectral levels explains a general qualitative restriction, but its abstract-level comparison does not establish the multi-parameter fractional expansion given here.

## Limitations
The numerical verification is finite and does not establish historical priority. The exact full-text comparison was available for Riascos–Mateos and the cited general eventual-positivity papers, but not for every potentially related specialist source; a relevant published three-spectral-level finding was available for summary-level rather than full-text inspection. The expansion is pointwise in the fixed graph and makes no claim uniform in graph size. The natural complete-graph case (all parts singleton) has a positive semigroup for all exponents and is expressly excluded from the critical transition.

## References
1. A. P. Riascos and J. L. Mateos, "Fractional dynamics on networks: Emergence of anomalous diffusion and Lévy flights," *Physical Review E* **90**, 032809 (17 September 2014), DOI 10.1103/PhysRevE.90.032809; lawful full text arXiv:1506.06167 (19 June 2015), especially Sections II–IV.
2. D. Daners, J. Glück, and J. B. Kennedy, "Eventually and asymptotically positive semigroups on Banach lattices," arXiv:1511.05294, 17 November 2015, especially Sections 1, 5 and 6.
3. D. Daners, J. Glück, and J. B. Kennedy, "Eventually Positive Semigroups of Linear Operators," arXiv:1511.09020, 29 November 2015, especially Introduction and eventual-positivity criteria.
4. "A three-spectral-value barrier for gaps in positivity times of self-adjoint semigroups," published mathematical finding (2026); only an abstract-level comparison was possible.
