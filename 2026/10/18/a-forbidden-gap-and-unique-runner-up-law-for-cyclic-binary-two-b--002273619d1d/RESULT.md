# A forbidden-gap and unique runner-up law for cyclic binary two-binomial spread

## Finding

Let \(n\ge5\) and \(2\le b\le n-2\) be integers with \(\gcd(n,b)=1\); put \(a=n-b\). For any length-\(n\) binary word \(w\) containing \(b\) ones, let \(R_i(w)\) be its left cyclic shift by \(i\) positions. Define the scattered-pair count and its cyclic spread by

\[
F_i(w)=\#\{(j,k):0\le j<k<n,\ (R_iw)_j=0,\ (R_iw)_k=1\},\qquad
\Delta(w)=\max_{0\le i<n}F_i(w)-\min_{0\le i<n}F_i(w).
\]

**Theorem (first two cyclic-spread strata).** Among all words of the prescribed composition:

1. The minimum is \(\Delta=n-1\), attained by exactly one cyclic rotation class, the primitive Christoffel class. Its \(n\) distinct scattered-pair counts form the integer interval
\[
\left\{\frac{ab-n+1}{2},\frac{ab-n+1}{2}+1,\ldots,\frac{ab+n-1}{2}\right\}.
\]
2. The intermediate value \(\Delta=n\) is **impossible**.
3. The next attainable spread is \(\Delta=n+1\), again attained by exactly one cyclic rotation class. Its \(n\) distinct counts are exactly
\[
\left\{\frac{ab-n-1}{2},\frac{ab-n-1}{2}+2,\ldots,\frac{ab+n-1}{2}-1,\frac{ab+n+1}{2}\right\}.
\]
Equivalently, this is the full integer interval from \((ab-n-1)/2\) through \((ab+n+1)/2\), **minus the two integers one step above its minimum and one step below its maximum**. (The ellipsis in the displayed set enumerates every intermediate integer between the indicated endpoints.) Both classes contain exactly \(n\) words.

The unique minimizing necklace and unique runner-up necklace have explicit representatives: for \(0\le i\le n\), set
\[
r_i=(-bi)\bmod n,\qquad
h_i^{(0)}=r_i,\qquad
h_i^{(1)}=\begin{cases}n+1,&r_i=1,\\r_i,&r_i\ne1;\end{cases}
\]
and for \(0\le i<n\), define
\[
w_i^{(e)}=\frac{h_{i+1}^{(e)}-h_i^{(e)}+b}{n},\qquad e\in\{0,1\}.
\]
Each displayed digit is in \(\{0,1\}\); \(w^{(0)}\) is a conjugate of the primitive upper Christoffel word, and \(w^{(1)}\) is the unique runner-up up to rotation.

## Assumptions and scope

The statistic counts **scattered** occurrences, not adjacent factors. All rotations are linearized before counting, and extrema are taken across the \(n\) cuts of a single circular word. The coprimality and interior-composition hypotheses are essential to the stated uniqueness and to the existence of a second class. All \(n\) is quantified, with no finite-length cutoff.

## Proof

**Step 1: a cyclic height walk.** Fix a word \(w=w_0\cdots w_{n-1}\) in the domain. Let \(p_i=\sum_{j=0}^{i-1}w_j\) for \(0\le i\le n\) and define \(T_i=np_i-bi\). Then \(T_0=T_n=0\) and
\[
T_{i+1}-T_i=nw_i-b\in\{-b,a\}.
\]
Moving an initial \(0\) from the front to the end destroys \(b\) scattered \(01\)-pairs; moving an initial \(1\) destroys none and creates \(a\) pairs. Hence
\[
F_{i+1}(w)-F_i(w)=nw_i-b=T_{i+1}-T_i,\qquad F_i(w)=F_0(w)+T_i.
\]
Thus \(\Delta(w)=\max_iT_i-\min_iT_i\). Further, \(T_i\equiv-bi\pmod n\). As \(\gcd(n,b)=1\), the \(n\) values \(T_0,\ldots,T_{n-1}\) represent all residues modulo \(n\) exactly once; consequently the \(F_i\) are distinct and \(\Delta\ge n-1\).

**Step 2: normalization and minimum.** Rotate \(w\) to begin at its unique minimum-height index. Its new height walk is \(H_i=T_{t+i}-T_t\), extending \(T\) periodically, with \(H_0=H_n=0\) and \(\min_iH_i=0\). Its residues remain \(H_i\equiv-bi\pmod n\), so the \(n\) heights are determined by choosing one nonnegative representative of each residue within a range of length \(\Delta\). If \(\Delta=n-1\), the set of heights is precisely \(\{0,1,\ldots,n-1\}\); uniqueness of residue representatives forces \(H_i=r_i\). Its increments are \(-b\) or \(a\), so \(w_i=(H_{i+1}-H_i+b)/n\) is a binary word. In fact \(H_i=n\lceil bi/n\rceil-bi\), giving \(w_i=\lceil (i+1)b/n\rceil-\lceil ib/n\rceil\), the upper Christoffel word. Every minimizer must therefore be a rotation of that word. Since its rotation heights are distinct, it has exactly \(n\) distinct rotations.

**Step 3: the forbidden gap.** Suppose the normalized height range were \(\Delta=n\). Both \(0\) and \(n\) occur as heights, contradicting distinctness modulo \(n\). Thus no word has spread \(n\).

**Step 4: unique runner-up.** If \(\Delta=n+1\), both \(0\) and \(n+1\) occur as heights. Their residues are \(0\) and \(1\). The remaining residues \(2,\ldots,n-1\) each have only one representative in \(\{0,1,\ldots,n+1\}\), giving the forced height set
\[
\{0,2,3,\ldots,n-1,n+1\}
\]
and the forced sequence \(H_i=h_i^{(1)}\) determined by \(H_i\equiv-bi\pmod n\). Existence requires verifying the binary-step restriction. The ordinary residues \(r_i\) advance by \(-b\) or \(a\). Only the two steps entering and leaving residue \(1\) change upon lifting its height to \(n+1\). Their preceding and succeeding residues are \(b+1\) and \(a+1\), respectively. As \(a,b\ge2\), both lie between \(2\) and \(n-1\), and the modified steps are respectively \(a\) and \(-b\). Every step is consequently still in \(\{-b,a\}\); hence the displayed formula constructs a binary word. It has exactly \(b\) ones because the height walk is closed. Every possible runner-up is a rotation of this unique constructed word, whose heights are distinct. Again the class has exactly \(n\) rotations.

**Step 5: the exact integer spectra.** Let \(j_1<\cdots<j_b\) be the positions of ones in any representative. Directly counting earlier zeros at each one gives
\[
F_0=\sum_{s=1}^{b}j_s-\binom b2.
\]
On the other hand, summation of \(T_i=np_i-bi\) yields
\[
\sum_{i=0}^{n-1}T_i=n\left(\frac{b(n-1)}2-\sum_{s=1}^{b}j_s\right),\qquad
F_0=\frac{ab}{2}-\frac1n\sum_{i=0}^{n-1}T_i.
\]
For a normalized minimizing word, the height sum is \(n(n-1)/2\), whence \(F_0=(ab-n+1)/2\), and adding every height \(0,1,\ldots,n-1\) gives the first stated interval. For a normalized runner-up the height sum is \(n(n+1)/2\); hence \(F_0=(ab-n-1)/2\), and adding the heights \(\{0,2,\ldots,n-1,n+1\}\) gives exactly the punctured interval claimed. Since \(\gcd(n,b)=1\), \(ab-n+1\) is even, so all endpoints are integers. This completes the theorem.

## Verification

The included self-contained \(\texttt{check.py}\) enumerates every binary word with coprime interior composition for \(5\le n\le15\) and directly counts scattered \(01\)-subsequences for every rotation. It checks both constructions, complete spectra, the forbidden value, and uniqueness of each extremal rotation class. Results: 44 coprime parameter pairs, 33,122 words, 457,898 rotations, and 88 extremal necklaces; every assertion passed. The proof, not this finite census, establishes the unbounded result.

As examples, at \((n,b)=(7,3)\), the representative minimizing word is \(1010100\) with spectrum \(\{3,4,5,6,7,8,9\}\); the representative runner-up is \(1100100\) with spectrum \(\{2,4,5,6,7,8,10\}\).

## Relationship to prior work

Rigo, Stipulanti, and Whiteland treat scattered-subword binomial counts and characterize Sturmian words by binomial complexity; their stated results concern factor equivalence classes of infinite words, not the spread of one scattered-pair count over the rotations of a prescribed finite word. Bugeaud and Reutenauer classify Christoffel conjugates and their ordinary borders, but the inspected results do not calculate scattered-\(01\) cyclic spread. De Luca and Fici describe circular balance and Christoffel matrices, including the fact that neighboring sorted Christoffel conjugates differ by one adjacent swap. That accounts for familiar minimal-class regularity, not the forbidden gap and unique punctured runner-up class. Richomme's geometric and partition treatment of binary two-binomial coefficients concerns equivalence classes of individual words, not the two extremal spread strata of rotation orbits. A general rotation-difference identity for fixed-content binary two-binomial profiles is also available; the new result is the sharp spread/uniqueness/runner-up classification, not the difference identity by itself. Inaccessible or unindexed equivalent sources remain a residual originality risk.

## Limitations

The result is restricted to coprime interior binary compositions and scattered patterns of length two. It neither treats noncoprime compositions nor classifies spreads above \(n+1\), nor does it determine analogous spectra for length-three subsequences. The originality assessment is based on the identified accessible literature; it does not claim a comprehensive proof of absence from all publications. No independent mathematical audit has been performed.

## References

1. M. Rigo, M. Stipulanti, M. A. Whiteland, *Characterizations of families of morphisms and words via binomial complexities*, arXiv:2201.04603, first posted 12 January 2022. https://arxiv.org/abs/2201.04603
2. Y. Bugeaud, C. Reutenauer, *On the conjugates of Christoffel words*, arXiv:2202.05486, 2022. https://arxiv.org/abs/2202.05486
3. A. De Luca, G. Fici, *Some Results on Digital Segments and Balanced Words*, arXiv:2211.09417, 2022. https://arxiv.org/abs/2211.09417
4. G. Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, arXiv:2510.07159, 2025. https://arxiv.org/abs/2510.07159
