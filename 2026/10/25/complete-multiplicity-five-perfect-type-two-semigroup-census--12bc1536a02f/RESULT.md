# Complete multiplicity-five perfect type-two semigroup census

## Finding
A numerical semigroup is a cofinite additive submonoid \(S\subseteq\mathbb N\) containing zero. A gap \(f\notin S\) is *pseudo-Frobenius* if \(f+s\in S\) for every \(s\in S\setminus\{0\}\). Write \(F(S)\) for the largest gap and \(\operatorname{PF}(S)\) for all pseudo-Frobenius gaps. The condition \(\operatorname{PF}(S)=\{F(S)-1,F(S)\}\) is equivalent to being a perfect numerical semigroup of type two [1,2].

**Theorem (complete multiplicity-five classification).** Every numerical semigroup of multiplicity five with \(\operatorname{PF}(S)=\{F(S)-1,F(S)\}\) belongs to exactly one of the following two families, expressed as Kunz coordinates \((k_1,k_2,k_3,k_4)\):

\[
\begin{array}{ll}
\text{U:}&(c+d+1,c+d+1,c,d),\quad 1\le d\le c\le2d+1,\\[2pt]
\text{V:}&(a,b,a+b,a+b),\quad 1\le a\le b\le2a.
\end{array}
\]

Conversely every such tuple defines a semigroup having precisely these two pseudo-Frobenius gaps. Put \(s=c+d\) in family U and \(s=a+b\) in family V. The genus, Frobenius number and embedding dimension satisfy

\[
\begin{array}{c|cc|c}
 &g(S)&F(S)&\text{embedding dimension}\,e(S)\\\hline
\text{U}&3s+2&5s+2&4\ \text{iff}\ d<c<2d+1,\ \text{else }3\\
\text{V}&3s&5s-1&4\ \text{iff}\ a<b<2a,\ \text{else }3.
\end{array}
\]

For every integer \(s\ge2\), the *total* numbers in the two families at their indicated genus (and Frobenius number) are

\[
U_s=\left\lfloor\frac{s}{2}\right\rfloor-\left\lceil\frac{s-1}{3}\right\rceil+1,
\qquad
V_s=\left\lfloor\frac{s}{2}\right\rfloor-\left\lceil\frac{s}{3}\right\rceil+1.
\]

The numbers of those with embedding dimension four are exactly

\[
U_s^{(4)}=\max\!\left(0,\left\lfloor\frac{s-1}{2}\right\rfloor-\left\lceil\frac{s}{3}\right\rceil+1\right),\qquad
V_s^{(4)}=\max\!\left(0,\left\lfloor\frac{s-1}{2}\right\rfloor-\left\lceil\frac{s+1}{3}\right\rceil+1\right).
\]

No other genera or Frobenius numbers occur in multiplicity five. In particular, if \(N_5(G)\) counts these semigroups with genus at most \(G\), then
\[
N_5(G)=\frac{G^2}{54}+O(G),
\]
with the same leading term for the embedding-dimension-four subfamily. Thus asymptotically almost all multiplicity-five perfect type-two semigroups have embedding dimension four. The two distinct Frobenius congruence classes are \(F\equiv2,4\pmod5\), with the precise lower bounds and counts above.

## Assumptions and scope
The multiplicity is exactly five; all semigroups are submonoids of the nonnegative integers. For \(1\le i\le4\), the Apéry element \(w_i\) is the least member of \(S\) congruent to \(i\pmod5\), and \(w_i=5k_i+i\). Thus each \(k_i\) is a positive integer; the genus is \(\sum_{i=1}^4k_i\). The classification is unlabelled: a numerical semigroup is identified with its underlying set of integers, and distinct tuples represent distinct semigroups. The assertion includes all admissible parameter values and has no implicit upper bound.

## Proof
**1. Kunz criterion and the Apéry order.** A positive integral quadruple is the Kunz vector of a multiplicity-five semigroup if and only if
\[
\begin{gathered}
k_2\le2k_1,\quad k_3\le k_1+k_2,\quad k_4\le k_1+k_3,\quad k_4\le2k_2,\\
k_1\le k_2+k_4+1,\quad k_1\le2k_3+1,\quad k_2\le k_3+k_4+1,\quad k_3\le2k_4+1.
\end{gathered}
\]
This follows by requiring \(w_{i+j\bmod5}\le w_i+w_j\), for nonzero residues \(i+j\bmod5\); these conditions are also sufficient for closure of the corresponding residue rays. The pseudo-Frobenius elements are precisely the \(w_i-5\) for maximal \(w_i\) in the Apéry order \(u\preceq v\iff v-u\in S\). For a nonmaximal \(w_i\), one has some exact equality \(w_t=w_i+w_j\) with \(j,t\in\{1,2,3,4\}\): if \(w_t-w_i\) lies in residue \(j\) and in \(S\), it is at least \(w_j\), while minimality of \(w_t\) makes it at most \(w_j\). The only possible nonmaximality equalities, listed by index, are
\[
\begin{array}{c|l}
 i&\text{possible equalities}\ \\ \hline
1&k_2=2k_1,\ k_3=k_1+k_2,\ k_4=k_1+k_3\\
2&k_3=k_1+k_2,\ k_4=2k_2,\ k_1=k_2+k_4+1\\
3&k_4=k_1+k_3,\ k_1=2k_3+1,\ k_2=k_3+k_4+1\\
4&k_1=k_2+k_4+1,\ k_2=k_3+k_4+1,\ k_3=2k_4+1.
\end{array}
\]

**2. Exhaust the consecutive maximal pairs.** Since none of \(w_i-5\) is divisible by five and the two maxima differ by one, their residue indices must be \((1,2)\), \((2,3)\) or \((3,4)\), with the indicated equal Kunz coordinates.

For indices \((2,3)\), put \(k_2=k_3=b\). Both indices \(1,4\) must be nonmaximal. The table forces for index \(1\) either \(b=2k_1\) or \(k_4=k_1+b\); for index \(4\) it forces either \(k_1=b+k_4+1\) or \(b=2k_4+1\). Combining any of these alternatives is impossible: \(b=2k_1\) contradicts the first option for index \(4\) by positivity and the second by parity; \(k_4=k_1+b\) contradicts the first by positivity and the second by size. Thus this pair never occurs.

For indices \((1,2)\), set \(k_1=k_2=A\), write \(k_3=c,k_4=d\). Nonmaximality of index \(4\) gives \(A=c+d+1\) or \(c=2d+1\); the remaining table option is impossible. If \(A\ne c+d+1\), nonmaximality of index \(3\) forces \(A=2c+1\) or \(d=A+c\). The latter contradicts positivity together with \(c=2d+1\); the former gives \(A=4d+3\), contradicting the Kunz inequality \(A\le c+d+1=3d+2\). Hence \(A=c+d+1\). Substitution into all eight Kunz inequalities leaves exactly \(1\le d\le c\le2d+1\). In this cone \(w_2=w_3+w_4\), so indices \(3,4\) are not maximal, while \(w_1,w_2\) are the two largest Apéry elements and therefore both maximal.

For indices \((3,4)\), set \(k_3=k_4=C\), write \(k_1=a,k_2=b\). Nonmaximality of index \(1\) gives \(b=2a\) or \(C=a+b\); nonmaximality of index \(2\) gives \(C=a+b\), \(C=2b\), or \(a=b+C+1\). If \(C\ne a+b\), the equality \(b=2a\) is forced. It cannot be combined with \(C=2b=4a\), because \(C\le a+b=3a\), nor with \(a=b+C+1\). Thus \(C=a+b\), and the Kunz inequalities reduce to \(1\le a\le b\le2a\). Here \(w_3=w_1+w_2\), so indices \(1,2\) are nonmaximal, and \(w_3,w_4\) are both maximal. This proves both directions and their disjointness.

**3. Invariants and counts.** The Apéry gap formula gives \(g=\sum k_i\) and \(F=\max_i(w_i-5)\), yielding the displayed genus and Frobenius formulas. The only composite nonzero Apéry elements in U are \(w_2=w_3+w_4\), additionally \(w_1=2w_3\) exactly at \(c=d\), and additionally \(w_3=2w_4\) exactly at \(c=2d+1\). In V they are \(w_3=w_1+w_2\), additionally \(w_4=2w_2\) exactly at \(a=b\), and additionally \(w_2=2w_1\) exactly at \(b=2a\). Since the multiplicity itself is always a generator, this proves the stated embedding dimensions.

In U, fixing \(s\) means \(c=s-d\), and the admissible integers satisfy \(\lceil(s-1)/3\rceil\le d\le\lfloor s/2\rfloor\); imposing strict inequalities instead gives \(\lceil s/3\rceil\le d\le\lfloor(s-1)/2\rfloor\). In V, fixing \(s\) means \(b=s-a\), with \(\lceil s/3\rceil\le a\le\lfloor s/2\rfloor\), and strict inequalities give \(\lceil(s+1)/3\rceil\le a\le\lfloor(s-1)/2\rfloor\). Counting the integers in these intervals proves all four formulas. Each family has \(s/6+O(1)\) members at its \(s\)-level, while boundary members with embedding dimension three contribute only \(O(1)\) per level. Summation over \(s\le G/3+O(1)\) proves \(N_5(G)=G^2/54+O(G)\) and asymptotic dominance of embedding dimension four.

## Verification
The standalone, standard-library-only program `verify.py` independently constructs each represented semigroup by additive closure of its Apéry generators. It computes gaps, pseudo-Frobenius elements, genus, Frobenius number and minimal generators from membership, then compares the results with the classification and exact formulas. All valid positive Kunz quadruples of genus at most 60 were checked (32,065 candidates satisfying the Kunz inequalities; 88 perfect type-two examples, of which 57 have embedding dimension four). For each integer \(2\le s\le1000\), it also independently enumerates the admissible intervals and agrees with all four closed counting formulas. Run `python3 verify.py` in the directory containing the file; expected terminal marker: `VERIFY_OK`. The finite sweep is supplementary, not a proof of the unbounded classification.

## Relationship to prior work
Moreno-Frías and Rosales [1] characterized perfect semigroups of type two through consecutive pseudo-Frobenius numbers and presented algorithms at fixed Frobenius number; they did not supply a uniform multiplicity-five two-cone classification or the exact infinite genus census. Their earlier embedding-dimension-three theorem [2, Theorem 17] covers the boundary families where one inequality is an equality: that pre-existing coverage is not claimed as new. The interior embedding-dimension-four cones are not covered by its hypothesis, and they contribute the quadratic leading term. General fixed-Frobenius and fixed-multiplicity enumeration algorithms [3,4] can enumerate bounded instances but do not state these closed parameter cones and formulas. The present result derives and proves them uniformly, without relying on algorithm output as an infinite proof.

## Limitations
No assertion is made for other multiplicities, or for semigroups of type greater than two. The embedding-dimension-three boundary cases intersect known general structure [2]; originality pertains to the full uniform multiplicity-five classification, particularly the unbounded embedding-dimension-four interior and exact counts. A mathematically equivalent classification outside the inspected literature remains possible. The 2019 publisher download was inaccessible, so its abstract and stated algorithmic scope were used, not an asserted complete-text exclusion. No independent mathematical audit has been performed.

## References
1. M. A. Moreno-Frías and J. C. Rosales, "Perfect numerical semigroups of type two," *Congressus Numerantium* 237 (2026), 99–112, DOI: 10.61091/cn237-07. Public online date: 2026-06-17. https://combinatorialpress.com/cn-articles/volume-237/perfect-numerical-semigroups-of-type-two/
2. M. A. Moreno-Frías and J. C. Rosales, "Perfect numerical semigroups with embedding dimension three," *Publicationes Mathematicae Debrecen* 97 (2020), 77–84, DOI: 10.5486/PMD.2020.8699. https://rodin.uca.es/bitstream/10498/24618/1/SC_2020_402.pdf
3. M. A. Moreno-Frías and J. C. Rosales, "The covariety of perfect numerical semigroups with fixed Frobenius number," *Czechoslovak Mathematical Journal* 74 (2024), 697–714, arXiv:2305.14967. https://arxiv.org/abs/2305.14967
4. M. A. Moreno-Frías and J. C. Rosales, "Perfect numerical semigroups," *Turkish Journal of Mathematics* 43 (2019), 1742–1754, DOI: 10.3906/mat-1901-111. https://journals.tubitak.gov.tr/math/vol43/iss3/47/
