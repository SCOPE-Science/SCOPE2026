# Finite-versus-countable monotone-subset boundary at \(\omega_1\)

## Finding

For every infinite well-orderable cardinal \(\kappa\), every finite family of maps \(g_0,\ldots,g_{r-1}:\kappa\to\kappa\) has a subset \(S\subseteq\kappa\) with \(|S|=\kappa\) on which every map is nondecreasing. The countable-family extension fails sharply: in ZFC there are binary maps \(f_n:\omega_1\to\{0,1\}\), for \(n\in\omega\), such that any set on which all \(f_n\) are nondecreasing has at most one element.

## Assumptions and scope

The finite-family statement is in ZF for infinite well-orderable cardinals and follows by iterating the monotone-subset corollary in [1]. The counterexample is stated in ZFC, where an injection \(e:\omega_1\hookrightarrow 2^\omega\) exists because \(2^{\aleph_0}\ge\aleph_1\). No continuum hypothesis is assumed. “Nondecreasing” means that \(f(\alpha)\le f(\beta)\) whenever \(\alpha<\beta\) are in the subset. The result concerns one common subset for the entire family; it does not claim that every countable family fails.

## Proof

**Finite family.** Let \(S_0=\kappa\). Given \(S_i\subseteq\kappa\) of size \(\kappa\), apply Corollary 3.3 of [1] to \(g_i\!\upharpoonright S_i\). It gives \(S_{i+1}\subseteq S_i\), with \(|S_{i+1}|=\kappa\), on which \(g_i\) is nondecreasing. Restricting to a subset preserves monotonicity already obtained for \(g_0,\ldots,g_{i-1}\). After finitely many steps, \(S_r\) works for all maps.

**Countable-family obstruction.** Fix an injection \(e:\omega_1\hookrightarrow 2^\omega\). For every \(n\in\omega\), define
\[
 f_{2n}(\alpha)=1-e(\alpha)(n),\qquad f_{2n+1}(\alpha)=e(\alpha)(n).
\]
Each map takes values in \(\{0,1\}\). Suppose \(\alpha<\beta\) and all the maps are nondecreasing on a set containing both points. Since \(e\) is injective, there is an \(n\) with \(e(\alpha)(n)\ne e(\beta)(n)\). If the two bits are \(0,1\), then \(f_{2n}(\alpha)=1>0=f_{2n}(\beta)\). If they are \(1,0\), then \(f_{2n+1}(\alpha)=1>0=f_{2n+1}(\beta)\). Either case contradicts nondecreasingness. Thus no two distinct points can lie in a common monotone subset.

## Verification

The finite-family argument is a finite induction using the cited one-map result. The counterexample uses only the injection \(e\), the displayed definitions, and the two possible unequal binary-bit cases. The inequality \(2^{\aleph_0}\ge\aleph_1\) suffices; CH is not used. No finite computation is needed, and no claim about ZF alone for the counterexample is made.

## Relationship to prior work

Shen’s choice-free proof of the Erdős–Dushnik–Miller theorem proves the one-map monotone-subset statement in Corollary 3.3 of [1]. Iteration yields the finite-family half above. The countable-family obstruction is a separate explicit coding construction: each bit is represented by a complementary pair of binary maps, forcing a decrease in at least one coordinate for every ordered pair of distinct inputs. The searched literature did not yield an exact statement of this finite-versus-countable boundary. The claim is limited to this boundary and does not assert a new proof of the Erdős–Dushnik–Miller theorem.

## Limitations

The countable-family counterexample is in ZFC and depends on choosing an injection from \(\omega_1\) into Cantor space. It does not settle common monotone-subset questions for families with additional structure, eventual monotonicity, or other cardinal/domain assumptions. The coding argument is elementary and may be folklore; no claim is made that the existence of large antichains in Cantor space is new.

## References

[1] Guozhen Shen, “A choice-free proof of the Erdős–Dushnik–Miller theorem,” arXiv:2609.02703v1, first posted 2026-09-02, especially §3, Theorem 3.2 and Corollary 3.3. https://arxiv.org/abs/2609.02703
