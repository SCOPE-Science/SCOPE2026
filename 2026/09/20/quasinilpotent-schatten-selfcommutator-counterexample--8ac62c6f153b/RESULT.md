# A quasinilpotent Schatten self-commutator counterexample

## Result

Let \(S_p\) denote the Schatten \(p\)-class on \(\ell_2(\mathbb N_0)\). There exists a single compact, injective, quasinilpotent unilateral weighted shift \(W\) such that

\[
[W^*,W]=W^*W-WW^*\in S_1,
\]

while

\[
W\notin S_q\qquad\text{for every finite }q>0.
\]

Consequently, for every finite \(p\ge 1\),

\[
[W^*,W]\in S_p\quad\not\Rightarrow\quad W\in S_{2p}
\]

even under the stronger assumption that \(W\) is compact and quasinilpotent. This gives a negative answer to the quasinilpotent extension question left in Remark 1 of Kittaneh (1991): the finite-nilpotence implication \( [T^*,T]\in S_p\Rightarrow T\in S_{2p}\) does not survive when nilpotence is weakened to quasinilpotence.

The mechanism is more general. If \(a_0\ge a_1\ge\cdots>0\) and \(a_n\to0\), define

\[
W_a e_n=\sqrt{a_n}\,e_{n+1}.
\]

Then \(W_a\) is compact and quasinilpotent,

\[
W_a\in S_{2p}\iff (a_n)\in\ell_p,
\]

and

\[
[W_a^*,W_a]
=\operatorname{diag}\bigl(a_0,\ a_1-a_0,\ a_2-a_1,\ldots\bigr).
\]

In particular,

\[
\|[W_a^*,W_a]\|_{S_1}
=a_0+\sum_{n\ge1}(a_{n-1}-a_n)
=2a_0,
\]

so every such monotone compact weighted shift has trace-class self-commutator, regardless of how slowly its singular values tend to zero.

## Explicit example

Take

\[
a_n=\frac1{\log(n+2)},\qquad
W e_n=\frac1{\sqrt{\log(n+2)}}\,e_{n+1}.
\]

The weights are positive, decrease to zero, and hence \(W\) is injective and compact.

For \(N\ge1\),

\[
\|W^N\|
=\sup_{k\ge0}\prod_{j=0}^{N-1}\frac1{\sqrt{\log(k+j+2)}}
=\prod_{j=0}^{N-1}\frac1{\sqrt{\log(j+2)}}.
\]

Given \(\varepsilon>0\), all sufficiently late weights are below \(\varepsilon\); separating the finitely many early factors shows
\(\limsup_N\|W^N\|^{1/N}\le\varepsilon\). Hence \(r(W)=0\), so \(W\) is quasinilpotent.

Since

\[
W^*W=\operatorname{diag}(a_0,a_1,a_2,\ldots),\qquad
WW^*=\operatorname{diag}(0,a_0,a_1,\ldots),
\]

the self-commutator is diagonal as above. Monotonicity gives

\[
\|[W^*,W]\|_{S_1}=2a_0=\frac{2}{\log2}<\infty.
\]

On the other hand, the singular values of \(W\) are precisely its decreasing weights
\(\sqrt{a_n}\). Thus, for every finite \(q>0\),

\[
\|W\|_{S_q}^q
=\sum_{n=0}^{\infty} a_n^{q/2}
=\sum_{n=0}^{\infty}\frac1{(\log(n+2))^{q/2}}
=\infty.
\]

The final divergence follows, for example, because
\((\log(n+2))^{-q/2}\ge n^{-1}\) for all sufficiently large \(n\).

## Relation to prior work

Kittaneh proved in 1991 that finite nilpotence together with a Schatten-class self-commutator forces the corresponding doubled Schatten membership. In the same paper he observed that the compact-ideal endpoint admits quasinilpotence in place of nilpotence and explicitly asked whether the finite-\(p\) conclusion remains true under quasinilpotence.

Jocić and Kittaneh (1994) subsequently used and restated the finite-nilpotent Schatten implication in their perturbation inequalities. Later work on almost-normal operators and self-commutators, including Filonov--Safarov (2011), studies substantially broader approximation and normality questions. Standard weighted-shift literature also contains the diagonal formula for the self-commutator used above.

The individual weighted-shift formulas are therefore not claimed as new. The claimed contribution is the explicit observation that the monotone compact weighted-shift mechanism gives a single quasinilpotent counterexample lying in no finite Schatten class, thereby negatively resolving Kittaneh's finite-\(p\) quasinilpotent extension question.

## Originality and limitations

Originality is asserted only to the best of our knowledge. Exact and synonymous searches around Kittaneh's quasinilpotent question, Schatten self-commutators, and quasinilpotent weighted shifts did not locate a published resolution by this mechanism. The 1991 primary statement and its explicit question were inspected, and later self-commutator literature was compared for stronger coverage.

The residual originality risk is nonzero because the counterexample is elementary once the standard weighted-shift formulas are written down. Older weighted-shift, almost-normal-operator, and norm-ideal literature was not exhaustively checked theorem by theorem, so an unadvertised equivalent observation may exist.

This result does not characterize all quasinilpotent operators with Schatten self-commutator, nor does it address additional hypotheses such as hyponormality or membership in more restrictive operator classes.

## References

1. F. Kittaneh, *Some trace class commutators of trace zero*, Proc. Amer. Math. Soc. **113** (1991), 655--661. https://doi.org/10.1090/S0002-9939-1991-1086332-X
2. D. Jocić and F. Kittaneh, *Some perturbation inequalities for self-adjoint operators*, J. Operator Theory **31** (1994), 3--10. https://www.theta.ro/jot/archive/1994-031-001/1994-031-001-001.pdf
3. N. Filonov and Y. Safarov, *On the relation between an operator and its self-commutator*, J. Funct. Anal. **260** (2011), 2902--2932. https://doi.org/10.1016/j.jfa.2011.02.011
4. D.-V. Voiculescu, *Almost normal operators mod Hilbert--Schmidt and the K-theory of the algebras \(E\Lambda(\Omega)\)*, J. Noncommut. Geom. **8** (2014), 1123--1145. https://doi.org/10.4171/JNCG/181
