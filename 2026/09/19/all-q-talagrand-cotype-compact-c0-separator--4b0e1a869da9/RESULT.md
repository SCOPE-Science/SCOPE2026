# Compact cotype separators inside c0 at every finite exponent

## Result

Fix \(2\le q<\infty\). There exist a separable real Banach space \(X_q\), isometric to a closed subspace of \(c_0\), and a compact operator
\[
T_q:X_q\longrightarrow c_0
\]
such that
\[
\boxed{C_q^g(T_q)<\infty,\qquad \|T_q\|_{q,1}<\infty,\qquad C_q^r(T_q)=\infty.}
\]
Thus finite Gaussian cotype \(q\) together with finite \((q,1)\)-summing norm does not imply Rademacher cotype \(q\), even for a compact operator whose domain is a closed subspace of \(c_0\).

The finite-dimensional all-\(q\) separation used below is prior work: for dyadic dimensions there are Walsh--Hadamard blocks \(U_n:X_n\to\ell_\infty^n\) with
\[
\frac{C_q^r(U_n)}{\max\{C_q^g(U_n),\|U_n\|_{q,1}\}}\longrightarrow\infty
\]
for every fixed finite \(q\). The contribution here is the compact infinite-dimensional separator obtained from those blocks.

## Proof

For the fixed exponent \(q\), write
\[
M_n=\max\{C_q^g(U_n),\|U_n\|_{q,1}\}.
\]
Choose dyadic dimensions \(n_k\) so that
\[
\frac{C_q^r(U_{n_k})}{M_{n_k}}\ge\\(4^k\\),
\]
and set
\[
V_k=M_{n_k}^{-1}U_{n_k}.
\]
Then
\[
C_q^g(V_k)\le1,\qquad \|V_k\|_{q,1}\le1,\qquad C_q^r(V_k)\ge\\(4^k\\).
\]
Since the \((q,1)\)-summing norm dominates the operator norm, \(\|V_k\|\le1\).

Let
\[
X_q=\left(\bigoplus_{k\ge1}X_{n_k}\right)_{c_0},\qquad
Y=\left(\bigoplus_{k\ge1}\ell_\infty^{n_k}\right)_{c_0}\cong c_0,
\]
and define
\[
T_q(x_k)_k=(2^{-k}V_kx_k)_k.
\]
The finite block truncations converge to \(T_q\) in operator norm because \(\|V_k\|\le1\) and \(2^{-k}\to0\). Hence \(T_q\) is compact.

For a finite family \(x_i=(x_{i,k})_k\in X_q\),
\[
\sum_i\|T_qx_i\|^q
\le\sum_k2^{-kq}\sum_i\|V_kx_{i,k}\|^q.
\]
Applying the Gaussian cotype inequality blockwise and using the \(c_0\)-sum norm gives
\[
C_q^g(T_q)\le\left(\sum_k2^{-kq}\right)^{1/q}<\infty.
\]
The same blockwise estimate with the sign supremum gives
\[
\|T_q\|_{q,1}\le\left(\sum_k2^{-kq}\right)^{1/q}<\infty.
\]
On the other hand, testing only vectors supported in the \(k\)-th block yields
\[
C_q^r(T_q)\ge2^{-k}C_q^r(V_k)\ge\\(2^k\\)
\]
for every \(k\), hence \(C_q^r(T_q)=\infty\).

Finally, the Walsh--Hadamard block norm has the form
\[
\|x\|_{X_n}=\max\left\{\|x\|_\infty,\frac{\|H_nx\|_\infty}{s_n}\right\},
\]
so \(x\mapsto(x,H_nx/s_n)\) embeds \(X_n\) isometrically in \(\ell_\infty^{2n}\). Taking the \(c_0\)-sum of these finite-dimensional embeddings identifies \(X_q\) isometrically with a closed subspace of \(c_0\).

## Prior boundary

The negative operator-cotype example at \(q=2\) is due to Xinglong Wu. Before this record, a published result had already extended the same Walsh--Hadamard family to every finite \(q\), with the logarithmic quantitative separation needed above. A separate same-day result also removed the power-of-two restriction by a flat cosine transform. Those finite-dimensional statements are prior inputs, not contributions of this record.

Classical comparison theorems for \(C(K)\) and Banach-lattice domains remain compatible with the result: the domain here is only a closed subspace of \(c_0\), not a Banach lattice under an inherited coordinate order.

## Limitations

The construction is for real spaces and a fixed finite \(q\). It gives a separate compact operator for each \(q\), does not determine optimal constants, and does not locate the separator in a finer compact-operator ideal.

## References

1. X. Wu, *A Counterexample to Talagrand's Operator Cotype Problem*, arXiv:2609.19731 (2026).
2. *A single Walsh--Hadamard family separates operator cotype for every finite q*, 18 September 2026, https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-walsh-hadamard-operator-cotype-all-q--8d7e06d62b42
3. M. Junge, *Comparing gaussian and Rademacher cotype for operators on the space of continuous functions*, Studia Mathematica 118 (1996), 101--115, https://doi.org/10.4064/sm-118-2-101-115
4. M. Talagrand, *Cotype and (q,1)-summing norm in a Banach space*, Inventiones Mathematicae 110 (1992), 545--556, https://doi.org/10.1007/BF01231344
