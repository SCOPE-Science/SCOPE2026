# Sharp two-orbit threshold for coprime two-gap shifts

## Finding

Let \(2\le a<b\) be coprime integers. In the two-sided binary shift \(X_{a,b}\), successive occurrences of the symbol \(1\) are separated by exactly \(a-1\) or \(b-1\) zeros. Let \(Q_n(a,b)\) be the number of distinct shift-orbits whose **least** period equals \(n\), counting each orbit once rather than each periodic point separately. Put

\[
M(a,b)=\max\{(a+1)b,\,2(a+b)\}.
\]

Then the **last period carrying fewer than two distinct primitive orbits** is exactly \(M(a,b)\):

\[
\boxed{Q_{M(a,b)}(a,b)=1,\qquad Q_n(a,b)\ge2\quad\text{for every integer }n>M(a,b).}
\]

Thus \(M(2,3)=10\), while \(M(a,b)=(a+1)b\) for every other coprime pair \(2\le a<b\). The qualification “last” is essential: below this cutoff, periods with one orbit and periods with two or more orbits may be interlaced; the theorem does not assert monotonicity of \(Q_n\).

For completeness, the exact primitive-orbit count has the known necklace form

\[
Q_n(a,b)=\mathbf 1_{\{n=a\}}+\mathbf 1_{\{n=b\}}+
\sum_{\substack{r,s\ge1\\ar+bs=n}}
\frac1{r+s}\sum_{d\mid\gcd(r,s)}\mu(d)
\binom{(r+s)/d}{r/d}.
\]

Here \(\mu\) is the number-theoretic Möbius function. The enumeration identity is a standard consequence of primitive-necklace enumeration and of the previously known zeta function; it is **not** claimed as the new contribution. The sharp universal cutoff, with its exceptional pair, is the finding.

## Assumptions and scope

All assertions quantify over arbitrary integers \(a,b\) satisfying \(2\le a<b\) and \(\gcd(a,b)=1\), and over all positive integer periods \(n\). The phase space comprises bi-infinite binary sequences with exactly \(a-1\) or \(b-1\) zeros between each successive pair of ones; because the permitted set of gaps is finite, sequences containing only finitely many ones are excluded. The shift acts by translating the sequence one position. Since both gap lengths are at least one, no adjacent ones occur. No claim of a finite cutoff for **all integer periods** is made if the two block lengths are not coprime: then every primitive period is divisible by their common divisor.

Write \(A=10^{a-1}\) and \(B=10^{b-1}\) for the two admissible return blocks, regarded as two distinct letters when discussing gap patterns. These symbols are return blocks, not a claim that the physical shift acts once per block. A gap pattern containing \(r\) copies of \(A\) and \(s\) copies of \(B\) has physical length \(ar+bs\).

## Proof

**1. Cyclic gap coding and primitivity.** Every periodic binary sequence in the shift contains at least one \(1\). Choosing successive positions of \(1\) turns it into a cyclic word over \(\{A,B\}\). Moving the origin to another occurrence of \(1\) cyclically rotates that word; conversely, any cyclic word of return blocks defines a periodic binary sequence. As \(a\ne b\), the gap lengths recover the return letters uniquely. A physical periodic sequence has least period \(n\) precisely when its length-\(n\) cyclic return-block word is primitive: any smaller physical period preserves the set of \(1\)-positions and thus induces a nontrivial repeated cyclic return word, and conversely. Therefore primitive binary necklaces of content \((r,s)\), where \(ar+bs=n\), correspond bijectively to distinct physical least-period-\(n\) orbits. A word entirely of one letter supplies only the orbits of periods \(a\) and \(b\). Möbius inversion on the repetition divisor yields the displayed necklace formula.

**2. A lemma providing two primitive necklaces.** For every \(r,s\ge1\), the cyclic word \(A^rB^s\) is primitive: its cyclic order has precisely two transitions between letter types. If \(r,s\ge2\) and \((r,s)\ne(2,2)\), the cyclic word

\[
A^{r-1} B A B^{s-1}
\]

is also primitive and is not a rotation of \(A^rB^s\), since it has exactly four transitions. Indeed, if a four-transition cyclic word were a proper power, the power would have to be a square of a two-transition word. For the above four-run pattern, this would force both \(A\)-run lengths \(r-1,1\) and both \(B\)-run lengths \(1,s-1\) to agree, hence \(r=s=2\), which was excluded. Thus \(r,s\ge2\) and \((r,s)\ne(2,2)\) produce at least two distinct primitive orbits with the same physical length \(ar+bs\).

**3. Every larger integer has at least two primitive orbits.** Set \(M=M(a,b)\) and fix an arbitrary integer \(n>M\). Coprimality gives a unique integer \(r_0\in\{1,\ldots,b\}\) satisfying \(ar_0\equiv n\pmod b\). Define the integer \(s_0=(n-ar_0)/b\). Since

\[
n>M\ge(a+1)b=ab+b\qquad\text{and}\qquad ar_0\le ab,
\]

we have \(s_0\ge2\). There are two cases.

If \(s_0\ge a+1\), then both positive integer solutions

\[
(r,s)=(r_0,s_0)\qquad\text{and}\qquad(r,s)=(r_0+b,s_0-a)
\]

satisfy \(ar+bs=n\). Each yields the primitive cyclic block word \(A^rB^s\); their different numbers of \(A\)-blocks ensure distinct orbits.

If \(2\le s_0\le a\), then \(r_0\ne1\), for otherwise \(n=a+bs_0\le a+ab<ab+b<M+1\). Thus \(r_0\ge2\). Since \(n>2(a+b)\), the pair \((r_0,s_0)\) is not \((2,2)\), and the lemma in step 2 supplies two primitive orbits of period \(n\). This proves \(Q_n\ge2\) for every \(n>M\).

**4. Sharp endpoint.** First suppose \(M=(a+1)b\ge2(a+b)\). Every nonnegative solution of \(ar+bs=M\) has either \((r,s)=(b,1)\) or \((r,s)=(0,a+1)\): from \(ar\equiv0\pmod b\), coprimality forces \(b\mid r\), while \(0\le r\le M/a<2b\) under \(b>a\). The pure \(B\)-word is a repetition of an orbit with smaller least period, whereas \(A^bB\) is primitive and unique up to cyclic rotation because it contains exactly one \(B\). Therefore \(Q_M=1\). If \(2(a+b)>b(a+1)\), the identity \((a-1)(b-2)<2\) and \(2\le a<b\) force \((a,b)=(2,3)\). Here \(M=10\), and the only nonnegative block solutions are \((r,s)=(2,2)\) and \((5,0)\). The latter is nonprimitive; among the former, \(AABB\) is the unique primitive necklace, while \(ABAB\) is a square. Hence \(Q_{10}(2,3)=1\). This establishes sharpness in both cases.

## Verification

The self-contained standard-library program `verification/verify.py` implements three distinct finite checks. First it counts primitive binary return-block necklaces using Möbius inversion. Second it independently derives least-period orbit counts from the established dynamical zeta identity

\[
\zeta_{X_{a,b}}(t)=\frac1{1-t^a-t^b},
\]

via the coefficient recurrence for its logarithmic derivative, then checks both counts agree. Third it independently exhausts cyclic binary sequences at small periods, tests the original gap constraint and primitive least period directly, and compares orbit counts.

Running `python3 verification/verify.py` completed successfully: **18,094 exact comparisons** between the necklace and zeta formulations; **6,120 finite sharp-threshold checks** over coprime pairs; and **192 independent cyclic-word enumerations**. For \((a,b)=(2,3),(3,5),(4,7),(5,8)\), the resulting sharp endpoint periods are respectively \(10,20,35,48\), each with exactly one primitive orbit, and their immediate successors have \(2,2,2,7\) orbits. These finite diagnostics do not replace steps 1–4, which prove the all-parameter conclusion.

## Relationship to prior work

De Jong, *On sets of periodic orbit lengths in finitely presented dynamical systems*, Theorem 3.19, identifies the **support** of the least-period spectrum of any finite-gap shift via almost sum-closure; its Section 1 also explains the role of periodic-point counts in Krieger's embedding theorem. Knowing that at least one orbit of a given length exists does not determine whether at least two exist. The theorem above determines the exact last multiplicity-one-or-zero obstruction for a canonical mixing two-gap family.

Dastjerdi and Jangjoo established the dynamical zeta function \(\zeta(t)=1/(1-\sum_{j\in S}t^{j+1})\) for finite \(S\)-gap shifts in *Computations on sofic S-gap shifts* (Corollary 2.3). Combining that zeta function with general Möbius inversion already determines the full sequence of periodic-orbit counts in principle. The present claim of new content is **only** the closed-form, optimal parameter-uniform last-singleton cutoff; it is not a newly discovered zeta function or necklace formula. Doering and Pavlov classify realizable sets of period lengths for SFTs rather than this sharp two-orbit threshold.

## Limitations

The result is restricted to exactly two admissible return lengths, which must be distinct and coprime, with minimum length at least two. It does not classify all exceptional smaller periods, all multiplicity values, or shifts with more than two admissible gaps. No consequence asserting a particular embedding is proved; Krieger's theorem motivates why distinguishing one from two orbits is natural, but full embedding conditions involve the complete count sequence and entropy. Known zeta-function and necklace enumeration tools are credited, and earlier equivalent formulations of the **sharp cutoff** in renewal-system, run-length-limited coding or necklace literature remain a bibliographic-priority risk.

## References

1. Huub de Jong, *On Sets of Periodic Orbit Lengths in Finitely Presented Dynamical Systems*, arXiv:2510.10848v1 (first posted 2025-10-12), Theorem 3.19 and Section 1. Later published in *Ergodic Theory and Dynamical Systems*, DOI:10.1017/etds.2026.10313. https://arxiv.org/abs/2510.10848
2. D. Ahmadi Dastjerdi and S. Jangjoo, *Sofic S-gap Shifts, Entropy Function and Bowen–Franks Groups*, arXiv:1108.3414v1 (2011); subsequently *Computations on Sofic S-gap Shifts*, *Qualitative Theory of Dynamical Systems* 12 (2013), 393–406, Corollary 2.3. https://arxiv.org/abs/1108.3414
3. M. Doering and R. Pavlov, *A Characterization of the Sets of Periods within Shifts of Finite Type*, *Involve* 12 (2019), 203–220. https://cs.du.edu/~rpavlov/MDRP_periods.pdf
4. D. Ahmadi Dastjerdi and S. Jangjoo, *Dynamics and Topology of S-gap Shifts*, *Topology and its Applications* 159 (2012), 2654–2661, arXiv:1108.3242. https://arxiv.org/abs/1108.3242
