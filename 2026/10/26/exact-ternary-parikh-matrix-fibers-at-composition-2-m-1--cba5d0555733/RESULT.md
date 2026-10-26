# Exact ternary Parikh-matrix fibers at composition \((2,m,1)\)

## Finding

Fix an integer \(m\ge0\). Over the ordered ternary alphabet \(a<b<c\), let \(\mathcal L_m\) be the collection of all words having exactly two \(a\)'s, \(m\) \(b\)'s, and one \(c\). For any word \(w\), let \(|w|_u\) count occurrences of \(u\) as a **scattered subsequence**, with distinct choices of positions counted separately. The Parikh matrix of \(w\in\mathcal L_m\) is completely determined by the triple
\[
(\alpha,\beta,\gamma)=\bigl(|w|_{ab},|w|_{bc},|w|_{abc}\bigr).
\]

For integers \(B\ge0\) and \(t\in\mathbb Z\), define
\[
T_B(t)=\begin{cases}
\lfloor t/2\rfloor-\max\{0,t-B\}+1,&0\le t\le2B,\\
0,&\text{otherwise}.
\end{cases}
\]
For every integer triple \((\alpha,\beta,\gamma)\), the **exact number** \(F_m(\alpha,\beta,\gamma)\) of words in \(\mathcal L_m\) with this Parikh matrix is zero if \(\beta\notin\{0,\ldots,m\}\). Otherwise, writing \(h=m-\beta\), it is
\[
\boxed{F_m(\alpha,\beta,\gamma)
=\mathbf 1_{\gamma=0}T_h(\alpha)
+\mathbf 1_{0\le\gamma\le\beta}\,\mathbf 1_{h+\gamma\le\alpha\le2h+\gamma}
+\mathbf 1_{\alpha=\gamma+2h}T_\beta(\gamma).}
\]
Here \(\mathbf 1\) denotes the indicator of a stated condition. All triples outside these supports have zero multiplicity.

Consequently the number of *distinct* Parikh matrices realized in \(\mathcal L_m\), equivalently the maximum size of a code that can reconstruct a source in this slice without error from its Parikh matrix, is
\[
\boxed{N_m=\frac{(m+1)(m^2+11m+6)}6.}
\]
The **largest** ambiguity class has size
\[
\boxed{M_m=\max\left\{3,\left\lfloor\frac m2\right\rfloor+2\right\}.}
\]
The average preimage count per realized matrix tends to \(3\) as \(m\to\infty\), while the maximum grows linearly in \(m\).

## Assumptions and scope

The alphabet order \(a<b<c\) is fixed and is part of the measurement. A Parikh matrix here uses all scattered counts for consecutive blocks of that ordered alphabet. For the present fixed composition, the letter counts and the entries indexed by \(ab\), \(bc\), and \(abc\) are the only independent entries. Distinct words are distinguished by positions of the symbols, not by algebraic renaming. All formulas are for **every integer** \(m\ge0\), including the boundary case \(m=0\); the size of the alphabet is three even when a particular letter has zero occurrences.

## Proof

**Parikh-matrix reduction.** By the defining triangular matrix product, for a ternary ordered alphabet the first superdiagonal consists of \(|w|_a,|w|_b,|w|_c\), the next superdiagonal is \(|w|_{ab},|w|_{bc}\), and the final upper-right entry is \(|w|_{abc}\). The fixed composition therefore leaves exactly the triple in the finding as the independent signature. Let \(\beta=|w|_{bc}\). Because there is exactly one \(c\), \(\beta\) is the number of \(b\)'s *preceding* \(c\), and hence \(0\le\beta\le m\). Put \(h=m-\beta\), the number of \(b\)'s following \(c\).

**Three exhaustive letter skeletons.** On deleting all \(b\)'s, exactly one of the ordered skeletons \(caa\), \(aca\), or \(aac\) remains. They are mutually disjoint as word sets. Each of their \(b\)-gap parametrizations is unique, as follows; all gap variables are nonnegative integers.

1. In the \(caa\) skeleton a word has the form \(b^\beta c\,b^u a\,b^v a\,b^z\), with \(u+v+z=h\). Its third signature coordinate is \(\gamma=0\), while \(\alpha=v+2z\). Thus, for a specified \(\alpha\), valid \(z\) satisfy \(\max(0,\alpha-h)\le z\le\lfloor\alpha/2\rfloor\). This interval contains exactly \(T_h(\alpha)\) integers.

2. In the \(aca\) skeleton a word has the form \(b^p a\,b^\gamma c\,b^u a\,b^z\), with \(p+\gamma=\beta\) and \(u+z=h\). The count of \(abc\) is exactly \(\gamma\): only the first \(a\) precedes \(c\). Moreover \(\alpha=\gamma+u+2z=\gamma+h+z\). There is exactly one word for this signature when \(0\le\gamma\le\beta\) and \(h+\gamma\le\alpha\le2h+\gamma\), and no word otherwise.

3. In the \(aac\) skeleton a word has the form \(b^p a\,b^v a\,b^z c\,b^h\), with \(p+v+z=\beta\). Since both \(a\)'s precede \(c\), \(\gamma=v+2z\); since all \(h\) later \(b\)'s follow both \(a\)'s, \(\alpha=\gamma+2h\). The number of valid gap triples is therefore exactly \(T_\beta(\gamma)\).

Adding the three disjoint skeleton contributions proves the complete displayed fiber formula, including its boundary cases. No other words exist because deleting \(b\)'s always gives one of the three skeletons.

**Image cardinality.** Fix \(\beta\in\{0,\ldots,m\}\), so \(h=m-\beta\). In the coordinate plane \((\alpha,\gamma)\), the signature supports of the three skeletons, denoted \(C,A,D\) in skeleton order, have sizes
\[
|C|=2h+1,\qquad |A|=(\beta+1)(h+1),\qquad |D|=2\beta+1.
\]
Their intersections have sizes
\[
|C\cap A|=h+1,\quad |A\cap D|=\beta+1,\quad
|C\cap D|=1,\quad |C\cap A\cap D|=1.
\]
Indeed \(C\) fixes \(\gamma=0\) with \(0\le\alpha\le2h\); \(D\) fixes \(\alpha=\gamma+2h\) with \(0\le\gamma\le2\beta\); and \(A\) requires \(0\le\gamma\le\beta\) with \(\gamma+h\le\alpha\le\gamma+2h\). These inequalities immediately give the four intersections, even for \(\beta=0\) or \(h=0\). Inclusion–exclusion gives precisely
\[
|C\cup A\cup D|=\beta h+2m+1.
\]
Distinct values of \(\beta\) cannot share a Parikh matrix. Therefore
\[
N_m=\sum_{\beta=0}^m\bigl(\beta(m-\beta)+2m+1\bigr)
=\frac{m(m+1)(m-1)}6+(m+1)(2m+1)
=\frac{(m+1)(m^2+11m+6)}6.
\]
For each signature, choose one representative word to attain a zero-error code of this size. Two representatives sharing the same signature cannot be distinguished, establishing optimality.

**Largest fiber.** For all integer \(B\ge0\), \(T_B(t)\le\lfloor B/2\rfloor+1\), directly from the interval counting expression; the bound is attained at \(t=B\). The \(C\) and \(D\) signature supports intersect at exactly the point \((\alpha,\gamma)=(2h,0)\). At that point both triangular contributions are \(1\) and the \(A\) contribution is \(1\), making a three-word fiber. At every other point at most one triangular contribution is positive; the remaining \(A\) contribution is at most \(1\). Thus all fibers have size at most \(\max\{3,\lfloor m/2\rfloor+2\}\). The three-word fiber exists for **every** \(\beta\). For \(m\ge2\), take \(\beta=0,\gamma=0,\alpha=m\): here \(h=m\), the \(C\) contribution is \(\lfloor m/2\rfloor+1\), the \(A\) contribution is \(1\), and the \(D\) contribution vanishes; hence the second bound is attained. The formula for the maximum holds also at \(m=0,1\) by the three-word fiber.

**Mean occupancy.** The number of words in \(\mathcal L_m\) is \((m+3)!/(2!m!)=(m+1)(m+2)(m+3)/2\), by placement of the two identical \(a\)'s and the unique \(c\). Dividing by \(N_m\) gives
\[
\frac{|\mathcal L_m|}{N_m}=\frac{3(m+2)(m+3)}{m^2+11m+6}\longrightarrow3.
\]
This mean is over the set of **realized Parikh matrices**, each counted once; it is not the expected fiber size for a uniformly sampled *word*.

## Verification

The standalone file `check.py` generates every word of composition \((2,m,1)\) for \(0\le m\le35\), independently computes all three scattered-subsequence counts, groups equal signatures, and checks the explicit fiber formula for every realized signature, all predicted signature supports, the total image count, total word count, and largest fiber. Its exact integer arithmetic covers \(246{,}753\) words. Run `python3 check.py` to reproduce. The finite enumeration is corroborating evidence only; the preceding proof is uniform in \(m\).

## Relationship to prior work

The classical Parikh matrix mapping and its use to classify \(M\)-equivalent words were developed before this work. Teh's 2015 paper *Parikh matrices and Parikh Rewriting Systems* defines the map precisely and studies transformation/rewrite descriptions of \(M\)-equivalence for ternary alphabets; its Section 2 provides the matrix-entry identity used here, and later sections address rewriting rules rather than the exact fiber spectrum of the specified composition slice. The exact formula above concerns a different kind of information: **fiber cardinality** for every signature, the total image size, and the largest fiber as \(m\) varies. Teh's later work on \(M\)-unambiguity and Hahn–Cheon–Han's ternary unambiguity characterization concern singleton fibers, which do not by themselves imply the full multiplicity law. The latter full conference paper was not accessible for complete textual comparison; its available description concerns singleton classification.

## Limitations

No claim is made for arbitrary ternary compositions, for strong \(M\)-equivalence, or for reconstruction from contiguous factors rather than scattered subsequences. The result uses the fixed letter order \(a<b<c\). The literature comparison is not a proof of historical priority: an unindexed exact enumeration or an algebraically equivalent earlier formula may exist, and the full 2023 ternary-unambiguity conference paper was not accessible. The proof establishes the all-length formulas independently of finite enumeration; the checker covers only the stated finite range. No independent mathematical audit is reported here.

## References

1. Wen Chean Teh, *Parikh matrices and Parikh Rewriting Systems*, arXiv:1506.06476, first posted 22 June 2015, https://arxiv.org/abs/1506.06476 . See Sections 2 and 7 for matrix entries and ternary rewriting systems.
2. Wen Chean Teh, *On M-unambiguity of Parikh matrices*, 2020. The treatment of singleton classes provides context but not the complete slice-fiber formula.
3. H. Hahn, G. Cheon, and Y. Han, *M-equivalence of Parikh Matrix over a Ternary Alphabet*, 2023, DOI: 10.1007/978-3-031-40247-0_10 . Its accessible abstract discusses characterization of unambiguous words; full text was not available for examination.
