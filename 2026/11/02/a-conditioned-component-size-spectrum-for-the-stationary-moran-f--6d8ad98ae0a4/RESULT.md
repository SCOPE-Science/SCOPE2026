# A conditioned component-size spectrum for the stationary Moran forest

## Finding

Let \(F_n\) be the stationary Moran forest on \(n\ge3\) vertices as defined by Bienvenu, Duchamps, and Foutel-Rodier. Let \(N_n\) be its number of rooted-tree components and \(C_{n,k}\) the number having exactly \(k\) vertices. Fix \(\alpha\in(0,1)\), and put \(r_n=\lfloor\alpha n\rfloor\). All conclusions below concern sufficiently large \(n\), for which \(1\le r_n\le n-1\).

There is a unique \(\lambda=\lambda(\alpha)>0\) satisfying
\[
\alpha=\int_0^1\frac{\lambda(1-t)}{\lambda+(1-\lambda)t}\,dt
=\begin{cases}\displaystyle\frac{\lambda(\lambda-1-\log\lambda)}{(\lambda-1)^2},&\lambda\ne1,\\[4pt] 1/2,&\lambda=1.\end{cases}
\]
Define \(d_\lambda(t)=\lambda+(1-\lambda)t\),
\[
q_\lambda(t)=\exp\!\left(-\int_t^1\frac{du}{d_\lambda(u)}\right)
=\begin{cases}d_\lambda(t)^{1/(1-\lambda)},&\lambda\ne1,\\ e^{t-1},&\lambda=1,\end{cases}
\]
and for every integer \(k\ge1\),
\[
c_k(\alpha)=\int_0^1 \frac{\lambda(1-t)}{d_\lambda(t)}
q_\lambda(t)[1-q_\lambda(t)]^{k-1}\,dt.
\]
Then, under the **exact conditioning** \(N_n=r_n\),
\[
\boxed{\quad\sum_{k\ge1}k\left|\frac{C_{n,k}}n-c_k(\alpha)\right|
\xrightarrow[n\to\infty]{\mathbb P}0.\quad}
\]
The deterministic spectrum obeys \(\sum_{k\ge1}c_k(\alpha)=\alpha\) and \(\sum_{k\ge1}k c_k(\alpha)=1\). Thus the conditional size of a uniformly sampled component converges in total variation to the law assigning probability \(c_k(\alpha)/\alpha\) to size \(k\); the conditional size of the component containing a uniformly sampled vertex converges in total variation to the size-biased law with probabilities \(k c_k(\alpha)\). The special case \(\alpha=1/2\) recovers the previously known unconditioned geometric-mixture spectrum.

## Assumptions and scope

The Moran forest is the stationary law of the finite-vertex forest rewiring chain in [1]. Its uniform-attachment representation [1, Proposition 2.1] is used: independently for each \(i\in\{1,\ldots,n\}\), sample \(U_i\) uniformly from \(\{1,\ldots,n\}\setminus\{i\}\), and place the edge from \(U_i\) to \(i\) precisely when \(U_i<i\). The resulting increasing forest, uniformly relabeled, has law \(F_n\). Both component counts and sizes are relabeling-invariant. The parameter \(\alpha\) is fixed strictly between zero and one, and the asserted limits are conditional probabilities under \(N_n=r_n\), not almost-sure limits under a coupling across \(n\).

## Proof

**1. Exponential change of measure and conditioning.** Let \(R_i=\mathbf1\{U_i>i\}\), so \(N_n=\sum_iR_i\). For any \(\lambda>0\), weight the original probability of the independent parent-choice vector by \(\lambda^{N_n}\) and normalize to define \(\mathbb P_\lambda\). This product tilt leaves the choices independent. Specifically, with
\[
D_{i,n}=i-1+\lambda(n-i),\qquad
p_{i,n}=\frac{\lambda(n-i)}{D_{i,n}},
\]
the \(i\)-th vertex becomes a root with probability \(p_{i,n}\), and every particular older vertex is selected as its parent with probability \(1/D_{i,n}\). Consequently
\[
\mathcal L( F_n\mid N_n=r)
=\mathcal L_\lambda(F_n\mid N_n=r)
\]
for every admissible \(r\) (up to the independent uniform relabeling). This identity is exact, not asymptotic.

**2. Root-count local probability.** Write \(p_\lambda(t)=\lambda(1-t)/d_\lambda(t)\). Since \(D_{i,n}=(n-1)d_\lambda((i-1)/(n-1))\), a Riemann sum gives
\[
\mathbb E_\lambda N_n=n\alpha+O(1),\qquad
\operatorname{Var}_\lambda N_n=n v_\lambda+O(1),\qquad
v_\lambda=\int_0^1p_\lambda(t)(1-p_\lambda(t))\,dt>0.
\]
The integral defining \(\alpha\) increases continuously and strictly from zero to one as \(\lambda\) runs from zero to infinity: its integrand has derivative \(t(1-t)/d_\lambda(t)^2>0\) for \(0<t<1\). This proves the claimed uniqueness. Independence of the Bernoulli indicators and the bound
\[
\left|\mathbb E_\lambda e^{is(N_n-\mathbb E_\lambda N_n)}\right|
\le\exp\!\left[-2\operatorname{Var}_\lambda(N_n)\sin^2(s/2)\right]
\]
combine with their third-order characteristic-function Taylor expansion for \(s=O(n^{-1/2})\) to give the standard lattice local central limit theorem by Fourier inversion. Since \(r_n-\mathbb E_\lambda N_n=O(1)\),
\[
\mathbb P_\lambda(N_n=r_n)=\frac{1+o(1)}{\sqrt{2\pi n v_\lambda}}.
\]
The entire mass of this conditioning event is polynomially, rather than exponentially, small under the tilt.

**3. An exact component-count recurrence.** Let \(C_k(i)\) count size-\(k\) components after the first \(i\) arrivals under \(\mathbb P_\lambda\), and put \(m_{k,i}=\mathbb E_\lambda C_k(i)\), \(m_{k,0}=0\), \(m_{0,i}=0\). In a root arrival, exactly one new singleton appears; otherwise a size-\(h\) component is selected with total probability \(h C_h(i-1)/D_{i,n}\). Thus, with no approximation,
\[
m_{k,i}-m_{k,i-1}=p_{i,n}\mathbf1_{\{k=1\}}+
\frac{(k-1)m_{k-1,i-1}-k m_{k,i-1}}{D_{i,n}}.
\]
Because \(d_\lambda\) stays uniformly positive on \([0,1]\), for every fixed \(k\) this is a stable Euler approximation to the uniquely solved triangular system
\[
c_k'(t)=p_\lambda(t)\mathbf1_{\{k=1\}}
+\frac{(k-1)c_{k-1}(t)-k c_k(t)}{d_\lambda(t)},
\qquad c_k(0)=0.
\]
It follows that \(m_{k,n}/n\to c_k(1)\).

**4. Explicit solution.** A component immigrating as a singleton at time \(t\) subsequently follows the pure-birth (Yule) equations with per-particle rate \(1/d_\lambda(u)\) at time \(u\). Its size at time one has geometric distribution
\[
\Pr\{\text{size}=k\mid\text{birth at }t\}
=q_\lambda(t)[1-q_\lambda(t)]^{k-1}.
\]
Integrating this Green function against the immigration intensity \(p_\lambda(t)\) solves the triangular ODE and gives the displayed \(c_k(\alpha)\). Summing the geometric masses yields \(\sum_kc_k=\int_0^1p_\lambda(t)dt=\alpha\). The first moment is also exact: since \(q_\lambda'(t)=q_\lambda(t)/d_\lambda(t)\),
\[
\frac{d}{dt}\left(\frac{t}{q_\lambda(t)}\right)
=\frac{1-t/d_\lambda(t)}{q_\lambda(t)}
=\frac{p_\lambda(t)}{q_\lambda(t)}.
\]
Therefore \(\sum_k k c_k=\int_0^1p_\lambda(t)/q_\lambda(t)\,dt=[t/q_\lambda(t)]_0^1=1\).

**5. Concentration persists under exact conditioning.** Changing one parent choice moves at most one descendant subtree from one component into another, affecting at most a bounded number of component sizes. In particular the bounded-difference constant for any fixed \(C_k(n)\) is at most four. McDiarmid's inequality for the independent tilted choices gives, for every fixed \(\varepsilon>0\),
\[
\mathbb P_\lambda\left(\left|C_k(n)-m_{k,n}\right|>\varepsilon n\right)
\le2\exp(-\varepsilon^2 n/8).
\]
Dividing by the lower bound of order \(n^{-1/2}\) for \(\mathbb P_\lambda(N_n=r_n)\), and using the exact conditional-measure identity from step 1, proves \(C_{n,k}/n\to c_k(\alpha)\) in conditional probability for each fixed \(k\). Finally, \(\sum_k k C_{n,k}/n=1=\sum_k k c_k(\alpha)\); truncation at a sufficiently large fixed \(K\) then upgrades coordinatewise convergence to the displayed weighted \(\ell^1\) convergence. Dividing by \(r_n/n\to\alpha\) gives total-variation convergence for a uniformly chosen component, while the weighted convergence directly gives the analogous assertion for a uniformly chosen vertex. \(\square\)

## Verification

The accompanying standalone `verify.py` independently enumerates every parent-choice vector for \(2\le n\le6\), compares exact rational tilted mean component counts against the distinct recursion, checks the partition-size identities and compares the limiting integrals with numerical finite-size recurrences for six different tilt values. It passes 170 assertions. These finite checks support the calculations but do not substitute for the infinite-sample proof, which is in the preceding section.

## Relationship to prior work

Bienvenu, Duchamps and Foutel-Rodier [1] establish the stationary Moran forest's independent uniform-attachment representation (Proposition 2.1), independent-Bernoulli root-count law (Proposition 3.1), and the unconditioned limiting size of a uniformly selected tree (Section 5). They also explain why the complete exchangeable partition probability function is difficult to express. The present theorem treats the genuinely different rare conditioning \(N_n=\lfloor\alpha n\rfloor\) at any fixed \(\alpha\ne1/2\), obtains the entire empirical spectrum rather than one unconditional randomly sampled tree, and strengthens convergence to a weighted total-variation statement. The explicit time-inhomogeneous Yule law and the polynomial-cost conditioning argument are needed beyond the cited marginal results. Standard bounded-difference and local-limit tools [2,3] are used, not claimed as new.

## Limitations

The result concerns fixed interior component densities \(0<\alpha<1\), not an endpoint limit \(\alpha\to0\) or \(\alpha\to1\), a moving-density critical window, a largest-component extreme-value law, or the complete finite exchangeable partition law. No finite-sample error rate for the conditioned weighted spectrum is asserted. The source's precise unconditioned component-size law is recovered at \(\alpha=1/2\), so that case alone is not a novelty claim. Mathematical priority beyond the inspected sources is not established by the absence of a matching search result.

## References

[1] F. Bienvenu, J.-J. Duchamps and F. Foutel-Rodier, *The Moran forest*, arXiv:1906.08806 (first publicly posted 20 June 2019), later *Random Structures & Algorithms* 59 (2021), 155–188. https://arxiv.org/abs/1906.08806 ; full preprint https://arxiv.org/pdf/1906.08806.

[2] C. McDiarmid, *On the method of bounded differences*, in *Surveys in Combinatorics 1989*, London Mathematical Society Lecture Note Series 141, 148–188, Cambridge University Press, 1989.

[3] V. V. Petrov, *Sums of Independent Random Variables*, Springer, 1975; standard local limit theorems for triangular arrays of independent integer-valued variables.
