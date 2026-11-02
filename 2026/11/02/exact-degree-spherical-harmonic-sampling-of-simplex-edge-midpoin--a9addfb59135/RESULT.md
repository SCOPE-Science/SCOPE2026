# Exact-degree spherical-harmonic sampling of simplex-edge midpoints

## Finding

Let \(n\ge5\) be an integer, \(N=\binom n2\), and \(X_n\subset S^{n-2}\) the \(N\) centered, normalized midpoints of the edges of a regular \((n-1)\)-simplex. For each integer \(k\ge0\), let \(E_{n,k}\) evaluate **homogeneous spherical harmonics of exact degree** \(k\) at every point of \(X_n\), with real target \(\mathbb R^N\). Then

\[
\operatorname{rank}E_{n,k}=\begin{cases}
1,&k=0,\\
n-1,&k=1,\\
N-1,&k=2,\\
N-(n-1),&(n,k)=(8,3),\\
N-1,&(n,k)=(8,4)\text{ or }(16,5),\\
N,&\text{otherwise, for }k\ge3.
\end{cases}
\]

In particular, every exact harmonic degree \(k\ge6\) interpolates arbitrary data on \(X_n\) for **every** \(n\ge5\). At \(n=16\), precisely the degree-five constant-weight direction is absent: all degree-five harmonics have zero sum over the \(120\) vertices, whereas the evaluation rank is \(119\). At \(n=8\), the degree-three defect has dimension \(7\), and the degree-four defect has dimension \(1\). The equal-weight harmonic-index degrees of \(X_n\) are exactly \(\{1,2\}\), enlarged by \(\{4\}\) for \(n=8\) and by \(\{5\}\) for \(n=16\).

The complete **normalized sampling Gram spectrum** is also explicit at every degree. Set
\[
P_{n,k}(z)=\frac{C_k^{(n-3)/2}(z)}{C_k^{(n-3)/2}(1)},\qquad
a=\frac{n-4}{2(n-2)},\qquad b=-\frac2{n-2}.
\]
Here \(C_k^{\lambda}\) denotes the ordinary Gegenbauer polynomial, and \(P_{n,k}(1)=1\). The Gram matrix \(G_{n,k}=(P_{n,k}(\langle x,y\rangle))_{x,y\in X_n}\) has eigenvalues
\[
\begin{aligned}
\gamma_0&=1+2(n-2)P_{n,k}(a)+\frac{(n-2)(n-3)}2 P_{n,k}(b),&&\text{multiplicity }1,\\
\gamma_1&=1+(n-4)P_{n,k}(a)-(n-3)P_{n,k}(b),&&\text{multiplicity }n-1,\\
\gamma_2&=1-2P_{n,k}(a)+P_{n,k}(b),&&\text{multiplicity }\frac{n(n-3)}2.
\end{aligned}
\]
These nonnegative numbers determine rank by counting positive eigenvalues with multiplicity.

## Assumptions and scope

Let \(e_1,\dots,e_n\) be the standard basis of \(\mathbb R^n\), let \({\bf1}=(1,\ldots,1)\), and put \(H=\{u:\sum_i u_i=0\}\), with its inherited Euclidean inner product. The point labelled by an unordered pair \(\{i,j\}\) is
\[
x_{ij}=\frac{e_i+e_j-(2/n){\bf1}}{\sqrt{2(n-2)/n}}\in H.
\]
The degree-\(k\) harmonic space is the real space of homogeneous polynomials of degree \(k\) on \(H\) annihilated by the Euclidean Laplacian on \(H\). The result covers all integral \(n\ge5\) and all integral \(k\ge0\); it does not assert the same ranks for other hypersimplex levels or for \(n=4\), where antipodal symmetry changes the pattern. Annihilation by all harmonics of degree \(k\) is equivalent to vanishing of the constant-weight projection of \(G_{n,k}\).

## Proof

**1. Three Johnson-scheme sectors.** Distinct centered simplex-edge midpoints have inner product \(a\) when their labels share one index and \(b\) when their labels are disjoint. The adjacency matrix \(A\) of the triangular graph \(J(n,2)\) has eigenvalues \(2(n-2),n-4,-2\), of multiplicities \(1,n-1,n(n-3)/2\). This follows, without classification assumptions, by writing the unsigned vertex-edge incidence matrix \(M\): \(M^{\mathsf T}M=2I+A\), while \(MM^{\mathsf T}=(n-2)I+J\). The disjointness matrix is \(J-I-A\). Hence \(G_{n,k}=I+P_{n,k}(a)A+P_{n,k}(b)(J-I-A)\), which yields the three displayed eigenvalues. The spherical harmonic addition formula identifies \(G_{n,k}\), up to a strictly positive scalar, with \(E_{n,k}E_{n,k}^{\mathsf T}\).

**2. Exact low-degree and finite-degree certificates.** Direct Gegenbauer substitution gives for degrees \(0,1,2\) the ranks \(1,n-1,N-1\). In degree \(3\),
\[
\gamma_1=\frac{n^2(n-8)^2(n-3)}{8(n-2)^4},\quad
\gamma_0=\frac{n(n-4)^2(n+1)}{4(n-2)^3},\quad
\gamma_2=\frac{3n^2(n-4)(n+1)}{4(n-2)^4}.
\]
The possible degree-four and degree-five constant-sector zeros are respectively
\[
\gamma_0(n,4)=\frac{n(n-8)^2(n-3)(n+3)}{8(n-2)^4},\qquad
\gamma_0(n,5)=\frac{n(n-16)^2(n-4)(n-3)(n+3)}{16(n-2)^5}.
\]
All other sector zeros at integral \(n\ge5\) in degrees \(3\le k\le20\) are excluded by an exact **finite integer-root certificate**, reproduced in `verify.py`. Here are the integer-polynomial identities used by the certificate, so that its check has a mathematical interpretation. Define
\[
F_k=\prod_{j=0}^{k-1}(n-3+j),\qquad H_r=\prod_{j=0}^{r-1}(n-3+2j),\qquad R_k=2^k(n-2)^kF_k,
\]
with empty products equal to \(1\), and define the integer polynomial
\[
U_k(z)=k!\sum_{j=0}^{\lfloor k/2\rfloor}
\frac{(-1)^j2^jH_{k-j}z^{k-2j}(n-2)^{2j}}{j!(k-2j)!}.
\]
The Gegenbauer expansion gives \(P_{n,k}(a)=U_k(n-4)/R_k\) and \(P_{n,k}(b)=U_k(-4)/R_k\). Thus the three eigenvalues have respective numerators
\[
\begin{aligned}
&2R_k+4(n-2)U_k(n-4)+(n-2)(n-3)U_k(-4),\\
&R_k+(n-4)U_k(n-4)-(n-3)U_k(-4),\\
&R_k-2U_k(n-4)+U_k(-4),
\end{aligned}
\]
with denominators \(2R_k,R_k,R_k\), all positive at \(n\ge5\). For each \(3\le k\le20\), the certificate forms these integer polynomials, strips the known irrelevant factors \(n\), \(n-3\), \(n-4\), divides by their integer coefficient content, enumerates **all positive divisors of the remaining nonzero constant term** using fully checked prime factorization, and evaluates the resulting candidates exactly (using modular filters only for rejection). By the rational-root theorem, this is exhaustive over all integral \(n\ge5\), with surviving roots only \((k,\text{sector},n)=(3,1,8),(4,0,8),(5,0,16)\). The source code is part of this package; it performs no floating-point tests.

**3. Uniform high-degree proof, without finite extrapolation.** We prove that \(E_{n,k}\) has full row rank whenever \(k\ge21\). Suppose real weights \(w_{ij}\) annihilate every exact-degree harmonic on \(X_n\). Complexify and choose any \(v\in H_{\mathbb C}\) satisfying \(\sum_i v_i^2=0\). Since \((v\cdot x)^k\) is harmonic, \(\sum_{i<j}w_{ij}(v_i+v_j)^k=0\).

Fix any four indices, relabel them \(1,2,3,4\), and set all other coordinates of \(v\) to zero. Write
\[
(v_1,v_2,v_3,v_4)=\tfrac12(s+t+u,\ s-t-u,\ -s+t-u,\ -s-t+u).
\]
Then \(\sum v_i=0\) and \(\sum v_i^2=s^2+t^2+u^2\). Put \(D_i=\sum_{j\notin\{1,2,3,4\}}w_{ij}\). On the complex conic \(s^2+t^2+u^2=0\), the annihilation identity is
\[
\sum_{i=1}^4D_iv_i^k+
(w_{12}+(-1)^kw_{34})s^k+
(w_{13}+(-1)^kw_{24})t^k+
(w_{14}+(-1)^kw_{23})u^k=0.
\]
The seven linear forms \(v_1,v_2,v_3,v_4,s,t,u\), restricted to this nonsingular conic, become seven binary quadratics with **two simple roots each and no shared root between distinct quadratics**. This can be verified directly: their coefficient triples are the three coordinate normals and four tetrahedral sign normals; each normal has nonzero squared length, and the cross product of any two distinct normals has nonzero squared length.

We use an elementary Wronskian bound. If \(r\le7\) such pairwise root-disjoint binary quadratics have a minimal linear dependence among their \(k\)-th powers, take the nonzero Wronskian of any \(r-1\) independent powers. As a section on \(\mathbb P^1\), its degree is \((r-1)(2k-r+2)\). At each of the \(2r\) disjoint zeros of the original quadratics it vanishes to order at least \(k-r+2\): minimal dependence permits replacing the omitted power by any of the included powers when forming the Wronskian. Hence
\[
2r(k-r+2)\le(r-1)(2k-r+2),
\]
which implies \(k\le(r-2)(r+1)/2\le20\). Therefore all seven powers are independent for every \(k\ge21\).

Consequently, \(D_i=0\) and \(w_{ab}=(-1)^{k+1}w_{cd}\) for every pair of disjoint edges \(ab,cd\). The graph of disjoint pairs \(KG(n,2)\) is connected for \(n\ge5\), and it contains a five-cycle. For even \(k\), alternating signs around that cycle force every weight to vanish. For odd \(k\), connectivity makes all weights equal to one constant \(c\), and the equations \(D_i=(n-4)c=0\) force \(c=0\). This rules out every nonzero annihilator, completing the proof for all degrees.

## Verification

Execute `python3 verify.py` with Python 3. The program uses only the standard library. It constructs all 54 exact sector polynomials for \(3\le k\le20\), applies the integer-root theorem by exhaustive divisor checking, verifies the required four-coordinate conic incidence facts, and asserts precisely the three exceptional positive roots. The expected message is `HYPERSIMPLEX_SAMPLING_CERTIFICATE_OK`. The analytically proved Wronskian bound handles every \(k\ge21\); the finite certificate by itself does **not** imply the infinite theorem.

## Relationship to prior work

Musin's 2008 study explicitly uses the edge-midpoint two-distance configuration to obtain sharp bounds on spherical two-distance sets, but its polynomial independence argument concerns degree-at-most-two dimension bounds, not the present exact-degree harmonic evaluation spectrum. Bannai–Okuda–Tagami (first publicly posted 2013) develop harmonic-index spherical designs and Gegenbauer methods; Zhu–Bannai–Bannai–Kim–Yu (first publicly posted 2015) chiefly classify tight designs of specified **even** harmonic indices; Barg–Glazyrin–Okoudjou–Yu (2014) classify tight two-distance frames. None of those inspected statements supplies the exact all-degree rank classification or the unusual \(n=16,k=5\) defect. Misawa–Munemasa–Sawa (2024 preprint, published 2026) study *simultaneous* consecutive odd harmonic-index cancellation and do not determine this single exact-degree family spectrum. The \(n=8\) ranks are consistent with the already-known antipodal Gosset/equiangular-line case; they are included for completeness, not separately asserted as a new isolated phenomenon.

## Limitations

The proof is for integer dimensions \(n\ge5\) and the specific centered weight-two hypersimplex orbit, and does not characterize all spherical designs with a fifth harmonic cancellation. The polynomial-root stage is a finite exact computation, exposed as standalone source; no claim of independent mathematical validation or a formal proof assistant is made. An equivalent all-degree calculation might exist in older Johnson association-scheme, tight-frame, or cubature literature; the literature search cannot establish absolute priority. The result establishes ranks and all three Gram eigenvalues, but not a uniform lower bound on their positive magnitudes.

## References

1. O. R. Musin, *Spherical two-distance sets*, arXiv:0801.3706, first posted 2008-01-24. The original simplex-edge midpoint configuration appears in Section 1, and polynomial dimension arguments in Section 2.
2. E. Bannai, T. Okuda, M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101, first posted 2013-08-23; later Journal of Approximation Theory 195 (2015), 1–18.
3. A. Barg, A. Glazyrin, K. Okoudjou, W.-H. Yu, *Finite two-distance tight frames*, arXiv:1402.3521, first posted 2014-02-14.
4. Y. Zhu, E. Bannai, E. Bannai, K.-T. Kim, W.-H. Yu, *More on spherical designs of harmonic index t*, arXiv:1507.05373, first posted 2015-07-20.
5. R. Misawa, A. Munemasa, M. Sawa, *Antipodality of spherical designs with odd harmonic indices*, arXiv:2410.09471, first posted 2024-10-12; Discrete Mathematics 349 (2026), 114978.
