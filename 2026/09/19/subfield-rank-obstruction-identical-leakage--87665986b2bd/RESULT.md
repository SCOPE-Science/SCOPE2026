# Subfield-rank obstruction for identical leakage under linear computations

## Statement

Let \(B=\mathbb F_q\subseteq F=\mathbb F_{q^m}\). Let \(C_0\le F^{n+1}\) be a linear base code whose coordinate \(0\) is the secret, and let \(C_{\rm comp}\le F^N\) be a \([N,K]_F\) computation code with generator matrix \(G_{\rm comp}\). The associated product code is \(C_{\rm comp}\otimes C_0\).

An **identical one-subsymbol leakage scheme** means that for every share position \(j\in[n]\) there is one \(B\)-linear map
\[
 g_j:F\to B
\]
which is applied at that share position in every one of the \(N\) computation slots, and from the resulting \(Nn\) values the \(K\) independent input secrets are reconstructed. This is the identical-leakage model of Aoutouf--Augot; over finite fields their trace maps \(x\mapsto\operatorname{Tr}_{F/B}(\beta_jx)\) represent all \(B\)-linear functionals \(F\to B\).

For \(a=(a_1,\ldots,a_N)\in F^N\), define its **subfield rank**
\[
 \rho_B(a)=\dim_B\operatorname{span}_B\{a_1,\ldots,a_N\},
\]
and
\[
 \rho_B(C_{\rm comp})=\min_{0\ne a\in C_{\rm comp}}\rho_B(a).
\]

**Theorem 1 (rank-transfer obstruction).** If \(C_{\rm comp}\otimes C_0\) admits an identical one-subsymbol leakage scheme, then for every nonzero \(a\in C_{\rm comp}\) of subfield rank \(r\), the base code \(C_0\) admits a linear exact-repair/leakage scheme using at most \(r\) \(B\)-symbols from each share. In particular, it admits such a scheme with at most \(\rho_B(C_{\rm comp})\) \(B\)-symbols per share.

Consequently, if
\[
 \rho_B(C_{\rm comp})=1,
\]
then an identical one-subsymbol product leakage attack can exist only if the base code itself already has a one-subsymbol linear exact-repair scheme. Thus the computation supplies no new one-subsymbol leakage vulnerability.

Equivalently, rank one occurs exactly when \(C_{\rm comp}\) contains a nonzero word lying in a projective \(B\)-line \(\alpha B^N\) for some \(\alpha\in F^*\).

## Proof of Theorem 1

Fix \(0\ne a\in C_{\rm comp}\), and write
\[
 a=uG_{\rm comp},\qquad u=(u_1,\ldots,u_K)\in F^K\setminus\{0\}.
\]
Let \(r=\rho_B(a)\), and choose a \(B\)-basis \(\alpha_1,\ldots,\alpha_r\) of the coordinate span of \(a\). Then
\[
 a_i=\sum_{\ell=1}^r b_{i,\ell}\alpha_\ell,
 \qquad b_{i,\ell}\in B.
\]

Take an arbitrary base-code word \(c=(c_0,\ldots,c_n)\in C_0\). Feed the product decoder the valid \(K\) input codewords
\[
 u_1c,\ldots,u_Kc.
\]
Because \(C_0\) is \(F\)-linear, these are in \(C_0\). The computation word at slot \(i\) is exactly \(a_ic\). Hence at share position \(j\), the product leakage equals
\[
 g_j(a_ic_j)
 =\sum_{\ell=1}^r b_{i,\ell}g_j(\alpha_\ell c_j),
\]
using \(B\)-linearity of \(g_j\).

Therefore all \(N\) product leakages at position \(j\) can be synthesized from the \(r\) base leakage values
\[
 \widetilde g_{j,\ell}(c_j):=g_j(\alpha_\ell c_j),
 \qquad \ell=1,\ldots,r.
\]
The product reconstruction returns the input secret vector
\[
 (u_1c_0,\ldots,u_Kc_0).
\]
Choose \(t\) with \(u_t\ne0\); multiplication of the \(t\)-th recovered coordinate by \(u_t^{-1}\) returns \(c_0\). Thus the maps \(\widetilde g_{j,\ell}:F\to B\) form a base-code repair using at most \(r\) subsymbols per share. All transformations are \(B\)-linear. \(\square\)

## A complete criterion for one linear output

Consider the systematic single-output computation
\[
 (x_1,\ldots,x_K)\longmapsto
 (x_1,\ldots,x_K,\mu_1x_1+\cdots+\mu_Kx_K),
\]
with computation code
\[
 C_\mu=\{(x_1,\ldots,x_K,\textstyle\sum_i\mu_ix_i):x_i\in F\}.
\]
Write \(\overline\mu_i=\mu_i+B\in F/B\).

**Theorem 2 (quotient-space criterion).**
\[
 \rho_B(C_\mu)=1
 \quad\Longleftrightarrow\quad
 \overline\mu_1,\ldots,\overline\mu_K
 \text{ are linearly dependent over }B.
\]
If these quotient classes are independent, then
\[
 \rho_B(C_\mu)=2.
\]

**Proof.** A nonzero codeword of \(C_\mu\) has rank one iff there are \(\alpha\in F^*\) and \(b_1,\ldots,b_K,b\in B\), not all \(b_i\) zero, such that
\[
 x_i=\alpha b_i,
 \qquad
 \sum_i\mu_ix_i=\alpha b.
\]
After dividing by \(\alpha\), this is precisely
\[
 \sum_i b_i\mu_i\in B,
\]
which is equivalent to \(\sum_i b_i\overline\mu_i=0\) in \(F/B\). This proves the rank-one equivalence. If the quotient classes are independent, no rank-one word exists. On the other hand every generator row \((0,\ldots,1,\ldots,0,\mu_i)\) has subfield rank \(2\), because independence forces \(\mu_i\notin B\). Hence the minimum rank is exactly \(2\). \(\square\)

### Consequences

Since \(\dim_B(F/B)=m-1\), every single-output computation on
\[
 K\ge m
\]
inputs has \(\rho_B(C_\mu)=1\), for every choice of coefficients. Therefore no such relation can create a new identical one-subsymbol attack beyond what is already possible against the base code.

For two inputs, \(\mu_uu+\mu_vv=w\), a necessary condition for any genuine identical-leakage advantage is
\[
 \overline\mu_u,\overline\mu_v\text{ independent in }F/B.
\]
In particular, when \([F:B]=2\), this is impossible for every coefficient pair, including distinct \(\mu_u,\mu_v\in F\setminus\{0,1\}\). Thus the coefficient condition used in the simulations of Aoutouf--Augot is not by itself sufficient to permit a genuine identical-leakage gain in all extension degrees.

Whenever the quotient classes are independent, Theorem 1 still shows that an identical one-subsymbol attack on the computation can be compressed to at most two \(B\)-symbols per base share. Hence a single linear output has an intrinsic two-subsymbol ceiling along a suitable one-dimensional family of input secrets.

## LFSR interpretation

For the \([N,1]_F\) LFSR computation code generated by
\[
 (1,\alpha,\alpha^2,\ldots,\alpha^{N-1}),
\]
one has
\[
 \rho_B(C_{\rm comp})
 =\dim_B\operatorname{span}_B\{1,\alpha,\ldots,\alpha^{N-1}\}
 =\min\{N,[B(\alpha):B]\}.
\]
This gives a structural explanation for the opposite behavior observed for LFSRs: if \(\alpha\) generates an extension of degree \(m\) and \(N\ge m\), identical leakage across the successive computation values can synthesize up to \(m\) independent base subsymbols, enough in principle to reveal a full \(F\)-symbol.

## Relation to prior work

Aoutouf and Augot introduce leakage attacks on Massey secret sharing under a computation code and show that independent leakage maps can exploit general linear relations. In their identical-leakage section they prove that the simple addition relation \(u+v=w\) collapses to a base-code LERS, while simulations suggest that weighted relations \(\mu_uu+\mu_vv=w\) with distinct nontrivial coefficients can behave differently. They also observe that identical leakage can accumulate information in an LFSR.

Theorems 1 and 2 give a common mechanism for these phenomena. Simple addition has a rank-one computation word, as do all computation codes containing a projectively \(B\)-rational word. Weighted single-output relations are governed exactly by linear dependence of coefficient classes in \(F/B\). LFSRs instead have subfield rank equal to the dimension generated by successive powers of the multiplier.

The claim of novelty is limited to this rank-transfer theorem, the quotient-space criterion for single-output computations, and their consequences for identical leakage. Standard facts about finite-field trace duality, linear exact repair, and quotient-vector-space dimension are not claimed as new.

## Verification

`artifacts/verify_subfield_rank.py` exhaustively checks Theorem 2 for representative binary extensions \(\mathbb F_{2^m}/\mathbb F_2\): \((m,K)=(2,2),(3,2),(3,3),(4,2)\). It compares the minimum subfield rank of all nonzero codewords of every coefficient tuple against the rank of the coefficient classes in \(F/B\). The recorded output is in `artifacts/verify_output.txt`.

The finite enumeration is a sanity check; the general result is proved algebraically above.

## Limitations

The theorem is a necessary obstruction, not a sufficient criterion for the existence of an identical-leakage attack when \(\rho_B(C_{\rm comp})>1\). It does not determine whether a two-subsymbol base repair exists, nor whether the random subfield-subcode construction succeeds for quotient-independent coefficients. It concerns linear leakage maps and linear computation codes over finite fields. The motivating preprint is very recent, so near-simultaneous observations or a later revision remain a material originality risk.

## References

1. N. Aoutouf and D. Augot, *On the Leakage of Massey Secret Sharing Schemes under Linear Computations*, arXiv:2609.19929, 2026. https://arxiv.org/abs/2609.19929
2. N. Aoutouf and D. Augot, *A Subfield Subcode Construction of a Linear Exact Repair Scheme*, WCC 2026 extended abstract. https://wcc2026.inria.fr/
3. V. Guruswami and M. Wootters, *Repairing Reed-Solomon Codes*, STOC 2017 / arXiv:1509.04764. https://arxiv.org/abs/1509.04764
