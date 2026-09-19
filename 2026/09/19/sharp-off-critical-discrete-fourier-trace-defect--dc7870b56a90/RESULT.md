# Sharp off-critical powers for discrete Fourier trace defects

## Result

Let \(d\ge 1\), let \(0<\gamma,\eta\le 1\), and assume
\(\gamma\ne\eta\). For a finite \(\Omega\subset\mathbb Z^d\) and a measurable
\(S\subset\mathbb T^d\), write
\[
T_{\Omega,S}=P_\Omega B_S P_\Omega,\qquad
D(\Omega,S)=\operatorname{tr}(T_{\Omega,S}-T_{\Omega,S}^2).
\]

For every such pair \((\gamma,\eta)\), there exist a bounded measurable set
\(F\subset\mathbb R^d\), with \(0<|F|<\infty\), and a measurable
\(S\subset\mathbb T^d\), with \(0<|S|<1\), such that

- \(F\) satisfies an upper Minkowski-neighborhood estimate with exponent
  \(\gamma\);
- \(\operatorname{Per}^{\mathbb T}_\eta(S)<\infty\); and
- for a sequence \(R_j\to\infty\),
\[
D\bigl((R_jF)\cap\mathbb Z^d,S\bigr)
 \gtrsim_{\gamma,\eta,d,F,S}
 R_j^{\,d-\min\{\gamma,\eta\}}.
\]

Consequently, the powers in the two off-critical cases of Mayeli's
discretized trace-defect theorem are sharp:
\[
R^{d-\eta}\quad(\gamma>\eta),\qquad
R^{d-\gamma}\quad(\gamma<\eta).
\]
The lower bounds already occur with the smoother member of the spatial/spectral
pair chosen to be a box. Thus the obstruction is carried entirely by the
rougher exponent.

This answers the off-critical part of Remark 9.4 of Mayeli,
*Trace-defect bounds for discrete Fourier concentration operators*,
arXiv:2609.12226v1. The critical problem
\(0<\gamma=\eta<1\), including the possible logarithmic factor, is not addressed.

## Background identity

For
\[
K_S(k)=\int_S e^{2\pi i k\cdot\xi}\,d\xi,
\]
Mayeli proves the exact identity
\[
D(\Omega,S)
 =\frac12\sum_{k\in\mathbb Z^d}
 |K_S(k)|^2\,\#\bigl(\Omega\triangle(\Omega-k)\bigr).
\tag{1}
\]
The same paper proves, for \(\Omega_R=(RF)\cap\mathbb Z^d\),
\[
D(\Omega_R,S)\lesssim
\begin{cases}
R^{d-\eta},&\gamma>\eta,\\
R^{d-\gamma},&\gamma<\eta,
\end{cases}
\tag{2}
\]
under the hypotheses used above. It explicitly leaves the sharpness of both
off-critical powers open.

We construct examples attaining (2).

## A rough set at every fractional exponent

We first record a one-dimensional construction.

### Lemma

For every \(0<\alpha<1\), there is an open set
\(E_\alpha\subset(0,1)\), an integer \(q\ge 3\), and positive constants
\(c,C\) with the following properties.

1. If \(C_\alpha=\partial E_\alpha\), then
\[
c r^\alpha\le |(C_\alpha)_r|\le C r^\alpha
\qquad(0<r<r_0).
\tag{3}
\]
2. For every odd positive integer \(\ell\), with
\(h_\ell=q^{-\ell}\),
\[
|E_\alpha\triangle(E_\alpha+h_\ell)|
 \ge c h_\ell^\alpha.
\tag{4}
\]
Here and below translation can be taken on the line, or modulo \(1\) when
\(E_\alpha\) is regarded as a subset of \(\mathbb T\).
3. For every odd \(\ell\), with \(R_\ell=q^{\ell+1}\) and
\[
\Omega_\ell=(R_\ell E_\alpha)\cap\mathbb Z,
\]
one has
\[
\#\bigl(\Omega_\ell\triangle(\Omega_\ell-1)\bigr)
 \ge c R_\ell^{1-\alpha}.
\tag{5}
\]

In particular,
\[
\operatorname{Per}^{\mathbb T}_\alpha(E_\alpha)<\infty,
\tag{6}
\]
and the exponent \(\alpha\) is genuinely attained: neither the
Minkowski-neighborhood estimate nor the translation estimate can be improved
to any larger exponent.

### Construction and proof of the lemma

Put \(\delta=1-\alpha\). Choose \(q\) so large that
\[
a:=\lfloor q^\delta\rfloor\ge2,\qquad
b:=a+1\le q/3.
\]
If \(q^\delta=a\), set \(p=0\). Otherwise choose \(p\in(0,1)\) from
\[
(1-p)\log a+p\log b=\delta\log q.
\]
Let
\[
\varepsilon_\ell=\lfloor p\ell\rfloor-\lfloor p(\ell-1)\rfloor\in\{0,1\},
\qquad
m_\ell=
\begin{cases}
b,&\varepsilon_\ell=1,\\
a,&\varepsilon_\ell=0.
\end{cases}
\]
Then, with \(M_\ell=\prod_{j=1}^{\ell}m_j\),
\[
M_\ell\asymp q^{\delta\ell},
\tag{7}
\]
because the number of \(b\)'s among the first \(\ell\) levels differs from
\(p\ell\) by less than one.

Construct a \(q\)-adic Moran set. At level \(\ell\), subdivide every surviving
interval into \(q\) equal children and retain the \(m_\ell\) children whose
digits are
\[
D_\ell=\{0,2,4,\ldots,2(m_\ell-2),q-1\}.
\]
The set \(D_\ell\) has \(m_\ell\) elements, contains both endpoint children,
and consecutive retained children are separated by at least one discarded
child. Let \(C_\alpha\) be the limiting compact set.

At level \(\ell\), \(C_\alpha\) is covered by \(M_\ell\) intervals of length
\(q^{-\ell}\), separated at that scale. Hence, whenever
\(q^{-(\ell+1)}<r\le q^{-\ell}\),
\[
|(C_\alpha)_r|\asymp M_\ell r
\quad\text{up to fixed \(q\)-dependent constants,}
\]
and (7) gives (3). More explicitly, the upper bound follows by enlarging all
level-\(\ell\) intervals, while the lower bound follows by placing disjoint
subintervals of length comparable to \(r\) around one endpoint from each
level-\(\ell\) interval.

Let \(\mathcal G_\ell\) be the connected open gaps created between consecutive
retained children at level \(\ell\). Their number is
\[
G_\ell=(m_\ell-1)M_{\ell-1}\asymp M_\ell
 \asymp q^{\delta\ell},
\tag{8}
\]
and every such gap has length at least \(q^{-\ell}\). Since the endpoint
children are always retained, all endpoints of these gaps belong to
\(C_\alpha\).

Define
\[
E_\alpha=
\bigcup_{\substack{\ell\ge1\\ \ell\ {\rm odd}}}
\ \bigcup_{G\in\mathcal G_\ell}G.
\tag{9}
\]
Odd- and even-level gaps both accumulate at every point of \(C_\alpha\), so
\(\partial E_\alpha=C_\alpha\). Also \(0<|E_\alpha|<1\).

Fix an odd \(\ell\), put \(h=q^{-\ell}\), and take a level-\(\ell\) gap.
The level-\(\ell\) retained child immediately to its left is an interval
\(I\) of length \(h\), and the first subinterval \(J\) of length \(h\) inside
the gap is contained in \(E_\alpha\). Because level \(\ell+1\) is even,
all parts of \(E_\alpha\) lying inside \(I\) are contained in the
\(m_{\ell+1}\) retained children at the next level. Therefore
\[
|E_\alpha\cap I|
 \le \frac{m_{\ell+1}}q\,h\le \frac h3.
\]
For at least \(2h/3\) of the points \(x\in J\), one has
\(x-h\notin E_\alpha\). Summing over the \(G_\ell\) disjoint gaps gives
\[
|E_\alpha\triangle(E_\alpha+h)|
 \ge \frac23G_\ell h
 \gtrsim q^{\delta\ell}q^{-\ell}
 =h^\alpha,
\]
which proves (4). Conversely,
\[
E_\alpha\triangle(E_\alpha+h)
 \subset (C_\alpha)_{|h|}
\]
for sufficiently small \(h\), and (3) gives the matching upper
\(O(|h|^\alpha)\), proving (6).

For the lattice statement, take \(R=q^{\ell+1}\). Every endpoint of a
level-\(\ell\) gap becomes an integer after scaling by \(R\), and every such
gap has scaled length at least \(q\). If \(A\) is its left endpoint after
scaling, then
\[
A\notin R E_\alpha,\qquad A+1\in R E_\alpha.
\]
Thus \(A\in(\Omega_\ell-1)\setminus\Omega_\ell\). The \(G_\ell\) left
endpoints are distinct, so
\[
\#(\Omega_\ell\triangle(\Omega_\ell-1))
 \ge G_\ell
 \asymp q^{\delta\ell}
 \asymp R^{1-\alpha}.
\]
This proves (5) and the lemma.

## The regime \(\gamma<\eta\)

Take
\[
F=E_\gamma\times[0,1)^{d-1},
\qquad
S=(-1/4,1/4)^d\subset\mathbb T^d.
\]
The product boundary estimate and (3) give
\[
|(\partial F)_r|\lesssim r^\gamma+r\lesssim r^\gamma.
\]
The box \(S\) has Lipschitz boundary and therefore
\(\operatorname{Per}^{\mathbb T}_\eta(S)<\infty\) for every
\(0<\eta\le1\).

For the sequence \(R=R_\ell=q^{\ell+1}\), \(\ell\) odd, the lattice set is a
Cartesian product and (5) gives
\[
\#\bigl(\Omega_R\triangle(\Omega_R-e_1)\bigr)
 =R^{d-1}
 \#\bigl(((R E_\gamma)\cap\mathbb Z)
       \triangle(((R E_\gamma)\cap\mathbb Z)-1)\bigr)
 \gtrsim R^{d-\gamma}.
\tag{10}
\]
Moreover
\[
K_S(e_1)
 =\left(\int_{-1/4}^{1/4}e^{2\pi i\xi}\,d\xi\right)
   |(-1/4,1/4)|^{d-1}
 =\frac1\pi\,2^{-(d-1)}\ne0.
\]
Keeping only \(k=e_1\) in (1) yields
\[
D(\Omega_R,S)\gtrsim R^{d-\gamma}.
\tag{11}
\]
This matches the \(\gamma<\eta\) upper power.

## The regime \(\gamma>\eta\)

Take
\[
F=[0,1)^d,\qquad
S=E_\eta\times(-1/4,1/4)^{d-1},
\]
where \(E_\eta\) is regarded modulo \(1\) in the first torus coordinate.
The cube \(F\) satisfies the upper Minkowski estimate with every exponent
\(0<\gamma\le1\), since \(O(r)\le O(r^\gamma)\) for \(0<r\le1\).
The product boundary estimate and (3), or directly (6), give
\[
\operatorname{Per}^{\mathbb T}_\eta(S)<\infty.
\]

First consider one dimension. For
\[
\Omega_N=\{0,1,\ldots,N-1\}
\]
the exact identity (1) becomes
\[
D(\Omega_N,E_\eta)
 =\sum_{m\in\mathbb Z}|K_{E_\eta}(m)|^2\min(N,|m|).
\tag{12}
\]
Parseval gives
\[
|E_\eta\triangle(E_\eta-h)|
 =\sum_{m\in\mathbb Z}
 |e^{2\pi i m h}-1|^2|K_{E_\eta}(m)|^2.
\tag{13}
\]
At \(h=1/N\),
\[
|e^{2\pi i m/N}-1|^2
 \le 4\pi^2\min\{1,m^2/N^2\}
 \le 4\pi^2\min\{1,|m|/N\}.
\]
Combining (12) and (13),
\[
D(\Omega_N,E_\eta)
 \ge \frac{N}{4\pi^2}
 |E_\eta\triangle(E_\eta-1/N)|.
\tag{14}
\]
For \(N=q^\ell\) with \(\ell\) odd, (4) gives
\[
D(\Omega_N,E_\eta)\gtrsim N^{1-\eta}.
\tag{15}
\]

For the \(d\)-dimensional cube
\(\Omega_N=\{0,\ldots,N-1\}^d\), retain in (1) only frequencies
\(k=me_1\). Then
\[
\#\bigl(\Omega_N\triangle(\Omega_N-me_1)\bigr)
 =2N^{d-1}\min(N,|m|)
\]
and
\[
K_S(me_1)=2^{-(d-1)}K_{E_\eta}(m).
\]
Consequently,
\[
D(\Omega_N,S)
 \ge 2^{-2(d-1)}N^{d-1}D(\{0,\ldots,N-1\},E_\eta)
 \gtrsim N^{d-\eta}
\tag{16}
\]
along the same odd-level sequence. This matches the
\(\gamma>\eta\) upper power.

## Consequence

Equations (11) and (16), together with Mayeli's upper theorem, show that
\[
R^{d-\min\{\gamma,\eta\}}
\]
is the optimal uniform power of the scale \(R\) throughout the entire
off-critical region \(\gamma\ne\eta\).

The construction is deliberately asymmetric. The side carrying the smaller
regularity exponent is a fractional-boundary Moran set with a matching
translation lower bound; the other side is smooth. Thus no interaction between
two rough boundaries is needed to force the endpoint power.

## Limitations

- The result does not settle the critical regime
  \(0<\gamma=\eta<1\), where Mayeli asks whether the logarithmic factor is
  sharp.
- The lower bounds are proved along explicit lacunary sequences of scales;
  no all-\(R\) two-sided asymptotic is claimed.
- The examples prove class-level sharpness of the powers. The smoother member
  of the pair has regularity exponent \(1\), although it of course satisfies
  the weaker hypothesis with any prescribed larger exponent.
- No matching lower bound for the plunge count at a fixed spectral threshold
  is claimed; the theorem concerns the trace defect itself.

## Relation to prior literature and originality

Mayeli's arXiv:2609.12226v1 proves the two-exponent upper bounds, proves the
critical logarithm sharp only at \(\gamma=\eta=1\), and explicitly states in
Remark 9.4 that sharpness of the two off-critical powers is open. Section 10
uses alternating-gap Cantor examples numerically and labels the computations
as evidence rather than a proof. The construction above turns that geometric
idea into a rigorous lower-bound mechanism and uses balanced variable branching
to realize every fractional exponent \(0<\alpha<1\).

Hughes--Israel--Mayeli, arXiv:2607.02996, develops a continuous trace-defect
framework for rough domains, while Marceca--Romero--Speckbacher,
arXiv:2301.11685 / Arch. Ration. Mech. Anal. 248 (2024), obtains quantitative
concentration-eigenvalue estimates under different Ahlfors-regular hypotheses.
Neither source was found to state the off-critical sharpness theorem above.

Originality is asserted only to the best of our knowledge. Searches for
off-critical trace-defect sharpness, fractional Fourier concentration,
Minkowski/translation exponents, Cantor and Moran concentration examples, and
equivalent formulations located no prior proof of the two lower powers.
Because arXiv:2609.12226 is very recent, an unindexed contemporaneous proof
remains a residual risk. No inaccessible paper was identified whose available
metadata or theorem description gave concrete evidence that it contains the
same result.

## References

1. A. Mayeli, *Trace-defect bounds for discrete Fourier concentration
   operators*, arXiv:2609.12226v1 (2026).
   https://arxiv.org/abs/2609.12226
2. K. Hughes, A. Israel, A. Mayeli, *Trace bounds for limiting operators on
   rough domains*, arXiv:2607.02996 (2026).
   https://arxiv.org/abs/2607.02996
3. F. Marceca, J. L. Romero, M. Speckbacher, *Eigenvalue estimates for Fourier
   concentration operators on two domains*, Arch. Ration. Mech. Anal. 248
   (2024), Article 35.
   https://arxiv.org/abs/2301.11685
