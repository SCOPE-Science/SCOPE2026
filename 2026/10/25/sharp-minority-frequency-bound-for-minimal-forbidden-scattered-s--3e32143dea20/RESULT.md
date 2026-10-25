# Sharp minority-frequency bound for minimal forbidden scattered subwords

## Finding
Let \(w\) be any finite binary word with exactly \(k\geq0\) occurrences of \(1\). Write \(\mathcal M(w)\) for the set of words absent as scattered subsequences of \(w\) for which every proper scattered subsequence occurs in \(w\). Then
\[
|\mathcal M(w)|\leq 2^{k+1}.
\]
The bound is sharp for every \(k\): the word \(w_k=(010)^k\) has exactly \(2^{k+1}\) such minimal forbidden scattered subwords. Exchanging the binary letters gives the symmetric statement for the other symbol. There is no restriction on the total length or on the number of zeros.

## Assumptions and scope
The alphabet is precisely \(\{0,1\}\), even if one letter does not occur in the source. A scattered subsequence preserves letter order but need not be contiguous. The empty word is a subsequence of every source, and is not forbidden. Minimality means that deletion of **any single position** in the absent word yields a subsequence of the source (equivalently, every proper scattered subsequence does). All counts are of distinct strings, not embeddings. The result is a sharp bound parameterized by the number of minority-letter occurrences; it does not classify every equality case.

## Proof
For a source \(v\), let \(A(v)\) and \(B(v)\) be the numbers of members of \(\mathcal M(v)\) ending respectively in \(0\) and \(1\), and let \(C(v)\) count those ending in \(00\). All minimal absent words are nonempty, so \(|\mathcal M(v)|=A(v)+B(v)\).

We use the binary specialization of the minimal-forbidden-subword append recurrence of Petković, Ćirić and Bogdanović (2004, Theorem 4.1). It can also be read directly from that theorem's suffix-extension construction: when a letter \(x\) already occurs in \(v\), appending \(x\) preserves the number of forbidden words ending in \(x\). Each old forbidden word ending in the other letter \(y\) persists; each old forbidden word ending in \(x\) contributes one replacement ending in \(x\) and can contribute **at most one additional** replacement ending in \(y\). If \(v\) ends in \(x\), no additional replacement occurs. If \(v\) ends in a run of exactly one \(y\), and \(x\) appears earlier, precisely the old minimal forbidden words ending in \(xx\) contribute an additional ending in \(y\). If \(v\) ends in a run of at least two \(y\)'s, and \(x\) appears earlier, every old forbidden word ending in \(x\) contributes this additional replacement. The extra replacement always appends \(y\) to a word formerly ending in \(x\); in particular, when appending \(1\), the newly created words ending in \(0\) end in \(10\), never in \(00\). If \(x\) has never occurred, the recurrence instead replaces the singleton forbidden word \(x\) by the strings \(xy\) for the letters \(y\) present after append. These assertions include the zero- and one-run boundaries and use distinct-word accounting, not multiplicities.

We establish by induction on the length of \(v\), where \(k=|v|_1\), the two inequalities
\[
A(v)\leq2^k,\qquad B(v)\leq2^k.
\]
We simultaneously use the consequence, for every word \(v\) ending in \(1\) with \(k\geq1\),
\[
B(v)\leq2^{k-1},\qquad C(v)\leq2^{k-1}.
\]
For \(v=0^m\), including \(m=0\), the minimal forbidden set is \(\{0^{m+1},1\}\), hence both counts are one. For \(v=0^m1\), the first occurrence of \(1\), the append recurrence gives \(B(v)=1\) and \(C(v)\leq1\). The two main bounds also hold, since \(A(v)\leq2\).

Suppose the bounds hold for a prefix \(v\) with \(k\) ones. Appending \(1\) when one is already present leaves \(B\) unchanged and increases \(A\) by no more than \(B\), so the resulting counts are bounded by \(2^k\) and \(2^{k+1}\). Furthermore, the new \(B\) is at most \(2^k\); the new \(C\) comes solely from old words ending in \(00\), because newly generated forbidden words ending in \(0\) end in \(10\). Hence \(C\leq A(v)\leq2^k\). This establishes the displayed stronger bounds for the new word ending in \(1\). The first occurrence of \(1\) was handled above.

Appending \(0\) to a word already ending in \(0\) changes neither of the two ending-letter counts. Suppose instead that \(v\) ends in \(1\), with \(k\geq1\). If \(v\) contains no \(0\), then \(v=1^k\); the newly formed word \(1^k0\) has minimal forbidden set \(\{00,01,1^{k+1}\}\), giving \(A=1\), \(B=2\leq2^k\). Otherwise \(0\) has appeared earlier. In all cases the appended \(0\) leaves \(A\) unchanged. If the final run of ones in \(v\) has length one, the append recurrence gives \(B(v0)=B(v)+C(v)\leq2^k\). If it has length at least two, deleting its last \(1\) gives a shorter word \(v'\) with \(k-1\) ones and the same counts \(A\) and \(B\) as \(v\), by the repeated-letter append recurrence. Thus \(A(v),B(v)\leq2^{k-1}\), and the append recurrence yields \(B(v0)\leq B(v)+A(v)\leq2^k\). This proves the induction and the general upper bound.

For sharpness, set \(u_k=(010)^k\), \(k\geq1\). Directly, \(\mathcal M(u_1)=\{000,001,100,11\}\): the two ending-letter counts are \(A(u_1)=B(u_1)=2\), and every forbidden word ending in \(0\) ends in \(00\). Suppose for \(u_k\) that \(A=B=2^k\) and every forbidden word ending in \(0\) ends in \(00\). Appending a second \(0\) leaves \(A,B\) unchanged and ensures the final zero run has length two. Appending \(1\) then splits **every** old forbidden word ending in \(1\) into an ending-in-\(1\) replacement plus an extra ending-in-\(0\) replacement; thus the new counts are \(A=2^{k+1}\), \(B=2^k\). The count \(C\) equals \(2^k\): old ending-in-\(0\) forbidden words persist and end in \(00\), whereas all new ending-in-\(0\) replacements end in \(10\). Finally appending \(0\) after the singleton last \(1\) adds exactly \(C=2^k\) new forbidden words ending in \(1\), without changing \(A\). The resulting \(u_{k+1}\) therefore satisfies \(A=B=2^{k+1}\), and all its forbidden words ending in \(0\) end in \(00\). Induction gives \(|\mathcal M(u_k)|=2^{k+1}\). For \(k=0\), the empty word has the two singleton symbols as its minimal absent subsequences, again attaining the bound. \(\square\)

## Verification
The standalone `check.py` independently enumerates distinct scattered subsequences, generates all minimal absent words by checking every one-position deletion, verifies the ending-letter inequalities and required append identities for every binary source of length at most \(14\), and checks sharpness for \(0\leq k\leq7\). It prints `VERIFY_OK 32767`. These finite checks corroborate but do not replace the infinite induction and the cited recurrence. The published recurrence was read in full, including its binary specialization.

## Relationship to prior work
Petković, Ćirić and Bogdanović (2004) introduced the append recurrence used above and proved a Fibonacci upper bound in terms of the **number of constant-letter runs**, with equality when each run has length at least two. The present theorem instead fixes the **number of occurrences of one specified symbol** while allowing arbitrarily many occurrences of the other; this different extremal constraint yields the sharp power-of-two bound and a family of witnesses with singleton one-runs. The run-count bound by itself does not give the sharp claimed value for this constraint. Later work on absent subsequences gives general characterizations and efficient representations; the inspected survey does not assert this frequency-specific optimum.

## Limitations
The result does not determine the complete equality classification, the fixed-total-length optimum, or a comparable bound for alphabets larger than two. Priority could be affected by unindexed older derivations of the 2004 recurrence. The exact first dissemination date of a preliminary conference version of the 2004 paper was not established; its fully dated journal issue is used for the documented public-source date.

## References
1. T. Petković, M. Ćirić, S. Bogdanović, "Minimal forbidden subwords," *Information Processing Letters* 92(5) (2004), 211–218. DOI: 10.1016/j.ipl.2004.09.001; journal issue dated 16 December 2004. Author-uploaded full text: https://www.academia.edu/2579981/Minimal_forbidden_subwords.
2. M. Kosche, T. Koß, F. Manea, S. Siemer, "Absent Subsequences in Words," arXiv:2108.13968 (2021); *Fundamenta Informaticae* 189 (2023), 199–240.
3. F. Manea and collaborators, "Combinatorial Algorithms for Subsequence Matching: A Survey," arXiv:2208.14722, Section 4.2 (accessible HTML at https://arxiv.org/html/2208.14722v2).
