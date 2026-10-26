# Trace-matched cat-map strips: three-block Bernoulli mimicry and an exact fourth-block bias

## Finding
For each integer \(q\ge3\), let \(A\in\operatorname{SL}_2(\mathbb Z)\) have trace \(q\), choose any nonzero row \(\ell\in\mathbb Z^{1\times2}\), and give \(\mathbb T^2=\mathbb R^2/\mathbb Z^2\) its normalized Haar measure. Define the stationary alphabet-valued process
\[
 u_n=\{\ell A^nz\}\in[0,1),\qquad S_n=\lfloor q u_n\rfloor\in\{0,\ldots,q-1\},\quad n\in\mathbb Z.
\]
For every triple \((a,b,c)\) of alphabet symbols and every integer \(n\),
\[
 \Pr(S_n=a,S_{n+1}=b,S_{n+2}=c)=q^{-3}.
\]
Nevertheless the fourth consecutive symbol, conditional on three zeros, satisfies
\[
\Pr(S_3=d\mid S_0=S_1=S_2=0)=
\begin{cases}
\displaystyle\frac{q}{q^2-1},&0\le d\le q-2,\\[3pt]
\displaystyle\frac{1}{q+1},&d=q-1.
\end{cases}
\]
Equivalently, the complete list of four-word cylinder measures beginning with three zeros is
\[
\boxed{\Pr(000d)=
\begin{cases}
\displaystyle\frac{1}{q^2(q^2-1)},&0\le d\le q-2,\\[3pt]
\displaystyle\frac{1}{q^3(q+1)},&d=q-1.
\end{cases}}
\]
Thus the first possible failure of consecutive-block Bernoulli behavior occurs **exactly at length four**, for every allowed trace. For the standard cat matrix \(\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)\), whose trace is three, the three probabilities \(\Pr(0000),\Pr(0001),\Pr(0002)\) equal \(1/72,1/72,1/108\) respectively, not the independent value \(1/81\). In particular the entropy of three consecutive observations is \(3\log q\), while that of four consecutive observations is strictly less than \(4\log q\).

## Assumptions and scope
The integer \(q\) is arbitrary but at least three. Only the determinant-one, positive-trace hyperbolic case is asserted, and \(\ell\) is allowed to be nonprimitive. Coordinates are interpreted on the torus and \(\{\cdot\}\) is the unique representative in the half-open unit interval; bin endpoints do not affect Haar probabilities. All entropy logarithms are natural. The result concerns **consecutive** blocks of this specific equal-width, one-dimensional observable, not nonconsecutive time sets, winding-number encodings, or general partitions.

## Proof
**1. The two-coordinate reduction.** The characteristic polynomial of \(A\) is \(t^2-qt+1\). If the integer rows \(\ell\) and \(\ell A\) were linearly dependent over \(\mathbb R\), \(\ell\) would be a rational left eigenvector with a rational eigenvalue. By the rational-root theorem the latter could only be \(\pm1\), inconsistent with \(q\ge3\). Consequently the integer matrix with these two rows has nonzero determinant. It induces a finite-to-one surjective torus homomorphism and sends normalized Haar measure to normalized Haar measure. Hence \((u_0,u_1)\) consists of two independent uniform circle variables. Stationarity follows because \(A\) itself preserves Haar measure.

**2. The first three symbols.** Cayley–Hamilton gives the exact congruence
\[
 u_{n+2}\equiv q u_{n+1}-u_n\pmod1.
\]
Conditional on \(S_0=a,S_1=b\), write \(u_0=(a+U)/q\) and \(u_1=(b+V)/q\), where \(U,V\) remain independent uniform variables on \([0,1)\). Then
\[
 u_2=\{V-u_0\}.
\]
For each fixed \(U,a,b\), uniform translation modulo one makes \(u_2\) uniform. Thus \(S_2\) is conditionally uniform and independent of the first two symbols; the first two were independent uniform already. Stationarity gives the result at every consecutive triple.

**3. Resolve the fourth coordinate on one natural cylinder.** Conditioning further on \(S_0=S_1=S_2=0\), the preceding argument shows that \(u_0=U/q\) and \(u_2=W/q\) for independent uniform \(U,W\in[0,1)\). Because \(S_1=0\), we have \(0\le q u_1<1\). Also \(u_0+u_2<2/q<1\) since \(q\ge3\). Using the congruence \(q u_1\equiv u_0+u_2\pmod1\) therefore yields the equality
\[
 u_1=\frac{U+W}{q^2},\qquad u_3=\left\{W-\frac{U+W}{q^2}\right\}.
\]
Decompose \(W=(J+R)/q\), where \(J\) is uniform on \(\{0,\ldots,q-1\}\) and \(U,R,J\) are mutually independent with \(U,R\) uniform on \([0,1)\). A direct substitution gives
\[
 q\left(W-\frac{U+W}{q^2}\right)
 =J+R-\frac{qU+J+R}{q^2}.
\]
The last two terms lie strictly between \(-1\) and \(1\) for the parameter range. Consequently \(S_3=J-1\pmod q\) precisely if
\[
 R<\frac{qU+J}{q^2-1},
\]
and otherwise \(S_3=J\). The threshold belongs to \([0,1]\) for all \(0\le J\le q-1\), and integration in \(U,R\) gives
\[
 f_j:=\Pr(S_3=j-1\pmod q\mid J=j,000)=\frac{q/2+j}{q^2-1}.
\]
For \(0\le d\le q-2\), the desired probability equals \(q^{-1}(1-f_d+f_{d+1})=q/(q^2-1)\). For \(d=q-1\) it equals \(q^{-1}(1-f_{q-1}+f_0)=1/(q+1)\). Multiplying these values by the three-zero probability \(q^{-3}\) proves the displayed four-word formula. The conditional law is not uniform, because \(q/(q^2-1)\ne1/(q+1)\). Therefore the full four-block distribution cannot be iid.

**4. Independence of matrix and sensor.** All steps after the Haar two-coordinate reduction use only the trace \(q\); that reduction holds for every admissible \(A\) and \(\ell\). This establishes the claimed universality without requiring a conjugacy between the matrices.

## Verification
The standalone `verify.py` uses only Python's standard-library exact rational arithmetic. It computes the areas of all equal-strip three-word cylinders for \(q=3,4,5\) by convex polygon clipping, and computes the four-word cylinders \(000d\) for \(q=3,4,5\) independently from the linear forms \(u_2\equiv q u_1-u_0\) and \(u_3\equiv(q^2-1)u_1-q u_0\pmod1\). These exact calculations agree with both displayed formulas, including all relevant wraparound integer branches. They corroborate the separate algebraic proof for unrestricted \(q\); finite verification is not its justification.

## Relationship to prior work
Classical work on Markov partitions for toral automorphisms, including Adler's 1996 exposition, studies coding by dynamically adapted geometric cells. Here the cells are equal-width strips induced by one integer linear observable and need not form a Markov partition. Cafaro–Lord–Sun–Bollt (2015) study changes in symbolic causal and statistical structure under finite partitioning, but their principal worked example uses the tent map. Gutkin–Cvitanović–Jafari–Saremi–Han (2019/2020) study exactly computable cat-map cylinder measures using a **different integer winding-number alphabet** in the recurrence; their formulas and general method motivate precise short-block comparisons, but the inspected results do not state the equal-width trace-matched strip law here. Percival–Vivaldi (1987) is the historical origin of that winding-number coding, not a verified source of the present equal-strip theorem. A search of indexed analogous results did not identify a statement implying this explicit three-to-four-block transition, but a search alone is not a proof of historical priority.

## Limitations
No independence is asserted for nonconsecutive triples, arbitrary symbols at five or more times, other bin numbers than the trace, or other partitions. This result does not classify complete cylinder distributions of arbitrary lengths or give the full entropy rate. Historical priority against older unindexed coordinate-quantization computations and the inaccessible full text of Percival–Vivaldi (1987) remains a genuine risk. The computational verifier checks finite examples only. No independent mathematical audit has been performed.

## References
1. R. L. Adler, *Symbolic Dynamics and Markov Partitions*, arXiv:math/9607214v1 (public 1996-07-02), https://arxiv.org/abs/math/9607214.
2. C. Cafaro, W. M. Lord, J. Sun and E. M. Bollt, *Causation entropy from symbolic representations of dynamical systems*, arXiv:1507.07262v1 (public 2015-07-11), https://arxiv.org/abs/1507.07262.
3. B. Gutkin, L. Han, R. Jafari, A. Saremi and P. Cvitanović, *Linear encoding of the spatiotemporal cat*, arXiv:1912.02940v1 (public 2019-12-06), https://arxiv.org/abs/1912.02940.
4. I. Percival and F. Vivaldi, *A linear code for the sawtooth and cat maps*, Physica D **27** (1987), 373–386, DOI:10.1016/0167-2789(87)90037-6 (bibliographic record and abstract examined; full text not obtained).
