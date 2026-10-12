# Exact minimum dual supports for good-rational-function LRCs
## Finding

Let \(q\) be a prime power and let \(C\) be any code from Theorem 3.2 of Liu--Mesnager--Tang--Zheng constructed from an \((r,l)\)-good rational function. Write
\[
k=tr,\qquad 2\le t\le l,
\]
and let \(A_1,\ldots,A_l\) be the disjoint full fibers, each of size \(r+1\). Then
\[
d(C^\perp)=r+1.
\]
More precisely, the supports of all weight-\(r+1\) words of \(C^\perp\) are exactly
\[
A_1,\ldots,A_l.
\]
For every \(m\), the dual words supported on \(A_m\) form a one-dimensional subspace, so the exact number of nonzero minimum dual words is
\[
A_{r+1}(C^\perp)=l(q-1).
\]
Consequently every coordinate has exactly one recovery set of minimum possible size \(r\): if \(P\in A_m\), it is \(A_m\setminus\{P\}\).

## Assumptions and scope

The source chooses distinct fiber values \(t_m\) and a value \(b\in\mathbb F_q\) outside the image of the rational function. Put
\[
d_m=(t_m-b)^{-1},
\]
using the natural projective convention that the image of \(t_m=\infty\) under \(y\mapsto (y-b)^{-1}\) is \(0\). The source proves that the \(d_m\) are pairwise distinct.

For a finite projective point \(P\), define
\[
u(P)=(1,P,\ldots,P^{r-1})^{\mathsf T},
\]
and for the point at infinity define
\[
u(\infty)=(0,\ldots,0,1)^{\mathsf T}.
\]
The source's special infinity coordinate is exactly this extended Reed--Solomon evaluation functional. After ordering the message coordinates by the exponent \(j\), the generator column at \(P\in A_m\) is
\[
g(P)=u(P)\otimes(1,d_m,\ldots,d_m^{t-1})^{\mathsf T},
\]
up to an immaterial permutation of row coordinates.

The hypothesis \(t\ge2\) is essential for the support classification. At \(t=1\), the second fiber-label block disappears and arbitrary \((r+1)\)-subsets of projective evaluation points can be dependent, so the designated fibers need not be the unique minimum supports.

## Proof

First consider any set \(S\) of at most \(r\) generator columns. Project to the block with exponent \(j=0\). The resulting columns are the extended Vandermonde columns \(u(P)\) at distinct points of \(\mathbb P^1(\mathbb F_q)\). Every set of at most \(r\) such columns is linearly independent. Therefore every set of at most \(r\) columns of the full generator matrix is independent, and hence
\[
d(C^\perp)\ge r+1.
\]

Fix a fiber \(A_m\). Its \(r+1\) extended Vandermonde columns have rank \(r\), so there is a unique relation up to scalar,
\[
\sum_{P\in A_m}\lambda_Pu(P)=0.
\]
Every coefficient \(\lambda_P\) is nonzero, because deleting any one column leaves \(r\) independent columns. On the fiber, \(d_m\) is constant. Thus for every \(0\le j<t\),
\[
\sum_{P\in A_m}\lambda_Pd_m^j u(P)
=d_m^j\sum_{P\in A_m}\lambda_Pu(P)=0.
\]
The same coefficients therefore annihilate the full generator columns. This produces a dual word of weight \(r+1\), proving
\[
d(C^\perp)=r+1.
\]

It remains to classify all minimum supports. Let \(S\) be the support of a weight-\(r+1\) dual word, with nonzero coefficients \(\lambda_P\). The \(j=0\) block gives
\[
\sum_{P\in S}\lambda_Pu(P)=0.
\]
Because \(|S|=r+1\) and every \(r\)-subset is independent, the nullspace of these extended Vandermonde columns is one-dimensional. Since \(t\ge2\), the \(j=1\) block also gives
\[
\sum_{P\in S}\lambda_Pd_{m(P)}u(P)=0,
\]
where \(m(P)\) denotes the fiber containing \(P\). The second coefficient vector must be a scalar multiple of the first. Hence there is a constant \(c\) such that
\[
\lambda_Pd_{m(P)}=c\lambda_P
\]
for every \(P\in S\). All \(\lambda_P\) are nonzero, so all \(d_{m(P)}\) are equal. Pairwise distinctness of the \(d_m\) forces every point of \(S\) into one fiber. Because both \(S\) and that fiber have size \(r+1\), one has \(S=A_m\).

For each fiber the relation space is one-dimensional, yielding exactly \(q-1\) nonzero dual words. Summing over the \(l\) disjoint fibers gives \(l(q-1)\). Finally, for a linear code a recovery set of size \(r\) for coordinate \(P\) is equivalent to a dual word supported on that coordinate together with at most \(r\) helpers. The proved dual minimum distance rules out fewer helpers, and the support classification leaves only the other points of the same fiber.

## Verification

`artifacts/verify.py` uses only the Python standard library and replays two finite models from the embedded package. The first reconstructs the explicit degree-three rational function from Proposition 5.5 at \(q=11\), \(w=1\):
\[
h(x)=\frac{x^3-3x+1}{x(x-1)}.
\]
It recovers its four three-point fibers on \(\mathbb P^1(\mathbb F_{11})\), builds the source generator for \(r=2\), \(t=2\), and exhausts every subset of up to three columns. Exactly the four source fibers are dependent triples, so the verifier obtains dual distance \(3\) and \(40=4(11-1)\) minimum dual words.

A second model over \(\mathbb F_{13}\) uses three four-point fibers, including a point at infinity, with \(r=3\) and \(t=2\). Exhaustive column-subset checks give exactly three dependent four-subsets and hence \(36=3(13-1)\) minimum dual words. The script also repeats the second model with \(t=1\) and verifies that extra dependent four-subsets appear, confirming that the excluded boundary is real.

These finite computations test the implementation and the infinity convention. They are not an exhaustive proof over all prime powers; the all-parameter result is the symbolic argument above. Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Liu, Mesnager, Tang, and Zheng introduce good rational functions and prove Theorem 3.2, which constructs optimal LRCs from full fibers. Their proof explicitly gives the fiber constants \(d_m\), the Vandermonde structure across fibers, and the local polynomial interpolation mechanism. The paper does not state the dual minimum distance, enumerate minimum dual words, or classify all minimum recovery supports; searches of its public full text for “dual” and “minimum weight” return no occurrence.

Tamo--Barg good-polynomial codes are the constructional predecessor, and general LRC theory identifies small recovery sets with low-weight dual words. Gruica, Jany, and Ravagnani develop a recent duality framework for LRCs and record the general implication \(d(C^\perp)\le r+1\). That implication supplies only an upper bound and does not force equality, identify every minimum support, or show uniqueness of a minimum recovery set. The argument here uses the new source's two independent Vandermonde blocks to obtain exactly those stronger conclusions.

Searches under the source identifier, good-rational-function terminology, Tamo--Barg aliases, dual distance, minimum dual words, and unique recovery sets found no statement implying the exact formula \(A_{r+1}(C^\perp)=l(q-1)\) for this family.

## Limitations

The support-classification theorem requires \(t=k/r\ge2\). It does not claim uniqueness of larger recovery sets; only recovery sets of minimum cardinality are classified. It also does not claim that analogous uniqueness holds for arbitrary optimal LRCs or arbitrary algebraic-geometry LRCs.

A general matroid or good-polynomial theorem not indexed under the searched recovery-set or dual-support terminology could contain an equivalent statement. The proof here is nevertheless independent and explicitly covers the good-rational-function construction, including its projective infinity coordinate.

## References

1. Hengfeng Liu, Sihem Mesnager, Chunming Tang, and Xuemin Zheng, *Beyond Polynomials: Optimal Locally Recoverable Codes from Good Rational Functions*, arXiv:2605.11465v1, first public 2026-05-12.
2. Itzhak Tamo and Alexander Barg, *A family of optimal locally recoverable codes*, IEEE Transactions on Information Theory 60 (2014), 4661--4676.
3. Elisa Gorla Gruica, Benjamin Jany, and Alberto Ravagnani, *LRCS: Duality, LP bounds, and field size*, Designs, Codes and Cryptography (2026), DOI 10.1007/s10623-026-01829-7.
