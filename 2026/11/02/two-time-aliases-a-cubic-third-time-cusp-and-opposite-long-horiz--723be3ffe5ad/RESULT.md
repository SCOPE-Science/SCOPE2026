# Two-time aliases, a cubic third-time cusp, and opposite long-horizon signs for split exponential–Euler maps

## Finding

Consider two positive, directly observed maps at distinct horizons and the ambiguity in attributing their rates to exponential linear evolution and an explicit reaction factor. For the split exponential–Euler family
\[
S_t=e^{t(L+aI)}(I+tbI)=e^{at}(1+bt)e^{tL},
\]
two observed time horizons need not identify \(a\) and \(b\). The complete classification, cubic sensitivity law for the third horizon, and a counterexample to long-horizon sign stability are proved below.

When \(S_h=m_1e^{hL}\) and \(S_{2h}=m_2e^{2hL}\), where \(m_1,m_2>0\), a real realization exists exactly for
\[
m_1>0,\qquad 0<m_2\le m_1^2.
\]
For \(0<m_2<m_1^2\), put \(\Delta=m_1^2-m_2\) and \(z=\sqrt\Delta/m_1\in(0,1)\). There are **exactly two** pairs:
\[
(a_\pm,b_\pm)=\left(\frac{\log[m_1(1\mp z)]}{h},\ \frac{\pm z}{h(1\mp z)}\right).
\]
At a third horizon \(3h\), the two values are
\[
\boxed{m_3^\pm=3m_1m_2-2m_1^3\pm2\Delta^{3/2}}.
\]
In particular their separation is \(4\Delta^{3/2}\), a semicubical data cusp as the two branches merge. **Any** additional nonnegative time different from \(0,h,2h\) uniquely distinguishes the branches.

There is an open region of two-map strict contraction but incompatible direct long-time behavior: if \(1/(1+z)<m_1<1\), the plus branch decays along every mode, whereas the minus branch eventually changes sign and grows exponentially along a zero eigenvector of \(L\). For example, \(m_1=4/5\), \(z=3/5\) gives
\[
m_2=256/625,\qquad m_3^+=2816/15625,\qquad m_3^-=-4096/15625.
\]

## Assumptions and scope

Fix \(h>0\), \(d\ge1\), and a known real symmetric negative-semidefinite \(d\times d\) matrix \(L\). For the long-time instability assertion assume also \(\ker L\ne\{0\}\), as for a periodic discrete heat Laplacian. Let \(a,b\) be unconstrained real coefficients and define the whole **step-size-parametrized direct map** at any real \(t\ge0\) using the formula above. Observed operators are exactly \(m_1e^{hL}\) and \(m_2e^{2hL}\), with \(m_1,m_2>0\); invertibility of every finite matrix exponential allows recovery of both scalar factors from the operator maps. The word contraction refers to the induced Euclidean operator norm.

We do **not** impose the semigroup law \(S_{s+t}=S_sS_t\), and do not identify \(S_{nh}\) with \(S_h^n\). These two distinct tasks give different long-horizon inferences. This theorem treats a Lie-composed, first-order exponential-plus-explicit-reaction **model**, not the higher-order ETDRK4 integrator implemented in the motivating paper.

## Proof

**Algebraic inverse.** Write \(q=e^{ah}>0\) and \(\beta=bh\), so that \(m_1=q(1+\beta)\), \(m_2=q^2(1+2\beta)\). Since \(m_1>0\), necessarily \(1+\beta>0\). Subtract to obtain
\[
m_1^2-m_2=q^2\beta^2\ge0.
\]
The condition \(m_2>0\) requires \(1+2\beta>0\). Thus \(z=\beta/(1+\beta)\in(-1,1)\), \(q=m_1(1-z)\), \(\beta=z/(1-z)\), and
\[
m_2=m_1^2(1-z^2).
\]
Conversely any \(m_1>0\), \(0<m_2\le m_1^2\) yields \(z=\pm\sqrt\Delta/m_1\in(-1,1)\), each producing a valid real \(a\), \(b\), with equality forcing \(z=0\) and the unique solution \(b=0\), \(a=h^{-1}\log m_1\). For strict inequality the two signs are distinct and exhaustive.

**All-time values and the cubic cusp.** For every \(s\ge0\) the direct map at \(sh\) has scalar factor
\[
M(s;z)=m_1^s(1-z)^{s-1}\left[1+(s-1)z\right].
\]
For \(s=3\) a direct binomial expansion gives
\[
M(3;z)=m_1^3(1-3z^2+2z^3),\quad M(3;-z)=m_1^3(1-3z^2-2z^3).
\]
Because \(m_1^2z^2=\Delta\), these are the displayed \(m_3^\pm\). Equivalently,
\[
\left[m_3-3m_1m_2+2m_1^3\right]^2=4(m_1^2-m_2)^3.
\]
For fixed \(m_1\) the two third-time branches meet with the exact \(3/2\)-power separation at \(\Delta=0\). Consequently distinguishing them in additive third-data error \(\epsilon\) requires \(\epsilon\) small relative to \(4\Delta^{3/2}\); this is a deterministic resolution statement, not a statistical lower bound.

**Any different horizon separates.** Suppose two distinct parameters with \(\Delta>0\) agreed at an additional real \(s\). In dimensionless time, their scalar difference is
\[
G(s)=e^{\alpha_+s}(1+\beta_+s)-e^{\alpha_-s}(1+\beta_-s),
\]
with \(\alpha_+\ne\alpha_-\) and \(\beta_+\ne0\). Dividing by \(e^{\alpha_-s}>0\) leaves
\[
H(s)=e^{\lambda s}(1+\beta_+s)-(1+\beta_-s),\quad \lambda=\alpha_+-\alpha_-\ne0.
\]
Its second derivative is \(H''(s)=e^{\lambda s}[\lambda^2(1+\beta_+s)+2\lambda\beta_+]\), which has at most one distinct real zero because the bracket is a nonconstant affine function. Four distinct zeros of \(H\) would force at least two zeros of \(H''\) by two applications of Rolle's theorem. Yet \(0,1,2\) are already zeros. Therefore there is no additional real zero, proving the exact three-horizon uniqueness assertion, including noninteger horizons.

**Sign and instability phase.** For \(z>0\), the plus factor has \(q_+=m_1(1-z)>0\) and \(\beta_+=z/(1-z)>0\), so \(M(s;z)>0\) for every \(s\ge0\). The minus factor has \(q_-=m_1(1+z)>0\) and \(\beta_-=-z/(1+z)<0\); hence it crosses zero exactly at
\[
s_*=\frac{1+z}{z}=1+\frac1z>2
\]
and is strictly negative for every \(s>s_*\). Under \(1/(1+z)<m_1<1\), \(q_- >1\) while \(q_+<1\). The plus multiplier then tends to zero and the negative multiplier tends to minus infinity as \(s\to\infty\). Because \(L\preceq0\), \(\|e^{hL}\|_2\le1\) and \(\|e^{2hL}\|_2\le1\); \(m_1,m_2<1\) make both observed maps strict contractions. On any \(v\in\ker L\setminus\{0\}\), \(e^{shL}v=v\), so the opposite long-time scalar behavior is realized by actual vectors.

**Exact witness.** Let \(m_1=4/5\), \(z=3/5\), \(h>0\). Both branches have \(m_2=m_1^2(1-z^2)=256/625\). The pairs are \(e^{a_+h}=8/25\), \(b_+h=3/2\), and \(e^{a_-h}=32/25\), \(b_-h=-3/8\). At \(3h\), their scalar outputs are \(2816/15625\) and \(-4096/15625\), respectively. These are exact rational equalities and persist with active nonconstant diffusive modes because \(e^{shL}\) is a shared invertible factor.

## Verification

Run `python verify.py` from the package directory. The standalone standard-library checker tests 22,426 exact-rational identities and direct floating evaluations, including all-parameter candidate formulas, the cubic discriminant, the rational witness and a three-node heat semigroup. Numerical checks are illustrations and consistency tests; the proof of the infinite-time statements and universal quantifiers is the analytical argument above. No external dependencies are needed.

## Relationship to prior work

Marques and collaborators (2026, arXiv:2609.31539v1, first posted 2026-09-25) motivate exponential integration with a learned remainder and point out that allocating linear terms to the exponential part is partly a modeling convention; their inverse PDE applications motivate the identifiability question. **Their implemented method is higher-order ETDRK4, not the first-order split map analyzed here.** Thus the theorem does not assert a failure of their algorithm or of its training scheme. Batenkov and Yomdin (2011 preprint, arXiv:1106.1137v3) treat general confluent Prony systems, including exponentials multiplied by polynomials, and their general reconstruction framework is relevant to our uniqueness discussion. The claim here is the exact positive two-horizon inverse classification, its explicit cubic separation, and the split-map sign/growth discrepancy; it does not claim the underlying exponential-polynomial representation or general Prony reconstruction as new.

## Limitations

This is a deterministic exact-data result for an affine-reaction scalar subclass with known finite-dimensional \(L\), not a general nonlinear neural operator, spatially variable reaction, ETDRK4 method, or noisy inverse problem. No positive-data semigroup realizability is asserted: whenever \(m_2<m_1^2\), the pair cannot itself be the exact autonomous continuous semigroup of one fixed scalar generator, because semigroup factors would satisfy \(m_2=m_1^2\). The long-time divergence applies to one-step maps **evaluated directly with a long time argument**; iterating the common \(h\)-step map gives the same stable evolution for both parameter choices. Historical priority for closely related specialized algebraic formulations remains unverified.

## References

- M. Marques, L. Mendonça, L. M. Moreira, C. J. de Oliveira, V. Balestro, T. Novello, D. Yukimura, P. Petrov, L. Nissenbaum, *NEXT: Physics-Informed Neuro-Spectral Exponential Time Differencing Architectures*, arXiv:2609.31539v1, posted 2026-09-25. https://arxiv.org/abs/2609.31539
- D. Batenkov, Y. Yomdin, *On the Accuracy of Solving Confluent Prony Systems*, arXiv:1106.1137v3, 2011 preprint. https://arxiv.org/abs/1106.1137
