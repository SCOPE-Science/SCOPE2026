# Complete commuting-retraction graphs of three-dimensional symmetric Leibniz algebras

## Finding

Let \(K\) be a field of characteristic not \(2\), and let \(\lambda\in K^\times\). In the Leibniz algebra \(L_\lambda=Kx\oplus Ky\oplus Kz\), the only nonzero brackets of basis vectors are
\[
[x,x]=z,\qquad [y,y]=\lambda z.
\]
Let \(E_\lambda\) be the idempotents in the endomorphism monoid of \(L_\lambda\). An idempotent endomorphism is also called a retraction. Put \(V=Kx\oplus Ky\), \(B=\operatorname{diag}(1,\lambda)\) and write \([v+az,w+bz]=B(v,w)z\).

**Structure over arbitrary fields of characteristic not \(2\).** If \(-\lambda\) is not a square in \(K\), then \(E_\lambda=\{0,I\}\). If \(-\lambda\) is a square, let \(U_+\) and \(U_-\) be the two distinct isotropic one-dimensional subspaces for \(B\). Every element of \(E_\lambda\setminus\{0,I\}\) is uniquely determined by an isotropic line \(U\in\{U_+,U_-\}\), an idempotent rank-one projection \(A:V\to U\) with \(A|_U=I_U\), and a linear map \(\psi:V\to K\) vanishing on \(\ker A\); its action is \(f(v+az)=Av+\psi(v)z\). Equivalently, choose \(0\ne u\in U\), \(\alpha\in V^*\) with \(\alpha(u)=1\), and \(t\in K\), and set \(f(v+az)=\alpha(v)(u+tz)\). Only \(0\) and \(I\) have rank other than \(1\).

**Complete finite-field commuting graph.** Now suppose \(K=\mathbb F_q\) with \(q\) odd. In the split case there are \(2q^2+2\) idempotents. The simple graph on the \(2q^2\) distinct elements other than \(0\) and \(I\), with adjacency for commuting under composition, is
\[
K_{q,q}\sqcup 2q(q-1)K_1.
\]
The full graph is its join with \(K_2\), whose two vertices are \(0,I\). In particular its clique polynomial, including the empty clique and writing \(s\) for the counting variable, is
\[
C_q(s)=(1+s)^2(1+2q^2s+q^2s^2).
\]
Every maximal pairwise commuting idempotent subset is automatically a subsemigroup, and there are exactly \(q^2\) such maximal subsemigroups of size \(4\) and \(2q(q-1)\) of size \(3\). For \(e\in E_\lambda\), centralizers \(C_E(e)=\{f\in E_\lambda:ef=fe\}\) have sizes
\[
|C_E(e)|=\begin{cases}
2+2q^2&\text{for exactly two }e,\\
q+3&\text{for exactly }2q\text{ elements},\\
3&\text{for exactly }2q(q-1)\text{ elements}.
\end{cases}
\]
Thus independent uniform idempotents commute with probability
\[
\frac{3q^2+1}{(q^2+1)^2}.
\]
In the nonsplit case \(E_\lambda=\{0,I\}\), \(C_q(s)=(1+s)^2\), and \(\{0,I\}\) is the unique maximal commuting idempotent subsemigroup. The nonsplit cardinality itself is known and is not asserted to be new.

## Assumptions and scope

This is the explicit three-dimensional two-step nilpotent left Leibniz algebra above. Endomorphisms are \(K\)-linear bracket-preserving maps. The graph is a *simple* commuting graph, so a vertex has no loop, while its centralizer includes itself. The graph description and all cardinality formulas require a finite field of odd cardinality, but the retraction classification and the commuting criterion hold over any field of characteristic different from \(2\). A square of zero is excluded by requiring \(\lambda\ne0\). No claim is made in characteristic \(2\), for degenerate forms, or for arbitrary nonsymmetric two-step Leibniz algebras.

## Proof

**Step 1: Endomorphism equations.** Since \([L_\lambda,L_\lambda]=Kz\), an endomorphism must have block form
\[
f=\begin{pmatrix}A&0\\\psi&\mu\end{pmatrix},
\qquad A\in\operatorname{End}_K(V),\quad\psi\in V^*,\quad\mu\in K.
\]
The bracket identity for all \(v,w\in V\) is exactly
\[
B(Av,Aw)=\mu B(v,w),\quad\text{or equivalently }A^{\mathsf T}BA=\mu B.
\]
Conversely these equations suffice because \(z\) is central. For \(f^2=f\), block multiplication gives
\[
A^2=A,\qquad \mu^2=\mu,\qquad \psi A+\mu\psi=\psi.
\]
As \(K\) is a field, \(\mu\in\{0,1\}\).

**Step 2: Rank and isotropy.** If \(\mu=1\), nonsingularity of \(B\) makes \(A\) invertible, so \(A^2=A\) yields \(A=I_V\); the last equation gives \(\psi=0\), hence \(f=I\). If \(\mu=0\), the equation \(A^{\mathsf T}BA=0\) makes \(\operatorname{im}A\) totally isotropic. A nondegenerate symmetric form on a two-space in characteristic different from \(2\) has no nonzero totally isotropic subspace in the anisotropic case, and has exactly the two isotropic lines \(U_+,U_-\) in the hyperbolic case. Thus \(A=0\) entails \(\psi=0\) and yields the zero map. Otherwise \(A\) is a rank-one projection, hence \(A=u\alpha\) for \(u\in U\setminus\{0\}\) and \(\alpha(u)=1\). The equation \(\psi A=\psi\) forces \(\psi=t\alpha\), uniquely for some \(t\in K\). This proves the asserted classification and gives \(q\) projection kernels times \(q\) lifts for each of the two isotropic lines, hence \(2q^2\) rank-one idempotents in the split finite-field case.

**Step 3: Commutation within and between the two types.** Regard a nontrivial idempotent \(f\) as a rank-one projection onto \(K(u+tz)\), with coefficient functional \(\alpha\) killing \(z\). For two idempotents \(f,g\) with the *same* projected isotropic line, their coefficient functionals are nonzero on the common line and their products do not vanish. Commuting distinct rank-one idempotents of this type is impossible: their equal products would have image in both \(\operatorname{im}f\) and \(\operatorname{im}g\), forcing their full image lines to agree; with the same image line, the identities \(fg=g\) and \(gf=f\) force \(f=g\). (If the full image lines differ their intersection is zero, contradicting nonzero products.)

If \(f,g\) project to *different* isotropic lines in \(V\), the one-dimensional images in \(L_\lambda\) are distinct. Thus \(fg=gf\) is equivalent to both products being zero. This holds exactly when \(\ker(A_f)=U_g\) and \(\ker(A_g)=U_f\): every functional kills \(z\), and its restriction to the opposite line must be zero. For the fixed pair \((U_+,U_-)\), these conditions specify one projection \(A_+\) and one \(A_-\), but allow each central lift parameter \(t\) to vary independently. Therefore \(q\) idempotents on one side commute with all \(q\) on the other side, while no other pair of distinct nontrivial idempotents commutes. This proves \(K_{q,q}\sqcup 2q(q-1)K_1\).

**Step 4: Cliques, semilattices, centralizers.** Both \(0\) and \(I\) commute with every endomorphism. The noncentral graph contains \(2q^2\) vertices and exactly \(q^2\) edges, with no triangle, so its clique polynomial is \(1+2q^2s+q^2s^2\), and adding two universal adjacent vertices multiplies this by \((1+s)^2\). Maximal cliques of the noncentral graph are its \(q^2\) edges and its \(2q(q-1)\) isolated vertices. Appending \(0,I\) gives the asserted two sizes. Products within any such clique are either one of its elements or \(0\), so it is closed under composition. Centralizer size counts follow from the two universal elements, the degree \(q\) of each of the \(2q\) nonisolated nontrivial vertices, and the \(2q(q-1)\) isolated vertices. Summing \(|C_E(e)|\) over all \(e\in E\) gives \(4+12q^2\) ordered commuting pairs. Division by \((2+2q^2)^2\) proves the probability formula. The anisotropic case follows from Step 2.

## Verification

The included standard-library programs `verify_leibniz.py` and `verify_gf9.py` are independent finite computations. The first enumerates bracket-preserving matrices, tests \(f^2=f\) by full matrix multiplication, and computes the commuting graph for all eight tested pairs \((q,\lambda)\) with prime \(q\in\{3,5,7,11\}\), testing both split and nonsplit coefficients. The second implements the extension field \(\mathbb F_9=\mathbb F_3[t]/(t^2+1)\) explicitly and checks two square classes there. Both executed successfully and print `VERIFY_OK` or `VERIFY_GF9_OK`. The all-field proof is independent of these finite verifications.

## Relationship to prior work

Kurdachenko, Pypka, and Semko (2023, arXiv:2310.11180v1) study automorphism groups of exactly the type of three-dimensional nilpotent Leibniz algebra in this note. Their section 3 derives the bracket-preservation equations and matrix shape for automorphisms; those equations are a starting point here and are not claimed to be new. The 2022 low-dimensional classification supplies the structural type. Earlier work on Leibniz endomorphisms concerns cyclic Leibniz algebras. The contribution asserted here is not the bracket presentation, the general matrix identity, or previously counted nonsplit idempotents, but the complete split/nonsplit retraction structure and particularly the full commuting graph, compatibility families, clique polynomial, and centralizer census. No inspected source gives these combined endomorphism-monoid compatibility statements. The possibility of differently formulated broader coverage remains a literature-priority risk.

## Limitations

The finite enumeration is corroboration, not an infinite proof or an independent mathematical audit. Publication-priority claims are relative to the inspected primary literature and searched scientific records, not exhaustive. The general square/nonsquare criterion requires characteristic different from \(2\). Only this concrete symmetric, nondegenerate two-dimensional bracket tensor is treated; conclusions do not automatically transfer to arbitrary nilpotent Leibniz structures. The result overlaps prior descriptions of the underlying algebra and its automorphism group, but those are not submitted as novel conclusions.

## References

1. L. A. Kurdachenko, O. O. Pypka, M. M. Semko, *On the automorphism groups of some nilpotent 3-dimensional Leibniz algebras*, arXiv:2310.11180v1 (first submitted 17 October 2023), https://arxiv.org/html/2310.11180v1.
2. L. A. Kurdachenko, O. O. Pypka, I. Ya. Subbotin, *On the structure of low-dimensional Leibniz algebras: some revision* (2022), https://admjournal.luguniv.edu.ua/index.php/adm/article/download/2036/pdf.
3. L. A. Kurdachenko, I. Ya. Subbotin, V. S. Yashchuk, *On the endomorphisms and derivations of some Leibniz algebras*, arXiv:2104.05922 (2021), https://arxiv.org/abs/2104.05922.
4. P. Ye. Minaiev, O. O. Pypka, M. M. Semko, *Low-dimensional nilpotent Leibniz algebras and their automorphism groups* (2024), https://admjournal.luguniv.edu.ua/index.php/adm/article/download/2264/pdf.
