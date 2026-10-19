# Self-review

## Correctness — PASS

The finite lemma is a complete ternary enumeration of all \(3^n\) words through length thirteen, not sampling. Two independent exact profile constructions agree on every nonsingleton word pair, verify the length-thirteen twelve-doubleton census and the support-two property, and confirm injectivity from lengths three through twelve. The proof independently converts this finite classification into an all-alphabet statement using deterministic projections. No finite computation is used as an unjustified proof for arbitrary alphabet size.

## Originality — PASS against inspected literature, with residual risk

Golm et al. (2022, arXiv:2201.12671) already establish the binary \(G(3)=13\) threshold and a witness. The full **four binary doubletons** are also known from an earlier binary classification; neither this binary result nor the shorter-length injectivity is claimed as new. Rigo et al. (2023, ISIT, DOI 10.1109/ISIT54713.2023.10206676) study related binomial equivalence in languages of infinite words. The new point is the nonexistence of any length-thirteen ambiguous q-ary pair whose combined alphabet uses three or more symbols, which forces the exact family of \(4inom q2\) doubletons on every \(q\)-symbol alphabet. Relevant search results did not reveal a broader theorem implying this conclusion. An inaccessible or unindexed equivalent result is a remaining bibliographic risk.

## Mathematical value — PASS

Alphabet-robust unique reconstruction and the exact confusability census matter directly to selecting codebooks for a gapped-read channel. The first nontrivial ambiguity boundary is a natural finite cutoff, and the four-symbol specialization is a meaningful DNA-alphabet case. The theorem supplies the exact optimum and counts all labeled maximum codebooks, not merely one new collision witness.

## Limitations

Computationally assisted finite base case; no independent audit, no claimed efficient encoder, and no classification beyond length thirteen. The full code and exact proof reduction are supplied.

Self-review: passed. Independent audit: not yet performed.
