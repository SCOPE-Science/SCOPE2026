# Exact third cumulant and skewness-scale crossover of circular number variance

## Finding

Let \(U_1,\ldots,U_n\) be independent uniform points on the unit circle and, for \(0<s\le 1/3\), let \(C_n(x,s)\) count points in the circular interval of length \(s\) beginning at \(x\). Define the circular number variance
\[
V_n(s)=\int_0^1\bigl(C_n(x,s)-ns\bigr)^2\,dx.
\]
For every integer \(n\ge 2\), its **exact third centered moment** is
\[
\boxed{\kappa_3(V_n(s))=2n(n-1)s^4\left[(1-2s)^2+(n-2)\left(\frac{11}{5}s-4s^2\right)\right].}
\]
It is strictly positive throughout the stated parameter domain. With the known exact variance
\[
\kappa_2(V_n(s))=\frac43 n(n-1)s^3\left(1-\frac32s\right),
\]
write \(\gamma_n(s)=\kappa_3(V_n(s))/\kappa_2(V_n(s))^{3/2}\) for the standardized skewness. For any \(s_n\downarrow0\), as \(n\to\infty\),
\[
\gamma_n(s_n)\sim
\begin{cases}
\displaystyle\frac{3\sqrt3}{4n\sqrt{s_n}},& ns_n\longrightarrow0,\\[4pt]
\displaystyle\frac{3\sqrt3}{4}\left(1+\frac{11\tau}{5}\right)\frac1{n\sqrt{s_n}},&ns_n\longrightarrow\tau\in(0,\infty),\\[4pt]
\displaystyle\frac{33\sqrt3}{20}\sqrt{s_n},&ns_n\longrightarrow\infty.
\end{cases}
\]
The width \(s_n\asymp n^{-1}\) is therefore the precise crossover between repeated-edge and triangular three-edge contributions to the third cumulant. These asymptotic equivalences concern skewness and require no assumption that a central limit theorem holds. In particular, when \(n^2s_n\) stays bounded, skewness need not vanish.

## Assumptions and scope

All circle coordinates are modulo one; the \(n\) observations are independent and exactly uniform. Both \(n\ge2\) and \(0<s\le 1/3\) are essential stated domains. Endpoints have probability zero. The third cumulant equals the third centered moment. The formulas are not asserted for \(s>1/3\), where a triple of close points may wrap around the whole circle and change the triangle integral. The asymptotic statements additionally require \(s_n\to0\), and \(n\to\infty\).

## Proof

Write \(D_{ij}=\min(|U_i-U_j|,1-|U_i-U_j|)\) and \(Y_{ij}=(s-D_{ij})_+\). The length of overlap of two circular intervals of length \(s\le1/2\) is \(Y_{ij}\). Expanding the integral of the squared count gives the exact deterministic identity
\[
V_n(s)=ns-n^2s^2+2\sum_{i<j}Y_{ij}.
\]
For two independent uniform positions, circular distance has density \(2\) on \((0,1/2)\). Hence \(\mathbb E Y_{ij}=s^2\), \(\mathbb E Y_{ij}^2=2s^3/3\), \(\mathbb E Y_{ij}^3=s^4/2\). Set \(h_{ij}=Y_{ij}-s^2\). Then
\[
\mathbb E h_{ij}^3=\frac{s^4}{2}-2s^5+2s^6,
\qquad \mathbb E[h_{ij}\mid U_i]=\mathbb E[h_{ij}\mid U_j]=0.
\]
Expand \(\mathbb E(\sum_{i<j}h_{ij})^3\) over three ordered edges. If the union of the edges contains a vertex occurring in exactly one edge, conditioning on that vertex annihilates the term. The only surviving edge patterns are one edge repeated three times and the three distinct edges of a triangle. The first has multiplicity \(\binom n2\); the second has multiplicity \(6\binom n3\).

For three distinct vertices, conditioning on the center of two incident edges gives \(\mathbb E[Y_{12}Y_{23}]=s^4\), and therefore
\[
\mathbb E[h_{12}h_{23}h_{31}]=\mathbb E[Y_{12}Y_{23}Y_{31}]-s^6.
\]
For \(s\le1/3\), a contributing triple cannot make a nontrivial full-circle winding. Fix \(U_1=0\), rescale the differences by \(s\), and split into equal-sign and opposite-sign quadrants. Their two contributions are respectively
\[
4\int_0^1\int_0^u (1-u)(1-v)(1-u+v)\,dv\,du=\frac{11}{30},
\]
\[
2\int_0^1\int_0^{1-u}(1-u)(1-v)(1-u-v)\,dv\,du=\frac{11}{60}.
\]
Thus \(\mathbb E[Y_{12}Y_{23}Y_{31}]=11s^5/20\). Note that all integrals are finite and nonnegative.

Combining multiplicities and the factor \(2^3\) from the centered number variance gives
\[
\kappa_3(V_n(s))=8\left[\binom n2\left(\frac{s^4}{2}-2s^5+2s^6\right)+6\binom n3\left(\frac{11s^5}{20}-s^6\right)\right],
\]
which simplifies to the claimed formula. For the sign, \((1-2s)^2>0\) and \(11/5-4s\ge13/15>0\). The variance follows by orthogonality of distinct centered pair terms:
\[
\operatorname{Var}V_n(s)=4\binom n2\left(\frac{2s^3}3-s^4\right).
\]
Finally substitute these exact identities into the definition of skewness. In the bracket of the third moment, the ratio of the triangle term to the repeated-edge term has leading value \((11/5)ns\). Evaluating its zero, finite, and infinite regimes yields the three stated constants, with no moment-to-distribution inference.

## Verification

The standalone script `verify.py` evaluates both triangle integrals symbolically, checks the exact polynomial equality and positivity for a grid of integer dimensions and rational window lengths, independently approximates the geometric triple integral using circular-grid quadrature, and numerically tests all three asymptotic constants. Run `python verify.py` with the dependency in `requirements.txt`. The complete analytical proof is above; the finite checks do not certify the infinite asymptotic statements by themselves.

## Relationship to prior work

Aistleitner, Hörmann and Manskova (2026) define precisely this number-variance statistic and derive its expectation, exact variance and first-order microscopic estimates; their Section 6, Lemma 10 and equation (17) are especially relevant. The displayed third cumulant and its positive-skewness crossover are not contained in their first- and second-moment calculations. The repeated-edge/triangle expansion employs standard degenerate U-statistic reasoning rather than claiming that framework as new. Jammalamadaka and Penrose (2000), Section 3, establish Poisson limits for short interpoint distances; such process-level limits can yield leading sparse-limit moments after appropriate uniform-integrability work but do not give the exact finite-\(n\) polynomial with its triangle contribution and entire crossover. This is an explicit, non-asymptotic third-order complement to those results, not a new Poisson-process theorem.

## Limitations

The formula is restricted to independent uniform circle samples and \(s\le1/3\). Finite-grid checks supplement but cannot prove symbolic integration or all-\(n\) claims. The nonzero third cumulant rules out an exactly Gaussian finite-dimensional number-variance law, but the vanishing skewness in some regimes **does not by itself prove** asymptotic normality or a Berry–Esseen rate. An older general diagram-cumulant identity may offer an alternative derivation; priority for the evaluated closed form is subject to independent literature review.

## References

1. C. Aistleitner, S. Hörmann and M. Manskova, *On the asymptotic behavior of the number variance of random points on the unit torus*, arXiv:2610.11687v1 (first posted 8 October 2026), especially Lemma 10 and equation (17). https://arxiv.org/html/2610.11687v1
2. S. R. Jammalamadaka and M. D. Penrose, *Poisson limits for pairwise and area interaction point processes*, Advances in Applied Probability **32** (2000), 75–85, DOI:10.1239/AAP/1013540023, Section 3.
