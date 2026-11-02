# A common-neighbor phase transition in two-round stochastic mixing on strongly regular graphs

## Finding
Let \(G\) be a connected, simple, noncomplete strongly regular graph with parameters \((N,d,\lambda,\mu)\), adjacency matrix \(A\), and combinatorial Laplacian \(L=dI-A\). In two successive rounds, apply the spatially homogeneous symmetric Markov kernels
\[
P(t)=I-tL=(1-dt)I+tA,\qquad 0\le t\le \frac1d.
\]
For \(p,q\) in this interval set \(R(p,q)=\|P(q)P(p)-J/N\|_2\), where \(J\) is the all-ones matrix. Define
\[
r=\frac{\lambda-\mu+\sqrt{(\lambda-\mu)^2+4(d-\mu)}}2.
\]
The globally minimum two-round contraction **within this exact homogeneous, individually stochastic class** is
\[
\boxed{\min_{0\le p,q\le1/d}R(p,q)=
\begin{cases}
(r/d)^2,&\lambda\ge\mu,\\[3pt]
\dfrac{d-\mu}{d(d+\mu-\lambda)},&\lambda<\mu.
\end{cases}}
\]
The unique optimal unordered pair of round gains is
\[
\boxed{\{p,q\}=\begin{cases}
\{1/d,1/d\},&\lambda\ge\mu,\\
\{1/d,1/(d+\mu-\lambda)\},&\lambda<\mu.
\end{cases}}
\]
In the strictly accelerated phase \(\lambda<\mu\), writing \(R_*\) for the displayed minimum, the complete two-round transition matrix satisfies the stronger entrywise identity
\[
\boxed{P(q)P(p)=R_*I+(1-R_*)J/N.}
\]
The same mean-field form holds at \(\lambda=\mu\), whereas when \(\lambda>\mu\) it is impossible for any nonidentity admissible two-round product. A fixed gain repeated twice is optimal exactly when \(\lambda\ge\mu\); for \(\lambda<\mu\) the stated unequal gains improve its contraction strictly. In the complete-multipartite case \(\mu=d\), the accelerated contraction is zero, giving **exact average consensus in two individually stochastic rounds**.

## Assumptions and scope
A noncomplete strongly regular graph here has \(0<d<N-1\), is connected, and every adjacent vertex pair has exactly \(\lambda\) common neighbors while every nonadjacent pair has exactly \(\mu>0\) common neighbors. Its adjacency matrix obeys
\[
A^2=(d-\mu)I+(\lambda-\mu)A+\mu J.
\]
All vertices share one gain \(t\) in each round, although the two rounds may differ. Since \(P(t)\) has off-diagonal entries \(t\) precisely on the edges and diagonal \(1-dt\), its entrywise nonnegativity and row-stochasticity are equivalent to \(0\le t\le1/d\). The objective is the centered Euclidean operator norm after **exactly two rounds**, not total-variation mixing time, arbitrary edge-by-edge transition design, or unconstrained polynomial filtering. Edges not present in \(G\) remain unavailable in each individual round.

## Proof
The strong-regularity identity and \(AJ=dJ\) imply that on the orthogonal complement of constants the adjacency eigenvalues are the two roots
\[
r=\frac{\lambda-\mu+\sqrt{(\lambda-\mu)^2+4(d-\mu)}}2,
\quad s=\frac{\lambda-\mu-\sqrt{(\lambda-\mu)^2+4(d-\mu)}}2.
\]
They satisfy \(0\le r<d\), \(s<0\), \(r+s=\lambda-\mu\), and \(rs=\mu-d\). Both eigenspaces occur for a connected noncomplete strongly regular graph. Put \(a=d-r\) and \(b=d-s\), so \(0<a\le d<b\le2d\), and
\[
R(p,q)=\max\{|(1-ap)(1-aq)|,|(1-bp)(1-bq)|\}.
\]

**Case \(\lambda\ge\mu\).** Here \(a+b=2d-(\lambda-\mu)\le2d\). The first product is nonnegative and decreases strictly with either gain, so it is always at least \((1-a/d)^2=(r/d)^2\). At \(p=q=1/d\), the second product has modulus \((b/d-1)^2\le(1-a/d)^2\). This proves the optimum. Strict decrease proves unique gains.

**Case \(\lambda<\mu\), with \(r>0\).** Then \(a<d\), \(a+b>2d\), and \(c:=a+b-d=d+\mu-\lambda>d\). Define
\[
R_*=\frac{(d-a)(b-d)}{dc},\qquad
w=\frac{b(b-d)}{a(d-a)+b(b-d)}\in(0,1).
\]
For all feasible gains, \(f_a=(1-ap)(1-aq)\ge0\), while \(f_b=(1-bp)(1-bq)\) is real, so
\[
R(p,q)\ge wf_a+(1-w)f_b=:F(p,q).
\]
The bilinear function \(F\) takes value \(1\) at \((0,0)\) and value \(R_*\) at each of the other three vertices of the feasible square. Bilinear interpolation therefore gives the exact certificate
\[
F(p,q)=R_*+(1-R_*)(1-dp)(1-dq)\ge R_*.
\]
At \(p=1/d\) and \(q=1/c\), which both satisfy the stochastic bounds, the two spectral products coincide at \(R_*\); thus the lower bound is attained. Because \(R_*<1\), equality in the certificate forces at least one gain to be \(1/d\); equality in the positive-weight spectral average then forces the other gain to be \(1/c\). Hence the unordered optimal pair is unique.

**Case \(\lambda<\mu\), with \(r=0\).** The identity \(rs=\mu-d\) forces \(\mu=d\), and \(a=d\). The stated gains \(1/d\) and \(1/b=1/(d+\mu-\lambda)\) zero both nontrivial spectral products. Conversely, to zero the \(a\)-product one gain must be \(1/d\), and then to zero the \(b\)-product the other must be \(1/b\), proving uniqueness and the formula \(R_*=0\).

**Mean-field form and its boundary.** For \(\lambda<\mu\), the optimal kernels have product
\[
P(1/d)P(1/c)=\frac{A^2+(\mu-\lambda)A}{dc}
=\frac{(d-\mu)I+\mu J}{dc}.
\]
Since this product is stochastic, \(\mu N=dc-(d-\mu)\); the result is exactly \(R_*I+(1-R_*)J/N\). At \(\lambda=\mu\) the optimum \(A^2/d^2\) has the same form. For \(\lambda>\mu\), the coefficient of \(A\) in any product is
\[
p+q-(2d+\mu-\lambda)pq.
\]
If both gains are positive and this coefficient were zero, then \(1/p+1/q=2d+\mu-\lambda<2d\), contradicting \(p,q\le1/d\). If just one gain is zero, this coefficient is positive unless both gains vanish. As \(I,A,J\) are linearly independent for a noncomplete strongly regular graph, no nonidentity product can have mean-field form in this case.

**Comparison with the best repeated gain.** If \(\lambda\ge\mu\), the best fixed gain is \(1/d\) and repeated use is optimal. If \(\lambda<\mu\), set \(m=\mu-\lambda>0\), \(k=d-\mu\ge0\). The best feasible *single* gain is \(2/(2d+m)\); its two-round contraction is \((m^2+4k)/(2d+m)^2\), whereas the unequal-gain optimum is \(k/[d(d+m)]\). The strictly positive improvement is
\[
\frac{m^2(d^2+dm-k)}{d(d+m)(2d+m)^2}>0.
\]
Indeed \(d\ge2\) and \(0\le k\le d\), so the numerator's last factor is positive. This completes the proof.

## Verification
Run the accompanying standard-library program with Python 3.10 or newer, using `python3 verify.py`. It constructs eight graph families from their vertices and edge predicates (five-cycle, Petersen, Clebsch, rook graph, triangular graph, balanced complete multipartite graph, Shrikhande graph, and four-cycle). It checks the common-neighbor parameters and the quadratic adjacency identity, recomputes both stochastic matrices and their exact rational product, checks the mean-field identity where applicable, and scans a \(41\times41\) gain grid for each graph. A fresh replay returned `VERIFY_OK 20687 assertions; 8 independently constructed graphs`. The matrix products and equalities use exact fractions; spectral and grid checks use floating point. The all-parameter theorem is proved above, **not inferred from finite experiments**.

For the Petersen graph \((N,d,\lambda,\mu)=(10,3,0,1)\), optimal gains are \(1/3,1/4\), and the product is \(I/6+J/12\); the two-round contraction is \(1/6\), compared with \(9/49\) for the best repeated gain. For the Clebsch graph \((16,5,0,2)\), the optimum is \(3/35\), attained at \(1/5,1/7\). For triangular graphs \(T(n)\), \((d,\lambda,\mu)=(2(n-2),n-2,4)\); switching is strictly beneficial at \(n=5\), neutral at \(n=6\), and unnecessary for \(n\ge7\).

## Relationship to prior work
Boyd, Diaconis, and Xiao established the single-round stochastic spectral-optimization framework; Boyd, Diaconis, Parrilo, and Xiao developed symmetry-based fastest-mixing methods. Neither framework statement supplies the present **two-round, fixed-edge-uniform stochastic minimax**. Apers and Sarlette study two-step polynomial acceleration, including exact spectral filtering, but explicitly drop Markov transition-positivity requirements; their general polynomial optimizer can involve a step exceeding \(1/d\) and therefore does not directly give this constrained phase diagram. Hendrickx and collaborators study finite-time consensus via more general graph-supported matrices; their admissible class differs from the two fixed-Laplacian stochastic steps considered here. Ghosh and Lee address finite-time consensus through dynamic-feedback synthesis; only the public abstract of that potentially related article was accessible, so it remains a named historical uncertainty rather than a claimed whole-text exclusion. The five-cycle example is a special case already handled by prior odd-cycle two-round analysis and is not treated as a new standalone contribution. The assessed contribution is the all-strongly-regular common-neighbor phase criterion, sharp constrained gains, uniqueness, and exact mean-field collapse.

## Limitations
No claim is made that the two-round kernels are globally optimal among arbitrary spatially inhomogeneous Markov matrices, nonreversible chains, or products involving more than two steps. The closed form concerns noncomplete connected simple strongly regular graphs and exact homogeneous gains. The work has received no independent audit, and unindexed or inaccessible specialist literature may contain equivalent assertions. Numerical examples are checks, not a substitute for the global proof.

## References
1. S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. https://web.stanford.edu/~boyd/papers/fmmc.html
2. S. Boyd, P. Diaconis, P. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955 (first public September 6, 2007). https://arxiv.org/abs/0709.0955
3. J. M. Hendrickx, R. M. Jungers, A. Olshevsky, G. Vankeerberghen, *Graph diameter, eigenvalues, and minimum-time consensus*, arXiv:1211.6324 (first public November 27, 2012). https://arxiv.org/abs/1211.6324
4. S. Apers, A. Sarlette, *Accelerating Consensus by Spectral Clustering and Polynomial Filters*, arXiv:1503.01269 (first public March 4, 2015). https://arxiv.org/abs/1503.01269
5. S. Ghosh, J.-W. Lee, *Optimal Finite-Time Consensus on Fixed and Periodic Graphs*, SIAM Journal on Control and Optimization 51 (2013), 3946–3970. https://doi.org/10.1137/120862478 (public abstract compared; full text not inspected).
