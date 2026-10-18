# Two-shell Walsh tight sampling and the first arithmetic support transition

## Finding
On the Boolean cube \(\{-1,1\}^n\), let \(\mathcal W_1=\operatorname{span}\{1,x_1,\ldots,x_n\}\) be the first Walsh band. A permutation-invariant sampling measure supported on two different *complete* Hamming-weight shells makes the displayed \(n+1\) Walsh characters orthonormal exactly when \(n\) is odd or divisible by four. All such measures have an explicit divisor parametrization.

For odd \(n\), the minimum number of distinct measured vertices is
\[
M(n)=\min_{s\mid n,\ s>0}\left[\binom n{(n-s)/2}+\binom n{(n-n/s)/2}\right].
\]
The first odd dimension where \(M(n)\) is strictly smaller than \(1+\binom n{(n-1)/2}\) is \(n=51\). Its unique optimal unordered shell pair is \(\{24,34\}\), containing exactly \(244362982488625\) vertices, compared with \(247959266474053\) vertices in the baseline construction. The improvement holds for every \(n\equiv3\pmod6\) with \(n\ge51\).

## Assumptions and scope
Fix an integer \(n\ge3\). The weight-\(k\) shell \(H_k\) consists of vectors having exactly \(k\) negative coordinates. Sampling uses all vertices in two distinct shells \(H_k,H_\ell\), with strictly positive and equal per-vertex weights within each shell (weights may differ between shells). The weights sum to one. Tightness here means \(\int f\overline g\,d\mu=\langle f,g\rangle_{\text{uniform cube}}\) for every \(f,g\in\mathcal W_1\), equivalently the Gram matrix of the standard basis \(1,x_1,\ldots,x_n\) is the identity. This does not minimize over arbitrary irregular subsets or arbitrary within-shell weights.

## Proof
Write \(S(x)=\sum_{j=1}^n x_j=n-2k\) on \(H_k\). Coordinate-permutation invariance gives, for distinct \(i,j\),
\[
\mathbb E_\mu x_i=\frac{\mathbb E_\mu S}{n},\qquad
\mathbb E_\mu x_i x_j=\frac{\mathbb E_\mu S^2-n}{n(n-1)}.
\]
Therefore the first Walsh Gram matrix equals the identity if and only if \(\mathbb E_\mu S=0\) and \(\mathbb E_\mu S^2=n\). For two shells the random variable \(S\) takes values \(s>0\) and \(-t<0\) with positive probabilities \(\alpha\) and \(1-\alpha\). The first equation gives \(\alpha=t/(s+t)\), and substituting in the second yields the exact factor condition \(st=n\). Conversely these conditions make all Gram entries correct.

Shell integrality is equivalent to \(s\equiv t\equiv n\pmod2\) with \(1\le s,t\le n\), with shell indices \(k=(n-s)/2\), \(\ell=(n+t)/2\). When \(n\) is odd every positive factorization \(st=n\) qualifies. When \(n\) is even both factors must be even, so \(4\mid n\); conversely, if \(4\mid n\), take \(s=2\) and \(t=n/2\). A single shell cannot give full rank because \(S\) is constant there, so at least two distinct shells are required for this symmetric recovery problem.

The union contains \(\binom n{(n-s)/2}+\binom n{(n+t)/2}=\binom n{(n-s)/2}+\binom n{(n-t)/2}\) points. For odd \(n\), put \(t=n/s\) and minimize over positive divisors \(s\) to obtain the exact formula. The baseline \(s=1,t=n\) uses \(1+\binom n{(n-1)/2}\) points. Exact integer evaluation of every factorization for odd \(3\le n\le49\) proves that the baseline is optimal in this range. At \(n=51\), the available factor pairs \((1,51)\) and \((3,17)\), up to reversal, give respectively \(247959266474053\) and \(244362982488625\) points; hence the latter pair is uniquely optimal up to reversal.

To show the improvement persists along all \(n=51+6j\), write \(n=6r+3\) and compare factor pair \((3,n/3)\) against \((1,n)\). Set
\[
R_r=\frac{\binom{6r+3}{2r+1}}{\binom{6r+3}{3r+1}}.
\]
The binomial identity
\[
\binom n{(n-3)/2}=\frac{n-1}{n+3}\binom n{(n-1)/2}
\]
shows that the interior pair is strictly better whenever \(R_r<4/(n+3)\). Direct integer comparison gives this strict inequality at \(n=51\) (\(r=8\)). For every integer \(r\ge0\), factorial cancellation gives
\[
\frac{R_{r+1}}{R_r}=\frac{9(3r+2)(3r+4)^2(3r+5)}{16(2r+3)^2(4r+3)(4r+5)}<\frac34.
\]
Indeed, the difference between \(3/4\) and the displayed ratio is exactly
\[
\frac{3(13r^4+65r^3+138r^2+144r+60)}{16(2r+3)^2(4r+3)(4r+5)}>0.
\]
Since \(3(n+9)<4(n+3)\) for \(n>15\), the bound \(R_r<4/(n+3)\) propagates under \(n\mapsto n+6\). Thus every odd multiple of three at least \(51\) admits a strictly smaller tight two-shell design than the central-shell-plus-pole baseline. The divisor minimum remains exact in all dimensions; no assertion is made that \((3,n/3)\) globally minimizes for all large \(n\).

## Verification
The standalone `check.py` performs exact rational Gram calculations for all possible admissible shell pairs through dimension ten, including direct enumeration of cube vectors through dimension eight. It checks every odd dimension through \(51\) by exact binomial integers, verifies the first strict improvement, and verifies the polynomial identity proving the all-dimensions contraction estimate. Run `python3 check.py`; output is recorded in `check_output.txt`. The infinite theorem follows from the algebra above, not the finite enumeration alone.

## Relationship to prior work
The theory of weighted relative designs on Hamming shells is developed by Bannai, Bannai, Tanaka, and Zhu (arXiv:2006.02054, first public June 3, 2020). That paper studies Fisher bounds and coherent configurations for *tight relative designs* on two shells; the full-shell Walsh Gram-identity problem and its support-cost arithmetic transition do not appear in the inspected results. Zhu (2021, DOI below) develops nonbinary relative design theory; accessible material supplies only the abstract and first page, not a decisive full-text exclusion. Known single-shell first-Walsh-band concentration results concern a different, intrinsically rank-deficient restriction. Our positive-weighted full two-shell conditions restore every direction and optimize sample count among permutation-invariant full-shell designs.

## Limitations
The optimization is restricted to *complete* shell unions with uniform weights per shell; smaller irregular tight cubature sets may exist. The all-dimension formula is an exact divisor minimum rather than a closed-form minimizing divisor for every odd \(n\). The infinite improvement claim concerns the baseline, not proof of global optimal divisor pair on the entire progression. Originality is assessed against inspected and searchable literature, not independently certified.

## References
1. E. Bannai, E. Bannai, H. Tanaka, Y. Zhu, *Tight relative \(t\)-designs on two shells in hypercubes, and Hahn and Hermite polynomials*, arXiv:2006.02054, first submitted June 3, 2020; later Ars Mathematica Contemporanea 22 (2022), P2.01. https://arxiv.org/abs/2006.02054
2. Y. Zhu, *Relative t-Designs in Nonbinary Hamming Association Schemes*, Graphs and Combinatorics 37 (2021), 1775–1791. https://doi.org/10.1007/s00373-021-02389-4
