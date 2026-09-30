# Independent audit — 2026-09-29

Record: `2026/09/18/fixed-alphabet-qary-deletion-coefficient-2t-minus-1--bf884156e5ce`  
Assigned and audited source tree: `0ac26142df2b32be17c04515ffa0d15c917d4b76`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **repaired**

## Correctness

**supported**. The q-ary extension itself is correct. The primary En Gad proof was checked through the bubble catalogue, witness extraction and counting lemmas. Replacing the binary boundary symbol 1-d by arbitrary left/right symbols unequal to d preserves the two endpoint contradictions in Lemma 2.6. In Lemma 5.1, the edited bit becomes one of q symbols and the optional transferred bit becomes one q-ary symbol; for fixed q this is only a constant-per-rule factor. The record's choice k=2 ceil(log_2 n)+2 is conservative for q>2 and keeps En Gad's n<=2^R large-witness absorption literally available. An independent rerun of the packaged local verifier reproduced all 42 overlap-probability cases, 2,783,928 q-ary bubble cases and 32,642,112 offset comparisons with PASS. Thus the theorem and proof survive; the needed repair is to the originality/provenance framing, not the mathematics.

## Originality

**duplicate_with_earlier_scope_record**. This record cannot be retained as a separate original SCOPE discovery. Repository history shows that the substantively identical record `fixed-qary-deletion-codes-2t-minus-1--0b8ba422fcea` was committed at 2026-09-18 04:23:02 UTC, whereas this record was first committed at 2026-09-18 19:28:14 UTC, about fifteen hours later. Both prove the same fixed-q, fixed-t redundancy coefficient 2t-1 by the same q-ary adaptation of En Gad's method. The later record does have a separate finite verification artifact and a slightly more conservative k scale, so it is useful as corroboration, but its current text's distinct-new-contribution framing is false relative to the repository's prior record and must be removed.

## Scientific value

**corroborating_after_repair**. After provenance repair, the record has value as an independently written same-day corroboration of the earlier SCOPE theorem and as a reproducibility package for the local q-ary bubble step. It should not be counted as an additional novel theorem or discovery.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/fixed-alphabet-qary-deletion-coefficient-2t-minus-1--bf884156e5ce
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/fixed-qary-deletion-codes-2t-minus-1--0b8ba422fcea
- https://github.com/SCOPE-Science/SCOPE2026/commit/16286e5fce08fe8b0dfd1d35cec5c21c696f587b
- https://github.com/SCOPE-Science/SCOPE2026/commit/c4a347eb8acfce1ceee4652e749e43e2c5fa463b
- https://arxiv.org/abs/2609.19493

## Limitations

- This is not a separately original research result because the same theorem already existed in the repository before this record was committed.
- The theorem remains existential, with fixed q and t and an O_{q,t}(log log n) correction.
- The local verifier is corroborative; the general theorem rests on the analytic adaptation of En Gad's witness and counting argument.
- The motivating binary preprint is extremely recent, so external priority remains qualified even for the earlier SCOPE record.
