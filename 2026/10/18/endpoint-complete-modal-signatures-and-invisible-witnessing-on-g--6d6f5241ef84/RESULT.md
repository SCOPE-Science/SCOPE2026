# Endpoint-complete modal signatures and invisible witnessing on Gödel stars

## Finding

In constant-free propositional Gödel modal logic, with primitives \(\bot,\wedge,\vee,\to,\Box,\Diamond\), consider the **star models** over a countable supply of propositional variables \(\mathfrak M_S\) defined below, for an arbitrary nonempty set \(S\subset(0,1)\). Put \(a=\inf S\) and \(b=\sup S\).

**Endpoint and witnessing theorem.** For every modal formula, its exact truth degree at the root depends on \(S\) only through \((a,b)\), and two such roots have the same exact truth degree for *every* formula if and only if their endpoint pairs agree. Nevertheless, \(\mathfrak M_S\) is a witnessed model if and only if \(a,b\in S\). If \(0<a<b<1\), the quotient of *all modal formulas* by agreement at every world of \(\mathfrak M_S\) has **exactly twelve** elements; explicit representatives are listed below.

Consequently, for any rational \(0<a<b<1\), the models corresponding to \(S=(a,b)\cap\mathbb Q\) and \(T=S\cup\{a,b\}\) have identical exact values at their respective roots, validate exactly the same modal formulas globally, and induce exactly the same local consequence relation (even for arbitrary sets of premises). The first is **not** witnessed (neither \(\Box p\) nor \(\Diamond p\) is witnessed at the root), whereas the second **is** witnessed for every modal formula. Hence no set, finite or infinite, of formulas in this constant-free language defines witnessedness as a property of Gödel-Kripke **models with fixed valuations**. This is a model-level claim; it does **not** assert failure of the known axiomatizations of the logics valid over witnessed models, and it does not concern validity under every valuation of a fixed frame.

## Assumptions and scope

Truth degrees form the standard Gödel algebra \([0,1]\), with
\[
 x\wedge y=\min(x,y),\quad x\vee y=\max(x,y),\quad
 x\to y=\begin{cases}1&x\le y,\\y&x>y.\end{cases}
\]
A model is \((W,R,v)\), where \(W\ne\varnothing\), the accessibility weight \(R\) maps \(W^2\) to \([0,1]\), and propositional variables receive worldwise truth degrees. Modal evaluation is
\[
 v_w(\Box\varphi)=\inf_{u\in W}(R(w,u)\to v_u(\varphi)),\qquad
 v_w(\Diamond\varphi)=\sup_{u\in W}\min(R(w,u),v_u(\varphi)).
\]
It is *witnessed* when, at every world and for every modal formula, both extremal values are attained by some world in these respective infimum/supremum expressions.

For any nonempty \(S\subset(0,1)\), put \(W_S=\{r\}\sqcup\{u_s:s\in S\}\). Define \(R(r,u_s)=1\) for every \(s\in S\), and put \(R=0\) on every other pair. Thus leaves have no positive-weight successors and the root has no self-loop. Give the variable \(p\) the value \(v_{u_s}(p)=s\), set \(v_r(p)=0\), and make every other variable have value \(0\) at all worlds. These valuations are *part of the models*: no universal quantification over alternative valuations is intended.

Formulas may have arbitrary finite size and nesting depth; there are no extra non-Boolean truth constants and no involutive negation. Abbreviations \(\neg\varphi=(\varphi\to\bot)\) and \(\top=(\bot\to\bot)\) are permitted. The theorem also allows \(a=0\), \(b=1\), or \(a=b\), except where the twelve-element count explicitly assumes \(0<a<b<1\).

## Proof

**1. Uniform leaf normal form.** Every formula \(\varphi\) has exactly one of three *uniform leaf roles*, denoted \(0,t,1\), such that for every \(s\in S\) its value at \(u_s\) is respectively \(0,s,1\). Prove this by induction. Atomic formulas take role \(0\), except \(p\), which takes role \(t\). Since no leaf has a positive-weight outgoing arrow, \(\Box\psi\) has role \(1\) and \(\Diamond\psi\) has role \(0\), irrespective of \(\psi\). The three ordered values satisfy \(0<s<1\) at every leaf. Hence the Gödel operations \(\min,\max,\to\), with implication returning \(1\) or its consequent, operate uniformly on these three symbols without testing the particular \(s\). This closes the induction. The role is uniform even when \(\varphi\) uses arbitrarily many propositional variables, as all variables other than \(p\) are fixed at zero.

**2. Endpoint normal form at the root.** The root modal values depend only on the role of the immediate subformula:
\[
\begin{array}{c|ccc}
\text{leaf role of }\psi&0&t&1\\\hline
v_r(\Box\psi)&0&a&1\\
v_r(\Diamond\psi)&0&b&1
\end{array}
\]
Indeed, the root's zero self-edge contributes \(1\) to each boxed infimum and \(0\) to each diamond supremum, and its other edges have weight \(1\). Propositional connectives compute solely from their operand values, proving by induction that every root value is determined by \((a,b)\). Conversely, \(v_r(\Box p)=a\) and \(v_r(\Diamond p)=b\), so exact agreement on all formulas requires the two endpoints to agree.

**3. Complete twelve-element formula quotient.** Suppose \(0<a<b<1\). By the previous inductions every formula has a semantic signature \((\ell,c)\), where \(\ell\in\{0,t,1\}\) is its leaf role and \(c\in\{0,a,b,1\}\) is its root value. The latter set is closed under Gödel propositional operations, so there are at most \(3\cdot4=12\) signatures. Every one occurs, as shown by these explicit representatives (row: leaf role; column: root value):

| Leaf role | Root \(0\) | Root \(a\) | Root \(b\) | Root \(1\) |
|---|---|---|---|---|
| \(0\) | \(\bot\) | \(\Box p\wedge\Diamond p\) | \(\Diamond p\) | \(\neg p\) |
| \(t\) | \(p\) | \(p\vee(\Box p\wedge\Diamond p)\) | \(p\vee\Diamond p\) | \(\Box\bot\to p\) |
| \(1\) | \(\Box\bot\) | \(\Box p\) | \(\Box\bot\vee\Diamond p\) | \(\top\) |

As \(a,b\) are distinct interior values, the signatures are pairwise distinct as functions on the model. Thus there are exactly twelve classes, with no hidden depth restriction.

**4. Exact witnessing criterion.** At every leaf, \(\Box\psi=1\) and \(\Diamond\psi=0\), and any world witnesses each extremum through its zero-weight edge; these leaves therefore always satisfy witnessing. At the root, the extremum for \(\Box p\) is \(a\) and can be attained only at a leaf with \(s=a\); similarly \(\Diamond p=b\) can be attained only at a leaf with \(s=b\). Hence witnessing forces \(a,b\in S\). Conversely, if both endpoints belong to \(S\), the uniform leaf-role normal form says that each boxed/diamonded formula takes its root extremum at any leaf (role \(0\) or \(1\)) or at the appropriate endpoint leaf (role \(t\)). Thus *every* modal formula is witnessed, proving the equivalence.

**5. Indistinguishable witnessed and unwitnessed structures.** Fix rational \(0<a<b<1\), let \(S=(a,b)\cap\mathbb Q\) and \(T=S\cup\{a,b\}\). Both sets have the same infimum and supremum, so every formula has equal exact values at the two roots. At any leaf of either model, its truth value is \(0\), the leaf parameter \(s\in(0,1)\), or \(1\) according to one uniform role. Therefore a formula has truth degree \(1\) at all leaves of the first model if and only if it has truth degree \(1\) at all leaves of the second. The roots also agree, yielding identical sets of globally valid formulas. More strongly, every leaf in either model satisfies exactly the formulas with uniform role \(1\), and the two roots satisfy the same formulas; therefore the same sets of pointed truth-one theories occur in the two models. Consequently, for every set of premises \(\Gamma\) and conclusion \(\varphi\), the universal local consequence assertion \(\Gamma\models_{\mathfrak M_S}\varphi\) holds exactly when \(\Gamma\models_{\mathfrak M_T}\varphi\) does. But the first model omits both endpoints and the second includes them; Step 4 proves their different witnessing statuses. Were a family of formulas to define precisely the witnessed models under global satisfaction, it would have to distinguish these two, a contradiction. The same pair also refutes a characterization by root satisfaction alone or by any collection of requirements stated solely in terms of the full local consequence relation.

## Verification

The standalone file `star_checker.py` constructs the exact finite algebra of the three leaf roles and four possible root values using rational parameters \(a=1/3\) and \(b=2/3\). Starting from \(\bot\) and \(p\), it closes semantic signatures under both modalities and all three propositional connectives. It obtains precisely the twelve signatures above and independently interprets the twelve displayed representatives as syntax trees. A separate direct finite-star evaluator checks the representatives against two different finite collections of leaves sharing both endpoints. Run `python star_checker.py`; the expected and observed output is `GODEL_STAR_ENDPOINT_AND_12_SIGNATURES_OK`.

The infinite pair's equivalence and non-witnessing are proved by the all-formula structural inductions above, **not** by finite testing. The checker supports the exact finite closure certificate and representative table; it is not a substitute for the mathematical proof.

## Relationship to prior work

Ferrari, Fiorentini, Giardini and Rodriguez (2026) define fully witnessed Gödel-Kripke models and prove a finite-model property for the resulting modal logic; the two semantic clauses and witnessing definition used here are theirs. Vidal and Rodriguez (2026) develop axiom systems complete for witnessed-model *consequence* and examine partial witnessing conditions. Ferrari, Fiorentini and Rodriguez (2025) treat the crisp-accessibility case, while Metcalfe and Olivetti (2011) develop proof systems for Gödel modal fragments. None of the inspected relevant sections states the endpoint classification of this one-variable star family, its twelve signatures, or the witnessed/unwitnessed pair with identical complete model theories.

The present finding does **not** contradict completeness or axiomatizability of modal theorem sets: having formulas sound and complete for a class is different from defining exact membership in the semantic class for each **fixed-valued model**. The non-definability claim is restricted to this precise model-level distinction. Standard facts about Gödel implication and crisp star frames are used, not claimed as inventions. The full historical literature may contain an equivalent observation expressed in terms of attainable infima or semantic compactifications; novelty remains subject to that risk.

## Limitations

The proof is specific to the constant-free Gödel propositional language, arbitrary fixed valuations, crisp rooted stars and terminal leaves. Adding named interior truth constants or involutive negation may separate the paired models, and changing valuations of other propositional variables may likewise destroy equivalence. The theorem gives **model-level**, not **frame-level**, undefinability; it does not preclude formulas characterizing the logic valid in all witnessed models, which has been studied in the cited literature. It does not establish an analogous statement for richer logics, for first-order languages or for all Gödel models. An older theorem about dense completion of Gödel-modal stars could imply the result; that possibility has not been completely excluded.

## References

1. M. Ferrari, C. Fiorentini, P. Giardini, R. O. Rodriguez, *A Gödel Modal Logic Over Witnessed Models*, arXiv:2606.31906v1 (first public 2026-06-30), https://arxiv.org/html/2606.31906v1.
2. A. Vidal, R. O. Rodriguez, *Axiomatizing logics of finite Gödel-Kripke models*, arXiv:2605.15810v1 (first public 2026-05-15), https://arxiv.org/html/2605.15810v1.
3. M. Ferrari, C. Fiorentini, R. O. Rodriguez, *A Gödel Modal Logic over Witnessed Crisp Models*, TABLEAUX 2025, https://doi.org/10.1007/978-3-032-06085-3_8.
4. G. Metcalfe, N. Olivetti, *Towards a Proof Theory of Gödel Modal Logics*, arXiv:1105.1256v2, https://arxiv.org/html/1105.1256v2.
