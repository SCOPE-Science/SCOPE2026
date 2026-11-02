# Exact cyclic binary three-window composition spectra and a cubic period-three capacity law

## Finding

For every integer \(n\ge3\), let \(w\in\{0,1\}^n\) be an indexed binary circular word, with positions read modulo \(n\). For \(j\in\{0,1,2,3\}\), define \(c_j(w)\) as the number of starting positions \(i\in\{0,\ldots,n-1\}\) for which the length-three cyclic window \((w_i,w_{i+1},w_{i+2})\) contains exactly \(j\) ones. The receiver observes only the four multiplicities \((c_0,c_1,c_2,c_3)\), not the order or location of the windows.

**Complete realizability theorem.** A nonnegative integer tuple \((c_0,c_1,c_2,c_3)\) with sum \(n\) is realizable precisely when either it is one of the constant tuples \((n,0,0,0)\) and \((0,0,0,n)\), or all four conditions hold:

\[
 c_1+c_2>0,\qquad c_1\equiv c_2\pmod 3,\qquad
 c_0>0\Longrightarrow c_1\ge2,\qquad
 c_3>0\Longrightarrow c_2\ge2.
\]

**Exact capacity.** Let \(P_n\) denote the number of realizable tuples, equivalently the maximum size of a subset of \(\{0,1\}^n\) on which this observation is injective. For every \(n\ge3\),

\[
 P_n=\begin{cases}
 (n^3-6n^2+39n-18)/18,&n\equiv0\pmod3,\\
 (n-1)(n^2-5n+34)/18,&n\equiv1\pmod3,\\
 (n^3-6n^2+39n-26)/18,&n\equiv2\pmod3.
 \end{cases}
\]

The generating function starting at length three is

\[
 \sum_{n\ge3}P_nz^n=
 \frac{2z^3}{1-z}+
 \frac{2(z^3+z^5)}{(1-z)(1-z^3)}+
 \frac{z^4+z^6+z^8}{(1-z)^2(1-z^3)^2}.
\]

In particular, \(P_n=n^3/18+O(n^2)\). The exact cubic growth is a capacity statement about *composition-only* cyclic triple reads, not about fully oriented ternary or binary trigram frequencies.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). Each of the \(n\) cyclic windows contributes once, including windows that cross the chosen boundary. Repeated windows are counted with multiplicity. The channel reports the number of ones in each window but loses the window order, orientation and phase; rotation does not change the observation. The theorem covers indexed words with \(n\ge3\); it does not assert unique recovery of an arbitrary word from its profile.

## Proof

First consider a nonconstant circular binary word. There are exactly \(t\ge1\) cyclic zero-runs and \(t\) cyclic one-runs. Let \(u_0\) and \(u_1\) be their respective numbers of length-one runs, and let \(N_0\) and \(N_1\) be the two symbol totals. Every zero-run of length \(a\) contributes \(\max\{a-2,0\}\) all-zero triple windows, and similarly for all-one runs. Therefore

\[
 c_0=N_0-2t+u_0,\qquad c_3=N_1-2t+u_1.
\]

Each position belongs to exactly three cyclic windows, so

\[
 \sum_{j=0}^{3}c_j=n,\qquad \sum_{j=0}^{3}j c_j=3N_1.
\]

Eliminating \(N_0,N_1\) gives

\[
 c_1=2t-2u_0+u_1,\qquad c_2=2t+u_0-2u_1.
\]

Set \(A=2t-u_0\) and \(B=2t-u_1\). The last equations become \(c_1=2A-B\), \(c_2=2B-A\), hence

\[
 A=\frac{2c_1+c_2}{3},\qquad
 B=\frac{c_1+2c_2}{3}.
\]

Thus \(c_1\equiv c_2\pmod3\). Because \(0\le u_0,u_1\le t\), necessarily \(\lceil\max(A,B)/2\rceil\le t\le\min(A,B)\). Furthermore, \(c_0>0\) requires a zero-run of length at least three and therefore \(u_0<t\), equivalently \(t<A\); similarly \(c_3>0\) requires \(t<B\). These conditions imply \(c_0>0\Rightarrow c_1\ge2\) and \(c_3>0\Rightarrow c_2\ge2\). The constant words give the two separately listed profiles. Necessity follows.

For sufficiency, take a nonconstant tuple satisfying the four conditions and put

\[
 A=(2c_1+c_2)/3,\quad B=(c_1+2c_2)/3,\quad
 t=\left\lceil\max(A,B)/2\right\rceil.
\]

The congruence and positivity give positive integers \(A,B\). Since \(c_1=2A-B\ge0\) and \(c_2=2B-A\ge0\), \(t\le\min(A,B)\). If \(c_0>0\), the requirement \(c_1\ge2\) strengthens this to \(t\le A-1\); if \(c_3>0\), \(c_2\ge2\) strengthens it to \(t\le B-1\). Hence \(u_0=2t-A\) and \(u_1=2t-B\) are integers between zero and \(t\), and \(c_0>0\Rightarrow u_0<t\), \(c_3>0\Rightarrow u_1<t\).

Construct \(t\) zero-run lengths by taking \(u_0\) copies of one and \(t-u_0\) copies of two, then adding the remaining \(c_0\) zeros to any length-two run whenever \(c_0>0\). Construct \(t\) one-run lengths analogously from \(u_1,c_3\). Alternate these zero- and one-runs around the circle. The resulting word has length

\[
 (2t-u_0+c_0)+(2t-u_1+c_3)=A+B+c_0+c_3=n,
\]

and its four window counts are exactly the prescribed tuple by the preceding identities. This proves sufficiency constructively.

To count profiles, for \(c_1+c_2>0\) the congruence reduces to \(c_1\equiv c_2\pmod3\). If both are at least two, their exponent-generating function is \((z^4+z^6+z^8)/(1-z^3)^2\). For fixed \(c_1,c_2\), the remaining \(R=n-c_1-c_2\) is distributed arbitrarily between \(c_0,c_3\) in \(R+1\) ways, giving the factor \((1-z)^{-2}\). If precisely one of \(c_1,c_2\) is smaller than two, it equals zero or one, and the larger count respectively begins at three or four. These boundary pairs contribute \(2(z^3+z^5)/(1-z^3)\); the corresponding \(c_0,c_3\) split is forced and contributes \((1-z)^{-1}\). The all-constant profiles contribute \(2z^3/(1-z)\). Summing proves the displayed generating function. Its partial fractions or direct coefficient extraction yield the stated three residue-class formulas. Finally, any zero-error code contains at most one word for each profile, and the constructive sufficiency proof supplies one representative for every profile, proving exact optimality.

## Verification

The standalone file `verify.py` computes each cyclic window histogram directly, compares the entire predicted profile set to brute-force enumeration of all \(2^n\) indexed binary words for every \(3\le n\le18\), compares the profile count to the stated cubic residue-class formula, and independently constructs and checks one realizing word for every predicted profile through length \(45\). Its expected success lines are `EXHAUSTIVE_OK lengths=3..18 words= 524280` and `CONSTRUCTIONS_OK n=3..45 profiles= 51223`. These finite checks support the proof but are not substitutes for its all-length run argument.

## Relationship to prior work

Gabrys and Milenkovic (2018) study reconstruction from the full ordered substring multispectrum. Gupta and Mahdavifar (2022) analyze reconstruction from compositions of *all* linear substrings. Ye and Elishco (2022) develop partial composition readouts, including length-limited *linear* substrings. The present observation uses *only cyclic length-three composition multiplicities* and computes the complete image and exact maximum zero-error code size of that deliberately coarsened channel. Previous analyses of the fully oriented cyclic three-gram profile address a strictly finer measurement; their numerical profile counts do not determine the image cardinality after collapsing windows by composition. The result should not be read as claiming novelty for the trivial mod-three conservation identity alone.

## Limitations

The theorem is binary and concerns error-free full cyclic coverage with length-three windows. It does not determine decoding fiber sizes, noisy or partial observation performance, or capacities at longer window lengths. As in any literature comparison, undiscovered equivalent formulations remain possible; the result has not received independent scientific validation.

## References

- R. Gabrys and O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, 2018 public preprint, https://arxiv.org/abs/1804.04548 .
- U. Gupta and H. Mahdavifar, *A New Algebraic Approach for String Reconstruction from Substring Compositions*, 2022 public preprint, https://arxiv.org/abs/2201.09955 .
- Z. Ye and O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, 2022 public preprint, https://arxiv.org/abs/2208.14963 .
