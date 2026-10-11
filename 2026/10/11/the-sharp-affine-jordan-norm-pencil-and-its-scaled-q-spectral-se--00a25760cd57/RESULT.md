# The sharp affine Jordan norm pencil and its scaled \(q\)-spectral-set transition

## Finding
Let \(n\ge2\) be an integer and let \(J_n\in M_n(\mathbb C)\) be the nilpotent Jordan shift with ones on the first superdiagonal. Set
\[
B_n(\lambda)=(1-\lambda)I_n+\lambda J_n,\qquad
s_n=\frac{n+1}{2n+1},\qquad
\gamma_n=\|B_n(s_n)\|_2.
\]
Here \(\|\cdot\|_2\) is the induced Euclidean operator norm and \(\lambda\) ranges over **all complex numbers**, not just a real interval. Then
\[
\boxed{\quad\|B_n(\lambda)\|_2>\gamma_n\quad(\lambda\ne s_n).\quad}
\]
In particular, \(s_n\) is the unique complex minimizer. There is a finite exact prescription
\[
\boxed{\quad\gamma_n=\frac{\sqrt{\lambda_{\max}(Q_n)}}{2n+1},\quad
Q_n=(nI_n+(n+1)J_n)^*(nI_n+(n+1)J_n).\quad}
\]
The matrix \(Q_n\) is real symmetric tridiagonal: its first diagonal entry is \(n^2\), all other diagonal entries are \(n^2+(n+1)^2\), and both adjacent diagonals are \(n(n+1)\). Equivalently its eigenvalues consist of the simple eigenvalue \(1\) and \(n-1\) values \(\Lambda=n^2+(n+1)^2+2n(n+1)\cos\theta>1\) for roots \(\theta\in(0,\pi)\) of
\[
 n\sin((n+1)\theta)+(n+1)\sin(n\theta)=0.
\]
The largest of these values determines \(\gamma_n\). In the first two dimensions,
\[
\gamma_2=\frac45,\qquad
\gamma_3=\frac{\sqrt{29+4\sqrt7}}7.
\]
Moreover \(0<\gamma_n<1\), the sequence is nondecreasing, and \(\gamma_n\to1\).

A single interpretation of this sharp minimax identity uses the scaled \(q\)-numerical range. For \(0<q\le1\), let
\[
W_q(J_n)=\{\langle J_nx,y\rangle:\|x\|=\|y\|=1,\ \langle x,y\rangle=q\},\qquad
\Omega_q(J_n)=q^{-1}W_q(J_n),
\]
using the complex Hilbert inner product linear in the first entry. Then \(\Omega_q(J_n)\) is a closed disk centered at zero, and it is a \(1\)-spectral set for \(J_n\) **if and only if**
\[
\boxed{\quad0<q\le\gamma_n.\quad}
\]
Thus the same exact finite matrix singular value both solves the affine operator-norm minimization and gives the sharp dimension-dependent contractive spectral-set transition. For \(n\ge3\) the threshold is strictly greater than the universal \(4/5\) boundary of the known sharp dimension-free scaled-\(q\) spectral-constant estimate.

## Assumptions and scope
The field is complex, the dimension is any fixed finite integer \(n\ge2\), and the shift \(J_n\) is the unweighted nilpotent upper Jordan block; the assertion is not made for arbitrary weighted shifts or nonnilpotent matrices. Complex \(\lambda\) is unconstrained. The definition of \(1\)-spectral set here means the inequality \(\|p(J_n)\|_2\le\max_{z\in\Omega}|p(z)|\) for **every complex polynomial** \(p\); by standard disk functional calculus the equivalent statement holds for functions holomorphic near the disk. Only these disks, not arbitrary convex regions, are considered.

## Proof
**1. An isolated bottom singular value.** Fix \(n\ge2\) and abbreviate \(m=2n+1\), \(d=n(n+1)\), \(a_j=n+1-j\), and \(Q=Q_n\). Direct expansion gives, for all \(x\in\mathbb C^n\), the *exact ground-state decomposition*
\[
\langle(Q-I_n)x,x\rangle
=d\sum_{j=1}^{n-1}a_ja_{j+1}
\left|\frac{x_j}{a_j}+\frac{x_{j+1}}{a_{j+1}}\right|^2.
\]
The endpoint and interior diagonal coefficients are respectively \(n^2-1\) and \(2d=n^2+(n+1)^2-1\), so this equality can be checked by expansion, including the two endpoints. Hence \(Q-I_n\) is positive semidefinite and has one-dimensional kernel spanned by \(v=(n,-(n-1),\ldots,(-1)^{n-1})\). Every other eigenvalue is greater than \(1\). On the other hand \(\|nI_n+(n+1)J_n\|_2<m\): equality in the norm triangle inequality would require a unit vector satisfying \(J_nx=x\), impossible for a nilpotent shift. Thus all eigenvalues of \(Q\) are less than \(m^2\).

**2. Stationarity of every nonbottom singular branch.** Let \(\Lambda>1\) be an eigenvalue of \(Q\). Write \(\Lambda=n^2+(n+1)^2+2d\cos\theta\) with \(0<\theta<\pi\), possible by the preceding bounds. The constant-coefficient Jacobi recurrence for \(Q\) gives an eigenvector
\[
x_j=\sin((n+1-j)\theta),\qquad1\le j\le n,
\]
and its first-row equation becomes \(n\sin((n+1)\theta)+(n+1)\sin(n\theta)=0\). The last-row equation is automatic. Put \(z=\cos\theta\), \(L=\Lambda\). The boundary equation and the sine addition formula yield
\[
\sin^2(n\theta)=\frac{n^2(1-z^2)}{L}.
\]
The finite sine-sum formulas, simplified with that same boundary condition, give
\[
\sum_{j=1}^{n}|x_j|^2=\frac{m}{4}\left(1-\frac1L\right),\qquad
\sum_{j=1}^{n-1}x_jx_{j+1}=
\frac{nz}{2}+\frac{n^2}{2L}\left(\frac{n+1}{n}+z\right).
\]
Substitution of \(L=n^2+(n+1)^2+2dz\) into these two identities shows exactly that
\[
\boxed{\quad\sum_{j=1}^n|x_j|^2-\sum_{j=1}^{n-1}x_jx_{j+1}
=(n+1)|x_1|^2.\quad}
\]
The displayed formulas derive from finite geometric trigonometric sums; no limiting argument or numerical eigenvector computation is used. They are also verified as an identity in the symbols \(n,z\) by the accompanying checker.

For \(B_n(s)=(1-s)I_n+sJ_n\) and \(H(s)=B_n(s)^*B_n(s)\), differentiation at the real point \(s=s_n\) gives
\[
H'(s_n)=\frac2m\left(I_n-(n+1)e_1e_1^*-
\frac{J_n+J_n^*}{2}\right).
\]
Consequently, for every real eigenvector of \(Q\) with eigenvalue greater than \(1\), the displayed identity gives \(\langle H'(s_n)x,x\rangle=0\). In particular the top right singular vector \(x_0\) can be chosen real and unit, so
\[
\langle B_n(s_n)x_0,(J_n-I_n)x_0\rangle=0.
\]
Here no simplicity assumption is needed to expand the norm along this fixed vector, though the top eigenvalue is in fact simple because \(Q\) is irreducible symmetric tridiagonal.

**3. Strict global minimization, including complex coefficients.** For any \(\lambda\in\mathbb C\), since \(B_n(\lambda)=B_n(s_n)+(\lambda-s_n)(J_n-I_n)\), the exact orthogonality above yields
\[
\|B_n(\lambda)x_0\|^2
=\gamma_n^2+|\lambda-s_n|^2\|(J_n-I_n)x_0\|^2.
\]
The final factor is strictly positive because \(J_n\) has no eigenvalue \(1\). Hence \(\|B_n(\lambda)\|_2\ge\|B_n(\lambda)x_0\|>\gamma_n\) for every \(\lambda\ne s_n\). This proves both the global complex minimum and its uniqueness. The tridiagonal description, the two small-dimensional formulas and the bounds \(0<\gamma_n<1\) now follow by direct algebra. The compression \(B_{n}(\lambda)\) of \(B_{n+1}(\lambda)\) shows \(\gamma_{n+1}\ge\gamma_n\). Testing \(B_n(s_n)\) on \((1,\ldots,1)/\sqrt n\) gives
\[
\gamma_n^2\ge \frac{n-1+(n/(2n+1))^2}{n}\longrightarrow1,
\]
while \(\gamma_n\le1\), proving convergence.

**4. Exact \(1\)-spectral-set transition.** Simultaneous diagonal unitary rotation of the Jordan shift sends \(J_n\) to \(e^{i\phi}J_n\). The space of admissible pairs of unit vectors with fixed inner product \(q\) is connected (for \(q<1\) it is a complex two-frame manifold, and for \(q=1\) a sphere). Moreover \(0\in W_q(J_n)\) by taking \(x=e_1\). It follows by continuity and circular symmetry that \(W_q(J_n)\) is precisely a closed centered disk of radius \(r_n(q)=\max|\langle J_nx,y\rangle|\).

Let \(s=s_n\), \(\gamma=\gamma_n\), and take the top singular vectors \(x_0\), \(y_0=B_n(s)x_0/\gamma\). The orthogonality in Step 2 gives
\[
\langle x_0,y_0\rangle=\langle J_nx_0,y_0\rangle=\gamma.
\]
Thus \(r_n(\gamma)\ge\gamma\). Conversely, for every \(0<q\le1\), circular symmetry permits a maximizing admissible pair for \(r_n(q)\) whose value \(\langle J_nx,y\rangle\) is nonnegative real. The bound \(\|B_n(s)\|=\gamma\) therefore implies
\[
\boxed{\quad(1-s)q+s\,r_n(q)\le\gamma.\quad}
\]
In particular \(r_n(\gamma)=\gamma\) and \(r_n(q)<q\) when \(q>\gamma\). To treat \(q<\gamma\), decompose \(J_nx_0=a x_0+bz_0\) with \(z_0\perp x_0\), \(a\ge0\), \(b>0\); positivity of the top singular vector ensures \(a\ge0\), and nilpotency implies \(b\ne0\). The above singular-pair identity gives \(a+\sqrt{\gamma^{-2}-1}\,b=1\). The admissible choice \(y=q x_0+\sqrt{1-q^2}\,z_0\) then shows
\[
\frac{r_n(q)}q\ge a+\sqrt{q^{-2}-1}\,b>1\qquad(0<q<\gamma).
\]
Consequently the radius of \(\Omega_q(J_n)\) is at least \(1\) exactly for \(q\le\gamma\). Since \(\|J_n\|=1\), von Neumann's disk inequality proves that every centered disk of radius at least \(1\) is a \(1\)-spectral set for \(J_n\). Conversely the polynomial \(p(z)=z\) rules out any centered disk of radius less than \(1\). This proves the stated equivalence without an unproved interpolation or generic minimax interchange.

## Verification
The separate source file `verify_jordan_pencil.py` checks the all-parameter rational identity used in the trigonometric calculation with symbolic simplification; checks the ground-state Gram factorization exactly for the first eight nontrivial sizes; checks the two characteristic polynomials exactly; and tests the singular-vector stationarity and comparison at multiple scalar values in dimensions \(2\) through \(9\). It prints the markers `JORDAN_PENCIL_EXACT_GRAM_AND_TRIG_IDENTITY_OK` and `JORDAN_PENCIL_NUMERIC_SINGULAR_STATIONARITY_OK` when successful. The infinite-dimensional-parameter statement (all integers \(n\ge2\)) is proved analytically above: these finite computations are supplementary, not a purported exhaustive proof.

## Relationship to prior work
O'Loughlin and Rani's first-public 16 March 2026 preprint `arXiv:2603.15536v1`, *\(q\)-Numerical Ranges and Spectral Sets*, motivates operator-dependent scaled-range spectral constants and studies their general geometric bounds. Its later 19-page version was inspected, including Section 4 and the application to GMRES; it does not give the above all-size unique affine Jordan minimizer or dimension-dependent exact \(1\)-spectral cutoff. The August 2026 result of Aouichaoui and O'Loughlin (`arXiv:2608.09866`) establishes a sharp dimension-free spectral constant, which guarantees the \(1\)-spectral property for \(q\le4/5\), but does not give the larger operator-specific threshold \(\gamma_n\) for \(n\ge3\). Tichý, Liesen, and Faber, *Worst-case and ideal GMRES for a Jordan block* (2007), Section 6, investigate precisely the corresponding one-step norm minimization for the Jordan block with eigenvalue \(1\); their Theorem 6.2 proves the bounds \(\cos(\pi/(2n))\le\gamma_n\le\cos(\pi/(2n+1))\), not the unique exact minimizing coefficient given here. The September 2026 paper by Kaunisto, O'Loughlin and Virtanen (`arXiv:2610.00443`) concerns general scaled-\(q\) dilation constants; its full text was not retrieved. These comparisons concern implications and exact coefficients, not title similarity.

## Limitations
This is a finite-dimensional, unweighted-Jordan statement, not a universal \(1\)-spectral theorem for arbitrary matrices or \(q\)-numerical ranges. The trigonometric root formula is an exact implicit finite-dimensional spectral prescription, not a radical expression for arbitrary \(n\). Exact novelty beyond the primary manuscripts carries residual risk from inaccessible relevant full texts or unindexed prior results. No independent mathematical audit has been performed.

## References
1. R. O'Loughlin and J. Rani, *\(q\)-Numerical Ranges and Spectral Sets*, `arXiv:2603.15536`, first submitted 16 March 2026; inspected 19-page version dated 3 October 2026. https://arxiv.org/abs/2603.15536
2. M. A. Aouichaoui and R. O'Loughlin, *Sharp spectral constants for scaled \(q\)-numerical ranges*, `arXiv:2608.09866`, first submitted 10 August 2026. https://arxiv.org/abs/2608.09866
3. M. Kaunisto, R. O'Loughlin and J. Virtanen, *Dilation Theory for Scaled \(q\)-Numerical Ranges*, `arXiv:2610.00443`, first submitted 30 September 2026. https://arxiv.org/abs/2610.00443
4. P. Tichý, J. Liesen and V. Faber, *Worst-case and ideal GMRES for a Jordan block*, 2007, Section 6, Theorem 6.2. https://www2.karlin.mff.cuni.cz/~ptichy/download/public/TiLiFa2007.pdf
5. J. von Neumann, the classical contraction inequality for polynomial functional calculus on the unit disk.
