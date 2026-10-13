# Sharp three-marker generation threshold for cyclic three-agent S5 frames

## Finding

For each integer \(n\ge 1\), equip the grid \(W_n=(\mathbb Z/n\mathbb Z)^2\) with three **named equivalence relations** whose classes consist respectively of cells with fixed first coordinate, fixed second coordinate, and fixed coordinate sum modulo \(n\). For any \(P\subseteq W_n\), let \(\mathcal A_n(P)\) be the smallest Boolean subalgebra of \(\mathcal P(W_n)\) containing \(P\) and closed under the three existential modal operators induced by these relations. Define the minimum one-proposition support

\[
\mu_3(n)=\min\big\{|P|:\mathcal A_n(P)=\mathcal P(W_n)\big\}.
\]

**Theorem (sharp support and explicit depth).** For every \(n\),

\[
\boxed{\mu_3(n)=\begin{cases}0,&n=1,\\1,&n=2,\\3,&n\ge3.\end{cases}}
\]

For every \(n\ge3\), the three-element set \(P_n=\{(0,0),(1,0),(0,1)\}\) generates the complete powerset algebra of \(2^{n^2}\) elements. Indeed every cell is definable by an **ordinary, ungraded, one-variable** modal formula of depth at most

\[
\boxed{2+2\lceil\log_2(n-1)\rceil.}
\]

By contrast, omitting the coordinate-sum modality forces \(|P|\ge n-1\) for a two-modality generator on \(W_n\). Thus the third named S5 modality changes the minimum marker-support requirement from at least linear to exactly three.

## Assumptions and scope

The modalities are standard normal existential modalities associated to the full equivalence classes, including reflexive loops. They count neither successor multiplicities nor thresholds; coordinates are in the cyclic group \(\mathbb Z/n\mathbb Z\); all three modalities remain distinguished by name. The Boolean algebra contains \(\varnothing\) and \(W_n\), and is closed under complement, union, intersection, and each modal diamond. The quantitative bound is an upper bound, not a claim that the depth is optimal.

For coordinates \(i,j,s\), denote the corresponding row, column, and sum-diagonal sets by \(X_i=\{(x,y):x=i\}\), \(Y_j=\{(x,y):y=j\}\), and \(D_s=\{(x,y):x+y=s\pmod n\}\). The respective diamonds are \(\Diamond_x,\Diamond_y,\Diamond_s\).

## Proof

**Construction.** Let \(n\ge3\) and \(P=P_n\). The two one-step sets \(\Diamond_x P=X_0\cup X_1\) and \(\Diamond_yP=Y_0\cup Y_1\) intersect in exactly four cells. Removing the three marked cells therefore defines

\[
U=(\Diamond_xP\cap\Diamond_yP)\setminus P=\{(1,1)\}.
\]

In particular \(X_1=\Diamond_xU\) and \(Y_1=\Diamond_yU\) have depth at most two, while \(X_0=(\Diamond_xP)\setminus X_1\) and \(Y_0=(\Diamond_yP)\setminus Y_1\) have depth at most two. We now know the coordinate selectors \(X_i,Y_i\) for \(i=0,1\).

Suppose \(X_i,Y_i\) have been defined for every integer \(0\le i\le L\), where \(1\le L<n-1\), using formulas of depth at most \(d\), and the selectors \(X_0,Y_0\) are retained. For each integer \(0\le s\le\min(2L,n-1)\), select \(a,b\in[0,L]\) with \(a+b=s\). Their intersection \(X_a\cap Y_b=\{(a,b)\}\) is a singleton, so

\[
D_s=\Diamond_s(X_a\cap Y_b),\qquad
X_s=\Diamond_x(D_s\cap Y_0),\qquad
Y_s=\Diamond_y(D_s\cap X_0)
\]

are definable; the latter two have depth at most \(d+2\). The identity \(D_s\cap Y_0=\{(s,0)\}\) holds because \(0\le s<n\), and similarly \(D_s\cap X_0=\{(0,s)\}\). Therefore the known index interval doubles to \([0,\min(2L,n-1)]\). Starting at \(L=1,d=2\), after at most \(\lceil\log_2(n-1)\rceil\) steps all coordinate selectors are definable at the asserted depth. Finally every singleton equals \(X_i\cap Y_j\), and finite Boolean combinations generate every subset of \(W_n\).

**Two markers do not suffice.** For a two-element support \(P=\{u,v\}\subseteq W_n\), define the affine involution \(F(z)=u+v-z\), applied coordinatewise modulo \(n\). It interchanges \(u\) and \(v\), and preserves each of the three equivalence relations: differences in the first coordinate, in the second, and in their sum are all transformed by multiplication by \(-1\). Thus \(F[P]=P\). For \(n\ge3\), \(F\) is not the identity. Any modal formula over the single proposition naming \(P\) is invariant under this nontrivial valuation-preserving automorphism, so a singleton cannot be definable for every world. For a one-element support \(P=\{u\}\), instead use \(F(z)=2u-z\); again \(F[P]=P\) and \(F\ne\mathrm{id}\) for \(n\ge3\). The empty support also cannot distinguish all worlds, since every nontrivial translation is a frame automorphism. This proves \(\mu_3(n)\ge3\), completing the first claim for \(n\ge3\).

For \(n=2\), taking \(P=\{(0,0)\}\), the sets \(\Diamond_xP=X_0\) and \(\Diamond_yP=Y_0\) and their complements yield every \(X_i\cap Y_j\). Zero markers cannot distinguish the four cells. For \(n=1\), the constants already form the whole two-element powerset algebra.

**Two-modality contrast.** With only the first- and second-coordinate relations, a support of fewer than \(n-1\) cells leaves at least two entire first-coordinate classes disjoint from \(P\). Transposing those two first-coordinate indices while fixing all others is a nontrivial automorphism preserving both modalities and \(P\). Hence no such support generates all singletons, giving \(\mu_2(n)\ge n-1\).

## Verification

The accompanying self-contained Python 3 program `verify_latin_modal_generators.py` evaluates ordinary set-based modal refinement, an independent direct Boolean-subalgebra closure, the affine reflection obstructions, and the constructive row/column selectors. Executing it produced:

```
VERIFY_OK direct_boolean_closures 63 reflection_checks 7798 three_modal_constructive_sizes 62 three_modal_partition_sizes 58 two_modal_sparse_cases 2773
```

The direct closure checks exhaust all supports of size at most two for \(n=3\), all \(n=2\) valuations, and the three-marker \(n=3\) witness; further checks cover sizes through \(64\). The computational checks are finite consistency tests: the assertions for all \(n\) follow from the proof above.

## Relationship to prior work

Bezhanishvili and Meadors analyze finitely generated MS4-algebras, modal-algebra generation, and S5-related constructions. Their checked treatment gives the relevant algebraic framework but not this cyclic three-modality support-minimum theorem. Delhommé, Miyakawa, Pouzet, Rosenberg, and Tatsumi analyze **three equivalence relations** and affine cyclic-group constructions, including a notion of *monogenicity under triangle closure*. Their two-point generation under a distinct triangle-closure operation must not be confused with one-proposition Boolean-modal generation: the reflection obstruction above rules out two marked cells for the latter. Nunn and Schwarzentruber study graph-neural-network-related modal expressivity; the present theorem concerns ordinary (ungraded) modal S5 operators. The standard correspondence between modal indistinguishability and refinement is background, not claimed as new.

The proposed contribution is the simultaneous **exact** support threshold for the cyclic three-net, an explicit logarithmic-depth generator, and the two-modality linear lower bound. Closely related older three-net/algebraic-logic formulations could contain an implicit antecedent; no independent novelty audit has yet been performed.

## Limitations

The result is specific to the cyclic addition Latin square and its three named modalities; it does not assert the same marker threshold for every Latin square or arbitrary third equivalence relation. The depth bound is not asserted sharp. The two-modal comparison is a lower bound, not an exact census. Independent mathematical and originality audits remain outstanding.

## References

1. G. Bezhanishvili and C. Meadors, *Local finiteness in varieties of MS4-algebras*, first public version 2023-12-28, https://arxiv.org/abs/2312.16754 .
2. C. Delhommé, T. Miyakawa, M. Pouzet, I. G. Rosenberg, and H. Tatsumi, *Semirigid systems of three equivalence relations*, first public version 2015-05-12, https://arxiv.org/abs/1505.02955 .
3. L. Nunn and F. Schwarzentruber, *A Modal Logic for Explaining some Graph Neural Networks*, 2023-07-11, https://arxiv.org/abs/2307.05150 .
