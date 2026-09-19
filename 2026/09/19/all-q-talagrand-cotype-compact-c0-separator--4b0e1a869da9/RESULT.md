# All finite cotype exponents fail Talagrand's operator comparison, with compact separators inside \(c_0\)

## Statement

For a bounded operator \(U:X\to Y\) and \(2\le q<\infty\), write \(C_q^g(U)\) and \(C_q^r(U)\) for the Gaussian and Rademacher cotype-\(q\) constants, using first moments,
\[
\Big(\sum_i\|Ux_i\|^q\Big)^{1/q}
 \le C_q^g(U)\,\mathbb E\Big\|\sum_i g_i x_i\Big\|,
\qquad
\Big(\sum_i\|Ux_i\|^q\Big)^{1/q}
 \le C_q^r(U)\,\mathbb E\Big\|\sum_i \varepsilon_i x_i\Big\|,
\]
and let \(\|U\|_{q,1}\) be the least constant in
\[
\Big(\sum_i\|Ux_i\|^q\Big)^{1/q}
\le
\|U\|_{q,1}\max_{\eta_i=\pm1}\Big\|\sum_i\eta_i x_i\Big\|.
\]

Xinglong Wu recently constructed, for \(n=2^k\), the real Banach space
\[
X_n=\left(\mathbb R^n,\ 
\|x\|_{X_n}:=
\max\left\{\|x\|_\infty,\frac{\|H_nx\|_\infty}{s_n}\right\}\right),
\qquad
s_n=\sqrt{2\log(2n)},
\]
where \(H_n\) is the normalized Walsh--Hadamard matrix, and the identity map
\[
U_n:X_n\longrightarrow \ell_\infty^n,\qquad U_nx=x.
\]
Wu proves a logarithmic separation for \(q=2\). The same family in fact separates the three operator ideals at **every finite cotype exponent**.

### Theorem 1: all-\(q\) finite-dimensional gap

There is an absolute constant \(C\) such that, for every \(2\le q<\infty\) and every dyadic \(n\),
\[
\boxed{C_q^r(U_n)\ge \frac12 n^{1/q}},
\]
\[
\boxed{
C_q^g(U_n)\le
C\left(\frac{n}{\log(n+1)}\right)^{1/q}},
\]
and
\[
\boxed{
\|U_n\|_{q,1}
\le
n^{1/(2q)}(2\log(2n))^{1/(2q)} }.
\]
Consequently, for all sufficiently large dyadic \(n\),
\[
\boxed{
\frac{C_q^r(U_n)}
{\max\{C_q^g(U_n),\|U_n\|_{q,1}\}}
\ge
c\,(\log(n+1))^{1/q}},
\]
with an absolute \(c>0\). In particular, for every fixed \(2\le q<\infty\), there is no finite constant \(L_q\) such that
\[
C_q^r(U)
\le
L_q\max\{C_q^g(U),\|U\|_{q,1}\}
\]
for all bounded operators \(U\).

Thus the failure is not confined to the endpoint \(q=2\): every finite exponent fails separately.

### Theorem 2: a compact qualitative separator

For every fixed \(2\le q<\infty\), there exist a separable real Banach space \(X_q\), isometric to a closed subspace of \(c_0\), and a compact operator
\[
T_q:X_q\longrightarrow c_0
\]
such that
\[
\boxed{
C_q^g(T_q)<\infty,\qquad
\|T_q\|_{q,1}<\infty,\qquad
C_q^r(T_q)=\infty.}
\]
Hence finite Gaussian cotype \(q\) together with finite \((q,1)\)-summing norm does not even qualitatively imply Rademacher cotype \(q\), and the failure can occur for a compact operator between separable spaces with both domain and range sitting in \(c_0\).

For \(2<q<\infty\), this also marks a sharp structural boundary with Maurey's positive theorem for Banach-lattice domains: the Banach-lattice hypothesis cannot be replaced merely by "closed subspace of \(c_0\)."

## Proof of Theorem 1

Wu proves for the same \(X_n,U_n\) that
\[
\mathbb E\|\varepsilon\|_{X_n}\le 2
\]
for the sign vector \(\varepsilon=(\varepsilon_1,\ldots,\varepsilon_n)\), and that
\[
C_2^g(U_n)\le C_0\sqrt{\frac{n}{\log(n+1)}}.
\]
He also establishes the matrix estimates used below.

### Rademacher lower bound

Apply the definition of \(C_q^r(U_n)\) to the standard basis \(e_1,\ldots,e_n\). Since
\[
\|U_ne_j\|_\infty=1,
\]
the left side is \(n^{1/q}\), while
\[
\mathbb E\Big\|\sum_{j=1}^n\varepsilon_je_j\Big\|_{X_n}
=
\mathbb E\|\varepsilon\|_{X_n}
\le2.
\]
Therefore
\[
C_q^r(U_n)\ge \frac12n^{1/q}.
\]

### Gaussian upper bound

Let \(x_1,\ldots,x_m\in X_n\), set
\[
a_i=\|U_nx_i\|_\infty,
\qquad
G=\mathbb E\Big\|\sum_i g_ix_i\Big\|_{X_n}.
\]
For \(q\ge2\), interpolation between \(\ell_2\) and \(\ell_\infty\) gives
\[
\|(a_i)\|_{\ell_q}
\le
\|(a_i)\|_{\ell_2}^{2/q}
\|(a_i)\|_{\ell_\infty}^{1-2/q}.
\]
The \(q=2\) estimate yields
\[
\|(a_i)\|_{\ell_2}\le C_2^g(U_n)G.
\]
Also
\[
\max_i\|x_i\|_{X_n}
\le
\sqrt{\frac{\pi}{2}}\,G.
\]
Indeed, for each \(i\), choose a norming functional \(\phi_i\in B_{X_n^*}\). Then
\[
G\ge
\mathbb E\left|\sum_jg_j\phi_i(x_j)\right|
=
\sqrt{\frac2\pi}
\left(\sum_j|\phi_i(x_j)|^2\right)^{1/2}
\ge
\sqrt{\frac2\pi}\|x_i\|_{X_n}.
\]
Since \(\|U_n\|\le1\),
\[
\|(a_i)\|_{\ell_\infty}
\le
\max_i\|x_i\|_{X_n}
\le
\sqrt{\frac{\pi}{2}}\,G.
\]
Consequently,
\[
C_q^g(U_n)
\le
\big(C_2^g(U_n)\big)^{2/q}
\left(\sqrt{\frac{\pi}{2}}\right)^{1-2/q}
\le
C\left(\frac{n}{\log(n+1)}\right)^{1/q},
\]
where \(C\) may be chosen absolute.

### The \((q,1)\)-summing upper bound

For \(x_1,\ldots,x_m\in X_n\), write
\[
A=[x_1\ \cdots\ x_m]=(a_{ji}),
\qquad
H_nA=(c_{ji}),
\]
and set
\[
\alpha=\max_j\sum_i|a_{ji}|,
\qquad
\beta=\max_j\sum_i|c_{ji}|.
\]
Wu's exact sign formula is
\[
D:=
\max_{\eta_i=\pm1}
\Big\|\sum_i\eta_i x_i\Big\|_{X_n}
=
\max\left\{\alpha,\frac{\beta}{s_n}\right\}.
\]
If \(u_i=\|x_i\|_\infty\), then Wu's argument gives
\[
u_i\le\alpha,
\qquad
\sum_i u_i^2\le \sqrt n\,\alpha\beta.
\]
For \(q\ge2\),
\[
\sum_i u_i^q
\le
\alpha^{q-2}\sum_i u_i^2
\le
\sqrt n\,\alpha^{q-1}\beta.
\]
Taking \(q\)-th roots and using
\(\alpha\le D\), \(\beta\le s_nD\),
\[
\left(\sum_i\|U_nx_i\|_\infty^q\right)^{1/q}
\le
n^{1/(2q)}s_n^{1/q}D
=
n^{1/(2q)}(2\log(2n))^{1/(2q)}D.
\]
This proves the stated \((q,1)\)-summing estimate.

Finally,
\[
\frac{
n^{1/(2q)}(2\log(2n))^{1/(2q)}
}{
(n/\log(n+1))^{1/q}
}
=
\left(
\frac{\sqrt{2\log(2n)}\,\log(n+1)}
{\sqrt n}
\right)^{1/q},
\]
which is at most \(1\) for all sufficiently large \(n\), uniformly in \(q\ge2\). Combining the three estimates gives
\[
\frac{C_q^r(U_n)}
{\max\{C_q^g(U_n),\|U_n\|_{q,1}\}}
\gtrsim
(\log(n+1))^{1/q}.
\]

## Proof of Theorem 2

Fix \(2\le q<\infty\), and set
\[
M_n=
\max\{C_q^g(U_n),\|U_n\|_{q,1}\}.
\]
By Theorem 1,
\[
\frac{C_q^r(U_n)}{M_n}\longrightarrow\infty
\]
along dyadic \(n\). Choose dyadic \(n_k\) so that
\[
\frac{C_q^r(U_{n_k})}{M_{n_k}}\ge 4^k,
\]
and define
\[
V_k=M_{n_k}^{-1}U_{n_k}.
\]
Then
\[
C_q^g(V_k)\le1,\qquad
\|V_k\|_{q,1}\le1,\qquad
C_q^r(V_k)\ge4^k.
\]
Since the \((q,1)\)-summing norm dominates the operator norm,
\[
\|V_k\|\le1.
\]

Let
\[
X_q=\left(\bigoplus_{k\ge1}X_{n_k}\right)_{c_0},
\qquad
Y=\left(\bigoplus_{k\ge1}\ell_\infty^{n_k}\right)_{c_0}.
\]
Concatenating the finite coordinate blocks identifies \(Y\) isometrically with \(c_0\). Define
\[
T_q(x_k)_{k\ge1}
=
(2^{-k}V_kx_k)_{k\ge1}.
\]
Because \(\|V_k\|\le1\) and \(2^{-k}\to0\), the finite block truncations converge to \(T_q\) in operator norm, so \(T_q\) is compact.

For a finite sequence \(x_i=(x_{i,k})_k\in X_q\),
\[
\sum_i\|T_qx_i\|^q
=
\sum_i\sup_k
\big(2^{-k}\|V_kx_{i,k}\|\big)^q
\le
\sum_k2^{-kq}\sum_i\|V_kx_{i,k}\|^q.
\]
For Gaussian sums,
\[
\left(\sum_i\|V_kx_{i,k}\|^q\right)^{1/q}
\le
\mathbb E\Big\|\sum_i g_ix_{i,k}\Big\|
\le
\mathbb E\Big\|\sum_i g_ix_i\Big\|_{X_q}.
\]
Hence
\[
C_q^g(T_q)
\le
\left(\sum_k2^{-kq}\right)^{1/q}<\infty.
\]
Likewise, if
\[
D=
\max_{\eta_i=\pm1}
\Big\|\sum_i\eta_ix_i\Big\|_{X_q},
\]
then for every \(k\),
\[
\left(\sum_i\|V_kx_{i,k}\|^q\right)^{1/q}
\le
\max_{\eta_i=\pm1}
\Big\|\sum_i\eta_ix_{i,k}\Big\|
\le D,
\]
so
\[
\|T_q\|_{q,1}
\le
\left(\sum_k2^{-kq}\right)^{1/q}<\infty.
\]

On the other hand, restricting test sequences to the \(k\)-th coordinate block gives
\[
C_q^r(T_q)
\ge
2^{-k}C_q^r(V_k)
\ge
2^k
\]
for every \(k\). Therefore
\[
C_q^r(T_q)=\infty.
\]

Finally, each \(X_n\) embeds isometrically in \(\ell_\infty^{2n}\) via
\[
J_nx=
\left(x,\frac{H_nx}{s_n}\right).
\]
Thus the \(c_0\)-sum \(X_q\) embeds isometrically as a closed subspace of
\[
\left(\bigoplus_k\ell_\infty^{2n_k}\right)_{c_0}\cong c_0.
\]

## Context and comparison with known results

Talagrand's Research Problem 19.1.2 asks whether
\[
C_q^r(U)\lesssim
\max\{C_q^g(U),\|U\|_{q,1}\}
\]
holds universally. The same chapter proves the comparison for operators whose domain is \(\ell_\infty^N\), and notes the corresponding \(C(K)\) theory.

Wu's arXiv:2609.19731v1 gives a negative answer at \(q=2\), with the finite-dimensional Walsh--Hadamard spaces used above. The present result uses Wu's construction and his \(q=2\) estimates as prior input, but obtains new estimates for every \(q\ge2\) and then glues normalized blocks to produce a single compact qualitative separator for each fixed \(q\).

For \(2<q<\infty\), Maurey's classical theorem says that for an operator from a Banach lattice, being \((q,1)\)-summing is equivalent to having Rademacher cotype \(q\). Thus Theorem 2 does not conflict with the lattice theory: \(X_q\) is merely a closed subspace of \(c_0\), not a Banach-lattice domain under the inherited coordinate order. It shows that the positive lattice-domain theorem does not extend to arbitrary closed subspaces of \(c_0\).

## Originality qualification

To the best of our knowledge, the following were not stated in the inspected sources:

1. the Walsh--Hadamard counterexample satisfies a logarithmic Talagrand gap for every fixed finite \(q\ge2\);
2. the explicit \((q,1)\)-summing estimate
   \[
   \|U_n\|_{q,1}
   \le
   n^{1/(2q)}(2\log(2n))^{1/(2q)};
   \]
3. for every fixed finite \(q\ge2\), there is a compact \(T_q:X_q\to c_0\), with \(X_q\) a closed subspace of \(c_0\), that has finite Gaussian cotype \(q\) and finite \((q,1)\)-summing norm but infinite Rademacher cotype \(q\).

The Walsh--Hadamard construction, the \(q=2\) estimates, interpolation of sequence norms, direct sums, and the classical Banach-lattice/C(K) cotype theory are prior art. The direct-sum step is standard once the fixed-\(q\) finite-dimensional gap is known.

## Limitations

The result treats real spaces and finite \(q\). It does not determine optimal constants or the optimal growth of the finite-dimensional ratio, and it does not address a simultaneous single operator for all exponents \(q\). The compact gluing is qualitative and does not locate \(T_q\) in a finer operator ideal. No claim is made that the domain \(X_q\) is a Banach lattice or isomorphic to \(c_0\).

## References

1. X. Wu, *A Counterexample to Talagrand's Operator Cotype Problem*, arXiv:2609.19731v1 (2026). https://arxiv.org/abs/2609.19731
2. M. Talagrand, *Upper and Lower Bounds for Stochastic Processes: Decomposition Theorems*, 2nd ed., Springer (2021), Research Problem 19.1.2 and Theorem 19.1.5. https://michel.talagrand.net/ULBSPRINGER.pdf
3. M. Junge, *Comparing gaussian and Rademacher cotype for operators on the space of continuous functions*, Studia Math. 118 (1996), 101--115. https://arxiv.org/abs/math/9302206
4. H. J. Song, *Characterizations of cotype of operators acting on Banach lattices*, Kangweon-Kyungki Math. J. 13 (2005), 61--82, surveying Maurey's equivalence for \(2<q<\infty\). https://www.kkms.org/kkms/vol13_1/13107.pdf
5. M. Talagrand, *Cotype and \((q,1)\)-summing norm in a Banach space*, Invent. Math. 110 (1992), 545--556. https://doi.org/10.1007/BF01231344
