# Exactly six symmetric semigroups from consecutive hexagonal triples

## Finding

For \(n\in\mathbb Z\) with \(n\ge2\), let \(H_n=n(2n-1)\), and put
\[
S_n=\langle H_n,H_{n+1},H_{n+2}\rangle
=\{uH_n+vH_{n+1}+wH_{n+2}:u,v,w\in\mathbb N_0\}.
\]
**Theorem.** The numerical semigroup \(S_n\) is symmetric exactly for
\[
\boxed{n\in\{2,3,6,7,8,18\}.}
\]
In particular the last symmetric member is \(S_{18}\): every \(n\ge19\) is nonsymmetric. This is an exact all-index classification, not a bounded search conjecture.

## Assumptions and scope

The index \(n\) ranges over all integers \(n\ge2\); the generators are the *ordinary hexagonal numbers*, not centered hexagonal numbers. A numerical semigroup \(S\subseteq\mathbb N_0\) is **symmetric** if its Frobenius number \(F=\max(\mathbb N_0\setminus S)\) has the property that each gap \(z\) satisfies \(F-z\in S\). This is equivalent to the genus equation \(2\,g(S)=F+1\), where \(g(S)=|\mathbb N_0\setminus S|\).

For a minimally three-generated numerical semigroup \(\langle a,b,c\rangle\), the classical criterion recalled in García-Sánchez--Llena--Moscariello [2, p. 13] says it is symmetric if and only if one of the three generator pairs has gcd \(d>1\), and the remaining generator is a nonnegative integer combination of the members of that pair divided by \(d\), with the nonredundancy restriction from the minimal-generator assumption. This is used only for minimal triples. Every two-generated numerical semigroup with coprime generators is symmetric.

## Proof

**1. Generator gcds and minimality.** Write
\[
a=H_n=2n^2-n,\qquad b=H_{n+1}=2n^2+3n+1,\qquad c=H_{n+2}=2n^2+7n+6.
\]
Here \(a<b<c\), \(b-a=4n+1\), \(c-b=4n+5\), and \(c-a=8n+6\). Since each of the two factors in each \(H_j=j(2j-1)\) is coprime to the other, cross-factor Euclidean gcd computations give
\[
\gcd(a,b)=\gcd(2n-1,3),\qquad
\gcd(b,c)=\gcd(2n+1,3),
\]
\[
\gcd(a,c)=\gcd(n,2)\gcd(n,3)\gcd(2n-1,5)\le30.
\]
In the last formula the unused cross term is \(\gcd(2n-1,2n+3)=1\). If \(\gcd(a,b)=3\), then \(n\equiv2\pmod3\) and \(3\nmid c\); otherwise \(\gcd(a,b)=1\). Thus \(\gcd(a,b,c)=1\), so every \(S_n\) is numerical. For \(n\ge6\), \(c<2a\), making all three distinct generators minimal. Direct checks show minimality also at \(n=2,4,5\). At \(n=3\), \(c=45=3a\), so \(S_3=\langle15,28\rangle\) is two-generated and symmetric.

**2. Uniform obstruction for \(n\ge61\).** All four exact differences
\[
4a-3c=2n^2-25n-18,\qquad 3a-2c=2n^2-17n-12,
\]
\[
a-30(b-a)=2n^2-121n-30,\qquad
b-29(c-b)=2n^2-113n-144
\]
are strictly positive for every integer \(n\ge61\), as is seen at \(n=61\) and from their positive, increasing derivatives on that half-line. Also \(4n+3>60\).

If the pair \((a,b)\) has gcd greater than one, this gcd is \(3\). A putative representation \(c=x(a/3)+y(b/3)\) would give \(3c=xa+yb\) for nonnegative integers \(x,y\). If \(x+y\ge4\), the right side is at least \(4a>3c\); if \(x+y\le3\), it is at most \(3b<3c\). Both possibilities contradict the equation.

Similarly, if \(\gcd(b,c)>1\) then it equals \(3\); a putative \(a=x(b/3)+y(c/3)\) would give \(3a=xb+yc\). If \(x+y\ge3\), the right side is at least \(3b>3a\); if \(x+y\le2\), it is at most \(2c<3a\). Again impossible.

Finally set \(d=\gcd(a,c)\). Only \(2\le d\le30\) requires consideration. If \(b=x(a/d)+y(c/d)\), then \(db=xa+yc\). Positivity of the last two quadratic expressions above implies
\[
(d-1)c<db<(d+1)a.
\]
Therefore \(x+y=d\): sums below \(d\) are too small even using only \(c\), and sums above \(d\) are too large even using only \(a\). Solving with \(x+y=d\) yields
\[
x=\frac{d(c-b)}{c-a}=\frac d2+\frac d{4n+3}.
\]
Since \(0<d/(4n+3)<1/2\), this expression is strictly between two successive integers if \(d\) is odd (and strictly between an integer and the following half-integer if \(d\) is even); in either case it cannot be an integer. Thus the classical symmetry criterion fails for every \(n\ge61\).

**3. Exact finite closure.** The finitely many remaining indices \(2\le n\le60\) are checked by exhaustive integer arithmetic, with the independent Apéry-set check described below. For any pair \((u,v)\) having gcd \(d>1\), membership of the third generator \(w\) in \(\langle u/d,v/d\rangle\) is decided by ranging \(x\) over all integers \(0\le x\le\lfloor w/(u/d)\rfloor\), and testing whether \(w-x(u/d)\) is divisible by \(v/d\). There is no computational cutoff inside this exhaustive finite test. The nonminimal-generator case \(n=3\) is handled separately. Precisely the indices \(2,3,6,7,8,18\) pass.

For the five minimally three-generated survivors, the following are explicit divided-gcd witnesses (each identity is in ordinary integers):
\[
\begin{aligned}
n=2:\;&28=4(6/3)+4(15/3),\\
n=6:\;&91=1(66/6)+4(120/6),\\
n=7:\;&91=1(120/3)+1(153/3),\\
n=8:\;&153=8(120/10)+3(190/10),\\
n=18:\;&703=5(630/30)+23(780/30).
\end{aligned}
\]
These give sufficiency. All other indices in \([2,60]\) fail the exhaustive classical criterion, establishing necessity there. The uniform obstruction supplies necessity for \(n\ge61\). This completes the proof.

## Verification

Run the attached standalone Python 3 program \(\texttt{verify.py}\). Its exact-integer output is:

```text
EXACT_CERTIFICATE_OK indices=2,3,6,7,8,18 checked=2..60 independent_apery=59 oeis_F=29 universal_cutoff=61
```

The program checks all 59 finite indices by the three possible pair gcd conditions, and independently computes all 59 Frobenius numbers and genera through minimal residue representatives modulo \(a=H_n\). If \(w_r\) is the smallest semigroup member congruent to \(r\pmod a\), then
\[
F=\max_{0\le r<a}w_r-a,\qquad
2g=\frac{2}{a}\sum_{r=0}^{a-1}w_r-(a-1).
\]
It checks exactly \(2g=F+1\) for the six claimed cases and the strict failure for every other finite index. The 29 Frobenius numbers at \(n=2,\dots,30\) independently match OEIS A069758 [1]. The finite checks do not establish the all-index theorem by themselves; that part follows from Step 2.

## Relationship to prior work

OEIS A069758 [1] records Frobenius numbers for consecutive hexagonal triples, beginning with \(n=2\), not an all-index symmetry classification. García-Sánchez, Llena and Moscariello [2, p. 13] give the general characterization of symmetric minimally three-generated semigroups used here; they do not specialize it to the hexagonal family or determine its exceptional indices. Robles-Pérez and Rosales [3] analyze the different sequences of consecutive *triangular* and *tetrahedral* numbers. Pascadi [4, §5.5] likewise treats triangular and tetrahedral examples and states a general Apéry/genus method. In particular the established symmetric/free behavior of triangular triples does not transfer to hexagonal triples. The present calculation supplies an explicit sharp finite classification and a proof excluding every later hexagonal index.

## Limitations

No closed formula for the Frobenius number or genus at arbitrary nonsymmetric indices is asserted; no analogous classification for other polygonal shapes or longer generator blocks is claimed. General-purpose semigroup algorithms may independently decide a fixed index, but do not by themselves establish this uniform list. Searches of the cited literature and indexed related results cannot exclude unknown or unindexed prior derivations. The proof and program have not undergone independent external audit.

## References

1. V. A. Sapko, *Frobenius number of the numerical semigroup generated by three consecutive hexagonal numbers*, OEIS A069758 (entry dated April 8, 2002), https://oeis.org/A069758 .
2. P. A. García-Sánchez, D. Llena, A. Moscariello, *Delta sets for numerical semigroups with embedding dimension three*, arXiv:1504.02116 (April 8, 2015), especially p. 13, https://arxiv.org/pdf/1504.02116 .
3. A. M. Robles-Pérez, J. C. Rosales, *The Frobenius number for sequences of triangular and tetrahedral numbers*, arXiv:1706.04378 (June 14, 2017), https://arxiv.org/pdf/1706.04378 .
4. A. Pascadi, *A Graphical Approach to Finding the Frobenius Number, Genus and Hilbert Series of a Numerical Semigroup*, arXiv:1712.02522 (December 7, 2017), esp. §5.5, https://arxiv.org/html/1712.02522v3 .
