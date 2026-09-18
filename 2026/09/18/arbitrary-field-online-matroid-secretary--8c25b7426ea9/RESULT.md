# Arbitrary-field online representations for strong linear matroid secretary

## Result

Let \(\mathbb F\) be an arbitrary field and let \(V\) be a finite-dimensional \(\mathbb F\)-vector space. An adversary fixes \(n\) represented matroid elements \(v_e\in V\) with distinct nonnegative weights. The elements arrive in uniformly random order; when an element arrives, its vector in the common coordinate system and its relative weight rank among observed elements are revealed. The future vectors are not known.

There is an ordinal online randomized policy that always selects a linearly independent set \(\mathrm{ALG}\) and satisfies
\[
\Pr[e\in\mathrm{ALG}]\ge \frac1e
\qquad\text{for every }e\in\operatorname{OPT}(E),
\]
where \(\operatorname{OPT}(E)\) is the maximum-weight basis under a fixed tie-breaking rule.

Thus the finite-field hypothesis in the online-representation theorem of Bérczi--Dughmi--Livanos--Soto--Verdugo (2026) is unnecessary for the existence of the policy. In particular, the same \(1/e\) guarantee holds when the online vectors are supplied over \(\mathbb Q\), \(\mathbb R\), \(\mathbb C\), or any other field.

A slightly more general form also holds. Let \(N\) be a fixed finitary modular matroid of finite rank whose closure and rank structure are available to the online policy. An adversary may choose an unknown finite \(n\)-element subset of its ground set and reveal those elements only on arrival. The same ordinal \(1/e\)-probability guarantee holds for the greedy optimum of the revealed finite restriction. The arbitrary-field vector result is the special case in which the ambient modular geometry is the lattice of subspaces of \(V\).

## Why this is not the known-matroid corollary

The motivating paper proves its online-representation theorem only over finite fields. For a matroid known before arrivals, it removes the field restriction by invoking Rado's theorem: a finite linear matroid can be re-represented over a finite field before any online decisions are made. That argument does not directly apply when the representation itself is revealed one vector at a time, because the future dependency structure is not yet known when early decisions are required.

The key observation is instead that the paper's own finite-signature argument for infinite modular extensions can be moved into the online construction at every observed prefix.

## Proof

We use the notation and acceptance LP of Bérczi et al. Fix a sample size \(k\). For every observed set \(Y\), the policy maintains a distribution \(\mu_Y\) on possible accepted spans. Recursively, every state in the support of \(\mu_Y\) is the span of a subset of \(Y\). Hence
\[
\mathcal S_Y:=\{\langle Z\rangle:Z\subseteq Y\}
\]
is finite, with \(|\mathcal S_Y|\le 2^{|Y|}\), over every field.

For a subspace \(L\le V\), define the signature
\[
\sigma_Y(L)=\left(\dim L,\ (\dim(W\cap L))_{W\in\mathcal S_Y}\right).
\]
If \(D=\dim V\), each coordinate of the signature lies in \(\{0,1,\ldots,D\}\). Consequently only finitely many signatures occur, even when \(\mathbb F\) is infinite.

The acceptance LP at a step \(Y\) has finitely many variables \(p_Y(e,W)\), because \(e\in Y\) and \(W\in\operatorname{supp}(\mu_{Y-e})\). Its only apparently infinite family of constraints is
\[
g_p(L)\le 0\qquad(L\le V),
\]
where, with \(|Y|=i\),
\[
g_p(L)=-(i-k)\dim L+
\sum_{e\in Y}u_e(L)+
\sum_{e\in\operatorname{OPT}(Y)}
\mathbb E_{W\sim\mu_{Y-e}}[p_Y(e,W)\Delta_e(W,L)].
\]
Here
\[
u_e(L)=\mathbb E_{W\sim\mu_{Y-e}}\dim(W\cap L)
\]
and
\[
\Delta_e(W,L)=
\dim((W+\langle e\rangle)\cap L)-\dim(W\cap L).
\]
Both \(W\) and \(W+\langle e\rangle\) belong to \(\mathcal S_Y\). Therefore every coefficient and constant in the inequality \(g_p(L)\le0\) is determined by \(\sigma_Y(L)\). Subspaces with the same signature give exactly the same affine inequality. The LP thus has only finitely many essential constraints over an arbitrary field.

It remains to check feasibility. Choose one representative subspace for every realized signature. The supermodularity argument of the motivating paper is field-independent:
\[
g_p(L)+g_p(H)\le g_p(L\cap H)+g_p(L+H).
\]
Because the signature set is finite, the same finite minimax argument used in the paper's modular-extension section applies. If an optimal dual distribution places positive mass on incomparable representative subspaces, move the common mass from \(L,H\) to representatives of the signatures of \(L\cap H\) and \(L+H\). The minimax objective does not decrease by supermodularity, while the secondary objective
\[
\mathbb E[(\dim L)^2]
\]
strictly increases, since
\[
\dim L+\dim H=\dim(L\cap H)+\dim(L+H).
\]
Thus an optimal dual distribution can be supported on a chain.

For a fixed chain, the source paper's greedy construction of the acceptance probabilities uses only modular dimension identities. In particular, for \(e\notin W\),
\[
\Delta_e(W,L)=\mathbf 1[e\in W+L],
\]
and the chain nesting of the sets \(\{W:e\notin W+L\}\) lets one allocate the target acceptance mass \(k/(i-1)\) greedily. Summing the resulting inequalities over the current greedy basis gives \(g_p(L)\le0\) on the whole chain. Hence the finite-signature LP is feasible.

All LP coefficients are rational: they are built from previously chosen rational probabilities and integer dimensions. A finite feasible rational LP has a rational feasible point, so the recursion may use exact rational acceptance probabilities. The support of every newly formed \(\mu_Y\) remains finite because it is obtained from predecessor states \(W\) and the states \(W+\langle e\rangle\).

The rest of the source proof is unchanged. Conditional on an improving element \(e\in\operatorname{OPT}(X)\) arriving last among an observed set \(X\) of size \(i>k\), it is accepted with probability exactly
\[
\frac{k}{i-1}.
\]
Taking \(k=\lfloor n/e\rfloor\) and averaging over the uniformly random arrival position gives
\[
\Pr[e\in\mathrm{ALG}]
 =\frac{k}{n}\sum_{j=k}^{n-1}\frac1j
 \ge \frac1e.
\]
The cases \(n\le2\) are handled by accepting the first nonloop element.

The same proof works in a fixed finite-rank modular ambient matroid by replacing span, sum, intersection, and dimension with closure, join, meet, and rank. The finite signature is then
\[
\sigma_Y(L)=\left(r(L),\ (r(W\cap L))_{W\in\mathcal S_Y}\right),
\]
exactly as in the modular-extension argument of the motivating paper. Crucially, no knowledge of the future finite subset is required if the invariant is imposed on the entire fixed finite-rank ambient geometry.

## Verification

`artifacts/verify_signatures.py` performs an exact rational sanity check in dimension four. It constructs all subset-span states of four observed vectors, samples additional rational lines and planes not generated by observed subsets, verifies that affine intersection-dimension constraints are constant on signatures, and checks the supermodularity inequality on every ordered pair in the sampled family. The recorded output is `PASS` with 1,521 supermodularity checks. This is a finite sanity check; the theorem is proved by the argument above.

## Originality boundary

The \(1/e\) linear-matroid secretary theorem, the dimension invariant, the acceptance LP, the supermodular uncrossing argument, and the finite-signature treatment of infinitely many flats are all due to the cited 2026 work and are not claimed as new here. The contribution is the observation and proof that the finite-signature treatment can be used *inside the online-representation model*, eliminating the finite-field assumption and yielding the online finite-rank modular-ambient formulation.

The motivating paper explicitly states its online theorem for representations over a finite field, while its arbitrary-field conclusion is only for the known-matroid model via an offline finite-field re-representation. Its later modular-extension section separately develops the finite-signature device for possibly infinitely many flats. Searches for arbitrary-field/infinite-field online representation, modular online representation, and equivalent strong matroid secretary formulations found no inspected source stating the extension above. The two motivating strong-secretary preprints are extremely recent, so a contemporaneous revision or independent observation is a material residual originality risk.

## Limitations

No polynomial-time implementation is claimed. The source construction already maintains data for all observed subsets and solves large LPs. Over an infinite ambient geometry, the proof shows that only finitely many constraint signatures are essential, but the effective cost of identifying realized signatures depends on how the field or modular geometry is represented. The result is therefore an unrestricted online policy theorem, not a uniform efficient algorithm over arbitrary field encodings.

The theorem also assumes a fixed finite-dimensional vector space, or more generally a fixed finite-rank modular ambient geometry. It does not cover an unknown ambient geometry of unbounded rank.

## References

1. K. Bérczi, S. Dughmi, V. Livanos, J. A. Soto, V. Verdugo, *The Strong Secretary Conjecture is True for Linear Matroids*, arXiv:2609.20797 (2026). https://arxiv.org/abs/2609.20797
2. H. Abdi, K. Banihashem, M. T. Hajiaghayi, D. Mittal, *On the Strong Matroid Secretary Conjecture and Beyond*, arXiv:2609.19118 (2026). https://arxiv.org/abs/2609.19118
