# Underrelaxed randomized Douglas–Rachford gains mean-square acceleration from momentum
## Finding

The momentum randomized two-set Douglas–Rachford scheme of Han, Su, and Xie is known to accelerate certain bounds for the **norm of the expected iterate**. Its published upper bound for the **expected squared error**, by contrast, worsens whenever momentum is added. The distinction between this upper bound and actual mean-square dynamics matters.

For the consistent linear system
\[
Ax=b,\qquad A=I_2,\quad b=0,
\]
consider Algorithm 2 with two independent uniformly chosen rows per outer step, a relaxation parameter
\[
0<\alpha<1,
\]
and constant nonnegative heavy-ball coefficient
\[
\beta\ge0.
\]
Use the source initialization
\[
x^1=x^0\ne0.
\]

Set
\[
\mu=1-\alpha,\qquad s=1-2\alpha+2\alpha^2.
\]
The exact second-moment transition matrix is
\[
\boxed{
M_{\alpha,\beta}=
\begin{pmatrix}
s+2\mu\beta+\beta^2&-2\beta(\mu+\beta)&\beta^2\\
\mu+\beta&-\beta&0\\
1&0&0
\end{pmatrix}.
}
\]
In particular, the actual zero-momentum expected squared error contracts by the exact factor
\[
\boxed{s=1-2\alpha+2\alpha^2}
\]
per outer step.

For all sufficiently small
\[
\beta\ge0,
\]
the spectral radius of the moment transition is a simple positive real eigenvalue. Its derivative at zero is
\[
\boxed{
\left.\frac{d\rho(M_{\alpha,\beta})}{d\beta}\right|_{\beta=0^+}
=
\frac{2\alpha(1-\alpha)(2\alpha-1)}{1-2\alpha+2\alpha^2}.
}
\]
Thus **every underrelaxation**
\[
0<\alpha<\frac12
\]
admits a positive momentum interval on which the **actual mean-square asymptotic contraction factor is strictly smaller** than its zero-momentum value. Conversely, for
\[
\frac12<\alpha<1,
\]
all sufficiently small positive momentum strictly worsens that factor. At the dividing value,
\[
\boxed{
\rho(M_{1/2,\beta})=\frac12+\beta^2+O(\beta^3),
}
\]
so momentum also fails to improve the rate for sufficiently small positive values there.

There is a completely rational, nonperturbative witness. Take
\[
\boxed{\alpha=\frac14,\qquad\beta=\frac1{10}.}
\]
Then
\[
M_{1/4,1/10}=
\begin{pmatrix}
157/200&-17/100&1/100\\
17/20&-1/10&0\\
1&0&0
\end{pmatrix}
\]
and its characteristic polynomial is
\[
\boxed{1000z^3-685z^2+56z-1.}
\]
The polynomial has one root in each of the disjoint rational intervals
\[
\left(\frac1{50},\frac3{100}\right),\qquad
\left(\frac3{50},\frac7{100}\right),\qquad
\left(\frac{59}{100},\frac35\right).
\]
These three intervals exhaust its roots, so its spectral radius satisfies
\[
\boxed{
\frac{59}{100}<\rho(M_{1/4,1/10})<\frac35<\frac58=s.
}
\]
Numerically,
\[
\rho(M_{1/4,1/10})=0.593480527629\ldots,
\]
compared with the exact no-momentum rate
\[
s=\frac58=0.625.
\]
The actual asymptotic mean-square factor therefore improves, with the same two row reflections per outer step.

Importantly, this witness lies **inside the sufficient mean-square stability regime** of the defining paper's Theorem 4.1. That theorem's constants become
\[
\gamma_1=\frac{87}{100},\qquad
\gamma_2=\frac{19}{200},\qquad
\gamma_1+\gamma_2=\frac{193}{200}<1.
\]
The source upper-bound rate nevertheless gives
\[
q=\frac{\gamma_1+\sqrt{\gamma_1^2+4\gamma_2}}2
=0.9681275644\ldots>
\frac58.
\]
The source bound remains mathematically valid; it simply does not detect the actual acceleration.

## Assumptions and scope

The method is the fixed-parameter mRrDR algorithm of Han, Su, and Xie, not its later adaptive-momentum replacement. Each of the two row reflections is sampled **independently with replacement**. This is important: sampling without replacement would remove the identity-reflection event on this particular two-row system.

The coefficient matrix is
\[
I_2,
\]
the linear system is consistent and homogeneous, and every nonzero source initialization
\[
x^1=x^0
\]
is allowed. The correct solution is the origin.

The main theorem is local in momentum, but uniform over each fixed
\[
\alpha\in(0,1/2)
\]
or
\[
\alpha\in(1/2,1).
\]
The positive-momentum witness is nonperturbative.

The compared quantity is
\[
\mathbb E\|x^k\|_2^2,
\]
not
\[
\|\mathbb E x^k\|_2^2.
\]
Asymptotic rate means the exponential contraction factor of the exact finite-dimensional second-moment recursion; for the small-momentum regime and the rational witness the dominant mode is excited by nonzero equal initial states.

No claim is made that momentum accelerates every row geometry, every relaxation, every initialization of unrelated algorithms, or the optimal row-action-normalized performance over all methods.

## Proof

For
\[
A=I_2,
\]
the two homogeneous row reflections are
\[
R_1=\operatorname{diag}(-1,1),
\qquad
R_2=\operatorname{diag}(1,-1).
\]
Two independent uniform row draws give
\[
R_{i_2}R_{i_1}=
\begin{cases}
I_2,&i_1=i_2,\\
-I_2,&i_1\ne i_2,
\end{cases}
\]
with probability one half in each case. Inserting these into Algorithm 2 yields
\[
x^{k+1}
=(c_k+\beta)x^k-\beta x^{k-1},
\]
where the independent scalar variables satisfy
\[
\mathbb P(c_k=1)=\mathbb P(c_k=1-2\alpha)=\frac12.
\]
Their first two moments are exactly
\[
\mathbb E c_k=\mu=1-\alpha,
\qquad
\mathbb E c_k^2=s=1-2\alpha+2\alpha^2.
\]

Introduce
\[
U_k=\mathbb E\|x^k\|_2^2,
\qquad
V_k=\mathbb E\langle x^k,x^{k-1}\rangle,
\qquad
W_k=\mathbb E\|x^{k-1}\|_2^2.
\]
Independence of the fresh row samples from the previous iterates gives
\[
\begin{aligned}
U_{k+1}
&=(s+2\mu\beta+\beta^2)U_k
-2\beta(\mu+\beta)V_k
+\beta^2W_k,\\
V_{k+1}
&=(\mu+\beta)U_k-\beta V_k,\\
W_{k+1}&=U_k.
\end{aligned}
\]
This proves the displayed exact moment matrix. At zero momentum,
\[
U_{k+1}=sU_k,
\]
which proves the baseline rate.

At
\[
\beta=0,
\]
this matrix has eigenvalues
\[
s,0,0.
\]
Since
\[
s>0,
\]
the dominant eigenvalue is simple and isolated. A right eigenvector and left eigenvector, normalized to have inner product one, are
\[
r_0=(1,\mu/s,1/s)^\top,
\qquad
\ell_0=(1,0,0)^\top.
\]
Differentiating the matrix at zero gives the first row
\[
(2\mu,-2\mu,0)
\]
and second row
\[
(1,-1,0).
\]
The standard simple-eigenvalue perturbation identity therefore yields
\[
\begin{aligned}
\lambda'(0)
&=\ell_0^\top M'_{\alpha,0}r_0\\
&=2\mu-\frac{2\mu^2}s\\
&=\frac{2\alpha(1-\alpha)(2\alpha-1)}s.
\end{aligned}
\]
All other eigenvalues tend to zero with
\[
\beta\to0,
\]
so this analytic eigenvalue remains the spectral radius for sufficiently small momentum. Its coefficient in the second-moment trajectory is nonzero for
\[
x^1=x^0\ne0,
\]
because at zero momentum the initial left-eigenvector projection equals
\[
U_1=\|x^0\|_2^2>0
\]
and this projection varies continuously with the momentum coefficient. This proves the strict acceleration and deceleration statements.

At the critical relaxation
\[
\alpha=\frac12,
\]
the characteristic polynomial becomes
\[
P(z,\beta)
=z^3-\left(\frac12+\beta^2\right)z^2
+\beta^3z-\beta^3.
\]
Inserting the simple-root expansion
\[
z=\frac12+c\beta^2+O(\beta^3)
\]
forces
\[
c=1.
\]
Therefore the second-order correction is positive.

For the rational witness, direct substitution into the moment matrix gives
\[
P(z)=\frac1{1000}(1000z^3-685z^2+56z-1).
\]
The integer polynomial changes sign across each of the three disjoint rational intervals stated in the finding. As a cubic it has exactly one real root in each interval; all are positive and below
\[
\frac35.
\]
The largest is the dominant rate and satisfies
\[
\frac35<\frac58.
\]
Finally, substituting
\[
\sigma_{\min}^2(I_2)=1,
\qquad
\|I_2\|_F^2=2,
\qquad
r=2
\]
into the published Theorem 4.1 formulas makes its normalized expected-reflection eigenvalue zero. The displayed rational values of
\[
\gamma_1,\gamma_2
\]
then follow directly. Their sum is strictly below one, while the certified upper bound remains much larger than the actual contraction factor.

## Verification

The accompanying `verify.py` is a standard-library-only checker. It reconstructs the two reflections and their four equally likely ordered pairs, verifies the exact rational moment recurrence by exhaustive enumeration through several outer steps, checks the rational characteristic polynomial, and isolates all three roots by exact rational sign changes.

It also computes the source Theorem 4.1 constants directly, checks its sufficient condition and pessimistic rate, and confirms the critical-relaxation expansion algebraically.

The finite enumeration does not prove the infinite-step result: that result follows from the exact conditional-moment recurrence and simple-eigenvalue perturbation theory.

## Relationship to prior work

Han, Su, and Xie introduce randomized multi-set Douglas–Rachford for consistent linear systems. Their Theorem 3.1 bounds expected squared error, and their Algorithm 2 adds heavy-ball momentum. In Theorem 4.1 they establish another expected-squared-error upper bound and observe that this **certified bound** worsens with momentum. Theorem 4.2 separately establishes accelerated convergence for the **norm of the expected error**. Those results and the distinction between the two notions of convergence are prior.

The new point is that, already on the smallest full-rank orthonormal system with two reflections, the **actual expected-squared-error rate** can strictly improve under positive momentum despite the bound's opposite comparison. The exact three-state recurrence quantifies why, gives a sharp small-momentum transition at
\[
\alpha=\frac12,
\]
and supplies a rational parameter witness that satisfies the original theorem's sufficient hypotheses.

The later first-party continuation by Guo, Xiang, Han, and Xie improves sampling probabilities and introduces adaptive momentum. Its without-replacement rule changes the distribution of the two-reflection product, so it does not imply the result for the earlier independently sampled fixed-momentum scheme.

Bollapragada, Chen, and Ward prove acceleration of minibatch stochastic heavy-ball optimization on quadratics under sufficient batch-size conditions. That broader guarantee does not evaluate this exact two-reflection with-replacement second-moment operator or the sharp relaxation transition. Han and Xie's pseudoinverse-free framework analyzes a wider family of randomized solvers and mean-iterate acceleration, but likewise does not supply the displayed three-state equality and rational witness in the inspected material.

Focused searches for two-reflection randomized Douglas–Rachford, mRrDR, heavy-ball mean-square acceleration, orthogonal rows, and Bernoulli identity-versus-contraction maps did not identify an implication-equivalent published analysis.

## Limitations

The instance is two-dimensional, exactly orthonormal, and uses independent with-replacement sampling. This is an exact benchmark, not a universal speedup guarantee.

The phase transition is local in the momentum coefficient; larger positive momentum may eventually slow or destabilize the iteration.

The improvement concerns actual mean-square contraction per outer step, not the best runtime or row-action complexity among all solvers. Both compared runs use two reflections per outer step.

The paper's published upper bound remains valid; the finding shows its non-tightness for this family and metric, not a counterexample to its theorem.

## References

1. Deren Han, Yansheng Su, and Jiaxin Xie, “Randomized Douglas–Rachford methods for linear systems: Improved accuracy and efficiency,” arXiv:2207.04291v1, first submitted 2022-07-09; the full Algorithm 2 and Theorems 4.1–4.2 were inspected in arXiv:2207.04291v4.
2. Liqi Guo, Ruike Xiang, Deren Han, and Jiaxin Xie, “Enhanced randomized Douglas–Rachford method: Improved probabilities and adaptive momentum,” arXiv:2506.10261v1, 2025-06-12.
3. Raghu Bollapragada, Tyler Chen, and Rachel Ward, “On the fast convergence of minibatch heavy ball momentum,” arXiv:2206.07553v5, 2025-06-22 revision of a manuscript first submitted 2022-06-15.
4. Deren Han and Jiaxin Xie, “On pseudoinverse-free randomized methods for linear systems: Unified framework and acceleration,” arXiv:2208.05437v3, 2022-08-24.
