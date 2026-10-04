# Fourth-moment universality between real Gaussian hafnians and Pfaffians
## Finding
For every integer \(n\ge 1\), let \(S_n\) be a \(2n\times 2n\) real symmetric matrix with zero diagonal and independent \(N(0,1)\) entries above the diagonal, and define \(H_n=\operatorname{haf}(S_n)\). Then
\[
\mathbb E H_n^2=(2n-1)!!,
\qquad
\mathbb E H_n^4=(2n+1)\bigl((2n-1)!!\bigr)^2.
\]
Consequently the RMS-normalized variable \(\widehat H_n=H_n/\sqrt{(2n-1)!!}\) has Pearson kurtosis
\[
\mathbb E\widehat H_n^4=2n+1,
\]
excess kurtosis \(2n-2\), and
\[
\frac{\operatorname{Var}(H_n^2)}{(\mathbb E H_n^2)^2}=2n.
\]
If \(\mathrm{Pf}_n\) denotes the Pfaffian of a \(2n\times2n\) real skew-symmetric Gaussian matrix with independent \(N(0,1)\) entries above the diagonal, then \(H_n\) and \(\mathrm{Pf}_n\) have the same first four centered moments for every \(n\).

## Assumptions and scope
The matrix entries above the diagonal are mutually independent, centered, unit-variance real Gaussians. The diagonal of \(S_n\) is irrelevant to the hafnian and is set to zero. The claim concerns the independent-entry real symmetric Gaussian hafnian, not a finite-row Gram hafnian, and concerns moments through order four only. The Pfaffian comparison uses the corresponding independent-entry real skew-symmetric Gaussian model.

## Proof
Write the perfect-matching expansion along vertex \(1\) as
\[
H_n=\sum_{j=2}^{2n} X_{1j}A_j,
\]
where \(A_j\) is the hafnian of the induced matrix obtained by deleting vertices \(1\) and \(j\). Conditional on all entries not incident to vertex \(1\), the variables \(X_{1j}\) are independent standard Gaussians and therefore
\[
H_n\mid (A_2,\ldots,A_{2n})\sim N(0,V),
\qquad
V=\sum_{j=2}^{2n}A_j^2.
\]
Let \(M_n=\mathbb E H_n^4\). The conditional Gaussian fourth moment gives
\[
M_n=3\,\mathbb E V^2.
\]
Each \(A_j\) has the same law as \(H_{n-1}\), so the diagonal terms in \(\mathbb E V^2\) contribute \((2n-1)M_{n-1}\).

For distinct \(j,k\), put \(R=\{2,\ldots,2n\}\setminus\{j,k\}\). For \(\ell\in R\), let \(B_\ell\) be the hafnian on the vertex set \(R\setminus\{\ell\}\). Expanding \(A_j\) along vertex \(k\) and \(A_k\) along vertex \(j\) gives
\[
A_j=\sum_{\ell\in R}X_{k\ell}B_\ell,
\qquad
A_k=\sum_{\ell\in R}X_{j\ell}B_\ell.
\]
Conditional on the entries internal to \(R\), the two displayed Gaussian sums are independent and both have variance
\[
U=\sum_{\ell\in R}B_\ell^2.
\]
Hence \(\mathbb E[A_j^2A_k^2]=\mathbb E U^2\). Now take an independent real symmetric Gaussian hafnian of order \(n-1\) on a vertex set consisting of one new vertex together with \(R\), and expand it along the new vertex. Conditional on the entries internal to \(R\), its variance is exactly \(U\), so
\[
M_{n-1}=3\,\mathbb E U^2.
\]
Thus, for every ordered pair \(j\ne k\),
\[
\mathbb E[A_j^2A_k^2]=\frac{M_{n-1}}3.
\]
There are \((2n-1)(2n-2)\) such ordered pairs. Therefore
\[
\begin{aligned}
M_n
&=3\left((2n-1)M_{n-1}+(2n-1)(2n-2)\frac{M_{n-1}}3\right)\\
&=(2n-1)(2n+1)M_{n-1}.
\end{aligned}
\]
Since \(H_1\) is standard normal, \(M_1=3\). Iterating gives
\[
M_n=(2n+1)\bigl((2n-1)!!\bigr)^2.
\]
The same first-vertex conditioning gives the second-moment recurrence \(\mathbb E H_n^2=(2n-1)\mathbb E H_{n-1}^2\), with base value \(1\), proving \(\mathbb E H_n^2=(2n-1)!!\).

The law of \(H_n\) is symmetric: changing the signs of all entries incident to one fixed vertex preserves the matrix law and changes the sign of every perfect-matching monomial. Hence its first and third centered moments vanish. For the Gaussian Pfaffian, the independent-product law
\[
\mathrm{Pf}_n\stackrel{d}=Z\prod_{r=2}^n\chi_{2r-1}
\]
with independent \(Z\sim N(0,1)\) and chi variables gives
\[
\mathbb E\mathrm{Pf}_n^4
=3\prod_{r=2}^n(2r-1)(2r+1)
=(2n+1)\bigl((2n-1)!!\bigr)^2,
\]
and its second moment is \((2n-1)!!\). Its law is also symmetric. Thus the two models agree in centered moments through order four.

## Verification
The proof is finite and analytic for every \(n\ge1\). The only probabilistic identities used are conditional second and fourth moments of a centered Gaussian and independence of disjoint Gaussian edge sets. The mixed-cofactor identity is reduced to the same conditional-variance functional one order lower, so no enumeration or asymptotic passage is used. At \(n=1\) the formula gives Gaussian kurtosis \(3\); at \(n=2\) it gives kurtosis \(5\), consistent with the known equality in law of the symmetric hafnian and skew Pfaffian in that order.

## Relationship to prior work
Zhao, arXiv:2609.06526v1, defines this real symmetric Gaussian hafnian, proves its exact second moment and shifted anticoncentration, and compares its normalized density peak with the real Gaussian Pfaffian. The paper explicitly notes equality in law at orders \(n=1,2\), but its inspected full text contains no fourth-moment statement for the symmetric Gaussian hafnian. Its Appendix B.3 records the independent chi-product law for the Gaussian Pfaffian, which immediately supplies the Pfaffian fourth moment used only for the comparison above.

Zhao, arXiv:2608.17065v1, computes exact second and fourth absolute moments for a different object: a complex Gaussian Gram hafnian \(\operatorname{haf}(X^{\mathsf T}X)\). Its abstract and the later paper's discussion distinguish that finite-row complex Gram model from the independent-entry real symmetric limit treated here. The present recursion does not follow by substituting parameters into the published complex Gram formula.

Dumitriu and Forrester, arXiv:0904.2216v2, provide the antisymmetric Gaussian matrix reduction underlying the Pfaffian product benchmark. That benchmark covers the signed model, not the unsigned symmetric hafnian recurrence proved here.

## Limitations
No equality in distribution between \(H_n\) and \(\mathrm{Pf}_n\) is claimed for \(n\ge3\). The result does not identify the exact density peak of \(H_n\), its sixth or higher moments, or fourth moments for finite-row real Gram hafnians. It also does not transfer the formula to complex symmetric hafnians or to non-Gaussian entries.

## References
1. Hongru Zhao, *Shifted Anticoncentration for Real Gram Hafnians and Symmetric Gaussian Hafnians*, arXiv:2609.06526v1, 2026.
2. Hongru Zhao, *Exact Moments of Gaussian Gram Hafnians Reveal an \(n^2/\log n\) Threshold for Weak Anticoncentration*, arXiv:2608.17065v1, 2026.
3. Ioana Dumitriu and Peter J. Forrester, *Tridiagonal Realization of the Anti-Symmetric Gaussian \(\beta\)-Ensemble*, arXiv:0904.2216v2, 2010.
