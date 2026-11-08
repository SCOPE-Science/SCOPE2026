# Normalized rank-one Fourier coefficients of squarefree matrix-characteristic-polynomial fibres

## Finding
Let \(q\) be a prime power, \(n\ge2\), and \(f\in\mathbb F_q[X]\) a monic squarefree polynomial of degree \(n\). Let
\[
 V_f=\{M\in M_n(\mathbb F_q):\det(XI-M)=f(X)\},\quad S=|V_f|,\quad R=\{\lambda\in\mathbb F_q:f(\lambda)=0\},\quad s=|R|.
\]
Fix a nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C^\times\). For \(u,v\in\mathbb F_q^n\setminus\{0\}\), write \(A=uv^{\mathsf T}\) and \(c=\operatorname{tr}(A)=v^{\mathsf T}u\). With the **unnormalized** transform \(\widehat{1_{V_f}}(A)=\sum_{M\in V_f}\psi(\operatorname{tr}(AM))\), one has
\[
 \widehat{1_{V_f}}(A)=
 \begin{cases}
 \displaystyle\frac{S(q-1)}{q^n-1}\sum_{\lambda\in R}\psi(c\lambda),&c\ne0,\\[5pt]
 \displaystyle\frac{S}{q^{n-1}-1}\left(\frac{q^{n-1}(q-1)}{q^n-1}s-1\right),&c=0.
 \end{cases}
\]
Thus the **normalized** rank-one profile \(S^{-1}\widehat{1_{V_f}}\), for fixed \(q,n,\psi\), is completely determined by the rational-root set \(R\). The **unnormalized** profile depends on both \(R\) and the fibre size \(S\), which in general is not determined by \(R\).

The size \(S\) is computable from the complete irreducible factorization \(f=\prod_i f_i\) (distinct monic irreducibles, \(d_i=\deg f_i\)):
\[
 S=\frac{|\operatorname{GL}_n(\mathbb F_q)|}{\prod_i(q^{d_i}-1)}.
\]
Given \(S\) and the rank-one coefficients, the set \(R\) can be reconstructed exactly as follows. For every \(c\in\mathbb F_q^\times\) select a rank-one \(A_c\) of trace \(c\), and select a rank-one \(A_0\) of trace zero. Such matrices exist for \(n\ge2\). Set
\[
 T(c)=\frac{q^n-1}{S(q-1)}\widehat{1_{V_f}}(A_c)\quad(c\ne0),\qquad
 T(0)=s=\frac{q^n-1}{q^{n-1}(q-1)}\left(1+\frac{q^{n-1}-1}{S}\widehat{1_{V_f}}(A_0)\right).
\]
Then for every \(r\in\mathbb F_q\),
\[
 \boldsymbol1_{f(r)=0}=\frac1q\sum_{c\in\mathbb F_q}T(c)\psi(-cr).
\]
These statements hold for every finite field, including characteristic two, without a splitting or rational-root assumption.

## Scope and essential normalization distinction
The two Fourier formulas use rank-one nonzero frequencies, \(\operatorname{tr}(AM)\) rather than \(\operatorname{tr}(A^{\mathsf T}M)\), and the *unnormalized* sum on \(V_f\). Transposing \(A\) converts between those pairings. The inverse formula uses the known fibre size \(S\) (or equivalently the normalized Fourier data), and does not claim that unnormalized coefficients are functions of \(R\) alone.

For example, over \(\mathbb F_2\) at \(n=5\), both
\[
 f_1=X^5+X^2+1,\qquad f_2=(X^2+X+1)(X^3+X+1)
\]
are monic squarefree and have \(R=\varnothing\). The first is irreducible of degree five; the second has irreducible factors of degrees two and three. Their fibre sizes are \(|\operatorname{GL}_5(\mathbb F_2)|/31=322560\) and \(|\operatorname{GL}_5(\mathbb F_2)|/21=476160\), respectively. At any rank-one trace-zero frequency, the unnormalized transforms are \(-21504\) and \(-31744\). This demonstrates why \(S\) is indispensable before normalization. Both normalized values equal \(-1/15\).

## Proof
**1. Conjugacy and the fibre size.** A squarefree characteristic polynomial has a single rational canonical form: every matrix in \(V_f\) is conjugate to the companion matrix of \(f\). Its centralizer's unit group is \((\mathbb F_q[X]/(f))^\times\cong\prod_i\mathbb F_{q^{d_i}}^\times\), giving the displayed value of \(S\).

**2. The image of one nonzero vector.** Fix \(u\ne0\), and define \(N_w=\#\{M\in V_f:Mu=w\}\). Conjugation by the subgroup of \(\operatorname{GL}_n\) fixing \(u\) is transitive on \(\mathbb F_q^n\setminus\mathbb F_qu\), so \(N_w\) is a common number \(t\) there. The value \(N_{\lambda u}\) does not depend on the chosen nonzero \(u\). For \(\lambda\in R\), squarefreeness makes the \(\lambda\)-eigenspace of each \(M\in V_f\) one-dimensional over \(\mathbb F_q\), with exactly \(q-1\) nonzero vectors. For \(\lambda\notin R\), no such eigenvectors exist. Double-counting \((M,u)\) therefore gives
\[
 N_{\lambda u}=k\boldsymbol1_{\lambda\in R},\qquad k=\frac{S(q-1)}{q^n-1}.
\]
Since the possible values of \(Mu\) partition the fibre, \(S=sk+(q^n-q)t\) and hence \(t=(S-sk)/(q^n-q)\). Every denominator is nonzero for \(q\ge2,n\ge2\).

**3. Fourier coefficients.** Cyclicity of matrix trace gives \(\operatorname{tr}(uv^{\mathsf T}M)=v^{\mathsf T}Mu\), so
\[
 \widehat{1_{V_f}}(uv^{\mathsf T})=k\sum_{\lambda\in R}\psi(c\lambda)+t\sum_{w\notin\mathbb F_qu}\psi(v^{\mathsf T}w).
\]
Since \(v\ne0\), the complete sum over \(w\in\mathbb F_q^n\) is zero by additive-character orthogonality. Its restriction to the line \(\mathbb F_qu\) is zero when \(c\ne0\), and \(q\) when \(c=0\). Thus the off-line sum is respectively zero or \(-q\). Substitution yields the first formula or \(sk-qt\); the latter simplifies to the displayed second formula.

**4. Reconstruction.** For \(c\ne0\), normalization gives \(T(c)=\sum_{\lambda\in R}\psi(c\lambda)\); the trace-zero formula yields \(T(0)=s\). Hence the function \(c\mapsto T(c)\) is the finite-field Fourier transform of the indicator of \(R\). Fourier orthogonality gives the stated inverse formula. The construction uses no unproved computational extrapolation.

## Independent checks and limits
A bounded exact check can enumerate all squarefree characteristic-polynomial fibres and rank-one probes for small prime fields, but does not prove a statement for all prime powers. The unrestricted argument is the stabilizer/eigenvector count followed by character orthogonality. The result does not treat nonsquarefree fibres, higher-rank frequencies, or reconstruction of the entire factorization of \(f\). It claims only recovery of the *rational* roots, supplied with \(S\). The example above rules out any stronger claim that raw rank-one coefficients depend on \(R\) alone.

## Relation to existing literature
Browning, Gundlach and Sawin's *Counting matrices with given characteristic polynomial* (arXiv:2610.18226v1, 2026-10-13), Sections 3.1–3.3, develops general Fourier bounds for these characteristic-polynomial varieties, not the exact normalized rank-one formulas or root inversion established here. Its discussion of a unique squarefree conjugacy class is consistent with Step 1. Standard semisimple matrix/conjugacy-class counts provide \(S\), but recovering the additive rank-one profile still requires the image-distribution and character-sum calculation. Earlier orbital Fourier work may contain an equivalent specialization; this has not been exhaustively ruled out.

## References
1. T. Browning, F. Gundlach, W. Sawin, *Counting matrices with given characteristic polynomial*, arXiv:2610.18226v1 (2026-10-13), especially Section 3, https://arxiv.org/html/2610.18226v1.
2. J. R. Britnell, *Cyclic, Separable and Semisimple Matrices in the Special Linear Groups Over a Finite Field*, Journal of the London Mathematical Society 66 (2002), 605–622, DOI:10.1112/S0024610702003678 (background on semisimple classes; no assertion of whole-document exclusion).
