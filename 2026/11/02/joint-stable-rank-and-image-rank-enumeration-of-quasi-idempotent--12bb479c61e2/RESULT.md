# Joint stable-rank and image-rank enumeration of quasi-idempotents on a finite chain

## Finding

For every integer \(n\ge 1\), let \(\mathcal O_n\) consist of *all* order-preserving (nondecreasing) self-maps of the labeled chain \([n]=\{1,\ldots,n\}\), including the identity. For \(f\in\mathcal O_n\) with \(f^3=f^2\), write \(k=|\operatorname{im}f^2|\) and \(r=|\operatorname{im}f|\). Then, for all integers \(1\le k\le r\le n\),

\[
\#\{f\in\mathcal O_n:f^3=f^2,\ |\operatorname{im}f^2|=k,\ |\operatorname{im}f|=r\}
=\binom{k+r-1}{r-k}\binom{n+k-1}{2r-1}.
\]

As usual, a binomial coefficient is zero when its lower index lies outside the range from zero to its upper index. The genuine (non-idempotent) quasi-idempotents \(f\ne f^2=f^4\) are *exactly* the terms \(r>k\). Thus the displayed formula gives their complete joint stable-image/image-rank distribution, with every idempotent on the diagonal \(r=k\).

With \(\mathcal O_0\) containing one empty map, the complete ordinary generating function is

\[
\begin{aligned}
F(z;u,v)&=\sum_{n\ge0}\,z^n\sum_{\substack{f\in\mathcal O_n\\f^3=f^2}}
 u^{|\operatorname{im}f^2|}v^{|\operatorname{im}f|}\\
 &=\frac{1}{1-uvz\left(\frac{1-z}{(1-z)^2-vz^2}\right)^2}.
\end{aligned}
\]

Subtracting the idempotent polynomial yields the complete strict quasi-idempotent enumerator:

\[
F(z;u,v)-\frac1{1-uvz/(1-z)^2}.
\]

In particular, setting \(u=v=1\) gives

\[
F(z;1,1)=\frac{(1-2z)^2}{1-5z+6z^2-z^3},
\]

whose coefficients for positive lengths \(n=1,\ldots,10\) are \(1,3,10,33,108,352,1145,3721,12087,39254\). The corresponding strictly quasi-idempotent counts are \(0,0,2,12,53,208,768,2734,9503,32489\).

## Assumptions and scope

The order is the standard linear order on \([n]\). Maps are total, order-preserving, and labeled; no quotient by conjugacy or isomorphism is taken. Multiplication is ordinary composition; iterated powers are unambiguous. The variables \(z,u,v\) are formal variables, and the displayed rational functions are interpreted as formal series at \(z=0\). All assertions hold for every \(n\ge1\), without a field or characteristic hypothesis.

A map satisfying \(f^4=f^2\) on a finite chain automatically satisfies \(f^3=f^2\): a nondecreasing self-map has no cycles of length greater than one, and \(f^4=f^2\) forces each point of \(\operatorname{im}(f^2)\) to lie on a cycle of period at most two. Every such point must therefore be fixed. Conversely \(f^3=f^2\) implies \(f^4=f^2\). The additional inequality \(f\ne f^2\) is exactly the strict inequality of ranks \(r>k\), since the image of \(f^2\) is a subset of the image of \(f\), and equality of their sizes forces \(f\) to be idempotent in this setting.

## Proof

**1. Rooted-interval decomposition.** Let \(f^3=f^2\) and \(e=f^2\). Then \(e\) is an order-preserving idempotent. Moreover, \(f\) fixes every point of \(\operatorname{im}e\). Each fiber \(I_a=e^{-1}(\{a\})\) is a contiguous interval containing its unique fixed point \(a\). Because \(ef=fe\) and \(f(a)=a\), \(f\) maps \(I_a\) into itself. The monotonicity of \(f\) ensures that points below \(a\) remain at or below \(a\), and points above \(a\) remain at or above \(a\). Each side evolves toward \(a\) in at most two applications.

Conversely, take an ordered sequence of nonempty intervals partitioning \([n]\). Choose one root in each interval. On each left and right side choose an order-preserving map fixing the root and whose square collapses that side to the root. Assemble these maps and fix each root. Adjacent intervals are mapped within themselves, so the assembled map is order-preserving, and its square is the prescribed idempotent retraction onto the roots. The construction is inverse to the preceding decomposition. There are \(k\) intervals if and only if \(\operatorname{rank}(f^2)=k\).

**2. One-sided lemma.** Reflecting a side if necessary, identify its root and its \(a\) other points with \(\{0,1,\ldots,a\}\), with root zero. Let \(g\) be nondecreasing with \(g(0)=0\) and \(g^2\equiv0\). Let \(j\) count distinct nonzero values in the image of \(g\). Then

\[
\#\{g:\text{side length }a,\ j\text{ positive image values}\}=\binom{a}{2j}.
\]

Indeed, the unique map for \(j=0\) is the zero map. If \(j\ge1\), put \(t=g(a)\). The condition \(g^2(a)=0\) and monotonicity imply \(g(i)=0\) for every \(0\le i\le t\). The remaining \(a-t\) values are nondecreasing from the alphabet \(\{0,\ldots,t\}\), end in \(t\), and use exactly \(j\) distinct positive values. Choose the \(j-1\) positive values other than \(t\) in \(\binom{t-1}{j-1}\) ways; distribute the \(a-t\) positions into possibly-empty zero-run followed by \(j\) nonempty positive runs in \(\binom{a-t}{j}\) ways. Summation over \(j\le t\le a-j\) gives the Vandermonde identity

\[
\sum_{t=j}^{a-j}\binom{t-1}{j-1}\binom{a-t}{j}=\binom{a}{2j}.
\]

Therefore the side generating function, marking length by \(z\) and the number of nonzero image values by \(v\), is

\[
L(z,v)=\sum_{a,j\ge0}\binom{a}{2j}z^av^j
=\frac{1-z}{(1-z)^2-vz^2}.
\]

**3. Concatenating blocks.** A rooted interval contributes one root to both image ranks, one position, and two independent sides. Thus its weight is \(uvzL(z,v)^2\). The rooted intervals occur in a linearly ordered sequence, so the generating function is the geometric series

\[
F(z;u,v)=\sum_{k\ge0}(uvzL(z,v)^2)^k.
\]

Put \(j=r-k\). Expanding the \(k\)-block term gives

\[
(uvz)^kL(z,v)^{2k}
=(uvz)^k(1-z)^{-2k}\sum_{j\ge0}\binom{2k+j-1}{j}
 v^jz^{2j}(1-z)^{-2j}.
\]

Taking the coefficient of \(z^nu^kv^r\), the first factor becomes \(\binom{k+r-1}{r-k}\); the remaining factor is

\[
[z^{n-k-2(r-k)}](1-z)^{-2r}
=\binom{n+k-1}{2r-1}.
\]

This proves the stated exact formula. When \(j=0\), every side is the zero map, hence \(f=e\) and the idempotent generating function is \(\left(1-uvz/(1-z)^2\right)^{-1}\), proving the strict-difference formula.

## Verification

Run `python3 verify.py` with the Python standard library. The program independently enumerates all nondecreasing self-maps on \([n]\) for \(1\le n\le10\), computes composition powers and both image ranks directly, checks that \(f^4=f^2\) and \(f^3=f^2\) select the same maps, and compares every joint-rank cell to the closed formula. It also directly enumerates the one-sided maps up to side length nine and checks the one-sided binomial lemma. The executable ends with `VERIFY_OK`.

The direct census at \(n=5\) gives 108 square-idempotent maps, 55 idempotents, and **53** strict quasi-idempotents. The finite checks are corroboration, not a substitute for the proof for arbitrary \(n\).

## Relationship to prior work

Imam, Ibrahim, Garba, Usman and Idris (2023) establish the characterization of strict quasi-idempotents of order-preserving transformations by stationary and nonstationary blocks, and study generating sets. Their Theorem 1 and surrounding results supply the motivating semigroup objects; their generating-set results are not claimed anew. The exact joint stable-image/image-rank distribution and its rational three-variable generating function are not stated there.

Eze, Olaiya, Pokalas Tal and Kasim (2025) analyze stable quasi-idempotents and tabulate finite counts, with a cubic interpolation only for four small parameters. Their table reports 52 strict quasi-idempotents at \(n=5\); direct enumeration and the formula above instead give 53. Their other displayed values through \(n=10\) agree with this theorem. The difference is precisely one finite-table cell, not a claim that the rest of that work is invalid.

OEIS A060557 already records the univariate sequence \(1,3,10,33,108,\ldots\) and its rational generating function, but with a shifted index and a different combinatorial description. The univariate integer sequence itself is therefore not claimed as a newly discovered sequence. OEIS A060556 supplies a separate triangle summing to A060557, which is not the two-rank table above. Idempotent counts and their classical Fibonacci pattern are also prior results.

## Limitations

The formula concerns only *total nondecreasing* self-maps and the precise power condition \(f^3=f^2\) (equivalently \(f^4=f^2\) on a chain). It does not enumerate partial transformations, arbitrary transformations, maps requiring more than two iterates to stabilize, or semigroup generating sets. The exact joint-rank identity is proved; the finite exhaustive census does not constitute an infinite certificate. A broader unlocated enumeration result could still imply the formula, so publication priority remains provisional. No independent audit has been performed.

## References

1. A. T. Imam, S. Ibrahim, G. U. Garba, L. Usman, A. Idris, *Quasi-idempotents in finite semigroup of full order-preserving transformations*, Algebra and Discrete Mathematics 35 (2023), 62–72; DOI 10.12958/adm1846; https://admjournal.luguniv.edu.ua/index.php/adm/article/download/1846/pdf . Author-uploaded complete text dated 2023-06-19.
2. C. Eze, O. O. Olaiya, P. Pokalas Tal, S. Kasim, *Graph-Theoretic and Algebraic Characterization of Stable Quasi-Idempotents in Full Order-Preserving Transformation Semigroups*, Journal of Mathematics and Artificial Intelligence 1(2) (2025), 58–66; https://www.researchgate.net/publication/395110201_Graph-Theoretic_and_Algebraic_Characterization_of_Stable_Quasi-Idempotents_in_Full_Order-Preserving_Transformation_Semigroups .
3. OEIS A060557, https://oeis.org/A060557 ; OEIS A060556, https://oeis.org/A060556 .
4. OEIS A144224, idempotent order-preserving full transformations, https://oeis.org/A144224 .
