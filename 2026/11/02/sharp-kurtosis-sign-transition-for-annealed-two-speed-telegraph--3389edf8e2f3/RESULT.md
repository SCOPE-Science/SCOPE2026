# Sharp kurtosis-sign transition for annealed two-speed telegraph transport

## Finding
Consider a one-dimensional persistent particle whose direction changes at every Poisson event, with a new positive speed independently redrawn at that same event. When the two possible speeds have equal probabilities, there is a **unique, exactly solvable speed-contrast threshold** at which the long-time fourth cumulant of its displacement changes sign. The leading standardized excess kurtosis additionally has a unique global maximum at a different, explicit contrast.

Let the Poisson reversal rate be \(\lambda>0\), the two possible speed magnitudes be \(c\) and \(cq\) with \(c>0\), \(q\ge1\), and let the velocity process start in its stationary distribution. Define the displacement \(X_t=\int_0^t V_s\,ds\), its second cumulant \(K_2(t)=\mathbb E[X_t^2]\), and its fourth cumulant \(K_4(t)=\mathbb E[X_t^4]-3\mathbb E[X_t^2]^2\). Set

\[
d(q)=3q^2-2q+3,\qquad P(q)=3q^4+28q^3-78q^2+28q+3.
\]

For each fixed \(c,\lambda,q\), as \(t\to\infty\),

\[
K_2(t)=\frac{c^2d(q)}{4\lambda}\,t+O(1),\qquad
K_4(t)=\frac{3c^4P(q)}{16\lambda^3}\,t+O(1),
\]

and the standardized excess kurtosis satisfies

\[
\frac{K_4(t)}{K_2(t)^2}=\frac{H(q)}{\lambda t}+O(t^{-2}),\qquad
H(q)=\frac{3P(q)}{d(q)^2}.
\]

There is precisely one transition contrast \(q_{\mathrm c}>1\):

\[
 u_{\mathrm c}=\frac{8\sqrt7-14}{3},\qquad
 q_{\mathrm c}=\frac{u_{\mathrm c}+\sqrt{u_{\mathrm c}^2-4}}2
 =1.84735597443071\ldots.
\]

For \(1\le q<q_{\mathrm c}\), the excess kurtosis is eventually strictly negative; for \(q>q_{\mathrm c}\), it is eventually strictly positive. At equality the leading term vanishes and the excess kurtosis is \(O(t^{-2})\). Moreover, \(H\) has a unique global maximum on \([1,\infty)\), attained at

\[
q_{\max}=\frac{7+2\sqrt{10}}3=4.44151844011225\ldots,
\qquad H(q_{\max})=\frac73.
\]

The endpoints are \(H(1)=-3\) (constant-speed telegraph motion) and \(\lim_{q\to\infty}H(q)=1\). Thus bounded, independently refreshed speed disorder can reverse the sign of the leading Gaussian-approach correction; the strongest positive correction is attained at a finite, not infinite, speed contrast.

## Assumptions and scope
At the times of an independent rate-\(\lambda\) homogeneous Poisson process, the sign of \(V_t\) is **forced to reverse** and a speed magnitude is drawn afresh, independently of the history, uniformly from \(\{c,cq\}\). Between events \(V_t\) is constant. Initially each sign is equally likely and the speed magnitude has this two-point law, independently. The four velocity labels are therefore stationary (for \(q=1\), repeated labels may coincide physically). No Brownian noise, drift, quenched per-trajectory speed variation, or automatic independent-sign redraw is included. The asserted sign concerns sufficiently large \(t\), not every finite observation time.

## Proof
The velocity chain on \(\{+c,+cq,-c,-cq\}\) is an irreducible finite-state continuous-time Markov chain with every transition to either opposite-sign velocity at rate \(\lambda/2\). Its backward generator \(Q\) has diagonal entries \(-\lambda\), two off-sign entries \(\lambda/2\) per row, and zero remaining entries. The Feynman--Kac matrix for the moment generating function of \(X_t\) is \(Q+k\,\mathrm{diag}(c,cq,-c,-cq)\). Its eigenvalue \(s(k)\) continuing the simple eigenvalue zero of \(Q\) is analytic and even near \(k=0\). All other eigenvalues have negative real parts near zero. Therefore \(\log\mathbb E[e^{kX_t}]=t\,s(k)+O(1)\), with the remainder analytic near zero with locally uniform derivative bounds. Differentiation yields \(K_2(t)=t\,s''(0)+O(1)\) and \(K_4(t)=t\,s^{(4)}(0)+O(1)\).

More generally, write \(\mu_j=\mathbb E[R^j]\) for a redrawn positive speed magnitude \(R\). If \(A_+\) and \(A_-\) are the speed averages of the components of a right eigenvector, then the eigenvalue equations give

\[
 A_+=\lambda A_-\,\mathbb E\frac1{s+\lambda-kR},\qquad
 A_-=\lambda A_+\,\mathbb E\frac1{s+\lambda+kR}.
\]

For the eigenbranch near zero, neither average vanishes, so

\[
1=\lambda^2\,\mathbb E\frac1{s+\lambda-kR}\;
\mathbb E\frac1{s+\lambda+kR}.
\]

Set \(A=2\mu_2-\mu_1^2\) and \(B=2\mu_4-2\mu_1\mu_3+\mu_2^2\). Expanding the two finite-support rational functions around \(k=0\) gives

\[
s(k)=\frac{A}{2\lambda}k^2+
\frac{4B-5A^2}{8\lambda^3}k^4+O(k^6).
\]

For \(R\) uniform on \(\{c,cq\}\), elementary algebra yields

\[
A=\frac{c^2d(q)}4,
\qquad 4B-5A^2=\frac{c^4P(q)}{16}.
\]

Consequently \(s''(0)=c^2d(q)/(4\lambda)\) and \(s^{(4)}(0)=3c^4P(q)/(16\lambda^3)\), proving both cumulant formulas and the standardized expansion. The variance coefficient is strictly positive because \(d(q)>0\).

To classify the zeros of \(P\), divide by \(q^2\) and set \(u=q+q^{-1}\). One gets \(P(q)/q^2=3u^2+28u-84\). For \(q\ge1\), \(u\ge2\) increases strictly away from \(q=1\), and this quadratic has exactly one root above two, \(u_{\mathrm c}\). Its inverse image \(q_{\mathrm c}>1\) is therefore the unique sign change.

Finally, direct differentiation gives

\[
H'(q)=-\frac{96(q-1)(q+1)(3q^2-14q+3)}{d(q)^3}.
\]

For \(q>1\), the sole derivative zero is \(q_{\max}=(7+2\sqrt{10})/3\). The derivative changes from positive to negative there, giving the unique global maximum. Exact substitution gives \(H(q_{\max})=7/3\); direct evaluation at \(q=1\) and the leading polynomial coefficients establish the endpoint values. This completes the proof.

## Verification
Run `python checker.py` with Python, NumPy, SciPy, and SymPy. The checker separately constructs the four-state tilted generator, obtains its characteristic polynomial symbolically, evolves moment ODEs of orders zero through four via a \(20\times20\) block matrix, and compares large-time cumulant slopes with the closed formulas for six choices of speeds and reversal rates. The checks include constant speed, contrasts on both sides of the threshold, the exact optimizing contrast, and a large contrast. This numerical test is not a substitute for the analytic spectral proof.

## Relationship to prior work
Classical Goldstein--Kac transport has deterministic speed, covered here only at \(q=1\). Stadje and Zacks (2004) derive distributions and low moments for processes choosing new random velocities at Poisson times; the available description does not assert **forced alternating signs with freshly redrawn magnitudes**, nor the present sharp fourth-cumulant phase diagram. Sim, Liepe and Stumpf (2015) discuss random **trajectory-level speed variation**, with a non-Gaussian mixture of diffusion profiles, rather than the present refreshing of magnitudes after every reversal. De Bruyne, Majumdar and Schehr (2021) study first-passage survival for randomly selected run velocities (and a constant-speed sign-flip specialization), not the free-displacement fourth cumulant or its sign/maximum thresholds. These are comparisons by model and mathematical implication, not claims to have surveyed all literature.

## Limitations
The theorem is asymptotic at fixed positive parameters and pertains to the alternating-sign, annealed, equal-probability two-speed model. It does not imply any particular sign at early times or a non-Gaussian limiting rescaled law; indeed the rescaled displacement converges to a Gaussian. Broader random velocity distributions can be handled by the displayed cumulant-coefficient identities when suitable bounded-support assumptions hold, but no global phase classification for arbitrary distributions is asserted. Complete text of some especially relevant older papers was inaccessible; historical priority remains provisional. No independent audit has been performed.

## References
- W. Stadje and S. Zacks, “Telegraph Processes with Random Velocities,” *Journal of Applied Probability* **41** (2004), 665–678, doi:10.1239/jap/1091543417.
- A. Kolesnik, “Moment analysis of the telegraph random process,” *Bulletin of the Academy of Sciences of Moldova. Mathematics* (2012), available at https://www.math.md/en/publications/basm/issues/y2012-n1/11070/.
- A. Sim, J. Liepe, and M. P. H. Stumpf, “Goldstein-Kac telegraph processes with random speeds: Path probabilities, likelihoods, and reported Lévy flights,” *Physical Review E* **91** (2015), 042115, doi:10.1103/PhysRevE.91.042115 (publicly dated 2015-04-15).
- B. De Bruyne, S. N. Majumdar, and G. Schehr, “Survival probability of a run-and-tumble particle in the presence of a drift,” *Journal of Statistical Mechanics* (2021), 043211, arXiv:2101.11895v1, https://arxiv.org/html/2101.11895v1.
