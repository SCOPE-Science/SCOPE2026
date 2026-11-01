# Sharp Schoenberg exponents and endpoint Euclidean ranks for crown-graph metrics

## Finding
For each integer \(n\ge3\), delete a perfect matching from the complete bipartite graph \(K_{n,n}\). Equip the resulting crown graph \(\operatorname{Cr}_n\) with shortest-path distance \(d\). The **supremal negative-type exponent** \(\beta_n\) is exactly
\[
\beta_n=\begin{cases}1,&n=3,4,\\
\text{the unique root in }(0,1)\text{ of }(n-1)(2^p-1)=3^p,&n\ge5.
\end{cases}
\]
More precisely, for every real \(p\ge0\), the matrix \((d(x,y)^p)_{x,y}\) is conditionally negative semidefinite exactly for \(0\le p\le\beta_n\). By Schoenberg's theorem, this is equivalent to positive definiteness of the invariant Gaussian-type kernel \(\exp(-t d(x,y)^p)\) for **every** real \(t>0\). This is a simultaneous, all-bandwidth result, not a statement about a particular chosen bandwidth.

At the sharp endpoint, the kernel of the powered-distance form on the zero-sum subspace has dimension \(n-1\) for \(n=3\), dimension \(n\) for \(n=4\), and dimension \(1\) for \(n\ge5\). Therefore the associated centered Schoenberg embedding has respectively \(3\), \(3\), and \(2n-2\) Euclidean dimensions. For \(0\le p<\beta_n\), the corresponding dimension is \(2n-1\).

Writing \(N=n-1\), the exact exponent has the asymptotic expansion
\[
\beta_n=\frac{1}{N\log 2}+\frac{\log 3/(\log 2)^2-1/(2\log 2)}{N^2}+O(N^{-3}).
\]
The known formula \(\wp(K_{n,n})=\log_2(n/(n-1))\) consequently implies
\[
\beta_n-\wp(K_{n,n})=\frac{\log 3}{(\log 2)^2N^2}+O(N^{-3}).
\]
In fact \(\beta_n>\wp(K_{n,n})\) for all \(n\ge3\): deleting the matching improves the negative-type exponent.

## Assumptions and scope
Label the vertices \(a_1,\dots,a_n,b_1,\dots,b_n\), with an edge \(a_i\sim b_j\) precisely when \(i\ne j\). The graph is connected for \(n\ge3\). Distances between distinct vertices on the same side equal \(2\); distances between vertices on opposite sides equal \(1\), except for the deleted matched pairs \((a_i,b_i)\), which have distance \(3\).

For \(p>0\), use the powered distance \(d^p\); at \(p=0\), set each off-diagonal entry to one and each diagonal entry to zero, the standard limiting convention. A real symmetric kernel \(D\) on the vertex set is *conditionally negative semidefinite* when \(z^{\mathsf T}Dz\le0\) for every real vector \(z\) satisfying \(\sum_xz_x=0\). The supremal exponent \(\beta_n\) is the largest \(p\ge0\) with this property.

A function on \(S_n\times C_2\), obtained by taking the powered graph distance from a fixed vertex to its image under a group element, is a conditionally negative-type function; its exponential is positive definite on that group precisely in the parameter range asserted above. This follows from transitivity on the vertex set and restriction to an orbit. Here \(S_n\) simultaneously permutes the two index sets, and \(C_2\) swaps the two sides.

## Proof
**Step 1: exact full spectrum.** Put \(u=2^p\), \(v=3^p\), and let \(J\) and \(I\) be the \(n\times n\) all-ones and identity matrices. The powered-distance matrix has the block form
\[
D_{n,p}=\begin{pmatrix}u(J-I)&J+(v-1)I\\ J+(v-1)I&u(J-I)\end{pmatrix}.
\]
The constant vector \((\mathbf1,\mathbf1)\) has eigenvalue \((n-1)(u+1)+v\), which is strictly positive. The orthogonal complement of the constants decomposes into the following mutually orthogonal invariant spaces:
\[
\begin{array}{rcll}
(\mathbf1,-\mathbf1)&:&(n-1)(u-1)-v,&\text{multiplicity }1,\\
(z,z),\quad \sum_i z_i=0&:&v-u-1,&\text{multiplicity }n-1,\\
(z,-z),\quad \sum_i z_i=0&:&1-u-v,&\text{multiplicity }n-1.
\end{array}
\]
The dimensions sum to \(2n-1\), proving that these are all eigenvalues on the centered subspace. Conditional negative semidefiniteness is equivalent to nonpositivity of all three displayed eigenvalues.

**Step 2: isolate the valid exponents.** For \(0\le p\le1\), subadditivity gives \(3^p\le2^p+1\). Equality holds at \(p=1\), and strictly fails in the opposite direction for \(p>1\), by strict superadditivity of powers. Therefore the second centered eigenvalue is nonpositive exactly for \(0\le p\le1\). The third is always negative. On \((0,1]\), the remaining condition is
\[
 n-1\le R(p),\qquad R(p)=\frac{3^p}{2^p-1}.
\]
The logarithmic derivative is
\[
\frac{R'(p)}{R(p)}=\log3-\frac{2^p\log2}{2^p-1}<0
\qquad(0<p\le1).
\]
Indeed the second term decreases as \(p\) increases, and its value at \(p=1\) is \(2\log2>\log3\). Moreover \(R(p)\to\infty\) as \(p\downarrow0\), whereas \(R(1)=3\). Thus the condition holds for all \(p\le1\) when \(n=3,4\), and ends at a unique internal root when \(n\ge5\). This also proves strict conditional negative definiteness below the endpoint.

**Step 3: boundary multiplicities and Euclidean ranks.** At \(p=1\), the second centered eigenvalue is zero with multiplicity \(n-1\). For \(n=3\), the first centered eigenvalue is negative, while for \(n=4\) it is also zero. For \(n\ge5\), the critical exponent lies below one, so the second centered eigenvalue is strictly negative, and only the first centered eigenvalue vanishes. The dimensions of the respective nullspaces are therefore \(n-1\), \(n\), and \(1\). The centered Euclidean Gram matrix \(-\tfrac12 H D_{n,p}H\), with \(H=I_{2n}-\mathbf1\mathbf1^{\mathsf T}/(2n)\), has rank equal to the number of strictly negative centered eigenvalues. This yields the asserted ranks \(3,3,2n-2\); below the endpoint it has full centered rank \(2n-1\).

**Step 4: asymptotics and perturbation gain.** Write \(N=n-1\), \(a=\log2\), and \(b=\log3\). The unique root is \(O(N^{-1})\): since \(R(p)\sim1/(ap)\) near zero, its defining equation forces this scale. Substitute \(p=c_1/N+c_2/N^2+O(N^{-3})\) into \(N(e^{ap}-1)=e^{bp}\). Matching constant and inverse-linear coefficients gives \(ac_1=1\) and \(ac_2+a^2c_1^2/2=bc_1\). Hence \(c_1=1/a\) and \(c_2=b/a^2-1/(2a)\). The analytic implicit-function theorem applied to \((e^{ap}-1)/e^{bp}=1/N\) justifies the remainder. For the complete bipartite graph, Sánchez's formula yields \(\wp(K_{n,n})=\log_2(1+1/N)=1/(aN)-1/(2aN^2)+O(N^{-3})\). Subtraction proves the displayed gain. The strict finite-\(n\) comparison follows since \(N(2^{\wp(K_{n,n})}-1)=1<3^{\wp(K_{n,n})}\), while \(\beta_n\le1\).

**Step 5: uniform positive-type equivalence.** Schoenberg's theorem states that a zero-diagonal symmetric kernel \(D\) is conditionally negative semidefinite if and only if \(e^{-tD}\) is positive semidefinite for all \(t>0\). If a centered eigenvalue of \(D\) is positive, the associated quadratic form of \(e^{-tD}\) is negative for sufficiently small \(t>0\) by the expansion \(e^{-tD}=J_{2n}-tD+O(t^2)\). This proves both directions, including failure beyond the critical exponent. The transitive group-orbit reformulation is equivalent because the full vertex matrix is the restriction of the corresponding group-invariant function to coset representatives.

## Verification
The supplied standalone checker `verification/check_crown.py` builds the actual shortest-path distance matrix from the graph definition, multiplies it by explicit vectors from all four spectral sectors, and compares with the claimed eigenvalues. It verifies \(5152\) explicit vector/eigenvalue identities across \(3\le n\le25\), eight distinct powers, \(23\) critical-endpoint tests, and three asymptotic cases. Run using `python3 verification/check_crown.py`. Its successful output starts with `CHECK_OK`. Numerical tests are independent finite checks and do not establish the all-\(n\) theorem; the complete proof is given above.

## Relationship to prior work
Sánchez (2011, arXiv:1108.0451) gives a general determinant method for finite metric spaces and exactly computes the supremal negative-type exponent of \(K_{n,m}\); his balanced specialization is explicitly used in the comparison. Murugan (2011, arXiv:1112.5657) develops a general determinant characterization for vertex-transitive graphs, covering crown graphs *in principle* but not providing their powered-distance spectrum, precise root, sharp degeneracies, or second-order difference from complete bipartite graphs. The present result is an explicit complete special-family classification rather than a claimed new general criterion. The matrix is also a four-class association-scheme matrix; familiar Fourier/representation block diagonalization supplies its method, not automatically the threshold or asymptotic coefficients.

## Limitations
Only connected crown graphs with \(n\ge3\) are considered; \(n=1,2\) are disconnected. The classification concerns the entire family of powered geodesic distances and all bandwidths collectively; for \(p>\beta_n\), some individual sufficiently large bandwidths may still produce positive-definite matrices. The precise newness of the explicit formula is based on bounded literature review, not a proof of its absence from all preexisting association-scheme or metric-embedding sources. Independent validation of the theorem has not been performed.

## References
1. Stephen Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451, first public posting 2011-08-02. https://arxiv.org/abs/1108.0451
2. Mathav Kishore Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657, first public posting 2011-12-23. https://arxiv.org/abs/1112.5657
3. I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society 44 (1938), 522–536, DOI: 10.1090/S0002-9947-1938-1501980-0.
