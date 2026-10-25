# Exact fixed-content Parikh-matrix image and its parity boundary

## Finding
For the ordered alphabet \(a<b<c\), let \(\mathcal W_m\) comprise all words with exactly two \(a\)'s, \(m\) \(b\)'s, and two \(c\)'s, where \(m\ge0\). Denote by \(u=\binom{w}{ab}\), \(v=\binom{w}{bc}\), and \(z=\binom{w}{abc}\) the counts of scattered subwords. These three numbers determine the Parikh matrix once the letter multiplicities are fixed.

**Exact image theorem.** For integers \(0\le u\le m\) and \(0\le v\le2m\), set \(s=u+v\). The set of attainable \(z\) at the prescribed \((u,v)\) is exactly
\[
\mathcal Z_m(u,v)=\begin{cases}
\{0,1,\ldots,\min(u,\max(0,s-m))\},&s<2m,\\
\{j:0\le j\le u,\ j\equiv u\pmod 2\},&s=2m,\\
\{2(s-2m),2(s-2m)+1,\ldots,u+s-2m\},&s>2m.
\end{cases}
\]
For \(m<u\le2m\), the full image follows by reversal: \((u,v,z)\) occurs if and only if \((2m-u,2m-v,4m-2u-2v+z)\) occurs.

Consequently the number of distinct Parikh matrices realized by \(\mathcal W_m\) is
\[
\boxed{I(m)=\frac{(m+1)(m+2)(2m+1)}2}\qquad(m\ge0).
\]
For a fixed \(0\le u\le m\), precisely \(2m+1+mu-\lceil u/2\rceil\) distinct pairs \((v,z)\) occur. In particular the image is cubic in \(m\) while the number of input words is \(6\binom{m+4}{4}\), of quartic order.

## Assumptions and scope
Subsequences are scattered and their occurrences are counted by increasing index tuples, not just presence. The Parikh matrix uses the fixed order \(a<b<c\); no statement is made about strong matrix equivalence, which varies the alphabet order. Words are linear, including all orders of the four distinguished markers and all \(m\ge0\). Two matrices are distinct if any entry differs. The result is an image-size and support classification, not a classification of individual fiber sizes.

## Proof
**Step 1: four independently placed cuts.** Index the \(m\) occurrences of \(b\) from left to right. For each occurrence of \(a\), count the number of \(b\)'s to its right; write those numbers as \(x_1\ge x_2\), where \(0\le x_i\le m\). For each \(c\), count the number of \(b\)'s to its left; write \(y_1\ge y_2\), with \(0\le y_i\le m\). Any two such pairs can be realized simultaneously: insert the \(a\)'s and \(c\)'s at their prescribed cuts in the sequence of \(b\)'s, ordering markers arbitrarily at coincident cuts. Then
\[
u=x_1+x_2,\qquad v=y_1+y_2,\qquad
z=\sum_{i=1}^{2}\sum_{j=1}^{2}(x_i+y_j-m)_+,
\]
where \((t)_+=\max(0,t)\). Indeed an \(a\)-\(c\) pair spans exactly \((x_i+y_j-m)_+\) positions containing \(b\), and every \(abc\) subsequence has a unique outer pair.

**Step 2: reduce the image to an integer-grid interval.** First suppose \(u\le m\). Put \(X=x_1-x_2\), \(Y=y_1-y_2\), and \(h=u+v-2m\). Exactly the grid values
\[
X\in\{u\bmod2,u\bmod2+2,\ldots,u\},\quad
Y\in\{v\bmod2,v\bmod2+2,\ldots,\min(v,2m-v)\}
\]
are possible, independently. The four terms in the formula for \(z\) are
\[
\frac12(h+X+Y)_+,\quad\frac12(h+X-Y)_+,\quad
\frac12(h-X+Y)_+,\quad\frac12(h-X-Y)_+.
\]
For \(q\ge0\) define
\[
G_q(X,Y)=\frac12\big((X+Y-q)_+ +(|X-Y|-q)_+\big).
\]
Pairing opposite signs gives the identity
\[
z=2\max(h,0)+G_{|h|}(X,Y).
\]

Here is the elementary grid lemma needed to determine the complete support. Suppose \(U,V,q\) are nonnegative integers, \(q\ge1\), \(q\ge|U-V|\), and \(q\equiv U+V\pmod2\). On the grid \(X=U\bmod2,U\bmod2+2,\ldots,U\), \(Y=V\bmod2,V\bmod2+2,\ldots,V\), the values of \(G_q\) are precisely
\[
\{0,1,\ldots,\max(0,(U+V-q)/2)\}.
\]
To prove this, observe that \(G_q\) is nondecreasing in both \(X\) and \(Y\), and its maximum occurs at \((U,V)\). Since \(|U-V|\le q\), its value there is \(\max(0,(U+V-q)/2)\). Start at the smallest grid point \((U\bmod2,V\bmod2)\), where \(G_q=0\), and increase coordinates by two until reaching \((U,V)\), always staying in the strip \(|X-Y|\le q\): increase the smaller coordinate first when the difference is at the strip boundary. Such a monotone lattice path exists since both endpoints lie in the strip and \(q\ge1\) (when one coordinate is exhausted, its remaining endpoint lies in the strip). Inside the strip, \(G_q=(X+Y-q)_+/2\), so each step changes it by either zero or one. Its consecutive attained values therefore contain every integer between its endpoints, proving the lemma. When \(q=0\), the same expression simplifies instead to \(G_0(X,Y)=\max(X,Y)\).

Apply the lemma with \(U=u\), \(V=\min(v,2m-v)\), \(q=|h|\). If \(h\ne0\), then \(q\ge|U-V|\) and \(q\equiv U+V\pmod2\), as follows directly by separating \(v\le m\) from \(v>m\). When \(h<0\), the grid maximum is \(\min(u,\max(0,u+v-m))\). When \(h>0\), the minimum is \(2h\) and the maximum is \(u+h\). For \(h=0\), both \(X,Y\) have the parity of \(u\), their upper bounds are both \(u\), and \(G_0=\max(X,Y)\) produces exactly the integers of that parity from \(u\bmod2\) to \(u\). These are exactly the three displayed cases.

**Step 3: reflect and count.** Reverse each word. At a fixed \(b\), the numbers of \(a\)'s before it and \(c\)'s after it change from \((A,C)\) to \((2-A,2-C)\). Summing over all \(m\) positions proves the affine reflection stated above. Hence the number of distinct \((v,z)\) at \(u\) agrees with that at \(2m-u\). Summing the cardinalities of the three support cases over \(0\le v\le2m\) gives, for \(0\le u\le m\),
\[
R_m(u)=2m+1+mu-\left\lceil\frac u2\right\rceil.
\]
Finally,
\[
I(m)=2\sum_{u=0}^{m-1}R_m(u)+R_m(m)
=\frac{(m+1)(m+2)(2m+1)}2.
\]
The identity also holds at \(m=0\), for which all six marker-only words have the same Parikh matrix.

## Verification
The accompanying standalone `checker.py` computes each Parikh matrix directly for all words with two \(a\)'s, two \(c\)'s and up to fifteen \(b\)'s. Independently, it realizes the outer-marker cuts and compares every \((u,v)\) support with the displayed piecewise formula. It checks 93,024 words and all 5,456 parameter slices through \(m=15\), and additionally 2,500 seeded random cut slices with \(m\le90\). Run `python3 checker.py`; the expected output begins `CHECK_OK`. These finite checks test implementations and boundaries; the unrestricted theorem follows from the preceding proof, not from finite enumeration.

## Relationship to prior work
Parikh matrices were introduced to encode counts of ordered scattered subwords; the classical ternary matrix has exactly the entries \(\binom{w}{a}\), \(\binom{w}{b}\), \(\binom{w}{c}\), \(\binom{w}{ab}\), \(\binom{w}{bc}\), \(\binom{w}{abc}\). The 2015 work of Teh on rewriting systems characterizes general matrix equivalence in terms of rewriting and counters. Teh's 2015 work on strong matrix equivalence studies the more stringent invariant obtained by varying alphabet orders, including results at small values of \(\binom{w}{abc}\). The present result instead identifies all attainable matrices and their exact number for a fixed infinite family of contents \((2,m,2)\). General definitions and rewriting criteria do not directly provide the stated piecewise image or polynomial, and no covering fixed-content formula was found in the inspected sections or targeted searches. Distinct prior findings on contents \((2,m,1)\) and general polynomial upper bounds likewise do not imply the \((2,m,2)\) image.

## Limitations
Priority is subject to possible equivalent enumerations in older literature under different terminology; lack of a matching search result is not a proof of novelty. The theorem is specific to the ordered ternary alphabet and content \((2,m,2)\). It does not determine the multiplicities of matrix fibers or strong matrix-equivalence classes. Although a direct checker is provided, no independent mathematical audit has been performed.

## References
1. W. C. Teh, *Parikh matrices and Parikh rewriting systems*, arXiv:1506.06476, first posted 2015-06-22; https://arxiv.org/html/1506.06476v1 (especially Definition 2.2, Theorem 2.3, and Sections 4–6).
2. W. C. Teh, *Parikh matrices and strong M-equivalence*, arXiv:1501.07354, first posted 2015-01-29; https://arxiv.org/html/1501.07354v2 (Sections 2–4).
3. A. Atanasiu, C. Martín-Vide, and A. Mateescu, *On the Injectivity of the Parikh Matrix Mapping*, Fundamenta Informaticae 49 (2002), 289–299; https://doi.org/10.3233/FUN-2002-49401 (bibliographic record and abstract).
