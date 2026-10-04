# Sharp variance envelope at fixed success probability under memoryless catastrophe
## Finding
Fix a catastrophe probability \(q\in(0,1)\), put \(s=1-q\), and let \(T_0\) be a positive-integer-valued base completion time with probability generating function
\[
g(z)=\mathbb E[z^{T_0}].
\]
Under independent memoryless catastrophe at every step, the one-attempt success probability is
\[
p=g(s)\in(0,s].
\]
The mean restarted completion time is already determined by \(p\):
\[
\mathbb E[T]=\frac{1-p}{qp}.
\]
The remaining degree of freedom in the variance is
\[
M:=s g'(s)=\mathbb E[T_0s^{T_0}],
\]
because
\[
\operatorname{Var}(T)=
\frac{(1-p)(1+ps)-2qM}{p^2q^2}.
\]

For \(p<s\), define
\[
k=\left\lfloor\frac{\log p}{\log s}\right\rfloor,
\qquad
\theta=\frac{p-s^{k+1}}{s^k-s^{k+1}},
\]
so that \(s^{k+1}\le p\le s^k\), and set
\[
M_+=\theta k s^k+(1-\theta)(k+1)s^{k+1}.
\]
Then the exact attainable range is
\[
M\in(p,M_+].
\]
Therefore the exact variance range is
\[
\operatorname{Var}(T)\in
\left[
\frac{(1-p)(1+ps)-2qM_+}{p^2q^2},
\frac{(1-p)(1+ps)-2qp}{p^2q^2}
\right).
\]
The minimum variance is attained by
\[
\Pr(T_0=k)=\theta,\qquad
\Pr(T_0=k+1)=1-\theta.
\]
The variance supremum is not attained when \(p<s\), but it is approached by two-point laws supported on \(\{1,N\}\) with \(N\to\infty\). At the boundary \(p=s\), necessarily \(T_0=1\) almost surely and
\[
\operatorname{Var}(T)=\frac{q}{s^2}.
\]

## Assumptions and scope
The base completion time \(T_0\) takes values in \(\{1,2,\ldots\}\). Catastrophe occurs independently at each step with fixed probability \(q\in(0,1)\), and a catastrophe restarts the task from its initial state. The statement fixes both \(q\) and the one-attempt success probability \(p=g(s)\), where \(s=1-q\). No moment assumption on \(T_0\) beyond being positive-integer-valued is needed, because \(T_0s^{T_0}\) is bounded.

The finding is a finite-\(p\) extremal classification. It does not optimize the catastrophe rate \(q\), and it does not claim stochastic ordering of the full restarted-completion distribution.

## Proof
Write
\[
X=s^{T_0}\in\{s,s^2,s^3,\ldots\}.
\]
Then
\[
\mathbb E[X]=p,\qquad
M=\mathbb E[T_0s^{T_0}].
\]
On \(x\in(0,s]\), define
\[
\phi(x)=\frac{x\log x}{\log s}.
\]
Because \(\log s<0\),
\[
\phi''(x)=\frac{1}{x\log s}<0,
\]
so \(\phi\) is strictly concave, and at every lattice point \(x=s^t\),
\[
\phi(s^t)=t s^t.
\]

Let \(L\) be the piecewise-linear interpolant joining the consecutive points
\[
\bigl(s^t,t s^t\bigr),\qquad t=1,2,\ldots,
\]
together with the limiting point \((0,0)\). Since these points lie on the strictly concave graph of \(\phi\), \(L\) is concave. Moreover,
\[
L(X)=\phi(X)=T_0s^{T_0}
\]
almost surely. Jensen's inequality for the concave function \(L\) gives
\[
M=\mathbb E[L(X)]\le L(\mathbb E[X])=L(p).
\]
When \(s^{k+1}\le p\le s^k\), the value \(L(p)\) is precisely
\[
M_+=\theta k s^k+(1-\theta)(k+1)s^{k+1},
\]
with
\[
\theta=\frac{p-s^{k+1}}{s^k-s^{k+1}}.
\]
Equality in Jensen is possible exactly when \(X\) is supported in the single affine segment containing \(p\). Hence the maximizing law is the adjacent two-point law on \(\{k,k+1\}\), degenerating to the deterministic law when \(p\) is a lattice point.

For the lower bound, \(T_0\ge1\) gives pointwise
\[
T_0s^{T_0}\ge s^{T_0},
\]
and therefore
\[
M\ge p.
\]
Equality would require \(T_0=1\) almost surely, which forces \(p=s\). Thus \(M>p\) whenever \(p<s\).

To see sharpness of the lower endpoint, choose \(N\) with \(s^N<p\) and let
\[
a_N=\frac{p-s^N}{s-s^N}.
\]
The law
\[
\Pr(T_0=1)=a_N,\qquad
\Pr(T_0=N)=1-a_N
\]
satisfies \(\mathbb E[s^{T_0}]=p\), while
\[
M_N=a_Ns+(1-a_N)Ns^N\longrightarrow p
\]
because \(Ns^N\to0\). Convex mixtures of two laws having the same value of \(p\) preserve that value of \(p\), so every \(M\in(p,M_+]\) is attainable.

Finally, substituting the exact range of \(M=s g'(s)\) into the published variance identity
\[
\operatorname{Var}(T)=
\frac{(1-p)(1+ps)-2qM}{p^2q^2}
\]
reverses the endpoints because the right-hand side is strictly decreasing in \(M\). This proves the stated variance interval and its extremizers.

## Verification
The proof is analytic. The only optimization step is the one-dimensional convex-hull problem above. Its upper boundary is the concave polygonal interpolation through the lattice points \(\bigl(s^t,t s^t\bigr)\), while the lower boundary is the unattained line \(M=p\) for \(p<s\).

As numerical stress checks, several values of \(s\) and \(p\) were evaluated against the explicit adjacent-support formula; in every case \(M_+\ge p\), and substitution into the variance identity produced nonnegative ordered endpoints. These finite checks are supplementary and are not used as proof.

## Relationship to prior work
Wang and Lu derive the memoryless-catastrophe mean and the exact variance formula in terms of \(p=g(s)\) and \(g'(s)\). They also use the concavity of \(-x\log x\) to obtain an asymptotic upper estimate needed for their exponential-approximation theory. Their paper does not give the exact feasible interval of \(s g'(s)\) at fixed \(g(s)=p\), nor the resulting sharp finite-\(p\) variance extremizers.

Lauber Bonomo and Pal give a general discrete-restart renewal formula and an explicit second moment for geometric restart. Their framework likewise does not classify the base laws that minimize or maximize restarted variance under a fixed one-attempt success probability.

The present result keeps the mean-determining scalar \(p\) fixed and solves the remaining discrete moment problem exactly. The lattice constraint is essential for the sharp upper envelope: continuous Jensen gives only the curved bound \(\phi(p)\), whereas the true maximum is the lower polygonal value \(L(p)\).

## Limitations
The upper variance endpoint is a supremum, not a maximum, when \(p<s\). The result does not compare higher moments, quantiles, or full distributions. It also does not treat non-memoryless catastrophe mechanisms or non-integer base completion times.

A residual literature risk remains that an equivalent two-moment convex-hull classification may have appeared under different restart notation. Focused searches and inspection of the closest general discrete-restart paper did not locate such a statement.

## References
S. Wang and Z. Lu, *On Completion Times under Memoryless Catastrophe*, arXiv:2609.16566v1, 2026.

O. Lauber Bonomo and A. Pal, *First passage under restart for discrete space and time: application to one dimensional confined lattice random walks*, arXiv:2102.00895v1, 2021.

S. Reuveni, *Optimal Stochastic Restart Renders Fluctuations in First Passage Times Universal*, Physical Review Letters 116, 170601, 2016.
