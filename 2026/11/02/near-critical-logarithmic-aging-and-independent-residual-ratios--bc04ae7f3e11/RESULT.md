# Near-critical logarithmic aging and independent residual ratios for Zipf disaster renewals

## Finding
For each fixed \(c\in\mathbb R\), the Zipf disaster chain at the logarithmic recurrence boundary has a finite-size scaling limit. If the exponent at observation horizon \(N\) is \(\beta_N=1+c/\log N\), then the logarithmic age and remaining lifetime relative to the age converge jointly to **independent** limits:
\[
\left(\frac{\log(1+A_N)}{\log N},\frac{R_N}{1+A_N}\right)\ \Rightarrow\ (U_c,V),\qquad
f_{U_c}(u)=\frac{e^{-cu}}{h(c)}\mathbf1_{(0,1)}(u),\quad
\Pr(V>v)=\frac1{1+v}\ (v\ge0),
\]
where \(h(c)=\int_0^1e^{-cu}\,du=(1-e^{-c})/c\) for \(c\ne0\), and \(h(0)=1\). In particular, for every \(0<\theta<1\),
\[
\lim_{N\to\infty}\Pr(A_N\ge N^\theta)
=\frac{\int_\theta^1e^{-cu}\,du}{h(c)}.
\]
The case \(c=0\) recovers the classical critical logarithmic-age law; the nonzero-\(c\) finite-size crossover is the distinguishing contribution.

## Assumptions and scope
For a fixed real \(c\), at each sufficiently large integer \(N\), define a **separate**, time-homogeneous Markov chain \((K_j^{(N)})_{j\ge0}\) starting at \(K_0^{(N)}=0\). For every state \(k\in\mathbb N_0\), the transition \(k\to k+1\) has probability
\[
p_{N,k}=\left(\frac{k+1}{k+2}\right)^{\beta_N},\qquad \beta_N=1+\frac{c}{\log N}>0,
\]
and the complementary probability produces a reset to zero. Independent transition uniforms are used, conditionally on current state. Define \(A_N=K_N^{(N)}\) and \(R_N=\inf\{r\ge1:K_{N+r}^{(N)}=0\}\). The statement is about triangularly indexed chains (not one chain whose transitions vary over time). \(R_N\) is almost surely finite for each row because the excursion length has proper tail \((k+1)^{-\beta_N}\).

## Proof
**1. Exact renewal representation.** A complete excursion length \(T_N\) has tail
\[
\Pr(T_N>k)=\prod_{j=0}^{k-1}p_{N,j}=(k+1)^{-\beta_N},\quad k\in\mathbb N_0,
\]
and mass \(f_{N,j}=j^{-\beta_N}-(j+1)^{-\beta_N}\) at \(j\ge1\). Put \(u_{N,m}=\Pr(K_m^{(N)}=0)\). The renewal generating series satisfies
\[
\sum_{m\ge0}u_{N,m}z^m=\frac1{(1-z)B_N(z)},\qquad
B_N(z)=\sum_{k\ge0}(k+1)^{-\beta_N}z^k,\quad 0\le z<1.
\]
Renewal decomposition according to the last visit to zero before time \(N\) gives, for \(0\le k\le N\),
\[
\Pr(A_N=k)=u_{N,N-k}(k+1)^{-\beta_N}. \tag{1}
\]
**2. Monotone renewal masses.** For every fixed positive exponent, the transition map \(T(k,v)=(k+1)\mathbf1_{\{v\le((k+1)/(k+2))^\beta\}}\) is nondecreasing in \(k\), since the success probability increases with \(k\). Consequently, the Markov transition kernel preserves stochastic order. Since the initial point mass at zero is stochastically below its one-step image, induction gives \(K_{m+1}\succeq_{\mathrm{st}}K_m\) for all \(m\); hence \(u_{N,m}\) is nonincreasing in \(m\).

**3. Triangular logarithmic renewal estimate.** Write \(h(c)=\int_0^1e^{-cs}\,ds\). For each fixed \(t>0\),
\[
\frac{B_N(e^{-t/N})}{\log N}\longrightarrow h(c).
\tag{2}
\]
Indeed, on \(1\le j\le N\), \(j^{-\beta_N}=j^{-1}\exp[-c(\log j)/(\log N)]\), and a logarithmic Riemann sum divided by \(\log N\) tends to \(h(c)\). Replacing the summand by its factor \(e^{-tj/N}\) changes the sum by at most \((t/N)\sum_{j\le N}j^{1-\beta_N}=O_c(1)\). The contribution of \(j>N\) is \(O_{c,t}(1)\), by exponential damping and \(N^{1-\beta_N}=e^{-c}\). The initial index shift affects only a bounded error.

Define a locally finite measure on \([0,\infty)\) by
\[
\mu_N=\frac{h(c)\log N}{N}\sum_{m\ge0}u_{N,m}\delta_{m/N}.
\]
Using the renewal generating identity and (2), its Laplace transform tends to \(1/t\) for each \(t>0\):
\[
\int e^{-tx}\mu_N(dx)=\frac{h(c)\log N}{N(1-e^{-t/N})B_N(e^{-t/N})}\longrightarrow\frac1t.
\]
For rigor with these locally finite measures, tilt by \(e^{-x}\). Their finite tilted masses tend to one, and the Laplace transforms of these tilted measures tend to \(1/(1+t)\) for every \(t\ge0\). The continuity theorem for probability Laplace transforms gives weak convergence to the exponential law, hence \(\mu_N\) converges vaguely to Lebesgue measure. Nonincreasing \(u_{N,m}\) and interval-average bounds now give
\[
h(c)\log N\ u_{N,\lfloor Nx\rfloor}\longrightarrow1
\quad(x>0), \tag{3}
\]
uniformly for \(x\) in any compact subinterval of \((0,\infty)\). Specifically, average the masses over \((x-\delta,x+\delta)\) and sandwich the central mass between the two monotone endpoint values; then let \(\delta\downarrow0\).

**4. Logarithmic age.** Fix \(0<a<b<1\). For all ages \(N^a\le k\le N^b\), the renewal index \(N-k\) lies in \([N-N^b,N-N^a]\), and (3) holds uniformly. Using (1),
\[
\Pr\left(a<\frac{\log(1+A_N)}{\log N}<b\right)
\longrightarrow\frac1{h(c)}\int_a^be^{-cs}\,ds.
\]
The limiting interval masses integrate to one over \((0,1)\); since \(0\le A_N\le N\), no mass can escape to the endpoints. Therefore the logarithmic age converges to \(U_c\) with the stated density, and \(A_N\to\infty\) in probability.

**5. Relative residual lifetime and independence.** By the Markov property and telescoping, for every integer \(r\ge0\),
\[
\Pr(R_N>r\mid A_N=k)=\left(\frac{k+1}{k+r+1}\right)^{\beta_N}.\tag{4}
\]
For any \(v\ge0\), choosing \(r=\lfloor v(k+1)\rfloor\), the right-hand side tends to \((1+v)^{-1}\) **uniformly over all \(k\ge N^a\)** for fixed \(a>0\), since \(\beta_N\to1\). By Step 4 the probability of \(A_N<N^a\) can be made arbitrarily small by sending \(a\downarrow0\) after \(N\to\infty\). Conditional laws of \(R_N/(1+A_N)\) therefore converge uniformly in probability to the same continuous law, which implies joint weak convergence with the logarithmic age and independence. This proves the assertion.

## Verification
The standalone `verify.py` verifies the exact renewal convolution, finite-time age law and monotonic renewal masses with rational arithmetic at the critical exponent, checks full finite-time normalization for multiple near-critical exponents, and computes illustrative logarithmic-age CDFs. The `verification_output.txt` records actual results. These finite checks are diagnostic, not a replacement for the renewal-transform proof.

## Relationship to prior work
Huillet (arXiv:2610.29974v1, §§3–3.2) defines the disaster chain, identifies its excursion law, its recurrence boundary \(\beta=1\), and the contact-probability asymptotics for fixed \(\beta\). Those facts are prior work. Erickson (1970, Theorem 6 and §9) gives a general fixed-law infinite-mean renewal waiting-time theorem at tail exponent one; for \(\Pr(T>k)=1/(k+1)\), it implies the **\(c=0\)** uniform logarithmic-age case, so that special case is expressly not asserted as new. Caravenna–Sun–Zygouras (2019, §§1.1–1.2) study a different triangular renewal array with cutoff-normalized interarrival masses proportional to \(1/j\), and give Dickman-subordinator renewal limits. It does not directly provide the present untruncated excursion-tail array with exponent \(1+c/\log N\), its tilted-log-age crossover, or its joint residual-ratio law. Known classical fixed-exponent renewal theorems are relevant analytic background; absence of an identified dominating theorem is not a proof of priority.

## Limitations
The result is proved only for the specified Zipf-power tail and fixed finite \(c\), with one separately homogeneous chain per observation horizon. It makes no uniform assertion for unbounded \(c\), no finite-sample error bound, and no assertion for arbitrary slowly varying modifications of the excursion law. The logarithmic uniform result at \(c=0\) was already implied by Erickson's fixed-law theorem. A broad historical triangular-array theorem might subsume some or all of the nonzero-\(c\) conclusion; independent priority review has not been performed.

## References
1. T. E. Huillet, *On Divisibility Properties of Zipf Law and Relatives*, arXiv:2610.29974v1 (first submitted 2026-10-21), §§3–3.2. https://arxiv.org/abs/2610.29974
2. K. B. Erickson, *Strong Renewal Theorems with Infinite Mean*, Trans. Amer. Math. Soc. 151 (1970), 263–291, especially Theorem 6 (§9). https://doi.org/10.1090/S0002-9947-1970-0268976-9
3. F. Caravenna, R. Sun, N. Zygouras, *The Dickman subordinator, renewal theorems, and disordered systems*, Electron. J. Probab. 24 (2019), paper 101, §§1.1–1.2. https://arxiv.org/abs/1805.01465
