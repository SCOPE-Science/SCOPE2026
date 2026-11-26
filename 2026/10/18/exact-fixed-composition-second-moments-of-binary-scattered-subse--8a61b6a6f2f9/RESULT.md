# Exact fixed-composition second moments of binary scattered-subsequence diversity

## Finding

For a finite binary word \(w\), let \(D(w)\) be its number of distinct scattered subsequence **words**, including the empty word once. For \(a,b\ge0\), let \(U_{a,b}\) and \(V_{a,b}\) be the sums of \(D(w)\) and \(D(w)^2\), respectively, over words with \(a\) zeros and \(b\) ones. Put \(s=x+y\), \(t=1-s\), and
\[
\begin{aligned}
Q&=t^2-xy,\\
K&=1-3s+3(x^2+y^2)+xy-x^3-y^3,\\
P&=1-s-x^2-y^2+x^3+y^3+5xy-2x^2y-2xy^2.
\end{aligned}
\]
The composition-resolved second-moment series is
\[
\boxed{\sum_{a,b\ge0}V_{a,b}x^ay^b=\frac{(1-x)(1-y)P}{tQK}.}
\]
In particular, for \(X_{a,b}\) uniform among the \(M=\binom{a+b}{a}\) words with that composition, write \(F_2=(1-x)(1-y)P/(tQK)\) and \(F_1=(1-x)(1-y)/(tQ)\). Then
\[
\operatorname{Var}(D(X_{a,b}))=\frac{[x^ay^b]F_2}{M}-\left(\frac{[x^ay^b]F_1}{M}\right)^2.
\]
Here \(F_1=\sum U_{a,b}x^ay^b\) is the first-moment series, included for use in the formula, not as a distinct research claim. The fair independent-letter second moment and variance are also prior consequences, as explained below. The contribution is the evaluated second-moment series retaining both composition weights.

## Assumptions and scope

A scattered subsequence preserves relative order, allows omitted positions, and is counted as a word, not as an embedding. Both weights are formal variables, and all inverses have unit denominators in \(\mathbb Q[[x,y]]\). The fixed-composition law does not mix compositions. The formulas include \((a,b)=(0,0)\) and the constant-word cases.

## Proof

Let \(i(w)\) be one plus the number of nonempty subsequence words ending in zero, and let \(j(w)\) be its analogue for one. The set of words ending in an appended zero is exactly the old set of all subsequences with zero appended to each: an existing word ending in zero can use the new zero in place of its last letter, and the construction is injective. The words ending in one are unchanged. Thus appending zero maps \((i,j)\) to \((i+j,j)\), and appending one maps it to \((i,i+j)\). The initial pair is \((1,1)\) and \(D=i+j-1\).

In the following sums each word has weight \(x^{|w|_0}y^{|w|_1}\). Write \(I,J\) for the weighted sums of \(i,j\), and \(A,B,C\) for those of \(i^2,j^2,ij\). Splitting by the last letter gives
\[
\begin{pmatrix}t&-x\\-y&t\end{pmatrix}\binom{I}{J}=\binom{1}{1},
\qquad
\begin{pmatrix}t&-x&-2x\\-y&t&-2y\\-y&-x&t\end{pmatrix}
\begin{pmatrix}A\\B\\C\end{pmatrix}=\begin{pmatrix}1\\1\\1\end{pmatrix}.
\]
The determinants are \(Q\) and \(t^3-5txy-2sxy=K\). The first system gives \(I=(1-y)/Q\), \(J=(1-x)/Q\). The adjugate of the second matrix applied to the right-hand side gives
\[
K(A,B,C)=\big((1-y)(1+x-y),\ (1-x)(1+y-x),\ (1-x)(1-y)\big).
\]
The total weight is \(1/t\), so \(F_1=I+J-1/t\) and
\[
F_2=A+B+2C-2(I+J)+1/t
=\frac{4-3s+x^2+y^2}{K}-\frac{2(2-s)}{Q}+\frac1t.
\]
Combining the fractions gives the stated numerator \((1-x)(1-y)P\). Division by the exact count \(M\) gives the two normalized moments and therefore the variance. At \(y=0\), for example, the two series reduce to \(1/(1-x)^2\) and \((1+x)/(1-x)^3\), as required for the single constant word with \(D=a+1\) in each length. Symmetry gives the other axis.

## Prior exact results and relationship to the weighted claim

Collins gives the fair iid mean \(2(3/2)^n-1\) [1]. Biers-Ariel, Godbole and Kelley give the mean for every fixed bias [2]. After including the empty word, the known biased mean is the specialization \([z^n]F_1(pz,(1-p)z)\) at zero probability \(p\). Its polynomial for each \(n\) determines the fixed-composition first moments, since the functions \(p^a(1-p)^{n-a}\) for \(0\le a\le n\) are linearly independent. The shifted two-counter update is also familiar from the subsequence-counting and Euclidean-algorithm description in Żak [3, Theorem 1 and its proof].

The fair iid second moment is a consequence of Stanley's unweighted Stern-array square sums [4, equation (3)]. To see the relation precisely, let \(d(0)=0,d(1)=1\) be Stern's diatomic sequence, with \(d(2m)=d(m)\) and \(d(2m+1)=d(m)+d(m+1)\). If \(m\) is the integer whose binary expansion is a leading one followed by the bitwise complement of \(w\), the two-counter update gives \((i,j)=(d(m),d(m+1))\). Consequently \(D(w)+1=d(2m+1)\).

Let \(r_n\) denote Stanley's sum of squares of all coefficients of \(\prod_{j=0}^{n-1}(1+u^{2^j}+u^{2^{j+1}})\). The coefficient at degree \(k<2^n\) is \(d(k+1)\), by the hyperbinary recurrence; the other coefficients reflect by symmetry and \(d(2^n)=1\). Thus \(r_n=1+2\sum_{k=1}^{2^n-1}d(k)^2\). Set \(H_n=(r_{n+1}-r_n)/2\), the sum of squares on \([2^n,2^{n+1})\). By removing the even entries of the next interval, the sum of \((D(w)+1)^2\) over length-\(n\) words is \(H_{n+1}-H_n\). Stanley's recurrence \(r_{n+2}=5r_{n+1}-2r_n\) therefore makes these shifted sums obey the same recurrence, with initial values \(4,18\).

Dividing by \(2^n\) gives the ordinary generating function \((4-z)/(1-5z/2+z^2/2)\) for the shifted square expectation of a length-\(n\) fair iid word \(X_n\). Solving this recurrence and subtracting the square of the shifted mean gives, with \(\lambda_\pm=(5\pm\sqrt{17})/4\),
\[
\operatorname{Var}(D(X_n))=\left(2+\frac8{\sqrt{17}}\right)\lambda_+^n+
\left(2-\frac8{\sqrt{17}}\right)\lambda_-^n-4(9/4)^n.
\]
This unweighted specialization does not resolve the individual composition coefficients: in the Stern representation the weights refine by the number of ones among the nonleading bits of \(m\) (or equivalently the number of zeros in \(w\)). An all-length fair-source joint deletion-ball result [5] also recovers the fair iid specialization by summing over deletion radii; its marks are radii, not letter composition. The weighted second-moment evaluation quantifies within-composition fluctuations rather than fluctuations under the random mixture of compositions. Equivalently it gives the total-diversity second moment as a polynomial in the bias for every length via \(F_2(pz,(1-p)z)\).

## Reproducibility and limitations

The two small linear systems, their adjugates, and the final fraction combination are exact identities. The accompanying `verify.py` checks the same rational functions through equivalent unshifted state polynomial identities and bounded coefficient comparisons. The symbolic identities, not the bounded comparisons, justify all nonnegative compositions. The result does not address the full distribution, general alphabets or a non-independent source. The comparisons above do not establish universal literature completeness.

## References

1. M. J. Collins, *The Number of Distinct Subsequences of a Random Binary String*, arXiv:1310.7288, Theorem 3.
2. Y. Biers-Ariel, A. Godbole and E. Kelley, *Expected Number of Distinct Subsequences in Randomly Generated Binary Strings*, DMTCS 19(2), paper 10 (2018), Theorem 2.9, DOI: 10.23638/DMTCS-19-2-10.
3. R. Żak, *Finding binary words with a given number of subsequences*, Theor. Comput. Sci. 921 (2022), DOI: 10.1016/j.tcs.2022.03.032; arXiv:2210.00342.
4. R. P. Stanley, *Some linear recurrences motivated by Stern's Diatomic Array*, Amer. Math. Monthly 127 (2020), 99–111; arXiv:1901.04647.
5. *Exact joint second moments of binary deletion-ball sizes at all deletion radii*, Resultary, 2026-11-02, record `4ce40b9cbccc`.
