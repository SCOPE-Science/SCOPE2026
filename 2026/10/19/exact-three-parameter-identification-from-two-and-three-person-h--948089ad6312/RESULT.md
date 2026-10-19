# Exact three-parameter identification from two- and three-person household epidemics

## Finding

In the stochastic single-introduction household SIR model defined below, the population-level final-size laws for households containing two and three people uniquely identify three previously unknown quantities simultaneously: the base per-pair infectious-contact rate \(\beta>0\), the household-size mixing exponent \(\eta\in[0,1]\), and the finite Gamma infectious-period shape \(a>0\) (with mean period fixed at one). Two-person households need only their no-secondary-case probability; three-person households need their probabilities of zero and exactly one secondary cases. An explicit one-dimensional, strictly monotone inversion recovers all three parameters globally.

This observation design is sharp among these two household sizes. Complete three-person final-size data alone cannot separate \(\beta\) and \(\eta\). Knowing only the expected secondary-case fractions separately for both household sizes cannot identify all three parameters at any interior point \(0<\eta<1\): a smooth one-parameter family of distinct admissible triples has the same two means. Thus, the distinction between household-size-stratified means and outcome-count-stratified data is substantive once the infectious-period shape is also unknown. The shape-sensitive signal in three-person final sizes is strictly positive and only second order in the contact intensity at weak transmission.

## Assumptions and scope

For each household with \(n\in\{1,2\}\) initially susceptible contacts and exactly one initially infected index case, each infective \(u\) has an independent duration \(I_u\sim\operatorname{Gamma}(a,a)\), in shape/rate parametrization, so \(\mathbb E I_u=1\). During that period each ordered susceptible recipient receives independent conditional Poisson infectious-contact attempts at rate \(\lambda_n=\beta n^{-\eta}\). Poisson clocks to different recipients are conditionally independent given the infective's duration; different infectives' durations and processes are independent. Each successful contact to a susceptible creates infection; immunity after recovery is permanent. There are no outside introductions or household infections before the single index case, and all household outbreaks are observed until extinction. No infection or recovery times, or transmission identities, are assumed observed.

Let \(Z_n\in\{0,\ldots,n\}\) be the number of additional persons ultimately infected, and set
\[
 h=\Pr(Z_1=0),\qquad q=\Pr(Z_2=0),\qquad r=\Pr(Z_2=1).
\]
Here \(n=1\) means a **two-person household** and \(n=2\) means a **three-person household**. These are exact population probabilities, not finite-sample frequencies. The shape \(a\) is arbitrary finite and positive; \(\beta>0\) and \(0\le\eta\le1\). The theorem is structural identification, not a finite-sample confidence or numerical conditioning guarantee.

## Proof

**Step 1: exact two-contact law.** Define the infectious-period Laplace transform
\[
 L_a(s)=\mathbb E(e^{-sI})=(1+s/a)^{-a}\qquad(s\ge0),
\]
and abbreviate \(\lambda=\lambda_2\), \(p=L_a(\lambda)\), \(q=L_a(2\lambda)\). Neither of the two initially susceptible contacts is infected precisely when the index sends no infectious contact to either one, giving
\[
 \Pr(Z_2=0)=q.
\]
Exactly one contact is ultimately infected when the index makes infectious contact to exactly one of the two people and that newly infected person makes none to the remaining susceptible contact. For one specified recipient, the first condition has probability \(\mathbb E[(1-e^{-\lambda I})e^{-\lambda I}]=p-q\); the newly infected individual's independent failure to transmit to the other has probability \(p\). Summing the two disjoint possibilities yields
\[
 \Pr(Z_2=1)=2p(p-q),\qquad \Pr(Z_2=2)=1-q-2p(p-q).
\]
For the household with one initially susceptible contact, \(\lambda_1=\beta\), so
\[
 h=L_a(\beta).
\]
These statements also follow from directly integrating all directed contact-edge configurations.

**Step 2: extract two Laplace evaluations.** For every admissible parameter triple, \(0<p<1\), \(p^2<q<p\), and \(r>0\). The strict inequality \(q>p^2\) is the positive variance of \(e^{-\lambda I}\) for a nonconstant finite-shape Gamma duration. Since \(p\) is the positive root of \(p^2-qp-r/2=0\), observed \((q,r)\) uniquely recover
\[
 p=\frac{q+\sqrt{q^2+2r}}2.
\]

**Step 3: uniquely recover shape and the three-person contact intensity.** Set \(u=\lambda/a>0\). Then
\[
 R:=\frac{\log q}{\log p}=
 \frac{\log(1+2u)}{\log(1+u)}=:f(u).
\]
Because \(p^2<q<p<1\), \(1<R<2\). The function \(f\) maps \((0,\infty)\) continuously and strictly decreasingly onto \((1,2)\): its endpoint limits are \(2\) and \(1\). For strict monotonicity, differentiating shows that the sign of \(f'(u)\) equals the sign of \(2H(u)-H(2u)\), with \(H(v)=(1+v)\log(1+v)\). Since \(H\) is strictly convex and \(H(0)=0\), this quantity is negative for all \(u>0\). Hence there is exactly one positive \(u\) solving \(f(u)=R\). Recover
\[
 a=-\frac{\log p}{\log(1+u)},\qquad
 \lambda=au.
\]
The remaining parameters follow uniquely from \(h\):
\[
 \beta=a\bigl(h^{-1/a}-1\bigr),\qquad
 \eta=\frac{\log(\beta/\lambda)}{\log2}.
\]
The assumed data are in the model image, so the last inversion gives \(0\le\eta\le1\), including both endpoint mixing regimes. This proves global injectivity of \((a,\beta,\eta)\mapsto(h,q,r)\) on the stated domain.

**Step 4: a sharp information distinction.** Three-person households alone identify \((a,\lambda_2)\), but changing \(\eta\) arbitrarily in \([0,1]\) and setting \(\beta=2^\eta\lambda_2\) leaves their entire final-size law unchanged. Two-person households alone determine only \(L_a(\beta)\), so do not identify three parameters either.

Suppose instead that the only outcomes reported for both household sizes are the two exact expected secondary-case fractions
\[
 m_1=1-L_a(\beta),\qquad
 m_2=\frac{\mathbb E Z_2}{2}=1-p^2-q(1-p),
\]
where \(p=L_a(\lambda_2)\) and \(q=L_a(2\lambda_2)\). Write derivatives with respect to the intensity \(\lambda_2\) as primes. Since \(p'<0\), \(q'<0\), and \(0<q<p<1\),
\[
 \frac{\partial m_2}{\partial\lambda_2}
 =(q-2p)p'-(1-p)q'>0.
\]
Also \(\partial m_1/\partial\beta=(1+\beta/a)^{-a-1}>0\). At every \(a>0\), \(\beta>0\), \(0<\eta<1\), the Jacobian of \((m_1,m_2)\) with respect to \((\beta,\eta)\) has nonzero determinant, since \(\partial\lambda_2/\partial\eta=-(\log2)\lambda_2\ne0\). The implicit-function theorem therefore supplies an open interval of distinct shapes \(a\), with uniquely adjusted \(\beta(a),\eta(a)\), for which both means are **exactly constant**. The adjustments remain admissible for a sufficiently small interval around any interior initial parameters. This proves structural nonidentifiability even with arbitrarily accurate medium-resolution outcomes from exactly these two household sizes.

**Step 5: weak-transmission boundary.** For fixed finite \(a>0\), Taylor expansion of the Gamma Laplace transform gives
\[
 q-p^2=\operatorname{Var}(e^{-\lambda I})
 =\frac{\lambda^2}{a}+O_a(\lambda^3)
 \quad\text{as }\lambda\downarrow0.
\]
This signal is strictly positive for each \(\lambda>0\) but vanishes quadratically when transmission becomes rare. It quantifies a practical limitation of the exact structural inverse without contradicting injectivity.

## Verification

A rational example has \(a=1\), \(\beta=1\), and \(\eta=\log(3/2)/\log2\), so \(\lambda_2=2/3\). Its exact observables are
\[
 h=\frac12,\quad
 (\Pr(Z_2=0),\Pr(Z_2=1),\Pr(Z_2=2))
 =\left(\frac37,\frac{36}{175},\frac{64}{175}\right),
\]
and \(m_2=82/175\). The inverse yields \(p=3/5\), \(u=2/3\), and precisely the stated \((a,\beta,\eta)\).

Run `python verify.py` from the directory containing this document; it requires only Python's standard library. The script enumerates all \(64\) directed arc configurations of each three-person epidemic, integrating their correlated outgoing arcs in exact rational arithmetic for four choices of integer Gamma shape. It compares that independent finite-state calculation with the closed probability formulas, checks the rational example, verifies inverse recovery for seven admissible triples, exhibits a distinct shape with exactly the same two medium-resolution means, and checks the weak-transmission signal. These finite checks do not substitute for the all-parameter mathematical proof.

## Relationship to prior work

Brooks, House, Pellis and Hilton (arXiv:2603.25235v1, first public March 26, 2026) develop a stochastic household-final-size likelihood with contact rates \(\beta/n^\eta\), fixing the Gamma infectious-period shape when estimating the other two parameters. In the discussion of their revised version they explicitly suggest that freeing the Gamma shape would create identifiability difficulties for medium-resolution data potentially resolved by high-resolution data. Their paper provides the underlying forward model, probability recursion, and qualitative experimental evidence; it does not state the present global explicit three-parameter inverse, the two-size information minimum, or the exact medium-mean nonidentifiability manifold. The direct verification here independently reconstructs the required three-person final-size formulas.

General household final-size distributions and numerical parameter inference are established earlier, notably by Ball (1986) and Miller (2019), so no novelty is claimed for the standard triangular final-size calculation, for Gamma Laplace transforms, or for the elementary convexity lemma by themselves. Miller (arXiv:1907.05138) discusses finite-population final-size inference and identifiability difficulties, but its materially inspected inference section does not resolve this specific three-parameter, two-household-size inverse problem. Ball, Britton and Neal (arXiv:2505.17890) treat broader stochastic household epidemics, principally large-population final-size limits and monotonicity, not the same inverse identification statement.

## Limitations

The inverse identifies a parametric Gamma family with *known mean infectious duration equal to one*. If the absolute time scale or the duration mean is unknown, infection-rate scaling introduces another ambiguity. The model requires one index case per household, homogeneous susceptibility, independent infective durations, complete follow-up, no further introductions, and the specified power-law contact rate across household sizes. The theorem concerns exact outcome probabilities from known-size households, not recovery from a single finite outbreak or statistical precision with finite samples. Near zero intensity or very large shape, inverse estimation can be severely ill-conditioned. The medium-summary nonidentifiability proof is for precisely two household sizes and does not exclude identifiability from means at additional sizes. More general infectious-period laws are not globally identified by just two Laplace-transform evaluations. Priority relative to unexamined specialized inverse-epidemic literature remains an open bibliographic risk; independent assessment has not been conducted.

## References

1. J. Brooks, T. House, L. Pellis, J. Hilton, *Bayesian Inference for Epidemic Final Size Datasets with Hidden Underlying Household Structure*, arXiv:2603.25235v1 (March 26, 2026), revised v2 (June 17, 2026). https://arxiv.org/html/2603.25235
2. J. C. Miller, *Distribution of outbreak sizes for SIR disease in finite populations*, arXiv:1907.05138 (July 11, 2019). https://arxiv.org/abs/1907.05138
3. F. Ball, T. Britton, P. Neal, *Household epidemic models revisited*, arXiv:2505.17890 (May 23, 2025). https://arxiv.org/abs/2505.17890
4. F. Ball, *A unified approach to the distribution of total size and total area under the trajectory of infectives in epidemic models*, Advances in Applied Probability 18 (1986), 289–310. https://doi.org/10.2307/1427303
