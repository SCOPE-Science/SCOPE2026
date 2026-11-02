# Gcd resonance of motivic local densities on products of monomial curve germs

## Finding
For integers \(a,b\ge2\) and \(A>a,B>b\) with \(\gcd(a,A)=\gcd(b,B)=1\), consider the plane branches
\[C_{a,A}=\{(x,y):y^a=x^A\},\qquad C_{b,B}=\{(u,v):v^b=u^B\}\]
over \(\mathbb C\). Embed their Cartesian product \(X=C_{a,A}\times C_{b,B}\) in \(\mathbb A^4\) using the displayed coordinates. With \(d=\gcd(a,b)\), its embedded motivic local density at the origin is
\[
\boxed{\Theta_2(\underline X,0)=\frac{d}{ab}\frac{\mathbb L-1}{\mathbb L+1}\frac{\mathbb L^d+1}{\mathbb L^d-1}.}
\]
Here \(\mathbb L=[\mathbb A^1_{\mathbb C}]\) and the coefficient is understood in \(\mathbb Q\otimes\mathcal M_{\mathbb C}\). Each factor has density \(\Theta_1(\underline C_{a,A},0)=1/a\) and \(\Theta_1(\underline C_{b,B},0)=1/b\). Thus the embedded local density is multiplicative **precisely when** \(a\) and \(b\) are coprime. Its failure for other pairs is a rational motivic invariant detected by the common divisor.

For two ordinary cusps \(y^2=x^3\), the exact product density and multiplicativity defect are
\[
\Theta_2(\underline C_{2,3}^{\;2},0)=\frac{\mathbb L^2+1}{2(\mathbb L+1)^2},\qquad
\Theta_2-\Theta_1^2=\frac{(\mathbb L-1)^2}{4(\mathbb L+1)^2}.
\]

## Assumptions and scope
Work over the Laurent-series valued field \(\mathbb C((t))\) and use motivic measure in the localized Grothendieck ring
\[\mathcal M_{\mathbb C}=K_0(\mathrm{Var}_{\mathbb C})[\mathbb L^{-1},(1-\mathbb L^{-i})^{-1}:i\ge1].\]
The normalization \(\nu_a:\mathbb A^1\to C_{a,A}\) is \(z\mapsto(z^a,z^A)\); analogously define \(\nu_b\). For integer \(m\ge0\), let \(B_N(0,m)\) be the coordinatewise valuation ball of radius \(m\) in \(\mathbb A^N\). The normalized volume sequence is
\[\theta_{Z,j}(m)=\mu_j(\underline Z\cap B_N(0,m))/\mathbb L^{-jm}.\]
The density \(\Theta_j(\underline Z,0)\) is the mean of the eventual residue-class limits of this sequence, as in Forey and Ratajczak. The product has a positive-dimensional singular locus; therefore the statement concerns this *embedded definable-set* density and does not invoke the intrinsic isolated-singularity invariant from Ratajczak's Proposition 2.11.

## Proof
**1. Monomial branch measure.** Since \(\gcd(a,A)=1\), \(\nu_a\) is finite and birational and induces a bijection on arcs; a nonzero arc \((x(t),y(t))\) has a unique parameter \(z(t)\) in \(\mathbb C[[t]]\). If \(q=\operatorname{ord}_t z\ge0\), then \(\operatorname{ord}x=aq\) and \(\operatorname{ord}y=Aq\), so the ball condition is exactly \(q\ge\lceil m/a\rceil\). The coordinate one-forms pull back to \(az^{a-1}dz\) and \(Az^{A-1}dz\). Since \(A>a\), the minimal order defining the canonical measure is \((a-1)q\). The motivic mass of \(\operatorname{ord}z=q\) is therefore
\[(\mathbb L-1)\mathbb L^{-q-1}\mathbb L^{-(a-1)q}=(1-\mathbb L^{-1})\mathbb L^{-aq}.\]
The zero arc has measure zero. Summing the geometric progression gives the **exact**, not merely asymptotic, ball volume
\[\mu_1(\underline C_{a,A}\cap B_2(0,m))=\frac{1-\mathbb L^{-1}}{1-\mathbb L^{-a}}\mathbb L^{-a\lceil m/a\rceil}.\]
Thus, with \(c_a=(1-\mathbb L^{-1})/(1-\mathbb L^{-a})\),
\[\theta_a(m)=c_a\mathbb L^{m-a\lceil m/a\rceil}.\]
It has period \(a\); explicitly \(\theta_a(0)=c_a\) and \(\theta_a(r)=c_a\mathbb L^{r-a}\) for \(1\le r<a\). Summation over the period yields \(a^{-1}\sum_{r=0}^{a-1}\theta_a(r)=1/a\), in agreement with the known branch-multiplicity density.

**2. Product canonical measure.** The map \(\nu_a\times\nu_b:\mathbb A^2\to X\) is finite birational. Its four coordinate differentials have a block-diagonal Jacobian: every nonzero two-by-two minor is the product of one derivative from each block. At nonnegative parameter valuations \((q_1,q_2)\), the smallest possible order of such a minor is
\[(a-1)q_1+(b-1)q_2.\]
The pullback of the canonical two-dimensional measure therefore factors into the two canonical one-dimensional measures. The product ball is the Cartesian product of the factor balls, and Fubini gives at **each** radius
\[\theta_{X,2}(m)=\theta_a(m)\theta_b(m).\]
Averaging is performed only after this multiplication, not separately.

**3. Conditional period averaging.** Let \(d=\gcd(a,b)\) and \(\ell=\operatorname{lcm}(a,b)\). For each residue \(s\pmod d\), the Chinese remainder theorem gives independent, uniform residues modulo \(a\) and modulo \(b\) among the \(\ell/d\) indices in that class. For a divisor \(d\mid a\), the geometric formula from Step 1 gives
\[\sum_{\substack{0\le r<a\\r\equiv s\ (\mathrm{mod}\ d)}}\theta_a(r)=\theta_d(s),\]
where \(\theta_d\) is the same periodic expression with exponent \(d\). Hence the conditional average in this residue class is \(\frac da\theta_d(s)\). Consequently
\[\Theta_2(\underline X,0)=\frac{d}{ab}\sum_{s=0}^{d-1}\theta_d(s)^2.\]
Using \(c_d=(1-\mathbb L^{-1})/(1-\mathbb L^{-d})\), the finite geometric sum is
\[\sum_{s=0}^{d-1}\theta_d(s)^2=c_d^2\sum_{j=0}^{d-1}\mathbb L^{-2j}
=\frac{\mathbb L-1}{\mathbb L+1}\frac{\mathbb L^d+1}{\mathbb L^d-1},\]
which proves the boxed expression.

**4. Exact multiplicativity criterion.** When \(d=1\), the two rational factors cancel, yielding \(1/(ab)\). When \(d\ge2\), the ratio between the product density and \(1/(ab)\) is the rational function
\[d\frac{\mathbb L-1}{\mathbb L+1}\frac{\mathbb L^d+1}{\mathbb L^d-1}.\]
Its rational-function limit as \(\mathbb L\to\infty\) is \(d>1\), hence it is not the constant \(1\). The distinction is genuine in the Grothendieck-ring localization: apply the Hodge–Deligne realization and send \(\mathbb L\) to the indeterminate \(uv\). Thus equality with \(1/(ab)\) fails for \(d>1\).

## Verification
The standalone file `verify_density.py` checks exact rational normalized-volume sums against the claimed closed formula for \(2\le a,b\le14\) and the independent specializations \(\mathbb L=2,3,5,11\): 676 paired tests. It also checks the single-branch period mean for each exponent and verifies the two-cusp defect algebraically through exact rational evaluation. These finite checks corroborate the residue algebra but do not prove the infinite statement; the preceding change-of-variables and CRT argument does.

## Relationship to prior work
Forey, *Motivic local density* (arXiv:1512.00420), introduces the residue-class mean and already computes the single cusp density \(1/2\); the single-factor result here is **not claimed as new**. Ratajczak, *Motivic local density of isolated singularities of algebraic varieties* (arXiv:2610.32416v1, first posted 2026-10-23), recalls the canonical measure, proper-birational change-of-variables and the normalized-volume zeta/residue formula. Its main resolution formula applies to isolated singularities, while the present product has nonisolated singularities. Neither inspected primary text states the synchronised two-factor density, gcd classification or nonmultiplicativity example. The new input is the explicit common-radius correlation of periodic motivic volumes, not an objection to Fubini at fixed radius.

## Limitations
The formula assumes characteristic zero, irreducible monomial branches, positive exponents satisfying the stated coprimality, and the specified product embedding with coordinatewise valuation balls. A general product law for arbitrary singular germs, invariance under embeddings at nonisolated points, extension to mixed characteristic, and an independent priority audit are **not** established. Literature searches can miss older equivalent descriptions of periodic motivic volumes; originality is conditional on available comparisons. The specialization \(\mathbb L\to1\) of the rational expression is \(1/(ab)\); this analytic limit is **not** asserted to define a specialization homomorphism on the entire localized Grothendieck ring.

## References
1. S. Ratajczak, *Motivic local density of isolated singularities of algebraic varieties*, arXiv:2610.32416v1 (2026-10-23), https://arxiv.org/html/2610.32416v1 . Relevant: Definitions 2.3–2.8, Theorem 2.5, Propositions 2.10–2.11, Theorem 3.2.
2. A. Forey, *Motivic local density*, arXiv:1512.00420v2, https://arxiv.org/pdf/1512.00420 . Relevant: Introduction pp. 1–3, §3, Example 3.22, and canonical density construction.
