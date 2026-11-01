# The unique worst-conditioned exact-degree harmonic sampler on the icosidodecahedron

## Finding

The thirty unit vertices of the regular icosidodecahedron form fifteen antipodal pairs. Choose one point \(x_i\) from each pair. Write \(P_k\) for the standard Legendre polynomial with \(P_k(1)=1\), and define the positive-semidefinite sampling Gram matrix
\[
K_k=(P_k(x_i\mathbin{\cdot}x_j))_{1\le i,j\le15}.
\]
For every integer degree \(k\) for which this matrix is positive definite, its Euclidean spectral condition number satisfies
\[
\kappa_2(K_k)\le\frac{2702133/1048576}{\frac12\bigl(793/512-\sqrt{(793/512)^2-4(37828791/8589934592)}\bigr)}=904.644497713258\ldots.
\]
**Equality holds exactly at degree \(k=12\)**. Every other positive-definite degree has \(\kappa_2(K_k)<875\). These statements refer to the normalized parity-compatible \(15\times15\) Gram matrix, not a singular \(30\times30\) matrix. The full Gram matrix on all thirty vertices has twice these nonzero eigenvalues.

At degree twelve the exact spectrum, with multiplicities, is
\[
\left(\frac{2702133}{1048576}\right)^{[1]},\quad
\left(\frac{4906187}{4194304}\right)^{[4]},\quad
\left(\frac{793/512-\sqrt{(793/512)^2-4(37828791/8589934592)}}{2}\right)^{[5]},\quad
\left(\frac{793/512+\sqrt{(793/512)^2-4(37828791/8589934592)}}{2}\right)^{[5]}.
\]
The notation \(\lambda^{[m]}\) means that \(\lambda\) occurs with multiplicity \(m\).

## Assumptions and scope

The standard Cartesian model for the thirty unit vertices consists of the six signed coordinate axes and the twenty-four vectors formed by independent coordinate signs and cyclic permutations of
\[
\frac12\left(\varphi,\varphi^{-1},1\right),\qquad \varphi=\frac{1+\sqrt5}{2}.
\]
Changing the antipodal representatives replaces \(K_k\) by a diagonal-sign conjugate when \(k\) is odd and leaves its spectrum unchanged when \(k\) is even. Thus the conditioning is well-defined independently of the representatives. Positive definiteness occurs exactly for \(k\in\{7,9,10,11,12,13\}\cup\{k\in\mathbb Z:k\ge15\}\). The known rank classification is used as background only; it is **not** the originality claim here.

## Proof

**1. Exact dot-product algebra.** Set \(a=(\sqrt5-1)/4\), \(c=(\sqrt5+1)/4\). For any representative \(x_i\), the remaining fourteen representatives have two zero dot products and exactly four dot products of each absolute value \(a\), \(1/2\), and \(c\). The zero-dot-product graph is a disjoint union of five triangles. Write \(N_0\) for its adjacency matrix. Then \(Q=(I+N_0)/3\) is an orthogonal projection of rank five, and \(I-Q\) has rank ten.

**2. Sharp degree-twelve spectral identity.** Evaluate \(P_{12}\) at \(0\), \(\pm a\), \(\pm1/2\), \(\pm c\) using the Legendre three-term recurrence over \(\mathbb Q(\sqrt5)\). Direct exact matrix multiplication gives
\[
K_{12}Q=\frac{4906187}{4194304}Q+\left(\frac{2702133}{1048576}-\frac{4906187}{4194304}\right)\frac{J}{15},
\]
where \(J\) is the all-ones matrix, and also
\[
(K_{12}^2-\tfrac{793}{512}K_{12}+\tfrac{37828791}{8589934592}I)(I-Q)=0.
\]
The first identity gives one constant-vector eigenvalue \(L=2702133/1048576\) and four eigenvalues \(4906187/4194304\); the second gives the remaining pair \(\lambda_\pm\) with multiplicity five each, by trace and the nonzero discriminant. Exact rational brackets show \(L>51/20\) and \(0.0028<\lambda_-<0.0029\). In particular the maximum degree-twelve condition number exceeds \((51/20)/0.0029>875\).

**3. Other degrees below the tail.** Let \(q=2^{48}\). For each \(k\in\{7,9,10,11,13\}\cup\{15,\ldots,499\}\), the standalone certificate computes an integer matrix \(M_k\) satisfying the entrywise bound \(\lVert K_k-M_k/q\rVert_{\max}<2/q\). This is rigorous because all Legendre evaluations are computed in \(\mathbb Q(\sqrt5)\) using the exact recurrence; an integer square-root enclosure of \(\sqrt5\) with width \(2^{-70}\) gives verified outward dyadic intervals. For every such \(k\), fraction-free integer Sylvester elimination proves that both matrices \(200M_k-qI\) and \(3qI-M_k\) are positive definite (all fifteen leading principal minors strictly positive). By the symmetric matrix perturbation bound, \(\lVert K_k-M_k/q\rVert_2<30/q\), so \(\lambda_{\min}(K_k)>1/250\) and \(\lambda_{\max}(K_k)<7/2\). Consequently \(\kappa_2(K_k)<875\). The certificate exhausts precisely the \(485\) degrees from fifteen through 499, in addition to the five other low full-rank degrees; no numerical floating-point spectral tests are involved.

**4. Every degree from 500 onward.** The Laplace integral
\[
P_k(t)=\frac1\pi\int_0^\pi\bigl(t+i\sqrt{1-t^2}\cos\theta\bigr)^k\,d\theta
\]
shows, using \(1-u\le e^{-u}\) and \(\sin\theta\ge2\theta/\pi\) on the first quadrant, that for every integer \(k\ge1\) and \(-1<t<1\),
\[
|P_k(t)|\le\sqrt{\frac{\pi}{2k(1-t^2)}}.
\]
The fourteen off-diagonal entries in any row have absolute dot products \(0\) (twice) and \(a\), \(1/2\), \(c\) (four times each), hence their absolute sum is at most
\[
\sqrt{\frac{\pi}{2k}}\left(2+4\left[\frac1{\sqrt{1-a^2}}+\frac2{\sqrt3}+\frac1{\sqrt{1-c^2}}\right]\right).
\]
Exact rational squares give \(1/\sqrt{1-a^2}<263/250\), \(2/\sqrt3<231/200\), and \(1/\sqrt{1-c^2}<851/500\), making the parenthesis less than \(4409/250\). With \(\pi<22/7\) and \(k\ge500\), its product with the preceding square-root factor is strictly below \(99/100\). Gershgorin then places every eigenvalue of \(K_k\) between \(1/100\) and \(199/100\); thus \(\kappa_2(K_k)<199<875\). Combined with steps 2–3, degree twelve is the **unique** sharp conditioning extremizer over every nonsingular degree.

## Verification

Run `python3 h3_cert.py` using only the Python standard library. The program constructs all thirty vectors in exact \(\mathbb Q(\sqrt5)\) arithmetic, checks antipodes, dot-product multiplicities and the five orthogonal triples, computes the exact degree-twelve spectral identities, verifies the rational spectral brackets, and provides a reproducible integer Sylvester certificate for every degree from fifteen to 499 and for the five other low full-rank degrees. It also checks all rational constants in the analytic tail. Successful termination prints `H3_ALL_DEGREE_CERTIFICATE_OK`. These computations certify the finite section; the independent integral bound in the proof covers all infinitely many remaining degrees.

## Relationship to prior work

The icosidodecahedral configuration and its coordinates appear in work on icosahedral cluster packings; the harmonic-index-design framework defines exact-degree Legendre kernels. General numerical conditioning techniques for spherical sampling and Gram-matrix optimization are related but address other sampling sets or optimized, rather than fixed, node configurations. Previously established exact-degree **rank** data for this thirty-point orbit do not determine the sharp degree-uniform positive spectral condition number, so the rank data are not claimed as new here.

## Limitations

The result is restricted to the thirty unit vertices, exact-degree (not cumulative-degree) Legendre kernels, one representative from each antipodal pair, and the spectral condition number in nonsingular degrees. It does not optimize point locations, resolve noise models, or claim conditioning bounds for other root configurations. The nonstandard finite positivity step has a standalone exact certificate; an independent proof audit has not been performed. Historical equivalents in older icosahedral representation theory or numerical cubature are possible and warrant expert comparison, particularly the 1958 icosahedral harmonics literature, whose entire article was not accessible for this comparison.

## References

- N. Cotfas, *Algorithm for generating quasiperiodic packings of icosahedral three-shell clusters* (2005), arXiv:math-ph/0504044, version 1 dated 2005-04-14; full open preprint inspected: https://arxiv.org/html/math-ph/0504044v1.
- E. Bannai, T. Okuda, M. Tagami, *Spherical designs of harmonic index t* (2013), arXiv:1308.5101, version 1 dated 2013-08-23; full open preprint inspected: https://arxiv.org/html/1308.5101v1.
- Z. Khalid, R. A. Kennedy, J. D. McEwen, *An optimal-dimensionality sampling scheme on the sphere with fast spherical harmonic transforms* (2014), arXiv:1403.4661, open full text examined: https://ar5iv.labs.arxiv.org/html/1403.4661.
- Chen, Womersley, and Ye, *Minimizing the Condition Number of a Gram Matrix*, SIAM J. Optim. (2011), doi:10.1137/100786022; accessible abstract examined, not full text.
- N. V. Cohan, *The spherical harmonics with the symmetry of the icosahedral group* (1958), doi:10.1017/S0305004100033156; publisher abstract/extract examined, full text inaccessible.
