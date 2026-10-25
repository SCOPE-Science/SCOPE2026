# The two-reversal singleton-correlation window in a symmetric reinforced urn

## Finding

Start with one ball of each of \(q\ge3\) colors. At each of \(n\ge2\) successive draws, replace the selected ball and add another ball of the same color. For two distinct specified colors, let \(I_i=\mathbf1_{\{N_i=1\}}\), where \(N_i\) is the number of occurrences among these \(n\) draws. Let \(C_q(n)=\operatorname{Cov}(I_1,I_2)\).

Define the cubic
\[
F_q(x)=x^3-(q+1)x^2-(q^2-4q+2)x+(q-1)(q-2)^2.
\]
Then, for all integers \(q\ge3\) and \(n\ge2\),
\[
C_q(n)=-\frac{n(q-1)F_q(n)}{(n+q-4)(n+q-3)(n+q-2)^2(n+q-1)^2}.
\]
The polynomial \(F_q\) has exactly one negative zero and exactly two distinct positive zeros \(a_q<q<b_q\). Consequently \(C_q(n)>0\) exactly for \(a_q<n<b_q\), equals zero only at integer endpoints, and is negative otherwise. For \(q\ge5\), as the integer sample size increases from \(n=2\), covariance changes from negative to positive and back to negative (with a possible zero at a crossing). For \(q=3,4\), it starts positive instead.

The transition endpoints have the sharp location
\[
a_q=q-\sqrt q-\frac34+O(q^{-1/2}),\qquad b_q=q+\sqrt q-\frac34+O(q^{-1/2}).
\]
For every fixed real \(s\), with \(n_q=q+\lfloor s\sqrt q\rfloor\),
\[
\lim_{q\to\infty}q^2 C_q(n_q)=\frac{1-s^2}{32}.
\]
This is a **finite-size critical window**: away from occupancy density one, for every fixed \(\lambda>0\) with \(\lambda\ne1\),
\[
\lim_{q\to\infty}q C_q(\lfloor\lambda q\rfloor)=-\frac{\lambda(\lambda-1)^2}{(1+\lambda)^5}<0.
\]
Thus the positive covariance island is only \(O(\sqrt q)\) wide, where a leading negative dependence term vanishes.

## Assumptions and scope

The number of colors \(q\) is an arbitrary fixed integer at least three for the exact results and varies to infinity in the stated asymptotics. The initial urn has exactly one ball per color; each reinforcement adds **one** same-colored ball. The indicators record the number of draws, not the number of balls presently in the urn. A pair of different, fixed colors is considered. The asymptotic formulas have \(s\) and \(\lambda\) fixed, with integer horizons defined by the displayed floors. The positive roots are zeros of the continuous polynomial, and the covariance sign assertion applies only to integer sample sizes \(n\ge2\).

## Proof

**Uniform weak-composition law.** An ordered draw-color sequence with cell counts \((x_1,\ldots,x_q)\) has probability \(\prod_i x_i!/(q)^{\overline n}\), where \((q)^{\overline n}=q(q+1)\cdots(q+n-1)\). Summing over its \(n!/\prod_i x_i!\) orderings gives the constant mass \(n!/(q)^{\overline n}=1/\binom{n+q-1}{q-1}\) for every weak composition of \(n\) into \(q\) labeled components. This is the standard Dirichlet–multinomial law with all concentration parameters one.

**Exact indicator covariance.** Fixing \(N_1=1\) leaves a weak composition of \(n-1\) into \(q-1\) parts; fixing \(N_1=N_2=1\) leaves a weak composition of \(n-2\) into \(q-2\) parts. Stars and bars therefore gives
\[
p_1=\Pr(N_1=1)=\frac{(q-1)n}{(n+q-1)(n+q-2)},
\]
\[
p_{11}=\Pr(N_1=N_2=1)=\frac{(q-1)(q-2)n(n-1)}{(n+q-1)(n+q-2)(n+q-3)(n+q-4)}.
\]
The expression for \(C_q(n)=p_{11}-p_1^2\) reduces by common-denominator multiplication to the displayed cubic formula; its denominator and the prefactor \(n(q-1)\) are strictly positive for the specified domain.

**Exactly two positive roots.** The exact signs are \(F_q(0)=(q-1)(q-2)^2>0\) and \(F_q(q)=-2(q-1)(q-2)<0\). As \(x\to-\infty\), the monic cubic tends to \(-\infty\), and as \(x\to+\infty\) it tends to \(+\infty\). The intermediate value theorem gives one root in each disjoint interval \(( -\infty,0)\), \((0,q)\), and \((q,\infty)\). A cubic has no other roots; hence all three are simple. Its sign alternates across these roots, proving the covariance sign classification. Moreover \(F_q(2)=(q-2)(q^2-5q+2)\), which is negative at \(q=3,4\) and positive at every integer \(q\ge5\). Since \(n=q\) is positive and all large horizons have negative covariance, the asserted discrete reversal regimes follow.

**Location of the critical roots.** Set \(x=q+\delta\). Direct expansion yields
\[
F_q(q+\delta)=2q\delta^2-2q^2+\delta^3+2q\delta-\delta^2+6q-2\delta-4.
\]
For \(\delta=d\sqrt q\), the leading term is \(2(d^2-1)q^2\); the positive roots therefore lie at \(d=-1+o(1)\) and \(d=1+o(1)\). More quantitatively, the cubic evaluated at \(\delta=\pm\sqrt q+c\) has order-\(q^{3/2}\) coefficient \(\pm(4c+3)\), while its derivative at either of these points is \(\pm4q^{3/2}+O(q)\). Bracketing at \(c=-3/4\pm Bq^{-1/2}\), with sufficiently large fixed \(B\), proves there is a unique root at \(\delta=\pm\sqrt q-3/4+O(q^{-1/2})\).

**Signed finite-size scaling.** Put \(n=q+\lfloor s\sqrt q\rfloor\). The above identity implies \(F_q(n)=2(s^2-1)q^2+O(q^{3/2})\) for each fixed \(s\). The numerator prefactor \(n(q-1)=q^2+O(q^{3/2})\), and the denominator is \(64q^6(1+O(q^{-1/2}))\). Division gives the stated limit. For \(n=\lfloor\lambda q\rfloor\), \(F_q(n)=(\lambda-1)^2(\lambda+1)q^3+O(q^2)\), which gives the fixed-density negative limit. Neither finite enumeration nor the fixed-density limit alone proves the all-size sign theorem; that theorem follows from the exact cubic.

## Verification

Run `python3 verify.py` with standard Python. It enumerates every weak composition in 116 parameter cases (373,343 outcomes total) and independently compares the frequency of one or two singleton colors against the displayed rational expressions. It also checks polynomial signs for 997 further color counts and verifies the predicted scaled limit numerically at four large sizes. The enumerations are finite diagnostics; the proof above supplies the all-size classification and asymptotics.

## Relationship to prior work

Chen's 1981 work and Keener and Wu's 2006 work treat occupancy profiles under symmetric Dirichlet–multinomial/Bose–Einstein sampling; the uniform composition law and generic occupancy moment framework are classical and are not claimed here. In particular, Keener and Wu give a central limit theorem for aggregate occupancy statistics and a first-order approximation to finite-coordinate joint distributions with an error of order \(q^{-2}\). Their displayed approximation does not determine the **sign of the order-\(q^{-2}\) singleton-pair covariance at critical density**. Eaton, Godbole and Sinclair study different independent-draw occupancy statistics and Poisson approximations, not the reinforced critical window. The contribution here is the exact two-reversal phase classification for the reinforced model, with its cubic root locations and the critical sign profile.

## Limitations

The result assumes one initial ball and unit reinforcement, not arbitrary Dirichlet concentration or unequal initial weights. It concerns two specified singleton-color indicators, not the entire vector of occupancy-frequency counts. The scaled limiting covariance vanishes at \(s=\pm1\), so that limit alone does not decide the sign on the exact boundary; the finite-root formula does. Earlier equivalent results, especially in the historical Pólya/Bose–Einstein occupancy literature, remain possible; the original full text of a relevant 1981 article was not available for complete comparison.

## References

- W.-C. Chen, *Limit theorems for general size distributions*, Journal of Applied Probability **18** (1981), 139–147. DOI: 10.2307/3213174. Abstract and publisher record: https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/limit-theorems-for-general-size-distributions/C1152C0E3104F15E9430084C54BFD0DF.
- R. W. Keener and W. B. Wu, *On Dirichlet Multinomial Distributions*, (2006). DOI: 10.1142/9789812772558_0008. Author-hosted full text: https://www.stat.uchicago.edu/~wbwu/papers/keener.pdf.
- J. Eaton, A. P. Godbole and B. Sinclair, *Competition between Discrete Random Variables, with Applications to Occupancy Problems*, arXiv:0806.1007v1, first posted 2008-06-05. https://arxiv.org/abs/0806.1007.
