# Sharp stagewise-safe Richardson frontier and a no-acceleration barrier

**Same-model review: passed. Independent audit: not yet performed.**

## Result

Let
\[
A=A^\top\succ0,\qquad \sigma(A)\subset[\mu,L],\qquad 0<\mu<L,
\]
and consider two nonstationary Richardson steps
\[
x^{(1)}=x^{(0)}+\tau_1(b-Ax^{(0)}),\qquad
x^{(2)}=x^{(1)}+\tau_2(b-Ax^{(1)}).
\]
For the error \(e=x-x^\star\),
\[
e^{(2)}=p_2(A)e^{(0)},\qquad
p_2(\lambda)=(1-\tau_1\lambda)(1-\tau_2\lambda).
\]

Impose a stagewise safety requirement in the Euclidean operator norm:
\[
\|I-\tau_i A\|_2\le1
\quad\text{uniformly for every SPD }A\text{ with }\sigma(A)\subset[\mu,L],
\qquad i=1,2.
\]
Because \(A\) is symmetric, this is equivalent to
\[
\boxed{0\le\tau_i\le \frac2L.}
\]

Define the best robust two-stage factor under this requirement by
\[
Q_2^{\rm safe}(\mu,L)
=
\min_{0\le\tau_1,\tau_2\le2/L}
\max_{\lambda\in[\mu,L]}
|(1-\tau_1\lambda)(1-\tau_2\lambda)|.
\]
Write \(\kappa=L/\mu>1\).

### Theorem 1: exact two-stage frontier

There is a sharp phase transition at
\[
\boxed{\kappa_\star=1+\sqrt2.}
\]

If
\[
1<\kappa\le1+\sqrt2,
\]
the unconstrained degree-two Chebyshev polynomial is already stagewise safe, and
\[
\boxed{
Q_2^{\rm safe}
=
\frac{(\kappa-1)^2}{\kappa^2+6\kappa+1}.
}
\]
The optimal steps are, up to permutation,
\[
\boxed{
\tau_\pm
=
\frac{2}{L+\mu\pm (L-\mu)/\sqrt2}.
}
\]

If
\[
\kappa\ge1+\sqrt2,
\]
the Chebyshev factorization violates stagewise safety and the exact constrained optimum is
\[
\boxed{
Q_2^{\rm safe}
=
\frac{\kappa-2}{\kappa+2}
=
\frac{L-2\mu}{L+2\mu}.
}
\]
The unique optimal unordered pair is
\[
\boxed{
\{\tau_1,\tau_2\}
=
\left\{\frac2L,\frac{2}{L+2\mu}\right\}.
}
\]

Thus, once the condition number exceeds \(1+\sqrt2\), the best safe two-step cycle places one stage exactly on the single-step nonexpansive boundary \(2/L\); the second stage is then uniquely determined by endpoint balancing.

### Corollary 1: safe variation is better than repeating optimal fixed-step Richardson

The optimal fixed Richardson step is
\[
\tau_{\rm GD}=\frac{2}{L+\mu},
\qquad
q_{\rm GD}=\frac{\kappa-1}{\kappa+1}.
\]
In the constrained branch \(\kappa\ge1+\sqrt2\),
\[
q_{\rm GD}^2-Q_2^{\rm safe}
=
\boxed{
\frac{4}{(\kappa+1)^2(\kappa+2)}
}>0.
\]
Hence stagewise-safe variation gives a strict two-step improvement over simply repeating the best fixed step.

### Corollary 2: the price of stagewise safety relative to Chebyshev

The unrestricted degree-two Chebyshev factor is
\[
Q_2^{\rm Ch}
=
\frac{(\kappa-1)^2}{\kappa^2+6\kappa+1}.
\]
For \(\kappa>1+\sqrt2\),
\[
Q_2^{\rm safe}-Q_2^{\rm Ch}
=
\boxed{
\frac{4(\kappa^2-2\kappa-1)}
{(\kappa+2)(\kappa^2+6\kappa+1)}
}>0.
\]
Therefore the unrestricted two-step Chebyshev improvement beyond the transition necessarily uses at least one Richardson factor whose Euclidean operator norm exceeds one on the full spectral interval.

This does not contradict stable three-term implementations of Chebyshev semi-iteration: the restriction here is specifically that the method be represented as a product of first-order Richardson factors and that every factor itself be nonexpansive.

## Theorem 2: any number of individually nonexpansive Richardson stages loses Chebyshev-order acceleration

For \(m\ge1\), let
\[
Q_m^{\rm safe}(\mu,L)
=
\inf_{0\le\tau_j\le2/L}
\max_{\lambda\in[\mu,L]}
\prod_{j=1}^m |1-\tau_j\lambda|.
\]
If \(\kappa\ge2\), then
\[
\boxed{
\left(1-\frac2\kappa\right)^m
\le
Q_m^{\rm safe}(\mu,L)
\le
\left(\frac{\kappa-1}{\kappa+1}\right)^m.
}
\]
The lower bound follows from the single curvature \(\lambda=\mu\): every individually nonexpansive stage satisfies
\[
1-\tau_j\mu
\ge
1-\frac{2\mu}{L}
=
1-\frac2\kappa
\ge0.
\]
The upper bound is obtained by repeating \(\tau=2/(L+\mu)\).

Consequently, to force \(Q_m^{\rm safe}\le\varepsilon\) as \(\kappa\to\infty\), any such stagewise-safe first-order factorization requires
\[
m\ge
\frac{\log(1/\varepsilon)}
{-\log(1-2/\kappa)}
=
\left(\frac{\kappa}{2}+O(1)\right)\log\frac1\varepsilon.
\]
Repeated optimal Richardson attains the same leading \(\Theta(\kappa\log(1/\varepsilon))\) scaling. By contrast, unrestricted Chebyshev semi-iteration has the familiar \(\Theta(\sqrt\kappa\log(1/\varepsilon))\) spectral complexity. Thus individual nonexpansiveness of every first-order Richardson factor is itself a structural obstruction to Chebyshev-order acceleration.

## Proof of Theorem 1

Normalize the spectral interval by
\[
a=\frac{\mu}{L}=\frac1\kappa,\qquad
x=\frac{\lambda}{L},\qquad
u=L\tau_1,\quad v=L\tau_2.
\]
Stagewise safety becomes \(u,v\in[0,2]\), and
\[
Q_2^{\rm safe}
=
\min_{u,v\in[0,2]}
\max_{x\in[a,1]}
|(1-ux)(1-vx)|.
\]

### Chebyshev-feasible branch

Without the root restriction \(u,v\le2\), the unique degree-two minimax polynomial with \(p(0)=1\) on \([a,1]\) is the shifted Chebyshev polynomial. Its norm is
\[
M_{\rm Ch}(a)
=
\frac{(1-a)^2}{1+6a+a^2},
\]
and its two roots are
\[
r_\pm
=
\frac{1+a}{2}
\pm
\frac{1-a}{2\sqrt2}.
\]
Hence the corresponding normalized Richardson parameters are
\[
u_\pm=\frac1{r_\pm}
=
\frac{2}{1+a\pm(1-a)/\sqrt2}.
\]
The larger of these parameters is at most \(2\) exactly when
\[
1+a-\frac{1-a}{\sqrt2}\ge1
\iff
a\ge\sqrt2-1
\iff
\kappa\le1+\sqrt2.
\]
In this range the unconstrained minimax polynomial is feasible, so it is also the constrained optimum. Replacing \(a=1/\kappa\) gives the stated formula.

### Boundary branch

Now assume
\[
0<a\le\sqrt2-1.
\]
Set
\[
A=1-u,\qquad B=1-v,
\]
so \(A,B\in[-1,1]\). With \(c=1-a\),
\[
p(1)=AB,
\qquad
p(a)=(c+aA)(c+aB).
\]
Let
\[
m=\frac{1-2a}{1+2a}.
\]

We show that every feasible pair has
\[
\max\{|p(a)|,|p(1)|\}\ge m.
\]

If \(A\ge0\) or \(B\ge0\), then both factors at \(x=a\) are nonnegative, one is at least \(c\), and the other is at least \(c-a=1-2a\). Therefore
\[
p(a)\ge(1-a)(1-2a)\ge\frac{1-2a}{1+2a}=m,
\]
because \((1-a)(1+2a)\ge1\) for \(0\le a\le1/2\).

It remains to consider \(A,B<0\). Write
\[
x=-A,\qquad y=-B,\qquad x,y\in(0,1].
\]
Then
\[
p(1)=xy,
\qquad
p(a)=(c-ax)(c-ay).
\]
If \(xy\ge m\), the endpoint bound is already proved. Otherwise let \(s=xy\le m\). Since
\[
(1-x)(1-y)\ge0,
\]
we have
\[
x+y\le1+s.
\]
Hence
\[
\begin{aligned}
p(a)
&=c^2-ac(x+y)+a^2s\\
&\ge c^2-ac(1+s)+a^2s\\
&=(1-2a)(1-a-as)\\
&\ge(1-2a)(1-a-am)\\
&=m.
\end{aligned}
\]
Thus every feasible polynomial has interval norm at least \(m\).

Take now
\[
u=2,\qquad v=\frac{2}{1+2a}.
\]
Its two endpoint values are both exactly \(m\). Its roots are \(1/2\) and \(1/2+a\), so the unique interior extremum occurs at \(x=(1+a)/2\), where
\[
p\!\left(\frac{1+a}{2}\right)
=
-\frac{a^2}{1+2a}.
\]
The condition
\[
\frac{a^2}{1+2a}\le m
\]
is exactly
\[
a^2\le1-2a
\iff
a\le\sqrt2-1.
\]
Therefore the full interval norm equals \(m\), proving optimality.

Equality in the lower-bound argument requires \(xy=m\) and \(x+y=1+m\), hence
\[
\{x,y\}=\{1,m\}.
\]
Thus the optimal pair is unique up to permutation:
\[
\{u,v\}
=
\left\{2,1+m\right\}
=
\left\{2,\frac{2}{1+2a}\right\}.
\]
Returning to \((\mu,L)\) gives
\[
\left\{\tau_1,\tau_2\right\}
=
\left\{\frac2L,\frac{2}{L+2\mu}\right\}.
\]

## Context and relation to known results

Golub and Varga's classical 1961 work develops Chebyshev semi-iteration and its relation to Richardson-type methods. Axelsson's 2010 historical review explicitly notes a practical weakness of the factorized one-step Chebyshev form: for several Chebyshev parameters the individual matrices \(I-\tau_k C^{-1}A\) can have norm substantially larger than one, even though the completed polynomial is highly contractive; parameter permutations and stable three-term forms are used to control this behavior.

The result here isolates a sharp version of that tradeoff under an especially transparent safety constraint. It does not optimize rounding-error growth or internal amplification in a general recurrence. Instead it asks for every first-order Richardson factor itself to be a Euclidean nonexpansion, derives the exact two-stage minimax frontier, and shows that imposing this property at every stage rules out the \(\sqrt\kappa\) Chebyshev acceleration order for any number of stages.

Manteuffel's work on second-degree stationary methods solves a related but different minimax problem for stationary second-degree recurrences. Recent work by Sambharya and Stellato gives closed-form multi-step hyperparameter solutions for quadratic minimization under a data-distribution mean-square training objective. Neither checked formulation imposes the interval-uniform per-stage nonexpansiveness constraint used here.

## Computational model and limitations

- Exact arithmetic is assumed in the theorem. Each Richardson stage uses one multiplication by \(A\) and one residual update.
- The norm is the Euclidean operator norm, and the guarantee is uniform over the entire spectral interval \([\mu,L]\), not merely a particular finite set of eigenvalues.
- A matrix with a known discrete spectrum may admit better parameters tailored to its actual eigenvalues.
- The theorem does not claim that stagewise nonexpansiveness is the weakest useful stability notion. Ordering Chebyshev factors can reduce internal growth, and stable three-term Chebyshev recurrences fall outside the imposed factor-by-factor constraint.
- No floating-point backward-stability or rounding-error theorem is claimed.
- Nonsymmetric, indefinite, nonlinear, stochastic, adaptive, momentum, conjugate-gradient, and line-search methods are outside the statement.
- The full theorem-level text of both 1961 Golub--Varga papers was not inspected in the checked source access, so an equivalent historical statement hidden there remains a residual originality risk.
- General approximation theory contains minimax problems with restricted zero locations; the checked 2022 Pestovskaya abstract concerns a different monic-polynomial/zero-exclusion problem and does not establish the present normalized Richardson frontier.

## Reproducibility

`artifacts/verify_stagewise_safe_richardson.py` evaluates the closed forms on representative condition numbers, checks the resulting polynomial sup norms on dense interval grids, verifies the exact comparison identities numerically, and checks the general safe-stage sandwich for sample values. Its recorded output is in `artifacts/verification.txt`.

## References

1. G. H. Golub and R. S. Varga, “Chebyshev semi-iterative methods, successive overrelaxation iterative methods, and second order Richardson iterative methods. Part I,” *Numerische Mathematik* 3 (1961), 147–156. https://doi.org/10.1007/BF01386013
2. G. H. Golub and R. S. Varga, “Chebyshev semi-iterative methods, successive overrelaxation iterative methods, and second order Richardson iterative methods. Part II,” *Numerische Mathematik* 3 (1961), 157–168. https://doi.org/10.1007/BF01386014
3. O. Axelsson, “Milestones in the Development of Iterative Solution Methods,” *Journal of Electrical and Computer Engineering* 2010, Article 972794. https://doi.org/10.1155/2010/972794
4. T. A. Manteuffel, “Optimal Parameters for Linear Second-Degree Stationary Iterative Methods,” *SIAM Journal on Numerical Analysis* 19 (1982), 833–839. https://doi.org/10.1137/0719058
5. R. Sambharya and B. Stellato, “Learning Algorithm Hyperparameters for Fast Parametric Convex Optimization,” *SIAM Journal on Mathematics of Data Science* 8 (2026), 649–676. https://doi.org/10.1137/24M1712242
6. A. E. Pestovskaya, “Polynomials least deviating from zero with a constraint on the location of roots,” *Trudy Instituta Matematiki i Mekhaniki UrO RAN* 28 (2022), 166–175. https://journal.imm.uran.ru/node/1104
