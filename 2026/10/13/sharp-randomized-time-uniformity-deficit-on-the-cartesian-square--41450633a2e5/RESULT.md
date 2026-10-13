# Sharp randomized-time uniformity deficit on the Cartesian square of the three-vertex path

## Finding

Let \(G=P_3\square P_3\) be the Cartesian square of the ordinary three-vertex path. For its unweighted adjacency matrix \(A\), put \(M(t)_{uv}=|[\exp(itA)]_{uv}|^2\). Among **all** probability distributions \(\mu\) on nonnegative observation times, the exact global minimum of the squared Frobenius distance from uniform mixing is
\[
\min_{\mu}\left\|\mathbb E_{T\sim\mu}M(T)-\frac19J_9\right\|_F^2
=\frac{81r^4-108r^3+142r^2-60r+9}{16}
=0.0909764868554665\ldots,
\]
where \(r\) is the unique real root of
\[
81r^3-81r^2+71r-15=0,\qquad r=0.273128985745271\ldots.
\]
Every minimizing distribution induces precisely the balanced two-point law
\[
\mathbb P\{\cos(\sqrt2T)=\sqrt r\}
=\mathbb P\{\cos(\sqrt2T)=-\sqrt r\}=\tfrac12.
\]
In particular, the minimum is attained by equally weighted observation times
\[
t_+=\frac{\arccos(\sqrt r)}{\sqrt2},\qquad
 t_-=\frac{\pi-\arccos(\sqrt r)}{\sqrt2}.
\]
The underlying path itself can be made exactly uniform in average by another sampling law, but minimizing the deficit on its synchronized square requires a different second moment.

## Assumptions and scope

The graph is the simple unweighted nine-vertex grid \(P_3\square P_3\); the Hamiltonian is **adjacency**, not the combinatorial or normalized Laplacian. A single common random time \(T\ge0\) controls both Cartesian coordinates. The same distribution must work simultaneously for every initial and final vertex. The squared Frobenius norm counts all 81 matrix entries, with no normalization factor. No restriction on support size or smoothness is imposed. The optimization includes discrete, continuous, and mixed probability laws.

## Proof

**1. Reduce the walk to one cosine variable.** Let \(A_3\) be the adjacency matrix of \(P_3\). Since \(A_3^3=2A_3\), spectral functional calculus gives
\[
\exp(itA_3)=I+\frac{i\sin(\sqrt2t)}{\sqrt2}A_3
 +\frac{\cos(\sqrt2t)-1}{2}A_3^2.
\]
Writing \(x=\cos(\sqrt2t)\), its entrywise squared moduli are
\[
B(x)=\begin{pmatrix}
(1+x)^2/4&(1-x^2)/2&(1-x)^2/4\\
(1-x^2)/2&x^2&(1-x^2)/2\\
(1-x)^2/4&(1-x^2)/2&(1+x)^2/4
\end{pmatrix}.
\]
The Cartesian adjacency is \(A=A_3\otimes I_3+I_3\otimes A_3\), so commuting exponentials yield \(M(t)=B(x)\otimes B(x)\).

**2. Reflection never worsens the objective.** Let \(P\) swap the two endpoints of \(P_3\). Directly, \(B(-x)=B(x)P\). Thus the global objective for a law of \(x\) equals that of its reflection \(x\mapsto-x\), since \(P\otimes P\) permutes columns and fixes \(J_9\). Convexity of the squared Frobenius distance implies that averaging the law with its reflection cannot increase its objective. Every law of \(x\in[-1,1]\) is realizable by nonnegative times, because \(t=\arccos(x)/\sqrt2\) works. Hence global minimization may be performed over symmetric laws of \(x\).

**3. Two moments completely determine the symmetric-law objective.** Set \(s=\mathbb E[x^2]\) and \(q=\mathbb E[x^4]\). The moment domain obeys
\[
0\le s\le1,\qquad s^2\le q\le s.
\]
Expanding all 81 entries of \(\mathbb E[B(x)\otimes B(x)]-J_9/9\) and squaring gives the exact identity
\[
\Phi(s,q)=\frac{81q^2-108sq+18q+124s^2-60s+9}{16}.
\]
For fixed \(s\),
\[
\frac{\partial\Phi}{\partial q}=\frac98(9q-6s+1)
\ge\frac98(3s-1)^2\ge0.
\]
The inequality is strict for every \(q>s^2\) (even when \(s=1/3\)). Thus every optimum must have \(q=s^2\), i.e. \(x^2=s\) almost surely. Every such point is attainable by a two-point law supported on \(\{\pm\sqrt s\}\).

**4. Exact one-variable minimization.** Substituting \(q=s^2\) leaves
\[
h(s)=\frac{81s^4-108s^3+142s^2-60s+9}{16},\qquad
 h'(s)=\frac{81s^3-81s^2+71s-15}{4}.
\]
The cubic numerator \(g(s)\) has strictly positive derivative
\[
g'(s)=243(s-1/3)^2+44>0
\]
for every real \(s\); also \(g(0)=-15<0\) and \(g(1)=56>0\). Therefore a unique \(r\in(0,1)\) minimizes \(h\) globally. Evaluating \(h(r)\) proves the stated formula and decimal.

**5. Uniqueness of the optimal cosine law.** Equality in the strict-convexity symmetrization step forces the averaged 9-by-9 matrix to equal its reflected copy. Because \(q=s^2\) at every minimizer, \(x\) is supported on the two points \(\pm\sqrt r\). A nonbalanced choice of their weights makes the matrix unequal to its reflected copy (for example compare its \(((1,1),(1,1))\) and \(((1,1),(3,3))\) entries), so the weights must both be \(1/2\). Multiple physical times producing the same cosine value remain equivalent; uniqueness is asserted only for the cosine pushforward, not for the raw law of \(T\).

**6. Why the factor-optimal law is different.** The known exact uniform-average-mixing condition for \(P_3\) forces \(\mathbb E[x]=0\) and \(\mathbb E[x^2]=1/3\). Symmetric laws meeting it exist; for their synchronized product, \(q\ge1/9\), and Step 3 shows the smallest possible squared deficit is \(h(1/3)=1/9\), strictly larger than \(h(r)\). Thus exact uniformity of the expected **factor** matrix does not optimize uniformity of the expected **product** matrix under a shared clock.

## Verification

The accompanying standalone `verify.py` rebuilds the single-path evolution from \(A_3^3=2A_3\), the 81-entry Cartesian matrix and its polynomial moment average, and checks the objective and cubic derivative as exact symbolic identities. It then evaluates the two optimal times using an independent matrix exponential of the original nine-vertex adjacency matrix and checks that the resulting objective agrees numerically with the exact formula. Run `python3 verify.py` with Python, SymPy, NumPy, and SciPy installed. The numerical test is a consistency check; the all-distributions optimum follows from the proof above.

## Relationship to prior work

Baptista, Coutinho and Marques, *Unexpected Averages of Mixing Matrices* (arXiv:2308.16378v1, August 31, 2023), §3.2, explicitly construct probability laws giving exact uniform average mixing on \(P_3\). Their §5 (especially Equation (7), Theorem 17 and Corollaries 18–20) establishes Cartesian mixing factorization and trace/covariance bounds and warns that a shared observation clock does **not** tensorize independently averaged matrices. Neither section computes the unrestricted squared Frobenius optimum for \(P_3\square P_3\) or its unique optimal cosine law. Their identity is used here as a starting point, not claimed as new.

Coutinho and Guo, *Selected Open Problems in Continuous-Time Quantum Walks* (arXiv:2404.02236v1, §4.2), surveys alternative average mixing matrices and motivates quantitative questions; it does not contain this nine-vertex sharp optimization. Lo et al., *Mixing of Quantum Walk on Circulant Bunkbeds* (arXiv:quant-ph/0509059v1, §§2 and 5), treats different asymptotic, big-O average uniformity notions and Cartesian products involving circulants; it does not characterize arbitrary-time-law Frobenius distance for \(P_3\square P_3\).

## Limitations

The theorem concerns exactly this unweighted nine-vertex Cartesian square and the specific squared Frobenius global-uniformity metric. It does not classify all Cartesian products, optimize other divergences, or assert uniqueness of observation times modulo the cosine map. Existing factorization and qualitative covariance observations remain prior results. Although direct source and semantic database comparisons did not locate an equivalent exact formula, a stronger unlocated quantitative theorem could still imply it. No independent validation has been performed.

## References

1. P. Baptista, G. Coutinho, V. Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378v1 (first publicly posted August 31, 2023), https://arxiv.org/html/2308.16378v1.
2. G. Coutinho, K. Guo, *Selected Open Problems in Continuous-Time Quantum Walks*, arXiv:2404.02236v1 (April 2, 2024), https://arxiv.org/html/2404.02236v1.
3. P. Lo, S. Rajaram, D. Schepens, D. Sullivan, C. Tamon, J. Ward, *Mixing of Quantum Walk on Circulant Bunkbeds*, arXiv:quant-ph/0509059v1 (September 8, 2005), https://arxiv.org/html/quant-ph/0509059v1.
