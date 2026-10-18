# Optimal seed-depth allocation has a sharp finite switching law

## Finding

For a low-density disturbance-responsive seed-bank model with \(n\ge2\) depth classes, optimizing a single fixed allocation of newborn seeds across classes always admits a pure-class optimum. More precisely, for any disturbance frequency \(0<q\le1\), dormant survival rates \(0<s_i<1\), germination rates \(0<g_i\le1\), and common expected fecundity \(B>0\), define
\[
L_i(q)=s_i+qg_i(B-s_i),\qquad \Lambda(q)=\max_{1\le i\le n}L_i(q).
\]
The largest possible expected-population asymptotic growth factor is exactly \(\Lambda(q)\). A newborn-seed allocation is optimal **if and only if** all its positive mass is placed on depth classes attaining \(\Lambda(q)\). At \(q=0\), every allocation is optimal and the growth factor is \(\max_i s_i\).

As \(q\) varies through \((0,1)\), there are at most \(n-1\) distinct genuine changes of the optimal depth class; this bound is sharp for every \(n\ge2\), even when the depth classes have strictly decreasing survival and strictly increasing germination rates. The optimal growth factor is a convex, piecewise-affine function of \(q\).

## Assumptions and scope

There are \(n\) depth classes of viable seeds. At each discrete census, an individual in class \(i\) germinates with unconditional probability \(qg_i\); its germination contributes an expected \(B\) viable newborn seeds allocated independently of parental class according to the fixed vector \(w=(w_1,\ldots,w_n)\), with \(w_i\ge0\) and \(\sum_iw_i=1\). A nongerminating seed survives dormant into the same class with probability \(s_i\). Germination and dormancy are mutually exclusive during a census interval. We optimize the **spectral radius of the deterministic matrix of conditional mean contributions**, not the top Lyapunov exponent of a population subject to common random disturbances, quasi-extinction risk, or realized population growth in a random environment.

Writing \(g=(g_i)\) and \(d_i(q)=s_i(1-qg_i)\), the expected class-count vector evolves as
\[
x_{t+1}=M(q,w)x_t,\qquad M(q,w)=\operatorname{diag}(d_1(q),\ldots,d_n(q))+Bq\,w g^{\mathsf T}.
\]
Every assertion is for any integer \(n\ge2\), any real \(B>0\), and all admissible \(s_i,g_i,q,w\) specified above. No independence among seeds is needed for this **mean-matrix** calculation, beyond the stated first-moment contributions.

## Proof

**Exact optimizer and equality characterization.** Fix \(q>0\) and put \(D=\operatorname{diag}(d_i(q))\), \(d_{\max}=\max_i d_i(q)\), and \(\Lambda=\max_i(d_i(q)+Bqg_i)\). Because \(Bqg_i>0\), the class with the largest \(d_i\) has \(d_i+Bqg_i>d_{\max}\), proving \(\Lambda>d_{\max}\).

For every real \(z>d_{\max}\), the matrix determinant lemma gives
\[
\det(zI-M(q,w))=\prod_{i=1}^n(z-d_i)\left[1-Bq\sum_{i=1}^n\frac{w_ig_i}{z-d_i}\right].
\]
The secular expression \(H_w(z)=Bq\sum_i w_ig_i/(z-d_i)\) is positive and strictly decreasing from its finite or infinite left limit towards zero as \(z\to\infty\). At \(z=\Lambda\), every ratio \(Bqg_i/(\Lambda-d_i)\le1\), with equality exactly when \(d_i+Bqg_i=\Lambda\). Hence
\[
H_w(\Lambda)\le\sum_iw_i=1,
\]
with equality exactly when \(\operatorname{supp}(w)\subseteq\operatorname{argmax}_iL_i(q)\). By Perron–Frobenius, the nonnegative matrix \(M(q,w)\) has real nonnegative spectral radius. Any real eigenvalue above \(d_{\max}\) must solve \(H_w(z)=1\), and this equation has at most one solution there. Since \(H_w\) decreases strictly, \(H_w(\Lambda)\le1\) excludes any such eigenvalue above \(\Lambda\). The nonnegative matrix has a real Perron eigenvalue equal to its spectral radius, so its spectral radius is at most \(\Lambda\), even if the matrix is reducible and its spectral radius is a diagonal entry at most \(d_{\max}\). If equality in the spectral bound holds, \(\Lambda>d_{\max}\) is an eigenvalue and therefore \(H_w(\Lambda)=1\), giving exactly the support condition above. Conversely, that condition yields \(H_w(\Lambda)=1\), hence \(\Lambda\) is an eigenvalue and realizes the proven upper bound. Every pure allocation at a maximizing index satisfies it. At \(q=0\), \(M(0,w)=\operatorname{diag}(s_i)\), independent of \(w\).

**Switch upper bound.** The \(n\) candidate functions \(L_i(q)\) are affine in \(q\). Their pointwise maximum is convex and piecewise affine. After merging identical lines, the slopes of consecutively active pieces strictly increase. Therefore each of the at most \(n\) distinct lines is active on at most one interval; at most \(n-1\) distinct interior switchpoints occur. Coincident equal lines do not create new switches.

**Sharpness, with a biologically ordered tradeoff.** For each \(n\ge2\), index classes by \(i=0,\ldots,n-1\), set \(\delta=1/(8n^2)\), \(B=2\), and choose
\[
s_i=\frac34-\delta i(i+1),\quad b_i=\frac14+2\delta ni,\quad g_i=\frac{b_i}{2-s_i}.
\]
All parameters satisfy \(0<s_i<1\), \(0<g_i<1\), and \(s_i>s_{i+1}\). Furthermore \(g_i<g_{i+1}\), since this inequality is equivalent to \(n(2-s_i)>b_i(i+1)\); the left side is at least \(5n/4\), while the right side is less than \(n/2\). Consequently \(L_i(q)=s_i+b_iq\), and for any pair of indices
\[
L_i(q)-L_j(q)=\delta(i-j)\,[2nq-(i+j+1)].
\]
For every \(i=0,\ldots,n-1\), the \(i\)-th line is the unique maximum when \(i/n<q<(i+1)/n\). At each \(q=k/n\), for \(k=1,\ldots,n-1\), exactly lines \(k-1\) and \(k\) tie at the maximum, and mixtures of those two classes are precisely the optimal allocations. Thus all \(n-1\) switches occur within \((0,1)\), proving sharpness.

**Concrete three-depth illustration.** With \(B=2\), \(s=(9/10,4/5,1/2)\), and \(g=(1/11,5/12,3/5)\), the three candidates are
\[
L_1(q)=\frac9{10}+\frac q{10},\quad L_2(q)=\frac45+\frac q2,\quad L_3(q)=\frac12+\frac{9q}{10}.
\]
The uniquely optimal depth changes from class 1 to class 2 at \(q=1/4\), and from class 2 to class 3 at \(q=3/4\). At each crossing exactly the adjacent pair's mixtures are optimal, yielding values \(37/40\) and \(47/40\), respectively.

## Verification

The standalone `verify.py` uses exact rational arithmetic to test the determinant-lemma equality criterion for seven allocation vectors at five disturbance frequencies in the three-depth example. It also verifies the affine-line identities, all designated unique winners and adjacent ties, and admissibility and strict ordering of the sharp construction for every integer \(2\le n\le16\). Execute `python verify.py` in an environment with Python 3 and SymPy. It prints `PASS: three-depth exact determinant tests and sharp families n=2..16`. The proof above, not this finite test, establishes all-integer and all-real-parameter assertions.

## Relationship to prior work

Eager, Haridas, Pilson, Rebarber, and Tenhumberg [1] developed a *stochastic density-dependent integral-projection* model of seed-bank depth and disturbances, and reported frequency-dependent changes in how disturbance depth affects viability. Their **qualitative disturbance-depth reversals are already known** and are not claimed here. The present result instead isolates a deterministic low-density rank-one mean-projection model, optimizes **arbitrary newborn-depth allocations** over the entire simplex, characterizes **all** optimal ties, and proves an exact worst-case switching count attained at every class number. The full text of [1] was not available for direct comparison, so an equivalent special case inside it remains a residual uncertainty.

Satterthwaite [2] studied dormancy via spatial competition and evolutionary invasion/ESS conditions; its payoff, demographic mechanism, and decision variables differ. Nesterov and Protasov [3] developed broad methods for optimizing nonnegative-matrix spectral radii. Protasov and Logofet [4] studied rank-one corrections in matrix-population models, primarily their second positive eigenvalue and stability indicators. Both supply related general matrix theory, but the inspected results did not state the exact seed-depth allocation/support characterization and its sharp \(n-1\) frequency-switch construction. The narrower, class-specific characterization is the contribution asserted here; the underlying determinant lemma and Perron theory are classical. Eager, Rebarber, and Tenhumberg [5] studied stochastic seed-bank population persistence, a different objective.

## Limitations

The result is about asymptotic growth of the **expectation** under fixed aggregate disturbance frequency and fixed parameter values, not almost-sure population growth under season-to-season common environmental randomness. It excludes density dependence, vertical redistribution of existing seeds, seed-age effects, annual variability, and any cost for changing allocation policies. If such mechanisms are present, mixtures can be beneficial and the pure-optimality theorem need not apply. The sharp family shows mathematical possibility, not empirical typicality. The published literature comparison is bounded by source accessibility; no priority or independent verification is asserted beyond the cited, inspected material.

## References

1. E. A. Eager, C. V. Haridas, D. Pilson, R. Rebarber, and B. Tenhumberg (2013), “Disturbance Frequency and Vertical Distribution of Seeds Affect Long-Term Population Dynamics: A Mechanistic Seed Bank Model,” *The American Naturalist* 182:180–190, doi:10.1086/670987. Earliest verified public date: 2013-06-21 (PubMed and OpenAlex).
2. W. H. Satterthwaite (2009), “Competition for space can drive the evolution of dormancy in a temporally invariant environment,” *Plant Ecology*, doi:10.1007/s11258-009-9696-y. Open-access full text.
3. Y. Nesterov and V. Protasov (2011 preprint; journal 2013), “Optimizing the Spectral Radius,” https://optimization-online.org/2011/12/3272/ , doi:10.1137/110850967. Preprint full text.
4. V. Yu. Protasov and D. O. Logofet (2014), “Rank-One Corrections of Nonnegative Matrices, With an Application to Matrix Population Models,” *SIAM Journal on Matrix Analysis and Applications* 35:749–764, doi:10.1137/130935537. Public author-shared text.
5. E. A. Eager, R. Rebarber, and B. Tenhumberg (2014), “Modeling and analysis of a density-dependent stochastic integral projection model for a disturbance specialist plant and its seed bank,” *Bulletin of Mathematical Biology* 76:1809–1834, doi:10.1007/s11538-014-9978-y.
