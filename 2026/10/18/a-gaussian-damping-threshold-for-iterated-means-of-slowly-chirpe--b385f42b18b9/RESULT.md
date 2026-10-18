# A Gaussian damping threshold for iterated means of slowly chirped weighted shifts

## Finding

The arithmetic (mean) transform of a positive weighted shift is an averaging operation. Nevertheless, slowly oscillating weights can produce three distinct topological regimes under repeated mean transforms. The critical frequency exponent is \(\beta=1/2\), where binomial averaging leaves a nontrivial Gaussian damping factor.

**Theorem.** Fix real \(0<\varepsilon<1\), \(\vartheta>0\), and \(0<\beta<1\). Let \(H=\ell^2(\mathbb N_0)\) over the complex numbers with orthonormal basis \((e_j)_{j\ge0}\). Let \(S e_j=e_{j+1}\) and let \(W_\beta\) be the strictly positive unilateral weighted shift
\[
W_\beta e_j=w_j e_{j+1},\qquad w_j=1+\varepsilon\cos\!\bigl(\vartheta(j+1)^\beta\bigr),\qquad j\ge0.
\]
For the mean transform \(M(T)=(T+|T|U)/2\) with \(T=U|T|\), write \(W_{\beta,n}=M^n(W_\beta)\), for integers \(n\ge0\). Define \(h_{j,n}=j+1+n/2\) and \(t_{j,n}=\vartheta\beta h_{j,n}^{\beta-1}\). Then the \(j\)-th weight of \(W_{\beta,n}\) is exactly
\[
w_j^{(n)}=1+\varepsilon\operatorname{Re}\mathbb E\exp\!\bigl(i\vartheta(j+J_n+1)^\beta\bigr),\qquad J_n\sim\operatorname{Bin}(n,1/2),
\]
and, for each fixed \(j\),
\[
\mathbb E\exp\!\bigl(i\vartheta(j+J_n+1)^\beta\bigr)
=e^{i\vartheta h_{j,n}^\beta}\Bigl[\cos(t_{j,n}/2)^n+O(n^{\beta-1})\Bigr]. \tag{1}
\]
The constants implicit in (1) may depend on \(\beta,\vartheta,j\), not on \(n\). Put
\[
A_\beta=\begin{cases}1&0<\beta<1/2,\\ e^{-\vartheta^2/16}&\beta=1/2,\\ 0&1/2<\beta<1.\end{cases}
\]
For every fixed \(j\ge0\),
\[
\limsup_{n\to\infty}w_j^{(n)}=1+\varepsilon A_\beta,\qquad
\liminf_{n\to\infty}w_j^{(n)}=1-\varepsilon A_\beta. \tag{2}
\]
In particular:

* When \(1/2<\beta<1\), the iterates converge to \(S\) in the strong operator topology.
* When \(0<\beta\le1/2\), they do not converge even in the weak operator topology.
* For **every** \(0<\beta<1\) and every finite integer \(n\ge0\),
  \[
  \|W_{\beta,n}-S\|=\varepsilon,\qquad \|W_{\beta,n}\|=1+\varepsilon. \tag{3}
  \]

Moreover, each \(W_\beta\) is essentially normal (its self-commutator is compact), and
\[
\lim_{N\to\infty}\frac1N\sum_{j=0}^{N-1}w_j=1. \tag{4}
\]
Thus the initial weights have the same Cesàro mean in all regimes, and their adjacent variations tend to zero, but these facts do not determine the topology of convergence of their iterated arithmetic means.

## Assumptions and scope

We use the usual operator norm and the strong and weak operator topologies on \(B(H)\). All weights are real and belong to \([1-\varepsilon,1+\varepsilon]\), so their polar partial isometry is exactly \(S\) at every stage. Only \(0<\beta<1\) is asserted. The assertions concern fixed coordinates as \(n\to\infty\) and norms over **all** coordinates; these are different orders of quantification. No monotonicity, hyponormality, or subnormality of the initial shift is assumed.

## Proof

**1. Arithmetic binomial law.** For a strictly positive weighted shift, the Duggal transform \(|T|U\) is the shift of the same weights by one site. Thus \(M(T)\) has the average of adjacent weights. Iterating this identity yields, by Pascal's recurrence,
\[
w_j^{(n)}=2^{-n}\sum_{k=0}^n\binom nk\left[1+\varepsilon\cos\!\bigl(\vartheta(j+k+1)^\beta\bigr)\right]. \tag{5}
\]
This is the stated binomial expectation, without approximation.

**2. Uniformly controlled phase linearization at a fixed site.** Put \(Y_n=J_n-n/2\) so \(\mathbb E Y_n=0\), \(\mathbb E Y_n^2=n/4\). For each fixed \(j\), set \(h=h_{j,n}=j+1+n/2\). On \(|Y_n|\le n/4\), the second derivative of \(x\mapsto x^\beta\) has modulus at most \(C_{\beta,j}n^{\beta-2}\) throughout the segment joining \(h\) and \(h+Y_n\). Taylor's theorem therefore gives
\[
|(h+Y_n)^\beta-h^\beta-\beta h^{\beta-1}Y_n|
\le C_{\beta,j}n^{\beta-2}Y_n^2.
\]
Using \(|e^{iu}-e^{iv}|\le|u-v|\), expectation of the right-hand side is \(O(n^{\beta-1})\). The binomial Chernoff bound makes \(\mathbb P(|Y_n|>n/4)\) exponentially small; on its complement both exponentials have modulus one. Consequently
\[
\mathbb E e^{i\vartheta(h+Y_n)^\beta}
=e^{i\vartheta h^\beta}\mathbb E e^{it_{j,n}Y_n}+O(n^{\beta-1}).
\]
The centered binomial characteristic function is exactly
\[
\mathbb E e^{itY_n}=\left(\cos(t/2)\right)^n.
\]
This proves (1), including its error bound. The error tends to zero for each fixed \(j\) because \(\beta<1\).

**3. Exact damping transition.** Since \(t_{j,n}\to0\),
\[
\log\cos(t_{j,n}/2)^n=-\frac n8t_{j,n}^2+O(nt_{j,n}^4),
\]
and the leading exponent is
\[
\frac n8t_{j,n}^2\sim\vartheta^2\beta^2 2^{-1-2\beta}n^{2\beta-1}.
\]
For \(\beta<1/2\) it tends to zero, at \(\beta=1/2\) it tends to \(\vartheta^2/16\), and for \(\beta>1/2\) it tends to infinity. In the last regime, the cosine power tends to zero even though the displayed fourth-order remainder need not vanish absolutely for \(\beta\) near one: the relative error in the exponent is \(O(t_{j,n}^2)=o(1)\), which suffices. The leading complex expectation therefore has the three stated limiting envelopes.

**4. Oscillatory subsequences and operator topology.** For each fixed \(j\), the phase \(\phi_j(n)=\vartheta(j+1+n/2)^\beta\) is increasing and unbounded while \(\phi_j(n+1)-\phi_j(n)\to0\). Its values approach integer multiples of \(2\pi\) and odd multiples of \(\pi\) along separate subsequences. Combining this with the damping factors in step 3 proves both exact limits in (2). If \(\beta\le1/2\), \(\langle W_{\beta,n}e_j,e_{j+1}\rangle=w_j^{(n)}\) has no limit, excluding weak operator convergence. If \(\beta>1/2\), every fixed weight tends to one, hence \((W_{\beta,n}-S)x\to0\) on all finitely supported vectors. Uniform boundedness \(\|W_{\beta,n}-S\|\le\varepsilon\) and density then establish strong convergence for all \(x\in H\).

**5. Sharp nonconvergence in operator norm.** For each fixed finite \(n\), arbitrarily large integers \(j\) have phase \(\vartheta(j+1)^\beta\) arbitrarily close to an even multiple of \(\pi\); because the phase increment across a fixed window of \(n\) sites tends to zero, all phases \(\vartheta(j+k+1)^\beta\) with \(0\le k\le n\) can simultaneously approach an even multiple of \(\pi\). The corresponding binomial averages approach one. Odd multiples produce averages approaching minus one. Since the absolute averages never exceed one, (5) implies \(\sup_j|w_j^{(n)}-1|=\varepsilon\) and \(\sup_jw_j^{(n)}=1+\varepsilon\), proving (3). Neither supremum is asserted to be attained.

**6. Essential normality and Cesàro mean.** The self-commutator of a unilateral positive weighted shift is diagonal with first entry \(w_0^2\) and later entries \(w_j^2-w_{j-1}^2\). Because \(\vartheta((j+1)^\beta-j^\beta)\to0\), these entries tend to zero, so the commutator is compact. Finally, elementary sum-integral comparison and integration by parts after the substitution \(u=x^\beta\) yield
\[
\sum_{j=1}^N e^{i\vartheta j^\beta}=O_{\beta,\vartheta}(N^\beta+N^{1-\beta})=o(N).
\]
Taking real parts proves (4). This completes the proof.

## Verification

The standalone Python 3 checker `check.py` independently computes binomial averages using a centered recurrence for binomial probabilities, compares with the linearized characteristic function, verifies representative amplitudes on both sides of the transition, and checks the full finite binomial identity against direct combinatorial sums for small orders. It reports `PASS: 387 independent finite numerical assertions`. These assertions support the formulas but are not proofs of limiting or infinite-dimensional statements; the analytic argument above supplies those proofs.

## Relationship to prior work

Lee, Lee, and Yoon introduced the mean transform and gave the binomial formula for its iterates on weighted shifts (Proposition 2.2); that finite-order identity is used here and is **not** claimed as original. Jung, Ko, and Park developed spectral and hyponormality criteria for transforms; their Lemma 3.19 and Theorem 3.20 similarly concern finite mean iterates. The present claim is the exponent-dependent limiting topological phase diagram and explicit critical Gaussian attenuation for a natural slowly oscillating positive-weight family, including simultaneous essential normality, fixed Cesàro mean, and uniform norm separation. Classical binomial/Euler summability explains the averaging mechanism but does not, in the inspected material, assert this complete weighted-shift topology classification. An equivalent earlier oscillatory-summation theorem could reduce the claim's priority; this possibility is not excluded by a negative search.

## Limitations

The classification is proved only for the displayed power-phase family with \(0<\beta<1\), real \(0<\varepsilon<1\), and \(\vartheta>0\); it makes no general claim for arbitrary slowly oscillating weights. The asymptotic error in (1) is for each fixed coordinate and is **not** uniform in all coordinates. The sharp norm identities instead require a separate far-tail argument. No quantitative rate for strong convergence on arbitrary infinite-support vectors is claimed. The originality assessment is literature-limited; classical Euler summation may contain equivalent special asymptotics. The earliest precisely day-resolved online source used for archive dating is 21 July 2015; the antecedent 2014 paper was public earlier, but its exact initial-publication day was not independently verified.

## References

1. S. H. Lee, W. Y. Lee, and J. Yoon, *The mean transform of bounded linear operators*, Journal of Mathematical Analysis and Applications **410** (2014), 70–81. DOI: `10.1016/j.jmaa.2013.08.003`. Proposition 2.2 provides the finite binomial-iterate formula.
2. S. Jung, E. Ko, and S. Park, *Subscalarity of operator transforms*, Mathematische Nachrichten **288** (2015), 2042–2056, published online 21 July 2015. DOI: `10.1002/mana.201500037`. See especially Lemma 3.19, Theorem 3.20, and Corollary 3.21. Public PDF: `https://cms.ewha.ac.kr/user/ebkmath/k2board/2019%20%EC%A2%85%ED%95%A9%ED%8F%89%EA%B0%80/%EB%B0%95%EC%8B%A0%ED%98%9C_S.pdf`.
3. R. W. Hakala, *The use of normalized binomial coefficients as weights to accelerate convergence of oscillatory first-order iterations*, International Journal of Quantum Chemistry **1** (1967), 277–284. DOI: `10.1002/qua.560010633`. The accessible abstract concerns general binomial smoothing rather than operator-limit classifications.
