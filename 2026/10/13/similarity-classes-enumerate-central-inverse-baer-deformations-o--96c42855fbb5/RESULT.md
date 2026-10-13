# Similarity classes enumerate central inverse-Baer deformations of an extraspecial Heisenberg brace
## Finding
Let \(p\) be an odd prime, \(d\ge2\), and let \((V,\omega)\) be a \(2d\)-dimensional symplectic space over \(\mathbb F_p\). On \(E=V\times\mathbb F_p\) fix the Heisenberg product
\[
(v,s)\circ(w,t)=(v+w,s+t+\omega(v,w)).
\]
For every alternating \(\mathbb F_p\)-bilinear form \(\beta\) define
\[
(v,s)+_\beta(w,t)=(v+w,s+t+\beta(v,w)),\qquad X_\beta=(E,+_\beta,\circ).
\]
**Theorem.** Each \(X_\beta\) is a two-sided (bi-)skew brace, and its Baer transform is the same left brace \(B=(E,+_0,\circ)\). The isomorphism classes of the entire displayed central-bilinear family \(\{X_\beta\}\) correspond bijectively to ordinary similarity classes of \(d\times d\) matrices \(T\) over \(\mathbb F_p\). Specifically, if \(A_\beta\) is determined by \(\beta(v,w)=\omega(A_\beta v,w)\), then \(A_\beta\) has a symplectic normal form \(\operatorname{diag}(T,T^{\mathsf T})\), and \(T\)'s ordinary similarity class is the complete invariant.

Writing \(k_d(p)\) for the number of such brace classes, and \(k_d^\times(p)\) for those with **both** additive and multiplicative groups extraspecial of exponent \(p\),
\[
\sum_{d\ge0}k_d(p)u^d=\prod_{j\ge1}(1-pu^j)^{-1},\qquad
\sum_{d\ge0}k_d^\times(p)u^d=\prod_{j\ge1}\frac{1-u^j}{1-pu^j}.
\]
In particular \(k_2(p)=p^2+p\) and \(k_2^\times(p)=p^2-1\); for \(p=3\), the twelve classes have respectively \(1,3,8\) representatives by alternating-form ranks \(0,2,4\). Each individual brace also has
\[
|\operatorname{Aut}(X_\beta)|=p^{2d}|C_{\operatorname{GSp}(V,\omega)}(A_\beta)|.
\]
The zero coefficient \(d=0\) in the two generating functions is a counting convention, not an extra member of the stated \(d\ge2\) family.

## Assumptions and scope
All vector spaces and bilinear maps are over the **prime** finite field \(\mathbb F_p\); \(p\) is odd. The group \((E,\circ)\) is a fixed extraspecial group of order \(p^{2d+1}\) and exponent \(p\), since its commutator is \((0,2\omega(v,w))\). The only deforming additions considered are precisely the centrally-valued alternating bilinear laws \(+_\beta\) displayed above. The theorem is **not** a classification of every skew brace of order \(p^{2d+1}\), nor of all possible inverse-Baer deformations of \(B\). Ordinary brace isomorphisms must preserve both group laws; no marking of \(V\) or its basis is assumed.

## Proof
**1. All displayed laws are skew braces with one Baer transform.** Bilinearity makes \(+_\beta\) associative, with identity \((0,0)\) and inverse \((v,s)^{-1}_{+_\beta}=(-v,-s)\). Its commutator is \((0,2\beta(v,w))\). The map
\[
\lambda_{(v,s)}(w,t)=(-_\beta(v,s))+_\beta((v,s)\circ(w,t))
=(w,t+(\omega-\beta)(v,w))
\]
is an automorphism of \((E,+_\beta)\): it preserves all \(w\)-coordinates and adds a linear functional to the center. Moreover, \(\lambda_{a\circ b}=\lambda_a\lambda_b\), since the functional depends only on the quotient vector \(v\) and quotient vectors add under \(\circ\). This is the left skew-brace identity. For the right law, direct cancellation gives \((a+_\beta b)\circ c=(a\circ c)+_\beta(-_\beta c)+_\beta(b\circ c)\), so it is also a two-sided skew brace. Interchanging \(+_\beta\) with \(\circ\) gives the same lambda calculation with \(\beta-\omega\), hence the separate bi-skew property. The Baer operation \(a\oplus b=a+_\beta b+_\beta\tfrac12[b,a]_{+_\beta}\) cancels the central term \(\beta(v,w)\), giving exactly \(+_0\) while leaving \(\circ\) fixed.

**2. Brace isomorphisms are simultaneous symplectic similitudes.** Any automorphism of \((E,\circ)\) preserves its center \(\{0\}\times\mathbb F_p\). Its induced action on \(V\) is an invertible linear map \(P\); its action on the center is multiplication by some \(\tau\in\mathbb F_p^\times\). Commutator preservation gives \(\omega(Pv,Pw)=\tau\omega(v,w)\), so \(P\in\operatorname{GSp}(V,\omega)\). Each such automorphism has the form \((v,s)\mapsto(Pv,\tau s+\ell(v))\) for arbitrary linear \(\ell:V\to\mathbb F_p\). Indeed, the homomorphism equation makes the defect of \(\ell\) simultaneously symmetric (as a coboundary) and alternating (as the difference of two alternating forms); odd characteristic forces it to vanish. Preservation of \(+_\beta\) in addition to \(\circ\) is equivalent to
\[
\beta'(Pv,Pw)=\tau\beta(v,w).
\]
Because \(\omega\) is nondegenerate, \(A_\beta\) is unique; alternation of \(\beta\) is equivalent to \(\omega(A_\beta v,w)=\omega(v,A_\beta w)\). Substituting \(P\) into the two displayed identities shows \(A_{\beta'}P=PA_\beta\). Conversely, any symplectic \(P\) conjugating these operators yields a brace isomorphism. Thus brace orbits are the symplectic conjugacy classes of \(\omega\)-selfadjoint operators, and the stated automorphism order follows from the \(p^{2d}\) choices of \(\ell\).

**3. Symplectic normal form (including the needed nonstandard lemma).** Regard \(V\) as a module over \(R=\mathbb F_p[t]\), with \(t\) acting as a selfadjoint operator \(A\). For polynomial operators \(f(A),g(A)\), selfadjointness and alternation yield
\[
\omega(f(A)v,g(A)v)=\omega(v,f(A)g(A)v)
=-\omega(f(A)g(A)v,v)=0,
\]
so every cyclic \(R\)-submodule is isotropic. Primary components for distinct irreducible polynomials are mutually orthogonal, by Bézout and selfadjointness. On any nonzero primary component select \(v\) with maximal annihilator \(f^m\) and choose \(w\) for which \(\omega(f(A)^{m-1}v,w)\ne0\); projecting \(w\) to the same primary component preserves this. The \(R\)-modules \(Rv\) and \(Rw\) both have length \(m\), by maximality, and their pairing is perfect: a nonzero ideal of the local principal ring \(R/(f^m)\) contains its socle \((f^{m-1})/(f^m)\), on which the functional \(h\mapsto\omega(h(A)v,w)\) is nonzero. Both cyclic summands are isotropic, hence \(Rv\oplus Rw\) is nondegenerate, \(A\)-stable, and hyperbolic, and its orthogonal complement is also \(A\)-stable. Inducting gives a symplectic basis in which \(A\) acts as \(\operatorname{diag}(T,T^{\mathsf T})\). The elementary divisors of this \(2d\)-operator are exactly **two copies** of those of \(T\), so the ordinary similarity class of \(T\) is uniquely determined. Conversely, if \(T'=Q T Q^{-1}\), the symplectic block transformation \(\operatorname{diag}(Q,(Q^{-1})^{\mathsf T})\) conjugates the two normal forms. Thus there is exactly one symplectic orbit per ordinary similarity class of \(T\), as claimed. This also recovers a classical alternating-Hamiltonian normal form (Waterhouse 2005), which is not claimed as novel on its own.

**4. Count the classes.** Rational canonical form parametrizes similarity classes by a partition for each monic irreducible polynomial \(f\in\mathbb F_p[t]\), with total dimension \(d=\sum_f\deg(f)|\lambda_f|\). The standard polynomial Euler identity
\[
\prod_{f\ \text{monic irreducible}}(1-z^{\deg f})^{-1}=(1-pz)^{-1}
\]
gives \(\prod_{j\ge1}(1-pu^j)^{-1}\) after multiplying over partition sizes \(j\). Since \(A\) has matrix \(\operatorname{diag}(T,T^{\mathsf T})\), the form \(\beta=\omega(A\cdot,\cdot)\) is nondegenerate exactly when \(T\) is invertible. Excluding the zero-eigenvalue polynomial \(f=t\) removes one partition factor \(\prod_{j\ge1}(1-u^j)^{-1}\), yielding the second product. All nondegenerate alternating \(\beta\) give extraspecial additive groups, and conversely a group of the form \((E,+_\beta)\) has one-dimensional center exactly when \(\beta\) is nondegenerate. Expansion through \(u^2\) yields the two specified polynomials.

## Verification
Run the bundled \(`verify.py`\) under Python 3 using only its standard library; successful execution prints \(`VERIFY_OK`\). The code constructs all \(729=3^6\) alternating forms on a four-dimensional \(\mathbb F_3\)-space, generates the symplectic conjugation action from the 40 distinct nontrivial transvections, and performs a complete orbit traversal. It finds twelve orbits of sizes \(1,1,1,72,72,72,80,80,80,90,90,90\) with rank distribution \(0:1,2:3,4:8\). A separate exhaustive check tests the skew-brace lambda identity on all three central alternating additions on \(\mathbb F_3^2\oplus\mathbb F_3\) (27 elements). Finite checks illustrate, but do not establish, the theorem for all odd \(p\) and \(d\); Steps 1–4 supply that proof.

## Relationship to prior work
Ercan, Gül, Güloğlu and Kızmaz introduce the Baer transform and establish its structural properties (2026, arXiv:2607.03081). Damele introduces general inverse Baer deformations and constructs simple braces with nilpotent additive groups (2026, arXiv:2609.24640). These constructions precede and motivate the present **isomorphism-orbit count for a fixed Heisenberg brace's explicitly specified central-bilinear family**; no general inverse-Baer construction is claimed here. Waterhouse (2005) provides the underlying alternating-Hamiltonian symplectic normal-form theorem, so the linear-algebra classification is expressly prior art. Nejabati Zenouz (2018/2019, arXiv:1804.01360) classifies the smaller Heisenberg-order-\(p^3\) skew braces, distinct from the present \(d\ge2\) census. The contribution is the combined brace-isomorphism reduction, its complete family-specific enumeration, and the nonabelian-additive subfamily count, not a new enumeration of similarity classes of matrices in isolation.

## Limitations
The family imposes a **fixed multiplicative Heisenberg law** and central alternating bilinear additive deformations. Other compatible non-bilinear additions and other braces are not counted. The 2026 Damele paper was available by abstract but its full text could not be inspected in this investigation; an earlier equivalent specialization to this precise family remains a historical-overlap risk. Waterhouse's paper was checked by its published abstract and bibliographic information rather than by a complete copy, while a self-contained proof of its required lemma is supplied here. The computational checks use only \(p=3\) and dimensions two and four. No independent audit has been performed.

## References
1. G. Ercan, Ş. Gül, İ. Ş. Güloğlu and M. Y. Kızmaz, *The Baer Transform for Skew Braces*, arXiv:2607.03081v1 (first public 2026-07-03).
2. M. Damele, *Inverse Baer deformations and finite simple skew braces of nilpotent type*, arXiv:2609.24640v1 (first public 2026-09-21).
3. W. C. Waterhouse, *The structure of alternating-Hamiltonian matrices*, Linear Algebra and its Applications 396 (2005), 385–390, doi:10.1016/j.laa.2004.10.003.
4. K. Nejabati Zenouz, *Skew Braces and Hopf-Galois Structures of Heisenberg Type*, arXiv:1804.01360v5; Journal of Algebra (2019).
