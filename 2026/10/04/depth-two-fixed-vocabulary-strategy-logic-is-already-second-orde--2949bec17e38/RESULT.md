# Depth-two fixed-vocabulary Strategy Logic is already second-order complete
## Finding

Let
\[
\mathrm{Ag}_0=\{a_1,a_2,a_3,b,c\}
\]
and
\[
\mathrm{AP}_0=\{p_b,p_c,p_S,p_A,p_M\}.
\]

Write
\[
\mathrm{SL}^{5,5}_{X,\mathrm{BG},\le2}
\]
for the sentences of the next-time Boolean-goal fragment of Strategy Logic that use only the fixed vocabulary
\[
(\mathrm{Ag}_0,\mathrm{AP}_0)
\]
and have temporal depth at most \(2\), where temporal depth is the largest nesting depth of the next-time operator \(X\).

Then
\[
\boxed{
\mathrm{SAT}\!\left(\mathrm{SL}^{5,5}_{X,\mathrm{BG},\le2}\right)
\text{ is computably isomorphic to true second-order arithmetic.}
}
\]

In particular, in the terminology of Pshenitsyn,
\[
\mathrm{SAT}\!\left(\mathrm{SL}^{5,5}_{X,\mathrm{BG},\le2}\right)
\]
is
\[
\Pi^1_\infty\text{-complete}.
\]

Thus full second-order complexity already appears simultaneously under three restrictions:

\[
\text{only the temporal operator }X,
\]
\[
\text{temporal nesting depth at most }2,
\]
and
\[
\text{a fixed vocabulary of five agents and five atomic propositions.}
\]

The source proves the corresponding complexity theorem for the entire next-time Boolean-goal fragment. The stronger depth-two and fixed-vocabulary restriction follows by auditing the actual reduction.

## Assumptions and scope

Strategy Logic and its Boolean-goal fragment are those of Pshenitsyn, following the standard concurrent-game semantics.

The fixed agent and proposition sets are exactly the ones chosen in the source's lower-bound construction:
\[
\mathrm{Ag}_0=\{a_1,a_2,a_3,b,c\},
\qquad
\mathrm{AP}_0=\{p_b,p_c,p_S,p_A,p_M\}.
\]

For a formula in the next-time fragment, define temporal depth inductively by
\[
\operatorname{td}(p)=0,
\]
\[
\operatorname{td}(\neg\varphi)=\operatorname{td}(\varphi),
\]
\[
\operatorname{td}(\varphi\circ\psi)=
\max\{\operatorname{td}(\varphi),\operatorname{td}(\psi)\}
\]
for Boolean connectives, strategy quantifiers, and bindings, and
\[
\operatorname{td}(X\varphi)=1+\operatorname{td}(\varphi).
\]

No bound is imposed on the number or alternation of strategy quantifiers. Those quantifiers carry the second-order power.

The result concerns satisfiability over the same class of at-most-countable concurrent game structures used in the source. It does not claim the lower bound when the action set is fixed finite; indeed, prior work shows that bounding the number of available actions changes decidability.

## Proof

Pshenitsyn proves an injective reduction
\[
\mathrm{Th}_2(\mathbb N)
\le_1
\mathrm{SAT}(\mathrm{SL}_X[\mathrm{BG}]).
\]

We inspect the range of that reduction.

### The vocabulary is fixed

Before defining any arithmetic encoding, the source fixes once and for all
\[
\mathrm{Ag}_0=\{a_1,a_2,a_3,b,c\}
\]
and
\[
\mathrm{AP}_0=\{p_b,p_c,p_S,p_A,p_M\}.
\]

Every auxiliary formula and every translated arithmetic formula is built using only these five agent names and five proposition names. Arbitrarily many strategy variables are permitted, but strategy variables are not part of the modal vocabulary being fixed here.

### Every auxiliary formula has temporal depth at most two

The formulas \(I_i\) and \(P_i\), used to define \(\mathrm{Test}\), contain one occurrence of \(X\) in the scope of strategy binding. Hence
\[
\operatorname{td}(I_i)\le1,
\qquad
\operatorname{td}(P_i)\le1.
\]

The formula
\[
L
\]
has the form
\[
[\![\bar x]\!]\,B(\bar x)X\mathrm{Test}.
\]
Since \(\mathrm{Test}\) has temporal depth \(1\),
\[
\operatorname{td}(L)\le2.
\]

The independence formulas \(J_b,J_c\) compare expressions of the form
\[
B(\bar x)XXp_i,
\]
so
\[
\operatorname{td}(J_b)=
\operatorname{td}(J_c)=2.
\]

Therefore
\[
\mathrm{Good}=L\wedge J_b\wedge J_c
\]
has temporal depth exactly at most \(2\).

### The arithmetic interpretation does not increase temporal depth

Membership is encoded by
\[
\mathrm{Mem}(Y,x)
=
B(x,e,e,Y,e)\,XXp_b,
\]
so it has temporal depth \(2\).

Equality is defined by quantifying over \(Y\) and comparing two membership formulas. Strategy quantification and Boolean combination do not increase temporal depth, so
\[
\operatorname{td}(\mathrm{Eq})\le2.
\]

The basic arithmetic relations are encoded as
\[
\mathrm{Succ}(x,y)=B(x,y,e,e,e)Xp_S,
\]
\[
\mathrm{Add}(x,y,z)=B(x,y,z,e,e)Xp_A,
\]
and
\[
\mathrm{Mult}(x,y,z)=B(x,y,z,e,e)Xp_M.
\]
Each has temporal depth \(1\).

The extensionality formulas and the second-order Peano axioms are built from
\[
\mathrm{Eq},\mathrm{Mem},\mathrm{Succ},\mathrm{Add},\mathrm{Mult}
\]
using only strategy quantifiers and Boolean connectives. Hence their temporal depth is at most \(2\).

Now take an arbitrary closed second-order arithmetic sentence
\[
\theta.
\]
Its translation
\[
\theta^\dagger
\]
replaces equality, membership, successor, addition, and multiplication by the formulas above, translates first- and second-order quantifiers into strategy quantifiers, and treats Boolean connectives homomorphically. It introduces no new temporal operator.

Thus
\[
\operatorname{td}(\theta^\dagger)\le2.
\]

The full source formula
\[
\Phi_\theta
=
\mathrm{Good}\wedge
\langle\!\langle e\rangle\!\rangle
\bigl(
\mathrm{Ext}\wedge
\mathrm{PA}_2^\dagger\wedge
\theta^\dagger
\bigr)
\]
therefore has temporal depth at most \(2\).

To place the formula formally inside the Boolean-goal grammar, the source renames bound strategy variables and prenexes the strategy quantifiers while treating bound goals as atoms. This manipulation changes no occurrence of \(X\), and therefore preserves the depth-two bound.

Finally, to make the reduction injective, the source pads with repeated copies of the propositional tautology
\[
p_c\leftrightarrow p_c.
\]
This has temporal depth \(0\) and uses no new symbol.

Consequently the source's one-one reduction in fact has range inside
\[
\mathrm{SL}^{5,5}_{X,\mathrm{BG},\le2}.
\]
Hence
\[
\mathrm{Th}_2(\mathbb N)
\le_1
\mathrm{SAT}\!\left(\mathrm{SL}^{5,5}_{X,\mathrm{BG},\le2}\right).
\]

### The reverse one-one reduction

Pshenitsyn's Proposition 3.1 gives an injective computable translation from arbitrary Strategy Logic satisfiability to true second-order arithmetic by coding a concurrent game structure, strategies, and the satisfaction relation in second-order arithmetic.

Restricting the domain of an injective reduction preserves injectivity. Therefore
\[
\mathrm{SAT}\!\left(\mathrm{SL}^{5,5}_{X,\mathrm{BG},\le2}\right)
\le_1
\mathrm{Th}_2(\mathbb N).
\]

We have one-one reductions in both directions. Myhill's isomorphism theorem now gives
\[
\mathrm{SAT}\!\left(\mathrm{SL}^{5,5}_{X,\mathrm{BG},\le2}\right)
\cong_c
\mathrm{Th}_2(\mathbb N),
\]
as claimed.

## Verification

The primary PDF was inspected at the following load-bearing locations.

The abstract and Theorem 1.1 state computable isomorphism with true second-order arithmetic for full Strategy Logic and the next-time Boolean-goal fragment.

The lower-bound section explicitly fixes
\[
\mathrm{Ag}=\{a_1,a_2,a_3,b,c\}
\]
and
\[
\mathrm{AP}=\{p_b,p_c,p_S,p_A,p_M\}.
\]

Definitions 3.4 and 3.6 show that the auxiliary testing and independence formulas contain only \(X\) or \(XX\).

Definition 3.9 defines membership using
\[
XXp_b.
\]

Definition 3.13 defines successor, addition, and multiplication using one \(X\).

Definition 3.15 translates arbitrary second-order arithmetic by strategy quantification and Boolean composition of these atomic translations, without adding temporal operators.

Theorem 3.20 gives the semantic equivalence
\[
\mathbb N\models\theta
\quad\Longleftrightarrow\quad
\Phi_\theta\text{ is satisfiable}.
\]

The final syntax analysis confirms that prenex conversion preserves membership in the next-time Boolean-goal fragment, and the injectivizing padding is purely propositional.

The upper injective translation is given by Proposition 3.1.

These observations establish the arbitrary-input theorem symbolically; no finite experiment is used as a substitute.

## Relationship to prior work

Pshenitsyn's main theorem proves that satisfiability for Strategy Logic, and already for its next-time Boolean-goal fragment, is computably isomorphic to true second-order arithmetic.

The source emphasizes that only the next-time temporal operator is needed. It does not formulate a temporal-depth bound, and the terms “temporal depth” and “depth two” do not occur in the checked text. Its proof nevertheless uses at most two nested next-time operators.

The source also fixes five agents and five propositions inside the lower-bound construction, but the main theorem is stated for the whole fragment rather than for the fixed-vocabulary sublanguage.

Earlier work on one-goal Strategy Logic obtains decidable \(2\mathrm{EXPTIME}\) satisfiability, while other syntactic restrictions recover decidability or lower complexity. The present refinement locates the full second-order jump at a particularly shallow temporal boundary: the hard formulas need only inspect one or two transitions, and all unbounded complexity resides in strategy quantification.

Targeted searches for Strategy Logic together with temporal depth two, fixed five-agent/five-proposition vocabulary, and fixed-vocabulary high undecidability did not locate an equivalent statement.

## Limitations

The theorem does not reduce the number of agents below five or the number of propositions below five.

It does not bound the number or alternation depth of strategy quantifiers.

The satisfying structures used in the source reduction have countably infinite action sets. No fixed finite-action analogue is claimed.

Temporal depth at most \(2\) is an upper bound for the reduction, not a minimality theorem. The satisfiability problem at temporal depth \(1\) may have lower complexity; this result does not decide that boundary.

## References

[1] Tikhon Pshenitsyn, “Exact Complexity of the Satisfiability Problem for Strategy Logic,” arXiv:2609.16173, first posted 14 September 2026.

[2] Fabio Mogavero, Aniello Murano, Giuseppe Perelli, and Moshe Y. Vardi, “Reasoning about Strategies: on the Satisfiability Problem,” *Logical Methods in Computer Science* 13(1), 2017.

[3] François Laroussinie and Nicolas Markey, “Satisfiability of ATL with Strategy Contexts,” *Electronic Proceedings in Theoretical Computer Science* 119 (2013), 208–223.
