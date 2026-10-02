# Exact tenth-power stable obstruction set via a numerical semigroup

## Corrected main result

Let \(\mathbf B^k\) be the stabilized positive-offset obstruction set for representations by exactly \(j\) positive \(k\)-th powers. For \(k=10\),

\[
\mathbf B^{10}=\mathbb Z_{>0}\setminus\langle 1023,59048,25937424600\rangle.
\]

Therefore

\[
a_{10}=259379677393,\qquad b_{10}=129689838697,\qquad a_{10}=2b_{10}-1.
\]

The semigroup is symmetric, so for \(0\le n\le a_{10}\), with \(0\notin\mathbf B^{10}\),

\[
n\in\mathbf B^{10}\quad\Longleftrightarrow\quad a_{10}-n\notin\mathbf B^{10}.
\]

These are exact exponent-10 symmetry identities. They are **not** cases of Benfield--Lippard Conjectures 10.1 or 10.2: those conjectures are stated for exponents of the form \(2^j\), and \(10\) is not such an exponent. Since both \(a_{10}\) and \(b_{10}\) are odd, the result does give the exponent-10 case of their Conjecture 10.4.

Benfield--Lippard prove only the lower bound \(|\mathbf B^{10}|\ge129687123005\); the exact value here is larger by \(2715692\).

## Stable offsets are numerical-semigroup gaps

Define

\[
\Gamma_k=\langle m^k-1:m\ge2\rangle\subseteq\mathbb Z_{\ge0}.
\]

A positive offset \(b\) satisfies

\[
j+b=\sum_{i=1}^j x_i^k
\]

if and only if \(b\) is a sum of at most \(j\) nonzero generators \(x_i^k-1\); extra summands \(1^k\) contribute zero. Thus the stabilized obstruction set is exactly the positive gap set of \(\Gamma_k\). No originality claim is made for this general reformulation.

## Reduction at exponent ten

Let

\[
T=\langle93,5368\rangle,\qquad C=11^{10}-1=25937424600.
\]

The first two generators satisfy \(2^{10}-1=11\cdot93\) and \(3^{10}-1=11\cdot5368\). Since \(\gcd(93,5368)=1\),

\[
F(T)=93\cdot5368-93-5368=493763,
\]

and

\[
g(T)=\frac{(93-1)(5368-1)}2=246882.
\]

We claim

\[
\Gamma_{10}=11T+C\mathbb Z_{\ge0}=\langle1023,59048,C\rangle.
\]

If \(11\nmid m\), Fermat's theorem gives \(11\mid m^{10}-1\). For \(m=4\),

\[
\frac{4^{10}-1}{11}=95325=1025\cdot93\in T.
\]

For every \(m\ge5\) with \(11\nmid m\),

\[
\frac{m^{10}-1}{11}\ge887784>F(T),
\]

so the quotient is in \(T\). If \(m=11r\), then \(m=11\) gives \(C\), while for \(r\ge2\),

\[
m^{10}-1=C+11\bigl(11^9(r^{10}-1)\bigr),
\]

and the parenthesized integer exceeds \(F(T)\), hence lies in \(T\). The reverse containment is immediate from the three displayed original generators.

Also

\[
C=93\cdot278893056+5368\cdot69\in T,
\]

and \(C\equiv-1\pmod{11}\). Every \(N\ge0\) has a unique representation

\[
N=rC+11z,\qquad 0\le r\le10,\quad z\in\mathbb Z,
\]

and the preceding reduction gives

\[
N\in\Gamma_{10}\quad\Longleftrightarrow\quad z\in T.
\]

## Frobenius number, genus and symmetry

In residue class \(r\), the largest nonnegative-\(z\) gap is \(rC+11F(T)\), so

\[
a_{10}=10C+11F(T)=259379677393.
\]

The eleven residue classes contribute \(11g(T)\) gaps with \(z\ge0\). For \(1\le r\le10\), positive integers with \(z<0\) contribute

\[
\left\lfloor\frac{rC}{11}\right\rfloor.
\]

Because \(C\) is coprime to \(11\),

\[
\sum_{r=1}^{10}\left\lfloor\frac{rC}{11}\right\rfloor=5(C-1)=129687122995.
\]

Hence

\[
b_{10}=11\cdot246882+129687122995=129689838697,
\]

and \(2b_{10}-1=a_{10}\).

Finally, the two-generator semigroup \(T\) is symmetric. Under \(N=rC+11z\),

\[
a_{10}-N=(10-r)C+11(F(T)-z),
\]

so symmetry transfers residue by residue to \(\Gamma_{10}\), proving the complement relation.

## Verification and scope

`artifacts/verify.py` independently enumerates \(T\) through its Frobenius number, checks the small generator reductions and an explicit representation of \(C\), verifies the first 500 original generators against the reduction, evaluates the genus formula, and checks symmetry. `artifacts/verify-output.txt` records that execution. These finite checks are supplementary; the result above is proved symbolically.

The exact exponent-10 reduction and invariants are claimed to the best of our knowledge. A separate published result gives the general stable-offset numerical-semigroup reformulation and repairs a modular lower-bound argument, but does not determine these exact exponent-10 values. Zenkin's 1995 full text was inspected; it develops the generalized Waring framework and stabilized exception sets but does not state the exact exponent-10 semigroup calculation above. No claim is made about Benfield--Lippard Conjectures 10.1 or 10.2, about all even exponents, or about the stabilization index \(g(1,10)\).

## References

1. Brennan Benfield and Oliver Lippard, *Integers that are not the sum of positive powers*, arXiv:2404.08193v2 (2025).
2. A. A. Zenkin, *The generalized Waring problem: A new property of positive integers*, Mathematical Notes 58 (1995), 933--937.
