# The complete singular scheme of the elementary symmetric cubic in characteristic two

## Finding
Let \(K\) be an algebraically closed field of characteristic \(2\), and let \(n\geq5\) with \(n\not\equiv2\pmod4\). In \(\mathbf P_K^{n-1}\), let \(X_n=V(e_3)\), where
\[
e_3=\sum_{1\leq i<j<k\leq n}x_ix_jx_k.
\]
Write \(\Sigma_n\) for the projective singular subscheme of \(X_n\) defined by its homogeneous partial derivatives. For a nonempty subset \(S\subseteq\{1,\ldots,n\}\), put \(p_S=[\mathbf{1}_{i\in S}]\). Then:

1. The geometric support of \(\Sigma_n\) is **exactly** the set of \(p_S\) with \(|S|\equiv1\pmod4\). Its cardinality is
\[
N_n=\sum_{\substack{1\leq j\leq n\\j\equiv1\ (\mathrm{mod}\ 4)}}\binom{n}{j}.
\]
2. When \(n\) is odd, \(\Sigma_n\) is reduced: it consists of exactly \(N_n\) distinct reduced points.
3. When \(4\mid n\), \(\Sigma_n\) is a zero-dimensional complete intersection of \(n-1\) quadrics. There are \(N_n=2^{n-2}\) support points, the local ring at each is \(K[\varepsilon]/(\varepsilon^2)\), and the scheme has total length \(2^{n-1}\).
4. In both cases, every point of \(\Sigma_n\) is an **ordinary quadratic singularity** of the cubic hypersurface: its projectivized quadratic tangent cone is smooth over \(K\). In particular, the doubled Jacobian points for \(4\mid n\) are compatible with an ordinary quadratic tangent cone in characteristic \(2\).

For illustration, the reduced point counts at \(n=5,7,9\) are \(6,28,136\), while at \(n=8\) there are \(64\) double points of total Jacobian length \(128\).

## Assumptions and scope
Here \(e_3\) is the third elementary symmetric polynomial in independent projective coordinates, not a specialization or generic symmetric cubic. The singular subscheme is \(\operatorname{Proj} K[x_1,\ldots,x_n]/J\), where \(J=(f_1,\ldots,f_n)\) and \(f_i=\partial e_3/\partial x_i\). Since Euler's identity gives \(e_3=\sum_i x_if_i\) in characteristic \(2\), this is the hypersurface singular subscheme without an extra equation. The theorem covers **all** algebraically closed fields of characteristic \(2\), every integer \(n\ge5\) except \(n\equiv2\pmod4\), and the entire geometric projective singular scheme, not merely its coordinate strata.

## Proof
**Step 1: the critical equations and support.** Set \(s_1=\sum_ix_i\) and \(s_2=\sum_{i<j}x_ix_j\). Direct deletion of coordinate \(x_i\) gives
\[
f_i=x_i^2+s_1x_i+s_2.
\]
Hence every critical coordinate is a root of the same monic quadratic \(T^2+s_1T+s_2\); there are at most two distinct coordinate values.

Suppose first the coordinate values are \(u\ne0\) and \(0\), with \(r\) occurrences of \(u\). At a zero coordinate the equation is \(\binom r2u^2=0\), while at a nonzero coordinate it is \(\binom{r-1}2u^2=0\). When no zero coordinate occurs only the latter condition applies. For integers \(r\ge1\), the simultaneous conditions in the two-value case, and the single condition when \(r=n\), require and suffice for \(r\equiv1\pmod4\) (in the all-nonzero case \(r=n\), the condition \(\binom{n-1}2=0\) also holds for \(n\equiv2\pmod4\), which is excluded by hypothesis). Thus every such projective critical point is \(p_S\) with \(|S|\equiv1\pmod4\), and conversely all these points are critical.

It remains to exclude two distinct *nonzero* values \(u\) and \(v\), with respective multiplicities \(a,b\ge1\) and \(a+b=n\). Their common root polynomial forces \(s_1=u+v\). Comparing this with \(s_1=au+bv\) in characteristic \(2\) shows that \(a,b\) are both odd: the other three parity choices force \(u=0\), \(v=0\), or \(u=v\). Since \(ab\) is odd, comparing the constant term with \(s_2=\binom a2u^2+\binom b2v^2+abuv\) gives
\[
\binom a2u^2+\binom b2v^2=0.
\]
For odd integers, \(\binom a2\) is \(0\) modulo \(2\) when \(a\equiv1\pmod4\) and \(1\) when \(a\equiv3\pmod4\). Mixed residues force one value to vanish, the pair \((3,3)\) forces \(u=v\), and the sole remaining pair \((1,1)\) implies \(n\equiv2\pmod4\), excluded. This proves the asserted support (the all-nonzero single-value case already matches the support criterion under the standing hypothesis).

**Step 2: quadratic tangent cones.** Fix a support point \(p_S\), write \(r=|S|\equiv1\pmod4\), and use the affine chart \(x_k=1\) for any \(k\in S\). Put \(x_i=1+y_i\) for \(i\in S\setminus\{k\}\) and \(x_i=z_i\) for \(i\notin S\). All constant and linear terms vanish. For distinct coordinates \(i,j\), the coefficient of their product in the degree-two Taylor term is the sum of the remaining base coordinates. Consequently the quadratic initial form is
\[
Q=e_2(y_1,\ldots,y_{r-1})+e_2(z_1,\ldots,z_{n-r}).
\]
Here the two block sizes are \(A=r-1\equiv0\pmod4\) and \(B=n-r\). The polar matrix of \(e_2\) in a block of size \(m\) is the matrix with zero diagonal and ones off the diagonal. If \(m\) is even its radical is zero; if \(m\) is odd its radical is spanned by the all-ones vector. The zero-dimensional block contributes nothing.

If \(n\) is odd, then \(A,B\) are even and the full polar matrix is nonsingular. If \(4\mid n\), then \(A\) is even and \(B\equiv3\pmod4\) is odd. Its one-dimensional polar radical is generated by the all-ones vector supported on the \(B\)-block, and
\[
Q(\mathbf1_B)=\binom B2=1\quad\text{in }K.
\]
Thus even in this case no nonzero vector lies simultaneously in the polar radical and the null quadric. Therefore the projectivized tangent quadric \(V(Q)\subset\mathbf P^{n-2}\) is smooth in **both** cases. This verifies the ordinary quadratic singularity claim without erroneously requiring a nonsingular polar form in odd vector dimension in characteristic \(2\).

**Step 3: the reduced odd case.** If \(n\) is odd, the polar matrix of \(Q\) has full rank \(n-1\). Consequently the differentials of the local partial-derivative equations span the entire cotangent space at each support point. The Jacobian scheme is smooth of dimension zero there, hence reduced. Step 1 exhausts the support, so \(\Sigma_n\) consists precisely of the stated distinct reduced points.

**Step 4: the doubled even case.** Assume \(4\mid n\). Each monomial of \(e_3\) occurs \(n-2\) times in \(\sum_i f_i\) after deleting a variable, so \(\sum_i f_i=(n-2)e_2=0\) in characteristic \(2\). Hence the homogeneous ideal \(J\) is generated by \(n-1\) quadrics. Step 1 proves that its affine cone is a finite union of lines, hence has dimension \(1\). Its height in the regular ring \(K[x_1,\ldots,x_n]\) is \(n-1\). Therefore these \(n-1\) generators form a regular sequence; its projective zero scheme is a zero-dimensional complete intersection of degree \(2^{n-1}\).

The standard fourth-roots-of-unity filter on \((1+t)^n\), or equivalently the two-bit binomial recurrence, gives
\[
\sum_{j\equiv1\ (\mathrm{mod}\ 4)}\binom{n}{j}=2^{n-2}\qquad(4\mid n).
\]
At each of these support points, the polar matrix in Step 2 has corank \(1\). Thus the Zariski tangent space to the local Jacobian scheme has dimension \(1\), and its Artin length is at least \(2\). The sum of these lower bounds is \(2\cdot2^{n-2}=2^{n-1}\), already the complete-intersection length. Every local length is therefore **exactly** \(2\). Over the algebraically closed field \(K\), every length-two local Artin algebra with residue field \(K\) is \(K[\varepsilon]/(\varepsilon^2)\). This proves the full scheme-theoretic assertion.

## Verification
The standalone file `verify.py` exhaustively enumerates normalized \(\mathbf F_4\)-projective vectors for \(n=5,6,7,8,9\), evaluates the exact quadratic critical equations, and checks the predicted support in the theorem's three admissible sample dimensions and the additional odd examples. For admissible sizes it also verifies polar-matrix ranks and tests every nonzero \(\mathbf F_2\)-vector against the singularity condition for the quadratic initial form. Separately, an exact binomial calculation checks the complete-intersection degree and doubled support count for \(n=8,12,16,20\). The deterministic output is `verification_output.txt`, ending `VERIFY_OK`. These **finite checks are corroborating evidence**, not proofs of the infinite family or of the local-algebra classification; the proof is given above.

## Relationship to prior work
Ying Xie's `arXiv:2610.00259v1` proves uniform dimension formulas for elementary-symmetric derivative and multiplicity schemes, classifies components attaining the larger dimensions, and computes local rings along **coordinate components**. Its Section 7 expressly leaves smaller-dimensional/embedded-component classification, primary decomposition and global reducedness open. The present theorem is confined to the third elementary symmetric polynomial in characteristic two and supplies complete projective support, multiplicities, a complete-intersection criterion and transverse quadratic types in that family.

Orzel's `arXiv:2509.05009v3` establishes dimension bounds and a proposed characteristic-dependent criterion for these derivative loci, rather than this support and local-scheme classification. Cafure--Matera--Privitelli's `arXiv:1109.2265` develops partition-space arguments for general symmetric hypersurfaces; their dimension framework does not by itself determine the stated projective local rings. The four-variable case is outside the stated domain \(n\ge5\); no classification or novelty assertion for that case is made here.

## Limitations
The congruence class \(n\equiv2\pmod4\) is excluded: its derivative locus has positive-dimensional two-value strata, so the finite-support and complete-intersection conclusions do not extend to it. The theorem gives local *Jacobian* rings, not full analytic normal forms of the hypersurface germs, and does not classify resolutions, moduli, or arithmetic point counts. Smoothness of quadratic tangent cones is proved directly and is not inferred from the computational samples. The originality comparison cannot rule out an older equivalent statement under alternative symmetric-hypersurface terminology; no independent audit has been carried out.

## References
1. Ying Xie, *Derivative and multiplicity loci of elementary symmetric polynomials in positive characteristic*, arXiv:2610.00259v1 (first publicly available September 24, 2026), especially Theorems 1.1, 1.3, 1.4, and Section 7. https://arxiv.org/html/2610.00259v1
2. Ian Orzel, *Computing the Elementary Symmetric Polynomials in Positive Characteristics*, arXiv:2509.05009v3, Section 2. https://arxiv.org/html/2509.05009v3
3. A. Cafure, G. Matera, M. Privitelli, *Singularities of symmetric hypersurfaces and an application to Reed–Solomon codes*, arXiv:1109.2265 (2011), for the general partition-space framework. https://arxiv.org/abs/1109.2265
