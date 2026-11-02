# Exact inverse design of maximal endemic multiplicity in higher-order SIS contagion

## Finding

Fix an integer \(M\ge 2\). In the normalized homogeneous complete-simplicial SIS mean-field model
\[
\dot x=x\left[(1-x)\sum_{j=1}^{M}\frac{s_j}{j!}x^{j-1}-1\right],\qquad 0\le x\le1,
\]
all \(M\) interaction-channel coefficients \(s_j\) must be strictly positive. Given arbitrary **distinct, prescribed** prevalences
\[
0<r_1<\cdots<r_M<1,
\]
there is a choice of strictly positive \(s_1,\ldots,s_M\) for which these are exactly the \(M\) endemic equilibria **if and only if**
\[
\boxed{\sum_{i=1}^{M}r_i<1.}
\]
When the condition holds, the choice of normalized channel rates is unique. With \(D=\prod_{i=1}^{M}(1-r_i)\), \(e_0=1\), and \(e_k\) the elementary symmetric polynomial of degree \(k\) in the \(r_i\), the rates are
\[
\boxed{\frac{s_j}{j!}=\frac{1}{D}\sum_{k=0}^{M-j}(-1)^k e_k(r_1,\ldots,r_M),\quad 1\le j\le M.}
\]
These rates give the exact factorization
\[
\boxed{\dot x=-\frac{x}{D}\prod_{i=1}^{M}(x-r_i).}
\]
All endemic roots are hyperbolic. The equilibria \(r_M,r_{M-2},r_{M-4},\ldots\) are asymptotically stable and the intervening endemic roots are unstable; the disease-free state is stable when \(M\) is even and unstable when \(M\) is odd. The inverse criterion, rather than the previously discussed possibility of attaining \(M\) roots, is the claimed finding.

## Assumptions and scope

The variable \(x\) is the prevalence in \([0,1]\). The unit recovery rate is fixed by rescaling time, and \(s_j>0\) is the scaled infection rate through a complete \(j\)-simplex, namely a group comprising \(j\) infected neighbors and one susceptible individual. The maximal interaction order \(M\) is any fixed finite integer at least two. The equation is the deterministic homogeneous limiting ODE of the complete-simplicial stochastic SIS model; it is not a claim about finite-population stochastic absorption times or stationary laws.

The inverse problem prescribes *the full set* of \(M\) distinct endemic equilibria. It does not ask whether a prescribed smaller subset can appear together with other roots, or classify multiple/nonhyperbolic roots. Strict positivity matters: allowing a zero coefficient changes the attainable boundary at \(\sum_i r_i=1\).

## Proof

Write \(\lambda_j=s_j/j!\) and \(P(x)=\sum_{j=1}^{M}\lambda_jx^{j-1}\). Every positive equilibrium is a root of
\[
q(x)=(1-x)P(x)-1.
\]
Since \(\lambda_M>0\), this polynomial has degree exactly \(M\), leading coefficient \(-\lambda_M\), and satisfies \(q(1)=-1\). If it has the prescribed \(M\) distinct roots, necessarily
\[
q(x)=-\frac{\prod_{i=1}^M(x-r_i)}{D},\qquad D=\prod_{i=1}^M(1-r_i)>0.
\]
Indeed evaluation at \(x=1\) fixes the only possible multiplicative constant. Thus \(P\) and all its coefficients, hence all channel rates, are uniquely determined:
\[
P(x)=\frac{1-D^{-1}\prod_{i=1}^{M}(x-r_i)}{1-x}.
\]
The numerator vanishes at \(x=1\), so this is a polynomial of degree \(M-1\).

Expanding \(\prod_i(x-r_i)=\sum_{k=0}^{M}(-1)^{M-k}e_{M-k}x^k\) and comparing coefficients in \((1-x)P(x)\) gives
\[
\lambda_j=D^{-1}\sum_{k=0}^{M-j}(-1)^k e_k,\qquad j=1,\ldots,M.
\]
In particular \(\lambda_M=1/D\) and, since \(M\ge2\),
\[
\lambda_{M-1}=\frac{1-e_1}{D}=\frac{1-\sum_i r_i}{D}.
\]
Strictly positive rates therefore **require** \(\sum_i r_i<1\). If the sum equals one, the penultimate channel vanishes; if it exceeds one, this channel is negative.

For the converse, assume \(S=\sum_i r_i<1\). For every \(k\ge0\), the elementary symmetric functions satisfy
\[
(k+1)e_{k+1}=\sum_i r_i\,e_k(r_1,\ldots,\widehat{r_i},\ldots,r_M)\le S e_k.
\]
Here the hat means that the variable is omitted. Consequently
\[
1=e_0>e_1>e_2>\cdots>e_M>0,
\]
where the strict inequalities also follow from \(S<1\). Every partial alternating sum \(1-e_1+e_2-\cdots+(-1)^\ell e_\ell\), for \(0\le\ell\le M-1\), is positive: it is at least \(1-e_1>0\) after pairing successive later terms \(e_2-e_3,e_4-e_5,\ldots\). Hence the displayed formula yields \(\lambda_j>0\) for every \(j\). The factorization of \(\dot x=xq(x)\) shows exactly the prescribed \(M\) endemic equilibria, establishing sufficiency.

Finally the linearization at each endemic root is
\[
\left.\frac{d\dot x}{dx}\right|_{r_i}=-\frac{r_i}{D}\prod_{k\ne i}(r_i-r_k).
\]
The factors \(r_i,D\) are positive, and the product has sign \((-1)^{M-i}\). Thus the derivative is negative precisely when \(M-i\) is even, establishing the alternating stability statement. At zero,
\[
\left.\frac{d\dot x}{dx}\right|_{0}=\frac{(-1)^{M+1}}{D}\prod_i r_i,
\]
so zero is hyperbolically attracting exactly for even \(M\). No further equilibria exist: the polynomial is of degree \(M+1\) with roots \(0,r_1,\ldots,r_M\).

## Verification

A standalone standard-library Python program, `verify_inverse_sis.py`, implements exact rational polynomial multiplication, elementary symmetric polynomials, and rate reconstruction, without floating-point arithmetic. Execute it with `python3 verify_inverse_sis.py`. It checks the full polynomial identity, positivity exactly on the claimed strict-sum domain, the sharp sum-one boundary, uniqueness-enforcing leading coefficients, root evaluations, and stability signs for 2,338 distinct test families (18,718 root evaluations) with interaction orders through \(M=15\). This finite verification supplements, but does not replace, the all-order proof above.

For example, at \(M=4\), the target roots \((1/20,1/10,3/20,1/5)\) have sum \(1/2\) and are realized by the strictly positive normalized rates
\[
(\lambda_1,\lambda_2,\lambda_3,\lambda_4)=\left(\frac{3875}{3876},\frac{5875}{5814},\frac{2500}{2907},\frac{5000}{2907}\right).
\]
Their stability pattern is unstable, stable, unstable, stable, and the disease-free equilibrium is also stable.

## Relationship to prior work

Kiss, Iacopini, Simon, and Georgiou (arXiv:2309.12752v1, Section II.3, Equation II.31 and Discussion) derive the arbitrary-order complete-simplicial SIS limiting equation and explore multistability explicitly through four-body interactions. Their discussion anticipates arbitrarily many endemic equilibria but does not give an inverse characterization for arbitrarily **prescribed** equilibrium prevalences.

Kiss, Bick, and Simon (2025), *Decoding how higher-order network interactions shape contagion dynamics*, Section 3.2, observe the degree bound and state that a model with high-order channels can have the corresponding number of positive roots. This establishes a nearby general existence assertion and is **not** claimed as a new contribution here. The present result instead characterizes the precise attainable target-root region \(\sum_i r_i<1\), proves its necessity and sufficiency under strict positivity, and uniquely reconstructs all infection rates. Mere attainability of some maximal-root configuration does not imply a complete classification of which prevalence vectors are attainable.

Ferraz de Arruda, Petri, Rodriguez, and Moreno (2023) study multistability and intermittency through heterogeneous hypergraph structure and critical-mass interactions, a related but different mechanism, rather than inversion of the homogeneous all-order polynomial coefficients.

## Limitations

The theorem is for the deterministic scalar homogeneous mean-field equation, not stochastic persistence in finite complete complexes, nor heterogeneous or time-dependent networks. The full-equilibrium inverse problem is solved only for exactly \(M\) distinct endemic roots and strictly positive rates; partial root prescriptions and degenerate roots are not classified. The result is an algebraic inverse-design statement, not a claim that independently estimating high-order infection rates from data is easy. Although the searched literature did not identify the sharp target-root-sum criterion, comprehensive publication priority and independent scientific validation remain open.

## References

1. I. Z. Kiss, I. Iacopini, P. L. Simon, and N. Georgiou, *Insights from exact social contagion dynamics on networks with higher-order structures*, arXiv:2309.12752v1, first submitted 2023-09-22, Sections II.3, III, and IV. https://arxiv.org/html/2309.12752v1
2. I. Z. Kiss, C. Bick, and P. L. Simon, *Decoding how higher-order network interactions shape contagion dynamics*, Journal of Mathematical Biology 91, 29 (2025), published 2025-08-19, Section 3.2. https://link.springer.com/article/10.1007/s00285-025-02247-4
3. G. Ferraz de Arruda, G. Petri, P. M. Rodriguez, and Y. Moreno, *Multistability, intermittency, and hybrid transitions in social contagion models on hypergraphs*, Nature Communications 14, 1375 (2023). https://www.nature.com/articles/s41467-023-37118-3
