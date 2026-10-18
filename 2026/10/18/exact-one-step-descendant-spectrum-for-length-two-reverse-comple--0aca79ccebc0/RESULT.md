# Exact one-step descendant spectrum for length-two reverse-complement duplication

## Finding
Let \(\Sigma\) be an alphabet of even cardinality \(q\ge2\), equipped with a fixed-point-free complement involution \(a\mapsto\bar a\). For \(n\ge2\), let \(\mathcal D_2(w)\) be the *set* of words obtained from \(w\in\Sigma^n\) by exactly one reverse-complement duplication of a consecutive pair: replace a factor \(ab\) by \(ab\bar b\bar a\), leaving all other letters in place. Let \(B(w)=|\mathcal D_2(w)|\).

**Exact collision and sphere law.** For positions \(0\le i<j\le n-2\), the two duplications yield the same word **if and only if** the entire factor \(w_iw_{i+1}\cdots w_{j+1}\) alternates between a letter and its complement. Consequently,
\[
B(w)=n-1-C(w),\qquad
C(w)=\#\{i:0\le i\le n-3,\ w_{i+1}=\bar w_i,\ w_{i+2}=w_i\}.
\]
Thus the number of distinct outputs is determined by the number of complementary-alternating length-three factors.

**Full distribution.** Put \(F_{q,n}(z)=\sum_{w\in\Sigma^n}z^{\,n-1-B(w)}\). For every even \(q\ge2\), the entire distribution, at *every* length, has the bivariate generating function
\[
\boxed{\displaystyle
\sum_{n\ge2}F_{q,n}(z)t^{n-2}
=\frac{q\bigl[q+(q-1)(1-z)t\bigr]}{
1-(q-1+z)t+(q-1)(z-1)t^2}.}
\]
In particular, the coefficient \([z^k]F_{q,n}(z)\) counts exactly the words having \(n-1-k\) distinct one-step descendants. For a uniformly random word \(W\in\Sigma^n\),
\[
\mathbb E B(W)=n-1-\frac{n-2}{q^2},
\qquad
\operatorname{Var}B(W)=
\frac{(n-2)(q^2-1)+2(n-3)(q-1)}{q^4}\quad(n\ge3),
\]
with variance zero at \(n=2\).

For \(n\ge3\), the minimum \(B=1\) is attained by precisely \(q\) completely complementary-alternating words. The maximum \(B=n-1\) is attained exactly by the words avoiding complementary-alternating length-three factors; their number is \(F_{q,n}(0)\), with initial values \(F_{q,2}(0)=q^2\), \(F_{q,3}(0)=q^3-q\) and recurrence \(F_{q,n}(0)=(q-1)[F_{q,n-1}(0)+F_{q,n-2}(0)]\) for \(n\ge4\).

## Assumptions and scope
The complement operation is an involution with no fixed points; it need not be defined by numerical symbols. A duplication is inserted **immediately after** its original pair. A one-step descendant *set* counts identical outputs only once; it is not a multiset of positions. No assertions are made about multiple sequential errors, descendant-cone sizes, optimal codes, or arbitrary duplication lengths. The theorem includes every even alphabet size and all integers \(n\ge2\). The size of \(\Sigma\) must be even for a fixed-point-free involution.

## Proof
**1. Cancellation reduces equality to a word equation.** Index letters starting at zero. Let the pair chosen at position \(i\) be \(w_iw_{i+1}\), and write \(\mathrm{rc}(ab)=\bar b\bar a\). For \(i<j\), both duplication outputs share the prefix through position \(i+1\) and the suffix after position \(j+1\). Cancel these common strings. With
\[
x=\mathrm{rc}(w_iw_{i+1}),\quad
z=w_{i+2}\cdots w_{j+1},\quad
y=\mathrm{rc}(w_jw_{j+1}),
\]
where \(|x|=|y|=2\) and \(|z|=d=j-i\), equality is exactly the equation \(xz=zy\).

When \(d=1\), write the three source letters as \(a,b,c\). The equation is \(\bar b\bar a c=c\bar c\bar b\), which holds exactly when \(a=c=\bar b\).

When \(d\ge2\), comparing the first two letters of \(xz=zy\) gives \(x=z_0z_1\); comparing the remaining positions inside \(z\) gives \(z_h=z_{h-2}\) for every \(2\le h<d\). The final two letters give \(z_{d-2}z_{d-1}=y=\bar z_{d-1}\bar z_{d-2}\). Hence \(z_{d-1}=\bar z_{d-2}\), and period two implies that all successive letters of \(z\) are complements. Since \(x=z_0z_1\) is complementary-alternating, \(\mathrm{rc}(x)=x\), so the preceding original pair \(w_iw_{i+1}\) equals \(x\). The complete factor from \(i\) through \(j+1\) is therefore complementary-alternating. Conversely, on any such alternating factor, the two inserted reverse-complement pairs and the intervening string satisfy \(xz=zy\); both duplication outputs coincide. This proves the exact two-position collision criterion, including overlapping inserted blocks.

**2. Count distinct outcomes.** The \(n-1\) possible duplication positions \(0,\ldots,n-2\) are partitioned by output equality. By step 1, positions \(i<j\) are equivalent precisely when every consecutive pair in the interval \(w_i\cdots w_{j+1}\) is complementary. Thus each equivalence class is a consecutive block of positions in a maximal complementary-alternating run, or one isolated position. Adjacent positions \(i,i+1\) merge exactly when \(w_iw_{i+1}w_{i+2}\) is complementary-alternating. There are \(C(w)\) such adjacent mergers, and an interval partition with \(n-1\) positions and \(C(w)\) mergers has \(n-1-C(w)\) classes. These are exactly the distinct one-step descendants.

**3. Enumerate the complete distribution.** Classify a length-two suffix as type \(X\) if its two letters are *not* complements, or type \(Y\) if they are. For \(q^2\) length-two words the state counts are \(q(q-1)\) and \(q\), respectively. Appending one symbol from type \(X\) gives \(q-1\) choices for type \(X\) and one for type \(Y\), with no new complementary-alternating length-three factor. Appending from type \(Y\) gives \(q-1\) choices for \(X\) and one for \(Y\), but the latter creates exactly one such triple and receives weight \(z\). Therefore
\[
F_{q,n}(z)=q\begin{pmatrix}q-1&1\end{pmatrix}
\begin{pmatrix}q-1&1\\q-1&z\end{pmatrix}^{n-2}
\begin{pmatrix}1\\1\end{pmatrix}.
\]
Summing with the geometric matrix identity \(\sum_{m\ge0}t^mT^m=(I-tT)^{-1}\) and evaluating the \(2\times2\) inverse yields the stated rational generating function. This identity is formal in \(t\), so it is valid for every \(n\ge2\), not merely asymptotically.

**4. Moments and extreme cases.** Define \(I_i\) as the indicator of a complementary-alternating triple starting at position \(i\). Under the independent uniform-letter model, \(\mathbb E I_i=q^{-2}\) and \(\operatorname{Var}I_i=(q^2-1)/q^4\). Consecutive indicators have joint probability \(q^{-3}\) and covariance \((q-1)/q^4\). Indicators with starts at distance at least two are independent: at distance two their joint probability is \(q^{-4}\), and at greater distances they involve disjoint letters. Summing the \(n-2\) variances and the \(n-3\) adjacent covariances, then using \(B=n-1-\sum I_i\), proves both moment formulas. All \(n-2\) triples are alternating precisely for fully complementary-alternating words, of which there are \(q\). Evaluating the rational generating function at \(z=0\) gives the indicated recurrence for the zero-collision words, completing the proof.

## Verification
The companion standalone script `verify.py` uses direct duplication construction, independently of the collision criterion, on **every** word of lengths \(2\) through \(12\) for \(q=2\), through \(7\) for \(q=4\), through \(5\) for \(q=6\), and through \(4\) for \(q=8\). It compares every pair of duplication positions, the full sphere-size histogram, exact rational moments, and the transfer-matrix recurrence for lengths through \(35\) at each tested alphabet size. Run `python verify.py` with Python 3 and no external dependencies. These are finite corroborations; the symbolic argument in the Proof section establishes the claims for every length and even alphabet size.

## Relationship to prior work
Ben-Tolila and Schwartz introduced and analyzed this reverse-complement duplication model across alphabet sizes, and specifically studied the binary length-two system's expressive capacity and entropy. Their results do not state the full one-step descendant-size spectrum or its rational bivariate generating function. Yohananov and Schwartz treat coding capacity under arbitrary numbers of duplications; their statements likewise concern a different invariant. A later paper by Zabokritskiy studies multiple reverse-complement and palindromic duplications, including the *maximum two-error* descendant count and a coordinate-wise channel conjugacy for even duplication lengths. A maximum count after exactly two errors does not entail the distribution of one-error output degrees; the full text of this later paper could not be inspected and remains an explicit overlap risk. Research records on inverse branching and ordinary tandem duplication count different output or parent relations, and likewise do not directly imply this full distribution.

## Limitations
This result gives the complete **one-step forward** distribution, not an optimal error-correcting code, the inverse-parent distribution for a fixed received word, or the number of descendants following two or more errors. The complement involution must be fixed-point-free. The later multi-error paper noted above was checked at abstract level only; its inaccessible details might contain a related one-step lemma, and the possibility of earlier unpublished or unindexed statements is not eliminated. The mathematical result has undergone self-review only; no independent audit has been performed.

## References
1. E. Ben-Tolila and M. Schwartz, *On the Reverse-Complement String-Duplication System*, arXiv:2112.11811v1 (first public submission 22 December 2021), particularly Sections II, IV and V. https://arxiv.org/abs/2112.11811
2. L. Yohananov and M. Schwartz, *On the Coding Capacity of Reverse-Complement and Palindromic Duplication-Correcting Codes*, arXiv:2312.00394 (first public submission 1 December 2023), Sections 2–5. https://arxiv.org/abs/2312.00394
3. A. L. Zabokritskiy, *Coding for Multiple Reverse-Complement and Palindromic Duplications*, arXiv:2609.00779 (first public submission 1 September 2026); abstract inspected, full text unavailable. https://arxiv.org/abs/2609.00779
