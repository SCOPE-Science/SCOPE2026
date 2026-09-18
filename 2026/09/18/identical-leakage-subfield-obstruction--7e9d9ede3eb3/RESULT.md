# Identical linear leakage cannot exploit computations over its stabilizer field

## Result

Let \(\mathbb B\subseteq\mathbb F\) be finite fields, let \(C_0\subseteq\mathbb F^{n+1}\) be a linear code used as a Massey secret-sharing base code, and for every share position \(j\in\{1,\ldots,n\}\) let
\[
\ell_j:\mathbb F\longrightarrow V_j
\]
be a \(\mathbb B\)-linear leakage map into a finite-dimensional \(\mathbb B\)-vector space.

For each \(j\), define the **leakage-stabilizer field**
\[
S_j:=\{a\in\mathbb F: a\,\ker(\ell_j)\subseteq\ker(\ell_j)\},
\qquad
S:=\bigcap_{j=1}^n S_j.
\]
Then every \(S_j\), and hence \(S\), is a subfield of \(\mathbb F\) containing \(\mathbb B\).

Consider \(K\) independently masked input secrets with codewords
\(c^{(1)},\ldots,c^{(K)}\in C_0\), and an \([N,K]_{\mathbb F}\) systematic computation code with generator matrix
\[
G_{\rm comp}=[I_K\mid A]\in S^{K\times N}.
\]
For each block \(r\in\{1,\ldots,N\}\), let
\[
c^{(r)}=\sum_{i=1}^K (G_{\rm comp})_{i,r}c^{(i)},
\]
so the first \(K\) blocks are the input maskings and the remaining blocks are linear computations of them. Suppose the same leakage map \(\ell_j\) is reused at position \(j\) of every block.

**Theorem (stabilizer obstruction).** The leakage of every computed block is a \(\mathbb B\)-linear function of the leakages of the \(K\) input blocks. Consequently the complete leakage from all \(N\) blocks carries exactly the same information as the leakage from the \(K\) input blocks alone. In particular, an identical-leakage linear exact repair scheme for the product code exists if and only if the corresponding base-code repair scheme exists with the same \(\ell_j\)'s.

Thus computations with coefficients in \(S\) cannot enlarge the set of base codes vulnerable to an identical-leakage attack.

## Proof

Fix a share position \(j\), and put \(K_j=\ker(\ell_j)\). Since \(\ell_j\) is \(\mathbb B\)-linear, \(K_j\) is a \(\mathbb B\)-subspace of \(\mathbb F\). Every element of \(\mathbb B\) stabilizes \(K_j\), so \(\mathbb B\subseteq S_j\). If \(a,b\in S_j\), then for \(x\in K_j\),
\[
(a+b)x=ax+bx\in K_j,
\qquad
(ab)x=a(bx)\in K_j.
\]
Hence \(S_j\) is closed under addition and multiplication. If \(a\in S_j\setminus\{0\}\), multiplication by \(a\) is a bijection of the finite-dimensional \(\mathbb B\)-space \(\mathbb F\), so
\(\dim_{\mathbb B}(aK_j)=\dim_{\mathbb B}K_j\). The inclusion \(aK_j\subseteq K_j\) is therefore equality, and multiplying by \(a^{-1}\) gives \(a^{-1}K_j=K_j\). Thus \(S_j\) is a subfield. Intersections of subfields are subfields, proving the first assertion.

For every \(a\in S_j\), multiplication by \(a\) descends through the quotient by \(K_j\). Equivalently, there is a well-defined \(\mathbb B\)-linear map
\[
T_{j,a}:\operatorname{Im}(\ell_j)\longrightarrow\operatorname{Im}(\ell_j)
\]
satisfying
\[
T_{j,a}(\ell_j(x))=\ell_j(ax)
\qquad (x\in\mathbb F).
\]
Indeed, if \(\ell_j(x)=\ell_j(y)\), then \(x-y\in K_j\), hence \(a(x-y)\in K_j\), so \(\ell_j(ax)=\ell_j(ay)\).

Now let \(r>K\) be a computed block. Since every coefficient \(g_{i,r}:=(G_{\rm comp})_{i,r}\) lies in \(S\subseteq S_j\),
\[
\ell_j(c^{(r)}_j)
 =\ell_j\!\left(\sum_{i=1}^K g_{i,r}c^{(i)}_j\right)
 =\sum_{i=1}^K T_{j,g_{i,r}}\bigl(\ell_j(c^{(i)}_j)\bigr).
\]
Therefore every leaked value on every computed block is determined \(\mathbb B\)-linearly by the leaked values on the input blocks. Conversely, the full leakage vector contains the input-block leakage vector because the computation code is systematic. The two leakage collections are therefore deterministically equivalent.

If a product-code LERS recovers an input secret from all \(N\) leakage blocks, compose its reconstruction map with the preceding linear map from input leakage to full leakage. This recovers that secret from the \(K\) input-block leakages. Setting the other \(K-1\) input codewords to zero restricts the reconstruction to the leakage of one arbitrary base-code codeword, giving a base-code LERS with the same \(\ell_j\)'s. The converse is immediate by repairing each input block separately. This proves the equivalence.

## Exact specialization to trace leakage

The leakage maps used by Aoutouf and Augot are one-symbol trace maps
\[
\ell_{\beta_j}(x)=\operatorname{Tr}_{\mathbb F/\mathbb B}(\beta_jx),
\qquad \beta_j\ne0.
\]
For these maps the stabilizer is **exactly** the base field:
\[
S_j=\mathbb B.
\]
To see this, if \(a\in S_j\), then multiplication by \(a\) preserves the kernel of the nonzero \(\mathbb B\)-linear functional \(\ell_{\beta_j}\). Since \(\mathbb F/\ker(\ell_{\beta_j})\) is one-dimensional over \(\mathbb B\), there is some \(\lambda\in\mathbb B\) such that
\[
\operatorname{Tr}(\beta_jax)=\lambda\operatorname{Tr}(\beta_jx)
\quad\text{for every }x\in\mathbb F.
\]
The trace pairing of finite fields is nondegenerate, so
\(\beta_j a=\lambda\beta_j\), and \(\beta_j\ne0\) implies \(a=\lambda\in\mathbb B\). The reverse inclusion follows from \(\mathbb B\)-linearity.

Hence, for identical one-subsymbol trace leakage, **every computation whose systematic computation matrix is defined over the base field is incapable of improving on the base-code attack**. At least one coefficient outside \(\mathbb B\) is necessary for computed-block leakage to carry genuinely new information. This condition is necessary, not sufficient.

This gives a sharp structural distinction between the two behaviors reported in arXiv:2609.19929. Repeated additions and array summation use only coefficients in \(\mathbb B\), so identical leakage cannot help. By contrast, examples using multipliers from \(\mathbb F\setminus\mathbb B\), such as extension-field LFSR multipliers, are not subject to this obstruction. It also shows that merely requiring coefficients to be nonzero, unequal, and different from one is not a field-uniform sufficient condition: when \(|\mathbb B|\ge4\), distinct coefficients satisfying those syntactic conditions can still lie entirely inside \(\mathbb B\), where the obstruction applies.

## Rank-factorization corollary for the Aoutouf--Augot criterion

Use the notation of arXiv:2609.19929. Under identical leakage, all diagonal matrices are equal:
\[
M_{1,\beta}=\cdots=M_{N,\beta}=M_\beta.
\]
If \(G_{\rm comp}\in\mathbb B^{K\times N}\), then for every matrix \(X\) over \(\mathbb F\), base-field expansion gives, up to harmless row ordering,
\[
(G_{\rm comp}\otimes X)_{\mathbb B}
 =G_{\rm comp}\otimes X_{\mathbb B}.
\]
Since \(G_{\rm comp}\) has rank \(K\),
\[
\operatorname{rank}_{\mathbb B}(G_{\rm comp}\otimes X_{\mathbb B})
 =K\,\operatorname{rank}_{\mathbb B}(X_{\mathbb B}).
\]
Applying this to
\(X=\overline G_0M_\beta\) and
\(X=[\phi;\overline G_0]M_\beta\) shows that the generalized rank gap in their Eq. (30) is exactly
\[
K\left(
\operatorname{rank}_{\mathbb B}\!\left(\begin{bmatrix}\phi\\\overline G_0\end{bmatrix}M_\beta\right)_{\mathbb B}
-
\operatorname{rank}_{\mathbb B}(\overline G_0M_\beta)_{\mathbb B}
\right).
\]
Therefore the product-code condition that this gap equal \(Km\) holds if and only if the base-code gap equals \(m\), exactly the base criterion in their Eq. (8). This extends their explicit simple-addition argument to every base-field-defined linear computation at once.

## Context and significance

Aoutouf and Augot (2026) study leakage on Massey secret sharing when the masked secrets participate in linear computations. Their general construction allows different leakage functions on different computation blocks and improves the existential parameter range from the base case to \(k\le Nn/(Km)\). For identical leakage functions, they prove that simple addition cannot yield an improvement, state that the same phenomenon appears to extend to array summation, and report simulations in which more general extension-field relations can exploit identical leakage.

The theorem above identifies the general mechanism behind that boundary. The relevant object is not the syntactic form of the computation but the subfield that stabilizes the kernels of the reused leakage maps. For trace-to-base-field leakage this stabilizer is exactly the base field. The result therefore covers arbitrary base-field linear circuits, arbitrary numbers of inputs and intermediate values, and, in its first form, arbitrary finite-dimensional \(\mathbb B\)-linear leakage maps rather than only one-symbol traces.

## Verification

`artifacts/verify_stabilizer.py` performs finite sanity checks over \(\mathbb F_8/\mathbb F_2\). It verifies that the kernel stabilizer of the trace map is exactly \(\mathbb F_2\), that an outside-base coefficient can produce new trace information, and representative instances of the Kronecker rank factorization used in the rank corollary. The general theorem is proved algebraically above and does not depend on enumeration.

## Limitations

The obstruction assumes that the same leakage map at a given share position is reused across all computation blocks. It does not apply when different leakage functions are permitted on different blocks, which is precisely the broader model where the motivating paper proves improved existence bounds.

For general vector-valued leakage maps the stabilizer field may strictly contain \(\mathbb B\); the correct obstruction is then the intersection \(S\), not necessarily the base field itself. For one-symbol nonzero trace leakage, the equality \(S=\mathbb B\) is exact.

A coefficient outside the stabilizer field is only a necessary opportunity for extra information, not a guarantee that a successful attack or LERS exists. No claim is made about nonlinear computations or multiplication.

Originality is asserted only to the best of our knowledge. The motivating preprint was submitted on 17 September 2026, so near-simultaneous observations or a subsequent revision are a material residual risk.

## References

1. Nadja Aoutouf and Daniel Augot, *On the Leakage of Massey Secret Sharing Schemes under Linear Computations*, arXiv:2609.19929v1, 2026. https://arxiv.org/abs/2609.19929
2. Nadja Aoutouf and Daniel Augot, *A Subfield Subcode Construction of a Linear Exact Repair Scheme*, Workshop on Coding and Cryptography (WCC 2026), 2026. https://wcc2026.inria.fr/assets/final_versions/WCC2026_paper_33.pdf
3. Venkatesan Guruswami and Mary Wootters, *Repairing Reed-Solomon Codes*, STOC 2016. https://doi.org/10.1145/2897518.2897525
