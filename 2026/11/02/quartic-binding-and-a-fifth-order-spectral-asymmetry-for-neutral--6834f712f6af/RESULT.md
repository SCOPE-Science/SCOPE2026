# Quartic binding and a fifth-order spectral asymmetry for neutral lattice defects

## Finding

For a nonzero, real, finitely supported potential \(w:\mathbb Z\to\mathbb R\) satisfying \(\sum_n w_n=0\), consider the selfadjoint tight-binding Hamiltonian
\[
(H_\varepsilon\psi)(n)=J\bigl(\psi(n-1)+\psi(n+1)\bigr)+\varepsilon w_n\psi(n),\qquad J>0.
\]
Let its occupied defect positions be \(n_1<\cdots<n_m\), with weights \(w_i=w_{n_i}\). Set
\[
A=\sum_{k=n_1}^{n_m-1}\left(\sum_{n_i\le k}w_i\right)^2
=-\frac12\sum_{i,j=1}^m w_iw_j|n_i-n_j|>0,
\]
\[
B=\sum_{i=1}^m w_i\left(\sum_{j=1}^m|n_i-n_j|w_j\right)^2.
\]
For all sufficiently small nonzero real \(\varepsilon\), precisely one simple eigenvalue \(E_+(\varepsilon)\) lies above \(2J\), and precisely one simple eigenvalue \(E_-(\varepsilon)\) lies below \(-2J\). Their positive distances from the free band obey
\[
\boxed{\begin{aligned}
E_+(\varepsilon)-2J&=\frac{A^2}{4J^3}\varepsilon^4+\frac{AB}{8J^4}\varepsilon^5+O(\varepsilon^6),\\
-2J-E_-(\varepsilon)&=\frac{A^2}{4J^3}\varepsilon^4-\frac{AB}{8J^4}\varepsilon^5+O(\varepsilon^6).
\end{aligned}}
\]
Thus their gap difference is \(AB\varepsilon^5/(4J^4)+O(\varepsilon^7)\). For **every** nonzero real \(\varepsilon\), not just weak coupling, there is at least one eigenvalue on each side of the free band; uniqueness at arbitrary coupling is **not** asserted.

The quartic law expresses cancellation of the ordinary nonzero-mean quadratic binding mechanism. The fifth-order term detects a cubic signed-charge imbalance; geometric reflection symmetry by itself need not make it vanish. For example, at \(J=1\) and \((n_i,w_i)=(0,1),(1,-2),(5,1)\), one has \(A=5\), \(B=-32\), hence the two gaps are respectively \(25\varepsilon^4/4-20\varepsilon^5+O(\varepsilon^6)\) and \(25\varepsilon^4/4+20\varepsilon^5+O(\varepsilon^6)\).

## Assumptions and scope

The ambient Hilbert space is \(\ell^2(\mathbb Z)\). The hopping coefficient \(J\) is fixed and strictly positive. The weights are real, not all zero, and vanish outside a finite set; their total sum is exactly zero. The coupling \(\varepsilon\) may have either sign. The essential spectrum is \([-2J,2J]\), by finite-rank perturbation. The statements about uniqueness and series expansion hold for sufficiently small \(|\varepsilon|>0\), with the smallness bound allowed to depend on \(J\) and the potential. The all-coupling existence assertion has no uniqueness or quantitative gap claim.

## Proof

**1. Positivity of the neutral-potential invariant.** For consecutive integer cuts \(k\), write \(Q_k=\sum_{n_i\le k}w_i\). Every unordered pair of defect positions is separated by precisely \(|n_i-n_j|\) cuts. Since \(\sum_i w_i=0\), its contribution to the quadratic form gives
\[
\sum_{i,j}w_iw_j|n_i-n_j|=2\sum_k Q_k(-Q_k)=-2\sum_kQ_k^2.
\]
Because the nonzero finitely supported potential is neutral, at least one cumulative charge \(Q_k\) is nonzero, whence \(A>0\).

**2. Secular reduction.** For \(\kappa>0\), define \(E=2J\cosh\kappa\). The free resolvent \((E-H_0)^{-1}\) restricted to the defect positions has kernel
\[
G_\kappa(i,j)=\frac{e^{-\kappa|n_i-n_j|}}{2J\sinh\kappa}.
\]
An eigenvalue outside the band must solve \(\det(I-\varepsilon G_\kappa W)=0\), where \(W=\operatorname{diag}(w_1,\dots,w_m)\). Let \({\bf 1}\) be the all-ones column and \(D_{ij}=|n_i-n_j|\). Split
\[
G_\kappa=\frac{{\bf 1}{\bf 1}^{\mathsf T}}{2J\sinh\kappa}+R_\kappa,
\qquad
R_\kappa(i,j)=\frac{e^{-\kappa D_{ij}}-1}{2J\sinh\kappa}.
\]
The matrix \(R_\kappa\) extends analytically to \(\kappa=0\), with \(R_0=-D/(2J)\), and remains bounded over \(\kappa\ge0\). Consequently, for sufficiently small \(|\varepsilon|\), \(K=I-\varepsilon R_\kappa W\) is invertible for every \(\kappa\ge0\). The rank-one determinant lemma now reduces the entire positive-edge eigenvalue condition to the scalar equation
\[
F(\kappa,\varepsilon):=2J\sinh\kappa-\varepsilon\,w^{\mathsf T}(I-\varepsilon R_\kappa W)^{-1}{\bf 1}=0.
\]

**3. The complete weak-coupling edge expansion.** Neutrality cancels the zeroth-order term \(w^{\mathsf T}{\bf 1}\). Expanding the inverse and using \(R_0=-D/(2J)\) gives, uniformly for \(\kappa=O(\varepsilon^2)\),
\[
\begin{aligned}
w^{\mathsf T}(I-\varepsilon R_\kappa W)^{-1}{\bf 1}
&=\varepsilon w^{\mathsf T}R_0w
+\varepsilon^2w^{\mathsf T}R_0WR_0w+O(\varepsilon^3)\\
&=\frac{A}{J}\varepsilon+\frac{B}{4J^2}\varepsilon^2+O(\varepsilon^3).
\end{aligned}
\]
The analytic implicit function theorem applies at \((\kappa,\varepsilon)=(0,0)\), because \(F(0,0)=0\) and \(\partial_\kappa F(0,0)=2J\ne0\). It yields a unique small analytic branch
\[
\kappa_+(\varepsilon)=\frac{A}{2J^2}\varepsilon^2+\frac{B}{8J^3}\varepsilon^3+O(\varepsilon^4).
\]
The leading positive coefficient guarantees \(\kappa_+(\varepsilon)>0\) for both coupling signs when \(\varepsilon\ne0\) is small. Since \(F\) has strictly positive \(\kappa\)-derivative in a fixed neighborhood of zero, the root there is unique. Outside that neighborhood, \(2J\sinh\kappa\) is uniformly bounded away from zero while the second term in \(F\) is \(O(\varepsilon^2)\), so there can be no additional root. The rank-one reduction and simple scalar root imply the corresponding eigenvalue is simple. Finally,
\[
2J\cosh\kappa_+-2J=J\kappa_+^2+O(\kappa_+^4),
\]
which proves the stated upper-edge quartic and quintic terms.

**4. Lower edge and spectral asymmetry.** The unitary \((U\psi)(n)=(-1)^n\psi(n)\) satisfies \(UH_\varepsilon U^{-1}=-H_{-\varepsilon}\). Hence \(E_-(\varepsilon)=-E_+(-\varepsilon)\) for the unique weak-coupling extremal branches. Substitute \(-\varepsilon\) into the upper-edge expansion to obtain the lower formula. Analyticity shows that the even powers cancel from the difference, leaving the stated \(O(\varepsilon^7)\) remainder.

**5. Existence at arbitrary nonzero coupling.** The function \(M(\varepsilon)=\sup\sigma(H_\varepsilon)\) is finite and convex, being a supremum of affine Rayleigh quotients. It satisfies \(M(\varepsilon)\ge2J=M(0)\) for every real \(\varepsilon\). The weak-coupling result shows \(M(\varepsilon)>2J\) on each side of zero near zero. Convexity therefore forces \(M(\varepsilon)>2J\) at every positive and every negative nonzero coupling. Since the perturbation has finite rank, such spectral points above the essential spectrum are eigenvalues. The unitary identity in step 4 supplies an eigenvalue below \(-2J\) for every nonzero coupling.

## Verification

Run `python check.py` from the same directory with Python, NumPy, SciPy and mpmath installed. The program checks five nontrivial neutral potential patterns. For each, it computes \(A\) independently by a signed distance quadratic form and by cumulative charges, solves the finite-rank secular determinant to 65-digit working precision at four weak couplings of either sign, and compares with the fourth- and fifth-order expansion. It additionally constructs large finite Jacobi matrices and checks both exterior eigenvalues against the infinite-volume secular solutions (eight matrix comparisons in total). See `check_output.txt` for the actual values and assertion results. These finite examples corroborate, but do not replace, the infinite-family proof above.

## Relationship to prior work

Damanik, Hundertmark, Killip and Simon proved a general variational existence criterion for indefinite-sign discrete Schrödinger potentials (their Theorem 3.1), but it does not give the two simultaneous band-edge branches, the neutral-potential quartic coefficient, or the quintic asymmetry invariant here. Simon's continuum weak-coupling work is an antecedent to quadratic and exceptional higher-order binding, not a discrete-lattice formula. Webb and Olver gave a general polynomial framework for finite-rank Jacobi spectra; extracting the sign-independent two-edge quartic term and the signed fifth-order term requires an additional singular band-edge analysis. The present result uses and credits the standard finite-rank resolvent method rather than claiming that method itself as new.

## Limitations

There is no claim of global uniqueness, no treatment of infinite-support defects, nonuniform hopping, nonlinear interactions or multi-particle spectra. The \(O\)-constants depend on the fixed potential and hopping. For arbitrary coupling, the number of bound states may exceed two. Prior-art comparison is necessarily provisional, particularly because the full text of some early continuum threshold papers was not available during this review. The numerical checks are finite tests, not exhaustive evidence for infinitely many potentials.

## References

1. D. Damanik, D. Hundertmark, R. Killip, B. Simon, *Variational Estimates for Discrete Schrödinger Operators with Potentials of Indefinite Sign*, arXiv:math-ph/0211015 (first posted 2002-11-11), https://arxiv.org/abs/math-ph/0211015.
2. M. Webb, S. Olver, *Spectra of Jacobi operators via connection coefficient matrices*, arXiv:1702.03095 (first posted 2017-02-10), https://arxiv.org/abs/1702.03095.
3. B. Simon, *The bound state of weakly coupled Schrödinger operators in one and two dimensions*, Annals of Physics **97** (1976), 279–288, https://doi.org/10.1016/0003-4916(76)90038-5.
