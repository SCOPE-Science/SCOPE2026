# Complete gap-multiplicity law and square-slope structure for binary inclusion-exclusion polynomials

## Finding

Let \(2\le a<b\) be coprime integers. Define the binary inclusion-exclusion polynomial
\[
Q_{a,b}(z)=\frac{(1-z)(1-z^{ab})}{(1-z^a)(1-z^b)}
\]
of degree \(C=(a-1)(b-1)\), and let \(M_d(a,b)\) be the number of adjacent **nonzero** coefficients whose exponents differ by \(d\). This includes \(d=1\), representing adjacent nonzero coefficients, and \(1\le d\le a-1\) is the full possible range.

Write \(b=ha+r\), where \(h\ge1\), \(1\le r<a\), and let \(u\) be the inverse of \(r\) modulo \(a\). For a distance \(d=D-1\) with \(2\le D\le a\), calculate the following integers \(\delta,H\):

* If \(D=a\), set \(\delta=0\), \(H=1\).
* If \(2\le D<a\), sort the \(D+1\) distinct least nonnegative residues
  \[
  \mathcal P_D=\{[uj]_a:0\le j\le D\},\qquad t=[uD]_a.
  \]
  If \(t\) is the second-smallest element, set \(\delta=t\) and \(H=a-\max\mathcal P_D\). If \(t\) is the largest element, set \(\delta=a-t\) and \(H=t-\operatorname{secondmax}\mathcal P_D\). Otherwise the gap of distance \(d\) does not occur and \(M_d(a,b)=0\).

In every active case \(H\ge1\), and the **complete exact frequency** is
\[
\boxed{
M_{D-1}(a,ah+r)=2hH^2+2\sum_{s=0}^{H-1}
\left(\left\lfloor\frac{(\delta+s+H)r}{a}\right\rfloor-
\left\lfloor\frac{(\delta+s)r}{a}\right\rfloor\right).}
\]
In particular, for fixed coprime \(a,r\), every frequency is either identically zero as \(h\) varies or affine-linear with slope **twice a perfect square**, \(2H^2\). The formula computes all distances and frequencies using only \(a,r,h\) without forming a polynomial of degree \(\Theta(ab)\). When \(a=p<b=q\) are primes, \(Q_{p,q}=\Phi_{pq}\), so the result is a complete gap-multiplicity formula for every binary cyclotomic polynomial.

For example, \(M_1(7,17)=20\), \(M_2(7,17)=20\), \(M_3(7,17)=4\), \(M_6(7,17)=4\), and all other frequencies vanish. The special residues \(r=1\) and \(r=a-1\) recover the previously known frequencies of positive zero gaps: for \(r=1\), \(M_d=2h\) for all \(1\le d<a\); for \(r=a-1\), \(M_{a-1}=2h\) and \(M_d=2(h+1)\) for all \(1\le d<a-1\).

## Assumptions and scope

All variables \(a,b,h,r,D,d\) above are integers with the stated bounds and \(\gcd(a,b)=1\). The notation \([x]_a\) means the residue in \(\{0,1,\dots,a-1\}\). A gap of distance \(d\) means the exponent difference between successive nonzero coefficients, **not** the number of intervening zero coefficients (which is \(d-1\)). The polynomial is self-reciprocal; its nonzero coefficients alternate signs. Composite coprime \(a,b\) are included, without asserting that \(Q_{a,b}\) is an irreducible cyclotomic polynomial in that case.

## Proof

**1. Semigroup coefficients and reflection.** Let \(S=\langle a,b\rangle\) and put \(w(n)=1\) when \(n\in S\), and \(0\) otherwise, with \(w(-1)=0\). For \(0\le n\le C=(a-1)(b-1)<ab\), any expression \(n=ia+jb\) with \(i,j\ge0\) is unique: two distinct nonnegative representations require a change of \(a\) in the coefficient of \(b\), hence at least one representation has value \(\ge ab\). Therefore, in degrees \(0\le n\le C\), the coefficients of \(1/((1-z^a)(1-z^b))\) are exactly \(w(n)\). Because \(C<ab\), the factor \(1-z^{ab}\) does not affect these degrees, and the coefficient of \(z^n\) in \(Q_{a,b}\) is \(c_n=w(n)-w(n-1)\). It follows that all \(c_n\) lie in \(\{-1,0,1\}\), with the nonzero entries alternating in sign; \(c_0=c_C=1\).

The rational identity \(z^CQ_{a,b}(1/z)=Q_{a,b}(z)\) proves palindromicity. Whenever two consecutive members of \(S\) are separated by \(D\ge2\), a run of \(D-1\) nonmembers produces a coefficient pair \((-1,+1)\) whose exponent gap is \(D-1\). Reversing the coefficient word gives exactly as many pairs of type \((+1,-1)\) at the same distance. Thus \(M_{D-1}\) is twice the number of consecutive semigroup-member gaps of length \(D\). The latter are all \(\le a\), since \(a\in S\).

**2. Increasing residue sets in blocks.** Every nonnegative integer has a unique expression \(ka+s\), with \(0\le s<a\). For each \(0\le j<a\), the least member of \(S\) congruent to \([jr]_a\) modulo \(a\) is \(jb\); its block index is
\[
T_j=\left\lfloor\frac{jb}{a}\right\rfloor=hj+\left\lfloor\frac{jr}{a}\right\rfloor.
\]
The thresholds \(T_j\) are strictly increasing since \(h\ge1\). Exactly for the blocks \(T_j\le k<T_{j+1}\), the present residues form
\[
R_j=\{[ir]_a:0\le i\le j\}.
\]
Each \(R_j\) contains zero, which is the first present residue in every block. Therefore a cyclic arc of length \(D\) between consecutive residues of \(R_j\), including the wrap to zero in the next block, corresponds to exactly one consecutive member gap of length \(D\) starting in this block. There is no gap with length at least two once all residues are present. Writing \(c_{j,D}\) for the number of cyclic arcs of length \(D\) in \(R_j\), we obtain
\[
\frac12M_{D-1}(a,b)=\sum_{j=0}^{a-2}(T_{j+1}-T_j)c_{j,D}.
\tag{1}
\]

**3. The cyclic insertion lemma.** Fix \(2\le D<a\). For a possible arc from residue \(x\) to \([x+D]_a\), list the insertion times of the \(D+1\) consecutive residues along the arc:
\[
([u(x+j)]_a:0\le j\le D).
\]
This is a circular translate of \(\mathcal P_D\), so its endpoints are the first two points inserted if and only if \(0,t\) are neighboring points on the circle of ordered insertion times and the circular cut lies in the gap preceding the first one. Since zero is the smallest point of \(\mathcal P_D\), this is possible precisely when \(t\) is its second-smallest or largest point. In all other cases \(c_{j,D}=0\) for every \(j\).

Suppose \(t\) is the second-smallest point. Then \(0,t\) are the first two insertion times, followed by a third point \(t+H\) where \(H=a-\max\mathcal P_D\). Indeed the reflection \(v\mapsto[t-v]_a\) permutes \(\mathcal P_D\), carrying its largest member to its third-smallest member; thus their adjacent gaps both have width \(H\). The permitted circular translations add exactly \(s\) to all insertion times, with \(s=0,\ldots,H-1\); the first three then become \(s,s+\delta,s+\delta+H\), where \(\delta=t\).

If \(t\) is instead the largest point, reflect the same order. Now the first three insertion times under the permitted translations are again \(s,s+\delta,s+\delta+H\), where \(\delta=a-t\) and \(H=t-\operatorname{secondmax}\mathcal P_D\). The equality between the gap from zero to the smallest positive point and this \(H\) follows from the same reflection. In either case precisely \(H\) cyclic translations work, indexed by \(0\le s<H\).

Such an arc is present in \(R_j\) exactly after both endpoints, but before any of its interior residues, are inserted. Hence it occurs when
\[
\delta+s\le j<\delta+s+H.
\]
Equivalently, the cyclic gap counts have the **triangular insertion law**
\[
c_{j,D}=\#\{(s,t):0\le s,t<H,\ j=\delta+s+t\}.
\tag{2}
\]
All displayed indices lie in \(0\le j\le a-2\) because a positive-length arc cannot survive in the full residue set. Finally, when \(D=a\), the full-length arc occurs only when \(R_0=\{0\}\), so equation (2) still applies on taking \(\delta=0,H=1\).

**4. Exact frequency and square slope.** Insert (2) into (1). From
\[
T_{j+1}-T_j=h+\left\lfloor\frac{(j+1)r}{a}\right\rfloor-\left\lfloor\frac{jr}{a}\right\rfloor,
\]
we get
\[
\frac12M_{D-1}=\sum_{s,t=0}^{H-1}\left(h+
\left\lfloor\frac{(\delta+s+t+1)r}{a}\right\rfloor-
\left\lfloor\frac{(\delta+s+t)r}{a}\right\rfloor\right).
\]
Summing first over \(t\) telescopes the floor differences, yielding the boxed formula. The \(h\)-coefficient is exactly \(2H^2\). This completes the proof for all coprime \(a,b\) and all possible \(d\).

## Verification

The standalone Python 3 program `verify_gaps.py` evaluates the formula using modular inverses, sorting and integer floor sums, and **independently** constructs the coefficients of \(Q_{a,b}\) by finite arithmetic on the generating function. It independently checks the critical triangular insertion law for every coprime remainder at \(2\le a\le27\), every possible distance and every partial residue set. It also compares complete distance histograms for 3,256 coprime pairs, including composite cases and larger quotients, and checks four explicit samples. Execute `python3 verify_gaps.py`; success prints `VERIFIED: 3256 coprime pairs; exact coefficient gaps and square-slope formula`. These finite checks supplement, rather than replace, the general proof.

## Relationship to prior work

Camburu–Ciolan–Luca–Moree–Shparlinski (2015 preprint, published 2016) established maximal-gap facts and studied coefficient gaps. Cafure–Cesaratto (2021 preprint) gave a compact word algorithm for every coefficient vector; its full output *implicitly determines* any gap histogram, but the stated word theorem is not the direct all-residue frequency formula or triangular insertion/square-slope law above. Cafure–Cesaratto (2025 preprint) determined the frequency of each positive gap length only for residue classes \(q\equiv\pm1\pmod p\), and gave the second-largest gap for general residues. The present formula extends their frequency assertions to every residue and both prime and coprime composite parameters. Bachman (2026) classified the possible gap **lengths** in the general coprime setting, while the present result specifies their **multiplicities**, and provides a separate affine-law refinement. These are comparisons of mathematical statements, not claims of exhaustive priority certainty.

## Limitations

The theorem is specific to two coprime generators and does not assert analogous perfect-square slopes for three or more generators, ternary cyclotomic polynomials, or arbitrary zero/nonzero patterns. Its running time may be quadratic or more in \(a\) when all lengths are computed; it is not an output-sensitive coefficient generator. The explicit coefficient representation in the 2021 work can theoretically yield the histogram by further analysis, and an equivalent unstated or differently phrased formula could exist in work not located by the literature searches.

## References

1. O.-M. Camburu, E.-A. Ciolan, F. Luca, P. Moree, I. E. Shparlinski, *Cyclotomic coefficients: gaps and jumps*, arXiv:1507.07098 (submitted July 25, 2015), J. Number Theory **163** (2016), 211–237. https://arxiv.org/abs/1507.07098
2. A. Cafure and E. Cesaratto, *Binary Cyclotomic Polynomials: Representation via Words and Algorithms*, arXiv:2109.07544 (submitted September 2021). https://arxiv.org/abs/2109.07544
3. A. Cafure and E. Cesaratto, *Gaps in binary cyclotomic polynomials*, arXiv:2507.19381 (submitted July 25, 2025; May 2026 revision), especially Theorems 1.1–1.2. https://arxiv.org/abs/2507.19381
4. G. Bachman, *Gaps of Binary Numerical Semigroups and of Binary Inclusion-Exclusion Polynomials*, arXiv:2605.17157 (submitted May 16, 2026). https://arxiv.org/abs/2605.17157
