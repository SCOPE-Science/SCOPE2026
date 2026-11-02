# Balancing inversion for generalized roundness of two-heavy-part multipartite graph metrics

## Finding

Fix integers \(r\ge3\) and \(u\ge4\). For positive integers \(a,b\) satisfying \(a+b=u\), let \(G_{r;a,b}=K_{a,b,1,\ldots,1}\) denote the complete \(r\)-partite graph with \(r-2\) singleton parts, equipped with unit-edge shortest-path distance \(d\). Write \(\wp(G)\) for its supremal exponent of negative type: the supremum of \(p\ge0\) for which
\[
\sum_{x,y\in V(G)}d(x,y)^p\alpha_x\alpha_y\le0
\quad\text{for all real }\alpha\text{ with }\sum_x\alpha_x=0.
\]

Put \(v=ab\), \(T=(r-1)u+2v\), and \(C=u+r-2\). Define
\[
\mu_{r,u}(v)=\frac{T-\sqrt{T^2-4rvC}}{2rv}.
\]
Then \(0<\mu_{r,u}(v)<1\), and the exact negative-type exponent is
\[
\boxed{\wp(G_{r;a,b})=-\log_2\bigl(1-\mu_{r,u}(ab)\bigr).}
\]
The exponent is attained: the powered distance kernel has negative type at \(p=\wp(G_{r;a,b})\), and fails to have negative type at every larger exponent.

**Balance-reversal theorem.** At fixed \((r,u)\), increasing \(ab\) (making the two non-singleton-eligible part sizes more balanced) has three sharply different effects:

- If \(u>r\), it strictly *decreases* \(\wp\).
- If \(u<r\), it strictly *increases* \(\wp\).
- If \(u=r\), it leaves \(\wp\) unchanged, with the exact common value \(\log_2\bigl(r/(r-2)\bigr)\).

Consequently, except on the equality line, the most balanced split and the extreme split \((1,u-1)\) are the unique opposite optimizers, up to exchanging \(a,b\). At \(u=r\), every split has the same critical exponent, although its part-size profile may differ.

For example, with \(u=4\) the extreme split \((1,3)\) and the balanced split \((2,2)\) have respectively
\[
\begin{array}{c|cc}
 r &\wp(G_{r;1,3})&\wp(G_{r;2,2})\\\hline
 3 &\log_2(9/4)&1\\
 4 &1&1\\
 5 &\log_2(15/8)&1.
\end{array}
\]
Thus the strict ordering reverses when the number of parts passes the fixed total \(u\).

## Assumptions and scope

The vertex set is finite and carries its **graph shortest-path metric**; distances are \(1\) across distinct parts and \(2\) between distinct vertices in the same part. There are exactly \(r-2\) singleton parts, with \(a,b\ge1\). The real zero-sum definition of negative type is used, including equality at the critical exponent. The name “generalized roundness” is used for this same supremal negative-type exponent, as in the standard finite-metric convention. A finite metric \((V,d^{p/2})\) embeds isometrically into a Hilbert space precisely when \(d^p\) is conditionally negative semidefinite.

## Proof

**1. Exact quadratic-form reduction.** Let \(n_1=a,n_2=b,n_3=\cdots=n_r=1\), let \(V_i\) denote the parts, and let \(\alpha_x\in\mathbb R\) satisfy \(\sum_x\alpha_x=0\). Set \(s_i=\sum_{x\in V_i}\alpha_x\), so \(\sum_i s_i=0\), and set \(q=2^p\). Expanding the distance-power matrix gives the exact identity
\[
\sum_{x,y}d(x,y)^p\alpha_x\alpha_y
=(q-1)\sum_{i=1}^r s_i^2-q\sum_x\alpha_x^2.
\]
Cauchy–Schwarz within each part gives \(\sum_{x\in V_i}\alpha_x^2\ge s_i^2/n_i\), with equality for constant values on each part. Thus the negative-type inequality holds for **every** \(\alpha\) if and only if
\[
(q-1)\sum_i s_i^2\le q\sum_i\frac{s_i^2}{n_i}
\quad\text{for every }s\in\mathbb R^r,\ \sum_i s_i=0.
\]
Let
\[
\mu=\min_{s\ne0,\ \sum_i s_i=0}
\frac{\sum_i s_i^2/n_i}{\sum_i s_i^2}.
\]
Then the condition is exactly \(q\le(1-\mu)^{-1}\). This threshold is included because the constrained Rayleigh quotient attains its minimum, and above it the equality-form partwise-constant vector violates negative type.

**2. Two-variable eigenvalue.** On the subspace in which the \(r-2\) singleton coordinates sum to zero and the first two coordinates vanish, the Rayleigh quotient equals \(1\). By averaging over permutations of the singleton coordinates and the Rayleigh quotient minimax decomposition, the smallest quotient lies in the invariant subspace \(s=(x,y,z,\ldots,z)\), with \(z=-(x+y)/(r-2)\). There the quotient is
\[
\frac{x^2/a+y^2/b+(x+y)^2/(r-2)}
{x^2+y^2+(x+y)^2/(r-2)}.
\]
The generalized eigenvalue determinant of the two displayed quadratic forms simplifies, using \(a+b=u\) and \(ab=v\), to
\[
F(\mu,v)=rv\mu^2-\bigl((r-1)u+2v\bigr)\mu+u+r-2=0.
\]
The lower root is the minimum. Indeed, its counterpart (the upper root) is strictly greater than \(2/r\): the test vector \(x=y=1\), \(z=-2/(r-2)\), has quotient
\[
\frac{(r-2)(1/a+1/b)+4}{2r}>\frac2r.
\]
The lower root lies in \((0,1)\), since the original constrained Rayleigh quotient is positive and choosing \(s_1=1,s_2=-1\) gives quotient \(\tfrac12(1/a+1/b)<1\) (as \(u\ge4\)). This proves the radical formula and the exact exponent.

**3. The sign-changing comparison.** Substitution at the distinguished value \(2/r\) yields
\[
F(2/r,v)=(r-2)\bigl(1-u/r\bigr).
\]
Since the upper root exceeds \(2/r\), the lower root is less than, equal to, or greater than \(2/r\) precisely as \(u>r\), \(u=r\), or \(u<r\). Its discriminant is strictly positive. Implicit differentiation of \(F(\mu,v)=0\) at the lower root gives
\[
\frac{\partial\mu}{\partial v}=
\frac{\mu(r\mu-2)}{\sqrt{T^2-4rvC}}.
\]
Therefore the derivative is negative, zero, or positive in exactly the three regimes stated. Because \(p=-\log_2(1-\mu)\) is strictly increasing in \(\mu\), the same trichotomy applies to \(\wp\). On the equality line \(\mu=2/r\) for every admissible \(v\), giving \(p=\log_2(r/(r-2))\). Finally, among positive integer splits with fixed sum, \(v=a(u-a)\) increases strictly as \(a\) runs from \(1\) to \(\lfloor u/2\rfloor\). This proves the optimizer and uniqueness assertions.

## Verification

The included `verify.py` checks the exact characteristic equation and its sign trichotomy for \(1308\) parameter combinations, checks \(1080\) adjacent-balancing comparisons, and independently diagonalizes \(133\) full vertex distance-power matrices on their zero-sum subspaces at, above, and below the predicted critical exponent. Six exact rational cases verify the three regimes for a fixed four-vertex heavy-part budget. These finite checks are diagnostics, not a proof of the all-parameter statement; the proof is the preceding Rayleigh-quotient reduction and derivative argument. The program requires Python 3 and NumPy.

## Relationship to prior work

Sánchez (2011, Theorem 3.1) calculates supremal negative type for complete **bipartite** metric graphs using the established finite-distance-matrix method, and cites the older Euclidean-embedding work of Deza and Maehara. Deza and Grishukhin (2000) study general two-distance embeddings, spectral calculations, and multipartite-related distance structures. Thus neither the concept of supremal negative type nor the use of distance matrices or spectral reductions is claimed as new. The present result concerns the **strict reversal of the ordering between allocations of two variable parts under a fixed vertex budget when singleton parts are varied**, including its equality locus \(u=r\). Those fixed-budget comparison statements are not stated in the portions of the primary works that were available and inspected. An older general formula could conceivably imply the phase diagram after further algebra; this is a residual originality risk, rather than evidence of established coverage.

## Limitations

The classification applies only to finite unweighted, unit-edge complete multipartite graphs with at most two parts of size exceeding one. It does not classify arbitrary multipartite part vectors, weighted metrics, nonlinear metric embeddings outside Hilbert snowflakes, or graph interiors. No assertion of independently verified novelty is made. The full text of Deza–Maehara's 1990 primary paper could not be inspected, so an implicit equivalent balance comparison there cannot be excluded.

## References

1. Stephen Sánchez, “On the supremal \(p\)-negative type of a finite metric space,” arXiv:1108.0451, version 1 publicly dated 2011-08-02. Sections 2–3, especially Theorem 3.1 (complete bipartite case).
2. Michel Deza and Viacheslav Grishukhin, “Hypermetric two-distance spaces,” 2000. Available author-posted mathematical text (two-distance spectral and embedding criteria).
3. Michel Deza and Hiroshi Maehara, “Metric transforms and Euclidean embeddings,” *Transactions of the American Mathematical Society* 317 (1990), DOI: 10.1090/S0002-9947-1990-0974513-6. Historical comparator; full text was not available for inspection.
