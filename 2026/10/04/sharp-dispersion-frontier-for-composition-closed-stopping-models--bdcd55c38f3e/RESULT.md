# Sharp dispersion frontier for composition-closed stopping models
## Finding
Consider a positive-integer-valued family \(\{{N_\theta:0<\theta\le1}}\) whose probability generating functions satisfy
\[
h_{{\theta_1}}\!\circ h_{{\theta_2}}=h_{{\theta_1\theta_2}},\qquad h_1(t)=t,
\]
and whose canonical parameter is \(\theta=\Pr(N_\theta=1)\). The dual representation of Valero and Ginebra associates to such a family a positive-integer-valued random variable \(J\) with pgf \(\phi\). If
\[
a=\mathbb E[J]<\infty,\qquad \mathbb E[J^2]<\infty,
\]
then, for every \(0<\theta\le1\),
\[
\mathbb E[N_\theta]=\theta^{{-a}},\qquad
\operatorname{{Var}}(N_\theta)=\kappa\,\mathbb E[N_\theta]\bigl(\mathbb E[N_\theta]-1\bigr),
\qquad
\kappa=\frac{{\mathbb E[J^2]}}{{\mathbb E[J]}}.
\]

This reduces the entire mean--variance curve to two moments of the dual law. Moreover, the dispersion coefficient has an exact sharp frontier at fixed mean-growth exponent. Write
\[
q=\lfloor a\rfloor,\qquad \delta=a-q\in[0,1).
\]
Then
\[
\kappa\ge \kappa_{{\min}}(a)
= a+\frac{{\delta(1-\delta)}}{a}.
\]
Equality holds if and only if \(J\) is supported on \(\{{q,q+1}}\) with probabilities \(1-\delta\) and \(\delta\), with the evident one-point interpretation when \(\delta=0\). For \(a>1\), every value \(\kappa\ge\kappa_{{\min}}(a)\) is attainable by some admissible dual law. When \(a=1\), positivity forces \(J\equiv1\), so the only possible value is \(\kappa=1\).

Equivalently, among all composition-closed stopping models having the same expectation exponent \(a\), the adjacent-two-point dual law gives the unique least-variable family at every nontrivial parameter value. The limiting squared coefficient of variation is also sharp:
\[
\lim_{{\theta\downarrow0}}\frac{{\operatorname{{Var}}(N_\theta)}}{{\mathbb E[N_\theta]^2}}=\kappa,
\]
so \(\kappa_{{\min}}(a)\) is the exact asymptotic relative-dispersion floor.

## Assumptions and scope
The family is assumed to be in the identity-containing composition-closed class characterized by Theorem 5 of Valero and Ginebra, so its dual \(\phi\) is the pgf of a random variable supported on the positive integers. The finite-second-moment assumption on \(J\) is essential for the finite variance formula. No finite-variance assertion is made when \(\mathbb E[J^2]=\infty\).

The claim concerns the distribution of the stopping count \(N_\theta\), not the distribution obtained after using \(N_\theta\) to stop some other stochastic process. It is a structural statement about the stopping-model family itself.

## Proof
Set \(s=-\log\theta\) and \(H_s(t)=h_{{e^{{-s}}}}(t)\). The source's differential identity for the canonical family is
\[
\partial_\theta h_\theta(t)=\frac{{h_\theta(t)\bigl(1-\phi(h_\theta(t))\bigr)}}{\theta}.
\]
Therefore
\[
\partial_s H_s(t)=H_s(t)\bigl(\phi(H_s(t))-1\bigr),\qquad H_0(t)=t.
\]
Let \(a=\phi'(1)=\mathbb E[J]\) and \(b=\phi''(1)=\mathbb E[J(J-1)]\). Since \(H_s(1)=1\), differentiation once with respect to \(t\) gives, for \(m(s)=H_s'(1)=\mathbb E[N_{{e^{{-s}}}}]\),
\[
m'(s)=a\,m(s),\qquad m(0)=1.
\]
Hence \(m(s)=e^{{as}}\), or \(\mathbb E[N_\theta]=\theta^{{-a}}\).

Differentiate twice with respect to \(t\). Writing
\[
f(s)=H_s''(1)=\mathbb E\!\left[N_{{e^{{-s}}}}\bigl(N_{{e^{{-s}}}}-1\bigr)\right],
\]
one obtains
\[
f'(s)=a f(s)+(2a+b)m(s)^2,\qquad f(0)=0.
\]
Solving this linear equation and using \(m(s)=e^{{as}}\) yields
\[
f(s)=\frac{{2a+b}}{a}\,m(s)\bigl(m(s)-1\bigr).
\]
Since \(\operatorname{{Var}}(N)=\mathbb E[N(N-1)]+\mathbb E[N]-\mathbb E[N]^2\),
\[
\operatorname{{Var}}(N_\theta)
=\left(1+\frac{b}{a}\right)m(m-1)
=\frac{{\mathbb E[J^2]}}{{\mathbb E[J]}}m(m-1).
\]

It remains to optimize the dual second moment at fixed \(a\). For every positive integer \(j\),
\[
(j-q)(j-q-1)\ge0.
\]
Taking expectations gives
\[
\mathbb E[J^2]-(2q+1)a+q(q+1)\ge0.
\]
With \(a=q+\delta\), the right side rearranges to
\[
\mathbb E[J^2]\ge a^2+\delta(1-\delta).
\]
Equality in the pointwise inequality occurs exactly at \(j=q\) or \(j=q+1\), proving the stated equality characterization and the lower bound for \(\kappa\).

For attainability, the lower endpoint is realized by the adjacent-two-point dual distribution. If \(a>1\), choose any integer \(M>a\) and the two-point law on \(\{{1,M}}\) with
\[
\Pr(J=M)=\frac{{a-1}}{{M-1}}.
\]
Its mean is \(a\), while its second moment diverges as \(M\to\infty\). Mixing this law with the lower-endpoint law preserves the mean \(a\) and continuously interpolates the second moment. Thus every \(\kappa\ge\kappa_{{\min}}(a)\) is attained. Theorem 5 of the source turns each such positive-integer dual pgf into a valid composition-closed family. For \(a=1\), the constraint \(J\ge1\) forces \(J=1\) almost surely.

For integer \(a=q\), the lower-endpoint dual is \(\phi(t)=t^q\). Direct integration gives the explicit extremal family
\[
h_\theta(t)=\frac{{\theta t}}{{\left(1-(1-\theta^q)t^q\right)^{{1/q}}}},
\]
which has mean \(\theta^{{-q}}\) and variance \(q\theta^{{-q}}(\theta^{{-q}}-1)\).

## Verification
A standalone exact-rational checker accompanies this note. It verifies the discrete second-moment inequality and its equality cases on broad finite grids of rational means, checks exact interpolation to prescribed dispersion coefficients by mean-preserving mixtures, verifies the explicit integer-extremal composition identity through rational substitution in the transformed variable \(z=t^q\), and checks the geometric dual special case used in the source's examples. These computations test algebraic consequences but are not substitutes for the general proof above.

## Relationship to prior work
Valero and Ginebra characterize the identity-containing composition-closed stopping families by positive-integer dual pgfs and give the differential representation from which the moment equations are derived. They also note that this is a reformulation of classical embeddability of Galton--Watson laws into continuous-time branching processes and cite the two 1968 papers of Karlin and McGregor. The inspected source does not state a general mean--variance formula in the canonical singleton-probability parameter, nor the sharp adjacent-two-point dispersion frontier, equality classification, or full attainable range at fixed exponent.

Classical branching-process theory contains general moment evolution equations, so those equations themselves are not claimed as new. The contribution asserted here is the combination specific to this canonical composition-closed class: the exact invariant \(\kappa=\mathbb E[J^2]/\mathbb E[J]\), its translation into the whole \(\theta\)-indexed mean--variance curve, and the sharp optimization of \(\kappa\) over all positive-integer dual laws with fixed \(\mathbb E[J]=a\).

## Limitations
The proof requires \(\mathbb E[J^2]<\infty\) for a finite variance. The source contains examples with heavier dual tails; those lie outside this finite-dispersion statement. The originality search did not obtain full text for the 1968 Karlin--McGregor papers, so an equivalent extremal formulation under older branching-process terminology remains a residual literature risk. No claim is made about higher moments, tail order, stochastic order, or optimality under constraints other than fixed dual mean.

## References
1. Jordi Valero and Josep Ginebra, *Stopping models closed under pgf composition, and the stability of randomly stopped model extensions*, arXiv:2609.30106v1, first public version 2026-09-24. Primary MSC2020: 62E10.
2. Samuel Karlin and James McGregor, *Embedding Iterates of Analytic Functions with Two Fixed Points into Continuous Groups*, Transactions of the American Mathematical Society 132 (1968), DOI 10.2307/1994886.
3. Samuel Karlin and James McGregor, *Embeddability of discrete-time simple branching processes into continuous-time branching processes*, Transactions of the American Mathematical Society 132 (1968), DOI 10.2307/1994885.
