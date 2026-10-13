# Exact worst-case ambiguity of binary two-gram profiles

## Finding

For each integer \(n\ge3\), let \(P(w)=(N_{00}(w),N_{01}(w),N_{10}(w),N_{11}(w))\) be the four counts of consecutive ordered pairs in a *linear* binary word \(w\in\{0,1\}^n\). Define the largest collision fiber
\[
F_n=\max_{p\in\mathbb Z_{\ge0}^4}|\{w\in\{0,1\}^n:P(w)=p\}|.
\]
Writing \(m=n-1\) and \(k=\lceil m/4\rceil\), one has exactly
\[
\boxed{F_n=\frac{m}{k}\binom{\lfloor m/2\rfloor-1}{k-1}\binom{\lceil m/2\rceil-1}{k-1}.}
\]
Moreover all and only maximizing profiles have the following form:
\[
N_{01}=N_{10}=j,\quad j=k\ \text{or, if }m\equiv1\pmod4,\ j=k-1,
\]
with \(N_{00}+N_{11}=m-2j\); when \(j\ge2\) necessarily \(|N_{00}-N_{11}|\le1\), while for \(j=1\) **every** nonnegative split of \(m-2\) is maximizing. In particular there are no maximizing profiles with unequal numbers of \(01\) and \(10\) transitions. As \(n\to\infty\),
\[
F_n\sim\frac{2^{n+1}}{\pi(n-1)},\qquad
\max_p\Pr(P(W)=p)\sim\frac{2}{\pi n},
\]
for a uniformly distributed binary word \(W\) of length \(n\). When \(n=4s+1\) with \(s\ge1\), the exact value simplifies to \(F_n=\binom{2s}{s}^2\).

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\); the input is a noncyclic length-\(n\) word with known fixed length and \(n\ge3\). Multiplicities of all \(n-1\) overlapping adjacent two-grams are counted, so this is not a set-of-two-grams or support-only channel. Both endpoint symbols are unobserved by the recipient. Fibers are counted as labeled words in their original left-to-right order, not modulo reversal, rotation, or bit complementation. All binomial coefficients have ordinary nonnegative integral arguments within the ranges used below.

## Proof

**1. Exact fibers by run compositions.** Write \(a=N_{00}\), \(b=N_{11}\), \(c=N_{01}\), \(d=N_{10}\), so \(a+b+c+d=m\). Traversing the word shows \(|c-d|\le1\). If \(c=d=j\ge1\), either the word starts and ends in zero or it starts and ends in one. In the first case there are \(j+1\) positive zero-runs and \(j\) positive one-runs, with respectively \(a+j+1\) zeros and \(b+j\) ones. Positive compositions give \(\binom{a+j}{j}\binom{b+j-1}{j-1}\) choices. Interchanging the symbols gives the second endpoint case. Their sum is
\[
B_j(a,b)=\binom{a+j}{j}\binom{b+j-1}{j-1}
+\binom{b+j}{j}\binom{a+j-1}{j-1}
=\frac{m}{j}\binom{a+j-1}{j-1}\binom{b+j-1}{j-1},
\]
where \(a+b=m-2j\). If \((c,d)=(j,j-1)\) or \((j-1,j)\), the word starts and ends in opposite symbols and has \(j\) positive runs of each; the fiber count is
\[
U_j(a,b)=\binom{a+j-1}{j-1}\binom{b+j-1}{j-1},
\]
where \(a+b=m-2j+1\) and \(j\ge1\). If \(c=d=0\), the only nonempty fibers are those of the two constant words, each of size one. Any other profile is impossible. These cases exhaust all profiles.

**2. Balance the self-pairs.** At fixed \(j\ge2\), the ratio of consecutive factors is
\[
\frac{\binom{(a+1)+j-1}{j-1}}{\binom{a+j-1}{j-1}}
=\frac{a+j}{a+1},
\]
which strictly decreases with \(a\ge0\). Therefore, for fixed \(a+b\), the product of the two binomial factors is strictly maximized exactly when \(|a-b|\le1\). For \(j=1\), each factor equals one and all splits tie. Thus the best balanced-transition fiber at \(j\) is
\[
B_j^*=\frac{m}{j}\binom{\lfloor m/2\rfloor-1}{j-1}
\binom{\lceil m/2\rceil-1}{j-1},\quad 1\le j\le\lfloor m/2\rfloor.
\]
The best unequal-transition fiber is
\[
U_j^*=\begin{cases}
\binom{r-1}{j-1}\binom r{j-1},&m=2r,\\
\binom r{j-1}^2,&m=2r+1,
\end{cases}\quad 1\le j\le\lfloor(m+1)/2\rfloor.
\]

**3. Optimize the balanced transitions.** Put \(p=\lfloor m/2\rfloor-1\) and \(q=\lceil m/2\rceil-1\). For adjacent allowable indices,
\[
\frac{B_{j+1}^*}{B_j^*}=\frac{(p-j+1)(q-j+1)}{j(j+1)}.
\]
For \(m=2r\) this ratio exceeds one precisely when \(j<r^2/(2r+1)\). As \(r^2/(2r+1)\) lies strictly between \(\lfloor(r-1)/2\rfloor\) and \(\lceil r/2\rceil\), the unique maximum is at \(j=\lceil r/2\rceil=\lceil m/4\rceil\). For \(m=2r+1\), the ratio exceeds one precisely when \(j<r/2\), and equals one at \(j=r/2\) when \(r\) is even. Therefore the maximum is at \(j=k=\lceil m/4\rceil\), with a second maximizing index \(k-1\) precisely when \(m\equiv1\pmod4\). This establishes the displayed formula among balanced-transition profiles.

**4. Exclude all unbalanced transitions.** If \(m=2r\), the binomial formula for \(U_j^*\) increases to its unique maximum at \(j_0=\lfloor r/2\rfloor+1\). For \(r\ge3\),
\[
\frac{B_{j_0}^*}{U_{j_0}^*}=\frac{2(r-j_0+1)}{j_0}>1.
\]
The cases \(r=1\) and \(r=2\) have \(\max_j B_j^*=2,4\), respectively, while \(\max_j U_j^*=1,2\); both are strict. If \(m=2r+1\), the maximum of \(U_j^*=\binom r{j-1}^2\) is attained at \(j_0=\lfloor r/2\rfloor+1\), and also at \(j_0+1\) for odd \(r\). In every case \(r\ge1\),
\[
\frac{B_{j_0}^*}{U_{j_0}^*}=\frac{(2r+1)(r-j_0+1)}{rj_0}>1.
\]
The inequalities follow immediately from \(j_0=\lfloor r/2\rfloor+1\): for \(r=1\) it equals three, and for \(r\ge2\), \((2r+1)(r-j_0+1)>rj_0\). Consequently no unbalanced-transition fiber can maximize. Constant-word fibers have size one, whereas \(F_n\ge m\ge2\). Combining this with steps 2–3 proves the exact formula and *all* equality cases.

**5. Asymptotics.** For \(m=4s\), direct simplification gives \(F_{4s+1}=\binom{2s}{s}^2\). Stirling's formula makes this asymptotic to \(16^s/(\pi s)=4\cdot2^m/(\pi m)\). For the other three residue classes of \(m\) modulo four, the displayed binomials differ from the corresponding central binomial factors by bounded integer shifts; applying the same central binomial asymptotic to each yields \(F_n\sim4\cdot2^m/(\pi m)=2^{n+1}/(\pi(n-1))\). Dividing by \(2^n\) gives the maximum profile probability statement.

## Verification

The standalone programs `verify_bruteforce.py` and `verify_profiles.py` accompany this finding. Run `python3 verify_bruteforce.py` and `python3 verify_profiles.py` from the directory containing these files. The first directly enumerates all \(2^n\) words for every \(3\le n\le18\), checks maximum fiber sizes, *all* maximizing profiles, and totals. The second independently enumerates all nonnegative four-count profiles for \(3\le n\le80\), computes fibers using run-composition counts, checks modal formulas and equality cases, and verifies that fiber sizes sum to \(2^n\). Both completed without error from packaged sources. These finite checks support but do not replace the proof for every \(n\ge3\).

For \(n=3,4,5,6,7,8,9,10\), the exact maxima are \(2,3,4,5,12,21,36,54\), respectively. The numbers of maximizing profiles are \(1,2,3,6,1,2,1,4\) at the same lengths.

## Relationship to prior work

Jacquet, Knessl and Szpankowski (2010) introduce Markov frequency matrices, recall Whittle's fixed-transition class-count formulas, and chiefly enumerate the *number of different Markov types* (in their main results, cyclic strings). That is a different extremal problem from finding the *largest fiber* of the full linear two-gram profile and classifying all fibers attaining it. Kiah, Puleo and Milenkovic (arXiv 2014, revised 2015) study substring-profile equivalence and code design; their full text defines profile vectors and concentrates on the number of equivalence classes and code constructions, not this modal-fiber theorem. Whittle's 1955 paper supplies an exact distribution for observed transition totals, which is relevant background but does not, in its accessible abstract, claim this all-length extremum. The complete original Whittle text could not be inspected, and no claim of verified absence from it is made.

## Limitations

This determines only the largest fiber and its attaining transition profiles for the complete length-two *noncyclic binary* count spectrum; it does not classify all fibers of arbitrary sizes or give a corresponding result for longer grams, larger alphabets, cyclic words, incomplete spectra, or noisy observations. The asymptotic applies along all integer lengths but not to finite-length error bounds. Although highly relevant accessible primary full texts were inspected and semantic searches made, an earlier equivalent maximum-fiber result in unindexed or inaccessible work cannot be ruled out.

## References

1. P. Jacquet, C. Knessl, W. Szpankowski, “Counting Markov Types,” *Discrete Mathematics & Theoretical Computer Science Proceedings*, AofA 2010, 387–400. DOI: 10.46298/dmtcs.2768. Full text: https://dmtcs.episciences.org/2768/pdf.
2. H. M. Kiah, G. J. Puleo, O. Milenkovic, “Codes for DNA Sequence Profiles” (arXiv v2; abstract page titled “Codes for DNA Storage Channels”), arXiv:1410.8837, first submitted October 31, 2014. Full text: https://arxiv.org/pdf/1410.8837.
3. P. Whittle, “Some Distribution and Moment Formulae for the Markov Chain,” *JRSS Series B* 17 (1955), 235–242. DOI: 10.1111/j.2517-6161.1955.tb00197.x; full article not inspected.
