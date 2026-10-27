# Strict run-count likelihood ordering and exact parity compression for symmetric Pólya urns

## Finding
For every integer \(n\ge2\), draw \(P\sim\operatorname{Beta}(\alpha,\alpha)\) with \(\alpha>0\), then conditionally on \(P\), draw \(n\) independent Bernoulli observations. Write \(R=1+\sum_{i=1}^{n-1}\mathbf1\{X_i\ne X_{i+1}\}\) for the total number of constant-symbol runs. For every \(0<\alpha<\beta\) and \(1\le r<n\),
\[
\Pr_\beta(R=r+1)\Pr_\alpha(R=r)-\Pr_\beta(R=r)\Pr_\alpha(R=r+1)
\begin{cases}>0,&r\text{ odd},\\=0,&r\text{ even}.\end{cases}
\]
Thus the entire run count is ordered in monotone likelihood-ratio order as the common beta concentration increases. The equality steps are universal: for every exchangeable binary sequence, with arbitrary exchangeable law, and every \(1\le j\) with \(2j+1\le n\),
\[
\Pr(R=2j+1)=\frac{n-2j}{2j}\Pr(R=2j).
\]
In the beta family the statistic \(B=\lfloor R/2\rfloor\) is a **minimal sufficient coarsening of the observed run count** for the concentration parameter: within the pair \(R=2j,2j+1\), the conditional relative probabilities are \(2j/n\) and \((n-2j)/n\), independently of \(\alpha\). The singleton \(R=1\) and any terminal singleton are retained. All distinct \(B\)-classes are separated by strictly varying likelihood ratios.

## Assumptions and scope
The length \(n\) is fixed and known; the initial concentrations are equal and strictly positive; samples are conditionally independent given their common random success probability. Equivalently, the sequence follows a symmetric two-color Pólya–Eggenberger reinforcement urn with unit reinforcement, interpreted via beta mixing for arbitrary real \(\alpha>0\). Here \(\Pr_\alpha\) refers only to the law at concentration \(\alpha\). Every one of the \(n\) possible run counts has positive mass. The order is *likelihood-ratio* ordering; it implies ordinary stochastic ordering, but the converse is not asserted. The parameter \(\alpha\) is not identified from a single binary word with certainty; sufficiency is relative to the reduced experiment observing \(R\), not to the full observed word.

## Proof
Define \(K=\sum_i X_i\) and \(H=\min\{K,n-K\}\), so \(0\le H\le m=\lfloor n/2\rfloor\). Set \(d_h=2\) for \(2h<n\) and \(d_{n/2}=1\) when \(n\) is even. Exchangeability and beta mixing give
\[
W_\alpha(h)=\Pr_\alpha(H=h)=d_h{n\choose h}\frac{(\alpha)^{\overline h}(\alpha)^{\overline{n-h}}}{(2\alpha)^{\overline n}},
\]
where \((a)^{\overline q}=\prod_{t=0}^{q-1}(a+t)\). For \(0\le h<m\), the successive ratio is
\[
\frac{W_\alpha(h+1)}{W_\alpha(h)}
=\frac{d_{h+1}}{d_h}\frac{n-h}{h+1}\frac{\alpha+h}{\alpha+n-h-1}.
\]
The final fraction has derivative \((n-2h-1)/(\alpha+n-h-1)^2>0\); hence for every \(\alpha<\beta\), the folded-count weights obey \(W_\beta(h+1)W_\alpha(h)>W_\beta(h)W_\alpha(h+1)\) for all \(h<m\). Their full matrix has strict positive \(2\)-minors in the ordered columns \(h\).

Conditional on \(H=h\), the ordering of the \(n\) symbols is uniform on compositions with that count; complementing all symbols does not change \(R\). For \(1\le h\le m\), the number \(A_h(r)\) of words with exactly \(h\) ones and \(n-h\) zeros and \(r\) total runs equals
\[
A_h(2j)=2{h-1\choose j-1}{n-h-1\choose j-1},\quad
A_h(2j+1)={h-1\choose j}{n-h-1\choose j-1}+{h-1\choose j-1}{n-h-1\choose j},
\]
where out-of-range binomial coefficients vanish. At \(h=0\), only \(A_0(1)=1\) is nonzero. Indeed, an even number of runs gives \(j\) runs of each color, with two possible starting colors; an odd number gives \(j+1\) of one color and \(j\) of the other. Thus \(\sum_r A_h(r)={n\choose h}\), and \(M(h,r)=A_h(r)/{n\choose h}\) is the conditional transition kernel from \(H\) to \(R\).

The two adjacent kernel ratios simplify, whenever their denominators are positive, to
\[
\frac{A_h(2j+1)}{A_h(2j)}=\frac{n-2j}{2j},\qquad
\frac{A_h(2j+2)}{A_h(2j+1)}=\frac{2(h-j)(n-h-j)}{j(n-2j)}.
\]
The first is constant in \(h\); the second is increasing in \(h\le\lfloor n/2\rfloor\), since \((h-j)(n-h-j)\) has forward difference \(n-2h-1\ge0\) in the relevant range. Positivity sets of successive columns are nested final segments in \(h\); \(A_0(1)=1\) alone handles the initial transition. Therefore \(M\) is totally positive of order two. Each transition \(r=2j+1\) to \(r+1=2j+2\) has a positive minor using \(h=j,j+1\), and transition \(r=1\) to \(r=2\) has a positive minor using \(h=0,1\). All transitions from \(r=2j\) to \(r=2j+1\) are proportional column pairs.

Now \(\Pr_\alpha(R=r)=\sum_{h=0}^mW_\alpha(h)M(h,r)\). For \(\alpha<\beta\), expand the determinant of two successive run-probability columns by the Cauchy–Binet identity:
\[
\Pr_\beta(R=r+1)\Pr_\alpha(R=r)-\Pr_\beta(R=r)\Pr_\alpha(R=r+1)
=\sum_{h<h'}\bigl[W_\alpha(h)W_\beta(h')-W_\beta(h)W_\alpha(h')\bigr]
\bigl[M(h,r)M(h',r+1)-M(h,r+1)M(h',r)\bigr].
\]
All summands are nonnegative; an explicit pair is positive at odd \(r\); at even \(r\) the kernel columns are proportional, so the whole determinant is zero. This establishes the advertised sharp likelihood-ratio order.

Because the even-to-odd kernel proportionality holds for every fixed success count, it holds under any exchangeable mixture without requiring symmetry or a beta prior. The stated conditional probabilities within each two-element \(B\)-class follow by normalization. Consequently the conditional distribution of \(R\) given \(B=\lfloor R/2\rfloor\) does not depend on \(\alpha\), which is sufficiency for the reduced experiment. Conversely, every two distinct \(B\)-classes are separated by at least one strictly positive adjacent determinant, so their likelihood ratio is not constant as \(\alpha\) varies. By the finite-support likelihood-ratio criterion, \(B\) is minimal sufficient within the experiment observing \(R\). Finally, conditional beta-binomial mixing gives \(\Pr(X_i\ne X_{i+1})=\alpha/(2\alpha+1)\), yielding
\[\mathbb E_\alpha R=1+(n-1)\frac{\alpha}{2\alpha+1}.\]

## Verification
An accompanying standalone Python 3 exact-arithmetic checker independently enumerates every binary word of length \(2\le n\le11\), compares composition counts, verifies all \(7980\) ordered \(2\)-minors of the conditional run kernel for \(2\le n\le14\), and verifies \(364\) adjacent likelihood-ratio determinants at rational positive beta concentrations (\(196\) strict), as well as exact mean identities. Fraction arithmetic uses no tolerances. These finite checks corroborate but do not replace the proof valid for every \(n\) and every real \(\alpha>0\).

## Relationship to prior work
Makri–Philippou–Psillakis (2007) establish Pólya-urn success-run distributions and conditional composition formulas; Eryilmaz (2008) develops joint multicolor run distributions. Both provide distributional antecedents, not an implication of the concentration-indexed strict likelihood-ratio theorem or the lossless parity pairing. Goldstein–Reinert (arXiv:1207.1460v1, 2012-07-05 UTC) studies beta/urn approximations rather than run ordering. Eryilmaz (2018), by available abstract and first-page preview, treats stochastic comparisons of different success-run schemes for exchangeable trials, including beta-binomial examples; its full proof text was not accessible for exact implication checking. Schuster (1991) and Eryilmaz–Demir (2007) study exchangeable-run distribution formulas; their full texts were not established accessible. Literature overlap was assessed by *statements*, not merely by article titles. No claim of universally exhaustive priority is made.

## Limitations
Symmetry of the beta prior is essential to the proved strict ordering of folded success counts; an arbitrary asymmetric beta prior is not covered. The parity identity alone holds for all exchangeable binary laws. Nonexchangeable dependence, random observation length, and multicolor models are not included. A narrowly relevant later ordering paper has only partial accessible text; mathematical correctness here does not settle external historical priority. Minimal sufficiency is for the run-count observation alone, not for the full binary sample. The exact checker handles finitely many sizes and rational parameters; all-parameter generality rests on the displayed analytic proof.

## References
1. F. S. Makri, A. N. Philippou, and Z. M. Psillakis, “Success run statistics defined on an urn model,” *Advances in Applied Probability* **39** (2007), 991–1019. DOI: 10.1239/aap/1198177236.
2. S. Eryilmaz, “Run statistics defined on the multicolor urn model,” *Journal of Applied Probability* **45** (2008), 1007–1023. DOI: 10.1239/jap/1231340230.
3. L. Goldstein and G. Reinert, “Stein's method for the Beta distribution and the Pólya–Eggenberger urn,” arXiv:1207.1460v1, first public 2012-07-05 UTC; later *Journal of Applied Probability* **50** (2013), 1187–1205.
4. S. Eryilmaz, “Stochastic ordering among success runs statistics in a sequence of exchangeable binary trials,” *Methodology and Computing in Applied Probability* **20** (2018), 563–573. DOI: 10.1007/s11009-017-9576-1.
5. E. F. Schuster, “Distribution theory of runs via exchangeable random variables,” *Statistics & Probability Letters* **11** (1991), 379–386. DOI: 10.1016/0167-7152(91)90185-T.
6. S. Eryilmaz and S. Demir, “Success runs in a sequence of exchangeable binary trials,” *Journal of Statistical Planning and Inference* **137** (2007), 2954–2963. DOI: 10.1016/j.jspi.2006.10.015.
