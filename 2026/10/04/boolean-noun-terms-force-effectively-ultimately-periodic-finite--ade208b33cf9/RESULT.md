# Boolean noun terms force effectively ultimately periodic finite spectra
## Finding

Extend the syllogistic language with cardinality comparisons studied by Jiang by allowing noun terms generated from finitely many raw nouns under
\[
\text{union}
\]
and
\[
\text{complement}.
\]
Equivalently, noun terms may use all finite Boolean operations. Sentence-level Boolean connectives may also be present.

For a finite theory \(\Gamma\), let
\[
\operatorname{Spec}(\Gamma)
=
\{N\ge1:\Gamma\text{ has an }N\text{-element model}\}.
\]

Then:

\[
\boxed{
\operatorname{Spec}(\Gamma)\text{ is effectively Presburger-definable.}
}
\]

Consequently,
\[
\boxed{
\operatorname{Spec}(\Gamma)\text{ is semilinear and effectively ultimately periodic.}
}
\]

There is a second structural restriction:
\[
\boxed{
N\in\operatorname{Spec}(\Gamma),\ m\ge1
\Longrightarrow
mN\in\operatorname{Spec}(\Gamma).
}
\]

Thus every finite spectrum in this Boolean-noun extension is closed under positive integer dilation.

The extension is nevertheless substantially richer than the original language. For every integer
\[
k\ge2
\]
there is an explicit finite theory \(\Delta_k\) whose spectrum is exactly
\[
\boxed{
\operatorname{Spec}(\Delta_k)=\{kn:n\ge1\}.
}
\]

Jiang exhibits the case \(k=3\) after adding noun-level union. The construction below gives all moduli at once and the Presburger translation gives a global upper bound on the spectra of **every finite theory** in the Boolean-noun extension.

In particular, no finite theory in this extension can have as its spectrum the primes, the powers of two, or any other non-ultimately-periodic subset of the positive integers.

## Assumptions and scope

The underlying syllogistic atoms are those of \(S^\dagger(\mathrm{card})\):

\[
\forall(x,y),
\qquad
\exists(x,y),
\qquad
\exists^{\ge}(x,y),
\qquad
\exists^{>}(x,y).
\]

Their finite-model meanings are, respectively,

\[
x\subseteq y,
\]
\[
x\cap y\ne\varnothing,
\]
\[
|x|\ge |y|,
\]
and
\[
|x|>|y|.
\]

A Boolean noun term is built from raw noun symbols by complement relative to the universe and finite union. Intersection is therefore definable by De Morgan duality.

The theorem is about **finite theories**. This finiteness is essential to the finite-atom Presburger reduction: a finite theory mentions only finitely many raw nouns.

If sentence-level Boolean connectives are absent, a finite theory is simply treated as a finite conjunction of atomic syllogistic sentences. If they are present, the same translation applies recursively to the Boolean combinations.

The result gives a necessary global form for spectra and an infinite family of exactly realizable spectra. It does not claim that every semilinear dilation-closed set is realizable.

## Proof

### Boolean atoms turn every noun cardinality into a linear form

Let the raw nouns occurring in \(\Gamma\) be
\[
p_1,\ldots,p_r.
\]

Every element of a finite model has a unique Boolean membership type
\[
\varepsilon=(\varepsilon_1,\ldots,\varepsilon_r)\in\{0,1\}^r,
\]
where
\[
\varepsilon_i=1
\]
means membership in \(p_i\).

For each
\[
\varepsilon\in\{0,1\}^r
\]
introduce a nonnegative integer variable
\[
z_\varepsilon
\]
counting the elements of that Boolean atom.

Every Boolean noun term \(t\) is a union of some of these atoms. Hence there is a set
\[
B_t\subseteq\{0,1\}^r
\]
such that
\[
|t|
=
\sum_{\varepsilon\in B_t}z_\varepsilon.
\]

Thus noun cardinalities are linear forms with coefficients in
\[
\{0,1\}.
\]

The total size of the universe is
\[
N=\sum_{\varepsilon\in\{0,1\}^r}z_\varepsilon.
\]

### Every syllogistic atom is Presburger

For Boolean noun terms \(s,t\), the four atomic sentence forms translate as follows.

The universal inclusion
\[
\forall(s,t)
\]
holds exactly when no element lies in
\[
s\setminus t.
\]
Hence it becomes
\[
\sum_{\varepsilon\in B_s\setminus B_t}z_\varepsilon=0.
\]

The existential overlap
\[
\exists(s,t)
\]
becomes
\[
\sum_{\varepsilon\in B_s\cap B_t}z_\varepsilon\ge1.
\]

The weak cardinal comparison
\[
\exists^{\ge}(s,t)
\]
becomes
\[
\sum_{\varepsilon\in B_s}z_\varepsilon
\ge
\sum_{\varepsilon\in B_t}z_\varepsilon.
\]

The strict cardinal comparison
\[
\exists^{>}(s,t)
\]
becomes
\[
\sum_{\varepsilon\in B_s}z_\varepsilon
\ge
\sum_{\varepsilon\in B_t}z_\varepsilon+1.
\]

These are quantifier-free Presburger formulas.

If sentence-level Boolean connectives are available, translate them by the same Boolean connectives. Let the resulting Presburger formula be
\[
\Phi_\Gamma((z_\varepsilon)_\varepsilon).
\]

Then
\[
N\in\operatorname{Spec}(\Gamma)
\]
if and only if
\[
\exists(z_\varepsilon)_{\varepsilon\in\{0,1\}^r}
\left[
\bigwedge_\varepsilon z_\varepsilon\ge0
\ \wedge\
N=\sum_\varepsilon z_\varepsilon
\ \wedge\
\Phi_\Gamma((z_\varepsilon)_\varepsilon)
\right].
\]

This is a Presburger definition of the spectrum.

All steps are effective. Standard Presburger quantifier elimination therefore computes a semilinear presentation of the set of admissible \(N\). Since a one-dimensional Presburger set is ultimately periodic, \(\operatorname{Spec}(\Gamma)\) is effectively ultimately periodic.

### Dilation closure

Suppose
\[
M\models\Gamma
\]
has
\[
|M|=N.
\]

For any
\[
m\ge1,
\]
replace every element of \(M\) by \(m\) indistinguishable copies. Interpret every raw noun by taking all \(m\) copies of each of its old members.

Every Boolean noun cardinality is multiplied by the same factor \(m\).

Therefore inclusions and nonempty intersections keep the same truth value, and both
\[
|s|\ge|t|
\]
and
\[
|s|>|t|
\]
keep the same truth value after multiplying both sides by \(m\).

Hence every atomic sentence has the same truth value in the blown-up model. The same is true of every sentence-level Boolean combination.

The blown-up model has size
\[
mN
\]
and still satisfies \(\Gamma\). Thus
\[
N\in\operatorname{Spec}(\Gamma)
\Longrightarrow
mN\in\operatorname{Spec}(\Gamma).
\]

### Exact divisibility by every modulus

Fix
\[
k\ge2
\]
and use raw nouns
\[
x_1,\ldots,x_k.
\]

Let \(\Delta_k\) contain:

1. pairwise disjointness:
\[
\forall(x_i,\overline{x_j})
\qquad
(1\le i<j\le k);
\]

2. coverage:
\[
\forall\left(\overline{x_1},x_2\vee\cdots\vee x_k\right);
\]

3. equal cardinalities:
\[
\exists^{\ge}(x_i,x_1)
\quad\text{and}\quad
\exists^{\ge}(x_1,x_i)
\qquad
(2\le i\le k).
\]

Pairwise disjointness gives
\[
x_2\vee\cdots\vee x_k
\subseteq
\overline{x_1}.
\]
Coverage gives the reverse inclusion. Hence
\[
\overline{x_1}
=
x_2\vee\cdots\vee x_k.
\]

Thus the universe is the disjoint union
\[
x_1\sqcup\cdots\sqcup x_k.
\]

The paired weak comparisons force
\[
|x_1|=\cdots=|x_k|.
\]

Since the universe is nonempty, the common cardinality is at least one. Therefore every model of \(\Delta_k\) has size
\[
kn
\]
for some
\[
n\ge1.
\]

Conversely, every set of size
\[
kn
\]
can be partitioned into \(k\) blocks of size \(n\), producing a model of \(\Delta_k\).

Therefore
\[
\operatorname{Spec}(\Delta_k)=\{kn:n\ge1\}.
\]

## Verification

The argument was checked at three independent levels.

First, the source language and the noun-level extension were inspected directly. Jiang explicitly adds noun-level union and complement, constructs a finite theory with spectrum equal to the positive multiples of \(3\), and notes that the analogous intersection extension has the same expressive effect.

Second, the Presburger translation was reconstructed from the finite Boolean partition induced by the raw nouns. Each of the four syllogistic atomic forms becomes exactly one linear equality or inequality over nonnegative integer atom counts. Sentence-level Boolean operations preserve Presburger definability, and existentially projecting away the atom counts preserves it as well.

Third, the divisibility construction was checked algebraically for arbitrary \(k\): pairwise disjointness and the coverage sentence force a partition into \(k\) blocks, while paired cardinal comparisons force equal block sizes.

The dilation argument is independent of the Presburger argument: it uses only the homogeneity of all four atomic semantic clauses under replacing every element by \(m\) copies.

No finite experiment is used to infer ultimate periodicity or the arbitrary-\(k\) construction.

## Relationship to prior work

Jiang completely classifies spectra of the original syllogistic language with cardinality comparisons: besides the empty spectrum, only eventual tails and eventual even tails occur. The paper also classifies the extension by Boolean connectives at the **sentence level**.

In Section 5.1, Jiang turns instead to Boolean structure at the **noun level**. The paper gives an explicit theory whose spectrum is divisibility by \(3\), showing that noun-level union has substantially greater arithmetic expressive power than sentence-level Boolean combination alone. It then leaves the broader expressive landscape of such noun connectives for further study.

The present theorem supplies a global upper bound for every finite theory in that noun-Boolean extension: after partitioning the universe into Boolean atoms, model existence at size \(N\) is an existential Presburger problem. This implies effective semilinearity and ultimate periodicity. The arbitrary-\(k\) construction simultaneously generalizes the source's divisibility-by-\(3\) example to every modulus.

Earlier work by Moss on syllogistic logic with cardinality comparisons studies finite reasoning in the base comparison language, while Moss--Topal study infinite-set semantics. Ding--Harrison-Trainor--Holliday study comparative cardinality over Boolean algebras in a broader logical setting. The checked sources do not state the finite-spectrum semilinearity consequence for Jiang's noun-level extension.

Targeted searches for syllogistic cardinality spectra together with Presburger definability, semilinearity, ultimate periodicity, Boolean noun terms, and arbitrary divisibility did not locate an equivalent theorem.

## Limitations

The theorem is an upper-envelope result, not a complete realization theorem for all semilinear dilation-closed sets.

Presburger quantifier elimination can have very high computational complexity. “Effective” here means computable, not efficient.

The proof applies to finite theories because only finitely many raw nouns then occur. An infinitary theory can mention infinitely many raw nouns and is not covered by the finite Boolean-atom reduction.

The dilation-closure theorem prevents many semilinear sets from occurring and shows that semilinearity alone is not an exact characterization.

The arbitrary-\(k\) lower construction uses \(k\) noun symbols. No minimal-symbol claim is made.

## References

[1] Ruiting Jiang, “Finite Spectra of Syllogistic Logic with Cardinality Comparisons,” arXiv:2609.24902, first posted 21 September 2026.

[2] Lawrence S. Moss, “Syllogistic Logic with Cardinality Comparisons,” *Proceedings of WoLLIC 2016*, Lecture Notes in Computer Science 9803, 2016.

[3] Lawrence S. Moss and Selçuk Topal, “Syllogistic Logic with Cardinality Comparisons, On Infinite Sets,” *Review of Symbolic Logic* 13(1) (2020), 155–179.

[4] Yifeng Ding, Matthew Harrison-Trainor, Wesley H. Holliday, and Thomas F. Icard III, “The Logic of Comparative Cardinality,” *Journal of Symbolic Logic* 85(3) (2020), 972–1005.
