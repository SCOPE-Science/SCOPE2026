# Every finite-time image of traffic Rule 184: forbidden words and a sharp entropy relaxation law

## Finding

Let \(F:\{0,1\}^{\mathbb Z}\to\{0,1\}^{\mathbb Z}\) be elementary cellular automaton Rule 184, defined at every integer position by
\[
(Fx)_i=x_{i-1}(1-x_i)+x_i x_{i+1}.
\]
For each integer \(t\ge0\), put \(Y_t=F^t(\{0,1\}^{\mathbb Z})\), regarded as a spatial subshift. Then **all** its minimal forbidden words are exactly
\[
\mathcal F_t=\{\,11(01)^k00:0\le k<t\,\}.
\]
Thus each finite-time image is a shift of finite type, and \(Y_{t+1}\subsetneq Y_t\) for every \(t\ge0\). In particular, the finite-time images never stabilize.

If \(a_{t,n}\) is the number of length-\(n\) spatial words occurring in \(Y_t\), with \(a_{t,0}=1\), then, as a formal power series,
\[
\sum_{n\ge0}a_{t,n}z^n
=\frac{1}{1-2z+\sum_{k=0}^{t-1}z^{2k+4}}
=\frac{1-z^2}{(1-z-z^2)^2-z^{2t+4}}
\]
for every \(t\ge0\); the last fraction is understood by cancellation at \(t=0\). In particular, for negative indices set \(a_{t,n}=0\); then
\[
a_{t,n}=2a_{t,n-1}-\sum_{k=0}^{t-1}a_{t,n-2k-4},\qquad n\ge1.
\]
The spatial topological entropy is
\[
h_t=\log\lambda_t,
\qquad
\lambda_t^t(\lambda_t^2-\lambda_t-1)=1,
\qquad \lambda_t>\varphi=\frac{1+\sqrt5}{2}.
\]
The displayed equation has precisely one real solution greater than \(\varphi\). The decreasing entropies have the **sharp** convergence law
\[
\boxed{\lim_{t\to\infty}\varphi^{t+1}(h_t-\log\varphi)=\frac1{\sqrt5}.}
\]
The global limit set \(Y_\infty=\bigcap_{t\ge0}Y_t\) has spatial entropy \(\log\varphi\), although the images never reach it at finite time.

## Assumptions and scope

The alphabet is binary and the spatial lattice is bilateral, \(\mathbb Z\). No probabilistic initialization, finite ring, or spatial-density hypothesis is imposed. Time \(t\) is any nonnegative integer. Entropies are spatial shift entropies of compact images, not the temporal entropy of the cellular automaton or the entropy of a pushforward probability measure.

An occurrence of \(11(01)^k00\) is read in the usual overlapping sense; \(k=0\) gives `1100`, \(k=1\) gives `110100`. The notation \(F^0\) means the identity and \(Y_0\) is the full shift.

## Proof

**1. Defect representation.** On bond \(i\) of a binary configuration \(x\), mark \(+\) if \(x_ix_{i+1}=11\), mark \(-\) if \(x_ix_{i+1}=00\), and otherwise mark \(0\). If consecutive nonzero marks occur at bonds \(i<j\), their distance \(j-i\) is odd for equal signs and even for opposite signs. Conversely, every bi-infinite ordered set of marked bonds with this adjacent-mark parity property comes from a binary configuration: begin at any mark, fix its two equal cell values according to its sign, and propagate by alternation across unmarked bonds. When at least one mark exists this configuration is unique. With no marks there are exactly two alternating configurations.

An exhaustive check of the sixteen four-cell patterns \(x_{i-1}x_ix_{i+1}x_{i+2}\) establishes the following local particle law. Each \(+\) mark moves one bond left, each \(-\) mark moves one bond right, except that a \(-\) at bond \(i-1\) and a \(+\) at bond \(i+1\) annihilate upon their common arrival at bond \(i\). There is no other creation, annihilation, or collision. This local identity is also checked directly by the included program.

**2. Forward exclusion.** Write \(X_t\) for the configurations that avoid every word in \(\mathcal F_t\). The occurrence \(11(01)^k00\) is exactly an adjacent \(+\), then \(-\), among the nonzero bond marks, with separation \(2k+2\). Thus membership in \(X_t\) is equivalent to the condition that every consecutive \(+,-\) pair has separation at least \(2t+2\). For \(t=0\) there is no restriction.

If consecutive output marks \(+,-\) have separation \(d\), they have distinct incoming ancestors at bonds separated by \(d-2\). The incoming ancestors are a \(+\) followed by a \(-\), though there may have been intermediate marks that subsequently annihilated. In any finite list beginning with \(+\) and ending with \(-\), there is a consecutive \(+,-\) pair no farther apart than the endpoints. Therefore, if the input belongs to \(X_t\), the output cannot contain a consecutive \(+,-\) pair with separation at most \(2t+2\). Hence \(F(X_t)\subseteq X_{t+1}\).

**3. Reverse construction.** Let \(y\in X_{t+1}\). Move each \(+\) mark in \(y\) one bond right and each \(-\) mark one bond left, with no new marks. Equal-sign neighboring marks retain their odd separation; a neighboring \(-,+\) pair increases its even separation by two; and a neighboring \(+,-\) pair decreases its even separation by two. Because \(y\) avoids at least `1100`, every last separation is at least four, so the moved marks remain distinct, ordered, and parity-compatible. They determine a unique binary configuration \(x\) whenever any mark exists. If there are no marks, choose the alternating configuration complementary to \(y\).

Every consecutive \(+,-\) pair in \(x\) has separation at least \(2t+2\), so \(x\in X_t\). Moreover, a collision among the proposed input marks would require a \(-\) and \(+\) at bonds two apart; their projected output positions would be the same bond with incompatible signs. This is impossible. All proposed marks therefore survive and move to exactly the marks of \(y\). Since a nonempty marked-bond pattern uniquely determines its binary configuration, \(F(x)=y\). With no marks, Rule 184 exchanges the two alternating configurations, also giving \(F(x)=y\). Consequently \(F(X_t)=X_{t+1}\) for every \(t\ge0\). As \(X_0=Y_0\), induction gives \(Y_t=X_t\) for all time.

Each forbidden word \(11(01)^k00\) has only one `11`, at its beginning, and only one `00`, at its end. Different words in this family cannot contain each other, and every proper subword lacks either `11` or `00`; it extends to a bi-infinite configuration avoiding the entire family. Hence these and only these are the minimal forbidden words of \(Y_t\). The periodic configuration with period word \(11(01)^t00\) lies in \(Y_t\) but not in \(Y_{t+1}\), proving strict descent.

**4. Exact finite-word enumeration.** Let \(a_{t,n}\) count admissible length-\(n\) words, with \(a_{t,n}=0\) for \(n<0\). Among the \(2a_{t,n-1}\) one-symbol extensions of admissible words of length \(n-1\), inadmissible extensions are those ending in one of \(11(01)^k00\), for \(0\le k<t\). Every such ending has a unique, admissible prefix of length \(n-2k-4\), since two forbidden family members cannot overlap at a proper nonempty suffix/prefix: any forbidden prefix begins in `11`, but no proper suffix of a forbidden word begins in `11`. Conversely an admissible prefix concatenated with one forbidden word creates no earlier forbidden word crossing their junction. There are exactly \(\sum_{k=0}^{t-1}a_{t,n-2k-4}\) invalid extensions. This proves the recurrence and its rational generating function.

**5. Entropy and its sharp limit.** Write \(q_t(z)=1-2z+\sum_{k=0}^{t-1}z^{2k+4}\). The algebraic identity
\[
(1-z^2)q_t(z)=(1-z-z^2)^2-z^{2t+4}
\]
holds for every integer \(t\ge0\). Let \(r=\varphi^{-1}\). On \((0,r)\), the equation \(q_t(z)=0\) reduces to \(1-z-z^2=z^{t+2}\), which has exactly one root \(\rho_t\), because its left side strictly decreases from one to zero and its right side strictly increases. There is no smaller positive real root. Since the word-count series has nonnegative coefficients, its radius of convergence is a positive real singularity; hence it is \(\rho_t\). Standard subshift word-complexity subadditivity gives entropy \(-\log\rho_t=\log\lambda_t\). The variable \(\lambda_t=1/\rho_t\) obeys the claimed unique equation above \(\varphi\).

As \(t\to\infty\), \(\lambda_t\downarrow\varphi\), while
\[
(\lambda_t-\varphi)(\lambda_t+\varphi^{-1})=\lambda_t^{-t}.
\]
The identity bounds \(\lambda_t-\varphi\le\varphi^{-t}/\sqrt5\), hence \(t(\lambda_t-\varphi)\to0\) and \((\lambda_t/\varphi)^t\to1\). Taking ratios yields \(\lambda_t-\varphi\sim\varphi^{-t}/\sqrt5\), and the mean-value theorem for the logarithm yields the sharp entropy limit. Finally, \(Y_\infty\) contains the golden-mean subshift forbidding `11`, so its entropy is at least \(\log\varphi\); monotonicity of entropy under containment and \(h_t\downarrow\log\varphi\) give the reverse inequality.

## Verification

The portable `verify.py` implements independently the local Rule-184 update, its \(t\)-fold block rule, the finite labeled preimage graph, and cyclic one-step inverse construction. Executing `python verify.py` checks all sixteen four-cell defect updates, compares eighty independently enumerated finite-image word counts with the recurrence (time \(0\le t\le4\), length \(0\le n\le15\)), and checks 20,782 admissible cyclic inverse cases (ring sizes \(1\) through \(13\), time indices \(0\) through \(5\)). It also evaluates the entropy root and convergence ratio numerically. All these checks passed in the recorded execution. The finite computations corroborate, rather than replace, the unrestricted proof above.

## Relationship to prior work

Rule 184 and its interpretation as deterministic traffic flow have long been established. Fukś, *Exact results for deterministic cellular automata traffic models* (arXiv:math/9904182, first public 1999-04-12), obtains arbitrary-time flow and selected zero-block preimage formulas through lattice paths. Belitsky and Ferrari, *Invariant Measures and Convergence Properties for Cellular Automaton 184 and Related Processes* (2005), study invariant measures, phase separation and hydrodynamic limits; its full text was not available for the comparison. Hellouin de Menibus and Sablik, *Self-organisation in cellular automata with coalescent particles* (arXiv:1602.06093, first public 2016-02-19), explicitly give the two defect species and their ballistic annihilation law, and develop results concerning measure-dependent asymptotic behavior.

The defect dynamics themselves are **not** claimed as new. The evaluated claim here is the exact forbidden-word presentation of **every** finite-time full-image subshift, its full family of word-count generating functions, and the explicit sharp entropy-relaxation constant. These are distinct from selected block probabilities, hydrodynamic limits, and measure-dependent \(\mu\)-limit sets. Deriving the evaluated theorem requires the reverse-image construction and nonoverlap enumeration in addition to the preexisting particle rule.

## Limitations

This concerns the bilateral global images of a deterministic rule. It does not give the distribution of words under a chosen initial probability measure, temporal entropy, or quantitative convergence of random trajectories. Although earlier checked sources did not provide the stated full-image formulas, the historical-priority comparison is not exhaustive; notably, the full 2005 Belitsky–Ferrari paper and the 1995 antecedent were not accessible. The entropy limit describes spatial image complexity, not necessarily the measure-theoretic mixing time.

## References

1. H. Fukś, *Exact results for deterministic cellular automata traffic models*, arXiv:math/9904182, initial public submission 1999-04-12, https://arxiv.org/abs/math/9904182.
2. B. Hellouin de Menibus and M. Sablik, *Self-organisation in cellular automata with coalescent particles: qualitative and quantitative approaches*, arXiv:1602.06093, initial public submission 2016-02-19, https://arxiv.org/abs/1602.06093.
3. V. Belitsky and P. A. Ferrari, *Invariant Measures and Convergence Properties for Cellular Automaton 184 and Related Processes*, J. Stat. Phys. 118 (2005), 589–623, https://doi.org/10.1007/s10955-004-8822-4 (abstract consulted; full text unavailable).
4. V. Belitsky and P. A. Ferrari, *Ballistic annihilation and deterministic surface growth*, J. Stat. Phys. 80 (1995), 517–543, https://doi.org/10.1007/BF02178546 (abstract consulted; full text unavailable).
