# Dimension-threshold classification of weighted block identities

## Statement

Let \(1\le p<q\le\infty\), with \(1/\infty=0\). Let \((E_n)_{n\ge1}\) be non-zero finite-dimensional Banach spaces. Put
\[
X_p=\Big(\bigoplus_{n=1}^\infty E_n\Big)_p,
\]
and let \(X_q=(\bigoplus E_n)_q\) when \(q<\infty\), while for \(q=\infty\) let \(X_\infty=(\bigoplus E_n)_{c_0}\).

For a bounded scalar sequence \(\lambda=(\lambda_n)\), define the weighted block identity
\[
D_\lambda:X_p\to X_q,\qquad D_\lambda(x_n)=(\lambda_nx_n).
\]
For \(t>0\), define the high-weight dimension profile
\[
d_\lambda(t)=\sup\{\dim E_n:\ |\lambda_n|\ge t\},
\]
with the supremum of the empty set equal to \(0\).

Then:

1. \(D_\lambda\) is always strictly singular.
2. \(D_\lambda\) is finitely strictly singular if and only if
   \[
   d_\lambda(t)<\infty\qquad\text{for every }t>0.
   \]
3. \(D_\lambda\) is compact if and only if \(\lambda_n\to0\).

Consequently the three regimes inside this natural class are completely separated by two elementary profiles:

- compact: \(\lambda_n\to0\);
- finitely strictly singular but non-compact: \(\lambda_n\not\to0\), while every positive weight level occurs only on blocks of uniformly bounded dimension;
- strictly singular but not finitely strictly singular: some positive weight level occurs on blocks of unbounded dimension.

A quantitative version is also available. Write
\[
\alpha=\frac1p-\frac1q>0,\qquad M=\sup_n|\lambda_n|,
\]
and let \(b_m(T)\) denote the \(m\)-th Bernstein number. If
\[
h_m=\sup\{|\lambda_n|:\dim E_n\ge m\},
\]
then
\[
b_m(D_\lambda)\ge h_m.
\]
Moreover, whenever \(d_\lambda(t)<\infty\),
\[
b_m(D_\lambda)
\le t+M\,d_\lambda(t)^{\,1+\alpha}m^{-\alpha}.
\]
Thus, under the finite-strict-singularity criterion,
\[
b_m(D_\lambda)\le
\inf_{t>0}\left[t+M\,d_\lambda(t)^{\,1+\alpha}m^{-\alpha}\right],
\]
where terms with \(d_\lambda(t)=\infty\) are ignored.

## Proof

### 1. The unweighted block identity is strictly singular

Let
\[
J:X_p\to X_q,\qquad J(x_n)=(x_n).
\]
Clearly \(\|J\|\le1\). Suppose that \(J\) were bounded below by a constant \(c>0\) on an infinite-dimensional subspace \(M\subset X_p\).

Let \(P_N\) be the projection onto the first \(N\) blocks. Since \(P_N\) has finite rank, a standard gliding-hump argument gives unit vectors \(x_k\in M\) and finitely supported vectors \(u_k\) with successive, pairwise disjoint block supports such that
\[
\sum_{k=1}^\infty\|x_k-u_k\|_{X_p}<1.
\]
In particular \(\|u_k\|_{X_p}\to1\). For \(S_m=\sum_{k=1}^m x_k\),
\[
\|S_m\|_{X_p}
\ge
\left(\sum_{k=1}^m\|u_k\|_{X_p}^p\right)^{1/p}
-\sum_{k=1}^m\|x_k-u_k\|_{X_p},
\]
so the left side grows on the order of \(m^{1/p}\).

On the other hand, disjoint block supports and \(\|Ju_k\|_{X_q}\le\|u_k\|_{X_p}\) give, for \(q<\infty\),
\[
\|JS_m\|_{X_q}
\le
\left(\sum_{k=1}^m\|u_k\|_{X_p}^q\right)^{1/q}
+\sum_{k=1}^m\|x_k-u_k\|_{X_p},
\]
which grows at most on the order of \(m^{1/q}\). For \(q=\infty\) the corresponding first term is \(\max_{k\le m}\|u_k\|_{X_p}\), hence is bounded. This contradicts
\[
\|JS_m\|_{X_q}\ge c\|S_m\|_{X_p},
\]
because \(1/p>1/q\). Hence \(J\) is strictly singular.

Now \(D_\lambda=M_\lambda J\), where \(M_\lambda\) is the bounded coordinate multiplier on \(X_q\). Since strictly singular operators form an operator ideal, \(D_\lambda\) is strictly singular.

### 2. Necessity of the dimension-threshold condition for finite strict singularity

Assume that \(d_\lambda(t)=\infty\) for some \(t>0\). For every \(m\) there is an index \(n\) with \(\dim E_n\ge m\) and \(|\lambda_n|\ge t\). Choose any \(m\)-dimensional subspace \(F\subset E_n\). For every \(x\in F\),
\[
\|D_\lambda x\|_{X_q}=|\lambda_n|\,\|x\|_{X_p}\ge t\|x\|_{X_p}.
\]
Therefore \(b_m(D_\lambda)\ge t\) for all \(m\), so \(D_\lambda\) is not finitely strictly singular. The same argument gives the sharper lower bound
\[
b_m(D_\lambda)\ge h_m.
\]

### 3. Uniformly bounded block dimensions force finite strict singularity

Fix a set \(A\subset\mathbb N\) for which
\[
d:=\sup_{n\in A}\dim E_n<\infty.
\]
Let \(J_A\) be the unweighted block identity restricted to the blocks in \(A\).

For every \(n\in A\), choose an Auerbach basis
\[
(e_{n,j},e^*_{n,j})_{j=1}^{d_n},\qquad d_n=\dim E_n,
\]
so \(\|e_{n,j}\|=\|e^*_{n,j}\|=1\). Define the coordinate map
\[
A_0:\Big(\bigoplus_{n\in A}E_n\Big)_p\longrightarrow \ell_p(\{(n,j)\})
\]
by \(A_0x=(e^*_{n,j}(x_n))\). Then
\[
\|A_0\|\le d^{1/p}.
\]
Define the reconstruction map
\[
B_0:\ell_q(\{(n,j)\})\longrightarrow
\Big(\bigoplus_{n\in A}E_n\Big)_q
\]
blockwise by
\[
B_0(a_{n,j})_n=\sum_{j=1}^{d_n}a_{n,j}e_{n,j}.
\]
For \(q<\infty\),
\[
\|B_0\|\le d^{1-1/q},
\]
and for \(q=\infty\) the same formula gives \(\|B_0\|\le d\). Thus in both cases, with \(1/q=0\) for \(q=\infty\),
\[
J_A=B_0 I_{p,q} A_0,
\]
where \(I_{p,q}:\ell_p\to\ell_q\) (or \(c_0\) for \(q=\infty\)) is the scalar formal inclusion.

The classical Bernstein-number formula
\[
b_m(I_{p,q})=m^{1/q-1/p}=m^{-\alpha}
\]
therefore yields, by the ideal property of Bernstein numbers,
\[
b_m(J_A)\le d^{1+\alpha}m^{-\alpha}.
\]
In particular \(J_A\) is finitely strictly singular.

Now fix \(t>0\) with \(d_\lambda(t)<\infty\). Split
\[
D_\lambda=H_t+L_t,
\]
where \(H_t\) retains the blocks with \(|\lambda_n|\ge t\), and \(L_t\) retains the remaining blocks. The previous paragraph and bounded multiplication give
\[
b_m(H_t)\le M\,d_\lambda(t)^{1+\alpha}m^{-\alpha},
\]
while
\[
\|L_t\|\le t.
\]
Using \(b_m(S+T)\le b_m(S)+\|T\|\),
\[
b_m(D_\lambda)
\le
t+M\,d_\lambda(t)^{1+\alpha}m^{-\alpha}.
\]
If \(d_\lambda(t)<\infty\) for every \(t>0\), first choose \(t\) small and then \(m\) large; this forces \(b_m(D_\lambda)\to0\). Hence \(D_\lambda\) is finitely strictly singular.

### 4. Compactness

If \(\lambda_n\to0\), truncate \(D_\lambda\) after the first \(N\) blocks. The truncation has finite rank because each \(E_n\) is finite-dimensional, and the norm of the tail is
\[
\sup_{n>N}|\lambda_n|\to0.
\]
Hence \(D_\lambda\) is compact.

Conversely, suppose \(\lambda_n\not\to0\). Then some \(\varepsilon>0\) and distinct indices \(n_k\) satisfy \(|\lambda_{n_k}|\ge\varepsilon\). Choose unit vectors \(x_k\in E_{n_k}\). The vectors \(D_\lambda x_k\) have disjoint block supports and are uniformly separated in \(X_q\), so the image of the unit ball is not relatively compact. Thus \(D_\lambda\) is not compact.

This proves the classification.

## Relation to known results

The scalar case \(\dim E_n=1\) reduces to the classical formal inclusion \(\ell_p\hookrightarrow\ell_q\), which is finitely strictly singular but non-compact. Milman's 1970 work introduced superstrict/finitely strict singularity and supplied classical examples separating finite strict singularity from strict singularity. Later accounts of the \(\ell_p\)-to-\(\ell_q\) ideal structure explicitly describe Milman's formal inclusion as finitely strictly singular and his finite-dimensional Hilbert-block construction as a strictly singular operator that is not finitely strictly singular.

The theorem above turns those two opposite examples into one exact dimension-threshold criterion for arbitrary finite-dimensional Banach blocks and arbitrary bounded block weights. The 2025 review by Edmunds and Lang and the 2025 work of Lang and Nekvinda give modern Bernstein-number criteria for scalar and structured sequence-space embeddings; no equivalent arbitrary-Banach-block threshold classification was located in the searches listed below.

## Originality and limitations

Originality is claimed **to the best of our knowledge** for the complete weighted-block classification and the displayed Bernstein upper envelope, not for the scalar formal inclusion, Milman's separation examples, the definition of finite strict singularity, or the scalar Bernstein formula.

Searches covered the terms “finitely strictly singular”, “superstrictly singular”, “weighted block”, “block diagonal”, “direct sum”, “formal identity”, “Bernstein numbers”, finite-dimensional blocks, synonymous formulations, and modern sequence-space embedding results. No source found stated the criterion
\[
D_\lambda\in\mathcal{FSS}
\iff
\sup\{\dim E_n:|\lambda_n|\ge t\}<\infty\quad\forall t>0
\]
for arbitrary finite-dimensional Banach blocks.

Residual literature risk remains. Milman's 1970 Russian paper was not inspected in full, and Pietsch's 1978 *Operator Ideals* was not exhaustively checked. Either could contain an equivalent block formulation under older terminology. Schlumprecht's 2012 paper and later literature confirm the relevant classical Milman examples, but this does not eliminate that residual risk.

## References

- V. D. Milman, “Operators of class \(C_0\) and \(C_0^*\)” (Russian), *Teor. Funkcii Funkcional. Anal. i Priložen.* 10 (1970), 15–26. Bibliographic reference reproduced in later operator-ideal literature.
- Th. Schlumprecht, “On the closed subideals of \(L(\ell_p\oplus\ell_q)\),” *Operators and Matrices* 6 (2012), 311–326. https://doi.org/10.7153/oam-06-22
- D. E. Edmunds and J. Lang, “Notes on Non-Compact Maps and the Importance of Bernstein Numbers,” *Advances in Operator Theory* 10 (2025), article 95; arXiv:2503.19600. https://arxiv.org/abs/2503.19600
- J. Lang and A. Nekvinda, “Embeddings between sequence variable Lebesgue spaces, strict and finitely strict singularity,” *Mathematische Nachrichten* 298 (2025), 2926–2941. https://doi.org/10.1002/mana.12031
- D. L. Fernandez, M. Mastyło, and E. B. Silva, “Pietsch’s variants of s-numbers for multilinear operators,” *Rev. Real Acad. Cienc. Exactas Fís. Nat. Ser. A-Mat.* 115 (2021), 189. https://doi.org/10.1007/s13398-021-01123-2
