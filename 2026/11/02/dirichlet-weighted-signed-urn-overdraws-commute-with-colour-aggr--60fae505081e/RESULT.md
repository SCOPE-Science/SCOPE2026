# Dirichlet-weighted signed urn overdraws commute with colour aggregation

## Finding

Let \(S\) be a finite nonempty colour set, \(\beta\in\mathbb N_0^S\) a nonempty urn with total \(m=\sum_s\beta_s\), and \(\alpha\in(0,\infty)^S\). Write \(\mathcal P_m(S)\) for the polynomials of total degree at most \(m\) on the probability simplex, and \(B_{m,\eta}(p)=\frac{m!}{\prod_s\eta_s!}\prod_s p_s^{\eta_s}\) for the multinomial Bernstein basis with \(|\eta|=m\). For normalized \(\mu_\alpha=\operatorname{Dirichlet}(\alpha)\), there exists a unique \(d^{\alpha}_{m,\beta}\in\mathcal P_m(S)\) satisfying
\[
\int B_{m,\eta}(p)d^{\alpha}_{m,\beta}(p)\,\mu_\alpha(dp)=\mathbf1_{\eta=\beta}\quad(|\eta|=m).
\]
For every \(k\in\mathbb N_0\), define a finite signed histogram law on \(|\gamma|=k\):
\[
H^{\alpha}_k(\beta;\gamma)=\int B_{k,\gamma}(p)d^{\alpha}_{m,\beta}(p)\,\mu_\alpha(dp).
\]
These signed laws have total mass one, and for \(k\le m\) equal the usual hypergeometric law
\[
H^\alpha_k(\beta;\gamma)=\frac{\prod_s\binom{\beta_s}{\gamma_s}}{\binom mk}.
\]
For **every** surjective aggregation of colours \(f:S\to T\), every \(\alpha,\beta,k\) as above and \(\delta\in\mathbb N_0^T\) with \(|\delta|=k\), aggregation commutes **exactly** with signed overdraws:
\[
\boxed{\sum_{\gamma:f_*\gamma=\delta}H^\alpha_k(\beta;\gamma)=H^{f_*\alpha}_k(f_*\beta;\delta).}
\]
Thus the intrinsic full-support choice \(\alpha=\beta\in\mathbb N_{>0}^S\) gives a signed overdrawing rule that preserves classical sampling through \(k=m\) and is natural under any colour merge for every larger \(k\). It is intrinsic within this specified weighted-dual family; uniqueness among all conceivable signed extensions is **not** claimed.

By contrast, using the *uniform-simplex reference measure separately for each colour set*, \(\alpha=(1,\ldots,1)\), does not respect aggregation. The earliest possible full-support obstruction has \(S=\{a,b,c\}\), \(\beta=(1,1,1)\), \(k=4\) and merge \(a,b\mapsto A\), \(c\mapsto C\). For \(J\), the number of \(A\) balls in the four-ball signed outcome, the pushed-forward three-colour rule and the separately constructed uniform-reference two-colour rule have respective signed probability vectors, indexed by \(J=0,1,2,3,4\),
\[
\left(\tfrac1{18},-\tfrac29,\tfrac13,\tfrac{10}9,-\tfrac5{18}\right)
\quad\text{and}\quad
\left(\tfrac{17}{210},-\tfrac{34}{105},\tfrac{17}{35},\tfrac{106}{105},-\tfrac{53}{210}\right).
\]
Their signed total-variation norm distance, defined as half the sum of absolute coordinate differences, is exactly \(64/315\). This is a failure of a previously **unasserted** compatibility property, not a contradiction of conservativity.

## Assumptions and scope

The simplex contains nonnegative \(p_s\) summing to one. All reference Dirichlet parameters are strictly positive real numbers. Urn multiplicities are nonnegative integers with positive total; the canonical full-support subfamily has all multiplicities positive. All \(k\) are arbitrary nonnegative integers, including values exceeding \(m\); signed values need not be nonnegative. A colour aggregation \(f\) is a surjection, and \((f_*v)_t=\sum_{s:f(s)=t}v_s\). At \(k=0\), the single empty histogram has mass one.

## Proof

**1. Existence and normalization.** The degree-\(m\) multinomial Bernstein functions constitute a basis for \(\mathcal P_m(S)\). Their Gram matrix in \(L^2(\mu_\alpha)\) is strictly positive definite because \(\mu_\alpha\) has strictly positive density in the relative interior and a nonzero polynomial cannot vanish there almost everywhere. Hence the dual polynomial exists uniquely. Since \(\sum_{|\eta|=m}B_{m,\eta}=1\), duality gives \(\int d^{\alpha}_{m,\beta}\,d\mu_\alpha=1\); since \(\sum_{|\gamma|=k}B_{k,\gamma}=1\), every signed histogram sums to one.

**2. Conservativity.** For \(k\le m\), the classical degree elevation identity is
\[
B_{k,\gamma}(p)=\sum_{|\eta|=m}\frac{\prod_s\binom{\eta_s}{\gamma_s}}{\binom mk}B_{m,\eta}(p),
\]
where binomial coefficients vanish when their lower entry exceeds the upper. Integrating against the weighted dual leaves exactly the coefficient of \(\eta=\beta\). This proves the displayed hypergeometric formula without any dependence on \(\alpha\).

**3. Exact aggregation.** Let \(P\sim\operatorname{Dirichlet}(\alpha)\), put \(Q_t=\sum_{f(s)=t}P_s\), and write \(\alpha'=f_*\alpha\). The gamma construction of the Dirichlet law gives \(Q\sim\operatorname{Dirichlet}(\alpha')\), and conditional on \(Q\), the within-group proportions are independent Dirichlet random vectors. If \(r\in\mathbb N_0^S\) and \(r'_t=\sum_{f(s)=t}r_s\), then
\[
\mathbb E\bigl[\prod_sP_s^{r_s}\mid Q\bigr]
=\prod_t Q_t^{r'_t}\,
\frac{\prod_s(\alpha_s)_{r_s}}{\prod_t(\alpha'_t)_{r'_t}},
\]
where \((z)_j=z(z+1)\cdots(z+j-1)\), \((z)_0=1\). The conditional expectation of **any** degree-at-most-\(m\) polynomial in \(P\) is therefore a degree-at-most-\(m\) polynomial in \(Q\). Let \(g(Q)=\mathbb E[d_{m,\beta}^{\alpha}(P)\mid Q]\). For every \(|\delta|=m\), the multinomial theorem gives \(B_{m,\delta}(Q)=\sum_{f_*\eta=\delta}B_{m,\eta}(P)\), whence
\[
\int B_{m,\delta}(q)g(q)\,\mu_{\alpha'}(dq)=\sum_{f_*\eta=\delta}\mathbf1_{\eta=\beta}=\mathbf1_{\delta=f_*\beta}.
\]
By uniqueness in step 1, \(g=d^{\alpha'}_{m,f_*\beta}\). Applying the same multinomial aggregation identity at degree \(k\), then conditional expectation, proves the boxed formula for all \(k\), not just \(k\le m\). For \(\alpha=\beta>0\), automatically \(f_*\alpha=f_*\beta\), so the intrinsic assignment is closed under every merge.

**4. Exact obstruction.** At \(m=3\), the signed dual functional \(L\) on polynomials satisfies \(L(1)=1\), \(L(z)=1/3\), and \(L(z^2)=L(z^3)=0\) for \(z=P_c\), regardless of the positive reference parameter. In the fine model \(z\) has marginal reference law \(\operatorname{Beta}(1,2)\); in the independently uniform-referenced two-colour model it has \(\operatorname{Beta}(1,1)\). For either reference law, let \(\pi_4(z)=z^4+c_3z^3+c_2z^2+c_1z+c_0\) be its unique monic fourth-degree orthogonal polynomial. Since \(d_{3,\beta}\) has degree at most three, \(L(\pi_4)=0\), so \(L(z^4)=-c_1/3-c_0\). Exact integration gives, respectively,
\[
\pi^{(1,2)}_4(z)=z^4-\tfrac{16}9z^3+z^2-\tfrac4{21}z+\tfrac1{126},
\quad L_{(1,2)}(z^4)=\tfrac1{18};
\]
\[
\pi^{(1,1)}_4(z)=z^4-2z^3+\tfrac97z^2-\tfrac27z+\tfrac1{70},
\quad L_{(1,1)}(z^4)=\tfrac{17}{210}.
\]
For the event that all four draws have colour \(C\), these are precisely the two conflicting signed probabilities. All lower moments match, so by expanding \(\binom4j(1-z)^jz^{4-j}\), the difference for \(J=j\) is \(-\frac8{315}(-1)^j\binom4j\). Half its absolute-coordinate sum equals \(\frac4{315}2^4=\frac{64}{315}\). With one or two positive-support colours every surjective aggregation is bijective or collapses to one colour, so it cannot furnish a failure; with three positive-support colours the least urn size is \(m=3\), and \(k=4\) is the first overdraw size. This proves the stated minimality qualification.

## Verification

Run `python checker.py` with Python 3 and no external dependencies. It uses exact rational arithmetic and independently constructs Gram matrices from Dirichlet rising-factorial moments, solves the linear systems, and tests conservation, aggregation and the explicit first obstruction. Observed result: `PASS: 2101 exact-rational assertions; weighted aggregation, hypergeometric conservativity, normalization, and sharp obstruction`. Finite enumeration verifies formulas in small cases only; the proof in steps 1–4 establishes the universal quantifiers.

## Relationship to prior work

Jacobs and Stein (2023) introduced signed overdraws through the uniform-simplex dual Bernstein basis, proving normalization and conservativity. Their three-colour and two-colour worked examples concern distinct urn configurations, without identifying their compatibility under aggregation. The present result generalizes the reference measure to positive Dirichlet weights, proves an exact all-sizes naturality identity, and exhibits an explicit full-support obstruction for the independently uniform-reference convention. Classical Dirichlet aggregation and Bernstein degree elevation are ingredients; neither alone supplies the signed dual's conditional-expectation identity. Benavoli, Facchini and Zaffalon (2023) study signed finite-exchangeability representations, rather than this aggregation-compatible selection. Allen and Kirby's Bernstein mass-matrix inversion is relevant to computational duals but not itself evidence of this aggregation theorem; its complete text was not inspected.

## Limitations

The laws are signed, not sampling probabilities when overdrawn. The canonical parameter assignment \(\alpha=\beta\) is only stated for urns with all colour counts positive; empty colour labels require a separate convention. The theorem is for exact merges of finite colour sets, not arbitrary stochastic relabelling kernels or a characterization of all possible natural signed extensions. The example does not refute any claimed theorem of Jacobs and Stein, and priority against all classical approximation-theory or signed-measure literature has not been definitively established. Independent validation has not occurred.

## References

1. B. Jacobs and D. Stein, *Overdrawing Urns using Categories of Signed Probabilities*, arXiv:2312.12453 (first posted 14 December 2023), https://arxiv.org/abs/2312.12453. Sections 6–8 and Appendix A.
2. A. Benavoli, A. Facchini and M. Zaffalon, *Connecting classical finite exchangeability to quantum theory*, arXiv:2306.03869 (first posted 6 June 2023), https://arxiv.org/abs/2306.03869.
3. B. Allen and R. C. Kirby, *Structured inversion of the Bernstein mass matrix*, SIAM Journal on Matrix Analysis and Applications (2020), DOI:10.1137/19M1284166; bibliographic/abstract relevance only.
