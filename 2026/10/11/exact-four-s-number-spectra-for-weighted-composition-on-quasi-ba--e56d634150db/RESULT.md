# Exact four s-number spectra for weighted composition on quasi-Banach sequence spaces

## Finding
Let \(0<p\le1\), let \(w=(w_n)_{n\ge1}\) be strictly positive, and let \(X=\ell_p(w)\) over either \(\mathbb R\) or \(\mathbb C\), equipped with
\[
\|x\|_{p,w}=\left(\sum_{n\ge1}|w_nx_n|^p\right)^{1/p}.
\]
Let \(\varphi:\mathbb N\to\mathbb N\), \(u:\mathbb N\to\mathbb C\) (real-valued in the real case), and let the weighted composition operator \(T:X\to X\) act by \((Tx)_k=u_kx_{\varphi(k)}\). Define its fiber coefficients
\[
\lambda_n=\frac1{w_n}\left(\sum_{k:\,\varphi(k)=n}|w_ku_k|^p\right)^{1/p}\in[0,\infty]
\]
and suppose \(L=\sup_n\lambda_n<\infty\). For \(j\ge1\) put
\[
\sigma_j=\sup_{F\subset\mathbb N,\ |F|=j}\ \min_{n\in F}\lambda_n .
\]
Thus \(\sigma_j\) is the generalized \(j\)-th-largest fiber coefficient even when its supremum is not attained. Then, for every positive integer \(j\),
\[
\boxed{a_j(T)=b_j(T)=c_j(T)=d_j(T)=\sigma_j.}
\]
Here \(a_j\), \(b_j\), \(c_j\), and \(d_j\) are respectively the approximation, Bernstein, Gelfand, and Kolmogorov numbers defined in the next section using the displayed quasi-norm. In particular, within this operator family, compactness, strict singularity, and finite strict singularity are equivalent, and occur exactly when \(\lambda_n\to0\).

## Assumptions and scope
The full index set is \(\mathbb N\); all positive weights are permitted, with no upper or lower bound on \(w_n\). The sum over an empty fiber is zero. Boundedness is equivalent to \(L<\infty\), because finitely supported vectors are dense and the fiber supports are disjoint. Write \(B_X=\{x:\|x\|_{p,w}\le1\}\) and \(S_E=\{x\in E:\|x\|_{p,w}=1\}\). For an arbitrary bounded linear operator \(R:X\to X\), set
\[
\begin{aligned}
a_j(R)&=\inf_{\operatorname{rank} A<j}\|R-A\|,\\
b_j(R)&=\sup_{\dim E=j}\inf_{x\in S_E}\|Rx\|,\\
c_j(R)&=\inf_{\operatorname{codim}E<j}\sup_{x\in S_E}\|Rx\|,\\
d_j(R)&=\inf_{\dim F<j}\sup_{x\in B_X}\inf_{y\in F}\|Rx-y\|.
\end{aligned}
\]
All infima are over linear subspaces or bounded linear finite-rank operators of the indicated type. Codimensions are algebraic finite codimensions of closed subspaces; for the lower bound this choice does not matter. These definitions do not invoke Banach-space duality. The conclusion concerns operators acting on the *same* weighted \(\ell_p\) space, not arbitrary operators, analytic composition on Hardy spaces, other \(p\)-scales, or metric entropy numbers.

## Proof
**Disjoint-fiber identity.** Normalize the input coordinates as \(e_n/w_n\). Define \(v_n=T(e_n/w_n)\); then \(\|v_n\|_{p,w}=\lambda_n\), and the supports of \(v_n\) and \(v_m\) are disjoint when \(n\ne m\). For every finitely supported \(x\), and by continuity for all \(x\in X\),
\[
\|Tx\|_{p,w}^p=\sum_{n\ge1}\lambda_n^p|w_nx_n|^p.
\]
Hence \(\|T\|=L\). For a finite set \(F\), the coordinate truncation \(TP_F\) has rank at most \(|F|\), and \(\|T(I-P_F)\|=\sup_{n\notin F}\lambda_n\).

**Upper bounds for the four numbers.** Fix \(t>\sigma_j\). By the definition of \(\sigma_j\), the set \(F_t=\{n:\lambda_n>t\}\) contains at most \(j-1\) indices. The rank-\(<j\) operator \(TP_{F_t}\) witnesses \(a_j(T)\le t\). The subspace \(\ker P_{F_t}\), of codimension less than \(j\), witnesses \(c_j(T)\le t\). Every \(j\)-dimensional subspace of \(X\) meets \(\ker P_{F_t}\) nontrivially, proving \(b_j(T)\le t\). Finally \(F=T(\operatorname{span}\{e_n:n\in F_t\})\), of dimension less than \(j\), witnesses \(d_j(T)\le t\). Let \(t\downarrow\sigma_j\).

**Lower bounds for three numbers.** Fix \(s\) with \(0<s<\sigma_j\). Select \(j\) distinct input coordinates \(n_1,\dots,n_j\) with \(\lambda_{n_i}>s\), and put \(E=\operatorname{span}\{e_{n_i}\}_{i=1}^j\). The disjoint-fiber identity gives \(\|Tx\|\ge s\|x\|\) on \(E\), hence \(b_j(T)\ge s\). Every operator of rank below \(j\) has a nonzero kernel vector on \(E\), giving \(a_j(T)\ge s\). Every subspace of codimension below \(j\) intersects \(E\) nontrivially, giving \(c_j(T)\ge s\).

**Disjoint-support distance lemma (critical step for Kolmogorov numbers).** In any real or complex \(\ell_p\) space with \(0<p\le1\), let \(z_1,\dots,z_j\) be normalized vectors with pairwise disjoint supports \(B_1,\dots,B_j\). For each subspace \(F\) of dimension less than \(j\), at least one \(z_i\) has \(\operatorname{dist}(z_i,F)\ge1\). Indeed, otherwise select \(f_i\in F\) with \(\|z_i-f_i\|_p^p<1\). Put \(D_{ri}=\|P_{B_r}f_i\|_p^p\). The pointwise \(p\)-subadditivity \(\|a+b\|_p^p\le\|a\|_p^p+\|b\|_p^p\), together with disjoint block splitting, yields
\[
1\le\|z_i-P_{B_i}f_i\|_p^p+D_{ii},\qquad
\|z_i-P_{B_i}f_i\|_p^p+\sum_{r\ne i}D_{ri}<1.
\]
Therefore \(D_{ii}>\sum_{r\ne i}D_{ri}\) for every \(i\): the matrix of block \(p\)-masses has strictly dominant *columns*. If \(\sum_i\alpha_i f_i=0\), applying the same \(p\)-subadditivity on every block and summing gives
\[
\sum_i|\alpha_i|^pD_{ii}\le
\sum_i|\alpha_i|^p\sum_{r\ne i}D_{ri}.
\]
Strict column dominance makes this impossible unless all \(\alpha_i=0\), so the \(f_i\) are independent, contradicting \(\dim F<j\). This proves the lemma; no unproved basis projection or duality assumption is involved.

Apply the lemma in the weighted target after the isometry \(x\mapsto(w_nx_n)\) to the normalized columns \(z_i=v_{n_i}/\lambda_{n_i}\). For every target subspace \(F\) with \(\dim F<j\), some \(i\) satisfies \(\operatorname{dist}(z_i,F)\ge1\). Since \(\lambda_{n_i}>s\) and \(F\) is linear, \(\operatorname{dist}(v_{n_i},F)>s\). Testing the input unit vector \(e_{n_i}/w_{n_i}\) shows \(d_j(T)\ge s\). Let \(s\uparrow\sigma_j\). If \(\sigma_j=0\), the lower bounds are automatic. Together with the upper bounds this proves the displayed identity for every \(j\).

**Operator-ideal consequence.** If \(\lambda_n\to0\), truncating the first \(N\) input coordinates gives finite-rank approximants in operator norm, so \(T\) is compact and \(b_j(T)\to0\), which is finite strict singularity. Conversely, if \(\lambda_n\not\to0\), infinitely many input columns have \(\lambda_n\ge\delta>0\); their closed coordinate span is isometric to \(\ell_p\), and \(T\) is bounded below on it, so \(T\) is not strictly singular. Finite strict singularity always implies strict singularity, completing the equivalence.

## Verification
The deterministic script `VERIFY.py` checks exact rational strict block dominance for \(p=1/2\) and \(p=1\), algebraic rank of the perturbed block vectors, weighted composition fiber identities across 420 finite sample matrices, and the non-complementation example. Run `python3 VERIFY.py` with a standard Python 3 installation; it requires no external modules. Its observed output is

`VERIFY_OK exact_dominance_profiles=130 finite_fiber_identities=420 noncomplemented_p_checks=3 proof_is_analytic=True`

These computations test the mechanism but do not certify all dimensions, arbitrary real exponents, or infinite sequences. Those quantifiers follow from the preceding analytic argument. A noteworthy obstacle avoided here is that for \(0<p<1\), the span of \((2^{-1/p},2^{-1/p})\) in \(\ell_p^2\) has no norm-one linear projection: its unit vector has \(\ell_1\)-mass \(2^{1-1/p}<1\), whereas the dual functional bound needed for a contractive retraction would force mass at least one. Thus the Kolmogorov equality is not justified by merely transferring the Hilbert-space singular-value argument through a contractive range projection.

## Relationship to prior work
Lechner, Li, Queffélec and Rodríguez-Piazza (arXiv:1612.01177, first publicly submitted 4 December 2016) investigate approximation numbers of weighted composition operators on the analytic Hardy space \(H^2\). Their Section 2.1 recalls the equality of classical four minimax definitions in Hilbert spaces, but that does not imply a quasi-Banach sequence-space statement. Abanin and Mannanikov (DOI 10.46698/x5057-2500-3053-t, 2023 journal issue) study precisely the quasi-Banach weighted sequence spaces at issue; their publicly accessible abstract reports boundedness, compactness, essential and \(\omega\)-essential norms, and closed range, not these four finite-rank or quotient-width sequences. The full published statement for \(C(K)\) identifies the same four minimaxes using fiber *maxima* in a supremum norm; the finite-fiber multiplication result explicitly assumes \(1<p<\infty\) and derives Kolmogorov numbers by Banach duality. Neither implies the \(0<p<1\) disjoint-block distance lemma. Classical diagonal-operator width literature likewise does not yield the quotient-width identity for generally uncomplemented quasi-Banach output fibers by an isometric factorization alone. The proof above supplies the missing strict block-dominance lemma rather than claiming uniqueness from a search failure.

## Limitations
The assertion is restricted to weighted composition on weighted coordinate quasi-Banach \(\ell_p\) with \(0<p\le1\), not arbitrary operators, entropy numbers, spaces with overlapping input columns, or \(p>1\). The complete 2023 article could not be obtained during the literature comparison despite checking its open bibliographic page and a publicly indexed PDF excerpt; overlap in its nonindexed full text is a residual originality risk. As with any limited literature search, other equivalent earlier results may exist. No independent mathematical audit or exhaustive novelty certification is claimed.

## References
1. G. Lechner, D. Li, H. Queffélec, L. Rodríguez-Piazza, *Approximation numbers of weighted composition operators*, arXiv:1612.01177 (v1, 4 December 2016); J. Funct. Anal. 274 (2018), 1928–1958, DOI 10.1016/j.jfa.2018.01.010.
2. A. V. Abanin and R. S. Mannanikov, *Weighted composition operators on quasi-Banach weighted sequence spaces*, Vladikavkaz. Mat. Zh. 25(4) (2023), 5–19, DOI 10.46698/x5057-2500-3053-t; primary MSC 47B37.
3. R. S. Mannanikov, *On the Essential and ω-Essential Norms of a Linear Operator in Weighted Sequence Spaces* (2025), DOI 10.18522/1026-2237-2025-4-14-19. Later essential-norm result, not a four s-number theorem.
4. C. V. Hutton, J. S. Morrell, J. R. Retherford, *Diagonal operators, approximation numbers, and Kolmogoroff diameters*, J. Approx. Theory 16 (1976), 48–80, DOI 10.1016/0021-9045(76)90095-2. Classical diagonal approximation literature; its full text was not inspected.
