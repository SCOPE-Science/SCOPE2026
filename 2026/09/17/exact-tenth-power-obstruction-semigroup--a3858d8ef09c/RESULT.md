# Exact tenth-power stable obstruction set via a numerical semigroup

## Main result

Let \(\mathbf B^k\) be the stabilized set of positive offsets used by Benfield and Lippard for integers that are not sums of exactly \(j\) positive \(k\)-th powers, and write

\[
a_k=\max \mathbf B^k,\qquad b_k=|\mathbf B^k|.
\]

For \(k=10\),

\[
\boxed{\mathbf B^{10}=\mathbb Z_{>0}\setminus
\langle 1023,59048,25937424600\rangle}.
\]

Consequently,

\[
\boxed{a_{10}=259379677393},\qquad
\boxed{b_{10}=129689838697}.
\]

In particular,

\[
a_{10}=2b_{10}-1.
\]

Thus the even-exponent symmetry relation conjectured in Conjecture 10.1 of Benfield--Lippard holds at exponent 10. The semigroup is symmetric, so for \(0\le n\le a_{10}\),

\[
n\in \mathbf B^{10}
\quad\Longleftrightarrow\quad
a_{10}-n\notin \mathbf B^{10},
\]

with the convention that \(0\notin\mathbf B^{10}\). This gives the exponent-10 case of their Conjecture 10.2 as well. Both \(a_{10}\) and \(b_{10}\) are odd, giving the exponent-10 case of Conjecture 10.4.

Benfield--Lippard proved only the lower bound

\[
|\mathbf B^{10}|\ge 129687123005
\]

(Corollary 10.8). The exact value above exceeds that lower bound by \(2715692\).

## Offset-semigroup lemma

For a fixed exponent \(k\), define the additive semigroup

\[
\Gamma_k=\langle m^k-1:m\ge2\rangle\subseteq\mathbb Z_{\ge0}.
\]

For a positive offset \(b\),

\[
j+b=\sum_{i=1}^j x_i^k\quad(x_i\ge1)
\]

if and only if

\[
b=\sum_{i=1}^j(x_i^k-1).
\]

Terms with \(x_i=1\) contribute zero. Therefore \(j+b\) is representable by exactly \(j\) positive \(k\)-th powers if and only if \(b\) has a factorization in \(\Gamma_k\) using at most \(j\) nonzero generators. It follows that every gap of \(\Gamma_k\) remains an obstruction for every \(j\), whereas every element of \(\Gamma_k\) eventually ceases to be an obstruction. Hence the stabilized offset set is precisely the positive gap set of \(\Gamma_k\).

This observation is used here as a reduction; no originality claim is made for the general semigroup reformulation itself.

## Reduction of \(\Gamma_{10}\)

Put

\[
T=\langle93,5368\rangle.
\]

The generators arise from

\[
2^{10}-1=11\cdot93,\qquad
3^{10}-1=11\cdot5368.
\]

Since \(\gcd(93,5368)=1\), Sylvester's formulas give

\[
F(T)=93\cdot5368-93-5368=493763
\]

and

\[
g(T)=\frac{(93-1)(5368-1)}2=246882,
\]

where \(F\) is the Frobenius number and \(g\) is the genus.

Let

\[
C=11^{10}-1=25937424600.
\]

We claim

\[
\Gamma_{10}
=\langle1023,59048,C\rangle
=11T+C\mathbb Z_{\ge0}.
\]

It suffices to reduce every generator \(m^{10}-1\).

### Case 1: \(11\nmid m\)

Fermat's little theorem gives \(11\mid m^{10}-1\), so write

\[
m^{10}-1=11q_m.
\]

For \(m=2,3\), the quotients are the two generators \(93,5368\). For \(m=4\),

\[
q_4=95325=1025\cdot93\in T.
\]

For every \(m\ge5\) with \(11\nmid m\),

\[
q_m\ge \frac{5^{10}-1}{11}
=887784>F(T),
\]

hence \(q_m\in T\). Thus every such generator belongs to \(11T\).

### Case 2: \(11\mid m\)

Write \(m=11r\). If \(r=1\), the generator is exactly \(C\). If \(r\ge2\), then

\[
m^{10}-1
=C+11\bigl(11^9(r^{10}-1)\bigr).
\]

The integer in parentheses is greater than \(F(T)\), so it lies in \(T\). Hence every generator with \(11\mid m\) lies in \(C+11T\).

The reverse containment is immediate because \(1023=2^{10}-1\), \(59048=3^{10}-1\), and \(C=11^{10}-1\) are original generators. This proves the claimed three-generator description.

## Canonical residue decomposition

The number \(C\) itself belongs to \(T\); for example,

\[
C=93\cdot278893056+5368\cdot69.
\]

Also \(C\equiv-1\pmod{11}\). Every integer \(N\ge0\) has a unique expression

\[
N=rC+11z,
\qquad 0\le r\le10,\ z\in\mathbb Z,
\]

obtained by choosing \(r\) from the residue class modulo 11. The three-generator description and \(C\in T\) imply

\[
N\in\Gamma_{10}
\quad\Longleftrightarrow\quad
z\in T.
\]

Indeed, one direction is immediate. Conversely, if
\(N=sC+11t\) with \(s\ge0\) and \(t\in T\), then
\(s=r+11q\) for some \(q\ge0\), and

\[
z=t+qC\in T.
\]

Thus the gaps of \(\Gamma_{10}\) split into 11 translated copies of the gap pattern of \(T\), together with the positive terms arising from negative \(z\) in the ten nonzero residue classes.

## Frobenius number

For a fixed \(r\), the largest gap with \(z\ge0\) is

\[
rC+11F(T).
\]

The negative-\(z\) gaps in that residue class are smaller than \(rC\), so the global maximum occurs at \(r=10\). Therefore

\[
a_{10}=F(\Gamma_{10})
=10C+11F(T)
=259379677393.
\]

## Genus

Each of the 11 residue classes contributes the \(g(T)=246882\) nonnegative-\(z\) gaps of \(T\). For \(1\le r\le10\), there are additionally

\[
\left\lfloor\frac{rC}{11}\right\rfloor
\]

positive integers with negative \(z\).

Because \(\gcd(C,11)=1\), the residues \(rC\bmod11\) for \(1\le r\le10\) are a permutation of \(1,\ldots,10\). Hence

\[
\sum_{r=1}^{10}
\left\lfloor\frac{rC}{11}\right\rfloor
=\frac{55C-55}{11}
=5(C-1)
=129687122995.
\]

It follows that

\[
b_{10}=g(\Gamma_{10})
=11\cdot246882+129687122995
=129689838697.
\]

Finally,

\[
2b_{10}-1=259379677393=a_{10}.
\]

## Symmetry

The two-generator semigroup \(T=\langle93,5368\rangle\) is symmetric. Under the canonical decomposition,

\[
N=rC+11z
\]

and

\[
a_{10}-N=(10-r)C+11(F(T)-z).
\]

The symmetry of \(T\) therefore transfers residue-by-residue to \(\Gamma_{10}\), proving the stated complement relation for \(\mathbf B^{10}\).

## Verification

`artifacts/verify.py` independently checks the two-generator Frobenius number and genus by finite enumeration through \(F(T)\), verifies the small-generator reductions, confirms an explicit representation of \(C\) in \(T\), checks the first 500 original generators against the reduction, evaluates the residue-class genus formula, and checks the symmetry of \(T\). Its recorded output is in `artifacts/verify-output.txt`.

The finite computation is supplemental; the theorem above is proved symbolically.

## Literature context and limitations

Benfield and Lippard determine \(\mathbf B^k\) for \(k\le9\), formulate the symmetry conjectures in Section 10.1, and for exponent 10 give only Corollary 10.8, the lower bound \(|\mathbf B^{10}|\ge129687123005\). Their current arXiv version is v2, revised 31 March 2025.

Searches for the exact values above, the three-generator semigroup
\(\langle1023,59048,25937424600\rangle\), the equivalent generators
\(2^{10}-1,3^{10}-1,11^{10}-1\), `B^10`, and follow-up work citing or naming the Benfield--Lippard problem did not locate an earlier exact determination. The originality claim is therefore to the best of our knowledge.

A. A. Zenkin's 1995 paper on the generalized Waring problem is directly relevant background and is cited by Benfield--Lippard. Only its bibliographic page and abstract were inspected here, not its subscription-only full text. Because Benfield--Lippard use Zenkin's framework while still recording only a lower bound for \(\mathbf B^{10}\), this is a limited but nonzero residual originality risk. The general offset-semigroup lemma above is therefore not asserted to be new; the originality claim concerns the exact exponent-10 reduction, invariants, and resulting resolution of the exponent-10 symmetry cases.

No claim is made about the full conjectures for all even exponents or about the stabilization index \(g(1,10)\).

## References

1. Brennan Benfield and Oliver Lippard, *Integers that are not the sum of positive powers*, arXiv:2404.08193v2 (2025). https://arxiv.org/abs/2404.08193
2. A. A. Zenkin, *The generalized Waring problem: A new property of positive integers*, Mathematical Notes 58 (1995), 933--937. https://doi.org/10.1007/BF02304770
3. Standard numerical-semigroup symmetry criterion and two-generator facts are reviewed, for example, in *The ideal duplication*, Semigroup Forum (2021). https://link.springer.com/article/10.1007/s00233-021-10201-1
