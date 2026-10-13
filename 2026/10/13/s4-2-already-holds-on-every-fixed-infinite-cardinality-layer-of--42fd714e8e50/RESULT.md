# S4.2 already holds on every fixed infinite-cardinality layer of abelian groups

## Finding

For every infinite cardinal \(\kappa\), let \(\mathscr A_\kappa\) be the class of abelian groups of cardinality exactly \(\kappa\). Put \(A\le B\) when \(A\) is isomorphic to a subgroup of \(B\). Then

\[
\operatorname{ML}_{\mathcal L_{\rm Gr}}(\mathscr A_\kappa,\le)=\mathsf{S4.2}.
\]

Moreover this is robust: for every \(\mathscr A_\kappa\)-adequate language \(\mathcal L\),

\[
\operatorname{ML}_\mathcal L(\mathscr A_\kappa,\le)=\mathsf{S4.2}.
\]

In particular, countable abelian groups alone already realize exactly the same structure modal logic as the class of all abelian groups.

## Assumptions and scope

The cardinal \(\kappa\) is infinite. Accessibility is subgroup embeddability up to isomorphism, exactly as in Berger--Block--Löwe. The statement concerns structure-modal validity under substitutions by first-order group sentences, and then the standard robustness sandwich extends the equality to every adequate language.

The result is not claimed for finite cardinalities. It also does not concern the open problem for all, not necessarily abelian, groups.

## Proof

Berger--Block--Löwe prove that on the class \(\mathscr A\) of all abelian groups, subgroup accessibility is reflexive, transitive, and directed, and that arbitrarily large finite independent families of first-order buttons and switches exist. Their buttons are

\[
\beta_p:=\exists x\,(x\ne0\wedge p x=0)
\]

for primes \(p\), and their switches are

\[
\sigma_q:=\forall x\,\exists y\,(q y=x)
\]

for primes \(q\). Their Lemma 3.2 says that for disjoint finite prime sets \(P,Q\), the family \(\{\beta_p:p\in P\}\cup\{\sigma_q:q\in Q\}\) is independent.

Fix an infinite \(\kappa\). First, \((\mathscr A_\kappa,\le)\) is directed. If \(|A|=|B|=\kappa\), then \(|A\times B|=\kappa\), and both \(A\) and \(B\) embed in \(A\times B\). Hence every theorem of \(\mathsf{S4.2}\) is valid on this frame.

For the converse, start with any \(A\in\mathscr A_\kappa\), any finite control family from Berger--Block--Löwe, and any target control pattern permitted by independence. Their construction gives some abelian extension \(A\le B\) realizing that target pattern; its cardinality need not equal \(\kappa\).

Identify \(A\) with its image in \(B\). By downward Löwenheim--Skolem in the first-order language of groups, there is an elementary subgroup \(C\preccurlyeq B\) containing the whole set \(A\) and satisfying

\[
|C|\le |A|+|\mathcal L_{\rm Gr}|=\kappa.
\]

Since \(A\subseteq C\), also \(|C|\ge\kappa\), so \(|C|=\kappa\). Thus \(C\in\mathscr A_\kappa\) and \(A\le C\).

Every \(\beta_p\) and \(\sigma_q\) is a first-order sentence, so elementarity gives

\[
B\models\beta_p\iff C\models\beta_p,
\qquad
B\models\sigma_q\iff C\models\sigma_q.
\]

Therefore exactly the same target control pattern is realizable by an extension that remains inside \(\mathscr A_\kappa\). Hence the Berger--Block--Löwe buttons and switches are still arbitrarily large and independent on each fixed-cardinality layer. The Hamkins--Löwe control-statement theorem then gives

\[
\operatorname{ML}_{\mathcal L_{\rm Gr}}(\mathscr A_\kappa,\le)\subseteq\mathsf{S4.2}.
\]

Combining the two inclusions proves equality. Finally, for any adequate language \(\mathcal L\), the usual valuation inclusions give

\[
\mathsf{S4.2}\subseteq \operatorname{ML}_\mathcal L(\mathscr A_\kappa,\le)
\subseteq \operatorname{ML}_{\mathcal L_{\rm Gr}}(\mathscr A_\kappa,\le)=\mathsf{S4.2},
\]

so the equality is robust.

## Verification

The proof was checked against the precise control-statement definitions, Berger--Block--Löwe's Lemma 3.2, and the standard downward Löwenheim--Skolem theorem with the entire starting group used as the parameter set. The cardinal arithmetic step uses only \(\kappa\cdot\kappa=\kappa\) and \(\kappa+\aleph_0=\kappa\) for infinite \(\kappa\).

The bundled verifier checks the finite control-pattern frame: buttons can only move from off to on, switches may be reset arbitrarily, the resulting reachability relation is reflexive, transitive, and directed, and its exact number of arrows is \(3^n4^m\). This finite check is not a substitute for the Löwenheim--Skolem step.

## Relationship to prior work

Berger, Block, and Löwe prove \(\mathsf{S4.2}\) for the class of all abelian groups and provide the specific independent controls used here. Their published construction is not cardinality preserving: the controlled amplification employs a full function group and can increase size.

Saveliev and Shapirovsky prove a downward Löwenheim--Skolem theorem for modal theories under the extension relation and, for elementary classes, identify the modal theory of the whole class with the subclass of structures of size at most \(\kappa\). That theorem is adjacent but does not state the present fixed-cardinality result. Equality on a size-bounded class does not by itself imply equality on its exact-\(\kappa\) sublayer, because restricting worlds can add modal validities. The argument above instead cardinal-corrects every Berger--Block--Löwe control extension while preserving its first-order control pattern.

Targeted exact-phrase, equivalent-formulation, broader-coverage, semantic-database, and owned-ledger searches found these ingredients but no theorem asserting \(\mathsf{S4.2}\) separately on every exact infinite cardinality of abelian groups.

## Limitations

The new step is short once Berger--Block--Löwe's independent controls and downward Löwenheim--Skolem are combined, so the result may exist as uncatalogued folklore. The proof depends on the controls being first-order sentences; it does not show that arbitrary non-first-order target properties can be cardinal-corrected by the same argument.

The 2023 article notes that its results form part of Sören Berger's 2018 Master's thesis. An exact day-level public release date for that thesis was not located in the checked sources; the metadata therefore uses the article's fully verified online publication date, 2023-07-26, as the precise public date attached to the inspected primary source.

## References

1. S. Berger, A. Christensen Block, and B. Löwe, *The modal logic of abelian groups*, Algebra Universalis 84 (2023), Article 25, DOI 10.1007/s00012-023-00821-9.
2. D. I. Saveliev and I. B. Shapirovsky, *On modal logics of model-theoretic relations*, Studia Logica 108 (2020), 989--1017, DOI 10.1007/s11225-019-09885-y; arXiv:1804.09810.
