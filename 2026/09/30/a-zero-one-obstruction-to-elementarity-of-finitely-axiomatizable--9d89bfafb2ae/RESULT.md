# A zero-one obstruction to elementarity of finitely axiomatizable modal logics
## Finding
Let \(L\) be a finitely axiomatizable normal unimodal logic. If \(L\) is elementary, then its finite-frame validity class obeys a zero-one law under the standard uniform distribution on labelled finite Kripke frames: if \(P_n(L)\) is the fraction of binary relations on \(\{1,\ldots,n\}\) whose frames validate \(L\), then
\[
\lim_{n\to\infty} P_n(L)\in\{0,1\}.
\]
Therefore, if \(P_n(L)\) has no limit, or has a limit strictly between \(0\) and \(1\), then \(L\) is not elementary.

In particular, let \(\varphi_{\mathrm{LB}}\) denote the MODAL-KERNEL formula used by Le Bars to prove failure of the zero-one law for modal frame validity. Le Bars proved that the finite-frame validity probability of \(\varphi_{\mathrm{LB}}\) has no asymptotic limit. Hence the one-axiom normal logic \(K+\varphi_{\mathrm{LB}}\) is non-elementary, unconditionally.

## Assumptions and scope
A Kripke frame is a nonempty finite set equipped with one binary accessibility relation. For each \(n\), frames are labelled on \(\{1,\ldots,n\}\) and sampled uniformly from all binary relations, equivalently each ordered pair is independently an edge with probability \(1/2\). A normal modal logic is elementary when it is sound and complete with respect to some first-order definable class of Kripke frames. “Finitely axiomatizable” means finitely axiomatizable over the basic normal modal logic \(K\).

The recent input is Takahashi’s arXiv preprint arXiv:2609.10872v1. Its Lemma 2.5 constructs, for every finitely axiomatizable elementary \(L\), a finitely axiomatizable elementary frame class whose finite members are exactly the finite frames validating \(L\). Older zero-one-law literature is used only to supply the classical first-order theorem and the explicit modal counterexample.

## Proof
Assume that \(L\) is finitely axiomatizable and elementary. By Takahashi’s Lemma 2.5, there is a frame class \(\mathcal K\) axiomatized by finitely many first-order sentences such that the finite members of \(\mathcal K\) are exactly the finite Kripke frames validating \(L\). Conjoin those finitely many sentences into one first-order sentence \(\alpha\). Thus, for every finite frame \(F\),
\[
F\models L \quad\Longleftrightarrow\quad F\models\alpha.
\]

The classical first-order zero-one law for finite relational structures applies to the single binary relation of a Kripke frame. Hence the probability that a uniformly random labelled \(n\)-point frame satisfies \(\alpha\) converges to either \(0\) or \(1\). Because the two finite-frame classes are identical for every \(n\), the same is true of \(P_n(L)\). Taking the contrapositive proves the obstruction.

For the explicit instance, Le Bars exhibited a modal formula \(\varphi_{\mathrm{LB}}\) whose frame-validity probability on uniformly random finite frames has no asymptotic probability. Let \(L_{\mathrm{LB}}=K+\varphi_{\mathrm{LB}}\). This logic is finitely axiomatizable. A frame validates \(L_{\mathrm{LB}}\) exactly when it validates \(\varphi_{\mathrm{LB}}\): all axioms of \(K\) are valid on every Kripke frame, and the normal inference rules preserve frame validity. Therefore \(P_n(L_{\mathrm{LB}})\) is exactly the Le Bars sequence, which has no limit. The obstruction above gives that \(L_{\mathrm{LB}}\) is non-elementary without any complexity-theoretic assumption.

## Verification
The proof was reconstructed from the finite-frame equivalence in Takahashi’s Lemma 2.5, the standard first-order zero-one law, and the published Le Bars counterexample as summarized by Goranko. The quantifiers are over all finite labelled frames and the conclusion concerns only elementarity of finitely axiomatizable normal unimodal logics. The argument does not use \(P\ne NP\).

Edge cases were checked: allowing or forbidding the empty frame does not affect the asymptotic statement; the random-frame model is the ordinary uniform model for a finite binary relational vocabulary; and the passage from a finite first-order theory to one sentence is by finite conjunction.

## Relationship to prior work
Takahashi proves the weaker necessary condition that finite-frame validity is decidable in polynomial time for finitely axiomatizable elementary modal logics and uses it to obtain conditional non-elementarity results assuming \(P\ne NP\). His proof already yields the stronger finite first-order definition on finite frames, but the zero-one consequence is not stated there.

Le Bars proved that the zero-one law fails for modal frame validity, and Goranko later highlighted the MODAL-KERNEL example in work on almost-sure frame validities. Those works predate Takahashi’s finite-frame reduction and do not draw the elementarity consequence above. The new point is the combination: Takahashi’s reduction transports the classical first-order zero-one law to every finitely axiomatizable elementary modal logic, turning any modal zero-one counterexample into an unconditional non-elementarity certificate.

## Limitations
This criterion does not by itself settle Takahashi’s open K4-stable examples: the Le Bars counterexample is used over unrestricted Kripke frames, whereas random transitive frames have a different asymptotic theory. The claim is also tied to finite axiomatizability, exactly as in Takahashi’s reduction. Finally, the originality statement is best-of-knowledge rather than an exhaustive bibliographic theorem: no checked source stated this combination, but older or inaccessible literature could contain an equivalent observation.

## References
1. Tenyo Takahashi, “Non-elementary modal logics, assuming \(P\ne NP\),” arXiv:2609.10872v1, submitted 9 September 2026. In particular Lemma 2.5 and Theorem 2.7.
2. Jean-Marie Le Bars, “The 0-1 law fails for frame satisfiability of propositional modal logic,” Proceedings of LICS 2002, pp. 225–234.
3. Valentin Goranko, “The Modal Logic of Almost Sure Frame Validities in the Finite,” Advances in Modal Logic 13, 2020, pp. 249–268.
4. Ronald Fagin, “Probabilities on finite models,” Journal of Symbolic Logic 41(1), 1976, pp. 50–58.
