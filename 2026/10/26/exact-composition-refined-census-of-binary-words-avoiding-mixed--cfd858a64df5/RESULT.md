# Exact composition-refined census of binary words avoiding mixed Abelian squares

## Finding
Let \(T(x,y)\) count nonempty binary words with exactly \(x\) zeros and \(y\) ones whose contiguous Abelian-square factors are all monochromatic. For positive \(x,y\), the complete exact composition-refined count is
\[
T(x,y)=2+(y-1)\mathbf 1_{2\nmid x}+(x-1)\mathbf 1_{2\nmid y}+2\left\lfloor\frac{x}{4}\right\rfloor\left\lfloor\frac{y}{4}\right\rfloor.
\]
For \(x=0<y\) or \(y=0<x\), \(T(x,y)=1\). The empty word is excluded. A qualifying word has at most four runs, and its exact run characterization is given below. In particular, the generating function of the number \(t(n)\) of qualifying words of length \(n\ge1\) is
\[
\sum_{n\ge1}t(n)z^n=\frac{2z}{1-z}+\frac{2z^2}{(1-z)^2}+\frac{2z^3}{(1-z)^2(1-z^2)}+\frac{2z^8}{(1-z)^2(1-z^4)^2},
\]
with \(t(n)=n^3/48+O(n^2)\). These are counts of words, not counts of Abelian-square factors or of distinct Abelian-square patterns.

## Assumptions and scope
A binary word is a finite sequence over \(\{0,1\}\). A contiguous factor of even length \(2m\), \(m\ge1\), is an Abelian square if each of its two successive length-\(m\) halves has the same number of zeros and the same number of ones. A *mixed* Abelian square contains both letters; a *trivial* or monochromatic Abelian square contains just one letter. All words in this theorem avoid **mixed** Abelian squares but may contain arbitrarily long constant runs and therefore many trivial ones. A run is a maximal nonempty block of identical letters. All integers \(x,y\) are nonnegative and at least one is positive.

The complete characterization, with \(a\ne b\), is: a word of one or two runs always qualifies; \(a^h b^i a^j\) with positive parameters qualifies exactly when \(i\) is odd; \(a^h b^i a^j b^k\) with all parameters positive qualifies exactly when \(i,j\) are odd and \(h<j\), \(k<i\); no word with five or more runs qualifies. Here a run written \(a^h\) denotes \(h\) consecutive copies of the single symbol \(a\).

The exact bivariate generating function is
\[
\begin{aligned}
F(u,v)&=\sum_{\substack{x,y\ge0\\x+y\ge1}}T(x,y)u^xv^y\\
&=\frac{u}{1-u}+\frac{v}{1-v}+\frac{2uv}{(1-u)(1-v)}\\
&\quad+\frac{u^2v}{(1-u)^2(1-v^2)}+\frac{uv^2}{(1-v)^2(1-u^2)}\\
&\quad+\frac{2u^4v^4}{(1-u)(1-u^4)(1-v)(1-v^4)}.
\end{aligned}
\]

## Proof
**Five-run obstruction.** Suppose a word contains five consecutive runs \(a^A b^B a^C b^D a^E\) with positive lengths. If \(B\le D\) and \(C\) is even, the factor \(b^B a^C b^B\) is a mixed Abelian square, since its halves contain \(B\) copies of \(b\) and \(C/2\) copies of \(a\). If \(B\le D\) and \(C\) is odd, use \(a b^B a^C b^B\), whose two halves both have \(B\) copies of \(b\) and \((C+1)/2\) copies of \(a\). If \(B>D\), reverse the five-run word and apply the corresponding case with \(D<B\). Hence any qualifying word has at most four runs.

**One or two runs.** A mixed Abelian square must have both letters in both halves. With at most one change of letter, that is impossible, so every one- or two-run word qualifies.

**Three runs.** In \(a^h b^i a^j\), a mixed Abelian square cannot have only one run boundary, as its two halves would then have incompatible letter counts. It must cross both boundaries, so must include the entire interior \(b\)-run and have its midpoint inside that run. Equality of the numbers of \(b\)'s in the halves forces \(i\) even. Conversely, if \(i\) is even, the factor \(a b^i a\) is a mixed Abelian square, with one \(a\) and \(i/2\) copies of \(b\) per half. Thus the central run is odd exactly in the qualifying three-run case.

**Four runs: necessity.** In \(a^h b^i a^j b^k\), the preceding three-run argument, applied to both overlapping triples, forces \(i,j\) odd. If \(h\ge j\), the factor \(a^j b^i a^j b\) exists and is a mixed Abelian square: \(i\) is odd, and its two halves each contain \(j\) copies of \(a\) and \((i+1)/2\) copies of \(b\). If \(k\ge i\), the factor \(a b^i a^j b^i\) exists and is likewise a mixed Abelian square: \(j\) is odd, and each half has \((j+1)/2\) copies of \(a\) and \(i\) copies of \(b\). Thus \(h<j\) and \(k<i\) are necessary.

**Four runs: sufficiency.** Assume \(i,j\) odd, \(h<j\) and \(k<i\). A mixed Abelian-square factor cannot cross fewer than three boundaries: one boundary is impossible by the two-run argument, and two boundaries involve a complete odd central run, which is impossible by the three-run argument. Any remaining hypothetical square must span all three boundaries. Its midpoint lies in the second or third run. If it lies in the second run, the left half contains at most \(h\) copies of \(a\), whereas the right half contains all \(j>h\) copies in the third run; this contradicts equal Parikh vectors. If the midpoint lies in the third run, the left half contains all \(i\) copies of \(b\) in the second run, whereas the right half contains at most \(k<i\) copies in the last run. Again the Parikh vectors differ. Thus there is no mixed Abelian square.

**Counting by composition.** For \(x,y>0\), there are exactly two two-run words. A three-run word beginning and ending with \(0\) uses an odd central run of \(1\)'s and can split the \(x\) zeros positively in \(x-1\) ways; this contributes \((x-1)\mathbf 1_{2\nmid y}\). The complementary orientation contributes \((y-1)\mathbf 1_{2\nmid x}\). A four-run word beginning with \(0\) corresponds to positive \(h<j\), odd \(j\), \(h+j=x\), and positive \(k<i\), odd \(i\), \(k+i=y\). The first constraints have exactly \(\lfloor x/4\rfloor\) solutions and the second exactly \(\lfloor y/4\rfloor\) solutions; complementing the letters gives the factor two. Monochromatic words give the boundary cases. Summation proves \(T(x,y)\).

**Generating functions and asymptotics.** The positive composition sums for the respective one-, two-, three-, and four-run cases are precisely the six displayed terms in \(F(u,v)\). Setting \(u=v=z\) gives the one-variable generating function. Near \(z=1\), its final term has leading singular part \(1/[8(1-z)^4]\), and the remaining terms have poles of order at most three at \(z=1\). The other poles of the exact rational function are roots of unity of order at most four and have multiplicity at most two, so their contribution is \(O(n)\). Extracting coefficients of \((1-z)^{-4}\) yields \(t(n)=n^3/48+O(n^2)\), as asserted.

## Verification
Run `python3 verify_trivial_abelian.py` with the Python standard library. It independently enumerates every binary word through length \(16\), explicitly checks all even-length contiguous factors against their Parikh vectors, compares with the structural characterization and weight-refined formula, tests randomized longer words, and compares two exact counting procedures up to length \(500\). A successful run emits `VERIFY_OK`; the captured output is in `VERIFY_OUTPUT.txt`. These finite checks are consistency tests, not a substitute for the proof above.

## Relationship to prior work
Fazekas, Mammoliti, Mercaş and Simpson (2026) study lower bounds on the number of Abelian-square occurrences. In particular, their five-run obstruction and a sufficient construction of *effective* four-run words using a uniquely specified smallest permitted odd interior run supply motivating background; neither ingredient is claimed as new here. For example, a composition with eight occurrences of each letter has four admissible four-run words in each of the two orientations collectively, whereas the canonical effective construction selects only one per orientation. The distinct claim of this result is the necessary-and-sufficient classification of **all** mixed-square-avoiding binary words together with the composition-refined exact count, complete rational generating function and asymptotic. Fici and Saarela's 2014 formulation and Simpson's 2018 survey address minimum Abelian-square occurrence counts and related open questions, not this exact enumeration. Standard enumeration by runs alone does not imply the parity and cross-run inequalities needed here. The formula does not settle any conjecture on the minimum number of trivial Abelian-square occurrences.

## Limitations
Only linear finite words on the two-letter alphabet are counted; circular factors, alphabets of larger size, Abelian powers of exponent greater than two, and counts of all Abelian-square occurrences are outside the claim. The literature check cannot exclude an earlier unindexed equivalent enumeration. No independent scientific audit has been performed.

## References
1. Szilard Zsolt Fazekas, Adam Mammoliti, Robert Mercaş and Jamie Simpson, *Binary Words Containing Few Abelian Squares*, arXiv:2604.23188 (first version publicly posted 2026-04-25).
2. Gabriele Fici and Aleksi Saarela, *On the Minimum Number of Abelian Squares in a Word*, 2014, Dagstuhl seminar proceedings, DOI:10.4230/DagRep.4.3.28.
3. Jamie Simpson, *Solved and Unsolved Problems about Abelian Squares*, arXiv:1802.04481 (2018).
4. Felix Balado and Guénolé C. M. Silvestre, *Systematic Enumeration of Fundamental Quantities Involving Runs in Binary Strings*, arXiv:2602.10005 (2026); general run enumeration rather than the present constrained avoidance count.
