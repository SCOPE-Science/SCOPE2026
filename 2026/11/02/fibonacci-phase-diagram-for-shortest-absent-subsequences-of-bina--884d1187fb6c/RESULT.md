# Fibonacci phase diagram for shortest absent subsequences of binary block powers

## Finding

For integers \(a,b,m\ge1\), consider the periodic run word \(W=(0^a1^b)^m\). A *scattered subsequence* selects letters of the host in strictly increasing positions, and a *shortest absent subsequence* (SAS) is a binary word not embeddable this way with minimum possible length.

Put \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). The shortest-absent length is \(m+1\) if \(\min(a,b)=1\), and \(2m\) otherwise. The **complete exact count** is

\[
|\operatorname{SAS}((0^a1^b)^m)|=
\begin{cases}
m+2,&a=b=1,\\
2,&\min(a,b)=1<\max(a,b),\\
F_{2m},&a=b=2,\\
2^{m-1},&\min(a,b)=2<\max(a,b),\\
1,&a,b\ge3.
\end{cases}
\]

In particular, changing both run lengths from two to three collapses a Fibonacci-growing shortest-absence set to a singleton. These are *scattered* absences; the claim is not about contiguous absent factors.

## Assumptions and scope

All statements are for the ordered alphabet \(\{0,1\}\), positive integers \(a,b,m\), and ordinary finite subsequences. The empty word is present. Shortest-absence sets are sets of distinct words, not counts of embeddings. Run lengths are not assumed coprime, balanced, or bounded. The conventions \(F_0=0,F_1=1\) fix the Fibonacci indexing.

A *binary arch* is a shortest nonempty segment starting at the current position that contains both symbols; the remaining single-symbol suffix is called the rest. If the greedy arch decomposition has \(k\) arches, every binary word of length \(k\) is a subsequence by choosing one desired letter from each arch; and there is an absent word of length \(k+1\), obtained by greedily taking the final new letter of each arch and appending a letter absent from the rest. Thus the shortest absent length is exactly \(k+1\).

## Proof

**1. The one-per-arch lemma.** Let \(A_1\cdots A_kR\) be the greedy arch factorization. For any absent binary word \(v=v_1\cdots v_{k+1}\), greedy leftmost matching of \(v_1\cdots v_k\) matches position \(j\) inside arch \(A_j\). Indeed, every length-\(k\) word can be matched with one letter per arch, so the greedy \(j\)-th match is never beyond \(A_j\). If some greedy \(j\)-th match were in an earlier arch \(A_h\) with \(h<j\), then the remaining \(k+1-j\) requested letters could be matched, one per arch, using the \(k-h\ge k+1-j\) complete arches after \(A_h\). This contradicts absence. Conversely, if the first \(k\) greedy matches lie one in each arch and the final requested letter has no occurrence after the last match, the word is absent and hence shortest absent. This gives a complete deterministic test.

**2. The cases with a run of length one.** If \(a=b=1\), there are \(m\) arches \(01\), with empty rest. Label a greedy arch match \(E\) if it uses its initial 0 and \(L\) if it uses its last 1. An \(L\) may be followed by either type, but an \(E\) can only be followed by an \(E\): another 1 would be matched at the end of the *previous* arch. Therefore the legal type words are \(L^tE^{m-t}\) for \(0\le t\le m\). If the final type is \(E\), only 0 may be appended as an absent last letter; if it is \(L\), either letter may be appended. Thus the shortest-absent set is precisely \(\{1^t0^{m+1-t}:0\le t\le m\}\cup\{1^{m+1}\}\), of size \(m+2\).

If \(a=1<b\), the \(m\) arches are \(01\), followed (if \(m\ge2\)) by \(1^{b-1}0\) and then by \(m-2\) copies of \(1^b0\); the rest contains only 1s. The last missing letter must be 0. The last greedy arch match must be its terminal 0, because matching a 1 inside the last arch leaves a 0 available. In every arch after the first, matching terminal 0 forces the previous match to have been terminal 0 as well; otherwise that 0 would have matched in the preceding arch. The first match may be its initial 0 or terminal 1. Consequently exactly \(0^{m+1}\) and \(10^m\) are shortest absent.

If \(b=1<a\), there are \(m\) identical arches \(0^a1\), with empty rest. The last match must use the terminal 1 because the initial 0 leaves both letters still available. Backwards, using the terminal 1 in any arch forces the preceding match to have used the terminal 1 too, or it would have matched the previous arch's 1. Thus the first \(m\) requested letters are all 1, and either terminal letter is absent: the set is \(\{1^m0,1^{m+1}\}\).

**3. Both run lengths at least two.** The arches are \(A_1=0^a1\); for even \(j\), \(A_j=1^{b-1}0\); for odd \(j\ge3\), \(A_j=0^{a-1}1\). There are \(k=2m-1\) arches and a final rest \(1^{b-1}\). Each arch has the form \(x_j^{R_j}y_j\), with \(x_j\ne y_j\); the first-run lengths are \(R_1=a\), \(R_j=b-1\) at even \(j\), and \(R_j=a-1\) at odd \(j\ge3\). A greedy match in arch \(j\) has type \(E\) when it chooses the first \(x_j\), and type \(L\) when it chooses the last \(y_j\).

Because \(a\ge2\), starting with type \(E\) would cause the second requested letter to be matched inside the first arch: either another 0 remains or the terminal 1 can be used. Hence \(T_1=L\). From type \(L\) in one arch either type can be chosen in the next. From type \(E\), the next arch can be reached only by choosing its terminal symbol (type \(L\)) and only if \(R_j=1\): the other symbol occurs at the previous arch's terminal position, and when \(R_j>1\) another copy of the first-run symbol also remains inside the previous arch. Therefore \(E\to L\) is permitted exactly when \(R_j=1\), while \(L\to E\) and \(L\to L\) are always permitted. No \(E\to E\) transition is allowed. The rest contains only 1s, so the final requested letter must be 0. A final type \(L\) leaves no 0; a final type \(E\) leaves no 0 only when the final arch's initial 0-run has length 1, equivalently \(a=2\). These conditions are both necessary and sufficient by step 1, and give an explicit *bijection* from legal type sequences to distinct shortest absent words. Under this map, odd arches encode \(E\mapsto0,L\mapsto1\), and even arches encode \(E\mapsto1,L\mapsto0\); append 0 at the end.

If \(a=b=2\), the first run in every arch after the first has length 1. The type sequences start with \(L\), avoid \(EE\), and may terminate in either state. Their number for length \(2m-1\) is \(F_{2m}\), by the usual two-state Fibonacci recurrence.

If \(a=2<b\), all even arches have first-run length at least 2, so no even arch may have type \(E\) (the even arches are nonterminal). The \(m-1\) later odd arches independently choose \(E\) or \(L\), including the final odd arch. The result is \(2^{m-1}\) words. If \(b=2<a\), every odd arch must have type \(L\), including the terminal arch, while the \(m-1\) even arches choose freely, again yielding \(2^{m-1}\). If \(a,b\ge3\), all arches must have type \(L\), and the unique shortest absent word is \((10)^m\). The case \(m=1\) is covered by the same initial and terminal conditions.

All five branches and their exact sets are now proved.

## Verification

A standalone Python verifier checks both the shortest absent *sets* and the universality boundaries independently of the above proof, using literal left-to-right subsequence matching against exhaustive binary targets. It covers all \(1\le a,b,m\le6\): 216 distinct parameter instances, 139,272 length-specific candidate targets, and 985 absent words. The verifier reconstructs the predicted type-language sets and compares equality, rather than only comparing counts. Execute \(\texttt{python3 verify_binary_block_sas.py}\). Its successful output is \(\texttt{VERIFY_OK instances=216 literal_targets=139272 classified_shortest_absent=985}\). These finite checks support but do not replace the unbounded proof in the preceding section.

## Relationship to prior work

Kosche, Koß, Manea and Siemer (arXiv:2108.13968, initially public 2021-08-31) develop the general SAS/MAS framework, including arch factorization and greedy witness characterizations. The proof here uses this established viewpoint but supplies the explicit run-sensitive type automaton and an all-parameter, five-regime enumeration for one natural infinite block-power family. Schnoebelen and Veron (arXiv:2304.11932) investigate arch-jumping and compressed-word universality, rather than this absence cardinality phase diagram. Manea et al. (arXiv:2504.21471) treat optimal SAS/MAS enumeration algorithms, rather than the specialized symbolic formula. A separate known extremal Fibonacci result concerns maxima over arbitrary binary hosts and does not by itself determine these fixed-period counts.

## Limitations

The claim is for two-symbol periodic run blocks and shortest absent **subsequences** only; it does not classify all minimal absent subsequences of every length, or higher alphabets. The originality comparison cannot exclude an unindexed equivalent specialization. It does not imply a new algorithmic complexity bound beyond existing general-purpose SAS enumeration methods. Independent validation has not been performed.

## References

1. Maria Kosche, Tore Koß, Florin Manea, Stefan Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (2021); Fundamenta Informaticae 189 (2023), 199–240.
2. Philippe Schnoebelen, Julien Veron, *On arch factorization and subword universality for words and compressed words*, arXiv:2304.11932 (2023).
3. Florin Manea, Tina Ringleb, Stefan Siemer, Maximilian Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471 (2025).
