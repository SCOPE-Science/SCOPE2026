# Sharp square-root joint discrepancy for two meta-automatic sequences

## Finding

Let \(a,b:\mathbb{Z}_{\ge0}\to\{0,1\}\) be the two meta-automatic sequences described precisely below. Define
\[
S(N)=\sum_{0\le n<N}(-1)^{a(n)+b(n)}\qquad(N\in\mathbb{Z}_{\ge0}).
\]
There is an absolute constant \(C>0\) such that
\[
|S(N)|\le C\sqrt N\qquad\text{for every integer }N\ge1.
\]
The exponent is sharp on complete base-four blocks:
\[
0<\limsup_{k\to\infty}\frac{|S(4^k)|}{2^k}<\infty.
\]
Consequently, for each \((i,j)\in\{0,1\}^2\),
\[
\#\{0\le n<N:(a(n),b(n))=(i,j)\}
=\frac N4+O(\sqrt N).
\]
For \(k\ge1\) the four counts on \([0,4^k)\) are exactly
\[
C_{00}=C_{11}=\frac{4^k+S(4^k)}4,\qquad
C_{01}=C_{10}=\frac{4^k-S(4^k)}4,
\]
and the \(O(\sqrt N)\) exponent cannot be decreased in any of these four formulas. Thus the two individually balanced words are jointly equidistributed, with a sharp square-root-order signed discrepancy.

## Assumptions and scope

The first sequence \(a\) has \(a(0)=0\), \(a(1)=1\), and, for every \(n\ge0\),
\[
\begin{aligned}
a(4n)&=a(n),&a(4n+1)&=1-a(n),\\
a(4n+2)&=a(2n+1-a(n)),&a(4n+3)&=1-a(4n+2).
\end{aligned}
\]
The second sequence \(b\) has \(b(0)=0\), \(b(1)=1\), and, for every \(n\ge1\) in its first two branch equations and every \(n\ge0\) in its latter two,
\[
\begin{aligned}
b(4n)&=b(2n+b(n)),&b(4n+1)&=1-b(4n),\\
b(4n+2)&=b(2n+1-b(n)),&b(4n+3)&=1-b(4n+2).
\end{aligned}
\]
The first two equations for \(b\) at \(n=0\) also agree with the stated initial values. Both recurrences determine their sequences by induction; the source establishes their four-state automata and balancedness, \(a(2n)+a(2n+1)=b(2n)+b(2n+1)=1\). In the source notation they are \(\mathcal M_1\) and \(\mathcal M_2\), respectively. The assertion concerns joint *one-position* frequencies, not frequencies of words of arbitrary length.

## Proof

**1. Coupled digit transfer.** The published four-uniform morphisms, in state order \(0,1,2,3\), are
\[
\begin{array}{c|cccc}
q&0&1&2&3\\\hline
\sigma_1(q)&0112&1230&2301&3023\\
\sigma_2(q)&0132&2310&3201&1023
\end{array}
\]
with initial state \(0\) for both automata and output \(h(0)=h(2)=0\), \(h(1)=h(3)=1\). A base-four digit \(r\in\{0,1,2,3\}\) sends the pair state \((u,v)\in\{0,1,2,3\}^2\) to \((\sigma_1(u)_r,\sigma_2(v)_r)\), where the subscript indexes the \(r\)-th digit starting at zero. Define a \(16\times16\) nonnegative integer matrix \(T\), indexed by these ordered pairs, by
\[
T_{(u',v'),(u,v)}
=\#\{r\in\{0,1,2,3\}:\sigma_1(u)_r=u',\ \sigma_2(v)_r=v'\}.
\]
Let \(e\) be the unit column for pair state \((0,0)\), and let \(w\) be the sign column \(w_{(u,v)}=(-1)^{h(u)+h(v)}\). Reading all length-\(k\) base-four strings (including leading zeros) gives the exact identity
\[
S(4^k)=w^{\mathsf T}T^k e\qquad(k\ge0).
\]
More generally, after any fixed base-four prefix has reached pair state \((u,v)\), the sum of the next \(4^k\) signs is \(w^{\mathsf T}T^ke_{(u,v)}\).

**2. Exact characteristic polynomial and root locations.** Direct expansion of the four morphism rules yields
\[
\det(\lambda I-T)=\lambda^8(\lambda-4)(\lambda-1)
(\lambda^2+3\lambda+4)
(\lambda^4-3\lambda^3+5\lambda^2-12\lambda+16).
\]
The quadratic roots have modulus \(2\). For the quartic, write \(\lambda=2z\) and \(u=z+z^{-1}\). Its zero equation becomes
\[
u^2-\frac32u-\frac34=0,\qquad
u\in\left\{\frac{3+\sqrt{21}}4,\frac{3-\sqrt{21}}4\right\}.
\]
Both values lie strictly between \(-2\) and \(2\); thus the four quartic roots are pairwise distinct, on \(|\lambda|=2\). They also differ from the quadratic roots. The six modulus-two eigenvalues are therefore simple. The remaining eigenvalues are \(0\) (algebraic multiplicity eight), \(1\) and \(4\), the last two simple.

Every row of \(T\) sums to \(4\), so the all-ones column spans the eigenline at \(4\). Since \(w\) sums to zero over the sixteen pair states, \(w^{\mathsf T}\) annihilates that eigenline. All other nonzero eigenvalues have modulus at most \(2\) and are simple; the generalized zero-eigenspace disappears after at most eight applications of \(T\). It follows that an absolute \(K\) satisfies
\[
\bigl|w^{\mathsf T}T^ke_{(u,v)}\bigr|\le K2^k
\quad\text{for all }k\ge0\text{ and all pair states }(u,v).
\]

**3. Arbitrary prefixes.** The integer interval \([0,N)\) can be partitioned into aligned base-four intervals \([t4^k,(t+1)4^k)\) with at most three pieces of each length \(4^k\), by the usual greedy expansion of \(N\) in base four. Every piece has the corresponding fixed-prefix form from step 1, hence its sign sum has magnitude at most \(K2^k\). If \(4^m\le N<4^{m+1}\), the triangle inequality gives
\[
|S(N)|\le3K\sum_{k=0}^{m}2^k<6K\,2^m\le6K\sqrt N.
\]
Balancedness of the individual sequences shows that each individual sign sum over \([0,N)\) has absolute value at most one. Expanding the product of the two indicator identities \(\mathbf1_{a=i}=(1+(-1)^{a+i})/2\) and \(\mathbf1_{b=j}=(1+(-1)^{b+j})/2\) yields the asserted joint counts; on complete blocks of length \(4^k\) the two individual sign sums vanish exactly.

**4. Sharpness.** Exact integer multiplication of the defined transfer matrix gives
\[
S(4^8)=-364,\qquad S(4^9)=-372.
\]
By the characteristic polynomial, for \(k\ge8\) the scalar sequence \(S(4^k)\) is a sum of a constant and six exponentials with pairwise distinct eigenvalues of modulus \(2\); the eigenvalue \(4\) contributes nothing. If all six modulus-two coefficients vanished, this scalar sequence would be constant for \(k\ge8\), contradicting the two values displayed. Thus at least one of the six coefficients is nonzero. Dividing by \(2^k\), the distinct unit-modulus exponentials have strictly positive limiting Cesàro mean square (their cross terms average to zero). Consequently the displayed positive finite limsup holds. The exact four-cell formulas then transfer this lower-order obstruction to all four joint counts.

## Verification

The standalone `verify.py` reconstructs both transition morphisms, builds the \(16\times16\) integer matrix, independently computes its characteristic polynomial by exact Newton trace identities, and checks the displayed factorization. It also computes both original nested recurrences at all indices \(0\le n<262144\), independently compares their DFAO outputs, verifies full-block transfer sums through \(k=12\) (with direct recurrence comparisons through \(k=9\)), and tests an aligned-block formula for 271 prefixes. Run with `python3 verify.py`; expected output is in `verify_output.txt`. These exact finite checks corroborate the transfer calculation. The infinite bound and sharpness follow from the proved spectral and interval-decomposition arguments, not the finite enumeration.

## Relationship to prior work

Campbell and Cloitre introduced the two balanced meta-automatic sequences and proved their separate four-state DFAOs, morphisms, and factor-complexity properties. Their stated results do not include a joint correlation or a sharp joint-frequency discrepancy; the present argument uses their explicit individual automata as inputs to a new coupled matrix and its spectral calculation. The individual sequences are recorded as OEIS A392736 and A391614. The standard finite-state transfer technique alone does not force square-root joint cancellation for arbitrary pairs (identical balanced sequences, for example, have signed product identically one). Prior records on unrelated morphic statistics do not imply this pairwise bound.

## Limitations

The theorem establishes simultaneous one-position frequencies and sharp order of the signed overlap discrepancy. It does not assert independence of adjacent symbols, joint normality, an optimal numerical value of the universal constant \(C\), or an exact positive value for the limiting upper oscillation. Search-based novelty checks cannot rule out every unpublished or unindexed equivalent treatment. The proof uses already established individual DFAOs; an error in either published transition rule would require the coupled calculation to be re-examined, although the independent recurrence checks provide substantial finite corroboration.

## References

1. J. M. Campbell and B. Cloitre, *Meta-Automatic Sequences*, arXiv:2602.23395v2 (2026), Sections 3–5, Theorems 13 and 22 and Corollaries 16 and 23; https://arxiv.org/abs/2602.23395 . First arXiv version made public February 25, 2026.
2. Campbell and Cloitre, *Meta-Automatic Sequences*, *Journal of Integer Sequences* **29** (2026), Article 26.4.1; https://cs.uwaterloo.ca/journals/JIS/VOL29/Cloitre/cloitre20.html .
3. *OEIS A392736*, https://oeis.org/A392736 ; earliest sequence data in the public revision history dated January 21, 2026; https://oeis.org/history?seq=A392736&start=10 .
4. *OEIS A391614*, https://oeis.org/A391614 ; sequence established in February 2026.
