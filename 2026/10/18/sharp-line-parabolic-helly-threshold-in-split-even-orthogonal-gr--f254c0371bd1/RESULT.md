# Sharp line-parabolic Helly threshold in split even orthogonal groups

## Finding

**Theorem (point-apartment criterion and sharp restricted Helly number).** For each integer \(m\ge4\), let \(V\) be a \(2m\)-dimensional complex vector space with a nondegenerate symmetric bilinear form \(B\) of Witt index \(m\), and put \(G=\mathrm{SO}(V,B)\). For a finite family of **distinct** isotropic projective lines \(\mathcal L=\{L_1,\ldots,L_s\}\), let \(P_i\le G\) be the parabolic subgroup stabilizing \(L_i\). Choose arbitrary nonzero representatives \(v_i\in L_i\). Form the graph \(\Gamma\) on \(\{1,\ldots,s\}\), with an edge \(ij\) exactly when \(B(v_i,v_j)\ne0\).

The following are equivalent:

1. The parabolics \(P_i\) contain one common maximal torus of \(G\) (equivalently, all the lines lie among the coordinate lines of one hyperbolic frame).
2. Every vertex of \(\Gamma\) has degree at most one, and the vectors belonging to the isolated vertices are linearly independent.

Every inclusion-minimal incompatible family is consequently either (a) three isotropic lines with one line nonorthogonal to both other lines, or (b) a minimally linearly dependent family of pairwise orthogonal isotropic lines. In case (b), the number of lines is between \(3\) and \(m+1\).

In particular, the **optimal Helly number restricted to isotropic-line stabilizers** is
\[
\boxed{h_{\mathrm{line}}(\mathrm{SO}_{2m})=m+1.}
\]
Thus compatibility of every subfamily of at most \(m+1\) such parabolics implies compatibility of the entire family, and \(m\) tests do not suffice.

**Toric-bundle consequence.** For each \(d\ge2\), every toric principal \(\mathrm{SO}_{2m}\)-bundle on \(\mathbb P^d_{\mathbb C}\) whose ray parabolics are stabilizers of isotropic lines splits *equivariantly* if and only if \(d\ge m+1\). More precisely, for every \(2\le d\le m\) there exists a nonsplit bundle in this restricted class.

## Assumptions and scope

The base field is \(\mathbb C\); the symmetric form is nondegenerate and split. The rank range is \(m\ge4\). The family of isotropic lines is finite and contains no repetitions. Compatibility means a **common maximal torus**, not merely pairwise common tori or a parabolic intersection of positive dimension. Graph edges are invariant under rescaling line representatives. The toric assertion uses the standard \(d+1\) rays of the fan of \(\mathbb P^d\), the classification of framed toric principal bundles via their ray parabolics, and *equivariant* (not ordinary) splitting. No statement is made about arbitrary parabolic types or the unrestricted Helly number of type \(D_m\).

## Proof

**Step 1: necessary incidence and independence conditions.** Every maximal torus of \(\mathrm{SO}(V,B)\) is conjugate to the diagonal torus of a hyperbolic basis
\[
(e_1,\ldots,e_m,f_1,\ldots,f_m),\qquad B(e_i,f_j)=\delta_{ij},\quad B(e_i,e_j)=B(f_i,f_j)=0.
\]
Its standard representation has \(2m\) distinct one-dimensional weights. Thus any torus-invariant line is one of these coordinate lines. Among distinct such lines, the only nonzero pairings occur between the two lines of a hyperbolic pair; hence \(\Gamma\) is a matching. Distinct coordinate representatives are independent, especially at its isolated vertices.

**Step 2: sufficiency.** Suppose \(\Gamma\) is a matching with \(r\) edges. The two lines at each edge span a nondegenerate hyperbolic plane; different such planes are mutually orthogonal. Their orthogonal sum \(U\) has dimension \(2r\) and is nondegenerate. All remaining (isolated) line representatives lie in \(U^\perp\), pair to zero with one another and are independent by assumption. Their span \(W\subset U^\perp\) is therefore totally isotropic of dimension equal to the number of isolated lines. The form on \(U^\perp\) is split of Witt index \(m-r\). By Witt's hyperbolic-basis extension, a basis of \(W\) extends to an isotropic half of a hyperbolic basis of \(U^\perp\), with dual complementary isotropic lines. Together with the hyperbolic pairs in \(U\), this gives a hyperbolic basis of \(V\) whose coordinate lines include all \(L_i\). Its diagonal maximal torus lies in each \(P_i\), proving (1).

**Step 3: classify minimal failures.** If some vertex of \(\Gamma\) has two neighbors, those three lines violate Step 1; any two distinct isotropic lines do fit in a hyperbolic frame (their pairing is either zero or nonzero). Thus any minimal failure of this type has three lines. Otherwise \(\Gamma\) is a matching. Failure of Step 2 then produces a minimally dependent subset of the isolated line representatives. They are pairwise orthogonal, so the span of any independent proper subset is totally isotropic, of dimension at most \(m\). Consequently a minimal dependent subset has at most \(m+1\) members. It cannot have two members because the projective lines are distinct. Conversely, a three-line nonorthogonality obstruction and any orthogonal linear circuit are incompatible while all proper subfamilies are compatible, by Steps 1–2.

**Step 4: derive the optimal threshold.** If every subfamily of size at most \(m+1\) is compatible, Step 3 excludes every minimal incompatible subfamily; hence the whole family is compatible. For sharpness choose a totally isotropic \(m\)-plane \(E=\langle e_1,\ldots,e_m\rangle\) and the \(m+1\) distinct lines
\[
\mathbb C e_1,\ldots,\mathbb C e_m,\quad \mathbb C(e_1+\cdots+e_m).
\]
Their representatives form a circuit: every \(m\)-element subset is independent, so it can be completed to a hyperbolic frame by Step 2, whereas all \(m+1\) are dependent and cannot be distinct torus weight lines. Hence \(m\) does not suffice.

**Step 5: the projective-space threshold.** A toric principal bundle on \(\mathbb P^d\) has \(d+1\) ray parabolics. Every proper subset of those rays lies in a cone, so Proposition 5.1 of Tsvelikhovskiy makes each proper family of ray parabolics compatible. If \(d\ge m+1\), every collection of at most \(m+1\) rays is a proper subfamily, hence compatible. Step 4 forces all ray parabolics to have a common maximal torus. The same proposition then yields equivariant splitting. Conversely, if \(2\le d\le m\), assign to the \(d+1\) rays the isotropic-line stabilizers of
\[
\mathbb C e_1,\ldots,\mathbb C e_d,\quad\mathbb C(e_1+\cdots+e_d).
\]
Every proper subfamily is independent and pairwise orthogonal, hence compatible, but the full family is incompatible by Step 2. Proposition 5.1 therefore constructs a toric principal \(G\)-bundle with these exact ray parabolics, and its global incompatibility certifies nonsplitting. This proves the claimed sharp threshold in the stated restricted class.

## Verification

The standalone Python 3 program `verify_examples.py` carries out exact rational linear-algebra checks, **not** a substitute for the infinite-rank proof. Run from the same package directory with `python3 verify_examples.py`. It checks every \(4\le m\le12\) and every \(2\le d\le m\): isotropy and pairwise orthogonality of the \(d+1\)-line circuit, full rank \(d\), independence of all \(d\)-line subfamilies, and the sharp example at \(d=m\). It also tests mixed matching and three-line incidence obstructions. The check has been executed successfully, with terminal result `EXACT_TESTS_OK`.

## Relationship to prior work

Tsvelikhovskiy, arXiv:2610.11340v1 (first public 8 October 2026), proves \(h(G)\le m+2\) for general rank-\(m\) connected reductive groups and records \(m+1\le h(D_m)\le m+2\). His Section 4 already establishes the **unrestricted lower bound** using \(\mathrm{GL}_m\hookrightarrow\mathrm{SO}_{2m}\); the circuit in Step 4 is **not** claimed to be a new general lower-bound construction. His Proposition 5.9 gives the weaker \(m+2\) test for the isotropic-line parabolic Levi type, while Proposition 5.1 supplies the bundle reconstruction/splitting principle used here. What is added is the exact **restricted** upper bound, complete two-obstruction criterion, and the corresponding dimension threshold for bundles with isotropic-line ray parabolics. These do **not** determine the unresolved unrestricted number \(h(D_m)\).

The polar-frame/apartment literature, including Pankov's 2011 study of apartments in polar Grassmannians and Cooperstein's work on independent partial frames, supplies general geometric context. These results may already imply aspects of hyperbolic-frame extension; the new claim is the combined complete obstruction bound and sharp restricted toric-bundle application. The cited 2005/2014 partial-frame literature was accessible only through abstracts during this comparison, so exact overlap there remains a specifically identified risk.

## Limitations

The work concerns *only* maximal parabolics stabilizing isotropic one-dimensional subspaces in split even orthogonal groups over \(\mathbb C\), not parabolics of arbitrary types, other fields, symplectic groups, or the full Helly invariant of type \(D_m\). The finite checker verifies selected exact instances rather than every complex configuration. The toric statement concerns equivariant splittings and requires the ray-parabolic condition. A plausible residual priority risk exists in older partial-frame/Witt-type results whose full texts were not available for complete implication comparison; an equivalent formulation elsewhere cannot be excluded.

## References

1. B. Tsvelikhovskiy, *Helly Numbers for Connected Reductive Groups and Splitting of Toric Principal Bundles*, arXiv:2610.11340v1 (8 October 2026), Sections 4 and 5; especially Table 1, Proposition 5.1, and Proposition 5.9. https://arxiv.org/html/2610.11340v1
2. S. Huang and K. Kaveh, *Toric principal bundles, Tits buildings and reduction of structure group*, Documenta Mathematica 29 (2024), 815–830, DOI:10.4171/DM/962. https://ems.press/journals/dm/articles/14297952
3. M. Pankov, *Characterization of apartments in polar Grassmannians*, arXiv:1109.2555 (2011). https://arxiv.org/abs/1109.2555
4. B. N. Cooperstein, A. Kasikova, and E. E. Shult, *Witt-type theorems for Grassmannians and Lie incidence geometries*, Advances in Geometry 5 (2005), 15–36, DOI:10.1515/advg.2005.5.1.15 (abstract compared; full text unavailable).
5. B. N. Cooperstein, *Witt-Type Theorems for Subspaces of Lie Geometries: A Survey*, in *Groups of Exceptional Type, Coxeter Groups and Related Geometries* (2014), DOI:10.1007/978-81-322-1814-2_6 (abstract compared; full text unavailable).
