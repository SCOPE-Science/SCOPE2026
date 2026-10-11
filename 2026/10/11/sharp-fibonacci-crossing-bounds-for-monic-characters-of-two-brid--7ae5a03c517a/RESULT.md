# Sharp Fibonacci crossing bounds for monic characters of two-bridge knots
## Finding
Let \(K\) be a two-bridge knot with crossing number \(c\ge 3\), in Schubert form \(K(p,q)\) with \(p>0\) odd. Let \(X_0\) be an irreducible curve component of the \(\mathrm{SL}(2,\mathbb C)\)-character variety containing an irreducible character and a nonmonic character. Write \(\mathcal N\) for the number of monic characters on \(X_0\).

Set \(F_0=0\), \(F_1=1\), and \(F_{m+1}=F_m+F_{m-1}\). Define
\[
M_c=\begin{cases}
F_{c+1},&c\not\equiv2\pmod 3,\\
F_{c+1}-F_{c-4},&c\equiv2\pmod 3.
\end{cases}
\]
Then
\[
p\le M_c,
\qquad
\mathcal N\le16M_c^2.
\]
Moreover the bound \(p\le M_c\) is sharp for every \(c\ge3\) among two-bridge knots with crossing number \(c\).

## Assumptions and scope
Kim--Morifuji prove that for a two-bridge knot \(K(p,q)\), under exactly the stated hypothesis on \(X_0\), one has \(\mathcal N\le16p^2\). Their \(p\) is the odd Schubert numerator. For a positive reduced rational diagram with twist lengths \(a_1,\ldots,a_m\), the crossing number is \(c=a_1+\cdots+a_m\), and its determinant/Schubert numerator is the continuant \(K(a_1,\ldots,a_m)\). The assertion here is therefore an extremal statement about odd continuants of fixed weight, followed by substitution into the published \(16p^2\) estimate.

No claim is made that \(16M_c^2\) is the optimal possible number of monic characters. The sharpness statement concerns the determinant \(p\), not the character-count estimate.

## Proof
For a positive sequence \(a=(a_1,\ldots,a_m)\), let \(P(a)=K(a_1,\ldots,a_m)\) and let \(Q(a)=K(a_1,\ldots,a_{m-1})\), with the empty continuant equal to \(1\). Starting from the weight-one sequence \((1)\), for which \((P,Q)=(1,1)\), increasing the last entry by one sends
\[
(P,Q)\longmapsto(P+Q,Q),
\]
whereas appending a final \(1\) sends
\[
(P,Q)\longmapsto(P+Q,P).
\]
Conversely, repeatedly decreasing a last entry bigger than \(1\), or deleting a final \(1\), reduces any positive sequence to \((1)\). Thus every positive continuant of total weight \(c\) is obtained from \((1,1)\) by \(c-1\) such sum steps.

At every stage \(P\ge Q>0\). Among the two next states, retaining the larger old coordinate as the new second coordinate, \((P+Q,P)\), dominates \((P+Q,Q)\) for every future first coordinate. Repeating this greedy choice gives
\[
(P,Q)=(F_{c+1},F_c).
\]
Hence every positive continuant of weight \(c\) is at most \(F_{c+1}\).

If \(c\not\equiv2\pmod3\), then \(F_{c+1}\) is odd, because Fibonacci parity has period three. Thus the upper bound is already an admissible knot determinant. For \(c=3\), the sequence \((3)\) realizes it; for \(c\ge4\), the reduced positive sequence
\[
(2,\underbrace{1,\ldots,1}_{c-4},2)
\]
has continuant \(F_{c+1}\), giving a two-bridge knot of crossing number \(c\).

Now suppose \(c\equiv2\pmod3\). Then \(F_{c+1}\) is even, so the all-greedy extremum is a two-component rational link rather than a knot. Any knot determinant is odd and therefore its sum-step path must make a non-greedy choice before the last effective step. Suppose the first such choice occurs after weight \(j\), with \(2\le j\le c-2\). Up to that point the state is \((F_{j+1},F_j)\). The non-greedy step produces \((F_{j+2},F_j)\), instead of \((F_{j+2},F_{j+1})\). Even if every remaining step is greedy, the final first coordinate falls short of \(F_{c+1}\) by
\[
F_{c-j-1}F_{j-1}.
\]
Put \(r=j-1\) and \(s=c-j-1\), so \(r,s\ge1\) and \(r+s=c-2\). The elementary Fibonacci inequality
\[
F_rF_s\ge F_{r+s-2}
\]
holds: if \(r,s\ge2\), the difference is \(F_{r-2}F_{s-2}\), and the cases with an index \(1\) are immediate. Therefore every odd continuant of weight \(c\) satisfies
\[
P\le F_{c+1}-F_{c-4}.
\]
The bound is attained. At \(c=5\), the sequence \((3,2)\) has continuant \(7=F_6-F_1\). For \(c\ge8\) with \(c\equiv2\pmod3\), the reduced positive sequence
\[
(2,2,\underbrace{1,\ldots,1}_{c-6},2)
\]
has continuant \(F_{c+1}-F_{c-4}\), as follows directly from the continuant recurrence. Since \(c-4\not\equiv0\pmod3\), the subtracted Fibonacci number is odd, so the displayed determinant is odd and the rational link is a knot.

This proves the sharp determinant formula. Kim--Morifuji's Example 4.5 gives \(\mathcal N\le16p^2\), hence \(\mathcal N\le16M_c^2\).

## Verification
The standalone file `verify_bound.py` exhausts every positive composition of \(c\) for \(3\le c\le18\), computes the continuant, restricts to odd numerators, and confirms that the exact maximum equals \(M_c\). It separately checks the explicit witnesses above. Its expected terminal line is `VERIFY_OK c=3..18 exact_odd_continuant_max`.

The finite enumeration is only a sanity check. The infinite statement rests on the sum-step domination argument and the proved Fibonacci product inequality.

## Relationship to prior work
Kim--Morifuji's Theorem A gives presentation-dependent bounds for monic characters, their Corollary B gives the general crossing-number estimate \((c-1)2^{3c-1}\), and their Example 4.5 specializes a two-generator presentation of \(K(p,q)\) to \(\mathcal N\le16p^2\). They do not convert that polynomial-in-\(p\) bound into a sharp function of the crossing number for two-bridge knots.

Kauffman--Lopes give explicit determinant formulas and the recursion
\[
D_{m+1}=a_{m+1}D_m+D_{m-1}
\]
for rational knots and links, and note the Fibonacci specialization when all twist lengths are one. Their result supplies the continuant framework, but not the odd-numerator extremum at fixed total crossing number.

The new combination is therefore the exact parity-corrected extremal determinant \(M_c\) and its consequence for monic-character counts. Since \(F_c\) grows like \(\varphi^c/\sqrt5\), the resulting bound is \(O(\varphi^{2c})\), with exponential base \(\varphi^2\approx2.618\), rather than the base \(8\) in the general crossing estimate.

## Limitations
The character-count bound inherits all hypotheses of Kim--Morifuji's theorem: the chosen component must be an irreducible curve containing an irreducible character and a nonmonic character. The determinant extremum is specific to two-bridge knots. It does not assert that every value below \(M_c\) occurs, nor that \(16M_c^2\) is attained by any character variety.

The literature comparison found no statement of the parity-corrected maximum \(M_c\), but an older specialized rational-knot source could conceivably contain an equivalent continuant extremum under different terminology. This is a residual literature risk, not a gap in the proof.

## References
1. T. Kim and T. Morifuji, *Quantitative finiteness of monic characters of knots*, arXiv:2609.36772v1 (2026), especially Theorem A, Corollary B, and Example 4.5.
2. L. H. Kauffman and P. Lopes, *Determinants of Rational Knots*, Discrete Mathematics and Theoretical Computer Science 11 (2009), 111--122, DOI 10.46298/dmtcs.454, especially Proposition 7.1 and Remark 7.1.
