# Exact multiplicative first-band Fourier spectra on finite-field toric hyperplanes

## Finding
For every prime power \(q\ge3\), integer \(d\ge3\), coefficients \(a_1,\ldots,a_d\in\mathbb F_q^\times\), and \(b\in\mathbb F_q\), put
\[
X_b(a)=\{x\in(\mathbb F_q^\times)^d:\ \sum_{i=1}^d a_i x_i=b\}.
\]
Let \(G_b\) be the normalized Gram matrix of the constant function and all **nontrivial single-coordinate multiplicative characters**, restricted to \(X_b(a)\) with uniform probability measure. Its dimension is \(1+d(q-2)\). The following is its **complete eigenvalue multiset**, including zeros; zero multiplicity means omit that entry. It depends on \(a\) only through the harmless coordinate rescaling and on \(b\) only through whether \(b=0\).

Put \(m=q-1\) and \(e=(-1)^d\), where the latter is an ordinary integer. When \(b=0\), set
\[
N_0=\frac{m^d+me}{q},\qquad c=\frac{me}{N_0}.
\]
There is one eigenvalue \(1\). For each sign \(\varepsilon\in\{+1,-1\}\), there are eigenvalues
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
1+(d-1)c\varepsilon&r_\varepsilon\\
1-c\varepsilon&(d-1)r_\varepsilon
\end{array}
\]
where \((r_+,r_-)=((q-3)/2,(q-1)/2)\) for odd \(q\) and \((q-2,0)\) for even \(q\). The signs encode \(\chi(-1)\) for multiplicative characters. Thus the homogeneous system is linearly independent except at \((q,d)=(3,3),(3,4),(4,3)\), where its nullities are respectively \(2,1,2\). For odd \(q\ge5\), the **sharp squared condition number** is
\[
\kappa(G_0)=\frac{1+(d-1)|c|}{1-(d-1)|c|}.
\]
Here \(\kappa(G_0)\) means the ratio of the largest to smallest eigenvalues, hence the squared condition number of the restriction synthesis map.

For \(b\ne0\), set
\[
N=\frac{m^d-e}{q},\qquad C=\frac{m^{d-1}+e}{q},\qquad N=mC-e.
\]
For \(\sigma=\pm1\), let
\[
(u_+,u_-)=\begin{cases}
((q-3)/2,(q-3)/2),&q\text{ odd},\\
((q-4)/2,(q-2)/2),&q\text{ even}.
\end{cases}
\]
The spectrum consists precisely of
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
\frac{m[C+(d-1)e\sigma]}N&u_\sigma\quad(\sigma=\pm1)\\
\frac{m(C-e\sigma)}N&(d-1)u_\sigma\quad(\sigma=\pm1)\\
\frac{m(C-e)}N&d-1
\end{array}
\]
and the two eigenvalues (counting multiplicity) of the **explicit symmetric matrix**
\[
B=\begin{pmatrix}
1&-e\sqrt{d(m-1)}/N\\
-e\sqrt{d(m-1)}/N&[mC+e(d-m)]/N
\end{pmatrix}.
\]
Equivalently, with \(\alpha=[mC+e(d-m)]/N\), the final two eigenvalues are
\[
\frac{1+\alpha\pm\sqrt{(1-\alpha)^2+4d(m-1)/N^2}}2.
\]
Every eigenvalue in this inhomogeneous spectrum is strictly positive **except** when \((q,d)=(3,3)\), where the nullity is exactly one. In particular changing the hyperplane level from zero to nonzero **restores linear independence** at \((q,d)=(3,4)\) and \((4,3)\). For fixed \(q\) all eigenvalues converge uniformly to \(1\) as \(d\to\infty\), with deviation \(O_q(d/(q-1)^{d-1})\).

## Assumptions and scope
The finite field order \(q\) is any prime power, including powers of two. The coefficients \(a_i\) are all nonzero; neither the characteristic nor the dimension is otherwise restricted beyond \(q,d\ge3\). Multiplicative characters are the complete orthonormal character family on \(\mathbb F_q^\times\); the trivial character is used only once, as the global constant. Each matrix entry is the \(L^2\) inner product on \(X_b(a)\) normalized by its cardinality. Character phases and coefficient rescalings are unitary changes of basis. These are spectra for **linear restriction of a Fourier interaction band**, not Fourier extension operator bounds for arbitrary nonlinear or higher-band functions.

## Proof
**1. Normalize and count.** Replace \(a_ix_i\) by \(y_i\), then, if \(b\ne0\), divide every \(y_i\) by \(b\). This multiplies the character columns by unimodular constants, so the Gram spectrum is unchanged. With \(m=q-1\), let \(A_r(v)\) count \(r\)-tuples in \((\mathbb F_q^\times)^r\) summing to \(v\). Orthogonality of additive characters gives, for all integers \(r\ge1\),
\[
A_r(0)=\frac{m^r+m(-1)^r}{q},\qquad
A_r(v)=\frac{m^r-(-1)^r}{q}\quad(v\ne0).
\]
In particular the sets are nonempty, and their cardinalities are exactly \(N_0\) or \(N\) as above.

**2. The homogeneous matrix.** At \(b=0\), scaling all coordinates by any \(t\in\mathbb F_q^\times\) proves that each coordinate marginal is uniform. Thus the constant is orthogonal to every nontrivial coordinate character and a fixed coordinate has identity character Gram. For \(i\ne j\), condition on \(x_i=u,x_j=v\). By the formula above the number of completions equals
\[
\frac{m^{d-2}-e}{q}+e\mathbf1_{\{u+v=0\}}.
\]
The constant part vanishes after pairing against nontrivial characters. The exceptional term gives the cross block \(c\chi(-1)\) when the character labels agree and zero otherwise. Thus for each nontrivial \(\chi\) the \(d\)-by-\(d\) block is
\[
(1-c\chi(-1))I_d+c\chi(-1)\mathbf1\mathbf1^*.
\]
Its symmetric eigenvector and its \(d-1\) orthogonal contrasts yield the displayed eigenvalues. The character parity counts are \(r_\pm\). Checking when these explicit eigenvalues vanish gives exactly the three homogeneous exceptional pairs. To see this without asymptotic assumptions, in odd dimension \(|c|=q/(m^{d-1}-1)\), and in even dimension \(|c|=q/(m^{d-1}+1)\). The possible vanishing conditions are \((d-1)q=m^{d-1}\mp1\) or \(q=m^{d-1}\mp1\), subject to presence of the corresponding parity. Directly at \(d=3,4\) and then by strict growth of \(m^{d-1}\) compared with \(d-1\) for \(d\ge5\), they occur only in the stated cases. For odd \(q\ge5\), both parities occur and the extreme eigenvalues are \(1\pm(d-1)|c|\), giving the condition number formula.

**3. The nonzero-level operator.** Normalize \(b=1\). Let \(S=\mathbb F_q^\times\), equip its functions with uniform probability inner product, let \(W\) be the mean-zero subspace, and denote orthogonal projection onto \(W\) by \(P_W\). The full interaction band is unitarily \(\mathbb C\oplus W^d\). Counting coordinate completions gives
\[
\#\{x\in X_1:x_i=u\}=C-e\mathbf1_{\{u=1\}},
\]
and for \(i\ne j\) the pair completion count is a constant plus \(e\mathbf1_{\{u+v=1\}}\). Hence the constant-to-\(W\) coupling is \(-ef(1)/N\) per coordinate, each diagonal coordinate operator is \((m/N)P_W(CI-e\operatorname{diag}\mathbf1_{\{u=1\}})P_W\), and each off-diagonal operator is \((me/N)P_WRP_W\), where \(R\) maps a function supported away from \(1\) by \((Rf)(u)=f(1-u)\) for \(u\ne1\), with value zero at \(1\).

Let \(\eta=(m\mathbf1_{\{u=1\}}-1)/\sqrt{m-1}\) (a unit vector in \(W\)), and set \(U=\{f\in W:f(1)=0\}\). Then \(W=\mathbb C\eta\oplus U\), \(\dim U=q-3\). The reflection \(u\mapsto1-u\) permutes \(S\setminus\{1\}\); its plus/minus eigenspaces on \(U\) have exactly dimensions \(u_\pm\) specified above. In odd characteristic there is one fixed point \(u=1/2\), in even characteristic none. On \(U\), the coordinate-diagonal operator is \(mC/N\) and off-diagonal operator is \(meR/N\). Symmetric and contrast combinations across the \(d\) coordinates give both \(\sigma\)-families.

On \(\mathbb C\eta\), direct calculation yields diagonal entry \([mC-e(m-1)]/N\), off-diagonal entry \(e/N\), and constant coupling \(-e\sqrt{m-1}/N\). Coordinate contrasts therefore have eigenvalue \(m(C-e)/N\) with multiplicity \(d-1\); the symmetric coordinate direction coupled to the constant has precisely the matrix \(B\). These invariant, mutually orthogonal subspaces exhaust the \(1+d(q-2)\) dimensions and prove the full spectrum, including algebraic multiplicities and all zeros.

**4. Rank and equality cases.** Every \(U\)-eigenvalue and every distinguished coordinate contrast is positive whenever its stated multiplicity is nonzero: the only possible boundary tests \(C=d-1\) at \((q,d)=(3,4),(4,3)\) occur in absent \(U\)-parities, and all remaining cases have \(C>d-1\) or the other sign is strictly positive. For the remaining \(2\)-by-\(2\) block, direct expansion gives the exact determinant
\[
\det B=\frac{m}{N^2}\bigl[mC^2+eC(d-m-1)-(d-1)\bigr].
\]
For \(d=3\), one has \(e=-1\) and \(C=m-1\); the bracket is \((m-1)(m^2-2)-2\), equal to zero at \(m=2\) and strictly positive for \(m\ge3\). For \(d\ge4\), one has \(C\ge d-1\): at \(d=4\), \(C=m^2-m+1\ge3\); at \(d\ge5\), the bound \(C\ge(m^{d-1}-1)/(m+1)\ge d-1\) holds for \(m\ge2\), by elementary monotonicity in \(m\) and induction on \(d\). Moreover \(m(d-1)-|d-m-1|>1\) whenever \(m\ge2,d\ge4\). Therefore
\[
mC^2+eC(d-m-1)-(d-1)\ \ge\ C\bigl(mC-|d-m-1|\bigr)-(d-1)>0.
\]
Since the leading principal entry of \(B\) is \(1\), its two eigenvalues are positive for all \(d\ge4\) and for \(d=3,m\ge3\). For \(d=3,m=2\), \(B\) has rank one and hence exactly one zero eigenvalue. This proves the complete exceptional rank list without relying on finite enumeration. The explicit spectra also establish the uniform fixed-field asymptotic.

## Verification
The accompanying `verification/verify_spectra.py` (Python 3, NumPy) independently enumerates the actual finite-field point sets and their coordinate-character Gram matrices, including \(\mathbb F_4\) with polynomial arithmetic, and compares their entire eigenvalue multisets with these formulas. Its stored output records **44 exact cardinality checks and 44 complete matrix-spectrum comparisons** over \(q\in\{3,4,5,7,11\}\), \(3\le d\le10\) as computationally feasible, and both \(b=0\) and \(b=1\). The maximum absolute eigenvalue discrepancy is below \(7\cdot10^{-15}\), with all exceptional nullities reproduced. These finite enumerations are independent corroboration; the all-prime-power, all-dimension assertion follows from the character-counting and block-diagonalization proof, not from experiments.

## Relationship to prior work
Multiplicative-character orthogonality and Jacobi-sum identities are classical and are not claimed new. Rojas-León's work [1] studies generalized Jacobi sums and their estimates over finite-field affine subspaces, but does not give the exact combined Gram spectra of the constant and complete first-coordinate multiplicative character band, nor its sharp homogeneous/nonzero-level rank transitions. Koh [2] develops additive Fourier restriction on a different family of finite-field flat quadratic disks; neither its object nor its operator gives these spectra. The new claim is the **complete joint spectral decomposition and all exceptional rank/conditioning statements for the toric hyperplane family**, not the standard character-counting identity. These comparisons are best-knowledge rather than a certification that no older equivalent character-sum matrix computation exists.

## Limitations
These are normalized finite-dimensional **linear sampling** results, not universal phase retrieval, arbitrary interaction degree, or Fourier extension bounds in all \(L^p\) spaces. The nonzero-coefficient hypothesis on each \(a_i\) is essential to the stated uniform coordinate model. For fixed field size the estimates are asymptotic in dimension with constants depending on the field. A potentially unindexed equivalent in classical Jacobi-sum matrices or association schemes remains a bibliographic originality risk.

## References
[1] A. Rojas-León, *On a generalization of Jacobi sums*, first version June 9, 2021, arXiv:2106.05339v1, https://arxiv.org/abs/2106.05339 .

[2] D. Koh, *Restriction estimates for the flat disks over finite fields*, first version August 16, 2022, arXiv:2208.07784v1, https://arxiv.org/abs/2208.07784 .
