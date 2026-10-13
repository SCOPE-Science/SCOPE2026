# Reflexivity changes the exact minimum countermodel size in the IS4 loop example
## Finding

Let
\[
F=\Box((\Box a\to\bot)\wedge((a\to\bot)\to\bot))\to\bot.
\]
This is the formula used in Example 2.6 of Girlando, Kuznets, Marin, and Straßburger to illustrate why a naive countermodel construction for intuitionistic modal logic can keep creating worlds.

The exact minimum number of worlds in a birelational countermodel to \(F\) is \(2\) for \(\mathsf{IS4}\), but only \(1\) for \(\mathsf{IK4}\).

For \(\mathsf{IS4}\), an optimal countermodel has
\[
W=\{w,v\},\qquad w\le v,
\]
with reflexive closure understood for \(\le\), universal modal relation
\[
R=W\times W,
\]
and valuation
\[
V(a)=\{v\}.
\]
The frame satisfies the forward- and backward-confluence conditions because \(R\) is universal, and it satisfies the \(\mathsf{S4}\) requirements because \(R\) is reflexive and transitive.

For \(\mathsf{IK4}\), a one-world frame with reflexive intuitionistic order and empty modal relation is already a countermodel.

## Assumptions and scope

The forcing clauses are the birelational clauses used in the cited paper. Atomic truth is monotone along \(\le\); implication is intuitionistic:
\[
x\Vdash A\to B
\quad\Longleftrightarrow\quad
\text{for every }y\ge x,\ y\Vdash A\text{ implies }y\Vdash B;
\]
and \(\bot\) is forced nowhere. The box clause is the paper's standard birelational modal clause; on the universal relation used below it requires the boxed formula at both worlds.

For \(\mathsf{IS4}\), \(R\) is reflexive and transitive. For \(\mathsf{IK4}\), transitivity is required but reflexivity is not. The result concerns this one explicit formula and the minimum cardinality of a countermodel; it is not a general small-model bound for either logic.

The scientific classification is MSC2020 \(03B45\), whose official description is “Modal logic (including the logic of norms).”

## Proof

Write
\[
B=(\Box a\to\bot)\wedge((a\to\bot)\to\bot),
\]
so that
\[
F=\Box B\to\bot.
\]

In the two-world \(\mathsf{IS4}\) model above, neither world forces \(\Box a\). At \(v\), modal accessibility reaches \(w\), where \(a\) is false. At \(w\), the same is true. Consequently, at every intuitionistic extension of either world, the antecedent \(\Box a\) of \(\Box a\to\bot\) is false. Hence
\[
w\Vdash\Box a\to\bot
\qquad\text{and}\qquad
v\Vdash\Box a\to\bot.
\]

Neither world forces \(a\to\bot\). At \(v\), this fails because \(v\Vdash a\). At \(w\), it fails because the extension \(v\ge w\) forces \(a\). Thus every intuitionistic extension of either world fails to force \(a\to\bot\), and therefore
\[
w\Vdash(a\to\bot)\to\bot
\qquad\text{and}\qquad
v\Vdash(a\to\bot)\to\bot.
\]
So
\[
w\Vdash B
\qquad\text{and}\qquad
v\Vdash B.
\]
Because \(R\) is universal, every modal successor relevant to the box clause forces \(B\). Hence
\[
w\Vdash\Box B.
\]
Since \(\bot\) is forced nowhere, the implication \(\Box B\to\bot\) fails at \(w\). This proves that a two-world \(\mathsf{IS4}\) countermodel exists.

It remains to prove optimality. Consider any one-world \(\mathsf{IS4}\) frame. Reflexivity forces its unique world \(u\) to satisfy \(uRu\). There are only two possible valuations of \(a\).

If
\[
u\Vdash a,
\]
then reflexivity gives
\[
u\Vdash\Box a,
\]
so
\[
u\nVdash\Box a\to\bot.
\]
Thus \(u\nVdash B\).

If
\[
u\nVdash a,
\]
then the sole intuitionistic world forces
\[
a\to\bot,
\]
so
\[
u\nVdash(a\to\bot)\to\bot.
\]
Again \(u\nVdash B\).

Therefore in every one-world \(\mathsf{IS4}\) model,
\[
u\nVdash B.
\]
By modal reflexivity this yields
\[
u\nVdash\Box B.
\]
Hence
\[
u\Vdash\Box B\to\bot.
\]
No one-world \(\mathsf{IS4}\) countermodel exists, so the minimum size is exactly \(2\).

For \(\mathsf{IK4}\), let \(W=\{u\}\), let \(\le\) be reflexive, and take
\[
R=\varnothing.
\]
This frame satisfies transitivity and both confluence conditions vacuously. The box
\[
\Box B
\]
is true vacuously at \(u\), so
\[
u\nVdash\Box B\to\bot.
\]
Thus one world suffices for \(\mathsf{IK4}\), and nonemptiness of Kripke frames makes \(1\) the exact minimum.

## Verification

The proof exhausts the only two valuations of \(a\) on a one-world \(\mathsf{IS4}\) frame, so the lower bound does not rely on a search cutoff. The two-world upper bound is checked directly from the forcing clauses.

The load-bearing frame conditions are also explicit. Universal \(R\) on the two-world chain is reflexive, transitive, forward-confluent, and backward-confluent. Empty \(R\) on the one-world \(\mathsf{IK4}\) frame is transitive and satisfies the confluence conditions vacuously.

The distinction between the two minima uses exactly the presence or absence of modal reflexivity. No finite experiment is used as an infinite proof.

## Relationship to prior work

The 2026 paper proves decidability and the finite model property for \(\mathsf{IS4}\) and \(\mathsf{IK4}\). Its Example 2.6 uses the displayed formula to show that a naive countermodel construction can keep adding worlds indefinitely. The checked full text does not state the exact minimum countermodel size for that example and does not isolate the one-world difference between \(\mathsf{IS4}\) and \(\mathsf{IK4}\).

Targeted searches in the published-finding index covered the exact-minimum formulation, the formula's box/double-negation structure, the Example 2.6 loop phenomenon, and the \(\mathsf{IS4}\)-versus-\(\mathsf{IK4}\) reflexivity contrast. No covering result was found.

Related literature on intuitionistic modal finite-model properties establishes existence of finite countermodels or decision procedures. Those results do not imply the exact minimum for this particular example.

## Limitations

The theorem is deliberately local: it determines the exact minimum countermodel size for one motivating formula, not an asymptotic small-model function. It does not bound the size of countermodels produced by the paper's algorithm.

The originality comparison is search-bounded. An older textbook or lecture note could contain the same tiny countermodel without using the paper's Example 2.6 terminology, although targeted searches for the formula's semantic pattern and the exact size contrast did not locate one.

## References

1. Marianna Girlando, Roman Kuznets, Sonia Marin, and Lutz Straßburger, “A decision procedure for intuitionistic modal logic IS4 (and IK4),” arXiv:2609.24922, first posted 21 September 2026. See the birelational semantics and Example 2.6.
2. MSC2020 database, class \(03B45\): Modal logic (including the logic of norms).
