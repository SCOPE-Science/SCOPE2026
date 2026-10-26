# Scientific review

## Correctness
**PASS.** The coordinate involution is threshold-defined using exclusively indices before the adjacent candidate times, so its swap-or-fix decision is symmetric and invariant under the transposition. Exchangeability gives equality of laws even with ties and dependence. On every input it preserves the ordered full-record-height list and the multiset, and it exchanges the relevant final selected-record indicator. Repeated adjacent moves establish the exact joint-law claim. The iid atomless specialization uses uniform independent insertion ranks; its covariance and correlation calculations have no omitted future contributions. Exact finite checks were performed with the included standalone checker; they are not substitutes for the all-size proof.

## Originality
**PASS on inspected evidence; historical priority uncertain.** Falk, Khorrami Chokami and Padoan (2017, arXiv:1707.06254) treat two/three prescribed *full-record events* and corresponding record-value distributions, rather than the joint distribution of all full-record heights with the record count of a sparsely observed subsequence. Li (2022, arXiv:2208.06791) treats discrete recent-window records rather than arbitrary sparse retained observations. Searches and comparisons against related published record-indicator and record-kill claims found no matching statement. A general 2016 finite record-position paper was available only at abstract level; that source and implicit earlier permutation arguments remain risks.

## Value
**PASS.** This is an all-distribution non-identifiability theorem for the last measurement time in record-based incomplete-observation designs. It retains the complete record-height sequence and full-sample multiset as auxiliary information, and therefore explains why much stronger observations than a marginal record count cannot resolve the final retained position. The two-observation formula shows sharply why the analogous invariance fails when the *first* retained position moves.

## Limits
The result concerns strict upper-record *heights*, not record occurrence times, and fixes all selected times other than the final one. Independence of the retained count from full-record information is not claimed. The explicit covariance requires iid atomless data, though the joint-law theorem does not. Independent historical-priority verification is still required before asserting definitive novelty.

Self-review: passed. Independent audit: not yet performed.
