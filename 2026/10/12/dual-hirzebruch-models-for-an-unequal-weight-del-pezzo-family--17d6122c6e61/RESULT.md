# Dual Hirzebruch models for an unequal-weight del Pezzo family
## Finding
Let \(1\le n<m\), set \(a=n+1\), \(b=m+1\), and \(d=a+b=n+m+2\). Let
\[
f(x,y)=\prod_{i=1}^d\ell_i(x,y)
\]
be a square-free binary form, and consider
\[
S=\{tz+f(x,y)=0\}\subset\mathbb P(1,1,a,b),
\]
where \(x,y,z,t\) have weights \(1,1,a,b\). Assume \(\widetilde S\to S\) is the minimal resolution. Then the rational projection to \([x:y]\) extends to a morphism
\[
\pi:\widetilde S\longrightarrow\mathbb P^1
\]
whose general fiber is \(\mathbb P^1\) and whose only reducible fibers are the \(d\) fibers over the roots of \(f\). Each such fiber is the transverse union of two \((-1)\)-curves.

The exceptional curves over the weighted points \(p_z=[0:0:1:0]\) and \(p_t=[0:0:0:1]\) are disjoint sections \(E_z,E_t\) with
\[
E_z^2=-a,\qquad E_t^2=-b.
\]
If, in every reducible fiber, one contracts the component meeting \(E_z\), the resulting ruled surface is \(\mathbb F_b\); the image of \(E_z\) is its section of self-intersection \(+b\), and the image of \(E_t\) is its negative section. Contracting instead the components meeting \(E_t\) gives \(\mathbb F_a\).

Equivalently, \(\widetilde S\) is the blow-up of \(\mathbb F_b\) at the \(d\) distinct points on the \(+b\)-section lying over the roots of \(f\), and symmetrically it is the blow-up of \(\mathbb F_a\) at the corresponding points on the \(+a\)-section. In particular,
\[
\rho(\widetilde S)=d+2=n+m+4,\qquad K_{\widetilde S}^2=8-d=6-n-m.
\]

## Assumptions and scope
The statement is over \(\mathbb C\) and uses \(1\le n<m\), so both cyclic quotient points are genuinely singular and their one-curve resolutions are minimal. The binary form \(f\) is square-free, exactly as in the quasi-smooth family of Kim--Won Lemma 4.2. The boundary case \(n=0\) is not claimed: then the point of type \(\frac11(1,1)\) is smooth and the corresponding \((-1)\)-section is not part of a minimal resolution.

## Proof
Kim--Won put every surface in this family into the form \(tz+f(x,y)=0\), with \(f=\prod_i\ell_i\) square-free, and identify \(p_z\) and \(p_t\) as cyclic quotient points of types \(\frac1a(1,1)\) and \(\frac1b(1,1)\), respectively. For a quotient \(\frac1r(1,1)\) with \(r\ge2\), the minimal resolution has one exceptional rational curve of self-intersection \(-r\). Hence the full minimal resolution has disjoint exceptional curves \(E_z^2=-a\) and \(E_t^2=-b\).

Kim--Won resolve \(p_t\) by the weighted blow-up with weights \(1,1\). For
\[
L_i=\{z=\ell_i=0\},
\]
they compute that the strict transforms are pairwise disjoint \((-1)\)-curves and each meets the exceptional curve over \(p_t\) once. The same calculation after interchanging \((z,a,p_z)\) with \((t,b,p_t)\) gives curves
\[
M_i=\{t=\ell_i=0\}
\]
which are pairwise disjoint \((-1)\)-curves, each meeting \(E_z\) once. Resolving one weighted point does not alter the curves through the other weighted point, because the two points are disjoint.

The map \([x:y:z:t]\mapsto[x:y]\) extends across each weighted blow-up: the exceptional curve is precisely the projectivized \((x,y)\)-direction, so both \(E_z\) and \(E_t\) map isomorphically to \(\mathbb P^1\). Thus they are sections. Away from a root of \(f\), after fixing an affine coordinate on the base the fiber has equation \(zt=c\) with \(c\ne0\); adding its two points on the exceptional sections gives a smooth rational curve. At a simple root of \(f\), choose a local base parameter \(s\) with \(f=s u(s)\), where \(u(0)\ne0\). The surface germ is
\[
zt+s u(s)=0.
\]
It is smooth, and the fiber \(s=0\) is \(zt=0\), so its two components \(L_i\) and \(M_i\) meet transversely. These are exactly the \(d\) reducible fibers.

Now contract all \(M_i\). They are disjoint \((-1)\)-curves, so the contraction is smooth. In each reducible fiber, the other component \(L_i\) changes from self-intersection \(-1\) to \(0\), and the operation is the elementary transformation that turns that fiber into a smooth fiber. Therefore the resulting surface is a \(\mathbb P^1\)-bundle over \(\mathbb P^1\). Because every \(M_i\) meets \(E_z\) once and misses \(E_t\), the section self-intersections become
\[
(E_z')^2=-a+d=b,\qquad (E_t')^2=-b.
\]
A ruled surface over \(\mathbb P^1\) with a section of self-intersection \(-b\) is \(\mathbb F_b\), and the disjoint section has self-intersection \(+b\). Reversing the roles of \(z\) and \(t\) contracts all \(L_i\) and yields \(\mathbb F_a\), since \(-b+d=a\).

The inverse description is therefore the claimed blow-up model. A Hirzebruch surface has Picard rank \(2\) and canonical square \(8\); each of the \(d\) distinct point blow-ups increases the Picard rank by \(1\) and lowers the canonical square by \(1\). This gives the stated numerical consequences.

## Verification
The source computation used in the proof is Kim--Won Lemma 4.2: it gives the equation, the two quotient types, and, on the weighted blow-up of \(p_t\), the identities \(\overline L_i^2=-1\), \(\overline L_i\cdot\overline L_j=0\) for \(i\ne j\), and \(\overline L_i\cdot E_t=1\). The symmetric statement follows from the same equation by exchanging \(z\) and \(t\) together with their weights.

The accompanying `verify.py` checks the algebraic intersection-number identities for arbitrary symbolic \(n,m\): \(d=a+b\), \(-a+d=b\), \(-b+d=a\), \(\rho=2+d\), and \(K^2=8-d\). These checks support the bookkeeping; the existence and identification of the ruled models are proved geometrically above, not inferred from finite experiments.

## Relationship to prior work
Kim--Won use the displayed family to prove K-instability. Their Lemma 4.2 resolves only the point \(p_t\) needed for the beta-invariant computation and records one family of \((-1)\)-curves; it does not state the full minimal resolution, the \(\mathbb P^1\)-fibration, either Hirzebruch blow-down, or the formulas for \(\rho(\widetilde S)\) and \(K_{\widetilde S}^2\). Liu--Petracci study the equal-weight family \(\mathbb P(1,1,a,a)\) through K-stability and binary-form GIT, including a toric degeneration, but their paper does not supply the unequal-weight dual ruled models proved here.

## Limitations
The claim is restricted to square-free \(f\) and \(1\le n<m\). Multiple roots produce different singular fibers and require a separate resolution analysis. No assertion is made about automorphism groups, K-stability beyond the cited results, or the degeneration behavior when factors of \(f\) collide. A classical equivalent description may exist in the literature on rational \(\mathbb C^*\)-surfaces or ruled-surface compactifications; targeted searches did not locate one, so this remains the principal originality risk.

## References
1. In-kyun Kim and Joonyeong Won, *Unstable singular del Pezzo hypersurfaces with lower index*, arXiv:2011.04152v1 (2020), Lemma 4.2; published in *Communications in Algebra* 49 (2021), 2679--2688, DOI 10.1080/00927872.2021.1880591.
2. Yuchen Liu and Andrea Petracci, *On K-stability of some del Pezzo surfaces of Fano index 2*, arXiv:2011.05094; *Bulletin of the London Mathematical Society* 54 (2022), 517--525, DOI 10.1112/blms.12581.
