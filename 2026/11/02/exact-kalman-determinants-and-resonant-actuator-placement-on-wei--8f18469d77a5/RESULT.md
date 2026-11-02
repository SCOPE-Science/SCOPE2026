# Exact Kalman determinants and resonant actuator placement on weighted fans

## Finding
Let \(n\ge3\), and let \(F_n(t)\), \(t>0\), be the weighted fan with a hub \(0\), path vertices \(1,\ldots,n\), unit conductance on each path edge and conductance \(t\) on every hub-to-path spoke. Let \(L_n(t)\) be its combinatorial weighted Laplacian. Put
\[
\lambda_k=2-2\cos(k\pi/n)\quad(1\le k\le n-1),\qquad
q_n(z)=\prod_{k=1}^{n-1}(z-\lambda_k)=(-1)^{n-1}U_{n-1}(1-z/2).
\]
For a single unit point actuator at vertex \(j\), define the square Kalman matrix
\[
\mathcal C_j(t)=[e_j,L_n(t)e_j,\ldots,L_n(t)^n e_j].
\]
Then for **every path vertex** \(1\le j\le n\),
\[
\boxed{|\det\mathcal C_j(t)|=
\begin{cases}
\dfrac{t}{n}|q_n(-t)q_n(nt)|,&\gcd(2j-1,n)=1,\\[4pt]
0,&\gcd(2j-1,n)>1.
\end{cases}}
\]
Here and below, the displayed determinant is the determinant of the square Kalman matrix, not the infinite-horizon controllability Gramian. A sole hub actuator always has determinant zero. In particular, away from the finite exceptional set
\[
\mathcal T_n=\{\lambda_k/n:1\le k\le n-1\},
\]
precisely \(\varphi(2n)\) individual path locations are controllable, **and their absolute Kalman determinants are exactly equal**. At each of the \(n-1\) distinct exceptional spoke strengths every single-vertex actuator fails, because a Laplacian eigenvalue becomes double. Nevertheless the minimum number of independent vertex actuators is two there, versus one elsewhere.

For any two distinct path vertices \(j,\ell\), put \(A=2j-1\), \(B=2\ell-1\). Their two-input pair is controllable off \(\mathcal T_n\) exactly when
\[\gcd(n,A,B)=1.\]
At \(t=\lambda_k/n\), the necessary and sufficient condition is the same gcd condition **together with**
\[
2n\nmid k(j-\ell)\qquad\text{and}\qquad 2n\nmid k(j+\ell-1).
\]
The hub and a path vertex \(j\) are jointly controllable for *every* \(t>0\) if and only if \(\gcd(2j-1,n)=1\). Thus both the hub–endpoint pair \(\{0,1\}\) and the neighboring-path pair \(\{1,2\}\) work at every positive spoke strength; these two placements also follow from existing zero-forcing results and are not presented as new by themselves.

Finally, at each resonance \(t_k=\lambda_k/n\) the common nonzero single-site determinant for coprime locations vanishes *linearly*, with the exact one-sided absolute slope
\[
\boxed{\lim_{t\to t_k}\frac{|\det\mathcal C_j(t)|}{|t-t_k|}
=\frac{\lambda_k}{2\sin^2(k\pi/n)}
\prod_{h=1}^{n-1}\left(\lambda_h+\frac{\lambda_k}{n}\right)>0,\quad\gcd(2j-1,n)=1.}
\]

## Assumptions and scope
Every \(n\) is an integer at least three; every spoke weight \(t\) is strictly positive. The graph has \(n+1\) scalar states, an undirected connected weighted Laplacian, and independent unit-amplitude vertex inputs. The dynamics may be written \(\dot x=-L_n(t)x+Bu\); changing \(L_n(t)\) to \(-L_n(t)\) changes only column signs, leaving the absolute single-input determinant and all controllability statements unchanged. For two input vertices, the controllability matrix comprises all columns \(L_n(t)^r e_j\), \(L_n(t)^r e_\ell\), with \(0\le r\le n\), and full row rank means controllability. The zero-mode is included, and the singular cases at exactly \(t_k\) are part of the theorem. The claimed determinant is in the fixed standard vertex-coordinate Euclidean normalization; no claim is made about coordinate-invariant control energy.

## Proof
**1. Complete orthonormal Laplacian decomposition.** The weighted fan Laplacian is the Laplacian of the path plus \(t\) times the hub-to-path star Laplacian. It has the normalized all-ones eigenvector \(v_0=\mathbf 1/\sqrt{n+1}\), of eigenvalue zero. It has an orthonormal hub-versus-path vector
\[
v_H=\frac{(-n,1,\ldots,1)}{\sqrt{n(n+1)}},\qquad L_n(t)v_H=(n+1)t\,v_H.
\]
For each \(1\le k\le n-1\), it has a path-supported vector \(v_k(0)=0\) and
\[
v_k(j)=\sqrt{\frac2n}\cos\left(\frac{(2j-1)k\pi}{2n}\right),\qquad
L_n(t)v_k=(t+\lambda_k)v_k.
\]
The cosine addition identity verifies the path-Laplacian eigenvalue equation and the weighted spoke edges add \(t\); orthogonality to the constant path mode makes the hub coordinate zero. Standard finite cosine orthogonality gives normalization and pairwise orthogonality. The \(\lambda_k\) increase strictly with \(k\), so the sole possible spectral coincidences are between \((n+1)t\) and \(t+\lambda_k\), precisely \(nt=\lambda_k\); at each such point the eigenspace has dimension two.

**2. Arithmetic visibility and product.** For a path site \(j\), write \(A=2j-1\) and \(d=\gcd(A,n)\), which is odd. A path-harmonic coordinate vanishes exactly when \(Ak\equiv n\pmod{2n}\). Writing \(n=db\) and \(A=da\), with coprime \(a,b\), shows that the invisible harmonics are exactly \(k=b,3b,5b,\ldots,(d-2)b\), a set of size \((d-1)/2\). Thus none vanish if and only if \(d=1\). In that case multiplication by odd \(A\), invertible modulo \(2n\), permutes the nontrivial cosine absolute values, so
\[
\prod_{k=1}^{n-1}\left|\cos\left(\frac{Ak\pi}{2n}\right)\right|
=\prod_{k=1}^{n-1}\cos\left(\frac{k\pi}{2n}\right)
=\frac{\sqrt n}{2^{n-1}}.
\]
The final identity follows from the elementary sine product \(\prod_{k=1}^{n-1}\sin(k\pi/n)=n/2^{n-1}\) and the double-angle formula. Multiplying the normalized modal amplitudes at \(j\) gives
\[
|v_0(j)v_H(j)\prod_{k=1}^{n-1}v_k(j)|
=\frac{1}{(n+1)(2n)^{(n-1)/2}}.
\]
There are exactly \(\varphi(2n)\) odd residues \(2j-1\) coprime to \(2n\), which are exactly the coprime sites.

**3. Exact Vandermonde determinant.** The columns of \(\mathcal C_j\) in the orthonormal eigenbasis form a diagonal modal-amplitude matrix times a Vandermonde matrix in the \(n+1\) eigenvalues. Consequently the absolute determinant is the product of the modal amplitudes and the absolute pairwise eigenvalue differences, including multiplicities; this identity remains true when an eigenvalue collision makes the Vandermonde determinant zero. For the \(n-1\) positive path eigenvalues, their pairwise Vandermonde product is
\[
\prod_{1\le k<\ell<n}(\lambda_\ell-\lambda_k)
=2^{(n-1)/2}n^{(n-3)/2}.
\]
To verify this normalization, differentiate the monic polynomial \(q_n(z)=(-1)^{n-1}U_{n-1}(1-z/2)\) at its roots; the exact derivative satisfies
\[
|q_n'(\lambda_k)|=\frac{n}{2\sin^2(k\pi/n)}.
\]
Then the product of derivatives is the **square** of the path eigenvalue Vandermonde, and the sine product yields the claimed factor. After multiplying this factor by the common modal-amplitude product, the remaining constant is \(1/[n(n+1)]\). Differences involving the zero eigenvalue and hub mode contribute \((n+1)t\), \(\prod_k(t+\lambda_k)\), and \(\prod_k|nt-\lambda_k|\), respectively. The claimed formula follows immediately:
\[
\frac{(n+1)t}{n(n+1)}\prod_k(t+\lambda_k)|nt-\lambda_k|
=\frac{t}{n}|q_n(-t)q_n(nt)|.
\]
If any path modal amplitude is zero, the determinant vanishes for all weights, as already counted.

**4. Exact one- and two-actuator criteria.** For a real symmetric matrix, the Popov–Belevitch–Hautus criterion says a set of vertex inputs controls the system precisely when restriction of **every eigenspace** to the selected vertices is injective. For one vertex, a double eigenspace always defeats injectivity, while a simple spectrum and nonzero eigenvector coordinates suffice. Hence the one-actuator count and the jump from one to two at \(t_k\).

For two path sites \(j,\ell\), a simple path eigenspace is invisible to both exactly when \(\gcd(n,2j-1,2\ell-1)>1\): by the preceding congruence the intersection of invisible-harmonic indices is nonempty precisely when that common odd gcd exceeds one. At a collision, the restrictions of \(v_H\) and \(v_k\) to the two path vertices form, up to nonzero row and column scales, the matrix
\[
\begin{pmatrix}1&\cos((2j-1)k\pi/(2n))\\1&\cos((2\ell-1)k\pi/(2n))\end{pmatrix}.
\]
It has nonzero determinant exactly when the cosines differ; their equality is equivalent to either \(2n\mid k(j-\ell)\) or \(2n\mid k(j+\ell-1)\). This proves the complete two-path classification. The hub coordinate vanishes on every \(v_k\), while it is nonzero on \(v_H\) and \(v_0\), so \(\{0,j\}\) is controllable exactly when every path harmonic is visible at \(j\). Finally \(\{1,2\}\) passes the pair condition, since neither \(k(1-2)\) nor \(k(1+2-1)\) is a multiple of \(2n\) for \(1\le k<n\). Thus two vertices always suffice.

**5. Exact approach to resonance.** At \(t_k=\lambda_k/n\), the factor \(q_n(nt)\) has a simple zero. Its absolute first-order coefficient is \(n|q_n'(\lambda_k)|\). Multiplying by \(t_k/n\) and \(|q_n(-t_k)|\) proves the displayed positive slope formula. This uses no limiting graph-size or numerical approximation.

## Verification
The accompanying dependency-free `verify_fan.py` builds integer-scaled weighted-fan Laplacians and Kalman matrices from the graph definition. Exact Bareiss determinants over integers check the formula against rational spoke strengths for every vertex, including the hub and the always-invisible vertices, on sizes \(3\le n\le9\). Exact rational row reduction independently checks the two-path and hub–path actuator criteria, including rational eigenvalue collisions. The verifier also checks the arithmetic zero-mode and simultaneous-zero counting rules for sizes through \(55\), and uses separate supplementary trigonometric products through \(32\). One completed replay yielded 30,141 successful assertions. The exact all-size proof is the spectral and number-theoretic argument above; finite checks are corroborative, not proof by enumeration.

## Relationship to prior work
Parlangeli and Notarstefano (arXiv:1109.3556v1, first public 16 September 2011) prove arithmetic reachability/observability criteria for path and cycle Laplacians, including path cosine eigenvectors. Those already provide the bare-path visibility mechanism used here, but their network has no weighted apex and does not have this spoke-resonance family or exact fan Kalman determinant. Aguilar and Gharesifard (first published 18 December 2014) give general Laplacian leader–follower controllability and spectral criteria, but their inspected text does not supply the fan determinant or exceptional spoke weights. The graph-join spectral literature provides a broader diagonalization technique, not an inspected full fan controllability classification.

The existing *Zero forcing polynomial of fan graphs* result explicitly gives \(\{0,1\}\) and \(\{1,2\}\) as minimum zero-forcing sets. Under the standard zero-forcing sufficient condition, that covers the robustness of those two particular pairs: they are included here as consistency checks, not as independent novelty. The inspected *Universal endpoint optimality for dynamical sampling on normalized paths* result treats a different graph operator (symmetric normalized adjacency), graph (plain path), and spectral-evolution determinant, and does not imply the weighted-fan determinant or its resonant collapse. The distinctive contribution proposed here is the exact determinant equality over all arithmetically admissible single sites, its finite sharp resonance locus and slope, and complete two-site parameter-specific classification. This is a best-knowledge comparison, not an assertion that all specialist literature was searched.

## Limitations
The theorem applies to one homogeneous spoke weight and unit path weights, not arbitrary individually weighted edges or directed dynamics. It concerns exact finite-dimensional controllability and a coordinate- and power-horizon-dependent Kalman determinant, not minimal-energy actuation or condition numbers. The ordinary path gcd criterion, spectral decomposition method, and robust zero-forcing pairs are already known. The closest general join-spectrum paper was not fully accessible, and hidden specialist overlap remains possible; no independent expert audit has been performed.

## References
1. G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556v1 (16 September 2011), https://arxiv.org/abs/1109.3556.
2. C. Aguilar and B. Gharesifard, *Graph Controllability Classes for the Laplacian Leader-Follower Dynamics*, IEEE Transactions on Automatic Control (first published 18 December 2014), DOI 10.1109/TAC.2014.2381435, https://www.geneseo.edu/~aguilar/public/assets/papers/tac2015.pdf.
3. D. M. Cardoso and collaborators, *Spectra of graphs obtained by a generalization of the join graph operation*, Discrete Mathematics (2013), DOI 10.1016/j.disc.2012.10.016. Only indexed sections were accessible for comparison.
4. *Zero forcing polynomial of fan graphs*, published-finding corpus published finding, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-zero-forcing-polynomial-of-fan-graphs--f3b2c94da283.
5. *Universal endpoint optimality for dynamical sampling on normalized paths*, published-finding corpus published finding, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-universal-endpoint-optimality-for-dynamical-sampling-on-normaliz--d0ca7333cb0f.
6. L. Dai, *Minimum leader selection for controllability of undirected graphs with leader–follower framework*, IET Control Theory & Applications, first published 29 October 2022, DOI 10.1049/cth2.12385 (general PBH/critical-set context).
