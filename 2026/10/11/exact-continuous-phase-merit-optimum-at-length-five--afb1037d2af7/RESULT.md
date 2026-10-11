# Exact continuous-phase merit optimum at length five
## Finding
For every polynomial
\[
P(z)=c_0+c_1z+c_2z^2+c_3z^3+c_4z^4,
\qquad |c_j|=1,
\]
on \(\mathbb T\), with normalized Haar measure,
\[
\|P\|_4^4\ge 29.
\]
Equality holds exactly for
\[
(c_0,c_1,c_2,c_3,c_4)=\lambda(1,\eta,\eta^2,-\eta^3,\eta^4),
\qquad |\lambda|=|\eta|=1.
\]
If \(C_k=\sum_{j=0}^{4-k}c_{j+k}\overline{c_j}\) denotes the aperiodic autocorrelation, then the base energy \(E=\sum_{k=1}^4|C_k|^2\) therefore has the exact minimum \(2\), and the merit factor \(25/(2E)\) has the exact maximum \(25/4\).

## Assumptions and scope
The coefficient phases are unrestricted: each \(c_j\) may be any point of the complex unit circle. The norm is the normalized \(L^4\)-norm on the continuous unit circle, not a finite-grid norm. Scalar multiplication and linear phase modulation preserve all autocorrelation magnitudes and are the only symmetries used in the equality classification.

## Proof
Parseval applied to \(|P|^2\) gives
\[
\|P\|_4^4=25+2\sum_{k=1}^4|C_k|^2.
\]
Because \(|C_4|=1\), it is enough to prove
\[
|C_1|^2+|C_2|^2+|C_3|^2\ge1.
\]
Use scalar and linear-phase invariance to normalize the first successive phase ratio to \(1\). Write the remaining successive ratios as \(p,q,r\in\mathbb T\). Then the coefficient vector is \((1,1,p,pq,pqr)\), and
\[
C_1=1+p+q+r,\qquad C_2=p+pq+qr,\qquad |C_3|=|1+r|.
\]
Fix \(q=e^{i\beta}\) and \(r=e^{i\gamma}\). Minimization over \(p\in\mathbb T\) gives
\[
|C_1|^2+|C_2|^2+|C_3|^2=K-2|L|,
\]
where, with \(x=\cos\beta\), \(y=\cos\gamma\), and \(z=\cos(\beta-\gamma)\),
\[
K=9+4x+4y+2z,
\qquad
|L|^2=7+6x+6y+2z+4xy.
\]
Since \(K\ge2\), it suffices to prove \((K-1)^2\ge4|L|^2\). After division by \(4\), the difference is
\[
D=4x^2+4xy+4xz+10x+4y^2+4yz+10y+z^2+6z+9.
\]
Put
\[
A=\cos\frac{\beta+\gamma}2,
\qquad
B=\cos\frac{\beta-\gamma}2.
\]
Using \(x+y=2AB\), \(xy=A^2+B^2-1\), and \(z=2B^2-1\), one obtains the exact factor reduction
\[
D=4Q(A,B),
\]
with
\[
Q(A,B)=(4B^2-1)A^2+B(4B^2+3)A+B^4+B^2+2.
\]
By the symmetry \(Q(A,B)=Q(-A,-B)\), assume \(B\ge0\). If \(0\le B\le1/2\), then \(Q\) is concave in \(A\), so its minimum on \([-1,1]\) is an endpoint; the smaller endpoint is \(A=-1\), where
\[
Q(-1,B)=(1-B)\bigl((1-B)^2+B^2(2-B)\bigr)\ge0.
\]
If \(1/2\le B\le1\), then \(Q\) is convex. Its vertex lies at or to the left of \(-1\), because
\[
B(4B^2+3)-2(4B^2-1)
=1+(1-B)\bigl(1+4B(1-B)\bigr)>0.
\]
Hence the minimum is again \(Q(-1,B)\ge0\). This proves the lower bound.

Equality in \(Q\ge0\) forces \((A,B)=(-1,1)\) or \((1,-1)\), hence \(q=r=-1\). The remaining expression becomes
\[
|C_1|^2+|C_2|^2+|C_3|^2=|p-1|^2+1,
\]
so equality further forces \(p=1\). Undoing the normalization gives exactly the stated family \(\lambda(1,\eta,\eta^2,-\eta^3,\eta^4)\).

## Verification
The proof is algebraic and does not depend on finite enumeration. The accompanying checker expands the key trigonometric reduction symbolically, verifies the endpoint and vertex identities, evaluates the extremal family, and performs an additional numerical stress test. The numerical test is corroborative only; the universal inequality and equality classification are established by the analytic proof above.

## Relationship to prior work
Neuwirth's phase-extremal work on trigonometric polynomials treats maximum-modulus and Sidon-type questions, and explicitly places this class of phase-choice problems in harmonic analysis. Borwein and Ferguson define the same aperiodic base energy and merit factor used here. Their 2005 table reports the value \(E=2.000\) at length five as the lowest value found by stochastic optimization, while their surrounding text describes statistical evidence for global optimality rather than an analytic proof. The present result certifies that table entry exactly over the full continuous phase torus and classifies every minimizer.

## Limitations
This result is specific to five coefficients and the fourth moment. It does not determine the continuous-phase merit optimum at longer lengths, nor does it imply analogous rigidity for other moments. Older polyphase/Barker literature may contain equivalent small-length statements under different normalization; the literature checks recorded in the review found the numerical candidate and the general even-moment framework, but no prior analytic global proof with the same equality classification.

## References
1. S. Neuwirth, “The maximum modulus of a trigonometric trinomial,” HAL hal-00135804v1, first public 2007-03-08; 2000 MSC includes primary 42A05.
2. P. Borwein and R. Ferguson, “Polyphase Sequences With Low Autocorrelation,” IEEE Transactions on Information Theory 51 (2005), 1564–1567, DOI 10.1109/TIT.2004.842778.
3. S. Neuwirth, “Metric unconditionality and Fourier analysis,” arXiv:math/9707211, first public 1997-07-28.
