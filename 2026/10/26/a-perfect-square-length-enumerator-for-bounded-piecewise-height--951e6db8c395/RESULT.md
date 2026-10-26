# A perfect-square length enumerator for bounded piecewise height of four-run binary words

## Finding

For a binary word \(w\), let \(h(w)\) denote its **piecewise height**: the smallest nonnegative integer \(k\) such that the collection of all scattered subsequences of \(w\) of length at most \(k\) distinguishes \(w\) from every other binary word. For positive integers \(a,b,c,d\), set \(w=0^a1^b0^c1^d\). For every integer \(H\ge 3\), define

\[
S_m(z)=\sum_{j=1}^{m}z^j\quad(m\ge0),\qquad
T_m(z)=\sum_{j=2}^{m}z^j\quad(m\ge1),
\]

where an empty sum is zero, and set

\[
P_H(z)=zS_{H-2}(z)+S_{H-3}(z)T_{H-2}(z).
\]

**Theorem (complete bounded-height length enumerator).** The following identity holds as an equality of polynomials for every integer \(H\ge3\):

\[
\boxed{\sum_{\substack{a,b,c,d\ge1\\h(0^a1^b0^c1^d)\le H}}
 z^{a+b+c+d}=P_H(z)^2.}
\]

Consequently, the number of four-run binary words beginning with zero and having height at most \(H\), with no restriction on their length, is exactly

\[
\boxed{(H^2-5H+7)^2.}
\]

The exact length-and-height enumerator is \(P_H(z)^2-P_{H-1}(z)^2\) for \(H\ge4\), while height \(3\) occurs only for the word `0101`. Words beginning with one have the same enumerator by exchanging alphabet symbols; hence the corresponding count for all binary words with exactly four runs is twice the displayed value.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). A subsequence means an order-preserving, not necessarily contiguous, selection of positions. The empty subsequence is included in the defining collection without affecting height. All four run lengths are positive integers. A word with four maximal constant-letter runs and initial symbol zero has a unique representation \(0^a1^b0^c1^d\), so the sum does not overcount words.

The key intermediary identity is

\[
\boxed{h(0^a1^b0^c1^d)=
\max\{a+\min(c,2)+1,\ b+2,\ c+2,\ d+\min(b,2)+1\}.}
\]

This intermediary formula specializes previously published methods for computing piecewise height. The theorem's enumerative claim is the all-parameter generating polynomial and its square factorization, not a claim to have introduced piecewise height, its general algorithms, or their binary reduction.

## Proof

**1. Published distance characterization.** Write \(u\sim_k v\) if \(u\) and \(v\) have identical sets of scattered subsequences of length at most \(k\). The right side-distance \(r(x,t)\) is the largest \(k\) such that \(x\sim_k xt\), and \(\ell(t,x)=r(x^{\mathrm{rev}},t^{\mathrm{rev}})\). Here \(t\) is a letter. For a binary word \(w\), the insertion/deletion characterizations and the binary identity \(h(w)=\rho(w)+1\) from [1, Sections 3.1--3.4] give

\[
h(w)=2+\max_{w=u t v}\{r(u,t)+\ell(t,v)\},
\]

where the maximum is over every individual symbol occurrence \(t\) of \(w\), with its prefix \(u\) and suffix \(v\). This is a theorem of [1], used here rather than reproved.

For clarity, its side-distances satisfy the recurrence [1, Lemma 3.6]: \(r(u,t)=0\) when \(t\) does not occur in \(u\), and if \(u=x t y\) with no \(t\) in \(y\), then

\[
r(u,t)=1+\min_{s\in\operatorname{alph}(ty)}r(x,s).
\]

Thus the relevant distances may be calculated directly, without enumerating arbitrary comparison words.

**2. Uniform contributions within each run.** Fix \(a,b,c,d\ge1\) and an occurrence at position \(j\) within its own run, counting \(j\) from one. The recurrence yields the following complete table; the last column equals \(r(u,t)+\ell(t,v)+1\), the corresponding candidate for \(\rho(w)\).

| Run containing \(t\) | \(r(u,t)\) | \(\ell(t,v)\) | Candidate for \(\rho(w)\) |
|---|---:|---:|---:|
| First, \(0^a\) | \(j-1\) | \(a-j+\min(c,2)\) | \(a+\min(c,2)\) |
| Second, \(1^b\) | \(j-1\) | \(b-j+1\) | \(b+1\) |
| Third, \(0^c\) | \(j\) | \(c-j\) | \(c+1\) |
| Fourth, \(1^d\) | \(j-1+\min(b,2)\) | \(d-j\) | \(d+\min(b,2)\) |

Each displayed value holds for every \(1\le j\le\) the corresponding run length, including singleton runs. For example, the recurrence yields \(r(0^a1^b0^c,1)=\min(b,2)\); the reverse recurrence gives the first-row suffix entry. Taking the maximum of the four entries and adding one proves the intermediary identity in the preceding section.

**3. Decoupling the parameters.** Define

\[
g(x,y)=\max\{x+\min(y,2)+1,\ y+2\}\qquad(x,y\ge1).
\]

The four-term height expression becomes exactly

\[
h(0^a1^b0^c1^d)=\max\{g(a,c),g(d,b)\}.
\]

For \(H\ge3\), the inequality \(g(x,y)\le H\) is equivalent to the disjoint alternatives

\[
\begin{cases}
y=1, &1\le x\le H-2,\\
2\le y\le H-2, &1\le x\le H-3.
\end{cases}
\]

The length polynomial for one admissible pair \((x,y)\) is therefore

\[
\sum_{\substack{x,y\ge1\\g(x,y)\le H}}z^{x+y}
=zS_{H-2}(z)+S_{H-3}(z)T_{H-2}(z)=P_H(z).
\]

The admissibility restrictions on the two disjoint parameter pairs \((a,c)\) and \((d,b)\) are independent, and their lengths add. Multiplying these two identical pair enumerators proves the perfect-square identity. Evaluating at \(z=1\) gives \(P_H(1)=(H-2)+(H-3)^2=H^2-5H+7\). Subtracting successive height-bounded generating polynomials proves the exact-height assertion. At \(H=3\) the only admissible pair is \((1,1)\), yielding the single four-run word `0101`.

## Verification

The accompanying `verify_piecewise.py` implements a finite independent check using greedy subsequence automata, rather than the right-distance recurrence. It checks all \(8^4=4096\) positive four-run parameter quadruples with each run length between one and eight. It separately checks the polynomial coefficient identities at every integer height from \(3\) through \(11\), and fixed-length extremal heights through length \(25\). For short binary words it directly constructs all distinct scattered subsequences to independently check the greedy-automata distances for \(8192\) one-letter insertions.

Run: `python3 verify_piecewise.py`. Expected terminal line:

`VERIFY_OK four_run_bfs=4096 height_polynomials=9 length_extrema=22 direct_subword_pairs=8192`

These finite checks do not constitute an infinite proof; the all-parameter result follows from the side-distance characterization and the displayed algebraic factorization.

## Relationship to prior work

Praveen, Schnoebelen, Veron, and Vialard [1] introduce the piecewise minimality index and prove the individual-word distance formulas, binary equality, and algorithms from which the intermediary height identity may be derived. Schnoebelen and Vialard [2] give a particularly relevant direct binary run-block formula when internal blocks are non-singletons (Lemma 5.3), transformations handling isolated letters (Lemmas 5.4--5.5), and an exact **global** maximum word length at bounded height (Theorem 5.7). In the region \(b,c\ge2\), the intermediary height identity agrees exactly with [2, Lemma 5.3]. These published results are credited rather than reclaimed.

The enumerative result here is the exact polynomial counting **every length** and **every height threshold** within the four-run family, including singleton internal blocks. Its perfect-square factorization comes from the pairing \((a,c)\), \((d,b)\). Neither cited source presents this all-coefficient polynomial or the unrestricted four-run cumulative count in the inspected relevant sections. This is a short enumerative specialization of the published wordwise theory, not a new general decision algorithm.

## Limitations

The square identity is specific to four nonempty alternating runs of a binary word. It does not claim an analogous factorization for arbitrary run counts or larger alphabets. The intermediary formula relies on established theorems from [1]. The novelty is therefore limited to exact weighted enumeration and decoupling in this particular family. General binary algorithms in [1,2] can compute every individual height, and it is possible an unindexed source or unstated summation of these formulas already records an equivalent aggregate count. No independent external mathematical audit has been performed.

## References

[1] M. Praveen, Ph. Schnoebelen, J. Veron, I. Vialard, *On the piecewise complexity of words and periodic words*, arXiv:2311.15431v1, publicly posted 2023-11-26. https://arxiv.org/abs/2311.15431 . Relevant material: Sections 3.1--3.4 and 4, especially Proposition 3.4, Theorem 3.11, Lemma 3.6.

[2] Ph. Schnoebelen, I. Vialard, *On the piecewise complexity of words*, arXiv:2412.16560v1, publicly posted 2024-12-21. https://arxiv.org/abs/2412.16560 . Relevant material: Section 5, Lemmas 5.3--5.5, Theorems 5.6--5.7, and Appendix A.1.
