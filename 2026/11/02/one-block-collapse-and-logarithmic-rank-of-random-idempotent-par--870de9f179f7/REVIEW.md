# Self-review

## Correctness — PASS

For any idempotent character on the \(r\) labeled blocks, its rooted basin sizes \(c_j\) partition \(r\). The fixed points of each rooted image block form an arbitrary nonempty subset; every other point in its basin may map to those fixed points. This independently yields exactly \(\prod_j H_{c_j}(m)\), with \(H_c(m)=\sum_{k=1}^m\binom mk k^{cm-k}\). A uniform compact-scale logarithmic estimate and explicit small- and large-image-size tail bounds yield \(\log H_c(m)=cm(\log m-\log\log m+\log c-1)+o(m)\) and rank concentration at \(cm/\log m\). The strict entropy maximum among nonconstant idempotent characters occurs at basin sizes \((r-1,1)\), with precisely \(r(r-1)\) representatives when \(r\ge3\) and one when \(r=2\); all other shapes are exponentially negligible. The resulting probability and conditional-rank claims follow with correct fixed-\(r\) quantifiers. A direct-map verifier confirmed the character formula in ten small finite cases; asymptotic proof does not depend on numerical convergence.

## Originality — PASS relative to inspected evidence

Dolinka–East (arXiv:1407.3312, 2014, especially Propositions 3.1–3.2) already classify and enumerate all idempotents of a uniform-partition transformation monoid. This fact is not claimed new. The inspected paper develops finite enumerations and tables but does not prove the fixed-number-of-blocks, growing-block-size concentration on a constant character, the precise logarithmic rare-event decay rate, the conditional \((r-1,1)\) shape, or image-rank concentration. Sarkar–Singh (arXiv:2310.19414, 2023, especially Proposition 3.9) proves a general idempotent-character criterion and regularity results, not this probability law. Dolinka–East–Mitchell (arXiv:1504.02520, 2015) studies nonuniform partition idempotent-generating ranks, not the present rank statistic and limit. The 2017 Al-aadhami thesis abstract was examined but its complete body was not, leaving a specific publication-priority risk. A derived asymptotic from a published finite count is not automatically original: the novel work here is the nontrivial \(m\)-scale Laplace and strict competing-shape analysis, establishing information absent from the inspected statements.

## Mathematical value — PASS

Conditional idempotence gives a highly nonuniform distribution on the finite wreath-product/partition endomorphism monoid. The theorem resolves a natural typical-structure problem by proving that almost every idempotent collapses *all* blocks to a single image block, quantifies the probability of failure at an explicit exponential rate, identifies the overwhelmingly dominant failure morphology, and shows the typical image contains about \(rm/\log m\) points. These are structural distributional invariants for the complete fixed-\(r\) family, not routine small parameter substitutions or re-publication of known finite counts. The asymptotic scale and shape require analysis rather than direct inspection of prior counting formulas.

## Closest literature and remaining limitations

Primary references: Dolinka–East, 2014, arXiv:1407.3312; Sarkar–Singh, 2023, arXiv:2310.19414; Dolinka–East–Mitchell, 2015, arXiv:1504.02520. The accessible 2017 York doctoral thesis abstract for Al-aadhami was also reviewed but not its full text. The result assumes a fixed number of equally sized blocks and makes no assertion about simultaneous growth or non-idempotents. The theorem gives a sharp logarithmic decay rate; it does **not** claim a fixed prefactor for the pure exponential form. Global publication priority is not certified.

Self-review: passed. Independent audit: not yet performed.
