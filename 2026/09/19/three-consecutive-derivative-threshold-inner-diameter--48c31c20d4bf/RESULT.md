# Arbitrary derivative gaps fail on finite-inner-diameter domains

## Finding

Let \(0\le a<b\) be integers with \(b-a\ge3\). There is a simply connected plane domain \(\Omega\) of finite interior-path diameter and an unbounded holomorphic function \(F\) on \(\Omega\) such that
\[
\sup_{z\in\Omega}\min\{|F^{(a)}(z)|,|F^{(b)}(z)|\}<\infty.
\]
Consequently, if a nonempty derivative set \(S\subseteq\mathbb N_0\) contains \(a=\min S\) and some \(b\in S\) with \(b-a\ge3\), finite interior-path diameter does not universally force simultaneous divergence of all \(F^{(k)}\), \(k\in S\).

This is only the obstruction direction. It does not assert that three consecutive derivative orders are universally forced: the published proof of that positive assertion has an unresolved gap.

## Assumptions and scope

The interior-path diameter is the supremum of intrinsic rectifiable path distances in \(\Omega\). The function and domain may depend on \((a,b)\). Derivatives are ordinary complex derivatives. The source construction for \((0,3)\) is due to MacMahon; the statement here treats every starting order and every gap at least three.

## Proof

Write \(m=b-a\ge3\). Set \(t_j=1-1/j\), \(I_j=[t_j,t_{j+1}]\), and \(\ell_j=1/(j(j+1))\). On \(I_j\) put
\[
u_j(x)=4(x-t_j)(t_{j+1}-x)/\ell_j^2,
\qquad A_j=j^{a+1}.
\]
Take a smooth step \(\eta\) that vanishes on \(( -\infty,1/3]\), equals one on \([2/3,\infty)\), and lies between zero and one. Choose \(0<\delta_j\le\min\{\ell_j/8,\ell_j/(8A_j)\}\) and define
\[
h(x)=A_j u_j(x)\eta((x-t_j)/\delta_j)\eta((t_{j+1}-x)/\delta_j)
\quad(x\in I_j).
\]
The pieces glue smoothly because each vanishes in a neighborhood of its endpoints. On the core, \(h\) is quadratic, so \(h^{(m)}=0\). On a cutoff collar, \(u_j\le4\delta_j/\ell_j\), so \(|h|\le1/2\). Therefore \(\min\{|h|,|h^{(m)}|\}\le1/2\) everywhere.

For \(a=0\) let \(H=h\). For \(a\ge1\), let
\[
H(x)=\frac1{(a-1)!}\int_0^x(x-t)^{a-1}h(t)\,dt.
\]
Then \(H^{(a)}=h\) and \(H^{(b)}=h^{(m)}\). For \(a=0\), the core maxima \(A_j\to\infty\) show that \(H\) is unbounded. For \(a\ge1\), on the middle half of \(I_j\) the cutoffs equal one and \(u_j\ge3/4\); hence each interval contributes at least a fixed positive amount to
\[
\int_{I_j}(1-t)^{a-1}h(t)\,dt
\asymp A_j\ell_j j^{-(a-1)}\asymp1.
\]
More precisely the contribution is bounded below by \(c_a(j/(j+1))^a\), with \(c_a>0\) independent of \(j\). Extend the integration kernel by zero for \(t>x\); it increases to \((1-t)^{a-1}\) as \(x\uparrow1\). Monotone convergence then proves \(H(x)\to\infty\).

Whitney's original Lemma 6 (Section 16, pp. 76–78) applies on an OPEN real set to a function of class \(C^m\), where \(m\) may be any fixed finite integer. Apply it with \(R=(0,1)\), \(m=b\), \(R_1=\varnothing\), a subsequent bounded open exhaustion with \(\overline{R_p}\subset R_{p+1}\), and constant positive tolerances \(\varepsilon_p=\varepsilon\). In Whitney's notation (14.1), \(\alpha_p=b\) for every \(p\); (16.1), or explicitly (16.2), therefore gives a real-analytic \(g\) satisfying \(|g^{(r)}(x)-H^{(r)}(x)|<\varepsilon\) for all \(0\le r\le b\) and every \(x\in(0,1)\). No differentiability or boundedness at the endpoints is required. It remains unbounded, and \(\min\{|g^{(a)}|,|g^{(b)}|\}\le1/2+\varepsilon\) on the real interval. The local holomorphic Taylor-series extensions glue: discs centered on the real interval that overlap have an overlapping real subinterval, where the extensions agree, so the identity theorem applies. They define one holomorphic function on an open neighborhood \(U\) of \((0,1)\). The subset where both derivative differences from the values at the real part are below \(\varepsilon\) is open and contains the entire interval. A positive continuous minorant of its distance-to-complement function gives a width \(0<\rho(x)\le1\) small enough that on
\[
\Omega=\{x+iy:0<x<1,\ |y|<\rho(x)\}
\]
the continuations of \(g^{(a)}\) and \(g^{(b)}\) differ from their real-axis values by at most \(\varepsilon\). Then the displayed minimum is at most \(1/2+2\varepsilon\) throughout \(\Omega\). The domain deformation retracts vertically onto \((0,1)\), so is simply connected. Any two points can be joined by vertical, horizontal and vertical segments of total length at most three. The real-axis restriction shows \(g\) remains unbounded. Taking \(F=g|_\Omega\) proves the assertion.

If \(S\) has span at least three, choose \(a=\min S\) and a \(b\in S\) with \(b-a\ge3\). The same pair obstruction prevents simultaneous divergence for all orders in \(S\).

## Verification

The core derivative vanishes because \(m\ge3\), the collar bound is uniform in \(j\), and the primitive diverges because its interval contributions stay bounded below. These are analytic arguments, not finite sampling. No program or external certificate is needed.

## Relationship to prior work

MacMahon, arXiv:2609.20607v1, Section 4 constructs the \((a,b)=(0,3)\) case and asks in Section 6 whether the three-consecutive window is the full universal guarantee. The present negative statement extends the obstruction to all \(a\) and \(b-a\ge3\). The positive direction of the earlier full-threshold claim is removed: Section 5 of that same paper does not currently justify it, as documented by the separate SCOPE proof-gap analysis.

## Limitations

This does not classify positive simultaneous-divergence guarantees. It gives a domain depending on a selected forbidden pair, not one universal domain for all pairs. The conclusion relies on the cited finite-order analytic approximation theorem. The original full if-and-only-if assertion is not retained.

## References

1. C. MacMahon, *On Simply Connected Domains Supporting an Unbounded Analytic Function with Bounded Derivative*, arXiv:2609.20607v1 (2026), Sections 4–6.
2. H. Whitney, [*Analytic extensions of differentiable functions defined in closed sets*](https://www.math.ucdavis.edu/~saito/data/high-dimensions/whitney1.pdf), Trans. Amer. Math. Soc. 36 (1934), 63–89; Section 16, Lemma 6 and (16.1)–(16.2), pp. 76–78.
