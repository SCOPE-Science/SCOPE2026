# Non-smooth projective stabilizers of Kollár's characteristic-two cusp curves

## Finding
Let \(k=\overline{\mathbb F}_2\) and \(q=2^n\) for any integer \(n\geq1\). Let \(C_q\subset\mathbb P^2_k\) be the integral plane curve
\[
 C_q:\quad Z^2Y^q=X^{q+2}+XZ^{q+1}.
\]
Let \(G_q\) be its scheme-theoretic stabilizer inside \(\operatorname{PGL}_{3,k}\). Its group of geometric points, its reduced geometric group, and its Zariski tangent space at the identity are as follows.

For \(q\geq4\),
\[
 G_q(k)=\{[X:Y:Z]\mapsto[a^qX:aY:Z]:a^{q+1}=1\}
 \cong\mu_{q+1}(k),\qquad (G_q)_{\mathrm{red}}\cong\mu_{q+1}.
\]
In particular the reduced stabilizer is finite of order \(q+1\). In the exceptional quartic case \(q=2\),
\[
 G_2(k)=\left\{[X:Y:Z]\mapsto
 [a^2X+b^2Z:aY+(b^4+b)Z:Z]:a^3=1,\ b\in k\right\}
 \cong(k,+)\rtimes\mu_3(k),
\]
and \((G_2)_{\mathrm{red}}\cong\mathbb G_a\rtimes\mu_3\), with \(\mu_3\) acting on \(\mathbb G_a\) by scalar multiplication. For every \(n\geq1\), independently of this jump in the reduced group,
\[
 \boxed{\dim_k T_eG_q=3.}
\]
Thus \(G_q\) is non-smooth, hence nonreduced, for **every** \(q=2^n\). In the degrees \(q+2\geq6\) the reduced stabilizer is zero-dimensional even though it has three independent infinitesimal projective automorphisms.

## Assumptions and scope
The base field is the algebraic closure of \(\mathbb F_2\); group points mean geometric projective linear transformations, not arbitrary abstract automorphisms of the singular curve. The scheme \(G_q\) is defined by the condition that a projective change of homogeneous coordinates carry the principal homogeneous ideal of \(C_q\) to itself. Only its reduced group and tangent dimension are determined, not the full nilpotent group-scheme structure. All integers \(n\geq1\) are covered, including the exceptional \(n=1\) boundary.

## Proof
**Normalization and linear series.** Kollár's explicit parametrization [1, Example 1, Lemma 2, Example 3] gives a finite birational map
\[
 \nu_q:\mathbb P^1_k\longrightarrow C_q,
 \qquad [T:U]\longmapsto[T^qU^2:T^{q+2}+TU^{q+1}:U^{q+2}].
\]
On \(U\ne0\) it is the closed affine embedding \(t\mapsto(t^q,t^{q+2}+t)\). The affine curve is smooth, since its defining equation has derivative \(1\) with respect to \(X\) there. Its unique singular point is \([0:1:0]\), with unique normalization preimage \([1:0]\). Hence every projectivity preserving \(C_q\) lifts uniquely to an automorphism of \(\mathbb P^1\) fixing \([1:0]\), and so has the form \(t\mapsto at+b\), where \(a\in k^*\) and \(b\in k\). A projectivity induces, and is induced by, preservation of the three-dimensional basepoint-free linear series
\[
 V_q=\langle1,t^q,t^{q+2}+t\rangle
 \subset H^0(\mathbb P^1,\mathcal O(q+2)).
\]

**All geometric stabilizer points.** Frobenius and the characteristic-two binomial identity give
\[
 \begin{aligned}
 (at+b)^q&=a^qt^q+b^q,\\
 (at+b)^{q+2}+(at+b)
 &=a^{q+2}t^{q+2}+a^qb^2t^q+a^2b^qt^2+at+b^{q+2}+b.
 \end{aligned}
\]
If \(q\geq4\), the monomial \(t^2\) is absent from \(V_q\), forcing \(a^2b^q=0\), hence \(b=0\). Comparison of the coefficients of \(t^{q+2}\) and \(t\) then forces \(a^{q+2}=a\), equivalently \(a^{q+1}=1\). Conversely these conditions preserve \(V_q\) and induce the stated diagonal projectivity.

If \(q=2\), the two potential \(t^2\) contributions cancel in characteristic two. The transformed last generator is \(a^4t^4+at+b^4+b\). Thus preservation of \(V_2\) is equivalent to \(a^3=1\), with \(b\) arbitrary; the explicitly displayed projectivities realize all such affine changes. Composition on the normalization is \((a,b)(a',b')=(aa',ab'+b)\), proving the semidirect-product description. The matrix formulas also identify the corresponding reduced closed subgroups: in the quartic case the inverse to the parametrized translation subgroup is polynomial in its two displayed translation coordinates, so it is reduced; in the higher-degree cases \(q+1\) is odd, making \(\mu_{q+1}\) reduced.

**Infinitesimal stabilizer.** Put \(F=Z^2Y^q+X^{q+2}+XZ^{q+1}\). In characteristic two, for every \(q=2^n\),
\[
 F_X=Z^{q+1},\qquad F_Y=0,\qquad F_Z=XZ^q.
\]
A first-order projective transformation \(I+\epsilon D\), with \(\epsilon^2=0\), has rows
\[
 D_X=A X+B Y+C Z,\quad
 D_Y=D_0X+E Y+H_0Z,\quad
 D_Z=J X+K Y+L Z.
\]
Its first-order change is
\[
 \delta F=(A+L)XZ^{q+1}+B YZ^{q+1}+C Z^{q+2}
 +JX^2Z^q+KXYZ^q.
\]
For \(q\geq2\) these five monomials are pairwise distinct. As \(F\) contains \(X^{q+2}\) but \(\delta F\) does not, the condition \(\delta F\in kF\) reduces to \(\delta F=0\). Hence \(B=C=J=K=0\) and \(L=A\). There are four free matrix parameters \(A,D_0,E,H_0\). Quotienting by the one-dimensional scalar matrices yields \(\dim_k\operatorname{Lie}(G_q)=3\), as claimed. The reduced groups have dimensions zero for \(q\geq4\) and one for \(q=2\). Their tangent dimensions therefore differ from that of \(G_q\), which cannot be smooth or reduced over the perfect field \(k\).

## Verification
The self-contained companion program `check_stabilizers.py` enumerates all affine normalization changes over \(\mathbb F_{q^2}\) for \(q=2,4,8\), using exact finite-field arithmetic and preservation of the linear series. It obtains respectively \(12,5,9\) changes, matching \(q^2(q+1)\) for \(q=2\) and \(q+1\) for \(q=4,8\). It separately checks independence of the five infinitesimal monomials. Its expected output begins `STABILIZER_CHECK_OK`. The computations do not prove the all-\(n\) assertions; these follow from the explicit general expansions above.

## Relationship to prior work
Kollár [1] introduced the curves, proved their rationality and single multiplicity-two cusp, and used them for characteristic-dependent resolution and lifting phenomena. This result concerns their complete projective stabilizer and its mismatch with infinitesimal symmetries, which are not computed in [1]. Borges, Korchmáros and Speziali [2] study plane curves invariant under certain large finite linear groups; their objects, finite subgroup hypotheses and conclusions do not give this stabilizer classification or its non-smooth group scheme. The Frobenius-induced non-smoothness is essential: the group of geometric points alone does not recover the infinitesimal stabilizer.

## Limitations
Only projective-linear automorphisms of the embedded singular curves are classified. The full abstract automorphism groups and the full defining equations or lengths of the nonreduced stabilizer schemes are not determined. Search-based originality assessment is not a proof that no equivalent earlier characterization appears under a different parametrization; literature on positive-characteristic strange curves or automorphism schemes may contain further comparisons. Verification by small finite fields is supportive rather than exhaustive.

## References
[1] János Kollár, *Planar, rational curves over \(\mathbb F_2\) whose only singularity is a double point*, arXiv:2603.04211 (first posted 2026-03-04), Example 1, Lemma 2, Example 3, Remarks 6–8, https://arxiv.org/html/2603.04211.

[2] H. Borges, G. Korchmáros and P. Speziali, *Plane curves with a large linear automorphism group in characteristic \(p\)*, arXiv:2202.05765 (2022), Introduction, §2, https://arxiv.org/pdf/2202.05765.
