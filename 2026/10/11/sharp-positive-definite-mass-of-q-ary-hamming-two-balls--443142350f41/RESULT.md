# Sharp positive-definite mass of q-ary Hamming two-balls

## Finding
For every prime power \(q\ge3\) and integer \(d\ge3\), put \(G=\mathbb F_q^d\) and let \(B_2=\{x\in G:\operatorname{wt}(x)\le2\}\). The weight is the number of nonzero coordinates. For functions \(f:G\to\mathbb C\) that are positive definite, satisfy \(f(0)=1\), and vanish outside \(B_2\), their sharp **counting-measure mass** is
\[
T_q(d):=\max_f\sum_{x\in G}f(x)
=\frac{r(r+1)}{\dfrac{d(q-1)}{q^2}-\theta(1-\theta)},\quad
r=\left\lfloor\frac{d(q-1)}q\right\rfloor,\quad
\theta=\frac{d(q-1)}q-r.
\]
The denominator is strictly positive. The optimal Fourier transform may be chosen to depend only on the dual Hamming weight \(k\) and is
\[
\widehat f(k)=\frac{(k-r)(k-r-1)}{\dfrac{d(q-1)}{q^2}-\theta(1-\theta)},\qquad k=0,\ldots,d.
\]
For radial positive-definite functions, this optimizer is **unique** when \(d\not\equiv1\pmod q\). When \(d\equiv1\pmod q\), the entire set of radial optimizers is the closed line segment joining this transform and the similarly normalized polynomial with consecutive zeros at \(r+1,r+2\). No claim of uniqueness or classification is made for unrestricted nonradial optimizers.

## Assumptions and scope
Use the unnormalized Fourier transform \(\widehat f(\xi)=\sum_{x\in G}f(x)\overline{\chi_\xi(x)}\), where \(\chi_\xi(x)\) is the product of a fixed nontrivial additive character evaluated at coordinate products \(\xi_jx_j\). Bochner positivity on finite abelian groups means \(\widehat f(\xi)\ge0\) for all \(\xi\). Fourier inversion gives \(f(0)=q^{-d}\sum_\xi\widehat f(\xi)\), while \(\sum_xf(x)=\widehat f(0)\).

Multiplying each coordinate independently by an element of \(\mathbb F_q^\times\), and permuting coordinates, preserves \(B_2\), Fourier positivity, and both normalizations. Averaging any feasible \(f\) under this symmetry gives a radial feasible function with identical mass. Thus solving the radial problem also gives the unrestricted sharp value.

## Proof
Let \(K_j(k)\) be the \(q\)-ary Krawtchouk polynomial
\[
K_j(k)=\sum_{h=0}^j(-1)^h(q-1)^{j-h}\binom{k}{h}\binom{d-k}{j-h},
\]
with the usual convention on out-of-range binomial coefficients. A radial function supported on the first three Hamming shells has Fourier transform
\[
P(k)=1+aK_1(k)+bK_2(k),\qquad 0\le k\le d.
\]
Every such \(P\) is a polynomial of degree at most two, and conversely every quadratic \(P\) with binomial average \(\mathbb EP(T)=1\) corresponds to some radial function with \(f(0)=1\) and support in \(B_2\); here \(T\sim\operatorname{Binomial}(d,(q-1)/q)\). Fourier positivity means precisely \(P(k)\ge0\) at each integer \(0\le k\le d\). Set \(\mu=\mathbb ET=d(q-1)/q\), \(\sigma^2=\operatorname{Var}(T)=d(q-1)/q^2\), \(r=\lfloor\mu\rfloor\), and \(\theta=\mu-r\). Since \(d\ge3\), \(1\le r<d\).

The polynomial \(Q_r(t)=(t-r)(t-r-1)\) is nonnegative at every integer. Its binomial average is
\[
D:=\mathbb EQ_r(T)=\sigma^2-\theta(1-\theta)>0.
\]
The last inequality follows also from strict positivity of \(Q_r(T)\) on at least one atom of the binomial law. Therefore \(P_r(t)=Q_r(t)/D\) is a feasible normalized Fourier polynomial. Its zero-frequency mass is \(M=r(r+1)/D\).

For any polynomial \(P\) of degree at most two, the exact *two-contact dual identity* is
\[
M\mathbb EP(T)-P(0)=\alpha P(r)+\beta P(r+1),
\]
where
\[
\alpha=M(r+1-\mu)-(r+1),\qquad
\beta=M(\mu-r)+r.
\]
It is enough to verify the identity on \(1,t,Q_r(t)\): the first two identities follow immediately from the definitions, while both sides vanish on \(Q_r\). We have \(\beta>0\). To see \(\alpha\ge0\), write \(d=q\ell+s\) with \(0\le s<q\). If \(s=0\), then \(\theta=0\) and \(\alpha=(q-1)(r+1)>0\). If \(1\le s<q\), then \(\theta=1-s/q\) and a direct cancellation gives
\[
\alpha=\frac{(r+1)\mu(s-1)}{qD}\ge0,
\]
with equality precisely when \(s=1\). Since \(\mathbb EP(T)=1\) and \(P(r),P(r+1)\ge0\), the dual identity proves \(P(0)\le M\). The feasible \(P_r\) attains equality; averaging proves the stated optimum for all, including nonradial, functions.

If \(s\ne1\), then both dual coefficients are positive; equality forces \(P(r)=P(r+1)=0\). Such a quadratic is a scalar multiple of \(Q_r\), and normalization makes it \(P_r\). If \(s=1\), then \(\alpha=0\), \(\beta>0\), and equality forces only \(P(r+1)=0\). The contact lies strictly between \(0\) and \(d\). A nonzero quadratic nonnegative on the integer grid and vanishing there has positive leading coefficient and its other root lies in \([r,r+2]\). Consequently the normalized feasible quadratics form exactly the segment joining the normalized products \((t-r)(t-r-1)\) and \((t-r-1)(t-r-2)\). This proves the asserted radial optimizer classification.

For additional constructive clarity, the inverse-Fourier shell values of \(P_r\) are
\[
f(0)=1,\quad f(x)=\frac{2((q-1)/q-\theta)}{qD}\quad(\operatorname{wt}(x)=1),\quad
f(x)=\frac2{q^2D}\quad(\operatorname{wt}(x)=2),
\]
and \(f(x)=0\) for larger weight. The coefficient formulas follow by matching the quadratic coefficients in \(P_r=1+aK_1+bK_2\). They are nonnegative, although pointwise nonnegativity was not required for the extremal problem.

## Verification
Run `python check.py` with Python 3 (standard library only). The script checks the Krawtchouk polynomial identities, exact binomial moment normalizations, primal nonnegativity and dual inequalities with rational arithmetic for nine alphabet sizes and every dimension \(3\le d\le64\), totaling 558 parameter pairs. It additionally computes the full character transforms directly on six small additive groups (including the additive group underlying the four-element field). Every test passed. Finite testing is corroboration; the all-parameter proof is the algebraic two-contact identity above.

For example, \(T_3(5)=27/2\), \(T_3(6)=15\), and \(T_4(6)=160/7\). The radial optimizer segment occurs precisely at dimensions \(d\equiv1\pmod q\), not generically.

## Relationship to prior work
The finite-group Turán extremal problem and its relation to positive-definite Fourier functions is classical; see Kolountzakis–Révész (2004). Berdysheva–Révész (first preprint 2019) study general Turán and Delsarte constants on locally compact groups, with bounds motivated by packing. Delsarte's Hamming association-scheme linear program and Krawtchouk polynomials are classical; Li (2022 preprint, published 2023) studies uniqueness of **coding-distance** LP optima. These frameworks are not claimed as new. The specific result here is the closed exact q-ary radius-two Turán mass and the congruence-dependent complete *radial* optimizer geometry. The source comparisons did not establish a prior identical formula; equivalence to an unindexed Hamming-scheme theta-number calculation is a residual bibliographic risk.

## Limitations
The formula concerns the **counting** measure on the finite additive group, not probability-normalized mass. The classification of equality cases is restricted to radial functions. This result supplies no classification of unrestricted nonradial equality cases and no classification of optimal error-correcting codes. Computations for finitely many fields and dimensions do not replace the all-parameter proof. The novelty comparison is not an independent literature certification, and any equivalent older formulation would supersede an originality claim.

## References
1. M. N. Kolountzakis and Sz. Gy. Révész, *Turán's extremal problem for positive definite functions on groups* (2004), arXiv:math/0312218, https://arxiv.org/abs/math/0312218.
2. E. Berdysheva and Sz. Gy. Révész, *Delsarte's Extremal Problem and Packing on Locally Compact Abelian Groups*, arXiv:1904.03614 (first version April 7, 2019), https://arxiv.org/abs/1904.03614.
3. R. Li, *Unique Optima of the Delsarte Linear Program*, arXiv:2204.06090 (2022), published in Designs, Codes and Cryptography (2023), https://arxiv.org/abs/2204.06090.
4. P. Delsarte, *An algebraic approach to the association schemes of coding theory*, Philips Research Reports Supplements 10 (1973). Krawtchouk-polynomial background: https://doc.sagemath.org/html/en/reference/coding/sage/coding/delsarte_bounds.html.
