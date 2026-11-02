# The full rank-support enumerator of nonbinary linear diameter-three anticodes

## Finding

For every prime power \(q\ge3\) and integer \(n\ge0\), let \(\mathscr A_q(n,3)\) consist of all \(\mathbb F_q\)-linear subspaces \(C\le\mathbb F_q^n\) such that every vector in \(C\) has Hamming weight at most three. Let \(s(C)\) be the number of coordinate positions that are nonzero in at least one word, and \(r(C)=\dim C\). Then the complete rank-by-support polynomial is

\[
\begin{aligned}
E_{q,n}(u,v)&=\sum_{C\in\mathscr A_q(n,3)}u^{s(C)}v^{r(C)}\\
&=1+nuv+\binom n2u^2((q-1)v+v^2)\\
&\quad+\binom n3u^3((q-1)^2v+(q^2+q-2)v^2+v^3)\\
&\quad+8\mathbf1_{q=3}\binom n4u^4v^2.
\end{aligned}
\]

Consequently the total number of subspaces is

\[
|\mathscr A_q(n,3)|=1+n+q\binom n2+(2q^2-q)\binom n3+8\mathbf1_{q=3}\binom n4.
\]

In particular its polynomial degree in \(n\) is four when \(q=3\), with leading coefficient \(1/3\), and three when \(q\ge4\), with leading coefficient \((2q^2-q)/6\). All full-support four-coordinate examples occur at \(q=3\), have dimension two, and are precisely the eight labelled ternary tetracodes on a prescribed four-coordinate support.

## Assumptions and scope

The alphabet size \(q\) is a prime power at least three, the ambient coordinates are labelled, and subspaces are counted as distinct subspaces, not up to code equivalence. We include \(n=0\), the zero subspace and codes whose actual support is smaller than their ambient length. The diameter of a linear code is the maximum Hamming weight of one of its codewords, because differences of codewords lie in the code. The indicator \(\mathbf1_{q=3}\) equals one only for the ternary field. No assertion is made for \(q=2\) or diameter greater than three.

## Proof

**Step 1 (rank and support).** Write \(s=s(C)\) and \(r=r(C)\). Any rank-\(r\) row-reduced generator has \(r\) pivot columns. Taking the linear combination of all \(r\) generator rows, whose coefficients are all one, yields a word nonzero at every pivot, so \(r\le3\). At each coordinate of its support, a uniformly chosen codeword is nonzero with probability \((q-1)/q\). Thus its expected Hamming weight is \(s(q-1)/q\), whence
\[
s\le\left\lfloor\frac{3q}{q-1}\right\rfloor.
\]
This is four for \(q=3,4\), and three for \(q\ge5\).

**Step 2 (exclude full-support rank three in length four).** Suppose \(C\le\mathbb F_q^4\) has rank three and full support. Then \(C\) is the kernel of a nonzero linear functional with coefficient vector \(h\), of weight \(t\). Since the code has full support, \(t\ge2\) (a functional supported on exactly one coordinate would force that coordinate to vanish). Among vectors all of whose four coordinates are nonzero, the number in \(\ker h\) equals
\[
(q-1)^{4-t}\frac{(q-1)^t+(q-1)(-1)^t}{q}.
\]
Indeed, this is the number of \(t\)-tuples of nonzero field elements summing to zero, times the free choices at the remaining coordinates; it follows by elementary additive-character orthogonality, or induction on \(t\). For \(t=2,3,4\) and \(q\ge3\) it is strictly positive. This produces a weight-four word, contradicting the anticode assumption. Rank one in length four also contains a weight-four word when its support is four.

**Step 3 (rank two, length four).** Choose a full-rank \(2\times4\) generator matrix \(G\) of a full-support rank-two subspace. Its four columns are nonzero vectors in \(\mathbb F_q^2\). The requirement that every nonzero codeword \(aG\) have at least one zero coordinate says that for each one-dimensional row direction \([a]\), at least one column lies in its perpendicular projective direction. Those perpendiculars are the \(q+1\) points of \(\mathrm{PG}(1,q)\). Four columns can cover all of them only when \(q=3\), in which case the four projective points each occur once. There are \(4!\cdot(q-1)^4\) ordered choices of the columns, and \(|\mathrm{GL}_2(3)|=(3^2-1)(3^2-3)=48\) ordered bases of each two-dimensional code. Therefore there are exactly \(4!\cdot2^4/48=8\) such subspaces on four specified coordinates. In each, every nonzero word has exactly one zero coordinate, so all eight are valid. These are the usual ternary tetracode, with coordinate ordering and scalings accounted for.

**Step 4 (rank-by-support census on at most three coordinates).** If \(s\le3\), every subspace automatically has diameter at most three. With specified exact support: rank one contributes \((q-1)^{s-1}\) for \(s=1,2,3\); rank two contributes one subspace for \(s=2\), and \(q^2+q-2\) for \(s=3\), since there are \(q^2+q+1\) planes (hyperplanes) in \(\mathbb F_q^3\) and the three coordinate planes are not full-support; rank three contributes only the full \(\mathbb F_q^3\) on three coordinates. Together with the single zero subspace and Step 3 this yields every coefficient of \(E_{q,n}\) after choosing its \(s\) labelled support positions in \(\binom ns\) ways. The displayed total and asymptotic-degree statements follow by setting \(u=v=1\). No unclassified rank or support remains.

## Verification

Run `python3 verify.py` using Python's standard library. The verifier generates all reduced row-echelon row spaces of dimensions at most three over \(\mathbb F_3\), \(\mathbb F_4\), \(\mathbb F_5\) and \(\mathbb F_7\), independently checks word weights and exact support/rank counts, and compares them with the claimed polynomial for ambient lengths zero through five for \(q=3\) and zero through four for the other tested fields. It implements \(\mathbb F_4\) using the polynomial \(X^2+X+1\). The terminal marker is `VERIFY_OK`. The rank bound in the proof, not the finite tests, rules out dimensions above three; the classification proof, not extrapolation, covers arbitrary \(q,n\).

For illustration, the total counts for \(n=4\) are \(91\) at \(q=3\), \(141\) at \(q=4\), \(215\) at \(q=5\), and \(411\) at \(q=7\). At \(q=3,n=5\), the count is \(226\), including \(40\) rank-two codes with support four.

## Relationship to prior work

Horlemann and Ravi [1], Proposition 4.3, express the number of linear fixed-diameter anticodes as a polynomial in ambient length with coefficients given by full-support counts; Theorem 4.6 bounds the degree but does not evaluate the coefficients here. The present result evaluates **all** full-support rank counts for diameter three and \(q\ge3\), including the exact labelled multiplicity of ternary support-four codes. Moreover, the four-support existence and hence the ternary degree four already follow from the simplex construction in Remark 4.8 of [1] combined with its support bound; these consequences are not claimed as independent discoveries. Zhang et al. [2] prove an antiGriesmer support bound, which already excludes support four when \(q\ge4\) for a rank-two code, but does not enumerate all admissible subspaces. The ternary tetracode itself is classical; the claim is the exact labelled multiplicity within this complete anticode polynomial, not discovery of that code or its equivalence class. Equivalent enumerations under other coding-theoretic terminology may exist; no definitive priority assertion is made.

## Limitations

The theorem is restricted to linear codes, fields with at least three elements, and diameter at most three. The verifier only exhausts stated small parameters; it is not an infinite certificate. The proof supplies the infinite conclusion. Historical priority requires further external assessment, especially across older enumerations of small maximum-weight linear codes. Independent verification or audit has not been performed.

## References

[1] Anna-Lena Horlemann and Ananthakrishnan Ravi, *The Asymptotic Number of Anticodes in Hamming Spaces*, arXiv:2610.31618v1 (first posted 2026-10-22), https://arxiv.org/html/2610.31618v1 . Relevant sections: Proposition 4.3, Theorem 4.6 and Remarks 4.7–4.8.

[2] Guanghui Zhang, Bocong Chen, Liren Lin, and Hongwei Liu, *Improved AntiGriesmer Bounds for Linear Anticodes and Applications*, arXiv:2511.02519v1 (first posted 2025-11-04), https://arxiv.org/html/2511.02519 . Relevant material: Theorem 1.1, its proof in Section 3, and Section 4.
