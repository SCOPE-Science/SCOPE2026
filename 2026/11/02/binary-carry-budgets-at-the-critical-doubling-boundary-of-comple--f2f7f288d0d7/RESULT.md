# Binary-carry budgets at the critical doubling boundary of complete sequences

## Finding
Let \(S=(s_n)_{n\ge1}\) be any strictly increasing sequence of positive integers for which \(s_{n+1}=2s_n\) whenever \(n\ge N\), for some fixed \(N\ge1\). For \(\alpha>0\), put
\[
a_n(\alpha)=\lfloor\alpha s_n\rfloor,\qquad H_j(\alpha)=1+\sum_{i<j}a_i(\alpha)-a_j(\alpha),
\]
and let \(V_S\) denote the set of scales for which every nonnegative integer is a sum of distinct indexed terms of \((a_n(\alpha))\). Write \(\operatorname{wt}_2(u)\) for the number of ones in the ordinary binary expansion of a nonnegative integer \(u\).

**Exact classification.** A scale \(\alpha>0\) lies in \(V_S\) if and only if the finite inequalities \(H_j(\alpha)\ge0\) hold for \(1\le j\le N\), and the fractional part of \(y=\alpha s_N\) is a dyadic rational \(u/2^k\), with \(0\le u<2^k\), whose binary weight satisfies
\[
\operatorname{wt}_2(u)\le H_N(\alpha).
\]
The choice of a nonminimal denominator \(2^k\) does not change this weight. In particular, every admissible scale is rational; \(V_S\) is countable, and \(V_S\cap[0,B]\) has upper box-counting dimension zero for every fixed \(B>0\).

**Sharp, unbounded logarithmic complexity.** For each \(m\ge2\), take
\[
S^{(m)}=(2,3,\ldots,2m,4m,8m,\ldots),\quad N=2m-1,
\]
and restrict \(\alpha\) to \(I_m=[1/2,1/2+1/(8m))\). Put \(h=(m-1)^2\). For every integer \(L\ge2\), the exact number of scales in \(V_{S^{(m)}}\cap I_m\) with \(2m\alpha=m+u/2^L\), \(u\) an integer, is
\[
\boxed{\sum_{j=0}^{\min(h,L-2)}\binom{L-2}{j}.}
\]
For fixed \(m\) this equals \(L^h/h!+O_m(L^{h-1})\) as \(L\to\infty\). Thus no uniform bound on the degree of logarithmic scale-counting growth is possible across eventually doubling sequences, even though every such parameter set has box dimension zero.

For the pure geometric family \(s_n=m2^{n-1}\) (\(m\ge1\)), the classification specializes to \(V_S=\{1/(m2^j):j\ge0\}\).

## Assumptions and scope
The sequence \(S\) is indexed, strictly increasing, and positive. Subset sums use each index at most once; equal floor values at distinct indices remain distinct available summands. Zero floor values are permitted. We call this property **full subset-sum coverage** (including zero), explicitly distinguishing it from eventual completeness (all sufficiently large integers) and deletion-stable strong completeness. No doubling condition is imposed before index \(N\). The box dimension assertion is local on bounded intervals, not a claim about a single global covering number on the unbounded parameter domain.

## Proof
**1. Subset-sum criterion.** Let \((b_n)\) be any nondecreasing nonnegative integer sequence tending to infinity. Its subset sums fill \(\mathbb Z_{\ge0}\) if and only if
\[
b_j\le1+\sum_{i<j}b_i\qquad(j\ge1).
\]
Indeed, if an inequality fails, the integer \(1+\sum_{i<j}b_i\) is too large to use only earlier terms, and is smaller than every later term. Conversely, induction shows that the first \(j\) terms fill the entire integer interval from zero to their sum whenever all \(j\) inequalities hold. Their sums are unbounded. This extends the usual Brown criterion to initial zero terms without changing its proof. Apply this with \(b_n=a_n(\alpha)\), which is nondecreasing and unbounded.

**2. Exact binary-carry budget.** For \(n\ge N\), the doubling identity gives
\[
a_{n+1}(\alpha)=2a_n(\alpha)+\varepsilon_n,
\qquad \varepsilon_n=\lfloor2\{\alpha s_n\}\rfloor\in\{0,1\}.
\]
Consequently
\[
H_{n+1}(\alpha)=H_n(\alpha)-\varepsilon_n,
\qquad H_{N+r}=H_N-\sum_{j=0}^{r-1}\varepsilon_{N+j}.
\]
The carries \(\varepsilon_N,\varepsilon_{N+1},\ldots\) are exactly the digits of the *terminating-choice* binary expansion of \(\{\alpha s_N\}\): repeated doubling and taking integer parts extracts these digits. If \(\alpha s_N\) is not dyadic, its binary expansion has infinitely many ones (a binary expansion with finitely many ones is a dyadic rational). If it is dyadic, the digits eventually vanish and their total number is \(\operatorname{wt}_2(u)\). Therefore all the infinitely many inequalities \(H_n\ge0\) for \(n\ge N\) hold if and only if \(\alpha s_N\) is dyadic and the total number of its binary ones is at most \(H_N\). Combining with the finitely many preceding inequalities proves the classification.

**3. Zero local upper box dimension.** Fix \(B>0\). When \(0<\alpha\le B\), every \(H_N(\alpha)\) is bounded above by the finite integer
\[
K_B=1+\sum_{i<N}\lfloor B s_i\rfloor.
\]
There are at most \(\lfloor Bs_N\rfloor+2\) choices of integer-part unit interval for \(\alpha s_N\). At binary resolution \(2^{-L}\), at most \(\sum_{j=0}^{\min(K_B,L)}\binom Lj\) binary-prefix cylinders are possible per interval, since an admissible fractional part has at most \(K_B\) one-bits. Rescaling by \(s_N\), these give a cover by at most
\[
(\lfloor Bs_N\rfloor+2)\sum_{j=0}^{\min(K_B,L)}\binom Lj=O_{S,B}(L^{K_B})
\]
intervals of length \(1/(s_N2^L)\). Hence the local upper box dimension is zero. Countability follows independently from the dyadic parameterization.

**4. Exact strata and sharpness.** For \(S^{(m)}\), at \(\alpha\in I_m\) each \(2\le k\le2m\) satisfies \(\lfloor\alpha k\rfloor=\lfloor k/2\rfloor\), because the additional amount over \(k/2\) is strictly less than \(1/4\). These first \(N=2m-1\) integers satisfy Brown's inequalities: their floor values are nondecreasing by increments at most one, begin at one, and the accumulated sum is at least the next value minus one. A direct sum of the first \(N\) values yields
\[
H_N=1+\sum_{k=2}^{2m-1}\lfloor k/2\rfloor-m
=1+(m^2-m)-m=(m-1)^2=h.
\]
Also \(2m\alpha=m+t\) with \(0\le t<1/4\), so in a terminating binary expansion of length at most \(L\) the first two fractional digits vanish. There are exactly \(\binom{L-2}{j}\) choices with \(j\) ones among the remaining \(L-2\) positions. The carry budget permits precisely \(j\le h\), proving the displayed exact count. The asymptotic follows by taking the highest-degree binomial term for fixed \(h\). For \(N=1\) and \(s_n=m2^{n-1}\), the prefix inequality and the carry budget force the binary expansion of \(\alpha m\) to have a single one in its complete (integer plus fractional) expansion; equivalently \(\alpha m=2^{-j}\), proving the pure geometric subcase.

## Verification
Run the standalone Python 3 file `verify.py`. It uses integer division, exact fractions, binary popcounts and binomial coefficients. It checks the explicit stratum counts and Brown inequalities for multiple \(m,L\) combinations and separately compares the classification with long finite Brown tests on varied prefixes and with the pure-geometric formula. The program reports

`VERIFY_OK stratum_cases=110 stratum_points=11253 arbitrary_prefix_tests=94535 pure_geometric_tests=859740 exact_integer_rational=yes`

The finite computations do not establish the infinite theorem. In particular, the infinite-tail claim follows from the carry identity and the mathematical binary-expansion argument; a finite Brown test is only a check of sampled dyadic cases.

## Relationship to prior work
Geneson, *Deletion thresholds and exponential examples for complete sequences* (arXiv:2609.25107v1, first posted 2026-09-20), distinguishes eventual completeness from representation of every positive integer, recalls Brown's prefix inequality, and investigates floor-scaled geometric sequences and two interlaced rays. Its Theorem 1 concerns robustness under deletions and its Theorem 9 constructs an eventually incomplete single ray at a base strictly between one and two. Neither gives the set of *all* scales with full subset-sum coverage for an arbitrary finite prefix followed by exact doubling, nor the local dimension and all-parameter binomial strata proved here. The previously known one-ray geometric base-two phenomenon is the elementary special case, not claimed as independently new. Ma and Chen, *Hegyvári's theorem on complete sequences, II* (2022), discuss eventually complete floor-scaled sequences; only their abstract was accessible, so implicit coverage remains a residual risk. Erdős Problem 354 concerns **two** geometric rays and eventual completeness, rather than the exact single-ray full-cover property. The finite-prefix slack and the binary budget are explicit additional steps beyond the classical Brown criterion.

## Limitations
The exact classification applies to tails with **exact** doubling from some finite index, not merely ratios converging to two. The general theorem does not assert \(V_S\ne\varnothing\) for arbitrary prefixes; the explicit strata do provide nonempty examples. The 2022 paper was available in abstract form, but full text was not inspected; an equivalent older binary-budget formulation cannot be ruled out. The upper box-dimension conclusion is an upper bound, while the binomial strata supply sharp polylogarithmic counts in particular families.

## References
1. J. Geneson, *Deletion thresholds and exponential examples for complete sequences*, arXiv:2609.25107v1 (2026-09-20), https://arxiv.org/html/2609.25107v1 .
2. W.-X. Ma and Y.-G. Chen, *Hegyvári's theorem on complete sequences, II*, Acta Arith. 203 (2022), 307–318, https://doi.org/10.4064/aa210811-30-3 .
3. J. L. Brown Jr., *Note on complete sequences of integers*, Amer. Math. Monthly 68 (1961), 557–560; see the historical discussion in reference 1.
4. Erdős Problems, Problem 354, https://www.erdosproblems.com/354 (two-ray eventual-completeness question).
