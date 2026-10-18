# Exact first-passage transform and strict balancing law for nonuniform clumsy coupon collection

## Finding

Consider \(m\ge2\) coupon types, sampled independently at each discrete step with respective probabilities \(w_i>0\), where \(\sum_{i=1}^m w_i=1\). Upon selecting type \(i\), its collection indicator is independently **refreshed**: it is set to one with probability \(q=1-p\) and zero with probability \(p\), with \(0\le p<1\). All other indicators remain unchanged. Start with every type absent. Let \(N_w\) be the first step at which all types are simultaneously present. Write \(w_S=\sum_{i\in S}w_i\) and \(r=p/q\).

**Theorem.** For \(0<z<1\), define \(s=(1-z)/z\). Then the exact probability generating function is
\[
\mathbb E z^{N_w}=\frac{\displaystyle\sum_{S\subseteq[m]}(-1)^{|S|}(s+w_S)^{-1}}{\displaystyle\sum_{S\subseteq[m]}r^{|S|}(s+w_S)^{-1}}.
\]
The empty subset contributes \(1/s\) to both sums. Further,
\[
\boxed{\mathbb E N_w=\sum_{\varnothing\ne S\subseteq[m]}
\frac{r^{|S|}-(-1)^{|S|}}{w_S}}
=\int_0^\infty\left[\prod_{i=1}^m(1+r e^{-w_i t})-\prod_{i=1}^m(1-e^{-w_i t})\right]dt.
\]
The map \(w\mapsto\mathbb E N_w\) is **strictly Schur-convex** on the open probability simplex: if \(u\) majorizes \(w\), then \(\mathbb E N_u\ge\mathbb E N_w\), with equality exactly when \(u\) is a permutation of \(w\). Consequently, uniform sampling is the unique minimizer up to permutation for every loss probability \(0\le p<1\). If any \(w_i=0\), the hitting time is infinite from the empty state.

At the uniform minimizer, the expected number of steps is explicitly
\[
\mathbb E N_{\mathrm{unif}}=m\sum_{k=1}^m\binom{m}{k}\frac{r^k-(-1)^k}{k}.
\]
For example, with two types and \(p=2/5\), probabilities \((1/2,1/2)\) give mean \(55/9\) while probabilities \((1/5,4/5)\) give mean \(355/36\).

## Assumptions and scope

Sampling is iid across discrete steps, the refresh coin is independent of sampling and of all earlier coins, the loss probability is the same for all coupon types, and completion is the **first** all-present time (the all-present state need not be absorbing). We assume a known finite \(m\), strictly positive sampling weights, and \(q>0\). There is no monotone retention assumption. The generating-function identity holds for \(0<z<1\); its values elsewhere are determined by analytic continuation where defined, but no larger domain is required here.

## Proof

**1. Finiteness and Poissonization.** From any starting configuration, the event that the next \(m\) steps select types \(1,2,\ldots,m\) in that order and each refresh is successful has probability \(q^m\prod_i w_i>0\). Thus the first all-present time has a geometric-block upper tail and finite expectation. Insert independent rate-one exponential waiting times between discrete updates. By independent Poisson thinning, type \(i\) is refreshed at the epochs of an independent rate-\(w_i\) Poisson process. The resulting coordinate processes are independent, with stationary success probability \(q\). If \(\tau\) denotes the continuous-time first all-present time, then, conditionally on \(N_w\), it is the sum of \(N_w\) iid unit-rate exponential waits. Consequently \(\mathbb E e^{-s\tau}=\mathbb E(1+s)^{-N_w}\), and \(\mathbb E\tau=\mathbb E N_w\).

**2. Two transition probabilities.** Starting from all zeroes, a coordinate has received a refresh by time \(t\) with probability \(1-e^{-w_i t}\), and the most recent refresh succeeds with probability \(q\). Independence therefore gives
\[
P_{\mathbf0}(X_t=\mathbf1)=q^m\prod_i(1-e^{-w_i t}).
\]
Starting from all ones, coordinate \(i\) is present at time \(t\) with probability \(q+p e^{-w_i t}\), giving
\[
P_{\mathbf1}(X_t=\mathbf1)=q^m\prod_i(1+r e^{-w_i t}).
\]

**3. Hitting transform.** By the strong Markov property applied to the first all-present time, for every \(t\ge0\),
\[
P_{\mathbf0}(X_t=\mathbf1)
=\int_{[0,t]}P_{\mathbf1}(X_{t-v}=\mathbf1)\,\Pr(\tau\in dv).
\]
Taking Laplace transforms in \(t\), dividing the two resolvents, and expanding the finite products yields
\[
\mathbb E e^{-s\tau}=
\frac{\sum_{S\subseteq[m]}(-1)^{|S|}/(s+w_S)}
{\sum_{S\subseteq[m]}r^{|S|}/(s+w_S)},\qquad s>0.
\]
The denominator is positive because it is the Laplace transform of a positive transition probability (with the harmless factor \(q^m\) removed). Substitution \(z=1/(1+s)\) proves the stated discrete-time generating function.

**4. Expected first hit.** Let \(A(s)\) and \(B(s)\) denote the numerator and denominator above. Their expansions as \(s\downarrow0\) have form \(A(s)=s^{-1}+a+O(s)\) and \(B(s)=s^{-1}+b+O(s)\), where
\[
a=\sum_{\varnothing\ne S}(-1)^{|S|}/w_S,
\qquad b=\sum_{\varnothing\ne S}r^{|S|}/w_S.
\]
Hence \(A(s)/B(s)=1+(a-b)s+O(s^2)\). Since the expectation is finite, \(-\frac{d}{ds}\mathbb E e^{-s\tau}|_{s=0}=\mathbb E\tau=b-a\). This gives the subset formula. Each reciprocal \(1/w_S\) is the integral of \(e^{-w_S t}\) over \(t\in[0,\infty)\); expanding the finite products proves the integral formula. Its integrand is nonnegative (indeed the first product is at least one, the second is at most one) and decays exponentially because every \(w_i>0\).

**5. Strict majorization.** Fix \(t>0\). For \(r>0\), direct differentiation gives
\[
\frac{d^2}{dx^2}\log(1+r e^{-tx})
=\frac{t^2 r e^{-tx}}{(1+r e^{-tx})^2}>0,
\]
whereas
\[
\frac{d^2}{dx^2}\log(1-e^{-tx})
=-\frac{t^2e^{tx}}{(e^{tx}-1)^2}<0\qquad(x>0).
\]
Thus Karamata's majorization inequality shows that \(\prod_i(1+r e^{-w_i t})\) is Schur-convex (constant if \(r=0\)), while \(\prod_i(1-e^{-w_i t})\) is **strictly** Schur-concave on positive weights. Their difference is strictly Schur-convex, with strictness whenever the two weight vectors are not permutations. Integrating the pointwise strict inequality over \(t>0\) proves the theorem. The uniform vector is majorized by every probability vector. If \(w_i=0\), the initially absent type \(i\) can never be present, so \(N_w=\infty\).

## Verification

A self-contained standard-library Python checker (`check.py`) implements the subset and resolvent formulas with exact rational numbers, constructs the absorbing finite-state transition matrix, solves its linear systems exactly, and compares both the mean and generating function. It checks seven representative input cases including the zero-loss boundary, five-type systems, three generating-function arguments for each of six small cases, and a grid of strict balancing comparisons. Execution command: `python3 check.py`. The observed result was `PASS: 207 exact rational checks; full matrix mean/PGF, sample strict minimizers.` The universal theorem rests on the arguments above, not on those finite diagnostics.

## Relationship to prior work

Aggarwal and Garoni (2025) introduced the clumsy coupon collector. Attrill and Garoni (2026, arXiv:2605.14206v1) develop a generating-function analysis and limit laws for **uniformly** selected coupon types. Long (2026, arXiv:2605.14511v1), in particular Section 4, treats the uniform selected-type refresh chain and obtains fixed-loss hitting-time asymptotics; its Section 3.6 has heterogeneous weights for a **different global-reset** coupon model. Anceaume, Busnel, Schulte-Geers and Sericola (arXiv:1504.03878) establish sampling-weight optimization for the **monotone** coupon collector. Neither uniform-only clumsy formulas, nonuniform global reset, nor monotone collection imply the stated nonuniform selected-type first-passage formula together with strict balancing for positive loss probability. The underlying techniques—Poisson thinning, strong-Markov renewal identities and Karamata's inequality—are classical; priority beyond inspected material remains open to independent verification.

## Limitations

The theorem is an exact finite-dimensional statement, not an asymptotic law as the number of types grows. It assumes one type is refreshed per draw, iid fixed scan weights, and a common refresh success probability. It does not establish a stochastic ordering of the entire completion-time distributions, nor optimality with heterogeneous loss rates, adaptive sampling or global simultaneous loss. The initiating Aggarwal–Garoni three-page note was inspected in full and treats uniformly sampled types. Parts of the later Attrill–Garoni manuscript could not be completely re-inspected; a prior general first-passage theorem for biased product chains might subsume some conclusions. Independent priority assessment remains outstanding.

## References

1. S. Aggarwal and T. M. Garoni, *The Clumsy Coupon Collector*, in *2023 MATRIX Annals*, 2025, DOI:10.1007/978-3-031-76738-8_32. Full author note: https://www.matrix-inst.org.au/wp_Matrix2016/wp-content/uploads/2023/Garoni.pdf.
2. L. J. Attrill and T. M. Garoni, *The clumsy coupon collector's problem*, arXiv:2605.14206v1 (first public 2026-05-14), https://arxiv.org/abs/2605.14206.
3. C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors*, arXiv:2605.14511v1 (2026), https://arxiv.org/abs/2605.14511.
4. E. Anceaume, Y. Busnel, E. Schulte-Geers and B. Sericola, *Optimization results for a generalized coupon collector problem*, arXiv:1504.03878 (2015), https://arxiv.org/abs/1504.03878.
5. C. Zhang, *Formulas for Hitting Times and Cover Times for Random Walks on Groups*, arXiv:2302.01963 (2023), https://arxiv.org/abs/2302.01963 (possible specialization at symmetric refresh).
