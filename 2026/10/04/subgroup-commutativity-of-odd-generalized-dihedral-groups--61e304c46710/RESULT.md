# Subgroup commutativity of odd generalized dihedral groups

## Finding

Let \(A\) be a nontrivial finite abelian group of odd order and let
\[
G=\operatorname{Dih}(A)=A\rtimes\langle t\rangle,
\qquad
tat=a^{-1}
\]
for every \(a\in A\). Write \(L(A)\) for the subgroup lattice and define
\[
\ell(A)=|L(A)|,
\qquad
\omega(A)=\sum_{B\le A}|A:B|,
\qquad
\eta(A)=\sum_{B,C\le A}|A:B\cap C|.
\]
Then the subgroup commutativity degree of \(G\) is
\[
\operatorname{sd}(G)
=
\frac{\ell(A)^2+2\ell(A)\omega(A)+\eta(A)}
     {(\ell(A)+\omega(A))^2}.
\]

For the elementary abelian kernel
\[
A\cong(C_p)^r
\]
with \(p\) an odd prime, put
\[
{n\brack k}_p
=
\prod_{h=0}^{k-1}
\frac{p^{n-h}-1}{p^{k-h}-1}.
\]
Then
\[
\ell_r(p)=\sum_{i=0}^r {r\brack i}_p,
\]
\[
\omega_r(p)=\sum_{i=0}^r {r\brack i}_p p^{r-i},
\]
and
\[
\eta_r(p)
=
\sum_{i=0}^r\sum_{j=0}^r
\sum_{k=\max(0,i+j-r)}^{\min(i,j)}
{r\brack i}_p
{i\brack k}_p
{r-i\brack j-k}_p
p^{(i-k)(j-k)+r-k}.
\]
Substitution in the first formula gives an exact finite expression for every \(p\) and \(r\).

There is a parity transition as \(p\to\infty\) with \(r\) fixed. In rank one,
\[
\operatorname{sd}(\operatorname{Dih}(C_p))
=
\frac{7p+9}{(p+3)^2}.
\]
For even rank \(r=2s\ge2\),
\[
\operatorname{sd}(\operatorname{Dih}((C_p)^r))
=
\frac14+O(p^{-1}),
\]
whereas for odd rank \(r=2s+1\ge3\),
\[
\operatorname{sd}(\operatorname{Dih}((C_p)^r))
=
\frac3p+O(p^{-2}).
\]
Thus, at fixed elementary-abelian rank, even ranks approach a nonzero subgroup-permutability probability while odd ranks at least three approach zero.

## Assumptions and scope

For a finite group \(H\), its subgroup commutativity degree is
\[
\operatorname{sd}(H)
=
\frac{|\{(U,V)\in L(H)^2:UV=VU\}|}{|L(H)|^2}.
\]
The products are ordered subgroup pairs.

The odd-order hypothesis on \(A\) is essential to the proof. It makes every quotient of \(A\) free of nontrivial \(2\)-torsion; this is exactly what converts the subgroup-permutability condition below into a single coset-incidence condition.

No claim is made here for generalized dihedral groups with even-order kernel.

## Proof

We write \(A\) additively. Every subgroup of \(G\) contained in \(A\) is simply a subgroup \(B\le A\). Every subgroup not contained in \(A\) has the form
\[
H(B,x)=B\rtimes\langle xt\rangle
\]
for some \(B\le A\) and some coset \(x+B\in A/B\). Conversely every such pair gives a subgroup, and two choices \(x,x'\) give the same subgroup exactly when
\[
x+B=x'+B.
\]
Hence the number of subgroups outside \(A\) is
\[
\sum_{B\le A}|A:B|=\omega(A),
\]
so
\[
|L(G)|=\ell(A)+\omega(A).
\]

Every subgroup \(B\le A\) is normal in \(G\): conjugation by \(A\) is trivial on \(A\), while \(t\) acts by inversion and therefore preserves \(B\). It follows that every ordered subgroup pair with at least one member contained in \(A\) is permutable. These contribute
\[
\ell(A)^2+2\ell(A)\omega(A)
\]
ordered pairs.

It remains to count pairs of subgroups outside \(A\). Let
\[
H=H(B,x),
\qquad
K=H(C,y),
\]
and put
\[
D=B+C.
\]
Using
\[
(a t)b=(a-b)t
\]
in additive notation, the product \(HK\) has \(A\)-part
\[
D\cup(x-y+D)
\]
and reflection part
\[
(x+D)t\cup(y+D)t.
\]
Similarly, \(KH\) has the same reflection part and \(A\)-part
\[
D\cup(y-x+D).
\]
Therefore \(HK=KH\) exactly when
\[
\{0,x-y+D\}=\{0,y-x+D\}
\]
in the quotient \(A/D\).

Because \(A/D\) has odd order, it has no nonzero element equal to its negative. Thus
\[
HK=KH
\quad\Longleftrightarrow\quad
x-y\in B+C.
\]

For fixed \(B,C\), count ordered pairs of cosets
\[
(x+B,y+C)\in A/B\times A/C
\]
whose images in \(A/(B+C)\) agree. Each fiber of
\[
A/B\longrightarrow A/(B+C)
\]
has size \(|B+C:B|\), and similarly for \(C\). The number of permuting ordered pairs is therefore
\[
|A:B+C|\,|B+C:B|\,|B+C:C|.
\]
Since
\[
|B+C|\,|B\cap C|=|B|\,|C|,
\]
this equals
\[
|A:B\cap C|.
\]
Summing over \(B,C\le A\) gives exactly \(\eta(A)\) permuting ordered pairs outside the kernel. Combining the three contributions proves
\[
\operatorname{sd}(G)
=
\frac{\ell(A)^2+2\ell(A)\omega(A)+\eta(A)}
     {(\ell(A)+\omega(A))^2}.
\]

Now assume
\[
A\cong(C_p)^r.
\]
Subgroups are vector subspaces of \(\mathbb F_p^r\). There are
\[
{r\brack i}_p
\]
subspaces of dimension \(i\), which immediately gives the displayed formulas for \(\ell_r(p)\) and \(\omega_r(p)\).

Fix subspaces \(B,C\) with
\[
\dim B=i,
\qquad
\dim C=j,
\qquad
\dim(B\cap C)=k.
\]
After \(B\) is chosen, the number of such \(C\) is
\[
{i\brack k}_p
{r-i\brack j-k}_p
p^{(i-k)(j-k)}.
\]
Since
\[
|A:B\cap C|=p^{r-k},
\]
summing over all feasible \(i,j,k\) gives the stated formula for \(\eta_r(p)\).

It remains to obtain the asymptotics. For fixed \(n,k\),
\[
{n\brack k}_p
=
p^{k(n-k)}(1+O(p^{-1})).
\]
Consequently, if \(r=2s\),
\[
\ell_r(p)\sim p^{s^2},
\qquad
\omega_r(p)\sim2p^{s(s+1)},
\]
while if \(r=2s+1\),
\[
\ell_r(p)\sim2p^{s(s+1)},
\qquad
\omega_r(p)\sim p^{(s+1)^2}.
\]

For \(\eta_r(p)\), set
\[
a=i-k,\qquad b=j-k.
\]
The exponent of \(p\) in the leading monomial of the corresponding summand is
\[
E_r(a,b,k)
=
r+a(r-k-a)+b(r-k-b)+k(r-k-1),
\]
under
\[
a,b,k\ge0,
\qquad
a+b+k\le r.
\]
For fixed \(k\), writing \(n=r-k\), the maximum of
\[
a(n-a)+b(n-b)
\]
subject to \(a+b\le n\) is
\[
\left\lfloor\frac{n^2}{2}\right\rfloor.
\]
The resulting maximum exponent for fixed \(k\) is
\[
r+\left\lfloor\frac{(r-k)^2}{2}\right\rfloor+k(r-k-1),
\]
which is strictly largest at \(k=0\).

If \(r=2s\), the unique maximizing triple is
\[
(i,j,k)=(s,s,0),
\]
so
\[
\eta_r(p)\sim p^{2s(s+1)}.
\]
Hence \(\eta_r(p)\) dominates the numerator and \(\omega_r(p)^2\) dominates the denominator, giving
\[
\operatorname{sd}(\operatorname{Dih}((C_p)^{2s}))
=
\frac14+O(p^{-1}).
\]

If \(r=2s+1\) with \(s\ge1\), the three maximizing triples are
\[
(s,s,0),\qquad
(s,s+1,0),\qquad
(s+1,s,0).
\]
Thus
\[
\eta_r(p)\sim3p^{2(s+1)^2-1}.
\]
Again the denominator is asymptotic to \(\omega_r(p)^2\), now of degree \(2(s+1)^2\), so
\[
\operatorname{sd}(\operatorname{Dih}((C_p)^{2s+1}))
=
\frac3p+O(p^{-2}).
\]

Finally, for \(r=1\),
\[
\ell_1(p)=2,\qquad
\omega_1(p)=p+1,\qquad
\eta_1(p)=3p+1.
\]
The general formula becomes
\[
\operatorname{sd}(\operatorname{Dih}(C_p))
=
\frac{7p+9}{(p+3)^2}.
\]

## Verification

The included replay constructs subgroup lattices for the odd abelian kernels
\[
C_3,\quad C_5,\quad C_9,\quad C_3\times C_3,
\]
builds every generalized-dihedral subgroup from the classification used in the proof, and directly tests the set equality \(HK=KH\) for every ordered subgroup pair.

The direct counts agree exactly with
\[
\ell(A)^2+2\ell(A)\omega(A)+\eta(A).
\]
The replay also evaluates the Gaussian-binomial formula independently for small ranks and primes and checks the rank-one closed form. It returns `VERIFY_OK`.

Finite experiments are not used as a proof of the universal formula or of the asymptotic statements.

## Relationship to prior work

Tărnăuceanu introduced subgroup commutativity degree and obtained explicit formulas for several standard finite-group families, including ordinary dihedral groups. Lazorec and Tărnăuceanu subsequently studied relative subgroup commutativity degrees and used the complete subgroup structure of ordinary dihedral groups in exact calculations.

The 2018 addendum develops relative subgroup commutativity degrees further and explicitly emphasizes exact computation for groups whose subgroup structure is known, while posing additional problems about the resulting subgroup-lattice probability functions.

The theorem above addresses a different family direction: the ordinary dihedral kernel is replaced by an arbitrary finite odd abelian group. The subgroup lattice then depends on the full lattice of \(A\), and the exact answer is encoded by the three natural lattice sums \(\ell(A)\), \(\omega(A)\), and \(\eta(A)\). For elementary abelian kernels, those sums reduce to Gaussian-binomial expressions and exhibit a parity-dependent asymptotic not present in the ordinary cyclic-kernel calculations inspected here.

A 2023 paper extending subgroup commutativity ideas to polygroups still cites the ordinary dihedral formulas as the standard explicit group examples. Its inspected full text does not state a generalized-dihedral formula.

## Limitations

The odd-order hypothesis is used decisively. If \(A/(B+C)\) contains nonzero \(2\)-torsion, two nonkernel subgroups may permute when the relevant coset has order \(2\), so the formula requires correction.

The elementary-abelian asymptotics keep the rank \(r\) fixed while \(p\) tends to infinity. They do not describe simultaneous growth of \(p\) and \(r\), nor fixed-\(p\) large-rank behavior.

The literature search did not locate the same generalized-dihedral formula or parity transition, but an equivalent statement could exist under different terminology or in an unindexed source.

## References

1. M.-S. Lazorec and M. Tărnăuceanu, “Finite groups with two relative subgroup commutativity degrees,” arXiv:1801.09133, first posted 27 January 2018.
2. M. Tărnăuceanu, “Addendum to ‘Subgroup commutativity degrees of finite groups’,” arXiv:1805.12156, first posted 21 May 2018.
3. M. Tărnăuceanu, “Subgroup commutativity degrees of finite groups,” *Journal of Algebra* 321 (2009), 2508–2520, DOI 10.1016/j.jalgebra.2009.02.010.
4. M. Al Tahan, S. Hoskova-Mayerova, B. Davvaz, and A. Sonea, “On subpolygroup commutativity degree of finite polygroups,” *AIMS Mathematics* 8 (2023), 23786–23799, DOI 10.3934/math.20231211.
