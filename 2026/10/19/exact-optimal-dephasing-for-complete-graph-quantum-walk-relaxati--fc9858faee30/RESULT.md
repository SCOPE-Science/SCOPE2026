# Exact optimal dephasing for complete-graph quantum-walk relaxation

## Finding

For every integer \(n\geq3\), positive hopping strength \(J\), and site-dephasing rate \(\gamma>0\), consider the Haken–Strobl quantum walk on the complete graph with \(n\) vertices. Let \(\mathcal L_\gamma\) be its Lindblad generator and define its **spectral relaxation gap** as
\[
 g_n(\gamma)=\min\{-\operatorname{Re}\lambda:\lambda\in\operatorname{spec}(\mathcal L_\gamma),\ \lambda\neq0\}.
\]
The exact Liouvillian characteristic polynomial is
\[
 \det(\lambda I-\mathcal L_\gamma)
 =\lambda(\lambda+\gamma)^{(n-1)(n-2)}
 \bigl[\lambda^3+2\gamma\lambda^2+(\gamma^2+n^2J^2)\lambda+2n\gamma J^2\bigr]^{n-1}.
\]
In particular, **the globally optimal dephasing rate is unique** and is given by
\[
 \boxed{\gamma_*=J(n-1)\sqrt{\frac n{n-2}},\qquad
 \max_{\gamma>0}g_n(\gamma)=g_n(\gamma_*)=J\sqrt{\frac n{n-2}}.}
\]
All other positive dephasing rates give a strictly smaller spectral gap. Thus the optimal environmental noise scales like \(nJ\), while the maximal asymptotic exponential relaxation rate approaches \(J\) as \(n\to\infty\).

## Assumptions and scope

The Hilbert space is \(\mathbb C^n\) with orthonormal site vectors \(\{|j\rangle\}_{j=1}^n\), and the Hamiltonian is \(H=J(\mathbf1\mathbf1^{\mathsf T}-I)\). The Markovian generator acts on all complex \(n\times n\) matrices according to
\[
 \mathcal L_\gamma(X)=-i[H,X]-\gamma\bigl(X-\operatorname{diag}X\bigr).
\]
This corresponds to local projective Lindblad jumps with common rate \(\gamma\); diagonal entries are not directly dephased and each off-diagonal entry is damped at rate \(\gamma\). We use units with \(\hbar=1\). No loss, hopping disorder, or additional bath terms are included.

For \(J>0\) and \(\gamma>0\), the stationary state \(I/n\) is unique. The spectral gap characterizes the least-damped nonstationary eigenmode, hence the leading exponential rate in finite-dimensional relaxation. It is **not** a claim that a finite-time trace-distance mixing criterion, its transient prefactor, or an experiment-specific distinguishability metric has the same optimizing rate.

## Proof

**1. Full-spectrum decomposition.** Since the scalar diagonal part of \(H\) drops out of the commutator, it suffices to use \(J\mathbf1\mathbf1^{\mathsf T}\). For every vector \(v\in\mathbb C^n\) with \(\sum_jv_j=0\), define
\[
 D(v)_{jk}=\delta_{jk}v_j,\quad
 S(v)_{jk}=(1-\delta_{jk})(v_j+v_k),\quad
 A(v)_{jk}=(1-\delta_{jk})(v_j-v_k).
\]
The row sums of \(S(v)\) and \(A(v)\) are, respectively, \((n-2)v\) and \(nv\), while the column sums of \(A(v)\) are \(-nv\). Direct substitution gives
\[
 \mathcal L_\gamma D(v)=iJ A(v),\qquad
 \mathcal L_\gamma S(v)=-\gamma S(v)+iJ(n-2)A(v),
\]
\[
 \mathcal L_\gamma A(v)=2iJnD(v)+iJnS(v)-\gamma A(v).
\]
Thus, on each of the \(n-1\) independent vector directions \(v\), the generator has the same block
\[
 M_n=\begin{pmatrix}
 0&0&2iJn\\
 0&-\gamma&iJn\\
 iJ&iJ(n-2)&-\gamma
 \end{pmatrix},\qquad
 \det(\lambda I-M_n)=p_{n,\gamma}(\lambda),
\]
where
\[
 p_{n,\gamma}(\lambda)=\lambda^3+2\gamma\lambda^2+(\gamma^2+n^2J^2)\lambda+2n\gamma J^2.
\]
These subspaces are linearly independent for \(n\ge3\). The remaining invariant complement is spanned by the identity, the all-ones off-diagonal matrix, and the symmetric or skew-symmetric zero-diagonal matrices whose row sums vanish. On the identity \(\mathcal L_\gamma\) is zero. The uniform off-diagonal matrix commutes with \(H\) and is damped at rate \(\gamma\). Each zero-row-sum symmetric or skew-symmetric matrix also commutes with \(H\) (its column sums vanish as well) and is damped at rate \(\gamma\). The latter eigenspace has dimension \((n-1)(n-2)\), by dimension counting (the symmetric zero-row-sum part has dimension \(n(n-3)/2\), the skew part has \((n-1)(n-2)/2\), and the all-ones off-diagonal matrix contributes one). This proves the characteristic polynomial for all \(n\ge3\), including algebraic multiplicities. Notice that the zero root is simple, and the Routh–Hurwitz inequality
\[
 (2\gamma)(\gamma^2+n^2J^2)>2n\gamma J^2
\]
shows all cubic roots have strictly negative real part.

**2. Universal upper bound.** Since \(p_{n,\gamma}(0)=2n\gamma J^2>0\) and \(p_{n,\gamma}(\lambda)\to-\infty\) as \(\lambda\to-\infty\), the cubic has at least one negative real root \(\lambda=-r\) with \(r>0\). The spectral gap cannot exceed \(r\). Rearrange \(p_{n,\gamma}(-r)=0\) as a quadratic equation in the real parameter \(\gamma\):
\[
 r\gamma^2-2(r^2+nJ^2)\gamma+r(r^2+n^2J^2)=0.
\]
Its discriminant equals
\[
 4nJ^2\bigl[nJ^2-(n-2)r^2\bigr].
\]
Nonnegativity of this discriminant forces \(r\le J\sqrt{n/(n-2)}\). Hence for **every** positive \(\gamma\),
\[
 g_n(\gamma)\le J\sqrt{\frac n{n-2}}.
\]
No assumption about which cubic root dominates the spectrum is needed for this upper bound.

**3. Sharpness and uniqueness.** Let \(r_*=J\sqrt{n/(n-2)}\) and \(\gamma_*=(n-1)r_*\). At this rate the cubic factorizes:
\[
 p_{n,\gamma_*}(\lambda)
 =(\lambda+r_*)\left[\lambda^2+(2n-3)r_*\lambda+2n(n-1)J^2\right].
\]
The two roots of the quadratic are a nonreal conjugate pair: its discriminant is
\[
 \frac{nJ^2}{n-2}(-4n^2+12n-7)<0\qquad(n\ge3).
\]
Their common real part equals \(-(n-\tfrac32)r_*<-r_*\). The remaining eigenvalues \(-\gamma_*=-(n-1)r_*\) are also strictly more damped. Therefore \(g_n(\gamma_*)=r_*\), attaining the bound.

If any other rate attained the same gap, then its negative real cubic root \(-r\) would satisfy both \(r\ge r_*\) (because the gap cannot exceed \(r\)) and \(r\le r_*\) (from the discriminant). Equality forces the discriminant to vanish, and the repeated solution of the quadratic in \(\gamma\) is necessarily \(\gamma=(r_*^2+nJ^2)/r_*=(n-1)r_*\). This proves uniqueness.

## Verification

The standalone `verify.py` builds the full complex \(n^2\)-dimensional Liouvillian directly from the master equation, without using the proposed three-dimensional reduction. It compares full spectra against the predicted factorization and checks the sharp upper bound and proposed maximizing rate across \(3\le n\le8\), two different positive hopping strengths, and seven noise-to-optimum ratios. The recorded execution passed 264 checks; the largest absolute eigenvalue-matching discrepancy was below \(4\times10^{-13}\). Execute with `python verify.py` after installing NumPy.

The finite checks only test examples. The exact formula, upper bound, and uniqueness for arbitrarily large \(n\) follow from the preceding algebraic proof.

## Relationship to prior work

Bressanini, Benedetti, and Paris [1] analyze quantum-classical distance for continuous-time quantum walks, including the complete graph under site-basis Haken–Strobl dephasing. Their position-dephasing section formulates the same master equation and reports numerical rates and nonmonotone dephasing behavior, but it does not provide this complete-graph Liouvillian characteristic polynomial or a closed global optimizer for its spectral gap.

Luppi, Benedetti, and Smirne [2] establish a bound on decay of a temporal nonclassicality measure in terms of a general Lindbladian spectral gap and discuss weak-/strong-dephasing scalings. Their result motivates calculating the gap exactly, but the graph-specific optimization here is not an implication of their general bound alone. The standard Haken–Strobl model itself is not new; the contribution is the dimension-uniform full-spectrum decomposition and unique optimal spectral relaxation rate.

## Limitations

This is a one-excitation, all-to-all, equal-hopping model with spatially uniform Markovian site dephasing. Results do not extend automatically to arbitrary graphs, inhomogeneous rates, non-Markovian dynamics, graph search time, or finite-time operational mixing optima. At vanishing dephasing the stationary state is no longer unique, so the \(\gamma=0\) point is excluded. The theorem begins at \(n=3\); the two-site case has different spectral degeneracies. The optimal spectral gap need not optimize every time-dependent distance or state-preparation protocol.

## References

[1] G. Bressanini, C. Benedetti, and M. G. A. Paris, *Decoherence and classicalization of continuous-time quantum walks on graphs*, Quantum Information Processing 21, 317 (2022), arXiv:2204.01836, DOI:10.1007/s11128-022-03647-x. First arXiv submission: 2022-04-04.

[2] P. Luppi, C. Benedetti, and A. Smirne, *Temporal nonclassicality in continuous-time quantum walks*, arXiv:2512.18873 (2025), especially Section V and Appendix A.
