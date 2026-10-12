# Critical blow-up law for sharp generalized-order-statistic moment bounds
## Finding
Let \(X_{*,r}\), \(r\ge2\), be a generalized order statistic with positive parameter vector \(\boldsymbol\gamma\). Let
\[
\delta=\min_i\gamma_i\le1
\]
and let \(d\) be the multiplicity of this minimal parameter. For an arbitrary life baseline distribution with finite positive mean \(\mu\), define the sharp normalized moment bound
\[
B(\boldsymbol\gamma,p)
=
\sup_F\frac{\mathbb E_F X_{*,r}^p}{\mu^p},
\qquad 0<p<\delta.
\]
Bieniek and Rychlik prove that, in this regime,
\[
B(\boldsymbol\gamma,p)
=
\left[
\int_0^1 g_{*,\boldsymbol\gamma}(x)^{1/(1-p)}\,dx
\right]^{1-p},
\tag{1}
\]
where \(g_{*,\boldsymbol\gamma}\) is the density of the corresponding uniform generalized order statistic.

Write the distinct parameter values as
\[
\delta_1>\cdots>\delta_\ell=\delta,
\]
with multiplicities \(d_1,\ldots,d_\ell=d\). The endpoint expansion in the source implies
\[
g_{*,\boldsymbol\gamma}(x)
\sim
b(1-x)^{\delta-1}[-\log(1-x)]^{d-1},
\qquad x\uparrow1,
\tag{2}
\]
where
\[
b
=
\frac{\delta^d}{(d-1)!}
\prod_{j=1}^{\ell-1}
\left(\frac{\delta_j}{\delta_j-\delta}\right)^{d_j}.
\tag{3}
\]

The critical behavior of the sharp bound is then as follows.

If
\[
0<\delta<1,
\]
then
\[
B(\boldsymbol\gamma,p)
\sim
b\,
\Gamma\!\left(1+\frac{d-1}{1-\delta}\right)^{1-\delta}
\left(\frac{1-\delta}{\delta-p}\right)^{d-\delta},
\qquad p\uparrow\delta.
\tag{4}
\]
Equivalently,
\[
\lim_{p\uparrow\delta}
(\delta-p)^{d-\delta}B(\boldsymbol\gamma,p)
=
b(1-\delta)^{d-\delta}
\Gamma\!\left(1+\frac{d-1}{1-\delta}\right)^{1-\delta}.
\tag{5}
\]

At the logarithmic boundary
\[
\delta=1,
\]
there are two regimes. If \(d\ge2\), then
\[
B(\boldsymbol\gamma,p)
\sim
b\left(\frac{d-1}{e(1-p)}\right)^{d-1},
\qquad p\uparrow1.
\tag{6}
\]
If \(d=1\), then the endpoint is nonsingular and
\[
B(\boldsymbol\gamma,p)\longrightarrow b.
\tag{7}
\]

Thus the same multiplicity \(d\) that enters the source's finiteness classification also fixes the exact critical blow-up exponent and leading constant.

## Assumptions and scope
The result applies to generalized order statistics with \(r\ge2\), positive fixed parameter vector \(\boldsymbol\gamma\), minimal parameter \(\delta\le1\), and baseline life distributions with finite positive mean. It concerns the sharp bound (1) for moment orders \(0<p<\delta\).

No claim is made here for \(\delta>1\), where the source's sharp bound is represented by a different variational formula involving an interior maximizing point. The statement is also about the distribution-free supremum over baseline laws, not the moment of one fixed baseline distribution.

## Proof
Put
\[
q_p=\frac1{1-p}.
\]
Then (1) is the \(L^{q_p}\)-norm of the uniform-GOS density:
\[
B(\boldsymbol\gamma,p)
=
\left(\int_0^1 g_{*,\boldsymbol\gamma}(x)^{q_p}\,dx\right)^{1/q_p}.
\tag{8}
\]

The source gives the endpoint density expansion as a finite linear combination of terms
\[
(1-x)^{\delta_j-1}[-\log(1-x)]^m.
\]
Only the term belonging to the minimal parameter \(\delta\) and its highest logarithmic power survives after division by
\[
(1-x)^{\delta-1}[-\log(1-x)]^{d-1}.
\]
This proves (2). Differentiating the leading survival term from the source gives (3).

Set
\[
x=1-e^{-t}.
\]
Then \(dx=e^{-t}dt\). By (2), for large \(t\),
\[
g_{*,\boldsymbol\gamma}(1-e^{-t})
\sim
b e^{(1-\delta)t}t^{d-1}.
\tag{9}
\]
Therefore the endpoint contribution to the integral in (8) has the asymptotic model
\[
b^{q_p}
\int_0^\infty
 e^{-\beta_p t}t^{m_p}\,dt,
\tag{10}
\]
where
\[
\beta_p
=
1-(1-\delta)q_p
=
\frac{\delta-p}{1-p},
\qquad
m_p=(d-1)q_p.
\tag{11}
\]
The integral in (10) equals
\[
b^{q_p}\Gamma(m_p+1)\beta_p^{-(m_p+1)}.
\tag{12}
\]

For rigor, fix an arbitrary \(\eta>0\). Equation (9) sandwiches the true density between \((1-\eta)\) and \((1+\eta)\) times its model for all sufficiently large \(t\). When \(0<\delta<1\), \(q_p\) stays bounded as \(p\uparrow\delta\), while \(\beta_p\downarrow0\). The contribution of every bounded \(t\)-interval remains bounded, whereas (12) diverges. The sandwich therefore yields the ratio asymptotic (12) for the full integral. Raising it to the power \(1/q_p=1-p\) gives
\[
B(\boldsymbol\gamma,p)
\sim
b\,
\Gamma\!\left(1+\frac{d-1}{1-p}\right)^{1-p}
\left(\frac{1-p}{\delta-p}\right)^{d-p}.
\tag{13}
\]
Multiplying by \((\delta-p)^{d-\delta}\) and using
\[
(\delta-p)^{p-\delta}\longrightarrow1
\]
proves (4) and (5).

Now let \(\delta=1\). Then \(q_p=(1-p)^{-1}\to\infty\), and (9) becomes
\[
g_{*,\boldsymbol\gamma}(1-e^{-t})
\sim bt^{d-1}.
\]
For \(d\ge2\), the endpoint term dominates every compact part of the \(L^{q_p}\)-norm. The same fixed-\(\eta\) sandwich is valid; after taking the \(q_p\)-th root, its multiplicative error becomes only \(1\pm\eta\). Hence
\[
B(\boldsymbol\gamma,p)
\sim
b\,\Gamma((d-1)q_p+1)^{1/q_p}.
\tag{14}
\]
Stirling's formula yields
\[
\Gamma((d-1)q_p+1)^{1/q_p}
\sim
\left(\frac{(d-1)q_p}{e}\right)^{d-1},
\]
which is (6).

If \(\delta=d=1\), the source shows that the density is nondecreasing and has finite endpoint limit \(b\). Equation (8) is then an \(L^{q_p}\)-norm with \(q_p\to\infty\), so it converges to the essential supremum \(b\), proving (7).

As a direct exact check, take two equal parameters
\[
\boldsymbol\gamma=(\delta,\delta).
\]
Then
\[
g(x)=\delta^2(1-x)^{\delta-1}[-\log(1-x)],
\]
and (1) reduces exactly to
\[
B((\delta,\delta),p)
=
\delta^2
\Gamma\!\left(1+\frac1{1-p}\right)^{1-p}
\left(\frac{1-p}{\delta-p}\right)^{2-p}.
\tag{15}
\]
Formula (15) specializes to both asymptotic regimes above.

## Verification
The bundled `verify.py` uses the exact two-equal-parameter formula (15), rather than numerical integration, to check the normalized limits for several values approaching the critical moment order. It also checks the first-GOS special case against the exact sharp bound printed in the source.

A successful run ends with a line beginning
`VERIFY_OK subunit_ratio=`.

These finite calculations do not prove the general theorem; the proof is the endpoint sandwich and gamma-integral argument above.

## Relationship to prior work
Bieniek and Rychlik determine the necessary and sufficient finiteness conditions for moments of generalized order statistics and the sharp distribution-free bound (1). Their endpoint analysis identifies the minimal parameter and its multiplicity as the decisive quantities and supplies the density asymptotic needed here, but the inspected full text does not state a critical asymptotic for \(B(\boldsymbol\gamma,p)\) as \(p\) approaches the finiteness boundary.

The closely related paper by Rychlik and Szymkowiak on \(k\)-th record values reports that its sharp bounds become extremely large when the moment order approaches the border value, based on numerical evaluations. The inspected full text does not give an asymptotic rate or leading constant. The present result gives exactly that kind of critical law in the encompassing generalized-order-statistic setting for \(\delta\le1\).

Earlier work by Cramer, Kamps, and Rychlik gives sufficient conditions for existence of generalized-order-statistic moments. Its accessible abstract concerns existence conditions rather than the sharp-bound endpoint asymptotics derived here.

Targeted searches for critical-exponent, minimal-parameter-multiplicity, sharp-moment-bound, and generalized-order-statistic asymptotics did not locate the formulas (4)–(7).

## Limitations
The result does not analyze the \(\delta>1\) critical boundary, where the source's optimizer is governed by a different interior-maximization formula. It also does not claim a new finiteness criterion: the source criterion is used as a premise.

The derivation is a sharp asymptotic consequence of the source's exact density expansion and sharp bound formula. Its originality therefore lies in the critical rate and constant, not in a new construction of generalized order statistics.

## References
1. M. Bieniek and T. Rychlik, “Conditions for finiteness and bounds on moments of generalized order statistics,” *Statistical Papers* 65 (2024), 2289–2312. First published online 19 September 2023. DOI: 10.1007/s00362-023-01482-5.
2. T. Rychlik and M. Szymkowiak, “Conditions for finiteness and bounds on moments of record values from iid continuous life distributions,” *Extremes* 26 (2023), 83–100. First published online 9 November 2022. DOI: 10.1007/s10687-022-00449-3.
3. E. Cramer, U. Kamps, and T. Rychlik, “On the existence of moments of generalized order statistics,” *Statistics & Probability Letters* 59 (2002), 397–404. DOI: 10.1016/S0167-7152(02)00238-9.
