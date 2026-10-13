# The first nonannihilating rank-two fiber of square-zero anticommuting matrix pairs

## Finding

Let \(k=\mathbb F_q\), with \(q\) any prime power, and let \(n\ge4\). Fix \(X\in M_n(k)\) with \(X^2=0\) and \(\operatorname{rank}X=2\). Define \(\mathcal F_X\) as the set of \(Y\in M_n(k)\) with \(Y^2=0\), \(XY+YX=0\), and \(XY\ne0\). Then
\[
|\mathcal F_X|=(q^2-1)q^{2n-6}S_{n-4}(q),
\qquad
S_s(q)=\sum_{t=0}^{\lfloor s/2\rfloor}{s\brack t}_q{s-t\brack t}_q\prod_{i=0}^{t-1}(q^t-q^i).
\]
Here \(S_s(q)\) is the total number of square-zero matrices of size \(s\) over \(k\), and empty products equal \(1\). Every \(Y\in\mathcal F_X\) satisfies \(\operatorname{rank}(XY)=1\). This identifies the first possible nonannihilating locus: if \(X^2=0\) and \(\operatorname{rank}X\le1\), anticommutation and \(Y^2=0\) force \(XY=0\).

In particular, for \(n=4,5,6\), the fixed-target counts are respectively \((q^2-1)q^2\), \((q^2-1)q^4\), and \((q^2-1)q^8\). For the last identity, \(S_2(q)=q^2\). For \(q=2\), they are \(12,48,768\). The corresponding count over *all* rank-two square-zero first matrices is obtained by multiplying by
\[
{n\brack 2}_q{n-2\brack 2}_q|\mathrm{GL}_2(k)|.
\]

## Assumptions and scope

All matrices act on \(k^n\); their multiplication is the ordinary matrix product. The matrix \(X\) is fixed, not chosen afresh for each \(Y\). Anticommutation means \(XY+YX=0\), which coincides with commutation in characteristic two. The product is required to be nonzero. The theorem makes no claim to classify the ranks of \(Y\), the separate \(XY=0\) locus, or fibers where \(\operatorname{rank}X>2\).

Write \({a\brack b}_q\) for the Gaussian binomial coefficient (zero unless \(0\le b\le a\)), and \(\mathrm{GL}_0(k)\) for the trivial group. The empty matrix case \(s=0\) has \(S_0(q)=1\).

## Proof

**Step 1: canonical form and block equations.** Put \(s=n-4\). Since \(X^2=0\) and \(\operatorname{rank}X=2\), choose a basis adapted to its image, a two-dimensional space of preimages, and a complementary \(s\)-space in the kernel. Relative to dimensions \(2,2,s\), we have
\[
X=\begin{pmatrix}0&I_2&0\\0&0&0\\0&0&0\end{pmatrix}.
\]
Solving \(XY+YX=0\) blockwise shows, with no restriction on characteristic, that \(Y\) has the unique form
\[
Y=\begin{pmatrix}P&Q&R\\0&-P&0\\0&W&Z\end{pmatrix},
\]
where \(P,Q\) are \(2\times2\), \(R\) is \(2\times s\), \(W\) is \(s\times2\), and \(Z\) is \(s\times s\). Furthermore, \(\operatorname{rank}(XY)=\operatorname{rank}P\). Multiplying blocks gives the *equivalent* system
\[
P^2=0,\quad Z^2=0,\quad PR+RZ=0,\quad ZW-WP=0,\quad PQ-QP+RW=0.
\]

**Step 2: nonzero-product block.** For \(P\in M_2(k)\), the simultaneous conditions \(P^2=0\) and \(P\ne0\) mean that \(P\) is a single nilpotent Jordan block. There are exactly \(q^2-1\) such \(P\): choose its one-dimensional image/kernel (\(q+1\) choices), then a nonzero map from the quotient to that line (\(q-1\) choices). Thus \(XY\ne0\) precisely when \(P\) is one of these, and every such product has rank one.

**Step 3: independent intertwiner spaces.** Fix such \(P\) and any square-zero \(Z\in M_s(k)\), of rank \(t\). As a \(k[z]/(z^2)\)-module, \(k^s\) splits as \(t\) indecomposable length-two modules and \(s-2t\) length-one modules. The nonzero \(2\)-block \(P\) is the free rank-one module over \(k[z]/(z^2)\). Multiplication by \(-1\) on the degree-one generator identifies the modules for \(P\) and \(-P\), even in characteristic two. Consequently the equations \(PR+RZ=0\) and \(ZW-WP=0\) define independent \(k\)-vector spaces of dimension
\[
2t+(s-2t)=s
\]
each: the first consists of maps from the module of \(Z\) to the length-two module and the second of maps in the opposite direction. There are therefore exactly \(q^{2s}\) admissible ordered pairs \((R,W)\), *independently of the Jordan type of \(Z\)*.

**Step 4: the remaining commutator is always soluble.** Combining \(PR=-RZ\) and \(ZW=WP\) yields \(P(RW)+(RW)P=0\). Conjugate \(P\) to \(J=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}\). The anticommutant \(\{C:JC+CJ=0\}\) is precisely the two-dimensional space
\[
\left\{\begin{pmatrix}a&b\\0&-a\end{pmatrix}:a,b\in k\right\}.
\]
It equals the image of the map \(Q\mapsto JQ-QJ\), which has two-dimensional kernel. Hence, for **every** admissible \((R,W)\), the equation \(PQ-QP=-RW\) has exactly \(q^2\) solutions \(Q\). This proves that each square-zero \(Z\) supports exactly \((q^2-1)q^{2s+2}\) matrices \(Y\) with nonzero product, giving the asserted factorization since \(2s+2=2n-6\).

**Step 5: exact square-zero matrix count.** If \(Z^2=0\) and \(\operatorname{rank}Z=t\), choose its image \(U\) (\({s\brack t}_q\) choices), choose its kernel of dimension \(s-t\) containing \(U\) (\({s-t\brack t}_q\) choices), and choose the induced isomorphism \(k^s/\ker Z\to U\) (\(|\mathrm{GL}_t(k)|\) choices). All choices are independent and exhaustive; rank constraints require \(2t\le s\). Summing proves the displayed formula for \(S_s(q)\).

**Step 6: sharp first rank and global count.** If \(\operatorname{rank}X=1\), the same construction with one-dimensional nonzero block makes \(P\) a scalar; \(P^2=0\) forces \(P=0\), hence \(XY=0\). Conversely choose any nonzero nilpotent \(P\) above and set \(Q=R=W=Z=0\) to obtain a nonannihilating partner whenever \(\operatorname{rank}X=2\). The number of rank-two square-zero \(X\)'s follows from the same image–kernel–quotient-isomorphism count in Step 5 with \(s=n\), \(t=2\). Its product with the fixed-target count proves the final total-count identity.

## Verification

The standalone `verify.cpp` evaluates the full defining matrix equations directly over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_5\), and the quadratic extension \(\mathbb F_4\), without using the theorem to accept a candidate. It enumerates every anticommuting \(Y\) via the exact linear block parametrization and checks \(Y^2=0\), \(XY+YX=0\), and \(\operatorname{rank}(XY)\) by elimination. Test dimensions are \(n=4\) over four fields, \(n=5\) over two fields, and \(n=6\) over \(\mathbb F_2\). All tested nonzero-product counts agree with the theorem. This is supporting finite evidence; the proof of the arbitrary-field and arbitrary-dimension claim is Steps 1–6, not finite enumeration.

## Relationship to prior work

Schröer's study of the mutually annihilating pair varieties imposes \(XY=YX=0\), and consequently excludes the \(XY\ne0\) locus counted here. Chen and Wang describe the full linear space of matrices anticommuting with a nilpotent Jordan normal form (their Proposition 2.2) and the geometry of complex anti-commuting varieties, but do not impose the second square-zero constraint to enumerate these finite-field nonzero-product fibers. Huang's finite-field counts likewise concern mutual annihilation \(XY=YX=0\). Those structural and enumerative results are credited. The present theorem is an explicit fixed-Jordan-type finite-field refinement for the first nonannihilating rank, not a claim of a general classification of anti-commuting matrix pairs.

## Limitations

No assertion is made for higher first-matrix ranks or the \(XY=0\) branch. Historical literature on representations of the two-generator exterior algebra may contain an equivalent expression under module-theoretic terminology; the literature comparison cannot exclude every unindexed source. The finite checks do not constitute an infinite-field or infinite-dimensional certificate. The result has not undergone independent mathematical audit.

## References

1. J. Schröer, “Varieties of pairs of nilpotent matrices annihilating each other,” arXiv:math/0211293 (first public 2002-11-19); *Commentarii Mathematici Helvetici* 79 (2004), 396–426, doi:10.1007/s00014-003-0788-3.
2. X. Chen and W. Wang, “Anti-commuting varieties,” arXiv:1805.00378 (first public 2018-05-01); *Transactions of the AMS* 373 (2020), 1597–1617, especially Proposition 2.2 and §6.
3. Y. Huang, “Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity,” arXiv:2110.15566 (first public 2021-10-29), especially §3.1.
