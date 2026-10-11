# Mixed hyperbolicity obstructs super asymptotic expansivity
## Finding
Let \(T\) be a bounded hyperbolic operator on a complex Banach space, and let \(X=X_s\oplus X_u\) be its Riesz spectral splitting for the parts of \(\sigma(T)\) inside and outside the unit circle. Under Definition 3.3 of arXiv:2610.01196v1, if both \(X_s\) and \(X_u\) are nonzero, then \(T\) is not super asymptotically expansive. If one of the two spectral subspaces is zero, then \(T\) is super asymptotically expansive. Consequently, on a finite-dimensional complex normed space, \(T\) is super asymptotically expansive if and only if either \(\sigma(T)\subset\mathbb D\) or \(\sigma(T)\subset\mathbb C\setminus\overline{\mathbb D}\). In particular, the hyperbolic and surjective Hilbert-space operator \(T=\operatorname{diag}(1/2,2)\) is not super asymptotically expansive, so the hyperbolicity-to-super implication asserted in Theorem 4.5 and Corollary 4.6 of arXiv:2610.01196v1, and the resulting finite-dimensional and surjective-Hilbert equivalences, fail for the stated definition.

For the concrete operator \(T=\operatorname{diag}(1/2,2)\) on \(\mathbb C^2\) with its Euclidean norm, fix \(N\ge 1\) and put
\[
a_N^2=\frac{4^N-1}{4^N-4^{-N}},\qquad b_N^2=\frac{1-4^{-N}}{4^N-4^{-N}},\qquad z_N=(a_N,b_N).
\]
Then \(a_N^2+b_N^2=1\), so \(\|z_N\|_2=1\), and
\[
\|T^Nz_N\|_2^2=4^{-N}a_N^2+4^Nb_N^2=1.
\]
Taking \(\varepsilon=1/2\) and \(M=2\), every proposed uniform cutoff \(N\) is defeated by the corresponding unit vector \(z_N\): at time \(N\), its norm is neither below \(\varepsilon\) nor above \(M\).

## Assumptions and scope
The definition of super asymptotic expansivity is exactly Definition 3.3 of Bag--Mandal--Das: for every \(\varepsilon,M>0\) there must be one \(N=N(\varepsilon,M)\) such that every unit vector is, for all \(n\ge N\), in the small-orbit alternative or the large-orbit alternative. The counterexample above actually defeats both the fixed-branch and pointwise readings of the displayed alternative because at the single testing time \(n=N\) its norm lies strictly between \(\varepsilon\) and \(M\).

The Banach-space statement assumes hyperbolicity, so the standard Riesz decomposition
\[
X=X_s\oplus X_u,
\]
with \(\sigma(T|_{X_s})\subset\mathbb D\) and \(\sigma(T|_{X_u})\subset\mathbb C\setminus\overline{\mathbb D}\), is available. The complete if-and-only-if classification is asserted only in finite dimension, where every spectral point is an eigenvalue.

## Proof
Assume first that both \(X_s\) and \(X_u\) are nonzero. Choose unit vectors \(x_s\in X_s\) and \(x_u\in X_u\). By the spectral-radius estimate on the stable restriction, \(\|T^n x_s\|	o0\). By applying the spectral-radius estimate to \((T|_{X_u})^{-1}\), one has \(\|T^n x_u\|	o\infty\), in fact uniformly exponentially from below on the unit sphere of \(X_u\). Hence there is \(n_0\) such that for every \(n\ge n_0\),
\[
\|T^n x_s\|<\frac12,\qquad \|T^n x_u\|>2.
\]

For each such \(n\), consider the explicit unit-sphere path
\[
\gamma(t)=\frac{(1-t)x_s+t x_u}{\|(1-t)x_s+t x_u\|},\qquad 0\le t\le1.
\]
The denominator never vanishes because \(X_s\cap X_u=\{0\}\). The continuous function \(t\mapsto\|T^n\gamma(t)\|\) starts below \(1/2\) and ends above \(2\), so the intermediate value theorem gives \(t_n\) with
\[
\|T^n\gamma(t_n)\|=1.
\]
Now set \(\varepsilon=1/2\) and \(M=2\). For any proposed cutoff \(N\), choose \(n\ge\max\{N,n_0\}\). The unit vector \(\gamma(t_n)\) violates the defining alternative at that time \(n\). Thus a mixed hyperbolic splitting is not super asymptotically expansive.

If \(X_u=\{0\}\), then \(\sigma(T)\subset\mathbb D\), so \(\|T^n\|	o0\) exponentially and all unit vectors eventually satisfy the small alternative uniformly. If \(X_s=\{0\}\), then \(T\) is invertible with \(r(T^{-1})<1\), and
\[
1=\|z\|\le\|T^{-n}\|\,\|T^nz\|
\]
for every unit vector \(z\); hence the minimum of \(\|T^nz\|\) over the unit sphere tends to infinity, and all unit vectors eventually satisfy the large alternative uniformly. This proves the hyperbolic Banach-space dichotomy.

Finally let \(X\) be finite dimensional. If \(T\) is not hyperbolic, some eigenvalue \(\lambda\) has \(|\lambda|=1\); a unit eigenvector has \(\|T^nv\|=1\) for all \(n\), so super asymptotic expansivity fails for \(\varepsilon=1/2\), \(M=2\). If \(T\) is hyperbolic, the preceding dichotomy shows that super asymptotic expansivity holds exactly when one spectral side is empty. This is equivalent to
\[
\sigma(T)\subset\mathbb D\quad	ext{or}\quad\sigma(T)\subset\mathbb C\setminus\overline{\mathbb D}.
\]

## Verification
The explicit \(2	imes2\) witness was checked by exact rational arithmetic: for each tested integer \(1\le N\le7\), the displayed formulas give both \(a_N^2+b_N^2=1\) and \(4^{-N}a_N^2+4^Nb_N^2=1\) identically. The proof itself does not depend on finite testing: the two identities follow by direct algebra for every \(N\ge1\).

The general argument uses only the standard Riesz splitting for hyperbolic bounded operators, the spectral-radius formula on the stable restriction and on the inverse unstable restriction, continuity of an explicit normalized line segment in the unit sphere, and the intermediate value theorem. The relevant spectral splitting and one-sided exponential estimates are stated in the motivating paper itself before Theorem 4.5.

## Relationship to prior work
Bag--Mandal--Das introduce super asymptotic expansivity and define it by a uniform small-or-large alternative on the whole unit sphere. Their Theorem 4.5 asserts that every hyperbolic complex Banach-space operator satisfies a uniform exponential version of that alternative, and Corollary 4.6 deduces hyperbolicity implies super asymptotic expansivity. Their finite-dimensional Corollary 4.8 and surjective-Hilbert Theorem 4.13 use that implication. The proof of Theorem 4.5 first splits the spectrum into stable and unstable invariant subspaces, where the separate estimates are valid, but then states the disjunctive estimate for arbitrary vectors in the whole space. Mixed vectors are exactly what the path argument above obstructs.

The older linear-expansivity literature of Bernardes et al. treats expansivity, uniform positive expansivity, spectra, and shadowing, while Lee--Morales--Villavicencio treat the earlier topological notion of asymptotic expansivity. The motivating preprint explicitly presents super asymptotic expansivity as a new strengthening. Searches using the exact term and aliases such as uniform small-or-large orbit dichotomy, mixed stable/unstable hyperbolicity, and uniform divergence versus decay found no prior statement of the mixed-subspace obstruction or the finite-dimensional classification above.

## Limitations
The exact global classification stated here is for finite-dimensional complex normed spaces. In general complex Banach spaces the proof gives the complete classification within the hyperbolic class, but it does not classify possible nonhyperbolic super asymptotically expansive operators. No claim is made about revised versions of the motivating preprint published after the inspected version \(v1\).

An equivalent observation could exist in older linear-dynamics literature under terminology different from the newly introduced phrase “super asymptotic expansivity”; targeted searches did not locate one. This residual risk affects originality only, not the explicit counterexample or the proof.

## References
1. P. Bag, P. N. Mandal, P. K. Das, *Asymptotic Expansive and Hyperbolic Linear Operators*, arXiv:2610.01196v1, 2026.
2. N. C. Bernardes Jr., P. R. Cirilo, U. B. Darji, A. Messaoudi, E. R. Pujals, *Expansivity and Shadowing in Linear Dynamics*, J. Math. Anal. Appl. 461 (2018), 796--816; arXiv:1612.02921.
3. K. Lee, C. A. Morales, H. Villavicencio, *Asymptotic expansivity*, J. Math. Anal. Appl. 507 (2022), 125729, DOI:10.1016/j.jmaa.2021.125729.
