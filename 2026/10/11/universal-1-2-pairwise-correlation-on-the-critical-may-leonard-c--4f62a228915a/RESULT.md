# Universal \(-1/2\) pairwise correlation on the critical May–Leonard cycle family
## Finding
Consider the classical May–Leonard competitive flow
\[
\dot x=x(1-x-\alpha y-\beta z),\qquad
\dot y=y(1-\beta x-y-\alpha z),\qquad
\dot z=z(1-\alpha x-\beta y-z).
\]
Assume \(\alpha,\beta>0\), \(\alpha+\beta=2\), and \(\alpha\ne1\). If \(\mu\) is an invariant Borel probability measure whose support is a compact subset of \((0,\infty)^3\), then \(\mu\) is supported on the simplex \(x+y+z=1\) and
\[
\mathbb E_\mu[y\mid x]=\mathbb E_\mu[z\mid x]=\frac{1-x}2,
\]
\[
\mathbb E_\mu[z\mid y]=\mathbb E_\mu[x\mid y]=\frac{1-y}2,
\qquad
\mathbb E_\mu[x\mid z]=\mathbb E_\mu[y\mid z]=\frac{1-z}2.
\]
It follows that
\[
\mathbb E_\mu[x]=\mathbb E_\mu[y]=\mathbb E_\mu[z]=\frac13.
\]
The three coordinate variances are equal. Writing their common value as \(\sigma^2\),
\[
\operatorname{Cov}_\mu(x,y)=\operatorname{Cov}_\mu(y,z)=\operatorname{Cov}_\mu(z,x)=-\frac{\sigma^2}2.
\]
Therefore every non-Dirac measure in this class has
\[
\operatorname{Corr}_\mu(x,y)=\operatorname{Corr}_\mu(y,z)=\operatorname{Corr}_\mu(z,x)=-\frac12.
\]
The case \(\sigma^2=0\) is exactly \(\delta_{(1/3,1/3,1/3)}\).

## Assumptions and scope
The result concerns the deterministic three-species May–Leonard ordinary differential equation above, on the critical integrable line \(\alpha+\beta=2\) with \(\alpha\ne1\). The invariant probability measure must have compact support strictly inside the positive octant. This includes invariant probability measures on the interior periodic orbits of the critical family and arbitrary invariant mixtures supported on compact interior invariant sets. Boundary measures, heteroclinic boundary dynamics, demographic noise, diffusion, spatial extensions, and the degenerate symmetric case \(\alpha=\beta=1\) are outside the claim.

## Proof
Let \(u=x+y+z\). On \(\alpha+\beta=2\), direct summation gives
\[
\dot u=u-u^2=u(1-u).
\]
Because the support of \(\mu\) is compact in \((0,\infty)^3\), \(u\) is bounded away from zero there. Invariance applied to \(\log u\) gives
\[
0=\int \frac{\dot u}u\,d\mu=1-\mathbb E_\mu[u],
\]
while invariance applied to \(u\) gives
\[
0=\int \dot u\,d\mu=\mathbb E_\mu[u]-\mathbb E_\mu[u^2].
\]
Hence \(\mathbb E_\mu[u]=\mathbb E_\mu[u^2]=1\), so \(\operatorname{Var}_\mu(u)=0\) and therefore \(u=1\) \(\mu\)-almost surely.

Next, for every continuously differentiable function \(\Phi\) of one variable, invariance gives
\[
0=\int \Phi'(x)x(1-x-\alpha y-\beta z)\,d\mu.
\]
On the compact support, \(x\) is bounded away from zero. Since \(\Phi'\) can be any continuous test function on the projected support, this implies
\[
\mathbb E_\mu[1-x-\alpha y-\beta z\mid x]=0.
\]
Using \(x+y+z=1\) and \(\beta=2-\alpha\),
\[
1-x-\alpha y-\beta z=(\alpha-1)(z-y).
\]
Because \(\alpha\ne1\),
\[
\mathbb E_\mu[z-y\mid x]=0.
\]
Together with \(y+z=1-x\), this yields
\[
\mathbb E_\mu[y\mid x]=\mathbb E_\mu[z\mid x]=\frac{1-x}2.
\]
The two other conditional identities follow by cyclic permutation.

Integrating any conditional identity gives the common mean \(1/3\). Let
\[
q_x=\mathbb E_\mu[x^2],\qquad q_y=\mathbb E_\mu[y^2],\qquad q_z=\mathbb E_\mu[z^2].
\]
Then
\[
\mathbb E_\mu[xy]=\mathbb E_\mu\!\left[x\,\mathbb E_\mu[y\mid x]\right]=\frac12\left(\frac13-q_x\right),
\]
and also, using the cyclic conditional identity conditioning on \(y\),
\[
\mathbb E_\mu[xy]=\frac12\left(\frac13-q_y\right).
\]
Thus \(q_x=q_y\); cycling gives \(q_x=q_y=q_z=:q\). Therefore the common variance is \(\sigma^2=q-1/9\), and
\[
\operatorname{Cov}_\mu(x,y)
=\frac12\left(\frac13-q\right)-\frac19
=-\frac12\left(q-\frac19\right)
=-\frac{\sigma^2}2.
\]
The other covariance identities are cyclic copies. If \(\sigma^2>0\), division by the common variance gives correlation \(-1/2\). If \(\sigma^2=0\), all three coordinates are almost surely equal to their mean \(1/3\), so \(\mu=\delta_{(1/3,1/3,1/3)}\).

## Verification
The proof uses only the generator identity for compactly supported invariant measures, the exact critical-line scalar equation for \(u\), conditional expectation, and elementary second-moment algebra. The bundled checker independently verifies the two critical algebraic reductions: the factorization of the first per-capita growth rate on \(x+y+z=1\), and the covariance simplification. It returns `ALGEBRA_OK`.

No finite numerical experiment is used as a substitute for the invariant-measure argument. No claim is made for boundary-supported measures or for \(\alpha=1\).

## Relationship to prior work
May and Leonard introduced the three-species competition model and its special periodic behavior in 1975. Leach and Miritzis analyze the same normalized system and derive the critical reduction \(\dot u=u-u^2\) when \(\alpha+\beta=2\). Blé, Castellanos, Llibre, and Quilantán identify complete integrability on this critical line and the periodic-orbit geometry on \(x+y+z=1\). Later work on stochastic May–Leonard dynamics also treats the deterministic critical periodic family as the baseline.

The closest same-model literature establishes the integrable critical-line geometry and the periodic family on \(x+y+z=1\). The conditional equal-sharing identity is a different statement: it is a stationary, coordinate-conditioned consequence of the generator equations, and the covariance law follows from its second-moment implications. The inspected same-model sources discuss integrability, periodic geometry, and stochastic extinction mechanisms rather than this conditional-moment identity.

## Limitations
The theorem is restricted to compactly supported invariant probability measures strictly inside \((0,\infty)^3\), to \(\alpha+\beta=2\), and to \(\alpha\ne1\). It does not classify all invariant measures, prove existence of a particular periodic orbit, or extend the correlation law to noisy, spatial, delayed, or boundary dynamics. 
## References
1. R. M. May and W. J. Leonard, “Nonlinear Aspects of Competition Between Three Species,” *SIAM Journal on Applied Mathematics* 29 (1975), 243–253. DOI: 10.1137/0129022. Earliest verified public date used here: 1975-09-01 (OpenAlex W2043691077).
2. P. G. L. Leach and J. Miritzis, “Analytic Behaviour of Competition among Three Species,” *Journal of Nonlinear Mathematical Physics* 13 (2006), 535–548. DOI: 10.2991/jnmp.2006.13.4.8.
3. G. Blé, V. Castellanos, J. Llibre, and I. Quilantán, “Integrability and global dynamics of the May-Leonard model,” *Nonlinear Analysis: Real World Applications* 14 (2013). DOI: 10.1016/j.nonrwa.2012.06.004.
4. “Heteroclinic cycling and extinction in May–Leonard models with demographic stochasticity,” *Journal of Mathematical Biology* (2023). DOI: 10.1007/s00285-022-01859-4.
