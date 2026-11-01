# Exact Euclidean criterion and one-obstruction theorem for complete multipartite resistance metrics

## Finding
Let \(G=K_{n_1,\ldots,n_k}\) be a connected complete multipartite graph with \(k\ge3\), positive integer part sizes \(n_i\), \(N=\sum_i n_i\), and unit electrical conductance on every edge. Write \(R(u,v)\) for its effective-resistance metric. Define
\[
 d_i=N-n_i,\qquad c=\frac{N-1}{N},\qquad
 \tau_i=\frac1{n_i}-\frac{2N-1}{N^2}.
\]
If all parts have equal size, \(R\) has strict \(2\)-negative type. Otherwise, set
\[
 S_0=\sum_i\tau_i^{-1},\qquad
 S_1=\sum_i d_i\tau_i^{-1},\qquad
 S_2=\sum_i d_i^2\tau_i^{-1},\qquad
 \Delta=S_0S_2-S_1^2,
\]
and \(\mathfrak m=S_2/\Delta\). Every \(\tau_i\) and \(\Delta\) is nonzero. The following is an exact rational, profile-only criterion:
\[
\boxed{\;R\text{ is isometrically Euclidean}\quad\Longleftrightarrow\quad
\mathfrak m\ge \frac{(N-1)^2}{2N^2}.\;}
\]
At strict inequality, \(R\) has strict \(2\)-negative type and requires exactly \(N-1\) Euclidean dimensions. At equality it has non-strict \(2\)-negative type, its entire nonzero equality-coefficient space is one-dimensional, and the minimum Euclidean dimension is exactly \(N-2\). At reversed strict inequality, \(R\) is not Euclidean: the double-centered Gram matrix of \(R^2\) has **exactly one** negative eigenvalue, \(N-2\) positive eigenvalues, and a one-dimensional kernel. Thus every part profile has at most one non-Euclidean spectral obstruction.

For the supremal negative-type exponent \(\wp(R)\), the three alternatives are respectively \(\wp(R)>2\), \(\wp(R)=2\), and \(1<\wp(R)<2\). No exact value of \(\wp(R)\) is asserted away from the equality threshold.

The criterion is not determined by the total order and largest part size: for \(K_{1,1,3,5}\) its margin \(\mathfrak m-c^2/2\) equals \(4941/118600>0\), but for \(K_{1,2,2,5}\) it equals \(-297/16300<0\). Both graphs have ten vertices and largest part of size five.

## Assumptions and scope
The graph is finite, has at least three nonempty independent vertex classes, all edges join different classes, and all edge conductances are exactly one. An effective-resistance metric is not the unweighted shortest-path metric. For \(p>0\), \(p\)-negative type means that \(\sum_{u,v}a_u a_v R(u,v)^p\le0\) for every real coefficient vector satisfying \(\sum_u a_u=0\); strictness means strict inequality for every nonzero such vector. The centered Euclidean Gram matrix for the candidate Euclidean distance \(R\) is \(B=-\frac12 H(R\circ R)H\), with \(H=I-\frac1N\mathbf1\mathbf1^\mathsf T\). Here \(\circ\) is entrywise multiplication, so the theorem concerns the *square of the resistance metric*, not the conventional resistance matrix itself.

## Proof
**1. Electrical distances.** The graph Laplacian has eigenvalue \(d_i\) on the \((n_i-1)\)-dimensional within-class contrast space, and eigenvalue \(N\) on the \((k-1)\)-dimensional space of class-constant functions whose weighted total sum is zero. Resolving a unit current using these orthogonal eigenspaces gives, for distinct vertices,
\[
 R(u,v)=\begin{cases}
 2/d_i,&u,v\in V_i,\\
 c(d_i^{-1}+d_j^{-1}),&u\in V_i,\ v\in V_j,\ i\ne j.
 \end{cases}
\]
The first case is needed only for classes with at least two vertices. These identities agree with established multipartite effective-resistance formulas, but they are also derived independently from the Laplacian decomposition.

**2. Full quadratic-form reduction.** Let \(a\in\mathbb R^N\) with \(\sum_u a_u=0\). Set \(x_i=\sum_{u\in V_i}a_u\), \(y_i=x_i/d_i\), and \(z_u=a_u-x_i/n_i\) for \(u\in V_i\). Then \(\sum_i d_i y_i=0\), each \(\sum_{u\in V_i}z_u=0\), and direct substitution of the preceding distances gives the exact identity
\[
\boxed{\;
 \sum_{u,v}a_u a_vR(u,v)^2
 =-\sum_i\frac4{d_i^2}\sum_{u\in V_i}z_u^2
   -4\sum_i\tau_i y_i^2
   +2c^2\left(\sum_i y_i\right)^2.
\;}
\]
No term is omitted when a class has size one.

**3. Universal positive subspace.** For arbitrary real \(w_i\) with \(\sum_iw_i=0\), Cauchy--Schwarz and equality of the total positive and negative masses give
\[
 \sum_i\frac{w_i^2}{n_i}
 \ge\frac{(\sum_i|w_i|)^2}{N}
 \ge\frac2N\sum_iw_i^2.
\]
Hence
\[
 \sum_i\tau_iw_i^2\ge\frac1{N^2}\sum_iw_i^2>0
\]
for every nonzero zero-sum \(w\). In particular, this quadratic form is strictly positive on \(W=\{w:\sum_iw_i=\sum_i d_iw_i=0\}\), regardless of whether any individual \(\tau_i\) is negative. If all \(d_i\) are equal, the zero-sum coefficient condition already forces \(\sum_i y_i=0\), proving strict \(2\)-negative type by Step 2.

**4. Exact constrained minimum.** Suppose the part sizes are not all equal. The two linear forms \(y\mapsto\sum_i y_i\) and \(y\mapsto\sum_i d_i y_i\) are independent. Positivity on \(W\) proves existence and uniqueness of the minimizer of \(\sum_i\tau_i y_i^2\) under \(\sum_i y_i=1\), \(\sum_i d_i y_i=0\). None of the \(\tau_i\) is zero: an integer equality \(n_i=N^2/(2N-1)\) would contradict \(\gcd(N^2,2N-1)=1\) and \(2N-1>1\). The corresponding bordered Lagrange system is invertible by positivity on \(W\), implying \(\Delta\ne0\). Solving its two constraints yields
\[
 y_i^*=\frac{S_2-S_1d_i}{\Delta\tau_i},\qquad
 \sum_i y_i^*=1,\quad \sum_i d_i y_i^*=0,\quad
 \sum_i\tau_i(y_i^*)^2=\frac{S_2}{\Delta}=\mathfrak m.
\]
First-order optimality makes \(y^*\) orthogonal to \(W\) for the bilinear form \(\sum_i\tau_i y_iw_i\). Every \(y\) with \(\sum_i d_i y_i=0\) has a unique representation \(y=s y^*+w\), \(w\in W\), \(s=\sum_i y_i\). The Step 2 form therefore becomes
\[
 \sum_{u,v}a_u a_vR(u,v)^2
 =-\sum_i\frac4{d_i^2}\sum_{u\in V_i}z_u^2
  -4\sum_i\tau_iw_i^2
  +\left(2c^2-4\mathfrak m\right)s^2.
\]
Every term except the last is strictly negative on its nontrivial sector. Thus the zero-sum powered-distance matrix has exactly zero or one positive direction, with a single null direction precisely at \(\mathfrak m=c^2/2\). The critical equality vector has constant value \(d_i y_i^*/n_i\) on every vertex of class \(V_i\), up to an arbitrary common nonzero scalar. The one-dimensional rank drop and Gram inertia follow by multiplying the form by \(-1/2\) and restoring the trivial constant Gram-kernel vector.

**5. Exponent comparison.** For every connected electrical network, \(R(u,v)=(e_u-e_v)^\mathsf T L^+(e_u-e_v)\); hence for zero-sum nonzero \(a\), \(\sum_{u,v}a_u a_vR(u,v)=-2a^\mathsf TL^+a<0\). Finiteness gives strict \(p\)-negative type on an open interval around \(p=1\). Strictness at \(p=2\) analogously gives \(\wp(R)>2\). When \(2\)-negative type holds with a nonzero equality, the strictness-below-endpoint theorem of Li--Weston rules out \(p\)-negative type for any \(p>2\), giving \(\wp(R)=2\). If \(2\)-negative type fails, its supremal exponent is strictly between one and two. This proves all alternatives.

## Verification
Run `python verify_multipartite.py` in an environment with `sympy` and `numpy`. The standalone verifier reconstructs the Laplacian and its exact rational pseudoinverse independently, verifies all pairwise resistances and the full quadratic reduction, compares the centered-Gram inertia and exact rank for sixteen specified profiles, and checks the scalar criterion against direct Gram eigenspectra for every nontrivial integer partition of each order \(2\le N\le12\) (259 profiles). Its successful completion prints `ALL_MULTIPARTITE_EUCLIDEAN_CHECKS_OK`. Rational tests are exact; numerical eigenvalue signs in the partition census corroborate, rather than replace, the analytic proof. All of the critical deductions, including the single-obstruction assertion for arbitrary part sizes, are analytic.

## Relationship to prior work
Schoenberg's criterion and Li--Weston's strict negative-type theorem supply the general metric-embedding framework. Jorgensen--Pearse establishes the universal Hilbert embedding of the *square root* of effective resistance, not the stronger embeddability of resistance itself. Gervacio's multipartite resistance work and Das--Yang's 2017 open-access article provide the pairwise effective-resistance formulas and the spectrum of the **unsquared** resistance matrix. Those are distinguished from the new entrywise-square conditional-inertia criterion and its exact part-profile threshold. Sánchez's complete-bipartite example and Obata's multipartite quadratic-embedding classification concern **unweighted shortest-path metrics**, not effective resistance. A preceding complete-bipartite effective-resistance classification treats only two classes; the present theorem deliberately asserts the new result for at least three classes. These distinctions are about mathematical implication, not merely differing titles.

## Limitations
The theorem gives a rational test at exponent \(2\), the exact centered-Gram inertia there, and the position of the maximal negative-type exponent relative to \(2\); it does **not** calculate the maximal exponent itself away from the critical case. It does not cover weighted interclass conductances, noncomplete graphs, or alternative metrics on the same graph. Earlier exact-resistance publications and general matrix-inertia principles may yield equivalent reformulations; originality should be checked independently before any publication-priority assertion. The 2012/2016 Gervacio full texts could not be examined through the available access routes; their accessible abstracts describe pairwise-resistance formulas, and the later full open-access Das--Yang article independently supplies them.

## References
- H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695 (first public 2009-01-06), especially Theorem 5.4.
- P. E. T. Jorgensen and E. P. J. Pearse, *A Hilbert space approach to effective resistance metric*, arXiv:0906.2535 (first public 2009-06-14), especially Section 5.
- S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451 (first public 2011-08-02).
- S. V. Gervacio, *Resistance distance in complete n-partite graphs*, The Mindanawan Journal of Mathematics 3 (2012), 1--19; publicly dated 2012-05-01, https://journals.msuiit.edu.ph/tmjm/article/view/26 . Related journal publication: Discrete Applied Mathematics 203 (2016), 53--61, doi:10.1016/j.dam.2015.09.017.
- K. C. Das and Y. Yang, *Eigenvalues of the resistance-distance matrix of complete multipartite graphs*, Journal of Inequalities and Applications 2017:296, doi:10.1186/s13660-017-1570-1 (open-access full text).
- N. Obata, *Complete multipartite graphs of non-QE class*, Electronic Journal of Graph Theory and Applications 11 (2023), 511--527, doi:10.5614/ejgta.2023.11.2.14 (unweighted graph shortest-path metric).
