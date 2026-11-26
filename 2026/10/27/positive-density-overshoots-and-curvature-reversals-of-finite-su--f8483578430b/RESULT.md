# Sharp block lengths for overshoots and curvature reversals of finite-support renewal masses

## Finding

Let the iid interarrival times have positive-integer support \(S\), finite, with \(|S|\ge2\) and \(\gcd(S)=1\). Put \(d=\max S\), \(\mu=\mathbb E X_1\), and let \(u_n\) be the probability of renewal at time \(n\), including \(u_0=1\). Write \(L=1/\mu\), \(e_n=u_n-L\), and \(h_n=u_{n-1}u_{n+1}-u_n^2\) for \(n\ge1\).

**Theorem.** Every block of \(d\) consecutive nonnegative indices contains both strict signs of \(e_n\). Every sufficiently late block of \(d\) consecutive indices contains both strict signs of \(h_n\). More precisely, for a curvature block starting at \(s\ge1\), positivity of \(u_{s-1},\ldots,u_{s+d}\) suffices. Consequently each of the four strict sign sets has lower natural density at least \(1/d\). The common block length and common density bound are sharp for each \(d\ge2\): there is a law of maximum step \(d\) with \(e_n>0\) and \(h_n<0\) each occurring exactly at multiples of \(d\) on their respective index sets.

## Assumptions and scope

Write \(p_j=\Pr(X_1=j)\), with \(p_j=0\) off \(S\); in particular \(p_1\) need not be positive. Renewal at \(n\) means that one of the partial sums of increments, starting with the empty sum, equals \(n\). The lower natural density of \(A\) is \(\liminf_{N\to\infty}N^{-1}|A\cap\{1,\ldots,N\}|\). The starting point for the curvature block guarantee can depend on the law. Sharpness is for the common bound; it does not say that each individual sign set can attain it.

## Proof

### 1. Renewal-limit errors cannot have a one-signed tail

For \(f(z)=\sum_{j=1}^d p_jz^j\), the renewal identity is \(U(z)=\sum_{n\ge0}u_n z^n=(1-f(z))^{-1}\). At \(z=1\) its principal part is \(L/(1-z)\), because \(f'(1)=\mu\). On \(|z|<1\), \(|f(z)|<1\); on \(|z|=1\), \(f(z)=1\) forces every positively weighted \(z^j=1\), hence \(z=1\). On the positive real axis strict monotonicity of \(f\) likewise leaves only \(1\). The rational function \(U(z)-L/(1-z)\) therefore has precisely the other roots of \(1-f\) as poles, with their multiplicities. There is at least one such root since \(d\ge2\).

Let \(R>1\) be the smallest modulus of these other roots, \(m\) the largest pole order on \(|z|=R\), and \(J\) the roots \(z_j\) there with order \(m\). Set \(\rho=R^{-1}\), \(\eta_j=(\rho z_j)^{-1}\) for \(j\in J\). These are distinct unit-modulus numbers not equal to \(1\). Partial fractions give
\[
 e_n=\rho^n n^{m-1}\left(\sum_{j\in J}c_j\eta_j^n+o(1)\right),\qquad c_j\ne0.
\]
In particular \(u_n\to L>0\). The leading sum \(v_n=\sum_j c_j\eta_j^n\) is real by conjugate symmetry. Geometric averaging gives it Cesàro mean zero and mean square \(\sum_j|c_j|^2>0\). If \(e_n\ge0\) eventually, then the negative part of \(v_n\) tends to zero. The mean-zero identity then forces the Cesàro average of \(|v_n|\) to vanish, and boundedness forces the mean square to vanish as well. The same argument for \(-e_n\) rules out an eventually nonpositive error. In particular \(u_n\) is not eventually constant.

### 2. Exact recurrences give both block bounds

The error obeys \(e_n=\sum_{j=1}^d p_j e_{n-j}\) for \(n\ge d\). A block of length \(d\) missing one strict sign would propagate its weak sign to all subsequent terms, contradicting Section 1.

For the curvature, let \(R_i=u_i/u_{i-1}\) where both masses are positive. The difference \(R_{i+1}-R_i=h_i/(u_iu_{i-1})\) has the sign of \(h_i\). In a block starting at \(s\ge1\) all the required masses are positive by hypothesis. Applying the renewal recurrence at \(t=s+d\) and \(t-1\) gives the ratio identity
\[
 R_t=\sum_{j=1}^d \frac{p_j u_{t-j-1}}{u_{t-1}}\,R_{t-j}.
\]
The weights sum to one and the coefficient of \(R_s\) is strictly positive since \(p_d>0\). If the block \(h_s,\ldots,h_{s+d-1}\) lacks either strict sign, then \(R_s,\ldots,R_t\) is monotone. The displayed convex combination forces \(R_s=R_t\): otherwise the positive weight on the first term would make the combination strictly below the last term in the nondecreasing case, or strictly above it in the nonincreasing case. By monotonicity all these ratios equal a single \(x>0\). Substituting the resulting geometric data into \(u_t=\sum_{j=1}^d p_j u_{t-j}\) gives \(f(x^{-1})=1\), hence \(x=1\) by strict increase on the positive axis. Thus the masses are constant over the block; the original recurrence propagates the constant to the entire tail, which is impossible by Section 1.

Since \(u_n\to L>0\), every sufficiently late curvature block satisfies the positivity condition. Counting disjoint blocks proves the four lower density bounds.

### 3. Sharpness

Fix any \(0<r<1\). Choose the truncated geometric law \(p_j=(1-r)r^{j-1}\) for \(1\le j<d\) and \(p_d=r^{d-1}\). All probabilities are positive, and telescoping gives
\[
 1-f(z)=(1-z)(1+rz+\cdots+(rz)^{d-1}),\qquad
 U(z)=\frac{1-rz}{(1-z)(1-(rz)^d)}.
\]
Here \(L=(1-r)/(1-r^d)\). With \(n=md+s\), \(m\ge0\), \(0\le s<d\), coefficient extraction gives
\[
 u_{md+s}=A_m+\mathbf1_{s=0}r^{dm+1},\qquad A_m=L(1-r^{d(m+1)}).
\]
Thus \(e_n<0\) off the multiples of \(d\), and at \(n=md\) it is \(r^{dm}(r-Lr^d)>0\). At each positive multiple \(md\), both neighbors are strictly smaller than \(u_{md}\): they are \(A_{m-1}\) and \(A_m\). At a nonmultiple the value is \(A_m\) and both neighbors have value at least \(A_m\); any neighbor in the next block has value \(A_{m+1}+r^{d(m+1)+1}\). These comparisons apply also to \(d=2\). It follows that \(h_n<0\) exactly at positive multiples of \(d\). Blocks of length \(d-1\) can miss those multiples arbitrarily late, and these sign sets have density exactly \(1/d\), so neither common bound can be improved.

## Relationship to prior work

Bell and Gerhold, *The Positivity Set of a Recurrence Sequence*, arXiv:math/0506398, Theorems 1–2, give existence of natural sign densities for real linear recurrences and positivity when there is no positive dominating characteristic root. Those results already imply the unquantified renewal sign-density assertions: \(e_n\) is a generalized power sum with roots \(z_j^{-1}\) from the nonunit poles; \(h_n\) is also a recurrence because sums, shifts and termwise products of such sums are recurrences. The quadratic part has roots of strictly smaller modulus than the dominant linear curvature terms, whose multipliers are nonzero. The new claim is the bound on gaps in terms of the maximum interarrival itself, uniform in the probabilities as a block **length**, and the sharp density consequence. Arbitrarily small positive sign density for general recurrences is consistent with the renewal-specific dependence on \(d\).

Nikolov and Savov, *Properties and conjectures regarding discrete renewal sequences*, arXiv:2307.00545v1, Proposition 3.1, give nonultimate monotonicity and monotone enclosing sequences for \(0<p_1<1\); their enclosing sequences and convergence also account for the error-block phenomenon in that setting. We do not treat that part alone as the contribution. For curvature the convex recurrence is on successive **ratios** and has time-dependent weights, not the constant-weight recurrence on the masses. Its equality case gives the matching block length and the explicit example realizes sharpness for every maximum step. No unrestricted historical-priority claim is made.

## Verification and limits

Run `python3 verify_sharp_blocks.py` for finite exact arithmetic checks of the extremizing family. This checks an explicit family and does not certify the general sign-block theorem. Eventual ratio monotonicity and eventual log-convexity or log-concavity are ruled out because \(u_n\to L>0\) and the sign of \(h_n\) equals the sign of \(u_{n+1}/u_n-u_n/u_{n-1}\) eventually. The theorem does not give the first curvature block from which the bound holds uniformly, nor the density for each individual law.
