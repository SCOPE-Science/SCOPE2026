# Four-block quantifier undecidability for rich-sequence arithmetic

## Statement

Write \(\Sigma_4\) for the prenex first-order fragment with prefix
\[
\exists^*\forall^*\exists^*\forall^*
\]
and quantifier-free matrix.

Let \(f:\mathbb N\to\mathbb N\) realise arbitrary permutations in the sense of Karimov--Nieuwveld--Ouaknine: every finite permutation occurs as the relative order of a consecutive block of values of \(f\). Then the \(\Sigma_4\) theory of
\[
\langle\mathbb N;0,1,<,f\rangle
\]
is undecidable. Consequently the same holds after adjoining addition.

More generally, the conclusion holds for their selected-permutation variant whenever the selector predicate \(\varphi(\bar x,n)\) is quantifier-free in the ambient language. In particular, their least-prime-factor construction has undecidable \(\Sigma_4\) theory.

The same quantifier bound applies to the function-valued linear-recurrence-sequence construction in Section 4 of their paper. Thus, if an integer LRS \((u_n)\) has exactly two non-repeated dominant roots whose ratio is not a root of unity and \(u(n)=\max\{0,u_n\}\), then
\[
\operatorname{Th}_{\Sigma_4}\langle\mathbb N;0,1,<,u\rangle
\]
is undecidable.

For the number-theoretic examples obtained from arbitrary permutations this yields, in particular,
\[
\operatorname{Th}_{\Sigma_4}\langle\mathbb N;0,1,<,\phi\rangle
\quad\text{and}\quad
\operatorname{Th}_{\Sigma_4}\langle\mathbb N;0,1,<,s\rangle
\]
undecidable, where \(\phi\) is Euler's totient and \(s\) is the sum-of-divisors function.

## Proof

The point is that the counter-machine reduction in the source paper can be stratified without changing its semantic encoding.

### 1. Quantifier classes of the rank predicates

For the arbitrary-permutation construction, a represented term is indexed by \(n\) with \(d<n\le e\); this is quantifier-free. The source definitions compare the rank of \(f(n)\) among the reference values \(f(m)\), \(c<m\le d\).

For fixed \(k\ge1\), the predicate saying that the rank is exactly \(k\) can be written
\[
\exists m_1\cdots m_k\;\forall m\;\Theta_k,
\]
where \(\Theta_k\) says that the \(m_i\) are distinct qualifying witnesses and every qualifying \(m\) equals one of them. Hence \(\mathrm{cnst}_k\in\Sigma_2\). The zero-rank predicate is \(\Pi_1\).

Likewise, the source predicate \(\mathrm{inc}\), which says that an appropriate interval contains exactly one reference value, is \(\Sigma_2\), while \(\mathrm{eq}\), which says that the corresponding symmetric interval contains none, is \(\Pi_1\).

Consecutiveness of representatives is \(\Pi_1\): in the bare \(<,f\) language, \(n'=n+1\) is expressed by
\[
n<n'\ \wedge\ \forall m\,(n<m\Rightarrow n'\le m).
\]
For the selected-permutation generalisation, if the selector \(\varphi\) is quantifier-free, the same classifications hold: representative membership stays quantifier-free, and consecutiveness merely adds one universal ``no selected point in between'' condition.

The Section 4 LRS-function encoding has exactly the same syntactic profile. Its representative condition is quantifier-free; its \(\mathrm{cnst}_0,\mathrm{succ},\mathrm{eq}\) predicates are \(\Pi_1\), while \(\mathrm{cnst}_k\) for \(k\ge1\) and \(\mathrm{inc}\) are \(\Sigma_2\).

### 2. Remove the only unnecessary negative rank test

The source proof allows the transition formula to use \(\neg\mathrm{cnst}_k\). For quantifier control, this is avoidable.

Counters in the chosen two-counter-machine model take positive values and a conditional instruction tests whether a counter is greater than one. If \(P_y(m)\) is the quantifier-free predicate saying that the reference point \(m\) is counted in the rank represented by \(y\), then
\[
\mathrm{gt1}(y):=\exists p\exists q\,[p\ne q\wedge P_y(p)\wedge P_y(q)]
\]
is \(\Sigma_1\) and, on positive counter values, is equivalent to ``the represented value is not 1.''

Now write the one-step transition relation as a finite disjunction, one disjunct for each program line. An increment line uses an exact control-state predicate, one \(\mathrm{inc}\), and one \(\mathrm{eq}\). A conditional-decrement line splits positively into the cases \(\mathrm{cnst}_1\) and \(\mathrm{gt1}\); decrement is expressed by reversing the arguments of \(\mathrm{inc}\). No negated exact-rank predicate is needed.

Each branch is therefore a conjunction of \(\Sigma_2\), \(\Sigma_1\), and \(\Pi_1\) formulas, hence is \(\Sigma_2\); a finite disjunction remains \(\Sigma_2\). Denote the resulting transition formula by \(\mathrm{Step}\).

### 3. Prenex the halting sentence

The source reduction describes a finite halting trace by three formulas: an initial block, a final block, and a universal local-transition condition.

The initial and final formulas have existentially chosen endpoint representatives. Their boundary conditions have the form \(\forall y\,\neg\mathrm{succ}(\cdots)\). Since \(\mathrm{succ}\in\Pi_1\), these boundary conditions are \(\Pi_2\). Combining them with \(\Pi_1\) successor/zero predicates and \(\Sigma_2\) fixed-positive-rank predicates puts each endpoint formula in \(\Sigma_3\).

For the local condition, universally quantify eight consecutive representative positions. The antecedent saying that they form the required consecutive block beginning with delimiter zero is \(\Pi_1\). The consequent is the conjunction of a \(\Pi_1\) delimiter condition with \(\mathrm{Step}\in\Sigma_2\), so it is \(\Sigma_2\). Therefore the implication is \(\Sigma_2\), and the universal eight-position closure is \(\Pi_3\).

Finally the sequence parameters are existentially quantified, exactly as in the source halting reduction. A conjunction of the two \(\Sigma_3\) endpoint conditions with the \(\Pi_3\) local condition can be prenexed as
\[
\exists^*\forall^*\exists^*\forall^*\;\Theta,
\]
with quantifier-free \(\Theta\). The construction is effective in the input two-counter machine, so decidability of the \(\Sigma_4\) fragment would decide the two-counter-machine Halting Problem.

This proves the theorem.

## Consequences and scope

Karimov--Nieuwveld--Ouaknine prove that Euler's totient and the sum-of-divisors function realise arbitrary permutations, using a theorem of Schinzel. They also prove that a quantifier-free selected-permutation construction works for the least-prime-factor function. Their Section 4 LRS construction uses the same rank-counting predicates and therefore inherits the same four-block bound.

The result localises the new undecidability phenomena at a fixed finite level of the first-order quantifier hierarchy. It does **not** show that \(\Sigma_4\) is optimal. In particular, it neither proves decidability of \(\Sigma_3\) nor excludes a different reduction at lower alternation depth. The motivating paper recalls that the earlier two-power-predicate result of Hieronymi--Schulz already has an undecidable \(\exists^*\forall^*\exists^*\) fragment; that stronger three-block bound is not claimed here for the new one-function structures.

The selected-permutation extension above requires its selector predicate to be quantifier-free. If a selector itself needs quantifiers, its alternation cost must be incorporated separately.

## References

1. T. Karimov, J. Nieuwveld, J. Ouaknine, *Rich Sequences and Decidability of Arithmetic Theories*, arXiv:2609.20415 (2026). https://arxiv.org/abs/2609.20415
2. P. Hieronymi, C. Schulz, *A strong version of Cobham's theorem*, STOC 2022, 1172--1179.
3. A. Schinzel, *On functions φ(n) and σ(n)*, Bulletin de l'Académie Polonaise des Sciences, Classe III 3 (1955), 415--419.
