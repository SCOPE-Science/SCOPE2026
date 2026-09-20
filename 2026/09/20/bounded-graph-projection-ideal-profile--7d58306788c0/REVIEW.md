# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The central identity follows from canonical orthonormal coordinates for a graph
and its orthogonal complement. For
\[
J_Tx=((I+T^*T)^{-1/2}x,\;T(I+T^*T)^{-1/2}x)
\]
and
\[
V_Ty=(-T^*(I+TT^*)^{-1/2}y,\;(I+TT^*)^{-1/2}y),
\]
the operator \([J_T\ V_T]\) is unitary and \(P_T=J_TJ_T^*\). The two cross
terms are exactly the normalized differences stated in RESULT.md.

For \(\Delta=P_A-P_B\), the identity
\(P_A\Delta^2=\Delta^2P_A=P_A-P_AP_BP_A\) makes \(\Delta^2\) block diagonal
relative to \(G(A)\oplus G(A)^\perp\). Its diagonal blocks are
\(S_{A,B}^*S_{A,B}\) and \(S_{B,A}S_{B,A}^*\). Positive functional calculus then
gives the asserted modulus decomposition.

The finite-rank formula follows because all four normalization factors are
boundedly invertible. The singular-value and Schatten statements follow from
unitary invariance, direct-sum rearrangement and the standard ideal inequality
for multiplication by bounded operators. The essential-norm formula is the
corresponding direct-sum identity in the Calkin algebra.

The geodesic corollary uses only the stated bounded-graph criterion. If \(A-B\)
is compact, \(I+B^*A\) is a compact perturbation of \(I+A^*A\), hence Fredholm
of index zero; its adjoint is \(I+A^*B\), giving equality of the two defect
dimensions.

No hidden complementability or inheritance assumption is used.

## Originality

**PASS, to the best of our knowledge.**

The closest located older result is Azizov–Behrndt–Jonas–Trunk (2009). For
bounded operators it proves exactly the qualitative equivalences
\[
P_A-P_B\text{ finite rank}\iff A-B\text{ finite rank}
\]
and
\[
P_A-P_B\text{ compact}\iff A-B\text{ compact}.
\]
The inspected full text contains no occurrence of “Schatten” or “trace class,”
and the bounded corollaries do not give the exact rank or singular-value
profile.

Andruchow (2015) proves a fixed-base Schatten result for the graph chart:
Schatten-\(p\) coordinates based at the horizontal subspace correspond to a
Schatten restricted Grassmannian chart. This is explicitly excluded from the
novelty claim. The present statement concerns the difference of two arbitrary
bounded graph projections and supplies an exact two-directed decomposition.

The current paper Andruchow–Recht–Varela (2026) treats bounded graph charts,
compact graphs, common complements and Grassmann geodesics. No occurrence of
“Schatten” was located in the inspected text, and the stated compact/geodesic
results do not give the two-graph ideal profile.

Residual risk remains from K. Y. Chung, *Subspaces and graphs* (Proc. AMS 119
(1993), 141–146), which was identified as foundational graph-chart literature
but was not exhaustively inspected in full, and from older canonical-angle
literature where the same identity might be encoded without Schatten/graph-map
terminology. The result is elementary enough that an equivalent statement may
exist as an unstated consequence. For this reason originality is asserted only
to the best of our knowledge.

## Value

**PASS.**

The result upgrades two classical qualitative perturbation equivalences to a
single exact operator identity. It simultaneously gives:

- exact rank doubling for finite-rank bounded perturbations;
- the complete compact singular-value multiset of \(P_A-P_B\);
- Schatten-\(p\) equivalence and an exact norm identity for every \(p>0\);
- explicit uniform two-sided Schatten estimates on operator-norm bounded sets;
- an exact essential-norm formula, quantitatively refining compactness
  equivalence;
- a compact-difference criterion guaranteeing a minimal Grassmann geodesic even
  when neither endpoint operator is compact.

These consequences make the statement useful both in operator-ideal
perturbation theory and in the geometry of Hilbert Grassmannians.

## Scientific limitations

The result is confined to bounded operators between Hilbert spaces. It does not
claim an exact analogue for general closed unbounded operators or multivalued
linear relations. The literature search cannot exclude a differently phrased
older canonical-angle identity, especially in the uninspected 1993 source noted
above.
