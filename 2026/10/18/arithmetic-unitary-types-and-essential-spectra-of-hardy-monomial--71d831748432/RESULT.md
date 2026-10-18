# Arithmetic unitary types and essential spectra of Hardy monomial composition-adjoint products

## Finding
Let \(m,k\geq2\) be integers and let \(C_m f=f(z^m)\) act on the classical complex Hardy space \(H^2(\mathbb D)\). Set \(T_{m,k}=C_k^*C_m\), \(d=\gcd(m,k)\), \(a=m/d\), and \(b=k/d\). Write \(S\) for the unilateral forward shift on \(\ell^2(\mathbb N_0)\), \(J_L\) for the length-\(L\) truncated forward shift on \(\mathbb C^L\), \(P_0\) for the projection onto constants, and \(\infty\cdot B\) for countably many orthogonal copies of \(B\).

**Complete unitary classification.** Exactly one of the following holds:
\[
T_{m,k}\simeq
\begin{cases}
 I, & a=b=1,\\
 1\oplus(\infty\cdot S),&a>1,\ b=1,\\
 1\oplus(\infty\cdot S^*),&a=1,\ b>1,\\
 1\oplus\displaystyle\bigoplus_{L=1}^{\infty}(\infty\cdot J_L),&a>1,\ b>1.
\end{cases}
\]
The four unitary classes are distinct. In particular, every pair of incomparable integers (neither divides the other) yields exactly the same unitary-equivalence class, irrespective of the integers themselves.

**Exact operator and essential spectral consequences.** For \(m\ne k\),
\[
\sigma(T_{m,k})=\sigma_{\mathrm{ess}}(T_{m,k})=\overline{\mathbb D},
\qquad
\|p(T_{m,k})\|=\|p(T_{m,k})\|_{\mathrm{ess}}=
\max_{|z|\le1}|p(z)|
\]
for every complex polynomial \(p\). Here the essential spectrum is the Fredholm/Calkin spectrum, and the essential norm is distance to the compact operators. If \(m=k\), then \(T_{m,m}=I\), its spectrum and essential spectrum are \(\{1\}\), and \(\|p(T_{m,m})\|=|p(1)|\).

The point spectra distinguish the nontrivial regimes: they are \(\{1\}\) for \(a>1,b=1\), \(\mathbb D\cup\{1\}\) for \(a=1,b>1\), and \(\{0,1\}\) for \(a,b>1\). If \(b>1\), then \(T_{m,k}^N\to P_0\) strongly while \(\|T_{m,k}^N-P_0\|=1\) for every positive integer \(N\).

## Assumptions and scope
All spaces are complex Hilbert spaces. The Hardy space has its usual orthonormal monomial basis \(e_n(z)=z^n\), \(n\in\mathbb N_0\), and \(\mathbb N_0=\{0,1,2,\ldots\}\). The operator \(C_m\) is composition with the holomorphic self-map \(z\mapsto z^m\). All orthogonal sums and multiplicities are Hilbert-space direct sums. The assertions are exact for every \(m,k\ge2\), without asymptotic restrictions.

## Proof
**1. Coefficient action.** Each \(C_m\) is an isometry, because \(C_m e_n=e_{mn}\) on the orthonormal basis. Consequently
\[
C_k^*e_j=\begin{cases}e_{j/k},&k\mid j,\\0,&k\nmid j,\end{cases}
\qquad
T_{m,k}e_n=\begin{cases}e_{an/b},&b\mid n,\\0,&b\nmid n.\end{cases}
\]
The last identity uses \(\gcd(a,b)=1\), and also gives \(T_{m,k}e_0=e_0\). Thus the constants reduce \(T_{m,k}\), and it suffices to classify the action on \(H_0=zH^2\). Since this action is an injective partial permutation on its nonzero images, \(T_{m,k}\) and all its positive powers are partial isometries.

**2. Arithmetic partition.** Every positive integer \(n\) has exactly one representation
\[
n=a^j b^h c,\quad j,h\in\mathbb N_0,\quad a\nmid c\ (a>1),\quad b\nmid c\ (b>1),
\]
with the conventions \(j=0\) when \(a=1\), and \(h=0\) when \(b=1\). Indeed, divide out the maximal powers of \(a\) and \(b\). These maximal exponents are independent because \(a\) and \(b\) are coprime. In the case \(a,b>1\), fix \(c\) with \(a\nmid c\) and \(b\nmid c\), and a length \(L\ge1\). The corresponding mutually orthogonal monomial chain is
\[
e_{cb^{L-1}}\longmapsto e_{cab^{L-2}}\longmapsto\cdots
\longmapsto e_{ca^{L-1}}\longmapsto0.
\]
Every basis vector belongs to exactly one such chain (its length is \(j+h+1\)). For each \(L\) there are infinitely many possible \(c\): for example all positive integers congruent to \(1\) modulo \(ab\). This proves that **every** truncated-shift length has multiplicity exactly countably infinite, and there are no other summands on \(H_0\).

If \(a>1,b=1\), the chains \(e_c\mapsto e_{ac}\mapsto e_{a^2c}\mapsto\cdots\), indexed by \(a\nmid c\), are forward shifts. If \(a=1,b>1\), the chains \(\cdots\mapsto e_{b^2c}\mapsto e_{bc}\mapsto e_c\mapsto0\), indexed by \(b\nmid c\), are backward shifts. Each index set is infinite. If \(a=b=1\), the coefficient action is the identity. The point-spectrum assertions now follow from the elementary point spectra of these shift models. The four models are pairwise inequivalent: in the identity case the eigenspace at \(1\) is infinite dimensional; in the forward-shift case it is one dimensional and the operator is injective; in the backward-shift case every point in \(\mathbb D\) is an eigenvalue; in the truncated-shift case \(0\) is an eigenvalue but the only other eigenvalue is \(1\).

**3. Polynomial norms.** All models are contractions, so von Neumann's polynomial inequality gives \(\|p(T_{m,k})\|\le\max_{|z|\le1}|p(z)|\). For every \(|\lambda|=1\), choose a unit vector in a length-\(L\) truncated-shift block with coordinates proportional to \(1,\lambda^{-1},\ldots,\lambda^{-(L-1)}\); its \((J_L-\lambda I)\)-residual is \(1/\sqrt L\). The same finite phase vectors supply approximate eigenvectors for \(S\), and reversed phase vectors do so for \(S^*\). Applying a polynomial and letting \(L\to\infty\) gives \(\|p(T_{m,k})\|\ge|p(\lambda)|\). To obtain the essential-norm inequality, take these unit vectors in mutually orthogonal blocks or copies so that they converge weakly to zero; a compact perturbation vanishes on such vectors. The maximum-modulus principle completes both equalities.

**4. Essential spectrum and power limits.** For \(|\lambda|>1\), \(T_{m,k}-\lambda I\) is invertible by the Neumann series. In the forward-shift regime, \(|\lambda|<1\) gives an infinite-dimensional kernel of \(S^*-\overline\lambda I\), hence an infinite-dimensional cokernel of \(S-\lambda I\); in the backward regime it gives an infinite-dimensional kernel. In the truncated-shift regime, \(\lambda=0\) has infinite-dimensional kernel. For \(0<|\lambda|<1\), a length-\(L\) block contains the vector with coordinates \(1,\lambda^{-1},\ldots,\lambda^{-(L-1)}\); after normalization its \((J_L-\lambda I)\)-residual tends to zero as \(L\to\infty\). Boundary points also admit singular Weyl sequences by the vectors in Step 3. Choosing these sequences in pairwise orthogonal blocks ensures weak convergence to zero; thus the corresponding operator cannot be Fredholm. This proves the full essential disk and hence the full spectral disk. For \(b>1\), every basis vector in \(H_0\) is annihilated by a sufficiently high power, so contraction plus density implies strong convergence to zero on \(H_0\). Yet arbitrarily long chains (or the co-shift) force the norm of every positive power restricted to \(H_0\) to equal one. Thus the displayed strong-but-not-uniform assertion follows.

## Verification
The accompanying pure-Python `checker.py` verifies the exact arithmetic coefficient rules, maximal-power decomposition, chain disjointness, and forward/backward/truncated transitions for eleven specified \((m,k)\) pairs and thousands of positive indices. It reports 90,377 passing finite integer assertions. This is a finite diagnostic, not a substitute for the general argument in Steps 1–4. In particular, it does not purport to prove an infinite-dimensional spectral assertion computationally.

## Relationship to prior work
Leng and Zhao (arXiv:2610.15472v1, first public 2026-10-11) study Schatten-class criteria for products of composition operators and their adjoints on Hardy and Bergman spaces. The present result instead classifies the **unitary equivalence type, every truncated-shift multiplicity, full Fredholm spectrum, and polynomial essential norms** of the monomial pair. The general Halmos–Wallen decomposition of power partial isometries already supplies abstract forward/backward/truncated-shift building blocks; it does not determine the arithmetic multiplicity profile for \(C_k^*C_m\). The fully accessible modern proof of that decomposition by an Huef, Raeburn and Tolich (arXiv:1703.03506, Section 2) is used as a comparison, not claimed as new. The classification here is derived directly from the basis action and divisibility.

## Limitations
This is a result only for standard unweighted Hardy-space composition operators with **integer monomial symbols**. It does not classify nonmonomial inner maps, general weighted Hardy spaces, or products taken in reversed order. The general partial-isometry model and polynomial inequality are established prior results; the claimed new content is their *exact arithmetic realization* for the natural monomial product family and the resulting sharp essential-norm/spectral characterization. Equivalent results in less searchable literature on arithmetic partial permutations cannot be categorically excluded without independent priority review.

## References
1. Q. Leng and X. Zhao, *Schatten class membership of products of composition operators and their adjoints*, arXiv:2610.15472v1 (2026), https://arxiv.org/abs/2610.15472.
2. A. an Huef, I. Raeburn and I. Tolich, *Structure theorems for star-commuting power partial isometries*, arXiv:1703.03506 (2017), especially Theorem 2.1, https://arxiv.org/abs/1703.03506.
3. P. R. Halmos and L. J. Wallen, *Powers of partial isometries*, Indiana Univ. Math. J. 19 (1970), 657–663.
4. J. von Neumann, polynomial inequality for Hilbert-space contractions (standard theorem).
