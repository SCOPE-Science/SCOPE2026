# Exact generating function and integer-momentum resonance for scalar Schedule-Free SGD
## Finding

Consider the equal-weight Schedule-Free SGD recursion on the deterministic scalar quadratic
\[
f(u)=\frac{a}{2}u^2,\qquad a>0,
\]
with
\[
y_t=(1-\beta)z_t+\beta x_t,
\]
\[
z_{t+1}=z_t-\gamma a y_t,
\]
\[
x_{t+1}=\frac{t}{t+1}x_t+\frac{1}{t+1}z_{t+1},
\qquad x_1=z_1\ne0,
\]
where
\[
\gamma>0,\qquad \beta\in[0,1).
\]
Set
\[
s=\gamma a,\qquad A=1-s(1-\beta).
\]

For \(\beta>0\), define
\[
r=\frac{\beta}{1-\beta}
\]
and the ordinary generating function
\[
G(q)=\sum_{t\ge1}x_tq^t.
\]
Then the exact generating function is
\[
G(q)=\frac{x_1}{s\beta}
\left[
1-
\left(\frac{1-q}{1-Aq}\right)^r
\right].
\]

For \(\beta=0\), the exact evaluation sequence is instead
\[
x_t=\frac{x_1\left[1-(1-s)^t\right]}{st}.
\]

The complete state converges to the minimizer,
\[
(x_t,z_t,y_t)\longrightarrow(0,0,0),
\]
if and only if
\[
0<s<\frac{2}{1-\beta}.
\]
Thus the scalar constant-step stability ceiling is enlarged from \(s<2\) at \(\beta=0\) to
\[
s<\frac{2}{1-\beta}.
\]
For example, the exact value \(\beta=0.9\) gives the ceiling \(s<20\).

Inside the stable region there is a sharp arithmetic rate dichotomy. If
\[
r\notin\mathbb N,
\]
then
\[
x_t\sim
-\frac{x_1}{s\beta}\,
\frac{[s(1-\beta)]^{-r}}{\Gamma(-r)}
\,t^{-r-1}.
\]
Because
\[
r+1=\frac{1}{1-\beta},
\]
the evaluation sequence has the polynomial rate
\[
x_t=\Theta\!\left(t^{-1/(1-\beta)}\right)
\]
for every noninteger \(r\).

If instead
\[
r=m\in\mathbb N,
\qquad
\beta=\frac{m}{m+1},
\]
the generating function is rational. When \(A\ne0\),
\[
|x_t|=\Theta\!\left(t^{m-1}|A|^t\right).
\]
Hence these exact momentum values convert the generic polynomial tail into geometric decay up to a polynomial factor.

There is a stronger finite-termination resonance at
\[
s=m+1=\frac{1}{1-\beta},
\]
for which \(A=0\). In exact arithmetic,
\[
x_t=\frac{x_1}{m}(-1)^{t+1}\binom mt,
\qquad 1\le t\le m,
\]
and
\[
x_t=0,\qquad t>m.
\]
The base and gradient-location sequences also become exactly zero one step later:
\[
z_t=y_t=0,\qquad t\ge m+2.
\]

For the exact rational value
\[
\beta=\frac9{10},
\]
the resonance is \(m=9\), and choosing
\[
s=10
\]
makes the evaluation sequence vanish from \(t=10\) onward and the complete state vanish from \(t=11\) onward.

## Assumptions and scope

The result concerns the basic equal-weight Schedule-Free SGD recursion with a deterministic exact gradient, a one-dimensional positive quadratic, a constant learning rate, and initialization \(x_1=z_1\). The interpolation parameter satisfies \(\beta\in[0,1)\).

The integer-resonance statements are exact-arithmetic statements about exact rational parameter identities. Floating-point representation, stochastic gradients, learning-rate warmup, nonconstant averaging weights, optimizer-specific preconditioning, and implementation details can destroy exact cancellation.

The theorem classifies full-state convergence, not merely convergence of the reported evaluation sequence \(x_t\). This distinction matters on the sharp boundary: for some parameters the average \(x_t\) can tend to zero while the base sequence \(z_t\) does not.

## Proof

Equal weighting gives
\[
t x_t=\sum_{j=1}^t z_j,
\]
so
\[
z_t=t x_t-(t-1)x_{t-1}.
\]
The base update can be written
\[
z_{t+1}=A z_t-s\beta x_t.
\]
Substituting the averaging identity yields, for \(t\ge1\),
\[
(t+1)x_{t+1}
=
\left[(1+A)t-s\beta\right]x_t
-
A(t-1)x_{t-1}.
\]

For \(\beta>0\), multiply this recurrence by \(q^t\), sum over \(t\ge1\), and write
\[
G(q)=\sum_{t\ge1}x_tq^t.
\]
The result is the first-order differential equation
\[
(1-q)(1-Aq)G'(q)+s\beta G(q)=x_1,
\qquad G(0)=0.
\]
Since
\[
1-A=s(1-\beta)
\]
and
\[
r=\frac{\beta}{1-\beta},
\]
an integrating factor is
\[
\left(\frac{1-Aq}{1-q}\right)^r.
\]
Integrating with \(G(0)=0\) gives
\[
G(q)=\frac{x_1}{s\beta}
\left[
1-
\left(\frac{1-q}{1-Aq}\right)^r
\right].
\]

For \(\beta=0\), the base sequence is ordinary scalar gradient descent:
\[
z_t=(1-s)^{t-1}x_1.
\]
Averaging these terms gives
\[
x_t=\frac{x_1[1-(1-s)^t]}{st}.
\]

Now suppose \(\beta>0\). Because \(s>0\),
\[
A<1.
\]
If
\[
|A|<1,
\]
the factor \((1-Aq)^{-r}\) is analytic on a disk strictly larger than the unit disk. The only unit-modulus singularity controlling the noninteger case is therefore the branch point at \(q=1\). Standard coefficient extraction gives
\[
[q^t](1-q)^r
\sim
\frac{t^{-r-1}}{\Gamma(-r)}.
\]
Evaluating the analytic factor at \(q=1\) gives
\[
(1-A)^{-r}=[s(1-\beta)]^{-r},
\]
and therefore
\[
x_t\sim
-\frac{x_1}{s\beta}
\frac{[s(1-\beta)]^{-r}}{\Gamma(-r)}
t^{-r-1}.
\]
The same averaging identity shows \(z_t\to0\), and then \(y_t\to0\).

If \(r=m\in\mathbb N\), the branch disappears and
\[
\left(\frac{1-q}{1-Aq}\right)^m
\]
is rational. For \(A\ne0\), its pole at \(q=1/A\) has order \(m\), giving
\[
|x_t|=\Theta(t^{m-1}|A|^t).
\]
If \(A=0\), then
\[
G(q)=\frac{x_1}{m}\left[1-(1-q)^m\right],
\]
because \(s\beta=m\). This is a polynomial of degree \(m\), and its coefficients are exactly
\[
x_t=\frac{x_1}{m}(-1)^{t+1}\binom mt
\]
for \(1\le t\le m\), followed by zeros. Since
\[
z_{t+1}=-m x_t
\]
when \(A=0\), the base state vanishes from \(t=m+2\) onward as well.

The condition
\[
|A|<1
\]
is equivalent to
\[
0<s<\frac{2}{1-\beta}.
\]
This proves sufficiency for full-state convergence. If \(A<-1\), the singularity \(q=1/A\) lies strictly inside the unit disk and produces geometric growth, so convergence fails. At the boundary \(A=-1\), the singularity at \(q=-1\) prevents full-state convergence. For \(\beta=0\), \(z_t=(-1)^{t-1}x_1\). For \(\beta>0\), the coefficient contribution from \(q=-1\) makes the alternating base sequence nonvanishing or growing; when \(0<r<1\), \(x_t\) itself may still tend to zero, but
\[
z_t=t x_t-(t-1)x_{t-1}
\]
has alternating magnitude of order \(t^r\). Hence the full-state boundary is strict.

## Verification

The accompanying `verify.py` reconstructs the source-indexed Schedule-Free SGD recursion. It checks the exact recurrence and generating-function coefficients, verifies the noninteger asymptotic constant numerically, tests the sharp stability frontier, checks the boundary case where the evaluation average hides a growing base sequence, and verifies exact finite termination at integer resonance using rational arithmetic.

The numerical asymptotic and boundary checks are not substitutes for the proof. The generating function, coefficient extraction, and exact recurrence establish the infinite-time statements.

## Relationship to prior work

Defazio et al. introduced Schedule-Free SGD with the three sequences \(x_t,y_t,z_t\), equal averaging, constant base learning rate, and interpolation parameter \(\beta\). Their quadratic experiment shows empirically that choosing \(\beta<1\) can permit much larger learning rates, and they state that the general conditions permitting large learning rates are not fully understood in stochastic settings. The inspected paper does not give the scalar generating function, the exact boundary \(2/(1-\beta)\), or the integer-resonance classification above.

Ahn, Magakyan, and Cutkosky later proved optimal nonconvex guarantees for Schedule-Free SGD and gave additional parameter-choice guidance. The inspected algorithm and main theoretical discussion address complexity and nonconvex stationarity rather than the exact constant-step scalar recurrence.

Earlier averaging theory for SGD explains why averaging can obtain optimal stochastic quadratic rates, but it does not by itself imply the \(\beta\)-dependent generating function of Schedule-Free interpolation. Focused searches over schedule-free quadratic stability, generating functions, exact learning-rate ceilings, finite termination, and momentum resonance did not identify the present statement. A residual risk remains that an equivalent recurrence analysis exists under primal-averaging or orthogonal-polynomial terminology.

## Limitations

The theorem is one-dimensional and deterministic. It does not cover stochastic gradient noise, matrix-valued quadratics with interacting spectral modes, nonquadratic objectives, time-varying learning rates, warmup, weighted averaging, or practical Schedule-Free AdamW states.

The exact integer resonance is fragile: perturbing \(\beta\) away from \(m/(m+1)\) restores a polynomial asymptotic tail, while perturbing the exact step \(s=m+1\) yields geometric decay only when the integer relation remains exact.

The finite-termination formula can contain large intermediate binomial coefficients, so exact annihilation does not imply a small transient.

The originality comparison is targeted rather than exhaustive across all historical primal-averaging recurrence literature.

## References

1. Aaron Defazio, Xingyu Alice Yang, Harsh Mehta, Konstantin Mishchenko, Ahmed Khaled, and Ashok Cutkosky, “The Road Less Scheduled,” arXiv:2405.15682v1, 2024.
2. Kwangjun Ahn, Gagik Magakyan, and Ashok Cutkosky, “General framework for online-to-nonconvex conversion: Schedule-free SGD is also effective for nonconvex optimization,” arXiv:2411.07061v1, 2024.
