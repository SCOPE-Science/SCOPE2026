# A modular Calkin-spectrum law for slant Toeplitz monomial commutators

## Finding

Fix an integer \(s\geq 2\), a real parameter \(\alpha>-1\), and nonnegative integers \(m,n\). On the normalized weighted Bergman space \(A^2_\alpha(\mathbb D)\), let \(e_j=z^j/\sqrt{h_j}\), where
\[
h_j=\frac{\Gamma(j+1)\Gamma(\alpha+2)}{\Gamma(j+\alpha+2)}.
\]
Consider either of the following bounded slant maps, initially specified on monomials or the orthonormal basis and then extended continuously:
\[
W_s^{\mathrm{mon}}z^{sj}=z^j,\qquad W_s^{\mathrm{mon}}z^t=0\quad(s\nmid t),
\]
\[
W_s^{\mathrm{on}}e_{sj}=e_j,\qquad W_s^{\mathrm{on}}e_t=0\quad(s\nmid t).
\]
For \(\nu\in\{\mathrm{mon},\mathrm{on}\}\), put \(B_m^{(\nu)}=W_s^{(\nu)}M_{z^m}\), \(C_{m,n}^{(\nu)}=[B_m^{(\nu)},B_n^{(\nu)}]\), and
\[
c_\nu=\begin{cases}s^{\alpha+1},&\nu=\mathrm{mon},\\1,&\nu=\mathrm{on}.\end{cases}
\]
Here \(\sigma_{\mathrm e}\) means Fredholm essential spectrum, and \(\|\cdot\|_{\mathrm e}\) is distance in operator norm to the compact operators. The following is an exact classification, not an asymptotic assertion about finite matrices.

If \(m=n\), then \(C_{m,n}^{(\nu)}=0\). If \(m\ne n\) and \(s^2\nmid(m-n)\), then
\[
\sigma_{\mathrm e}(C_{m,n}^{(\nu)}(C_{m,n}^{(\nu)})^*)=\{2c_\nu^2\},\quad
\sigma_{\mathrm e}(|C_{m,n}^{(\nu)}|)=\{0,\sqrt2c_\nu\},\quad
\|C_{m,n}^{(\nu)}\|_{\mathrm e}=\sqrt2c_\nu.
\]
If \(m\ne n\) and \(s^2\mid(m-n)\), then
\[
\sigma_{\mathrm e}(C_{m,n}^{(\nu)}(C_{m,n}^{(\nu)})^*)=[0,4c_\nu^2],\quad
\sigma_{\mathrm e}(|C_{m,n}^{(\nu)}|)=[0,2c_\nu],\quad
\|C_{m,n}^{(\nu)}\|_{\mathrm e}=2c_\nu.
\]
In particular, for each slant convention, the exact essential norm jumps between two distinct positive constants when the nonzero degree difference crosses divisibility by the **square** of the slant order. The essential spectrum of the positive commutator product changes from a singleton to an interval.

## Assumptions and scope

The measure defining \(A^2_\alpha\) is \((\alpha+1)(1-|z|^2)^\alpha\,dA(z)\), where normalized planar area gives \(\int_{\mathbb D}dA=1\). The two slant maps have different normalizations, so their constants must not be interchanged. Analytic Toeplitz operators with symbols \(z^m\) are the multiplication operators used above. Only bounded operators on this weighted Hilbert space are considered. The parameters \(s,m,n\) are fixed when taking any spectral or large-index limit. The theorem concerns the commutator's positive products and absolute value, **not** the ordinary spectrum of the nonnormal commutator.

## Proof

**1. Boundedness and coefficient asymptotics.** For \(t=sj\), the monomial slant map has \(W_s^{\mathrm{mon}}e_t=\sqrt{h_j/h_t}\,e_j\). Since \(h_j\sim\Gamma(\alpha+2)j^{-(\alpha+1)}\) as \(j\to\infty\), the coefficient converges to \(s^{(\alpha+1)/2}\), hence the map extends boundedly. The orthonormal slant map is a coisometry. Multiplication by \(z^m\) is a contraction in either case.

**2. Exact support and product weights.** Put
\[
\rho_A\equiv -n-sm\pmod{s^2},\qquad
\rho_B\equiv -m-sn\pmod{s^2},\qquad 0\leq\rho_A,\rho_B<s^2,
\]
and define the nonnegative integers
\[
a=\frac{\rho_A+n+sm}{s^2},\qquad
b=\frac{\rho_B+m+sn}{s^2}.
\]
The product \(B_m^{(\nu)}B_n^{(\nu)}\) kills \(e_t\) unless \(t\equiv\rho_A\pmod{s^2}\). If \(t=s^2j+\rho_A\), it sends \(e_t\) to a positive multiple of \(e_{j+a}\). For monomial normalization, this coefficient is **exactly**
\[
\omega_A^{\mathrm{mon}}(t)=\sqrt{\frac{h_{j+a}}{h_t}}\longrightarrow s^{\alpha+1}=c_{\mathrm{mon}}.
\]
For orthonormal normalization, the exact coefficient is
\[
\omega_A^{\mathrm{on}}(t)=
\sqrt{\frac{h_{t+n}}{h_t}
\frac{h_{(t+n)/s+m}}{h_{(t+n)/s}}}
\longrightarrow 1=c_{\mathrm{on}}.
\]
The intermediate indices are integers precisely on this residue class. Reversing \(m,n\) gives the corresponding coefficient for \(B_n^{(\nu)}B_m^{(\nu)}\), supported on \(\rho_B\), with output \(e_{j+b}\) and the same limit \(c_\nu\).

**3. Compact model.** Let \(S e_j=e_{j+1}\) be the unilateral shift on \(\ell_2(\mathbb N_0)\). For \(0\le r<s^2\), define an isometric embedding \(V_r e_j=e_{s^2j+r}\). Identifying \(A^2_\alpha\) with \(\ell_2(\mathbb N_0)\) by its basis, Step 2 gives
\[
B_m^{(\nu)}B_n^{(\nu)}-c_\nu S^aV_{\rho_A}^*\in\mathcal K,
\qquad B_n^{(\nu)}B_m^{(\nu)}-c_\nu S^bV_{\rho_B}^*\in\mathcal K.
\]
Indeed, on each active residue class the difference is a weighted coordinate shift with weights tending to zero; truncation at a finite input index converges in operator norm. Thus
\[
C_{m,n}^{(\nu)}\equiv c_\nu(S^aV_{\rho_A}^*-S^bV_{\rho_B}^*)\pmod{\mathcal K}.
\]
Moreover,
\[
\rho_A=\rho_B\iff s^2\mid(s-1)(m-n)\iff s^2\mid(m-n),
\]
since \(\gcd(s-1,s^2)=1\).

**4. Distinct residue classes.** If \(\rho_A\ne\rho_B\), then \(V_{\rho_A}^*V_{\rho_B}=0\), while \(S^aS^{*a}\) and \(S^bS^{*b}\) differ from the identity only by finite-rank projections. Hence
\[
C_{m,n}^{(\nu)}(C_{m,n}^{(\nu)})^*\equiv 2c_\nu^2 I\pmod{\mathcal K}.
\]
Its Fredholm essential spectrum is the stated singleton and its essential norm is \(\sqrt2c_\nu\).

**5. Coincident residue classes.** If \(\rho_A=\rho_B=r\) and \(m\ne n\), then
\[
a-b=\frac{(s-1)(m-n)}{s^2}\in\mathbb Z\setminus\{0\}.
\]
Let \(U\) be the class of \(S\) in the Calkin algebra. It is unitary with spectrum the whole unit circle: every unimodular number has arbitrarily long, weakly null approximate eigenvectors supported on high consecutive coordinates. Step 3 yields the Calkin identity
\[
[C_{m,n}^{(\nu)}(C_{m,n}^{(\nu)})^*]
=c_\nu^2(2I-U^{a-b}-U^{b-a}).
\]
Continuous functional calculus takes its spectrum to the range of \(c_\nu^2(2-2\cos((a-b)\theta))\), namely \([0,4c_\nu^2]\). Its positive square-root spectral edge gives \(\|C_{m,n}^{(\nu)}\|_{\mathrm e}=2c_\nu\).

**6. Absolute values and zero case.** The nonzero spectra of \([C^*C]\) and \([CC^*]\) in the Calkin algebra coincide (the standard nonzero-spectrum identity for the two products). For \(m\ne n\), the commutator vanishes on every residue input class except at most two, leaving an infinite-dimensional kernel. Hence zero belongs to \(\sigma_{\mathrm e}(|C|)\). Applying the square-root functional calculus proves both asserted descriptions of \(\sigma_{\mathrm e}(|C|)\). If \(m=n\), the commutator vanishes identically. This completes the proof.

## Verification

The accompanying standalone `check_slant.py` verified 184,712 finite assertions, including the exact residue support, both product coefficient formulas, their fixed-parameter limits, and the large-index diagonal/off-diagonal signatures of \(CC^*\). To reproduce, run `python3 check_slant.py` with Python's standard library; the script uses no external data. These tests sample finitely many parameters and do not prove the universal theorem. The universal statements follow from Steps 1–6.

For example, take \(s=2\), \(\alpha=0\), and monomial normalization. The essential norm is \(2\sqrt2\) for \((m,n)=(0,1)\), but equals \(4\) for \((m,n)=(0,4)\). The corresponding essential spectra of \(CC^*\) are \(\{8\}\) and \([0,16]\), respectively. In the orthonormal convention, the same two norms are \(\sqrt2\) and \(2\).

## Relationship to prior work

Cui, Li and Lu (2026, Theorem 2.5 and Corollary 2.6) characterize commutativity and finite-rank commutators for polyanalytic symbols using the unweighted monomial convention and a second-order slant. Their coefficient argument detects residue constraints but does not provide exact essential norms or the positive-product Calkin spectra above. The 2010 work of Lu, Liu and Yang gives qualitative equivalence of commutativity and essential commutativity; a nonzero essential norm is therefore not claimed as new in itself. Liu and Lu (2013) treat slant products and commutativity, not these quantified spectral alternatives.

Singh, Singh and Singh (2025) define the orthonormal-basis slant on weighted Bergman space, analyze individual slant spectra, and present finite commutator-norm simulations (including distinct monomials), but do not state the infinite-dimensional arithmetic spectral dichotomy. Zhang (2025) studies an analytic commutativity problem. Thus the exact scale constants for both conventions and the switch from singleton to interval essential spectrum are the contribution assessed here.

## Limitations

This is restricted to monomial analytic symbols, fixed slant order, and power-weighted Bergman Hilbert spaces. It does not identify the ordinary spectrum of the generally nonnormal commutator, describe arbitrary polynomial symbols, or assert uniform estimates as parameters vary. The numerical checks are finite. Publication priority is assessed on available primary literature and published record searches, not independently certified; the full 2010 Mathematische Nachrichten paper was not accessible for a line-by-line comparison, so an older implicit equivalent formula remains a residual risk. Independent audit has not been performed.

## References

1. P. Cui, R. Li and Y. Lu, *Commuting slant Toeplitz operators for polyanalytic and harmonic symbols*, arXiv:2610.09728v1 (first public 2026-10-07), especially Section 2, Theorem 2.5 and Corollary 2.6. https://arxiv.org/abs/2610.09728
2. O. N. Singh, M. P. Singh and T. S. Singh, *Algebraic and Spectral properties of slant Toeplitz and slant little Hankel Operators on weighted Bergman Space*, arXiv:2507.06546v1 (2025), especially Definition 2.3, Sections 3, 6–7. https://arxiv.org/abs/2507.06546
3. Y. Lu, C. Liu and J. Yang, *Commutativity of kth-order slant Toeplitz operators*, Math. Nachr. 283 (2010), 1304–1313. https://doi.org/10.1002/mana.200710100
4. C. Liu and Y. Lu, *Product and Commutativity of kth-Order Slant Toeplitz Operators*, Abstract Appl. Anal. 2013, 473916. https://doi.org/10.1155/2013/473916
5. H. Y. Zhang, *Commuting Slant Toeplitz Operators on the Bergman Space*, arXiv:2504.01042v1 (2025). https://arxiv.org/abs/2504.01042
