# A sharp second-variance gap for fixed-weight binary digit-sum shifts

## Finding

Let \(s_2(n)\) count the ones in the binary expansion of a nonnegative integer. For each positive integer \(t\), let \(\mu_t\) be the limiting distribution of \(s_2(n+t)-s_2(n)\) as \(n\) runs through the nonnegative integers, and define the second moment \(V(t)=\sum_{z\in\mathbb Z}z^2\mu_t(z)\). This moment is finite and is the variance because the distribution has mean zero.

**Theorem (exact pair energy and isolated first two variance levels).** Write \(t=\sum_{r=1}^k2^{p_r}\) with \(0\le p_1<\cdots<p_k\) and \(k=s_2(t)\). Then

\[
V(t)=2k-2\sum_{1\le r<s\le k}2^{-(p_s-p_r)}.
\]

For every integer \(k\ge2\), among all positive integer shifts with \(s_2(t)=k\),

\[
\min V(t)=4-2^{2-k}.
\]

Equality holds exactly when \(t=2^a(2^k-1)\) for some integer \(a\ge0\), that is, precisely when all \(k\) one-bits form a single consecutive block. For **every other** shift of weight \(k\), the sharp strictly separated next level is

\[
V(t)\ge5-3\cdot2^{1-k}.
\]

Equality in this second inequality holds precisely when all gaps \(p_{r+1}-p_r\) equal one except for a single gap equal to two, located at either the left or right edge of the sequence of gaps. Equivalently, up to multiplication by a power of two, the equality shifts are \(2^{k+1}-3\) and \(2^{k+1}-1-2^{k-1}\) (these coincide for \(k=2\)). The **exact variance isolation gap** is \(1-2^{1-k}\). Also, \(\sup_{s_2(t)=k}V(t)=2k\), which is never attained for \(k\ge2\) but is approached as all consecutive one-bit spacings grow.

For \(k=1\), the variance is identically two; there is no second level. This theorem concerns the second moment, not the sign bias \(\mu_t(\mathbb Z_{\ge0})\).

## Assumptions and scope

All integer parameters and indices are exact. The binary positions \(p_1,\dots,p_k\) are arbitrary nonnegative integers; neither a bound on \(t\) nor a bound on its bit length is assumed. The distribution \(\mu_t\) is the classical digit-sum correlation measure, whose existence is established in the cited literature. Its second moment coincides with the Cesàro limit of the squared increments because binary carry-chain lengths have geometric tails. No assumption about generic or random choices of \(t\) is made.

## Proof

**1. The complete carry process.** Let \((X_i)_{i\ge0}\) be independent fair binary digits and let \(b_i\) denote the \(i\)-th binary digit of \(t\), with \(b_i=0\) above its most significant bit. Set \(c_0=0\) and \(c_{i+1}=\mathbf 1_{\{X_i+b_i+c_i\ge2\}}\). Let \(q_i=\mathbb E[c_i]\). Conditioning on the incoming carry yields

\[
\mathbb E[c_{i+1}\mid c_i]=\tfrac12 b_i+\tfrac12 c_i,
\qquad q_i=\sum_{j<i}b_j2^{-(i-j)}.
\]

All carries eventually cease almost surely: above the highest one-bit of \(t\), an existing carry persists only while independent digits equal one. Therefore \(C=\sum_{i\ge1}c_i\) is finite almost surely and has finite second moment. The digit sum changes by one for each one-bit added and decreases by one for each carry, so the limiting shift increment is \(k-C\).

Each given one-bit contributes exactly \(\sum_{h\ge1}2^{-h}=1\) to \(\sum_iq_i\). Consequently \(\mathbb E C=k\) and the limiting digit-sum increment is centered.

**2. Exact variance.** For \(j>i\), repeated conditional expectation gives \(\operatorname{Cov}(c_i,c_j)=2^{-(j-i)}q_i(1-q_i)\), since the difference between the two one-step conditional carry probabilities is \(1/2\), independently of the digit \(b_i\). Absolute convergence is guaranteed by the geometric tail. Hence

\[
\begin{aligned}
V(t)&=\operatorname{Var}(C)
=\sum_{i\ge1}\left(1+2\sum_{h\ge1}2^{-h}\right)q_i(1-q_i)\\
&=3\sum_{i\ge1}q_i(1-q_i).
\end{aligned}
\]

Direct summation gives

\[
\sum_{i\ge1}q_i=k,
\qquad
\sum_{i\ge1}q_i^2=\frac{k}{3}+\frac23\sum_{r<s}2^{-(p_s-p_r)}.
\]

This proves the pair-energy identity. Equivalently, the result is the exact variance \(\kappa_2(t)\) of the correlation measure studied by Spiegelhofer and Wallner. The carry construction identifies that measure with the limiting increment law and supplies the finite second moment. For sampling \(n\) uniformly from \(\{0,\ldots,2^M-1\}\), the first \(M\) bits couple exactly to \((X_i)\); the chance that the carry reaches column \(M\) is \(q_M\), and the conditional remaining carry run is geometrically distributed. This makes the squared-increment discrepancy tend to zero. Arbitrary Cesàro endpoints follow from the same finite-bit cylinder approximation and geometric-tail bound.

**3. First and second extremal levels.** Put \(d_i=p_{i+1}-p_i\ge1\) for \(1\le i<k\), and define the pair energy

\[
E(d_1,\ldots,d_{k-1})=\sum_{1\le r<s\le k}2^{-(d_r+\cdots+d_{s-1})}.
\]

Every term that spans \(d_i\) is strictly decreasing in that gap, so \(E\) strictly decreases whenever any \(d_i\) is increased. Thus its unique maximum over integer gap vectors is attained at \((1,\ldots,1)\). At this vector,

\[
E_{\mathrm{full}}=\sum_{h=1}^{k-1}(k-h)2^{-h}=k-2+2^{1-k}.
\]

Substituting into the variance identity gives the minimum \(4-2^{2-k}\) and its equality characterization.

To study all nonconsecutive patterns, choose any gap \(d_i\ge2\). By decreasing any other excess gap to one, and decreasing \(d_i\) to two, we can only **increase** the energy, with strict increase unless the original pattern already had exactly that single gap of size two. Hence the largest pair energy among nonconsecutive patterns occurs for exactly one gap of size two.

Inserting a single zero-gap between the \(i\)-th and \((i+1)\)-st one-bit of a previously consecutive block halves every pair contribution crossing that cut and leaves every other contribution unchanged. Its energy loss is

\[
D_i=(1-2^{-i})(1-2^{-(k-i)}),\qquad1\le i<k.
\]

Indeed, the crossing pair energy before insertion is \(2(1-2^{-i})(1-2^{-(k-i)})\). The quantity \(D_i=1+2^{-k}-2^{-i}-2^{-(k-i)}\) is smallest at \(i=1\) or \(i=k-1\), since the convex function \(2^{-x}+2^{-(k-x)}\) is largest at the endpoints of the integer interval \([1,k-1]\). The least loss is therefore

\[
D_{\min}=\tfrac12(1-2^{1-k}).
\]

Since \(V=2k-2E\), every nonconsecutive shift has variance at least \((4-2^{2-k})+2D_{\min}=5-3\cdot2^{1-k}\). The strict-compression argument proves the stated equality cases. Finally, \(E>0\) when \(k\ge2\) and \(E\to0\) when \(p_r=(r-1)M\) with \(M\to\infty\), establishing the strict supremum.

## Verification

Run `python3 cusick_verify.py` using only Python's standard library. It checks the pair-energy expression exactly against the independently published even/odd cumulant recursion for all shifts from one through 8191; independently enumerates all binary supports through eleven positions to verify the sharp first and second levels and equality cases; and samples ten shifts directly across 262144 consecutive integers each. The exact checks pass. The largest direct-sample second-moment discrepancy is about 0.00811, within the verifier's declared tolerance of 0.02. The finite samples are corroboration only; the unrestricted result follows from the proof above.

## Relationship to prior work

Cheng (2026, arXiv:2608.25899v1) determines the fixed-Hamming-weight extremum for the **sign bias** and explains why digit-block geometry matters. His first-exit paper (arXiv:2606.23398v1) studies positivity of the sign bias, not the second variance level.

Spiegelhofer and Wallner (2023, arXiv:2005.07167) define the second cumulant, establish its even/odd recursion and analyze it by the number of one-blocks. In particular, their recursion determines \(V(t)\) algorithmically. Tarłowski (2026, arXiv:2605.08624v1, Section 4.4) obtains sharp variance inequalities under **tree-word length** and block-count constraints. Its minimum at fixed word length yields the first fixed-Hamming-weight minimum after a change of parameters; accordingly, that first minimum is not claimed as the new contribution. Neither inspected theorem states the explicit one-bit-pair energy or the sharp, isolated **second** variance level for every Hamming weight with equality patterns.

Sobolewski and Spiegelhofer (arXiv:2411.07779v2, Sections 1–3) give a correlation-measure decomposition and further low-block analyses, rather than the exact second-level fixed-weight extremum. The relationship is therefore a refinement of known cumulant recursions, with a discrete variance-gap classification, not a new proof of the sign-bias conjecture.

## Limitations

This is a theorem about second moments only: it does not furnish a new lower bound for the sign-bias probability or compute higher cumulants. The explicit variance formula is equivalent to an iterated evaluation of a previously known recurrence; priority of the **second-minimum gap and exact rigidity cases**, rather than the original definition or recurrence, is the central originality claim. A stronger older extremal theorem could subsume it; independent priority assessment has not been performed. Numerical tests are finite; their error tolerances are not bounds on the unrestricted theorem.

## References

1. K. Cheng, *Sharp extremal asymptotics for Cusick's sum-of-digits bias at fixed Hamming weight*, arXiv:2608.25899v1 (public 2026-08-26), https://arxiv.org/abs/2608.25899.
2. K. Cheng, *A first-exit proof of Cusick's sum-of-digits conjecture*, arXiv:2606.23398v1 (public 2026-06-22), https://arxiv.org/abs/2606.23398.
3. L. Spiegelhofer and M. Wallner, *The binary digits of n+t*, Ann. Sc. Norm. Super. Pisa 24 (2023), 1–31, arXiv:2005.07167, https://arxiv.org/abs/2005.07167.
4. D. Tarłowski, *The martingale evolution of probability measures defined via the sum-of-digits functions*, arXiv:2605.08624 (public 2026-05-09), https://arxiv.org/abs/2605.08624.
5. B. Sobolewski and L. Spiegelhofer, *Decomposing the sum-of-digits correlation measure*, arXiv:2411.07779 (public 2024-11-12), https://arxiv.org/abs/2411.07779.
