# Congruence rigidity blocks quotient repair of classical set-theoretic direct powers

## Finding

Let \(\mathcal M=(M,\in)\) be a transitive set model of \(\mathrm{ZF}\), and let \(I\ne\varnothing\). On the classical direct power \(M^I\), define \(f\in^*g\iff\forall i\in I,\ f(i)\in g(i)\). Every equivalence relation compatible with \(\in^*\) is equality: if \(f\ne g\), the coordinatewise singleton function \(s_f(i)=\{f(i)\}\) satisfies \(f\in^*s_f\) but \(g\notin^*s_f\). Consequently, when \(|I|\ge2\), the direct power's failure of extensionality cannot be repaired by any quotient that induces a well-defined membership relation.

## Assumptions and scope

Let \(\mathcal M=(M,\in)\) be a transitive set model of \(\mathrm{ZF}\), and let \(I\) be any nonempty set in the surrounding metatheory. The domain is the full function space \(M^I\), with \(f\in^*g\) defined by \(\forall i\in I,\ f(i)\in g(i)\). A congruence means an equivalence relation compatible with the binary relation in both arguments. The result does not assume metatheoretic Choice.

## Proof

Let \(\sim\) be any congruence on \((M^I,\in^*)\). Suppose for contradiction that \(f\sim g\) with \(f\ne g\). Choose \(i_0\in I\) such that \(f(i_0)\ne g(i_0)\). For each \(i\in I\), define \(s_f(i)=\{f(i)\}\). Since \(\mathcal M\models\mathrm{ZF}\), each singleton \(\{f(i)\}\) belongs to \(M\), so \(s_f\in M^I\).

By construction, \(f(i)\in s_f(i)\) for every \(i\), hence \(f\in^*s_f\). At coordinate \(i_0\), however, \(g(i_0)\ne f(i_0)\), so \(g(i_0)\notin\{f(i_0)\}=s_f(i_0)\), and therefore \(g\notin^*s_f\). Compatibility of \(\sim\), together with \(s_f\sim s_f\), would force \(f\in^*s_f\) iff \(g\in^*s_f\), a contradiction. Thus no two distinct functions are congruent, and \(\sim\) is equality.

For the final consequence, suppose \(|I|\ge2\) and choose distinct \(i_0,i_1\in I\). Let \(f(i)=\varnothing\) for all \(i\), and define \(g(i_0)=\{\varnothing\}\) while \(g(i)=\varnothing\) for \(i\ne i_0\). Then \(f\ne g\). Neither function has any \(\in^*\)-member, because each has an empty value at \(i_1\). Hence they violate extensionality. Since the only congruence is equality, every quotient that leaves membership well-defined is the identity quotient and retains this failure.

## Verification

The proof is uniform in every nonempty index set \(I\); it is not inferred from finite enumeration. The key separator is the coordinatewise singleton function, which is available by Pairing in the ground model. The extensionality witness for \(|I|\ge2\) is explicit. No computational certificate or external Choice assumption is needed.

## Relationship to prior work

The closest primary source is the recent preprint *Models of Arbitrary Sets*. Its Section 2 defines the same classical direct-power membership relation and proves failure of extensionality by giving one pair of distinct functions with no members; it also shows that the Separation scheme fails. The present theorem uses the coordinatewise singleton map to prove a stronger congruence-rigidity statement for every nonempty index set, and then deduces that no quotient preserving membership can repair extensionality when there are at least two coordinates. The preprint cites general direct-product preservation work, but that literature concerns preservation of first-order sentences under products rather than the congruences of this set-theoretic membership structure. Section 5.3 also asks whether intensional distinctions can be recovered through identity conditions in the Boolean-valued setting; the theorem here rules out only quotienting the classical direct-power relation and leaves those alternative semantics open.

## Limitations

The result concerns the classical direct power with coordinatewise membership and assumes a transitive set model of \(\mathrm{ZF}\). It does not rule out changing the semantics, changing the relation, or using a Boolean-valued construction rather than a quotient of the classical direct power. The closest older direct-product thesis was not available in full text during this check, so a priority risk remains for an equivalent congruence observation in broader preservation literature.

## References

1. Pedro Teixeira Yago, Santiago Jockwich Martinez, and Giorgio Venturi, “Models of Arbitrary Sets,” arXiv:2610.23219v1 (first public version dated 2026-10-16), especially Section 2, Lemma 2.2, and Propositions 2.10–2.11.
2. J. M. Weinstein, “First Order Properties Preserved by Direct Product,” Ph.D. thesis, University of Wisconsin, 1965. Bibliographic reference only; full text not accessed.
