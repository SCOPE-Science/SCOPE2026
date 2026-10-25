# Seven-or-eight minimal unique factors in separated five-run binary words

## Finding

For a finite binary word \(w\), a **minimal unique factor** is a nonempty contiguous factor occurring exactly once in \(w\), all of whose proper contiguous factors occur at least twice. Occurrences count starting positions, including overlaps.

For positive integers \(a,b,c,d,e\), set
\[
w=0^a1^b0^c1^d0^e,\quad A=\max(a,c,e),\quad B=\max(b,d),\quad x=\min(a,c),\quad y=\min(b,d),\quad z=\min(c,e).
\]
Assume the **separation condition**
\[
\min\{|a-c|,|a-e|,|c-e|,|b-d|\}\ge2.
\]
Then the *entire* set of minimal unique factors is precisely
\[
\begin{split}
\mathcal U(w)=\{&0^A,\ 1^B,\ 0^{x+1}1,\ 01^{y+1},\ 1^{y+1}0,\ 10^{z+1},\ 01^y0\}\\
&\quad\cup\begin{cases}\{10^c1\},&c<\min(a,e),\\\varnothing,&c>\min(a,e).\end{cases}
\end{split}
\]
(The separation hypothesis excludes equality in the latter comparison.) In particular,
\[
|\mathcal U(w)|=7+\mathbf1_{\{c<\min(a,e)\}}.
\]

For each length \(n\ge13\), let \(G_{n,7}\) and \(G_{n,8}\) count the positive five-run compositions satisfying separation and having respectively seven or eight minimal unique factors. Their exact generating functions are
\[
\sum_{n\ge13}G_{n,7}t^n=\frac{8t^{13}}{(1-t^3)(1-t^2)^2(1-t)^2},\qquad
\sum_{n\ge13}G_{n,8}t^n=\frac{4t^{13}}{(1-t^3)(1-t^2)^2(1-t)^2}.
\]
Thus for *every* \(n\ge13\), conditioning a uniformly selected positive five-run composition on the separation condition gives exact probabilities \(2/3\) for seven and \(1/3\) for eight minimal unique factors.

Without conditioning, if the run lengths are uniformly chosen among all positive compositions of \(n\), then the number \(N_n\) of minimal unique factors satisfies
\[
\Pr(N_n=7)=\frac23+O(n^{-1}),\qquad
\Pr(N_n=8)=\frac13+O(n^{-1}),\qquad
\Pr(N_n\notin\{7,8\})=O(n^{-1}).
\]
The implied constants are absolute.

## Assumptions and scope

Every run length is a positive integer. The seven/eight-factor classification requires the four explicit pairwise separation inequalities; it makes no claim of an exact classification for exceptional tuples violating them. The generating functions count the ordered run-length compositions, or equivalently the binary words beginning with zero and having exactly five nonempty maximal constant runs. The unconditional distribution statement concerns that same uniform finite set of words, *not* uniformly random independent bits. Complementing every word gives the corresponding statement for words beginning with one.

## Proof

**Unique-factor criterion.** A factor \(u\) is minimally unique exactly when it occurs once and both its prefix and suffix obtained by deleting one symbol occur at least twice. This follows because every proper contiguous factor is contained in one of those two length-\((|u|-1)\) factors; the empty word is repeated by convention. Both symbols occur in at least two runs, so no one-letter factor is unique.

**One-run factors.** Among the three zero runs, \(A\) is a unique strict maximum. Hence \(0^A\) occurs once, while every \(0^j\) with \(1\le j<A\) occurs at least twice within the longest run itself. There is no other minimally unique zero-only factor. The two one runs similarly yield exactly \(1^B\).

**Two-run factors.** A factor \(0^i1^j\) with \(i,j\ge1\) can occur only at the two zero-to-one transitions with run-length pairs \((a,b)\) and \((c,d)\), exactly once at each transition if it fits. Thus it repeats exactly when \(i\le x=\min(a,c)\) and \(j\le y=\min(b,d)\). If both \(i,j\ge2\), minimal uniqueness would force \(0^{i-1}1^j\) and \(0^i1^{j-1}\) to repeat; hence \(i\le x\) and \(j\le y\), forcing the original to repeat, a contradiction. If \(j=1\) and \(i\ge2\), minimal uniqueness forces \(i=x+1\) because \(0^{i-1}1\) must repeat. The candidate \(0^{x+1}1\) occurs just once and its other deletion is \(0^{x+1}\), which repeats within the larger of runs \(a,c\) since their lengths differ by at least two. Dually, the only minimally unique candidate with \(i=1\) is \(01^{y+1}\), whose pure-one deletion repeats within the larger of runs \(b,d\). Consequently precisely these two zero-to-one factors are minimal unique.

The same argument applied to the one-to-zero transition pairs \((b,c)\) and \((d,e)\) gives precisely \(1^{y+1}0\) and \(10^{z+1}\).

**Three-run factors.** Every \(0^i1^j0^k\) factor, with \(i,j,k\ge1\), must cross one whole one run, hence \(j\in\{b,d\}\). Since \(b\ne d\), either full middle run identifies a unique occurrence. Minimality therefore forces \(i=k=1\): if either exponent exceeded one, deleting that endpoint would leave a three-run factor crossing the same unique middle run. Of \(01^b0\) and \(01^d0\), only \(01^y0\), with \(y=\min(b,d)\), has both one-symbol deletions repeated: the shorter interior one run contributes one occurrence of each two-run deletion, and the longer run contributes a second. The longer-middle candidate has a one-occurrence deletion.

Every \(1^i0^j1^k\) factor must cross the unique zero run that has ones on both sides, so \(j=c\) and again minimality forces \(i=k=1\). The factor \(10^c1\) is unique; its two one-symbol deletions repeat precisely when \(e\ge c\) and \(a\ge c\), respectively. The separation condition makes this equivalent to \(c<\min(a,e)\).

**Factors with at least four runs.** Any factor with four or more runs has a proper unique factor. For a four-run factor starting in zero, a proper prefix ending in its third run crosses the entire first inner one run of length \(b\). The only alternative zero-one-zero triple has inner one run length \(d\ne b\), so this proper prefix occurs once. For a four-run factor starting in one, a proper prefix with three runs crosses the unique one-zero-one triple centered on the third run, so is unique. A five-run factor contains a four-run factor as a proper factor, which is itself unique. Thus no factor with four or five runs is minimal unique. These cases exhaust all possible factors, proving the displayed set.

**Enumeration.** To generate the three labeled zero-run lengths that are pairwise separated by at least two, first choose their increasing rearrangement. Writing its members as \(1+i,3+i+j,5+i+j+k\), where \(i,j,k\ge0\), and permuting the three values gives the generating series \(6t^9/((1-t^3)(1-t^2)(1-t))\). The two one-run lengths separated by at least two similarly contribute \(2t^4/((1-t^2)(1-t))\). Their product is \(12t^{13}/((1-t^3)(1-t^2)^2(1-t)^2)\). In exactly two of the six permutations of the three distinct zero-run lengths, \(c\) is smallest, independently of the one-run pair. Hence one third of each coefficient counts eight factors and two thirds count seven, giving both exact generating functions.

**Unconditional limit with a rate.** There are \(\binom{n-1}{4}\) positive five-part compositions of \(n\). For any fixed pair of coordinates and fixed difference in \(\{-1,0,1\}\), the number satisfying that difference is \(O(n^3)\): choose one coordinate (\(O(n)\) possibilities), which determines the other, then distribute the remaining sum among three positive coordinates (\(O(n^2)\) possibilities). A union bound over the four coordinate pairs in the separation hypothesis gives an exceptional probability \(O(n^{-1})\). Conditional on nonexceptionality, the exact probabilities are \(2/3\) and \(1/3\). The unconditional bounds follow.

## Verification

The accompanying `verify.py` independently constructs the complete multiset of contiguous factors using overlapping occurrences. For all 1,800 separated five-run parameter tuples with lengths in \(\{1,\dots,7\}\), it checks equality of the literal minimal-unique-factor set with the eight-pattern formula, including conditional absence of the eighth pattern. It also builds full unrestricted histograms at lengths 15, 20 and 25, and checks the two rational generating-function coefficients against direct compositions at every length 13 through 32. Run with `python verify.py` using Python 3; no dependencies are required. The infinite theorem is proved above, not inferred from these finite computations.

## Relationship to prior work

Mieno et al., *Space-Efficient Algorithms for Computing Minimal/Shortest Unique Substrings* (arXiv:1905.12854, first posted 2019-05-30), give general representations and algorithms for MUSs and shortest unique substrings. Mieno et al., *Minimal Unique Substrings and Minimal Absent Words in a Sliding Window* (arXiv:1909.02804, first posted 2019-09-06), develop sliding-window combinatorial and algorithmic results. Nishimoto and Tabei, *R-enum* (arXiv:2004.01493, first posted 2020-04-03), enumerate MUSs in compressed BWT space. Kimura and I, *R-enum Revisited* (arXiv:2511.11057, first posted 2025-11-14), prove a general \(2r\) upper bound using the number of BWT runs. These results supply definitions, general algorithms and complexity bounds; the exact separated five-run factor list and the conditioned/unconditioned two-point distribution are distinct, family-specific enumerative conclusions.

## Limitations

The explicit factor list is conditional on run-length separation. Exceptional compositions are not classified by this theorem, though they constitute only \(O(n^{-1})\) of the uniform composition model. The law does not apply to uniformly independent Bernoulli words. Literature comparison cannot exclude equivalent specializations buried in other string-algorithm results.

## References

1. T. Mieno, D. Köppl, Y. Nakashima, S. Inenaga, H. Bannai, M. Takeda, *Space-Efficient Algorithms for Computing Minimal/Shortest Unique Substrings*, arXiv:1905.12854 (2019), https://arxiv.org/abs/1905.12854.
2. T. Mieno et al., *Minimal Unique Substrings and Minimal Absent Words in a Sliding Window*, arXiv:1909.02804 (2019), https://arxiv.org/abs/1909.02804.
3. T. Nishimoto and Y. Tabei, *R-enum: Enumeration of Characteristic Substrings in BWT-runs Bounded Space*, arXiv:2004.01493 (2020), https://arxiv.org/abs/2004.01493.
4. K. Kimura and T. I, *R-enum Revisited: Speedup and Extension for Context-Sensitive Repeats and Net Frequencies*, arXiv:2511.11057 (2025), https://arxiv.org/abs/2511.11057.
