# Exact Lie complexity of the binary Rudin–Shapiro word
## Finding
Let \(\mathbf r=r(0)r(1)r(2)\cdots\) be the binary Rudin–Shapiro word, where \(r(n)\) is the parity of the number of overlapping occurrences of \(11\) in the ordinary binary expansion of \(n\), including \(r(0)=0\).

The Lie complexity \(L_{\mathbf r}(n)\) counts cyclic-conjugacy classes of binary words of length \(n\) **all** of whose cyclic rotations occur as contiguous factors of \(\mathbf r\). For every integer \(n\ge1\),
\[
L_{\mathbf r}(n)=
\begin{cases}
2,&n=1\text{ or }n=5,\\
3,&n=2\text{ or }n=6,\\
6,&n=4,\\
4,&n=3\text{ or }n=2^k\ (k\ge3),\\
0,&\text{otherwise}.
\end{cases}
\]

The four surviving cyclic classes at each length \(2^k\), \(k\ge3\), are represented explicitly by
\[
\tau(\sigma^k(a)),\quad \tau(\sigma^k(b)),\quad
\tau(\sigma^k(c)),\quad \tau(\sigma^k(d)),
\]
where the four-letter substitution and binary coding are
\[
\sigma:\ a\mapsto ab,\ b\mapsto ac,\ c\mapsto db,\ d\mapsto dc;
\qquad \tau(a)=\tau(b)=0,\ \tau(c)=\tau(d)=1.
\]
These four words are in different cyclic classes for each such \(k\).

## Assumptions and scope
A conjugacy class \([u]_C\) consists of all distinct cyclic rotations of the nonempty finite word \(u\). It contributes one to Lie complexity precisely when \([u]_C\) is contained in the factor language, not merely when one rotation occurs. All factors here are contiguous; indices of the infinite words start at zero.

Put \(\mathbf s=\sigma^\omega(a)\). Since \(\sigma(a)\) and \(\sigma(b)\) start in \(a\), whereas \(\sigma(c)\) and \(\sigma(d)\) start in \(d\), all letters of \(\mathbf s\) at even positions lie in \(\{a,d\}\). All letters at odd positions lie in \(\{b,c\}\). Directly from the substitution, \(\tau(\mathbf s)\) satisfies
\[
r(2j)=r(j),\qquad r(2j+1)=r(j)\oplus (j\bmod2),\qquad r(0)=0,
\]
which is also the binary digit-pair definition of the Rudin–Shapiro word. Thus \(\mathbf r=\tau(\mathbf s)\).

The complete two-letter factor set of \(\mathbf s\) is
\[
\mathcal B=\{ab,ac,ba,bd,ca,cd,db,dc\}.
\]
The four internal substitution pairs are \(ab,ac,db,dc\); the boundary pairs from elements of \(\mathcal B\) are precisely \(ba,bd,ca,cd\). The set is closed under substitution and all eight occur in the substitution fixed point. This fact makes the finite factor enumerations below exhaustive, rather than sampled.

## Proof
**1. A finite exact phase obstruction.** For every \(x\in\{a,b,c,d\}\), the block \(\tau(\sigma^4(x))\) has length \(16\). Every length-eight factor of \(\mathbf r=\tau(\sigma^4(\mathbf s))\) starts at a unique offset \(j\in\{0,\ldots,15\}\) inside such a block and lies in the concatenation \(\tau(\sigma^4(xy))\) for some \(xy\in\mathcal B\). Conversely every such pair and offset occurs in the fixed point. Hence the sets
\[
E=\bigl\{\tau(\sigma^4(xy))[j:j+8]:xy\in\mathcal B,\ 0\le j<16,\ j\equiv0\pmod2\bigr\},
\]
\[
O=\bigl\{\tau(\sigma^4(xy))[j:j+8]:xy\in\mathcal B,\ 0\le j<16,\ j\equiv1\pmod2\bigr\}
\]
are exactly the length-eight factors beginning at even and at odd positions, respectively. Exhaustive finite set construction gives
\[
|E|=24,\qquad |O|=32,\qquad E\cap O=\varnothing.
\]
All the individual eight-bit factors are recorded in `certificate.json`; `verify.py` recomputes them directly from the eight legal pairs. Thus **every length-eight factor determines the parity of its starting position**.

**2. No non-dyadic long lengths.** Let \(u\) be a circular binary word of length \(n\ge9\) such that every cyclic rotation occurs in \(\mathbf r\). Its successive cyclic length-eight windows have a unique starting parity, by step 1. The length-nine cyclic windows are each factors because every length-\(n\) rotation occurs, so the starting parities of successive eight-windows must alternate, including across the circular wrap. Hence \(n\) is even.

Write \(n=2m\), and rotate \(u\) so that its first eight letters have even starting parity. Split the word into consecutive two-bit blocks. The coding \(h=\tau\circ\sigma\) is a bijection from \(\{a,b,c,d\}\) onto \(\{00,01,10,11\}\). Every two-step rotation of \(u\) is a factor beginning at even position, hence its inverse under \(h\) is a factor of \(\mathbf s\). The inverse \(v\) of the chosen rotation therefore has **every cyclic rotation** in the factor language of \(\mathbf s\). Different binary conjugacy classes map to different four-letter conjugacy classes, so
\[
L_{\mathbf r}(2m)\le L_{\mathbf s}(m)\qquad(2m\ge10).
\]

For the four-letter fixed point, each factor of length at least two has letters alternating between the two disjoint classes \(\{a,d\}\) and \(\{b,c\}\). If all rotations of a word of length \(m\ge2\) occur, its **cyclic** letter-type sequence must alternate, forcing \(m\) even. For \(m=2q\), choose its rotation starting in \(\{a,d\}\). Each such occurrence starts at even position of \(\mathbf s=\sigma(\mathbf s)\); it therefore splits into distinct substitution pairs \(ab,ac,db,dc\), and the four-letter inverse exists uniquely. All two-step rotations have that same type and split at substitution boundaries. Thus the inverse has all its rotations as factors of \(\mathbf s\), yielding an injective map of qualifying conjugacy classes and
\[
L_{\mathbf s}(2q)\le L_{\mathbf s}(q).
\]
It follows by repeated division by two that \(L_{\mathbf s}(m)=0\) unless \(m\) is a power of two, and \(L_{\mathbf s}(2^j)\le L_{\mathbf s}(1)=4\). Therefore, for every \(n\ge9\),
\[
L_{\mathbf r}(n)=0\quad\text{unless }n\text{ is a power of two},
\qquad L_{\mathbf r}(2^k)\le4\quad(k\ge4).
\]

**3. Four full conjugacy classes at every large dyadic length.** Set \(W_k(x)=\tau(\sigma^k(x))\) and \(N=2^k\). From the images of the four letters, \(W_k(a)\) and \(W_k(b)\) have equal first halves, and so do \(W_k(c)\) and \(W_k(d)\); also \(W_k(a)\) and \(W_k(c)\) have equal last halves, and so do \(W_k(b)\) and \(W_k(d)\). All eight pairs in \(\mathcal B\) occur. Consequently the cyclic rotation of \(W_k(x)\) by \(t\) positions is a factor of \(\mathbf r\): for \(0\le t\le N/2\), it crosses the boundary in the legal pair \(ab,ba,cd,dc\), respectively for \(x=a,b,c,d\); for \(N/2\le t<N\), it crosses the boundary in \(ca,db,ac,bd\), respectively. In the first case the next word shares the first half with the target; in the second case the preceding word shares the last half. Thus all four displayed dyadic words are qualifying.

For \(k\ge4\), each \(W_k(x)\) occurs at an even position (indeed at a multiple of \(2^k\)). A hypothetical cyclic identity between \(W_k(x)\) and \(W_k(y)\) can only use an even rotation, because of the unique length-eight starting parity. Decoding two-bit blocks reduces it to a cyclic identity between \(\sigma^{k-1}(x)\) and \(\sigma^{k-1}(y)\). Each of these words starts in \(\{a,d\}\), and their letters alternate between the two classes, so their cyclic identity again has even shift. Apply the injective inverse of \(\sigma\), repeating until a cyclic identity between the one-letter words \(x\) and \(y\) remains. Hence \(x=y\). For \(k=3\), the four length-eight representatives are pairwise inequivalent by the explicit finite certificate. We therefore have exactly four classes at every \(2^k\) with \(k\ge3\).

**4. Short lengths.** The same legal-bigram/supertile formula lists all length-\(n\) factors for \(1\le n\le8\) using a block width at least \(n\). For each word it tests whether all rotations are among those exhaustive factors and then takes the lexicographically least representative of the qualifying class. The resulting class counts for lengths \(1,2,3,4,5,6,7,8\) are respectively
\[
2,\ 3,\ 4,\ 6,\ 2,\ 3,\ 0,\ 4.
\]
The complete short-length representatives are in `certificate.json`. These verified finite base cases and steps 1–3 establish the finding for all positive \(n\).

## Verification
Run `python3 verify.py` in the same directory as `certificate.json`. It reconstructs the exact eight legal four-letter bigrams and the complete length-eight factor sets by starting parity, verifies their \(24+32\) disjoint partition, and reconstructs the Rudin–Shapiro digit-pair definition independently through index \(65535\).

It computes the exhaustive Lie class lists for lengths \(1\) through \(8\), compares complete finite factor sets with a long independently generated prefix, checks the resulting formula on **every length through 128**, and verifies the four cyclic witnesses and legal-pair boundary rotations through dyadic length \(512\). The finite computations verify the nonstandard phase certificate and the boundary indexing; the all-length statement is proved by the two injective desubstitution arguments and the explicit four-class construction.

## Relationship to prior work
Bell and Shallit introduce Lie complexity, prove it is automatic for automatic words, and obtain exact formulas for the Thue–Morse, ternary Thue–Morse, Cantor, Fibonacci, and Tribonacci words. Their inspected examples do **not** contain the Rudin–Shapiro word. Their general automaticity theorem and their bound in terms of factor complexity do not give the exact values or the dyadic support proved here.

De Luca and Fici derive an exact Lie-complexity formula for Sturmian words, a different class of sequences. Cassaigne, Fici, Sciortino, and Zamboni study **cyclic complexity**, which counts classes having at least one occurring representative; it does not enforce occurrence of every rotation, and its results on Toeplitz and Thue–Morse words do not determine the Rudin–Shapiro Lie invariant.

Allouche and Shallit's 1993 Proposition 2 explicitly proves that the binary coding of the Rudin–Shapiro four-letter fixed point is injective on its \(56\) length-eight factors. Since the four-letter factors at even and odd positions start in disjoint letter types, **their result already implies the length-eight parity obstruction used in our proof**. That obstruction is therefore credited as prior structural information, independently recomputed here for self-contained verification, rather than claimed as novel. Their paper gives ordinary factor complexity, not Lie complexity, and does not classify the cyclic classes whose every representative occurs. The contribution here is the two-level cyclic desubstitution and complete exact Lie spectrum obtained from that known recognizability property.

## Limitations
This theorem treats the classical binary Rudin–Shapiro word only, not generalized Rudin–Shapiro words or other letter codings. Its exact class representatives are given at dyadic lengths at least eight; the exceptional short lengths are listed separately in the finite certificate. It says nothing about ordinary cyclic complexity, the number of classes with some but not all rotations present.

The finite phase lemma is certified by an exhaustive 16-superblock computation over all eight proven legal bigrams, and is also a consequence of the known eight-factor coding injectivity of Allouche and Shallit. This is a finite mathematical lemma with an explicit reproducible construction, not an infinite-pattern extrapolation or an asserted new lemma. Originality searches cannot exclude an unindexed earlier calculation of the same Lie invariant.

## References
1. J. P. Bell and J. Shallit, “Lie complexity of words,” arXiv:2102.03821v1, first public 2021-02-07; *Theoretical Computer Science* **927** (2022), 98–108.
2. A. De Luca and G. Fici, “On the Lie complexity of Sturmian words,” arXiv:2206.00995 (2022); *Theoretical Computer Science* **938** (2022), 81–85.
3. J. Cassaigne, G. Fici, M. Sciortino, and L. Q. Zamboni, “Cyclic complexity of words,” arXiv:1402.5843; *Journal of Combinatorial Theory, Series A* **145** (2017), 36–56.
4. J.-P. Allouche and J. Shallit, “Complexité des suites de Rudin–Shapiro généralisées,” *Journal de Théorie des Nombres de Bordeaux* **5** (1993), 283–302, DOI 10.5802/jtnb.94.
