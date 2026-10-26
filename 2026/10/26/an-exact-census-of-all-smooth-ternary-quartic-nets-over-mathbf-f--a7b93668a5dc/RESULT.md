# An exact census of all-smooth ternary quartic nets over \(\mathbf F_2\)

## Finding
Let \(V=H^0(\mathbf P^2_{\mathbf F_2},\mathcal O(4))\), a vector space of dimension \(15\). Call a three-dimensional vector subspace \(U\subset V\) **all-smooth** if every one of its seven nonzero sections defines a geometrically smooth plane quartic. Then the exact number of all-smooth subspaces \(U\), counted in fixed projective coordinates, is
\[
\boxed{28\,336\,176}.
\]
Equivalently, there are this many projective planes in \(\mathbf P(V)\) all seven of whose \(\mathbf F_2\)-points lie outside the geometric singular-quartic discriminant. Every such all-smooth net has no common \(\mathbf F_2\)-rational base point. No assertion is made here about the number of projective-equivalence classes of these nets.

## Assumptions and scope
All forms, linear subspaces, rational points and linear changes of coordinates are over \(\mathbf F_2\). Smoothness is **geometric**: the quartic curve must be nonsingular after base change to an algebraic closure. The \(15\) monomials are ordered by descending exponent triples \((a,b,4-a-b)\), first by \(a\) and then by \(b\). An integer between \(0\) and \(2^{15}-1\) encodes its monomial coefficients in binary. Distinct subspaces are counted separately even if related by projective transformations; a vector subspace is not counted once per ordered basis.

## Proof
First construct the exact smoothness indicator \(s:V\to\{0,1\}\). For each polynomial \(F\), and each affine chart \(X_i=1\) with affine polynomial \(f\), the geometric Jacobian criterion says that this chart is nonsingular exactly if
\[
( f,\partial f/\partial u,\partial f/\partial v)=\mathbf F_2[u,v].
\]
The inclusion of \(f\) is essential in characteristic two. The unit-ideal test is exact by the algebraic-closure Nullstellensatz. All \(2^{15}-1\) nonzero forms are partitioned into \(279\) orbits using substitutions \((X,Y,Z)\mapsto(Y,X,Z),(Y,Z,X),(X+Y,Y,Z)\), which generate \(\operatorname{GL}_3(\mathbf F_2)\). Gröbner tests of one representative per orbit yield \(78\) smooth-form orbits and \(10\,920\) smooth coefficient vectors. An independent grevlex Gröbner implementation checks all \(279\) representatives and agrees.

For each nonzero smooth vector \(a\), define \(B_a(h)=s(h)s(h+a)\). For any \(b\) with \(s(b)s(a+b)=1\), the number of vectors \(h\) for which the seven nonzero elements of \(\langle a,b,h\rangle\) are smooth equals
\[
C_a(b)=\sum_{h\in V}B_a(h)B_a(h+b).
\]
The product imposes smoothness at \(h,h+a,h+b,h+a+b\), while the condition on \(b\) imposes it at \(a,b,a+b\). The zero and dependent vectors contribute zero automatically because \(s(0)=0\). Every all-smooth three-space gives precisely \(7\cdot6\cdot4=168\) ordered independent triples \((a,b,h)\). Therefore the exact net count is
\[
N=\frac{1}{168}\sum_{a:s(a)=1}\ \sum_{b:s(b)s(a+b)=1} C_a(b).
\]
The autocorrelation \(C_a\) is the inverse Walsh--Hadamard transform of the square of the Walsh--Hadamard transform of \(B_a\), divided by \(2^{15}\). Since coordinate transformations preserve \(s\), the outer sum may be taken on the \(78\) smooth-form representatives, each multiplied by its proven orbit size. Integer Walsh transforms give the **exact ordered-triple total**
\[
4\,760\,477\,568=168\cdot28\,336\,176.
\]
As an independent calculation, a separate C++ program constructs bitsets for each \(B_a\), uses 64-bit bit permutations to calculate each autocorrelation directly through population counts, and obtains the identical ordered-triple integer using the same independently reconstructible orbit representatives. This method does not invoke the Walsh transform.

Finally suppose the common rational base locus of an all-smooth net contained \(P\in\mathbf P^2(\mathbf F_2)\). Evaluation of every section at \(P\) would vanish. The first derivative at \(P\) would then give a linear map from the three-dimensional \(U\) to the two-dimensional cotangent space of the surface at \(P\). Some nonzero \(F\in U\) lies in the kernel, so both its value and first derivatives vanish at \(P\), contradicting geometric smoothness.

## Verification
Run `python genquartic_maps.py` and `python quartic_representative_check.py` from this directory (requires SymPy). This regenerates the smoothness indicator, projective orbits, and transformation tables. Run `python quartic_nets_walsh.py` (requires NumPy) to reproduce the exact net count and ordered triple total. Compile and run `nets_direct.cpp` with a C++17 compiler to reproduce the same number by a different autocorrelation method; `quartic_reps.csv` contains the \(78\) verified smooth representatives and their orbit sizes. The source generator's computed `smoothquartic_orbits.json` must match these representatives. The remaining executable programs reproduce the pre-existing smooth-pencil count \(5\,796\,728\), providing a separate consistency test for the indicator and projective actions. Their results are supporting checks, not the new finding itself. Reference output is included in `verification_results.txt`. All arithmetic is exact.

## Relationship to prior work
Asgarli and Ghioca (2022) establish the theory and existence of smooth pencils over finite fields; Asgarli, Ghioca and Reichstein (2022) analyze dimensions of linear systems with only smooth rational members and prove general upper bounds. Neither inspected article contains the present fixed-field count of all-smooth three-dimensional subspaces of ternary quartic forms. The census of individual smooth binary plane quartics (\(10\,920\)) and their all-smooth two-dimensional pencils (\(5\,796\,728\)) is previous work: **these numbers are not claimed as new**. The new item is solely the \(28\,336\,176\)-net count and its all-base-point-free interpretation.

## Limitations
This is an exhaustive finite-field enumeration with algebraically exact smoothness tests, not a uniform formula for arbitrary fields or degrees. The net-count calculation depends on complete finite enumeration, verified by two distinct exact algorithms, rather than a short closed-form hand calculation. No projective orbit classification of the nets or classification of their geometric base schemes is claimed. Literature indexing may miss earlier unpublished computations; external independent audit has not been performed.

## References
1. B. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169, first posted 2022-03-14, https://arxiv.org/abs/2203.07169.
2. B. Asgarli, D. Ghioca and Z. Reichstein, *Linear families of smooth hypersurfaces over finitely generated fields*, arXiv:2207.00918, first posted 2022-07-02, https://arxiv.org/abs/2207.00918.
