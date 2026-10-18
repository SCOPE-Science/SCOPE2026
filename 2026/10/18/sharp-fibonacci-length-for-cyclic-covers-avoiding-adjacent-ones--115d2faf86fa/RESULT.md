# Sharp Fibonacci length for cyclic covers avoiding adjacent ones

## Finding

Let \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). For each integer \(n\ge2\), let \(\mathcal L_n\) consist of all binary length-\(n\) words containing no consecutive ones. A cyclic word avoids consecutive ones when the last and first positions, as well as adjacent internal positions, do not both carry \(1\). Its length-\(n\) windows are read cyclically, with wraparound.

**Theorem.** The minimum length of a cyclic word avoiding consecutive ones and containing every member of \(\mathcal L_n\) among its length-\(n\) windows is

\[
\boxed{M_n=F_{n+2}+F_n-1}.
\]

There is an optimal cyclic word whose window multiset comprises one copy of each word of \(\mathcal L_n\), plus one extra copy of every word

\[
\mathcal D_n=\{0u0:\; u\in\{0,1\}^{n-2},\;u\text{ avoids }11,\;u\text{ contains a }1\}.
\]

Thus exactly \(F_n-1\) different admissible windows occur twice; every other admissible window occurs once. The statement includes \(n=2\), where \(\mathcal D_2\) is empty and the optimum cyclic word is \(010\).

## Assumptions and scope

No primitivity, canonical rotation, distinct-window requirement, or bound on repetitions is assumed. The alphabet is binary, the forbidden factor is exactly \(11\), and the set of required windows is defined by *linear* factor avoidance, not by whether the periodic repetition of each window avoids \(11\). This distinction matters: the word \(101\) is an allowed member of \(\mathcal L_3\), although periodic repetition of \(101\) contains \(11\). The theorem concerns every integer \(n\ge2\); the one-letter case is deliberately outside the statement.

## Proof

**1. Overlap graph and Fibonacci count.** Form the directed overlap multigraph \(G_n\). Its vertices are all length-\(n-1\) words avoiding \(11\). For every \(e=e_1\cdots e_n\in\mathcal L_n\), place a directed arc labeled \(e\) from the prefix \(e_1\cdots e_{n-1}\) to the suffix \(e_2\cdots e_n\). Different labels distinguish arcs even if their endpoints coincide. The usual two-state recurrence for words with no adjacent ones gives \(|\mathcal L_n|=F_{n+2}\). Cyclic words meeting the theorem's constraints correspond to closed walks using every arc of \(G_n\) at least once, with walk length equal to cyclic word length. Conversely, an Eulerian circuit in any augmented overlap multigraph spells the required cyclic word.

The graph \(G_n\) is strongly connected: from any vertex append \(n-1\) zeros to reach the all-zero vertex, then append the letters of any target vertex. Every intermediate word avoids \(11\).

**2. Explicit balancing augmentation.** Add a second copy of every arc labeled by a word in \(\mathcal D_n\). Its count is

\[
|\mathcal D_n|=|\mathcal L_{n-2}|-1=F_n-1,
\]

where \(\mathcal L_0\) is the singleton containing the empty word. For any length-\(n-1\) vertex \(v\), write \(I_0(v)\) for the indicator that its first symbol is zero, and \(T_0(v)\) for the indicator that its last symbol is zero. Then

\[
\deg^+_{G_n}(v)=1+T_0(v),\qquad
\deg^-_{G_n}(v)=1+I_0(v).
\]

The added arcs contribute one outgoing arc at \(v\) exactly when \(I_0(v)=1\) and \(v\) is not all zero; likewise they contribute one incoming arc exactly when \(T_0(v)=1\) and \(v\) is not all zero. Thus the total outgoing and incoming degrees agree at every vertex. The augmentation retains strong connectivity, hence admits an Eulerian circuit. Spelling that circuit gives a legal cyclic word of length \(F_{n+2}+F_n-1\) with precisely the claimed length-\(n\) window multiset.

**3. Sharp lower bound.** Put \(m=n-1\). Define an integer potential \(\phi(v)\) on length-\(m\) vertices by the number of initial zeros before the first \(1\), or \(m\) if no \(1\) occurs. For every admissible arc \(e:v\to w\),

\[
\phi(v)-\phi(w)\le1.
\]

Indeed, when the first symbol of \(v\) is \(0\) and a later \(1\) exists, the first \(1\) moves one place left under the shift; when \(v\) is all zeros, the decrease is either zero or one; and when \(v\) begins with \(1\), the decrease is nonpositive. Every arc of \(\mathcal D_n\) has equality, because its prefix begins with zero and contains a one before its final position.

Now take an arbitrary closed covering walk and subtract one occurrence of each original arc. This leaves a nonnegative integral multiplicity \(x_e\) of additional admissible arcs. Degree balance of the closed walk yields, for all vertices \(v\),

\[
\sum_{e\,\mathrm{out\ of}\,v}x_e-\sum_{e\,\mathrm{into}\,v}x_e
=\deg^-_{G_n}(v)-\deg^+_{G_n}(v).
\]

Consequently, by telescoping against \(\phi\) and the one-step potential bound,

\[
\begin{aligned}
\sum_e x_e
&\ge \sum_e x_e\bigl(\phi(\operatorname{tail}(e))-\phi(\operatorname{head}(e))\bigr)\\
&=\sum_v\phi(v)\bigl(\deg^-_{G_n}(v)-\deg^+_{G_n}(v)\bigr)\\
&=\sum_{e\in\mathcal D_n}\bigl(\phi(\operatorname{tail}(e))-\phi(\operatorname{head}(e))\bigr)\\
&=|\mathcal D_n|=F_n-1.
\end{aligned}
\]

The third equality is valid because the explicit \(\mathcal D_n\) augmentation balances every vertex, and the fourth uses tightness on each of its arcs. Thus every covering walk uses at least \(F_n-1\) additional arcs beyond the \(F_{n+2}\) required arcs. The explicit Eulerian construction attains the bound. This proves the theorem for every \(n\ge2\).

## Verification

The accompanying dependency-free script `check.py`, run with `python3 check.py`, generates all admissible words and the specified repeated-word multiset. For each \(2\le n\le17\), it checks the Fibonacci counts, all augmented degree equations, all arc-potential inequalities, tightness for added arcs, the exact potential-dual value, a Hierholzer Eulerian circuit, the complete cyclic window multiset, and cyclic avoidance of \(11\). It also independently exhausts every shorter legal cyclic binary candidate for \(2\le n\le5\). The output is recorded in `check_output.txt`. These finite checks are corroboration; the proof of the infinite theorem is the preceding augmentation and potential argument.

For orientation, the constructed optimum examples at orders \(n=3,4,5\) are `010100`, `0100101000`, and `01000100101010000`, of lengths \(6,10,17\) respectively.

## Relationship to prior work

The motivating 2026 paper of Gabric, Imam, Janik Jones and Sawada treats efficient decoding of bounded-*weight* de Bruijn cycles. Here the constraint is a forbidden adjacent pattern, and some windows must repeat in a shortest full cover. Moreno and Matamala (2007) study lexicographically least de Bruijn sequences for restricted languages, defining admissibility via periodic repetition of each word. That requirement excludes, for instance, \(101\) from the golden-mean length-three language, whereas this theorem requires it. Chee and collaborators study longest distinct-window run-length-limited sequences (2024), an objective different from shortest all-window coverage with repetitions. Their separate work on de Bruijn covering sequences and arrays uses Hamming-radius coverage, not exact membership in this forbidden-factor family. The general directed route-inspection (Chinese-postman) viewpoint motivates the lower bound, but the Fibonacci optimum and explicit repeated-window multiset are established here.

## Limitations

This result does not determine the number of optimal cyclic words or characterize *all* optimal repeated-window multisets. It does not address other forbidden patterns, nonbinary alphabets, or decoding algorithms. Literature overlap beyond the inspected sources, including differently indexed studies of directed postman completions for constrained overlap graphs, remains a risk. No independent scientific audit has been performed.

## References

1. D. Gabric, W. Imam, L. Janik Jones, J. Sawada, *Decoding universal cycles for t-subsets and t-multisets by decoding bounded-weight de Bruijn sequences*, arXiv:2603.11934 (first public March 12, 2026), https://arxiv.org/abs/2603.11934.
2. E. Moreno, M. Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings*, arXiv:0711.1695 (2007), https://arxiv.org/abs/0711.1695.
3. Y. M. Chee, T. Etzion, T. L. Nguyen, D. H. Ta, V. D. Tran, V. K. Vu, *Maximum Length RLL Sequences in de Bruijn Graph*, arXiv:2403.01454 (2024), https://arxiv.org/abs/2403.01454.
4. Y. M. Chee, T. Etzion, H. Ta, V. K. Vu, *On de Bruijn Covering Sequences and Arrays*, arXiv:2404.13674 (2024), https://arxiv.org/abs/2404.13674.
5. F. Chung, J. N. Cooper, *De Bruijn Cycles for Covering Codes*, arXiv:math/0310385 (2003), https://arxiv.org/abs/math/0310385.
