# Arithmetic resonance and sparse sharp extremizers on a lacunary finite-field curve

## Finding

For every finite field \(F=\mathbb F_q\) of characteristic greater than \(3\), let \(\gamma(t)=(t,t^3,t^4)\in F^3\). Fix a nontrivial additive character \(\psi:F\to\mathbb C\) and define the Fourier synthesis map
\[
(Tf)(u,v,w)=\sum_{t\in F} f(t)\psi(ut+vt^3+wt^4).
\]
Give the input \(\ell^2(F)\) counting measure and the output \(L^4(F^3)\) **uniform probability measure**: \(\|h\|_{L^4(F^3)}^4=q^{-3}\sum_{(u,v,w)\in F^3}|h(u,v,w)|^4\). These conventions are part of the assertion. The exact endpoint operator norm is
\[
\boxed{\|T\|_{\ell^2(F)\to L^4(F^3)}^4=\begin{cases}2-q^{-1},&q\equiv3\pmod4,\\9/4,&q\equiv1\pmod4.\end{cases}}
\]
All nonzero extremizers are classified. When \(q\equiv3\pmod4\), they are exactly the functions whose absolute value is the same positive constant at every field point; all phases may vary independently. When \(q\equiv1\pmod4\), they are exactly the functions supported on a single four-point multiplicative orbit \(\{a,-a,\iota a,-\iota a\}\) with \(a\in F^\times\), \(\iota^2=-1\), equal nonzero magnitudes on the orbit, and
\[
\boxed{f(a)f(-a)=f(\iota a)f(-\iota a).}
\]
No point outside the selected orbit, including zero, may carry nonzero mass in the latter case.

## Assumptions and scope

Throughout, \(q\) is a prime power with characteristic at least \(5\); in particular, \(2\) and \(3\) are invertible in \(F\). The four coordinates of the displayed orbit are distinct. Each \(\iota\) exists precisely when \(q\equiv1\pmod4\). We make no claim in characteristics \(2\) or \(3\). No constant-factor normalization for the usual normalized-surface-measure/unnormalized-ambient-counting extension operator is silently imported: the input and output measures above fix the constant exactly.

## Proof

**Pair-sum fibers.** By character orthogonality,
\[
\|Tf\|_{L^4(F^3)}^4=Q(f):=\sum_{\gamma(a)+\gamma(b)=\gamma(c)+\gamma(d)} f(a)f(b)\overline{f(c)f(d)}.
\]
Put \(S=\sum_{t\in F}|f(t)|^2\), so the fourth power of the norm ratio is \(Q(f)/S^2\) for \(S>0\). If a common first-coordinate pair sum is \(s\ne0\), the identity
\[
a^3+b^3=s^3-3sab
\]
shows that equality of the first and third-power coordinate sums forces \(ab=cd\). Consequently \(\{a,b\}=\{c,d\}\) as unordered multisets, and the fourth coordinate is then automatically equal. If the common first sum is \(0\), the pairs are \((a,-a)\); their cubic sums vanish and their quartic sums agree if and only if \(a^4=c^4\). For nonzero \(a,c\), this is the condition that \(c/a\) be a fourth root of unity. Its solutions comprise exactly \(\{\pm1\}\) when \(q\equiv3\pmod4\), and \(\{1,-1,\iota,-\iota\}\) when \(q\equiv1\pmod4\).

**Exact fourth moments.** Trivial unordered-pair coincidences contribute
\[
Q_0(f)=2S^2-\sum_{t\in F}|f(t)|^4.
\]
Thus for \(q\equiv3\pmod4\), the moment equals \(Q_0(f)\). Cauchy–Schwarz gives \(\sum|f(t)|^4\ge S^2/q\), with equality if and only if every \(|f(t)|^2=S/q\). The first sharp constant and all of its equality cases follow, independently of phases.

For \(q\equiv1\pmod4\), partition \(F^\times\) into disjoint four-element multiplicative orbits \(O=\{a,-a,\iota a,-\iota a\}\). Each orbit supplies two unordered zero-sum pairs, with products \(U_O=f(a)f(-a)\) and \(V_O=f(\iota a)f(-\iota a)\). The four ordered pair choices in the cross term yield the **exact** identity
\[
Q(f)=2S^2-\sum_t|f(t)|^4+8\sum_O\operatorname{Re}(U_O\overline{V_O}).
\]
Let \(z_t=|f(t)|^2\ge0\), let \(w_O=\sum_{t\in O}z_t\), and put \(\alpha=z_0\). The real-part, arithmetic–geometric-mean, and Cauchy inequalities give, orbit by orbit,
\[
8\operatorname{Re}(U_O\overline{V_O})\le8\sqrt{\prod_{t\in O}z_t}\le\frac{w_O^2}{2},\qquad
\sum_{t\in O}z_t^2\ge\frac{w_O^2}{4}.
\]
Therefore
\[
Q(f)\le 2S^2-\alpha^2+\frac14\sum_Ow_O^2
\le 2S^2-\alpha^2+\frac14(S-\alpha)^2\le\frac94S^2.
\]
Equality in the last inequality for \(S>0\) requires \(\alpha=0\). Equality in \(\sum_Ow_O^2\le(\sum_Ow_O)^2\) requires exactly one orbit of positive mass. Equality in the two orbit inequalities requires four equal positive magnitudes and \(U_O\overline{V_O}\) positive real of maximal size; for equal magnitudes this is equivalent to \(U_O=V_O\). Conversely these conditions give \(Q(f)=9S^2/4\), proving both sharpness and the complete classification.

## Verification

The accompanying `artifacts/verify.py` reconstructs all ordered pair-sum fibers with exact arithmetic for seven prime fields of orders \(5,7,11,13,17,19,23\) and the quadratic extension fields of orders \(25,49\). It checks fiber multiplicities, the exact fourth-moment decomposition on five seeded complex test vectors per field, the claimed extremizers, and strict failure after a phase perturbation. The Fourier synthesis fourth moment is evaluated directly in physical-frequency space for orders \(5\) and \(7\) with the probability-output normalization. The code prints `VERIFY_OK` on successful completion. These finite checks do not prove the theorem over arbitrary finite fields: that comes from the algebraic pair-fiber argument and equality analysis above.

## Relationship to prior work

Mockenhaupt–Tao introduced the foundational finite-field restriction setting; their operator estimates do not state an exact sharp \(\ell^2\to L^4\) constant for this three-coordinate lacunary curve. Koh–Shen consider general **plane** algebraic curves with bounded extension constants, not this sharp three-dimensional fourth moment. The standard nonlacunary finite-field moment curve in recent sharp endpoint work includes successive monomials and has a different pair-collision structure. Published computations for the planar quartic graph \(\{(t,t^4):t\in F\}\), and sharp results for the planar cubic graph \(\{(t,t^3):t\in F\}\), do not determine the three-coordinate pair-sum fibers and do not imply this arithmetic sharp constant. The present result isolates the distinction by a self-contained pair-fiber proof.

## Limitations

The characteristic restriction is essential for the displayed proof because the cubic-sum identity loses information in characteristic three. The sharp constant is valid only with the explicitly declared counting-input/probability-output convention. No claim is made about higher even moments, nonlinear perturbations, general lacunary exponent sets, or Euclidean Fourier extension. Existing but unidentified equivalent formulations under additive-combinatorial or discrete restriction terminology remain an originality risk; no exhaustive novelty certification or independent audit has been performed.

## References

- G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234v1 (first submitted 18 April 2002), https://arxiv.org/abs/math/0204234.
- D. Koh and C.-Y. Shen, *Sharp extension theorems and Falconer distance problems for algebraic curves in two dimensional vector spaces over finite fields*, arXiv:1003.4240v1 (22 March 2010), https://arxiv.org/abs/1003.4240.
- *Sharp endpoint extension inequalities for the moment curve on finite fields*, arXiv:2508.08377v1 (11 August 2025), https://arxiv.org/abs/2508.08377.
