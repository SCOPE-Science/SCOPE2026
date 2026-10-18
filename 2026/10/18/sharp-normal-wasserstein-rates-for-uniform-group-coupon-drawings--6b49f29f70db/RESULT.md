# Sharp normal Wasserstein rates for uniform group coupon drawings via an exact Poisson–binomial structure

## Finding
Let \(n\ge2\). Repeatedly draw independent, uniformly random subsets of \(\{1,\ldots,n\}\) of fixed size \(s\), with \(s\ge1\) fixed. Write \(Z_n\) for the number of coupons unseen after \(k_n=\lfloor (n/s)(\alpha\log n+x)\rfloor\) such drawings, with fixed \(0<\alpha<1\) and \(x\in\mathbb R\); all assertions below concern sufficiently large \(n\), so \(0\le s\le n\) and \(k_n\ge0\).

**Sharp rate theorem.** Put \(\mu_n=\mathbb E Z_n\), \(\sigma_n^2=\operatorname{Var}(Z_n)\), and let \(G\sim N(0,1)\). Then
\[
\sigma_n^2\sim e^{-x}n^{1-\alpha},\qquad
\frac{1/4-o(1)}{\sigma_n}\le d_{W_1}\left(\frac{Z_n-\mu_n}{\sigma_n},G\right)\le \frac{2}{\sigma_n}.
\]
In particular, the optimal Wasserstein-one convergence order is \(\Theta(n^{-(1-\alpha)/2})\) for **every** \(\alpha\in(0,1)\), resolving the rate-optimality question left open in Remark 2(i) of Betken–Thäle for \(\alpha\le1/3\).

**Finite-horizon structural theorem.** More generally, for every \(n\ge1\), every finite deterministic sequence of packet sizes \(s_1,\ldots,s_k\in\{0,\ldots,n\}\), and independently sampled uniform \(s_t\)-subsets, the number of never-selected labels after these packets has a Poisson–binomial distribution: it equals in law a sum of at most \(n\) independent Bernoulli variables. This is a statement about the *count*, not independence of the missing-label indicators.

## Assumptions and scope
We use \(d_{W_1}(U,V)=\sup_{\|h\|_{\mathrm{Lip}}\le1}|\mathbb E h(U)-\mathbb E h(V)|\). A Poisson–binomial law is a finite sum of mutually independent Bernoulli variables with arbitrary parameters in \([0,1]\). Packet draws are independent from draw to draw; within a draw labels are sampled *without replacement*. Packet sizes in the structural theorem may vary deterministically. The normal approximation requires fixed \(s\), fixed \(x\), fixed \(\alpha\), and growing \(n\); it does not claim parameter-uniform rates or a limiting constant for the Wasserstein distance.

## Proof
**1. Uniform-subset intersection preserves Poisson–binomial counts.** Suppose an exchangeable random missing set has cardinality \(X\) with Poisson–binomial parameters \(r_1,\ldots,r_n\), padded by zeros if necessary. Its law equals that obtained by independently retaining index \(i\) with probability \(r_i\), followed by an independent uniformly random permutation of the indices. A fresh independent uniformly random packet of size \(s\) leaves a uniformly random complement of size \(q=n-s\). The cardinality \(X'\) of the intersection between the old missing set and this complement therefore satisfies
\[
\mathbb E z^{X'}=\binom nq^{-1}e_q(1-r_1+r_1z,\ldots,1-r_n+r_nz),
\]
where \(e_q\) denotes the elementary symmetric polynomial of degree \(q\).

To establish real-rootedness, fix \(\operatorname{Im}z>0\) and define \(H_z(t)=\prod_{i=1}^n(t+1-r_i+r_i z)\). Every zero of this polynomial in \(t\) equals \(-1+r_i-r_i z\): for \(r_i>0\) it lies in the open lower half-plane, and for \(r_i=0\) it equals \(-1\). The convex hull of these zeros avoids \(t=0\), since any convex combination with zero imaginary part consists exclusively of the root \(-1\). By repeated Gauss–Lucas, \(H_z^{(n-q)}(0)\ne0\). Since this derivative equals \((n-q)!e_q(1-r_i+r_i z)\), the displayed probability-generating polynomial has no zero in the upper half-plane. Its real coefficients force all zeros to be real; its nonnegative coefficients force every root to be nonpositive. Every such probability-generating polynomial factors, after normalization at \(z=1\), into Bernoulli factors \((1-\theta)+\theta z\), with \(\theta\in[0,1]\). Initially \(X=n\) is deterministic, hence Poisson–binomial. Every new missing set remains exchangeable, so induction handles all packet-size sequences, including empty and full packets.

**2. Variance at the logarithmic sampling horizon.** Write \(u=(1-s/n)^{k_n}\) and \(v=[(n-s)(n-s-1)/(n(n-1))]^{k_n}\) for sufficiently large \(n>s+1\). For each label the missing probability is \(u\), and for each pair it is \(v\); hence
\[
\mu_n=nu,\qquad \sigma_n^2=nu(1-u)+n(n-1)(v-u^2).
\]
The exact ratio is \(v/u^2=[1-s/((n-1)(n-s))]^{k_n}\). Since \(k_n=(n/s)(\alpha\log n+x)+O(1)\), logarithmic expansion gives \(u=e^{-x}n^{-\alpha}(1+O(\log n/n))\) and \(v-u^2=O(u^2\log n/n)\). Consequently, \(\sigma_n^2=nu[1+O(u\log n+u)]\sim e^{-x}n^{1-\alpha}\), and \(\sigma_n\to\infty\).

**3. Independent-Bernoulli upper bound.** Represent \(Z_n\) in distribution as \(\sum_{i=1}^nB_i\) with independent \(B_i\sim\mathrm{Bernoulli}(r_i)\), write \(W=\sigma_n^{-1}\sum_i(B_i-r_i)\), and \(v_i=r_i(1-r_i)\), so \(\sum_i v_i=\sigma_n^2\). For a 1-Lipschitz test function \(h\), its standard-normal Stein solution \(f\) satisfies \(f'(w)-wf(w)=h(w)-\mathbb Eh(G)\) and the standard bound \(\|f''\|_\infty\le2\). Put \(W_i=W-(B_i-r_i)/\sigma_n\). Bernoulli conditioning and the fundamental theorem of calculus yield
\[
\mathbb E[Wf(W)]=\sum_i\frac{v_i}{\sigma_n^2}\int_0^1\mathbb E f'\left(W_i+\frac{t-r_i}{\sigma_n}\right)dt.
\]
Subtract \(\mathbb Ef'(W)\); since \(|W-[W_i+(t-r_i)/\sigma_n]|=|B_i-t|/\sigma_n\le1/\sigma_n\) and the weights sum to one, the absolute error is at most \(2/\sigma_n\). The Stein equation and Wasserstein duality prove the upper bound. The absolute constant comes from a standard normal Stein derivative estimate, rather than any finite computation.

**4. Universal lattice lower bound.** For any real \(\mu\), \(\sigma>0\), and integer-valued \(X\), the function \(h_\sigma(w)=\operatorname{dist}(w,(\mathbb Z-\mu)/\sigma)\) is 1-Lipschitz and vanishes on \((X-\mu)/\sigma\). Therefore
\[
\sigma d_{W_1}((X-\mu)/\sigma,G)\ge\mathbb E\operatorname{dist}(\sigma G+\mu,\mathbb Z).
\]
The periodic function \(\operatorname{dist}(t,\mathbb Z)\) has period one and mean \(1/4\). For a standard Gaussian, smooth-density averaging (integrating its centered bounded periodic primitive against the Gaussian density) gives \(\mathbb E\operatorname{dist}(\sigma G+\mu,\mathbb Z)=1/4+O(1/\sigma)\), uniformly in \(\mu\). Apply with \(X=Z_n\), \(\mu=\mu_n\), and \(\sigma=\sigma_n\to\infty\). This proves the lower bound and the sharp two-sided order.

## Verification
The standalone `verify.py` reconstructs all hypergeometric update probabilities using exact rational arithmetic. Across 949 varying packet-size and sample-size configurations it checks normalization and every factorial moment \(\mathbb E\binom Xj=\binom nj\prod_t\binom{n-j}{s_t}/\binom n{s_t}\), with the convention that impossible binomial selections contribute zero. For 88 additional polynomial instances it obtains exact rational real-root isolating intervals and verifies all roots lie on the nonpositive real line. These finite cases independently stress-test the structural calculation; the Gauss–Lucas induction is the proof for arbitrary horizons and alphabet sizes.

## Relationship to prior work
Betken and Thäle, *Approaching the coupon collector's problem with group drawings via Stein's method* (arXiv:2202.07485v1, posted February 15, 2022), prove central limit behavior and upper Wasserstein rates \(O(\sqrt{\log n}/n^\alpha)\) for \(\alpha\le1/3\), and \(O(n^{-(1-\alpha)/2})\) for \(\alpha>1/3\). Their Remark 2(i) explicitly leaves optimality for \(\alpha\le1/3\) open. Our finite-horizon Poisson–binomial representation yields a sharper rate throughout that range; the lattice argument proves sharpness also above the boundary. General real-stability and negative-dependence methods in Borcea–Brändén–Liggett and classical Stein inequalities provide relevant background, but their general principles do not themselves state the specific group-drawing rate theorem. Vatutin–Mikhailov's early limit theorems address normal/Kolmogorov approximation for group allocation; available material does not establish the present Wasserstein rate.

## Limitations
The normal-rate theorem is for uniform packets of a fixed size \(s\), not arbitrary nonuniform subset distributions; the finite-horizon Poisson–binomial theorem permits varying deterministic sizes but still uniform subsets. The asymptotic constants are not asserted uniformly as \(\alpha\to0\) or \(\alpha\to1\). The result proves the optimal order, not an exact leading limit for the Wasserstein distance. Earlier literature could contain an equivalent theorem under different terminology; archival material was not all available in full. This is a self-review, not an independent audit.

## References
1. C. Betken and C. Thäle, *Approaching the coupon collector's problem with group drawings via Stein's method*, arXiv:2202.07485v1, February 15, 2022; https://arxiv.org/abs/2202.07485 .
2. J. Borcea, P. Brändén, T. M. Liggett, *Negative dependence and the geometry of polynomials*, Journal of the American Mathematical Society 22 (2009), 521–567; arXiv:0707.2340.
3. V. A. Vatutin and V. G. Mikhailov, *Limit theorems for the number of empty cells in an equiprobable scheme for group allocation of particles*, Theory of Probability and Its Applications 27 (1983), DOI:10.1137/1127084.
4. N. Ross, *Fundamentals of Stein's method*, Probability Surveys 8 (2011), 210–293, for classical normal Stein estimates.
