# A universal square-zero obstruction to relative spear operators on Hilbert spaces

## Finding
Let \(H\) and \(K\) be nonzero **complex Hilbert spaces**, without separability or finite-dimensionality assumptions, and let \(G\in\mathcal B(H,K)\) have \(\|G\|=1\). For \(T\in\mathcal B(H,K)\), define
\[
m_G(T)=\inf_{\delta>0}\sup\{\|Tx\|:\|x\|=1,\ \|Gx\|>1-\delta\},
\]
and
\[
v_G(T)=\inf_{\delta>0}\sup\{|\langle Tx,z\rangle|:\|x\|=\|z\|=1,\ \operatorname{Re}\langle Gx,z\rangle>1-\delta\}.
\]
The inner product is linear in its first variable. The following statements hold.

**(i)** If \(\dim K=1\), then \(v_G(T)=m_G(T)\) for every \(T\).

**(ii)** If \(\dim K\ge2\), there exists a square-zero partial isometry \(S\in\mathcal B(K)\) with \(\|S\|=1\) such that, for \(T=SG\),
\[
m_G(T)=1,\qquad v_G(T)\le\tfrac12.
\]
Consequently, the relative numerical index \(\inf_{m_G(T)>0}v_G(T)/m_G(T)\) is at most \(1/2\) for every such \(G\), and \(G\) is a relative spear operator (equality \(v_G=m_G\) for all \(T\)) **exactly when its codomain is one-dimensional**. The upper bound \(1/2\) is optimal as a universal bound, as witnessed by \(G=I\) on \(\mathbb C^2\).

## Assumptions and scope
The relative functional \(m_G\) is allowed to be a seminorm; no norm-attainment, spectral-gap, compactness, or closed-range condition is imposed on \(G\). The scalar field is \(\mathbb C\). The witness may be infinite-rank when the near-norming images of \(G\) escape weakly. The classification concerns all bounded test maps \(T:H\to K\), not just finite-rank test maps.

## Proof
**Step 1: a norming-image splitting lemma.** For any sequence \((y_n)\) of vectors in a Hilbert space \(K\) with \(\|y_n\|\to1\) and \(\dim K\ge2\), there is a subsequence \((y_{n_j})\) and a nonzero closed subspace \(M\subset K\) such that \(\operatorname{dist}(y_{n_j},M)\to0\) and \(\dim M\le\dim M^\perp\). In fact, the selected vectors can be chosen inside \(M\) in the case of a nonunit weak limit.

To prove the lemma, pass to a weakly convergent subsequence \(y_n\rightharpoonup y\), using weak sequential compactness of Hilbert balls. If \(\|y\|=1\), weak convergence together with \(\|y_n\|\to1\) gives norm convergence. Take \(M=\operatorname{span}\{y\}\); it has a nonzero orthogonal complement and the lemma follows.

If \(\|y\|<1\), then \(u_n=(y_n-y)/\|y_n-y\|\) is a weakly null sequence of unit vectors, because \(\|y_n-y\|\to\sqrt{1-\|y\|^2}>0\). By induction, select a subsequence \((u_{n_j})\) so that its distinct pairwise inner products are absolutely bounded by a summable matrix with operator norm less than \(1/4\); if \(y\ne0\), also make all inner products with \(y/\|y\|\) summably small, with a combined off-diagonal Gram-operator norm less than \(1/2\). This is possible because \(u_n\rightharpoonup0\). The Gram operator of the selected unit vectors, together with \(y/\|y\|\) when present, differs from the identity in operator norm by less than \(1/2\). Thus this family is a **Riesz sequence**, with a uniform lower \(\ell_2\)-coefficient bound.

Put \(M=\overline{\operatorname{span}}(\{y\}\cup\{u_{n_{2j}}:j\ge1\})\). Every corresponding even-indexed \(y_{n_{2j}}\) lies in \(M\). The Riesz lower bound shows that the odd-indexed \(u_{n_{2j+1}}\) are linearly independent modulo \(M\), with an infinite-dimensional closed span in the quotient: otherwise a nonzero finite combination of odd vectors could approach \(M\), contradicting the same lower bound. Hence \(\dim M^\perp=\infty\), while \(M\) is separable and infinite-dimensional. An isometric embedding \(V:M\longrightarrow M^\perp\) therefore exists. This proves the lemma, including the dimension inequality.

**Step 2: a norm-one square-zero witness.** Choose unit vectors \(x_n\in H\) with \(\|Gx_n\|\to1\) and apply Step 1 to \(y_n=Gx_n\). Obtain \(M\), a subsequence of near-norming images approaching \(M\), and an isometry \(V:M\to M^\perp\). Write \(P_M\) for the orthogonal projection onto \(M\) and let \(S=VP_M\). Then \(\|S\|=1\), \(S^2=0\), and \(S\) is a partial isometry. Moreover, the selected \(Gx_{n_j}\) satisfy \(\|SGx_{n_j}\|\to1\), so \(m_G(SG)=1\), since \(\|SG\|\le1\).

**Step 3: numerical-radius control.** Orthogonality of the initial and final spaces of \(S\) gives, for every \(a\in K\),
\[
|\langle Sa,a\rangle|
\le \|P_Ma\|\,\|P_{M^\perp}a\|
\le\tfrac12\|a\|^2.
\]
If \(\|x\|=\|z\|=1\) and \(\operatorname{Re}\langle Gx,z\rangle>1-\delta\), then
\[
\|Gx-z\|^2=\|Gx\|^2+1-2\operatorname{Re}\langle Gx,z\rangle<2\delta.
\]
Consequently
\[
|\langle SGx,z\rangle|
\le|\langle SGx,Gx\rangle|+\|SGx\|\,\|z-Gx\|
\le\tfrac12+\sqrt{2\delta}.
\]
Taking the defining infimum as \(\delta\downarrow0\) proves \(v_G(SG)\le1/2\).

**Step 4: scalar codomain and sharpness.** When \(\dim K=1\), every norm-one functional on \(K\) has modulus one on every unit vector. For each unit \(x\) with \(\|Gx\|>1-\delta\), choose the norm-one scalar functional evaluating \(Gx\) as \(\|Gx\|\). Its value on \(Tx\) has modulus \(\|Tx\|\). Hence, for \(0<\delta<1\), the inner suprema defining \(v_G(T)\) and \(m_G(T)\) are equal; taking infima proves (i).

Finally, if \(G=I\) on \(\mathbb C^2\), then \(m_G(T)=\|T\|\) and \(v_G(T)\) is the usual numerical radius \(w(T)\). The classical sharp inequality \(\tfrac12\|T\|\le w(T)\) holds for all complex Hilbert-space operators and equality occurs for \(T=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}\). Thus the universal coefficient cannot be reduced below \(1/2\). This completes the proof.

## Verification
The argument above uses only Hilbert-space weak compactness, an explicitly described almost-orthogonal subsequence extraction, and elementary numerical-range estimates. A standalone NumPy checker in `checker.py` performs 13,041 finite assertions, including complex finite-dimensional witnesses, square-zero identities, and a sharp identity-operator example. These finite tests corroborate but do not establish the infinite-dimensional Riesz-subsequence step.

## Relationship to prior work
Dey and Pal (2026, Section 3.2, Theorem 3.12 and Question 1) show that a finite-dimensional Hilbert relative spear operator must be a partial isometry and explicitly ask for the infinite-dimensional analogue. The theorem here instead gives a complete scalar-codomain classification in every dimension, with a uniform quantitative obstruction.

Kadets, Martín, Merí, Pérez, and Quero (2019) determine possible values of the **ordinary** relative numerical index, whose denominator is the full operator norm; this does not determine the index formed using \(m_G\), which can be strictly smaller than the operator norm. Kadets, Martín, Merí, and Quero (2024) introduce the near-norming relative seminorm and study generating operators; the quantitative square-zero obstruction is not among the results inspected. Their bibliography mentions unpublished work on relative spear operators, which remains a historical-priority caveat.

## Limitations
The conclusion requires Hilbert codomains. It does not classify relative spear operators into general Banach spaces, nor does it compute the exact relative index for each individual non-scalar \(G\). The coefficient \(1/2\) is optimal only as a uniform obstruction, not asserted to equal every individual index. Publication-priority comparison remains nonexhaustive because the referenced unpublished work has not been inspected.

## References
1. L. K. Dey and S. Pal, *On the geometry of G-norm*, arXiv:2603.20796, first public version 21 March 2026, Sections 1 and 3.2; https://arxiv.org/abs/2603.20796.
2. V. Kadets, M. Martín, J. Merí, A. Pérez, and A. Quero, *On the numerical index with respect to an operator*, arXiv:1905.12257, 2019, Sections 3–4; https://arxiv.org/abs/1905.12257.
3. V. Kadets, M. Martín, J. Merí, and A. Quero, *Generating operators between Banach spaces*, Rev. R. Acad. Cienc. Exactas Fís. Nat. Ser. A-Mat. 118 (2024), article 90; https://doi.org/10.1007/s13398-024-01582-3.
