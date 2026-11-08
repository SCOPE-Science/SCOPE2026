# A Gumbel law for Markovian super-coupon collection

## Finding

**Theorem.** Fix integers \(1\le s<r\). For each integer \(n>2r\), start with a uniformly sampled \(r\)-subset \(R_0\subset[n]\). At each integer time \(t\ge1\), choose an element uniformly from \(R_{t-1}\), remove it, and replace it by an element uniformly from \([n]\setminus R_{t-1}\), obtaining \(R_t\). An \(s\)-subset is *collected* once it is contained in some \(R_t\), including \(R_0\). Write \(T_n\) for the least \(t\ge0\) by which every \(s\)-subset has been collected, and put

\[
N_n=\binom ns,\qquad c_{r,s}=\binom{r-1}{s-1},\qquad \lambda_n=\frac{c_{r,s}}{N_n}.
\]

Then for every real \(x\),

\[
\boxed{\lim_{n\to\infty}\Pr\{\lambda_n T_n-\log N_n\le x\}=\exp(-e^{-x})},
\]

and

\[
\boxed{\mathbb ET_n\sim\frac{N_n}{c_{r,s}}\log N_n
=\frac rs\binom rs^{-1}\binom ns\log\binom ns.}
\]

Thus the fixed-parameter, temporally dependent case of the super-coupon cover-time conjecture of Athreya, Mukherjee and Mukherjee holds, and has a standard Gumbel fluctuation law. The proof also works for \(s=r\), whose first-order expectation was already known; that endpoint is not claimed as a new result.

## Assumptions and scope

The integers \(r,s\) are held fixed while \(n\to\infty\). Every move exchanges exactly one uniformly removed member of the current \(r\)-set with one uniformly sampled element outside the *old* \(r\)-set. The walk is the ordinary, non-lazy simple random walk on the Johnson graph \(J(n,r)\), started at its uniform stationary law. Any deterministic starting \(r\)-subset gives the same cover-time distribution by relabelling symmetry. The time convention including \(R_0\) differs by at most one from conventions that number the initial draw as round one.

The coefficient \(c_{r,s}\), not \(\binom rs\), is the stationary rate of *new entries* into the set of states containing a specified \(s\)-subset. A visit persists over several consecutive steps, and counting its full stationary occupation mass would give an incorrect cover-time scale.

## Proof

**1. Spectrum of the underlying walk.** On the vector space of real functions on the \(r\)-subsets of \([n]\), let \(P\) be the transition operator, and let \(\pi\) be uniform measure. It is reversible. For \(B\subset[n]\), \(|B|=j\le r\), write \(h_B(R)=\mathbf1\{B\subset R\}\). Directly enumerating the element removed and the element inserted gives

\[
Ph_B=\left(1-\frac{j(n+1-j)}{r(n-r)}\right)h_B
+\frac{r-j+1}{r(n-r)}\sum_{b\in B}h_{B\setminus\{b\}}.
\tag{1}
\]

Indeed, the indicator can become true only if \(B\) was already included and none of its members was removed, or if exactly one member was missing and that member was inserted. The identity \(\mathbf1\{|B\setminus R|=1\}=\sum_{b\in B}h_{B\setminus\{b\}}(R)-j h_B(R)\) yields (1). The spaces spanned by inclusion indicators of degrees at most \(j\) are nested, and those of degree \(r\) span all functions. Therefore the eigenvalues of \(P\) are among, and in fact are, the standard Johnson values

\[
\theta_j=1-\frac{j(n+1-j)}{r(n-r)},\qquad 0\le j\le r.
\tag{2}
\]

For all sufficiently large \(n\) (depending on fixed \(r\)), the eigenvalue \(1\) is simple and every other eigenvalue has absolute value at most \(1-\gamma_r\), for a constant \(\gamma_r>0\), for example \(\gamma_r=1/(2r)\). Hence

\[
\operatorname{Var}_\pi f\le\gamma_r^{-1}\langle f,(I-P)f\rangle_\pi
\tag{3}
\]

for all real functions \(f\). All the assertions in (1)--(3) use fixed \(r\) and sufficiently large \(n\).

**2. Entrance rates for finitely many specified super-coupons.** Fix an integer \(k\ge1\), independently of \(n\), and take any *distinct* \(s\)-subsets \(A_1,\ldots,A_k\). Let

\[
H_i=\{R:A_i\subset R\},\qquad H=\bigcup_{i=1}^k H_i.
\]

For an individual target, stationarity gives \(\pi(H_i)=\binom rs/N_n\). Conditional on \(R\in H_i\), the walk exits \(H_i\) in the next step precisely when one of the \(s\) prescribed members is removed. Consequently, by reversibility, the stationary entrance flux is **exactly**

\[
\Pr_\pi(R_0\notin H_i,R_1\in H_i)=\frac sr\frac{\binom rs}{N_n}=\lambda_n.
\tag{4}
\]

Uniformly over all distinct \(k\)-tuples of targets, with constants depending only on \(r,s,k\),

\[
\pi(H)=O(n^{-s}),\quad
\Phi_H:=\Pr_\pi(R_0\notin H,R_1\in H)
=k\lambda_n+O(n^{-s-1}).
\tag{5}
\]

To justify the second estimate rather than assuming independence, note that two distinct \(s\)-sets have union of size at least \(s+1\), whence \(\pi(H_i\cap H_j)=O(n^{-s-1})\). Moreover, if \(R_0\in H_j\) and \(R_1\in H_i\), with \(i\ne j\), either \(R_0\in H_i\cap H_j\), or the missing prescribed member of \(A_i\) must be the inserted element. The latter has conditional probability at most \(1/(n-r)\), giving \(O(n^{-s-1})\) after multiplication by \(\pi(H_j)\). Comparing entrance into the union with the sum of the individual entrance indicators, including simultaneous entrances, proves (5). Finally, with

\[
p_H(R)=\mathbf1\{R\notin H\}P(R,H),
\]

any first entry completes at least one target by inserting its single missing member, so

\[
0\le p_H(R)\le\frac{k}{n-r},\qquad
\lVert p_H\rVert_{L^2(\pi)}^2\le\frac{k}{n-r}\Phi_H=O(n^{-s-1}).
\tag{6}
\]

**3. The killed-chain eigenvalue and its entrance-flux expansion.** Let \(M\) be multiplication by \(\mathbf1_{H^c}\) and \(Q=MPM\) on \(L^2(\pi)\). The matrix is symmetric and entrywise nonnegative. Its largest eigenvalue \(\rho\) has a nonnegative eigenvector \(f\), normalized by \(\lVert f\rVert_2=1\), supported on \(H^c\); set \(a=\mathbb E_\pi f>0\) and \(\delta=1-\rho\). The Rayleigh quotient of \(\mathbf1_{H^c}\) yields

\[
0\le\delta\le\frac{\Phi_H}{1-\pi(H)}=O(n^{-s}).
\tag{7}
\]

Because \(\langle f,(I-P)f\rangle=\delta\), (3) gives \(\lVert f-a\rVert_2=O(n^{-s/2})\), hence \(a=1+O(n^{-s})\). Sum the eigenvalue equation \(Qf=\rho f\) over \(H^c\) with stationary weights, and use reversibility, to obtain the **exact identity**

\[
\delta a=\langle f,p_H\rangle_\pi.
\tag{8}
\]

Since \(\mathbb E_\pi p_H=\Phi_H\), Cauchy--Schwarz, (6) and (8) imply

\[
\left|\delta-\Phi_H\right|
\le a^{-1}\lVert f-a\rVert_2\lVert p_H\rVert_2
=O(n^{-s-1/2}).
\]

Combined with (5), this yields, uniformly over the prescribed \(k\) distinct targets,

\[
\boxed{1-\rho=k\lambda_n+O(n^{-s-1/2}).}
\tag{9}
\]

This argument is needed because stationary occupancy alone overcounts consecutive visits to the same target.

**4. Multiplicative avoidance probabilities.** By the minimax/interlacing principle, all eigenvalues of the compression \(Q|_{H^c}\) other than its largest are at most \(\theta_1\); by (2), they are also at least \(\theta_r\). Consequently, for large \(n\), their absolute values are at most \(1-\gamma_r\). Since the projection of \(\mathbf1_{H^c}\) onto the normalized positive eigenvector is \(a\), spectral expansion gives, for all integers \(t\ge0\),

\[
\begin{aligned}
\Pr_\pi\{R_0,\ldots,R_t\notin H\}
&=\langle\mathbf1_{H^c},Q^t\mathbf1_{H^c}\rangle_\pi\\
&=a^2\rho^t+O\bigl(n^{-s}(1-\gamma_r)^t\bigr),\qquad a^2=1+O(n^{-s}).
\end{aligned}
\tag{10}
\]

For \(t=\lfloor(\log N_n+x)/\lambda_n\rfloor\), where \(x\in\mathbb R\) is fixed, (9) gives

\[
\rho^t=\exp\{-k(\log N_n+x)+O(\log n/\sqrt n)\}.
\]

The remainder in (10) is negligible even relative to \(N_n^{-k}\). Thus the following **uniform joint avoidance estimate** holds for every fixed \(k\):

\[
\Pr\{A_1,\ldots,A_k\text{ all unseen by time }t\}
=N_n^{-k}e^{-kx}(1+o(1)),
\tag{11}
\]

uniformly over distinct \(s\)-sets \(A_1,\ldots,A_k\).

**5. Poisson cloud of missed super-coupons and Gumbel completion.** Let \(W_n(t)\) count the uncollected \(s\)-sets after observing \(R_0,\ldots,R_t\). From (11), for every fixed positive integer \(k\),

\[
\mathbb E(W_n(t))_k=(N_n)_k\,N_n^{-k}e^{-kx}(1+o(1))\longrightarrow e^{-kx},
\tag{12}
\]

where \((a)_k=a(a-1)\cdots(a-k+1)\) is the falling factorial. These are the factorial moments of a Poisson variable with mean \(e^{-x}\). The method of moments yields \(W_n(t)\Rightarrow\operatorname{Poisson}(e^{-x})\). Since \(T_n\le t\) exactly when \(W_n(t)=0\), (12) proves the Gumbel distribution statement, including its stated centering and time normalization.

**6. Expectation.** For any \(\varepsilon>0\), the Gumbel result gives

\[
\Pr\bigl\{T_n>(1-\varepsilon)\lambda_n^{-1}\log N_n\bigr\}\to1.
\]

For the upper bound put \(t_+=(1+\varepsilon)\lambda_n^{-1}\log N_n\) (rounded to an integer). Apply the union bound to the \(N_n\) possible missed targets, and use (10) with \(k=1\) for all subsequent times. If \(\rho_1=1-\lambda_n+O(n^{-s-1/2})\), then

\[
\sum_{t\ge t_+}\Pr(T_n>t)
\le \frac{N_n(1+O(n^{-s}))\rho_1^{t_+}}{1-\rho_1}
+O\bigl(N_n n^{-s}(1-\gamma_r)^{t_+}\bigr)
=o(\lambda_n^{-1}).
\tag{13}
\]

Summing the tail of the nonnegative integer-valued \(T_n\), and then letting \(\varepsilon\downarrow0\), proves \(\mathbb ET_n\sim\lambda_n^{-1}\log N_n\). This completes the proof.

## Verification

The standalone script `verify.py` enumerates the exact finite Johnson transitions, tests reversibility, checks identity (1) for all indicated small \(n,r,j,B,R\), verifies the single-target stationary flux (4) for every small \(s\), and checks the union-entry upper bound (6) with rational arithmetic. It also reports a seeded, finite stochastic diagnostic for the case \((r,s)=(3,2)\). The infinite-size theorem is proved by (1)--(13), **not** by finite enumeration or simulation. Run using `python3 verify.py` in a directory containing that supplied script.

## Relationship to prior work

Athreya, Mukherjee and Mukherjee (2023, Conjecture 2.4) state the exact leading-mean scale for their *temporally dependent* replacement-one-subset model; their Theorem 2.5 proves the equal-size case \(s=r\). Their different i.i.d.-subset model has rate \(\binom rs/N_n\), and they establish its Gumbel law (Theorem 2.3). The present result proves their dependent-model prediction for every fixed \(s<r\), and adds its Gumbel limit; the independent-subset theorem cannot be substituted because consecutive sampled \(r\)-sets overlap in \(r-1\) elements. The later open-access journal version retains the conjecture. Classical Johnson-graph eigenvalues, Matthews-type cover-time bounds, and rare-event exponential laws provide related tools, but none of the inspected specific sources states this shadow-cover theorem or the required uniform \(k\)-target avoidance estimates. Broader general cover-time theorems that may imply it remain a historical-priority risk.

## Limitations

The theorem requires \(r\) and \(s\) fixed, uniform single-element replacement, and an initially uniform state (although full cover time is invariant under the initial-state choice). It does not cover growing \(r\), growing \(s\), biased replacement, or a continuously changing universe. No explicit finite-\(n\) Kolmogorov error rate is claimed. The conclusions have not been independently mathematically audited; literature priority is not certified by unsuccessful searches.

## References

1. S. Athreya, S. Mukherjee, S. S. Mukherjee, *On a generalisation of the coupon collector problem*, arXiv:2304.01145, first submitted 3 April 2023, version 2 September 2023, especially Conjecture 2.4 and Theorems 2.3, 2.5. https://arxiv.org/abs/2304.01145
2. S. Athreya, S. Mukherjee, S. S. Mukherjee, same work, *Journal of Theoretical Probability* **38**, article 54 (2025); open-access version retains Conjecture 2.4. https://doi.org/10.1007/s10959-025-01417-w
3. D. Aldous and J. Fill, *Reversible Markov Chains and Random Walks on Graphs* (unfinished monograph), general background on finite reversible chains, Poincaré inequalities, hitting times and spectral methods. https://www.stat.berkeley.edu/~aldous/RWG/book.html
