# Equational probability spectra of finite Latin affine quandles

## Finding

Let \(p\) be any prime, let \(V\) be an \(n\)-dimensional vector space over \(\mathbb F_p\), with \(n\ge 1\), and let \(T\in\operatorname{GL}(V)\) satisfy \(I-T\in\operatorname{GL}(V)\). Equip \(V\) with the one-operation (no named constants) Latin Alexander quandle
\[
x\triangleright y=T x+(I-T)y.
\]
For terms \(s,t\) on any finite number of variables, let \(\Pr(s=t)\) be the proportion of assignments in \(V\) satisfying that equation; \(\operatorname{PSpec}(V,T)\) is the set of all these probabilities.

Write the \(\mathbb F_p[t]\)-module determined by the action of \(T\) in primary cyclic form
\[
V\cong\bigoplus_{i=1}^{s}\bigoplus_{j=1}^{r_i}
\mathbb F_p[t]/(f_i^{\lambda_{ij}}),
\]
where the \(f_i\) are distinct monic irreducible polynomials, all different from \(t\) and \(t-1\), and all \(\lambda_{ij}\ge1\). Let \(e_i=\max_j\lambda_{ij}\), \(d_i=\deg(f_i)\), and \(\sum_i d_i\sum_j\lambda_{ij}=n\). Then the **entire spectrum** is
\[
\boxed{\operatorname{PSpec}(V,T)=
\left\{p^{-n+\sum_{i=1}^{s}d_i\sum_{j=1}^{r_i}\min(b_i,\lambda_{ij})}:
0\le b_i\le e_i\ (1\le i\le s)\right\}.}
\]
Thus every equational probability is already obtained by a two-variable equation. In particular,
\[
\boxed{\operatorname{PSpec}(V,T)=\{p^{-n},1\}
\quad\Longleftrightarrow\quad \text{the minimal polynomial of }T\text{ is irreducible over }\mathbb F_p.}
\]
If the minimal polynomial is a power \(f^e\) of one irreducible polynomial, the spectrum has exactly \(e+1\) elements. The irreducible-minimal-polynomial condition does **not** require that \(V\) be a simple \(\mathbb F_p[t]\)-module: for example, \(T=2I\) on \(\mathbb F_3^2\) has the minimal spectrum \(\{1/9,1\}\) although it has proper nonzero invariant subspaces.

## Assumptions and scope

The statement concerns equations in the **single binary quandle operation alone**. In particular, addition, scalar multiplication, \(0\), and the division operations are not included in the signature. The finite-dimensional vector space is nonzero. The invertibility of both \(T\) and \(I-T\) is essential to the coefficient-reachability argument; the quandle is Latin. The prime \(p\) may equal two. The formulas concern all finite dimensions, with no bound on polynomial degrees, block multiplicities, or nilpotent Jordan lengths.

## Proof

**1. Exact reachability of two-variable term coefficients.** Put \(R=\mathbb F_p[T]\), a finite commutative unital subring of \(\operatorname{End}_{\mathbb F_p}(V)\). Because \(T\) and \(I-T\) are invertible on \(V\), their inverses belong to \(R\), by the minimal-polynomial/Bézout identity. Any two-variable term \(w(x,y)\) equals
\[
w(x,y)=a x+(I-a)y
\]
for some \(a\in R\), by induction on its formation. Let \(S\subseteq R\) be the set of all such coefficients. The projection terms \(x,y\) show \(I,0\in S\), and term composition shows that \(S\) is closed under
\[
a\star b=T a+(I-T)b.
\]
For \(b\in S\), the map \(\rho_b:a\mapsto Ta+(I-T)b\) sends \(S\) into itself and is injective on \(R\). Finiteness makes \(\rho_b\) a permutation of \(S\). Therefore both \(\rho_0\) and \(\rho_I\), and their inverse maps, preserve \(S\). Their composition \(\rho_I\rho_0^{-1}\) is translation by \(I-T\); conjugating this translation by \(\rho_0^j\) gives translation by \(T^j(I-T)\) for every integer \(j\ge0\). Since \(S\) contains zero, it consequently contains every additive integral combination of these translation increments. Their \(\mathbb F_p\)-span is \((I-T)\mathbb F_p[T]=R\), because \(I-T\) is a unit in \(R\). Hence \(S=R\). This proves, rather than assumes, that every polynomial operator \(a(T)\in R\) can be represented by a binary quandle term.

**2. No equation has an unlisted probability.** A term in variables \(x_1,\ldots,x_k\) is an \(R\)-affine expression \(\sum_j a_j x_j\) with \(\sum_j a_j=I\). Therefore an equation is equivalent to a homogeneous \(\mathbb F_p\)-linear system
\[
L(x_1,\ldots,x_k)=\sum_{j=1}^k c_j x_j=0,
\qquad c_j\in R,
\]
where \(\sum_j c_j=0\). The image is exactly \(\sum_j c_j V\). Let \(m\) be the minimal polynomial of \(T\). The evaluation map gives the principal ideal ring \(R\cong\mathbb F_p[t]/(m)\). Thus the ideal \((c_1,\ldots,c_k)\) of \(R\) has a generator \(g(T)\), with \(g\) chosen to be a monic divisor of \(m\) (including \(g=m\), whose operator is zero). The equality of ideals implies
\[
\operatorname{im}L=\sum_j c_jV=g(T)V.
\]
Uniform inputs to a linear map on finite vector spaces give a uniform output on its image. Thus
\[
\Pr(s=t)=\frac{1}{|g(T)V|}
=\frac{|\ker g(T)|}{|V|}.
\]
Conversely, by Step 1, choose a term \(w_g(x,y)=g(T)x+(I-g(T))y\). Then \(w_g(x,y)=y\) is equivalent to \(g(T)(x-y)=0\) and has exactly the probability above. Therefore
\[
\operatorname{PSpec}(V,T)=
\left\{\frac{|\ker g(T)|}{|V|}:g\mid m\right\}.
\]
This is an equality of sets, not merely an upper bound on possible probabilities.

**3. Primary-module kernel formula.** In the stated decomposition, \(g=\prod_i f_i^{b_i}\) with \(0\le b_i\le e_i\) represents all divisors of \(m=\prod_i f_i^{e_i}\). On the cyclic summand \(\mathbb F_p[t]/(f_i^{\lambda_{ij}})\), multiplication by \(g\) has kernel of \(\mathbb F_p\)-dimension exactly \(d_i\min(b_i,\lambda_{ij})\); every other irreducible factor is a unit on this summand. Summing gives the exponent in the boxed spectrum formula. Equivalently, this can be computed from the elementary divisors or the rational canonical form of \(T\).

**4. Sharp minimality characterization.** If \(m\) is irreducible, its only monic divisors are \(1,m\), and their kernel sizes are \(1,|V|\); the spectrum is minimal. If \(m\) has at least two distinct irreducible factors, taking \(g=f_1^{e_1}\) kills a nonzero primary component but is invertible on another, so \(1<|\ker g(T)|<|V|\). If \(m=f^e\) with \(e\ge2\), the polynomial \(g=f\) has a nonzero kernel but is not the zero operator, because a summand has length \(e\). In both reducible cases, an intermediate probability occurs. Finally, if \(m=f^e\), the consecutive nullities
\[
d\sum_j\min(b,\lambda_j),\qquad b=0,1,\ldots,e,
\]
are strictly increasing since some summand has length \(e\). Thus the spectrum has exactly \(e+1\) values.

## Verification

The self-contained `verify.py` enumerates the coefficient ring independently as polynomial evaluations and iteratively builds the coefficients reachable by actual two-variable terms. It checks equality of these finite sets and the attainable rank spectra for eight explicitly specified Latin examples; in the small cases it also directly counts vector solutions rather than relying on a rank formula. Run `python3 verify.py` with Python 3.8 or later. Its expected terminal status is `VERIFY_OK cases=8`.

The examples include irreducible degree-two and degree-three actions in characteristic two, repeated Jordan blocks in characteristic three, scalar actions on decomposable spaces, and two distinct eigenvalues over \(\mathbb F_5\). They illustrate all proof mechanisms; the infinite-dimensional family assertion (all finite \(n\)) rests on Steps 1–4, not on finite enumeration.

## Relationship to prior work

Carles Cardó introduced and studied the finite-algebra equational probabilistic spectrum in 2026 and proved necessary quasigroup conditions for nontrivial groupoids with minimal spectrum. This work addresses an identifiable, natural class of those quasigroups: Latin affine/Alexander quandles with elementary abelian displacement group. The all-equations formula and the irreducible-minimal-polynomial test are not supplied by Cardó's cited theorems. Bonatto's earlier work classifies simple affine quandles using irreducible actions; the condition here is **irreducibility of the minimal polynomial**, which allows arbitrary multiplicity of a simple module and does not assert that the quandle is simple.

For \(T=-I\) in odd characteristic, the formula reduces to the previously obtained minimal-spectrum statement for Takasaki quandles on elementary abelian \(p\)-groups. The present proof instead treats all Latin invertible operators, including nonsemisimple and mixed-primary actions, and determines every probability level. The general torsion-abellian Takasaki reconstruction claim is not reproduced or re-claimed here.

## Limitations

This result is limited to vector spaces over a prime field and Latin affine operations. No complete formula is claimed for arbitrary finite abelian groups, for non-Latin affine quandles, or for quasigroups outside the affine class. The spectrum need not distinguish the similarity class of \(T\); different irreducible polynomials of the same degree can produce the same set. Literature indexing is incomplete, and the absence of another independently stated identical characterization cannot be proved by search alone. No independent audit has been performed.

## References

1. C. Cardó, *On semigroups and groupoids with minimal probabilistic spectrum*, arXiv:2603.19487, first posted 19 March 2026, especially Theorem 4 and Section 4. https://arxiv.org/abs/2603.19487
2. C. Cardó, *Probabilistic equational spectrum, primality and approximation in finite algebras*, arXiv:2604.08446, first posted 9 April 2026, especially Definition 3.1 and the general clone/product observations. https://arxiv.org/abs/2604.08446
3. M. Bonatto, *Principal and Doubly Homogeneous Quandles*, arXiv:1904.13388, especially Theorem 2.21 and the discussion of Latin affine quandle modules. https://arxiv.org/abs/1904.13388
