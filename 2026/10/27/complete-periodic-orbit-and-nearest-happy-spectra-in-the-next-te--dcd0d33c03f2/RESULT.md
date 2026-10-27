# Complete periodic-orbit and nearest-happy spectra in the next ten negative bases

## Finding
For each negative integer base \(b\in\{-11,-12,\ldots,-20\}\), all positive periodic points of the sum-of-squared-digits map \(S_{2,b}\) are the cycles explicitly listed in the accompanying `negative_cycles_witnesses.json`. They are the **complete** cycle sets, not merely known examples. In addition, for each base, the least happy integer strictly greater than \(1\) and the greatest happy integer strictly less than \(-1\) are determined exactly.

Here a *happy* integer is one whose iterated digit-square sums reach \(1\). The table records fixed points, lengths of the other distinct directed cycles (one entry per cycle), the least happy positive integer beyond \(1\), and the greatest happy integer below \(-1\):

| Base | Fixed points | Nontrivial cycle lengths | Least happy >1 | Greatest happy <-1 |
| --- | --- | --- | ---: | ---: |
| \(-11\) | 1 | 2,3,7 | 31 | -11 |
| \(-12\) | 1 | 11 | 144 | -12 |
| \(-13\) | 1,65,66 | 2,3,4,9 | 169 | -13 |
| \(-14\) | 1 | 2,7 | 196 | -14 |
| \(-15\) | 1 | 2,2,4,9 | 55 | -15 |
| \(-16\) | 1,118 | 3,4,5 | 256 | -16 |
| \(-17\) | 1 | 4,4,4,5,9 | 97 | -17 |
| \(-18\) | 1 | 3,17 | 324 | -18 |
| \(-19\) | 1,158,262,282 | 3,5,5,5 | 5 | -17 |
| \(-20\) | 1,275 | 2,5,5 | 400 | -20 |

In particular, \(b=-18\) has a unique primitive \(17\)-cycle:
\[
86\to393\to454\to141\to347\to318\to146\to105\to395\to518\to264\to161\to390\to373\to429\to398\to204\to86.
\]
The cycles in the published census for \(-2\ge b\ge-10\) all have length less than \(17\). The new complete census for \(-11\) through \(-18\) therefore proves that \(b=-18\) is **the first negative base, in order of increasing absolute value**, having a primitive \(17\)-cycle. This is a first-occurrence result, not a statement about bases of larger absolute value.

## Assumptions and scope
Fix an integer \(p\in\{11,\ldots,20\}\) and set \(b=-p\). The base-\(b\) expansion of an integer has digits \(0\le d_i<p\), and \(S_{2,b}(n)=\sum_i d_i^2\), with \(S_{2,b}(0)=0\). Periodic points in the theorem are **strictly positive** (zero is another fixed point if it is included in the domain). A directed cycle is listed once, rotated to start at its least member, with the iteration direction preserved. The accompanying witness file lists every integer in every cycle, rather than only cycle lengths.

Write
\[
B_p=(p-1)(p^2-p+1),\qquad H_p=3(p-1)^2.
\]
The published descent theorem for negative-base happy maps shows that every positive \(n>B_p\) satisfies \(0<S_{2,-p}(n)<n\).

## Proof
**Reduction to a closed finite core.** A positive integer's base-\((-p)\) representation has odd length. The smallest positive integer with at least five base-\((-p)\) digits is
\[
\frac{p^4+p}{p+1}=p^3-p^2+p>B_p=p^3-2p^2+2p-1.
\]
For higher odd lengths, the corresponding lower bounds \((p^{2k}+p)/(p+1)\), \(k\ge2\), increase with \(k\). Thus every \(1\le n\le B_p\) has at most three nonzero-position slots. Consequently
\[
1\le S_{2,-p}(n)\le 3(p-1)^2=H_p<B_p.
\]
This bound is attained at \(n=B_p\), whose three digits are all \(p-1\), so the one-step core bound is sharp. Every positive orbit eventually enters \([1,B_p]\) by the published descent theorem and then enters the closed interval \([1,H_p]\). Every positive cycle is therefore contained in \([1,H_p]\).

**Exact finite graph certificate.** For each of the ten specified values of \(p\), construct the map \(f_p:\{1,\ldots,H_p\}\to\{1,\ldots,H_p\}\) by the standard Euclidean negative-base digit extraction. The accompanying `verify_negative_cycles.py` recomputes every edge, compares two independent digit-extraction recurrences, and enumerates **all** directed cycles by two different exhaustive finite-graph algorithms: (i) repeated path-following with first-return detection and (ii) zero-indegree peeling followed by reconstruction of the remaining cyclic components. Each returns the exact list in `negative_cycles_witnesses.json`, including every fixed point and the full directed order of all longer cycles. Since the graph lists every integer in its provably absorbing domain, these finite checks are an exhaustive proof of the stated cycle classification.

**Nearest happy integers.** For each base, the verifier tests the claimed least happy integer beyond \(1\), every preceding integer starting at \(2\), the claimed greatest happy integer below \(-1\), and every integer between it and \(-1\) (exclusive). Digit-square iteration is exact and terminates in the closed core. A trajectory is happy exactly when it enters the fixed point \(1\); encountering any other directed cycle proves it is not happy. These exhaustive intervals establish all twenty boundary entries of the table.

**First appearance of period \(17\).** The displayed \(17\)-cycle is included in the verified graph for \(b=-18\), while the complete graphs for \(-11\) through \(-17\) contain no period-\(17\) cycle. The previously published table for \(-2\) through \(-10\) likewise contains none. This proves the asserted sharp first base.

## Verification
Run `python3 verify_negative_cycles.py` in the same directory as `negative_cycles_witnesses.json`. The checker visits every \(1\le n\le B_p\) for each specified \(p\), verifies the sharp trapping bound and both digit-extraction procedures, constructs every graph edge on \([1,H_p]\), and independently checks the stated cycles by two algorithms. It also checks every smaller positive or larger negative candidate in the displayed nearest-happy searches and verifies the unique period-\(17\) cycle in base \(-18\). The complete deterministic execution terminates with a `VERIFIED` message. The finite scans are logically exhaustive only because the preceding proof establishes the absorbing bounds.

## Relationship to prior work
Grundman and Harris (2017, 2018 publication) define this negative-base digit-square dynamics, prove the descent bound used above, and publish a table of all fixed points, periodic cycles, and nearest happy integers for bases \(-2\) through \(-10\) (their Section 2, Table 1). The present result fills the immediately following **ten complete bases** using the same natural arithmetic invariants, and establishes the previously absent first-occurrence threshold for prime cycle length \(17\).

Grundman (2024) proves the conjecture that even negative bases have arbitrarily long consecutive sequences of happy numbers, but that existence theorem does not imply this exact cycle census, nearest-happy threshold table, or first period-\(17\) base. Those consecutive-run statements are prior theorems, **not** claimed here.

## Limitations
The classification covers precisely \(-11\) through \(-20\), plus a first-occurrence comparison with the published \(-2\) through \(-10\) table. It does not classify larger-magnitude negative bases or give a general formula for cycle counts or periods. The calculation uses finite exact arithmetic after a proved bound; it is not a symbolic all-base classification. An earlier unindexed independent tabulation remains possible. No claim of publication priority or external validation is made.

## References
1. H. G. Grundman and P. E. Harris, *Sequences of Consecutive Happy Numbers in Negative Bases*, arXiv:1705.04648v1, first publicly posted 12 May 2017; see especially Section 2 and Table 1. https://arxiv.org/html/1705.04648v1
2. H. G. Grundman, *Closing an Open Problem on Negative Base Happy Numbers*, Fibonacci Quarterly **62**(2) (May 2024), 125–129. https://www.mathstat.dal.ca/FQ/Papers/62-2/grundman11162023.pdf
