# Locality and self-injectivity of normal p-subgroup centralizer algebras

Let \(G\) be a finite group, let \(k\) be a field of characteristic \(p>0\), and let
\(1\ne P\unlhd G\) be a \(p\)-subgroup. Write
\[
A=(kG)^P=C_{kG}(P)
\]
for the fixed algebra under conjugation by \(P\), and let
\[
\operatorname{Br}_P:A\longrightarrow kC_G(P)
\]
be the Brauer projection, which retains the coefficients of elements centralizing
\(P\).

## Theorem

Put \(I=\ker(\operatorname{Br}_P)\). Then:

1. \(I\) is nilpotent and
   \[
   A/J(A)\cong kC_G(P)/J(kC_G(P)).
   \]
   In particular, \(A\) and \(kC_G(P)\) have the same simple-module quotient.

2. \(A\) is local if and only if \(C_G(P)\) is a \(p\)-group.

3. Suppose these equivalent locality conditions hold. Then the following are
   equivalent:
   \[
   P\le Z(G),\qquad I=0,\qquad
   A\text{ is symmetric},\qquad
   A\text{ is Frobenius},\qquad
   A\text{ is self-injective}.
   \]
   If \(P\not\le Z(G)\), then
   \[
   \dim_k \operatorname{Soc}({}_A A)\ge 2,
   \]
   so \(A\) is not self-injective and hence is not symmetric.


4. Suppose in addition that
   \[
   C_P(g)=1\qquad(g\in G\setminus P).
   \]
   If \(m=[G:P]\) and \(V\) is a vector space of dimension \(m-1\), then
   \[
   A\cong Z(kP)\ltimes V,
   \]
   where \(V^2=0\) and \(z\in Z(kP)\) acts on \(V\) on both sides as the scalar
   \(\varepsilon(z)\). Consequently
   \[
   J(A)=J(Z(kP))\oplus V,\qquad
   \operatorname{Soc}(A)=\operatorname{Soc}(Z(kP))\oplus V.
   \]
   In particular, if \(G\ne P\), then
   \[
   \dim_k\operatorname{Soc}(A)\ge [G:P]\ge2.
   \]

Thus, for a normal \(p\)-subgroup, locality of the centralizer algebra is governed
exactly by the group centralizer, while within the local regime symmetry and
self-injectivity occur exactly in the trivial-conjugation case.

## Proof

The \(P\)-orbits on \(G\) under conjugation give the standard orbit-sum basis of
\(A\). The Brauer map sends the orbit sum of a singleton orbit to the corresponding
element of \(C_G(P)\), and sends every non-singleton orbit sum to zero. Hence it is
a surjective algebra homomorphism
\[
\operatorname{Br}_P:A\twoheadrightarrow kC_G(P).
\]

We first show that its kernel \(I\) is nilpotent. Since \(P\unlhd G\) is a normal
\(p\)-subgroup, \(P\) acts trivially on every simple \(kG\)-module. Indeed, the
\(P\)-fixed subspace of a nonzero \(kG\)-module is nonzero for a \(p\)-group in
characteristic \(p\), and normality of \(P\) makes that fixed subspace \(G\)-stable;
simplicity then forces it to be the whole module.

Let \(C\) be a non-singleton \(P\)-orbit in \(G\), and let
\(C^+=\sum_{x\in C}x\). All elements of \(C\) induce the same operator on every
simple \(kG\)-module, while \(|C|\) is divisible by \(p\). Hence \(C^+\) annihilates
every simple \(kG\)-module. Therefore
\[
C^+\in J(kG).
\]
The kernel \(I\) is spanned by these non-singleton orbit sums, so
\[
I\subseteq J(kG)\cap A.
\]
Consequently \(I\) is nilpotent. In particular \(I\subseteq J(A)\). Since
\(A/I\cong kC_G(P)\), the standard radical identity for a quotient by an ideal
contained in the Jacobson radical gives
\[
J(A)/I=J(A/I)=J(kC_G(P)),
\]
and therefore
\[
A/J(A)\cong kC_G(P)/J(kC_G(P)).
\]
This proves part 1.

A finite group algebra \(kH\) in characteristic \(p\) is local exactly when \(H\)
is a \(p\)-group. Applying this to \(H=C_G(P)\), and using the preceding
semisimple-quotient isomorphism, proves part 2.

Now assume \(A\) is local. The augmentation
\[
\varepsilon:A\longrightarrow k
\]
is a surjective algebra homomorphism, so its kernel is a maximal ideal. Because
\(A\) is local,
\[
J(A)=\ker\varepsilon
\qquad\text{and}\qquad
A/J(A)\cong k.
\]

Let
\[
\omega_G=\sum_{g\in G}g.
\]
For every \(a\in kG\),
\[
a\omega_G=\varepsilon(a)\omega_G.
\]
Thus \(J(A)\omega_G=0\), and hence
\[
k\omega_G\subseteq\operatorname{Soc}({}_A A).
\]

Suppose \(P\not\le Z(G)\). Then the conjugation action of \(P\) on \(G\) has a
non-singleton orbit, so \(I\ne0\). As a nonzero finite-dimensional left
\(A\)-module, \(I\) has a nonzero socle:
\[
0\ne\operatorname{Soc}({}_A I)
   \subseteq\operatorname{Soc}({}_A A).
\]
Moreover,
\[
\operatorname{Br}_P(\omega_G)
   =\sum_{c\in C_G(P)}c\ne0,
\]
whereas \(\operatorname{Br}_P(I)=0\). Therefore
\[
k\omega_G\cap I=0,
\]
and hence
\[
\dim_k\operatorname{Soc}({}_A A)\ge2.
\]

A finite-dimensional local self-injective \(k\)-algebra with residue field \(k\)
has one-dimensional left socle. One way to see this is to dualize the injective
left regular module: \(A^*=\operatorname{Hom}_k(A,k)\) is then a projective right
module. Since \(A\) is local and \(\dim_k A^*=\dim_k A\), one has
\(A^*\cong A_A\); taking top/socle under the usual duality yields
\(\operatorname{Soc}({}_A A)\cong k\). The preceding lower bound therefore shows
that \(A\) is not self-injective whenever \(P\not\le Z(G)\).

Conversely, if \(P\le Z(G)\), then every conjugation orbit is a singleton, so
\(I=0\) and \(A=kG\). Under the standing locality assumption,
\(C_G(P)=G\) is a \(p\)-group. Every finite group algebra is symmetric, so \(A\)
is symmetric, hence Frobenius and self-injective. This proves all equivalences in
part 3. \(\square\)


## Fixed-point-free refinement

Assume now that \(C_P(g)=1\) for every \(g\notin P\). Every \(P\)-orbit outside
\(P\) then has size \(|P|\). Since such an orbit is contained in a coset of \(P\)
and a coset also has \(|P|\) elements, the non-singleton orbits outside \(P\) are
exactly the nontrivial cosets \(Pg\).

For a nontrivial coset \(q=Pg\), put
\[
X_q=\sum_{x\in Pg}x.
\]
The orbit-sum basis of \(A\) is therefore the union of a class-sum basis of
\(Z(kP)\) with the \(X_q\) for \(q\in G/P-\{P\}\). Let \(V\) be their span.
For \(z\in kP\),
\[
zX_q=X_qz=\varepsilon(z)X_q,
\]
because left or right multiplication by an element of \(P\) merely permutes a
coset. Also, if \(q=Pg\) and \(r=Ph\), every element of \(Pgh\) occurs exactly
\(|P|\) times in \(X_qX_r\). Hence
\[
X_qX_r=|P|X_{qr}=0
\]
in characteristic \(p\) (with the evident interpretation when \(qr=P\)).
Thus \(V^2=0\), and
\[
A=Z(kP)\ltimes V
\]
with the asserted augmentation action.

The center \(Z(kP)\) is local, with radical the kernel of augmentation restricted
to the center. The displayed multiplication immediately gives
\[
J(A)=J(Z(kP))\oplus V.
\]
Since the radical of \(Z(kP)\) kills \(V\), \(V^2=0\), and every element in
\(\operatorname{Soc}(Z(kP))\) has augmentation zero when \(P\ne1\), one obtains
\[
\operatorname{Soc}(A)=\operatorname{Soc}(Z(kP))\oplus V.
\]
This proves part 4.

## Corollaries

### Groups of characteristic \(p\)

If \(O_p(G)\ne1\) and
\[
C_G(O_p(G))\le O_p(G),
\]
then \(A=(kG)^{O_p(G)}\) is local. It is symmetric (equivalently Frobenius or
self-injective) if and only if
\[
G=O_p(G)\quad\text{is abelian}.
\]
Indeed, the displayed centralizer condition makes \(C_G(O_p(G))\) a \(p\)-group.
If \(O_p(G)\) were central, then
\(G=C_G(O_p(G))\le O_p(G)\), so \(G=O_p(G)\), and centrality makes it abelian.

### Frobenius groups with \(p\)-group kernel

If \(G\) is a nontrivial Frobenius extension with \(p\)-group kernel \(P\), then
every element outside \(P\) acts fixed-point-freely on \(P\). Thus
\(C_G(P)=Z(P)\), \(P\not\le Z(G)\), and the fixed-point-free refinement applies:
\[
(kG)^P\cong Z(kP)\ltimes k^{[G:P]-1}
\]
with square-zero second summand and augmentation action. In particular the algebra
is local but not self-injective, Frobenius, or symmetric.

For example, in characteristic \(3\), with \(G=S_3\) and
\(P=A_3\cong C_3\), the algebra \((kS_3)^{C_3}\) is local and not self-injective.

## Relation to prior work

Danz, Ellers and Murray asked whether modular centralizer algebras \(kG^H\) are
symmetric and exhibited general counterexamples. In the same paper they used the
Brauer map for a normal \(p\)-subgroup and observed that its kernel is nilpotent.
The first part of the theorem above extracts the resulting semisimple-quotient
control, while the socle argument gives a sharp locality/self-injectivity
classification.

Allan proved that if \(Q\) is a non-central subgroup of a finite \(p\)-group \(R\),
then \(kR^Q\) is not self-injective. The theorem above is complementary: normality
of the acting \(p\)-subgroup allows the ambient group to be arbitrary, and in the
entire local regime it gives an if-and-only-if criterion rather than only a
negative case.

## Originality and limitations

The result is asserted to the best of our knowledge. Targeted searches for
normal-\(p\)-subgroup centralizer algebras, local centralizer algebras,
self-injectivity, symmetry, the Brauer kernel, and self-centralizing or
characteristic-\(p\) hypotheses did not locate the theorem above or an equivalent
classification.

The main originality risk is that the statement may occur implicitly as an
unstated corollary of standard Brauer-map theory or in work using different Hecke
algebra terminology. The two principal ingredients are individually close to known
results: nilpotence of the Brauer kernel for normal \(p\)-subgroups appears in
Danz--Ellers--Murray, while Allan uses the same two-dimensional-socle obstruction
for centralizer algebras inside \(p\)-group algebras. The new content claimed here
is their combination into the locality criterion and the exact
self-injective/Frobenius/symmetric classification for arbitrary finite ambient
groups with a normal \(p\)-subgroup, together with the explicit square-zero
extension description under fixed-point-free outside action.

## References

1. S. Danz, H. Ellers and J. Murray, *The Centralizer of a Subgroup in a Group
   Algebra*, Proc. Edinburgh Math. Soc. **56** (2013), 49--56.
   DOI: 10.1017/S0013091512000077.
2. A. Allan, *Modular Centralizer Algebras Corresponding to p-Groups*,
   J. Algebra **339** (2011), 156--171.
   DOI: 10.1016/j.jalgebra.2011.04.026; arXiv:1011.3559.
