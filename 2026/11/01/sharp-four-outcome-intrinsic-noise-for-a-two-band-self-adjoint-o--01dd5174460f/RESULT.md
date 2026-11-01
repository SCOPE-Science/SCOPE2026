# Sharp four-outcome intrinsic noise for a two-band self-adjoint observable

## Finding

Let \(0\le a<1\), and let \(T\) be a bounded self-adjoint operator on a nonzero complex Hilbert space with precisely the spectrum
\[
K_a=[-1,-a]\cup[a,1].
\]
A normalized positive operator-valued measurement (POVM) with at most four real outcomes in \([-1,1]\) is a family \((\lambda_j,P_j)\) with \(P_j\succeq0\), \(\sum_jP_j=I\), and \(\lambda_j\in[-1,1]\). Require exact unbiasedness in the operator sense,
\[
\sum_j\lambda_jP_j=T.
\]
Its intrinsic-noise (second-moment excess) operator is
\[
N=\sum_j\lambda_j^2P_j-T^2.
\]
The exact optimum is
\[
\boxed{\inf\|N\|=E(a):=\frac{(2-\sqrt{1+3a^2})^2}{9}.}
\]
The infimum is attained by a commuting four-outcome POVM. Among four-element outcome sets contained in \([-1,1]\), the unique set supporting any optimal POVM is
\[
\boxed{\{-1,-s_a,s_a,1\},\qquad s_a=\frac{2\sqrt{1+3a^2}-1}{3}.}
\]
For \(0\le a<1\), one has \(a<s_a<1\), so the two inner outcome values lie *within the spectral bands*, not in the spectral gap. The theorem rules out any improvement by noncommuting effects. Uniqueness concerns the outcome values, not the effect operators.

The error decreases strictly from \(E(0)=1/9\) to zero as \(a\uparrow1\). The apparent alternative of placing the four outcomes at \(\{-1,-a,a,1\}\) has error \((1-a)^2/4\), strictly larger than \(E(a)\) whenever \(a<1\). The result is a quantitative nonzero-error counterpart to the obstruction to exactly representing \((I,T,T^2)\) by finitely many atoms when \(T\) has infinite spectrum.

## Assumptions and scope

The spectrum assumption includes *every* point of both bands and their endpoints; spectral multiplicities, absolute continuity, and separability are unrestricted. Thus a concrete example is multiplication by the coordinate on \(L^2(K_a,dt)\). The budget is the **number of distinct scalar outcome values**, at most four. Outcomes are required to lie in the convex spectral hull \([-1,1]\). Effects need not be projections or commute with \(T\). The optimization preserves the zeroth and first moments exactly and minimizes the operator norm of the excess second moment. It does not require exact second-moment reproduction, and it does not concern joint measurements of several observables.

For a fixed finite ordered outcome set \(\Lambda=\{\lambda_1<\cdots<\lambda_r\}\) whose convex hull contains \(\sigma(T)\), put
\[
g_\Lambda(t)=(t-\lambda_i)(\lambda_{i+1}-t)\quad\text{when }\lambda_i\le t\le\lambda_{i+1}.
\]
Its endpoint values agree, so the function is continuous on the hull. A useful more general statement, established below, is the exact fixed-support optimum
\[
\boxed{\inf_{\substack{P_j\succeq0,\ \sum P_j=I\\ \sum\lambda_jP_j=T}}\left\|\sum\lambda_j^2P_j-T^2\right\|=\max_{t\in\sigma(T)}g_\Lambda(t).}
\]
This formula holds for any bounded self-adjoint \(T\) and any finite real support spanning its spectrum, irrespective of commutativity of the effects. For the two-band claim the support is optimized over at most four values in \([-1,1]\).

## Proof

**1. Positivity and the fixed-support lower bound.** Since \(\sum P_j=I\) and \(\sum\lambda_jP_j=T\), direct expansion gives
\[
N=\sum_j(\lambda_jI-T)P_j(\lambda_jI-T)\succeq0.
\]
The products are ordered as written, so this argument does not assume that \(T\) commutes with any \(P_j\).

Fix adjacent support values \(\lambda_i<\lambda_{i+1}\). The polynomial \(q_i(x)=(x-\lambda_i)(x-\lambda_{i+1})\) is nonnegative at **every** support value: there is no intervening support value at which it could be negative. Hence
\[
0\preceq\sum_jq_i(\lambda_j)P_j
=N+(T-\lambda_iI)(T-\lambda_{i+1}I).
\]
Equivalently,
\[
N\succeq (T-\lambda_iI)(\lambda_{i+1}I-T).
\]
The self-adjoint functional calculus and positivity of \(N\) imply
\[
\|N\|\ge\sup_{t\in\sigma(T)\cap[\lambda_i,\lambda_{i+1}]}
(t-\lambda_i)(\lambda_{i+1}-t)
\]
whenever that intersection is nonempty. Taking the maximum over all adjacent pairs yields \(\|N\|\ge\max_{\sigma(T)}g_\Lambda\).

**2. The fixed-support upper bound.** Let \(w_j\) be the nonnegative piecewise-linear cardinal hat functions on \([\lambda_1,\lambda_r]\): on \([\lambda_i,\lambda_{i+1}]\), only
\[
w_i(t)=\frac{\lambda_{i+1}-t}{\lambda_{i+1}-\lambda_i},\qquad
w_{i+1}(t)=\frac{t-\lambda_i}{\lambda_{i+1}-\lambda_i}
\]
are possibly nonzero. Their sums and affine moments are exactly \(\sum_jw_j(t)=1\) and \(\sum_j\lambda_jw_j(t)=t\). By continuous functional calculus, \(P_j=w_j(T)\) are positive, sum to \(I\), and reproduce \(T\). Their noise is
\[
\sum_j\lambda_j^2w_j(T)-T^2=g_\Lambda(T).
\]
Consequently \(\|N\|=\max_{\sigma(T)}g_\Lambda\), proving the fixed-support identity. This also proves that allowing noncommuting POVMs cannot improve the norm.

**3. Four-outcome optimization.** Feasibility and \(\pm1\in\sigma(T)\) force the least and greatest outcomes to equal \(-1\) and \(1\), respectively, when all outcomes are in \([-1,1]\). Repeated outcomes or fewer than four outcomes may be augmented by new distinct values without increasing the fixed-support optimum. It therefore suffices to analyze ordered \(\Lambda=(-1,x_2,x_3,1)\).

Set
\[
s=\frac{2\sqrt{1+3a^2}-1}{3},\qquad e=\frac{(1-s)^2}{4}.
\]
The identity \(3s^2+2s=1+4a^2\) implies \(e=s^2-a^2\). Also \(a<s<1\) and \(e<(1-a)^2/4\).

For the symmetric choice \(\Lambda_*=(-1,-s,s,1)\), the maximum of \(g_{\Lambda_*}\) on each outer subband is \((1-s)^2/4=e\), attained at the outer midpoint. On the two pieces of the spectrum inside the middle support interval, the maximum is at \(t=-a\) or \(t=a\), and equals \(s^2-a^2=e\). Hence the optimal hat-function POVM has norm-noise exactly \(e\).

Now let an arbitrary four-outcome support have noise optimum no larger than \(e\). If \(x_2\ge-a\), its leftmost gap contains the entire spectral interval \([-1,-a]\), so at its midpoint the noise is at least \((1-a)^2/4>e\), a contradiction. Symmetrically, \(x_3\le a\) is impossible. Therefore \(x_2=-u<-a\) and \(x_3=v>a\), where \(a<u,v<1\). Since \([-1,-u]\) and \([v,1]\) are full spectral subintervals, their midpoint variances imply
\[
\frac{(1-u)^2}{4}\le e,\qquad\frac{(1-v)^2}{4}\le e.
\]
Thus \(u,v\ge1-2\sqrt e=s\). At the inner spectral endpoint \(t=-a\), which lies between \(-u\) and \(v\), the variance is
\[
(u-a)(v+a)\ge(s-a)(s+a)=s^2-a^2=e.
\]
This proves the universal lower bound. Equality throughout forces \(u=v=s\), proving uniqueness of the optimal four distinct outcome values. Supports of fewer than four distinct values cannot attain the bound because adding missing support values cannot increase the error, and any optimal augmented four-element set must have all four distinct specified values.

**4. Limits and comparison.** The explicit formula gives \(E(0)=1/9\), \(E(a)\downarrow0\) strictly for \(0<a<1\), and \(E(a)\sim(1-a)^2/4\) as \(a\uparrow1\). The spectral-endpoint codebook has outer gaps of length \(1-a\) and therefore exact noise \((1-a)^2/4\), which is strictly larger since \(s>a\). No norm-limit or finite spectral discretization is used in the proof.

## Verification

The companion `check_quantization.py` uses deterministic seeds, tests the closed formulas at seven distinct gap sizes, checks positivity and exact moment reconstruction on finite diagonal operators, samples 3,500 arbitrary competing four-level supports, and checks 450 random noncommuting matrix POVMs against the polynomial Loewner lower bounds. It passed all **3,957 grouped instances** on direct execution. Each instance contains several assertions; the counts are grouped test cases, not claims of independent verification. The source calculations and the arbitrary-Hilbert-space conclusion are established analytically above, not inferred from finite tests.

To reproduce, run `python check_quantization.py` in an environment with Python 3 and NumPy.

## Relationship to prior work

Curto, Ech-charyfy, El Azhar, and Zerouali analyze finite atomic representations of operator moment sequences. Their Section 5, especially Example 5.10, explains why exact representation of \((I,T,T^2)\) can fail when \(T\) has infinitely many spectral values. The present statement replaces impossible exact reproduction by the sharp **best operator-norm error** with exactly four allowed outcomes; it does not solve their full operator moment problem.

The intrinsic-noise operator itself and its positivity are established notions: Massar's Section II (2007) explicitly writes the same quadratic difference, and Pietrzycki–Stochel (2022/2023), Theorem 1.1 and equation (1.2), discuss its vanishing and rigidity. Neither inspected source gives this two-band four-outcome minimum, optimal support, or noncommuting optimality reduction. Mädler–Schmüdgen provide a finite-dimensional matricial Richter–Tchakaloff theorem; it concerns exact finite atomic representation for finite-dimensional matrix functionals rather than the fixed-cardinality second-moment error of an infinite-spectrum observable.

Nonuniform stochastic rounding, as in Ramezani-Kebrya et al., uses adjacent-level randomization and examines vector-gradient variance. Its formulas and application-specific optimization do not state the present disconnected-spectrum four-level law or arbitrary-operator Loewner lower bound. The one-dimensional randomization mechanism is standard and is not claimed as new.

## Limitations

The optimum is for the **operator norm** of the intrinsic-noise operator, not a Schatten norm, trace, mean-square error under a fixed state, or instrument disturbance. Values outside \([-1,1]\) are not part of the stated admissible class; the claim makes no uniqueness assertion for unrestricted outcome values. It concerns one self-adjoint observable with the entire two-band spectrum, not general arbitrary closed spectral sets or multivariate POVMs. Uniqueness of the effect operators is not asserted. The result has undergone analytical and reproducible computational checking, but independent external correctness and comprehensive historical-priority assessments have not been performed. A more general optimal unbiased quantization theorem could imply this specialization under alternative terminology.

## References

1. R. E. Curto, A. Ech-charyfy, H. El Azhar, and E. H. Zerouali, *The Local Operator Moment Problem on \(\mathbb R\)*, Complex Analysis and Operator Theory **19**, 25 (published online **6 January 2025**), DOI 10.1007/s11785-024-01649-4; accessible preprint arXiv:2605.04392v1 (6 May 2026).
2. S. Massar, *Uncertainty Relations for Positive Operator Valued Measures*, Physical Review A **76**, 042114 (2007), arXiv:quant-ph/0703036, Section II.
3. P. Pietrzycki and J. Stochel, *Two-moment characterization of spectral measures on the real line*, Canadian Journal of Mathematics **75** (2023), 1369–1392, DOI 10.4153/S0008414X22000426, Theorem 1.1 and equation (1.2).
4. C. Mädler and K. Schmüdgen, *On the Truncated Matricial Moment Problem. I*, arXiv:2310.00957 (2 October 2023), Section 5.
5. A. Ramezani-Kebrya et al., *NUQSGD: Provably Communication-efficient Data-parallel SGD via Nonuniform Quantization*, arXiv:1908.06077 (2019), Sections 3.1 and 4.1 and Appendix E.
