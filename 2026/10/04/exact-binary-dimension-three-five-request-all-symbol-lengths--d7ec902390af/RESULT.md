# Exact binary dimension-three five-request all-symbol lengths
## Finding
Over \(\mathbb F_2\), the exact minimum lengths for five-request all-symbol PIR and all-symbol batch codes of dimension \(3\) are both \(10\): \(\operatorname{ASP}(3,5,2)=\operatorname{ASB}(3,5,2)=10\). A length-\(10\) witness has column multiplicities \((0,1,1,2,2,2,2)\) on the seven nonzero vectors of \(\mathbb F_2^3\), and no rank-\(3\) binary generator multiset of length at most \(9\) satisfies the five-all-symbol PIR property.

Here \(\operatorname{ASP}(k,t,q)\) is the minimum length of a \(k\)-dimensional \(t\)-all-symbol PIR code over \(\mathbb F_q\), and \(\operatorname{ASB}(k,t,q)\) is the analogous minimum for all-symbol batch codes. For a generator matrix \(G\), the PIR condition requires five pairwise disjoint recovery sets for five copies of each column of \(G\); the batch condition requires pairwise disjoint recovery sets for every multiset of five columns of \(G\).

## Assumptions and scope
The statement is only for binary linear codes of dimension \(3\) and exactly five requests. Zero columns can be deleted from a minimum-length realization without decreasing rank or invalidating any requirement on the remaining stored symbols, so a minimum realization may be assumed to use only the seven nonzero vectors of \(\mathbb F_2^3\).

A generator multiset is therefore represented exactly by a seven-entry multiplicity vector. Recovery is by linear span, with no restriction on recovery-set size in the definition. It is enough to enumerate inclusion-minimal recovery sets: shrinking any recovery set to an inclusion-minimal subset preserves its target and cannot destroy pairwise disjointness. In dimension \(3\), every inclusion-minimal spanning set is linearly independent and hence has at most three columns.

## Proof
For the lower bound, enumerate every seven-entry nonnegative multiplicity vector of total length \(n\in\{3,4,5,6,7,8,9}\), expand it to a multiset of nonzero columns of \(\mathbb F_2^3\), and retain exactly the rank-\(3\) multisets. For each stored column type, enumerate every inclusion-minimal recovery set of sizes one, two, or three and test whether five pairwise disjoint such sets exist.

The exact numbers of rank-\(3\) multiplicity vectors checked, with the number satisfying five-all-symbol PIR in parentheses, are
\[
28\ (0),\ 119\ (0),\ 329\ (0),\ 742\ (0),\ 1478\ (0),\ 2702\ (0),\ 4634\ (0)
\]
for \(n=3,4,5,6,7,8,9\), respectively. Thus no binary dimension-three five-all-symbol PIR code has length at most \(9\), so \(\operatorname{ASP}(3,5,2)\ge 10\).

For the upper bound, identify the seven nonzero vectors with the nonzero three-bit integers \(1,\ldots,7\). Use the ten columns
\[
(2,3,4,4,5,5,6,6,7,7),
\]
whose multiplicity vector is \((0,1,1,2,2,2,2)\). This matrix has rank \(3\). Its six distinct stored column types yield exactly
\[
\binom{6+5-1}{5}=252
\]
multisets of five requested stored symbols. Exhaustive exact search finds five pairwise disjoint recovery sets for every one of the \(252\) multisets. The accompanying certificate records one complete recovery assignment for each request multiset, and the verifier checks every recorded span and every disjointness condition. Hence \(\operatorname{ASB}(3,5,2)\le 10\). Since \(\operatorname{ASP}(3,5,2)\le\operatorname{ASB}(3,5,2)\), the lower and upper bounds meet at \(10\).

## Verification
Run `python3 artifacts/verify.py`. The verifier uses only the Python standard library. It reconstructs every rank-\(3\) multiplicity vector of lengths \(3\) through \(9\), reconstructs all inclusion-minimal recovery sets from the columns themselves, and independently checks the length-\(10\) witness. It also reads `artifacts/witness_certificate.json` and verifies that its \(252\) request rows are complete and unique, that each row has exactly five recovery sets, that the target multiset matches the request, that the recovery sets are pairwise disjoint, and that each recovery set spans its target.

The expected terminal marker is `VERIFY_OK ASP(3,5,2)=ASB(3,5,2)=10`.

## Relationship to prior work
Boruchovsky, Gruica, Niemann, and Yaakobi introduce \(t\)-all-symbol PIR and batch codes and the notation \(\operatorname{ASP}(k,t,q)\) and \(\operatorname{ASB}(k,t,q)\) in arXiv:2601.04041. Their Proposition 13 gives, at \((k,t,q)=(3,5,2)\), only
\[
8\le \operatorname{ASP}(3,5,2)\le \operatorname{ASB}(3,5,2)\le 10.
\]
Their discussion of future directions states that exact minimum lengths are known only for \(t\in\{1,2,3}\) with partial results for \(t=4\), and specifically identifies optimal lengths at small dimension as open. The present exact value closes the three-point interval at this first five-request binary dimension-three instance.

The same paper notes that the \((t,s)\)-disjoint-repair-group property with \(s=n\) coincides with \((t+1)\)-all-symbol PIR. Thus the PIR half can equivalently be phrased as a small-parameter four-disjoint-repair-group statement. The 2022 paper of Karingula, Vardy, and Wootters develops general redundancy lower bounds for disjoint repair groups; the 2026 source imports from that line of work an exact all-symbol result only for three requests. No inspected source supplied the exact five-request dimension-three value above.

A published published-finding corpus entry on dimension-three four-request all-symbol lengths gives the binary four-request value \(7\). By strict monotonicity, that implies only the lower bound \(8\) for five requests and does not determine the value \(10\).

## Limitations
The proof is a finite exact classification only for \((k,t,q)=(3,5,2)\). It does not claim a formula for larger dimension, more requests, or nonbinary alphabets. The originality search cannot exclude every unindexed or differently notated older small-parameter computation; the strongest residual risk is literature phrased entirely in disjoint-repair-group or availability terminology. The 2026 paper's literature review and explicit small-dimension open direction reduce, but do not eliminate, that risk.

## References
1. A. Boruchovsky, A. Gruica, J. Niemann, and E. Yaakobi, “Serving Every Symbol: All-Symbol PIR and Batch Codes,” arXiv:2601.04041v2, 2026. Relevant items: Definition 2, Notation 4, Proposition 10, Proposition 13, Section 5.
2. S. R. Karingula, A. Vardy, and M. Wootters, “Lower bounds on the redundancy of linear codes with disjoint repair groups,” IEEE ISIT 2022, pp. 975–979, DOI 10.1109/ISIT50566.2022.9834487.
3. published-finding corpus record `2026/9/17/SCOPE-dimension-three-four-request-all-symbol-lengths--a938eedf9b5f`, “Exact dimension-three four-request all-symbol code lengths.”
