# Exact dyadic fibre and collision laws for sums of two odd powers

## Finding
For every fixed odd integer \(d\ge3\), the normalized number of ordered representations of a residue as a sum of two \(d\)-th powers modulo \(2^n\) obeys an exact finite-depth law, and its limit has a sharp moment transition.

Let
\[
R_{d,n}(a)=\#\{(x,y)\pmod{2^n}:x^d+y^d\equiv a\pmod{2^n}\},\qquad
F_{d,n}(a)=2^{-n}R_{d,n}(a),
\]
where \(n\ge1\). Define \(F_{d,0}=1\) on the singleton residue ring, and set
\[
M_{d,n}=2^{-n}\sum_{a\pmod{2^n}}F_{d,n}(a)^2
=2^{-3n}\#\{(x,y,u,v)\pmod{2^n}:x^d+y^d\equiv u^d+v^d\pmod{2^n}\}.
\]
Then \(M_{d,0}=1\), and
\[
\boxed{M_{d,n}=\frac78+2^{n-4}\quad(1\le n<d),\qquad
M_{d,n}=\frac78+2^{d-4}M_{d,n-d}\quad(n\ge d).}
\]
For Haar-uniform \(T\in\mathbb Z_2\), the functions \(F_{d,n}(T\bmod2^n)\) converge almost surely to an explicitly recursive probability density \(F_d(T)\). Its sharp integrability range is
\[
\boxed{F_d\in L^s(\mathbb Z_2)\iff0<s<\frac{d}{d-2}.}
\]
Convergence also holds in \(L^s\) throughout that range. In particular, \(M_{3,n}\to7/4\); for all odd \(d\ge5\), \(M_{d,n}\asymp_d2^{(d-4)n/d}\) diverges. This is an exact variance phase transition at the cubic exponent.

## Assumptions and scope
All exponents \(d\) are *fixed odd integers at least three*. All residues are ordered, and the pairs and quadruples are counted over the full ring \(\mathbb Z/2^n\mathbb Z\), including zero and nonunits. Haar measure on \(\mathbb Z_2\) gives measure \(2^{-m}\) to each residue class modulo \(2^m\). Every value of \(n\ge0\) is included. The local density is specified almost everywhere; the point \(T=0\) may be assigned any value without changing moment conclusions.

## Proof
**1. A unit-permutation fact.** For each \(n\ge1\), the multiplicative group of odd residues modulo \(2^n\) is a finite group of order a power of two. Since \(d\) is odd, exponentiation by \(d\) is a permutation of this group: the group is abelian and \(d\) is coprime to its (2-power) exponent, hence the power map is an automorphism. Thus the \(d\)-th power of a Haar-uniform odd 2-adic integer is Haar-uniform on the odd coset. On the even coset, \(X=2U\), and \(X^d=2^dU^d\), where \(U\) is Haar-uniform on \(\mathbb Z_2\).

**2. Exact law of the sum.** For independent Haar-uniform \(X,Y\), the one-odd/one-even cases together have probability \(1/2\), with the sum uniformly distributed among odd residues. The both-odd case has probability \(1/4\), with the sum uniform among even residues. The both-even case has probability \(1/4\), and gives \(2^d(U^d+V^d)\). Writing \(A=2^{d-2}\), the pushforward measure is absolutely continuous: the mass after \(h\) consecutive both-even branches is \(4^{-h}\to0\). Its Radon–Nikodym density therefore satisfies, for almost every \(t\in\mathbb Z_2\),
\[
F_d(t)=\begin{cases}
1,&t\text{ odd},\\
\frac12,&t\text{ even and }t\notin2^d\mathbb Z_2,\\
\frac12+A F_d(t/2^d),&t\in2^d\mathbb Z_2.
\end{cases}
\]
The density integrates to one because it is the pushforward of a probability measure. Its exact average on each residue class modulo \(2^n\) is \(F_{d,n}\). For \(n\ge d\), the same equation with lower index \(n-d\) is exact. In terms of integer representation counts it reads
\[
R_{d,n}(a)=\begin{cases}
2^n,&a\text{ odd},\\
2^{n-1},&a\text{ even},\ 2^d\nmid a,\\
2^{n-1}+2^{2d-2}R_{d,n-d}(a/2^d),&2^d\mid a.
\end{cases}
\]
For \(1\le n<d\), the both-even branch contributes only to residue zero; the exact counts are \(2^n\) at odd residues, \(2^{n-1}\) at nonzero even residues, and \(2^{n-1}+2^{2n-2}\) at zero. The formulas also apply at the boundary \(n=d\) using \(R_{d,0}(0)=1\).

**3. Quadratic moment.** The baseline density \(1\) on odd targets and \(1/2\) on even targets contributes \(1/2+1/8=5/8\) to the second moment. On \(2^d\mathbb Z_2\), the correction from the both-even branch is
\[
2^{-d}\mathbb E\left[(\tfrac12+A F_{d,n-d})^2-(\tfrac12)^2\right]
=2^{-d}\left(A+A^2M_{d,n-d}\right)
=\frac14+2^{d-4}M_{d,n-d},
\]
where \(\mathbb EF_{d,n-d}=1\). This proves the displayed recurrence for all \(n\ge d\). For \(1\le n<d\), replace the inner random density with a single point mass: the analogous correction is \(1/4+2^{n-4}\), proving \(M_{d,n}=7/8+2^{n-4}\). When \(d=3\), the recurrence has contraction factor \(1/2\), hence limit \((7/8)/(1-1/2)=7/4\). When \(d\ge5\), the factor \(2^{d-4}>1\) gives \(M_{d,n}\asymp_d2^{(d-4)n/d}\), uniformly over the finitely many residue classes of \(n\bmod d\).

**4. Sharp moment boundary.** Repeatedly applying the density recursion on the disjoint valuation shells \(t=2^{dh}u\), with \(u\) odd, yields
\[
F_d(2^{dh}u)=A^h+\frac12\frac{A^h-1}{A-1}\quad(h\ge0),
\]
and those shells have Haar measure \(2^{-dh-1}\). On any other shell with valuation between \(dh+1\) and \(d(h+1)-1\), the same recursion gives \(F_d(t)=O_d(A^h)\). Therefore \(\int F_d^s\) converges exactly when the geometric series \(\sum_{h\ge0}2^{-dh}A^{sh}\) converges, which is equivalent to \(s<d/(d-2)\). At the threshold and above, the odd terminal shells furnish a diverging subseries. Finally, \(F_{d,n}=\mathbb E(F_d\mid T\bmod2^n)\) is the conditional expectation martingale; its almost-sure and \(L^s\) convergence in the permitted range follow from standard conditional-expectation convergence, with \(L^1\) convergence implying \(L^s\) for \(0<s<1\).

## Verification
The accompanying standalone Python file `verify.py` uses only the standard library. For odd exponents \(d=3,5,7,9\), it independently constructs every power-residue multiplicity, convolves those counts exactly, and compares the resulting complete target distributions with both levels of the finite-depth formula. It also compares the exact collision moment as a rational number with the independent recurrence for every tested depth. It verifies 4,600 target counts in 36 exponent-depth cases (depths through 10, 9, 9 and 8 respectively). These finite tests are diagnostics; steps 1–4 are the proof for all exponents and depths.

## Relationship to prior work
Brüdern and Vaughan (2021) analyze sums of two positive cubes and their variance across arithmetic progressions, using residue representation counts and exponential sums. Their results concern global arithmetic-progression variance, not the all-depth dyadic fibre law for every odd exponent nor the sharp integrability transition. The classical permutation of odd unit residues under odd powers is the main elementary input here. Known local analyses for the exceptional prime \(3\) in the cubic case and for even-power dyadic cases do not imply the odd-exponent family. A more general published local-density or local-zeta framework could contain implicit versions of individual formulas; publication priority is not asserted.

## Limitations
The result is local to the prime \(2\) and applies only to *odd* \(d\ge3\). It does not give global integer asymptotics or Diophantine solvability over \(\mathbb Z\). The \(L^s\) divergence is about the 2-adic limiting density; each finite-depth \(F_{d,n}\) has all finite moments. No independent mathematical audit has been performed.

## References
- Jörg Brüdern and Robert C. Vaughan, *A Montgomery–Hooley Theorem for sums of two cubes*, European Journal of Mathematics **7** (2021), 1616–1644. DOI: `10.1007/s40879-021-00495-4`; full text: https://link.springer.com/article/10.1007/s40879-021-00495-4.
