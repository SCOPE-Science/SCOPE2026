# Finite exact randomized-time mixing on every odd prime quantum cycle

## Finding

**Theorem.** Let \(p\geq3\) be any odd prime, let \(A\) be the unweighted adjacency matrix of the cycle \(C_p\), and put \(U(t)=\exp(\mathrm{i}tA)\). For every real threshold \(T>0\), there exist an integer \(s\), pairwise distinct real times \(t_1,\ldots,t_s>T\), and positive weights \(w_1,\ldots,w_s\) such that

\[
1\leq s\leq\frac{p+1}{2},\qquad \sum_{\ell=1}^s w_\ell=1,
\]

and the entire averaged transition-probability matrix is exactly uniform:

\[
\boxed{\sum_{\ell=1}^s w_\ell\,|U(t_\ell)_{ab}|^2=\frac1p
\quad\text{for all vertices }a,b\in\mathbb Z/p\mathbb Z.}
\]

The same observation-time distribution works for every initial vertex. For primes \(p\geq5\), a published theorem excludes uniform mixing at any one time; the present theorem shows that exact uniformity is nevertheless attainable by a finite weighted choice of observation times.

## Assumptions and scope

The graph is a simple unweighted cycle of odd prime order and the Hamiltonian is its adjacency matrix. Observation times are strictly positive and can all be placed later than any prescribed finite \(T\). Randomization is classical and selects one observation time; the quantum evolution itself is unitary without intermediate measurements. The time law is common to all starting vertices. There is no claim about composite cycle orders, equally weighted sampling, fixed time grids, effective sizes of the times, or optimality of the number of atoms.

## Proof

**1. Fourier representation.** Set \(m=(p-1)/2\), \(\zeta=\exp(2\pi\mathrm{i}/p)\) and

\[
\lambda_0=2,\qquad \lambda_j=\zeta^j+\zeta^{-j}=2\cos(2\pi j/p)
\quad(1\leq j\leq m).
\]

For each graph distance \(0\leq d\leq m\) define real coefficients

\[
b_0(d)=1,\qquad b_j(d)=\zeta^{jd}+\zeta^{-jd}=2\cos(2\pi jd/p).
\]

For a phase tuple \(z=(z_0,\ldots,z_m)\), with \(z_0=1\) and \(|z_j|=1\), set

\[
F_d(z)=\frac1{p^2}\left|\sum_{j=0}^{m} b_j(d)z_j\right|^2,
\qquad F(z)=(F_0(z),\ldots,F_m(z)).
\]

Fourier inversion gives the transition probability at distance \(d\) as \(F_d(z(t))\), with \(z_j(t)=\exp(\mathrm{i}t(\lambda_j-2))\). Translation and reflection symmetry ensure that these coordinates give every entry of the mixing matrix. For every phase tuple, the associated spectral sum is a unitary circulant matrix, so

\[
F_0(z)+2\sum_{d=1}^{m}F_d(z)=1.
\tag{1}
\]

The sums \(S_d=\sum_{j=0}^{m}b_j(d)\) and \(Q_d=\sum_{j=0}^{m}b_j(d)^2\) obey

\[
S_0=p,\quad Q_0=2p-1;\qquad
S_d=0,\quad Q_d=p-1\quad(1\leq d\leq m).
\tag{2}
\]

The first identities sum the \(p\)-th roots of unity. For \(d\ne0\), the square expansion gives \(Q_d=1+(p-1)+\sum_{k=1}^{p-1}\zeta^{2kd}=p-1\), because multiplication by \(2d\) permutes nonzero residues modulo prime \(p\).

**2. An exactly uniform torus barycenter.** Let \(H\) be the law with \(z_0=1\) and the other \(m\) phases independent Haar-uniform on the unit circle. Off-diagonal correlations under \(H\) vanish. Define a second law \(P\) by putting \(N=m+1\), \(\eta=\exp(2\pi\mathrm{i}/N)\), choosing a uniformly random permutation \(\sigma\) of \(\{0,\ldots,m\}\), and setting

\[
z_j=\eta^{\sigma(j)-\sigma(0)}.
\]

Here \(z_0=1\), and sampling without replacement from all \(N\)-th roots, whose sum is zero, gives \(\mathbb E_P[z_j\overline{z_k}]=-1/m\) whenever \(j\ne k\). Under the mixture \(\mu=\tfrac12H+\tfrac12P\), all off-diagonal correlations equal

\[
c=-\frac1{2m}=-\frac1{p-1},
\]

while diagonal correlations equal one. Consequently

\[
\mathbb E_\mu F_d=\frac{(1-c)Q_d+cS_d^2}{p^2}=\frac1p
\quad(0\leq d\leq m),
\tag{3}
\]

by (2). This is an **exact average on the abstract spectral phase torus**, not yet an assertion about physical observation times.

**3. Physical phases are dense.** The real numbers \(\omega_j=\lambda_j-2\) for \(1\leq j\leq m\) are linearly independent over \(\mathbb Q\). Indeed, if \(\sum_j a_j\omega_j=0\) for rational coefficients and \(a=\sum_j a_j\), then

\[
R(X)=\sum_{j=1}^m a_j(X^j+X^{p-j})-2a
\]

vanishes at the primitive \(p\)-th root \(\zeta\). As \(\deg R\leq p-1\), irreducibility of \(\Phi_p(X)=1+X+\cdots+X^{p-1}\) implies \(R=c\Phi_p\) for some rational \(c\). Comparison of the nonconstant coefficients gives \(a_j=c\) for all \(j\), while comparison of constant terms gives \(-2mc=c\), hence \(pc=0\) and all coefficients vanish. The continuous-time Kronecker density theorem therefore makes the positive-time tail

\[
\{(z_1(t),\ldots,z_m(t)):t>T\}
\]

 dense in \((S^1)^m\) for every \(T\). No assumption of integer observation times is being made.

**4. Finite physical support.** Write \(K=F((S^1)^m)\) and \(C=\operatorname{conv}K\), contained in the affine hyperplane (1). The Haar barycenter \(h=\mathbb E_HF\) lies in the **relative interior** of \(C\). Otherwise a proper supporting affine functional attaining its minimum at \(h\) would have a continuous nonnegative difference with zero integral against the full-support Haar law. That difference would vanish everywhere on \(K\), making the supporting functional constant on \(C\), a contradiction. The permutation barycenter \(v=\mathbb E_PF\) lies in \(C\), so by (3) the uniform vector \(u=(h+v)/2\) also belongs to \(\operatorname{ri}C\).

Use the finite-dimensional **convex-density lemma**: if \(D\) is dense in a compact \(K\) in an affine Euclidean space, then \(\operatorname{ri}(\operatorname{conv}K)\subseteq\operatorname{conv}D\). To prove it, place a small full-dimensional simplex inside \(\operatorname{conv}K\) with the desired interior point inside it. Express its vertices as finite convex combinations of points of \(K\), approximate those points by points of \(D\), and observe that the interior point stays within the perturbed simplex. Each perturbed vertex belongs to \(\operatorname{conv}D\).

Apply this lemma with \(D=\{F(z(t)):t>T\}\), which is dense in \(K\) by step 3. Thus \(u\) is an **exact finite convex combination of actual mixing vectors** sampled at times \(t>T\). Carathéodory's theorem in the affine hyperplane (1), of dimension at most \(m\), reduces the support to at most \(m+1=(p+1)/2\) times. Discard zero weights and merge repeated times to make the weights positive and times pairwise distinct. Fourier symmetry in step 1 lifts equality for each distance to every pair of vertices. This proves the theorem.

## Verification

The bundled `verify.py` and `examples.json` can be placed in the same folder and run with `python3 verify.py`. The checker tests 592 exact rational barycentric identities at odd primes through \(101\), enumerates 752 phase permutations at the smallest odd prime orders, and independently evaluates 20 Fourier-displacement probabilities using positive-time approximate examples for orders \(5,7,11,13\). The numerical examples are floating-point approximations, **not exact existence certificates**; the unrestricted theorem rests on the complete analytic proof.

## Relationship to prior work

Baptista, Coutinho and Marques [1] introduced arbitrary time-sampling distributions for average mixing, with examples for paths, complete graphs and complete bipartite graphs. Their inspected primary preprint does not establish finite exact uniform sampling for every odd prime cycle.

Godsil, Mullin and Roy [2] prove that cycles of prime order at least \(5\) cannot mix uniformly at a **single time**, although they admit arbitrarily good **approximate** single-time mixing. Approximation alone does not imply that the uniform matrix belongs to the actual finite convex hull of the mixing curve. The root-permutation correlation law and relative-interior step establish that stronger inclusion and the support bound.

Adamczak and coauthors [3] prove that the **standard Cesàro time average** on Abelian circulants is not uniform. That prescribed limiting average differs from an optimally chosen nonuniform finite probability measure on observation times; the statements are compatible.

## Limitations

The proof is nonconstructive about exact times and weights, and provides no effective upper bound on time magnitudes or their conditioning. The support bound is not claimed optimal. No composite-order classification or equal-weight/integer-time assertion is made. Floating-point examples are corroborative only. A differently indexed general convex-reachability theorem might cover the statement, despite the source and equivalence comparisons performed.

## References

[1] P. Baptista, G. Coutinho, V. Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378v1 (2023), https://arxiv.org/html/2308.16378v1 . DOI: 10.48550/arXiv.2308.16378.

[2] C. Godsil, N. Mullin, A. Roy, *Uniform Mixing and Association Schemes*, Electronic Journal of Combinatorics 24(3), P3.22 (2017); arXiv:1301.5889v2, https://arxiv.org/pdf/1301.5889 . DOI: 10.37236/4745.

[3] W. Adamczak, K. Andrew, L. Bergen, D. Ethier, P. Hernberg, J. Lin, C. Tamon, *Non-uniform mixing of quantum walk on cycles*, International Journal of Quantum Information 5(6), 781–793 (2007); arXiv:0708.2096v1, https://arxiv.org/pdf/0708.2096 .
