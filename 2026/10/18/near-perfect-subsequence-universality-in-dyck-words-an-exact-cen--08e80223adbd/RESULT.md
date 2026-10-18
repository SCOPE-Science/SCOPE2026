# Near-perfect subsequence universality in Dyck words: an exact census and Fibonacci extremizers

## Finding
For an integer \(n\ge2\), let \(\mathcal D_n\) be the Dyck words with \(n\) zeros and \(n\) ones: in every prefix the number of zeros is at least the number of ones. Let \(\iota(w)\) be the largest integer \(k\) such that every binary word of length \(k\) occurs as a scattered subsequence of \(w\). Let \(S(w)\) count the distinct shortest absent binary scattered subsequences (distinct symbol sequences, not embeddings). Define \(F_0=0,F_1=1\), and \(F_{r+2}=F_{r+1}+F_r\).

**Near-perfect Dyck classification.** The class \(\mathcal D_n^{\star}=\{w\in\mathcal D_n:\iota(w)=n-1\}\) consists exactly of the distinct words
\[
w=(01)^{j-1}\,001\,C_1C_2\cdots C_{n-1-j}\,1,
\quad 1\le j\le n-1,\quad C_i\in\{01,10\}.
\]
Consequently \(|\mathcal D_n^{\star}|=2^{n-1}-1\). Moreover
\[
\max_{w\in\mathcal D_n^{\star}}S(w)=F_n.
\]
There is exactly one maximizer for \(n=2\) and for \(n=3\). For every \(n\ge4\), there are exactly two maximizers, both of the form
\[
001\,C_1\cdots C_{n-3}\,011,
\]
where the two-letter blocks alternate between \(01\) and \(10\), beginning with either choice. For \(n=2\) the unique word is \(0011\), and for \(n=3\) it is \(001011\). The corresponding shortest absent subsequences have length \(n\).

## Assumptions and scope
Words are **linear**, with the fixed ambient alphabet \(\{0,1\}\); \(0\) represents an up-step and \(1\) a down-step. A scattered subsequence retains the order of its selected positions but need not be contiguous. The Dyck balance condition applies to all prefixes, including the empty prefix. The claim concerns the penultimate possible universality index \(n-1\) at length \(2n\), not all Dyck words and not absent contiguous factors. Distinct decompositions in the displayed family give distinct words because greedy arches are unique.

## Proof
**1. Greedy arches and a two-symbol length budget.** Repeatedly remove the shortest nonempty prefix containing both symbols; each removed piece is a *greedy arch*. For a binary alphabet an arch is \(0^a1\) or \(1^a0\) with \(a\ge1\). The rest contains only one symbol or is empty. The number of arches equals \(\iota(w)\): each arch supplies an arbitrary next subsequence symbol, whereas concatenating the terminal symbol of every arch with a symbol absent from the rest gives an absent word one letter longer. This is the usual arch characterization of subsequence universality.

For \(w\in\mathcal D_n\), write \(w=A_1\cdots A_{n-1}R\) if \(\iota(w)=n-1\). Every arch has length at least two, so
\[
\sum_{i=1}^{n-1}(|A_i|-2)+|R|=2.
\]
A nonempty rest must consist of ones, since every nonempty Dyck word ends in \(1\). Every length-two arch is balanced (\(01\) or \(10\)). A length-three arch is either \(001\) (net height \(+1\)) or \(110\) (net height \(-1\)); a length-four arch has net height \(+2\) or \(-2\).

If \(|R|=2\), the overall word has net height \(-2\), impossible. If \(|R|=0\), one length-four exceptional arch alone cannot have net height zero. The only other possibility is a length-three \(001\) and a length-three \(110\). At height zero a \(110\) cannot be encountered first, so \(001\) must be first. All intervening length-two arches preserve height one; the next \(110\) falls to height \(-1\) on its second symbol. This is also impossible. Hence \(|R|=1\); exactly one arch has length three, and balance forces it to be \(001\). Before this arch the height is zero, so every length-two arch must be \(01\). After it the height is one, so either \(01\) or \(10\) is allowed. The final rest is \(1\). Conversely all displayed words obey the Dyck prefix condition and have precisely the stated greedy arches. Summing their numbers gives
\[
|\mathcal D_n^{\star}|=\sum_{j=1}^{n-1}2^{n-1-j}=2^{n-1}-1.
\]

**2. Shortest-absent transfer.** For any one-universal binary block \(U\), write \(H(U)_{ab}=1\) when the length-two word \(ab\) is *not* a scattered subsequence of \(U\), and zero otherwise (row and column labels \(0,1\)). When \(U_1,\ldots,U_{k-1}\) are full greedy arches and \(U_k\) is the last arch with its rest, the shortest-absent gluing lemma gives
\[
S(U_1\cdots U_k)=(1,1)\,H(U_1)\cdots H(U_k)\,(1,1)^\mathsf T.
\]
This follows by successively splitting a shortest absent sequence after its first \(k-1\) letters: the overlapping consecutive pairs must be absent in the corresponding one-universal blocks; conversely the absence of these pairs prevents a greedy realization of the whole sequence. This is the binary specialization of the gluing characterization in Kosche–Koß–Manea–Siemer, Lemma 3.16, and the needed blocks can also be checked directly.

Direct inspection of the four binary pairs gives
\[
H(01)=\begin{pmatrix}1&0\\1&1\end{pmatrix}=A,\qquad
H(10)=\begin{pmatrix}1&1\\0&1\end{pmatrix}=B,
\]
\[
H(001)=\begin{pmatrix}0&0\\1&1\end{pmatrix}=E,\qquad
H(0011)=\begin{pmatrix}0&0\\1&0\end{pmatrix},
\]
\[
H(011)=\begin{pmatrix}1&0\\1&0\end{pmatrix},\qquad
H(101)=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]
Row vectors transform by \((x,y)A=(x+y,y)\) and \((x,y)B=(x,x+y)\). In the classified word, the first \(j-1\) arches transform \((1,1)\) into \((j,1)\), and then the exceptional \(001\) transforms this into \((1,1)\), **independently of \(j\)**.

If \(j=n-1\), the exceptional arch and its final rest form the terminal block \(0011\), so \(S(w)=1\). Otherwise put \(t=n-1-j\ge1\). After the exceptional arch are \(t\) two-letter arches. Multiply by \(A\) or \(B\) for the first \(t-1\) of them. If the resulting row is \((x,y)\), the final arch plus the rest is \(011\) or \(101\). The final number \(S(w)\) is respectively \(x+y\) or \(x\). Since both coordinates are positive, choosing \(011\) is strictly preferable.

**3. Fibonacci maximization and equality cases.** Starting at \((1,1)\), after \(r\ge0\) choices of \(A,B\), the two coordinates in decreasing order are componentwise bounded by \((F_{r+2},F_{r+1})\). For \(r=0\) these are \((1,1)\). If the sorted pair is bounded by \((F_{r+2},F_{r+1})\), either update replaces one coordinate by the sum and preserves the other; thus the next sorted pair is bounded by \((F_{r+3},F_{r+2})\). Equality for \(r\ge1\) requires, after the first choice, always replacing the smaller coordinate by the sum. There are exactly two maximizing sequences, the alternating choices beginning with \(A\) or with \(B\).

For a fixed exceptional-arch position \(j<n-1\), take \(r=t-1\) to obtain
\[
S(w)\le F_{r+3}=F_{t+2}=F_{n-j+1}.
\]
The largest value over \(j\) is \(F_n\), reached at \(j=1\); positions \(j\ge2\) give smaller bounds for \(n\ge3\). When \(n=3\), no intermediate transfer remains and the final \(011\) is the sole maximizing choice. For \(n\ge4\), the \(n-3\) intermediate matrices must alternate, giving exactly the two claimed extremizers. For \(n=2\), the sole classified word has \(S(0011)=1=F_2\). This finishes all cases.

## Verification
Run \(\texttt{python3 verify.py}\) with Python 3. The standalone program independently generates all Dyck words of semilength \(2\) through \(12\), computes universality and the number of shortest absent subsequences using a backwards next-occurrence dynamic program, and compares the resulting entire class with the explicit parameterization. It separately compares the two-letter transfer calculation to the dynamic-programming count for every qualifying word, uses direct binary subsequence enumeration at semilength at most eight, and tests both all-parameter extremizer constructions through semilength \(79\).

Observed result:

```text
VERIFY_OK dyck_semilength_2_to_12=290510 near_perfect=4083 exact_family_and_extremizers=11 direct_SAS_levels_2_to_8=7 symbolic_witness_levels_4_to_79=76
```

These are finite corroborations. The quantifier over all \(n\ge2\) is justified by the arch and Fibonacci arguments, not by extrapolation.

## Relationship to prior work
Bernini–Ferrari–Pinzani–West (2013) develop the Dyck subword pattern poset, in which both pattern and host are Dyck paths. That differs from requiring **every binary word** as a scattered subsequence, and their enumerations do not imply the displayed near-perfect classification.

Kosche–Koß–Manea–Siemer (2021) develop the arch and shortest-absent-subsequence framework and prove the gluing lemma and unrestricted fixed-universality extremality. These tools are used here, but they do not impose Dyck prefix balance, count this restricted class, or give the sharp \(F_n\) extremum.

The published note *Fibonacci extremals for shortest absent subsequences of binary words* gives the unrestricted maximum \(F_{n+3}\) for **all binary words of length \(2n\)**. That larger unrestricted statement does not determine the lower, Dyck-constrained maximum \(F_n\), its two extremizers, or the exact \(2^{n-1}-1\) near-perfect count. The published note *Closed-form law for binary subsequence universality* counts all binary words by length and universality index without imposing the Dyck prefix condition; it likewise does not imply the restricted classification from its stated generating function alone.

## Limitations
The result concerns binary Dyck words with universality index exactly one below the length bound. It does not give a full distribution of \(S(w)\) over this class, the analogous answer for general index deficits, or results for other alphabets. A search of the accessible literature and mathematical records found no equivalent statement, but equivalence under an unindexed alternative formulation remains a possible originality risk. No independent scientific audit is claimed.

## References
1. A. Bernini, L. Ferrari, R. Pinzani, J. West, *The Dyck pattern poset*, arXiv:1303.3785v1, publicly submitted 2013-03-15, https://arxiv.org/abs/1303.3785.
2. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968v1, publicly submitted 2021-08-31, especially Definition 2.3 and Lemma 3.16, https://arxiv.org/abs/2108.13968.
3. *Fibonacci extremals for shortest absent subsequences of binary words*, publicly indexed mathematical result (2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-fibonacci-extremals-for-shortest-absent-subsequences-of-binary-w--1a6556f14d28.
4. *Closed-form law for binary subsequence universality*, publicly indexed mathematical result (2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-closed-form-law-for-binary-subsequence-universality--e77c4e8d9f37.
