# Exact two-scale fourth-moment deficit for subgroup-hole Fourier spectra

## Statement
Let \(G\) be a finite abelian group of order \(N\), let \(K<\widehat G\) be a proper subgroup of order \(k\), and set \(H=K^\perp\), \(m=|H|=N/k\ge 2\), \(\Lambda=\widehat G\setminus K\). All norms on \(G\) use normalized counting measure. For \(f=\sum_{\chi\in\Lambda}a_\chi\chi\) and each coset \(C\in G/H\), put \(z_C=f|_C\), \(S_C=\|z_C\|_2^2=\sum_{x\in C}|f(x)|^2\), and
\[
V_C=\{z\in\mathbb C^C:\sum_{x\in C}z_x=0\},\quad d=m-1,\quad
p_x=e_x-\frac1m\mathbf1_C\in V_C.
\]
On the real Hilbert space of Hermitian endomorphisms of \(V_C\), with the Hilbert--Schmidt inner product, define
\[
W_C=\operatorname{span}_{\mathbb R}\left\{p_xp_x^*-\frac1m I_{V_C}:x\in C\right\},\qquad
B_C=z_Cz_C^*-\frac{S_C}{d}I_{V_C},
\]
and \(R_C=B_C-\operatorname{Proj}_{W_C}B_C\). Then the following **exact two-scale deficit identity** holds for every complex Fourier coefficient family:
\[
\boxed{\;N\bigl(K_4(\Lambda)^4\|f\|_2^4-\|f\|_4^4\bigr)
=2\alpha_m\sum_{C<D}S_CS_D+\frac{m-2}{m}\sum_C\|R_C\|_{\mathrm{HS}}^2,\quad
\alpha_m=\frac{m^2-3m+3}{m(m-1)}.\;}
\]
Here \(C<D\) ranges over unordered distinct coset pairs, and the sharp norm is
\[
K_4(\Lambda)^4=N\alpha_m=k\left(m-2+\frac1{m-1}\right).
\]
The **norm value is already implied** by the 2026 sharp complex zero-sum \(\ell^4/\ell^2\) result of Zhang, combined with the elementary annihilator-coset reduction, and is given here only to normalize the new deficit identity. In particular the displayed equality for the norm is **not claimed as a new standalone classification**.

Each term on the right is nonnegative. The first measures the loss from distributing squared \(L^2\) mass over several annihilator cosets; the second measures the component of a rank-one operator orthogonal to the simplex-projector span within each coset. The coefficient of the second term vanishes for \(m=2\). The formula gives an exact characterization of equality as vanishing of these terms; it does not claim a more explicit enumeration of all equality orbits. The family \(a_\chi=c\overline{\chi(y)}\), \(c\ne0\), \(y\in G\), attains equality.

## Proof
The averaging operator \(P_Hf(x)=m^{-1}\sum_{h\in H}f(x+h)\) is Fourier projection onto \(K\). The assumed spectrum is disjoint from \(K\), hence \(P_Hf=0\). Thus every \(z_C\) lies in \(V_C\), and the coset masses sum to \(S=\sum_CS_C=N\|f\|_2^2\).

Fix a coset and identify \(V_C\) with \(V=\mathbf1^\perp\subset\mathbb C^m\). Put \(E_j=p_jp_j^*\), where \(p_j=e_j-m^{-1}\mathbf1\). The real self-adjoint map \(T\) on Hermitian endomorphisms of \(V\) is
\[
T(A)=\sum_{j=1}^{m}\operatorname{tr}(AE_j)E_j.
\]
Since \(\sum_jE_j=I_V\), \(\operatorname{tr}(E_j)=(m-1)/m\) and
\(\operatorname{tr}(E_iE_j)=|\langle p_i,p_j\rangle|^2\), the Gram matrix has diagonal \(((m-1)/m)^2\) and off-diagonal \(m^{-2}\). It has eigenvalue \(\lambda_0=(m-1)/m\) on the scalar direction and \(\lambda_1=(m-2)/m\) on the span \(W=\operatorname{span}_{\mathbb R}\{E_j-m^{-1}I_V\}\), and vanishes on the orthogonal complement. For \(m=2\), \(W=\{0\}\) and only the scalar eigenvalue is nonzero.

For \(z\in V\), write \(A=zz^*\), \(S_z=\|z\|_2^2\), and \(B=A-S_zI_V/(m-1)\). Then \(B\) is traceless and
\[
\|B\|_{\rm HS}^2=S_z^2\frac{m-2}{m-1},\qquad
\sum_{j=1}^{m}|z_j|^4=\langle A,T(A)\rangle_{\rm HS}
=\frac{S_z^2}{m}+\frac{m-2}{m}\|\operatorname{Proj}_W B\|_{\rm HS}^2.
\]
Consequently, using \(\alpha_m=1/m+(m-2)^2/[m(m-1)]\), Pythagoras yields the local exact identity
\[
\alpha_m S_z^2-\sum_j|z_j|^4=\frac{m-2}{m}\|B-\operatorname{Proj}_WB\|_{\rm HS}^2.
\]
Summing over all cosets and expanding \(S^2=\sum_CS_C^2+2\sum_{C<D}S_CS_D\) gives the asserted global identity after division by \(N\).

For completeness, this identity shows \(\|f\|_4^4\le N\alpha_m\|f\|_2^4\). Equality is achieved for \(a_\chi=c\overline{\chi(y)}\), since character orthogonality gives
\[
f(x)=c\bigl(N\mathbf1_{\{y\}}(x)-k\mathbf1_{y+H}(x)\bigr).
\]
Its only nonzero coset vector is a scalar multiple of \(p_y\), and then \(B\) belongs to \(W\); both deficit terms are zero. This establishes sharpness and finishes the proof.

## Scope and limitations
The result concerns the fourth moment on finite abelian groups with a deleted dual subgroup, including \(m=2\); it does not assert analogous identities for all higher even moments. The exact defect is measured in Hilbert--Schmidt operator geometry, not directly by Euclidean distance to the nearest extremizing Fourier coefficients. A separate explicit classification of the full equality set is not asserted.

## Relation to previous results
Holevo and Utkin, *A conjecture on a tight norm inequality in the finite-dimensional \(\ell_p\)*, arXiv:2603.24017v2 (2026), established the \(d=3\) real sharp norm and proposed the higher-dimensional theorem. Haonan Zhang, *Proof of the Holevo--Utkin conjecture on sharp \(\ell_p\) norms for zero-sum vectors*, arXiv:2605.05243 (2026), proved the sharp \(\ell^q/\ell^2\) inequality for every real dimension and \(q>2\), explicitly extending the optimal constant to complex vectors. For \(q=4\), the resulting sharp constant is \(\alpha_m\) for \(m\ge2\), and applying it separately on annihilator cosets already yields \(K_4(\Lambda)^4=N\alpha_m\). The norm and extremal-value part of the present statement is therefore covered; **the retained additional assertion is the displayed exact Hilbert--Schmidt two-scale deficit identity**. The published co-singleton character-set computation supplies a further prior special case, but no inspected primary or published-finding source states this full decomposition. A general prior simplex-frame stability identity remains a bibliographic risk.

Michels, *\(\Lambda(p)\)-sets and the limit order of operator ideals*, arXiv:math/9904176v1 (1999), treats infinite \(\Lambda(p)\)-sets and operator ideals. Bonami and Révész, *Concentration of the integral norm of idempotents*, arXiv:0811.4576v1 (2008), treats relative \(L^p\) concentration of idempotents, including finite cyclic groups, rather than the same deficit invariant. Neither source supplies the displayed two-scale operator identity.

## Verification
The proof above is an exact finite-dimensional argument valid for every \(m\) and every number of cosets. The unchanged numerical verifier checks finite samples of the sharp norm, not the new operator deficit. An independent checker separately tested 220 local/global projection identities over \(2\le m\le12\) and 1--5 cosets, with normalized numerical discrepancies below \(5\times10^{-16}\). These experiments corroborate the calculation but do not replace the proof.
