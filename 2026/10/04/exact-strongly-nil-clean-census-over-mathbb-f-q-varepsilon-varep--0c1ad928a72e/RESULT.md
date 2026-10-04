# Exact strongly nil-clean census over \(\mathbb F_q[\varepsilon]/(\varepsilon^2)\)
## Finding
Let \(q\) be a prime power, let \(n\ge 1\), and put
\[
R_q=\mathbb F_q[arepsilon]/(arepsilon^2).
\]
The exact number of strongly nil-clean matrices in \(M_n(R_q)\) is
\[
N_n(q)=\sum_{r=0}^n {nrack r}_q\,q^{2n^2-n-r(n-r)}.
\]
Equivalently, their density among all \(q^{2n^2}\) matrices is
\[
q^{-n}\sum_{r=0}^n {nrack r}_q q^{-r(n-r)}.
\]
For \(n=2\), this becomes \(N_2(q)=q^5(3q+1)\). In particular, over \(\mathbb F_2[arepsilon]/(arepsilon^2)\) there are exactly \(224\) strongly nil-clean matrices in \(M_2\), while all \(256\) matrices are nil-clean.

## Assumptions and scope
A ring element is strongly nil-clean if it is a sum of a commuting idempotent and nilpotent. The statement applies to every finite field \(\mathbb F_q\), including characteristic \(2\), and to every matrix size \(n\ge1\). It concerns the dual-number ring \(R_q\) with square-zero parameter \(arepsilon\).

## Proof
Write a dual matrix as \(\mathcal M=A+arepsilon B\), with \(A,B\in M_n(\mathbb F_q)\). The lifting argument used for dual matrices depends only on the decomposition of \(A\) into its generalized \(0\)- and \(1\)-eigenspaces and on the invertibility of the corresponding Sylvester operator. Hence the argument applies over every field: \(\mathcal M\) is strongly nil-clean exactly when \(A\) is strongly nil-clean. Indeed, if \(A=E+N\) with \(E^2=E\), \(N\) nilpotent and \(EN=NE\), then relative to \(\operatorname{im}E\oplus\ker E\), the diagonal blocks of \(A\) are \(I+N_1\) and \(N_0\). Their minimal polynomials divide powers of \(t-1\) and \(t\), respectively, so the off-diagonal Sylvester equations have unique solutions over any field. Thus every \(B\) lifts.

It remains to count strongly nil-clean matrices \(A\) over \(\mathbb F_q\). Such an \(A\) is strongly nil-clean exactly when its minimal polynomial divides \(t^a(t-1)^b\) for some \(a,b\ge0\): one direction follows from the commuting decomposition, and the converse follows from the primary decomposition for the coprime polynomials \(t\) and \(t-1\).

Fix \(r\), the dimension of the generalized \(1\)-eigenspace, and set \(s=n-r\). There are
\[
{nrack r}_q q^{rs}
\]
ordered decompositions \(\mathbb F_q^n=U\oplus W\) with \(\dim U=r\) and \(\dim W=s\): choose \(U\), then one of its \(q^{rs}\) complements. On \(U\), choose \(A=I+N_1\) with arbitrary nilpotent \(N_1\); on \(W\), choose arbitrary nilpotent \(N_0\). The classical finite-field nilpotent count gives \(q^{r^2-r}\) choices for \(N_1\) and \(q^{s^2-s}\) for \(N_0\). Therefore the number of strongly nil-clean \(A\) with this value of \(r\) is
\[
{nrack r}_q q^{rs+r^2-r+s^2-s}
={nrack r}_q q^{n^2-n-rs}.
\]
Each such \(A\) admits all \(q^{n^2}\) choices of \(B\), yielding
\[
N_n(q)=\sum_{r=0}^n {nrack r}_q q^{2n^2-n-r(n-r)}.
\]

## Verification
The accompanying checker exhausts all matrices \(A\) for \((q,n)=(2,1),(2,2),(2,3),(3,1),(3,2),(5,2)\), tests strong nil-cleanness through nilpotence of \(A-A^2\), and compares the result with the closed formula. It returns `CHECK_OK`. These finite checks are consistency tests only; the formula for arbitrary prime powers and arbitrary \(n\) is proved symbolically above.

## Relationship to prior work
Şentürk and Özbay characterize strong nil-cleanness for matrices over the real dual numbers and prove that the dual part imposes no additional obstruction; their proof also identifies the required Sylvester equations. Their paper does not count strongly nil-clean matrices and contains no finite-field enumeration. The same paper observes that \(M_n(\mathbb F_2[arepsilon]/(arepsilon^2))\) is nil-clean, making the exact strong nil-clean deficit especially natural.

Breaz, Călugăreanu, Danchev and Micu characterize nil-clean matrix rings over fields, but the inspected bibliographic and abstract material does not state the elementwise finite-field census above. Fine--Herstein's classical result that exactly \(q^{m^2-m}\) matrices in \(M_m(\mathbb F_q)\) are nilpotent supplies the counting input for the two primary blocks. Nearby finite-local-ring enumeration results for idempotent or von Neumann regular matrices concern different loci and do not imply the strong nil-clean count.

## Limitations
The theorem counts strongly nil-clean elements only for the square-zero dual-number extension. It does not enumerate merely nil-clean elements for general \(q\), nor does it treat longer truncated polynomial rings. The originality search did not locate an equivalent census, but an older enumeration could in principle be encoded indirectly in finite-matrix similarity or cycle-index literature under a different terminology.

## References
1. B. Şentürk and N. A. Özbay, *On the Regularity and Clean Properties of Matrices over Dual Numbers*, arXiv:2609.29468v1, 2026.
2. S. Breaz, G. Călugăreanu, P. V. Danchev and T. Micu, *Nil-clean matrix rings*, Linear Algebra and its Applications 439 (2013), 3115--3119, DOI 10.1016/j.laa.2013.08.027.
3. N. J. Fine and I. N. Herstein, *The probability that a matrix be nilpotent*, Illinois Journal of Mathematics 2 (1958), 499--504.
