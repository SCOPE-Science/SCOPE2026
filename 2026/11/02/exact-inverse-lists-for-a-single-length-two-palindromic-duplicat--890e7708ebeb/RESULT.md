# Exact inverse lists for a single length-two palindromic duplication

## Finding
Fix an alphabet \(\Sigma\) of cardinality \(q\ge 2\). A length-two palindromic duplication maps \(u a b v\) to \(u a b b a v\), where \(a,b\in\Sigma\). For every received word \(y\in\Sigma^m\), \(m\ge4\), let \(P(y)\) be its set of **distinct** length-\(m-2\) one-step parents, and write \(d(y)=|P(y)|\). Then:

1. Decompose \(y\) into maximal constant-symbol runs. **Exactly one distinct parent** is contributed by each run of length at least four and by each interior run of length exactly two whose two neighboring runs have the same symbol. No other run contributes. Thus \(d(y)\) is the number of such marked runs.
2. The worst-case exact inverse-list size is
   \[\max_{y\in\Sigma^m}d(y)=\left\lfloor\frac{m-2}{2}\right\rfloor.\]
   This holds for every \(q\ge2\) and \(m\ge4\), without asymptotic qualifications.
3. The total number of distinct parent–received-word incidences is
   \[\sum_{y\in\Sigma^m}d(y)=q^{m-4}\bigl((m-3)q(q-1)+q+(m-4)(q-1)\bigr).\]
The structural rule yields a one-pass algorithm for inverse-list cardinality and, by retaining one deletion per marked run, a linear-output enumeration of all parents.

## Assumptions and scope
A word is linear, not cyclic. Exactly one duplication of length two occurs; the inserted copy is the reversal of the adjacent source block and is placed immediately after it. There are no substitutions, complemented symbols, or additional duplications. Distinct deletion positions that reconstruct the same parent count once. The alphabet is arbitrary with \(q\ge2\). The received length is an integer \(m\ge4\); the parent length is \(m-2\).

Index letters of \(y\) from zero. A valid inverse operation at \(i\) requires \(y_i y_{i+1}y_{i+2}y_{i+3}=a b b a\) and deletes positions \(i+2,i+3\). Every legal parent arises in this way. A maximal constant run is a maximal interval of identical symbols. An interior run is one with a neighboring run on each side.

## Proof
**1. When do two inverse positions yield one parent?** Consider deletion of adjacent two-letter blocks starting at positions \(k<\ell\). Directly comparing the resulting strings from the earliest affected index to the latest shows that the outputs agree exactly when \(y_t=y_{t+2}\) for all \(k\le t<\ell\). This is a two-periodicity condition on \(y_k\cdots y_{\ell+1}\), valid also when the deleted blocks overlap.

Now require that both deletions are legal palindromic deduplications. The later legal window, starting at \(\ell-2\), has equal center letters \(y_{\ell-1}=y_{\ell}\). These occur within the two-periodic interval, so the entire interval \(y_k\cdots y_{\ell+1}\) is constant. The earlier legal window starts at \(k-2\) and satisfies \(y_{k-2}=y_{k+1}\) and \(y_{k-1}=y_k\). Hence the entire block \(y_{k-2}\cdots y_{\ell+1}\) is constant. Conversely, any two valid four-letter windows entirely within the same constant run produce the same parent, since both remove two indistinguishable letters from that run. Therefore different palindromic windows share a parent **if and only if** they lie in the same maximal constant run.

**2. Locate eligible windows.** A nonconstant four-letter palindrome \(a b b a\) with \(a\ne b\) has its two middle occurrences forming a complete maximal run of length two. The preceding and following runs both contain \(a\); conversely every such length-two interior run generates exactly one legal window (the immediately adjacent \(a\) letters). A constant four-letter palindrome occurs exactly inside a maximal run of length at least four, whose possibly many windows all yield one parent by Step 1. Step 1 also ensures distinct contributions from all different marked runs. This proves the exact run formula and constructive enumeration rule.

**3. Sharp maximum.** Let \(t\) be the number of marked interior length-two runs and \(s\) the number of marked length-at-least-four runs. Then \(d(y)=t+s\). If \(s\ge1\), disjoint marked runs consume at least \(2t+4s\ge2(t+s)+2\) symbols. If \(s=0\) and \(t\ge1\), the interior marked runs consume \(2t\) symbols, and the first and last runs supply at least two additional symbols: \(m\ge2t+2\). If \(d(y)=0\), the bound is automatic. Thus \(d(y)\le\lfloor(m-2)/2\rfloor\).

For equality put \(r=\lfloor(m-2)/2\rfloor\). Over two symbols, take \(r+2\) alternating constant runs, with lengths \(1,2,\ldots,2,1\), where there are \(r\) interior runs of length two; if \(m\) is odd, lengthen the final run from one to two. Every interior length-two run has the same symbol on its two neighboring runs, so exactly \(r\) runs are marked. This attains the bound for all \(m\ge4\).

**4. Aggregate incidence identity.** Every eligible nonconstant \(a b b a\) window gives a separate parent by Step 1. It has \(m-3\) possible starts, \(q(q-1)\) assignments for \((a,b)\), and \(q^{m-4}\) assignments elsewhere. A marked constant run has one unique beginning. If that beginning is position zero, there are \(q^{m-3}\) words beginning in a run of length at least four. For each other possible run start \(i=1,\ldots,m-4\), enforce \(y_{i-1}\ne y_i=y_{i+1}=y_{i+2}=y_{i+3}\); this yields \((q-1)q^{m-4}\) words. Summing the nonconstant windows and constant-run starts gives the claimed expression, without double counting distinct parents.

## Verification
An independent exhaustive enumerator constructs the actual distinct parent sets by deleting every valid \(a b b a\) window and compares their sizes with the run formula, the global maximum, and the incidence sum. Run \(`python verify.py`\) using a standard Python 3 interpreter. The verified parameter cases are \(q=2\), received lengths \(4\) through \(12\); \(q=3\), lengths \(4\) through \(9\); and \(q=4\), lengths \(4\) through \(7\). In total 19 parameter cases and 59,420 received strings were independently enumerated; all tests passed. The infinite-family result follows from the proof, not from finite exhaustion.

## Relationship to prior work
Yohananov and Schwartz [1] study codes correcting arbitrarily many palindromic and reverse-complement duplications and derive asymptotic code capacity. That question differs from the exact inverse list for **one** prescribed length-two palindromic duplication. Zeraatpisheh, Esmaeili and Gulliver [2], particularly their Section III and Table 1 on overlapping length-two palindromic squares, examine local deduplication ambiguities to construct multiple-error-correcting codes. Their comparisons are relevant to Step 1, but the inspected discussion does not assert a complete per-received-word marked-run list formula, a sharp \(q\)-ary worst-case inverse-list bound, or the aggregate distinct-parent incidence count. Lenz, Wachter-Zeh and Yaakobi [3] discuss duplication-correcting code constructions; the broader problem is distinct from this fixed-operation inverse enumeration.

## Limitations
The finding applies only to exact-one, fixed-span-two palindromic duplication and gives no minimum-distance or maximum-code-size theorem, no multi-step classification, and no statement about reverse-complement duplication. It does not claim that the local observations about overlapping palindromic squares are new; their prior use is explicitly acknowledged. Despite targeted searches, an independently published equivalent specialization of a general duplication inverse-enumeration result cannot be excluded. The exhaustive checks cover only the finite parameter sets stated above.

## References
[1] L. Yohananov and M. Schwartz, *On the Coding Capacity of Reverse-Complement and Palindromic Duplication-Correcting Codes*, arXiv:2312.00394, initially posted 2023-12-01. https://arxiv.org/abs/2312.00394

[2] M. Zeraatpisheh, M. Esmaeili and T. A. Gulliver, *Construction of Duplication Correcting Codes*, IEEE Access 8 (2020), 96150–96161, DOI:10.1109/ACCESS.2020.2995812. https://www.researchgate.net/publication/341536136_Construction_of_Duplication_Correcting_Codes

[3] A. Lenz, A. Wachter-Zeh and E. Yaakobi, *Duplication-Correcting Codes*, arXiv:1712.09345, initially posted 2017. https://arxiv.org/abs/1712.09345
