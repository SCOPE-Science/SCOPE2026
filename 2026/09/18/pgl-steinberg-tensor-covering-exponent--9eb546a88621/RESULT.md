# Exact Steinberg tensor covering exponent for \(\operatorname{PGL}_n(q)\)

## Statement

Let \(n\ge 2\), let \(q\) be a prime power, and put
\[
\overline G=\operatorname{PGL}_n(q)=\operatorname{GL}_n(q)/Z,
\qquad d=\gcd(n,q-1).
\]
Write \(\mathrm{St}\) for the Steinberg character, viewed as an irreducible character of \(\overline G\). For a character \(\theta\), write \(\operatorname{Irr}(\theta)\) for the set of its irreducible constituents.

**Theorem 1 (exact square defect and universal cube).**

1. If \((n,q)\ne(2,2)\), then
   \[
   \operatorname{Irr}(\mathrm{St}^2)
   =\operatorname{Irr}(\overline G)\setminus
   \bigl(\operatorname{Lin}(\overline G)\setminus\{1\}\bigr).
   \]
   In particular, \(\mathrm{St}^2\) misses exactly \(d-1\) irreducible characters, all linear.
2. For \((n,q)=(2,2)\), \(\overline G\cong S_3\) and \(\mathrm{St}^2\) contains every irreducible character.
3. For every \(n\ge2\) and every prime power \(q\),
   \[
   \boxed{\operatorname{Irr}(\mathrm{St}^3)=\operatorname{Irr}(\overline G).}
   \]
   Consequently \(\operatorname{Irr}(\mathrm{St}^r)=\operatorname{Irr}(\overline G)\) for every \(r\ge3\).

Define the **Steinberg tensor covering exponent**
\[
c_{\mathrm{St}}(\overline G)
 =\min\{r\ge1:\operatorname{Irr}(\mathrm{St}^r)=\operatorname{Irr}(\overline G)\}.
\]
Then
\[
\boxed{
 c_{\mathrm{St}}(\operatorname{PGL}_n(q))=
 \begin{cases}
 2,&\gcd(n,q-1)=1,\\
 3,&\gcd(n,q-1)>1.
 \end{cases}}
\]

The result gives an exact tensor-power boundary for the adjoint general linear groups: the Steinberg square fails precisely by the nontrivial linear characters, and one additional Steinberg factor always repairs the defect.

## Input from the recent tensor-square theorem

Monteiro and Stasinski prove that every nonlinear irreducible character of \(\operatorname{GL}_n(q)\) that is trivial on the center occurs in \(\mathrm{St}^2\). Equivalently, every nonlinear irreducible character of \(\overline G\) occurs in \(\mathrm{St}^2\). Their proof combines a restriction theorem for the diagonal torus with a Deligne--Lusztig formula for the Steinberg square.

They also show that, except for \(\operatorname{GL}_2(2)\), the linear characters of \(\operatorname{GL}_n(q)\) trivial on the center form a cyclic group of order \(d=\gcd(n,q-1)\). Thus \(\overline G\) has exactly \(d\) linear characters in the nonexceptional cases. Their Theorem 3.4 uses a different irreducible character \(\sigma\) to make the square cover all center-trivial irreducibles when the Steinberg square alone does not.

## Proof of Theorem 1

### Step 1: the exact support of the square

The trivial character occurs in \(\mathrm{St}^2\): the Steinberg character is self-dual, so
\[
\langle \mathrm{St}^2,1\rangle
 =\langle \mathrm{St},\mathrm{St}\rangle=1.
\]
By the theorem of Monteiro--Stasinski recalled above, every nonlinear irreducible character of \(\overline G\) also occurs in \(\mathrm{St}^2\).

It remains to determine the nontrivial linear characters. Assume \((n,q)\ne(2,2)\), and let \(\lambda\ne1\) be linear on \(\overline G\). Inflating to \(\operatorname{GL}_n(q)\), write \(\lambda=\varepsilon\circ\det\), where \(\varepsilon\) is a nontrivial character of \(\mathbb F_q^\times\) satisfying the central-triviality condition. Since \(\mathrm{St}\) is self-dual,
\[
\langle \lambda,\mathrm{St}^2\rangle
 =\langle \lambda\mathrm{St},\mathrm{St}\rangle.
\]
The character \(\lambda\mathrm{St}\) is irreducible. It is not equal to \(\mathrm{St}\): choose \(a\in\mathbb F_q^\times\) with \(\varepsilon(a)\ne1\) and put
\[
x=\operatorname{diag}(a,1,\ldots,1).
\]
The element \(x\) is semisimple and the standard Steinberg value formula gives \(\mathrm{St}(x)\ne0\). Hence
\[
(\lambda\mathrm{St})(x)=\varepsilon(a)\mathrm{St}(x)\ne\mathrm{St}(x).
\]
Therefore
\[
\langle \lambda,\mathrm{St}^2\rangle=0.
\]
Thus the only constituents missing from \(\mathrm{St}^2\) are the nontrivial linear characters. Their number is \(d-1\).

For \((n,q)=(2,2)\), \(\overline G\cong S_3\) and \(\mathrm{St}\) is its irreducible character of degree \(2\). The familiar decomposition
\[
\mathrm{St}^2=1+\operatorname{sgn}+\mathrm{St}
\]
shows that the square already has full support. This is also the exceptional direct check recorded in the recent tensor-square paper.

### Step 2: a degree obstruction forces the cube to be full

The case \((n,q)=(2,2)\) is immediate from the full square, so assume otherwise. Let
\[
\mathcal L=\operatorname{Lin}(\overline G)\setminus\{1\};
\qquad |\mathcal L|=d-1.
\]
Suppose, for contradiction, that some \(\chi\in\operatorname{Irr}(\overline G)\) does not occur in \(\mathrm{St}^3\). By self-duality of \(\mathrm{St}\),
\[
0=\langle\chi,\mathrm{St}^3\rangle
 =\langle\chi\mathrm{St},\mathrm{St}^2\rangle.
\]
All multiplicities are nonnegative, while Step 1 says that \(\mathrm{St}^2\) contains every irreducible character outside \(\mathcal L\). Hence every irreducible constituent of \(\chi\mathrm{St}\) would have to belong to \(\mathcal L\).

For \(\lambda\in\mathcal L\), tensor reciprocity gives
\[
[\chi\mathrm{St}:\lambda]
 =\langle\chi,\lambda\mathrm{St}\rangle.
\]
Because \(\lambda\mathrm{St}\) is irreducible, this multiplicity is either \(0\) or \(1\). Consequently,
\[
\chi(1)\mathrm{St}(1)
 =\sum_{\lambda\in\mathcal L}[\chi\mathrm{St}:\lambda]
 \le d-1.
\]
But
\[
\mathrm{St}(1)=q^{n(n-1)/2}\ge q,
\qquad d=\gcd(n,q-1)\le q-1,
\]
so
\[
\chi(1)\mathrm{St}(1)\ge q>d-1,
\]
a contradiction. Therefore every \(\chi\in\operatorname{Irr}(\overline G)\) occurs in \(\mathrm{St}^3\).

If \(\mathrm{St}^r\) has full support for some \(r\ge3\), then for any irreducible \(\chi\),
\[
\langle\chi,\mathrm{St}^{r+1}\rangle
 =\langle\chi\mathrm{St},\mathrm{St}^r\rangle>0,
\]
because \(\chi\mathrm{St}\) is a nonzero character and every one of its irreducible constituents occurs in \(\mathrm{St}^r\). Hence all higher powers also have full support.

### Step 3: exactness of the covering exponent

The Steinberg character alone does not contain the trivial character, so the covering exponent is at least \(2\). If \(d=1\), the square has full support: this follows from Step 1 outside the exceptional pair, and from the direct \(S_3\) computation when \((n,q)=(2,2)\). Thus \(c_{\mathrm{St}}=2\).

If \(d>1\), Step 1 exhibits \(d-1\) missing linear characters in the square, whereas Step 2 shows that the cube has full support. Hence \(c_{\mathrm{St}}=3\).

## A twisted Steinberg corollary for \(\operatorname{GL}_n(q)\)

Let \(G=\operatorname{GL}_n(q)\) and let \(\eta\) be any linear character of \(G\). For every \(r\ge3\),
\[
(\eta\mathrm{St})^r=\eta^r\mathrm{St}^r.
\]
Since \(\mathrm{St}^r\) contains every irreducible character trivial on \(Z(G)\), twisting gives the exact central-character fiber
\[
\boxed{
\operatorname{Irr}((\eta\mathrm{St})^r)
 =\{\rho\in\operatorname{Irr}(G):
 \rho|_{Z(G)}=\rho(1)\,\eta^r|_{Z(G)}\}.
}
\]
Thus every tensor power \(r\ge3\) of a linear twist of Steinberg fills the entire central-character fiber permitted by the center.

## Relation to prior work

Heide, Saxl, Tiep and Zalesski proved in 2013 that the Steinberg square contains every irreducible character for finite simple groups of Lie type, apart from a specified unitary family. That theorem applies in particular to the simple \(\operatorname{PSL}_n(q)\) cases and explains the \(d=1\) side of the present boundary, but it does not address the nonsimple adjoint groups \(\operatorname{PGL}_n(q)\) when \(d>1\).

Monteiro and Stasinski (arXiv:2609.17319v1) prove the decisive new square input: \(\mathrm{St}^2\) contains every nonlinear irreducible character of \(\operatorname{GL}_n(q)\) trivial on the center. They explicitly note that the Steinberg square can miss center-trivial linear characters and replace it by a different irreducible character \(\sigma\) whose square has complete center-trivial support. The exact support of the Steinberg square, the universal Steinberg-cube theorem, and the resulting \(2/3\) covering-exponent dichotomy are not stated there.

The classical character-covering-number literature studies a different invariant, requiring a uniform tensor-power bound for every nontrivial irreducible character of a group. In particular, that invariant is finite only for nonabelian simple groups. The invariant here fixes the Steinberg character, so it remains meaningful for nonsimple \(\operatorname{PGL}_n(q)\). Recent work on \(\operatorname{PSL}_2(q)\) likewise studies covering by powers of arbitrary nontrivial irreducibles rather than the exact Steinberg exponent for \(\operatorname{PGL}_n(q)\).

## Limitations and originality

Originality is asserted only to the best of our knowledge. Searches for Steinberg tensor cubes/powers, \(\operatorname{PGL}_n(q)\) Steinberg covering, and equivalent constituent-covering formulations did not locate the exact theorem above. The strongest directly relevant sources inspected were the recent full text of arXiv:2609.17319v1, the 2013 Steinberg-square theorem for finite simple groups of Lie type, and the classical/recent character-covering-number literature.

The new argument is short once the square support theorem of Monteiro--Stasinski is available, so concurrent observation or an older equivalent statement under different terminology remains a realistic originality risk. No independent validation is asserted.

## References

1. N. Monteiro and A. Stasinski, *A tensor square theorem for characters of \(\operatorname{GL}_n(q)\)*, arXiv:2609.17319v1 (2026). https://arxiv.org/abs/2609.17319
2. G. Heide, J. Saxl, P. H. Tiep and A. E. Zalesski, *Conjugacy action, induced representations and the Steinberg square for simple groups of Lie type*, Proc. London Math. Soc. 106 (2013), 908--930. https://doi.org/10.1112/plms/pds062
3. Z. Arad, D. Chillag and M. Herzog, *Powers of characters of finite groups*, J. Algebra 103 (1986), 167--178.
4. N. Arvind and S. Panja, *Character Covering Number of \(\operatorname{PSL}_2(q)\)*, arXiv:2402.10467 (2024). https://arxiv.org/abs/2402.10467
