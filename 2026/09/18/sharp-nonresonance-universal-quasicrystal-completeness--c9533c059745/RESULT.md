# Sharp nonresonance criterion for universal quasicrystal completeness

## Statement

Let \(d\ge 1\), let \(\alpha,\beta\in\mathbb R^d\), and assume that
\[
1,\alpha_1,\ldots,\alpha_d
\]
are linearly independent over \(\mathbb Q\). For \(n\in\mathbb Z^d\), put
\[
\lambda_n
=
n+\beta\left(\{n\cdot\alpha\}-\frac12\right),
\qquad
\Lambda_{\alpha,\beta}=\{\lambda_n:n\in\mathbb Z^d\}.
\]
Define the integer relation lattice
\[
\mathcal R_{\alpha,\beta}
=
\left\{(t,a)\in\mathbb Z\times\mathbb Z^d:
t(1+\alpha\cdot\beta)=a\cdot\beta\right\}
\]
and the common-phase translation group
\[
\mathcal P(\Lambda_{\alpha,\beta})
=
\left\{v\in\mathbb R^d:
\exists c\in\mathbb T\text{ such that }
e^{2\pi i\lambda\cdot v}=c
\text{ for every }\lambda\in\Lambda_{\alpha,\beta}\right\}.
\]

Then
\[
\boxed{
\mathcal P(\Lambda_{\alpha,\beta})
=
\left\{a-t\alpha:(t,a)\in\mathcal R_{\alpha,\beta}\right\}.
}
\]
The map
\[
(t,a)\longmapsto a-t\alpha
\]
is injective, so \(\mathcal P(\Lambda_{\alpha,\beta})\) is nontrivial exactly when
\[
1+\alpha\cdot\beta,\ \beta_1,\ldots,\beta_d
\]
are linearly dependent over \(\mathbb Q\).

If this rational-independence condition fails, then universal completeness fails at every positive scale: for every \(\varepsilon>0\) there is a bounded measurable set \(S\subset\mathbb R^d\) with
\[
0<|S|<\varepsilon
\]
and a nonzero bounded compactly supported function \(f\) on \(S\) such that
\[
\widehat f(\lambda)=0
\qquad(\lambda\in\Lambda_{\alpha,\beta}).
\]
Consequently \(E(\Lambda_{\alpha,\beta})\) is incomplete in \(L^p(S)\) for every
\(1\le p<\infty\), and the \(L^1\)-uniqueness property also fails on \(S\).

Combining this obstruction with item (1) of Section 6 of Bertolini--Florit-Simon--Liehr--Taylor, which proves universal \(L^1\) uniqueness and \(L^p\) completeness for all \(|S|<1\) when
\[
\|\beta\|_2<\frac12
\quad\text{and}\quad
1+\alpha\cdot\beta,\beta_1,\ldots,\beta_d
\text{ are \(\mathbb Q\)-independent},
\]
gives the exact dichotomy
\[
\boxed{
\begin{array}{c}
\|\beta\|_2<\frac12,\\[2mm]
1,\alpha_1,\ldots,\alpha_d\text{ \(\mathbb Q\)-independent}
\end{array}
\quad\Longrightarrow\quad
\begin{cases}
\text{universal uniqueness/completeness for every }|S|<1,
&\mathcal R_{\alpha,\beta}=\{0\},\\
\text{failure on sets of arbitrarily small positive measure},
&\mathcal R_{\alpha,\beta}\ne\{0\}.
\end{cases}
}
\]

Thus the second rational-independence hypothesis in the higher-dimensional universal-completeness theorem is not merely a sufficient arithmetic condition: it is sharp.

## Exact phase-lock group

We prove both inclusions in the displayed formula for \(\mathcal P\).

### A rational relation produces phase locking

Take \((t,a)\in\mathcal R_{\alpha,\beta}\), so
\[
t(1+\alpha\cdot\beta)=a\cdot\beta,
\]
and set
\[
v=a-t\alpha.
\]
Then
\[
v\cdot\beta
=
a\cdot\beta-t\alpha\cdot\beta
=t.
\]
Therefore
\[
\begin{aligned}
v\cdot\lambda_n
&=
v\cdot n
+t\left(\{n\cdot\alpha\}-\frac12\right)\\
&=
a\cdot n-t\alpha\cdot n
+t(n\cdot\alpha-\lfloor n\cdot\alpha\rfloor)-\frac t2\\
&=
a\cdot n-t\lfloor n\cdot\alpha\rfloor-\frac t2
\in\mathbb Z-\frac t2.
\end{aligned}
\]
Hence
\[
e^{2\pi i v\cdot\lambda_n}=(-1)^t
\]
for every \(n\in\mathbb Z^d\), and \(v\in\mathcal P(\Lambda_{\alpha,\beta})\).

If \(v=0\), then \(a=t\alpha\). Since \(a,t\) are integers and
\(1,\alpha_1,\ldots,\alpha_d\) are \(\mathbb Q\)-independent, this forces
\(t=0\) and \(a=0\). Thus a nontrivial integer relation always gives a nonzero
common-phase translation.

### Every common-phase translation comes from a rational relation

Conversely, let \(v\in\mathcal P(\Lambda_{\alpha,\beta})\). Since
\[
\lambda_0=-\frac{\beta}{2},
\]
the constancy of the phase implies
\[
e^{2\pi i(\lambda_n-\lambda_0)\cdot v}=1
\qquad(n\in\mathbb Z^d).
\]
Put
\[
\tau=v\cdot\beta.
\]
Because
\[
\lambda_n-\lambda_0=n+\beta\{n\cdot\alpha\},
\]
we have
\[
A_n:=v\cdot n+\tau\{n\cdot\alpha\}\in\mathbb Z
\qquad(n\in\mathbb Z^d).
\]

Choose \(n\in\mathbb Z^d\) with
\[
x:=\{n\cdot\alpha\}>\frac12.
\]
Such an \(n\) exists already among \(\pm e_j\): every \(\alpha_j\) is irrational, so its fractional part is neither \(0\) nor \(1/2\), and replacing \(e_j\) by \(-e_j\) if necessary makes the fractional part exceed \(1/2\). Then
\[
\{2n\cdot\alpha\}=2x-1,
\]
and therefore
\[
2A_n-A_{2n}
=
\tau(2x-\{2n\cdot\alpha\})
=
\tau.
\]
The left side is an integer, hence
\[
\tau\in\mathbb Z.
\]

Now \(A_{e_j}\in\mathbb Z\) gives
\[
v_j+\tau\{\alpha_j\}\in\mathbb Z.
\]
Since \(\tau\in\mathbb Z\),
\[
a_j:=v_j+\tau\alpha_j\in\mathbb Z.
\]
Thus \(a=v+\tau\alpha\in\mathbb Z^d\), or
\[
v=a-\tau\alpha.
\]
Finally,
\[
a\cdot\beta
=
(v+\tau\alpha)\cdot\beta
=
\tau(1+\alpha\cdot\beta).
\]
Hence \((\tau,a)\in\mathcal R_{\alpha,\beta}\), proving the reverse inclusion.

This also shows that the phase associated with \(v=a-t\alpha\) is necessarily
\[
c=(-1)^t.
\]

## Resonance forces arbitrarily small nonuniqueness sets

Assume \(\mathcal R_{\alpha,\beta}\ne\{0\}\), and choose the corresponding
\(v\ne0\) and \(c\in\mathbb T\) with
\[
e^{2\pi i\lambda\cdot v}=c
\qquad(\lambda\in\Lambda_{\alpha,\beta}).
\]

Given \(\varepsilon>0\), choose a bounded measurable set \(E\) of positive measure so small that
\[
|E|<\frac{\varepsilon}{2}
\qquad\text{and}\qquad
E\cap(E+v)=\varnothing.
\]
For example, a sufficiently small ball works. Let
\[
S=E\cup(E+v).
\]
Then \(0<|S|<\varepsilon\).

For any nonzero \(g\in L^\infty(E)\), define
\[
f(x)=
\begin{cases}
g(x),&x\in E,\\
-c\,g(x-v),&x\in E+v,\\
0,&x\notin S.
\end{cases}
\]
The function \(f\) is nonzero, bounded, compactly supported, and belongs to
\(L^q(S)\) for every \(1\le q\le\infty\). With the convention
\[
\widehat f(\xi)=\int_{\mathbb R^d}f(x)e^{-2\pi i\xi\cdot x}\,dx,
\]
translation gives
\[
\widehat f(\lambda)
=
\widehat g_E(\lambda)
\left(1-c\,e^{-2\pi i\lambda\cdot v}\right)
=0
\qquad(\lambda\in\Lambda_{\alpha,\beta}),
\]
because \(e^{2\pi i\lambda\cdot v}=c\).

Thus the Fourier-sampling map has a nontrivial kernel on \(L^1(S)\). In fact,
as \(g\) varies, it contains an infinite-dimensional family of such two-copy
cancellations.

For \(1<p<\infty\), the same \(f\in L^{p'}(S)\) defines a nonzero continuous
functional annihilating the span of \(E(\Lambda_{\alpha,\beta})\); for \(p=1\),
use \(f\in L^\infty(S)\). Hence \(E(\Lambda_{\alpha,\beta})\) is incomplete in
every finite-\(p\) space on this \(S\).

## One-dimensional specialization

Let \(d=1\), \(\alpha\notin\mathbb Q\), and \(0<|\beta|<1/2\). Then
\[
1+\alpha\beta,\ \beta
\]
are \(\mathbb Q\)-dependent if and only if
\[
\boxed{
\beta=-\frac{1}{\alpha+r}
\quad\text{for some }r\in\mathbb Q.
}
\]
Indeed, a nontrivial relation
\[
t(1+\alpha\beta)-a\beta=0
\]
has \(t\ne0\), and rearranging gives the formula with \(r=-a/t\).

For the uncentered frequencies
\[
\Lambda^{\mathrm{unc}}_{\alpha,\beta}
=
\left\{n+\beta\{n\alpha\}:n\in\mathbb Z\right\},
\]
which differ from the centered family by the fixed frequency shift \(\beta/2\),
the resonant formula becomes especially transparent. Writing \(r=p/q\) in lowest
terms,
\[
n+\beta\{n\alpha\}
=
-\beta\left(rn+\lfloor n\alpha\rfloor\right)
\in -\frac{\beta}{q}\mathbb Z.
\]
Thus, at resonance, the quasicrystal collapses into a lattice in frequency space.
The centered family lies in the corresponding affine lattice
\[
-\frac{\beta}{q}\mathbb Z-\frac{\beta}{2}.
\]
This explains the common translation phase and the two-copy nonuniqueness
construction directly.

In particular, the rational nonzero values of \(\beta\) used in Theorem 1.1 of
Bertolini--Florit-Simon--Liehr--Taylor are automatically nonresonant: if a
rational \(\beta\ne0\) satisfied the exceptional formula, then \(\alpha\) would
be rational.

## Relation to prior work

Bertolini, Florit-Simon, Liehr, and Taylor prove that under
\[
\|\beta\|_2<\frac12
\]
and the two rational-independence assumptions, \(\Lambda_{\alpha,\beta}\) is
uniformly discrete of density one and is an \(L^1\)-uniqueness set for every
measurable \(S\) with \(|S|<1\); they consequently obtain universal
\(L^p\)-completeness for every \(1\le p<\infty\). Their higher-dimensional
statement explicitly assumes the independence of
\[
1+\alpha\cdot\beta,\beta_1,\ldots,\beta_d.
\]
The inspected version states this as a sufficient hypothesis.

Earlier work of Matei--Meyer and Grepstad--Lev studies stable sampling, Riesz
bases, and bounded-remainder-set phenomena for simple quasicrystals. Those
results establish important arithmetic structure in related frame and sampling
questions, but they concern different target properties from the universal
\(L^1\)-uniqueness statement above.

The new point here is the exact converse for this newly introduced universal
completeness family, together with the explicit identification of the full
common-phase translation group and the zero-scale obstruction in the resonant
case.

## Limitations

- The positive direction uses the universal-completeness theorem of
  Bertolini--Florit-Simon--Liehr--Taylor; only the converse and phase-lock
  characterization are proved here.
- The sharp dichotomy is asserted for their family under
  \(1,\alpha_1,\ldots,\alpha_d\) rationally independent and, for the positive
  direction, \(\|\beta\|_2<1/2\).
- The result concerns uniqueness/completeness, not frame bounds, Riesz-basis
  constants, or stability at critical density.
- No claim is made that rational resonance is the only possible obstruction for
  other cut-and-project families.
- The source preprint is very recent. The current arXiv submission history lists
  only v1, so unindexed contemporaneous observations remain a residual
  originality risk.

## References

1. Susanna Bertolini, Enric Florit-Simon, Lukas Liehr, and Mitchell A. Taylor,
   *Universal completeness of exponentials*, arXiv:2609.20805v1 (2026).
   https://arxiv.org/abs/2609.20805v1
2. Basarab Matei and Yves Meyer, *Simple quasicrystals are sets of stable
   sampling*, Complex Variables and Elliptic Equations 55 (2010), 947--964.
   https://doi.org/10.1080/17476930903394689
3. Sigrid Grepstad and Nir Lev, *Universal sampling, quasicrystals and bounded
   remainder sets*, C. R. Math. Acad. Sci. Paris 352 (2014), 633--638.
   https://doi.org/10.1016/j.crma.2014.06.004
4. Sigrid Grepstad and Nir Lev, *Riesz bases, Meyer's quasicrystals, and bounded
   remainder sets*, Trans. Amer. Math. Soc. 370 (2018), 4273--4298.
   https://doi.org/10.1090/tran/7157
