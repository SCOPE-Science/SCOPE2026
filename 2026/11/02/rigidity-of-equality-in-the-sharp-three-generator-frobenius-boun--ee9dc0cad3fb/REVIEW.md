# Scientific review

**Correctness — PASS.** The proof uses the Kneser covering lemma for \(\{0,a,b\}\) in \(\mathbb Z/c\mathbb Z\), the minimal Apéry representatives, and a one-unit deficit argument to force \(b=a+1\). The exhaustive remaining cases distinguish \(a=1\), \(c<2a\), \(c=2a\), and \(c>2a\). The separate arithmetic verifier passes all \(116920\) coprime triples with \(c\le95\); these tests are only diagnostics.

**Originality — PASS, with residual priority risk.** Chen–Hu–Mao–Zhang (arXiv:2610.32219v1) state the bound and a sharpness family, not the converse. Aguiló–Miralles (doi:10.46298/dmtcs.3462) classify maximizers for a different bound determined by the fixed largest generator alone, not equality with the new bound retaining the second largest. The Hamidoune–Plagne inverse-additive paper is relevant to the proof method but no equivalent Frobenius classification was identified in the material inspected. A 1998 paper on the Frobenius problem by Hamidoune remains uninspected in full, and unindexed prior implications remain possible.

**Mathematical value — PASS.** A complete equality classification is a natural next question after a sharp bound. The new rigidity states that no irredundantly three-generated numerical semigroup is an equality case and exposes the additional unit-generator family. It does not claim a quantitative deficit or stability theorem.

**Limits.** Correctness is assessed by the proof rather than by finite experiments. Novelty is a best-knowledge comparison, not certified priority. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
