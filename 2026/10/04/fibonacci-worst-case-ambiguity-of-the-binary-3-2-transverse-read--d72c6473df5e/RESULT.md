# Fibonacci worst-case ambiguity of the binary \((3,2)\) transverse-read channel
## Finding
For every integer \(m\ge 1\), put \(n=2m+1\). For a binary word \(x=(x_1,\ldots,x_n)\), define its \((3,2)\) transverse-read vector by
\[
R_{3,2}(x)=\bigl(x_1+x_2+x_3,\ x_3+x_4+x_5,\ldots,\ x_{2m-1}+x_{2m}+x_{2m+1}\bigr).
\]
Let \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). Then
\[
\max_y \bigl|R_{3,2}^{-1}(y)\bigr|=F_{m+3}.
\]
Moreover, equality occurs for exactly two read vectors: \(y=(1,\ldots,1)\) and \(y=(2,\ldots,2)\).

This determines the exact worst-case ambiguity, or maximum zero-error list size, of the first nontrivial odd-window transverse-read channel at every admissible blocklength.

## Assumptions and scope
The alphabet is binary. The read window has length \(3\), successive windows start two coordinates apart, and \(n=2m+1\) so that exactly \(m\) complete windows are read. Fiber size counts distinct source words producing one fixed read vector. The theorem concerns noiseless read vectors and does not claim an error-correction result after substitutions, insertions, or deletions in the read vector.

## Proof
Fix a read-vector prefix and let \(p\) and \(q\) be the numbers of compatible source prefixes whose current shared endpoint bit is respectively \(0\) and \(1\). Before reading any window, either endpoint bit is possible, so \((p,q)=(1,1)\).

Appending one read symbol \(a\in\{0,1,2,3\}\) gives the following exact transitions. They follow by enumerating the middle bit and the new endpoint bit in one length-three window:
\[
\begin{array}{c|c}
a & (p,q)\mapsto(p',q')\\ \hline
0&(p,0)\\
1&(p+q,p)\\
2&(q,p+q)\\
3&(0,q).
\end{array}
\]
Consequently, if \(S=p+q\) and \(M=\max\{p,q\}\), symbols \(0\) and \(3\) cannot increase \(S\), while symbols \(1\) and \(2\) satisfy
\[
S'=S+c\le S+M,\qquad M'=S,
\]
where \(c\) is one of the two coordinates \(p,q\).

We prove by induction on the prefix length \(j\ge0\) that
\[
S\le F_{j+3},\qquad M\le F_{j+2}.
\]
At \(j=0\), \((S,M)=(2,1)=(F_3,F_2)\). If the next symbol is \(0\) or \(3\), both bounds are strict compared with the next Fibonacci bounds. If it is \(1\) or \(2\), then
\[
S'\le F_{j+3}+F_{j+2}=F_{j+4},\qquad M'=S\le F_{j+3}.
\]
Thus every length-\(m\) fiber has size \(S\le F_{m+3}\).

For equality, the first symbol must be \(1\) or \(2\). After symbol \(1\), the pair is \((2,1)\); after symbol \(2\), it is \((1,2)\). At every later step equality in \(S'\le S+M\) requires choosing the larger coordinate. If \(p>q\), only symbol \(1\) adds \(p=M\); if \(q>p\), only symbol \(2\) adds \(q=M\). Therefore an equality path can never switch between the two symbols. The only extremal outputs are \((1,\ldots,1)\) and \((2,\ldots,2)\), and along them the endpoint-count pair is, up to reversal, \((F_{m+2},F_{m+1})\), whose sum is \(F_{m+3}\).

## Verification
The accompanying `verify.py` implements the read map in two independent forms, exhaustively enumerates every binary source through \(n=19\), and independently computes each fiber through the two-state recurrence above. For \(m=1,\ldots,9\), the observed maxima are
\[
3,5,8,13,21,34,55,89,144,
\]
with exactly the two constant read vectors claimed above attaining each maximum. The script also checks the extremal recurrence through \(m=100\) and verifies the induction inequalities over all reachable endpoint-count pairs through prefix length \(15\). It terminates with `VERIFY_OK`.

These finite checks support the implementation and boundary cases; the all-\(m\) statement is proved by the induction above rather than inferred from enumeration.

## Relationship to prior work
Chee, Vardy, Vu, and Yaakobi introduced the transverse-read coding problem with shifted Hamming-weight windows and treated \((3,2)\) as the first nontrivial odd-window example. Their nondeterministic two-state machine records the same shared endpoint bit, while their deterministic machine and adjacency matrix are used to count distinct valid read vectors and obtain the asymptotic rate. The 2023 journal treatment develops the same valid-output language and error-correction applications.

Yerushalmi, Etzion, and Yaakobi later study the weighted-read channel systematically. They explicitly note that multiple source vectors can have the same read vector, but their principal invariant remains the number of distinct outputs and the resulting capacity. The present theorem instead optimizes the multiplicity of one fixed output. The deterministic adjacency matrix used for capacity counts output labels once and therefore does not itself give this worst-case source multiplicity; the proof above uses label-specific path multiplicities in the underlying two-state machine.

Targeted searches for “maximum fiber,” “preimage multiplicity,” “ambiguity,” “Fibonacci,” and the exact \((3,2)\) statement found no inspected source stating this theorem. The closest inspected papers provide the channel model and automata but not the maximum-fiber calculation or its unique extremizers.

## Limitations
The theorem is specific to binary \((3,2)\) reads. It does not determine maximum fibers for other window/shift pairs, noisy read vectors, or nonbinary alphabets. Literature searches cannot exclude an unindexed or unpublished derivation of the same formula. The result gives worst-case multiplicity, not the full distribution of fiber sizes.

## References
1. Y. M. Chee, A. Vardy, V. K. Vu, and E. Yaakobi, “Coding for Transverse-Reads in Domain Wall Memories,” IEEE International Symposium on Information Theory, 2021, pp. 2924–2929. DOI: 10.1109/ISIT45174.2021.9518271.
2. Y. M. Chee, A. Vardy, V. K. Vu, and E. Yaakobi, “Transverse-Read-Codes for Domain Wall Memories,” IEEE Journal on Selected Areas in Information Theory, vol. 4, 2023, pp. 784–793. DOI: 10.1109/JSAIT.2023.3334303.
3. O. Yerushalmi, T. Etzion, and E. Yaakobi, “The Capacity of the Weighted Read Channel,” arXiv:2401.15368v1, 2024.
