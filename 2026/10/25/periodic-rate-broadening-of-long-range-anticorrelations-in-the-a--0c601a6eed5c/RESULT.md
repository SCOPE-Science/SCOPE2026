# Periodic-rate broadening of long-range anticorrelations in the asymmetric simple inclusion process

## Finding
Consider the stationary asymmetric simple inclusion process (ASIP) with Poisson particle injection at rate \(\lambda>0\), and independent exponential gates with rates \(\mu_i>0\). Write \(X_i\) for the occupancy of site \(i\), with all particles at \(i\) moved together to \(i+1\) when gate \(i\) opens. On a finite array, the final gate removes its contents. For every \(1\le i<j\), define \(H_{i,j}\) by
\[
H_{0,j}=0,\qquad H_{i,i}=1,\qquad
H_{i,j}=\frac{\mu_i H_{i-1,j}+\mu_j H_{i,j-1}}{\mu_i+\mu_j}\quad(1\le i<j).
\]
Then the **exact** stationary covariance is
\[
\operatorname{Cov}(X_i,X_j)=-\frac{\lambda^2}{\mu_i\mu_j}H_{i,j}<0.
\]
This representation identifies \(H_{i,j}\) as a positive-index meeting probability for two independent pure-death chains.

More substantially, assume a fixed positive period \(p\), \(\mu_{i+p}=\mu_i\), and put
\[
\bar a=\frac1p\sum_{r=1}^p\mu_r^{-1},\qquad
\bar b=\frac1p\sum_{r=1}^p\mu_r^{-2}.
\]
For *every* sequence of positive integers \(d_L\) with \(d_L/\sqrt L\to s\in(0,\infty)\), and every array containing sites \(L\) and \(L+d_L\),
\[
\boxed{\displaystyle
\lim_{L\to\infty}\frac{\operatorname{Cov}(X_L,X_{L+d_L})}
{\mathbb E[X_L]\,\mathbb E[X_{L+d_L}]}=-\operatorname{erfc}\!\left(\frac{s\bar a}{2\sqrt{\bar b}}\right).}
\]
Here \(\mathbb E[X_i]=\lambda/\mu_i\). The coefficient is sensitive to periodic heterogeneity through \(\bar b/\bar a^2\). Since \(\bar b\ge\bar a^2\), with strict inequality for genuinely nonconstant rates, periodic heterogeneity *widens* the negative-correlation layer relative to the homogeneous case at equal \(\bar a\). This is a statement about the normalized covariance, **not** the Pearson coefficient or the probability of an empty interval.

## Assumptions and scope
The number of sites is arbitrary but finite and at least \(j\); the input and all gate clocks are mutually independent Poisson processes; the gate rates are strictly positive and independent of occupancies. The finite-site identities hold for **arbitrary** positive rates, without periodicity. In the limit, the period \(p\) and all \(\mu_r\) are fixed as \(L\to\infty\); injection rate \(\lambda>0\) is fixed. \(\operatorname{erfc}(x)=\frac{2}{\sqrt\pi}\int_x^\infty e^{-t^2}\,dt\).

## Proof
**Existence and integrability.** For an array of \(n\) sites, set \(V=\sum_{k=1}^n(n+1-k)X_k\). Every gate firing with nonzero occupancy at site \(k\) decreases \(V\) by \(X_k\), and an arrival increases it by \(n\). Consequently the generator satisfies \(\mathcal L V=n\lambda-\sum_{k=1}^n\mu_kX_k\). A quadratic calculation, using \(X_k\le V\) and \(\sum_k\mu_kX_k\ge(\min_k\mu_k)V/n\), gives
\[
\mathcal LV^2\le\lambda(2nV+n^2)-\frac{\min_k\mu_k}{n}V^2.
\]
The chain is irreducible and this Foster bound gives its unique invariant probability with the second moments needed below. (Alternately, construct the finite array by its stationary input and gate processes.)

**First and second moments.** For all \(i\), flow balance gives \(\mu_i\mathbb EX_i=\lambda\). For \(i<j\), abbreviate \(M_{ij}=\mathbb E[X_iX_j]\). Applying the stationary generator to \(X_iX_j\) gives
\[
(\mu_i+\mu_j)M_{ij}
=\begin{cases}\lambda\mathbb EX_j,&i=1,\\\mu_{i-1}M_{i-1,j},&i>1,\end{cases}
+\mathbf{1}_{\{j>i+1\}}\mu_{j-1}M_{i,j-1}.
\]
There is no second incoming term for adjacent sites because opening gate \(i\) erases the source occupancy as it deposits into site \(i+1\). Substitute \(M_{ij}=\frac{\lambda^2}{\mu_i\mu_j}(1-H_{i,j})\) and use \(\mu_k\mathbb EX_k=\lambda\); the displayed recursion for \(H\) follows, with the adjacent boundary \(H_{i,i}=1\) and injection boundary \(H_{0,j}=0\). All recurrences are triangular, hence uniquely determine the moments.

**Dual collision representation and strict sign.** Let \(A_t,B_t\) be independent decreasing nearest-neighbor continuous-time chains, started at \(i<j\), with a jump from site \(k\ge1\) to \(k-1\) at rate \(\mu_k\). Stop when the lower chain reaches 0 or the two chains meet. First-event conditioning gives exactly the recursion for \(H\), with value 1 at positive-index meeting and value 0 when the lower chain hits 0. Thus \(H_{i,j}\) is the meeting-first probability. It lies strictly between zero and one for every \(i<j\) and strictly positive rates: paths in which the upper chain catches up before the lower moves have positive probability; the reverse paths also have positive probability. This proves strict negative covariance.

**Periodic diffusive boundary layer.** For the asymptotic argument only, periodically extend the positive-index rates to all integers and *continue each independent death chain below zero*; this extension does not alter the event of a positive-index meeting before the lower chain reaches zero. A continued chain started at \(L+O(\sqrt L)\) encounters a periodic array of independent exponential holding times of means \(\mu_k^{-1}\) and variances \(\mu_k^{-2}\). For every fixed \(\epsilon>0\) and \(u\in[0,1+\epsilon]\), the number of jumps by physical time \(t=\bar a L u\), centered by \(Lu\) and divided by \(\sqrt L\), converges functionally to \((\sqrt{\bar b}/\bar a)B_u\), up to an irrelevant Brownian sign. To see this, group holding times into consecutive periods: centered complete-block sums are independent, identically distributed, with total variance \(p\bar b\), and bounded-length remainders are negligible on the \(\sqrt L\) scale. Donsker's theorem followed by continuity of the inverse map at a strictly increasing linear function yields the jump-count limit. The starting phase and the \(O(\sqrt L)\) displacement affect only the deterministic initial jump-count offset, not the diffusion constant.

Apply the functional limit jointly to the independent chains started at \(L\) and \(L+d_L\). Until collision, the (upper minus lower) position difference, divided by \(\sqrt L\), converges on time \(\bar a L u\) to
\[
s+\frac{\sqrt{2\bar b}}{\bar a}B_u.
\]
The lower chain reaches 0 at time \(\bar a L(1+o_{\mathbb P}(1))\). Since \(s>0\), Brownian first-passage times have continuous distributions; convergence of the hitting event on compact intervals on either side of \(u=1\), followed by squeezing as those endpoints approach 1, gives
\[
H_{L,L+d_L}\longrightarrow
\mathbb P\!\left(\inf_{0\le u\le1}\left[s+\frac{\sqrt{2\bar b}}{\bar a}B_u\right]\le0\right)
=\operatorname{erfc}\!\left(\frac{s\bar a}{2\sqrt{\bar b}}\right),
\]
by the Brownian reflection principle. The exact covariance identity finishes the proof. For constant rates \(\mu\), the argument recovers the coefficient \(\bar a/\sqrt{\bar b}=1\); it does not claim that the homogeneous error-function profile was previously unknown.

## Verification
The accompanying standalone script `verify.py` uses only the Python standard library. It verifies 224 exact rational stationary generator and homogeneous ballot identities and 12 finite-index comparisons of the periodic collision recursion with its scaling formula at \(L=900\), for gate patterns \((1)\), \((1,3)\), and \((1,2,4)\). All checks passed. These finite computations independently test the recurrence and coefficients; the arbitrary-length and asymptotic assertions are supplied by the proof above, not by finite enumeration.

## Relationship to prior work
Reuveni, Hirschberg, Eliazar and Yechiali [1] introduced exact incremental-load statistics in the self-review, developed a homogeneous interval scaling function \(\operatorname{erfc}(s/2)\), and supplied an inhomogeneous finite-array algorithm. Their Section IX specifically identifies correlations between *disjoint* intervals and asymptotic averaging of nonhomogeneous gate rates as natural further questions. These older results already imply some finite-site covariance information indirectly through differences of consecutive-interval moments; the finite recurrence and homogeneous profile are not asserted to be independently original. The present result isolates the **all-rate anticorrelation collision representation and the periodic-site, separated-position normalized covariance limit**, including its explicit ratio of inverse-rate moments. Reuveni, Eliazar and Yechiali [2] derived other large-system laws (traversal, loads, busy periods), but not this stated spatial periodic-rate limit. Yeger, Boxma, Resing and Vlasiou [3] analyze moments and correlations for an extended ASIP, and evaluate two-site cases of the original; those special cases are acknowledged as prior coverage. Their evaluated claims do not contain the general periodic large-index formula established here. The stochastic-clock FCLT and Brownian first-passage ingredients are classical; novelty, subject to further literature verification, concerns their combination with this stationary covariance observable and the explicit heterogeneity factor.

## Limitations
No claim about arbitrary nonperiodic or randomly disordered environments, vanishing rates, nonexponential gates, dynamic covariances, or Pearson correlation asymptotics is made. The functional limit assumes a fixed period with strictly positive finite rates. General moment algorithms can in principle compute fixed-site covariances; the main advance here is a tractable spatial structure and asymptotic coefficient. A comprehensive literature-priority examination of every queueing-theory variant has not been completed. Independent review has not been performed.

## References
[1] S. Reuveni, O. Hirschberg, I. Eliazar and U. Yechiali, “Occupation Probabilities and Fluctuations in the Asymmetric Simple Inclusion Process,” arXiv:1309.2894 (first public 2013-09-11); *Physical Review E* **89**, 042109 (2014), DOI:10.1103/PhysRevE.89.042109. https://arxiv.org/abs/1309.2894

[2] S. Reuveni, I. Eliazar and U. Yechiali, “Limit Laws for the Asymmetric Inclusion Process,” *Physical Review E* **86**, 061133 (2012), DOI:10.1103/PhysRevE.86.061133.

[3] Y. Yeger, O. Boxma, J. Resing and M. Vlasiou, “ASIP tandem queues with consumption,” *Performance Evaluation* **163**, 102380 (2024), DOI:10.1016/j.peva.2023.102380.
