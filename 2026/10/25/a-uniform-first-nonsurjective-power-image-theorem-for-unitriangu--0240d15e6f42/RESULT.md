# A uniform first-nonsurjective power-image theorem for unitriangular groups in every prime characteristic

## Finding

Let \(p\) be any prime, \(K\) any field of characteristic \(p\), and \(G=UT_{p+3}(K)\). Write a matrix with its first \(p-1\) superdiagonals zero as
\[
Y(u,v,w,s,t,z)=I+uE_{1,p+1}+vE_{2,p+2}+wE_{3,p+3}+sE_{1,p+2}+tE_{2,p+3}+zE_{1,p+3}.
\]
Then \(Y\) is a \(p\)-th power in \(G\) **if and only if**
\[
\big(v=0\ \text{and}\ uw=0\big)\quad\text{or}\quad
\big(v\ne0\ \text{and}\ (u,w)\ne(0,0)\big)\quad\text{or}\quad
\big(v\ne0,\ u=w=0,\ vz=st\big).
\]
Every \(p\)-th power has this prescribed upper-diagonal support. Consequently, if \(K=\mathbb F_q\) (with \(q\) any power of \(p\)), the number of distinct \(p\)-th powers is
\[
\boxed{|G^p|=q^6-q^5+q^4+q^3-q^2.}
\]
Exactly \(q^2(q-1)(q^2-1)\) elements of the six-dimensional subgroup \(G_p\) are not \(p\)-th powers, where \(G_p\) consists of matrices with their first \(p-1\) superdiagonals zero. The result is a uniform generalization to all primes of the previously known characteristic-two five-by-five criterion; neither the characteristic-two specialization nor the previously tabulated small-field numerical values are claimed as new.

## Assumptions and scope

The group \(UT_m(K)\) comprises upper-triangular \(m\)-by-\(m\) matrices with diagonal entries all equal to one. The matrices \(E_{i,j}\) are standard matrix units. For arbitrary \(p\ge2\), the six coordinates above are distinct and identify \(G_p\) with affine six-space as a set, although its group law need not be coordinatewise addition. Here \(G^p\) means the image set \(\{g^p:g\in G\}\), not a verbal subgroup, and \(|G^p|\) counts distinct images, not preimages.

## Proof

Write a source element as \(I+N\), with \(N\) strictly upper triangular of size \(p+3\). The binomial identity in characteristic \(p\) gives \((I+N)^p=I+N^p\). Every nonzero entry of \(N^p\) has displacement at least \(p\), hence lies in one of the six positions displayed in the finding. Its entries are sums over directed paths of exactly \(p\) positive-length jumps in the ordered vertex set \(\{1,\ldots,p+3\}\). Since the largest possible displacement is \(p+2\), only jumps of lengths one, two, and three can contribute.

Write \(a_i=N_{i,i+1}\) for \(1\le i\le p+2\), \(b_i=N_{i,i+2}\) for \(1\le i\le p+1\), and \(c_i=N_{i,i+3}\) for \(1\le i\le p\). Set unused entries zero when constructing witnesses. The length-\(p\) paths of displacement exactly \(p\) are unique, giving
\[
u=\prod_{i=1}^{p}a_i,\qquad v=\prod_{i=2}^{p+1}a_i,\qquad w=\prod_{i=3}^{p+2}a_i.
\]
If \(v=0\), then \(u\) and \(w\) cannot both be nonzero: otherwise both products would make every factor \(a_2,\ldots,a_{p+1}\) nonzero. If \(v\ne0\) but \(u=w=0\), the internal \(a_2,\ldots,a_{p+1}\) are nonzero and \(a_1=a_{p+2}=0\). The path sums then reduce to
\[
s=b_1\prod_{i=3}^{p+1}a_i,\qquad
t=b_{p+1}\prod_{i=2}^{p}a_i,\qquad
z=b_1b_{p+1}\prod_{i=3}^{p}a_i.
\]
Empty products are one. Therefore \(vz=st\). This proves all necessary restrictions.

We now explicitly construct a source for each permitted six-tuple. All unspecified \(a_i,b_i,c_i\) and all matrix entries above the third superdiagonal are set to zero. Whenever an unspecified intermediate value of \(z\) arises, denote it by \(z_0\).

**Case 1, \(v\ne0\).** Set \(a_2=v\), \(a_3=\cdots=a_{p+1}=1\), \(a_1=u/v\), \(a_{p+2}=w\), \(b_1=s\), and \(b_{p+1}=t/v\). These assignments give exactly the desired \(u,v,w,s,t\). If \(u=w=0\), the necessary identity already forces \(z=st/v\) and the chosen entries produce this \(z\). If \(u\ne0\), change \(c_p\) from zero to \((z-z_0)/(\prod_{i=1}^{p-1}a_i)\); its coefficient in the final entry is nonzero. Otherwise \(w\ne0\), and changing \(c_1\) to \((z-z_0)/(\prod_{i=4}^{p+2}a_i)\) adjusts precisely the final entry. Changes to these third-superdiagonal variables do not affect the five other target coordinates.

**Case 2, \(v=0\) and \(u\ne0\).** Then \(w=0\). Put \(a_1=u\), \(a_2=\cdots=a_p=1\), \(a_{p+1}=a_{p+2}=0\), \(b_p=s/u\), and \(b_{p+1}=t\). The five leading target values are as required. The coefficient of \(c_p\) in \(z\) is \(u\ne0\), so set \(c_p=(z-z_0)/u\). The symmetric case \(v=u=0\), \(w\ne0\) is obtained by reversing the matrix along its anti-diagonal: \(N_{i,j}\mapsto N_{p+4-j,p+4-i}\); this interchanges \(u\) with \(w\) and \(s\) with \(t\) while preserving \(v,z\) and all length-\(p\) path sums.

**Case 3, \(u=v=w=0\), \(s,t\ne0\).** When \(p=2\), put \(a_1=1\), \(a_4=t/s\), \(b_2=s\), \(c_2=z\). When \(p\ge3\), set all \(a_1,\ldots,a_{p+2}\) to one except \(a_3=0\) and \(a_{p+2}=t/s\), and put \(b_2=s\), \(c_2=zs/t\). In either subcase the target is \(Y(0,0,0,s,t,z)\) by the path formulas.

**Case 4, \(u=v=w=0\), \(s\ne0,t=0\).** Put every \(a_i=1\) except \(a_2=a_{p+2}=0\), and put \(b_1=s\), \(b_{p+1}=z/s\). The symmetric case \(s=0,t\ne0\) follows by anti-diagonal reflection.

**Case 5, \(u=v=w=s=t=0\).** Put \(a_4=\cdots=a_{p+2}=1\) and \(c_1=z\), with every other variable zero. All six target entries except the last vanish, and the last equals \(z\).

These cases exhaust the permitted parameter set and show sufficiency over every field, with no appeal to algebraic closure.

To count the complement when \(K=\mathbb F_q\), the obstruction \(v=0,\ uw\ne0\) contributes \((q-1)^2q^3\) forbidden tuples (free \(s,t,z\)). The obstruction \(v\ne0,\ u=w=0,\ vz\ne st\) contributes \((q-1)^2q^2\). Their sum is \(q^2(q-1)(q^2-1)\); subtracting it from \(q^6=|G_p|\) gives the stated polynomial.

## Verification

The standalone program `power_first_threshold_verify.cpp` enumerates all \(q^6\) possible six-coordinate targets, checks the image criterion, and constructs and directly evaluates an explicit source witness for each admitted target, for \((p,q)=(2,2),(2,4),(3,3),(5,5),(7,7)\). It additionally exhaustively enumerates all possible first-three-superdiagonal source parameters in the first three cases, independently checking that no forbidden target occurs. It uses a polynomial-basis implementation of \(\mathbb F_4\) and integer arithmetic for prime fields. The program outputs `VERIFY_OK_UNIFORM_P_POWER_FIRST_FAILURE` upon passing. Compile with `g++ -O2 -std=c++17 power_first_threshold_verify.cpp -o verify && ./verify`. These finite computations test, but do not replace, the universal path-counting proof.

## Relationship to prior work

Bier's unitriangular verbal-width work (2012), and Sosnovsky's publicly deposited 2012 study, establish classical power-width and first-nonsurjectivity thresholds; they do not state this complete uniform six-coordinate power-image criterion. Roman'kov--Menshov (2015) treat adjunction of roots in larger unitriangular groups, a distinct embedding problem. Dolfi--Singh--Yadav (2019) study the set of \(p\)-th powers and give bounds together with tabulated small-field images, including \(52\) for \((p,q)=(2,2)\), \(3376\) for \((2,4)\), and \(585\) for \((3,3)\). These finite values are already known, and an exact characteristic-two five-by-five six-coordinate membership criterion is also pre-existing: **the contribution here is the proof of the same closed six-coordinate criterion and polynomial uniformly for every prime \(p\), every characteristic-\(p\) field, and all finite-field extensions**. A less explicit or equivalent formulation may occur in older work; no claim of definitive historical priority is made.

## Limitations

No formula is asserted for numbers of individual \(p\)-th roots of a target, nor for dimensions other than \(p+3\). The theorem concerns the **set-theoretic image** of a power map, not its scheme-theoretic image or scheme fibers. The numerical count requires a finite field, while membership works over any field of the specified characteristic. The originality comparison does not eliminate the risk of earlier implicit equivalent formulas; independent mathematical review has not been performed.

## References

1. A. Bier, *The width of verbal subgroups in the group of unitriangular matrices over a field*, International Journal of Algebra and Computation 22 (2012), DOI: `10.1142/S0218196712500191`.
2. Yu. V. Sosnovsky, *On the Width of Verbal Subgroups of the Groups of Triangular Matrices over a Field of Arbitrary Characteristic*, arXiv:`1201.6513`, publicly posted 31 January 2012.
3. V. Roman'kov and A. Menshov, *Adjunction of roots to unitriangular groups over prime finite fields*, arXiv:`1506.02806` (2015).
4. S. Dolfi, A. Singh, and M. K. Yadav, *p-Power conjugacy classes in U(n,q) and T(n,q)*, arXiv:`1905.04244` (2019).
