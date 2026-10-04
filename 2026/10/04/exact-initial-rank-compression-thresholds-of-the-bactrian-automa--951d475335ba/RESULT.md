# Exact initial rank-compression thresholds of the bactrian automata \(B_n\)
## Finding
For every odd \(n>3\), let \(B_n\) be the automaton on \(Q=\{1,\ldots,n\}\) with \(b(i)=i+1\pmod n\), \(a(i)=i\) for \(i<n-1\), \(a(n-1)=1\), and \(a(n)=2\). Define \(\lambda_n(s)=\min\{|w|:|Qw|\le n-s\}\). For every \(1\le s\le(n+1)/2\), \(\lambda_n(1)=1\); for every \(k\ge0\) with \(2k+2\le(n+1)/2\), \(\lambda_n(2k+2)=5k+1\); and for every \(k\ge1\) with \(2k+1\le(n+1)/2\), \(\lambda_n(2k+1)=5k\). Sharp witnesses are \(a(b^4a)^k\) for deficiency \(2k+2\) and \(ab^3a(b^4a)^{k-1}\) for deficiency \(2k+1\).

Equivalently, after the first application of \(a\) creates deficiency two, the cheapest additional loss alternates between a one-state loss costing four more letters and a two-state loss costing five more letters. Thus the initial compression profile is \(1,1,5,6,10,11,15,16,\ldots\) as long as the target deficiency does not exceed \((n+1)/2\).

## Assumptions and scope
The state set is \(Q=\{1,\ldots,n\}\), where \(n>3\) is odd. The letter \(b\) is the cyclic permutation \(1\mapsto2\mapsto\cdots\mapsto n\mapsto1\). The letter \(a\) fixes \(1,\ldots,n-2\), sends \(n-1\) to \(1\), and sends \(n\) to \(2\). This is the standard relabeling of the bactrian series introduced by Ananichev, Volkov, and Zaks. The theorem concerns only targets \(1\le s\le(n+1)/2\); no formula is claimed here beyond that range.

## Proof
Put \(R=\{1,\ldots,n-2\}\). The only nontrivial kernel pairs of \(a\) are \(\{1,n-1\}\) and \(\{2,n\}\), so one application of \(a\) can lower the size of a set by at most two. Moreover every image under \(a\) lies in \(R\).

First consider any set \(T\subseteq R\). Directly from the transition rules, every word of length at most three acts injectively on \(R\), hence also on \(T\). Among the sixteen words of length four, all act injectively on \(R\) except \(b^3a\), whose action on \(R\) has exactly one collision. Therefore, starting immediately after an effective application of \(a\), the next strict decrease of image size costs at least four letters, and a decrease by two costs at least five letters.

The first effective \(a\) in any word applied to \(Q\) costs at least one letter and lowers the size by exactly two, since every leading power of \(b\) keeps the full set equal to \(Q\). After that, write the successive effective decreases as values in \(\{1,2\}\). A one-state decrease costs at least four letters after the preceding effective decrease, while a two-state decrease costs at least five. To create an additional deficiency \(2k-1\), the cheapest possibility is \(k-1\) two-state decreases and one one-state decrease, with total length at least \(1+5(k-1)+4=5k\). To create an additional deficiency \(2k\), the cheapest possibility is \(k\) two-state decreases, with total length at least \(1+5k=5k+1\). This proves the lower bounds.

For the matching upper bounds, track holes, meaning states absent from the current image. After the first \(a\), the holes are \(\{n-1,n\}\). For \(k\ge1\), induction using the transition rules gives
\[
Q\,ab^3a(b^4a)^{k-1}=Q\setminus\left(\bigcup_{r=1}^{k-1}\{4r-1,4r\}\cup\{4k-1,n-1,n\}\right),
\]
and for \(k\ge0\),
\[
Q\,a(b^4a)^k=Q\setminus\left(\bigcup_{r=1}^k\{4r-1,4r\}\cup\{n-1,n\}\right).
\]
In the odd-target case, \(2k+1\le(n+1)/2\) implies \(4k-1\le n-2\); in the even-target case, \(2k+2\le(n+1)/2\) implies \(4k\le n-3\). Hence the displayed hole sets are disjoint in the stated range. Their cardinalities are respectively \(2k+1\) and \(2k+2\), and the witness lengths are respectively \(5k\) and \(5k+1\). Together with the lower bounds, this proves the claimed equalities.

## Verification
A standalone standard-library script, `verify.py`, performs exact power-automaton breadth-first search for every odd \(n\in\{5,7,9,11,13,15,17\}\), compares all thresholds in the proved half-range with the formulas above, and separately checks the stated witness words and hole counts for every odd \(n\le101\). Its successful output is recorded in `verification_output.txt`. These finite checks are stress tests only; the proof above establishes the infinite statement.

## Relationship to prior work
Ananichev, Volkov, and Zaks introduced \(B_n\) and proved that its shortest reset word has length \((n-1)(n-2)\). Their full proof follows the complete reset process with a coin-weight argument and explicitly notes that one application of the deficiency-two letter can delete two coins, but it does not state the exact shortest length for each intermediate image size. Ananichev, Gusev, and Volkov later restated \(B_n\) in the labeling used here and again recorded only the reset threshold. Work on collapsing and compressing words studies universal words or decision problems over classes of automata rather than this exact family-specific threshold profile. Targeted searches using the aliases “rank of a word”, “compressing word”, “k-compressible”, “image size”, “deficiency”, and “subset compression” did not locate the piecewise \(5k\)/\(5k+1\) profile.

The endpoint reset theorem does not imply the present statement: knowing the minimum time to reach rank one leaves the earlier ranks undetermined. The new ingredient here is the local spacing lemma after every effective \(a\), paired with explicit hole-propagation witnesses.

## Limitations
The exact formula is proved only through deficiency \((n+1)/2\). The later compression profile is substantially more irregular in finite breadth-first searches and is not addressed. Literature search cannot prove novelty; an older equivalent statement may exist under different terminology. The most relevant primary source was inspected in full, while the older collapsing-words survey was available only at abstract/metadata level in this check.

## References
1. D. S. Ananichev, M. V. Volkov, Yu. I. Zaks, Synchronizing Automata with a Letter of Deficiency 2, DLT 2006, DOI:10.1007/11779148_39; journal version DOI:10.1016/j.tcs.2007.01.010.
2. D. S. Ananichev, V. V. Gusev, M. V. Volkov, Slowly synchronizing automata and digraphs, arXiv:1005.0129v1, DOI:10.1007/978-3-642-15155-2_7.
3. D. S. Ananichev, I. V. Petrov, M. V. Volkov, Collapsing Words: A Progress Report, DOI:10.1007/11505877_2; journal DOI:10.1142/S0129054106003966.
4. P. Martyugin, Complexity of problems concerning reset words for some partial cases of automata, Acta Cybernetica 19(2) (2009), 517–536.
