# Sharp worst-case inverse multiplicity for binary cyclic pair profiles

## Finding

For every integer \(n\ge1\), an **indexed binary circle** is a word \(w=(w_0,\ldots,w_{n-1})\in\{0,1\}^n\), with indices modulo \(n\); different indexed tuples are different even if one is a rotation of the other. Its cyclic pair-profile is the full matrix
\[
M(w)=(m_{ij}(w))_{i,j\in\{0,1\}},\qquad
m_{ij}(w)=|\{r\in\{0,\ldots,n-1\}:(w_r,w_{r+1})=(i,j)\}|.
\]
Let \(H_n=\max_M |\{w:M(w)=M\}|\), where the maximum is over realized matrices. Thus \(H_n\) is the largest inverse list of the exact, noiseless cyclic two-gram observation.

**Exact theorem.** For integers \(k\ge1\),
\[
\begin{array}{ll}
H_{4k}=\binom{2k}{k}^2,&
H_{4k+1}=\dfrac{4k+1}{k}\binom{2k-1}{k-1}\binom{2k}{k-1},\\[7pt]
H_{4k+2}=\dfrac{4k+2}{k+1}\binom{2k}{k}^2,&
H_{4k+3}=\dfrac{4k+3}{k+1}\binom{2k}{k}\binom{2k+1}{k}.
\end{array}
\]
The remaining initial cases are \(H_1=1\), \(H_2=2\), and \(H_3=3\); the displayed formula for \(H_{4k+1}\) also holds for \(k=1\). For \(n\ge6\) **all** maximizing profiles are given by the following table. Here \(z\) and \(o\) are the zero and one counts, and \(t=m_{01}=m_{10}\) is the number of zero-to-one changes; \(m_{00}=z-t\) and \(m_{11}=o-t\).

| \(n\) | maximizing \((z,o,t)\) | number of profiles |
|---|---|---:|
| \(4k\), \(k\ge2\) | \((2k,2k,k)\) | 1 |
| \(4k+1\), \(k\ge2\) | \((2k,2k+1,k)\), \((2k,2k+1,k+1)\) and both symbol swaps | 4 |
| \(4k+2\), \(k\ge1\) | \((2k+1,2k+1,k+1)\) | 1 |
| \(4k+3\), \(k\ge1\) | \((2k+1,2k+2,k+1)\) and its swap | 2 |

For \(n=1\), both constant profiles maximize; for \(n=2\), the sole mixed profile maximizes; for \(n=3\), the two mixed profiles maximize; for \(n=4\), all three profiles with \(t=1\) maximize; and for \(n=5\), the four \(t=1\) mixed profiles together with the two centered \(t=2\) profiles maximize. In particular, the odd case \(n\equiv1\pmod4\) has a genuine transition-count tie starting at \(n=9\).

The sharp asymptotic multiplicity is
\[
\frac{H_n}{2^n}=\frac{4}{\pi n}\left(1+O(n^{-1})\right),\qquad n\longrightarrow\infty.
\]
Consequently the worst inverse list has asymptotic size \(4\cdot2^n/(\pi n)\), not merely a logarithmic-order estimate. This theorem concerns *indexed* words, not rotation-equivalence classes.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), the observation includes the wraparound pair \((w_{n-1},w_0)\), and all \(2^n\) indexed words are counted with equal multiplicity. No stochastic independence of adjacent observations, primitive-period assumption, decoding errors, or transition constraints are imposed. The binary labels are distinct, so swapping zero and one generally produces another matrix.

## Proof

### 1. Exact inverse-fiber formula

Every nonconstant circle contains a positive number \(t\) of transitions \(01\) and the same number of transitions \(10\), by cyclic balance. If it has \(z\) zeros and \(o=n-z\) ones, necessarily \(1\le t\le\min(z,o)\) and its matrix is
\[
M=\begin{pmatrix}z-t&t\\t&o-t\end{pmatrix}.
\]
There are exactly \(t\) nonempty zero runs and exactly \(t\) nonempty one runs, alternating on the circle. Counting pairs \((w,r)\) where \(r\) is a distinguished indexed position of a transition \(01\), first choose its position (\(n\) choices), then the ordered positive compositions of \(o\) and \(z\) into \(t\) parts. Each indexed circle has exactly \(t\) distinguished positions. Therefore its fiber cardinality is **exactly**
\[
B_n(z,t)=\frac{n}{t}\binom{z-1}{t-1}\binom{n-z-1}{t-1}.
\tag{1}
\]
The two constant profiles each have fiber size \(1\). Formula (1) holds for periodic circles too, since the marked *indexed positions*, rather than distinct rotations, are counted.

### 2. Concentration of the symbol counts

For fixed \(t\ge2\), the ratio of successive positive binomial products in (1) is
\[
\frac{B_n(z+1,t)}{B_n(z,t)}
=\frac{z(n-z-t)}{(z-t+1)(n-z-1)}.
\]
Clearing the positive denominator, the difference between numerator and denominator is
\[
(t-1)(n-2z-1).
\tag{2}
\]
Thus the product strictly increases until the middle of the allowed \(z\)-interval and strictly decreases after it. For even \(n\), only \(z=o=n/2\) maximizes at each \(t\ge2\); for odd \(n\), the two counts \((\lfloor n/2\rfloor,\lceil n/2\rceil)\) and their swap are the only maximizers.

For \(t=1\), formula (1) is identically \(n\), independently of \(z\). For every \(n\ge6\), the centered choice with \(t=2\) has size \(\frac n2(z-1)(o-1)>n\). Hence a global maximizing nonconstant profile has \(t\ge2\) for all \(n\ge6\), and (2) forces centered symbol counts. Constant profiles cannot maximize, since their size is one.

### 3. Exact transition optimum and all ties

With centered \(z,o\) fixed, equation (1) yields
\[
\frac{B_n(z,t+1)}{B_n(z,t)}
=\frac{(z-t)(o-t)}{t(t+1)}.
\tag{3}
\]
This is greater than, equal to, or less than one according as \(zo\) is greater than, equal to, or less than \(t(n+1)\). In particular, it changes direction only once. For the four residue classes of \(n\) modulo four, direct division of the centered product \(zo\) by \(n+1\) gives, respectively,
\[
\begin{array}{c|c}
n&zo/(n+1)\\\hline
4k&k-\dfrac{k}{4k+1}\\[4pt]
4k+1&k\\[4pt]
4k+2&k+\dfrac{k+1}{4k+3}\\[4pt]
4k+3&k+\dfrac12.
\end{array}
\]
Thus the optimal integer transition counts are \(k\), \(k\) or \(k+1\) in a tie, \(k+1\), and \(k+1\), respectively. Substitution in (1) gives each closed formula in the statement. The strictness in (2) and (3) gives every asserted maximizer, with the special short-length cases obtained by evaluating (1) at \(n=1,\ldots,5\).

### 4. Asymptotics

By Stirling's formula, \(\binom{2k}{k}=4^k(\pi k)^{-1/2}(1+O(k^{-1}))\). Each of the four exact expressions for \(H_n\) reduces, with its corresponding \(n=4k+r\), to \(2^n\,4/(\pi n)\,(1+O(n^{-1}))\). This proves the asymptotic uniformly across the four residue classes.

## Verification

The exact proof above is valid at all \(n\), without computational assumptions. The package also contains `verify.py` and `crosscheck.cpp`. The first checks the closed form and maximizing parameter sets against an exhaustive integer parameter search for \(1\le n\le200\), then independently counts all indexed binary words for \(1\le n\le19\) and compares every fiber with (1). The C++17 program independently enumerates words and full four-entry pair matrices for \(1\le n\le20\), checking each claimed maximum and the complete maximizing-matrix set. Reproduction: `python3 verify.py`; then `c++ -O2 -std=c++17 crosscheck.cpp -o crosscheck && ./crosscheck`. No network, third-party dependencies, or external data are needed.

Selected maxima are \(H_6=12\), \(H_8=36\), \(H_9=54\), \(H_{12}=400\), \(H_{16}=4900\), and \(H_{20}=63504\).

## Relationship to prior work

Jacquet, Knessl and Szpankowski's *Counting Markov Types* (publicly dated 2009-12-31; proceedings edition 2010) treats these cyclic balanced matrices and determines the **number of types** via generating functions and asymptotics. Its introductory binary example counts balanced matrices; its main theorem is about the number of types, not the largest inverse fiber. The present theorem instead maximizes a fiber cardinality and classifies all equality cases, including short-length and residue-class ties.

Whittle's classical 1955 transition-count formula, cited in the preceding work, and related run-composition methods provide general fixed-profile cardinality tools. The closed-form inverse fiber formula (1) is not asserted as a new technique. The claimed additional result is the globally sharp binary cyclic inverse multiplicity, its complete equality classification, and the explicit leading asymptotic constant. Makri, Psillakis and Arapis (2013) count circular run statistics under a different one-run observation, not the four-entry cyclic pair-profile maximization here. Accessible related records on **linear** binary adjacent-pair multispectra count output classes and singleton classes, not this circular worst-fiber extremum.

## Limitations

The result assumes a binary alphabet, exact cyclic pair observations, and indexed input words. Neither individual rotation-necklace fiber sizes nor larger alphabets or longer windows are classified. It does not give a noisy-channel coding bound. Known general Markov type cardinality machinery may permit an independent derivation of equation (1), and the existence of unindexed prior explicit optimizations remains an historical-priority risk. Self-review is not independent validation.

## References

1. Philippe Jacquet, Charles Knessl, and Wojciech Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (2010), pp. 387–400, DOI: `10.46298/dmtcs.2768`, full text: https://dmtcs.episciences.org/en/articles/2768/download . Publisher's earliest exact publicly dated record: 2009-12-31.
2. Peter Whittle, *Some Distribution and Moment Formulae for the Markov Chain*, Journal of the Royal Statistical Society Series B 17 (1955), 235–242, DOI: `10.1111/j.2517-6161.1955.tb00197.x`.
3. Frosso Makri, Zaharias Psillakis, and Anastasios Arapis, *Counting Runs of Ones with Overlapping Parts in Binary Strings Ordered Linearly and Circularly*, International Journal of Statistics and Probability 2 (2013), DOI: `10.5539/ijsp.v2n3p50`, publicly dated 2013-07-09, https://ccsenet.org/journal/index.php/ijsp/article/view/28864 .
