# Mixed-length full-Fock Toeplitz spectral atoms and a rational zero mode

## Finding
For each integer \(d\ge2\), let \(\mathcal F_d=\ell^2(\{1,\ldots,d\}^*)\), and let \(L_we_v=e_{wv}\) be the left-creation maps. Set
\[
T_d=L_1+L_{22}+L_1^*+L_{22}^*,\qquad P_N=\operatorname{proj}\operatorname{span}\{e_v:|v|\le N\}.
\]
The empirical eigenvalue law of \(P_NT_dP_N\), counting multiplicity and dividing by \(D_N=(d^{N+1}-1)/(d-1)\), converges **in total variation** to the explicit probability measure
\[
\mu_d=\frac{(d-1)(d^2-d-1)}{d^3}\sum_{h=0}^{\infty}d^{-h}\eta_h,
\]
where \(\eta_h\) is the *unnormalized* counting eigenvalue measure of the finite rooted tree \(\mathcal T_h\) defined below. The limit is pure point, and
\[
\mu_d(\{0\})=\frac{(d-1)(d^2-d-1)}{d^3-1},\qquad \mu_2(\{0\})=\frac17.
\]
Its second moment is \(2(d^{-1}+d^{-2})\). Thus unequal word lengths yield an explicit finite-section law beyond the homogeneous-word formulas.

## Assumptions and scope
All operators act on the complex full Fock space over \(d\ge2\) letters. The pair of codewords is \(\{1,22\}\), which is prefix-free and incomplete. Define \(\mathcal T_h\) recursively: \(\mathcal T_0\) is a single vertex; \(\mathcal T_1\) has a root and one child; for \(h\ge2\), the root has two children whose subtrees are respectively \(\mathcal T_{h-1}\) and \(\mathcal T_{h-2}\). Every edge has unit weight, and \(A_h\) is its real symmetric adjacency matrix. Let \(a_h=|\mathcal T_h|\), and \(\eta_h=\sum_{j=1}^{a_h}\delta_{\lambda_j(A_h)}\). There is no assertion of absolute continuity or a full closed form for nonzero atoms.

## Proof
**Exact forest decomposition.** Every word \(v\) uniquely admits \(v=c_1\cdots c_k r\) with \(c_j\in\{1,22\}\) and \(r\) either empty or beginning with neither codeword. Indeed, repeatedly strip the unique initial codeword when present; prefix-freeness makes the choice unique and total length decreases. The graph of \(P_NT_dP_N\) has precisely the edges \(v\leftrightarrow1v\) and \(v\leftrightarrow22v\) when both endpoints have length at most \(N\). The residual suffix \(r\) is invariant along edges. Hence each connected component indexed by a residual word of length \(\ell\) is exactly \(\mathcal T_{N-\ell}\). No multiplicity or edge is lost.

Write \(c=d^2-d-1>0\). There is one residual word of length zero, \(d-1\) residual words of length one, and exactly \(c d^{\ell-2}\) residual words of each length \(\ell\ge2\): the forbidden initial prefixes have \(d^{\ell-1}\) and \(d^{\ell-2}\) words, respectively, and are disjoint. Consequently, for every \(N\ge2\), there is an **exact orthogonal direct-sum decomposition**
\[
P_NT_dP_N\ \simeq\ A_N\oplus A_{N-1}^{\oplus(d-1)}\oplus\bigoplus_{h=0}^{N-2}A_h^{\oplus(c d^{N-h-2})}.
\]
The dimensions on the right total \(D_N\), because each word has exactly one residual suffix. Thus the unnormalized eigenvalue-counting measure is
\[
\eta_N+(d-1)\eta_{N-1}+c\sum_{h=0}^{N-2}d^{N-h-2}\eta_h.
\]

**Total variation and normalization.** The component sizes obey \(a_0=1\), \(a_1=2\), \(a_h=1+a_{h-1}+a_{h-2}\). Their generating function is
\[
\sum_{h\ge0}a_hz^h=\frac1{(1-z)(1-z-z^2)},
\]
so \(a_h=O(\varphi^h)\), where \(\varphi=(1+\sqrt5)/2<d\). Dividing the exact finite measure by \(D_N\), each fixed-\(h\) multiplicity tends to \(c(d-1)d^{-h-3}\). Since \(\|\eta_h\|_{\mathrm{TV}}=a_h\) and \(\sum_h d^{-h}a_h<\infty\), dominated convergence for finite measures proves total-variation convergence; the last two exceptional components vanish in mass as \(O((\varphi/d)^N)\). The generating function at \(z=d^{-1}\) gives
\[
\sum_{h\ge0}d^{-h}a_h=\frac{d^3}{(d-1)c},
\]
so the announced positive atomic limit has mass one.

**Exact zero atom.** For a finite tree with nonzero unit edge weights, the nullity of its adjacency matrix equals its vertex count minus twice its maximum matching size: this follows by leaf elimination, equivalently by induction on pendant edges, since each removed matched leaf and neighbor contributes a nonsingular \(2\times2\) block and preserves the remaining nullity. Let \(F_h\) be the maximum matching size of \(\mathcal T_h\), and \(G_h\) the maximum size among matchings leaving the root unmatched. Set \(\Delta_h=F_h-G_h\). The root has one child for \(h=1\) and two for \(h\ge2\), giving
\[
\Delta_0=0,\quad\Delta_1=1,\quad\Delta_h=\max\{0,1-\Delta_{h-1},1-\Delta_{h-2}\}\quad(h\ge2).
\]
This has periodic values \(\Delta_h=0\) when \(h\equiv0\pmod3\), and \(1\) otherwise. For \(h\ge2\), \(F_h=F_{h-1}+F_{h-2}+\Delta_h\). The nullities \(z_h=a_h-2F_h\), initially \(z_0=1\), \(z_1=0\), therefore satisfy \(z_h=1+z_{h-1}+z_{h-2}-2\Delta_h\), hence \(z_h=1\) exactly when \(h\equiv0\pmod3\), otherwise zero. Summing their contributions yields
\[
\mu_d(\{0\})=\frac{(d-1)c}{d^3}\sum_{j\ge0}d^{-3j}=\frac{(d-1)c}{d^3-1}.
\]

**Second moment.** Each \(\mathcal T_h\) is a tree, hence \(\operatorname{tr}(A_h^2)=2(a_h-1)\). Therefore
\[
\int x^2\,d\mu_d(x)=\frac{2(d-1)c}{d^3}\left(\sum_{h\ge0}d^{-h}a_h-\frac d{d-1}\right)=2(d^{-1}+d^{-2}).
\]
All series converge absolutely by the established size bound.

## Verification
An independent finite-section matrix construction formed the full matrices \(P_NT_dP_N\) and the predicted block matrices and compared sorted eigenvalues. Tests for \(d=2\), \(2\le N\le6\), and \(d=3\), \(2\le N\le4\), agreed to double-precision roundoff (maximum discrepancy below \(6\times10^{-15}\)). Additional tree calculations for \(0\le h\le9\) verified sizes \(1,2,4,7,12,20,33,54,88,143\) and the periodic nullity law. These finite checks supplement the exact infinite-dimensional proof, not replace it. The complete construction is reproducible from the recursive tree and direct sum identities above; no external data files are required.

## Relationship to prior work
Jury and Memana (arXiv:2608.17859v1, first public August 18, 2026) prove a general weak eigenvalue-distribution limit and compute total-variation atomic laws for functions of one creation operator and homogeneous-word sums. Their §3 explicitly reduces the homogeneous case to equal-length blocks; their §5 identifies symbols involving multiple creation/annihilation terms as a further problem. The unequal-length code \(\{1,22\}\), its exact forest law, and the rational zero atom do not follow from those homogeneous reductions. General results about spectral atoms of trees and spectra of homogeneous rooted trees supply context but do not identify this finite word-length truncation law. A database search compared the statement against Fock, prefix-code, spectral-atom, and multi-Toeplitz variants; a negative search is not a uniqueness proof.

## Limitations
Only the specified two-codeword mixed-length symbol, integer alphabet size \(d\ge2\), and truncation by *letter length* are covered. The limit law is described by a convergent series of finite tree eigenvalue measures; nonzero atoms are not individually tabulated. No claim of priority beyond the inspected sources or independent audit is made. The spectrum of the infinite operator is a different question.

## References
- M. T. Jury and A. G. Memana, *Limiting eigenvalue distribution and entropy of multi-Toeplitz matrices*, arXiv:2608.17859v1 (first posted August 18, 2026), especially §§2–5; https://arxiv.org/html/2608.17859v1.
- D. R. DeFord and D. N. Rockmore, *On the Spectrum of Finite, Rooted Homogeneous Trees*, arXiv:1903.07134 (2019); https://arxiv.org/abs/1903.07134.
- J. Salez, *Spectral atoms of unimodular random trees*, J. Eur. Math. Soc. 22 (2020), 345–363, DOI:10.4171/JEMS/923.
