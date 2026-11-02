# A nonclosed-range counterexample and precise closed-range repair for woven \(K\)-frames

## Finding and definitions
Let \(H\) be a complex or real Hilbert space, \(K\in\mathcal B(H)\), and let \((f_i)\), \((g_i)\) be families of vectors of \(H\) indexed by a common finite or countable set \(I\). For a partition \(\sigma\subset I\) and \(x\in H\), define its weaving energy
\[
 E_\sigma(x)=\sum_{i\in\sigma}|\langle x,f_i\rangle|^2+
 \sum_{i\notin\sigma}|\langle x,g_i\rangle|^2.
\]
The image families are **\(K\)-woven in \(H\)** with bounds \(C,D>0\) if, for all partitions and all \(h\in H\),
\[
 C\|K^*h\|^2\le E_\sigma(K^*h)\le D\|h\|^2.
\tag{1}
\]
If \(M\) is a closed subspace, two families **of vectors in \(M\)** are woven ordinary frames for \(M\) if their weaving energies lie between \(A\|x\|^2\) and \(B\|x\|^2\) for every \(x\in M\), uniformly in the partition. Distinguish this standard definition from the weaker statement that ambient-space vectors merely satisfy the same inequalities when tested on \(M\).

Bhandari, Borah, and Mukherjee's Proposition 2.5 (*Characterizations of Weaving \(K\)-frames*, 2019/2020) asserts, for arbitrary bounded \(K\), equivalence between wovenness of \((f_i),(g_i)\) in \(R(K^*)\) and \(K\)-wovenness of \((Kf_i),(Kg_i)\) in \(H\). The reverse implication fails even if its left side is interpreted only as ambient frame inequalities on \(R(K^*)\).

## Explicit failure without closed range
Let \(H=\ell^2(\mathbb N)\), \(Ke_n=n^{-1}e_n\), and \(f_n=g_n=ne_n\). The operator \(K\) is bounded, self-adjoint, and has dense nonclosed range. Each original vector \(ne_n\) actually belongs to \(R(K^*)\), so the failure is not merely a missing-subspace-membership issue. Since \(Kf_n=Kg_n=e_n\), every transformed weave is the standard orthonormal basis, and
\[
 E_\sigma(K^*h)=\|h\|^2,\qquad \|K^*h\|^2\le\|h\|^2.
\]
Thus the image pair is \(K\)-woven with bounds \(1,1\). But with \(x_N=K^*e_N=N^{-1}e_N\in R(K^*)\),
\[
 E_\sigma(x_N)=1,\qquad\|x_N\|^2=N^{-2},
\]
so the energy/norm-squared ratio is \(N^2\), unbounded for every weave. No upper ambient frame inequality on \(R(K^*)\) exists.

Indeed,
\[
 R(K)=\{(y_n)\in\ell^2:\sum_{n\ge1}n^2|y_n|^2<\infty\}.
\]
The vector \((1/n)_{n\ge1}\) is in \(\ell^2\) but not in \(R(K)\), while its finite truncations lie in the range and converge to it. The use of a nonclosed range also means that \(R(K^*)\) with the inherited norm is not a Hilbert space; the inequality contradiction above avoids relying only on that definitional problem.

## Correct closed-range equivalence, with projection
**Theorem.** Assume \(K\) has closed range and put \(M=R(K^*)\), \(P=P_M\). The following are equivalent:

1. The projected families \((Pf_i)_{i\in I}\) and \((Pg_i)_{i\in I}\) are woven ordinary frames for the Hilbert space \(M\).
2. The image families \((Kf_i)_{i\in I}\) and \((Kg_i)_{i\in I}\) are \(K\)-woven in \(H\).

If condition 1 has uniform bounds \(A,B>0\), condition 2 has bounds \(A,B\|K\|^2\) whenever \(K\ne0\). If condition 2 has bounds \(C,D>0\), condition 1 has bounds \(C,D\|K^\dagger\|^2\) whenever \(K\ne0\). For \(K=0\), both sides reduce to the vacuous frame inequalities on \(\{0\}\), for which any positive bounds may be chosen. If all original \(f_i,g_i\) already lie in \(M\), the projections can be omitted; *without this membership assumption*, closed range guarantees the equivalence of the ambient inequalities but not literal wovenness of the unprojected families **as vectors of \(M\)**.

**Proof.** For every \(x\in M\), orthogonal projection gives \(\langle x,Pf_i\rangle=\langle x,f_i\rangle\) and likewise for \(g_i\); the projected weaving energy at \(x\) is \(E_\sigma(x)\). Moreover, \(\langle h,Kf_i\rangle=\langle K^*h,f_i\rangle\) and similarly for \(g_i\); hence (1) is exactly the pair of inequalities
\[
 C\|K^*h\|^2\le E_\sigma(K^*h)\le D\|h\|^2.
\]
From a woven frame pair on \(M\) with bounds \(A,B\), choose \(x=K^*h\) and use \(\|K^*h\|\le\|K\|\|h\|\). This yields bounds \(A,B\|K\|^2\) for the images.

Conversely, suppose (1) holds. Closed range makes the Moore–Penrose inverse \((K^*)^\dagger\) bounded. Every \(x\in M\) has the minimum-norm preimage \(h=(K^*)^\dagger x\) with \(K^*h=x\) and
\[
 \|h\|\le\|(K^*)^\dagger\|\,\|x\|=\|K^\dagger\|\,\|x\|.
\]
Substitution in (1) gives, uniformly over every partition,
\[
 C\|x\|^2\le E_\sigma(x)\le D\|K^\dagger\|^2\|x\|^2.
\]
As the projected vectors belong to \(M\), these are genuine ordinary-frame inequalities there, proving both directions. \(\square\)

## Why subspace membership matters
Closed range alone does not make each unprojected \(f_i\) belong to \(R(K^*)\). For example, take \(H=\mathbb R^2\), \(K=P_{\operatorname{span}(e_1)}\), and a single-index pair \(f_1=g_1=e_1+e_2\). Its image is \(e_1\), a \(K\)-frame with bounds \(1,1\). But the unprojected vector is not an element of the Hilbert space \(R(K^*)=\operatorname{span}(e_1)\). The projected vector \(Pf_1=e_1\) is a frame there and satisfies the theorem. This example does *not* contradict the ambient restricted inequality, which holds; it isolates the additional literal-frame membership requirement.

## Scope and relationship to prior work
The counterexample identifies a failed implication in the printed 2019/2020 characterization, and the theorem repairs the actual quantitative content with closed range, projection and explicit constants. It does not prove closed range necessary for an individual fixed pair, and does not address definitions that equip a nonclosed operator range with a different quotient/graph norm.

The source's Proposition 1.4 grants uniform upper bounds for weaves of **already Bessel** families; it cannot infer the upper bound of the original families from Bessel bounds on the images. The source's adjacent Proposition 2.6 explicitly uses a closed-range hypothesis for another operator-range implication. Later operator-transfer work imposing closed range is consistent with this correction, but that alone neither supplies this counterexample nor proves bibliographic priority. The exact, finite-index membership observation is independent of the nonclosed-range counterexample.

## References
1. A. Bhandari, D. Borah and S. Mukherjee, *Characterizations of Weaving \(K\)-frames*, arXiv:1907.08757 (2019), *Proc. Japan Acad. Ser. A* 96 (2020), 39–43, DOI 10.3792/pjaa.96.008; Proposition 2.5, its proof, and Proposition 2.6.
2. Z.-Q. Xiang, *Some new results on the weaving of \(K\)-\(g\)-frames in Hilbert spaces*, *Open Mathematics* 19 (2021), 1315–1329, DOI 10.1515/math-2021-0103.
3. G. Wang, *Some properties of weaving \(K\)-frames in \(n\)-Hilbert space*, *AIMS Mathematics* 9 (2024), 25438–25456, DOI 10.3934/math.20241242.
