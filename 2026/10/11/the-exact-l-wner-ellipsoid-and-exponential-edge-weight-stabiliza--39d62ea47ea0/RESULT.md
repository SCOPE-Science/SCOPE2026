# The exact Löwner ellipsoid and exponential edge-weight stabilization for wheel symmetric edge polytopes

## Finding
For each integer \(m\ge3\), let \(W_m=K_1*C_m\) be the wheel graph, with hub \(0\) and cyclic rim vertices \(1,\ldots,m\). In the zero-sum Euclidean subspace \(H_m\subset\mathbb R^{m+1}\), define the symmetric edge polytope
\[
P_m=\operatorname{conv}\{\pm(e_i-e_j):\{i,j\}\in E(W_m)\}.
\]
For \(k=1,\ldots,m-1\), set \(s_k=\sin^2(\pi k/m)\). There is exactly one \(t_m\in[1,2)\) satisfying
\[
\sum_{k=1}^{m-1}\frac{4s_k}{1+4t_m s_k}=\frac{m}{1+t_m}.
\]
Equality \(t_m=1\) occurs only for \(m=3\); otherwise \(1<t_m<2\). Put \(a_m=1/[m(1+t_m)]\), \(b_m=t_m a_m\), and, with cyclic rim indices,
\[
S_m=a_m\sum_{i=1}^m(e_0-e_i)(e_0-e_i)^T+b_m\sum_{i=1}^m(e_i-e_{i+1})(e_i-e_{i+1})^T.
\]
The unique minimum-volume enclosing ellipsoid of \(P_m\) is
\[
E_m=\{x\in H_m:x^T(mS_m|_{H_m})^{-1}x\le1\}.
\]
Its center is the origin, and all \(4m\) signed edge-root vertices lie on its boundary. The squared principal semiaxes are
\[
\frac{m+1}{1+t_m}\quad\text{(multiplicity one)},\qquad
\frac{1+4t_m\sin^2(\pi k/m)}{1+t_m}\quad(k=1,\ldots,m-1).
\]
Let \(\kappa_m=\pi^{m/2}/\Gamma(m/2+1)\). Its exact intrinsic Euclidean volume is
\[
\operatorname{vol}_m(E_m)=\kappa_m\sqrt{\frac{m+1}{(1+t_m)^m}\prod_{k=1}^{m-1}(1+4t_m\sin^2(\pi k/m))}.
\]
The optimizing rim-to-spoke ratio has the exponentially sharp limit
\[
\boxed{\lim_{m\to\infty}2^m(2-t_m)=18.}
\]

## Assumptions and scope
The graph is simple and unweighted, with \(m\ge3\). All volumes, inverses, orthogonal eigenspaces, and determinants are computed in the inherited Euclidean metric on \(H_m\), of dimension \(m\). The vertex roots have Euclidean squared norm \(2\). The ellipsoid convention is \(\{x:(x-c)^TQ^{-1}(x-c)\le1\}\) for a positive-definite shape matrix \(Q\); its volume is \(\kappa_m\sqrt{\det_{H_m}Q}\). The scalar \(t_m\) is characterized by the displayed equation rather than by a closed radical in general.

## Proof
**1. Laplacian determinant and optimization.** A wheel has two edge orbits, each of size \(m\). Assign per-edge masses \(a>0\) on spokes and \(b>0\) on rim edges, with \(m(a+b)=1\). The resulting covariance operator is \(S(a,b)\), the weighted graph Laplacian restricted to \(H_m\). The hub-versus-uniform-rim eigenvalue is \((m+1)a\). The other \(m-1\) eigenvalues are \(a+4b\sin^2(\pi k/m)\), by discrete Fourier diagonalization of the cyclic rim. Thus, with \(t=b/a\),
\[
\det_{H_m}S(a,b)=\frac{m+1}{m^m}\frac{C_m(t)}{(1+t)^m},\qquad
C_m(t)=\prod_{k=1}^{m-1}(1+4t\sin^2(\pi k/m)).
\]
The derivative of the logarithm of the variable part is \(F_m(t)=\sum_k 4s_k/(1+4ts_k)-m/(1+t)\). Strict concavity of \(\log\det S\) along the affine edge-weight parameter \(b\in(0,1/m)\) gives at most one stationary point, and a stationary point is the global maximizer.

**2. A root and its precise location.** Define \(q(t)=(1+2t-\sqrt{1+4t})/(2t)\) for \(t>0\). The finite Poisson-kernel identity (expand the geometric series and sum over roots of unity) gives
\[
\frac1m\sum_{k=0}^{m-1}\frac{1}{1+4t\sin^2(\pi k/m)}
=\frac{1}{\sqrt{1+4t}}\frac{1+q(t)^m}{1-q(t)^m}.
\]
Consequently
\[
\frac{F_m(t)}m= f(t)-\frac{2q(t)^m}{t\sqrt{1+4t}(1-q(t)^m)},\quad
f(t)=\frac{\sqrt{1+4t}-(1+t)}{t(1+t)\sqrt{1+4t}}.
\]
At \(t=1\), \(q(1)=(3-\sqrt5)/2\) and \(q(1)^3=9-4\sqrt5=(\sqrt5-2)/(\sqrt5+2)\). Since \(0<q(1)<1\), substitution proves \(F_m(1)\ge0\), with equality precisely when \(m=3\). At \(t=2\), \(q(2)=1/2\), \(f(2)=0\), and
\[
F_m(2)=-\frac{m}{3(2^m-1)}<0.
\]
Continuity, strict concavity in \(b\), and these endpoint signs prove existence and uniqueness of \(t_m\in[1,2)\); the corresponding masses \(a_m,b_m\) are positive.

**3. Every root is a contact and the ellipsoid is globally optimal.** For any edge root \(v_e=e_i-e_j\), differentiation of \(\log\det_{H_m}S\) with respect to its individual edge mass yields \(R_e=v_e^TS^{-1}v_e\), the graph effective resistance. Dihedral symmetry makes \(R_e\) constant within the spoke orbit and within the rim orbit. Stationarity of the logarithmic determinant under varying \(a+b=1/m\) forces the two constants to coincide. Because
\[
\sum_{e\in E(W_m)}w_eR_e=\operatorname{tr}_{H_m}(S^{-1}S)=m,\qquad\sum_ew_e=1,
\]
each resistance equals \(m\). Therefore every \(\pm v_e\) satisfies \(v_e^T(mS)^{-1}v_e=1\), so \(E_m\) contains \(P_m\) and every one of its \(4m\) vertices is a contact.

Now consider *any* enclosing ellipsoid with center \(c\in H_m\) and shape matrix \(Q\succ0\). For both \(v_e\) and \(-v_e\), the containment inequalities, averaged, give \(v_e^TQ^{-1}v_e+c^TQ^{-1}c\le1\). Averaging further using the positive weights \(w_e\) gives
\[
\operatorname{tr}(Q^{-1}S)+c^TQ^{-1}c\le1.
\]
The arithmetic–geometric mean inequality for the \(m\) eigenvalues of \(Q^{-1/2}SQ^{-1/2}\) gives
\[
\left(\frac{\det S}{\det Q}\right)^{1/m}
\le\frac{\operatorname{tr}(Q^{-1}S)}m\le\frac1m.
\]
Thus \(\det Q\ge m^m\det S\), and equality requires \(c=0\) and \(Q=mS\). This proves global minimum volume and uniqueness, with no symmetry assumption on the competitor.

**4. Exact volume and asymptotics.** Multiplying the eigenvalues of \(mS_m\) yields the displayed exact volume. Equivalently, the product \(C_m(t)\) has the finite closed form \(C_m(t)=\alpha(t)^m+\beta(t)^m-2t^m\), with \(\alpha=(1+2t+\sqrt{1+4t})/2\), \(\beta=(1+2t-\sqrt{1+4t})/2\); this follows by factoring the cycle characteristic polynomial and is also checked symbolically in the accompanying verifier.

On \([1,2]\), \(0<q(t)<1\) is uniformly bounded away from \(1\), so \(F_m(t)/m\) converges uniformly to \(f(t)\). Here \(f(t)>0\) for \(1\le t<2\) and \(f(2)=0\); hence the unique roots converge to \(2\). The same geometric-series expression implies uniform convergence of the derivatives on \([1,2]\), so, using \(f'(2)=-1/54\) and the exact value of \(F_m(2)/m=-1/[3(2^m-1)]\), the mean-value theorem gives
\[
2-t_m\sim\frac{18}{2^m}.
\]
This establishes the stated sharp exponential limit.

## Verification
The accompanying standard-library Python program `verify.py` implements an exact integer-polynomial recurrence for \(C_m(t)\), tests the exact endpoint identities through \(m=80\), checks several algebraic low-order factors, and independently calculates hub-to-rim and rim-to-rim effective resistances using finite-dimensional linear systems for \(3\le m\le20\). It also checks the asymptotic formula numerically. The command `python3 verify.py` completed with `VERIFY_OK`. Exact finite symbolic identities and floating-point matrix tests corroborate, but do not prove, the all-dimension result; the proof is the four-step argument above.

## Relationship to prior work
D’Alì, Delucchi, and Michałek, *Many Faces of Symmetric Edge Polytopes* (arXiv:1910.05193v1, 2019), develop symmetric edge polytopes and treat wheels in their Section 4.3, including facet and lattice invariants. Chen, Davis, and Korchevskaia, *Facets and Facet Subgraphs of Symmetric Edge Polytopes* (arXiv:2107.12315, 2021), study facet descriptions. Those statements do not calculate the wheel's unique Euclidean minimum-volume covering ellipsoid. Suliman and Weinstein, *Infinite Lewis Weights in Spectral Graph Theory* (arXiv:2302.05966v1, 2023), establish general graph-theoretic ellipsoid/optimal-design formulations; that general connection is not claimed here. The result here is the wheel-specific explicit spectral solution and the limiting correction factor \(18\) at exponential scale \(2^{-m}\). A reformulation in graph optimal-design terminology may contain an earlier equivalent calculation.

## Limitations
The theorem concerns wheels \(W_m\) and the inherited Euclidean metric, not arbitrary graph-symmetric-edge polytopes or a different norm. It does not give radicals for \(t_m\) in all dimensions, nor assert monotonicity of \(t_m\) without a proof. The spectrum has repeated numerical eigenvalues at Fourier-conjugate frequencies. Computational checks are finite and cannot establish the theorem independently. Literature checks do not certify absolute novelty or replace independent scientific review.

## References
1. A. D’Alì, E. Delucchi, and M. Michałek, *Many Faces of Symmetric Edge Polytopes*, arXiv:1910.05193v1, first publicly posted October 11, 2019. https://arxiv.org/abs/1910.05193
2. T. Chen, R. Davis, and E. Korchevskaia, *Facets and Facet Subgraphs of Symmetric Edge Polytopes*, arXiv:2107.12315v1, first publicly posted July 26, 2021. https://arxiv.org/abs/2107.12315
3. A. Suliman and O. Weinstein, *Infinite Lewis Weights in Spectral Graph Theory*, arXiv:2302.05966v1, first publicly posted February 12, 2023. https://arxiv.org/abs/2302.05966
