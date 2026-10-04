# Exactly \(p^2\) fixed points for separated rank-two abelian \(p\)-groups

## Finding

Let \(p\) be a prime and
\[
A=C_{p^a}\oplus C_{p^b},
\qquad
1\le a<b,
\qquad
b-a\ge2.
\]
Write \(\theta(A,d)\) for the number of automorphisms of \(A\) fixing exactly \(d\) elements.

Except for the already computed boundary pair
\[
(a,b)=(1,3),
\]
the complete separated-exponent formula at the \(p^2\)-fixed-point layer is
\[
\boxed{
\theta(A,p^2)=
\begin{cases}
2p^{b-1}(p-1)^2,
& a=1,\ b\ge4,\\[4pt]
p^5(3p^3-6p^2+p+1),
& a=2,\ b=4,\\[4pt]
p^{b+2}(3p^2-7p+3),
& a=2,\ b\ge5,\\[4pt]
p^{3a+b-5}(p-1)(3p^2-4p-1),
& a\ge3,\ b=a+2,\\[4pt]
p^{3a+b-4}(p-1)(3p-5),
& a\ge3,\ b\ge a+3.
\end{cases}
}
\]

The exceptional separated pair \((a,b)=(1,3)\) is not part of the new claim. The known formula there is
\[
\theta(C_p\oplus C_{p^3},p^2)
=
p(2p^3-3p^2+1)
=
p(p-1)^2(2p+1),
\]
and the valuation method below recovers it as a consistency check.

## Assumptions and scope

Every automorphism of
\[
A=C_{p^a}\oplus C_{p^b},
\qquad a<b,
\]
has a unique matrix representation
\[
\varphi=
\begin{pmatrix}
\alpha&\beta\\
p^{b-a}\gamma&\delta
\end{pmatrix},
\]
where
\[
\alpha\in(\mathbf Z/p^a\mathbf Z)^\times,
\qquad
\beta,\gamma\in\mathbf Z/p^a\mathbf Z,
\qquad
\delta\in(\mathbf Z/p^b\mathbf Z)^\times.
\]

The theorem assumes the exponent gap
\[
h=b-a\ge2.
\]
Adjacent exponents \(b=a+1\) have additional low-valuation interactions and are not claimed here.

The theorem counts automorphisms, not merely the set of fixed-point cardinalities that can occur.

## Proof

Put
\[
u=\alpha-1,
\qquad
z=\delta-1,
\qquad
h=b-a,
\]
and
\[
D=uz-p^h\beta\gamma.
\]
Let
\[
T=\varphi-I.
\]
Because \(A\) is finite,
\[
|\ker T|=|\operatorname{coker}T|.
\]

A presentation of \(\operatorname{coker}T\) has relation columns
\[
\binom{p^a}{0},
\qquad
\binom{0}{p^b},
\qquad
\binom{u}{p^h\gamma},
\qquad
\binom{\beta}{z}.
\]
Therefore its order is the gcd of the \(2\times2\) minors of this relation matrix.

Let \(\nu=\nu_p\), with
\[
\nu(0)=\infty.
\]
Writing
\[
|\operatorname{Fix}(\varphi)|=p^\kappa,
\]
the minors give the exact formula
\[
\kappa
=
\min\{
a+b,\,
b+\nu(\gamma),\,
a+\nu(z),\,
b+\nu(u),\,
b+\nu(\beta),\,
\nu(D)
\}.
\]
Thus the problem is to count automorphism parameters for which
\[
\kappa=2.
\]

For a displacement \(u=\alpha-1\) modulo \(p^m\), where \(\alpha\) is a unit,
\[
|\{u:\nu(u)=0\}|=(p-2)p^{m-1},
\]
and for
\[
1\le j<m,
\]
\[
|\{u:\nu(u)=j\}|=(p-1)p^{m-j-1}.
\]
There is one further choice \(u=0\). The same formulas hold for \(z=\delta-1\).

We now count by the exponent gap.

### Case \(a=1\), \(b\ge4\)

Here
\[
h\ge3.
\]
The condition \(\kappa=2\) is equivalent to one of the two valuation patterns
\[
u=0,\quad \nu(z)=1,
\]
or
\[
\nu(u)=0,\quad \nu(z)=2.
\]
Both \(\beta\) and \(\gamma\) are arbitrary modulo \(p\). Hence
\[
\theta(A,p^2)
=
p^2\left(
(p-1)p^{b-2}
+
(p-2)(p-1)p^{b-3}
\right),
\]
so
\[
\theta(A,p^2)
=
2p^{b-1}(p-1)^2.
\]

For comparison, when \(b=3\), the lower power of \(p\) in the off-diagonal term changes the count to
\[
p(p-1)^2(2p+1),
\]
which is exactly the previously published \((1,3)\) formula.

### Case \(a=2\), \(b\ge5\)

Again
\[
h\ge3.
\]
The only valuation patterns giving \(\kappa=2\) are
\[
\nu(z)=0,\ u=0,
\]
\[
\nu(z)=1,\ \nu(u)=1,
\]
and
\[
\nu(z)=2,\ \nu(u)=0.
\]
Now \(\beta\) and \(\gamma\) are arbitrary modulo \(p^2\), so their combined contribution is \(p^4\). Summing the three patterns gives
\[
\theta(A,p^2)
=
p^{b+2}(3p^2-7p+3).
\]

### Case \(a=2\), \(b=4\)

Now
\[
h=2,
\]
so the term
\[
p^2\beta\gamma
\]
can cancel the valuation-two contribution of \(uz\).

When \(\nu(z)=0\), one must have \(u=0\), contributing
\[
(p-2)p^7.
\]

For \(\nu(z)\ge1\), first suppose
\[
\nu(u)+\nu(z)=2.
\]
The number of \((u,z)\)-pairs is
\[
p^2(p-1)(2p-3).
\]
After division by \(p^2\), the leading residue of \(uz\) is nonzero. Among the \(p^4\) pairs \((\beta,\gamma)\), the number for which \(\beta\gamma\) does not equal that fixed nonzero residue modulo \(p\) is
\[
p^2(p^2-p+1).
\]

If instead
\[
\nu(u)+\nu(z)>2,
\]
the number of \((u,z)\)-pairs is
\[
3p^2(p-1).
\]
To make \(D\) have valuation exactly \(2\), both \(\beta\) and \(\gamma\) must be nonzero modulo \(p\), giving
\[
p^2(p-1)^2
\]
choices.

Therefore
\[
\theta(A,p^2)
=
(p-2)p^7
+
p^4(p-1)(2p-3)(p^2-p+1)
+
3p^4(p-1)^3,
\]
which simplifies to
\[
\theta(A,p^2)
=
p^5(3p^3-6p^2+p+1).
\]

### Case \(a\ge3\), \(b\ge a+3\)

Here
\[
h\ge3.
\]
All presentation minors other than \(D\) have valuation at least \(3\), while
\[
D\equiv uz\pmod{p^3}.
\]
Hence
\[
\kappa=2
\]
if and only if
\[
\nu(u)+\nu(z)=2.
\]
The three possible patterns are
\[
(0,2),\quad(1,1),\quad(2,0).
\]
Their total number is
\[
p^{a+b-4}(p-1)(3p-5).
\]
The parameters \(\beta,\gamma\) contribute \(p^{2a}\), so
\[
\theta(A,p^2)
=
p^{3a+b-4}(p-1)(3p-5).
\]

### Case \(a\ge3\), \(b=a+2\)

Again
\[
h=2,
\]
so cancellation in
\[
D=uz-p^2\beta\gamma
\]
must be counted.

The number of allowed \((u,z)\)-pairs satisfying
\[
\nu(u)+\nu(z)=2
\]
is
\[
p^{a+b-4}(p-1)(3p-5),
\]
while the number satisfying
\[
\nu(u)+\nu(z)>2
\]
is
\[
p^{a+b-4}(4p-5).
\]

In the first class, the number of \((\beta,\gamma)\) for which the valuation-two terms do not cancel is
\[
p^{2a-2}(p^2-p+1).
\]
In the second class, both residues must be nonzero, giving
\[
p^{2a-2}(p-1)^2.
\]
Thus
\[
\theta(A,p^2)
=
p^{3a+b-6}
\left[
(p-1)(3p-5)(p^2-p+1)
+
(4p-5)(p-1)^2
\right].
\]
The bracket equals
\[
p(p-1)(3p^2-4p-1),
\]
so
\[
\theta(A,p^2)
=
p^{3a+b-5}(p-1)(3p^2-4p-1).
\]

This completes all separated-exponent cases outside the previously known pair \((1,3)\).

## Verification

The included checker independently enumerates the automorphism matrices for representatives of every branch:
\[
(p,a,b)
=
(2,1,4),
(3,1,4),
(2,2,4),
(3,2,4),
(2,2,5),
(3,2,5),
(2,3,5),
(2,3,6).
\]
For each automorphism it computes the fixed-subgroup order from the exact presentation minors and compares the resulting count with the stated formula.

For the three smallest examples it additionally evaluates the automorphism on every group element and directly counts fixed points, checking the presentation-minor computation itself.

The checker also evaluates the excluded boundary pair
\[
(a,b)=(1,3)
\]
and verifies the previously published formula
\[
p(2p^3-3p^2+1).
\]

The replay returns `VERIFY_OK`.

Finite enumeration is not used as the proof of the universal formulas.

## Relationship to prior work

The 2018 paper *Fixed Points of Automorphisms of Certain Non-Cyclic p-Groups and the Dihedral Group* defines \(\theta(G,d)\), determines every \(\theta\)-value for
\[
C_p\oplus C_{p^2},
\]
and gives the general fixed-point-free formula
\[
\theta(C_{p^a}\oplus C_{p^b},1)
=
p^{3a+b-2}(p-2)^2.
\]
It concludes by asking for \(\theta\)-values for direct sums of cyclic \(p\)-groups with distinct exponents.

Earlier work computes all \(\theta\)-values for
\[
C_p\oplus C_{p^3},
\]
including the \(p^2\)-fixed-point value used above as a boundary check.

A 2019 paper computes the complete table for
\[
C_{p^2}\oplus C_{p^3},
\]
an adjacent-exponent pair outside the scope of the theorem here.

The 2022 Reidemeister-spectrum classification for finite abelian groups determines which fixed-point cardinalities occur, but it does not count how many automorphisms realize each cardinality. Thus occurrence of \(p^2\) does not imply any of the multiplicity formulas above.

Targeted searches using the \(\theta\)-notation, exact fixed-point counts, rank-two abelian \(p\)-groups, separated exponents, and Reidemeister-spectrum terminology located the isolated low-exponent tables and the general fixed-point-free formula, but no separated-exponent \(p^2\)-multiplicity theorem.

## Limitations

The adjacent-exponent case
\[
b=a+1
\]
is not covered.

The pair
\[
(a,b)=(1,3)
\]
is deliberately excluded because its complete \(\theta\)-table was already published.

The theorem resolves only the \(p^2\)-fixed-point layer, not the full \(\theta\)-table for arbitrary
\[
C_{p^a}\oplus C_{p^b}.
\]

The literature search does not constitute a proof of novelty; an equivalent multiplicity formula could exist under different fixed-point or Reidemeister terminology.

## References

1. U. Hayat, D. López-Aguayo, and A. Abbas, “Fixed Points of Automorphisms of Certain Non-Cyclic p-Groups and the Dihedral Group,” *Symmetry* 10 (2018), 238, DOI 10.3390/sym10070238.
2. U. Hayat and F. Ali, “Fixed Points of Automorphisms of \(Z_p\times Z_{p^3}\),” *Journal of Mathematical Analysis* 7 (2016), 91–101.
3. F. Ali, U. Hayat, and Y. Li, “Fixed Points of Automorphisms of Certain Finite Groups,” *International Journal of Algebra* 13 (2019), 167–183, DOI 10.12988/ija.2019.9618.
4. P. Senden, “The Reidemeister spectrum of finite abelian groups,” arXiv:2205.15740v1, 31 May 2022.
