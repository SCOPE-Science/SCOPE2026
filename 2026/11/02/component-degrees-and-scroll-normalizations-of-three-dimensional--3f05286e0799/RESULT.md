# Component degrees and scroll normalizations of three-dimensional orthogonal-frame varieties

## Finding
For each integer \(h\ge4\), let \(V=\mathbb C^3\) carry a nondegenerate symmetric form \(B\). Let \(Z_h\subset\mathbb P(V^{\oplus h})\cong\mathbb P^{3h-1}\) be the **reduced** projectivization of the affine zero locus of
\[
 B(v_i,v_j)=0\quad (1\le i<j\le h).
\]
Then the complete projective component-degree profile is as follows.

* For each three-element subset \(J\subset\{1,\ldots,h\}\), there is a component \(A_J\) supported on the coordinate subspace with \(v_i=0\) for \(i\notin J\). It has \(\dim A_J=5\) and \(\deg A_J=8\).
* For each \(i\in\{1,\ldots,h\}\), there is a component \(W_i\), the closure of configurations for which \(v_i\) is anisotropic and all other columns belong to one isotropic line \(\ell\subset v_i^\perp\). It has \(\dim W_i=h+1\) and \(\deg W_i=2h\). Its normalization, together with the pullback of the ambient hyperplane class, is the scroll
\[
 \mathbb P_{\mathbb P^1}\bigl(\mathcal O(-1)^{\oplus2}\oplus\mathcal O(-2)^{\oplus(h-1)}\bigr).
\]
Its natural map to the ambient projective space uses a codimension-one subspace of the full tautological linear series.

These are exactly the \(\binom h3+h\) irreducible components. All have generic scheme-theoretic multiplicity \(1\) in the scheme defined by the original Gram quadrics. At \(h=4\), all eight components have dimension \(5\) and degree \(8\); their total cycle degree is \(64\). For \(h\ge5\), the top-dimensional cycle has degree \(2h^2\), with the \(\binom h3\) components \(A_J\) living in smaller dimension.

## Assumptions and scope
The field is \(\mathbb C\); the quadratic form is nondegenerate; the tuple has \(h\ge4\) **ordered** columns. Degrees are for the ordinary hyperplane bundle from the embedding in \(\mathbb P^{3h-1}\). The quadratic zero scheme need not be globally reduced when \(h\ge5\); generic multiplicity refers only to the local ring at the generic point of each irreducible component. A point of the affine cone with all columns zero is irrelevant to projectivization.

## Proof
**1. Exhaustion and irreducibility.** Call a column anisotropic if \(B(v_i,v_i)\ne0\). Nonzero pairwise orthogonal anisotropic columns are independent and span a nondegenerate subspace. If three columns are anisotropic, all others are zero: the tuple belongs to \(A_J\). If exactly two are anisotropic, all remaining columns are zero, since their common orthogonal complement is a nondegenerate one-dimensional space and has no nonzero isotropic vector. Replacing one zero column by a small nonzero vector in this complement exhibits the tuple as a limit within some \(A_J\).

If exactly one column \(v_i\) is anisotropic, its perpendicular is a nondegenerate plane. All other columns must be isotropic. Two nonproportional isotropic vectors in a nondegenerate complex plane cannot be orthogonal; hence all remaining nonzero columns lie on one isotropic line \(\ell\subset v_i^\perp\), so the tuple lies in \(W_i\). If no column is anisotropic, every nonzero column is isotropic; by the Witt-index-one property in dimension three, pairwise orthogonal nonzero isotropic columns are proportional. Such tuples likewise lie in the closures \(W_i\). Thus the listed closed loci cover \(Z_h\).

For each \(J\), the anisotropic orthogonal triples form the image of \(\mathrm{SO}(3,\mathbb C)\times(\mathbb C^*)^3\) after choosing a split orthogonal basis. This is irreducible and dense in \(A_J\). The irreducibility of \(W_i\) follows from the projective-bundle construction below. Every \(A_J\) has a dense open locus with three anisotropic columns, which belongs to no \(W_i\) and no other \(A_{J'}\). For \(h\ge4\), a general \(W_i\) has one anisotropic column and at least three nonzero isotropic columns, hence belongs to neither another \(W_j\) nor any \(A_J\). Therefore every listed variety is maximal and the list is exhaustive.

**2. Incidence normalization of the isotropic components.** Let \(Q\subset\mathbb P(V)\) be the conic of isotropic lines, so \(Q\cong\mathbb P^1\). Its tautological subline \(S\subset V\otimes\mathcal O_Q\) satisfies \(S\cong\mathcal O_{\mathbb P^1}(-2)\). Let \(K=S^\perp\), the kernel of the evaluation surjection
\[
 V\otimes\mathcal O_{\mathbb P^1}\longrightarrow S^*\cong\mathcal O_{\mathbb P^1}(2).
\]
This is the standard evaluation map by the three independent quadratic forms on \(\mathbb P^1\), whose syzygy bundle is \(K\cong\mathcal O(-1)^{\oplus2}\). Put
\[
 E_i=K\oplus\bigoplus_{j\ne i}S
 \cong\mathcal O(-1)^{\oplus2}\oplus\mathcal O(-2)^{\oplus(h-1)}.
\]
The inclusions \(E_i\hookrightarrow V^{\oplus h}\otimes\mathcal O_Q\) define a morphism \(\pi_i:\mathbb P_Q(E_i)\to\mathbb P(V^{\oplus h})\), with \(\mathbb P(E_i)\) parametrizing lines in the fibers. Its image is exactly \(W_i\). If a column other than \(i\) is nonzero, the line \(\ell\) is uniquely recovered. If only column \(i\) survives, its perpendicular plane meets the conic \(Q\) in a finite subscheme of length two. Thus every fiber is finite; properness gives finiteness. The map is generically one-to-one and its smooth projective source is normal; consequently it is the normalization of \(W_i\).

The hyperplane line bundle pulls back to \(\mathcal O_{\mathbb P(E_i)}(1)\). Since \(\operatorname{rank}E_i=h+1\), \(\dim W_i=h+1\). The projective-bundle formula on the one-dimensional base gives
\[
 \deg W_i=\int_{\mathbb P(E_i)}c_1(\mathcal O(1))^{h+1}
 =-\int_Q c_1(E_i)=1+1+2(h-1)=2h.
\]
The complete tautological series has \(h^0(E_i^*)=4+3(h-1)=3h+1\) sections; the coordinate embedding uses \(3h\) sections, so it is a codimension-one subsystem.

**3. Triple-supported components.** The three nonzero columns on \(J\) satisfy exactly three independent off-diagonal quadratic equations inside a \(9\)-dimensional vector space. The anisotropic orthogonal-basis locus is a smooth dense open of affine dimension \(6\). For three-column frames, the locus of fewer than two anisotropic columns has affine dimension at most \(5\), using the conic-incidence description of step 2 with three labels; the exactly-two-anisotropic locus also lies in the triple-open closure by adding a small orthogonal third column. Any irreducible component cut out by three quadrics in affine \(9\)-space has dimension at least \(6\). Hence the six-dimensional anisotropic-three locus is dense in the entire three-column zero scheme, which is an irreducible codimension-three complete intersection of three quadrics in \(\mathbb P^8\). Its degree is \(2^3=8\) and projective dimension \(5\). Embedding that coordinate \(\mathbb P^8\) into \(\mathbb P^{3h-1}\) does not change the degree.

**4. Generic multiplicity and totals.** Use the split pairing
\[
 B((a,b,c),(a',b',c'))=ab'+ba'+cc'.
\]
For \(A_J\), at columns \((1,1,0),(1,-1,0),(0,0,1)\) in positions \(J\) and zero elsewhere, the Jacobian of all \(\binom h2\) Gram quadrics has rank \(3h-6\). The ambient tangent space therefore has dimension \(6\), exactly the affine component dimension. For \(W_i\), take \(v_i=(0,0,1)\) and \(v_j=(1,0,0)\) for every \(j\ne i\). For \(h\ge4\), the pair equations among \(j\ne i\) force the \(h-1\) distinct \(b_j\)-perturbations to vanish, while the equations involving \(i\) independently impose \(h-1\) further linear conditions. The Jacobian rank is exactly \(2(h-1)\), leaving affine tangent dimension \(h+2\), again the dimension of \(W_i\)'s cone. Each is therefore a smooth point on the Gram zero scheme, proving generic multiplicity one.

There are \(\binom h3\) components of degree \(8\) and \(h\) of degree \(2h\). For \(h=4\), both families have dimension \(5\), giving total degree \(4\cdot8+4\cdot8=64\), which independently matches the degree of the reduced complete intersection of six Gram quadrics. For \(h\ge5\), only the \(W_i\) have maximal dimension, so their reduced fundamental-cycle degree is \(h\cdot2h=2h^2\). This proves all claims.

## Verification
Run the standalone `check_degree_profile.py` with Python 3 and SymPy: it checks the Gram identities and exact Jacobian ranks for \(4\le h\le12\), for every distinguished index \(i\) and for two separated choices of \(J\), together with the Chern-degree identities and the \(h=4\) complete-intersection degree. In the present package this returned `VERIFY_OK`. These finite checks do **not** establish exhaustive results for arbitrarily large \(h\); those follow from the geometric arguments above.

## Relationship to prior work
Casabella–Sammartano, arXiv:2512.25058, Theorem 5.8, already classifies components of arbitrary orthogonal-frame varieties; Corollary 7.4 establishes generic reducedness and Theorem 7.5 the complete-intersection case. Those results are not being claimed here. Xie, arXiv:2610.02585, studies FRS and log-canonical thresholds for the same off-diagonal Gram maps, including reducible fibers. The present addition is the exact projective **degree profile for every \(h\ge4\) in quadratic dimension three**, and the explicit finite-birational scroll normalization of each isotropic component. The cited source material inspected did not give these formulas; implicit earlier expressions remain a priority risk.

## Limitations
This concerns ordered frames in a complex three-dimensional quadratic space, the ordinary projective embedding, reduced component cycles, and generic multiplicity of the equation scheme. It does not assert that the complete Gram ideal is radical for every \(h\), nor calculate arbitrary higher-dimensional ambient quadratic spaces, global singular loci, normality of \(W_i\), or Hilbert polynomials of the nonreduced Gram scheme. An independent historical-priority assessment has not been performed.

## References
1. Ying Xie, *Sharp FRS and singularity thresholds for off-diagonal Gram maps*, arXiv:2610.02585v1, originally submitted 2026-10-01, especially Introduction and Theorem 1.1.
2. Laura Casabella and Alessio Sammartano, *The variety of orthogonal frames*, arXiv:2512.25058v1, originally submitted 2025-12-31, especially Sections 3, 5, and 7 and Theorems 5.8 and 7.5.
