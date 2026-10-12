# Self-review

## Correctness
PASS. The normalization
\[
[u:v]\longmapsto[u^{4}:uv(u+v)^{2}:v^{4}]
\]
is checked directly and has an explicit rational inverse on a dense chart. The unique singular point is \([1:0:1]\). Every plane automorphism lifts to \(\mathbf P^{1}\), fixes its unique preimage \([1:1]\), and must preserve the pulled-back hyperplane series \(\langle u^{4},v^{4},uv(u+v)^{2}\rangle\). The coefficient equations reduce the normalization matrix uniquely to
\[
\begin{pmatrix}1+\lambda&\lambda\\ \lambda&1+\lambda\end{pmatrix},
\]
and the induced plane transformation is exactly the stated \(T_{\lambda}\). Exact symbolic verification checks preservation of the quartic and the additive group law. No finite experiment is used as an infinite-field proof.

## Originality
PASS. The closest primary source, arXiv:2409.05464, supplies the type-(4) equation, its universal fibration, singularity multiplicity, and strange/non-ordinary-inflection tangent geometry. Its isomorphism and automorphism statements concern regular function fields over the original ground field and do not imply the subgroup of \(\operatorname{PGL}_{3}(k)\) preserving the singular geometric member after base extension. The predecessor arXiv:2306.08579 likewise treats different function-field classes. Exact-equation, normalization, projective-stabilizer, additive-action, strange-curve, and smooth-orbit searches found no covering statement. Indexed stabilizer results located in the comparison search concern unrelated characteristic-zero curves and do not dominate this claim.

Residual risk: an older, poorly indexed classification of singular plane quartic automorphisms in positive characteristic could contain an equivalent coordinate calculation. No such source was located in the checked literature.

## Value
PASS. The source emphasizes that these quartics are strange and have highly nonclassical tangent behavior. Showing that the entire smooth locus is one simply transitive additive-group orbit provides a global structural explanation of that geometry and completely determines the plane symmetry group. This is not a renaming, a textbook deduction, or an arbitrary finite invariant.

## Limitations
The theorem concerns the \(c=1\) type-(4) plane model over an algebraically closed field of characteristic \(2\). It identifies the group of projective \(k\)-automorphisms, not the possibly nonreduced stabilizer scheme and not abstract non-projective automorphisms of the singular curve. No claim is made for all five Hilario--Stöhr families.

Self-review: passed. Independent audit: not yet performed.
