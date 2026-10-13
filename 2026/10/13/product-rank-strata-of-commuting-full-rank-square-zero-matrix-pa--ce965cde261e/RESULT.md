# Product-rank strata of commuting full-rank square-zero matrix pairs over finite fields

## Finding
Fix an arbitrary prime power \(q\) and a positive integer \(m\). Let \(\mathcal C_{m,q}(r)\) be the set of ordered pairs \((X,Y)\) of \(2m\)-by-\(2m\) matrices over \(\mathbb F_q\) such that \(X^2=Y^2=0\), \(XY=YX\), \(\operatorname{rank}X=\operatorname{rank}Y=m\), and \(\operatorname{rank}(XY)=r\). These are labeled pairs, **not** simultaneous-similarity classes. With the conventions \(\left[{a\atop b}\right]_q=0\) unless \(0\le b\le a\), \(|\mathrm{GL}_0(q)|=1\), and
\[
\left[{a\atop b}\right]_q=\prod_{j=0}^{b-1}\frac{q^{a-j}-1}{q^{b-j}-1},\qquad
|\mathrm{GL}_a(q)|=\prod_{j=0}^{a-1}(q^a-q^j),
\]
one has, for every integer \(r\) with \(0\le r\le\lfloor m/2\rfloor\),
\[
\boxed{|\mathcal C_{m,q}(r)|=\left[{2m\atop m}\right]_q|\mathrm{GL}_m(q)|\left[{m\atop r}\right]_q\left[{m-r\atop r}\right]_q|\mathrm{GL}_r(q)|q^{2r(m-r)}|\mathrm{GL}_{m-2r}(q)|.}
\]
All other product-rank strata are empty; every listed stratum is nonempty. In particular, whenever the product is nonzero, its rank is at most \(\lfloor m/2\rfloor\), or one quarter of the ambient matrix dimension rounded down. This bound is attained. Summing the formula over the listed \(r\) gives the exact total number of commuting maximal-rank square-zero pairs.

This provides the complete finite-field rational-point distribution of the multiplication-rank statistic on the locus of **two commuting maximal-rank square-zero matrices**. Unlike the mutually annihilating subcase \(XY=YX=0\), the strata with \(r>0\) have a nonzero product and detect nontrivial module structure over \(\mathbb F_q[x,y]/(x^2,y^2)\).

## Assumptions and scope
All matrices act on column vectors over \(k=\mathbb F_q\). No condition on the characteristic is imposed, and \(q\) may be a nonprime prime power. The hypotheses require square-zero, mutual commutativity, and **both** factors of the maximal possible square-zero rank \(m\) in dimension \(2m\). This is not a statement about arbitrary commuting nilpotent pairs, noncommuting pairs, or the number of isomorphism classes of modules. The small case \(m=1\) has only \(r=0\). Expressions for negative-dimensional general-linear groups are never used: \(r\) is restricted to the stated range.

## Proof
**Step 1: Fix one maximal-rank square-zero operator.** As \(X^2=0\) and \(\operatorname{rank}X=m\), the image and kernel of \(X\) coincide and have dimension \(m\). Choosing a complement gives
\[
X=\begin{pmatrix}0&I_m\\0&0\end{pmatrix}.
\]
Conversely, choose its common image/kernel in \(\left[{2m\atop m}\right]_q\) ways, then choose the induced isomorphism \(k^{2m}/\ker X\to\ker X\) in \(|\mathrm{GL}_m(q)|\) ways. Thus precisely \(\left[{2m\atop m}\right]_q|\mathrm{GL}_m(q)|\) choices of \(X\) exist.

**Step 2: Reduce the second operator.** An elementary block multiplication gives \(XY=YX\) precisely when
\[
Y=\begin{pmatrix}A&B\\0&A\end{pmatrix}
\]
for \(m\)-by-\(m\) matrices \(A,B\). The square-zero equation is exactly
\[
A^2=0,\qquad AB+BA=0,
\]
with the same formula valid in characteristic two. Moreover, \(XY=\begin{psmallmatrix}0&A\\0&0\end{psmallmatrix}\), so the desired product rank is \(r=\operatorname{rank}A\). Since \(A^2=0\), \(r\le\lfloor m/2\rfloor\).

**Step 3: Count choices of \(A\).** For any fixed \(r\) in the permitted range, choose \(I=\operatorname{im}A\) of dimension \(r\), then \(K=\ker A\) of dimension \(m-r\) containing \(I\), then the isomorphism \(k^m/K\to I\) defining \(A\). These choices give exactly
\[
S_m(r)=\left[{m\atop r}\right]_q\left[{m-r\atop r}\right]_q|\mathrm{GL}_r(q)|.
\]
The formula includes \(r=0\), where the unique \(A\) is zero.

**Step 4: Count the allowable \(B\) and its rank condition.** Put \(h=m-2r\). A basis adapted to \(I\subset K\subset k^m\) puts \(A\) in block form
\[
A=\begin{pmatrix}0&0&I_r\\0&0&0\\0&0&0\end{pmatrix},
\]
with block sizes \(r,h,r\). Solving \(AB+BA=0\) by block multiplication gives **all** solutions
\[
B=\begin{pmatrix}P&Q&R\\0&S&T\\0&0&-P\end{pmatrix},
\]
where \(P,R\) are arbitrary \(r\)-by-\(r\) matrices, \(Q\) has size \(r\)-by-\(h\), \(T\) has size \(h\)-by-\(r\), and \(S\) is an arbitrary \(h\)-by-\(h\) matrix. The displayed minus sign remains appropriate in characteristic two, where it equals plus. In intrinsic terms, \(S\) is the induced map \(\bar B\) on \(K/I\).

To calculate the rank of \(Y\), write its action as \(Y(v,w)=(Av+Bw,Aw)\). A kernel vector must satisfy \(w\in K\); it admits a solution for \(v\) precisely if \(Bw\in I\), i.e. \(\bar B(w+I)=0\). Once \(w\) is chosen, the set of possible \(v\) has dimension \(m-r\). Therefore
\[
\dim\ker Y=2(m-r)-\operatorname{rank}S,
\qquad
\operatorname{rank}Y=2r+\operatorname{rank}S.
\]
The required \(\operatorname{rank}Y=m\) is equivalent to invertibility of \(S\) on the \(h\)-space. There are \(|\mathrm{GL}_h(q)|\) choices for \(S\) and precisely \(q^{2r^2+2rh}=q^{2r(m-r)}\) independent choices for \(P,Q,R,T\), giving \(q^{2r(m-r)}|\mathrm{GL}_{m-2r}(q)|\) suitable \(B\) for each \(A\).

**Step 5: Multiply and prove nonemptiness.** Multiply the independent counts in Steps 1, 3, and 4. For each \(0\le r\le\lfloor m/2\rfloor\), a rank-\(r\) square-zero \(A\) exists and setting \(S=I_h\), with other blocks zero, produces a maximal-rank square-zero commuting \(Y\), proving every permitted rank occurs. No other rank occurs by Step 2. This completes the proof.

## Verification
The accompanying standalone Python 3 program, `verify.py`, uses only the standard library. Execute `python3 verify.py` after extracting it from the same package. The checker constructs finite fields of orders \(2,3,4,5\), including \(\mathbb F_4\) as a quadratic extension; performs independent finite-field Gaussian elimination; directly enumerates all \(A\) for the indicated small tests and all \(B\) for canonical \(A\); and checks \(A^2=0\), \(AB+BA=0\), \(\operatorname{rank}Y=m\), and all predicted counts. Cases run include \((m,q)=(1,2),(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2)\). The last three cases use canonical \(A\) instead of enumerating every \(m\)-by-\(m\) matrix \(A\); in the first five cases the full \(A\) census is performed. Replay prints `VERIFY_OK` on success. These finite checks are independent sanity tests; the proof above covers all \(m\) and all prime powers \(q\).

For \(m=2,q=2\), the number of \(X\) is \(210\); per \(X\) the two rank strata have \(6\) and \(12\) choices of \(Y\). Hence the total counts are \(1260\) at \(r=0\) and \(2520\) at \(r=1\). For \(m=4,q=2\), the per-\(X\) counts for \(r=0,1,2\) are \(20160,40320,53760\), respectively, illustrating the sharp rank cutoff.

## Relationship to prior work
Paul Levy's *Varieties of Modules for Z/2Z x Z/2Z* (first public preprint 6 September 2006), particularly Sections 1–3 and Lemma 2.1, studies the restricted nilpotent commuting variety, its block centralizers, its irreducible components, and the rank labels attached to components over algebraically closed fields; in characteristic two it connects this geometry to modules over the same truncated algebra. Those geometric descriptions motivate the present question, but do not supply the explicit count of \(\mathbb F_q\)-rational labeled pairs simultaneously constrained by the two maximal individual ranks and \(\operatorname{rank}(XY)=r\). Britnell–Wildon study *which* similarity classes commute and their centralizers, not this prescribed product-rank fiber. Basili–Iarrobino study Jordan partitions and Hilbert functions for commuting nilpotent pairs, primarily over infinite fields rather than finite-field point counts.

A related exact rank-and-image-intersection formula for **mutually annihilating** square-zero pairs only concerns the sublocus \(XY=YX=0\), that is, the \(r=0\) boundary here; that result cannot provide the nonzero-product counts \(r\ge1\). The new formula includes the boundary for completeness, but the positive-rank strata and their sharp complete distribution are the substantive result. The formula is not a statement about algebraic-geometric component dimensions, generic Jordan type, or a published matrix-commutation incidence count without these constraints.

## Limitations
The claim is restricted to pairs of commuting square-zero operators each of maximal possible rank in even matrix dimension. It does not enumerate arbitrary square-zero ranks, higher nilpotence indices, or simultaneous conjugacy orbits. The verification program exhausts only the indicated small finite instances; no finite test certifies the infinite-parameter theorem. A historical equivalent formula in unindexed or incompletely accessible representation-theoretic enumeration literature cannot be ruled out by the inspected sources; bibliographic priority is not independently established. There has been no independent mathematical audit.

## References
1. P. Levy, *Varieties of Modules for Z/2Z x Z/2Z*, arXiv:math/0609180 (first public submission 2006-09-06), Journal of Algebra **318** (2007), 933–952, DOI:10.1016/j.jalgebra.2007.06.024.
2. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811 (first public submission 2010-01-06), Journal of the London Mathematical Society **83** (2011), 470–492, DOI:10.1112/jlms/jdq088.
3. R. Basili and A. Iarrobino, *Pairs of commuting nilpotent matrices, and Hilbert function*, arXiv:0709.2304 (2007).
