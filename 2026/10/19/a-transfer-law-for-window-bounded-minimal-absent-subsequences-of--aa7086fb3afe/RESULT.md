# A transfer law for window-bounded minimal absent subsequences of cyclic permutation streams

## Finding

Let \(q\ge 2\), let \(\Sigma=\{0,1,\ldots,q-1\}\), and consider the one-sided periodic stream
\[
U_q=(0\,1\,\cdots\,q-1)^\omega.
\]
A word is *\(p\)-visible*, for an integer \(p\ge1\), if it occurs as a scattered subsequence of **at least one** contiguous length-\(p\) window of \(U_q\). A word is a *minimal absent \(p\)-subsequence* if it is not \(p\)-visible but all its proper scattered subsequences are \(p\)-visible. Distinct words, not position embeddings, are counted. Write \(A_q(p,m)\) for the number of these minimal absent words of length \(m\), and \(G_q(z,t)=\sum_{p\ge1,m\ge2}A_q(p,m)z^pt^m\).

Define the \(q\)-by-\(q\) polynomial matrix, indexed by \(1\le a,b\le q\),
\[
T_q(z)_{ab}=\begin{cases}z^b,&a+b>q,\\0,&a+b\le q.\end{cases}
\]
Then the **complete two-parameter length enumerator** is the rational formal series
\[
\boxed{G_q(z,t)=q t^2\sum_{a,b=1}^{q}z^a
  [(I-tT_q(z))^{-1}]_{ab}
  \sum_{e=1}^{\min(a,b)}z^{1-e}.}
\tag{1}
\]
In particular, for the alternating binary stream,
\[
\boxed{G_2(z,t)=\frac{2t^2z(2+z+t z^2)}{1-tz^2-t^2z^3}.}
\tag{2}
\]
If \(M(p)=\sum_m A_2(p,m)\), then
\[
\boxed{\sum_{p\ge1}M(p)z^p=\frac{2z(2+z+z^2)}{1-z^2-z^3}.}
\tag{3}
\]
Thus \(M(1)=4\), \(M(2)=2\), \(M(3)=6\), and \(M(p)=M(p-2)+M(p-3)\) for every \(p\ge4\). The initial totals are \(4,2,6,6,8,12,14,20,26,34,46,60\). The growth is
\[
M(p)\sim C\lambda^p,
\qquad \lambda^3=\lambda+1,\quad \lambda>1,
\quad C=\frac{2(2r+r^2+r^3)}{r(2r+3r^2)},\quad r=\lambda^{-1},
\]
where \(\lambda\approx1.3247179572\) is the plastic constant and \(C\approx2.0655064959\).

A direct *language classification*, which implies (1), is as follows. For every candidate \(v=v_1\cdots v_m\) of length \(m\ge2\), define cyclic-forward gaps \(d_j\in\{1,\ldots,q\}\), for \(1\le j<m\), as the unique number congruent to \(v_{j+1}-v_j\pmod q\). Put \(E=1+\sum_{j=1}^{m-1}d_j-p\). Then \(v\) is minimal absent if and only if
\[
\boxed{1\le E\le\min(d_1,d_{m-1})\quad\text{and}\quad
d_j+d_{j+1}>q\ \text{for every }1\le j\le m-2.}
\tag{4}
\]
The second condition is vacuous for \(m=2\). Thus the finite antichain of all minimal obstructions is given explicitly for each \(q,p\).

## Assumptions and scope

The stream extends indefinitely, but *one match* must lie in a single length-\(p\) window. Different words are considered distinct by their letter sequences, and windows may begin at any position of the periodic stream. No wraparound ambiguity arises: for any finite cyclic word \((0\cdots q-1)^h\) with \(qh\ge p\), the collection of all circular length-\(p\) windows, read in its infinite periodic lift, has exactly the same visible subsequences. This is not the same as taking subsequences of one fixed linear word, nor is it the same as allowing arbitrary-length windows. All identities are formal identities of power series; no convergence assumption is needed for (1)--(3).

A proper scattered subsequence is formed by deleting at least one letter. Since visibility is hereditary under deletions, minimality is equivalent to the visibility of all single-letter deletions. The one-letter words are all visible for \(p\ge1\), and therefore every minimal absent word has length at least two and at most \(p+1\).

## Proof

**Minimal span.** Fix a nonempty pattern \(v=v_1\cdots v_m\). In \(U_q\), after selecting one occurrence of \(v_j\), the first subsequent occurrence of \(v_{j+1}\) is exactly \(d_j\) positions later. Greedily selecting every such next occurrence minimizes the span from the first to the last selected symbol. The first symbol can be started at some stream position, and therefore the minimum possible window length containing \(v\) is exactly
\[
S(v)=1+\sum_{j=1}^{m-1}d_j.
\tag{5}
\]
Hence \(v\) is visible if and only if \(S(v)\le p\).

**Deletion costs.** For \(m\ge2\), deleting the first or last symbol decreases \(S\) by, respectively, \(d_1\) or \(d_{m-1}\). If an interior symbol \(v_{j+1}\) is removed, the two forward increments \(d_j,d_{j+1}\) are replaced by their sum reduced to the unique representative in \(\{1,\ldots,q\}\). Their total decrease is therefore \(0\) when \(d_j+d_{j+1}\le q\), and exactly \(q\) when \(d_j+d_{j+1}>q\). In particular, all deletion costs are nonnegative and at most \(q\).

Let \(E=S(v)-p\). The word is absent precisely when \(E\ge1\). Deleting its endpoints produces visible words if and only if \(E\le\min(d_1,d_{m-1})\). This already forces \(E\le q\). Each interior deletion is visible if and only if it has cost \(q\), which is equivalent to \(d_j+d_{j+1}>q\). As noted above, checking all single-letter deletions is sufficient. This proves both directions of (4), including \(m=2\).

**Weighted enumeration.** Every word of length \(m\ge2\) has a unique initial letter, with \(q\) choices, and a unique gap sequence \((d_1,\ldots,d_{m-1})\in\{1,\ldots,q\}^{m-1}\). Conversely these data uniquely determine the word. By (4), admissible gap sequences are exactly those with neighboring sums strictly greater than \(q\). With \(a=d_1\), \(b=d_{m-1}\), the permitted window sizes are
\[
p=1+\sum_jd_j-e,\qquad 1\le e\le\min(a,b).
\tag{6}
\]
All these values of \(p\) are positive. Weight the first gap by \(z^a\), each following gap by \(z^{d_j}\), and each additional symbol by \(t\). The transfer matrix for successive gaps is \(tT_q(z)\). The sum of all paths with at least one gap and given first and last gaps is
\[
t^2z^a[(I-tT_q(z))^{-1}]_{ab}.
\]
Multiplying by the window-size correction \(\sum_{e=1}^{\min(a,b)}z^{1-e}\), summing endpoints, and multiplying by the \(q\) choices for the first letter proves (1). The matrix has zero constant term in \(z\), so its formal inverse exists.

**Binary simplification.** For \(q=2\), gap sequences are words over increments \(1,2\) with no two consecutive \(1\)s. Their total-weight generating function including the empty sequence is \((1+z)/(1-z^2-z^3)\): each sequence is a sequence of blocks \(2\) (weight \(z^2\)) or \(12\) (weight \(z^3\)), optionally followed by one \(1\) (weight \(z\)). Thus the nonempty-sequence weight sum is \((z+z^2+z^3)/(1-z^2-z^3)\). The weight sum of sequences beginning and ending with \(2\) is \(z^2/(1-z^2-z^3)\). All sequences contribute one permitted excess \(e=1\); those beginning and ending with \(2\) also contribute \(e=2\), multiplying the latter class by an additional \(z^{-1}\). Restoring \(t\) to mark length, equivalently evaluating the displayed two-state transfer matrix, gives (2). Setting \(t=1\) proves (3) and the recurrence.

**Asymptotics.** The denominator \(1-z^2-z^3\) has one positive root \(r\in(0,1)\). Its reciprocal \(\lambda\) is the unique real root of \(\lambda^3-\lambda-1=0\), and its two other reciprocal roots have strictly smaller modulus. The numerator in (3) is nonzero at \(r\). The simple-pole coefficient formula therefore gives \(M(p)\sim C\lambda^p\) with the stated positive constant \(C=-N(r)/(rQ'(r))\), where \(N(z)=2z(2+z+z^2)\) and \(Q(z)=1-z^2-z^3\).

## Verification

Run the standalone Python 3 program `verify.py` using `python3 verify.py`. It independently constructs subsequences from all \(q\) distinct length-\(p\) windows, tests every candidate word of length at most \(p+1\) for absence and visibility of every single-letter deletion, and compares the resulting **sets of words**, not merely totals, against (4). It exhaustively checks \(11\) binary windows sizes \(p=1,\ldots,11\), \(8\) ternary sizes \(p=1,\ldots,8\), and \(6\) quaternary sizes \(p=1,\ldots,6\) (\(25\) parameter pairs). For binary windows it also independently compares each complete length histogram against the coefficient recurrence of (2), and checks total counts against (3). All assertions pass. The symbolic matrix identity has additionally been expanded exactly for alphabet sizes \(q=2,3,4,5\). Finite testing checks the implementation and boundary cases; the preceding proof establishes all \(q\ge2,p\ge1\).

## Relationship to prior work

Kosche, Koß, Manea and Pak, *Subsequences in Bounded Ranges: Matching and Analysis Problems* (arXiv:2207.09201, first public 19 July 2022), define bounded-range subsequences, minimal absent bounded-range subsequences, and their general algorithmic complexity. The article also studies subsequences of circular words. Its inspected full-text definitions, analysis theorems, circular-word section, and discussion of conclusions do not give the cyclic-permutation-stream antidictionary, transfer law (1), or plastic-constant binary enumerator (2)--(3). These notions and motivation are credited.

Kosche, Koß, Manea and Siemer, *Absent Subsequences in Words* (arXiv:2108.13968), give foundational characterizations and general enumeration approaches for minimal absent subsequences of **one linear finite word**, rather than a union of all periodic length-\(p\) windows. Manea, Ringleb, Siemer and Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String* (arXiv:2504.21471), improve algorithms in that finite-linear-word setting; they do not give the specific window-language enumeration here.

Related calculations for minimal absent subsequences of the fixed linear words \((01)^k\) and \((012)^k\) have different observational domains. In particular, a pattern is visible here if **any** phase's length-\(p\) window admits it, so its absent language is the intersection of the phase-specific absent languages and its minimal absent antichain is not obtained by a union of phase-specific minimal absent antichains. Existing linear length spectra alone do not imply the claimed circular-window spectra. The cyclic gap cost \(S\), sharp local minimality rule (4), and general transfer matrix address that distinction explicitly.

## Limitations

The theorem uses a periodic permutation cycle with each of the \(q\) symbols appearing exactly once in each period. It does not cover arbitrary periodic words, a single fixed linear host, or windows with nonuniform allowable spans. The binary plastic-constant asymptotic is not asserted for other alphabet sizes. Mathematical originality relies on the inspected and searchable literature rather than an exhaustive survey of all published work; an unindexed equivalent could exist. No independent audit has been performed.

## References

1. M. Kosche, T. Koß, F. Manea and V. Pak, *Subsequences in Bounded Ranges: Matching and Analysis Problems*, arXiv:2207.09201 (first public 19 July 2022), especially Definitions 2--3 and Sections 4--5. https://arxiv.org/abs/2207.09201
2. M. Kosche, T. Koß, F. Manea and S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (first public 31 August 2021), especially Section 3. https://arxiv.org/abs/2108.13968
3. F. Manea, T. Ringleb, S. Siemer and M. Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471 (first public 30 April 2025). https://arxiv.org/abs/2504.21471
