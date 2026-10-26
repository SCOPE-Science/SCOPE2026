# Unique optimal sampling density and quadratic stability of random-LCM fluctuations

## Finding

Consider each integer in \(\{1,\ldots,n\}\) independently retained with probability \(\theta\in(0,1)\), and let \(L_n\) be the least common multiple of the retained integers, with \(\operatorname{lcm}(\varnothing)=1\). The limiting variance coefficient for \(\log L_n\) is
\[
V(\theta)=\sum_{j=1}^{\infty}\frac{(1-\theta)^j[1-(1-\theta)^j]}{j(j+1)}.
\]
This already-identified coefficient has a **unique global maximum** over all fixed \(0<\theta<1\), attained at
\[
\theta_*=1-q_*=0.3299324252175184913\ldots,
\]
where \(q_*\) is the unique zero on \((0,1)\) of
\[
H(q)=(2-q)\log(1-q)+2\log(1+q)+q^2.
\]
The sharp maximal coefficient is \(V(\theta_*)=0.1854345441670716280\ldots\). For comparison, fair coin retention gives \(V(1/2)=0.1698990367953974729\ldots\); optimal retention raises the variance coefficient by approximately \(9.14396436\%\).

There is also a strict local stability law,
\[
V(\theta_*)-V(\theta)=\kappa(\theta-\theta_*)^2+O(|\theta-\theta_*|^3),\qquad
\kappa=-\frac{H'(q_*)}{2q_*^3}>0,
\]
with \(\kappa=0.6387895185247574271\ldots\). Thus the peak is nondegenerate, not a plateau. The variance profile has no other stationary points in \((0,1)\).

## Assumptions and scope

The parameter \(\theta\) is fixed while \(n\to\infty\); no joint limiting claim is made for \(\theta=\theta_n\). The known central limit theorem and moderate deviation principle identify \(V(\theta)\) as the endpoint Gaussian variance and reciprocal quadratic-deviation coefficient, respectively. This result concerns **optimization of that known coefficient**, not a new CLT, MDP, or LIL. The parameter \(\theta\) varies over \((0,1)\), and the coefficient extends continuously by zero at both endpoints.

For each fixed \(\theta\), the functional limit process has covariance \(C_\theta(s,t)\) with \(C_\theta(t,t)=t V(\theta)\); hence the same \(\theta_*\) maximizes its one-time marginal variances simultaneously for every fixed \(t>0\). The 2026 endpoint MDP rate \(J_\theta^{\mathrm{end}}(x)=x^2/[2V(\theta)]\) is minimized at \(\theta_*\) for each fixed nonzero \(x\); the endpoint LIL cluster radius is \(\sqrt{V(\theta)}\), so it is also maximized at \(\theta_*\). Those consequences compare coefficients for fixed parameters, not rare-event probabilities uniformly over varying \(\theta\).

## Proof

Put \(q=1-\theta\). For \(0<z<1\), define
\[
F(z)=\sum_{j\ge1}\frac{z^j}{j(j+1)}.
\]
Using \(1/[j(j+1)]=1/j-1/(j+1)\) and \(\sum_{j\ge1}z^j/j=-\log(1-z)\), one obtains
\[
F(z)=1+\frac{1-z}{z}\log(1-z).
\]
Consequently \(V(1-q)=S(q):=F(q)-F(q^2)\). Direct differentiation gives the exact identity
\[
S'(q)=\frac{H(q)}{q^3},\qquad H(q)=(2-q)\log(1-q)+2\log(1+q)+q^2.
\]
A second differentiation, with ordinary simplification, yields
\[
H''(q)=\frac{q\,[2q^3-q^2-8q+3]}{(1-q^2)^2}.
\]
Set \(R(q)=2q^3-q^2-8q+3\). Since
\[
R'(q)=2(q+1)(3q-4)<0\quad(0<q<1),\qquad R(0)=3,\quad R(1)=-4,
\]
there is exactly one \(r\in(0,1)\) with \(R(r)=0\). Therefore \(H''\) is positive on \((0,r)\) and negative on \((r,1)\). Direct expansion at the left endpoint gives
\[
H(q)=\frac{q^3}{2}+O(q^4),\qquad H'(0+)=0.
\]
Thus \(H'\) is positive through \((0,r]\), decreases strictly on \((r,1)\), and tends to \(-\infty\) as \(q\uparrow1\). It consequently vanishes exactly once after \(r\), at some \(s\in(r,1)\). Hence \(H\) strictly increases up to \(s\) and strictly decreases afterwards. It is positive on \((0,s]\), while \(H(q)\to-\infty\) as \(q\uparrow1\). The intermediate value theorem and strict decrease show that \(H\) has exactly one zero \(q_*\in(s,1)\) and changes sign there from positive to negative.

The derivative identity now implies that \(S\) strictly increases on \((0,q_*)\) and strictly decreases on \((q_*,1)\). Since \(S(q)>0\) on \((0,1)\) (each term in its defining series is positive) and \(S(0+)=S(1-)=0\), the unique critical point is the unique global maximizer. The substitution \(\theta=1-q\) proves the optimization statement.

Moreover \(H'(q_*)<0\) and \(S''(q_*)=H'(q_*)/q_*^3<0\), since \(H(q_*)=0\). Taylor's theorem yields
\[
S(q_*)-S(q)=\left[-\frac{H'(q_*)}{2q_*^3}\right](q-q_*)^2+O(|q-q_*|^3),
\]
which is the claimed stability law after replacing \(q-q_*\) by \(-(\theta-\theta_*)\).

For completeness, the two thin-selection limits follow directly from the closed form:
\[
V(\theta)=\theta\log(1/\theta)-2\theta\log 2+O(\theta^2|\log\theta|)\quad(\theta\downarrow0),
\]
\[
V(\theta)=\frac{1-\theta}{2}+O((1-\theta)^2)\quad(\theta\uparrow1).
\]
These expansions describe the analytic coefficient only, and do not extend the fixed-parameter CLT to moving-parameter regimes.

## Verification

The associated standalone script `verify_lcm_variance.py` uses Python's standard library. Its rational atanh-series bounds certify \(H(6700675747/10^{10})>0\) and \(H(6700675749/10^{10})<0\), so the unique root lies in that explicit interval. It also compares the closed form and the defining sum at six illustrative points; these numerical comparisons are auxiliary, not a proof of global uniqueness. The checker was replayed from its saved path, returning `PASS exact_root_signs=2 analytic_cubic_monotonicity=proved series_checks=6`. The global proof is the derivative-sign argument above, which applies over the entire real interval.

## Relationship to prior work

Alsmeyer, Kabluchko and Marynych (2018 preprint, 2019 journal) establish the functional CLT, give precisely the series \(g(q)=S(q)\), write it in closed form, and *plot* its shape in Figure 1. Their graph already illustrates an interior variance peak; the present contribution is not discovery of its qualitative appearance. Rather, the new result provides the **exact root characterization, proof of uniqueness, sharp maximum, and nondegenerate quadratic stability** for choosing the thinning density. The relevant statements and Remark 1.3 of their arXiv full text were compared.

Wang, Yang and Zhou (first publicly posted July 9, 2026) give the functional MDP and LIL, and explicitly identify the same series as the endpoint MDP variance in their equations (2.20)–(2.21). Those results make the optimal-density question matter simultaneously for Gaussian fluctuations, local moderate-deviation cost, and the endpoint LIL envelope; they do not state or prove a density optimizer in the inspected main results. Neither paper's results *directly imply a unique maximizer*: differentiating the existing formula and controlling every possible critical point is needed.

## Limitations

The Gaussian and moderate-deviation limit theorems and variance series are pre-existing results, not contributions claimed here. Because the 2018 paper already plots the variance function and supplies its closed form, the originality and incremental value are restricted to the exact strict optimization and curvature. A separate equivalent optimization of this elementary explicit function may appear elsewhere without being located. The reported decimals are approximations; the theorem uses the exact unique-root definition. The variance comparison concerns fixed \(\theta\), not a uniform triangular-array optimality theorem.

## References

- G. Alsmeyer, Z. Kabluchko, A. Marynych, *Limit theorems for the least common multiple of a random set of integers*, arXiv:1801.08934, first posted 2018-01-26, especially Theorem 1.1 and Remark 1.3. https://arxiv.org/abs/1801.08934
- S. Wang, G. Yang, W. Zhou, *Functional Limit Theorems for Random Least Common Multiples*, arXiv:2607.08129, first posted 2026-07-09, especially §2.2 and equations (2.20)–(2.21). https://arxiv.org/abs/2607.08129
