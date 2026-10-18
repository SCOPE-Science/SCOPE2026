# Prime-indexed singular strata and discrepancies of type-\(A_n\) Lipman toric varieties

## Finding
For every integer \(n\ge 2\), let \(C_n\) be the symmetric Cartan matrix of type \(A_n\), with diagonal entries \(2\) and adjacent off-diagonal entries \(-1\), and set \(N=n+1\). Over \(\mathbb C\), let
\[
 S_n=C_n\mathbb Z^n\cap\mathbb Z_{\ge0}^n,\qquad X_n=\operatorname{Spec}\mathbb C[S_n].
\]
The semigroup \(S_n\) is the intersection-number realization of the Lipman semigroup of the type-\(A_n\) resolution graph, not the coordinate ring of the original two-dimensional rational double point when \(n>2\).

**Theorem (complete prime-indexed singularity profile).** The variety \(X_n\) is the diagonal cyclic quotient
\[
 X_n\cong\mathbb A^n/\mu_N,\qquad
 \zeta\cdot(u_1,\ldots,u_n)=(\zeta u_1,\zeta^2u_2,\ldots,\zeta^n u_n).
\]
For every prime \(p\mid N\), let \(Z_p\) be the image in \(X_n\) of the coordinate subspace \(\{u_i=0:p\nmid i\}\). Then
\[
 \operatorname{Sing}(X_n)_{\mathrm{red}}=\bigcup_{p\mid N\atop p\text{ prime}}Z_p,
 \qquad \dim Z_p=\frac Np-1.
\]
The \(Z_p\) are precisely the distinct irreducible components. In particular, the number of singular components is \(\omega(N)\), the number of distinct prime divisors; the singularity is isolated exactly when \(N\) is prime, and the singular locus is non-equidimensional exactly when \(N\) has at least two distinct prime factors.

At a general point of \(Z_p\), the formal local analytic germ is a smooth factor of dimension \(N/p-1\) times the transverse cyclic quotient
\[
 \mathbb A^{N-N/p}/\mu_p\quad\text{with character weights}\quad
 \bigl(1^{N/p},2^{N/p},\ldots,(p-1)^{N/p}\bigr).
\]
Here an exponent on a listed character means its multiplicity. The Weil divisor class group and the canonical index satisfy
\[
 \operatorname{Cl}(X_n)\cong\mathbb Z/N\mathbb Z,
 \qquad \operatorname{ind}(K_{X_n})=
 \begin{cases}1&n\text{ even},\\2&n\text{ odd}.\end{cases}
\]
Every \(X_n\) is canonical and \(\mathbb Q\)-factorial, and it is terminal if and only if \(n\ge4\). For the unique torus-fixed closed point \(o\), its minimal log discrepancy (with zero boundary) is exactly
\[
 \boxed{\operatorname{mld}_o(X_n)=\frac n2.}
\]
The last equality concerns discrepancies of divisors with **center exactly \(o\)**; it is not the minimum age over all nonidentity group elements, which also detects divisors centered on positive-dimensional strata.

## Assumptions and scope
All statements use the characteristic-zero field \(\mathbb C\), the full saturated affine semigroup \(S_n\), the affine coarse quotient, and the reduced singular locus. A singular component is an irreducible closed subset of \(X_n\), not a component of the fixed-point scheme in the covering affine space. The local product assertion is formal/completed-local at a general complex point; no global product decomposition is asserted. The numerical invariant \(\operatorname{mld}_o\) is the usual minimal log discrepancy of the pair \((X_n,0)\) at the closed torus-fixed point.

## Proof
**1. Identify the toric semigroup.** Define the surjective homomorphism
\[
 \phi:\mathbb Z^n\longrightarrow\mathbb Z/N\mathbb Z,\qquad
 (a_1,\ldots,a_n)\longmapsto\sum_{i=1}^n i a_i\pmod N.
\]
Every column of \(C_n\) maps to zero: at an interior vertex this is \(2i-(i-1)-(i+1)=0\), and the last column gives \(2n-(n-1)=N\). Thus \(C_n\mathbb Z^n\subseteq\ker\phi\). The tridiagonal determinant recurrence \(D_n=2D_{n-1}-D_{n-2}\), with \(D_0=1,D_1=2\), yields \(\det C_n=N\). Both sublattices therefore have index \(N\) in \(\mathbb Z^n\), proving \(C_n\mathbb Z^n=\ker\phi\). Since a monomial is invariant under the displayed \(\mu_N\)-action precisely when its exponent belongs to \(\ker\phi\), equality of affine coordinate rings gives the claimed quotient presentation. The definition is the intersection-number semigroup described by Şahin and by Kaya–Mete–Şahin.

**2. Singular strata.** An element of \(\mu_N\) of exact order \(d>1\), where \(d\mid N\), fixes exactly the coordinate axes whose indices are divisible by \(d\); its fixed space has dimension \(N/d-1\). Its normal representation has codimension \(N-N/d\ge2\), so there are no pseudoreflections. The completed quotient at a point with stabilizer \(H\) is a finite linear quotient by \(H\); moreover, no nonidentity subgroup element is a pseudoreflection on its nontrivial transverse coordinates. The Chevalley–Shephard–Todd smoothness criterion therefore says that a quotient point is singular precisely when its lift has nontrivial stabilizer. Every nontrivial element has some prime \(p\mid d\); its fixed space lies inside the fixed space of the order-\(p\) subgroup. Taking images gives exactly the asserted union.

Each \(Z_p\) is irreducible because it is the finite image of a linear space. Distinct primes give incomparable fixed-coordinate sets: when \(p\ne q\), coordinate \(u_p\) is allowed in the \(p\)-space but not the \(q\)-space (also when \(p=N\) is prime, there is only one component). Thus no \(Z_p\) is contained in a different one. Finiteness preserves dimension, giving \(\dim Z_p=N/p-1\). Different primes have different dimensions. The isolated and non-equidimensional criteria follow, including the prime case \(Z_N=\{o\}\).

At a generic point of the \(p\)-fixed subspace, every \(u_i\) with \(p\mid i\) and \(1\le i<N\) is nonzero. Since index \(p\) itself occurs, the stabilizer is exactly \(\mu_p\). The \(N/p-1\) coordinates with indices divisible by \(p\) are fixed. Among indices \(1,\ldots,N-1\), each nonzero residue modulo \(p\) occurs exactly \(N/p\) times. Finite-group linearization of the completed local ring gives the transverse model, with the stated multiplicities.

**3. Divisor class and canonical index.** In the dual lattice of characters \(M=\ker\phi\), each standard coordinate valuation is primitive: each row of \(C_n\) contains a \(-1\) (as \(n\ge2\)), so some character in \(M\) has valuation \(\pm1\) on that ray. The toric class-group sequence is therefore
\[
 M\longrightarrow\mathbb Z^n\longrightarrow\operatorname{Cl}(X_n)\longrightarrow0.
\]
Its cokernel is \(\mathbb Z^n/M\cong\mathbb Z/N\mathbb Z\). The toric canonical class is represented by \(-(1,\ldots,1)\), whose image under \(\phi\) is \(-nN/2\pmod N\). This has order one when \(n\) is even, and order two when \(n\) is odd. The positive orthant cone is simplicial, hence \(X_n\) is \(\mathbb Q\)-factorial.

**4. Discrepancies and terminality.** The toric cocharacter lattice is
\[
 L=\mathbb Z^n+\frac1N(1,2,\ldots,n)\mathbb Z.
\]
The primitive rays are the coordinate unit vectors, and the log-discrepancy support function is \(\psi(v)=\sum_i v_i\). For \(1\le a<N\), write \(d=N/\gcd(a,N)\). Among the residues \(ai\pmod N\) for \(1\le i<N\), zero occurs \(N/d-1\) times and each positive multiple of \(N/d\) occurs \(N/d\) times. Consequently the sum of fractional coordinates is
\[
 \sum_{i=1}^{N-1}\left\{\frac{ai}{N}\right\}=\frac{N-N/d}{2}.
\]
This is the minimal discrepancy of a lattice point in the *closed* cone in that congruence class. The group contains no pseudoreflections; the Reid–Tai/toric criterion says canonicity requires these values at least one, and terminality requires them strictly greater than one. For \(N\ge3\) every value is at least one. Equality occurs for \(N=3\) (order three) or \(N=4\) (order two), and not for \(N\ge5\), proving the terminality statement.

For a torus-fixed closed point, the center condition requires every coordinate of the lattice point to be strictly positive, not merely nonnegative. Each of the \(N/d-1\) zero fractional coordinates must therefore be raised to one. The smallest interior sum for a nontrivial class of order \(d\) is
\[
 \frac{N-N/d}{2}+\frac Nd-1=\frac{N+N/d}{2}-1.
\]
It is minimized when \(d=N\), yielding \((N-1)/2=n/2\). The identity class gives interior sum \(n\), which is no smaller. Ambro's interior-lattice-point formula for the minimal log discrepancy at a torus-fixed point now proves the assertion for all \(n\ge2\).

## Verification
The standalone exact-arithmetic file `verify_lipman.py` reconstructs the inverse Cartan matrix, checks its lattice congruence on deterministic examples, enumerates subgroup fixed-coordinate patterns and character multiplicities, and verifies the discrepancy and canonical-index formulas for \(2\le n\le139\). Running `python3 verify_lipman.py` produced `VERIFY_OK 45520`. These finite tests are corroborative; Steps 1–4 give the infinite proof.

For orientation: \(n=2\) gives an isolated \(A_2\) surface quotient of type \(\frac13(1,2)\). For \(n=3\), the singular locus is a line with generic transverse \(\frac12(1,1)\) singularity and the canonical index is two. For \(n=5\), the two singular components have dimensions two and one, arising from \(p=2,3\), and the ambient fivefold is terminal despite this non-equidimensional singular locus.

## Relationship to prior work
Altınok–Tosun (2007, 2008), Şahin (2010), and Kaya–Mete–Şahin (2015) construct the Lipman semigroups and their normal toric invariant rings; Şahin's 2010 paper explicitly gives quotient-singularity structure and the \(A_2\) parametrization. Their inspected material concerns algorithms, Hilbert bases and Gröbner bases, not the all-\(n\) prime-indexed singular components and local transverse character profiles. General cyclic quotient smoothness and discrepancy theory, including Chevalley–Shephard–Todd and Ambro's toric minimal-log-discrepancy formula, supplies essential tools. The contribution here is the identification of the type-\(A_n\) semigroup with the exact *consecutive-weight* cyclic quotient and the consequent simultaneous arithmetic stratification and discrepancy formulas. These explicit formulas are derived specializations of general quotient theory, not a new general singularity criterion.

## Limitations
The result is not a statement about the original two-dimensional Du Val singularity for \(n>2\), nor a classification for \(D_n,E_6,E_7,E_8\), nor a positive-characteristic theorem. It concerns coarse affine quotient singularities and reduced supports, not full Jacobian singular schemes or a global desingularization. The available 2007 weighted-graph paper could not be materially inspected in full; potential uncatalogued overlap in that article or in general cyclic-quotient compilations is a residual originality risk. Published general quotient and toric discrepancy criteria apply in principle, so the novelty of this explicit specialization should be assessed against those broader results by an independent reader.

## References
1. M. Şahin, *Hilbert basis of the Lipman semigroup*, Comptes Rendus Math. 348 (2010), 1311–1314. Early preprint arXiv:1009.0385; full text https://www.numdam.org/item/10.1016/j.crma.2010.11.005.pdf.
2. G. Kaya, P. Mete, M. Şahin, *Toric ideals of simple surface singularities*, Hacettepe J. Math. Stat. 44 (2015), 1057–1069. arXiv:1512.02376; full text https://dergipark.org.tr/en/download/article-file/644728.
3. F. Ambro, *The set of toric minimal log discrepancies*, Central European J. Math. 4 (2006), 358–370; arXiv:math/0508429, especially the interior-cone formula in Section 1.
4. S. Altınok, M. Tosun, *Toric varieties associated with weighted graphs*, Int. Math. Forum 2 (2007), 1779–1793, DOI:10.12988/IMF.2007.07159 (bibliographic/abstract access only).
5. S. Altınok, M. Tosun, *Generators for semigroup of Lipman*, Bull. Braz. Math. Soc. 39 (2008), 123–135, DOI:10.1007/s00574-008-0075-4 (bibliographic/abstract access only).
6. C. Chevalley, *Invariants of finite groups generated by reflections*, Amer. J. Math. 77 (1955), 778–782; G. C. Shephard and J. A. Todd, *Finite unitary reflection groups*, Canad. J. Math. 6 (1954), 274–304 (general smoothness criterion).
