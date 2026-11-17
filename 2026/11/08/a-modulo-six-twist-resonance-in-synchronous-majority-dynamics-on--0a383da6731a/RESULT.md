# Fully flipping majority two-cycles on cyclic prisms and Möbius ladders

## Finding

For every integer \(n\ge3\), form the cubic prism \(T_n^{(0)}=C_n\square K_2\) or its one-seam twist \(T_n^{(1)}\), the Möbius ladder on \(2n\) labelled vertices. Label each rung by \(i\in\mathbb Z/n\mathbb Z\) and its ends by \(\ell\in\{0,1\}\); a twisted wrap swaps layers. On binary vertex configurations let \(M_{n,\theta}\) be simultaneous *strict majority of the three open neighbors*. Write \(\bar x\) for the bitwise complement of \(x\), and let
\[
Q_{n,\theta}=\#\{x\in\{0,1\}^{2n}:M_{n,\theta}(x)=\bar x\}.
\]
With Lucas numbers \(L_0=2,L_1=1,L_{m+2}=L_{m+1}+L_m\) and \(\delta_n=2\cos(2\pi n/3)\), the exact all-vertex-flipping population is
\[
\boxed{Q_{n,0}=L_n+\delta_n+2\mathbf1_{2\mid n},\qquad Q_{n,1}=L_n-\delta_n+2\mathbf1_{2\mid n}.}
\]
These are counts of labelled configurations, not of orbits modulo graph automorphisms. Complement commutes with majority, so each displayed configuration lies in a primitive two-cycle, and precisely \(Q_{n,\theta}/2\) distinct primitive two-cycle orbits flip **every vertex** on each step. Twisting the seam changes this population by the bounded but nonconstant arithmetic correction
\[
\boxed{Q_{n,1}-Q_{n,0}=-2\delta_n.}
\]
In contrast, the total primitive two-cycle population is of order \(\varphi^{2n}\), where \(\varphi=(1+\sqrt5)/2\); therefore the fully flipping share of those two-cycle configurations is \(\asymp\varphi^{-n}\), and in fact is asymptotic to \(\varphi^{-n}\).

## Proof

**The rung dichotomy.** Let the two bits at rung \(i\) be \((a_i,b_i)\). Suppose \(M(x)=\bar x\). If \(a_i=b_i=c_i\), the vertical neighbor at each rung end already votes *against* the required next bit \(1-c_i\). Both horizontal neighbors of both ends must therefore equal \(1-c_i\). This forces neighboring rungs to agree, and the same argument propagates. Hence every rung agrees and the rung bits alternate around the cycle. Such a pattern exists exactly for even \(n\), with two labelled configurations. Layer interchange at the seam has no effect because each rung agrees.

If no rung agrees, necessarily \(b_i=1-a_i\). The vertical vote at each rung end now already favors flipping. To obtain a strict majority for flipping, the two horizontal neighbors cannot both equal the present endpoint. Writing the first-layer bits as \(c_i=a_i\), the required condition is therefore \(c_{i-1}=c_i=c_{i+1}\) never occurs. On the prism the circular word satisfies \(c_{i+n}=c_i\). On the Möbius ladder the single twisted seam instead imposes \(c_{i+n}=1-c_i\). Both restrictions are necessary and sufficient, including for \(n=3\).

**Exact transfer.** Index overlapping two-bit words by \(00,01,10,11\), and use
\[
H=\begin{pmatrix}0&1&0&0\\0&0&1&1\\1&1&0&0\\0&0&1&0\end{pmatrix},\qquad
J=\begin{pmatrix}0&0&0&1\\0&0&1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
\]
\(H\) is the overlap transfer disallowing \(000\) and \(111\), and \(J\) complements both bits of a transfer state. They commute. On the \(+1\) eigenspace of \(J\), the characteristic polynomial of \(H\) is \(z^2-z-1\); on the \(-1\) eigenspace it is \(z^2+z+1\). Consequently
\[
\operatorname{tr}(H^n)=L_n+\delta_n,\qquad
\operatorname{tr}(H^nJ)=L_n-\delta_n.
\]
The first trace counts ordinary periodic no-triple words, and the second counts antiperiodically closed words. Adding the two alternating agreeing-rung configurations for even \(n\) proves both formulas for \(Q\). These transfer traces count each labelled configuration once, not twice. The polynomial eigenvalue calculation and the transition definition are explicit, so the formulas hold for all \(n\ge3\).

**Interpretation and rarity.** Binary complementation is an involution without fixed configurations on any nonempty graph. The strict-majority map commutes with it, so \(M(x)=\bar x\) implies \(M^2(x)=x\ne M(x)\), and two configurations form each orbit. For the same two graph families, earlier published recurrent-state formulas establish that the total number \(P_{n,\theta}\) of states satisfying \(M^2(x)=x\) is \(\varphi^{2n}+O(\varphi^n)\), while the fixed-state number \(F_{n,\theta}=\varphi^n+O(1)\). These formulas are credited below, not claimed as new here. Since \(Q_{n,\theta}=\varphi^n+O(1)\), division yields \(Q_{n,\theta}/(P_{n,\theta}-F_{n,\theta})\sim\varphi^{-n}\).

## Scope and verification

Only simple cubic cyclic ladders with \(n\ge3\), the specified synchronous open-neighbor majority update, and labelled binary configurations are covered. The theorem counts fully flipping two-cycles only; it does not newly classify all fixed states, all two-step recurrent states, all transient basins, or their separate twist-response formula. The companion `verify_transfer.cpp` independently counts closed local space-time words for both twist types and \(3\le n\le22\); `verify_exhaustive.cpp` enumerates microscopic configurations for \(3\le n\le12\). Their saved outputs are bounded corroboration, not proofs for all \(n\). Independent direct microscopic enumeration for \(n=3,4,5,6\) gives \((Q_{n,0},Q_{n,1})=(6,2),(8,10),(10,12),(22,18)\), agreeing with the formula.

## Prior-work boundary

The complete fixed-state and primitive-two-cycle populations and the modulo-six sign reversal for prisms versus Möbius ladders were already proved in *A Lucas-number seam response in majority oscillations on prism and Möbius ladders* (published November 1, 2026), https://github.com/Resultary/2026/tree/main/2026/11/1/SCOPE-a-lucas-number-seam-response-in-majority-oscillations-on-prism-a--69a75f8bbc7c . The present focused claim makes **no priority claim** for these earlier results, or for the classical general finite symmetric-majority period bound and graph double-cover construction. Agur, Fraenkel and Klein (1988) already derive the ordinary periodic no-triple word count \(L_n+\delta_n\) for a different single-cycle rule. The object-specific contribution retained here is the **two-graph fully flipping sector**, including its antiperiodic Möbius closure, the exact bounded twist difference and its rarity inside the previously counted recurrent population. No inspected earlier result states or logically implies this extra sector as a consequence of the total recurrent-state counts alone: knowing the total number of two-cycles does not determine the number in which every coordinate flips. An unindexed older equivalent remains a priority risk.

## References

1. *A Lucas-number seam response in majority oscillations on prism and Möbius ladders*, published mathematical result (2026-11-01), https://github.com/Resultary/2026/tree/main/2026/11/1/SCOPE-a-lucas-number-seam-response-in-majority-oscillations-on-prism-a--69a75f8bbc7c .
2. Z. Agur, A. S. Fraenkel, S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics 70 (1988), 295–302; DOI:10.1016/0012-365X(88)90005-2; https://www.imbm.org/wp-content/uploads/2020/01/AFK88.pdf .
3. E. Goles, J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189; DOI:10.1016/0012-365X(80)90121-1.
