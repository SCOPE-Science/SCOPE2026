# Joint-rank orbit laws and a discrete Gaussian limit for commuting affine retractions

## Finding

For every prime power \(q\), integers \(n\geq0\), \(k\geq1\), and vector space \(V=\mathbb F_q^n\), consider ordered tuples \((f_1,\ldots,f_k)\) of affine maps satisfying \(f_i^2=f_i\) and \(f_if_j=f_jf_i\) for all indices. Denote by \(G_d(q)=|\operatorname{GL}_d(\mathbb F_q)|\), with \(G_0(q)=1\), and put \(\Omega=2^{[k]}\). For every weak composition \(\mathbf d=(d_S)_{S\in\Omega}\) of \(n\), there is **one** conjugacy class under the affine general linear group, having cardinality
\[
N(\mathbf d)=q^{n-d_{[k]}}\frac{G_n(q)}{\prod_{S\in\Omega}G_{d_S}(q)}.
\]
Every nonempty product \(f_T=\prod_{i\in T}f_i\) has affine image dimension
\[
\rho_T=\sum_{S\supseteq T}d_S.
\]
Thus the exact joint image-dimension polynomial is
\[
J_{n,k,q}((t_T))=\sum_{\substack{d_S\ge0\\\sum_S d_S=n}}q^{n-d_{[k]}}\frac{G_n(q)}{\prod_S G_{d_S}(q)}\prod_{\varnothing\ne T\subseteq[k]}t_T^{\sum_{S\supseteq T}d_S}.
\]
The number of conjugacy classes is \(\binom{n+2^k-1}{2^k-1}\), independent of the field size. Here the image *cardinality* of \(f_T\) is \(q^{\rho_T}\), so \(\rho_T\) records affine dimension rather than cardinality.

For \(k=2\), the exact number of ordered commuting affine idempotent pairs whose two image dimensions are \(a,b\) and product image dimension is \(c\) equals
\[
\frac{q^{n-c}G_n(q)}{G_{n-a-b+c}(q)G_{a-c}(q)G_{b-c}(q)G_c(q)}
\]
when \(0\le c\le\min(a,b)\) and \(a+b-c\le n\), and equals zero otherwise. For instance, the total numbers of pairs in dimensions \(n=1\) and \(n=2\) are \(1+3q\) and \(1+3q^2(q^2+2q+2)\), respectively. For \((q,n)=(2,3)\), the total is \(5233\).

**Balanced-rank law.** Fix \(q\) and \(k\), write \(M=2^k\), and let \(n=M\ell+r\) tend to infinity along any fixed remainder \(0\le r<M\). For a uniformly chosen admissible tuple, let \(d_S\) be its joint eigenspace dimensions. The random vector \(e_S=d_S-\ell\), supported on \(\sum_S e_S=r\), converges in total variation to
\[
\Pr(e_S=h_S\ \forall S)=\frac{q^{-\sum_S h_S^2-h_{[k]}}}{\displaystyle\sum_{\substack{v_S\in\mathbb Z\\\sum_Sv_S=r}}q^{-\sum_Sv_S^2-v_{[k]}}}.
\]
The denominator is a finite, positive Gaussian lattice sum. The shift by \(h_{[k]}\) is a characteristic feature of the *affine*, rather than linear, tuple count.

## Assumptions and scope

An affine map has the form \(f(x)=Px+b\), with \(P\) a square matrix over \(\mathbb F_q\) and \(b\in V\). Composition is ordinary function composition. The tuple is ordered, and all \(k\) components are required to be idempotent and to commute pairwise. Conjugacy is by *all invertible affine maps* of \(V\). The notation \(d_{[k]}\) means the block indexed by the full subset, and the empty subset also participates in the weak composition. Zero-dimensional spaces, zero-dimensional blocks, and the identity and constant affine maps are included. Products indexed by \(T\ne\varnothing\) have order-independent meaning because the tuple commutes. No restriction is imposed on the characteristic of \(\mathbb F_q\).

## Proof

**Common affine center.** Define \(E=f_1\cdots f_k\). Pairwise commutation and idempotence show \(E^2=E\) and \(f_iE=E\) for each \(i\). Set \(c=E(0)\). Then \(f_i(c)=c\) for every \(i\). Conjugating by translation \(x\mapsto x+c\) makes each \(f_i\) linear, say \(P_i\); these linear maps are commuting idempotents. Conversely, for any commuting idempotent linear tuple and any common fixed point \(c\), the maps \(f_i(x)=P_i(x-c)+c\) form an admissible affine tuple.

**Canonical Boolean decomposition.** For \(S\subseteq[k]\), the endomorphism
\[
Q_S=\Bigl(\prod_{i\in S}P_i\Bigr)\Bigl(\prod_{j\notin S}(I-P_j)\Bigr)
\]
is idempotent. The \(Q_S\) are pairwise orthogonal and sum to the identity, over every field. Their images \(V_S\) yield a unique direct-sum decomposition \(V=\bigoplus_{S\in\Omega}V_S\). On \(V_S\), \(P_i\) is the identity exactly when \(i\in S\), and vanishes otherwise. Hence their simultaneous conjugacy class is determined precisely by \(d_S=\dim V_S\), and its linear stabilizer is \(\prod_S\operatorname{GL}(V_S)\). Orbit–stabilizer gives \(G_n(q)/\prod_SG_{d_S}(q)\) possible ordered linear tuples of each type.

**The translation multiplicity.** For a fixed linear tuple \((P_i)\), admissible affine parts \((b_i)\) are exactly \(b_i=(I-P_i)c\), with \(c\in V\). Two centers \(c,c'\) give the same tuple if and only if \(c-c'\in\bigcap_i\operatorname{im}P_i=V_{[k]}\). Therefore exactly \(q^{n-d_{[k]}}\) affine offsets occur for each linear tuple. All offsets of this type are conjugate by a translation. The affine stabilizer has order \(q^{d_{[k]}}\prod_SG_{d_S}(q)\), agreeing with the orbit formula. The image of \(f_T\) is an affine translate of the subspace \(\bigoplus_{S\supseteq T}V_S\), proving all joint-rank claims. For two maps, the four dimensions are uniquely recovered from \((a,b,c)\) as \((n-a-b+c,a-c,b-c,c)\), giving the displayed specialization and support criterion.

**Factorized rank series.** Put \(U_S=\prod_{\varnothing\ne T\subseteq S}t_T\), with \(U_{\varnothing}=1\). A formal generating-series consequence, useful for independent coefficient extraction, is
\[
\sum_{n\ge0}\frac{x^nJ_{n,k,q}((t_T))}{G_n(q)}=
\left(\sum_{d\ge0}\frac{(xU_{[k]})^d}{G_d(q)}\right)
\prod_{S\subsetneq[k]}\left(\sum_{d\ge0}\frac{(qxU_S)^d}{G_d(q)}\right).
\]
Each factor simply records one Boolean eigenspace block.

**Total-variation limit.** Write \(G_d(q)=q^{d^2}\phi_d(q)\), where \(\phi_d(q)=\prod_{j=1}^{d}(1-q^{-j})\), with \(\phi_0=1\). The decreasing sequence \(\phi_d\) converges to \(\phi_\infty(q)>0\). With \(d_S=\ell+e_S\) and \(\sum_S e_S=r\), the unnormalized probability of a dimension vector is, up to a factor independent of \(\mathbf e\),
\[
\mathbf1_{\{e_S\ge-\ell\ \forall S\}}\;
\frac{q^{-\sum_Se_S^2-e_{[k]}}}{\prod_S\phi_{\ell+e_S}(q)}.
\]
Indeed \(\sum_S d_S^2=M\ell^2+2\ell r+\sum_S e_S^2\), and \(n-d_{[k]}=(M-1)\ell+r-e_{[k]}\); every other exponent is common to all vectors at this \(n\). For each fixed integer vector of sum \(r\), the above unnormalized expression converges to \(\phi_\infty(q)^{-M}q^{-\sum e_S^2-e_{[k]}}\). It is bounded above by \(\phi_\infty(q)^{-M}q^{-\sum e_S^2-e_{[k]}}\), whose sum over the rank-\((M-1)\) integer lattice is finite by completing the square. Dominated convergence therefore gives convergence of normalization constants and convergence in total variation. This establishes the law, including the nonzero affine tilt.

## Verification

A self-contained Python checker `affine_semilattice_checker.py` independently enumerates all affine maps for prime-field parameter pairs \((q,n)=(2,1),(3,1),(2,2),(3,2),(2,3)\), tests actual composition idempotence and commutation, computes every rank triple, and compares the resulting distribution with the orbit formula. It also checks the dimension-one formula for \(k=2,3,4\) and \(q=2,3,5\). All exact checks pass, including \(5233\) commuting pairs for \((q,n)=(2,3)\). These finite tests are corroboration, not an infinite-dimensional proof; the general proof above is independent of them. The checker requires only the Python standard library and explicitly uses prime-field arithmetic for its tested cases.

## Relationship to prior work

Steinberg's 2023 study of the finite affine transformation monoid proves important semidirect-product and representation-theoretic facts, including the criterion for a *single* affine idempotent in Proposition 7.1(3), but its §7 does not determine joint conjugacy orbits, simultaneous product-image ranks, or the balanced-rank limit. Kulkarni's affine conjugacy classification concerns *single* affine transformations (Theorems 7.1–7.3), while Sharma's enumeration concerns general commuting tuples of **linear matrices**. Simultaneous diagonalization of commuting linear idempotents is classical and is not claimed as new here. The result assessed here is the affine translation-factor refinement, the complete joint image-dimension enumeration for arbitrary tuple length, and the limiting discrete Gaussian with the explicit affine tilt. An equivalent formulation in older finite-semigroup or probabilistic q-series literature remains possible.

## Limitations

The asymptotic theorem fixes \(q\) and \(k\), takes \(n\to\infty\) along one residue class modulo \(2^k\), and states a lattice-valued total-variation limit, not a continuous central limit theorem. If \(k\) or \(q\) varies with \(n\), no uniform assertion is made. The rank variables record dimensions, not raw image cardinalities. Direct computational checks cover only specified prime fields and finite dimensions. The literature comparison was substantive but cannot certify that no equivalent statement appears in unindexed material. Independent proof audit has not been performed.

## References

1. Benjamin Steinberg, *Topology and monoid representations*, arXiv:2306.16379, first publicly posted June 28, 2023; especially §7, Proposition 7.1. https://arxiv.org/abs/2306.16379
2. Ravi S. Kulkarni, *Dynamics of linear and affine maps*, in *Lie Groups and Invariant Theory*, 2008; especially Theorems 7.1–7.3.
3. Uday Bhaskar Sharma, *Simultaneous similarity classes of commuting matrices over a finite field*, arXiv:1409.2698, journal publication 2016.
