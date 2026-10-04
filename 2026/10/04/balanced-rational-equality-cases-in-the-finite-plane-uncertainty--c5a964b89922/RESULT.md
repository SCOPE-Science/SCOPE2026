# Balanced rational equality cases in the finite-plane uncertainty bound
## Finding
Let \(p\ge 3\) be prime and let \(f:\mathbb F_p^2\to\mathbb Q\) be nonzero. Put
\[
S=\operatorname{supp}f,\qquad X=\operatorname{supp}\widehat f.
\]
Assume \(|S|=|X|\) and equality holds in the Biró--Lev finite-plane uncertainty inequality
\[
\frac{1}{p-1}\min\{|S|,|X|\}+\frac12\max\{|S|,|X|\}=p+1.
\]
Then
\[
|S|=|X|=2(p-1),
\]
and there exist two nonparallel affine lines \(\ell_1,\ell_2\subset\mathbb F_p^2\) and a scalar \(c\in\mathbb Q^\times\) such that
\[
f=c(1_{\ell_1}-1_{\ell_2}).
\]
Conversely, every such difference of nonparallel affine-line indicators is a balanced equality case. Hence, up to multiplication by a nonzero rational scalar, the number of balanced rational extremizers is exactly
\[
\binom{p+1}{2}p^2=\frac{p^3(p+1)}2.
\]

## Assumptions and scope
The Fourier transform is the ordinary character transform on the additive group \(\mathbb F_p^2\). The result concerns rational-valued functions and the balanced slice \(|S|=|X|\) of equality in the complex-valued Biró--Lev inequality. It does not classify unequal-support equality cases or arbitrary complex-valued balanced equality cases.

## Proof
Write \(|S|=|X|=n\). Equality gives
\[
n\left(\frac1{p-1}+\frac12\right)=p+1,
\]
so \(n=2(p-1)\).

Fix a primitive \(p\)-th root of unity \(\zeta\). Because \(f\) is rational-valued, every Fourier coefficient belongs to \(\mathbb Q(\zeta)\), and for every \(j\in\mathbb F_p^\times\) the Galois automorphism \(\zeta\mapsto\zeta^j\) sends \(\widehat f(\xi)\) to \(\widehat f(j\xi)\). Therefore \(X\setminus\{0\}\) is a union of punctured one-dimensional subspaces of the dual plane, each of cardinality \(p-1\).

The principal character cannot lie in \(X\): otherwise \(|X|-1=2p-3\) would be divisible by \(p-1\), which is impossible for \(p\ge3\). Thus \(X\) is the disjoint union of two punctured dual lines, say \(L_1\setminus\{0\}\) and \(L_2\setminus\{0\}\). They are distinct. After an invertible linear change of coordinates, take them to be the two coordinate frequency axes. Fourier inversion then has the form
\[
f(x,y)=U(x)+V(y),
\]
where \(U,V:\mathbb F_p\to\mathbb C\) are nonconstant. Since the zero frequency is absent, both functions have mean zero.

We use the following elementary multiplicity lemma. If \(U\) and \(V\) are nonconstant functions on a \(p\)-point set, then
\[
\#\{(x,y):U(x)+V(y)=0\}\le (p-1)^2+1.
\]
To prove it, let \(r_1\ge r_2\ge\cdots\) be the multiplicities of the values of \(U\), and let \(s_1\ge s_2\ge\cdots\) be the multiplicities of the negatives of the values of \(V\), aligned so as to maximize the matching sum. Rearrangement gives
\[
\#\{U+V=0\}\le\sum_i r_i s_i.
\]
For fixed \((s_i)\), the largest value over nonconstant \((r_i)\) with total mass \(p\) is at most
\[
(p-1)s_1+s_2.
\]
If \(s_1=p-1\), nonconstancy forces \(s_2=1\), giving \((p-1)^2+1\). If \(s_1\le p-2\), then \(s_2\le p-s_1\), so
\[
(p-1)s_1+s_2\le (p-2)s_1+p\le (p-2)^2+p<(p-1)^2+1.
\]
Equality in the lemma therefore occurs exactly when both value-multiplicity patterns are \((p-1,1)\), with their two values paired oppositely.

Our support hypothesis says that the zero set of \(f\) has size
\[
p^2-2(p-1)=(p-1)^2+1,
\]
so equality holds in the multiplicity lemma. Hence there are \(x_0,y_0\in\mathbb F_p\) and values \(a,a'\) such that
\[
U(x)=a\quad(x\ne x_0),\qquad U(x_0)=a',
\]
and
\[
V(y)=-a\quad(y\ne y_0),\qquad V(y_0)=-a'.
\]
Mean zero gives \((p-1)a+a'=0\). Thus \(f\) vanishes off the union of the two coordinate affine lines \(x=x_0\) and \(y=y_0\), also vanishes at their intersection, and takes opposite nonzero constant values on their punctured parts. Consequently
\[
f=c(1_{y=y_0}-1_{x=x_0})
\]
for some nonzero scalar \(c\). Since the original function is rational-valued, \(c\in\mathbb Q^\times\). Undoing the coordinate change gives two nonparallel affine lines.

Conversely, two nonparallel affine lines meet in exactly one point, so the difference of their indicators has support \(2(p-1)\). The Fourier transform of an affine-line indicator is supported on the orthogonal dual line, with a unit-modulus phase factor. The principal coefficients cancel in the difference, while the two nonzero dual lines are distinct; hence its Fourier support is also \(2(p-1)\), and equality follows.

For the count, choose an unordered pair of distinct line directions in \(\binom{p+1}{2}\) ways and then one affine line in each direction in \(p^2\) ways. Interchanging the two lines multiplies the function by \(-1\), so these are exactly the projective rational extremizers.

## Verification
The accompanying `verify.py` performs two exact finite consistency checks. First, for \(p\in\{3,5,7,11\}\) it enumerates integer value-multiplicity partitions and confirms that the zero-count lemma has the unique equality pattern \((p-1,1)\) on both sides. Second, for \(p=3\) it exhausts all \(3^9-1\) nonzero functions \(\mathbb F_3^2\to\{-1,0,1\}\), computes Fourier support exactly in \(\mathbb Q(\zeta_3)\), and confirms that the balanced equality functions are precisely the \(108\) signed differences of nonparallel affine-line indicators. The script prints `VERIFY_OK`.

These finite checks are not used to prove the theorem for general \(p\); the universal statement is proved analytically above.

## Relationship to prior work
Biró and Lev prove the sharp complex-valued finite-plane uncertainty inequality used here and explicitly note line-indicator differences as equality examples, but they do not classify the balanced rational equality cases. Their rationality argument also records the Galois-orbit structure of Fourier support that is used here.

Bonami and Ghobber classify equality cases for minimal Fourier support at a prescribed spatial support size. For \(|S|=2(p-1)\), their exact uncertainty profile gives a minimum Fourier-support size \(p\), whereas the balanced case studied here has \(|X|=2(p-1)\). Thus their equality classification does not imply this result.

Lev later uses the same nonparallel-line difference as a sharp example in a point-distribution problem, without a uniqueness classification. Later work on special directions in finite affine planes concerns point sets and direction counts rather than weighted rational Fourier equality cases.

## Limitations
The rational-valued hypothesis is essential to the proof because it forces Fourier support to be invariant under the cyclotomic Galois action. No classification of arbitrary complex-valued balanced extremizers is claimed. The statement also does not cover unequal-support equality cases. A differently phrased or unindexed equivalent classification remains a residual literature risk.

## References
1. A. Biró and V. F. Lev, "Uncertainty in finite planes," arXiv:1808.07424, first public version 22 August 2018.
2. A. Bonami and S. Ghobber, "Equality cases for the uncertainty principle in finite Abelian groups," arXiv:1003.5060.
3. V. F. Lev, "Point distribution and perfect directions in \(\mathbb F_p^2\)," arXiv:1903.01518.
4. G. Kiss and G. Somlai, "Special directions on the finite affine plane," arXiv:2109.13992.
