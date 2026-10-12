# Projective rigidity of four explicit degree-seven conic-line arrangements
## Finding
Let \( [T:X:Z] \) be homogeneous coordinates and let the three conics and four lines be the explicit curves of Amram--Bannai--Shirane--Sinichkin--Tokunaga:
\[
C_1:\ XZ-T^2=0,\qquad
C_2:\ X^2-10TX+25XZ-36Z^2=0,
\]
\[
C_3:\ 4XZ-5T^2+8TZ-12Z^2=0,
\]
and
\[
egin{aligned}
L_1&:\ 25X-160T+256Z=0, &L_2&:\ X=0,\
L_3&:\ X-10T+25Z=0, &L_4&:\ 25X-90T+81Z=0.
\end{aligned}
\]
For \(i=1,2,3,4\), put \(\mathcal C_i=C_1+C_2+C_3+L_i\). Then the four \(\mathcal C_i\) are pairwise inequivalent under \(\operatorname{PGL}_3(\mathbb C)\), and every \(\mathcal C_i\) has trivial projective automorphism group.

More precisely, the stabilizer of the unordered pair \(\{C_1,C_2\}\) is a Klein four group, while the stabilizer of the ordered geometric triple \(C_1+C_2+C_3\) is trivial.
## Assumptions and scope
The ground field is \(\mathbb C\). Projective equivalence means equivalence under \(\operatorname{PGL}_3(\mathbb C)\). The statement concerns exactly the four explicit representatives above; it does not classify all projective orbits in either connected component of the full realization space.

The source proves that these four curves have the same combinatorics and that the corresponding realization space has two connected components. In that combinatorics, \(C_1\) and \(C_2\) meet transversely in four points, whereas \(C_3\) is tangent to both \(C_1\) and \(C_2\). Hence \(C_3\) is intrinsically distinguished among the three conic components as the unique conic tangent to both of the others.
## Proof
Parametrize \(C_1\) by
\[
[T:X:Z]=[u:u^2:1].
\]
Substitution into \(C_2\) gives
\[
u^4-10u^3+25u^2-36=(u+1)(u-2)(u-3)(u-6),
\]
so the four points of \(C_1\cap C_2\) correspond to \(u=-1,2,3,6\). No three are collinear because they lie on the smooth conic \(C_1\). Thus these four points form a projective frame: a projectivity preserving the unordered pair \(\{C_1,C_2\}\) must induce one of the \(24\) permutations of this frame, and each such permutation determines at most one projectivity.

For every permutation, solve exactly for that unique projectivity and pull back the two quadratic forms. Exhaustive rational arithmetic gives exactly four projectivities fixing both \(C_1\) and \(C_2\), and none exchanging them. The four fixing projectivities are the identity and three involutions, hence form \(V_4\). This proves
\[
\operatorname{Stab}_{\operatorname{PGL}_3}(\{C_1,C_2\})\cong V_4.
\]

Pulling back the quadratic form of \(C_3\) by these four matrices shows that only the identity preserves \(C_3\). Therefore
\[
\operatorname{Stab}_{\operatorname{PGL}_3}(C_1+C_2+C_3)=1.
\]

Now let a projectivity carry \(\mathcal C_i\) to \(\mathcal C_j\). The unique degree-one component must map to the unique degree-one component. Among the conics, \(C_3\) is uniquely characterized by being tangent to both other conics, so it must map to itself, and the set \(\{C_1,C_2\}\) must map to itself. The projectivity therefore lies in the trivial stabilizer of \(C_1+C_2+C_3\), hence is the identity. Since the four displayed lines are distinct, \(L_i=L_j\) forces \(i=j\). The same argument with \(i=j\) shows that each \(\mathcal C_i\) has trivial projective automorphism group.
## Verification
The accompanying `verify.py` uses only Python's standard library and exact rational arithmetic. It reconstructs the four frame points, enumerates all \(24\) frame permutations, builds the unique projectivity for each, and checks quadratic-form pullbacks. It verifies that the pair stabilizer has order \(4\), that there is no element exchanging \(C_1\) and \(C_2\), that only the identity also preserves \(C_3\), and that the four lines are distinct. A successful run ends with `VERIFY_OK`.
## Relationship to prior work
Amram--Bannai--Shirane--Sinichkin--Tokunaga introduce the four explicit degree-seven arrangements, prove that they have the same combinatorics, determine that the realization space has exactly two connected components, and show that representatives from distinct components form \(\pi_1\)-equivalent Zariski pairs. Their deformation argument places \(\mathcal C_1,\mathcal C_2\) in one component and \(\mathcal C_3,\mathcal C_4\) in the other, but it does not identify the four displayed representatives up to projective equivalence. The calculation here is a moduli-level refinement: even within each connected component, the two displayed representatives are distinct \(\operatorname{PGL}_3\)-orbits.

A later paper of Bannai--Tokunaga--Yorisaki revisits this combinatorics as case `Cmb223` and again records two connected components, but does not state an automorphism or projective-orbit classification for these four representatives.
## Limitations
This is a finite exact classification for the four displayed representatives, not a determination of the geometric quotient of the entire realization space. The originality search cannot exclude an equivalent calculation hidden in unindexed literature on conic pencils or Zariski pairs, although no such statement was found in the inspected source, its follow-up, or the targeted searches.
## References
1. M. Amram, S. Bannai, T. Shirane, U. Sinichkin, H.-o. Tokunaga, *The realization space of a certain conic line arrangement of degree 7 and a \(\pi_1\)-equivalent Zariski pair*, arXiv:2307.01736v1 (2023).
2. S. Bannai, H.-o. Tokunaga, E. Yorisaki, *The realization spaces of certain conic-line arrangements of degree 7*, arXiv:2409.05011v1 (2024).
