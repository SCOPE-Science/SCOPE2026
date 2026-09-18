# Curvature gives the exact proportional recovery-diffusion threshold for FitzHugh--Nagumo barriers

## Result

Consider the heterogeneous FitzHugh--Nagumo system studied by Courdurier and Paduro,

\[
v_t-\frac1{a(x)}\partial_x(b_0v_x)=f(v,x)-w,
\qquad
\tau w_t-\delta(x)w_{xx}=v-\gamma w,
\]

with constant \(b_0>0\), positive piecewise-smooth \(a,\delta\), and the source paper's stationary-barrier transmission convention. Let \(V>0\) be a fixed continuous piecewise-\(C^2\) activator profile satisfying \([V']_\xi\le0\) at every interface, and put

\[
h_V(x)=\min\{-f(V(x),x),f(-V(x),x)\},
\qquad
\mathcal A V=\frac{b_0}{a(x)}V''.
\]

Define

\[
c_*:=\inf_x\frac{h_V(x)-\mathcal A V(x)}{V(x)},
\qquad
\kappa_\delta:=\sup_x\delta(x)\frac{[V''(x)]_+}{V(x)},
\]

where the extrema are taken over the smooth pieces. Assume \(V''>0\) somewhere. Then there exists a constant \(c>0\) for which

\[
(V,cV,-V,-cV)
\]

is a stationary barrier if and only if

\[
\boxed{c_*>\frac1\gamma,
\qquad
\kappa_\delta\le \gamma-\frac1{c_*}.}
\]

When these conditions hold, the largest admissible proportional coefficient is optimal: \(c=c_*\) works. Thus a fixed activator barrier has an exact recovery-diffusion budget inside the entire constant-proportional ansatz \(W=cV\).

For constant recovery diffusion \(\delta\equiv D\), let

\[
\kappa_V:=\sup_x\frac{[V''(x)]_+}{V(x)}.
\]

If \(0<\kappa_V<\infty\), the exact persistence threshold for the fixed profile within this ansatz is

\[
\boxed{D_\sharp(V)=\frac{\gamma-1/c_*}{\kappa_V}.}
\]

Hence a proportional stationary barrier exists exactly for \(0<D\le D_\sharp(V)\).

## Proof

For the symmetric proportional tuple \((V,cV,-V,-cV)\), the two activator inequalities are equivalent to

\[
\mathcal A V\le h_V-cV,
\]

so they hold exactly when \(c\le c_*\). The recovery inequalities reduce to

\[
\delta(x)cV''(x)\le (\gamma c-1)V(x).
\]

Because \(\delta>0\), \(V>0\), and \(V''>0\) somewhere, this forces \(c>1/\gamma\). For such \(c\), points with \(V''\le0\) impose no further restriction, while points with \(V''>0\) give

\[
\delta(x)\frac{V''(x)}{V(x)}\le \gamma-\frac1c.
\]

Thus the recovery inequalities are equivalent to

\[
\kappa_\delta\le \gamma-\frac1c.
\]

The right-hand side is strictly increasing in \(c\). Consequently there is an admissible \(c\in(1/\gamma,c_*]\) if and only if \(c_*>1/\gamma\) and \(\kappa_\delta\le\gamma-1/c_*\), and then \(c=c_*\) is admissible. Since \(b_0\) and \(c\) are positive constants, both component transmission inequalities reduce to the assumed sign condition on \([V']\). The constant-\(D\) formula follows by writing \(\kappa_\delta=D\kappa_V\).

## Application to the source paper's exponential-tail barriers

The source paper proves persistence of a \(D=0\) barrier constructed with an auxiliary parameter \(0<\widetilde\gamma<\gamma\), keeping the recovery component \(W=V/\widetilde\gamma\), whenever recovery diffusion is sufficiently small. Its proof uses the global Lipschitz estimate

\[
d^*=\frac{\gamma-\widetilde\gamma}{C},
\qquad C=\max\{L_K,1\},
\]

and the sufficient condition \(a(x)\delta(x)/b_0\le d^*\).

For the exponentially decaying version of the source construction, the initial homogeneous tail is not merely an inequality: after replacing \(\gamma\) by \(\widetilde\gamma\), it satisfies

\[
\sigma_-V''=h_0(V)-\frac{V}{\widetilde\gamma},
\qquad \sigma_-=\frac{b_0}{a_-}.
\]

Therefore on that tail

\[
\frac{h_0(V)-\sigma_-V''}{V}=\frac1{\widetilde\gamma}.
\]

The \(D=0\) barrier inequality gives the opposite global bound, so the proportional activator budget is pinned exactly:

\[
\boxed{c_*=\frac1{\widetilde\gamma}.}
\]

Hence no alternative constant proportional choice \(W=cV\) can improve the recovery-diffusion allowance for the same activator profile. The exact criterion becomes

\[
\boxed{\sup_x\delta(x)\frac{[V''(x)]_+}{V(x)}
\le \gamma-\widetilde\gamma.}
\]

For constant diffusion,

\[
\boxed{D_\sharp(V)=\frac{\gamma-\widetilde\gamma}{\kappa_V}.}
\]

This refines the source theorem's global coefficient bound into a profile-dependent necessary-and-sufficient condition within the proportional class. It also shows that large recovery diffusion is harmless on flat or concave portions of the barrier; only positive normalized curvature consumes the diffusion budget.

The source proof remains a valid uniform sufficient estimate. Indeed its argument implies

\[
\kappa_V\le \frac{C}{b_0}\sup_x a(x),
\]

and therefore

\[
D_\sharp(V)\ge
\frac{(\gamma-\widetilde\gamma)b_0}{C\sup_x a(x)},
\]

which is precisely the constant-diffusion level guaranteed by its displayed smallness condition.

There is also an unavoidable tail ceiling. If

\[
k=-f_0'(0)>\frac1{\widetilde\gamma},
\]

then the exponential tail equation yields

\[
\frac{V''}{V}\longrightarrow
\frac{k-1/\widetilde\gamma}{\sigma_-}
\quad(x\to-\infty).
\]

Thus

\[
\boxed{D_\sharp(V)\le
\sigma_-\frac{\gamma-\widetilde\gamma}
{k-1/\widetilde\gamma}.}
\]

Equivalently, if \(\lambda_-^2=(k-1/\widetilde\gamma)/\sigma_-\) is the squared left-tail spatial exponent, then \(D_\sharp\le(\gamma-\widetilde\gamma)/\lambda_-^2\).

## The source sufficient bound can be arbitrarily conservative

The gap between the global Lipschitz estimate and the exact profile threshold is not bounded by a universal constant. Set \(a=b_0=1\), choose \(c_0=1/\widetilde\gamma>1/\gamma\), and take

\[
f(v)=-(1+c_0)v,
\qquad
V(x)=\begin{cases}e^x,&x<0,\\1,&x\ge0.\end{cases}
\]

Then \(h_V=(1+c_0)V\), the activator inequality is an equality on \(x<0\), and \([V']_0=-1\le0\). Hence \((V,c_0V,-V,-c_0V)\) is a \(D=0\) barrier for the auxiliary recovery parameter \(\widetilde\gamma=1/c_0\). Here

\[
c_*=c_0,\qquad \kappa_V=1,
\]

so

\[
D_\sharp=\gamma-\widetilde\gamma.
\]

By contrast, the source proof has \(C=1+c_0\) and guarantees only

\[
D\le\frac{\gamma-\widetilde\gamma}{1+c_0}.
\]

The ratio between the exact proportional threshold and that sufficient guarantee is exactly \(1+c_0\), which is unbounded as \(c_0\to\infty\). For example, \(\gamma=2\) and \(\widetilde\gamma=1/2\) give the exact threshold \(D_\sharp=3/2\), whereas the displayed sufficient bound gives \(D\le1/2\). For every \(D>3/2\), the recovery inequality fails on the entire exponential tail, so the threshold is genuinely sharp for this fixed profile and proportional class.

## Scope and limitations

The threshold is exact for a fixed positive activator profile \(V\) and constant-proportional recovery components \(W=cV\). It is not a global threshold for propagation failure, and it does not rule out a different barrier with a nonproportional recovery profile when \(D>D_\sharp(V)\). The tail identity applies to the exponentially decaying version of the source construction; barriers with a positive constant far-left tail require a separate analysis. The statement uses the source paper's nondivergence recovery operator and its interface convention.

## Prior literature and originality boundary

The source paper itself establishes persistence for sufficiently small recovery diffusion but does not state the profile-wise necessary-and-sufficient curvature criterion above. Kajiwara's 2018 work develops a sub/supersolution method for heterogeneous FitzHugh--Nagumo systems and introduces a Rayleigh-quotient parameter for a related stationary problem; its accessible abstract was inspected, but the complete article was not independently inspected here, so it remains the most plausible literature risk for a more general result implying part of this criterion. Earlier double-diffusive FitzHugh--Nagumo work also studies stationary pulses and heteroclinic structures. These general methods and phenomena are not claimed as new.

The originality claim is restricted to the explicit proportional-barrier criterion, its saturation by the source paper's exponential tail, the resulting exact profile threshold and tail ceiling, and the unbounded conservatism example for the specific persistence mechanism in arXiv:2609.14944v1. Originality is asserted only to the best of our knowledge.

## References

1. M. Courdurier and E. Paduro, *Propagation failure in heterogeneous FitzHugh--Nagumo systems via coupled upper and lower solutions*, arXiv:2609.14944v1 (2026).
2. T. Kajiwara, *The sub-supersolution method for the FitzHugh-Nagumo type reaction-diffusion system with heterogeneity*, Discrete Contin. Dyn. Syst. 38 (2018), 2441--2465, doi:10.3934/dcds.2018101.
3. C. A. Klaasen and W. C. Troy, *Stationary wave solutions of a system of reaction-diffusion equations derived from the FitzHugh--Nagumo equations*, SIAM J. Appl. Math. 44 (1984), 96--110, doi:10.1137/0144008.
