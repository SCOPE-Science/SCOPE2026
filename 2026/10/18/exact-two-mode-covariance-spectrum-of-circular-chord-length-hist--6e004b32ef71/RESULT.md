# Exact two-mode covariance spectrum of circular chord-length histograms

## Finding
For a uniformly random perfect matching on \(2n\) clockwise labeled points of a circle, \(n\ge2\), let \(L_j\) be the number of chords whose shorter intervening arc has exactly \(j\) points, for \(0\le j\le n-1\). Thus \(L_{n-1}\) counts diameters, and \(\sum_{j=0}^{n-1}L_j=n\) deterministically. The complete covariance matrix \(\Sigma_n=\operatorname{Cov}(L_0,\ldots,L_{n-1})\) has entries
\[
(\Sigma_n)_{ij}=\begin{cases}
A_n,&i=j<n-1,\\
B_n,&i\ne j,\ i,j<n-1,\\
C_n,&\min(i,j)<n-1=\max(i,j),\\
D_n,&i=j=n-1,
\end{cases}
\]
where
\[
A_n=\frac{4n(n-1)}{(2n-1)^2},\quad
B_n=-\frac{8n(n-1)}{(2n-3)(2n-1)^2},\quad
C_n=-\frac{4n(n-1)}{(2n-3)(2n-1)^2},\quad
D_n=\frac{4n(n-1)^2}{(2n-3)(2n-1)^2}.
\]
In particular, all distinct length classes have **strictly negative covariance**, for every \(n\ge2\). The full real spectrum is
\[
\operatorname{Spec}(\Sigma_n)=\left\{
0,\ \underbrace{\frac{4n(n-1)}{(2n-3)(2n-1)},\ldots,\frac{4n(n-1)}{(2n-3)(2n-1)}}_{n-2\text{ copies}},\ \frac{4n^2(n-1)}{(2n-3)(2n-1)^2}
\right\}.
\]
The middle collection is empty at \(n=2\). Consequently, for \(n\ge3\), the ratio of the largest to smallest **positive** eigenvalue is exactly \((2n-1)/n\), strictly below \(2\); all positive eigenvalues converge to \(1\) as \(n\) grows.

Equivalently, for arbitrary real \(w_0,\dots,w_{n-1}\), let \(\bar w=(n-1)^{-1}\sum_{j=0}^{n-2}w_j\), and set
\[
\lambda_{\mathrm{short}}=\frac{4n(n-1)}{(2n-3)(2n-1)},\qquad
\lambda_{\mathrm{diam}}=\frac{4n^2(n-1)}{(2n-3)(2n-1)^2}.
\]
Then the following *exact variance isometry* holds:
\[
\operatorname{Var}\left(\sum_{j=0}^{n-1}w_jL_j\right)
=\lambda_{\mathrm{short}}\sum_{j=0}^{n-2}(w_j-\bar w)^2
+\lambda_{\mathrm{diam}}\frac{n-1}{n}(\bar w-w_{n-1})^2.
\]
This gives sharp variances for every linear length-histogram statistic, including all length contrasts.

## Assumptions and scope
Points are distinct and cyclically ordered, the perfect matching is uniformly chosen among \((2n-1)!!\) labeled matchings, and arc length is the **smaller** count of strictly intervening points. For a diameter there are equal arcs with \(n-1\) interior points, but it is counted once. The theorem concerns exact finite-sample second moments; no joint normal approximation, independent Poisson law at growing dimension, or higher-moment formula is asserted.

## Proof
Write \(N=2n\). A prescribed edge in the complete graph on the endpoints belongs to the random matching with probability \(p=1/(N-1)\). Two **distinct** prescribed edges both belong to it with probability \(q=1/((N-1)(N-3))\) when they are disjoint, and probability zero when they share an endpoint. These follow by fixing the indicated pairs and uniformly matching the unused vertices.

For \(0\le j<n-1\), the set \(E_j\) of candidate chords of shorter arc length \(j\) is a spanning 2-regular undirected graph: each endpoint has the two neighbors at cyclic steps \(\pm(j+1)\). Thus \(|E_j|=2n\). The diameter class \(E_{n-1}\) is the antipodal perfect matching, so \(|E_{n-1}|=n\). No two different length classes share a candidate edge. Consequently, the number of **ordered** pairs of distinct edges that share an endpoint is \(4n\) within one non-diameter class, \(8n\) between two different non-diameter classes, \(4n\) between a non-diameter class and the diameter class, and zero within the diameter class. The counts follow by summing \(d_i(v)d_j(v)\) at each endpoint, using degrees \(2\) or \(1\) (and for one class, summing \(d_j(v)(d_j(v)-1)\)).

Let \(M_j=|E_j|\), and let \(R_{ij}\) denote those ordered shared-endpoint pairs of *distinct* candidate edges. For \(i\ne j\), summing pairwise indicator covariances gives
\[
\operatorname{Cov}(L_i,L_j)
=(M_iM_j-R_{ij})(q-p^2)-R_{ij}p^2.
\]
For \(i=j\), the diagonal pairs instead each contribute \(p(1-p)\), giving
\[
\operatorname{Var}(L_i)=M_ip(1-p)
+(M_i(M_i-1)-R_{ii})(q-p^2)-R_{ii}p^2.
\]
Substituting the four overlap counts and the common \(p,q\) yields exactly \(A_n,B_n,C_n,D_n\) stated above. This also proves their asserted signs.

The covariance matrix is constant on and between the two blocks of \(n-1\) short classes and the single diameter class. Because \(\sum_jL_j=n\), the all-ones vector has eigenvalue zero. Every vector supported on the first \(n-1\) coordinates and summing there to zero is an eigenvector with eigenvalue \(A_n-B_n=\lambda_{\mathrm{short}}\), giving multiplicity \(n-2\). The remaining contrast \((1,\ldots,1,-(n-1))\) is an eigenvector with eigenvalue \(D_n-C_n=\lambda_{\mathrm{diam}}\). The three mutually orthogonal subspaces span \(\mathbb R^n\); each asserted eigenvalue is positive except the conservation eigenvalue zero. Orthogonally decomposing any \(w\) into these three spaces gives the stated variance formula. Finally \(\lambda_{\mathrm{short}}/\lambda_{\mathrm{diam}}=(2n-1)/n\) for \(n\ge3\), and direct limits finish the claims. \(\square\)

## Verification
A standalone pure-Python exact-rational verifier, `verify.py`, enumerates every perfect matching for \(2\le n\le7\) (including all \(135135\) matchings at \(n=7\)); checks each mean, each entry of the exact covariance matrix, and its zero row sums; and prints `VERIFY_OK`. It independently constructs each histogram directly from its matching without referring to the symbolic proof. The exhaustive finite checks corroborate but do not establish the all-\(n\) theorem, which follows from the indicator and spectral argument above.

## Relationship to prior work
Acan's *On a uniformly random chord diagram and its intersection graph* (first public preprint 2015) defines the same shorter-arc length statistic and proves joint independent Poisson limits for every **fixed** collection of small-length counts (Theorem 4.2). That asymptotic statement does not determine the finite covariance matrix across all \(n\) classes, particularly the diameter mode, or its exact eigenvalues. Paguyo's *Convergence rates of limit theorems in random chord diagrams* (first public preprint 2021; primary MSC 60C05) obtains a quantitative Poisson approximation for the simple-chord count \(L_0\) and crossing-count normal approximation. Those marginal approximations do not imply the present simultaneous finite-dimensional exact identities. Earlier elementary matching-indicator formulas are explicitly used rather than claimed new. The result is a new explicit evaluation and spectral synthesis relative to these inspected statements, not proof that no earlier expression implicitly covers it.

## Limitations
The proof concerns the uniform pairing model, not nonuniform chord matchings. The formula gives second moments and cannot by itself prove multivariate Gaussian, Poisson, or independence conclusions. The claim of historical originality is based on the inspected results and available record searches; possible implicit coverage by a prior multivariate chord-diagram generating function remains a priority risk. Independent priority checking and independent auditing have not been performed.

## References
1. J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134, first submitted 2021-04-02, especially Theorems 1.1–1.2 and the prescribed-chord probability in Lemma 2.1.
2. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489, first submitted 2015-01-07, especially the chord-length definition, Lemma 3.3 and Theorem 4.2.
3. P. Flajolet and M. Noy, *Analytic combinatorics of chord diagrams*, 2000; background on chord-diagram asymptotics.
