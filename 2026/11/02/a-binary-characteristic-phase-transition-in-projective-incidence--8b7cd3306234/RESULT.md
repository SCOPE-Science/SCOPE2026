# A binary characteristic phase transition in projective incidence Gaussian kernels

## Finding
Let \(q\ge2\) be any prime power and \(d\ge2\) an integer. In the finite projective space \(\mathrm{PG}(d,q)\), form the bipartite graph \(G_{d,q}\) whose vertices are all points and all hyperplanes, with adjacency given by containment. Let \(\rho\) be its shortest-path metric. Define
\[
 v=\frac{q^{d+1}-1}{q-1},\qquad
 k=\frac{q^d-1}{q-1},\qquad
 t=q^{(d-1)/2},
\]
and let \(s=s_{d,q}\) be the unique positive solution of
\[
 t(3^s-1)=2^s.
\]
The largest exponent \(\beta_{d,q}\) for which \(\rho^p\) is conditionally negative semidefinite is
\[
\boxed{
\beta_{d,q}=\begin{cases}
 s,&q\ge3\ \text{or}\ (q=2,\ 2\le d\le4),\\
 c_{d},&q=2,\ d\ge5,
\end{cases}}
\]
where \(c_d\in(0,s_{d,2})\) is the unique solution of
\[
 (v-1)2^{c_d}-(v-k)3^{c_d}-k=0.
\]
For every real \(p\ge0\), conditional negative type holds precisely when \(p\le\beta_{d,q}\); it is strict for \(p<\beta_{d,q}\). Equivalently, the Gaussian distance kernel
\[
 K_{u,p}(x,y)=\exp(-u\rho(x,y)^p),\qquad u>0,
\]
is positive semidefinite for every \(u>0\) precisely in this range. In fact it is strictly positive definite for each \(u>0\) in the admitted range.

There is a sharp change of endpoint obstruction. In the first regime the zero-sum nullity of the powered distance matrix at \(p=\beta_{d,q}\) is \(v-1\), and its least squared-Euclidean embedding dimension is \(v\). In the binary regime \(d\ge5\), the nullity is \(1\), spanned by the vector equal to \(+1\) on points and \(-1\) on hyperplanes, and the embedding dimension is \(2v-2\). Before the threshold, the embedding dimension is \(2v-1\).

For example, \(\beta_{4,2}\approx0.335837815721\), but \(\beta_{5,2}\approx0.140368396171\), whereas the competing singular-mode root at \(d=5\) is \(s_{5,2}\approx0.234723152537\). As \(d\to\infty\) at fixed \(q\ge3\),
\[
 \beta_{d,q}\sim \frac{1}{(\log3)q^{(d-1)/2}},
\]
but in characteristic two,
\[
 \beta_{d,2}\sim\frac{1}{2^d\log(4/3)}.
\]

## Assumptions and scope
The finite field of order \(q\) exists because \(q\) is a prime power. No incidence polarity or transitivity beyond the ordinary projective construction is assumed. For \(p=0\), define the powered-distance matrix to have zero diagonal and unit off-diagonal; for \(p>0\), use ordinary positive real powers of shortest-path distances. Conditional negative type means \(\sum_{x,y} a_xa_y\rho(x,y)^p\le0\) for every real vector with \(\sum_x a_x=0\). Euclidean embedding dimension refers to the minimum \(m\) for which there exist points \(z_x\in\mathbb R^m\) with \(\|z_x-z_y\|^2=\rho(x,y)^p\). Claims concern the full point–hyperplane graph, not its nonincidence complement.

## Proof
**1. Exact distance-power spectrum.** Write \(A\) for the \(v\)-by-\(v\) point–hyperplane incidence matrix, with rows indexed by points. A hyperplane has \(k\) points, each point belongs to \(k\) hyperplanes, and two distinct points lie in \(\lambda=(q^{d-1}-1)/(q-1)\) common hyperplanes. Duality gives the same block–block intersection number. Therefore
\[
 A\mathbf1=k\mathbf1,\qquad
 AA^{\mathsf T}=(k-\lambda)I+\lambda J=t^2I+\lambda J.
\]
Distinct vertices in the same bipartition class have distance two; an incident point–hyperplane pair has distance one, and a nonincident pair has distance three. Accordingly, writing \(D_p=(\rho(x,y)^p)\),
\[
 D_p=\begin{pmatrix}
 2^p(J-I)&3^pJ-(3^p-1)A\\
 3^pJ-(3^p-1)A^{\mathsf T}&2^p(J-I)
 \end{pmatrix}.
\]
On the orthogonal complement of the global constants, its eigenvalues are exactly
\[
 h(p)=(v-1)2^p-(v-k)3^p-k \quad\text{(multiplicity one)},
\]
and
\[
 g_+(p)=-2^p+t(3^p-1),\qquad
 g_-(p)=-2^p-t(3^p-1)
\]
(each of multiplicity \(v-1\)). The first eigenspace is the point-versus-hyperplane contrast; the other two arise by pairing the nonconstant singular vectors of \(A\). The omitted global-constant eigenvalue is positive. For all \(p\ge0\), \(g_-(p)<0\); \(g_+(p)\) increases strictly through zero exactly once, at \(p=s\), since \(g_+(0)=-1\) and \(g_+'(p)=t(\log3)3^p-(\log2)2^p>0\).

**2. Which mode reaches zero first?** The design identities imply \(k-\lambda=t^2\) and \(v=(k^2-t^2)/(k-t^2)\). At \(p=s\), put \(x=2^s\) and use \(3^s=1+x/t\). Algebra gives
\[
 h(s)=\frac{k-t}{k-t^2}\big((k-1)x-k-t\big).
\]
The prefactor is positive, so the comparison is between \(x\) and
\[
 x_0=\frac{k+t}{k-1}
 =1+\frac{q-1}{q(t-1)}.
\]
Write \(\alpha=\log_2 3\). The positive number \(x\) is the unique solution \(x>1\) of \(t(x^\alpha-1)=x\). Since \(\alpha>3/2\), Bernoulli's inequality gives
\[
 x-1\le\frac{1}{\alpha t-1}<\frac{2}{3(t-1)}
 \le \frac{q-1}{q(t-1)} \quad(q\ge3).
\]
Hence \(h(s)<0\) for every \(q\ge3\).

For \(q=2\), \(x_0=1+1/[2(t-1)]\) and \(t=2^{(d-1)/2}\). The function \(F_t(X)=t(X^\alpha-1)-X\) is strictly increasing on \(X\ge1\). For \(d=2,3\), with \(t=\sqrt2,2\), the inequality \(\alpha>3/2\) and the exact positive quantities
\[
 x_0^3-(1+x_0/t)^2=\frac94+\frac{11\sqrt2}{8}
 \quad(t=\sqrt2),\qquad \frac5{16}\quad(t=2)
\]
show \(F_t(x_0)>0\). For \(d=4\), \(t=2\sqrt2\), use \(\alpha>11/7\), since \(2^{11}<3^7\); direct rationalization shows
\[
 x_0^{11}-(1+x_0/t)^7
 =\frac{60239381294415}{129586085429248}
 +\frac{119793971382233\sqrt2}{518344341716992}>0.
\]
Thus \(x<x_0\) in each of these three dimensions, and \(h(s)<0\).

For \(d\ge5\), first take \(t>5\). Since \(\alpha<8/5\), we have, for \(X\ge1\),
\[
 X^\alpha-1\le\frac85(X-1)X.
\]
At \(X=x_0\), this implies \(t(X^\alpha-1)\le X\,4t/[5(t-1)]<X\). The remaining discrete value \(t=4\) corresponds to \(d=5\); here \(x_0=7/6\), and \((7/6)^8<(31/24)^5\) gives \(x_0^\alpha<31/24=1+x_0/4\). Consequently \(F_t(x_0)<0\) for every \(d\ge5\), and \(h(s)>0\).

**3. Sharpness and nullities.** We have \(h(0)=g_+(0)=-1\). If \(h(s)<0\), all nonconstant eigenvalues are nonpositive at \(s\). The interval property of negative type (a nonnegative exponent below an admissible exponent is admissible) makes every smaller exponent admissible; strictness below the largest admissible exponent follows also directly from the strict snowflake principle. At \(s\) only the \(g_+\)-sector vanishes. Beyond \(s\), \(g_+>0\) rules out negative type.

If \(h(s)>0\), the function \(2^{-p}h(p)=(v-1)-(v-k)(3/2)^p-k2^{-p}\) is strictly concave, negative at zero and positive at \(s\). Hence it has exactly one zero \(c\in(0,s)\), is negative before \(c\), and positive for \(c<p\le s\). For \(p>s\), \(g_+(p)>0\). Thus \(c\) is sharp and only the contrast sector vanishes at the endpoint. The positive-semidefinite Gaussian-kernel characterization follows from Schoenberg's criterion for conditionally negative definite matrices; the strictness for each \(u>0\) follows from the injectivity of the finite squared-distance Euclidean embedding. For centered Gram matrix \(B=-\tfrac12 H D_pH\), its rank is \(2v-1\) minus the zero-sum nullity, yielding the stated dimensions.

**4. Large-dimension asymptotics.** For fixed \(q\ge3\), \(t\to\infty\) and \(s\to0\), so expanding \(t(3^s-1)=2^s\) gives \(s\sim1/(t\log3)\). For \(q=2\), write \(N=2^d\), so \(v=2N-1\), \(k=N-1\) and
\[
 h(p)=(2N-2)2^p-N3^p-(N-1).
\]
The first positive zero tends to zero, because \(h(0)=-1\) but \(2\cdot2^p-3^p-1>0\) for every sufficiently small fixed \(p>0\). Taylor expansion at zero yields \(h'(0)=N\log(4/3)-2\log2\), and the second derivative is \(O(N)\) for bounded \(p\). Thus \(c_d\sim1/[2^d\log(4/3)]\).

## Verification
The included standalone script `verify_projective_incidence.py` uses only the Python standard library. It reconstructs the point–hyperplane incidence graphs of \(\mathrm{PG}(d,q)\) for eight representative prime-field cases, including the two sides of the binary dimension boundary. It checks the exact design intersection identities, every shortest-path distance, the predicted contrast and singular-pair eigenvectors at several real exponents, and the signs of the two competing spectral branches at the calculated threshold. Output ends with `PROJECTIVE_INCIDENCE_NEGATIVE_TYPE_PHASE_OK`. The general prime-power and all-dimension theorem is proved above; finite tests are consistency checks, not an infinite certificate.

## Relationship to prior work
Sánchez established general finite-metric negative-type tests and the interval principle. Murugan studied generalized roundness of regular/vertex-transitive distance matrices, giving a determinant-based characterization. The 2015 distance-spectra work of Aalipour and collaborators concerns unpowered graph distance matrices. Mirafzal computed ordinary distance eigenvalues for exactly the projective point–hyperplane graphs (in the equivalent form \(S(q,d+1,1)\)); the present calculation does not claim those ordinary eigenvalues as new. The derived all-real-exponent threshold and its binary field/dimension change are not stated in these inspected works. Earlier projective-plane incidence and nonincidence exponents are consistent with the \(d=2\) specialization and are not claimed as new.

## Limitations
No assertion is made for arbitrary nonsymmetric incidence geometries, other graph powers, or metrics weighted differently from unit edges. The novelty comparison is bounded by literature access and search coverage; an equivalent result in older metric-embedding or algebraic-graph literature may exist. The calculation provides mathematical proof and reproducible finite checks, not independent validation.

## References
1. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451 (first posted 2011-08-02), especially Section 2.
2. M. K. Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657 (first posted 2011-12-23), especially Theorem 3.1.
3. G. Aalipour et al., *On the distance spectra of graphs*, arXiv:1509.01196 (first posted 2015-09-03).
4. S. M. Mirafzal, *On the distance eigenvalues of design graphs*, arXiv:2111.05239 (first posted 2021-11-09), especially Theorem 3.1.
