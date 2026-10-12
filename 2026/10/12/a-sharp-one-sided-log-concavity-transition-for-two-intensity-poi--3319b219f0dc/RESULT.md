# A sharp one-sided log-concavity transition for two-intensity Poisson mixtures

## Finding

A mixture of two distinct Poisson laws has a **single, explicit critical weight** for global probability-mass log-concavity. Surprisingly, adding an arbitrarily small but positive amount of the *higher*-intensity law to the lower-intensity Poisson law eventually destroys log-concavity, although the pure lower-intensity law is strictly log-concave. On the other side of the critical weight, every mass inequality is satisfied. When log-concavity fails, the violating indices form exactly one nonempty finite consecutive block.

Here is the sharp statement. Let \(0<a<b\) be finite, let \(0<w<1\), and define
\[
 p_k=(1-w)e^{-a}\frac{a^k}{k!}+w e^{-b}\frac{b^k}{k!},\qquad k=0,1,2,\ldots.
\]
Put
\[
 d=\log(b/a),\qquad C=\frac{(b-a)^2}{ab},\qquad
 r=\frac4C,\qquad K=\lfloor r\rfloor+1,
\]
and define the explicit positive threshold
\[
 \theta_*=\left(\frac ab\right)^K
 \left(\frac{KC}{2}-1+\sqrt{\left(\frac{KC}{2}-1\right)^2-1}\right),
 \qquad
 w_*=\frac{e^{b-a}\theta_*}{1+e^{b-a}\theta_*}.
\]
Then \(0<w_*<1\), and
\[
 \boxed{p_k^2\ge p_{k-1}p_{k+1}\ \text{for every integer }k\ge1
 \quad\Longleftrightarrow\quad w\ge w_*}\qquad (0<w<1).
\]
For \(0<w<w_*\), the set of integers satisfying the strictly reversed inequality is a nonempty finite interval of consecutive integers. At \(w=w_*\), equality occurs at \(k=K\); if \(r\) is an integer, equality also occurs at \(k=r\), and there are no other equality indices. For \(w>w_*\), all inequalities are strict. The endpoint \(w=0\), excluded from the displayed equivalence, is itself a strictly log-concave Poisson law; \(w=1\) is likewise strictly log-concave.

In the concrete two-rate model \(a=1,b=2\), the result specializes to
\[
 \boxed{w_*=\frac{e}{256+e}},\qquad K=9,\qquad r=8.
\]
At this exact weight there are equalities at indices \(8\) and \(9\). The lower-intensity pure model and every mixture with \(w\ge e/(256+e)\) are log-concave, but **every** mixture with \(0<w<e/(256+e)\) is not.

## Assumptions and scope

All logarithms are natural. Log-concavity refers to the global discrete condition \(p_k^2\ge p_{k-1}p_{k+1}\) at every \(k\ge1\); it is not a claim about the modes, likelihood geometry, ultra-log-concavity, or the tail ratio alone. The parameters \(a,b\) are fixed positive real numbers with \(a<b\); \(w\) is the probability of selecting the higher-intensity component. No separation, integrality, or large-sample assumption is imposed on the intensities. All probability masses are strictly positive.

For \(0<w<1\), set \(A=(1-w)e^{-a}\), \(B=we^{-b}\), \(q_k=Aa^k+Bb^k\), and \(\theta=B/A=(w/(1-w))e^{-(b-a)}\). The proof works with these positive quantities and takes no limiting approximation to establish the threshold.

## Proof

**1. An exact curvature factorization.** Since \(p_k=q_k/k!\), elementary expansion gives
\[
 q_{k-1}q_{k+1}=q_k^2+AB(ab)^{k-1}(b-a)^2.
\]
Consequently, for every integer \(k\ge1\),
\[
 \begin{aligned}
 \mathcal D_k&:=(k+1)(k!)^2\bigl(p_k^2-p_{k-1}p_{k+1}\bigr)\\
 &=(k+1)q_k^2-kq_{k-1}q_{k+1}\\
 &=q_k^2-kAB(ab)^{k-1}(b-a)^2.
 \end{aligned}
\]
Divide by the positive quantity \(AB(ab)^k\), and put \(\eta=\log\theta\). The resulting exact sign identity is
\[
 \frac{\mathcal D_k}{AB(ab)^k}
 =\frac{(1+e^{\eta+kd})^2}{e^{\eta+kd}}-kC
 =2+2\cosh(\eta+kd)-kC.
\]
In particular, a strict failure is impossible if \(k\le r=4/C\), because \(2+2\cosh(u)\ge4\) for all real \(u\).

**2. The intervals of failure overlap and have decreasing right endpoints.** For real \(x>r\), let
\[
 W(x)=\operatorname{arcosh}\!\left(\frac{xC}{2}-1\right).
\]
For each integer \(k>r\), the factorization implies
\[
 \mathcal D_k<0
 \quad\Longleftrightarrow\quad
 \eta\in I_k:=(-kd-W(k),\,-kd+W(k)).
\]
The function \(W\) extends continuously to \(r\) with \(W(r)=0\), and the identity
\(C=4\sinh^2(d/2)\) gives
\[
 W(r+1)=\operatorname{arcosh}(1+C/2)=d.
\]
Direct differentiation for \(x>r\) yields
\[
 W'(x)=\frac1{\sqrt{x(x-r)}},\qquad
 W''(x)=-\frac{2x-r}{2[x(x-r)]^{3/2}}<0.
\]
Thus \(W\) is strictly increasing and strictly concave. For every integer \(k>r\), the unit forward increment satisfies
\[
 W(k+1)-W(k)<W(r+1)-W(r)=d.
\]
It follows that the right endpoints \(-kd+W(k)\) decrease strictly for \(k=K,K+1,\ldots\). In addition, since \(W(k+1)>W(r+1)=d\) for \(k\ge K\), the intervals \(I_k\) and \(I_{k+1}\) overlap: the right endpoint of \(I_{k+1}\) is greater than the left endpoint of \(I_k\). Finally, their left endpoints tend to minus infinity, because \(W(k)=O(\log k)\).

The union of all strict-failure intervals is therefore **exactly**
\[
 \bigcup_{k\ge K} I_k=(-\infty,-Kd+W(K)).
\]
Hence all discrete log-concavity inequalities hold if and only if
\(\eta\ge-Kd+W(K)\), or equivalently
\[
 \theta\ge \theta_*=e^{-Kd+W(K)}.
\]
Using \(e^{\operatorname{arcosh}z}=z+\sqrt{z^2-1}\) produces the stated explicit expression for \(\theta_*\). The relation between \(\theta\) and \(w\) is strictly increasing and rearranges to
\(w=e^{b-a}\theta/(1+e^{b-a}\theta)\), giving the claimed sharp weight threshold.

**3. One finite block of failing indices.** For a fixed \(\eta\), define the real-variable function
\[
 H(x)=2+2\cosh(\eta+xd)-xC,\qquad x\ge0.
\]
Its second derivative is \(H''(x)=2d^2\cosh(\eta+xd)>0\). Also \(H(0)>0\) and \(H(x)\to+\infty\) as \(x\to\infty\). Therefore the negative set of \(H\), when nonempty, is one bounded real interval. Its integer points are consecutive. For every \(0<w<w_*\), Step 2 supplies at least one such integer, proving the nonempty finite-block assertion.

**4. Equality and pure-component boundaries.** At \(\eta=-Kd+W(K)\), equality holds at \(k=K\) by construction. No integer \(k>K\) can give equality because its right interval endpoint is strictly smaller. For \(k<r\), the normalized curvature is strictly positive. If \(r\) is not an integer, these exhaust the cases. If \(r\) is an integer, then \(K=r+1\), \(W(K)=d\) and \(\eta=-rd\), so the index \(k=r\) also has \(H(r)=4-rC=0\). These are the only boundary equalities. When \(w>w_*\), all curvatures are strictly positive, including any index with \(k=r\). At \(w=0\) or \(w=1\), the law is Poisson with a single positive intensity, so its curvatures are strictly positive.

**5. Nonuniformity of the zero-contamination limit.** For each fixed \(k\ge1\), the curvature \(p_k^2-p_{k-1}p_{k+1}\) is continuous in \(w\) and strictly positive at \(w=0\). Consequently, as \(w\downarrow0\), every fixed finite set of indices eventually satisfies strict log-concavity. Yet every sufficiently small positive \(w\) lies below \(w_*\) and has a violation somewhere. Thus the first violating index tends to infinity as \(w\downarrow0\), establishing that the loss of global log-concavity occurs at increasingly remote tail positions.

## Verification

The standalone script `verify.py` uses only the Python standard library. Run `python verify.py` in the directory containing the script. It checks the exact curvature factorization on 2,240 rational/integer configurations, checks the exact boundary equalities for four explicit parameter choices, and checks additional below-threshold contiguous-failure diagnostics and sample threshold inequalities. It does not attempt to certify the universal statements by finite enumeration. The analytic argument above provides the proof for all positive real intensities, mixing weights, and indices.

As exact illustrative certificates, at \((a,b)=(1,2)\), the critical condition \(B/A=1/256\) yields unnormalized masses \(q_k=256+2^k\), for which the curvature numerator vanishes at \(k=8,9\). At \((a,b)=(1,4)\), the critical condition \(B/A=1/8\) yields \(q_k=8+4^k\), with a unique zero at \(k=2\).

## Relationship to prior work

Valiquette, Toulemonde, Peyhardi, Marchand and Mortier (2023; earliest preprint May 26, 2023) study the behavior of Poisson mixtures under varying intensity-tail classes. Their Theorem 1 concerns ratios of discrete tails, while Theorem 2 and Corollary 1 address a continuous bounded-intensity mixing class. These statements do not give global discrete log-concavity or a weight threshold for a **two-atomic** mixing law. The present theorem addresses that different exact-shape question and is compatible with Poisson-like eventual tails.

Puig (2024), Section 3.2, presents weighted-Poisson models and sufficient conditions for overdispersion or underdispersion based on curvature of the weight function. A two-rate Poisson mixture can be represented by a sum-of-exponentials weight, but that dispersion criterion does not imply the sharp mass-log-concavity classification here. Karlis and Xekalaki (2005) provide a broad historical review of mixed-Poisson distributions. Only its accessible abstract and bibliography could be inspected; the complete review has not been excluded as an earlier source of a related identity.

A foundational undated manuscript by Le Cam, *Mixtures of Poisson Distributions. I. Some Simple Cases*, was also sampled at its introduction, identifiability discussion and statistical-testing statements (pp. 1, 4, 8, 12, 21 and 31). Those examined pages address different problems. The manuscript was not inspected in full, so it remains an additional historical priority risk.

The key additions are the explicit one-sided mixing-weight phase boundary, the proof that all failing mass inequalities form one consecutive index block, the exact boundary-equality classification, and the discontinuity of global log-concavity under vanishing contamination. The derivation is elementary but requires combining a factorial curvature identity with the interval geometry of a strictly concave inverse-hyperbolic function. No assertion of independent priority verification is made.

## Limitations

The result is specific to exactly two distinct positive Poisson intensities and global ordinary discrete log-concavity. It gives neither a criterion for three or more intensity levels nor an exact enumeration of the failing integers for each subthreshold weight. It does not imply that the mixture is ultra-log-concave, underdispersed, unimodal only in a particular regime, or statistically identifiable from limited observations. The sharp cutoff is theoretical; estimating the mixture parameters from data is a separate inference problem.

Although dedicated searches did not identify a covering theorem, an earlier equivalent formulation under weighted-Poisson, strong-unimodality, or likelihood-ratio terminology remains possible, especially in literature not available in full text. Independent audit and historical priority confirmation have not been performed.

## References

1. S. Valiquette, G. Toulemonde, J. Peyhardi, É. Marchand and F. Mortier, *Asymptotic tail properties of Poisson mixture distributions*, arXiv:2305.17095 (first posted May 26, 2023); *Stat* (2023), DOI: 10.1002/sta4.622. Relevant: Theorems 1–2, Corollary 1 and Sections 2–4.
2. P. Puig, *Some mechanisms leading to underdispersion: Old and new proposals*, *Scandinavian Journal of Statistics* (2024), DOI: 10.1111/sjos.12677. Relevant: Section 3.2, Proposition 5.
3. D. Karlis and E. Xekalaki, *Mixed Poisson Distributions*, *International Statistical Review* **73** (2005), 35–58, DOI: 10.1111/j.1751-5823.2005.tb00250.x. Abstract/bibliography inspected; full text unavailable in this comparison.
4. L. Le Cam, *Mixtures of Poisson Distributions. I. Some Simple Cases*, undated manuscript in Berkeley collection of unpublished work, https://www.stat.berkeley.edu/~rice/LeCam/papers/poisson.pdf. Selected pages inspected; full manuscript not compared.
