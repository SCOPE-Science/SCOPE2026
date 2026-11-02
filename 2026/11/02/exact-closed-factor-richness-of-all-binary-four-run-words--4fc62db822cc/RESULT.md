# Exact closed-factor richness of all binary four-run words

## Finding

A word is **closed** if it is empty, has length one, or has a nonempty proper border (an equal prefix and suffix) with no internal occurrence. Equivalently, it is a complete first return to a proper factor. Count the empty word once. For a finite word \(w\), let \(\mathcal C(w)\) be its set of **distinct contiguous closed factors**, and put \(C(w)=|\mathcal C(w)|\).

**Theorem.** For positive integers \(a,b,c,d\), write
\[
w=0^a1^b0^c1^d,\qquad n=a+b+c+d,
\qquad x=\min(a,c),\quad y=\min(b,d).
\]
Then
\[
\boxed{C(w)=n+1+xy.}
\]
The same formula holds with the letters exchanged. Thus, for every integer \(n\ge4\),
\[
\boxed{\max_{\operatorname{runs}(w)=4,\ |w|=n}C(w)
=n+1+\left\lfloor\frac{\lfloor n/2\rfloor^2}{4}\right\rfloor.}
\]
Among length-\(n\) words beginning with \(0\), the exact number of maximizers is \(1,4,2,8\) for \(n\equiv0,1,2,3\pmod4\), respectively. The count over both starting letters is twice this.

More generally, define the excess \(E(w)=C(w)-n-1\). The complete two-variable generating series of four-run words beginning with \(0\) is
\[
\sum_{a,b,c,d\ge1}z^{a+b+c+d}u^{E(0^a1^b0^c1^d)}
=\left(\frac{1+z}{1-z}\right)^2\sum_{x,y\ge1}z^{2(x+y)}u^{xy}.
\]
In particular, summing excesses over all four-run words beginning with \(0\) gives
\[
\sum_{n\ge4} z^n\sum_{\substack{a+b+c+d=n\\a,b,c,d\ge1}}E(0^a1^b0^c1^d)
=\frac{z^4}{(1-z)^6(1+z)^2}.
\]
Both generating series are formal power series and require no convergence assumptions.

## Assumptions and scope

All factors are **linear, contiguous, distinct words**, not positioned occurrences or circular factors. Every run exponent is positive, so the displayed word has exactly four maximal equal-letter runs. Closedness is checked within each factor itself, not relative to occurrences in the ambient word. Single letters and the empty word are closed. Relabeling \(0\) and \(1\) preserves closed factors. No claim is made for words having a different number of runs or for alphabets of more than two symbols.

## Proof

**1. Classification by run count.** Every nonempty factor of \(w\) has from one to four runs. A closed one-run factor is a power of one letter. The distinct one-run closed factors are \(0^i\) for \(1\le i\le\max(a,c)\) and \(1^j\) for \(1\le j\le\max(b,d)\), giving \(\max(a,c)+\max(b,d)\) words.

No factor with exactly two runs is closed: its first and last letters differ, so it has no nonempty border.

A three-run factor must be \(0^i1^b0^j\) or \(1^i0^c1^j\); the complete middle run is forced. Such a factor is closed exactly when its two outer run lengths agree. Indeed, when the outer lengths agree, the whole first outer run is a border with exactly the two terminal occurrences. If they differ, any border is a constant-letter power of length at most the smaller outer run and appears internally within the longer outer run. The corresponding distinct factors are
\[
0^i1^b0^i\quad(1\le i\le x),\qquad
1^j0^c1^j\quad(1\le j\le y),
\]
so their count is \(x+y\).

A four-run factor has necessarily the form \(0^i1^b0^c1^j\), with \(1\le i\le a\) and \(1\le j\le d\). Any nonempty border must start with \(0\) and end with \(1\). Its suffix occurrence must begin in the third run; hence the border is of the form \(0^r1^s\). To coincide with the prefix and suffix we must have \(r=i\) and \(s=j\). Such a border exists exactly when \(i\le c\) and \(j\le b\), equivalently \(1\le i\le x\), \(1\le j\le y\). It has exactly two occurrences, one across each of the two \(01\) transitions; there is no third transition. Thus these and only these four-run factors are closed:
\[
0^i1^b0^c1^j\qquad(1\le i\le x,\ 1\le j\le y).
\]
They are all distinct and number \(xy\). The run-count classes are disjoint, and exponents identify words within each class. Consequently
\[
C(w)=1+\max(a,c)+\max(b,d)+x+y+xy
=1+(a+c)+(b+d)+xy=n+1+xy.
\]

**2. Fixed-length sharpness and all maximizers.** Since \(2x\le a+c\) and \(2y\le b+d\), we have \(x+y\le\lfloor n/2\rfloor\). For fixed positive integral sum, the product \(xy\) is maximal when the integers differ by at most one. Hence
\[
xy\le\left\lfloor\frac{\lfloor n/2\rfloor^2}{4}\right\rfloor.
\]
Equality requires \(x+y=\lfloor n/2\rfloor\), \(\{x,y\}=\{\lfloor\lfloor n/2\rfloor/2\rfloor,\lceil\lfloor n/2\rfloor/2\rceil\}\), and a residual \(n-2(x+y)\) of either zero or one. If zero, each outer same-letter pair has equal lengths; if one, it is assigned to exactly one of the four runs. This yields the exact maximizer counts \(1,4,2,8\) by the residue of \(n\) modulo four. Every equality case meets the bound, and exchanging letters gives the second starting-letter family.

**3. Generating series.** For fixed \(x\ge1\), the series counting ordered pairs \((a,c)\) of positive integers with \(\min(a,c)=x\) is
\[
z^{2x}\left(1+2z+2z^2+\cdots\right)
=z^{2x}\frac{1+z}{1-z}.
\]
The same calculation holds for \((b,d)\) with minimum \(y\). Their contributions are independent, and the excess is exactly \(xy\), proving the bivariate series. Differentiating formally in \(u\) at \(u=1\) yields
\[
\left(\frac{1+z}{1-z}\right)^2
\left(\sum_{x\ge1}xz^{2x}\right)^2
=\frac{z^4}{(1-z)^6(1+z)^2},
\]
as stated.

## Verification

Run `python3 verify_closed_four_runs.py` from the extracted directory. The standalone standard-library program independently constructs closed factors in two ways: (i) direct counting of border occurrences and (ii) longest-border prefix-function checking. It also constructs the five run-pattern classes in the proof and compares their actual sets. It exhausts every positive four-run composition through length \(16\), checks \(128\) additional seeded longer instances, checks the exact maximizer counts, and compares coefficients of the bivariate enumerator through length \(20\). A successful run prints `VERIFY_OK` with the number of tested words. The program is a finite cross-check, while the proof above establishes the identities for every length.

For example, \(w=0^3 1^3 0^3 1^3\) (length \(12\)) has \(C(w)=12+1+3\cdot3=22\), the unique maximum among length-\(12\) four-run words beginning with \(0\).

## Relationship to prior work

Badkobeh, Fici and Lipták established the general lower bound \(C(w)\ge|w|+1\), characterized binary words meeting it, and used a four-block binary construction to show quadratic closed-factor growth [1]. Their proof gives a lower-bound construction, not the exact count of all four-run words, its all-length maximum or its maximizers. The present exact factor classification quantifies the **first non-CR-poor binary run class** (all words with at most three linear runs are bitonic, hence CR-poor) and sharpens this particular four-block construction.

Parshina and Puzynina established the asymptotic unrestricted maximum \(\sim n^2/6\) for closed-factor richness [2]. This does not determine the sharp restricted four-run value, whose leading coefficient is \(1/16\). Thus the asymptotically optimal four-run richness is \(3/8\) of the unrestricted leading-order optimum; no unrestricted extremality is asserted.

## Limitations

Only binary finite words with exactly four positive-length runs are classified. The equalities do not determine the maximum among arbitrary words, words of at least five runs, or circular words. The originality assessment relies on the cited full-text comparisons and searches; it is not an assertion of definitive historical priority. Independent validation has not been performed.

## References

[1] G. Badkobeh, G. Fici, Z. Lipták, *On the Number of Closed Factors in a Word*, first posted May 28, 2013, arXiv:1305.6395, https://arxiv.org/abs/1305.6395 (see Theorem 23 and Theorem 25).

[2] O. Parshina, S. Puzynina, *Finite and Infinite Closed-Rich Words*, first posted November 1, 2021, arXiv:2111.00863, https://arxiv.org/abs/2111.00863 (see the Introduction, Preliminaries and asymptotic extremal theorem).
