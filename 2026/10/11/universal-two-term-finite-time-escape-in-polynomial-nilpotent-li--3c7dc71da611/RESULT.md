# Universal two-term finite-time escape in polynomial nilpotent Liénard systems

## Finding

Let \(n\ge2\) be an integer and let \(b\) be a real odd polynomial of odd degree \(m\ge n\), with leading coefficient \(b_m\ne0\). Consider the polynomial differential system in its **original, unrescaled physical time**,
\[
\dot x=-y,\qquad \dot y=x^{2n-1}+b(x)y.
\]
Write
\[
 s=\operatorname{sgn}(b_m),\quad B=|b_m|,\quad
 c=s b_{m-2},\quad A=\frac{B}{m+1},\quad
 Q=\frac{c-\mathbf 1_{\{m=n\}}/A}{m-1},\quad
 L=\frac{1}{Am}=\frac{m+1}{mB}.
\]
The coefficient \(b_{m-2}\) is interpreted as zero when its monomial is absent, and the indicator is one exactly when \(m=n\).

There is \(R>0\) (depending only on the polynomial and \(n\)) such that the open set
\[
\mathcal W_R=\left\{(x,y):z=sx>R,\quad v=-sy>\frac{B}{4(m+1)}z^{m+1}\right\}
\]
is forward invariant up to the maximal existence time. **Every** trajectory initially in \(\mathcal W_R\) reaches infinity in finite forward time \(T\). Both \(z(t)\) and \(v(t)\) tend to \(+\infty\), and on any such trajectory
\[
\boxed{v(t)=A z(t)^{m+1}+Q z(t)^{m-1}+o(z(t)^{m-1}).}
\]
The remaining *physical* time obeys
\[
\boxed{T-t=L z(t)^{-m}-\frac{Q}{A^2(m+2)}z(t)^{-m-2}
       +o(z(t)^{-m-2}).}
\]
Equivalently, with \(\tau=T-t\),
\[
\boxed{z(t)=\left(\frac{L}{\tau}\right)^{1/m}
 -\frac{Q}{A(m+2)}\left(\frac{\tau}{L}\right)^{1/m}
 +o(\tau^{1/m}).}
\]
Consequently \(\lim_{t\uparrow T}\tau^{1/m}sx(t)=L^{1/m}\) and \(\lim_{t\uparrow T}v(t)/z(t)^{m+1}=A\). The two coefficients \(L\) and \(Q\) do not depend on the initial point in \(\mathcal W_R\).

**Restoring-force resonance.** The second coefficient is \(c/(m-1)\) if \(m>n\), but becomes \((c-1/A)/(m-1)\) if \(m=n\). Thus the restoring force first influences this order precisely at equality of the damping degree and the nilpotency index. Equality is possible only for odd \(n\), since \(m\) is odd.

## Assumptions and scope

The integers satisfy \(n\ge2\), \(m\ge n\), and \(m\) is odd. No local-center, focus, monodromy, or polynomial-coefficient sign conditions are assumed beyond the nonzero leading coefficient. The result asserts finite-time blow-up **for every point in the displayed open wedge**, not for every nonperiodic orbit, and makes no classification of its complementary region.

When the polynomial satisfies the classical additional nilpotent-center conditions at the origin, these escaping solutions lie outside the center's periodic annulus. The existence of a nilpotent center is not used as a premise in the proof below.

## Proof

**Step 1: oriented coordinates and an invariant wedge.** Let \(z=sx\) and \(v=-sy\). Because \(b\) is odd and \(s=\pm1\), the system becomes
\[
\dot z=v,\qquad \dot v=-z^{2n-1}+\widetilde b(z)v,
\qquad \widetilde b(z)=b(sz)=Bz^m+cz^{m-2}+O(z^{m-4}).
\]
Set \(K=B/[4(m+1)]\), and choose \(R\) large enough that \(\widetilde b(z)\ge (B/2)z^m\) for \(z\ge R\) and
\[
- z^{2n-1}+\frac{KB}{4}z^{2m+1}>0\qquad(z\ge R).
\]
This is possible because \(2m+1>2n-1\). Along the boundary \(v=Kz^{m+1}\), the outward derivative is
\[
\frac{d}{dt}(v-Kz^{m+1})
=-z^{2n-1}+[\widetilde b(z)-K(m+1)z^m]v
\ge -z^{2n-1}+\frac{KB}{4}z^{2m+1}>0.
\]
On the other boundary \(z=R\), \(\dot z=v>0\). The open wedge is therefore positively invariant up to maximal existence time. Inside it,
\[
\dot z=v\ge Kz^{m+1},\qquad
\frac{d}{dt}z^{-m}\le -mK.
\]
Hence any maximal forward time satisfies \(0<T\le [mKz(0)^m]^{-1}<\infty\). If \(z\) stayed bounded as \(t\uparrow T\), the equation \(\dot v=\widetilde b(z)v-z^{2n-1}\), which is linear in \(v\) with bounded coefficients and forcing, would keep \(v\) bounded by Gronwall's inequality, contradicting maximality. Since \(z\) increases, \(z(t)\to\infty\), and the wedge then gives \(v(t)\to\infty\).

**Step 2: asymptotic velocity at infinity.** Since \(z\) strictly increases, treat \(v\) as a function of \(z\):
\[
\frac{dv}{dz}=\widetilde b(z)-\frac{z^{2n-1}}{v(z)}.
\]
The wedge estimate \(v\ge Kz^{m+1}\) implies that the final term is \(O(z^{2n-m-2})\). Since \(m\ge n\), integrating from any fixed large \(z_0\) proves
\[
 v(z)=\frac{B}{m+1}z^{m+1}+O(z^{m-1})=Az^{m+1}(1+O(z^{-2})).
\]
(The marginal integration \(\int z^{-1}dz\) may produce a logarithm, which remains within the stated bound.) Therefore
\[
\frac{z^{2n-1}}{v(z)}=\frac1A z^{2n-m-2}(1+O(z^{-2})).
\]
If \(m=n\), its leading order is \(z^{m-2}/A\). If \(m>n\), its order is at most \(z^{m-4}\), and after integration is \(o(z^{m-1})\). The lower monomials of \(\widetilde b\) beyond \(cz^{m-2}\) similarly have integrated size \(o(z^{m-1})\). Integrating the differential equation a second time yields
\[
 v(z)=Az^{m+1}+
 \frac{c-\mathbf 1_{\{m=n\}}/A}{m-1}z^{m-1}+o(z^{m-1}),
\]
which is precisely the claimed coefficient \(Q\). This also covers \(m=3\); all logarithmic integrated remainders are \(o(z^2)\).

**Step 3: original-time law.** Strict monotonicity gives the exact identity
\[
T-t=\int_{z(t)}^{\infty}\frac{d\zeta}{v(\zeta)}.
\]
Reciprocating the two-term velocity expansion,
\[
\frac1{v(z)}=\frac1A z^{-m-1}-\frac{Q}{A^2}z^{-m-3}+o(z^{-m-3}).
\]
Termwise integration, justified by the uniform tail meaning of little-oh, gives the displayed two-term expression for \(T-t\). To invert, set \(Z=(L/\tau)^{1/m}\) and substitute \(z=Z+d Z^{-1}+o(Z^{-1})\). Balancing the \(Z^{-m-2}\) terms gives \(d=-Q/[A(m+2)]\), establishing the physical-time expansion. No rescaling or reparametrization of the clock was used.

## Verification

The identities \((m+1)A=B\), \((m-1)Q=c-\mathbf 1_{\{m=n\}}/A\), \(AmL=1\), and the time-inversion coefficient are checked with exact rational arithmetic in `verification/check_coefficients.py` for representative allowed degrees, including the borderline \(m=n\). The checker runs with Python's standard library by `python verification/check_coefficients.py` and prints `CHECK_OK`. These finite checks are supporting reproducibility only: the proof above establishes the theorem for all specified polynomials and initial points.

## Relationship to prior work

García and Llibre determine local and global nilpotent-center conditions for this polynomial Liénard family and obtain non-global cases (2022 online). Chen, Li and Zhang (2022 preprint, later published) and Han, Kong and Yu (2026) give broader center and non-global-center classifications; their geometric classifications are not asserted as new here. In particular, the García–Llibre global-center conjecture was subsequently solved and is **not** a claim of the present theorem.

Dumortier and Herssens classify qualitative phase portraits near infinity; Matsue's general blow-up work discusses polynomial Liénard equations in a different balance regime with a periodic orbit at infinity. Their cited classifications and blow-up mechanisms are distinct from the present open escape wedge, its original-time leading constant, and the two-term degree-resonance correction. General blow-up theory motivates the question but does not by itself supply this equation-specific correction without the explicit analysis above. Earlier explicit blow-up results for certain integrable cubic Liénard equations concern a different damping degree.

## Limitations

The theorem does not establish that all unbounded solutions blow up, does not determine the full phase portrait or the boundary of the escape wedge, and does not provide a uniform error constant over all initial data. The \(o(\cdot)\) terms are for each fixed escaping trajectory. Published-source overlap checks cannot establish absolute priority; the complete text of Dumortier–Herssens (1999) was not obtained through the available legal access route, so equivalent formulas hidden there or in unindexed work remain a residual risk. No independent mathematical audit is asserted here.

## References

1. I. A. García and J. Llibre, *Polynomial Liénard systems with a nilpotent global center*, Rendiconti del Circolo Matematico di Palermo (2023), first online 19 December 2022, DOI: 10.1007/s12215-022-00850-8.
2. H. Chen, Z. Li, and R. Zhang, *A sufficient and necessary condition of generalized polynomial Liénard systems with global centers*, arXiv:2208.06184 (2022); revised journal title *Establishing definitive conditions for global centers in generalized polynomial Liénard systems*, DOI: 10.3934/dcdsb.2024130.
3. M. Han, C. Kong, and P. Yu, *Global and non-global center conditions of generalized Liénard systems*, Nonlinear Analysis: Real World Applications 88 (2026), 104474, DOI: 10.1016/j.nonrwa.2025.104474, especially Theorem 3.5.
4. F. Dumortier and C. Herssens, *Polynomial Liénard equations near infinity*, Journal of Differential Equations 153 (1999), 1–29, DOI: 10.1006/jdeq.1998.3543.
5. K. Matsue, *Geometric treatments and a common mechanism in finite-time singularities for autonomous ODEs*, arXiv:1806.08487 (2018), especially Section 4.8; Journal of Differential Equations 267 (2019), 7313–7368.
6. G. Bluman, A. F. Cheviakov, and M. Senthilvelan, *Solution and asymptotic/blow-up behaviour of a class of nonlinear dissipative systems*, Journal of Mathematical Analysis and Applications 339 (2008), 1199–1209, DOI: 10.1016/j.jmaa.2007.06.076.
