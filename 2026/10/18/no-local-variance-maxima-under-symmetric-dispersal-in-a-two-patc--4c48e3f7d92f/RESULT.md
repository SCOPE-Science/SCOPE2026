# No local-variance maxima under symmetric dispersal in a two-patch fluctuating population

## Finding

Let \(a,b>0\). Consider a stable two-patch linear population-fluctuation process with equal reciprocal dispersal intensity \(d\ge0\), driven by possibly correlated, additive white-noise forcing with any positive-semidefinite covariance matrix. Each individual patch's stationary fluctuation variance, as a function of \(d\), is either constant, strictly increasing, strictly decreasing, or strictly decreases to **one unique global minimum** and then strictly increases. **An interior local maximum is impossible**, and **both patches cannot have interior minima**. This classification holds even under perfect correlation or anticorrelation of the forcing.

For independent forcing with strictly positive intensities \(q,r\), patch 1 has an interior minimum if and only if
\[
\frac rq>\frac{a^2+4ab+5b^2}{a^2+4ab+b^2}.
\]
Otherwise its variance strictly decreases with dispersal. The corresponding threshold for patch 2 is obtained by interchanging \((a,q)\) with \((b,r)\). At most one threshold can be met. The condition is sharp for every \(a,b>0\).

## Assumptions and scope

Fix real \(a,b>0\), \(d\ge0\), and real \(q,r,c\) with \(q,r\ge0\) and \(c^2\le qr\). Let \(B(t)\) be a two-dimensional Brownian process with increment covariance \(Q\,dt\), where
\[
Q=\begin{pmatrix}q&c\\c&r\end{pmatrix}.
\]
The centered fluctuations \(X(t)=(X_1(t),X_2(t))^\top\) solve
\[
dX(t)=-H(d)X(t)\,dt+dB(t),\qquad
H(d)=\begin{pmatrix}a+d&-d\\-d&b+d\end{pmatrix}.
\]
As \(H(d)\) is positive definite, there is a unique stationary Gaussian law, possibly degenerate, with covariance \(\Sigma(d)\) solving \(H\Sigma+\Sigma H=Q\). Put \(V_1(d)=\Sigma_{11}(d)\) and \(V_2(d)=\Sigma_{22}(d)\). All claims concern stationary **linearized fluctuation variance**, not nonnegative population counts, extinction probabilities, or nonlinear ecological persistence.

For the full classification of \(V_1\), define
\[
\begin{aligned}
K&=a^2+4ab+b^2,\\
A&=Kr+2(a^2+2ab-b^2)c-(a^2+4ab+5b^2)q,\\
C&=b^2(a+b)[2ac-(a+b)q].
\end{aligned}
\]
Then \(V_1\) has exactly one strict finite minimum if \(C<0<A\); it is strictly decreasing if \(C<0\) and \(A\le0\); it is strictly increasing if \(C\ge0\) and the covariance is not of the constant-variance form described next. Its only constant cases are \(Q=0\) and \(a=b\) with \(q=r=c\) (a common-noise mode). The classification for \(V_2\) swaps \((a,q)\) with \((b,r)\) and leaves \(c\) fixed.

## Proof

**1. Exact covariance.** Write \(\Sigma=\left(\begin{smallmatrix}x&z\\z&y\end{smallmatrix}\right)\). The Lyapunov equation is equivalent to
\[
2(a+d)x-2dz=q,\quad (a+b+2d)z-d(x+y)=c,\quad 2(b+d)y-2dz=r.
\]
Solving yields
\[
V_1(d)=\frac{abq+adq+b^2q+3bdq+2bcd+d^2(q+r+2c)}{2(a+b+2d)[ab+(a+b)d]}.
\]
The formula for \(V_2\) is obtained by swapping the patches. Every denominator displayed here is positive on the full specified domain.

**2. The derivative polynomial and the one-stationary-point rule.** Direct differentiation gives
\[
V_1'(d)=\frac{Ad^2+Bd+C}{2(a+b+2d)^2[ab+(a+b)d]^2},
\]
where \(A,C\) are above and
\[
B=4ab(a+b)c+2ab(a+b)r-2b(a^2+3ab+2b^2)q.
\]
The rational function \(V_1\) has a quadratic numerator and denominator of the same degree. The denominator is proportional to \((d+s)(d+t)\), with \(s=(a+b)/2>t=ab/(a+b)>0\). Partial fractions therefore give \(V_1(d)=V_\infty+U/(d+s)+W/(d+t)\) for real constants \(U,W\). Thus its derivative is \(-U/(d+s)^2-W/(d+t)^2\). If \(U,W\) have opposite signs, a zero requires the strictly monotone ratio \([(d+s)/(d+t)]^2\) to equal a fixed positive constant; if they do not, there is no zero unless the derivative vanishes identically. Consequently a nonconstant \(V_1\) has **at most one** stationary point, and any such stationary point is a strict sign-changing extremum.

**3. A covariance obstruction to maxima.** If \(q>0\) and \(C\ge0\), then \(h=c/q\ge h_0=(a+b)/(2a)\). Positive semidefiniteness implies \(r/q\ge h^2\). Therefore
\[
\frac Aq\ge F(h):=Kh^2+2(a^2+2ab-b^2)h-(a^2+4ab+5b^2).
\]
Direct substitution and differentiation give
\[
F(h_0)=\frac{(a-b)^2K}{4a^2}\ge0,
\qquad
F'(h_0)=\frac{3a^3+9a^2b+3ab^2+b^3}{a}>0.
\]
Because \(F\) is a convex quadratic with positive derivative at \(h_0\), it is increasing thereafter. Thus \(C\ge0\) forces \(A\ge0\), with strict positivity when \(C>0\). If \(q=0\), positive semidefiniteness gives \(c=0\), \(C=0\), and \(A=Kr\ge0\), yielding the same conclusion.

When \(A=0\), direct elimination of \(r\) gives
\[
B=\frac{4(a+b)}K C.
\]
When \(C=0\), elimination of \(c\) gives \(B=2b(a+b)(ar-bq)\ge0\): for \(q>0\) the inequality follows from \(r/q\ge(a+b)^2/(4a^2)\ge b/a\), and the \(q=0\) case is immediate.

Hence \(C>0\) implies the derivative is positive near zero and at infinity, and the one-stationary-point rule forces positivity everywhere. The case \(C=0\) is also nondecreasing and is strictly increasing unless constant. If \(C<0<A\), the derivative changes once from negative to positive, giving a unique strict global minimum. If \(C<0\) and \(A\le0\), the derivative stays negative (including the \(A=0\) case by the displayed relation for \(B\)). These exhaust all cases. The equality cases \(A=C=0\) force \(Q=0\), or \(a=b\), \(c=q=r\); then \(V_1\) is constant by the covariance equation. In particular an interior local maximum never occurs.

**4. At most one patch has a minimum.** Differentiating the Lyapunov trace identity gives
\[
V_1(d)+V_2(d)=\tfrac12\operatorname{tr}(QH(d)^{-1}),
\qquad
\frac{d}{dd}(V_1+V_2)
=-\tfrac12\operatorname{tr}\bigl(QH^{-1}LH^{-1}\bigr)\le0,
\]
where \(L=\left(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\right)\succeq0\). The inequality follows because \(Q\succeq0\). A patch having a strict interior minimum must have positive variance derivative for every larger \(d\). If both patches had a minimum, their derivatives would eventually both be positive, contradicting the trace inequality.

**5. Independent-noise boundary.** Set \(c=0\) and \(q,r>0\). Then \(C=-b^2(a+b)^2q<0\). Thus the unique-minimum condition \(A>0\) becomes precisely the stated sharp ratio \(r/q>(a^2+4ab+5b^2)/K\). For patch 2 the swapped ratio is \(q/r>(b^2+4ab+5a^2)/K\). Since
\[
(a^2+4ab+5b^2)(b^2+4ab+5a^2)-K^2=4(a+b)^4>0,
\]
the two strict inequalities cannot hold at once.

**6. Exact witness and regional contrast.** Take \(a=b=q=1\), \(r=4\), and \(c=0\). Then
\[
V_1(d)=\frac{5d^2+4d+2}{4(d+1)(2d+1)},\qquad
V_1'(d)=\frac{7d^2+2d-2}{4(d+1)^2(2d+1)^2}.
\]
The unique positive minimum is at \(d_*=(\sqrt{15}-1)/7\), with
\[
V_1(0)=\tfrac12,\qquad V_1(d_*)=\tfrac12(\sqrt{15}-3),\qquad \lim_{d\to\infty}V_1(d)=\tfrac58.
\]
Meanwhile, the **total-population** fluctuation \(X_1+X_2\) solves a one-dimensional Ornstein–Uhlenbeck equation with damping 1 and forcing intensity 5, so \(\operatorname{Var}(X_1+X_2)=5/2\) for **every** \(d\). Local-risk nonmonotonicity is therefore invisible to this regional aggregate.

## Verification

The standalone `verify.py` script symbolically solves the full Lyapunov system, reproduces the exact variance and derivative expressions, checks the coefficient and boundary identities, validates the trace derivative, and checks the complete radical witness. It also tests 1,280 rational positive-semidefinite covariance parameter tuples for sign exclusions and incompatibility of simultaneous local minima. Run with `python verify.py` using Python 3 and SymPy. The unrestricted classification is proved above; the parameter grid is supplementary rather than an infinite proof.

## Relationship to prior work

Linearized stochastic spatial ecology and the consequences of dispersal are established subjects. Lande, Engen, and Sæther (1999) studied spatial synchrony in homogeneous local dynamics and spatially correlated environments. Colombo and Anteneodo (arXiv:1503.08168, first public March 27, 2015) analyzed coupling and environmental fluctuations for nonlinear, spatially heterogeneous metapopulations, including multiplicative noise and population survival. Hening, Nguyen, and Yin (arXiv:1605.02027, first public May 6, 2016) addressed multiplicative stochastic growth and persistence, including two-patch cases and degenerate noise. These models and objectives do not state the local *additive* stationary covariance classification derived here. The simple two-patch Lyapunov equation is standard; the asserted contribution is its all-positive-semidefinite-covariance shape classification, the exclusion of two local minima, and the sharp independent-noise threshold and regional-versus-local contrast.

## Limitations

The theorem assumes **two patches**, symmetric dispersal, fixed local return rates, and additive time-white noise. Its interpretation concerns fluctuations around an assumed stable equilibrium; its Gaussian paths may be negative and should not be read as literal abundance values. It says nothing about nonlinear demographic persistence, absorbing extinctions, parameter estimation, or networks with more patches. A fully equivalent earlier result may exist in OU filtering, statistical mechanics, or spatial ecology literature under different language; bibliographic verification remains incomplete, including the full 1999 Lande–Engen–Sæther article, which was not accessible through the checked routes.

## References

1. R. Lande, S. Engen, and B.-E. Sæther, *Spatial scale of population synchrony: Environmental correlation versus dispersal and density regulation*, American Naturalist 154 (1999), 271–281. DOI: 10.1086/303240.
2. E. H. Colombo and C. Anteneodo, *Metapopulation dynamics in a complex ecological landscape*, arXiv:1503.08168 (first public 2015-03-27), https://arxiv.org/abs/1503.08168.
3. A. Hening, D. H. Nguyen, and G. Yin, *Stochastic population growth in spatially heterogeneous environments: The density-dependent case*, arXiv:1605.02027 (first public 2016-05-06), https://arxiv.org/abs/1605.02027.
4. M. J. Keeling, *Metapopulation moments: Coupling, stochasticity and persistence*, Journal of Animal Ecology 69 (2000), 725–736. DOI: 10.1046/j.1365-2656.2000.00430.x.
