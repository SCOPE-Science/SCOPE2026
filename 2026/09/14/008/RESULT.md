# Grötzsch graph M4 edge ideal: Waldschmidt constant 29/19 and resurgence 38/29

## Setup

Let \(G=M_4\) be the Mycielskian of \(C_5\), with vertices
\(v_0,\ldots,v_4,u_0,\ldots,u_4,w\), and let \(I=I(G)\) be its edge ideal over an arbitrary field.

For an exponent vector \(a\in\mathbb N^{11}\), define
\[
\operatorname{symb}(a)=\min_C\sum_{v\in C}a_v
\]
over the minimal vertex covers \(C\), and let \(\nu(a)\) be the integral capacitated edge-packing number. Then
\(x^a\in I^{(m)}\) iff \(\operatorname{symb}(a)\ge m\), while
\(x^a\in I^r\) iff \(\nu(a)\ge r\).

The graph has 20 edges and 16 minimal vertex covers, in the four \(D_5\)-types
\[
(3,3,1)^5,\quad(3,5,0)^5,\quad(4,2,1)^5,\quad(5,0,1)^1.
\]

## Result

\[
\widehat\alpha(I)=\frac{29}{19},\qquad
\rho(I)=\frac{38}{29}.
\]

Also,
\[
I^{(2r-1)}\subseteq I^r\qquad(r\ge1).
\]
The last containment follows from a general graph lemma and is included for completeness; originality is not claimed for that elementary lemma.

## Waldschmidt constant

By \(D_5\)-symmetry, the fractional-cover LP reduces to
\[
\min 5p+5q+s
\]
under the four cover-type inequalities. Its optimum is
\[
(p,q,s)=\frac1{19}(3,2,4),\qquad 5p+5q+s=\frac{29}{19}.
\]
A dual solution, constant on the four cover orbits with weights
\[
3/19,\ 2/19,\ 0,\ 4/19,
\]
loads every vertex by exactly 1 and has value \(29/19\), proving optimality.

The integral vector
\[
a_{\rm sym}=(3,3,3,3,3,2,2,2,2,2,4)
\]
has minimum cover sum 19 and degree 29. Its multiples therefore realize the LP value asymptotically, giving
\(\widehat\alpha(I)=29/19\).

## Stable Harbourne containment

Let \(y\) be a maximum integral \(b\)-matching for capacities \(a\), and let \(T\) be the set of saturated vertices, including vertices of zero capacity. If an edge had both endpoints outside \(T\), one more copy of that edge could be added; hence \(T\) is a vertex cover. Choosing a minimal cover \(C\subseteq T\),
\[
\operatorname{symb}(a)\le\sum_{v\in T}a_v
=\sum_{v\in T}\operatorname{load}_y(v)
\le 2\nu(a).
\]
Thus \(\operatorname{symb}(a)\ge2r-1\) implies the integer inequality \(\nu(a)\ge r\).

## Resurgence lower bound

For \(k a_{\rm sym}\),
\[
\operatorname{symb}(ka_{\rm sym})=19k.
\]
The constant fractional edge cover \(x_v=1/2\) gives
\[
\nu(ka_{\rm sym})\le\nu_{\rm frac}(ka_{\rm sym})\le 29k/2.
\]
Consequently failures approach ratio \(38/29\), so \(\rho(I)\ge38/29\).

## Resurgence upper bound

Two facts suffice.

**Lemma 1.**
For every real \(a\ge0\),
\[
29\,\operatorname{symb}(a)\le38\,\nu_{\rm frac}(a).
\]
By LP duality, \(\nu_{\rm frac}(a)=\min_x a\cdot x\) over fractional edge covers. Half-integrality reduces the check to half-integral covers. The archived exact certificates verify the inequality on all 474 \(D_5\)-orbits of half-integral edge-cover vectors; the extremal vector is \(x=(1/2,\ldots,1/2)\).

**Lemma 2.**
For every integral \(a\),
\[
\nu_{\rm frac}(a)-\nu(a)\le1/2.
\]
A minimal-support extreme fractional \(b\)-matching is half-integral, with nonintegral support on vertex-disjoint odd-cycle components. The Grötzsch graph has odd-cycle packing number 1, so at most one such component occurs; rounding it loses at most \(1/2\).

Therefore, if \(x^a\in I^{(m)}\setminus I^r\), we may take
\(m\le\operatorname{symb}(a)\) and \(r\ge\nu(a)+1\), and
\[
29m\le38\nu_{\rm frac}(a)
\le38\nu(a)+19
<38(\nu(a)+1)\le38r.
\]
Hence \(m/r<38/29\); taking the lower-bound family gives the supremum
\(\rho(I)=38/29\).

## Independent audit checks

The 2026-09-29 audit independently rebuilt the 20-edge graph and all 16 minimal covers; solved the Waldschmidt LP at \((3^5,2^5,4)/19\); enumerated all 3,656 half-integral edge covers, which form 474 \(D_5\)-orbits, and independently minimized the relevant dual objective to \(29/38\); and enumerated 594 nonbipartite induced vertex sets, finding no disjoint pair. These checks reproduce the structural inputs of both resurgence lemmas.

## Reproducibility

Use the committed files under `artifacts/`:
`m4_data.py`, `m4_setup.py`, `m4_dual.py`, `m4_witness_verify.py`,
and `artifacts/probe/verify_certs.py`, `verify_odd_packing.py`,
with the certificate data in the same `artifacts/probe/` directory.

## Literature context

Bocci et al. supply the squarefree-monomial LP framework. Gu–Hà–O'Rourke–Skelton compute exact symbolic-power invariants for unicyclic graphs. Those general results do not state the two numerical invariants above for \(M_4\). The retained claim is the exact Grötzsch-graph computation, not a new general LP theory.

## References

- C. Bocci et al., “The Waldschmidt constant for squarefree monomial ideals,” arXiv:1508.00477.
- Y. Gu, H. T. Hà, J. O'Rourke, J. Skelton, “Symbolic powers of edge ideals of graphs,” arXiv:1805.03428.
