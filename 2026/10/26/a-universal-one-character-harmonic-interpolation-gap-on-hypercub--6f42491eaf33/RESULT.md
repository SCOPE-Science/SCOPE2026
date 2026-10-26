# A universal one-character harmonic interpolation gap on hypercube vertices

## Finding
For every integer \(d\ge3\), let \(X_d=\{\varepsilon/\sqrt d:\varepsilon\in\{-1,1\}^d\}\subset S^{d-1}\), and let \(E_\ell:\mathcal H_\ell(\mathbb R^d)\to\mathbb R^{X_d}\) evaluate homogeneous real harmonic polynomials of exact degree \(\ell\) on \(X_d\). Then
\[
\operatorname{rank}E_d=2^{d-1},\qquad
\operatorname{rank}E_{d+2}=2^{d-1}-1,\qquad
\operatorname{rank}E_{d+4}=2^{d-1}.
\]
The unavoidable parity constraint is \(f(-x)=(-1)^d f(x)\) at all three degrees. In this parity-compatible data space, the **only** missing datum at degree \(d+2\) is the full Walsh character \(\chi_{[d]}(\varepsilon)=\prod_{i=1}^d\varepsilon_i\). At degrees \(d\) and \(d+4\), every parity-compatible datum can be interpolated by a homogeneous harmonic polynomial of that exact degree. This is a loss followed by recovery, rather than a monotone degree threshold.

## Assumptions and scope
Here \(\mathcal H_\ell(\mathbb R^d)\) means the vector space of real homogeneous polynomials \(H\) of total degree \(\ell\) satisfying \(\Delta H=0\) in \(\mathbb R^d\). The rank is over \(\mathbb R\); complexification has the same rank. No Sobolev, low-pass or cumulative-degree evaluation space is used. The theorem concerns exactly \(\ell=d,d+2,d+4\), not all degrees.

Identify \(\mathbb R^{X_d}\) with real functions of \(\varepsilon\in\{\pm1\}^d\) and write \(\chi_S(\varepsilon)=\prod_{i\in S}\varepsilon_i\) for subsets \(S\subset[d]\). The Walsh characters form an orthogonal basis. All three target degrees have parity \(d\), so the relevant data space is
\[
W_d=\operatorname{span}\{\chi_S:|S|\equiv d\pmod2\},\qquad\dim W_d=2^{d-1}.
\]

## Proof
**1. Universal parity upper bound.** Homogeneity gives \(H(-x)=(-1)^\ell H(x)\); hence \(\operatorname{im}E_\ell\subset W_d\) for the three degrees.

**2. A missing character at degree \(d+2\).** Average any \(H\in\mathcal H_{d+2}\) under independent coordinate sign changes against the character \(\chi_{[d]}\). The resulting harmonic polynomial \(H_{\rm top}\) is odd in every coordinate and still has degree \(d+2\). Therefore
\[
H_{\rm top}(x)=\left(\prod_{i=1}^d x_i\right)\sum_{i=1}^d a_i x_i^2.
\]
Because \(\Delta H_{\rm top}=6(\sum_i a_i)\prod_i x_i=0\), one has \(\sum_i a_i=0\). On cube vertices \(x_i^2=1/d\), so \(H_{\rm top}\) vanishes. Equivalently the Walsh coefficient \(\langle E_{d+2}H,\chi_{[d]}\rangle\) is zero for every \(H\). Consequently \(\operatorname{rank}E_{d+2}\le2^{d-1}-1\).

**3. Three explicit building blocks.** In disjoint coordinate groups use the solid harmonic polynomials
\[
A_4(u,v)=u^4-6u^2v^2+v^4,
\]
\[
B_6(u,v,w)=\frac{231u^6-315u^4R^2+105u^2R^4-5R^6}{16},\quad R^2=u^2+v^2+w^2,
\]
\[
B_7(u,v,w)=\frac{429u^7-693u^5R^2+315u^3R^4-35uR^6}{16}.
\]
These have vanishing Laplacian in their own variables. At every unscaled sign corner, \(A_4=-4\), \(B_6=6\), and \(B_7=15u\). The first two are even in each used coordinate; the third is odd only in its first coordinate. A product of harmonic factors supported on **disjoint** coordinate groups is harmonic. Unused coordinates cause no difficulty.

**4. Realizing the other characters at degree \(d+2\).** Fix \(S\subsetneq[d]\) with \(|S|\equiv d\pmod2\), put \(j=|S|\) and \(m=d-j\). Then \(m\) is even and \(m\ge2\). We construct an even-in-each-coordinate harmonic polynomial of degree \(m+2\) in the \(m\) complementary variables that is a nonzero constant on their sign corners. When \(m=4a+2\), use \(a+1\) copies of \(A_4\) on disjoint variable pairs (the number of used variables is \(2a+2\le m\)). When \(m=4a\), \(a\ge1\), use one copy of \(B_6\) and \(a-1\) copies of \(A_4\) (using \(2a+1\le m\) variables). Multiplying by \(\prod_{i\in S}x_i\) gives a homogeneous harmonic polynomial of degree \(d+2\) whose restriction is a nonzero multiple of \(\chi_S\). Thus all parity-compatible Walsh characters other than \(\chi_{[d]}\) appear, and \(\operatorname{rank}E_{d+2}=2^{d-1}-1\).

**5. Full parity rank at degree \(d\).** If \(S=[d]\), the product \(\prod_{i=1}^d x_i\) is harmonic and restricts to \(\chi_S\) up to scale. For \(m=d-|S|=2\), the condition \(d\ge3\) ensures \(S\ne\varnothing\). Choose \(i\in S\) and \(u\notin S\), and use
\[
H_S(x)=\left(\prod_{h\in S}x_h\right)(x_i^2-3x_u^2).
\]
The two Laplacian contributions \(6\prod_{h\in S}x_h\) and \(-6\prod_{h\in S}x_h\) cancel; the restriction is \(-2\chi_S/d\) times its common monomial normalization. For even \(m\ge4\), write \(m=4a\) or \(m=6+4a\) and use, respectively, \(a\) copies of \(A_4\), or one \(B_6\) and \(a\) copies of \(A_4\), in disjoint groups among the \(m\) complementary variables. Multiplying their product by \(\prod_{i\in S}x_i\) produces degree \(d\) and nonzero \(\chi_S\) restriction. Hence \(\operatorname{rank}E_d=2^{d-1}\).

**6. Recovery at degree \(d+4\).** For \(S=[d]\), use
\[
H(x)=\left(\prod_{i=3}^d x_i\right)\operatorname{Im}(x_1+i x_2)^6.
\]
It is harmonic, has degree \(d+4\), and is a nonzero multiple of \(\chi_{[d]}\) on cube vertices because \(\operatorname{Im}(1+i)^6=-8\). For \(m=d-|S|=2\), choose \(i\in S\) and the two complementary coordinates \(u,v\), and use \(\prod_{h\in S\setminus\{i\}}x_h\,B_7(x_i,x_u,x_v)\). The degree is \(d+4\) and the restriction is nonzero in \(\chi_S\). For \(m=4a\ge4\), use \(a+1\) copies of \(A_4\) on complementary variable pairs; for \(m=4a+2\ge6\), use one \(B_6\) and \(a\) copies of \(A_4\). These have degree \(m+4\), use at most the \(m\) available complementary variables, and have nonzero constant sign-corner values. Multiplying by \(\prod_{i\in S}x_i\) completes all characters. Thus \(\operatorname{rank}E_{d+4}=2^{d-1}\). \(\square\)

## Verification
The fully self-contained proof constructs an exact-degree harmonic interpolant for every claimed Walsh character and proves the unique missing character by harmonic sign projection. `checker.py` independently verifies the Laplacian and corner values of \(A_4,B_6,B_7\), and uses exact rational Gegenbauer/Krawtchouk spectra to check all three ranks for every \(3\le d\le10\). These finite tests are supplementary and do not establish the theorem for all dimensions.

## Relationship to prior work
Bannai, Okuda and Tagami (2013) develop spherical designs of harmonic index and recall Gegenbauer reproducing kernels and the addition formula. Zhu, Bannai, Bannai, Kim and Yu (2015) develop tight harmonic-index bounds and constructions. These works address ordinary (unweighted) harmonic sums and design extremality, rather than the full Walsh-character decomposition of the **exact-degree evaluation image** on cube vertices. Related published finite Fourier-sampling results for fixed Hamming shells study different restriction operators and do not imply the present ranks; likewise earlier harmonic evaluation results for exceptional root configurations concern distinct point sets and representations. The new statement is not a claim that its underlying harmonic identities or Walsh orthogonality are new.

## Limitations
The rank theorem is restricted to the three exact degrees stated and to \(d\ge3\). It does not give singular values, frame bounds, or an all-degree rank formula; it does not concern harmonic polynomials of degree **at most** a cutoff. The originality review used accessible indexed literature and mathematical research records, so differently formulated or unindexed antecedents remain possible. No independent external audit is claimed.

## References
1. Eiichi Bannai, Takayuki Okuda and Makoto Tagami, *Spherical designs of harmonic index t*, first public arXiv version 2013-08-23, arXiv:1308.5101, https://arxiv.org/abs/1308.5101 .
2. Yan Zhu, Eiichi Bannai, Etsuko Bannai, Kyoung-Tark Kim and Wei-Hsuan Yu, *More on spherical designs of harmonic index t*, first public arXiv version 2015-07-20, arXiv:1507.05373, https://arxiv.org/abs/1507.05373 .
3. Delsarte, Goethals and Seidel, *Spherical codes and designs*, Geometriae Dedicata 6 (1977), 363–388, for the general spherical-design and addition-formula framework.
