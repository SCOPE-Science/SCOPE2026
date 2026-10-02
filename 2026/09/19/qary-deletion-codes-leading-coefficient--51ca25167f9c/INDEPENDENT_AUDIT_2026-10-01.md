# Independent Audit — The 2t-1 deletion-code redundancy coefficient extends to q-ary alphabets

**Audit date:** 2026-10-01 (UTC) (UTC)  
**Disposition:** passed

## Correctness — PASS

The transfer keeps every alphabet-dependent factor inside \(q^{O_t(R)}\) description counts while the substring-hash range retains the \(n^{2t-1}\) exponent. The k-uniqueness scale is chosen using \(\log_2 n\), so its density estimate is uniform in \(q\); q-ary local bubbles still have coefficients in \(\{-1,0,1\}\) once boundary symbols differ from the edited symbol; and the exceptional overlap records add only fixed powers of \(q\), absorbable into the constant exponent \(A_t\). Thus the probabilistic label-class argument yields constants depending on \(t\) but not on \(q\). The committed finite verifier is only a sanity check and is not used as proof.

## Originality — PASS

The motivating En Gad paper proves the binary \((2t-1)\)-coefficient theorem. The earlier published q-ary record proves the same leading coefficient only for fixed \(q\), with constants allowed to depend on \(q\); it explicitly does not provide the audited uniform-in-\(q\) dependence. Targeted searches also found q-ary burst-deletion and read-channel results, but those solve different error models. No prior statement found implies a uniform bound with constants independent of \(q\).

## Scientific value — PASS

Uniformity in the alphabet size is a natural strengthening of the fixed-alphabet theorem, not a cosmetic parameter change: it controls how the construction behaves when \(q\) itself varies and removes hidden alphabet dependence from the redundancy statement. That directly answers the larger-alphabet extension problem identified around the new binary bound and is a reusable coding-theoretic fact.

## Source inspections

- Assigned proof and metadata were inspected from the frozen Git blobs.
- The earlier fixed-q q-ary SCOPE result was read in full and compared parameter-by-parameter.
- En Gad abstract/open metadata were inspected; direct and open full-text routes failed, and institutional retrieval was unavailable.
- A q-ary burst-deletion paper was inspected sufficiently to confirm that its channel model is not ordinary arbitrary deletions.

## Residual risks

- Full text of arXiv:2609.19493 was inaccessible in this run; this is recorded as an access risk, not used as proof of novelty.
