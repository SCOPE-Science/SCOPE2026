# The generalized packing–covering conjecture through redundancy fifteen

## Result

Let \(C\) be an \([n,k]_q\) linear code over an arbitrary finite field and let
\(\rho=n-k\le 15\). For every
\[
1\le t\le \min\{k,\rho\},
\]
the \(t\)-th generalized Hamming weight and generalized covering radius satisfy
\[
\boxed{d_t(C)\le 2R_t(C)+2.}
\]
Equivalently, the generalized packing radius
\[
\delta_t(C)=\left\lfloor\frac{d_t(C)-1}{2}\right\rfloor
\]
satisfies
\[
\delta_t(C)\le R_t(C).
\]

Essayag and Zabokritskiy proved the same statement uniformly through redundancy
\(14\), and identified the first binary parameter triple left open by their
reductions:
\[
\rho=15,\qquad t=3,\qquad R_3(C)=6,
\]
for which their dimension cap gives \(k\le 78\)
(arXiv:2609.19098v1, Section 6).  The theorem above closes exactly that next
redundancy level.

## The remaining binary case

Write \(r=R_t(C)\).  The reductions in arXiv:2609.19098 combine the known cases
\(t=1,2\), \(r=t\), \(t\ge \rho-4\), \(k\le 5t-2\),
\(3r\ge 2\rho\), the four auxiliary-code pairs
\[
(3,4),(3,5),(4,5),(4,6),
\]
and the large-alphabet case \(q\ge r\).  Under a hypothetical failure,
Lemma 4.1 of that paper gives
\[
k\le K(q,\rho,t,r)
\]
with
\[
K(q,\rho,t,r)=
\min_{a<h\le \rho}
\left\lfloor
\frac{(q^h-q^{h-a})h-b(q^h-1)}
     {q^{h-a}-1}
\right\rfloor,
\]
where
\[
a=\rho-2r+t-2,\qquad b=\rho-2r-1.
\]
Repeating the exact finite reduction at \(\rho=15\) leaves only
\[
(q,t,r)=(2,3,6).
\]
For this triple \(a=4\), \(b=2\), the minimum occurs at \(h=6\) and gives
\[
k\le 78.
\]
The supplied verification artifact reproduces this enumeration with exact
integer arithmetic.

Assume, for contradiction, that a binary \([n,k]\) counterexample exists with
\[
\rho=15,\qquad R_3(C)=6,\qquad d_3(C)\ge 15.
\]
The dual-weight step in Lemma 4.1 gives
\[
d_4(C^\perp)\ge n-13=k+2.
\]

Shorten \(C^\perp\) on nine independent coordinates of a generator matrix.
The resulting binary linear code \(D\) has dimension \(6\) and physical length
\[
N=n-9=k+6
\]
(allowing zero coordinates), while shortening preserves the support of every
surviving subcode.  Hence
\[
d_4(D)\ge k+2=N-4.
\]

The needed improvement over the averaging bound of Lemma 4.1 is the following
small finite-geometric fact.

## A binary six-dimensional weight lemma

**Lemma.** If a binary \([N,6]\) linear code \(D\) satisfies
\[
d_4(D)\ge N-4,
\]
then
\[
N\le 64.
\]

**Proof.**
Choose a full-rank \(6\times N\) generator matrix.  Let \(z\) be the number of
zero columns.  For each nonzero point
\[
p\in\mathbb F_2^6\setminus\{0\}
\]
let \(m_p\) be its column multiplicity, and put
\[
M=\sum_{p\ne0}m_p=N-z.
\]

A four-dimensional message subspace \(U\le\mathbb F_2^6\) gives a
four-dimensional subcode.  A nonzero column \(p\) is absent from its support
exactly when
\[
p\in U^\perp.
\]
Since \(U^\perp\) is two-dimensional, its three nonzero vectors form a
projective line of \(\operatorname{PG}(5,2)\).  Therefore the hypothesis
\(d_4(D)\ge N-4\) is equivalent to
\[
z+\sum_{p\in L}m_p\le 4
\qquad\text{for every projective line }L.
\tag{1}
\]

The space \(\operatorname{PG}(5,2)\) has \(63\) points and \(651\) lines, and
each point lies on \(31\) lines.  If \(z\ge1\), summing (1) over all lines gives
\[
31M\le 651(4-z)=31\cdot21(4-z),
\]
hence
\[
N=M+z\le 21(4-z)+z\le64.
\]

It remains to consider \(z=0\).  If some point \(p\) has \(m_p\ge3\), then the
other \(62\) points split into the \(31\) unordered pairs
\[
\{q,p+q\},
\]
one pair on each line through \(p\).  Equation (1) gives
\[
m_q+m_{p+q}\le 4-m_p\le1.
\]
Also \(m_p\le4\), so
\[
N=M\le m_p+31\le35.
\]

Otherwise every multiplicity is \(0,1\), or \(2\).  Let
\[
D_2=\{p:m_p=2\},\qquad Z_0=\{p:m_p=0\}.
\]
If \(D_2=\varnothing\), then \(N\le63\).  If \(D_2\ne\varnothing\), fix
\(p_0\in D_2\).  For every \(p\in D_2\setminus\{p_0\}\), the line
\(\{p_0,p,p_0+p\}\) and (1) force
\[
m_{p_0+p}=0.
\]
These points \(p_0+p\) are distinct, so
\[
|Z_0|\ge |D_2|-1.
\]
Consequently
\[
N=M=63+|D_2|-|Z_0|\le64.
\]
This proves the lemma. \(\square\)

Applying the lemma to the shortened dual gives
\[
k+6=N\le64,
\qquad\text{hence}\qquad
k\le58,\quad n=k+15\le73.
\]

## Final covering contradiction

For \(t=3\), \(q=2\), and \(R_3(C)=6\), the generalized ball-covering
inequality is
\[
V_8(n,6)\ge 2^{45},
\qquad
V_8(n,6)=\sum_{i=0}^{6}\binom ni 7^i.
\]
The left side is increasing in \(n\).  Exact evaluation at the largest possible
length gives
\[
V_8(73,6)
=
20\,282\,523\,983\,828
<
35\,184\,372\,088\,832
=
2^{45}.
\]
This contradicts the necessary covering inequality.  Thus the last
redundancy-\(15\) parameter triple cannot contain a counterexample, and the
generalized packing–covering conjecture holds for every linear code with
redundancy at most \(15\).

## Verification

`artifacts/verify_redundancy15.py` checks, with exact integers:

- the complete reduced parameter enumeration at \(\rho=15\), including that
  the sole tuple not removed by the previously used low-dimension/binomial
  tests is \((q,t,r)=(2,3,6)\) with \(K=78\);
- the \(63\)-point, \(651\)-line incidence counts of
  \(\operatorname{PG}(5,2)\);
- a sharp weight-\(64\) line-multiplicity example for the finite-geometric
  lemma's underlying inequality; and
- the exact final comparison \(V_8(73,6)<2^{45}\).

The computation is a reproducibility check; the theorem itself is proved
above.

## Originality and context

The generalized packing–covering conjecture and its established cases are not
new here.  In particular, Yu and Schwartz proved the second-order case and
several broad sufficient conditions, and Essayag and Zabokritskiy proved the
uniform redundancy-\(14\) theorem and the auxiliary/dimension-cap machinery
used above.

The new claim is the uniform extension from redundancy \(14\) to redundancy
\(15\), obtained by resolving the exact first parameter triple that
arXiv:2609.19098v1 leaves open.  Targeted searches for the redundancy-\(15\)
statement, the specific triple \((15,3,6)\), and equivalent generalized-weight
formulations did not locate prior coverage.  This claim is therefore only to
the best of our knowledge.  The motivating preprint is very recent, so a
near-simultaneous observation or a subsequent revision remains a material
priority risk.

## Limitations

This result advances the uniform redundancy threshold by one; it does not
settle the conjecture at redundancy \(16\) or in general.  The
six-dimensional lemma is specialized to the binary residual case and is not
claimed to be a new optimal theorem about arbitrary weight hierarchies outside
this application.  No algorithm for computing generalized covering radii is
provided.

## References

1. Isaac Barouch Essayag and Aryeh Lev Zabokritskiy (Yohananov),
   *Auxiliary Codes and the Generalized Packing–Covering Conjecture*,
   arXiv:2609.19098v1, 2026.
   https://arxiv.org/abs/2609.19098

2. Wenjun Yu and Moshe Schwartz,
   *On the Generalized Packing and Covering Radii of Codes*,
   arXiv:2609.14477, 2026.
   https://arxiv.org/abs/2609.14477
