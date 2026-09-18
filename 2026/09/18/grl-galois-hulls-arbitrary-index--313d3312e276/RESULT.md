# Full-field generalized Roth--Lempel Galois hulls for arbitrary indices

## Statement

Let \(q=p^e>4\), let \(1\le \ell\le e-1\), and put \(Q=p^\ell\). Let \(1\le s<k\) and consider generalized Roth--Lempel (GRL) codes whose evaluation vector consists of every element of \(\mathbb F_q\).

**Theorem.** For every
\[
  s<k\le \left\lfloor\frac{q+Q}{Q+1}\right\rfloor
  \quad\text{and}\quad
  0\le h\le k-s,
\]
there is a \([q+s,k]_q\) GRL code \(C\) with
\[
  \dim \operatorname{Hull}_\ell(C)=h.
\]
If \((Q+1)k<q+Q\), the extension matrix \(A_s\in\mathrm{GL}_s(\mathbb F_q)\) can be prescribed arbitrarily. If \((Q+1)k=q+Q\), a scalar extension matrix \(A_s=\mu I_s\) with \(\mu^{Q+1}\ne1\) suffices.

In particular, for \(s=2\), every
\[
  3\le k\le \left\lfloor\frac{q+Q}{Q+1}\right\rfloor,
  \qquad 0\le h\le k-2,
\]
admits an AMDS (and hence NMDS) GRL code
\[
  \boxed{[q+2,k,q-k+2]_q}
\]
with \(\ell\)-Galois hull dimension \(h\). Consequently there is an EAQECC
\[
  \boxed{[[q+2,k-h,q-k+2;\ q+2-k-h]]_q}.
\]
No assumption \(\ell\mid e\) or \(2\ell\mid e\) is required.

## Context

Wu, Liu, Chen and Zhou, *Galois Hulls of Generalized Roth-Lempel Codes and Their Applications to EAQECCs* (arXiv:2609.20453v1, 17 September 2026), develop a general GRL hull construction. Their paper works throughout its main constructions under \(q=p^e>4\), \(\ell>0\), and \(2\ell\mid e\). Their Lemma II.9 supplies \((p^\ell+1)\)-st roots for normalized Lagrange coefficients under divisibility hypotheses, and their Theorem IV.6 gives full-evaluation \([q+2,k,q-k+2]_q\) AMDS/NMDS GRL codes with prescribed hulls under \(2\ell\mid e\).

The full evaluation set has a special normalization that removes the root-existence obstruction completely: every Lagrange coefficient is \(-1\), so choosing the normalizing scalar \(\lambda=-1\) makes every required base multiplier power equal to \(1\). This works for every Galois index \(1\le\ell\le e-1\), even when \(\ell\nmid e\).

## Proof

Let the evaluation points be all \(a\in\mathbb F_q\). For
\[
  P(x)=\prod_{a\in\mathbb F_q}(x-a)=x^q-x,
\]
we have \(P'(a)=-1\). Hence the Lagrange coefficient used in the GRL dual description is
\[
  u_a=\prod_{b\ne a}(a-b)^{-1}=-1
\]
for every \(a\).

Write a message polynomial as
\[
  f(x)=\sum_{j=0}^{k-1}f_jx^j,
\]
and recall the GRL hull criterion (Proposition II.8 of arXiv:2609.20453): a codeword represented by \(f\) is in the \(\ell\)-Galois hull exactly when there exists \(g\) of degree at most \(q-k+s-1\) such that
\[
  v_a^{Q+1}f^Q(a)=u_ag(a)
\]
for every evaluation point, together with the coefficient-tail relation involving \(A_s\).

Choose \(\beta\in\mathbb F_q^*\) with
\[
  \gamma:=\beta^{Q+1}\ne1.
\]
Such a \(\beta\) always exists for \(q>4\): otherwise every element of \(\mathbb F_q^*\) would satisfy \(x^{Q+1}=1\), forcing \(q-1\mid Q+1\); but \(q-1>Q+1\) for \(1\le\ell<e\), except for the excluded case \(q=4\).

For a requested hull dimension \(h\), set
\[
  z=k-s-h.
\]
Give any chosen \(z\) evaluation coordinates multiplier \(\beta\), and give the other \(q-z\) coordinates multiplier \(1\).

### Strict range

Assume \((Q+1)k<q+Q\), equivalently
\[
  Q(k-1)<q-k.
\]
On each unscaled coordinate the hull equation is
\[
  f^Q(a)=-g(a).
\]
The polynomial \(g+f^Q\) has degree at most \(q-k+s-1\), while it vanishes on the \(q-z=q-k+s+h\) unscaled evaluation points. Therefore
\[
  g=-f^Q.
\]
Since \(\deg f^Q<q-k\), the relevant coefficient tail of \(g\) is zero. The coefficient-tail equation and nonsingularity of the prescribed \(A_s\) force
\[
  f_{k-s}=\cdots=f_{k-1}=0.
\]
At each scaled coordinate the evaluation equation becomes
\[
  \gamma f^Q(a)=f^Q(a),
\]
so \(f(a)=0\). Thus every hull polynomial is divisible by the \(z\) selected linear factors and has degree at most \(k-s-1\). The space of such polynomials has dimension
\[
  (k-s)-z=h.
\]
Conversely every such polynomial satisfies the hull equations with \(g=-f^Q\). Hence the hull dimension is exactly \(h\).

### Boundary range

Now assume
\[
  Q(k-1)=q-k,
\]
which is the only additional case permitted by
\(k\le\lfloor(q+Q)/(Q+1)\rfloor\). The same root count still gives \(g=-f^Q\), but \(g_{q-k}=-f_{k-1}^Q\) can now be nonzero.

Take \(A_s=\mu I_s\) with \(\mu^{Q+1}\ne1\). In the notation of the GRL dual formula, \(B_s=-T_s(A_s^{-1})^T\), and the first row of \(T_s\) is \((0,\ldots,0,1)\). The coefficient-tail equation reduces to
\[
  \mu^{Q+1}(f_{k-s}^Q,\ldots,f_{k-1}^Q)
  =f_{k-1}^Q(0,\ldots,0,1).
\]
Therefore
\[
  f_{k-s}=\cdots=f_{k-2}=0,
  \qquad
  (\mu^{Q+1}-1)f_{k-1}^Q=0,
\]
and hence again all top \(s\) coefficients vanish. The scaled-coordinate argument and converse are then identical to the strict case, giving hull dimension \(h\).

This proves the theorem.

## AMDS/NMDS specialization for \(s=2\)

For \(s=2\), write
\[
  A_\zeta=\begin{pmatrix}0&1\\1&\zeta\end{pmatrix}.
\]
Corollary IV.2 of arXiv:2609.20453 states that \(\mathrm{GRL}_k(a,v,A_\zeta)\) is AMDS/NMDS exactly when \(\zeta\) belongs to the set \(\Delta_{k-1}(a)\) of sums of \(k-1\) distinct evaluation points; the criterion is independent of the nonzero evaluation multipliers.

In the strict range, \(A_2\) is arbitrary, so choose any \(\zeta\in\Delta_{k-1}(\mathbb F_q)\), which is nonempty.

At the boundary, \((Q+1)k=q+Q\), so
\[
  k-1=\frac{q-1}{Q+1}.
\]
For \(k\ge3\), the multiplicative subgroup of \(\mathbb F_q^*\) of order \(k-1\) has sum zero. Thus \(0\in\Delta_{k-1}(\mathbb F_q)\). For the required scalar matrix \(A_2=\mu I_2\), Proposition IV.1 then gives the AMDS/NMDS distance \(q-k+2\). Hence the AMDS/NMDS corollary holds throughout the stated range.

Finally, Proposition VI.2 of the same paper is valid for every \(0\le\ell\le e-1\): an \([n,k,d]_q\) code with \(\ell\)-Galois hull dimension \(h\) yields an \([[n,k-h,d;n-k-h]]_q\) EAQECC. Applying it gives the displayed quantum parameters.

## Concrete checks

A standalone finite-field verifier is included in `artifacts/verify_examples.py`.

* Over \(\mathbb F_8\), take \(e=3\), \(\ell=1\). Here \(2\ell\nmid e\). For \(k=3,s=2\), the construction gives both hull dimensions \(h=0,1\). With \(\zeta=1\), exhaustive enumeration gives \([10,3,7]_8\) AMDS/NMDS codes. With \(\zeta=0\), it gives \([10,3,8]_8\) MDS codes.
* Over \(\mathbb F_{27}\), take \(e=3\), \(\ell=2\). Here even \(\ell\nmid e\). For \(k=3,s=2\), exhaustive enumeration gives \([29,3,26]_{27}\) AMDS/NMDS codes with hull dimensions \(h=0,1\).

The finite checks are consistency tests; the theorem is proved algebraically above.

## Originality and relation to prior work

The novelty claim is limited to the full-evaluation GRL construction above: prescribed \(\ell\)-Galois hulls, and the resulting length-\(q+2\) AMDS/NMDS family, for every Galois index without divisibility assumptions on \(\ell\) and \(e\).

This is not a claim that arbitrary-index Galois hulls are new in general. Wan and Zhu (arXiv:2412.05011) treat all Galois indices for GRS/EGRS MDS constructions and obtain MDS codes with arbitrary hull dimensions. Earlier Roth--Lempel-type work includes Hermitian-hull constructions, notably Sok (arXiv:2207.07792) and Liu--Wu--Zhou (arXiv:2604.11350). The distinction here is the generalized Roth--Lempel full-evaluation family of length \(q+s\), especially the \(q+2\) AMDS/NMDS family, at Galois indices excluded by the divisibility hypothesis in arXiv:2609.20453v1.

Targeted searches by title, code family, Galois-hull terminology, arbitrary/all Galois index, full evaluation, and equivalent parameter statements did not locate this extension before this record. Because the motivating preprint appeared on 17 September 2026, a near-simultaneous observation or later revision is a material residual originality risk. Originality is therefore asserted only to the best of our knowledge.

## Limitations

* The theorem uses the full evaluation set \(\mathbb F_q\); it does not remove divisibility hypotheses from all six evaluation-set constructions in arXiv:2609.20453.
* The largest boundary value of \(k\), when equality \((Q+1)k=q+Q\) occurs, uses a scalar extension matrix rather than an arbitrary prescribed \(A_s\).
* The result does not claim novelty for the general theory of Galois hulls of GRS/EGRS codes or for Hermitian Roth--Lempel hulls already studied in earlier work.
* No independent validation is asserted.

## References

1. X. Wu, Q. Liu, Y. Chen, H. Zhou, **Galois Hulls of Generalized Roth-Lempel Codes and Their Applications to EAQECCs**, arXiv:2609.20453v1 (2026). https://arxiv.org/abs/2609.20453
2. R. Wan, S. Zhu, **Galois self-orthogonal MDS codes with large dimensions**, arXiv:2412.05011 (2024). https://arxiv.org/abs/2412.05011
3. Q. Liu, X. Wu, H. Zhou, **Generalized Roth--Lempel Codes: NMDS Characterization, Hermitian Self-Orthogonality, and Quantum Constructions**, arXiv:2604.11350 (2026). https://arxiv.org/abs/2604.11350
4. L. Sok, **Hulls of special typed linear codes and constructions of new EAQECCs**, arXiv:2207.07792 (2022). https://arxiv.org/abs/2207.07792
