# Sharp elliptical width and complete compression rigidity for four-corner normal matrices

## Finding
For real \(a,b>0\), define the complex normal matrix
\[
D_{a,b}=\operatorname{diag}(a+ib,a-ib,-a+ib,-a-ib)\in M_4(\mathbb C).
\]
Write \(W(B)=\{\langle x,Bx\rangle:\|x\|=1\}\), let \(\delta(W(B))\) be the diameter of a largest closed Euclidean disk contained in \(W(B)\), and set
\[
\delta_2(D_{a,b})=\max_{V\in\mathbb C^{4\times2},\,V^*V=I_2}\delta(W(V^*D_{a,b}V)).
\]
**Theorem (exact value and all maximizers).** Put \(r=\sqrt{a^2+b^2}\), \(\lambda=b/r\), and \(\mu=a/r\). Then
\[
\boxed{\delta_2(D_{a,b})=\frac{2ab}{\sqrt{a^2+b^2}}.}
\]
Every maximizing compression has numerical range **exactly** the closed disk
\[
\boxed{W(V^*D_{a,b}V)=\{z\in\mathbb C:|z|\le ab/r\}.}
\]
Moreover all maximizing two-dimensional subspaces are a single orbit under diagonal unitaries commuting with \(D_{a,b}\). An explicit representative is the range of the \(4\times2\) isometry \(V_0\), with rows indexed by \((s,t)\in\{+1,-1\}^2\) in the diagonal order above,
\[
(v_0)_{s,t}=\frac12\left(\sqrt{1+t\mu},\ \frac{s\lambda}{\sqrt{1+t\mu}}\right).
\]
Precisely, \(\operatorname{ran}V\) attains the maximum if and only if \(\operatorname{ran}V=\operatorname{diag}(\zeta_{+,+},\zeta_{+,-},\zeta_{-,+},\zeta_{-,-})\operatorname{ran}V_0\) for unimodular complex numbers \(\zeta_{s,t}\).

The known positive-block extremal identity of Sababheh also gives, for this family, the exact optimal positive-block norm defect
\[
\Phi(D_{a,b})=
\sup\left\{\left\|\begin{pmatrix}A&D_{a,b}\\D_{a,b}^*&B\end{pmatrix}\right\|-\|A+B\|:
\begin{pmatrix}A&D_{a,b}\\D_{a,b}^*&B\end{pmatrix}\succeq0,\ A=A^*,\ B=B^*\right\}
=\frac{2ab}{r}.
\]
The equality \(\Phi(X)=\delta_2(X)\) is cited prior work; its evaluation for this rectangle is the consequence of the theorem here.

## Assumptions and scope
The scalars \(a,b\) are strictly positive real numbers; thus the four eigenvalues are distinct. The Hilbert space is \(\mathbb C^4\) with its standard Hermitian inner product. Two-dimensional compressions are orthogonal compressions represented by isometries. Positive-block matrices use the ordinary operator norm and the positive-semidefinite ordering. The eigenvalues may be globally translated and rotated without changing \(\delta_2\): for any \(c\in\mathbb C\) and \(|u|=1\), the same value and compression-subspace classification hold for \(cI_4+uD_{a,b}\), with the maximizing disk translated and rotated accordingly. No formula is asserted here for arbitrary quadrilaterals, other normal spectra, or higher compression ranks.

## Proof
**1. Bloch coordinates for arbitrary compressions.** Fix any isometry \(V:\mathbb C^2\to\mathbb C^4\). For \((s,t)\in\{\pm1\}^2\), let \(v_{s,t}\) be its row and let \(E_{s,t}=v_{s,t}^*v_{s,t}\). These are nonnegative Hermitian \(2\times2\) matrices of rank at most one and \(\sum E_{s,t}=I_2\). Let \(\sigma_x,\sigma_y,\sigma_z\) denote the usual Pauli matrices. We can write
\[
E_{s,t}=w_{s,t}(I_2+\mathbf n_{s,t}\cdot\boldsymbol\sigma),\quad
w_{s,t}=\tfrac12\operatorname{tr}E_{s,t}\ge0,\quad
\sum w_{s,t}=1.
\]
For every nonzero effect, \(\mathbf n_{s,t}\in\mathbb R^3\) is a unit vector, because the effect has rank one; at a zero effect choose any unit vector. Thus \(\sum w_{s,t}\mathbf n_{s,t}=0\). Define real vectors
\[
\mathbf h=\sum_{s,t}s w_{s,t}\mathbf n_{s,t},\qquad
\mathbf k=\sum_{s,t}t w_{s,t}\mathbf n_{s,t}.
\]
The compressed matrix is a scalar multiple of the identity plus \((a\mathbf h+ib\mathbf k)\cdot\boldsymbol\sigma\), because \(D_{a,b}\) has entry \(sa+itb\) in row \((s,t)\). The scalar term is \(a\sum s w_{s,t}+ib\sum t w_{s,t}\). For a pure qubit state, the vector of Pauli expectations ranges over the Euclidean unit sphere. Hence the numerical range of the compression is the (possibly degenerate) filled ellipse obtained by applying the real \(2\times3\) map with rows \(a\mathbf h\) and \(b\mathbf k\) to the unit ball, followed by the scalar translation. The image of the sphere equals that of the filled ball because this map has a nontrivial kernel. Its two semiaxis lengths are the singular values of this real map. Write \(\tau\) for its smaller singular value. In particular,
\[
\delta(W(V^*D_{a,b}V))=2\tau.
\]

**2. Universal upper bound.** The four effects and their marginals satisfy the elementary compatibility inequalities
\[
\|\mathbf h+\mathbf k\|
=2\|w_{+,+}\mathbf n_{+,+}-w_{-,-}\mathbf n_{-,-}\|
\le2(w_{+,+}+w_{-,-}),
\]
\[
\|\mathbf h-\mathbf k\|
=2\|w_{+,-}\mathbf n_{+,-}-w_{-,+}\mathbf n_{-,+}\|
\le2(w_{+,-}+w_{-,+}).
\]
Consequently \(\|\mathbf h+\mathbf k\|+\|\mathbf h-\mathbf k\|\le2\). With
\[
G=\begin{pmatrix}\|\mathbf h\|^2&\mathbf h\cdot\mathbf k\\
\mathbf h\cdot\mathbf k&\|\mathbf k\|^2\end{pmatrix},
\]
the definition of \(\tau\) says \(\operatorname{diag}(a,b)G\operatorname{diag}(a,b)\succeq\tau^2I_2\), or equivalently \(G\succeq\tau^2\operatorname{diag}(a^{-2},b^{-2})\). Applying this inequality to \((1,1)\) and \((1,-1)\) gives \(\|\mathbf h\pm\mathbf k\|\ge\tau\sqrt{a^{-2}+b^{-2}}\). Thus
\[
2\ge\|\mathbf h+\mathbf k\|+\|\mathbf h-\mathbf k\|
\ge2\tau\sqrt{a^{-2}+b^{-2}},
\]
so \(\tau\le ab/r\), giving \(\delta_2(D_{a,b})\le2ab/r\).

**3. An attaining isometry.** Define four effects by
\[
E^0_{s,t}=\frac14(I_2+s\lambda\sigma_x+t\mu\sigma_z).
\]
Because \(\lambda^2+\mu^2=1\), every \(E^0_{s,t}\) is positive and rank one; their sum is \(I_2\). The displayed rows of \(V_0\) factor these effects as \((v_0)^*_{s,t}(v_0)_{s,t}=E^0_{s,t}\), and therefore \(V_0^*V_0=I_2\). Directly,
\[
V_0^*D_{a,b}V_0=\frac{ab}{r}(\sigma_x+i\sigma_z)
=\frac{ab}{r}\begin{pmatrix}i&1\\1&-i\end{pmatrix}.
\]
The last matrix has trace zero and square zero, so it is unitarily similar to a nilpotent Jordan block with off-diagonal entry \(2ab/r\). The numerical range of this Jordan block is the closed disk centered at zero of radius \(ab/r\). This attains the upper bound.

**4. Classification of every maximizing compression.** Suppose \(\tau=ab/r>0\). The two bounds in part 2 are equalities. Write \(D=G-\tau^2\operatorname{diag}(a^{-2},b^{-2})\succeq0\). Equality in the two quadratic lower bounds implies \((1,\pm1)D(1,\pm1)^\top=0\). Since \(D\) is positive semidefinite and the two vectors span \(\mathbb R^2\), we obtain \(D=0\). Consequently
\[
\mathbf h\perp\mathbf k,\qquad \|\mathbf h\|=\lambda,\quad
\|\mathbf k\|=\mu,\quad
\|\mathbf h+\mathbf k\|=\|\mathbf h-\mathbf k\|=1.
\]
Equality in the two triangle inequalities forces, whenever the associated weights are positive,
\[
\mathbf n_{+,+}=\mathbf h+\mathbf k,\quad
\mathbf n_{-,-}=-\mathbf h-\mathbf k,\quad
\mathbf n_{+,-}=\mathbf h-\mathbf k,\quad
\mathbf n_{-,+}=-\mathbf h+\mathbf k.
\]
Their respective pairwise weight sums are \(w_{+,+}+w_{-,-}=w_{+,-}+w_{-,+}=1/2\). Since \(\sum w_{s,t}\mathbf n_{s,t}=0\) and \(\mathbf h+\mathbf k\) and \(\mathbf h-\mathbf k\) are linearly independent (because \(a,b>0\)), both differences \(w_{+,+}-w_{-,-}\) and \(w_{+,-}-w_{-,+}\) vanish. Thus all four weights are \(1/4\) (so none were zero), and the displayed Bloch vectors are valid at all four effects.

Any two orthogonal ordered vectors in \(\mathbb R^3\) of lengths \(\lambda,\mu\) can be transformed to \(\lambda e_x,\mu e_z\) by a proper rotation. Conjugation by a suitable \(2\times2\) unitary implements that rotation on Pauli matrices. Hence, after changing the orthonormal basis of the compressed subspace, all four effects equal \(E^0_{s,t}\). Two nonzero rows whose rank-one Gram matrices agree differ only by a scalar phase. Therefore the isometry is \(\operatorname{diag}(\zeta_{s,t})V_0U\) for some unitary \(U\in M_2(\mathbb C)\), and its range is as claimed. Conversely each diagonal unitary commutes with \(D_{a,b}\), so it preserves the numerical range of each compressed matrix. The scalar part of every maximizing compression is zero since the four weights are equal, while the semiaxes both equal \(ab/r\), proving the stated unique numerical-range disk.

**5. Positive-block consequence.** Sababheh's extremal theorem \(\Phi(X)=\delta_2(X)\) for complex finite matrices immediately supplies the displayed explicit value of \(\Phi(D_{a,b})\). It is not reproved or claimed as a new theorem here.

## Verification
The standalone standard-library program `verify_rectangle.py` checks exactly, using rational arithmetic, that the four proposed effects are positive rank one, sum to the identity, and reconstruct the required compressed matrix for the Pythagorean parameter pairs \((a,b,r)=(3,4,5),(5,12,13),(8,15,17),(7,24,25)\) and their side swaps. It also verifies the algebraic compatibility and semiaxis identities for these exact examples. The proof in parts 1–4 is valid for **all** real \(a,b>0\); finite arithmetic tests are consistency checks, not substitutes for that proof.

## Relationship to prior work
Bourin and Lee (2021, arXiv:2111.15180v1, Theorem 2.1) introduced the elliptical width and used it in positive-block eigenvalue inequalities. Sababheh (2026, arXiv:2610.04377v1, Theorem 3.2 and Section 5) proves the exact positive-block defect identity and treats a three-dimensional normal sharpness example. Neither of those inspected sources gives an exact four-rectangle compression formula or classifies its maximizing subspaces. The three-point normal-spectrum geometry and the four-vertex rectangle geometry address different compression optimization problems; a three-point formula does not supply the present four-point value.

There is a second important, genuinely related literature: Busch and Heinosaari (2007, arXiv:0706.1415, Proposition 5 and condition (39)) show that two jointly measurable binary qubit observables obey \(\|\mathbf h+\mathbf k\|+\|\mathbf h-\mathbf k\|\le2\), and Yu–Liu–Li–Oh (2008, arXiv:0805.1538, Theorem 1) characterize compatibility of general qubit marginals. These established results motivate, and substantially constrain, the upper-bound mechanism in part 2. They do **not** state an optimum of the two-dimensional normal-compression elliptical minor-axis functional for a four-vertex spectrum, nor the rigidity and diagonal-unitary orbit of all attaining subspaces. The short inequality used above is independently derived by grouping the four rank-one effects; the novel claim is the exact operator-geometric optimization together with complete extremizer classification, not a new qubit-compatibility criterion.

## Limitations
The result is for a four-corner rectangle with strictly positive half-sides, not for arbitrary four-point spectral configurations. The relation to qubit compatibility means that the numerical upper bound is close to previously known measurement trade-off inequalities; mathematical originality rests particularly on the exact normal-compression optimum and all-maximizer rigidity. An unindexed equivalent formulation in earlier numerical-range or quantum measurement literature cannot be excluded. No independent audit has occurred. Numerical checks cannot establish a universal formula over continuum parameters.

## References
1. Mohammad Sababheh, *An Extremal Formula for Elliptical Width and the Bourin–Lee Conjecture*, arXiv:2610.04377v1, publicly posted 2026-10-03, https://arxiv.org/pdf/2610.04377.
2. Jean-Christophe Bourin and Eun-Young Lee, *Eigenvalue inequalities for positive block matrices with the inradius of the numerical range*, arXiv:2111.15180v1 (2021), https://arxiv.org/html/2111.15180v1.
3. Paul Busch and Teiko Heinosaari, *Approximate joint measurements of qubit observables*, arXiv:0706.1415 (2007), https://arxiv.org/pdf/0706.1415.
4. Sixia Yu, Nai-le Liu, Li Li and C. H. Oh, *Joint measurement of two unsharp observables of a qubit*, arXiv:0805.1538 (2008), https://arxiv.org/pdf/0805.1538.
