# Exact real and complex Fourier uncertainty on the dihedral group of order eight

## Finding
Let \(D_8=\langle r,s\mid r^4=s^2=e,\;srs=r^{-1}\rangle\). For \(\mathbb F\in\{\mathbb R,\mathbb C\}\) and \(1\le k\le8\), define
\[
\Theta_{\mathbb F}(k)=\min_{\substack{f:D_8\to\mathbb F\\|\operatorname{supp}f|=k}}
\sum_{\pi\in\widehat{D_8}}(\dim\pi)\operatorname{rank}_{\mathbb C}\!\left(\sum_{g\in D_8}f(g)\pi(g)\right).
\]
The exact profiles, in order \(k=1,\ldots,8\), are
\[
\boxed{\Theta_{\mathbb C}=(8,4,4,2,4,2,3,1)},\qquad
\boxed{\Theta_{\mathbb R}=(8,4,6,2,4,2,3,1)}.
\]
Thus the fields differ only at exact support size three. The complex five-support value jumps to four between values two at supports four and six. In particular these are **exact-support**, not at-most-support, minima.

## Assumptions and scope
The function has precisely \(k\) nonzero coefficients in \(\mathbb F\); no positivity, unit-modulus, or subgroup-support assumption is imposed. The representation dimensions are four copies of one and one copy of two. Fourier matrices are unnormalized sums; multiplying them by any nonzero normalizing constants does not change ranks. All ranks are over \(\mathbb C\), including for real-valued functions. The group is the order-eight symmetry group of a square (some authors call it \(D_4\)); it is not the quaternion group or the cyclic group of order eight.

Write
\[
f=\sum_{j=0}^{3}a_j\delta_{r^j}+\sum_{j=0}^{3}b_j\delta_{sr^j}.
\]
The four one-dimensional Fourier values are
\[
\ell_{u,v}=\sum_{j=0}^3u^j(a_j+vb_j),\quad u,v\in\{1,-1\}.
\]
Set \(x=a_0-a_2\), \(y=a_1-a_3\), \(z=b_0-b_2\), \(w=b_1-b_3\). In the two-dimensional irreducible representation, take \(\pi(r)=\operatorname{diag}(i,-i)\) and \(\pi(s)=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\). Its Fourier matrix is
\[
M=\begin{pmatrix}x+iy&z-iw\\z+iw&x-iy\end{pmatrix},\qquad
\det M=x^2+y^2-z^2-w^2.
\]
Hence \(\sigma(f)=\#\{(u,v):\ell_{u,v}\ne0\}+2\operatorname{rank}M\). For real \(f\), \(x,y,z,w\) are real; for complex \(f\), the displayed squares are algebraic squares, not absolute squares.

## Proof
**General lower bounds and even-support sectors.** The finite-group Fourier uncertainty inequality gives \(k\sigma(f)\ge8\) for each nonzero \(f\) [1]. Every one-dimensional character is trivial on the central half-turn \(r^2\), while \(\pi(r^2)=-I\). Therefore, if the two-dimensional block vanishes, \(f(g)=f(gr^2)\) and support is even; if all one-dimensional blocks vanish, \(f(g)=-f(gr^2)\) and support is even. A single nonzero one-dimensional block with zero two-dimensional block gives eight nonzero group coefficients. These observations and the uncertainty inequality supply the lower bounds at supports one, two, four, six, and eight, and rule out \(\sigma\le2\) at support seven.

**Three-point supports.** Left translations and automorphisms \(r\mapsto r^{\pm1}\), \(s\mapsto r^j s\) give exactly three orbits on unordered three-point subsets, represented by \(\{e,r,r^2\}\), \(\{e,r,s\}\), \(\{e,r^2,s\}\). Their orbit sizes are respectively \(8,32,16\), totaling \(\binom83=56\); this classification can also be checked directly by distinguishing same-coset triples from the two types of two-rotation/one-reflection triples.

For \(f=a\delta_e+b\delta_r+c\delta_{r^2}\) with \(abc\ne0\), the four scalar values consist of \(a+c+b\) twice and \(a+c-b\) twice, while \(\det M=(a-c)^2+b^2\). At least two scalars are nonzero. Over the reals \(\det M>0\), so \(\sigma\ge2+4=6\). Over the complexes \(M\) cannot vanish because \(b\ne0\), so \(\sigma\ge2+2=4\).

For \(f=a\delta_e+b\delta_r+c\delta_s\), the scalar values are \(a\pm b\pm c\). At most one can vanish if \(abc\ne0\). If one vanishes, writing \(c=\pm a\pm b\) gives \(a^2+b^2-c^2=\pm2ab\ne0\), and hence \(\sigma\ge3+4=7\). Otherwise all four scalars are nonzero and \(M\ne0\), giving \(\sigma\ge6\).

For \(f=a\delta_e+b\delta_{r^2}+c\delta_s\), the scalar values are \(a+b+c\) twice and \(a+b-c\) twice. If two vanish, \(c=\pm(a+b)\); meanwhile \(\det M=(a-b)^2-c^2\). Its vanishing in addition would force \(a=0\) or \(b=0\). Thus either the two-dimensional block has rank two and at least two scalars survive, or it has rank at least one and all four scalars survive: \(\sigma\ge6\). This proves the stated three-support lower bounds over both fields.

**The five-point obstruction.** Suppose \(|\operatorname{supp}f|=5\) and \(\sigma(f)\le3\). With either the scalar sector or the two-dimensional sector alone, support would be even; having one scalar block alone gives support eight. Thus precisely one scalar block is nonzero and \(\operatorname{rank}M=1\). Fourier inversion now shows that each pair \(\{g,gr^2\}\) has sum equal to \(+t\) or \(-t\) for a common \(t\ne0\): this follows because the two-dimensional sector cancels in pair sums and the sole one-dimensional character has values \(\pm1\). For the four pairs, denote the differences by \(x,y,z,w\) as above. In a singleton pair, its nonzero pair sum equals its difference up to sign, so that difference has square \(t^2\).

Five nonzero group coefficients would require exactly three singleton pairs and one doubleton pair. But \(\det M=0\) says \(x^2+y^2=z^2+w^2\). If any three of these four squares equal \(t^2\), the fourth does too. The remaining pair is then also a singleton, a contradiction. Therefore \(\sigma\ge4\) at support five over either field.

**Seven points.** A value \(\sigma\le2\) requires either at most two one-dimensional blocks and no two-dimensional block, or a rank-one two-dimensional block and no scalars. Both cases have even support (except the single-scalar case, which has support eight), so support seven requires \(\sigma\ge3\).

**Sharpness.** In the coefficient order \((a_0,a_1,a_2,a_3,b_0,b_1,b_2,b_3)\), the following explicit vectors attain the asserted values; \(i^2=-1\):

| Exact support | Complex witness (real also unless indicated) | \(\sigma\) |
|---|---|---|
| \(1\) | \((1,0,0,0,0,0,0,0)\) | \(8\) |
| \(2\) | \((1,0,1,0,0,0,0,0)\) | \(4\) |
| \(3\) | \((1+i,2,1-i,0,0,0,0,0)\) | \(4\) |
| \(4\) | \((1,1,1,1,0,0,0,0)\) | \(2\) |
| \(5\) | \((-1,1,-1,-1,2,0,0,0)\) | \(4\) |
| \(6\) | \((3,4,-3,-4,5,0,-5,0)\) | \(2\) |
| \(7\) | \((-2,-3,8,-3,-7,6,1,0)\) | \(3\) |
| \(8\) | \((1,1,1,1,1,1,1,1)\) | \(1\) |

For real support three, replace the complex witness by \((1,2,1,0,0,0,0,0)\), whose \(\sigma\) is \(6\). Direct substitution in the four scalar formulas and determinant/rank test verifies all nine upper-bound witnesses. Combining the lower bounds with the witnesses proves the profiles.

## Verification
Run `python3 checker.py` with Python 3 (standard library only). It checks the exact Gaussian-integer Fourier ranks for every listed witness over both fields, independently enumerates the three support-orbits and verifies they exhaust all \(56\) three-point subsets, and checks the four coefficientwise singleton-pair identities. These checks corroborate the analytic proof; no finite numerical sampling is used in place of its quantifier arguments.

## Relationship to prior work
Alagic and Russell [1] prove the finite-group rank-weighted uncertainty inequality and operator bounds, but do not tabulate exact-support minima for the dihedral group. Jiang, Liu and Wu [2] characterize equality in noncommutative uncertainty inequalities through subgroup-based constructions; this does not yield the non-equality minimum values at exact supports three, five or seven. Chen, Fan and Luo [3] give stronger general support-dependent inequalities and equality conditions, but their formulas do not directly supply the two exact coefficient-field profiles above. In particular, the displayed five-support exclusion of Fourier rank three is an additional algebraic parity obstruction. Existing cyclic and quaternion Fourier profiles concern different groups; the ordinary order-eight discrete Fourier transform is not the nonabelian transform used here.

## Limitations
Only the order-eight dihedral group and real/complex coefficient fields are covered. The theorem concerns rank-weighted Fourier support, not the number of nonzero irreducible blocks or the norms of those blocks. It classifies minimum *values*, not all minimizers. A general result implying the full table through an unrecognized reformulation remains a bibliographic possibility; the cited papers and accessible comparisons did not show such an implication.

## References
[1] G. Alagic and A. Russell, *Uncertainty Principles for Compact Groups*, arXiv:math/0608702, first version posted 2006-08-28, https://arxiv.org/abs/math/0608702.

[2] C. Jiang, Z. Liu and J. Wu, *Noncommutative Uncertainty Principles*, arXiv:1408.1165, first posted 2014-08-06, https://arxiv.org/abs/1408.1165.

[3] B. Chen, Y. Fan and G. Luo, *Sharp Uncertainty Principle for Transitive G-Sets over Arbitrary Fields and Finite Groups*, arXiv:2211.11204, https://arxiv.org/abs/2211.11204 (later general sharpening; version examined is v3 from 2025).
