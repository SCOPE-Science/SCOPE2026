# Three target levels null-homotope every map from a height-two finite space
## Finding
Let \(P\) be a finite \(T_0\)-space whose specialization poset has no chain of three distinct points. Let
\[
W=A_1\oplus A_2\oplus\cdots\oplus A_h,\qquad h\ge 3,
\]
where every \(A_i\) is a nonempty antichain and every point of \(A_i\) lies below every point of \(A_j\) for \(i<j\). Then every continuous map \(f:P\to W\) is homotopic to a constant map. In fact there are order-preserving maps \(f_1,f_2:P\to W\) and a constant map \(c_t\) such that
\[
f\ge f_1\ge f_2\le c_t.
\]
Thus the compact-open finite mapping space \(W^P\) is path connected.

The bound on the number of target levels is sharp. If \(W=C_2\) is the four-point crown, equivalently the ordinal sum of two two-point antichains, then for \(P=W\) the identity map is not homotopic to a constant map.

## Assumptions and scope
The phrase “height at most two” is used here in the explicit sense that \(P\) has no chain of three distinct points. This includes incidence posets of finite graphs, fences, crowns, complete height-two posets, and arbitrary finite bipartite posets with order directed from one side to the other. No assumption of connectedness, purity, or minimality is imposed on \(P\). The target levels \(A_i\) may have arbitrary positive cardinalities, including singleton levels.

Continuity is identified with order preservation for finite \(T_0\)-spaces. Homotopy is ordinary topological homotopy of maps between finite spaces.

## Proof
Because \(P\) has no three-point chain, every point having a strict lower neighbor has no strict upper neighbor. Let \(L\) be the set of points with no strict lower neighbor and put \(U=P\setminus L\). Then every strict relation of \(P\) has the form \(x<u\) with \(x\in L\) and \(u\in U\). Isolated points lie in \(L\).

Choose points
\[
a\in A_{h-2},\qquad b\in A_{h-1},\qquad t\in A_h.
\]
Starting from an arbitrary order-preserving map \(f:P\to W\), define \(f_1\) by changing only points of \(L\): if \(x\in L\) and \(f(x)\) lies in \(A_{h-1}\cup A_h\), set \(f_1(x)=a\); otherwise set \(f_1(x)=f(x)\). On \(U\), set \(f_1=f\). Pointwise, \(f_1\le f\). To check monotonicity, take a strict relation \(x<u\). If \(x\) was unchanged, monotonicity is inherited from \(f\). If \(x\) was changed, then \(f_1(x)=a\). Since \(f(x)\) originally lay in one of the top two target levels and \(f(x)\le f(u)\), the value \(f(u)\) lies in \(A_{h-1}\cup A_h\), so \(a<f(u)=f_1(u)\). Thus \(f_1\) is order preserving.

Now define \(f_2\) by changing only points of \(U\): if \(u\in U\) and \(f_1(u)\in A_h\), set \(f_2(u)=b\); otherwise set \(f_2(u)=f_1(u)\). Keep \(f_2=f_1\) on \(L\). Then \(f_2\le f_1\). If \(x<u\) and \(u\) is changed, the preceding construction guarantees that \(f_1(x)\) lies in one of the levels \(A_1,\ldots,A_{h-2}\), hence \(f_2(x)=f_1(x)<b=f_2(u)\). All other relations remain valid. Therefore \(f_2\) is order preserving.

The image of \(f_2\) avoids the top level \(A_h\): top-level values on \(L\) were removed when constructing \(f_1\), and top-level values on \(U\) were removed when constructing \(f_2\). Consequently \(f_2(x)\le t\) for every \(x\in P\), so \(f_2\le c_t\), where \(c_t\) is the constant map with value \(t\).

For finite Alexandroff spaces, pointwise-comparable continuous maps are homotopic. Hence the comparison fence
\[
f\ge f_1\ge f_2\le c_t
\]
shows that \(f\) is null-homotopic. Since every map is connected by such a fence to the same constant map, the finite function space \(W^P\) is path connected.

For sharpness, take the two-level weak order \(C_2=A_1\oplus A_2\) with \(|A_1|=|A_2|=2\). Its order complex is a circle. The identity induces the identity on \(H_1\), while a constant map induces zero, so the identity is not homotopic to a constant. Thus the conclusion fails in general with only two target levels.

## Verification
The symbolic proof uses only the source height-two decomposition and the total ordering of target levels. A standalone verifier exhaustively checked the explicit construction on all \(104\) combinations formed by bipartite source sides of sizes at most two, every bipartite relation pattern, and four weak-order target level profiles with three or four nonempty levels. It checked \(18{,}598\) monotone maps and verified that both intermediate maps are monotone and satisfy the required pointwise inequalities. The verifier output was:

`VERIFY_OK source_cases=104 maps=18598 sharp_height2=checked`

This finite stress test is not the proof of the quantified theorem; the proof above is.

## Relationship to prior work
Barmak and Minian identify finite \(T_0\)-spaces with finite posets for purposes of continuous maps and record the standard beat-point/core framework; their 2006 preprint also develops minimal finite models of spheres and graphs. May’s finite-space notes state explicitly that pointwise-comparable maps between Alexandroff spaces are homotopic, and for finite source and target the compact-open specialization order on the function space is the pointwise order. These are the two standard finite-space facts used by the proof.

A closely related enumerative literature studies order-preserving maps involving fences and crowns. Farley’s 1995 paper computes numbers of order-preserving and order-reversing maps between fences and crowns, and explicitly describes an endpoint-counting strategy for maps from crowns. That work is enumerative and its stated source-target classes are fences and crowns; it does not supply the height-two-to-multilevel weak-order null-homotopy statement proved here.

A previously checked finding, opaque item `3a228577-217e-47ba-aa9c-2de9261840fb`, proves null-homotopy for maps between weak orders of different heights. The present result is not a special case of that statement: the source here is an arbitrary height-two finite poset and need not be a weak order. The proof also yields a uniform three-comparison homotopy fence independent of the source incidence pattern.

## Limitations
The theorem concerns direct maps of finite spaces and ordinary finite-space homotopy. It does not claim that the full mapping space \(W^P\) is contractible; only path connectedness is proved. It also does not classify maps when the target has exactly two levels, where non-null classes can occur. No claim is made for source spaces containing a three-point chain, and the proof uses the height-two hypothesis essentially when separating source points into lower and upper sides.

## References
1. J. A. Barmak and E. G. Minian, “Minimal Finite Models,” arXiv:math/0611156, first public version 2006-11-06.
2. J. P. May, “Finite Spaces and Larger Contexts,” Proposition 3.2.12 and Corollary 3.2.11, available from the University of Chicago finite-spaces notes.
3. J. D. Farley, “The Number of Order-Preserving Maps between Fences and Crowns,” Order 12 (1995), 5–44, DOI 10.1007/BF01108588.
