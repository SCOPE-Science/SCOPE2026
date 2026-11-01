# Sharp negative type and first-failure exponents for powers of Hamming graphs

## Finding

Let \(q\ge2\), \(d\ge1\), and \(k\ge1\) be integers. On the full word set \(X=(\mathbb Z/q\mathbb Z)^d\), join two different words if they differ in at most \(k\) coordinates. Let \(\rho_{d,q,k}\) be the shortest-path metric. Then

\[
\exp(-t\rho_{d,q,k}(x,y))\succeq0\quad\text{for every }t>0
\quad\Longleftrightarrow\quad
k=1\ \text{or}\ d\le k\ \text{or}\ [q=2\text{ and }(k=2\text{ or }d=k+1)].
\]

The positive-semidefinite statement concerns the full matrix indexed by \(X\), not merely a proper subspace. In each admissible case the matrix is strictly positive definite for every \(t>0\). In each excluded case it has a negative eigenvalue for all sufficiently small \(t>0\).

At the **first excluded dimension**, the exact supremal powered-distance negative-type exponent and critical Euclidean rank are as follows. Put \(N=q^m\) and \(K_{t,p}(x,y)=\exp(-t\rho_{m,q,k}(x,y)^p)\), with diagonal entries one even at \(p=0\).

For every \(q\ge3\), \(k\ge2\), and \(m=k+1\), set

\[
\alpha_{q,m}=\log_2\!\left(1+(q-1)^{-(m-2)}\right),\qquad
\nu_{q,m}=\binom m2(q-1)^2.
\]

Then \(K_{t,p}\) is positive semidefinite for every \(t>0\) if and only if \(0\le p\le\alpha_{q,m}\). At equality, the centered powered-distance form has nullity \(\nu_{q,m}\), and the least squared-Euclidean embedding dimension equals \(q^m-1-\nu_{q,m}\).

For \(q=2\), \(k\ge3\), and \(m=k+2\), set

\[
M_m=\begin{cases}m-1,&m\text{ odd},\\m-3,&m\text{ even},\end{cases}\qquad
\alpha_m=\log_2\!\left(1+M_m^{-1}\right),\qquad
\nu_m=\begin{cases}1,&m\text{ odd},\\\binom m2+m,&m\text{ even}.\end{cases}
\]

The same equivalence holds with endpoint \(\alpha_m\); the endpoint squared-Euclidean embedding dimension is \(2^m-1-\nu_m\). In both families the embedding dimension is \(N-1\) for \(0\le p<\alpha\), and \(K_{t,p}\) is strictly positive definite for every fixed positive \(t\) throughout the admissible interval.

## Assumptions and scope

Hamming distance \(h(x,y)\) counts the coordinates on which two words differ. Graph edges have unit length; the exponent in the powered kernel is applied to graph shortest-path distance rather than original Hamming distance. When \(p=0\), set \(\rho(x,x)^0=0\) and \(\rho(x,y)^0=1\) for distinct words. Only positive integers \(q,d,k\) in the stated ranges are considered; primality of \(q\) is not required.

For a real symmetric zero-diagonal matrix \(D\), conditional negative semidefiniteness means \(c^{\mathsf T}Dc\le0\) for every real vector \(c\) with zero coordinate sum. For a finite metric, this condition is equivalent to positive semidefiniteness of every \(\exp(-tD)\), \(t>0\), and to representability of \(D\) as squared Euclidean distances. The minimum such embedding dimension is the rank of \(-HDH/2\), where \(H=I-J/N\).

## Proof

**1. Metric and characters.** Every edge changes at most \(k\) coordinates, and a Hamming difference can be corrected in blocks of size at most \(k\). Therefore, for all words,

\[
\rho_{d,q,k}(x,y)=\left\lceil\frac{h(x,y)}k\right\rceil.
\]

Coordinate subcubes, obtained by fixing some coordinates, are isometric in this powered graph metric. On the abelian group \((\mathbb Z/q\mathbb Z)^d\), convolution with a radial distance matrix is diagonal in the character basis. For a character nontrivial on exactly \(j\) coordinates, the Fourier eigenvalue of the indicator of Hamming radius \(r\) is

\[
P_r(j)=\sum_{a=0}^{r}(-1)^a(q-1)^{r-a}\binom ja\binom{d-j}{r-a},
\]

where out-of-range binomial coefficients are zero. This character sector has multiplicity \(\binom dj(q-1)^j\). The constant sector is \(j=0\), and all other sectors lie in the zero-sum space.

**2. All admissible ordinary graph metrics.** At \(k=1\), the distance is ordinary Hamming distance, a sum of coordinatewise squared-Euclidean distances. At \(d\le k\), the graph is complete, so its distance matrix is \(J-I\) and has nonconstant eigenvalues \(-1\).

When \(q=2\) and \(k=2\), for every integer Hamming distance \(r\) we have the identity

\[
\left\lceil\frac r2\right\rceil
=\frac r2+\frac{1-(-1)^r}{4}.
\]

The first term is a positive multiple of the ordinary Hamming squared distance, while the second is the squared distance of one parity-sign coordinate, so their sum is conditionally negative semidefinite. Finally, for \(q=2\) and \(d=k+1\), every nonzero Hamming radius other than the antipodal radius has graph distance one, while antipodes have distance two. Thus \(D=J-I+A_d\), where \(A_d\) is the antipodal permutation. On a nonconstant Walsh character of support \(j\), the eigenvalue is \(-1+(-1)^j\le0\).

**3. Universal obstructions in all other dimensions.** Fix \(q\ge3\) and \(k\ge2\). In dimension \(m=k+1\ge3\), the graph distance matrix is \(D=J-I+A_m\), where \(A_m=(J_q-I_q)^{\otimes m}\) connects pairs differing in every coordinate. A character with support \(j=2\) has nonconstant eigenvalue

\[
-1+(q-1)^{m-2}>0.
\]

Since this subcube sits isometrically in every greater dimension, no \(d\ge k+1\) can have conditional negative type.

For \(q=2\), \(k\ge3\), and \(m=k+2\), let \(A_r\) denote the binary Hamming-radius-\(r\) matrix. Here \(D=J-I+A_{m-1}+A_m\). On the Walsh character of support two, the Fourier eigenvalue is

\[
-1+(m-4)+1=m-4=k-2>0.
\]

More explicitly, assign coefficients \(c(x)=(-1)^{x_1+x_2}\) on the \(2^m\)-point subcube, zero elsewhere. Their sum vanishes and \(c^{\mathsf T}Dc=2^m(k-2)>0\). Isometric inclusion excludes every \(d\ge k+2\). This and Step 2 exhaust every \((q,d,k)\).

**4. Exact powered endpoints.** Write \(b=2^p-1\ge0\). In the first excluded nonbinary dimension \(m=k+1\), every positive graph distance is one or two, hence

\[
D^{(p)}=J-I+bA_m,\qquad
\lambda_j(b)=-1+b(-1)^j(q-1)^{m-j},\quad 1\le j\le m.
\]

For \(q\ge3\), the largest positive coefficient of \(b\) on the nonconstant sectors is uniquely \((q-1)^{m-2}\), attained at \(j=2\). All sectors are strictly negative for \(b<(q-1)^{-(m-2)}\), with exactly the \(j=2\) sector vanishing at equality. Its multiplicity is \(\binom m2(q-1)^2\).

For the first excluded binary dimension \(m=k+2\), we similarly have

\[
D^{(p)}=J-I+b(A_{m-1}+A_m),\qquad
\lambda_j(b)=-1+b(-1)^j(m+1-2j),\quad 1\le j\le m.
\]

For even \(j\ge2\), the largest coefficient is \(m-3\) at \(j=2\). For odd \(j\), it is \(m-1\) at \(j=m\) if \(m\) is odd, and \(m-3\) at \(j=m-1\) if \(m\) is even. Therefore the maximum and its multiplicity are exactly \(M_m\) and \(\nu_m\) in the statement. In either alphabet family, \(\lambda_j\le0\) for all nonconstant sectors precisely up to the stated exponent. Beyond it the critical sector becomes positive, so the exponential kernel has a negative eigenvalue for all sufficiently small \(t>0\) by differentiating at \(t=0\).

The endpoint Euclidean rank follows from the nonconstant spectral nullity. For an admissible exponent, distinct graph vertices have nonzero powered distance, hence their Euclidean representing points are distinct. Gaussian kernels on finitely many distinct Euclidean points are strictly positive definite at every \(t>0\), including when the centered squared-distance form is singular.

## Verification

Run `python3 hamming_power_verify.py` with a standard Python 3 interpreter. The program tests the exact Hamming-scheme character sums for \(q=2,\dots,6\) and \(d\le10\), all graph-power orders in that finite rectangle, the rational critical kernel eigenvalues and multiplicities for nonbinary \(d\le8\) and binary \(d\le11\), and independently reconstructs graph shortest paths by breadth-first search for small alphabets and dimensions. It reports `HAMMING_POWER_EXACT_CHECK_OK 5278` if the tests succeed. The unlimited-parameter assertions come from Steps 1–4 and are not inferred from the finite checks.

## Relationship to prior work

The Hamming graph powers and their coding-theoretic motivation are already classical: Klotz and Sharifiyazdi study their distance chromatic number, and Kokkala and Östergård study binary square-hypercube colouring. Lee and Obata treat *exact-distance* graphs on cubes in asymptotic operator models, distinct from the *power* graph joining all distances up to a cutoff. Aalipour and collaborators compute distance spectra of halved cubes among other families; the halved-cube distance matrix is not the full powered Hamming-graph distance matrix. None of those inspected statements supplies the present all-alphabet conditional-negative-type classification or the sharp first-failure powered-distance exponents. The character-diagonalization method and the Hamming association scheme are established prior tools, not claimed as novel.

## Limitations

The theorem does not determine optimal fractional exponents in excluded dimensions larger than the first failure, nor positivity of the exponential kernel at individual scales outside the all-scale class. The literature comparison is bounded rather than an exhaustive mathematical priority determination. Independent mathematical validation has not been performed.

## References

1. H. H. Lee and N. Obata, *Distance k-graphs of hypercube and q-Hermite polynomials*, arXiv:1208.3792, first public arXiv version 2012-08-18. https://arxiv.org/abs/1208.3792
2. G. Aalipour et al., *On the distance spectra of graphs*, arXiv:1509.01196, first public arXiv version 2015-09-03. https://arxiv.org/abs/1509.01196
3. J. I. Kokkala and P. R. J. Östergård, *The chromatic number of the square of the 8-cube*, arXiv:1607.01605, first public arXiv version 2016-07-06. https://arxiv.org/abs/1607.01605
4. W. Klotz and E. Sharifiyazdi, *On the distance chromatic number of Hamming graphs*, Advances and Applications in Discrete Mathematics 2 (2008), 103–115. https://www.researchgate.net/publication/256063204_On_the_Distance_Chromatic_Number_of_Hamming_Graphs
5. The classical finite-group character criterion for positive definiteness and Schoenberg's negative-type theorem, used in their standard finite-metric forms.
