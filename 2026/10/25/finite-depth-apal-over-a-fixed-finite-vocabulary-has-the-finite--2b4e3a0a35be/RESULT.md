# Finite-depth APAL over a fixed finite vocabulary has the finite model property

## Finding

Fix a finite set \(A\) of agents, a finite set \(P\) of propositional atoms, and a fixed bound \(d\in\mathbb N\). Consider the variant \(\mathrm{APAL}_{P,d}\) of arbitrary public-announcement logic on multi-agent \(\mathsf{S5}\) models in which each quantified announcement ranges only over epistemic formulas using atoms from \(P\) and having modal depth at most \(d\). Then \(\mathrm{APAL}_{P,d}\) has the finite model property.

Write \(k=|P|\) and \(m=|A|\), and define

\[
N_0=2^k,\qquad N_{r+1}=2^{k+mN_r}.
\]

There are at most \(N_d\) depth-\(d\) epistemic types and at most \(2^{N_d}\) global equivalence classes of allowed announcements. Thus each quantified-announcement operator can be expanded into a finite conjunction of ordinary public-announcement modalities.

## Assumptions and scope

Each agent's accessibility relation is an equivalence relation. Both \(A\) and \(P\) are fixed and finite. Modal depth counts nested knowledge operators. The announcement quantifier ranges over formulas in the base epistemic language only; its announcements contain neither public-announcement operators nor quantified-announcement operators. The formula being evaluated may contain public announcements and nested bounded quantifiers. The bound \(d\) is fixed for this variant.

This statement does not assert the finite model property for unrestricted APAL, whose announcement quantifier has no modal-depth bound.

## Proof

**Finite type bound.** At depth zero, a pointed model's type is determined by its valuation on \(P\), so there are at most \(N_0=2^k\) types. Suppose there are at most \(N_r\) depth-\(r\) types. A depth-\((r+1)\) type is determined by (i) the valuation of the current world and (ii) for each of the \(m\) agents, the set of depth-\(r\) types realized in that agent's equivalence class. There are at most \(2^k\) choices for (i) and at most \(2^{N_r}\) choices for each agent's set in (ii). Hence there are at most

\[
2^k(2^{N_r})^m=2^{k+mN_r}=N_{r+1}
\]

depth-\((r+1)\) types. The induction proves the bound.

**Finite announcement basis.** The truth of every epistemic formula of modal depth at most \(d\) is determined by its depth-\(d\) type. Each such formula therefore defines a subset of a set with at most \(N_d\) types. There are at most \(2^{N_d}\) distinct such subsets, hence at most that many announcement-equivalence classes. Choose a set \(\Psi_{P,d}\) containing one representative from each class. If \(\psi\) and \(\chi\) are globally equivalent epistemic formulas, they have the same truth set in every model and induce the same updated model. Therefore

\[
\Box_d\varphi\ \equiv\ \bigwedge_{\psi\in\Psi_{P,d}}[\psi]\varphi.
\]

The conjunction is finite. By structural induction, replacing each bounded quantifier with this conjunction translates every \(\mathrm{APAL}_{P,d}\) formula into an equivalent public-announcement-logic formula. The induction also covers quantified operators nested inside public-announcement preconditions, because the preconditions are translated first.

**Finite model property.** Public announcement logic is reducible to the base epistemic language by its reduction axioms. Multi-agent \(\mathsf{S5}\) epistemic logic has the finite model property. The translated formula consequently has a finite \(\mathsf{S5}\) model whenever it is satisfiable, and the same finite model satisfies the original bounded-depth formula. This proves the claim.

## Verification

The type recurrence is an upper bound; no claim is made that it is exact. The finite-basis step uses global equivalence of announcements, not merely agreement at the evaluation point, so the induced updates agree on the whole model. The translation is finite for every formula because the representative set is finite and each formula has finite syntax. No computational experiment is needed for this symbolic argument.

## Relationship to prior work

Van Ditmarsch, French, and Galimullin prove that unrestricted APAL, group announcement logic, and coalition announcement logic lack the finite model property. Their proof explicitly uses the fact that quantified announcements may have arbitrary finite modal depth. The present result concerns a different, resource-bounded variant: the atom vocabulary and announcement modal depth are fixed and finite. Van Ditmarsch, Liu, Kuijer, and Sedlár study variants restricting the atom sets available to announcement quantifiers, but the checked results do not state this fixed-depth finite-basis theorem. The present claim does not imply that unrestricted APAL has the finite model property.

## Limitations

The bound \(N_r\) is only an upper bound on the number of types, and \(2^{N_d}\) is only an upper bound on the number of announcement classes. No optimal translation-size or complexity bound is claimed. The proof depends on a fixed finite atom vocabulary and a finite modal-depth bound; it does not settle the case of a fixed finite vocabulary with unbounded announcement depth. The semantics considered here is multi-agent \(\mathsf{S5}\).

## References

1. H. van Ditmarsch, T. French, and R. Galimullin, “No Finite Model Property for Logics of Quantified Announcements,” *Electronic Proceedings in Theoretical Computer Science* 335 (2021), 129–138. First public version: 22 June 2021. arXiv:2106.11498. DOI: 10.4204/EPTCS.335.12.
2. H. van Ditmarsch, M. Liu, L. B. Kuijer, and I. Sedlár, “Almost APAL,” *Journal of Logic and Computation* 33(6) (2023), 1350–1378. First public version: 25 November 2021. DOI: 10.1093/logcom/exac012.
