# A loss-only exceptional-point cusp and its complete-bipartite obstruction

## Finding
Let \(a,b,\gamma>0\) and consider the passive three-mode Hamiltonian
\[
H(a,b,\gamma)=\begin{pmatrix}-i\gamma&a&0\\a&0&b\\0&b&0\end{pmatrix}.
\]
An *exceptional point of order* \(k\) means an eigenvalue of algebraic multiplicity \(k\) whose eigenspace has dimension one. For fixed \(a,b\), **positive loss strengths with an exceptional point exist exactly when \(a^2\ge 8b^2\)**. Their full classification is:

1. If \(a^2<8b^2\), the spectrum is simple for every \(\gamma>0\).
2. If \(a^2=8b^2\), there is a unique exceptional point at \(\gamma=3\sqrt3\,b\), of order three, with sole eigenvalue \(-i\sqrt3\,b\).
3. If \(a^2>8b^2\), there are precisely two distinct exceptional points, each of order two, at the strictly positive rates
\[
\gamma_{\pm}^{2}=
\frac{a^{4}+20a^{2}b^{2}-8b^{4}\ \pm\ a(a^{2}-8b^{2})^{3/2}}{8b^{2}},\qquad \gamma_-<\gamma_+.
\]
All three eigenvalues lie on the negative imaginary axis for \(\gamma\in[\gamma_-,\gamma_+]\); outside this interval exactly one eigenvalue lies on that axis and the other two have nonzero, opposite real parts. In case 1 the latter pattern holds at every positive loss strength. At the isolated order-three point in case 2 all eigenvalues coincide on the negative imaginary axis.

For an unweighted complete bipartite graph \(K_{m,n}\), with \(m,n\ge1\), let \(A\) be its adjacency matrix and put one loss \(-i\gamma\) at a vertex \(v\). Then \(A-i\gamma|v\rangle\langle v|\) is diagonalizable for every \(\gamma>0\), **unless** \(v\) belongs to a singleton bipartition class. In that exceptional case the only exceptional-point strength is \(\gamma=2\sqrt{d(v)}\), and the exceptional point has order two. Here \(d(v)\) denotes the degree, and the statement includes \(K_{1,1}\).

## Assumptions and scope
The hopping amplitudes \(a,b\) are strictly positive real numbers, the loss is localized at the first endpoint, and the other two diagonal potentials vanish. For the graph corollary, all cross-edges have unit hopping and there is exactly one lossy vertex. The generator is the finite non-Hermitian Hamiltonian, not a trace-preserving master equation. The adjective *passive* means that no site has gain. The spectral classification is for every real \(\gamma>0\); no large-size limit or nonlinear effects are assumed.

## Proof
Direct determinant expansion gives
\[
p(z)=\det(zI-H)=z^3+i\gamma z^2-(a^2+b^2)z-i\gamma b^2.
\]
Its discriminant is the *real* quantity
\[
\Delta=4b^2\gamma^4+(8b^4-20a^2b^2-a^4)\gamma^2+4(a^2+b^2)^3.
\]
Put \(A_0=a^2\), \(B_0=b^2\), and \(X=\gamma^2\). Regarding \(\Delta\) as a quadratic polynomial in \(X\), its own discriminant is exactly
\[
A_0(A_0-8B_0)^3.
\]
The quadratic has positive leading coefficient and strictly positive constant coefficient. If \(A_0<8B_0\), its discriminant is negative and consequently \(\Delta>0\) for every real \(X\). If \(A_0=8B_0\), direct factorization yields \(\Delta=4b^2(\gamma^2-27b^2)^2\). If \(A_0>8B_0\), the two quadratic roots are the displayed values \(\gamma_\pm^2\). Both roots are positive: their product is positive and their sum, \((a^4+20a^2b^2-8b^4)/(4b^2)\), is positive. The signs of \(\Delta\) therefore alternate: positive, negative, positive as \(\gamma\) crosses \(\gamma_-\) and \(\gamma_+\).

Write \(z=-it\). The spectral equation \(p(-it)=0\) becomes the real cubic
\[
f(t)=t^3-\gamma t^2+(a^2+b^2)t-\gamma b^2=0.
\]
The cubic discriminant of \(f\) is \(-\Delta\); hence \(\Delta<0\) means three distinct real \(t\)'s and thus three distinct imaginary eigenvalues, whereas \(\Delta>0\) means exactly one real \(t\) and a nonreal conjugate pair. Every eigenvalue has *strictly negative* imaginary part: if \(Hv=zv\), then
\[
\operatorname{Im}z=-\gamma\frac{|v_1|^2}{\|v\|^2}<0,
\]
because \(v_1=0\) forces \(v_2=v_3=0\) successively by the first and second eigenvector equations. Thus all imaginary roots described above lie on the negative axis. For a nonimaginary eigenvalue, the real cubic pairing implies the other nonimaginary eigenvalue has opposite real part.

A finite irreducible tridiagonal matrix has geometric multiplicity one at **each** eigenvalue: the first-row eigenvector equation determines the second coordinate from the first, and the second determines the third; a nonzero eigenvector cannot have zero first coordinate. Thus a double discriminant root corresponds to a size-two Jordan block. At \(a=2\sqrt2\,b\) and \(\gamma=3\sqrt3\,b\), the polynomial factors as
\[
p(z)=(z+i\sqrt3\,b)^3.
\]
The eigenspace is still one-dimensional, proving an order-three exceptional point rather than an ordinary triple degeneracy. This proves the complete trimer classification.

For the graph corollary, suppose \(v\) lies in the bipartition class of size \(m\). If \(m\ge2\), the three-dimensional subspace spanned by the lossy-site vector, the normalized uniform vector on the other \(m-1\) same-class vertices, and the normalized uniform vector on the opposite \(n\) vertices is invariant. In that orthonormal basis the restricted Hamiltonian is \(H(\sqrt n,\sqrt{n(m-1)},\gamma)\). Its coupling ratio is \(a^2/b^2=1/(m-1)\le1<8\), so the restricted spectrum is simple for every \(\gamma>0\). Its determinant is \(i\gamma n(m-1)\ne0\) (up to an irrelevant sign convention for \(\det H\)), so none of these eigenvalues is zero. The orthogonal complement is a zero-eigenspace of dimension \(m+n-3\), and no Jordan block connects it to the invariant three-dimensional block. The full operator is therefore diagonalizable.

If \(m=1\), the lossy vertex is the unique vertex in its class; the active subspace has basis given by \(v\) and the normalized uniform opposite-class vector. Its matrix is
\[
\begin{pmatrix}-i\gamma&\sqrt n\\\sqrt n&0\end{pmatrix},
\]
whose two eigenvalues coalesce at exactly \(\gamma=2\sqrt n\). The remaining \(n-1\) dark eigenvectors have zero eigenvalue, which cannot collide with that nonzero exceptional eigenvalue. This also covers the two-vertex graph, proving the graph classification.

## Verification
The standalone checker `checks/verify.py` symbolically reconstructs the characteristic polynomial, both discriminants, the cubic exceptional-point factorization, and the Jordan rank. It checks the two positive squared thresholds at \((a,b)=(3,1)\), the sign change of the discriminant, the bipartite reduction for finite parameters, and the star-center dimer discriminant. Run with `python checks/verify.py` after installing SymPy. Its executable assertions passed in the preparation of this result. The proof above, not the finite parameter tests, establishes all universal quantifiers.

## Relationship to prior work
Joglekar, Scott, Babbey, and Saxena (2010) studied imaginary-impurity exceptional-point transitions in gain–loss tight-binding chains; the impurity pattern differs here. Ornigotti and Szameit (2014) investigated passive photonic couplers. Joglekar and Harter (2018), especially their section IV and equation (7), treated an endpoint-loss **equal-coupling** trimer, noting no exceptional point at zero real detuning. Its equal-coupling case corresponds to \(a^2/b^2=1<8\), consistent with the first branch above. The present claim adds the exact unequal-coupling cusp, its order-three collision, the intervening all-imaginary spectral interval, and a structural obstruction for one-loss complete bipartite graphs. Downing and Saroka (2021) study different balanced gain–loss oligomers and do not directly imply the loss-only diagram. The original published and indexed literature on more general non-Hermitian graph reductions could contain equivalent specializations; no exhaustive priority theorem is claimed.

## Limitations
No claim is made for diagonal detunings, nonuniform complete-bipartite edge weights, simultaneous losses, Lindblad spectra, scattering matrices, or passive-transition definitions based on transmission rather than eigenvalue coalescence. The result follows from a cubic discriminant and symmetry reduction; similar algebra could exist under alternate notation. The 2018 extended-star quantum-trap paper of Yalouz and Pouthier was not accessible in complete text during comparison, leaving a limited but genuine priority risk for the graph corollary. The graph result is not a characterization for arbitrary graphs.

## References
- Y. N. Joglekar, D. Scott, M. Babbey, and A. Saxena, *Robust and fragile PT-symmetric phases in a tight-binding chain* (2010), arXiv:1008.2968, first publicly submitted 2010-08-17. https://arxiv.org/abs/1008.2968
- M. Ornigotti and A. Szameit, *Quasi PT-symmetry in passive photonic lattices* (2014), arXiv:1401.2299. https://arxiv.org/abs/1401.2299
- Y. N. Joglekar and A. K. Harter, *Passive PT-symmetry breaking transitions without exceptional points in dissipative photonic systems* (2018), arXiv:1807.10330, particularly Section IV. https://arxiv.org/abs/1807.10330
- C. A. Downing and V. A. Saroka, *Exceptional points in oligomer chains* (2021), Communications Physics 4, DOI:10.1038/s42005-021-00757-3. https://doi.org/10.1038/s42005-021-00757-3
- S. Yalouz and D. Pouthier, *Continuous-time quantum walk on an extended star graph: Trapping and superradiance transition* (2018), Physical Review E 97, 022304, DOI:10.1103/PhysRevE.97.022304. Full text not available for the present comparison.
- *Spectral Distribution of Exceptional Points in Lattices with Localized Loss* (2026), arXiv:2601.09628, a uniform-hopping localized-loss chain comparison. https://arxiv.org/abs/2601.09628
