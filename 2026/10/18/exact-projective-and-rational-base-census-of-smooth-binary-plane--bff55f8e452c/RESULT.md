# Exact projective and rational-base census of smooth binary plane-quartic pencils

## Finding

Let \(V=\mathbf F_2[X,Y,Z]_4\), a vector space of dimension \(15\). A **smooth pencil** is a two-dimensional \(\mathbf F_2\)-linear subspace \(W\subset V\) such that each of its three nonzero forms cuts out a geometrically smooth plane quartic. Here equations, rather than individual abstract isomorphism classes of curves, are the objects being counted. Each of the three smooth members has genus three.

**Theorem.** There are exactly \(5{,}796{,}728\) smooth pencils. Under the natural coordinate action of \(\operatorname{PGL}_3(\mathbf F_2)\), they form exactly \(34{,}539\) orbits. Their complete orbit-size distribution is

| Stabilizer order | Orbit size | Number of orbits | Number of pencils |
|---:|---:|---:|---:|
| \(1\) | \(168\) | \(34{,}488\) | \(5{,}793{,}984\) |
| \(3\) | \(56\) | \(48\) | \(2{,}688\) |
| \(7\) | \(24\) | \(2\) | \(48\) |
| \(21\) | \(8\) | \(1\) | \(8\) |
| **Total** | | **34,539** | **5,796,728** |

Every nontrivial stabilizer has odd order. A stabilizer of order \(21\) is the normalizer \(C_7\rtimes C_3\) of a subgroup of order seven.

Let \(B(W)=\bigcap_{0\ne F\in W}V(F)(\mathbf F_2)\) denote the rational base set (the rational points common to all three curves). Its complete distribution is

| \(\#B(W)\) | Number of pencils |
|---:|---:|
| \(0\) | \(1{,}883{,}160\) |
| \(1\) | \(2{,}388{,}848\) |
| \(2\) | \(1{,}171{,}800\) |
| \(3\) | \(302{,}904\) |
| \(4\) | \(45{,}640\) |
| \(5\) | \(4{,}200\) |
| \(6\) | \(168\) |
| \(7\) | \(8\) |
| **Total** | **5,796,728** |

The eight pencils with all seven rational points in their base form precisely the unique eight-element orbit above.

## Assumptions and scope

All coefficient arithmetic and point counts are over \(\mathbf F_2\). Smoothness is **geometric**: there are no singular points over an algebraic closure, not merely no rational singular points. The coordinate group is the \(168\)-element \(\operatorname{PGL}_3(\mathbf F_2)=\operatorname{GL}_3(\mathbf F_2)\). Linear pencils are not ordered generating pairs. No assertion is made about orbit equivalence under arbitrary isomorphisms of the three member curves or about geometric reducedness of the length-sixteen base scheme.

We encode a ternary quartic by a nonzero 15-bit mask, reading its monomials \(X^iY^jZ^{4-i-j}\) in descending \(i\), then descending \(j\). This fixes an unambiguous exact computational domain of \(2^{15}-1=32{,}767\) equations.

## Proof

**Exact geometric smoothness criterion.** Put \(S=\mathbf F_2[X,Y,Z]\), with \(S_d\) its homogeneous degree-\(d\) part. For a quartic \(F\), let \(J=(F,F_X,F_Y,F_Z)\). The degree-ten multiplication map is

\[
\Phi_F:S_6\oplus S_7^{\oplus3}\longrightarrow S_{10},\qquad
(A,B,C,D)\longmapsto AF+BF_X+CF_Y+DF_Z.
\]

The plane curve is geometrically smooth **if and only if** \(\operatorname{rank}(\Phi_F)=66=\dim S_{10}\). Indeed, if the degree-ten component of \(J\) spans \(S_{10}\), a projective common zero of \(F\) and its partials would force every homogeneous degree-ten form to vanish there, impossible. Conversely, if that set has no projective common zero over an algebraic closure, then the degree-four forms in \(J\) have no common projective zero. Three generic degree-four forms in that ideal form a homogeneous regular sequence of degrees \((4,4,4)\). Their quotient has Hilbert series \((1+t+t^2+t^3)^3\), with top degree nine. Thus the degree-ten component of their ideal, hence of \(J\), is all \(S_{10}\). Extension of scalars preserves matrix rank, so the criterion is exact over \(\mathbf F_2\).

The program `pencils_main.cpp` constructs \(\Phi_F\) in a fixed degree-ten monomial basis, performs exact binary Gaussian elimination for every one of the \(32{,}767\) masks, and finds precisely \(10{,}920\) smooth quartics. For any two distinct nonzero forms \(A,B\), the three nonzero forms of their span are \(A,B,A+B\). Of the unordered pairs of distinct smooth forms, precisely \(17{,}390{,}184\) have a smooth sum. Each pencil contributes its three unordered pairs, giving

\[
\#\{\text{smooth pencils}\}=\frac{17{,}390{,}184}{3}=5{,}796{,}728.
\]

For the rational base set it suffices to evaluate two generating forms at the seven projective binary points. The exact bit-mask counts give the second table. Independently of pair iteration, `pencils_fourier.cpp` counts the same pencils by Walsh-transform convolution: for any specified rational-point subset \(T\), let \(s_T\) be the indicator of smooth forms vanishing at all points of \(T\), with \(s_T(0)=0\). Then

\[
P_T=\frac{1}{6\cdot2^{15}}\sum_{\chi\in\widehat V}\widehat{s_T}(\chi)^3
\]

counts pencils having \(T\) in their base. Summing over \(T\) of each cardinality and applying binomial inversion reproduces all eight entries of the table exactly.

**Projective orbit count.** The program expands all \(168\) invertible binary coordinate substitutions on quartic coefficients. Its exact fixed-pencil counts for an element of each possible order are

| Element order | Number of elements | Smooth pencils fixed by each |
|---:|---:|---:|
| \(1\) | \(1\) | \(5{,}796{,}728\) |
| \(2\) | \(21\) | \(0\) |
| \(3\) | \(56\) | \(98\) |
| \(4\) | \(42\) | \(0\) |
| \(7\) | \(48\) | \(7\) |

These are invariant under conjugacy; for the two order-seven conjugacy classes, invariance under any nontrivial element of a common cyclic subgroup is equivalent. Burnside's lemma gives

\[
\frac{5{,}796{,}728+56(98)+48(7)}{168}=34{,}539.
\]

A separate subgroup test identifies exactly one pencil fixed by the full order-\(21\) normalizer of a chosen Sylow-seven subgroup. Since every subgroup of order \(21\) is conjugate and self-normalizing, this means there is exactly one orbit with stabilizer of order \(21\). The vanishing order-two fixed count shows that all stabilizers have odd order, hence order \(1,3,7\), or \(21\). If the numbers of orbits with these stabilizer orders are \(u_1,u_3,u_7,u_{21}\), standard orbit-stabilizer double counting gives \(u_3+u_{21}=49\), \(3u_7+u_{21}=7\), and \(u_{21}=1\). With their sum \(34{,}539\), this yields \((u_1,u_3,u_7,u_{21})=(34{,}488,48,2,1)\).

## Verification

`pencils_main.cpp` is a standalone C++17 exact enumeration (compile with `g++ -O3 -std=c++17 pencils_main.cpp -o pencils_main`, then execute from the containing folder). It creates `smooth_form_masks.txt` and `smooth_representatives.txt` and prints the full counts. `pencils_fourier.cpp` compiles analogously, reads the smooth-mask list, and independently verifies the combinatorial pencil totals and all rational base-point counts by Fourier convolution rather than pair enumeration. `verify_groebner.py` uses SymPy over characteristic two to confirm that all \(78\) projective-coordinate orbits of quartic forms labelled smooth have unit affine Jacobian ideals on each of the three standard charts: \(234\) separate ideal checks.

All three programs were executed successfully, with transcripts saved as `pencils_main.out`, `pencils_fourier.out`, and `verify_groebner.out`. The two counting methods agree entry by entry. The Gröbner checker corroborates smoothness of every smooth-form projective orbit; it does **not** independently classify every nonsmooth form, so completeness of the original smooth-form list rests on the proved rank criterion and the exhaustive rank enumeration.

## Relationship to prior work

Asgarli and Ghioca, *Smoothness in pencils of hypersurfaces over finite fields* (arXiv:2203.07169, first public 14 March 2022), formulate and prove existence of smooth pencils under field-size hypotheses and give exact small-degree examples. Their theorem does not count or classify all quartic pencils over \(\mathbf F_2\). Asgarli, Ghioca and Reichstein, *Linear families of smooth hypersurfaces over finitely generated fields* (arXiv:2207.00918), prove general existence and dimension restrictions, not the incidence and orbit census here.

Nart and Ritzenthaler, *Non-hyperelliptic curves of genus three over finite fields of characteristic two* (arXiv:math/0312366), classify **individual smooth plane quartics** up to field isomorphism. That classification is background and does not itself enumerate two-dimensional coefficient subspaces with all three members smooth. Asgarli, Ghioca and Yip, *Existence of pencils with nonblocking hypersurfaces* (arXiv:2301.09215), study a distinct memberwise property; its existence result does not determine these counts. The eight quartic pencils whose members contain all seven rational points form a **properly contained special case**, not the complete present classification.

## Limitations

This is an exact, finite-field, fixed-degree theorem, not an asymptotic result or an existence theorem for other fields or degrees. Counts are for coefficient-subspace pencils and for rational-coordinate projective equivalence, not for unlabeled tuples of abstract genus-three curves. Rational base-set counts do not determine geometric intersection multiplicities. Novelty is assessed against inspected accessible sources and research-record searches, not asserted as an exhaustive priority guarantee; an unindexed equivalent computation remains possible. 

## References

1. S. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169 (2022), https://arxiv.org/abs/2203.07169.
2. S. Asgarli, D. Ghioca and Z. Reichstein, *Linear families of smooth hypersurfaces over finitely generated fields*, arXiv:2207.00918 (2022), https://arxiv.org/abs/2207.00918.
3. E. Nart and C. Ritzenthaler, *Non-hyperelliptic curves of genus three over finite fields of characteristic two*, arXiv:math/0312366 (2004), https://arxiv.org/abs/math/0312366.
4. S. Asgarli, D. Ghioca and C. H. Yip, *Existence of pencils with nonblocking hypersurfaces*, arXiv:2301.09215 (2023), https://arxiv.org/abs/2301.09215.
