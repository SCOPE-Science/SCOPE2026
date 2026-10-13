# Negative peak–area covariance and a square-root regression slope for uniform Dyck excursions

## Finding
For each integer \(n\ge1\), sample uniformly among all Dyck excursions of semilength \(n\). Let \(P_n\) be the number of peaks, and let \(S_n\) be the sum of all step-start heights. Write \(B_n=\binom{2n}{n}\) and \(C_n=B_n/(n+1)\). Then
\[
\operatorname{Cov}(P_n,S_n)=\frac{n+1}{2}-\frac{(n+1)4^{n-1}}{B_n}.
\]
The covariance vanishes for \(n=1\) and is strictly negative for every \(n\ge2\). The exact least-squares affine regression slope of \(S_n\) on \(P_n\), for \(n\ge2\), is
\[
\beta_n=\frac{2n-1}{n-1}\left(2-\frac{4^n}{B_n}\right),
\quad \beta_n\sim-2\sqrt{\pi n}.
\]
In particular \(\operatorname{Cov}(P_n,S_n)\sim-(\sqrt\pi/4)n^{3/2}\) as \(n\to\infty\).

## Assumptions and scope
A Dyck excursion is a word of \(n\) up-steps \(U=(1,1)\) and \(n\) down-steps \(D=(1,-1)\), starting and ending at height zero, never visiting a negative height. All \(C_n\) admissible words have equal weight. A peak is an adjacent \(UD\) factor. For a path with successive heights \(H_0,\ldots,H_{2n}\), the area \(S_n\) is \(\sum_{j=0}^{2n-1}H_j\), with no Brownian normalization. For example, the length-four excursion \(UUDD\) has \(P_2=1\) and \(S_2=4\); \(UDUD\) has \(P_2=2\) and \(S_2=2\).

## Proof
Subtract the deterministic baseline and put \(Q_n=S_n-n\). Under the unique first-return decomposition \(W=UVDX\) with interior Dyck word \(V\) and subsequent Dyck word \(X\), \(Q(W)=Q(V)+Q(X)+2|V|_U\) and \(P(W)=P(V)+P(X)+\mathbf1_{\{V=\varnothing\}}\). These recursions include the empty word, whose area and peak count are zero.

Define formal series \(F(z,t)=\sum_W z^{|W|_U}t^{P(W)}\) and \(G(z,t)=\sum_W Q(W)z^{|W|_U}t^{P(W)}\), summing over all Dyck words. First return gives
\[
F=1+zF(F+t-1),\qquad
G=z\{G(2F+t-1)+2zF_zF\}.
\]
Let \(J=1-z(2F+t-1)\). Differentiating the first equation with respect to \(z\) gives \(F_z=F(F+t-1)/J\), whence
\[
G=\frac{2z^2F^2(F+t-1)}{J^2}.
\]
Set \(s=\sqrt{1-4z}\). At \(t=1\) we have \(F=2/(1+s)\), \(J=s\), and differentiation of the displayed expression in \(t\) yields the following exact formal-series identities:
\[
G(z,1)=\frac4{1+s}-\frac3s+\frac1{s^2},
\]
\[
\left.\frac{\partial G(z,t)}{\partial t}\right|_{t=1}
=-\frac14+\frac3{4s}-\frac1{4s^2}-\frac3{4s^3}+\frac1{2s^4}.
\]
For every \(n\ge1\), use \([z^n]s^{-1}=B_n\), \([z^n]s^{-2}=4^n\), \([z^n]s^{-3}=(2n+1)B_n\), \([z^n]s^{-4}=(n+1)4^n\), and \([z^n]2F(z,1)=2C_n\), to obtain
\[
\sum_W Q(W)=4^n-\frac{3n+1}{n+1}B_n,
\quad
\sum_W P(W)Q(W)=\frac{2n+1}{4}4^n-\frac{3n}{2}B_n.
\]
Here both sums range over paths of semilength \(n\). The Narayana peak distribution gives \(\mathbb E P_n=(n+1)/2\) and \(\operatorname{Var}(P_n)=(n^2-1)/(4(2n-1))\). Because \(S_n=Q_n+n\), the covariance with \(S_n\) equals the covariance with \(Q_n\). Substitution and cancellation give
\[
\operatorname{Cov}(P_n,S_n)
=\frac{1}{C_n}\left(\frac{B_n}{2}-4^{n-1}\right)
=\frac{n+1}{2}-\frac{(n+1)4^{n-1}}{B_n}.
\]
For \(n\ge2\), the ratio \(B_n/4^n=\prod_{j=1}^n(2j-1)/(2j)\) is strictly less than \(1/2\), proving negativity; the \(n=1\) case is equality. Dividing by the Narayana variance proves the regression formula. Finally Stirling's approximation \(B_n\sim4^n/\sqrt{\pi n}\) gives the asserted asymptotic coefficients. All statements are exact for the stated integer ranges and do not depend on sampled or truncated paths.

## Verification
The accompanying `verify_dyck.py` independently generates every Dyck excursion through semilength \(12\), reconstructs the peak count and unscaled area from the steps, and checks the path count, peak mean and variance, first area moment, peak–area mixed moment, and exact covariance using rational arithmetic. Execute `python3 verify_dyck.py`. This checks \(290{,}511\) paths in all. The proof above, rather than the bounded calculation, establishes the universal result.

## Relationship to prior work
Mansour (2002) enumerated fixed-height peaks of Dyck paths. Mansour (2006) developed generating functions for particular step patterns. Blanco and Petersen (2012) enumerated area jointly with **a different rank statistic** induced by a particular noncrossing-partition bijection; they explicitly distinguish that rank from ordinary peak count. Flórez et al. (2021) treat peak counts and area for families with restrictions on successive valley heights, with the two marginals handled separately. The classical Narayana peak distribution and the Carlitz–Riordan area method are inputs, not new claims. The result here is the explicit mixed covariance, its strict sign, and the least-squares slope for *unrestricted uniform* Dyck excursions.

## Limitations
The result determines a second mixed moment, not the complete conditional law of area given peaks or an optimal nonlinear predictor. Earlier enumerative methods can make the mixed covariance algebraically derivable; independent historical-priority review has not been performed. One older broadly titled enumeration paper by Deutsch (1999) was not fully accessible, leaving a nonzero risk of implicit coverage. The unscaled discrete area must not be confused with a Brownian-excursion normalization.

## References
- T. Mansour, *Counting peaks at height k in a Dyck path*, arXiv:math/0203222 (first posted 21 March 2002), https://arxiv.org/abs/math/0203222.
- T. Mansour, *Statistics on Dyck paths* (manuscript dated 15 January 2006), https://cfc.nankai.edu.cn/_upload/article/files/c6/e1/a2c52bf04b1896f59003b5993582/3502d3e1-d1ee-4754-bccc-60fbd68ee709.pdf.
- S. A. Blanco and T. K. Petersen, *Counting Dyck paths by area and rank*, arXiv:1206.0803 (first posted 5 June 2012), https://arxiv.org/abs/1206.0803.
- R. Flórez et al., *Restricted Dyck paths on valleys sequence*, arXiv:2108.08299 (first posted 17 August 2021), https://arxiv.org/abs/2108.08299.
- E. Deutsch, *Dyck path enumeration*, Discrete Mathematics 204 (1999), 167–202, DOI:10.1016/S0012-365X(98)00371-9 (historical scope not fully checked).
