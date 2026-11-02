# Exact Abelian-factor spectra of cyclic distinct-run powers

## Finding
Fix an integer \(q\ge 3\), pairwise distinct letters \(a_0,\ldots,a_{q-1}\), positive integers \(r_0,\ldots,r_{q-1}\), and \(k\ge1\). Put \(P=a_0^{r_0}\cdots a_{q-1}^{r_{q-1}}\), \(p=\sum_i r_i\), \(W=P^k\), and \(S=\sum_{i<j}r_ir_j\). For \(1\le L\le kp\), let \(A_W(L)\) denote the number of distinct Parikh vectors of contiguous factors of \(W\) of length \(L\). Write \(x_+=\max(x,0)\).

**Exact length spectrum.** For \(1\le L\le(k-1)p\), put \(h=L\bmod p\), with \(0\le h<p\). Then
\[
A_W(L)=\begin{cases}
1,&h=0,\\
p-\displaystyle\sum_{i=0}^{q-1}\bigl((r_i-h)_++(r_i-(p-h))_+\bigr),&1\le h<p.
\end{cases}
\]
For \((k-1)p<L\le kp\), put \(h=L-(k-1)p\), so \(1\le h\le p\). Then
\[
A_W(L)=p-h+1-\sum_{i=0}^{q-1}(r_i-h)_+.
\]
In particular, the total number of nonempty distinct Parikh vectors of contiguous factors, counted across all lengths, is
\[
\boxed{\sum_{L=1}^{kp}A_W(L)=p+(2k-1)S+(k-1).}
\]
Every additional complete copy of the period therefore contributes exactly \(1+2S\) new Parikh vectors across its additional factor lengths. These are counts of *vectors*, not counts of factors or their occurrences.

## Assumptions and scope
The alphabet is precisely the \(q\) distinguished letters, which are pairwise distinct. All run lengths are strictly positive, and \(k\) is any positive integer. A factor is a contiguous, nonempty substring; its Parikh vector records the number of occurrences of each alphabet letter in the fixed order. Windows of different lengths cannot have the same Parikh vector because coordinate sums differ. No primitivity condition beyond distinct positive runs is imposed. The nonbinary hypothesis \(q\ge3\) is essential to the circular-window lemma.

## Proof
**Lemma 1 (linear windows).** A linear word consisting of positive blocks of pairwise distinct letters has, for any window length \(h\), the property that repetitions of a fixed Parikh vector occur only at *consecutive* starting positions. Indeed, the set of letters with positive coordinates uniquely identifies the interval of runs touched by the window. For a window touching at least two runs, the number of letters from its first run uniquely determines its starting position. For a one-run window, all starts yielding the same all-one-letter vector are consecutive within that run. Thus, as a window shifts through its \(p-h+1\) starting positions, the number of distinct vectors is one plus the number of shifts changing the vector:
\[
A_P(h)=1+\#\{0\le t<p-h:P_t\ne P_{t+h}\}.
\]
The two positions in this comparison coincide in a run of size \(r_i\) on exactly \((r_i-h)_+\) shifts. Therefore
\[
A_P(h)=p-h+1-\sum_i(r_i-h)_+,\quad 1\le h\le p.
\]

**Lemma 2 (circular windows).** For \(q\ge3\) and \(1\le h<p\), repetitions of any Parikh vector among the \(p\) cyclic starting positions are confined to one consecutive cyclic interval of starts. To see this, first suppose the window omits at least one alphabet letter. Its positive support is a proper nonempty *cyclic interval of run labels*. If it touches two or more runs, that support uniquely specifies the ordered first and last runs because the cyclic order and at least one missing label fix the break. The count in the first run then fixes the starting position. If the window touches only one run, all starts producing the same vector form one consecutive cyclic interval. If the window touches *all* \(q\) letters, consider its complementary circular window of length \(p-h\). Its Parikh vector is \((r_i)_i\) minus the original vector. This complementary window can touch at most two runs: otherwise a complete interior run would be absent from the original window, contradicting full support. Since \(q\ge3\), its support is proper, and the preceding cases apply; translating its starting position by \(h\) transfers consecutiveness to the original starts.

Consequently the circular list of Parikh vectors has no nonconsecutive repeats. It is not constant: the cyclic word \(P\) has smallest period \(p\), because each letter occupies exactly one nonempty run and \(q\ge3\); if the list were constant, consecutive windows would force \(P_t=P_{t+h}\) for all \(t\), hence a nontrivial cyclic period. Therefore the number of different circular window vectors is precisely the number of transitions between unequal consecutive vectors, equivalently
\[
C_P(h)=\#\{0\le t<p:P_t\ne P_{t+h\bmod p}\}.
\]
Inside run \(i\), the intersection of that run and its shift by \(h\) has \((r_i-h)_++(r_i-(p-h))_+\) positions (the two possible cyclic overlap placements). Summing yields
\[
C_P(h)=p-\sum_i\bigl((r_i-h)_++(r_i-(p-h))_+\bigr).
\]
Set \(C_P(p)=1\) for the complete period.

**Lemma 3 (complete powers).** A length-\(L\) window with \(L\le(k-1)p\) can start at each of the \(p\) residues modulo \(p\). If \(L=tp+h\) with \(1\le h<p\), the Parikh vector is \(t(r_i)_i\) plus the vector of a cyclic length-\(h\) window; if \(h=0\) it is constant. When \(L=(k-1)p+h\) with \(1\le h\le p\), only the \(p-h+1\) linear starting positions inside one copy of \(P\) remain; their Parikh vectors are \((k-1)(r_i)_i\) plus vectors of linear length-\(h\) factors of \(P\). Lemmas 1 and 2 give both formulas.

Finally
\[
\sum_{h=1}^p A_P(h)=\sum_{h=1}^p(p-h+1)-\sum_i\sum_{h=1}^p(r_i-h)_+
=p+\sum_{i<j}r_ir_j=p+S.
\]
And
\[
\sum_{h=1}^p C_P(h)=1+p(p-1)-\sum_i r_i(r_i-1)=1+2S.
\]
There are \(k-1\) full circular-length blocks and one terminal linear block. Hence the asserted total is \((k-1)(1+2S)+(p+S)\).

## Verification
The included `verify_abelian_spectrum.py` enumerates literal factor Parikh-vector sets at every length and independently evaluates both piecewise expressions and the total formula. It checks 3025 parameter instances, spanning alphabets of three through six letters and 77656 length-specific profiles. The script performs finite checks only; the preceding lemmas supply the proof for all permitted parameters.

For the binary boundary \(P=0011\), \(k=2\), the actual total is \(16\), while substituting the run lengths into the nonbinary formula would give \(17\). The theorem deliberately excludes \(q=2\).

## Relationship to prior work
Abelian complexity and Parikh (jumbled) indexing are established topics. Afshar, Amir, Goodrich, and Matias (2020) study exact learning and jumbled-index queries for periodic strings, rather than the present length-by-length count of distinct Parikh vectors for one-run-per-letter powers. Fici and Puzynina (2022) survey Abelian complexity, and Shallit (2020) develops techniques for automatic sequences; these works provide background and comparisons, not the stated exact formula. Rigo, Stipulanti, and Whiteland (2024) consider Parikh-collinear fixed points, with their main automatic-complexity result assuming non-ultimate periodicity. Searches did not locate an identical statement; this is not proof of exhaustive priority.

## Limitations
The classification is specific to cyclic powers of one distinct run per alphabet letter and requires at least three letters. It does not apply to arbitrary run repetitions, arbitrary ultimately periodic words, or binary cyclic two-run powers. Novelty is assessed against accessible sources and published-result searches, not certified against every possible earlier formulation. The computational checks are finite and not an alternative to the proof.

## References
- R. Afshar, A. Amir, M. T. Goodrich, P. Matias, *Adaptive Exact Learning in a Mixed-Up World: Dealing with Periodicity, Errors and Jumbled-Index Queries in String Reconstruction*, arXiv:2007.08787, first public 2020-07-17; https://arxiv.org/abs/2007.08787 .
- G. Fici, S. Puzynina, *Abelian Combinatorics on Words: a Survey*, arXiv:2207.09937 (2022); https://arxiv.org/abs/2207.09937 .
- J. Shallit, *Abelian Complexity and Synchronization*, arXiv:2011.00453 (2020); https://arxiv.org/abs/2011.00453 .
- M. Rigo, M. Stipulanti, M. A. Whiteland, *Automatic Abelian Complexities of Parikh-Collinear Fixed Points* (2024); https://arxiv.org/abs/2405.18032 .
