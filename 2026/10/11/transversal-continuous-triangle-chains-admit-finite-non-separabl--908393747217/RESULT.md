# Transversal continuous triangle chains admit finite non-separable realizations

## Finding

A finite family of planar convex sets is **non-separable** (NS) if no line disjoint from its union separates two nonempty subfamilies. For a finite NS-family \(\mathcal F\) of positive homothets of a fixed triangle, its **covering factor** is the smallest containing homothety ratio divided by the sum of the individual ratios. Let \(\Lambda\) denote the supremum of the covering factor over all such finite families and all cardinalities.

The cyclic contact recurrence of Lian--Xue--Yuan [1, Sections 5 and 7] admits the following **finite-realization principle**. Every continuous endpoint solution satisfying the strict sign conditions (5.15), the terminal conic (5.18), the nonvanishing trajectory condition and a nonzero derivative of its scalar endpoint equation is the limit of *exactly contacting finite chains with equal step parameters*. For every sufficiently large integer \(m\), one gets \(3(m+1)\) pairwise distinct positive homothetic triangles forming an NS-family, and the covering factors converge to that continuous solution's factor.

An explicit certified instance uses the **rational choices**
\[
d=\frac{415868}{10^6},\qquad \tau=\frac{67376}{10^5}.
\]
The scalar endpoint equation has a unique simple solution in
\[
\frac{1110182}{10^6}<s_*<\frac{1110185}{10^6}.
\]
Its continuous covering factor is strictly larger than \(10633/10000\). Therefore **actual finite NS-families**, not a formal continuum of zero-size triangles, attain factors strictly exceeding this number for all sufficiently large chain lengths:
\[
\boxed{\Lambda>\frac{10633}{10000}=1.0633.}
\]
This improves the rigorous lower bound \(250000000/235141779\) of [1]; the accompanying finite-realization theorem gives the structural reason an interior, transversal continuous chain can be approximated.

## Assumptions and scope

Take parameters \(0<d<1\), \(0<\tau<1\). Define
\[
v=\frac{1-d+d\tau}{1+\tau+\tau^2},\quad
u=\tau v,\quad
\kappa=\frac{d+(1-d)\tau^2}{1+\tau+\tau^2},\quad
D=v-d,\quad
E_f=\kappa(v-u)+D(v-\kappa).
\]
For \(s>0\) set
\[
B_0=\frac{(v-u)d}{v},\quad
c_\infty(s)=v-B_0e^{-(\kappa+D)s},\quad
F_\infty(s)=d(\kappa+D)-\kappa c_\infty(s)-\frac{dE_f}{v}e^{-\kappa s}.
\]
A **strict transversal continuous endpoint solution** is a number \(s_*>0\) with \(F_\infty(s_*)=0\), \(F_\infty'(s_*)\ne0\), and \(c_*=c_\infty(s_*)\) satisfying
\[
0<u<v<d<1-u,\quad u+v>d,\quad 0<c_*<v,\quad c_*+d<1-u,\quad d(\kappa+D)>\kappa c_*,\quad \kappa<v.
\]
In addition the continuous recovery denominator below must remain nonzero for \(0\le t\le s_*\). These are geometric and analytic conditions, not merely numerical sample tests.

Set
\[
E_0=d(\kappa+D)-\kappa c_*,\quad R_0=\frac{v-c_*}{E_0},\quad Y_0=\frac{d}{E_0},
\]
and along the continuum set
\[
E(t)=\frac{D\kappa}{\kappa R_0e^{Dt}+DY_0e^{-\kappa t}-1}.
\]
Write the limiting total homothety scale as
\[
S_\infty=3\left(1-c_*-d+\int_0^{s_*}E(t)\,dt\right).
\]
The corresponding limiting covering factor is
\[
\lambda_*=\left[3\left(1-c_*-d+\int_0^{s_*}E(t)\,dt\right)\right]^{-1}.
\]
The theorem does **not** require the parameters \(d,\tau\) to vary with chain length; the supporting parameter \(c\) and the total step length \(s\) are perturbed.

## Proof

**1. Reduction of both endpoint products to one scalar equation.** Let
\[
R_f=\frac{v-u}{E_f},\qquad Y_f=\frac{v}{E_f}.
\]
The source's finite contact theorem [1, Theorem 5.3] requires, for steps \(h_j>0\),
\[
\prod_{j=1}^m(1+Dh_j)=\frac{R_f}{R_0},\qquad
\prod_{j=1}^m(1-\kappa h_j)=\frac{Y_f}{Y_0}.
\]
Choose equal steps \(h_j=s/m\) and introduce
\[
p_m(s)=\left(1-\frac{\kappa s}{m}\right)^m,\qquad
q_m(s)=\left(1+\frac{Ds}{m}\right)^m.
\]
Solving the two product equations for the initial support parameter and eliminating its initial determinant gives exactly
\[
c_m(s)=v-\frac{(v-u)d}{v}\frac{p_m(s)}{q_m(s)},
\]
and
\[
F_m(s)=d(\kappa+D)-\kappa c_m(s)-\frac{dE_f}{v}p_m(s)=0.
\]
Indeed, the second product says \(E_0=dE_f p_m/v\), while the first then says \(v-c=(v-u)d p_m/(vq_m)\); these are precisely the displayed identities. Thus every positive zero of \(F_m\) in the strict-admissibility region satisfies **both** exact product equations, not just approximate endpoint matching.

**2. Transversal roots persist at every sufficiently fine discretization.** On every compact positive interval in \(s\), as \(m\to\infty\),
\[
p_m(s)\longrightarrow e^{-\kappa s},\qquad
q_m(s)\longrightarrow e^{Ds}
\]
uniformly together with first derivatives. Consequently \(c_m\to c_\infty\) and \(F_m\to F_\infty\) in \(C^1\) locally. At a simple root \(s_*\), select a compact interval containing no other roots and on which the derivative has constant nonzero sign, with opposite endpoint signs. Uniform convergence gives an exact root \(s_m\) of \(F_m\) in that interval for **each sufficiently large integer** \(m\), and \(s_m\to s_*\). Then \(c_m(s_m)\to c_*\); strict inequalities persist, and \(0<s_m/m<1/\kappa\) eventually.

The source's Theorem 5.3 now supplies the \(3(m+1)\) positive, pairwise distinct NS triangles. Their total homothety scale is
\[
S_m=3\left(1-c_m(s_m)-d+\sum_{j=1}^m\frac{s_m}{m}E_{j,m}\right).
\]
Here the source's recovery formula (5.10) gives
\[
E_{j,m}=\frac{D\kappa}{\kappa R_{0,m}(1+Ds_m/m)^j+D Y_{0,m}(1-\kappa s_m/m)^j-1},
\]
where \(R_{0,m}=(v-c_m)/E_{0,m}\), \(Y_{0,m}=d/E_{0,m}\), and \(E_{0,m}=d(\kappa+D)-\kappa c_m\). By the assumed nonvanishing continuous denominator and convergence of the finite products uniformly in normalized step time, the recovery functions converge uniformly on the compact trajectory. Thus the displayed sum is a convergent right Riemann sum and
\[
\lim_{m\to\infty}S_m=3\left(1-c_*-d+\int_0^{s_*}E(t)\,dt\right).
\]
The coordinate minima in each finite family equal zero by the source theorem, so its least containing triangle has scale \(1\) and \(\lambda_m=1/S_m\). This proves \(\lambda_m\to\lambda_*\).

**3. Existence and strict feasibility of an explicit solution.** Use the rational parameters in the Finding and the interval endpoints
\[
a=\frac{1110182}{10^6},\qquad b=\frac{1110185}{10^6}.
\]
The standalone verifier uses exact outward-rounded rational fixed-point arithmetic and Taylor remainder bounds. It certifies the **strict** inequalities
\[
F_\infty(a)<0<F_\infty(b),\qquad \min_{a\le s\le b}F_\infty'(s)>10^{-6}.
\]
It also certifies all listed geometric inequalities uniformly for \(c_\infty(s)\), \(s\in[a,b]\), including \(\kappa<v\) and positive initial determinant. There is therefore one simple exact root \(s_*\in(a,b)\), independent of any floating-point root finder.

**4. A certified upper bound for the continuum total scale.** For the above rational data and all \(s\in[a,b]\), \(c_\infty(s)\) lies in a certified compact interval. Put \(c=c_\infty(s)\),
\[
R_c(t)=\frac{v-c}{E_0(c)}e^{Dt},\quad
Y_c(t)=\frac d{E_0(c)}e^{-\kappa t},\quad
K_c(t)=\kappa R_c(t)+D Y_c(t)-1.
\]
The verifier proves \(R_c(t)<Y_c(t)\) throughout \([0,b]\), so
\[
K_c'(t)=D\kappa(R_c(t)-Y_c(t))>0.
\]
It certifies \(K_c(b)<0\) uniformly, hence the denominator never vanishes. Therefore \(E_c(t)=D\kappa/K_c(t)\) is positive and increasing. With \(N=16384\), the right-endpoint rectangle rule yields
\[
\int_0^{s_*}E_c(t)\,dt
\le \int_0^b E_c(t)\,dt
\le\frac bN\sum_{j=1}^N E_c\left(\frac{jb}{N}\right).
\]
Every rectangle term and the leftmost support parameter is bounded by outward-rounded intervals, giving the **exact rational comparisons**
\[
S_\infty<0.940465236<\frac{10000}{10633}.
\]
Thus \(\lambda_*=1/S_\infty>10633/10000\). Since \(\lambda_m\to\lambda_*\), the same strict bound holds for every sufficiently large finite chain.

## Verification

Run the standalone, Python-standard-library-only verifier with

```text
python3 verify_chain.py
```

It uses integer arithmetic on the \(10^{40}\) grid with outward rounding, and brackets each exponential by the degree-18 Taylor polynomial with the rigorous remainder \(3/19!\) whenever the argument lies in \((-1,1)\). The program asserts all sign, normalization and transversality inequalities, verifies negativity of the recovery denominator, and performs \(16384\) rigorously enclosed upper-rectangle evaluations. It prints `VERIFY_OK` only if the exact integer comparisons pass.

This is an analytic existence proof and an interval arithmetic certificate; it does not confuse a finite numerical experiment with the existence of all sufficiently long chains. The universal-in-\(m\) assertion comes from uniform convergence, the intermediate value theorem and the source's contact theorem, not from testing finitely many \(m\).

## Relationship to prior work

Bezdek--Lángi [2] surveyed classical non-separable homothetic covering bounds and the then-open search for the planar sharp covering factor. Akopyan--Balitskiy--Grigorev [3] proved the general planar upper bound \(3/2\). Neither paper develops the later cyclic-chain endpoint recurrence.

Lian--Xue--Yuan [1] prove a **rigorous finite** factor \(250000000/235141779\), and separately present a continuous-model **numerical** candidate near \(1.0633083238\). They explicitly explain that the finite endpoint products cannot be attained while holding the continuous support and terminal parameters fixed, and leave convergence of suitable finite chains open. Their Theorem 5.3 gives a finite construction once the two exact product equations hold; Section 7 does not supply a perturbation realizing both products simultaneously.

Here the supporting parameter \(c_m\) is algebraically eliminated and the total length \(s_m\) is adjusted by a scalar simple-root argument. This achieves both finite endpoint equalities exactly and proves asymptotic realization for the transversal interior class. A separate exact interval certificate supplies a new unconditional planar lower bound above \(1.0633\). This does not demonstrate that the source's numerical boundary candidate is attained or is optimal.

## Limitations

The existence of finite examples is proved for every sufficiently large chain length, but no explicit starting integer \(m_0\) or concrete list of rational triangle coordinates is furnished. The coordinates for a chosen large \(m\) are defined by a real root of the exact finite scalar equation and are therefore unambiguously mathematical, not rounded numerical data.

The approximation principle requires strict source inequalities and a transversal scalar root. It does not cover degenerate or tangent endpoint roots, including any boundary optimum where these hypotheses fail. It neither proves optimality of the chain pattern nor determines the global supremal factor. The displayed decimal certificate proves the strict rational bound; it does not claim more than that bound.

## References

1. Yanlu Lian, Fei Xue, and Qihui Yuan, *Non-Separable Homothetic Triangles, Part I: Constructions and Lower Bounds*, arXiv:2609.06558v1, first publicly posted 6 September 2026, especially Theorem 5.3 and Section 7.
2. Károly Bezdek and Zsolt Lángi, *Notes on non-separable arrangements of convex bodies*, arXiv:2512.23651v1, December 2025, overview of covering constants.
3. Arseniy Akopyan, Alexey Balitskiy, and Mikhail Grigorev, *On the Circle Covering Theorem by A. W. Goodman and R. E. Goodman*, arXiv:1605.04300v2, February 2017, general homothetic-covering upper bound.
