# Sharp centered maximal Hilbert norm and distance-two extremizers on the triangular prism

## Finding
On the unweighted triangular prism \(P=C_3\square K_2\), with counting measure, the centered Hardy–Littlewood maximal operator on graph balls has the exact, attained strong Hilbert norm
\[
\boxed{\|M_P\|_{\ell^2\to\ell^2}=\sqrt{\frac{123+\sqrt{7641}}{144}}\approx1.208801098270746.}
\]
Every nonzero real extremizer has, after taking coordinatewise absolute values and multiplying by a positive constant, the value \(1\) on an unordered pair at graph distance two and the common value
\[
a=\frac{\sqrt{7641}-73}{68}\approx0.211953142735306
\]
on the other four vertices. Conversely every such modulus profile is extremizing, with arbitrary independent coordinate signs. The six distance-two pairs give exactly six labeled nonnegative rays, forming one graph-automorphism orbit.

## Assumptions and scope
The vertex order is \(0,1,2,3,4,5\). The edges are the two triangles \(01,12,20\) and \(34,45,53\), together with the matching edges \(03,14,25\). Graph distance is the unweighted shortest-path metric. Each radius-zero ball has size \(1\), each radius-one ball has size \(4\), and every radius-two ball is the full six-vertex set. For any real \(f\),
\[
M_Pf(v)=\max_{r\in\{0,1,2\}}\frac1{|B(v,r)|}\sum_{w\in B(v,r)}|f(w)|,
\qquad \|f\|_2^2=\sum_{v=0}^5|f(v)|^2.
\]
The norm is the supremum over all nonzero real vertex functions. The result concerns centered, rather than uncentered, balls; no weights, other exponents, or larger Cartesian products are included.

## Proof
**Finite linearization.** For each radius selector \(c=(c_0,\ldots,c_5)\in\{0,1,2\}^6\), define the nonnegative averaging matrix \(B_c\) with row \(v\) equal to the normalized indicator of \(B(v,c_v)\). For any nonnegative input \(x\), each output coordinate of \(M_Px\) is one of three row averages. Choosing an attaining radius in each row gives \(M_Px=B_cx\). Hence
\[
\|M_Px\|_2^2\le\max_c\lambda_{\max}(B_c^{\mathsf T}B_c)\|x\|_2^2.
\]
It is enough to check all \(3^6=729\) matrices. Set \(T_c=12B_c\), an integer matrix, because the three ball sizes are \(1,4,6\). The symmetric integer matrix
\[
F_c=1044I-5T_c^{\mathsf T}T_c
=720\bigl((29/20)I-B_c^{\mathsf T}B_c\bigr)
\]
is positive definite exactly when the squared singular norm of \(B_c\) is smaller than \(29/20\). The included standalone Python certificate enumerates all selectors and checks positivity of all six leading principal minors of each \(F_c\), by exact fraction-free symmetric elimination and Sylvester's criterion. There are exactly \(723\) positive-definite cases. The remaining selectors are
\[
(0,1,2,1,0,2),\quad(0,2,1,1,2,0),\quad
(1,0,2,0,1,2),\quad(1,2,0,0,2,1),\quad
(2,0,1,2,1,0),\quad(2,1,0,2,0,1).
\]
They form precisely the orbit of the first selector under the permutations of the three triangle coordinates together with interchange of the two triangles. This gives an exact global comparison, not a numerical sampling argument.

**The exceptional spectrum.** For \(c_*=(0,1,2,1,0,2)\), its averaging matrix is
\[
B_*=
\begin{pmatrix}
1&0&0&0&0&0\\
1/4&1/4&1/4&0&1/4&0\\
1/6&1/6&1/6&1/6&1/6&1/6\\
1/4&0&0&1/4&1/4&1/4\\
0&0&0&0&1&0\\
1/6&1/6&1/6&1/6&1/6&1/6
\end{pmatrix}.
\]
Direct rational matrix multiplication gives the exact characteristic polynomial
\[
\det(\lambda I-B_*^{\mathsf T}B_*)
=\frac{\lambda^2(\lambda-1)(8\lambda-1)
(72\lambda^2-123\lambda+26)}{576}.
\]
Its largest eigenvalue is
\[
\lambda_*=(123+\sqrt{7641})/144>29/20;
\]
all the other eigenvalues are at most \(1\). The included verifier checks the characteristic polynomial by the integer Faddeev–LeVerrier recurrence for \(T_*^{\mathsf T}T_*\), without numerical diagonalization.

**Attainment and equality.** Put \(a=(\sqrt{7641}-73)/68\), so \(0<a<1\) and \(34a^2+73a-17=0\), and take
\[
x_*=(1,a,a,a,1,a)^{\mathsf T}.
\]
A direct multiplication shows that the two coordinates of \(B_*^{\mathsf T}B_*x_*\) at the high vertices equal \((49+17a)/36\), while the other four equal \((17+25a)/72\). The displayed quadratic identity gives \(B_*^{\mathsf T}B_*x_*=\lambda_*x_*\). Furthermore, the radius-zero averages at the high vertices equal \(1\), while the radius-one averages at vertices adjacent to both high vertices equal \((1+a)/2\), and the radius-two averages at vertices adjacent to just one high vertex equal \((1+2a)/3\). Comparison with the competing zero-, one-, and two-radius averages uses only \(0<a<1\) and shows that exactly \(c_*\) is selected. Therefore \(M_Px_*=B_*x_*\), and equality in the claimed bound is attained.

If equality holds for an arbitrary nonzero \(f\), apply linearization to \(x=|f|\). The strict bound \(29/20<\lambda_*\) rules out the \(723\) other selectors. The exceptional matrices are graph-automorphic. Their top eigenvalue is simple (as seen from the characteristic polynomial, or from positivity of the Gram matrices), and its positive eigenvector is unique up to scale. Thus \(|f|\) must be the transform of \(x_*\) under a graph automorphism. The two high vertices of \(x_*\) are at distance two, and the six automorphism images cover all six distance-two pairs. Conversely all these profiles attain equality. Independent signs do not affect \(M_P\) or the input \(\ell^2\) norm. This completes the classification.

## Verification
Run the bundled standalone, standard-library-only script with `python3 verification/triangular_prism_verify.py`. It reconstructs the graph metric from its nine edges, computes each ball indicator and each integer selector matrix, verifies \(723\) strict Sylvester certificates and the six exceptional selectors, and checks that those selectors form one automorphism orbit with distance-two high pairs. An independent exact characteristic-polynomial calculation identifies the exceptional spectrum, followed by numerical consistency checks of the explicitly proved radical eigenvector and strict active radii. Expected output begins `CERTIFICATE_OK selections=729 strict=723 exceptional=6 distance_two_pairs=6 characteristic=exact`.

The exact integer enumeration is exhaustive for the finite set of \(729\) selectors; the radical identities and the maximizing-radius comparisons are proved algebraically and are not inferred from floating-point tests.

## Relationship to prior work
Soria and Tradacete introduced graph-ball maximal operators and obtained optimal general graph bounds in the quasi-Banach range, together with some strong-exponent estimates for specific families [1]. González-Riquelme and Madrid computed exact strong Hilbert norms for complete graphs and stars and studied sharp variation questions [2]. These statements do not imply this triangular-prism value or its equality classification. Greenblatt studied dimensional asymptotics for maximal operators on Cartesian graph powers [3], rather than a closed sharp Hilbert norm and all extremizers for the single triangular prism. Work on generalized maximal operators on strong graph products [4] involves a different product metric and supplies bounds, not this exact constant.

The triangular prism is the nonbipartite member of the two connected simple cubic graphs on six vertices. Its sharp norm is attained by a two-level profile supported most strongly on a distance-two pair: a graph-theoretic characterization of every extremizer, not simply a numerical calculation. Search comparisons do not establish absolute publication priority; related unindexed calculations remain a risk.

## Limitations
Only this single unweighted graph, the centered ball operator, counting measure, and real \(\ell^2\) are covered. The finite selection certificate does not furnish a general formula for prism graphs of larger size or for product graphs. The characterization of all equality cases depends on the exact enumeration of \(729\) choices, not on a uniform graph-family theorem. Publication-priority checks cannot rule out unpublished or unindexed equivalent computations. Independent scientific validation has not been performed.

## References
[1] Javier Soria and Pedro Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204, first public version 2014-10-22, https://arxiv.org/abs/1410.6204.

[2] Cristian González-Riquelme and José Madrid, *Sharp Inequalities for maximal operators on finite graphs*, arXiv:2005.03146, first public version 2020-05-06, https://arxiv.org/abs/2005.03146.

[3] Jordan Schor Greenblatt, *Dimensional Asymptotics for Norms of Maximal Averaging Operators on Cartesian Powers of Finite Graphs*, UCLA dissertation (2016), https://escholarship.org/uc/item/16k3f6p1.

[4] Zaryab Hussain et al., *Estimates for the Norm of Generalized Maximal Operator on Strong Product of Graphs*, *Mathematical Problems in Engineering* (2021), doi:10.1155/2021/9338269.
