# A two-world negative answer to existential definability over upward neighborhood models

## Finding

In inquisitive neighborhood logic, the binary neighborhood conditional \(\varphi\Rrightarrow\psi\) cannot be defined using only the existential neighborhood modality \(\mathsf E\) and the inquisitive propositional connectives, even over **upward-monotone** inhabited neighborhood models. A single two-world frame witnesses the failure, and two worlds are the least possible finite size. This negatively answers the first question of Ciardelli's Open Problem 4.6; the separate definability question involving two unary modalities over convex models is not addressed.

## Assumptions and scope

An inhabited neighborhood model is \(M=(W,\Sigma,V)\), where \(W\ne\varnothing\), \(\Sigma(w)\) is a collection of nonempty subsets of \(W\), and \(V\) assigns Boolean truth values to atoms at each world. An information state \(s\subseteq W\) supports atoms by universal truth at every point, supports \(\bot\) exactly when it is empty, supports conjunction conjunctively, supports inquisitive disjunction \(\varphi\sqcup\psi\) when it supports either disjunct, and supports implication \(\varphi\to\psi\) when every subset supporting the antecedent supports the consequent. The empty information state supports every formula. Modal formulas are truth-conditional: a state supports them exactly when each of its worlds satisfies them.

The existential modality has semantics
\[
M,w\models\mathsf E\varphi\quad\Longleftrightarrow\quad
\exists s\in\Sigma(w)\;M,s\models\varphi.
\]
The binary strict conditional has semantics
\[
M,w\models\varphi\Rrightarrow\psi\quad\Longleftrightarrow\quad
\forall s\in\Sigma(w)\;(M,s\models\varphi\implies M,s\models\psi).
\]
A frame is upward-monotone if \(s\in\Sigma(w)\) and \(s\subseteq t\subseteq W\) together imply \(t\in\Sigma(w)\). The existential-only language permits arbitrary atoms, \(\bot\), \(\wedge\), \(\sqcup\), \(\to\), and arbitrary finite nesting of \(\mathsf E\), but no binary strict conditional or universal neighborhood modality. Abbreviate \(\neg\varphi:=\varphi\to\bot\), \(\top:=\neg\bot\), and \(?p:=p\sqcup\neg p\).

## Proof

**Singleton-generator lemma.** Fix a world \(a\) such that
\[
\Sigma(a)=\{s\subseteq W:a\in s\}.
\]
For every existential-only formula \(\theta\),
\[
M,a\models\mathsf E\theta\quad\Longleftrightarrow\quad M,a\models\theta.
\]
Indeed, if some \(s\in\Sigma(a)\) supports \(\theta\), persistence of inquisitive support under taking subsets implies that \(\{a\}\subseteq s\) supports \(\theta\). Conversely, \(\{a\}\in\Sigma(a)\), so its support witnesses the existential modality. By truth/support coincidence on a singleton, the equivalence follows. Moreover, a simultaneous structural induction proves that the truth of **every** existential-only formula at \(a\) depends only on the values of its atoms at \(a\): for atoms and \(\bot\) this is immediate; conjunction and inquisitive disjunction are local on the singleton; implication at \(\{a\}\) quantifies only over \(\varnothing\) and \(\{a\}\), and the empty state supports everything; and the modal step reduces \(\mathsf E\theta\) to \(\theta\) by the displayed equivalence. This lemma is uniform over nesting depth and all other valuations and neighborhood assignments.

**Two-world witness.** Let \(W=\{a,b\}\) and choose
\[
\Sigma(a)=\{\{a\},\{a,b\}\},\qquad
\Sigma(b)=\{\{b\},\{a,b\}\}.
\]
These neighborhood families contain only nonempty sets and are upward-monotone. In both models take \(p(a)=1\) and fix the same values for every other atom at \(a\). Let \(M_+\) have \(p(b)=1\) and \(M_-\) have \(p(b)=0\); all other valuations may be identical. By the singleton-generator lemma, every existential-only formula has the same truth value at \(a\) in \(M_+\) and \(M_-\). However, every neighborhood supports \(?p\) in \(M_+\), since \(p\) is constant there. In \(M_-\), the neighborhood \(\{a,b\}\) does not support \(?p\), since it supports neither \(p\) nor \(\neg p\). Every neighborhood supports \(\top\). Therefore
\[
M_+,a\models\top\Rrightarrow?p,\qquad
M_-,a\not\models\top\Rrightarrow?p.
\]
No existential-only formula can be equivalent to this conditional over all upward-monotone models. The conclusion already holds on this fixed frame.

**Sharpness in world count.** On a one-world inhabited frame \(W=\{a\}\), its neighborhood family is either \(\varnothing\) or \(\{\{a\}\}\). In the first case every binary strict conditional is true and \(\mathsf E\top\) is false. In the second, \(\mathsf E\top\) is true, while at \(a\), \(\varphi\Rrightarrow\psi\) is equivalent to the ordinary inquisitive implication \(\varphi\to\psi\), as the empty subset automatically supports both formulas. Thus, uniformly across all one-world models,
\[
\varphi\Rrightarrow\psi\quad\equiv\quad
\neg\mathsf E\top\;\sqcup\;(\varphi\to\psi).
\]
The equivalence holds in world truth and hence in support on both possible information states. Recursively replacing conditional occurrences from inside out gives a translation of any full-language formula into the existential-only language on one-world frames. Hence no one-world separation is possible.

## Verification

A standalone executable checker `check_inq_kite.py` computes inquisitive support directly, including implication over every substate. It checks both sides of the two-world separation, the locality and modal-collapse identities on many independently generated formulas, and the one-world elimination identity for sampled formulas on both possible singleton frames. Run with `python check_inq_kite.py`. Its successful run reports 22,584 assertion groups. Finite tests are corroboration only: the quantified result follows from the structural induction and explicit semantics above.

## Relationship to prior work

Ciardelli, *Inquisitive Neighborhood Logic*, Section 4, Open Problem 4.6, asks whether the binary conditional is definable from the existential neighborhood modality over upward-monotone models. Proposition 4.3 proves upward-closure invariance of existential formulas, while Corollary 4.4 separates the full language from its unary fragments over **arbitrary** neighborhood models. Neither statement alone gives nondefinability **restricted to upward-monotone models**. Proposition 4.5 treats a different direction: definability from the universal modality on downward-monotone frames. The present argument makes the upward restriction explicit and produces a smallest-size frame witness rather than applying an unrestricted-class separation.

## Limitations

The result applies to Ciardelli's inhabited neighborhood support semantics and to definability from the **existential modality alone**. It does not answer the other half of Open Problem 4.6, concerning both unary modalities over convex models. The proof establishes mathematical nondefinability, not a computational complexity classification. An independently discovered or unindexed equivalent result remains a literature risk.

## References

Ivano Ciardelli, *Inquisitive Neighborhood Logic*, arXiv:2411.04031 (first public submission November 6, 2024), especially Sections 2–4 and Open Problem 4.6. https://arxiv.org/abs/2411.04031

Ivano Ciardelli, *Inquisitive Neighborhood Logic*, Journal of Logic, Language and Information 34 (2025), 419–461, DOI: 10.1007/s10849-025-09440-0. Open-access full text: https://link.springer.com/article/10.1007/s10849-025-09440-0
