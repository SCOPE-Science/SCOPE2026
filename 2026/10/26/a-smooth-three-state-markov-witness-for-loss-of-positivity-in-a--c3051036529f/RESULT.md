# A smooth three-state Markov witness for loss of positivity in a third-order Magnus integrator

## Finding

For the seven-exponential third-order commutator-free Magnus method (3.19) displayed in arXiv:2102.08242 by Blanes, Iserles, and Macnamara, there exists one bounded \(C^3\) time-dependent three-state Markov generator \(A:\mathbb R\to\mathbb R^{3\times3}\), with initial state \(y(0)=e_1\), such that at every step size
\[
h_n=10^{-1}100^{-(n-1)},\qquad n\ge1,
\]
the method's one-step output from time zero has third coordinate
\[
\widehat y_3(h_n)=\frac{C-\exp(c s_n)-c\exp(-s_n)}{C}<0,
\qquad s_n=h_n^5/2,\quad C=2\sqrt3/3,\quad c=C-1.
\]
The exact solution stays in the probability simplex for \(t\ge0\). The negative coordinate is \(-c h_n^{10}/8+O(h_n^{15})\). This defect does not contradict third-order convergence.

## Assumptions and scope

For column-vector dynamics \(y'=A(t)y\), the Markov generator convention is nonnegative off-diagonal entries and zero column sums. Define
\[
G_{12}=\begin{pmatrix}-1&0&0\\1&0&0\\0&0&0\end{pmatrix},\qquad
G_{23}=\begin{pmatrix}0&0&0\\0&-1&0\\0&1&0\end{pmatrix}.
\]
Let \(b_-=1/2-\sqrt3/6\), \(b_+=1/2+\sqrt3/6\), \(\delta=1/50\), and let \(\psi\in C^\infty(\mathbb R)\) be nonnegative, supported in \([-1,1]\), with \(\psi(0)=1\). For example use \(e\exp[-1/(1-u^2)]\) on \(|u|<1\) and zero elsewhere. On all of \(\mathbb R\), define the single generator
\[
A(t)=\sum_{n\ge1}h_n^4\left[\psi\!\left(\frac{t-b_-h_n}{\delta h_n}\right)G_{12}
+\psi\!\left(\frac{t-b_+h_n}{\delta h_n}\right)G_{23}\right].
\]
In particular \(A=0\) for \(t\le0\), so the negative abscissa printed in (3.19) is in the domain. The generator is independent of which test step is chosen.

## Proof

**Regularity and exact flow.** The two pulse intervals on a scale are disjoint. Adjacent scales are disjoint since \((b_++\delta)/100<b_--\delta\); all supports lie in \((0,1)\). They are locally finite off zero. On a pulse at scale \(h_n\), \(t\ge(b_--\delta)h_n\), and the \(k\)-th derivative has norm \(O(h_n^{4-k})=O(t^{4-k})\) for \(k\le3\). These bounds give zero derivatives at the origin through order three, by successive difference quotients, and continuity there. Thus \(A\) is bounded and \(C^3\) on the line. Both generator coefficients are nonnegative. If they are denoted by \(a(t),b(t)\), the exact triangular flow has \(y_1(t)=\exp(-\int_0^t a)\), \(y_2(t)=\int_0^t a(u)y_1(u)\exp(-\int_u^t b)\,du\), and \(y_3(t)=\int_0^t b(u)y_2(u)\,du\). All are nonnegative, and the zero column sums conserve mass.

**Stage samples.** In the preprint's display (3.19), the first six sample fractions are
\[
d_0=\frac16-\frac{\sqrt3}{12},\quad \frac1{12},\quad -d_0,\quad
\frac13-\frac{\sqrt3}{6},\quad \frac16,\quad \frac13+\frac{\sqrt3}{6}.
\]
The final two fractions are \(b_-,b_+\). The negative sample is zero, and \(d_0\) is the smallest positive sample. All pulses at smaller scales lie below \((b_++\delta)h_n/100<d_0h_n\), and all larger ones above \(100(b_--\delta)h_n>h_n\). At scale \(h_n\), each of the first six fractions is at distance more than \(\delta\) from each of \(b_-,b_+\). The same check works if the upper in-interval half-step Gauss node \(1/6+\sqrt3/12\) is used in place of \(-d_0\). With either abscissa the first five stage exponentials therefore have zero arguments. Since \(A\) depends on time only, the remaining two samples are \(\mathcal B_1=h_n^4G_{12}\), \(\mathcal B_2=h_n^4G_{23}\).

**Stage order and sign.** Write \(\alpha=1/2+\sqrt3/3\), \(\beta=1/2-\sqrt3/3\), so \(\alpha+\beta=1\), \(C=\alpha-\beta\), \(c=-2\beta\). Formula (3.19) first forms \(x_6=\exp[(h_n/2)(\alpha\mathcal B_2+\beta\mathcal B_1)]e_1\), then applies \(\exp[(h_n/2)(\beta\mathcal B_2+\alpha\mathcal B_1)]\) to \(x_6\). Thus the column-vector product is
\[
\widehat y(h_n)=e^{s_n(\beta G_{23}+\alpha G_{12})}
                e^{s_n(\alpha G_{23}+\beta G_{12})}e_1.
\]
For a single stage \(e^{s(a G_{12}+b G_{23})}\) with \(a\ne b\), the first two coordinates transform as
\[
(y_1,y_2)\mapsto\left(e^{-as}y_1,\ e^{-bs}y_2+
\frac{a}{a-b}(e^{-bs}-e^{-as})y_1\right).
\]
With \(U=e^{-\beta s_n}\), \(V=e^{-\alpha s_n}\), the first stage gives \((U,\beta(U-V)/C)\). The second gives \((UV,U^2/C-UV/C)\) because \(\alpha+\beta=1\). Column sums conserve total mass even in these signed stages. Using \(UV=e^{-s_n}\), \(U^2=e^{cs_n}\) gives the stated formula for \(\widehat y_3\). The function \(e^{cs}+ce^{-s}-(1+c)\) vanishes at zero and has derivative \(c(e^{cs}-e^{-s})>0\) for \(s>0\). Its Taylor expansion starts with \(cC s^2/2\), giving \(-ch_n^{10}/8+O(h_n^{15})\) for the third coordinate.

## Verification

The proof uses the chronological order displayed in (3.19), with the negative sample allowed by the stated domain. The standalone `verify.py` checks the ordered triangular stages against the closed coordinate formulas with high-precision Python decimal arithmetic and checks that the reversed order instead gives a positive third coordinate. These checks are finite diagnostics; the separation and sign arguments above apply to all \(n\).

## Relationship to prior work

Blanes, Iserles, and Macnamara give the integrator and warn that positivity is conditional on weighted combinations of sampled graph Laplacians retaining the generator sign pattern. The negative coefficient alone does not establish the statement here, which requires exact negativity on arbitrarily small steps on one fixed bounded \(C^3\) generator. The related 2020 paper addresses a different, fourth-order commutator-free Magnus method.

## Limitations

This is a counterexample to exact nonnegativity, not a quantitative instability result or a loss of formal order. The violation is very small at the specified scales, and negativity is not asserted at every sufficiently small step or for every smooth generator. Publication priority beyond the cited context is not claimed.

## References

1. S. Blanes, A. Iserles, and S. Macnamara, “Positivity-preserving methods for ordinary differential equations,” *ESAIM: Mathematical Modelling and Numerical Analysis* 56 (2022), 1843–1870, DOI: 10.1051/m2an/2022042. See arXiv:2102.08242, §3.5, especially the displayed stages (3.19).
2. S. MacNamara, S. Blanes, and A. Iserles, “Simulation of bimolecular reactions: Numerical challenges with the graph Laplacian,” *ANZIAM Journal* 61 (2020), C59–C74. DOI: 10.21914/anziamj.v61i0.15169.
