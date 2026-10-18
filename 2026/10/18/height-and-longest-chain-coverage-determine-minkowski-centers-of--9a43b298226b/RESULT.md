# Height and longest-chain coverage determine Minkowski centers of every chain–order poset polytope

## Finding

Let \(P\) be any finite nonempty poset, let \(h\) be its maximum chain cardinality, and partition its elements arbitrarily as \(P=C\sqcup O\). Adjoin a bottom element \(\hat 0\), fixed at \(0\), and a top element \(\hat 1\), fixed at \(1\). Let \(K_{C,O}(P)\) be the standard unmarked chain–order polytope: its coordinates \(x_c\) for \(c\in C\) are nonnegative, and for every saturated chain from \(a\in O\cup\{\hat0\}\) to \(b\in O\cup\{\hat1\}\) whose intervening elements \(c_1,\ldots,c_r\) lie in \(C\), the inequality \(x_{c_1}+\cdots+x_{c_r}\le y_b-y_a\) holds, where \(y_{\hat0}=0\), \(y_{\hat1}=1\), and \(r\ge0\) is allowed.

Write \(U(P)\) for the union of all chains of cardinality \(h\), and put \(q=1/(h+1)\). Then
\[
\boxed{s(K_{C,O}(P))=h,\qquad \dim\operatorname{aff}\mathcal M(K_{C,O}(P))=|P\setminus U(P)|.}
\]
Both invariants are independent of the partition \(C\sqcup O\), including non-admissible decompositions. Every minimizing center is *exactly* a solution of the following explicit linear system:
\[
 x_c\ge q\ (c\in C),\qquad
 y_b-y_a-\sum_{j=1}^r x_{c_j}\ge q
 \quad\text{for every defining saturated chain }a<c_1<\cdots<c_r<b.
\]
In particular, a minimizing center is unique if and only if every element belongs to a longest chain. An explicit minimizing center, valid for every partition, is
\[
 x_c=q\quad(c\in C),\qquad
 y_o=q\,d(o)\quad(o\in O),
\]
where \(d(o)\) is the maximum cardinality of a chain in \(P\) ending at \(o\).

## Assumptions and scope

The polytope is full-dimensional in its \(|P|\) free coordinates. The bottom and top elements are formal added markings, not counted in \(h\). The partition may be arbitrary: the 2018 extended definition of marked chain–order polytopes permits such partitions. No restriction to ranked posets, connected Hasse diagrams, or admissible order-ideal partitions is imposed. Minkowski asymmetry means \(s(K)=\min_{z\in K}\inf\{\lambda\ge1:-(K-z)\subseteq\lambda(K-z)\}\); \(\mathcal M(K)\) is the complete set of minimizing centers.

## Proof

**1. Unit widths.** Write each defining inequality as \(\ell(x)\le\beta\), where either \(\ell=-x_c,\beta=0\), or \(\ell=\sum_{j=1}^r x_{c_j}+y_a-y_b,\beta=0\) (using fixed boundary values in the latter expression). The maximum of \(\ell\) on \(K\) equals \(\beta\), and its minimum is \(\beta-1\). For \(-x_c\), the witnesses are the zero point and the point with \(x_c=1\), all other chain coordinates zero, and order coordinates equal to the indicator of the upper order filter of \(c\). For a saturated-chain inequality, its minimum follows by setting all chain coordinates to zero and choosing order coordinates as the indicator of the upper filter of \(b\), or all zero if \(b=\hat1\). An equality witness for its maximum is the all-zero free-coordinate point when \(b\ne\hat1\); when \(b=\hat1\) and \(a\in O\), take all order coordinates equal to one and all chain coordinates zero; in the remaining bottom-to-top case take a unit chain coordinate along that chain and its upper-filter order assignment. Every described witness satisfies the complete inequality system. Consequently every defining functional has **exact range one**, even if its inequality is redundant.

**2. Reflection criterion.** For \(\ell\le\beta\) whose minimum on \(K\) is \(\beta-1\), the inclusion \(-(K-z)\subseteq\lambda(K-z)\) holds with respect to that halfspace exactly when \(\beta-\ell(z)\ge1/(\lambda+1)\). This follows by maximizing \(\ell((1+1/\lambda)z-x/\lambda)\) over \(x\in K\). Applying the condition to every defining halfspace yields the displayed complete center system with \(q=1/(\lambda+1)\).

**3. Lower bound and attainment.** Contract each saturated run of chain elements between consecutive order/marked elements into an arc of a directed acyclic graph. An arc crossing \(r\) chain elements imposes \(y_b-y_a\ge\sum_{j=1}^r x_{c_j}+q\). Each chain coordinate has \(x_c\ge q\). A bottom-to-top path tracing a longest chain of \(h\) poset elements therefore yields \(1\ge(h+1)q\), so \(\lambda\ge h\). Conversely, take \(q=1/(h+1)\), put \(x_c=q\), and \(y_o=q\,d(o)\). For any contracted arc \(a<c_1<\cdots<c_r<b\), longest-chain cardinalities obey \(d(b)-d(a)\ge r+1\), with \(d(\hat0)=0\) and \(d(\hat1)=h+1\). Thus all center inequalities hold and \(\lambda=h\) is attained.

**4. Forced and free coordinates.** Every source-to-sink chain of cardinality \(h\) exhausts all \(h+1\) units of available slack. The inequalities used on that chain must be equalities at any minimizing center. Therefore each \(c\in U(P)\cap C\) has \(x_c=q\), and each \(o\in U(P)\cap O\) has \(y_o=q\,d(o)\). This proves the upper bound \(\dim\operatorname{aff}\mathcal M\le|P\setminus U(P)|\).

For the reverse bound, call a defining inequality *forced* if it participates in a longest source-to-sink chain. Each nonforced chain-coordinate inequality can be made strict by increasing its coordinate from \(q\) to \(q+\varepsilon\); each nonforced contracted-arc inequality can be made strict by increasing that arc's required slack from \(q\) to \(q+\varepsilon\). Choose \(0<\varepsilon<q\). Every path using the modified coordinate or arc originally had strictly fewer than \(h\) poset elements and hence at least \(q\) unused slack. Assign the order coordinates by longest weighted source-to-vertex paths in the contracted DAG; all inequalities remain feasible and the top distance is at most one. Thus each nonforced inequality is strict at some minimizing center. Averaging finitely many such centers gives one at which **all** nonforced inequalities are strict simultaneously. Every forced inequality involves only coordinates in \(U(P)\), already fixed by longest-chain equalities. Sufficiently small independent perturbations of all \(|P\setminus U(P)|\) remaining coordinates preserve the center conditions. Hence the opposite dimension inequality holds, proving equality and the unique-center criterion.

## Verification

Run `python verify.py` with Python 3 and no third-party packages. It enumerates all transitive closures of directed edge sets compatible with the natural order on up to five vertices, and every chain/order partition for each generated poset. For each case it constructs the saturated compressed-path description; validates explicit zero-one witnesses for every defining functional's unit width; validates the canonical center using exact integer scaling; and constructs strict-slack certificates for each inequality not used by a longest chain. It reports 33,866 finite poset/partition cases and 175,583 compressed paths. This checks finite instances only; the preceding proof establishes the theorem for every finite poset.

## Relationship to prior work

Fang and Fourier introduced the chain–order interpolation and its facet and Ehrhart questions [1]. Fang, Fourier, and Pegel extended the construction to arbitrary partitions and studied Minkowski **sums**, reflexivity, and marked-poset lattice structure [2]; Minkowski sums are different from reflected-containment asymmetry. Ahmad, Fourier, and Joswig studied maximal ranked posets, proved monotonicity of face counts along admissible chain–order interpolation, and provided a facet description [3]. In contrast, the present statement concerns the affine Minkowski asymmetry and the affine dimension of the complete center set, invariant even across arbitrary partitions and nonpure posets. The previously determined general order-polytope and stable-set-polytope center classifications cover the two endpoints, but do not imply the intermediate case under a piecewise-linear, generally non-affine transfer map. No claim is made that the underlying polytopes, face descriptions, or endpoint classifications are new.

## Limitations

The theorem concerns the unmarked interval with fixed boundary values zero and one, not arbitrary multilevel marked-poset polytopes. It does not classify the combinatorial face types of the center polytope beyond its affine dimension and explicit inequalities. The finite program does not certify infinitely many cases. A general antecedent in two-level polytope theory or under alternate asymmetry terminology remains a publication-priority risk; independent assessment is outstanding.

## References

[1] X. Fang and G. Fourier, *Marked chain-order polytopes*, arXiv:1508.02232, first posted 2015-08-10; https://arxiv.org/abs/1508.02232.

[2] X. Fang, G. Fourier, and C. Pegel, *The Minkowski Property and Reflexivity of Marked Poset Polytopes*, arXiv:1807.03970, first posted 2018-07-11; https://arxiv.org/html/1807.03970v2.

[3] I. Ahmad, G. Fourier, and M. Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626, first posted 2023-09-04; https://arxiv.org/html/2309.01626v2.
