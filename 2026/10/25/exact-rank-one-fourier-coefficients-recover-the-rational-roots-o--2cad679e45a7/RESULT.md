# Exact rank-one Fourier coefficients recover the rational roots of squarefree matrix characteristic polynomials

## Finding
Let \(q\) be a prime power, \(n\ge2\), and \(f\in\mathbb F_q[X]\) a monic squarefree polynomial of degree \(n\). Write \(V_f=\{M\in M_n(\mathbb F_q):\det(XI-M)=f(X)\}\), \(S=|V_f|\), \(R=\{\lambda\in\mathbb F_q:f(\lambda)=0\}\), and \(s=|R|\). Fix a nontrivial additive character \(\psi\) of \(\mathbb F_q\). For nonzero \(u,v\in\mathbb F_q^n\), put \(A=uv^{\mathsf T}\), \(c=v^{\mathsf T}u\), and
\[
\widehat{1_{V_f}}(A)=\sum_{M\in V_f}\psi(\operatorname{tr}(AM)).
\]
Then the exact coefficients are
\[
\widehat{1_{V_f}}(A)=\begin{cases}
\displaystyle\frac{S(q-1)}{q^n-1}\sum_{\lambda\in R}\psi(c\lambda),&c\ne0,\\[5pt]
\displaystyle\frac{S}{q^{n-1}-1}\left(\frac{q^{n-1}(q-1)}{q^n-1}s-1\right),&c=0.
\end{cases}
\]
In particular, all nonzero rank-one Fourier coefficients are determined by the rational-root set of \(f\), and conversely the complete rank-one Fourier profile determines that set explicitly.

## Assumptions and scope
The field \(\mathbb F_q\) may have any characteristic, including two. The polynomial \(f\) must be monic, squarefree, and of degree at least two. There is no requirement that \(f\) split or have a rational root. The Fourier pairing is \(\operatorname{tr}(AM)\); using \(\operatorname{tr}(A^{\mathsf T}M)\) simply transposes the frequency matrix. A rank-one matrix has \(u\ne0\) and \(v\ne0\). All Fourier sums are unnormalized.

The reconstruction is as follows. Choose a rank-one matrix \(A_c\) with \(\operatorname{tr}(A_c)=c\) for each \(c\in\mathbb F_q^\times\), and any rank-one traceless matrix \(A_0\). Such matrices exist for \(n\ge2\). Define
\[
T(c)=\frac{q^n-1}{S(q-1)}\widehat{1_{V_f}}(A_c)\quad(c\ne0),\qquad
s=\frac{q^n-1}{q^{n-1}(q-1)}\left(1+\frac{q^{n-1}-1}{S}\widehat{1_{V_f}}(A_0)\right),\qquad T(0)=s.
\]
Then every rational-root indicator has the inversion formula
\[
\boldsymbol{1}_{f(r)=0}=\frac1q\sum_{c\in\mathbb F_q}T(c)\psi(-cr),\qquad r\in\mathbb F_q.
\]

## Proof
The fixed-characteristic-polynomial set \(V_f\) is invariant under conjugation. Fix \(u\ne0\). For \(w\in\mathbb F_q^n\), let \(N_w=\#\{M\in V_f:Mu=w\}\). The stabilizer of \(u\) in \(\mathrm{GL}_n(\mathbb F_q)\) acts transitively on \(\mathbb F_q^n\setminus\mathbb F_q u\), so all \(N_w\) outside the line \(\mathbb F_q u\) have one common value \(t\).

For \(\lambda\in\mathbb F_q\), conjugation also shows that the number of matrices with \(Mu=\lambda u\) is independent of the particular nonzero vector \(u\). Because \(f\) is squarefree, each matrix in \(V_f\) has a one-dimensional \(\lambda\)-eigenspace over \(\mathbb F_q\) when \(f(\lambda)=0\), and no \(\lambda\)-eigenvectors otherwise. Double-counting pairs \((M,u)\) with \(M\in V_f\), \(u\ne0\), and \(Mu=\lambda u\), gives
\[
N_{\lambda u}=\begin{cases}k:=S\frac{q-1}{q^n-1},&\lambda\in R,\\0,&\lambda\notin R.\end{cases}
\]
Counting every image \(Mu\) gives \(S=sk+(q^n-q)t\), hence \(t=(S-sk)/(q^n-q)\). All these divisions are legitimate because \(q\ge2\) and \(n\ge2\).

For \(A=uv^{\mathsf T}\), cyclicity of trace gives \(\operatorname{tr}(AM)=v^{\mathsf T}Mu\). Therefore
\[
\widehat{1_{V_f}}(A)=k\sum_{\lambda\in R}\psi(c\lambda)+t\sum_{w\notin\mathbb F_q u}\psi(v^{\mathsf T}w).
\]
The complete sum over \(\mathbb F_q^n\) vanishes because \(v\ne0\) and \(\psi\) is nontrivial. The line sum is \(\sum_{\lambda\in\mathbb F_q}\psi(c\lambda)\), which is zero for \(c\ne0\), and \(q\) for \(c=0\). Thus the outside-line sum is zero when \(c\ne0\) and \(-q\) when \(c=0\). Substituting \(k\) and \(t\) yields the displayed formulas, including the simplification
\[
ks-qt=\frac{S}{q^{n-1}-1}\left(\frac{q^{n-1}(q-1)}{q^n-1}s-1\right).
\]
The first formula shows \(T(c)=\sum_{\lambda\in R}\psi(c\lambda)\) for \(c\ne0\); the second yields \(s=T(0)\). Orthogonality of additive characters now proves the stated Fourier inversion identity for every \(r\in\mathbb F_q\).

## Verification
The standalone script `check_rankone.py` enumerates every squarefree monic characteristic-polynomial fibre and all nonzero rank-one probes \(e_1v^{\mathsf T}\) over three small prime-field matrix families: \((q,n)=(2,3),(3,2),(5,2)\). Character values are compared exactly in the cyclotomic integer ring, not by floating-point approximation. It checks 4, 6, and 20 fibres, respectively, and 556 fibre/probe pairs in total. The completed execution prints `CERTIFICATE_OK total_probes=556`. The script checks examples only; the proof above establishes the general theorem for every prime power and dimension.

## Relationship to prior work
Browning, Gundlach, and Sawin, *Counting matrices with given characteristic polynomial*, arXiv:2610.18226v1 (first public version dated 2026-10-13), study additive Fourier coefficients of these matrix fibres in connection with counting over local and global fields. Their Section 3 provides general bounds on the Fourier coefficients; those bounds do not determine the exact rank-one coefficients or recover rational roots. Their trace pairing may be written with a transposed frequency matrix, which is equivalent to ours. Standard conjugacy-class counting supplies background on squarefree characteristic polynomials; the argument here instead isolates the exact first-vector distribution and deduces the complete rank-one profile and inversion.

## Limitations
Only squarefree characteristic polynomials and rank-one nonzero frequencies are treated. No assertion is made about exact coefficients for higher-rank frequencies, or about arbitrary nonsquarefree fibres. Independent mathematical validation has not been performed. The search of accessible related literature did not identify an equivalent exact formula, but implicit coverage in general orbital-Fourier or finite-field character-sum literature remains a risk.

## References
1. T. Browning, J. Gundlach, W. Sawin, *Counting matrices with given characteristic polynomial*, arXiv:2610.18226v1 (2026-10-13), especially Section 3. https://arxiv.org/abs/2610.18226
2. J. R. Britnell, *Cyclic, Separable and Semisimple Matrices in the Special Linear Groups Over a Finite Field* (2002), for context on finite-field semisimple matrix counting; its abstract was consulted, not its full text.
