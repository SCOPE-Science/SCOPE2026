# Exact even-dilate Shapiro constants for Hamming balls on the Boolean cube
## Finding
Let
\[
G=\mathbb F_2^d,\qquad d\ge1,
\]
with Hamming weight \(|x|\), and let
\[
B_s=\{x\in G:|x|\le s\}.
\]
Take
\[
U=B_1=\{0,e_1,\ldots,e_d\}.
\]
For every integer \(r\ge1\), the \(2r\)-fold Minkowski sum of \(U\) is
\[
2r\,U=B_{\min(2r,d)}.
\]

For the Shapiro-type extremal quantity of Gaál--Révész,
\[
Q(U,2r)
=
\sup_{\substack{f\not\equiv0\\ f\ge0\\ f\text{ positive definite}}}
\frac{\sum_{x\in 2rU}f(x)}
{\sum_{x\in U}f(x)},
\]
one has the exact formula
\[
Q(B_1,2r)
=
\sum_{\substack{0\le w\le\min(2r,d)\\ w\ {\rm even}}}
\binom{d}{w}.
\]
Thus the sharp constant is exactly the number of even-weight vectors in the larger Hamming ball. An extremizer is
\[
f_{\rm even}(x)=
\begin{cases}
1,&|x|\ {\rm even},\\
0,&|x|\ {\rm odd}.
\end{cases}
\]

## Assumptions and scope
The group carries counting measure. Positive definiteness is in the finite-abelian-group sense, equivalently the Walsh--Fourier transform
\[
\widehat f(\xi)=\sum_{x\in G}f(x)(-1)^{\xi\cdot x}
\]
is nonnegative for every \(\xi\in G\). The pointwise assumption \(f\ge0\) is also required, exactly as in the Shapiro-type problem.

The theorem concerns even dilation parameters \(2r\). No formula for odd dilation parameters is claimed.

## Proof
Set
\[
R=\min(2r,d),\qquad B=B_R.
\]
Let
\[
E=\sum_{\substack{0\le w\le R\\w\ {\rm even}}}\binom{d}{w},
\qquad
O=\sum_{\substack{0\le w\le R\\w\ {\rm odd}}}\binom{d}{w}.
\]
Thus \(|B|=E+O\).

For \(\xi\in G\), write \(j=|\xi|\). We first prove the Fourier bound
\[
\widehat{1_B}(\xi)
\le
E+\frac{O}{d}(d-2j).
\tag{1}
\]
For \(\xi=0\), equality holds because \(\widehat{1_B}(0)=E+O\).

Now suppose \(\xi\ne0\), and let \(S\) be its support. Put
\[
N_S=
\bigl|\{x\in B:|x\cap S|\ {\rm odd}\}\bigr|.
\]
Choose one coordinate \(i\in S\). From the odd-weight part of \(B\), define
\[
\phi(x)=
\begin{cases}
x,&|x\cap S|\ {\rm odd},\\
x+e_i,&|x\cap S|\ {\rm even}.
\end{cases}
\]
The image always lies in \(B\): toggling one coordinate sends an odd weight to an even weight, and an upward toggle cannot cross the even radius \(R\); if \(B=G\), there is no boundary issue. The image always has odd intersection with \(S\). The map is injective because the first branch has odd-weight outputs while the second has even-weight outputs, and each branch is individually injective. Hence
\[
N_S\ge O.
\]
Therefore
\[
\widehat{1_B}(\xi)
=
|B|-2N_S
\le E-O.
\]
Since \(1\le j\le d\),
\[
E-O
\le
E+\frac{O}{d}(d-2j),
\]
which proves (1).

Let \(f\ge0\) be positive definite. Fourier inversion and \(\widehat f(\xi)\ge0\) give
\[
\sum_{x\in B}f(x)
=
2^{-d}\sum_{\xi\in G}\widehat f(\xi)\widehat{1_B}(\xi)
\le
E f(0)+\frac{O}{d}\sum_{|x|=1}f(x).
\tag{2}
\]
Indeed, the Walsh transform of the weight-one sphere is
\[
d-2|\xi|.
\]

Next,
\[
O\le dE.
\tag{3}
\]
To see this, send each odd-weight vector \(x\in B\) to the pair \((i,x+e_i)\), where \(i\) is the least coordinate in the support of \(x\). The second component has even weight and lies in \(B\), and the map is injective into a set of size \(dE\).

Because \(f\ge0\), combining (2) and (3) yields
\[
\sum_{x\in B}f(x)
\le
E\left(f(0)+\sum_{|x|=1}f(x)\right)
=
E\sum_{x\in B_1}f(x).
\]
Hence \(Q(B_1,2r)\le E\).

For the reverse inequality, let \(H\) be the even-parity subgroup of \(G\), and take \(f=1_H\). Its Walsh transform is supported on the trivial character and the all-ones character and is everywhere nonnegative, so \(f\) is positive definite. Also \(f\ge0\). Since the only even-weight point of \(B_1\) is \(0\),
\[
\sum_{x\in B_1}f(x)=1,
\]
whereas
\[
\sum_{x\in B}f(x)=E.
\]
Thus \(Q(B_1,2r)\ge E\), completing the proof.

## Verification
The accompanying `verify.py` performs exact integer checks for \(1\le d\le10\) and \(1\le r\le6\). It enumerates every character of \(\mathbb F_2^d\), computes the Walsh transform of the relevant Hamming ball, checks the affine Fourier majorant in (1), checks the stronger nonzero-character bound \(\widehat{1_B}(\xi)\le E-O\), and verifies that the even-parity subgroup indicator attains the claimed ratio. It prints `VERIFY_OK`.

These finite checks are sanity tests only. The theorem for all \(d\ge1\) and \(r\ge1\) is proved analytically above.

## Relationship to prior work
Gaál and Révész define the general Shapiro-type quantities \(S(U,V)\) and \(Q(U,k)=S(U,kU)\) for nonnegative positive definite functions on locally compact abelian groups and establish broad duality and equivalence results. Their paper does not specialize the problem to Boolean cubes or Hamming balls; a full-text search of the open preprint has no occurrence of "Hamming".

Earlier work of Efimov, Gaál, and Révész treats interval-doubling constants on the real line. Gorbachev studies discrete inequalities on cyclic groups \(\mathbb Z_q\), including a bound for nonnegative positive definite functions on intervals. Those geometries and statements do not imply the exact Boolean-cube Hamming-ball formula above.

Targeted searches for the Shapiro constant of a Hamming ball, the exact expression
\[
\sum_{2j\le 2r}\binom{d}{2j},
\]
and equivalent Walsh/Krawtchouk formulations found no covering statement.

## Limitations
Only even dilation parameters are determined. The proof does not classify all extremizers, and it does not give the corresponding exact constants for odd Hamming radii. Search non-detection is not proof of absolute novelty, so differently phrased or unindexed literature remains a residual originality risk.

## References
1. M. Gaál and Sz. Gy. Révész, "Integral comparisons of nonnegative positive definite functions on LCA groups," arXiv:1803.06409, first posted 16 March 2018; later published in *Mathematische Zeitschrift* 302 (2022), 995--1024.
2. A. Efimov, M. Gaál, and Sz. Gy. Révész, "On integral estimates of nonnegative positive definite functions," *Bulletin of the Australian Mathematical Society* 96 (2017), 117--125. DOI: 10.1017/S0004972717000119.
3. D. V. Gorbachev, "Certain inequalities for discrete, nonnegative, positive definite functions," *Izvestiya Tula State University. Natural Sciences* 2 (2015), 1--8.
