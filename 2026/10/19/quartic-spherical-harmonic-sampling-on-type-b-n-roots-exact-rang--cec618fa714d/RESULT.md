# Quartic spherical-harmonic sampling on type-\(B_n\) roots: exact range, spectrum and conditioning

## Finding
For every integer \(n\ge3\), select one representative from each antipodal pair of the normalized type-\(B_n\) roots:
\[
X_n^+=\{e_i:1\le i\le n\}\cup
\{(e_i+\varepsilon e_j)/\sqrt2:1\le i<j\le n,\ \varepsilon\in\{-1,1\}\}.
\]
Thus \(|X_n^+|=n^2\). Let \(\mathcal H_4(\mathbb R^n;\mathbb C)\) be the complex homogeneous harmonic quartics, restricted to the unit sphere, with probability-normalized spherical \(L^2\) inner product; let \(E_n\) evaluate such functions on \(X_n^+\). Write the sampled data as \(s_i\) at \(e_i\), and \(y_{ij}^\pm\) at \((e_i\pm e_j)/\sqrt2\).

**Exact attainable data.** The image of \(E_n\) is the codimension-\(n\) subspace given by the following \(n\) independent relations, one for each \(1\le i\le n\):
\[
2\sum_{j\ne i}\bigl(y_{\min(i,j),\max(i,j)}^+ + y_{\min(i,j),\max(i,j)}^-\bigr)
=(n-8)s_i+\sum_{k=1}^n s_k.
\tag{1}
\]
Consequently \(\operatorname{rank} E_n=n(n-1)\). Every feasible vector has an explicit harmonic-quartic interpolant given in the proof.

**Complete nonzero Gram spectrum.** With \(K_n=E_nE_n^*\), the four (possibly coincident) positive eigenvalue branches and multiplicities are
\[
\begin{array}{c|c}
\lambda_{\mathrm{odd}}=\dfrac{n(n+6)(n^2-4)}{24}&\binom n2\\[2pt]
\lambda_{\mathrm{std}}=\dfrac{n(n+6)(n+2)(n^2-8n+48)}{192}&n-1\\[2pt]
\lambda_{\mathrm{pair}}=\dfrac{n(n+6)(n+2)(n+4)}{32}&\dfrac{n(n-3)}2\\[2pt]
\lambda_{\mathrm{triv}}=\dfrac{n(n+6)(n+4)(n^2-4n+12)}{96}&1.
\end{array}
\tag{2}
\]
The zero eigenvalue has multiplicity \(n\). The pair branch has multiplicity zero at \(n=3\). Positive-branch coincidences occur only at \(n\in\{4,6,8,12,20\}\), respectively in the pairs (trivial, standard), (trivial, pair), (standard, odd), (standard, pair), and (odd, pair).

**Sharp dimension-dependent stability.** Let \(\kappa_n\) be the ratio of the largest to the smallest *positive* eigenvalue of \(K_n\) (so the condition number on the identifiable subspace is \(\sqrt{\kappa_n}\)). Then
\[
\kappa_n\ge\frac{15}{8}\quad(n\ge3),
\qquad \kappa_n=\frac{15}{8}\ \Longleftrightarrow\ n=6.
\tag{3}
\]
Thus the six-dimensional normalized type-\(B_n\) root configuration is the unique best-conditioned member of this family for fourth-degree harmonic interpolation on its attainable data space, with the stated unweighted counting norm on samples.

## Assumptions and scope
All dimensions \(n\) are integers at least three. The two root lengths are independently normalized to the unit sphere: the short roots are \(\pm e_i\) and the long roots are \((\pm e_i\pm e_j)/\sqrt2\). The sample measure is counting measure on the \(n^2\) chosen antipodal representatives; the domain is the **single** harmonic degree four, not the cumulative band. The \(L^2\) norm on the sphere uses probability surface measure. Data and harmonic polynomials may have complex coefficients. For the full \(2n^2\)-point antipodal root set, all attainable data must also be antipodally even; its nonzero unweighted Gram eigenvalues are twice those in (2).

## Proof
**1. Harmonic-trace obstruction and explicit converse.** Write a homogeneous quartic \(P\) as a sum of monomials. Only coefficients of \(u_i^4\), \(u_i^2u_j^2\), and \(u_i^3u_j,u_i u_j^3\) affect the chosen root samples; terms supported on three or four distinct coordinates vanish at every sample point. If the first two coefficients are \(a_i\) and \(b_{ij}\), harmonicity \(\Delta P=0\) yields
\[
12a_i+2\sum_{j\ne i}b_{\min(i,j),\max(i,j)}=0.
\tag{4}
\]
At the samples, \(s_i=a_i\) and \(y_{ij}^++y_{ij}^-=(a_i+a_j+b_{ij})/2\), giving (1).

Conversely, for any data obeying (1), define
\[
a_i=s_i,\quad b_{ij}=2(y_{ij}^++y_{ij}^-)-s_i-s_j,
\qquad c_{ij}=\frac{n+4}{n-2}(y_{ij}^+-y_{ij}^-).
\]
Writing \(r^2=\sum_{k=1}^n u_k^2\), put
\[
P_y(u)=\sum_i a_i u_i^4+\sum_{i<j}b_{ij}u_i^2u_j^2
+\sum_{i<j}c_{ij}u_i u_j\left(u_i^2+u_j^2-\frac6{n+4}r^2\right).
\tag{5}
\]
Condition (1) is exactly (4) for these coefficients, so the even part in (5) is harmonic. Each odd-pair summand is also harmonic since
\(\Delta[u_iu_j(u_i^2+u_j^2)]=12u_iu_j\) and \(\Delta[r^2u_iu_j]=2(n+4)u_iu_j\).
The odd-pair summand vanishes on all other sampled pairs and takes values \(\pm(n-2)/(2(n+4))\) on its own pair. Hence direct substitution proves \(E_nP_y=y\). Finally, a dependence between the \(n\) equations (1), with coefficients \(q_i\), forces \(q_i+q_j=0\) on every unordered pair. Because \(n\ge3\), this implies all \(q_i=0\). The equations are independent, proving the rank and complete image assertion.

**2. Zonal Gram kernel.** The standard spherical-harmonic addition formula gives the reproducing kernel
\[
K_n(x,y)=\frac{n(n+6)}{24}\left[(n+4)(n+2)\langle x,y\rangle^4
-6(n+2)\langle x,y\rangle^2+3\right].
\tag{6}
\]
Indeed the bracket at coincident points gives dimension \(\dim\mathcal H_4=n(n-1)(n+1)(n+6)/24\). Set \(c=n(n+6)/24\) and abbreviate the four kernel values at squared inner products \(0,1,1/4,1/2\) as
\[
k_0=3c,\quad k_1=c(n^2-1),\quad
k_q=c(n^2-18n+8)/16,\quad k_h=c(n^2-6n-4)/4.
\]

**3. Exact diagonalization.** Apply a unitary sum/difference transform to the two samples on each unordered pair. The odd differences form an eigenspace of dimension \(m=\binom n2\), with eigenvalue \(k_1-k_0=\lambda_{\mathrm{odd}}\). The remaining coordinate space is \(\mathbb C^n\oplus\mathbb C^m\). Let \(M\) be the unsigned vertex-edge incidence matrix of the complete graph on \(n\) vertices. Its Gram blocks are
\[
G_{SS}=(k_1-k_0)I_n+k_0J_n,
\]
\[
G_{SA}=\sqrt2\bigl[(k_h-k_0)M+k_0J_{n,m}\bigr],
\]
\[
G_{AA}=(k_1+3k_0-4k_q)I_m+2(k_q-k_0)M^*M+2k_0J_m.
\tag{7}
\]
Since \(MM^*=(n-2)I_n+J_n\), the subspace \(\ker M\) (dimension \(m-n=n(n-3)/2\), zero when \(n=3\)) has eigenvalue \(k_1+3k_0-4k_q=\lambda_{\mathrm{pair}}\). On the centered standard representation, \(G\) reduces to a \(2\times2\) Hermitian block whose diagonal entries are
\[
k_1-k_0,\qquad k_1+3k_0-4k_q+2(n-2)(k_q-k_0),
\]
with off-diagonal magnitude \(\sqrt{2(n-2)}|k_h-k_0|\). Its determinant vanishes identically and its trace equals \(\lambda_{\mathrm{std}}\), giving \(n-1\) positive and \(n-1\) zero eigenvalues.

On the two constant vectors, the diagonal entries are \(k_1+(n-1)k_0\) and \(k_1+k_0+4(n-2)k_q+(n-2)(n-3)k_0\), with off-diagonal magnitude \(2\sqrt{n-1}|k_h+(n-2)k_0/2|\). This block also has determinant zero; its trace is \(\lambda_{\mathrm{triv}}\). This accounts for all \(n^2\) eigenvalues, proving (2). Simple factorizations of the six pairwise eigenvalue differences give the stated collision list; for example \(\lambda_{\mathrm{std}}-\lambda_{\mathrm{odd}}=c(n+2)(n-8)^2/8\), and \(\lambda_{\mathrm{pair}}-\lambda_{\mathrm{odd}}=c(n+2)(20-n)/4\).

**4. Sharp conditioning.** The four branches show that the smallest positive eigenvalue is \(\lambda_{\mathrm{odd}}\) for \(3\le n\le20\), with a tie at \(n=20\), and \(\lambda_{\mathrm{pair}}\) thereafter. The largest is \(\lambda_{\mathrm{std}}\) at \(n=3\), \(\lambda_{\mathrm{pair}}\) at \(n=4,5\), and \(\lambda_{\mathrm{triv}}\) at all \(n\ge6\). Direct calculation at \(n=3,4,5,6\) gives \(\kappa_n=33/8,3,9/4,15/8\), respectively. For \(7\le n\le20\),
\[
\kappa_n=\frac{(n+4)(n^2-4n+12)}{4(n^2-4)},
\]
whose derivative has numerator \(n^4-8n^2-96n+16>0\) for \(n\ge7\). For \(n\ge20\),
\[
\kappa_n=\frac{n^2-4n+12}{3(n+2)},
\]
whose derivative has numerator \(n^2+4n-20>0\). Therefore the unique minimum occurs at \(n=6\), establishing (3).

## Verification
Run `python check_bn4.py` with SymPy and NumPy installed. The checker verifies the exact symbolic factorizations and both rank-one determinant identities, independently constructs the rational Gram entries for each \(3\le n\le13\), checks exact first and second spectral moments, and compares every eigenvalue numerically. It also tests the reconstruction and Laplacian relations over rational samples in dimensions \(3\le n\le15\) and tests the conditioning comparison in dimensions up to 1000, in addition to symbolic derivative factorizations. These finite checks corroborate, but are not substituted for, the unrestricted algebraic proof above.

## Relationship to prior work
The spherical-harmonic addition formula, dimension identity and Gegenbauer reproducing kernel are classical and are explained in Dai and Xu (2013), especially their sections 1–3. Dunkl (2002) develops invariant spherical harmonics and Gram determinants for the signed-permutation symmetry group, but its Gram matrix concerns a polynomial basis in an invariant inner product rather than sample evaluation on the union of short and long roots. The foundational spherical-code/design framework of Delsarte–Goethals–Seidel (1977) is relevant to these highly symmetric configurations. The present assertions specify the full fourth-degree *sampling* image, rank, all four Gram branches, resonance dimensions, constructive interpolation and sharp conditioning within this root-system family; these are not stated in the inspected full texts of Dai–Xu or Dunkl.

## Limitations
The result fixes a single harmonic degree, root-orbit union and unweighted antipodal-representative sample norm. Other degrees, arbitrary node weights, and erasure patterns are not classified. The claim is not that the general addition formula or harmonic projection machinery is new. The 1977 foundational design paper was located, but its full text was not successfully retrieved; an implicit equivalent in early association-scheme or root-system literature remains a real novelty risk. Independent scholarly assessment has not been performed.

## References
1. C. F. Dunkl, *Symmetric Functions and \(B_N\)-invariant Spherical Harmonics*, arXiv:math/0207122v1, publicly dated 2002-07-15, https://arxiv.org/abs/math/0207122 .
2. F. Dai and Y. Xu, *Spherical Harmonics*, arXiv:1304.2585v1, publicly dated 2013-04-09, https://arxiv.org/abs/1304.2585 .
3. P. Delsarte, J. M. Goethals and J. J. Seidel, *Spherical Codes and Designs*, Geometriae Dedicata 6 (1977), 363–388, DOI 10.1007/BF03187604 (full text unavailable during this comparison).
