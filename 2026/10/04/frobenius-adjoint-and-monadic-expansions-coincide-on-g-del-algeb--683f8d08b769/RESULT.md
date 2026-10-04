# Frobenius-adjoint and monadic expansions coincide on Gödel algebras
## Finding

Let
\[
\mathbf G=(G,\wedge,\vee,\odot,\to,0,1)
\]
be a Gödel algebra. Equivalently for the present argument, \(\mathbf G\) is a commutative integral residuated lattice satisfying
\[
x\odot x=x
\]
and the Gödel prelinearity law.

Let \(f,g:G\to G\). Then
\[
\boxed{
(\mathbf G,f,g)\text{ is Frobenius-adjoint}
\iff
(\mathbf G,\forall,\exists)\text{ is monadic Gödel}
}
\]
under the identification
\[
\forall=f,
\qquad
\exists=g.
\]

This is a genuine collapse of two generally different notions. Wang--Shi--Wang exhibit a monadic residuated lattice that is not Frobenius-adjoint and a Frobenius-adjoint residuated lattice that is not monadic. On Gödel reducts, however, the two classes coincide.

There is a complete finite-chain corollary. Let
\[
G_n=\{c_0<c_1<\cdots<c_{n-1}\}
\]
be the \(n\)-element Gödel chain, with
\[
n\ge2.
\]

Every common Frobenius-adjoint/monadic expansion is determined by a unique subset
\[
F
\quad\text{with}\quad
\{c_0,c_{n-1}\}\subseteq F\subseteq G_n.
\]

The operators are the lower and upper roundings to \(F\):
\[
f(x)=\max(F\cap\downarrow x),
\qquad
g(x)=\min(F\cap\uparrow x).
\]

Conversely, every such \(F\) defines both a Frobenius-adjoint expansion and a monadic Gödel expansion.

Hence
\[
\boxed{
\#\{\text{Frobenius-adjoint expansions of }G_n\}
=
\#\{\text{monadic Gödel expansions of }G_n\}
=
2^{n-2}.
}
\]

The first counts are
\[
1,2,4,8,16,32,\ldots
\]
for
\[
n=2,3,4,5,6,7,\ldots.
\]

## Assumptions and scope

A Frobenius-adjoint residuated lattice is taken in the sense of Wang--Shi--Wang: \(f,g\) satisfy the five axioms FARL1--FARL5, including the adjunction
\[
g(x)\le y
\quad\Longleftrightarrow\quad
x\le f(y)
\]
and the three Frobenius compatibility laws.

A monadic Gödel algebra is a Gödel algebra equipped with the standard monadic operators \(\forall,\exists\) satisfying the monadic residuated-lattice axioms M1--M5. We identify
\[
f=\forall,
\qquad
g=\exists.
\]

The general coincidence theorem is not restricted to finite algebras or chains.

The exact count
\[
2^{n-2}
\]
is the finite-chain specialization. It is a count of expansions on the fixed labelled Gödel chain. Since a finite chain has only the identity lattice automorphism, it is also the number of isomorphism classes with that fixed chain reduct.

## Proof

### Frobenius-adjoint implies monadic on every Gödel algebra

Assume
\[
(\mathbf G,f,g)\in\mathbb{FARL}.
\]

Wang--Shi--Wang derive the following identities from FARL1--FARL5:
\[
f(f(x)\to y)=f(x)\to f(y),
\]
\[
f(x\to f(y))=g(x)\to f(y),
\]
together with
\[
f(g(x)\vee y)=g(x)\vee f(y).
\]

These are precisely the nontrivial implication and join identities needed for the monadic axioms M2--M4 after identifying
\[
f=\forall,
\qquad
g=\exists.
\]

The monadic axiom M1 follows from
\[
f(x)\le x,
\]
because in an integral residuated lattice this is equivalent to
\[
f(x)\to x=1.
\]

It remains only M5. In a Gödel algebra,
\[
x\odot x=x.
\]
Therefore
\[
g(x\odot x)=g(x),
\]
while idempotence of the Gödel product also gives
\[
g(x)\odot g(x)=g(x).
\]
Hence
\[
g(x\odot x)=g(x)\odot g(x).
\]

Thus every Frobenius-adjoint expansion of a Gödel algebra is monadic Gödel.

### Monadic Gödel implies Frobenius-adjoint

Now assume
\[
(\mathbf G,\forall,\exists)
\]
is a monadic Gödel algebra, and put
\[
f=\forall,
\qquad
g=\exists.
\]

A standard structural lemma for monadic Gödel algebras states that
\[
F:=\exists G=\forall G
\]
is a Gödel subalgebra and, for every \(x\in G\),
\[
g(x)=\min\{c\in F:x\le c\},
\]
\[
f(x)=\max\{c\in F:c\le x\}.
\]

These formulas immediately give the Galois adjunction. Indeed,
\[
g(x)\le y
\]
holds exactly when some member of \(F\) above \(x\), namely the least one, lies below \(y\). This is equivalent to
\[
x\le f(y),
\]
because \(f(y)\) is the greatest member of \(F\) below \(y\). Hence FARL2 holds.

The inequality FARL1,
\[
f(x)\le x,
\]
is built into the lower-rounding formula.

For FARL3, let
\[
a=g(x)\in F.
\]
Elements of \(F\) are fixed by \(f\). The monadic implication identity M3, applied to the fixed element \(a\), gives
\[
f(a\to y)=a\to f(y),
\]
that is,
\[
f(g(x)\to y)=g(x)\to f(y).
\]

For FARL4, the monadic join law M4 is
\[
f(y\vee g(x))=f(y)\vee g(x),
\]
which, by commutativity of \(\vee\), is exactly
\[
f(g(x)\vee y)=g(x)\vee f(y).
\]

For FARL5, the standard monadic Gödel identity
\[
g(y\wedge c)=g(y)\wedge c
\qquad(c\in F)
\]
applied to
\[
c=g(x)\in F
\]
gives
\[
g(y\wedge g(x))=g(y)\wedge g(x).
\]
Renaming variables and using commutativity of \(\wedge\) yields FARL5.

Thus every monadic Gödel algebra is Frobenius-adjoint.

Combining the two directions proves the general coincidence theorem.

### Finite-chain normal form

Now let
\[
G_n=\{c_0<\cdots<c_{n-1}\}.
\]

For a Frobenius-adjoint expansion, Wang--Shi--Wang prove
\[
f(g(x))=g(x),
\qquad
g(f(x))=f(x),
\]
and idempotence of both \(f\) and \(g\). Therefore
\[
\operatorname{Fix}(f)
=
\operatorname{Im}(f)
=
\operatorname{Fix}(g)
=
\operatorname{Im}(g).
\]
Call this common set \(F\).

They also prove
\[
f(0)=g(0)=0,
\qquad
f(1)=g(1)=1,
\]
so
\[
\{c_0,c_{n-1}\}\subseteq F.
\]

Since \(f\) is monotone and
\[
f(x)\le x,
\]
the value \(f(x)\) is the greatest fixed point below \(x\). Indeed, if
\[
z\in F
\quad\text{and}\quad
z\le x,
\]
then
\[
z=f(z)\le f(x).
\]
Hence
\[
f(x)=\max(F\cap\downarrow x).
\]

Similarly, \(g\) is monotone and
\[
x\le g(x).
\]
If
\[
z\in F
\quad\text{and}\quad
x\le z,
\]
then
\[
g(x)\le g(z)=z,
\]
so
\[
g(x)=\min(F\cap\uparrow x).
\]

Thus every expansion is uniquely determined by \(F\).

Conversely, choose any
\[
F
\quad\text{with}\quad
\{c_0,c_{n-1}\}\subseteq F\subseteq G_n,
\]
and define \(f,g\) by lower and upper rounding.

The adjunction
\[
g(x)\le y
\quad\Longleftrightarrow\quad
x\le f(y)
\]
follows directly from the two rounding definitions.

To check FARL3, set
\[
a=g(x)\in F.
\]
On a Gödel chain,
\[
a\to y=
\begin{cases}
1,&a\le y,\\
y,&a>y.
\end{cases}
\]
If \(a\le y\), then \(a\le f(y)\), so both sides of FARL3 are \(1\). If \(a>y\), then \(f(y)\le y<a\), so both sides are \(f(y)\).

For FARL4, if \(a=g(x)\in F\), lower rounding commutes with joining by the fixed point \(a\):
\[
f(a\vee y)=a\vee f(y).
\]

For FARL5, upper rounding commutes with meeting by a fixed point:
\[
g(x\wedge g(y))=g(x)\wedge g(y).
\]

Therefore every endpoint-containing subset \(F\) gives a valid Frobenius-adjoint expansion and, by the general coincidence theorem, a monadic Gödel expansion.

There are
\[
n-2
\]
interior chain elements, each independently either included in \(F\) or omitted. Hence the exact count is
\[
2^{n-2}.
\]

## Verification

The bundled checker performs three independent finite replays.

First, for chain sizes
\[
2\le n\le4,
\]
it exhaustively enumerates every pair of unary maps
\[
f,g:G_n\to G_n
\]
and filters them separately by the FARL axioms and by the standard monadic Gödel axioms. The two surviving sets agree exactly.

Second, for
\[
2\le n\le6,
\]
it exhaustively enumerates every candidate right adjoint \(f\), reconstructs its possible left adjoint \(g\), checks FARL1--FARL5, and confirms that the survivors are exactly the lower/upper rounding pairs coming from endpoint-containing subsets \(F\).

Third, it constructs every such subset through
\[
n=12
\]
and checks both axiom systems directly, obtaining exactly
\[
2^{n-2}
\]
expansions at each size.

As a non-chain corroboration of the general coincidence theorem, the checker also exhaustively enumerates every pair of unary maps on the four-element Gödel algebra
\[
G_2\times G_2.
\]
The FARL and monadic Gödel survivors again agree exactly.

The computation is corroborative. The theorem for arbitrary Gödel algebras follows from the algebraic proof above, not from finite enumeration.

## Relationship to prior work

Wang--Shi--Wang introduce Frobenius-adjoint residuated lattices in 2026 as the algebraic semantics of their Frobenius--Galois expansion of \(\mathbf{FL}_{ew}\). Their Definition 3.8 gives FARL1--FARL5, and Proposition 3.13 derives the implication, fixed-point, monotonicity, and idempotence identities used above.

Crucially, the same paper explicitly compares FARL with monadic residuated lattices and proves that the two classes are incomparable in general: Example 3.16 gives a monadic residuated lattice outside FARL, while Example 3.17 gives a Frobenius-adjoint Łukasiewicz chain outside the monadic class. The checked full text contains no Gödel-algebra specialization.

Castaño--Cimadamore--Díaz Varela--Rueda study monadic Gödel algebras before FARL was introduced. Their structural lemma identifies the common image
\[
\exists G=\forall G
\]
as a Gödel subalgebra and expresses \(\exists\) and \(\forall\) as upper and lower approximation to that image. This supplies the established monadic side of the converse argument, but of course does not compare with the later Frobenius-adjoint notion.

The present result joins these two strands: the new FARL notion and the older monadic Gödel notion, although different on general residuated lattices, define exactly the same expansions on every Gödel algebra. The finite-chain count is then an exact corollary: every endpoint-containing subchain gives one expansion.

Targeted searches for Frobenius-adjoint Gödel algebras, FARL/monadic Gödel coincidence, and finite-chain Frobenius-adjoint counts did not locate this collapse theorem.

## Limitations

The coincidence uses the Gödel setting essentially. In particular, the implication
\[
\mathbb{FARL}\subseteq\mathbb{MRL}
\]
uses idempotence of the monoidal product to discharge M5. Wang--Shi--Wang's three-element Łukasiewicz example shows that the implication fails outside the idempotent setting.

The reverse implication uses structural properties of monadic Gödel algebras. The theorem does not assert that monadic and Frobenius-adjoint expansions coincide on arbitrary idempotent residuated lattices without the Gödel assumptions.

The exact formula
\[
2^{n-2}
\]
is only for finite chains. General finite Gödel algebras can have a richer lattice of Gödel subalgebras, so their number of common expansions need not be a power of two.

No claim is made about free Frobenius-adjoint Gödel algebras, the size of free algebras, or decision complexity.

## References

[1] Juntao Wang, Jieqiong Shi, and Mei Wang, “Frobenius–Galois expansions of substructural logics: Algebraization, Kalman equivalence and positive-cone semantics,” arXiv:2609.09529, first posted 8 September 2026.

[2] Diego Castaño, Cecilia Cimadamore, José Patricio Díaz Varela, and Laura Rueda, “An Algebraic Study of S5-Modal Gödel Logic,” arXiv:2006.10180, first posted 17 June 2020; *Studia Logica* 109 (2021), 937–967. DOI:10.1007/s11225-020-09934-x.

[3] Marcel Erné, Jorge Picado, and Aleš Pultr, “Adjoint maps between implicative semilattices and continuity of localic maps,” *Algebra Universalis* 83 (2022), Article 13. DOI:10.1007/s00012-022-00767-4.
