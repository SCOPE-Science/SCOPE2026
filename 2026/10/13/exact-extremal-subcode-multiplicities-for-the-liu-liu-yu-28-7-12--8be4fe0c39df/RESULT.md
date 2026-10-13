# Exact extremal-subcode multiplicities for the Liu–Liu–Yu \([28,7,12]_2\) code
## Finding

For the \(m=3\) punctured binary subfield code \(C_f^{*(2)}\) of Liu, Liu, and Yu associated with
\[
f(x,y)=\operatorname{Tr}_{8/2}(xy)+N_{8/2}(x+y),
\]
the generalized Hamming weights are
\[
(d_1,d_2,d_3,d_4,d_5,d_6,d_7)=(12,18,21,24,26,27,28).
\]
The numbers of \(r\)-dimensional subcodes whose support has the minimum possible size \(d_r\) are, respectively,
\[
(M_1,M_2,M_3,M_4,M_5,M_6,M_7)=(63,336,64,315,378,28,1).
\]
Equivalently, after identifying the code's \(28\) generator columns with a \(28\)-point subset of \(\mathbb F_2^6\), the largest intersections with affine subspaces of dimensions \(5,4,3,2,1,0\) have sizes
\[
16,10,7,4,2,1,
\]
and the numbers of affine subspaces attaining those maxima are
\[
63,336,64,315,378,28.
\]
The new content asserted here is the exact extremal-subcode, equivalently extremal affine-section, multiplicity profile. No novelty is asserted for the generalized-weight values in isolation.

## Assumptions and scope

Let \(F=\mathbb F_8=\mathbb F_2(\alpha)\) with \(\alpha^3+\alpha+1=0\). Let \(\operatorname{Tr}_{8/2}\) and \(N_{8/2}\) be the field trace and norm to \(\mathbb F_2\). Define
\[
S=\{(x,y)\in F^2:\operatorname{Tr}_{8/2}(xy)+N_{8/2}(x+y)=0\}.
\]
The source construction gives \(|S|=28\). Its punctured binary code is the evaluation code
\[
C=\{(a+\operatorname{Tr}_{8/2}(bx+cy))_{(x,y)\in S}:a\in\mathbb F_2,\ b,c\in F\}.
\]
The calculation concerns this exact \(m=3\) representative only. It does not classify all binary \([28,7,12]\) codes, nor identify this representative with a particular historical equivalence-class label.

## Proof

Using the basis \(1,\alpha,\alpha^2\) of \(F/\mathbb F_2\), the generator column attached to \((x,y)\in S\) is
\[
g(x,y)=\bigl(1,\operatorname{Tr}(x),\operatorname{Tr}(\alpha x),\operatorname{Tr}(\alpha^2x),\operatorname{Tr}(y),\operatorname{Tr}(\alpha y),\operatorname{Tr}(\alpha^2y)\bigr)\in\mathbb F_2^7.
\]
Exact finite-field reconstruction gives \(28\) distinct nonzero columns and rank \(7\). Exhausting all \(2^7\) messages reproduces the source weight enumerator
\[
1+63z^{12}+63z^{16}+z^{28}.
\]

Let \(U\le\mathbb F_2^7\) be an \(r\)-dimensional message subspace and put \(W=U^\perp\), so \(\dim W=7-r\). A coordinate indexed by a column \(g\) vanishes on every codeword from \(U\) exactly when \(g\in W\). Therefore
\[
|\operatorname{Supp}(U)|=28-|G\cap W|,
\]
where \(G=\{g(x,y):(x,y)\in S\}\). Consequently
\[
d_r=28-\max_{\dim W=7-r}|G\cap W|,
\]
and the number \(M_r\) of minimizing \(r\)-subcodes is exactly the number of \((7-r)\)-subspaces attaining the maximum.

Every subspace of \(\mathbb F_2^7\) was enumerated exactly once by its reduced-row-echelon basis. The maximum column intersections for dimensions \(6,5,4,3,2,1,0\) are
\[
16,10,7,4,2,1,0,
\]
with multiplicities
\[
63,336,64,315,378,28,1.
\]
Substitution in the support formula proves both displayed sequences.

Because every generator column has first coordinate \(1\), a nonempty intersection of a \(t\)-dimensional linear subspace with the column set is the homogenization of an affine \((t-1)\)-subspace of \(\mathbb F_2^6\). This gives the equivalent affine-section formulation.

## Verification

`artifacts/verify.py` uses only exact binary and finite-field arithmetic. It reconstructs \(\mathbb F_8\), the defining set \(S\), all \(28\) generator columns, and the published ordinary weight enumerator. It then enumerates every subspace of \(\mathbb F_2^7\) in reduced-row-echelon form. The numbers of subspaces in dimensions \(0\) through \(7\) are checked against the binary Gaussian binomial coefficients, and the complete intersection histograms are checked against `artifacts/certificate.json`.

The replay proves the extrema and their multiplicities by exhaustive finite enumeration, not sampling. Running

`python3 artifacts/verify.py`

prints `VERIFY_OK`.

## Relationship to prior work

Liu, Liu, and Yu construct the punctured code, determine its ordinary weight distribution, and record the binary \([28,7,12]\) example together with its dual parameters. Their stated focus is few-weight structure, dual parameters, and designs; the source does not give the extremal-subcode multiplicities above.

The binary \([28,7,12]\) self-complementary codes were classified earlier into four equivalence classes. Separate literature on projective near-Griesmer codes and the chain condition is sufficiently close that the generalized-weight tuple itself is not claimed as new here. A later optimum-distance-profile study explicitly works with the four historical \([28,7,12]\) representatives, but optimum distance profiles concern nested minimum-distance chains and do not, in the inspected material, enumerate all subcodes attaining each generalized support minimum.

Searches using the exact code parameters, the generalized-weight tuple, the multiplicity vector \((63,336,64,315,378,28,1)\), affine-section aliases, and the source construction found no prior statement of the exact minimizer counts. Some older full text was not obtainable from the lawful sources checked, so an equivalent unindexed count remains a residual literature risk.

## Limitations

The result is finite and source-specific. It does not prove a new classification theorem for all four historical \([28,7,12]\) equivalence classes. It also does not claim that the generalized-weight values themselves are new.

The originality assessment is limited by incomplete access to some older literature. In particular, prior projective-code work may contain equivalent generalized-weight information under different terminology; the accepted claim is narrowed to the exact extremal-subcode multiplicities, for which no covering statement was located.

## References

1. S. Liu, Y. Liu, X. Yu, *Weight distributions of subfield codes from special functions*, AIMS Mathematics 11 (2026), 2797–2815, DOI 10.3934/math.2026112.
2. S. M. Dodunekov, S. B. Encheva, S. N. Kapralov, *On the \([28,7,12]\) Binary Self-Complementary Codes and Their Residuals*, Designs, Codes and Cryptography 4 (1994), 57–67.
3. S. B. Encheva, G. Cohen, *On Linear Projective Codes Which Satisfy the Chain Condition*, Information Sciences 118 (1999), 213–222, DOI 10.1016/S0020-0255(99)00036-5.
4. F. Freibert, J.-L. Kim, *Optimal subcodes and optimum distance profiles of self-dual codes*, Finite Fields and Their Applications 25 (2014), 146–164, DOI 10.1016/j.ffa.2013.09.002.
5. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412–1418.
