# Sharp asymmetric double-exponential Gabor frame bounds at every higher integer redundancy

## Finding

Let \(a,b>0\) be distinct, let \(q\ge3\) be an integer, and set \(g(t)=e^{-at}\) for \(t\ge0\), \(g(t)=e^{bt}\) for \(t<0\). For the complete Gabor family
\[
\mathcal G=\{e^{2\pi i mt/q}g(t-k):m,k\in\mathbb Z\},
\]
all optimal frame constants are given by the following finite expressions. For each \(j=0,\ldots,q-1\), define
\[
u_j=\frac{e^{-aj}}{1+e^{-aq}},\quad
v_j=\frac{e^{-b(q-j)}}{1+e^{-bq}},\quad
U=\sum_j u_j^2,\quad V=\sum_j v_j^2,\quad W=\sum_j u_jv_j,
\]
and
\[
 t_* =\frac{(b-a)W+\sqrt{(a-b)^2W^2+4abUV}}{2bV},
 \qquad x_* =\frac{\log t_*}{a+b}.
\]
Then \(0<x_*<1\), and the **optimal lower frame bound** is
\[
\boxed{A=q\big(U e^{-2ax_*}+V e^{2bx_*}-2W e^{(b-a)x_*}\big)>0.}
\]
With
\[
 u_j^+=\frac{e^{-aj}}{1-e^{-aq}},\qquad
 v_j^+=\frac{e^{-b(q-j)}}{1-e^{-bq}},
\]
the **optimal upper frame bound** is
\[
\boxed{B=q\sum_{j=0}^{q-1}(u_j^++v_j^+)^2.}
\]
These constants are sharp in the inequality
\[
 A\lVert f\rVert_2^2\le\sum_{m,k\in\mathbb Z}|\langle f,M_{m/q}T_k g\rangle|^2\le B\lVert f\rVert_2^2
 \quad(f\in L^2(\mathbb R)).
\]
In the Zak fundamental domain, the sole minimal spatial coordinate is \(x_*\), attained at the frequency phases \(q\omega\equiv1/2\pmod1\), while the maximum occurs only at integer spatial coordinates and \(q\omega\equiv0\pmod1\). Thus the exact condition number is \(B/A\), and the optimizing phase-space fibers are completely classified.

## Assumptions and scope

The unnormalized two-sided exponential is continuous at the origin and square-integrable. Translation spacing is exactly one; modulation spacing is exactly \(1/q\). Distinct positive rates ensure genuine asymmetry. All integers \(q\ge3\) are included. The modulation, translation and Zak conventions are
\[
(M_\xi f)(t)=e^{2\pi i\xi t}f(t),\quad
(T_k f)(t)=f(t-k),\quad
Zg(x,\omega)=\sum_{n\in\mathbb Z}g(x+n)e^{-2\pi in\omega}.
\]
The two-dimensional Zak parameter domain is \(0\le x,\omega<1\). In formulas for the spectral extrema, the spatial coordinate is understood modulo one, and the phase \(q\omega\) modulo one.

## Proof

**1. Zak reduction and normalization.** For integer redundancy \(q\), unitarity of the Zak transform and Fourier orthogonality give the exact frame multiplier
\[
F_q(x,\omega)=\sum_{h=0}^{q-1}|Zg(x,\omega+h/q)|^2.
\]
For \(0\le x<1\), split the integer indices into residue classes \(j+q\mathbb Z\), where \(0\le j<q\). With \(z=e^{-2\pi iq\omega}\), \(s=e^{-aq}\), \(r=e^{-bq}\), and \(c=x+j\), the geometric sums yield
\[
P_j(x,z)=\sum_{h\in\mathbb Z}g(c+qh)z^h
=\frac{e^{-ac}}{1-sz}+\frac{e^{-b(q-c)}}{z-r}
=\frac{\alpha_j(x)z+\beta_j(x)}{(1-sz)(z-r)},
\]
where
\[
\alpha_j(x)=e^{-ac}-sr e^{bc}>0,\qquad
\beta_j(x)=r(e^{bc}-e^{-ac})\ge0.
\]
The inequalities follow from \(0\le c<q\). Orthogonality of the \(q\) roots of unity now gives
\[
F_q(x,\omega)=q\sum_{j=0}^{q-1}|P_j(x,z)|^2.
\]
Both displayed identities are exact, not numerical approximations.

**2. Frequency monotonicity.** Set \(h=\operatorname{Re}z\in[-1,1]\). Every term in the last sum equals
\[
\frac{\alpha_j(x)^2+\beta_j(x)^2+2\alpha_j(x)\beta_j(x)h}
{(1-2sh+s^2)(1-2rh+r^2)}.
\]
The numerator is nonnegative and nondecreasing in \(h\); both positive denominator factors strictly decrease in \(h\). At least one numerator is positive throughout, so the full multiplier strictly increases in \(h\). Hence its global frequency minimum always occurs at \(z=-1\), and maximum at \(z=1\). In particular, no hidden interior-frequency extremum can improve either constant.

**3. Upper bound and maximizing fiber.** At \(z=1\), the summands are
\[
P_j(x,1)=u_j^+e^{-ax}+v_j^+e^{bx}>0.
\]
Thus \(F_q(x,0)=q\sum_j(u_j^+e^{-ax}+v_j^+e^{bx})^2\) is a strictly convex function of \(x\in[0,1]\), since each positive exponential sum has positive second derivative and its square is strictly convex. Zak quasiperiodicity ensures \(F_q(0,0)=F_q(1,0)\). Therefore the only spatial maximizers modulo one are integers; substitution at \(x=0\) gives \(B\).

**4. Lower bound and unique minimizing fiber.** At \(z=-1\), the geometric sums instead give
\[
P_j(x,-1)=u_j e^{-ax}-v_j e^{bx},
\quad F_q(x,1/(2q))=q(Ue^{-2ax}+Ve^{2bx}-2We^{(b-a)x}).
\]
Differentiation and the substitution \(t=e^{(a+b)x}>0\) show that every stationary point solves
\[
bVt^2+(a-b)Wt-aU=0.
\]
The constant coefficient is strictly negative and the leading coefficient strictly positive, so this equation has exactly one positive root, namely \(t_*\). The derivative is negative before this root and positive after it. Moreover \(F_q(0,1/(2q))=F_q(1,1/(2q))\) by Zak quasiperiodicity. A continuously differentiable function with one strictly sign-changing minimum, equal endpoints, and nonconstant derivative must have its unique minimum strictly between the endpoints. Thus \(1<t_*<e^{a+b}\), equivalently \(0<x_*<1\). Substitution establishes the formula for \(A\) and uniqueness of the minimizing fiber.

**5. Strict frame property and sharpness.** The vectors \((u_j)_{j=0}^{q-1}\) and \((v_j)_{j=0}^{q-1}\) are not proportional: their coordinate ratios vary by the positive factor \(e^{a+b}\) from one index to the next. Hence strict Cauchy–Schwarz gives \(UV-W^2>0\). Consequently
\[
U e^{-2ax}+V e^{2bx}-2W e^{(b-a)x}>0
\]
for every real \(x\), proving \(A>0\). All Zak multipliers are continuous and the extrema above are attained. By unitarity of the Zak transform, their exact essential infimum/supremum are the optimal Gabor frame bounds. This completes the infinite-dimensional proof.

## Verification

Run `python3 CHECK.py` with a standard Python 3 installation. The checker independently evaluates finite truncations of the defining bilateral Zak series, compares them with the closed geometric-polyphase representation, verifies the candidate extremizers, scans interior phase-space points for numerous asymmetric slope pairs and redundancies, and checks rational geometric-series identities. It returns `CHECK_OK assertions=6246`. These computations are supplementary; the proof above establishes the stated universal quantifiers.

For example, at \(q=3\), \(a=0.3\), and \(b=0.7\), the formulas give \(A\approx0.9391720232\), \(B\approx23.6716332018\), and \(x_*\approx0.5452008240\). The minimizing coordinate moves away from the symmetric midpoint, a feature not visible in equal-rate formulas.

## Relationship to prior work

The integer-density Zak multiplier formula is classical. Kloos and Stöckler (2013/2014) established qualitative and nonsharp estimates for totally positive Gabor windows, including symmetric two-sided exponentials. Faulhuber and Shafkulovska (2022/2023), extending Janssen's framework, gave exact frame bounds and lattice optimization for **equal-rate**, even two-sided exponentials. The redundancy-two asymmetric setting is excluded from the novelty claim, as it has a separate earlier exact treatment. The present statement is restricted to the entire higher-redundancy family \(q\ge3\), where the non-even skew changes the unique minimizing spatial fiber and the exact lower constant.

The 2026 work of de Dios Pont, Gröchenig, Liehr, Shafkulovska and Taylor proves the all-density qualitative frame-set characterization for continuous totally positive generators. The present calculation specifies **both sharp constants and their exact optimizing Zak fibers** for the asymmetric two-sided exponentials at every integer redundancy at least three. These conclusions do not follow from a qualitative existence theorem or the symmetric formula by reflection or dilation, since neither operation makes unequal exponential rates equal. The inspected primary sources do not state this full higher-redundancy skew profile.

## Limitations

The result treats the integer-redundancy lattice \(\mathbb Z\times q^{-1}\mathbb Z\), strictly positive decay rates, and exactly this piecewise exponential generator. It does not classify arbitrary noninteger rational or irrational densities, dual windows, or optimal lattice geometries. The equal-rate and redundancy-two cases have antecedents and are not novelty claims. A related 1996 paper by Janssen on several exact frame-bound calculations was located, but its full text could not be inspected; it remains a documented priority risk. Independent review has not been performed.

## References

1. J. de Dios Pont, K. Gröchenig, L. Liehr, I. Shafkulovska, M. A. Taylor, *Gabor Frames of Totally Positive Functions: A Complete Characterization*, arXiv:2608.04992, first submitted 2026-08-05. https://arxiv.org/html/2608.04992v1
2. T. Kloos, J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359 (2013), *J. Approx. Theory* 184 (2014), 209–237. https://arxiv.org/abs/1311.7359
3. M. Faulhuber, I. Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917 (2022; revised 2023). https://arxiv.org/html/2204.02917v2
4. A. J. E. M. Janssen, *Some Weyl–Heisenberg frame bound calculations*, *Indag. Math.* 7 (1996), 165–183. https://doi.org/10.1016/0019-3577(96)85088-9

