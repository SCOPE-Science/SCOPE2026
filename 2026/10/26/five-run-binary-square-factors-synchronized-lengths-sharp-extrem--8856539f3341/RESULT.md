# Five-run binary square factors: synchronized lengths, sharp extrema and rare resonance

## Finding

For any positive integers \(a,b,c,d,e\), consider the binary word \(w=0^a1^b0^c1^d0^e\) of length \(n=a+b+c+d+e\). A **square factor** is a distinct nonempty contiguous substring \(xx\) with \(x\ne\varepsilon\), counted once even if it occurs in several positions. Write \(P=\max(a,c,e)\), \(Q=\max(b,d)\), and
\[
\begin{aligned}
\alpha&=\mathbf1_{\{c\le a,\ b\le d\}},\\
\beta&=\mathbf1_{\{c\le e,\ d\le b\}},\\
H&=\mathbf1_{\{b=d\}}\max\bigl(0,\min(a,c-1)-\max(1,c-e)+1\bigr).
\end{aligned}
\]
Then the number of distinct square factors is exactly
\[
S(w)=\left\lfloor\frac P2\right\rfloor+\left\lfloor\frac Q2\right\rfloor+\alpha+\beta+H.
\]
This formula follows from the complete explicit factor classification below, not only from counting. Every mixed-symbol square, if present, has the **same length** \(2(c+\min(b,d))\). Its total number \(T=\alpha+\beta+H\) obeys the simultaneous sharp bounds
\[
\boxed{S(w)\le\lfloor n/2\rfloor,\qquad T(w)\le\lfloor(n+1)/3\rfloor.}
\]
Both bounds are attained for **every** \(n\ge5\), though not necessarily by the same word. At most four alternating runs permit at most one distinct mixed-symbol square, whereas five runs admit \(\Theta(n)\) such squares.

For a uniformly chosen positive five-part composition of \(n\), denote by \(H_n\) the three-run-root contribution \(H\). Its first-moment and positive-event ordinary generating functions are
\[
\sum_{n\ge5}\binom{n-1}{4}\mathbb E[H_n]z^n
=\frac{z^6}{(1-z)^2(1-z^2)^3},
\]
\[
\sum_{n\ge5}\binom{n-1}{4}\Pr(H_n>0)z^n
=\frac{z^6(1+z+z^2)}{(1-z)^4(1+z)^3}.
\]
In particular, \(\mathbb E[H_n]\to1/8\), while \(\Pr(H_n>0)\sim3/(2n)\): rare resonances may produce a growing collection of distinct square factors.

Moreover, with \((A,B,C,D,E)\sim\mathrm{Dirichlet}(1,1,1,1,1)\),
\[
\frac{S(w)}n\ \xrightarrow{\mathrm d}\ \frac{\max(A,C,E)+\max(B,D)}2,
\qquad \frac{\mathbb E[S(w)]}n\longrightarrow\frac13.
\]
All limits are for \(n\to\infty\) among positive five-part compositions, with no additional randomization over symbol complementation.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), all five run lengths are strictly positive integers, and factors must be **contiguous**. A distinct square is a word, not an occurrence or a pair of equal halves. The empty word is excluded. The two one-run square families may have different lengths; the common-length assertion applies **only** to squares using both symbols. Expectations and probabilities refer to the uniform distribution on the \(\binom{n-1}{4}\) positive ordered compositions \((a,b,c,d,e)\).

The entire nonempty square-factor set is the disjoint union of:

1. \(0^{2j}\) with \(1\le j\le\lfloor P/2\rfloor\), and \(1^{2j}\) with \(1\le j\le\lfloor Q/2\rfloor\).
2. \((0^c1^b)^2\) when \(c\le a\) and \(b\le d\).
3. \((1^d0^c)^2\) when \(c\le e\) and \(d\le b\).
4. \((0^i1^b0^{c-i})^2\) when \(b=d\) and \(\max(1,c-e)\le i\le\min(a,c-1)\).

These four classes are distinguished by root run count or orientation. Empty parameter intervals contribute no factors.

## Proof

**1. Exhaustive classification.** Let \(x\) be a nonconstant root with \(r\ge1\) binary transitions. The square \(xx\) has \(2r+\mathbf1_{\{x_1\ne x_{|x|}\}}\) transitions, which cannot exceed the four transitions of \(w\). Consequently \(r\in\{1,2\}\). If \(r=1\), the root starts and ends in different symbols, so its square has exactly three transitions. A root \(0^i1^j\) forces the square's four maximal runs into source runs one through four: its interior runs must fill the source second and third runs, so \(j=b\), \(i=c\), with outer constraints \(a\ge c\) and \(d\ge b\). Hence its unique possible square is \((0^c1^b)^2\), present exactly under \(\alpha=1\). A root \(1^i0^j\) analogously occupies source runs two through five and yields \((1^d0^c)^2\) under \(\beta=1\).

If \(r=2\), the root starts and ends with the same symbol, so its square has four transitions and occupies all five maximal source runs. It must start and end in \(0\), taking the form \(x=0^i1^j0^k\) with \(i,j,k\ge1\). Equality of the two halves forces the second and fourth source run lengths to coincide, \(b=d=j\); the middle zero run is split as \(c=i+k\), while the outer source zero runs must satisfy \(a\ge i\) and \(e\ge k\). Thus \(\max(1,c-e)\le i\le\min(a,c-1)\). Conversely each listed factor embeds contiguously. Different valid \(i\) give different factors. The unary factors are precisely the even zero runs up to \(P\) and even one runs up to \(Q\). This proves the set and counting formula.

When \(\alpha=1\), the mixed square length is \(2(c+b)\), and \(b\le d\). When \(\beta=1\), it is \(2(c+d)\), and \(d\le b\). Every fourth-class factor has length \(2(c+b)=2(c+d)\). Therefore all present mixed squares have length \(2(c+\min(b,d))\).

**2. Sharp upper bound for all squares.** If \(b\ne d\), then \(H=0\) and \(\alpha+\beta\le1\). The three nonmaximum run lengths contribute at least three to \(n-P-Q\). It follows that
\[
S(w)\le\lfloor P/2\rfloor+\lfloor Q/2\rfloor+1
\le\lfloor(n-3)/2\rfloor+1\le\lfloor n/2\rfloor.
\]
If \(b=d=t\), write \(Z=a+c+e\) and \(q=Z-P\). The smaller two zero runs have total \(q\), whence \(H\le\lfloor q/2\rfloor\). If \(\alpha+\beta\le1\), clearly \(\alpha+\beta+H\le\lfloor q/2\rfloor+1\). Otherwise both indicators equal one: \(c\le\min(a,e)\), \(H=c-1\), \(\alpha+\beta+H=c+1\), and \(q\ge2c\), so the same inequality holds. Since \(\lfloor t/2\rfloor+1\le t\) for every positive integer \(t\),
\[
S(w)\le\lfloor P/2\rfloor+\lfloor t/2\rfloor+\lfloor q/2\rfloor+1
\le\lfloor Z/2\rfloor+t=\lfloor n/2\rfloor.
\]
For every \(n\ge5\), \((a,b,c,d,e)=(n-4,1,1,1,1)\) attains equality.

**3. Sharp mixed-square bound and threshold.** The indicator and interval description gives \(T\le1+\min(a,c,e)\): the case \(b\ne d\) has \(T\le1\); the case \(b=d\) with at most one orientation has \(H\le\min(a,c-1,e)\); and if both orientations occur, \(c\le\min(a,e)\), \(H=c-1\), and \(T=c+1\). Hence \(T\le1+\lfloor(a+c+e)/3\rfloor\le\lfloor(n+1)/3\rfloor\). Conversely set \(m=\lfloor(n-2)/3\rfloor\), \(\delta=n-3m-2\in\{0,1,2\}\). The run lengths \((m+\delta,1,m,1,m)\) give \(T=m+1=\lfloor(n+1)/3\rfloor\). A mixed square with a one-transition root has three transitions, requiring at least four runs; a two-transition root has four transitions, requiring five. With only four source runs, at most one mixed square can therefore occur. In contrast, \((m,1,m,1,m)\) has \(m+1\) mixed squares.

**4. Rare-event generating functions.** For a three-run-root square counted in \(H\), the data \((i,k,b)\) are positive, and the corresponding run lengths satisfy \(c=i+k\), \(d=b\), \(a\ge i\), and \(e\ge k\). Each such triple together with the two nonnegative extensions \(a-i\), \(e-k\) contributes one to the sum of \(H\) over words. Thus
\[
\sum_{n\ge5}\sum_{a+b+c+d+e=n}H\,z^n
=\left(\sum_{b\ge1}z^{2b}\right)
\left(\sum_{i\ge1}z^{2i}\right)
\left(\sum_{k\ge1}z^{2k}\right)
\frac1{(1-z)^2}
=\frac{z^6}{(1-z)^2(1-z^2)^3}.
\]
The event \(H>0\) is equivalent to \(b=d\), \(c\ge2\), and \(a+e\ge c\). For fixed \(c\), summing the positive pairs \((a,e)\) with \(a+e\ge c\), and then \(b\ge1\) and \(c\ge2\), gives
\[
\sum_{n\ge5}\#\{(a,b,c,d,e):H>0,\ a+b+c+d+e=n\}z^n
=\frac{z^6}{(1-z)^3(1-z^2)}-
\frac{z^7}{(1-z)(1-z^2)^3}
=\frac{z^6(1+z+z^2)}{(1-z)^4(1+z)^3}.
\]
At the dominant singularity \(z=1\), the first rational function has leading pole \((1-z)^{-5}/8\), the second has leading pole \(3(1-z)^{-4}/8\); poles at \(z=-1\) are lower order. Since \(\binom{n-1}{4}\sim n^4/24\), the stated expectation and event-probability asymptotics follow.

**5. Typical normalized square count.** Uniform positive compositions scaled by \(n\) converge in distribution to \(\mathrm{Dirichlet}(1,1,1,1,1)\). From the exact formula, the contribution of \(\alpha+\beta\) is at most two and \(H/n\to0\) in probability: \(H>0\) has probability \(O(1/n)\). Floors differ from their arguments by at most one. Hence the asserted distributional limit. The expectation of the maximum of \(k\) specified coordinates of a uniform five-coordinate simplex point is \(H_k/5\), where \(H_2=3/2\), \(H_3=11/6\) are harmonic numbers. Indeed, inclusion–exclusion on the simplex shows that the tail probability of this maximum is \(\sum_{j=1}^k(-1)^{j+1}\binom kj(1-jt)_+^4\); integration over \(t\ge0\) gives \(\frac15\sum_{j=1}^k(-1)^{j+1}\binom kj/j=H_k/5\). Therefore the mean of the limiting variable is \((H_3+H_2)/10=1/3\). Finally \(0\le S(w)/n\le1/2\), so bounded convergence in distribution transfers the mean.

## Verification

Run the included standalone Python file `verify.py` using a Python 3 interpreter. It constructs every distinct nonempty square factor directly from all substrings, separately constructs the claimed complete list, and compares the two sets for all \(5^5=3125\) positive parameter tuples with each parameter between one and five. It also independently computes exact histograms for all length-\(n\) compositions for \(5\le n\le26\), checks both rational generating functions coefficient-by-coefficient, verifies both sharp maxima, and checks explicit witnesses through length 159. Successful output:

`VERIFY_OK complete_distinct_square_sets=3125 enumerated_length_histograms=22 sharp_witness_lengths=5..159`

These finite computations corroborate, but do not replace, the infinite mathematical arguments above.

## Relationship to prior work

Brlek and Li, *On the number of squares in a finite word* (arXiv:2204.10204, public preprint April 21, 2022), prove an upper bound for the number of distinct square factors of arbitrary finite words. Their general bound neither enumerates the exact five-run set nor supplies the sharp fixed-run extrema or the rare-resonance distribution. Li, *An upper bound of the number of distinct powers in binary words* (arXiv:2209.06891, September 14, 2022), proves the binary frequency-dependent bound and related inequalities for the number of squares and powers; these do not entail the present full five-run parameter classification. Li, Pachocki and Radoszewski, *A note on the maximum number of \(k\)-powers in a finite word* (arXiv:2205.10156), give unrestricted extremal-power bounds in their public abstract; the complete paper was not inspected for possible specializations. Jonoska, Manea and Seki, *A stronger square conjecture on binary words* (SOFSEM 2014), discuss square density and zero-run coefficients; accessible talk material contains general bounds, not the present full formula. Their full conference paper was not available for complete comparison.

## Limitations

The result concerns **exact contiguous squares** in binary words with exactly **five positive alternating runs**. It is not a formula for arbitrary words, scattered or abelian squares, higher powers, occurrence multiplicity, or primitive-root-only squares. Full global literature novelty is not certified: in particular, the complete 2014 conference paper could not be examined, and an equivalent specialization in other literature remains possible. The distributional statement is asymptotic; the rational generating functions give finite-length information only about \(H\), not the entire joint finite-length distribution of all square counts. The verifier is finite-range evidence, not an exhaustive proof of the infinite assertions.

## References

1. S. Brlek and S. Li, *On the number of squares in a finite word*, arXiv:2204.10204 (first public version April 21, 2022). https://arxiv.org/abs/2204.10204
2. S. Li, *An upper bound of the number of distinct powers in binary words*, arXiv:2209.06891 (first public version September 14, 2022). https://arxiv.org/abs/2209.06891
3. S. Li, J. Pachocki and J. Radoszewski, *A note on the maximum number of \(k\)-powers in a finite word*, arXiv:2205.10156 (May 20, 2022). https://arxiv.org/abs/2205.10156
4. N. Jonoska, F. Manea and S. Seki, *A stronger square conjecture on binary words*, SOFSEM 2014, DOI:10.1007/978-3-319-04298-5_30. Accessible presentation: https://users.ics.aalto.fi/sseki/presen/20140127_SOFSEM2014.pdf
