# Exact parity dichotomy for projective revivals in harmonic spin-coupled Grover hypercube walks

## Finding
For the central-harmonic invariant sectors of the spin-coupled Grover walk on the \(d\)-dimensional hypercube defined in Wang's 2026 construction, with a common spin sign on the supporting central Hamming layers, exact *collective projective revival* exhibits a complete parity dichotomy. For every even \(d\ge2\), the restricted evolution is the identity, so the entire harmonic sector returns at every positive integer time. For every odd \(d\ge3\), **no positive integer \(T\) and no phase \(\zeta\in\mathbb C\), \(|\zeta|=1\), satisfy**
\[
U_d^{T}=\zeta I.
\]
Moreover, in every odd dimension, every harmonic initial vector with nonzero projections onto all eight distinct restricted eigenvalue sectors has no exact projective revival; such vectors form a full-measure open dense subset of the harmonic unit sphere. The odd statement is new arithmetic information about exact finite-time dynamics, rather than a restatement of the previously computed spectrum.

## Assumptions and scope
Let \(d\ge2\), and take the position space of the \(d\)-cube with coin space \(\mathbb C^d\). Use the spin-coupled Grover transition specified by the Grover coin \(G=2|u_d\rangle\langle u_d|-I\), conditional coordinate flips and the Hamming-level spin phase of Wang (2026), equations (2.5), (4.5)–(4.7). The fixed spin configuration has a common value \(\varepsilon\in\{\pm1\}\) on layers \(m-1,m,m+1\) if \(d=2m\), or on layers \(m-1,m,m+1,m+2\) if \(d=2m+1\); outside the specified layers, spin values are arbitrary. Let \(\mathcal H_{\mathrm{har}}\) be precisely Wang's three-layer (even) or four-layer (odd) central-harmonic invariant subspace, and let \(U_d\) be the restriction of the physical walk to that subspace. The statement is about **all state rays in this harmonic sector simultaneously**; it does not assert aperiodicity for each individual eigenstate or for all spin configurations.

A collective projective revival at \(T\in\mathbb N_{>0}\) means \(U_d^T=\zeta I\) for some unit complex \(\zeta\). A single vector \(\psi\) has an exact projective revival when \(U_d^T\psi=\zeta\psi\). These two definitions must not be conflated.

## Proof
**1. Even dimensions.** For \(d=2m\ge2\), the source's Theorem 4.1 constructs the harmonic lift and proves \(U_d=I\). Hence every positive integer is a collective revival time with phase \(1\). This even-dimensional half is a previously published result, not a separate novelty claim.

**2. The odd reduced matrix and two exact invariants.** Let \(d=2m+1\ge3\), and write \(\omega=\exp(-i\varepsilon\pi/d)\). Wang's Theorem 4.3 gives an invertible intertwining map under which \(U_d\) is similar to \(I\otimes M\), with an eight-dimensional matrix \(M\) defined by its action \(y=Mx\):
\[
\begin{aligned}
y_0&=\frac{\omega^m}{d}(-x_1+2(m+1)x_2+2x_3),&y_1&=-\omega^{m-1}x_0,\\
y_2&=-\omega^{m+1}x_4,&y_3&=\frac{\omega^{m+1}}d(2x_4+x_5+2mx_6),\\
y_4&=\frac{\omega^m}d(2mx_1+x_2+2x_3),&y_5&=-\omega^m x_3,\\
y_6&=-\omega^{m+2}x_7,&y_7&=\frac{\omega^{m+1}}d(2x_4+2(m+1)x_5-x_6).
\end{aligned}
\]
For reproducibility, these are precisely the eight formulas in the source's equation (4.20), rather than an inferred generic Grover matrix. Factoring \(\omega^{m+a_j}\) from row \(j\), with \((a_0,\ldots,a_7)=(0,-1,1,1,0,0,2,1)\), leaves a rational matrix. Moving rows \((0,1,4,5)\) ahead of \((2,3,6,7)\) (an even permutation) makes it block diagonal with
\[
B_1=\begin{pmatrix}0&-1/d&2(m+1)/d&2/d\\-1&0&0&0\\0&2m/d&1/d&2/d\\0&0&0&-1\end{pmatrix},\quad
B_2=\begin{pmatrix}-1&0&0&0\\2/d&1/d&2m/d&0\\0&0&0&-1\\2/d&2(m+1)/d&-1/d&0\end{pmatrix}.
\]
Cofactor expansion, using \(d=2m+1\), gives \(\det B_1=\det B_2=1\). Therefore
\[
\det M=\omega^{8m+4}=\omega^{4d}=1.
\]
Only five off-diagonal reciprocal pairs contribute to \(\operatorname{tr}(M^2)\). Direct multiplication, followed by \(\omega^d=-1\), yields
\[
\alpha_d:=\operatorname{tr}(M^2)
=-\frac2d(\omega^2+\omega^{-2})+\frac4d-\frac8{d^2}
=\frac{4d-8-2d\,t_d}{d^2},\qquad t_d=2\cos(2\pi/d).
\]
The value is independent of the choice \(\varepsilon=\pm1\). As a cross-check, Newton identities applied to the source's characteristic polynomial \(\lambda^8+A_d\lambda^6+B_d\lambda^4+A_d\lambda^2+1\) give the same \(\alpha_d=-2A_d\).

**3. Arithmetic obstruction in every odd dimension.** The number \(t_d=\exp(2\pi i/d)+\exp(-2\pi i/d)\) is a real algebraic integer. We prove that \(\alpha_d\) is **not** an algebraic integer for any odd \(d\ge3\):

* If \(d=3\), then \(t_3=-1\) and \(\alpha_3=10/9\), a nonintegral rational number.
* If \(d=5\), then \(t_5\) satisfies \(t_5^2+t_5-1=0\), while \(\alpha_5=(12-10t_5)/25\). Its norm from \(\mathbb Q(\sqrt5)\) is
  \[
  N_{\mathbb Q(\sqrt5)/\mathbb Q}(\alpha_5)=\frac{164}{625},
  \]
  not an integer. The norm of an algebraic integer must be an integer.
* If \(d\ge7\) is odd, every algebraic conjugate of \(t_d\) is \(2\cos(2\pi k/d)\) for some \(k\) coprime to \(d\), hence lies in \([-2,2]\). Consequently every conjugate of \(\alpha_d\) has absolute value at most
  \[
  \frac{4d-8+4d}{d^2}=\frac{8(d-1)}{d^2}<1.
  \]
  Also \(\alpha_d\ne0\): otherwise \(t_d=2-4/d\), a nonintegral rational algebraic integer, impossible. If \(\alpha_d\) were a nonzero algebraic integer, its nonzero integer field norm would have absolute value at least \(1\), contradicting the strict bound on every conjugate.

**4. No exact collective or generic projective revival.** Suppose \(U_d^T=\zeta I\) for an odd \(d\) and some positive integer \(T\). Similarity then gives \(M^T=\zeta I_8\). Taking determinants and using \(\det M=1\) gives \(\zeta^8=1\); hence \(M^{8T}=I_8\). Every eigenvalue of \(M\) is therefore a root of unity. Their squares are algebraic integers, so their sum \(\operatorname{tr}(M^2)=\alpha_d\) must be an algebraic integer, contradicting Step 3.

Finally, the source's Corollary 4.5 proves that the odd reduced matrix has eight distinct eigenvalues. If an initial harmonic vector has a nonzero projection into each eigenvalue sector and returns up to phase at some positive time, projecting the return equation to those eight sectors forces all eight eigenvalues to have the same \(T\)-th power, and hence \(M^T=\zeta I\), already excluded. The vectors missing one or more sectors form a finite union of proper linear subspaces, of measure zero and with empty interior in the harmonic sphere. This proves the stated generic consequence.

## Verification
The accompanying standalone `verify_revivals.py` reconstructs the eight rows directly from the stated formulas and checks exact rational determinants of both four-dimensional coefficient blocks. It separately verifies the complex trace-square and determinant for both spin signs in every odd dimension from \(3\) to \(201\), along with the two exceptional small-dimensional arithmetic calculations. It reports **603 passing deterministic assertions**. The universal conclusion is certified by the algebraic argument in Steps 2–4, **not** by the finite tests.

## Relationship to prior work
Wang (2026), Theorems 4.1 and 4.3 and Corollary 4.5, supplies the central harmonic subspaces, eight-dimensional odd reduction, complete characteristic polynomial, and spectral simplicity; none of those spectral or representation results is claimed here. Its equations (4.34)–(4.35) exclude only the eigenvalues \(\pm1\) and \(\pm i\), not arbitrary roots of unity or equality of all eigenvalue powers. The additional arithmetic obstruction above resolves the distinct question of **exact all-sector projective return** in every odd dimension.

Existing periodicity results for ordinary Grover or Fourier walks on cycles, regular graphs, and Grover walks modified by magnetic vector potentials investigate different transition operators and do not immediately subsume the present spin-coupled harmonic sector. Periodicity is a standard physical question; the new component is the all-dimension arithmetic exclusion for this particular eight-mode reduced dynamics. The general principle that finite-order unitary eigenvalues are roots of unity is classical and is not claimed as novel.

## Limitations
The finding concerns only the common-spin-sign central harmonic subspaces in Wang's construction. It does not classify the full walk across all spin sectors, individual vectors confined to fewer than eight eigenvalue sectors, near-recurrences, measurement probabilities that recur without full state revival, or perturbations of coin and spin-phase parameters. Even in an odd dimension, individual eigenvectors return projectively at every time; there is no contrary claim. The mathematical extension is derived from a source's explicit reduced matrix, and possible implication by broader published cyclotomic periodicity criteria remains an originality risk. No independent audit has been performed.

## References
1. Ce Wang, *Harmonic Reduction of Spin-Coupled Grover Walks on Hypercubes via Quantum Bernoulli Noises*, arXiv:2610.14467, initial public version 10 October 2026, relevant original equations (4.5), (4.6), (4.20), (4.34)–(4.36), Theorem 4.1, Theorem 4.3 and Corollary 4.5. Full-text HTML: https://arxiv.org/html/2610.14467v2 .
2. Hiroto Sekido and Etsuo Segawa, *Robustness of periodicity in Grover walks under a magnetic vector potential*, arXiv:2607.14797 (2026). Different ordinary/magnetic Grover operator; only abstract accessible in this comparison.
3. Takeshi Kajiwara, Norio Konno, Shohei Koyama and Kei Saito, *Periodicity for the 3-state quantum walk on cycles*, arXiv:1907.01725 (2019). Different cycle-walk family; abstract comparison.
