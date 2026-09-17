# The Steinberg covering number of \(\operatorname{PGL}_n(q)\) is \(2\) or \(3\)

## Statement

Let \(n\ge 2\), let \(q\) be a prime power, and put
\[
G=\operatorname{GL}_n(q),\qquad Z=Z(G),\qquad \overline G=G/Z=\operatorname{PGL}_n(q).
\]
The Steinberg character \(\operatorname{St}_n\) of \(G\) is trivial on \(Z\), so it descends to an
irreducible character, again denoted \(\operatorname{St}_n\), of \(\overline G\).

For a nonlinear irreducible character \(\theta\) of a finite group, define its character
covering number \(c(\theta)\) to be the least positive integer \(r\), if one exists, such that
every irreducible character of the group occurs in \(\theta^r\).

### Theorem

Let
\[
d=\gcd(n,q-1).
\]
Then
\[
\boxed{
c(\operatorname{St}_n)=
\begin{cases}
2,& d=1,\\[2mm]
3,& d>1.
\end{cases}}
\]

Equivalently, viewed on \(G\), the third tensor power
\[
\boxed{\operatorname{St}_n^{\,3}}
\]
contains every irreducible character of \(G\) that is trivial on \(Z\); moreover the second
tensor power already has this property exactly when \(\gcd(n,q-1)=1\).

Thus the canonical Steinberg representation always covers all irreducible representations of
\(\operatorname{PGL}_n(q)\) by its third tensor power, and the obstruction to doing so in the
square is exactly the nontrivial diagonal-outer quotient measured by
\(\gcd(n,q-1)\).

## Input from recent literature

Monteiro and Stasinski prove in arXiv:2609.17319 that
\[
\operatorname{St}_n^2
\]
contains every **nonlinear** irreducible character of \(G\) that is trivial on \(Z\). They also
show that a different irreducible character \(\sigma\) can be chosen so that \(\sigma^2\)
contains every center-trivial irreducible, including the linear ones. Their introduction
explicitly notes that the Steinberg square itself is insufficient in general because it can
miss center-trivial linear characters.

When \(d=1\), their character \(\sigma\) is the Steinberg character, and their theorem recovers
the Steinberg-square theorem in the corresponding projective special linear case. The new
point here is that, when \(d>1\), one more Steinberg factor always repairs exactly the missing
linear part, and no further tensor power is needed.

## A general completion lemma

The mechanism is not specific to general linear groups.

### Lemma

Let \(H\) be a finite group with cyclic abelianization \(H/H'\). Let
\(\theta\in\operatorname{Irr}(H)\) be nonlinear and self-dual. Assume that
\(\theta^2\) contains every nonlinear irreducible character of \(H\). Then
\[
\theta^3
\]
contains every irreducible character of \(H\).

#### Proof

First let \(\lambda\) be linear. Then \(\lambda\theta\) is a nonlinear irreducible character, so
\(\lambda\theta\) occurs in \(\theta^2\). Self-duality of \(\theta\) gives
\[
\langle \theta^3,\lambda\rangle
=
\langle \theta^2,\lambda\theta\rangle>0.
\]
Hence every linear character occurs in \(\theta^3\).

Now let \(\chi\) be nonlinear. We claim that \(\chi\theta\) has a nonlinear irreducible
constituent. Suppose instead that every constituent of \(\chi\theta\) were linear. Then the
restriction of a representation affording \(\chi\theta\) to \(H'\) would be trivial. For every
\(h\in H'\),
\[
\rho_\chi(h)\otimes \rho_\theta(h)=I.
\]
If invertible matrices \(A,B\) satisfy \(A\otimes B=I\), then both \(A\) and \(B\) are scalar.
Thus \(\rho_\theta(H')\) consists of scalars.

Because \(H/H'\) is cyclic, choose \(g\in H\) whose coset generates \(H/H'\). Every element of
\(H\) is \(h'g^j\) with \(h'\in H'\), so every matrix in \(\rho_\theta(H)\) is a scalar
multiple of a power of \(\rho_\theta(g)\). Hence \(\rho_\theta(H)\) is abelian. An irreducible
complex representation with abelian image is one-dimensional, contradicting the hypothesis
that \(\theta\) is nonlinear.

Therefore \(\chi\theta\) has a nonlinear constituent \(\psi\). By hypothesis
\(\psi\subseteq\theta^2\), so
\[
\langle\theta^3,\chi\rangle
=
\langle\theta^2,\chi\theta\rangle>0.
\]
This proves the lemma. \(\square\)

## Proof of the theorem

We work with center-trivial characters of \(G\), equivalently characters of
\(\overline G=\operatorname{PGL}_n(q)\).

### 1. The case \(d=1\)

Monteiro--Stasinski prove that in this case their universal-square character \(\sigma\) is
\(\operatorname{St}_n\). Hence every center-trivial irreducible occurs in
\(\operatorname{St}_n^2\).

The Steinberg character is nonlinear for \(n\ge2\), so its first tensor power cannot already
contain the trivial character. Therefore
\[
c(\operatorname{St}_n)=2.
\]

This includes the exceptional group \(\operatorname{GL}_2(2)\cong S_3\): its two-dimensional
Steinberg character satisfies
\[
\operatorname{St}_2^2=1+\operatorname{sgn}+\operatorname{St}_2.
\]

### 2. The case \(d>1\): the square is not enough

There is a nontrivial center-trivial linear character
\[
\lambda=\alpha\circ\det
\]
of \(G\), where \(\alpha\in\operatorname{Irr}(\mathbb F_q^\times)\) is nontrivial and
\(\alpha^n=1\).

The Steinberg character is self-dual, hence
\[
\langle \operatorname{St}_n^2,\lambda\rangle
=
\langle \operatorname{St}_n,\lambda\operatorname{St}_n\rangle.
\]
The two irreducible characters \(\operatorname{St}_n\) and
\(\lambda\operatorname{St}_n\) are distinct. Indeed choose \(a\in\mathbb F_q^\times\) with
\(\alpha(a)\ne1\) and put
\[
x=\operatorname{diag}(a,1,\ldots,1).
\]
The element \(x\) is semisimple, so the Steinberg value \(\operatorname{St}_n(x)\) is nonzero,
whereas
\[
(\lambda\operatorname{St}_n)(x)
=
\alpha(a)\operatorname{St}_n(x)
\ne
\operatorname{St}_n(x).
\]
Thus
\[
\langle \operatorname{St}_n^2,\lambda\rangle=0.
\]
Consequently the covering number is at least \(3\).

### 3. The cube contains every center-trivial linear character

Let \(\lambda\) be any center-trivial linear character of \(G\). Then
\(\lambda\operatorname{St}_n\) is nonlinear, irreducible, and center-trivial. By the
Monteiro--Stasinski nonlinear-coverage theorem,
\[
\lambda\operatorname{St}_n\subseteq \operatorname{St}_n^2.
\]
Therefore
\[
\langle \operatorname{St}_n^3,\lambda\rangle
=
\langle \operatorname{St}_n^2,\lambda\operatorname{St}_n\rangle>0.
\]

### 4. The cube contains every center-trivial nonlinear character

Let \(\chi\) be center-trivial and nonlinear. Since \(d>1\), we are not in the exceptional
case \(\operatorname{GL}_2(2)\), and
\[
[G,G]=\operatorname{SL}_n(q),\qquad
G/\operatorname{SL}_n(q)\cong\mathbb F_q^\times
\]
is cyclic.

Suppose every irreducible constituent of
\(\chi\operatorname{St}_n\) were linear. Every linear character of \(G\) is trivial on
\(\operatorname{SL}_n(q)\), so the tensor-product representation
\(\rho_\chi\otimes\rho_{\operatorname{St}}\) would be trivial on
\(\operatorname{SL}_n(q)\). Hence for every \(s\in\operatorname{SL}_n(q)\),
\[
\rho_\chi(s)\otimes\rho_{\operatorname{St}}(s)=I.
\]
The elementary tensor-scalar lemma used above forces
\(\rho_{\operatorname{St}}(s)\) to be scalar for all \(s\in\operatorname{SL}_n(q)\).
Since the quotient by \(\operatorname{SL}_n(q)\) is cyclic, the image of the Steinberg
representation would then be abelian, contradicting its irreducibility and dimension
\[
\operatorname{St}_n(1)=q^{n(n-1)/2}>1.
\]

Thus \(\chi\operatorname{St}_n\) has a nonlinear constituent \(\psi\). Its central character
is trivial, so Monteiro--Stasinski give
\[
\psi\subseteq\operatorname{St}_n^2.
\]
Self-duality again yields
\[
\langle\operatorname{St}_n^3,\chi\rangle
=
\langle\operatorname{St}_n^2,\chi\operatorname{St}_n\rangle>0.
\]

Together with the linear case, every center-trivial irreducible occurs in the cube. Since the
square misses a nontrivial center-trivial linear character when \(d>1\),
\[
c(\operatorname{St}_n)=3.
\]
This completes the proof. \(\square\)

## Small example

For \(G=\operatorname{GL}_2(3)\), the quotient by the center is
\[
\operatorname{PGL}_2(3)\cong S_4,
\qquad
d=\gcd(2,2)=2.
\]
The descended Steinberg character is a three-dimensional irreducible character. Its square
contains the trivial character and all nonlinear irreducibles of \(S_4\), but misses the
nontrivial linear character. The theorem says its cube contains every irreducible of \(S_4\),
so its covering number is exactly \(3\).

## Originality and limitations

The 2013 theorem of Heide--Saxl--Tiep--Zalesski proves Steinberg-square universality for
finite simple groups of Lie type, subject to their stated unitary exceptions. In the present
family, this covers the \(d=1\) projective-special-linear case.

Monteiro--Stasinski's September 2026 preprint is the direct recent source: it proves that the
Steinberg square contains every nonlinear center-trivial irreducible of
\(\operatorname{GL}_n(q)\), observes that the square can miss linear characters, and constructs
a different irreducible character whose square covers all center-trivial irreducibles.

Targeted searches for “Steinberg cube”, “third tensor power”, “covering number of the
Steinberg character”, and equivalent \(\operatorname{PGL}_n(q)\) formulations found the
simple-group Steinberg-square literature and the new Monteiro--Stasinski paper, but no
statement of the exact \(2/3\) covering-number formula above or the cyclic-abelianization
completion lemma.

The contribution claimed here is deliberately narrow: the recent nonlinear-coverage theorem
is not new, Steinberg self-duality and semisimple character values are standard, and no new
decomposition multiplicities are claimed. The new statement is the exact covering number of
the Steinberg character for \(\operatorname{PGL}_n(q)\), together with the general
cube-completion mechanism proving it.

Because arXiv:2609.17319 is a very recent v1 preprint, a concurrent revision or independent
observation is a realistic residual originality risk. The search cannot exclude unpublished
notes or all formulations in the older character-covering literature.

## References

1. N. Monteiro and A. Stasinski, *A tensor square theorem for characters of
   \(\operatorname{GL}_n(q)\)*, arXiv:2609.17319v1, submitted 15 September 2026.
   https://arxiv.org/abs/2609.17319

2. G. Heide, J. Saxl, P. H. Tiep, and A. E. Zalesski, *Conjugacy action, induced
   representations and the Steinberg square for simple groups of Lie type*,
   Proc. London Math. Soc. 106 (2013), 908--930; arXiv:1209.1768.
   https://arxiv.org/abs/1209.1768

3. R. Kundu and V. S., *Covering Numbers of Some Irreducible Characters of the
   Symmetric Group*, Electron. J. Combin. 32 (2025), #P2.56.
   https://doi.org/10.37236/13289
