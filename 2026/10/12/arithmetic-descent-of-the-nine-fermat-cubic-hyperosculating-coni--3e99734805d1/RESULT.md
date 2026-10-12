# Arithmetic descent of the nine Fermat-cubic hyperosculating-conic triples

## Finding
Let \(F=x^3+y^3+z^3\) and choose a primitive cube root of unity \(\omega\). For each unordered coordinate pair \(\{u,v\}\subset\{x,y,z\}\), write \(w\) for the remaining coordinate, and for \(j=0,1,2\) put
\[
 H_{uv,j}=(u-\omega^jv)^6-16w^3 F,\qquad D_{uv,j}=V(FH_{uv,j})\subset\mathbb P^2.
\]
The nine \(D_{uv,j}\) are exactly the nine degree-nine curves obtained by adjoining all three conics of one of the canonical three-conic blocks of the \(27\) hyperosculating conics of the Fermat cubic. Among these nine *embedded, Fermat-anchored curves*, exactly three \(D_{uv,0}\) have defining field \(\mathbb Q\); the other six have minimal defining field \(\mathbb Q(\omega)\). Each \(H_{uv,0}\) is irreducible over \(\mathbb Q\) but geometrically the union of three distinct smooth conics. The complete set of \(27\) hyperosculating conics has minimal common splitting field \(\mathbb Q(\alpha,\omega)\), where \(\alpha^3=2\), with Galois group \(S_3\); the orbit decomposition is \(3+3+3+6+6+6\). The nine three-conic blocks have orbits \(1+1+1+2+2+2\). Each \(D_{uv,j}\) is free with exponents \((3,5)\); this freeness is the previously published Theorem 4.10 of Dimca--Ilardi--Malara--Pokora, not an original assertion here.

## Assumptions and scope
The ground field is \(\mathbb Q\), its algebraic closure has characteristic zero, \(\omega^2+\omega+1=0\), and \(\alpha\) is any fixed root of \(T^3-2\). All fields of definition concern fixed embedded plane curves/components in the given \(\mathbb P^2\) with Fermat equation, *not* abstract isomorphism classes of curves up to arbitrary projective changes. The cited paper partitions the \(27\) conics into nine distinguished blocks of three, characterized by pairwise tangency at an off-cubic point. Only these nine blocks are classified; no assertion is made that every free triple is one of them.

## Proof
**Exact block equation.** Dimca--Ilardi--Malara--Pokora, Example 4.4, writes the hyperosculating conic at \((1:1:-\alpha)\) as
\[
 q_{\alpha}(x,y,z)=(x-y)^2-z\bigl(\alpha^2(x+y)+2\alpha z\bigr).
\]
The source's Proposition 4.7 identifies the three conics of this block as the three conjugates obtained by replacing \(\alpha\) with the roots \(\alpha_r=\alpha\omega^r\), \(r=0,1,2\). Eliminating \(T\) yields the exact polynomial identity
\[
 \operatorname{Res}_T\bigl(T^3-2,(x-y)^2-T^2z(x+y)-2Tz^2\bigr)
 =(x-y)^6-16z^3(x^3+y^3+z^3).
\]
This is independently verified by an exact symbolic resultant in `verify.py`. Because \((\omega^j v)^3=v^3\), substituting \(v\mapsto\omega^j v\) and permuting coordinates proves the nine displayed \(H_{uv,j}\) formulas. Distinct blocks are distinguished by the common tangency point on \(w=0\), namely \((u:v:w)=(\omega^j:1:0)\) after choosing the ordered presentation; their geometric existence and partition are prior results.

**Defining fields and irreducibility.** In normalized \(H_{uv,j}\) the coefficient of \(u^5v\) is \(-6\omega^j\); the other term is divisible by \(w^3\). Hence this coefficient alone recovers \(\omega^j\) from the projective equation, proving that the minimal coefficient field is \(\mathbb Q\) for \(j=0\) and \(\mathbb Q(\omega)\) otherwise. It also shows the three blocks with a fixed coordinate pair are pairwise distinct.

The conic \(q_{\alpha_r}\), normalized by its \(u^2\) coefficient, has \(w^2\) coefficient \(-2\alpha_r\). Thus its minimal defining field is \(\mathbb Q(\alpha_r)\). In a block indexed by \(j\ne0\), the \(uv\) coefficient additionally recovers \(\omega^j\), so an individual conic's minimal field is \(\mathbb Q(\alpha_r,\omega)=K\). The polynomial \(T^3-2\) is Eisenstein at two, and adjoining \(\omega\) produces its splitting field \(K\) of degree six with group \(S_3\). Its order-three subgroup acts transitively on the three conic factors in each block. Since those are geometrically irreducible and distinct (smoothness follows from the nonzero quadratic-form determinant), their product \(H_{uv,j}\) is irreducible over its minimal base field \(\mathbb Q(\omega^j)\); in particular the three rational \(H_{uv,0}\) are \(\mathbb Q\)-irreducible. This does not claim geometric irreducibility.

**Galois orbit census.** Use labels \((\{u,v\},j,r)\) for the conic equation
\[
 q_{j,r}=(u-\omega^jv)^2-w\bigl((\alpha\omega^r)^2(u+\omega^jv)+2\alpha\omega^r w\bigr).
\]
For each of three coordinate pairs there are three \(j\)-values and three \(r\)-values, totaling \(27\). The automorphisms \(\sigma(\alpha)=\alpha\omega,\sigma(\omega)=\omega\) and \(\tau(\alpha)=\alpha,\tau(\omega)=\omega^2\) induce label permutations \(\sigma:(j,r)\mapsto(j,r+1)\) and \(\tau:(j,r)\mapsto(-j,-r)\), modulo three. Thus for every coordinate pair the \(j=0\) conics form one three-element orbit, and the six conics with \(j=1,2\) form one six-element orbit. The nine three-conic blocks have one fixed block at \(j=0\) and one conjugate pair at \(j=1,2\) for each coordinate pair. The \(j\ne0\) conics already require both \(\omega\) and a cubic root of two, proving the *minimality* of the total splitting field. These field statements are not consequences of the source's geometric freeness theorem alone.

**Freeness.** Theorem 4.10 of the cited source proves that adjoining all three conics of any one block to \(F\) yields a free curve with exponents \((3,5)\). As an independent consistency check for \(D_{xy,0}\), the coefficient matrices of polynomial Jacobian syzygies in degrees one, two, and three have ranks \(9,18,29\) in \(9,18,30\) columns, respectively; consequently its minimal Jacobian relation degree is three. The source's complete local singularity calculation gives total Tjurina number \(49\). The standard degree-nine freeness criterion \(3^2-3(9-1)+(9-1)^2=49\) agrees. Projective symmetries of the Fermat cubic carry this calculation to the other blocks.

## Verification
Run `python verify.py` with Python 3 and SymPy. This exact program reconstructs the displayed polynomial resultant and the complete degree-one, degree-two, and degree-three Jacobian matrices over the integers for \(F H_{xy,0}\), then checks ranks \(9,18,29\). Both checks succeeded on the included standalone file. The Galois permutations, minimal coefficient-field recovery, and irreducibility argument are algebraic deductions explicitly reconstructed above; finite matrix checks do not by themselves certify a universal Galois statement. No external independence review has been performed.

## Relationship to prior work
Dimca--Ilardi--Malara--Pokora (arXiv:2311.08913), Examples 4.4 and Propositions 4.3, 4.7 and Theorem 4.10, supply the conic seed, its full group orbit, the partition into nine triples, and freeness of each associated degree-nine curve. The present contribution is the exact descent of **all** blocks and conics, the nine closed sextic equations and their rational irreducibility, and the complete \(S_3\)-Galois permutation profiles. Szemberg--Szpond (arXiv:2211.00494) supplies the earlier Fermat-cubic sextactic-point geometry and includes an integer-defined product of 81 different lines; that result does not determine the field or irreducibility of the nine hyperosculating-conic sextics. Moe--Toft (arXiv:2412.16993), in a later generalized study of Fermat curves, provides formulas and intersection geometry of hyperosculating conics; its examined relevant sections do not state the arithmetic descent classification. General forms can be algorithmically derived from the published formulas, so a possible implicit or unindexed prior calculation remains a bibliographic risk.

## Limitations
The novelty claim is limited to the arithmetic descent and complete Galois census of the specified embedded configurations, not the published hyperosculation, block partition, freeness or line-configuration results. The existence and freeness of these particular configurations rely on the cited primary theorems; the embedded verifier independently checks the central polynomial identity and one minimal-syzygy degree but does not redo every local singularity computation. No assertion concerns all possible free triples of 27 conics, positive characteristic, fields of abstract projective isomorphism, or independent certification. A related rational expression might be recoverable from existing unpublished or unindexed computational tables.

## References
1. A. Dimca, G. Ilardi, G. Malara, P. Pokora, *Construction of free curves by adding osculating conics to a given cubic curve*, arXiv:2311.08913, first posted 2023-11-15; especially Example 4.4, Proposition 4.7 and Theorem 4.10.
2. T. Szemberg, J. Szpond, *Sextactic points on the Fermat cubic curve and arrangements of conics*, arXiv:2211.00494 (2022), Sections 3--4.
3. T. K. Moe, N. P. A. Toft, *The Fermat curves, arrangements of lines, and intersections of osculating curves*, arXiv:2412.16993 (first public 2024-12-22), Sections 2.2 and 4.3.
4. A. Dimca, *Freeness versus maximal global Tjurina number for plane curves*, Math. Proc. Cambridge Philos. Soc. 163 (2017), for the freeness criterion as quoted by reference 1.