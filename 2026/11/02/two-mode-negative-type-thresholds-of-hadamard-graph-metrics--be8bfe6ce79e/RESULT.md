# Two-mode negative-type thresholds of Hadamard graph metrics

## Finding

Let \(H\) be any real Hadamard matrix of order \(k\ge4\), and let \(X_H\) be its \(4k\)-vertex Hadamard graph with unweighted shortest-path metric \(d\). Define \(\wp_k\) to be the supremum of exponents \(p\ge0\) for which \(\sum_{x,y}a_xa_y d(x,y)^p\le0\) for every real, finitely supported vector \(a\) with \(\sum_x a_x=0\). The result is independent of the equivalence or isomorphism class of \(H\).

For \(k=4\), \(\wp_4=1\). For every existing Hadamard order \(k\ge8\), define \(\rho_k\) and \(\sigma_k\) as the respective unique roots in \((0,1)\) of
\[
 F_k(p)=k(2\cdot2^p-1-3^p)+4^p-2\cdot2^p=0,
 \qquad G_k(p)=\sqrt{k}(3^p-1)-4^p=0.
\]
Then the exact supremal negative-type exponent, equivalently maximal generalized roundness, is
\[
\boxed{\wp_k=\min\{\rho_k,\sigma_k\}.}
\]
The two obstructions genuinely compete: \(\sigma_8<\rho_8\), whereas \(\rho_{12}<\sigma_{12}\). In particular \(\wp_8\approx0.472668518614\) and \(\wp_{12}\approx0.333888133778\). Along every sequence of existing Hadamard orders tending to infinity,
\[
\boxed{\wp_k\sim\frac{1}{k\log(4/3)}.}
\]
For every positive \(p\), \((X_H,d^{p/2})\) admits an isometric embedding into a real Hilbert space if and only if \(p\le\wp_k\). The metric has strict \(p\)-negative type below the threshold and non-strict negative type at it. For \(k\ge8\), the least affine Hilbert embedding dimension at the threshold is \(3k-1\) if \(\sigma_k<\rho_k\), \(4k-2\) if \(\rho_k<\sigma_k\), and \(3k-2\) if equality holds; below the threshold it is \(4k-1\). At \(k=4\) the endpoint dimension is \(4\) and the strictly subcritical dimension is \(15\).

## Assumptions and scope

A Hadamard matrix of order \(k\) is a \(k\times k\) matrix with entries \(\pm1\) and \(HH^{\mathsf T}=kI\). The graph \(X_H\) has row vertices \(r_i^\pm\), column vertices \(c_j^\pm\), and an edge between \(r_i^s\) and \(c_j^{sH_{ij}}\), with signs regarded multiplicatively. It has \(4k\) vertices, degree \(k\), and diameter \(4\). No existence of an order other than those supporting a Hadamard matrix is asserted. The two scalar roots are ordinary real roots; the theorem does not claim radical expressions for arbitrary orders.

Negative type refers to the distance-power matrix \(D_p=(d(x,y)^p)_{x,y\in X_H}\) restricted to the real zero-sum subspace \(\mathbf1^\perp\). Powers on the diagonal are taken as zero for positive \(p\). The graph metric and matrix are unweighted.

## Proof

**1. Spectral decomposition.** The Hadamard graph is distance regular with intersection array
\[
\{k,k-1,k/2,1;1,k/2,k-1,k\}.
\]
Write \(A_i\) for the distance-\(i\) adjacency matrices, with \(A_0=I\) and \(A=A_1\). The distance-regular recurrence \(AA_i=b_{i-1}A_{i-1}+c_{i+1}A_{i+1}\) (where the diagonal intersection numbers vanish) gives polynomials \(A_i=v_i(A)\). Evaluating the recurrence at the adjacency eigenvalues yields the following table, with columns indexed by \(i=0,1,2,3,4\):
\[
\begin{array}{c|ccccc|c}
\theta&v_0&v_1&v_2&v_3&v_4&\mathrm{multiplicity}\\\hline
 k&1&k&2k-2&k&1&1\\
 \sqrt k&1&\sqrt k&0&-\sqrt k&-1&k\\
 0&1&0&-2&0&1&2k-2\\
 -\sqrt k&1&-\sqrt k&0&\sqrt k&-1&k\\
 -k&1&-k&2k-2&-k&1&1
\end{array}
\]
For completeness, the adjacency spectrum can also be recovered directly: in the bipartite block \(A=\left(\begin{smallmatrix}0&N\\N^{\mathsf T}&0\end{smallmatrix}\right)\), orthogonality of Hadamard rows makes the eigenvalues of \(NN^{\mathsf T}\) equal to \(k^2\) once, \(k\) with multiplicity \(k\), and \(0\) with multiplicity \(k-1\). This proves the displayed adjacency multiplicities without assuming that the Hadamard graph is vertex-transitive.

**2. All negative-type eigenvalues.** Since \(D_p=\sum_{i=1}^4i^p A_i\), the four eigenvalues on \(\mathbf1^\perp\), in the same nontrivial-eigenspace order as above, are exactly
\[
\begin{aligned}
\mu_+(p)&=\sqrt k(1-3^p)-4^p,\\
\mu_0(p)&=4^p-2\cdot2^p,\\
\mu_-(p)&=\sqrt k(3^p-1)-4^p=G_k(p),\\
\mu_b(p)&=k(2\cdot2^p-1-3^p)+4^p-2\cdot2^p=F_k(p).
\end{aligned}
\]
Thus \(p\)-negative type holds exactly when all four quantities are nonpositive. We have \(\mu_+(p)<0\) for all \(p>0\), and \(\mu_0(p)\le0\) precisely when \(p\le1\). On \([0,1]\), \(G_k(0)=-1\), \(G_k(1)=2\sqrt k-4\), and
\[
G_k'(p)=\sqrt k\,3^p\log3-4^p\log4>0
\]
for \(k\ge4\): indeed \(2(3/4)^p\log3\ge(3/2)\log3>\log4\). Hence \(G_k\) has a unique root in \((0,1)\) for \(k>4\), and the root is \(1\) when \(k=4\).

**3. The second root and uniqueness.** Put \(a=\log2\), \(b=\log3\). For \(0<p<1\), strict concavity of \(x\mapsto x^p\) shows \(2\cdot2^p-1-3^p>0\), so \(F_k(p)\) is strictly increasing as a function of \(k\). For \(k\ge8\), \(F_k(0)=-1\), \(F_k(1)=0\), while
\[
F_k'(1)=-k\log(27/16)+4\log2<0.
\]
Moreover \(F_k''(p)<0\) throughout \([0,1]\). To verify this last claim, the coefficient \(2a^2 2^p-b^2 3^p\) is negative, so \(F_k''(p)\le F_8''(p)\), and
\[
F_8''(p)=a^2 2^p(14+4\cdot2^p)-8b^2 3^p.
\]
The function \((14+4\cdot2^p)(2/3)^p\) decreases on \([0,1]\) because its derivative has the sign of \(4\cdot2^p\log(4/3)-14\log(3/2)<0\), and its initial value is \(18\). But \(8(b/a)^2>18\), since \(\log_2 3>3/2\). Therefore \(F_8''(p)<0\), proving strict concavity. It follows that \(F_k\) has exactly one zero \(\rho_k\) in \((0,1)\), is negative before it, and is positive between that root and \(1\).

For \(k=4\), the Hadamard graph is the four-cube; its Hamming metric has \(1\)-negative type, and \(\mu_0(p)>0\) for \(p>1\), establishing \(\wp_4=1\). For \(k\ge8\), the four eigenvalue signs now give exactly the minimum-root formula. At the endpoint a zero eigenvalue occurs in the \(-\sqrt{k}\) sector (multiplicity \(k\)), the \(-k\) sector (multiplicity \(1\)), or both. The centered Gram matrix \(-\frac12 JD_pJ\), where \(J=I-\frac{1}{4k}\mathbf1\mathbf1^{\mathsf T}\), gives the stated least embedding dimensions by its rank. The Schoenberg correspondence gives the snowflake characterization.

**4. Distinct modes and asymptotics.** For \(k=8\), at \(p=1/2\) one has \(F_8(1/2)=14\sqrt2-8\sqrt3-6<0\) and \(G_8(1/2)=2\sqrt2(\sqrt3-1)-2>0\); hence \(\sigma_8<1/2<\rho_8\). For \(k=12\), let \(p=17/50\). A rational certificate is
\[
\begin{array}{c}
1.265756<2^p<1.265757,\quad
1.452851<3^p<1.452852,\\
1.602139<4^p<1.602140,\quad
3.464101<\sqrt{12}<3.464102.
\end{array}
\]
Each power bound follows by taking the positive fiftieth power of the two rational decimal endpoints and comparing with the exact integer base to the seventeenth power; the square-root bounds follow by squaring. Consequently
\[
 F_{12}(p)=22\cdot2^p-12\cdot3^p+4^p-12>0.014547>0,
 \quad G_{12}(p)<-0.0334134<0.
\]
Thus \(\rho_{12}<17/50<\sigma_{12}\). These strict inequalities are reproducible with only rational integer comparisons.

As \(k\to\infty\), the unique root of \(G_k\) satisfies \(\sigma_k\sim(\sqrt k\log3)^{-1}\), by expanding \(3^p-1\) at zero. Similarly
\[
F_k(p)=-1+k\log(4/3)\,p+O(kp^2+p^2)
\]
for \(p\) near zero. The unique first root therefore satisfies \(\rho_k\sim(k\log(4/3))^{-1}\). Since \(\rho_k/\sigma_k\to0\), the minimum-root formula yields \(\wp_k\sim(k\log(4/3))^{-1}\).

## Verification

The accompanying `check.py` independently constructs Hadamard graphs at orders \(4,8,12,16,20\) using Sylvester and Paley matrices. It obtains graph distances by breadth-first search, checks the adjacency spectrum, calculates distance-power eigenspectra independently from full matrices, compares them with the four analytic spectral formulas at six exponent choices per order, and estimates both scalar roots. The local run returned `HADAMARD_NEGATIVE_TYPE_CHECK_OK cases=30`. This is finite corroboration only; the general proof above covers all existing orders.

Run with `python check.py` after installing the packages in `requirements.txt`. The roots may be computed using bisection on \((0,1)\) because the proved sign properties make them uniquely defined. No enumerated graph list, stored eigenvector table, or external downloadable data is needed for the proof.

## Relationship to prior work

Cioabă, Gupta, Ihringer, and Kurihara (arXiv:2109.09708, originally posted 2021-09-20) give the Hadamard graph's intersection array and analyze least Euclidean distortion of the *unpowered graph metric*. Their Section 3.3.1 does not state the present continuous \(p\)-negative-type threshold, its competing modes, or the order-dependent sharp snowflake dimension. Hirasaka, Kim, and Yu (arXiv:1407.7346) study the Hadamard association scheme and structural isomorphism classes, not its powered-distance conditional negativity. Li and Weston (arXiv:0901.0695) supply general strict negative-type theory. Robertson (arXiv:2309.16070) studies distorted negative type, with explicit bipartite-graph and Hamming-cube examples, not the Hadamard-graph family. The new contribution is the exact competing-eigenmode root law, its sharp embedding consequence, and its inverse-order asymptotic, not the underlying association-scheme method or Schoenberg's theorem.

## Limitations

The theorem applies only to graphs arising from actually existing Hadamard matrices, with ordinary unweighted graph distance and real coefficients. It does not prove existence of Hadamard matrices in every multiple-of-four order. The exact roots are specified implicitly and do not constitute radical closed forms. Earlier work might contain an equivalent powered-distance calculation under a different name; the literature comparisons below do not independently certify historical priority. Numerical spectral checks do not establish the infinite-family theorem. Independent mathematical validation has not been performed.

## References

- S. M. Cioabă, H. Gupta, F. Ihringer, H. Kurihara, *The least Euclidean distortion constant of a distance-regular graph*, arXiv:2109.09708 (first posted September 20, 2021), particularly Section 3.3.1; https://arxiv.org/abs/2109.09708.
- G. Robertson, *Negative type and bi-lipschitz embeddings into Hilbert space*, arXiv:2309.16070 (first posted September 27, 2023), particularly Section 4; https://arxiv.org/abs/2309.16070.
- M. Hirasaka, K. Kim, H. Yu, *Isomorphism classes of association schemes induced by Hadamard matrices*, arXiv:1407.7346 (2014); https://arxiv.org/abs/1407.7346.
- H. Li, A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695 (2009); https://arxiv.org/abs/0901.0695.
