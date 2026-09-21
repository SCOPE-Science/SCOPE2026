# Heterogeneous order-statistic marginals: pointwise recovery, label braiding, and analytic identification

## Statement

Let \(X_1,\ldots,X_n\) be independent real-valued random variables with CDFs \(F_1,\ldots,F_n\), and let \(X_{1:n}\le\cdots\le X_{n:n}\) be their order statistics. Suppose that, for every rank \(r=1,\ldots,n\), the marginal CDF
\[
H_r(x)=\Pr\{X_{r:n}\le x\}
\]
is known. No joint distribution of different ranks is assumed observed.

The following conclusions hold.

### 1. Exact pointwise recovery and observational equivalence

For every fixed \(x\), the data \(H_1(x),\ldots,H_n(x)\) determine the multiset
\[
\{F_1(x),\ldots,F_n(x)\}
\]
exactly, including multiplicities. Consequently, two independent heterogeneous samples have the same marginal distribution for every order statistic if and only if their parent CDFs have the same pointwise multiset at every \(x\).

Equivalently, the data identify the sorted CDF envelopes
\[
F_{[1]}(x)\le\cdots\le F_{[n]}(x),
\]
where \(F_{[j]}(x)\) is the \(j\)-th smallest value among \(F_1(x),\ldots,F_n(x)\). Each \(F_{[j]}\) is itself a CDF. These canonical envelopes need not coincide with any globally labeled parent CDF when parent CDFs cross.

### 2. A general unique-continuation identification principle

Let \(\mathcal C\) be a class of continuous CDFs with the interval-identity property:

> if \(F,G\in\mathcal C\) agree on a nonempty open interval, then \(F\equiv G\) on \(\mathbb R\).

If all parent CDFs belong to \(\mathcal C\), then the marginal laws of all \(n\) order statistics identify the collection \(\{F_1,\ldots,F_n\}\) up to one global permutation.

In particular, this holds when the parent CDFs are real analytic on \(\mathbb R\). Thus real-analytic heterogeneous parent laws are identifiable from the separate marginal laws of all ranks without stochastic-dominance ordering, separated support endpoints, or rank identities.

### 3. Complete two-parent ambiguity: label braiding at crossings

For \(n=2\), write the two parent CDFs as \(F,G\). The minimum and maximum marginals give
\[
H_{\min}=F+G-FG,\qquad H_{\max}=FG,
\]
so pointwise
\[
\{F,G\}=
\left\{
\frac{s-\sqrt{s^2-4p}}2,
\frac{s+\sqrt{s^2-4p}}2
\right\},
\qquad
s=H_{\min}+H_{\max},\ p=H_{\max}.
\]
Let
\[
U=\{x:F(x)\ne G(x)\}.
\]
Every continuous pair \((A,B)\) having the same minimum and maximum marginals is obtained by choosing, independently on each connected component of \(U\), either
\((A,B)=(F,G)\) or \((A,B)=(G,F)\), with the common value used on \(\{F=G\}\). Conversely every such componentwise choice gives two valid continuous CDFs with the same observed rank marginals.

Hence, if \(U\) has \(m<\infty\) connected components, there are exactly \(2^m\) ordered continuous representations and \(2^{m-1}\) representations modulo a global swap (for \(m\ge1\)). If \(U\) has infinitely many components, there are continuum-many representations.

### 4. Infinite smoothness does not restore identification

The analytic conclusion cannot be weakened to \(C^\infty\), even with full support, strictly positive smooth densities, and light tails.

Let
\[
L(x)=\frac1{1+e^{-x}}
\]
and define the flat compactly supported function
\[
q(x)=
\begin{cases}
\operatorname{sgn}(x)\exp(-1/x^2)\exp\!\bigl(-1/(1-x^2)\bigr),&0<|x|<1,\\
0,&x=0\ \text{or}\ |x|\ge1.
\end{cases}
\]
Both \(q\) and \(|q|\) are \(C^\infty\). For sufficiently small \(\varepsilon>0\), all four functions
\[
F_1=L+\varepsilon q,\quad F_2=L-\varepsilon q,
\qquad
G_1=L+\varepsilon|q|,\quad G_2=L-\varepsilon|q|
\]
are strictly increasing \(C^\infty\) CDFs with everywhere positive densities and logistic tails. Pointwise,
\[
\{F_1(x),F_2(x)\}=\{G_1(x),G_2(x)\}
\]
for every \(x\), but \(\{G_1,G_2\}\) is not a global permutation of \(\{F_1,F_2\}\): the labels switch across the flat crossing at \(0\). Thus the two models have identical minimum and maximum distributions. Appending the same additional parent CDFs to both constructions gives the same failure for every \(n\ge2\), even when every rank marginal is observed.

## Proof

Fix \(x\) and let
\[
N_x=\sum_{i=1}^n \mathbf 1\{X_i\le x\}.
\]
Then \(H_r(x)=\Pr(N_x\ge r)\). With the conventions \(H_0(x)=1\) and \(H_{n+1}(x)=0\), the entire Poisson-binomial mass function is therefore known:
\[
q_k(x)=\Pr(N_x=k)=H_k(x)-H_{k+1}(x),\qquad k=0,\ldots,n.
\]
Its probability-generating polynomial is
\[
Q_x(z)=\sum_{k=0}^n q_k(x)z^k
      =\prod_{i=1}^n\bigl(1-F_i(x)+F_i(x)z\bigr).
\]
Writing \(z=1+t\),
\[
Q_x(1+t)=\prod_{i=1}^n\bigl(1+F_i(x)t\bigr)
        =\sum_{j=0}^n e_j(x)t^j,
\]
so all elementary symmetric polynomials \(e_j(x)\) of the numbers \(F_i(x)\) are known. Hence the monic polynomial
\[
R_x(u)=u^n-e_1(x)u^{n-1}+e_2(x)u^{n-2}-\cdots+(-1)^ne_n(x)
      =\prod_{i=1}^n\bigl(u-F_i(x)\bigr)
\]
is known, proving exact recovery of the pointwise multiset and the equivalence characterization.

The sorted envelopes are CDFs because a finite order statistic of coordinatewise nondecreasing right-continuous functions is again nondecreasing and right-continuous, with limits \(0\) and \(1\).

For the interval-identity result, suppose another collection \(G_1,\ldots,G_n\in\mathcal C\) has the same rank marginals. The first result gives pointwise multiset equality. Fix \(i\). The closed sets
\[
A_j=\{x:G_i(x)=F_j(x)\},\qquad j=1,\ldots,n,
\]
cover \(\mathbb R\). By the Baire category theorem, at least one \(A_j\) has nonempty interior. The interval-identity property then gives \(G_i\equiv F_j\). Remove this common member from both multisets and repeat inductively. This yields one global permutation. Real-analytic functions satisfy the interval identity theorem, giving the analytic corollary.

For \(n=2\), the displayed quadratic inversion is immediate. On any connected component of \(U=\{F\ne G\}\), continuity prevents a candidate branch from switching between \(F\) and \(G\), because they are separated there. Thus every continuous representation makes one binary choice per component. Conversely, componentwise swaps remain continuous at component boundaries because \(F=G\) there. They remain nondecreasing: within each component they follow a CDF, and across a boundary the two CDFs meet at the same value. This proves the braid classification and counting.

For the smooth counterexample, \(q\) and \(|q|\) are flat at \(0\) and at \(\pm1\), hence smooth. On \([-1,1]\), \(L'\) has a positive minimum while \(q'\) and \((|q|)'\) are bounded. Choosing \(\varepsilon\) smaller than the ratio of that minimum to the larger derivative bound makes all four derivatives strictly positive. Outside \([-1,1]\) the perturbations vanish, so all four distributions have the same full-support logistic tails. The pointwise multiset identity follows from \(\{q,-q\}=\{|q|,-|q|\}\), while the sign change of \(q\) rules out a global permutation.

## Interpretation and stability

All rank marginals contain exactly enough pointwise symmetric information to recover the unordered CDF values. The remaining obstacle is not pointwise inversion but global label matching across CDF crossings. Stochastic dominance removes crossings; an identity-principle class removes admissible branch switching in a different way.

The distinction is structural rather than a finite differentiability threshold: even \(C^\infty\) positive densities can braid invisibly, while real analyticity (more generally, any interval-rigid class) forbids such local relabeling.

For two parents, the discriminant is
\[
s^2-4p=(F-G)^2.
\]
Thus even when an analytic model is structurally identified, numerical root tracking is intrinsically ill-conditioned near a crossing: perturbations in the observed rank CDFs are amplified on the order of \(1/|F-G|\). The result is therefore an identification theorem, not a uniform finite-sample stability guarantee.

## Relation to prior literature and originality boundary

Forward distribution formulas for independent non-identically distributed order statistics are classical. David (1956), Maurer and Margolin (1976), and Bapat and Beg (1989) developed inclusion-exclusion/permanent representations. Those formulas are not claimed as new.

Espín-Sánchez, Hodgson, and O'Neill (2025) explicitly write the asymmetric rank CDF as a triangular linear combination of the symmetric products \(S_m(x)\). Their Proposition 8 obtains identification from all order statistics in an asymmetric model under stochastic-dominance and support-endpoint conditions, while their discussion and Proposition 9 emphasize nonidentification when ordering conditions are removed in their broader nonparametric setting. That paper therefore provides especially close current context.

The contribution claimed here, to the best of our knowledge, is the exact observational-equivalence statement in terms of the pointwise CDF multiset; the complete two-parent componentwise braid classification; the interval-identity/real-analytic identification theorem that replaces dominance by unique continuation; and the full-support positive-density \(C^\infty\) counterexample showing that arbitrary smoothness does not suffice. The elementary symmetric-polynomial mechanism itself is treated as classical algebra rather than as a novelty claim.

Cho, Luo, and Xiao (2024) study a different observation model: joint distributions of two ordered repeated measurements with an additive latent variable, and their heterogeneous extension uses group information. It does not resolve the separate-rank-marginal problem considered here.

### Residual originality uncertainty

The 1989 Bapat-Beg primary article was located but its full text was not directly inspected; its accessible abstract describes forward permanent representations and recurrences. The 1956 David article was likewise located at the journal level but not inspected in full. These sources are scientifically relevant because an inverse remark may be embedded in older order-statistic theory even though the currently accessible descriptions are forward-facing. A broad search across order-statistic identification, heterogeneous samples, anonymous/rank data, crossing CDFs, and analytic identification did not locate the pointwise-multiset/label-braiding/unique-continuation result. The originality claim therefore remains explicitly “to the best of our knowledge.”

## Limitations

- Independence of the parent variables is essential to the Poisson-binomial factorization.
- The pointwise recovery theorem uses the marginal law of every rank. It does not claim that fewer ranks suffice in the unrestricted heterogeneous model.
- The analytic result assumes real-analytic CDFs on \(\mathbb R\), which is a strong full-support regularity condition. The more general interval-identity theorem isolates the actual structural requirement.
- Structural identification can be statistically ill-conditioned near crossings.
- The result identifies parent distributions up to label permutation; external semantic labels are not recoverable from anonymous rank data alone.

## Reproducibility

`artifacts/verify.py` uses exact rational arithmetic to reconstruct Poisson-binomial probabilities, elementary symmetric polynomials, and root polynomials for several heterogeneous examples; it also checks the two-parent discriminant identity. A numerical grid check verifies the pointwise multiset identity, monotonicity, and side-dependent relabeling in the smooth flat-crossing construction. The executed output is recorded in `artifacts/VERIFICATION.txt`.

## References

1. H. A. David (1956), “On the Application to Statistics of an Elementary Theorem in Probability,” *Biometrika* 43(1/2), 85–91. https://doi.org/10.1093/biomet/43.1-2.85
2. W. Maurer and B. H. Margolin (1976), “The Multivariate Inclusion-Exclusion Formula and Order Statistics from Dependent Variates,” *Annals of Statistics* 4(6), 1190–1199. https://projecteuclid.org/euclid.aos/1176343650
3. R. B. Bapat and M. I. Beg (1989), “Order Statistics for Nonidentically Distributed Variables and Permanents,” *Sankhyā A* 51(1), 79–93. https://www.jstor.org/stable/25050725
4. J.-A. Espín-Sánchez, C. Hodgson, and K. O'Neill (2025), “Order Statistics as Finite Mixtures,” Cowles Foundation Discussion Paper 2455. https://cowles.yale.edu/sites/default/files/2025-08/d2455.pdf
5. J. Cho, Y. Luo, and R. Xiao (2024), “Deconvolution from two order statistics,” *Quantitative Economics* 15(4), 1065–1106. https://doi.org/10.3982/QE2077
