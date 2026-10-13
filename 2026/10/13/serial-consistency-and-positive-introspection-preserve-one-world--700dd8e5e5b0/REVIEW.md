# Review

## Correctness

PASS. Define the generated set at a one-world canonical model by finite boxed proof consequences: a formula \(\chi\) belongs exactly when finitely many boxed generator formulas prove \(\Box\chi\). For a full maximal consistent set this gives the exact bridge \(\chi\in\operatorname{cl}(G)\) if and only if \(\Box\chi\) belongs to the maximal set, so the standard Boolean induction gives the truth lemma and strong completeness.

The semantic conditions for \(\mathsf M\), \(\mathsf C\), \(\mathsf N\), \(\mathsf K\), and \(\mathsf{4}\) follow by composing finite proof supports with the selected axiom. For \(\mathsf D\), if both \(\chi\) and \(\neg\chi\) were generated, the union of their finite supports would derive both \(\Box\chi\) and \(\Box\neg\chi\), contradicting the selected \(\mathsf D\) axiom inside the consistent canonical set. The same argument works on a finite augmented subformula maximal set for a single non-theorem, where the generator is finite. Nishimura's notion of finiteness allows the generated closure itself to remain infinite.

## Originality

PASS. Nishimura's 2026 paper proves the singleton completeness mechanism only for selections from \(\mathsf M\), \(\mathsf C\), \(\mathsf N\), and \(\mathsf K\), and explicitly names \(\mathsf D\) and \(\mathsf{4}\) as prospective extensions. The retained theorem handles both simultaneously and uniformly across every no-rule selection, including \(\mathsf D\) together with Nishimura's axiom \(\mathsf N\).

Kogure--Kurahashi already give the natural membership conditions for \(\mathsf D\) and \(\mathsf{4}\) and prove completeness in an older closure semantics, but their closures are required to be extensive, monotone, and idempotent, their \(\mathsf N\) is the necessitation inference rule, and their axiom family does not contain Nishimura's \(\mathsf M\)/\(\mathsf K\) no-rule hierarchy. Their theorems therefore do not imply the arbitrary-operator singleton result retained here. Candidate-specific published-result searches under the principal aliases found no covering statement.

## Value

PASS. The primary source explicitly identifies extension to \(\mathsf D\) and \(\mathsf{4}\) as a first research direction. The result resolves those two principles together for the entire no-inference-rule hierarchy and shows that the negative consistency condition \(\mathsf D\) does not destroy the strongest finite phenomenon already present in the source: a single world with a finite generator suffices for every non-theorem. The proof-consequence closure also isolates a reusable mechanism for mixing Horn-like and consistency-style closure constraints.

## Closest literature and limitations

The closest prior source is Kogure--Kurahashi (2026), which studies \(\mathsf D\) and \(\mathsf{4}\) with genuine closure operators and necessitation-based provability logics. The closest same-framework source is Nishimura (2026), which supplies the broad arbitrary-operator semantics and the finite one-world construction for \(\mathsf M\), \(\mathsf C\), \(\mathsf N\), and \(\mathsf K\) but leaves \(\mathsf D\) and \(\mathsf{4}\) for future work.

The retained theorem excludes modal inference rules and does not establish effective decidability or a complexity classification for the extended systems.

Self-review: passed. Independent audit: not yet performed.
