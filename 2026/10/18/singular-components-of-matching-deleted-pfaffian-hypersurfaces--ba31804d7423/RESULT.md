# Singular components of matching-deleted Pfaffian hypersurfaces

## Finding

Let \(K\) be an algebraically closed field of characteristic zero. For integers \(m\ge 3\) and \(1\le k\le m\), write \(N=2m\) and let \(L_{N,k}\) be the vector space of alternating \(N\)-by-\(N\) matrices \(A\) satisfying \(a_{2i-1,2i}=0\) for \(1\le i\le k\); all other strict-upper-triangular entries are independent coordinates. Define the projective hypersurface
\[
X_{N,k}=\{[A]\in\mathbb P(L_{N,k}):\operatorname{Pf}(A)=0\}.
\]
Let \(R_{N,k}\) denote the projective locus of matrices of rank at most \(N-4\). For \(1\le i\le k\), put
\[
Z_i=\{[A]\in\mathbb P(L_{N,k}): A_{2i-1,j}=A_{2i,j}=0\text{ for all }j\}.
\]
Then \(X_{N,k}\) is an irreducible, reduced, normal, Cohen–Macaulay, Gorenstein hypersurface, and its **complete reduced singular locus** is
\[
\operatorname{Sing}(X_{N,k})_{\mathrm{red}}
=R_{N,k}\cup\bigcup_{i=1}^{k} Z_i.
\]
All \(k+1\) displayed subvarieties are distinct irreducible components. In \(X_{N,k}\), the codimension of \(R_{N,k}\) is \(5\), and the codimension of each \(Z_i\) is \(2N-5\).

At a general point of \(R_{N,k}\), the completed transverse hypersurface is a nondegenerate quadratic cone in six variables, equivalently the Pfaffian cone of a \(4\)-by-\(4\) alternating matrix. At a general point of each \(Z_i\), it is a nondegenerate quadratic cone in \(2(N-2)\) variables. Thus the two types of component have different generic quadratic slice dimensions (and have dimension \(\binom N2-k-7\) and \(\binom N2-k-2(N-2)-1\), respectively, in projective space).

## Assumptions and scope

The integer \(N\) is even and at least six, \(K\) has characteristic zero, and the forbidden positions form an actual matching, not an arbitrary graph. The singular locus is claimed only after reduction; this result makes no assertion about possible embedded components or the nonreduced structure of the Jacobian scheme. All codimensions refer to the projective hypersurface, not its ambient linear space. The quadratic normal form is at a **general** point of each irreducible component, not at arbitrary intersections of components.

## Proof

**1. Irreducibility and dimensions of the sparse rank loci.** Fix an even integer \(r\ge2\), and a nondegenerate alternating \(r\)-by-\(r\) matrix \(J_r\). Every alternating matrix of rank at most \(r\) can be expressed as \(A=BJ_rB^{\mathsf T}\) for some \(N\)-by-\(r\) matrix \(B\). Write \(b_j\) for its rows. Each of the \(k\) forbidden entries gives one equation \(b_{2i-1}J_rb_{2i}^{\mathsf T}=0\). This polynomial is an irreducible bilinear quadric, since the associated quadratic form has rank \(2r\ge4\). These equations involve disjoint sets of pairs of rows. Consequently their simultaneous zero locus in the \(Nr\)-dimensional space of \(B\)'s is irreducible of dimension \(Nr-k\).

The full-column-rank matrices form a nonempty dense open subset of this parameter space. For completeness, when \(r=2\), choose nonzero proportional vectors within each forbidden pair and use distinct pairs to span the two-dimensional target; the rank \(r=N-4\) case with \(r=2\) necessarily has \(N=6\). For \(r\ge4\), choose a symplectic basis ordered so that consecutive pairs of the first \(r\) rows are symplectically orthogonal; complete the remaining rows subject to their independent pairing constraints. For a full-column-rank \(B\), any other full-column-rank factorization of the same \(A\) differs by a symplectic \(r\)-by-\(r\) change of basis, a group of dimension \(r(r+1)/2\). Thus the sparse rank-at-most-\(r\) locus is irreducible of dimension
\[
Nr-k-\frac{r(r+1)}2.
\]
For \(r=N-2\), this equals \(\binom N2-k-1\), the expected dimension of \(X_{N,k}\); for \(r=N-4\), it equals \(\binom N2-k-6\). The Pfaffian is not the zero polynomial on \(L_{N,k}\): the complement of the forbidden matching has a perfect matching, so at least one Pfaffian matching monomial survives. The set \(\operatorname{Pf}(A)=0\) consists exactly of matrices of rank at most \(N-2\), hence is irreducible as a set. Step 2 exhibits smooth points, so the hypersurface equation is generically reduced and, being supported on an irreducible hypersurface, is irreducible as a polynomial up to a nonzero scalar. This also proves the asserted codimension \(5\) for \(R_{N,k}\) in \(X_{N,k}\).

**2. All points of the reduced singular locus.** The differential of the Pfaffian at an alternating \(A\) of rank \(N-2\) is, up to a nonzero scalar, the decomposable bivector \(u\wedge v\) spanning \(\bigwedge^2\ker(A)\). Equivalently, each free coordinate derivative is the corresponding signed principal \((N-2)\)-Pfaffian. The differential restricted to \(L_{N,k}\) vanishes exactly when
\[
u\wedge v\in\operatorname{span}\{e_{2i-1}\wedge e_{2i}:1\le i\le k\}.
\]
A nonzero decomposable bivector in the displayed span can have exactly one nonzero matching-pair coefficient: the Plücker relation on any two disjoint forbidden edges makes the product of their two coefficients zero. Therefore \(\ker(A)=\langle e_{2i-1},e_{2i}\rangle\) for one \(i\). This is equivalent to the two indicated rows and columns of \(A\) being zero. When \(\operatorname{rank}(A)\le N-4\), all first partial derivatives of the Pfaffian vanish automatically. These observations give the asserted singular-locus equality set-theoretically, and also show that the rank-\(N-2\) locus away from the \(Z_i\) is smooth.

Each \(Z_i\) is a linear space defined by \(2(N-2)\) independent entries: all cross-entries from its two distinguished indices to the other \(N-2\) indices. Its generic point has rank \(N-2\), since the complementary sparse alternating \((N-2)\)-by-\((N-2)\) matrix may be chosen invertible (the remaining forbidden edges are again a matching, whose complement has a perfect matching). Thus \(Z_i\) is not contained in \(R_{N,k}\), and neither is \(R_{N,k}\) contained in any \(Z_i\), because a generic full-column-rank factorization in Step 1 has no simultaneously zero row pair. Distinct \(Z_i\) are evidently not contained in one another. Since \(R_{N,k}\) is irreducible by Step 1 and each \(Z_i\) is irreducible and linear, this proves that there are exactly \(k+1\) irreducible components. The dimension of \(Z_i\) gives codimension \(2(N-2)-1=2N-5\) inside \(X_{N,k}\).

**3. The two generic quadratic slices.** At a generic rank-\(N-4\) point \(A\in R_{N,k}\), use an invertible alternating \((N-4)\)-by-\((N-4)\) block. Pfaffian Schur complement reduces the local equation, up to a unit, to the Pfaffian of a \(4\)-by-\(4\) alternating matrix \(S\). The six entries of \(S\) provide transverse regular parameters. Indeed, writing \(W=\ker(A)\) (dimension four), the differential of the Schur-complement map is restriction of alternating forms in \(L_{N,k}\) to \(\bigwedge^2W\). Failure of surjectivity would give a nonzero bivector common to \(\bigwedge^2W\) and the span of the forbidden coordinate bivectors. Any such nonzero combination has support containing a full forbidden coordinate two-plane, so \(W\) would contain that two-plane. A generic matrix of rank \(N-4\) from Step 1 has no two simultaneously zero rows in a forbidden pair, so this does not happen. Hence the six restrictions are independent. In these parameters the equation is exactly
\[
\operatorname{Pf}(S)=s_{12}s_{34}-s_{13}s_{24}+s_{14}s_{23}=0,
\]
a nondegenerate quadratic form of rank six.

At a general point \(A\in Z_i\), the complementary \((N-2)\)-by-\((N-2)\) alternating block \(B\) is invertible. Write the two formerly zero rows against the complementary indices as the rows \(u,v\) of a free \(2\)-by-\((N-2)\) block \(U\). The distinguished \(2\)-by-\(2\) block is zero because its one off-diagonal entry was forbidden. Schur complement gives the local equation, up to the unit \(\operatorname{Pf}(B)\), as
\[
q_B(u,v)=uB^{-1}v^{\mathsf T}=0.
\]
This is a nondegenerate quadratic form of rank \(2(N-2)\) in the \(2(N-2)\) independent coordinates of \(U\). The other allowed coordinates, those of \(B\), are smooth along \(Z_i\).

**4. Normality and other properties.** The preceding codimensions show that the singular locus has codimension at least five in the irreducible hypersurface. Thus the hypersurface is regular in codimension one. A hypersurface ring is Cohen–Macaulay (hence satisfies Serre's condition \(S_2\)) and Gorenstein. Serre's criterion \(R_1+S_2\) implies normality, completing the proof.

## Verification

The self-contained Python program `verification/check_pfaffian.py` is a finite-field reproducibility check, not an infinite proof. Run it with `python3 verification/check_pfaffian.py`. It uses only the Python standard library, samples all matching-deletion sizes for matrix orders six and eight over \(\mathbb F_{101}\), checks Pfaffian derivatives against the proposed singularity criterion, and evaluates exact Hessian ranks at both generic component types. The program's fixed seed makes its samples reproducible. A successful replay prints `VERIFY_OK`.

## Relationship to prior work

The general Pfaffian rank stratification and Pfaffian differentiation are classical. De Negri and Gorla study Pfaffian ideals of **ladders** and prove structural results including normality and Cohen–Macaulayness; their ladder definition uses connected square subladders, rather than the complement of an independent matching of removed entries in a full alternating matrix [1]. Their later work computes multiplicity and regularity of ladder Pfaffian ideals [2]. Goryunov and Mond study Tjurina and Milnor invariants of deformations and lower-dimensional sections of matrix singularities [3]. These results motivate the problem but do not, in their inspected statements, give the all-parameter singular-component decomposition or two transverse quadratic models here. General-purpose results about the full alternating Pfaffian rank locus are used as input, not presented as newly established facts.

## Limitations

The conclusion concerns one distinguished combinatorial sparsity pattern: a matching of forbidden off-diagonal entries. It does not classify arbitrary sparse alternating matrices, does not describe the Jacobian ideal's embedded or nonreduced structure, and does not classify singularities at intersections of the displayed components. The elementary characteristic-zero proof is not a claim about all positive characteristics. The work has not received an independent review; possible earlier equivalent formulations in the broad sparse-Pfaffian or combinatorial matching literature remain an overlap risk.

## References

[1] E. De Negri and E. Gorla, *G-biliaison of ladder Pfaffian varieties*, arXiv:0809.3417v1 (posted 19 September 2008), https://arxiv.org/abs/0809.3417.

[2] E. De Negri and E. Gorla, *Invariants of ideals generated by pfaffians*, arXiv:1303.6874v1 (posted 27 March 2013), https://arxiv.org/abs/1303.6874.

[3] V. Goryunov and D. Mond, *Tjurina and Milnor numbers of matrix singularities*, J. London Math. Soc. 72 (2005), 205–224, https://doi.org/10.1112/S0024610705006575.
