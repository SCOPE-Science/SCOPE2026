# Two independent mod-two transcendental specialization obstructions in an elliptic-surface degeneration

## Finding

In the elliptic-surface degeneration of Arapura, Greer and Zhang associated with their component \(Y_2\), the induced integral specialization between rank-two transcendental lattices has cokernel
\[
\operatorname{coker}\!\left(T_{S_{2,0}}\xrightarrow{\,sp_2^2\,}T_{S_t}\right)
\cong (\mathbb Z/2\mathbb Z)^2.
\]
More precisely, with \(A_2\) the positive-definite root lattice having Gram matrix
\[
G=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},
\]
there are isometries identifying the three lattices and the specialization image as
\[
T_{Y_2}\cong T_{S_{2,0}}\cong A_2(4),\qquad
T_{S_t}\cong A_2,\qquad
\operatorname{im}(sp_2^2)=2A_2\subset A_2.
\]
Here \(A_2(4)\) means the same underlying free group with its bilinear form multiplied by \(4\), and \(2A_2\) means the subgroup consisting of twice all vectors of \(A_2\). A complementary integral invariant is the discriminant group
\[
T_{Y_2}^{\vee}/T_{Y_2}\cong\mathbb Z/4\mathbb Z\oplus\mathbb Z/12\mathbb Z.
\]
The group structure of the specialization obstruction refines its previously known order \(4\): it consists of two independent elements of order \(2\), not one element of order \(4\).

## Assumptions and scope

Work over \(\mathbb C\). The surfaces, degeneration and specialization map are precisely the objects \(Y_2\), \(S_{2,0}\), \(S_t\), \(sp_2^2\) in Sections 6.2.3 and 7 of Arapura--Greer--Zhang [1]; no arbitrary deformation with the same fiber types is asserted to carry the same specialization map. Their \(Y_2\) is a singular (Picard-rank \(20\)) Jacobian elliptic K3 surface over \(\mathbb P^1\) with exactly two \(I_0^*\) fibers, one \(IV\) fiber and one \(IV^*\) fiber. Their Proposition 6.8 proves \(\operatorname{disc}T_{Y_2}=48\); their Lemmas 7.4, 7.6 and 7.7 give the source identification and isometric injection, and their Lemma 7.8 identifies \(T_{S_t}\cong A_2\) and the index \(4\). These published facts are inputs, not new claims.

For a smooth projective surface \(V\), its transcendental lattice is \(T_V=\operatorname{NS}(V)^\perp\subset H^2(V,\mathbb Z)\) with cup-product pairing. The transcendental group of the normal-crossings special fiber is taken in the precise sense defined in [1, Section 7.1]. The quotient described here is only the cokernel of the induced map on transcendental lattices. It is not identified with the cokernel of the entire integral cohomology specialization map.

## Proof

**Step 1: a fiber-forced automorphism.** A relatively minimal Jacobian elliptic K3 over \(\mathbb P^1\) admits a minimal Weierstrass model
\[
y^2=x^3+f x+g,\qquad
f\in H^0(\mathbb P^1,\mathcal O(8)),\quad
g\in H^0(\mathbb P^1,\mathcal O(12)).
\]
For a fiber of type \(I_0^*\), the Kodaira--Tate conditions force \(\operatorname{ord}(f)\ge2\); type \(IV\) forces \(\operatorname{ord}(f)\ge2\); and type \(IV^*\) forces \(\operatorname{ord}(f)\ge3\). The four distinct fiber positions of \(Y_2\) therefore force its section \(f\) to vanish with total order at least
\[
2+2+2+3=9>8=\deg\mathcal O(8).
\]
Thus \(f=0\) identically. In particular the Weierstrass equation is preserved by the order-three map \((x,y)\mapsto(\zeta_3 x,y)\), for \(\zeta_3\) a primitive cube root of unity. This automorphism extends through the unique minimal desingularization, since automorphisms of a normal surface lift to its minimal resolution. On a smooth chart it acts on the holomorphic two-form \(dt\wedge dx/y\) by multiplication by \(\zeta_3\), so it is non-symplectic.

**Step 2: identify the rank-two lattice.** Since \(Y_2\) has Picard rank \(20\), its positive definite transcendental lattice \(T=T_{Y_2}\) has rank \(2\). The automorphism preserves \(T\) and its pairing; on \(T\otimes\mathbb Q\) it has eigenvalues \(\zeta_3\) and \(\zeta_3^2\), because \(H^{2,0}\oplus H^{0,2}\) exhausts this complexification. Hence the induced integral isometry \(R\) satisfies \(R^2+R+1=0\). Thus \(T\) is a torsion-free rank-one module over the Euclidean domain \(\mathbb Z[\zeta_3]\), hence a free one. Choose its integral basis \(v,Rv\). Invariance of the pairing yields \((Rv,Rv)=(v,v)\); moreover
\[
0=(v,(1+R+R^2)v)=(v,v)+2(v,Rv),
\]
where \((v,R^2v)=(Rv,v)\). Since \(T\) is even, write \((v,v)=2m\) for a positive integer \(m\). The Gram matrix in the chosen basis is
\[
\begin{pmatrix}2m&-m\\-m&2m\end{pmatrix}=mG.
\]
Its determinant is \(3m^2\). The independently established discriminant \(48\) gives \(3m^2=48\) and therefore \(m=4\). This proves \(T_{Y_2}\cong A_2(4)\). The matrix \(4G=\bigl(\begin{smallmatrix}8&-4\\-4&8\end{smallmatrix}\bigr)\) has gcd of entries \(4\) and determinant \(48\), so its Smith factors are \(4\) and \(12\), giving the asserted discriminant group.

**Step 3: determine the image, not just its index.** Published Lemmas 7.4 and 7.6--7.8 of [1] give an integral pairing-preserving injection
\[
sp_2^2:T_{S_{2,0}}\cong A_2(4)\hookrightarrow A_2\cong T_{S_t}
\]
whose image \(L\) has index \(4\). Under any identification of the codomain with \(A_2=\mathbb Z^2\) with Gram matrix \(G\), a vector \(u=(a,b)\) has square
\[
(u,u)=2(a^2-ab+b^2).
\]
Every vector of \(L\) has square divisible by \(8\), because it comes from \(A_2(4)\). In particular, \(a^2-ab+b^2\) is even. Modulo \(2\), this polynomial is \(a+ab+b\), which is \(1\) at each of the three nonzero pairs \((a,b)\in(\mathbb Z/2\mathbb Z)^2\). Thus both \(a\) and \(b\) must be even, establishing \(L\subseteq2A_2\). Since both \(L\) and \(2A_2\) have index \(4\) in \(A_2\), they are equal. Consequently
\[
A_2/L=A_2/2A_2\cong(\mathbb Z/2\mathbb Z)^2.
\]
This identifies the exact two-torsion exponent of the transcendental obstruction and finishes the proof.

## Verification

The proof in Steps 1--3 is uniform and does not rely on computation or exhaustive search. The standalone standard-library script `verify_lattice.py` independently checks the Eisenstein symmetry and rank-two Gram determinant, the Smith factors of \(4G\), all seven column-Hermite normal forms for sublattices of index four in \(A_2\), and the unique form whose basis norms are divisible by eight. Its direct execution returned `VERIFY_OK`. The finite HNF check is a separate exhaustive test of this finite rank-two index-four classification; the parity argument above proves containment for every vector, without a finite-range assumption.

## Relationship to prior work

Arapura, Greer and Zhang [1] establish the invariant-cycle counterexample, the relevant K3 fiber types, the two discriminants \(48\) and \(3\), the isometric integral specialization and its index \(4\). The present result adds (i) an explicit Gram isometry type \(A_2(4)\) for their specific exceptional K3 component and (ii) the **group structure** of the specialization quotient. Knowing an index is four does not by itself distinguish \(\mathbb Z/4\mathbb Z\) from \((\mathbb Z/2\mathbb Z)^2\). This distinction is the precise refinement claimed; the previously established failure of the integral invariant cycle theorem is not claimed again. The Kodaira fiber valuation bounds and Eisenstein integer module facts used in the proof are classical. Earlier classification of singular elliptic K3 fibrations might contain the lattice isometry type implicitly; no first-priority assertion is made.

## Limitations

The result concerns the transcendental specialization for the specific second degeneration of [1]. It does not compute the full cokernel on integral second cohomology, establish that all missing integral classes have order two in that larger quotient, identify a canonical basis of the two obstruction classes, extend to the other degeneration in [1], or prove the result in positive characteristic. The source lattice has rank two; the proof does not classify higher-rank transcendental lattices. The mathematical arguments have not received an independent external audit, and historical priority of the explicit K3 lattice identification remains subject to scrutiny.

## References

[1] D. Arapura, F. Greer and Y. Zhang, *Failure of the Invariant Cycle Theorem over* \(\mathbb Z\), arXiv:2602.07302 (first public version 2026-02-07; cited text v2, 2026-05-15), especially Sections 2.1, 6.2.3 and 7; Proposition 6.8 and Lemmas 7.4, 7.6--7.8. https://arxiv.org/html/2602.07302v2

[2] T. Shioda and M. Schütt, *Elliptic surfaces*, in *Algebraic Geometry in East Asia* (2010), for Weierstrass models and Kodaira fiber classification (cited by [1] as SS10/SS19).
