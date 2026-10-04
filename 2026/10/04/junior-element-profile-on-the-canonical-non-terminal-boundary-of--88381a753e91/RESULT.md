# Junior-element profile on the canonical non-terminal boundary of two-heavy weighted projective spaces
## Finding
Let \(r\ge2\), let
\[
X_{r,a,b}=\mathbb P(1^r,a,b),\qquad 1\le a\le b,
\]
and suppose that \(X_{r,a,b}\) is canonical but not terminal. Write \(d=b-a\). The two heavy-coordinate affine charts are cyclic quotients
\[
\frac1a(1^r,b),\qquad \frac1b(1^r,a).
\]
For the first chart let \(j_a\) be the number of nonidentity group elements of Reid--Tai age exactly \(1\), and define \(j_b\) analogously for the second chart. Then the complete profile is as follows.

On the boundary family \(d=r\), so \((a,b)=(a,a+r)\) with \(1\le a\le2r\),
\[
(j_a,j_b)=
\begin{cases}
(0,1),&1\le a<r,\\
(1,2),&a=r,\\
(0,2),&r<a<2r,\\
(2,3),&a=2r.
\end{cases}
\]
On the other boundary family \(a=r+d\), after removing the intersection \(d=r\),
\[
(j_a,j_b)=
\begin{cases}
(1,1),&d=0,\\
(1,0),&1\le d<r.
\end{cases}
\]
Consequently, among the \(3r\) canonical non-terminal pairs, the total number
\[
J(X)=j_a+j_b
\]
has the exact distribution
\[
\#\{J=1\}=2r-2,\qquad
\#\{J=2\}=r,\qquad
\#\{J=3\}=1,\qquad
\#\{J=5\}=1.
\]
The unique \(J=3\) space is \(\mathbb P(1^r,r,2r)\), the unique \(J=5\) space is \(\mathbb P(1^r,2r,3r)\), and no canonical non-terminal member has \(J=4\). Summed over the whole boundary, the two heavy charts contain exactly
\[
4r+6
\]
local age-one elements.

## Assumptions and scope
The base field is \(\mathbb C\), \(r\ge2\), and the spaces are ordinary well-formed weighted projective spaces. Reid--Tai age is taken in the local finite cyclic quotient action on each heavy-coordinate affine chart. The count is a local chart count: if the same global divisorial valuation can be visible from overlapping toric charts, this statement does not identify or quotient such valuations. In particular, the theorem does not claim that \(4r+6\) is the number of distinct global crepant prime divisors over the projective variety.

For this family, the canonical region is
\[
0\le d\le r,\qquad 1\le a\le r+d,
\]
and terminality is obtained by making both inequalities strict. Thus the canonical non-terminal locus is exactly
\[
d=r\quad\text{or}\quad a=r+d,
\]
with the two boundary families meeting at \((a,b)=(2r,3r)\).

## Proof
For the \(a\)-chart, the element indexed by \(1\le k<a\) has age numerator
\[
N_a(k)=rk+[kb]_a=rk+[kd]_a,
\]
where \([u]_m\in\{0,\ldots,m-1\}\) denotes the least nonnegative residue. It has age one exactly when \(N_a(k)=a\). For the \(b\)-chart,
\[
N_b(k)=rk+[ka]_b=rk+[-kd]_b,
\]
and age one means \(N_b(k)=b\).

### The boundary \(d=r\)
Here \(b=a+r\). On the \(b\)-chart,
\[
N_b(k)=rk+[-rk]_b.
\]
If \(rk<b\), then \([-rk]_b=b-rk\), so \(N_b(k)=b\). If \(rk=b\), the residue is zero and equality still holds. If \(rk>b\), equality is impossible. Hence the junior indices are exactly
\[
1\le k\le \left\lfloor\frac br\right\rfloor
=1+\left\lfloor\frac ar\right\rfloor.
\]
Thus \(j_b=1\) for \(a<r\), \(j_b=2\) for \(r\le a<2r\), and \(j_b=3\) for \(a=2r\).

On the \(a\)-chart,
\[
N_a(k)=rk+[rk]_a.
\]
If \(rk<a\), then \(N_a(k)=2rk\), so equality requires \(a=2rk\). Since \(a\le2r\), this occurs only for \(a=2r,k=1\). If \(rk\ge a\), equality can occur only when \(rk=a\) and the residue vanishes. In the range \(a\le2r\), this gives \((a,k)=(r,1)\) and \((2r,2)\). Therefore \(j_a=1\) at \(a=r\), \(j_a=2\) at \(a=2r\), and \(j_a=0\) otherwise. Combining the two charts gives the first displayed profile.

### The boundary \(a=r+d\)
Now take \(0\le d<r\), so \(a=r+d\) and \(b=r+2d\). In the \(a\)-chart, \(k=1\) gives
\[
N_a(1)=r+d=a.
\]
For \(k\ge2\), if \(rk<a\), then \(kd<rk<a\) and
\[
N_a(k)=k(r+d)=ka>a.
\]
If \(rk\ge a\), equality would force \(rk=a\) and \([kd]_a=0\). For \(0<d<r\), the number \(a/r=1+d/r\) is not an integer, so this cannot happen; for \(d=0\), the only equality is already \(k=1\). Hence \(j_a=1\) throughout this boundary family away from the removed intersection.

On the \(b\)-chart, if \(0<d<r\) and \(rk<b\), then \(kd<rk<b\) and
\[
N_b(k)=rk+b-kd=b+k(r-d)>b.
\]
If \(rk\ge b\), equality is also impossible: when \(rk=b\), the residue \([-kd]_b=b-kd\) is positive, and when \(rk>b\) the first term already exceeds \(b\). Thus \(j_b=0\) for \(0<d<r\). At \(d=0\), both heavy charts have type \(\frac1r(1^r,0)\), and exactly \(k=1\) has age one, giving \((j_a,j_b)=(1,1)\).

The two boundary families contain \(2r\) and \(r+1\) pairs and intersect once. From the explicit chart profile, \(J=1\) occurs \((r-1)+(r-1)=2r-2\) times, \(J=2\) occurs \((r-1)+1=r\) times, and the two exceptional pairs \((r,2r)\) and \((2r,3r)\) give \(J=3\) and \(J=5\). The total is therefore
\[
(2r-2)+2r+3+5=4r+6.
\]

## Verification
The accompanying script `verify_junior_boundary.py` performs two independent finite replays. First, for every \(2\le r\le30\), it scans a box containing the entire canonical triangle, recomputes canonicity and terminality directly from every Reid--Tai group element in both heavy charts, and verifies both the boundary description and the asserted junior-index lists. Second, it checks the explicit boundary formulas directly through \(r=300\). It returns `VERIFY_OK`.

## Relationship to prior work
Kasprzyk gives general terminal/canonical criteria and classifications for weighted projective spaces, while Ghirlanda formulates canonicity and terminality of simplicial toric varieties directly in terms of the ages of elements in local class-group actions. These frameworks explain why age-one elements detect the canonical/non-terminal threshold, but the inspected sources do not state the two-heavy all-dimensional junior-element profile or the linear total \(4r+6\).

Targeted published-finding corpus searches for the exact family, junior/age-one elements, the distribution \((2r-2,r,1,1)\), and the total \(4r+6\) returned no equivalent record. The closest weighted-projective published-finding corpus hit concerned an unrelated four-dimensional reflexive-simplex \(h^*\)-inequality.

## Limitations
This is a refinement of the already established canonical/non-terminal boundary theorem for \(\mathbb P(1^r,a,b)\), not a classification of arbitrary weighted projective spaces. It counts local cyclic-group elements of age one in the two heavy charts and does not resolve identifications among global valuations or prove existence of a projective crepant resolution.

## References
- A. M. Kasprzyk, *Classifying terminal weighted projective space*, arXiv:1304.3029 (2013).
- M. Ghirlanda, *A canonicity criterion for toric varieties and the classification of canonical 4-simplices*, arXiv:2603.21198 (2026).
