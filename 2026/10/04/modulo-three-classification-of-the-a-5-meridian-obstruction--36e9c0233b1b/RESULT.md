# Modulo-three classification of the \(A_5\) meridian obstruction
## Finding
For the RBG trace-pair family \(K_{B_m},K_{G_m}\) of Bais--Di Prisa--Hartman--Hsueh--Kegel--Merz--Pencovitch--Ray--Santoro--Truöl--Wakelin, let
\[
\sigma=(15432)\in A_5
\]
and define
\[
N_K(A_5,\sigma)=\#\{\phi:\pi_1(K)\to A_5:\phi(\mu_K)=\sigma\}.
\]
Then for every integer \(m\ge1\),
\[
\bigl(N_{K_{B_m}}(A_5,\sigma),N_{K_{G_m}}(A_5,\sigma)\bigr)
=
\begin{cases}
(6,1),&m\equiv1\pmod3,\
(1,1),&m
ot\equiv1\pmod3.
\end{cases}
\]
Consequently, whenever \(m\equiv1\pmod3\), the two knots have diffeomorphic traces but their exteriors are not homotopy equivalent rel boundary.

This replaces the source's printed sufficient congruence \(m\equiv1\pmod{60}\) by an exact classification of all parameters for the same \(A_5\) meridian-count obstruction. In particular, the source's infinite construction can be indexed by \(m=3\ell+1\) rather than \(m=60\ell+1\). Distinct parameters are still separated by the source's Alexander-polynomial breadth \(2m\).

## Assumptions and scope
The source constructs, in every dimension covered by its RBG construction, pairs \(K_{B_m},K_{G_m}\) with diffeomorphic traces. The group calculation used here is dimension-independent because Proposition 4.10 identifies both knot groups with the same presentation
\[
F_m=\langle x,y,a\mid (yx)^m y (yx)^{-m}x^{-1}=1,\ (x^{-1}ax)a^{-1}x^{-1}(yay^{-1})=1\rangle.
\]
In that identification, \(x\) and \(y\) represent the meridian conjugacy class for \(K_{B_m}\), while \(a\) represents the meridian for \(K_{G_m}\).

The conclusion for \(m
ot\equiv1\pmod3\) is only that this particular \(A_5\) witness gives equal counts \((1,1)\). No homotopy equivalence of exteriors is claimed for those residues.

## Proof
The alternating group \(A_5\) has element orders \(1,2,3,5\), hence exponent
\[
\operatorname{exp}(A_5)=\operatorname{lcm}(1,2,3,5)=30.
\]
For any assignment \(x,y,a\in A_5\), the only dependence of the defining relators of \(F_m\) on \(m\) occurs through \((yx)^m\). Therefore the two representation counts are periodic in \(m\) with period dividing \(30\).

It is thus enough to check the thirty residues \(m=0,1,\ldots,29\). For \(K_{B_m}\), fix \(x=\sigma\) and exhaust the \(60^2\) choices of \((y,a)\). For \(K_{G_m}\), fix \(a=\sigma\) and exhaust the \(60^2\) choices of \((x,y)\). Exact permutation multiplication gives
\[
N_{K_{B_m}}(A_5,\sigma)=
\begin{cases}
6,&m\equiv1\pmod3,\
1,&m
ot\equiv1\pmod3,
\end{cases}
\qquad
N_{K_{G_m}}(A_5,\sigma)=1
\]
for all thirty residue classes. Periodicity then proves the formula for every \(m\ge1\).

The source proves that a homotopy equivalence of exteriors rel boundary preserves these meridian-constrained counts when \(\sigma\) is conjugate to \(\sigma^{-1}\), as it is in \(A_5\). Thus the unequal values \((6,1)\) obstruct such an equivalence for every \(m\equiv1\pmod3\).

Finally, the source proves that the two knots have diffeomorphic traces for every \(m\), and that their common Alexander polynomial has breadth \(2m\). Hence the same proof used there for the subsequence \(60\ell+1\) works on the denser subsequence \(3\ell+1\).

## Verification
The current source was checked at the common group presentation, the definition and invariance of \(N_K(A,\sigma)\), the printed \(A_5\) computation, the trace theorem, and the Alexander-polynomial calculation. The published proposition records the special case \(m\equiv1\pmod{60}\), where the counts are \((6,1)\).

The bundled verifier constructs all sixty even permutations of five letters, checks that their orders are exactly \(1,2,3,5\), computes the exponent \(30\), and exhausts all thirty residue classes. For each residue it evaluates both relators for all \(60^2\) possible assignments after fixing the prescribed meridian. It also repeats one complete shifted period and checks the published cases \(m=1\) and \(m=61\). It prints:

`VERIFY_OK A5_size=60 exponent=30 residues=30 distinguished=10 pattern=m_mod_3_eq_1 source_case=true`

The exhaustive residue calculation is sufficient because the presentation is exactly periodic modulo the exponent of \(A_5\); no inference from a finite sample to an unbounded parameter range is being made.

## Relationship to prior work
The source's Proposition 4.11 proves the values \((6,1)\) under the stronger hypothesis \(m\equiv1\pmod{60}\). Its proof uses the order of \(A_5\) to propagate the computation at \(m=1\), and Theorem 4.14 consequently selects \(m=60\ell+1\).

The present calculation classifies the same invariant on every parameter residue. The actual period is controlled by the group exponent \(30\), not its order \(60\), and the exhaustive period table collapses further to the congruence \(m\equiv1\pmod3\). Thus the printed family is a strict subfamily of the distinguished parameters: among each sixty consecutive values, the source condition selects one residue whereas the exact \(A_5\) witness selects twenty.

Targeted literature searches for the family notation, the meridian representation count, the \(A_5\) witness, and modulo-three formulations did not locate this residue classification. Earlier same-trace and same-exterior constructions discussed by the source concern different families and do not imply the present parameter computation.

## Limitations
For \(m
ot\equiv1\pmod3\), equality of the two \(A_5\) counts does not imply that the knot exteriors are homotopy equivalent rel boundary; it only means this particular finite-group witness does not distinguish them.

The result classifies one deliberately chosen finite-group invariant, not all finite quotients or all peripheral invariants of the knot groups. A different finite group could potentially distinguish additional residues.

A later revision of the recent preprint could incorporate the same residue calculation.

## References
1. V. Bais, A. Di Prisa, D. Hartman, C.-S. Hsueh, M. Kegel, A. Merz, M. Pencovitch, A. Ray, D. Santoro, P. Truöl, and L. Wakelin, *On the detection of knots by their traces in high dimensions*, arXiv:2511.07251v2, first posted 2025-11-10.
