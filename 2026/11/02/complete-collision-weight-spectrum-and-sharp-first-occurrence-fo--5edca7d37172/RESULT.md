# Complete collision-weight spectrum and sharp first occurrence for periodic Rule 30

## Finding

Let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be the simultaneous elementary Rule 30 map on *indexed*, cyclic rings of length \(n\ge1\):
\[
(F_n(x))_i=x_{i-1}\oplus(x_i\lor x_{i+1}),\qquad i\in\mathbb Z/n\mathbb Z.
\]
All ring positions are indexed; two rotated predecessors count separately. Define the collision-weight coefficients
\[
C_{n,k}=\#\{(x,x'):\ x,x'\in\{0,1\}^n,\ x\ne x',\ F_n(x)=F_n(x'),\ |F_n(x)|_1=k\}.
\]
The pairs are *ordered*. For \(n\ge1\), their complete bivariate generating function is
\[
\boxed{\mathcal C(z,u)=\sum_{n\ge1}\sum_{k=0}^n C_{n,k}z^nu^k=-z\,\frac{\partial}{\partial z}\log R(z,u),}
\]
where the formal power series logarithm is valid because \(R(0,u)=1\), and
\[
\boxed{R(z,u)=(1-uz)\bigl(1-z-(u^2+u^3)z^3\bigr)\bigl(1+(u-1)z+(u^2-u)z^2\bigr).}
\]
Equivalently, the logarithmic derivative is the explicit rational expression
\[
\mathcal C(z,u)=z\left[\frac{u}{1-uz}+\frac{1+3(u^2+u^3)z^2}{1-z-(u^2+u^3)z^3}-\frac{(u-1)+2(u^2-u)z}{1+(u-1)z+(u^2-u)z^2}\right].
\]

There is a collision output of Hamming weight \(k\) on *some* nonempty cyclic ring **if and only if**
\[
k=0\quad\text{or}\quad k\ge3\text{ and }k\not=5.
\]
More strongly, the **smallest permissible ring circumference** for such a collision is
\[
\boxed{n_{\min}(0)=1,\qquad n_{\min}(k)=k+2(k\bmod3)\ \text{for }k\ge3,\ k\ne5.}
\]
No circumference works for \(k=1,2,5\). Thus the obstruction at output weight five is global, not just a short-ring artifact. These results concern one update, not temporal iteration.

## Assumptions and scope

The alphabet is binary; the local rule is \(a\oplus(b\lor c)\), with indices reduced modulo \(n\), including the repeated-neighbor convention for \(n=1,2\). The Hamming weight refers to the **output**. No identification by rotation, complementation, or reversal is made. Every result is exact for all positive integers \(n\). In \(C_{n,k}\), pairs of distinct predecessors with a common output are counted in both orders; if an output has \(m\) predecessors, it contributes \(m(m-1)\) to its weight coefficient.

## Proof

**1. Paired de Bruijn graph and traces.** Let the four two-bit states be \(0,1,2,3\), representing \(00,01,10,11\). From state \(s=2a+b\) to \(t=2b+c\), give a directed edge of weight \(u^{f(a,b,c)}\), where \(f(a,b,c)=a\oplus(b\lor c)\). Define the \(4\times4\) matrix \(B(u)\) by adding these weights. Define the \(16\times16\) matrix \(M(u)\), indexed by ordered pairs of two-bit states, by placing the weight \(u^r\) on a simultaneous pair of edges exactly when both output bits equal \(r\). Multiple edges, if any, have weights added.

Closed \(n\)-edge walks in this de Bruijn graph biject with indexed cyclic input words, even at \(n=1,2\), by reading their overlapping two-bit labels. Hence \(\operatorname{tr}B(u)^n\) is the output-weight enumerator of all predecessors, while \(\operatorname{tr}M(u)^n\) is the weight enumerator of *ordered* input pairs with equal output. The diagonal pairs contribute exactly \(\operatorname{tr}B(u)^n\). Therefore
\[
\sum_kC_{n,k}u^k=\operatorname{tr}M(u)^n-\operatorname{tr}B(u)^n.
\]

**2. Exact determinant identity.** Direct polynomial computation from the explicitly defined matrices gives
\[
\det(I-zB(u))=(1-(u+1)z)\bigl(1+(u-1)z+(u^2-u)z^2\bigr)
\]
and
\[
\det(I-zM(u))=\det(I-zB(u))R(z,u).
\]
These are exact polynomial identities in \(\mathbb Z[z,u]\), not numerical interpolations. They can be certified using the bundled standard-library checker: each determinant has \(z\)-degree at most its matrix order, and its coefficient of \(z^j\) has \(u\)-degree at most \(j\), because each selected matrix edge has output weight either \(1\) or \(u\). The checker computes all integer characteristic coefficients via the Faddeev--LeVerrier recursion at every \(u\in\{0,1,\ldots,16\}\). Since the difference of either side has \(u\)-degree at most \(16\) in every coefficient, agreement at these 17 distinct integer values proves the identities over \(\mathbb Z[u]\) for each coefficient. No unbounded computation is assumed.

For any square matrix \(A\), the formal identity
\[
-z\frac{d}{dz}\log\det(I-zA)=\sum_{n\ge1}\operatorname{tr}(A^n)z^n
\]
now yields the boxed bivariate generating function by subtracting the two traces.

**3. Complete cycle-weight classification.** The paired graph has 12 *off-diagonal* vertices \((s,t)\) with \(s\ne t\), and precisely 20 directed edges between them. Rule 30 is left-permutive: knowing an output bit and the two input bits immediately to its right determines the next input bit to its left. Thus, if two common-output periodic predecessors ever agree on adjacent positions, they agree at every position. Consequently a distinct predecessor pair corresponds to a closed walk wholly within the off-diagonal graph, and conversely every such closed walk gives distinct predecessors with identical output.

The graph has exactly ten simple directed cycles, counted up to cyclic rotation of their vertex lists. Their \((\text{length},\text{number of one-output edges},\text{multiplicity})\) census is
\[
(1,0,2),\ (3,3,2),\ (4,3,2),\ (6,4,1),\ (7,4,2),\ (8,4,1).
\]
The graph definition above makes this finite assertion fully reproducible; `verify.py` enumerates all canonical simple directed cycles without a length cutoff. Every closed directed walk decomposes into simple directed cycles. Since all edge weights are nonnegative, its total output-one count is \(3a+4b\), for nonnegative integers \(a,b\), unless it is zero. This excludes exactly the positive counts \(1,2,5\).

Conversely, the weight-three, length-three simple cycle through \((0,1)\) and the weight-four, length-six simple cycle through \((0,1)\) can be concatenated in arbitrary order. They correspond, for example, to the two colliding input pairs `001` and `010` (common output `111`) and `001010` and `010001` (common output `011011`). Hence every integer \(3a+4b\) with \(a+b>0\) occurs as the output weight of a collision. The zero-weight case is witnessed by `0` and `1` on a ring of length one, both mapping to `0`.

**4. Sharp first circumference.** Every positive-weight simple cycle of weight three has length at least three, and every weight-four simple cycle has length at least six; a zero-weight cycle cannot reduce length. Thus any collision with output weight \(k=3a+4b\) has
\[
n\ge3a+6b=k+2b.
\]
Writing \(r=k\bmod3\in\{0,1,2\}\), the congruence forces \(b\equiv r\pmod3\), hence \(b\ge r\) and \(n\ge k+2r\). For any allowable positive \(k\), choosing \(b=r\) and \(a=(k-4r)/3\) gives nonnegative integers; concatenating the aforementioned two cycles achieves exactly this lower bound. The weight-zero one-cell witness establishes \(n_{\min}(0)=1\). This proves the stated necessary and sufficient support and the exact minimum lengths.

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter. The program (i) constructs both weighted matrices and verifies their full determinant polynomials at 17 integer specializations, promoted to polynomial identities by the degree bound; (ii) independently enumerates all cyclic Rule 30 input words up to length 14 and matches each exact output-weight coefficient against the derived rational series; (iii) exhaustively enumerates all simple off-diagonal cycles and checks the ten-cycle census; and (iv) independently computes the shortest graph-walk collision lengths for every output weight through 45 and compares them with the theorem. Successful replay prints `VERIFY_OK`. These finite tests support, but are not substitutes for, the all-length graph and polynomial arguments above.

The first few ordered-collision polynomials are
\[
\begin{aligned}
\sum_k C_{3,k}u^k&=2+6u^3,\\
\sum_k C_{6,k}u^k&=2+12u^3+6u^4+6u^6,\\
\sum_k C_{9,k}u^k&=2+18u^3+36u^4+36u^6+18u^7+6u^9.
\end{aligned}
\]

## Relationship to prior work

Jen's rule-matrix/preimage framework (1989) and Wolfram's *A New Kind of Science* note on Rule 30 inversion (2002) provide prior general machinery. Wolfram explicitly discussed the prevalence of zero-, one-, or two-predecessor periodic configurations and gave a direct inverse algorithm; those known facts are not claimed as new. An accessible discussion of closed-ring inversions separately exhibits the threefold all-one case. Powley and Stepney (2010) count predecessors of *homogeneous* configurations by de Bruijn methods. The complete output-Hamming-weight collision series, the forbidden weights \(1,2,5\), and the sharp first circumference for every allowed weight are the present assertions. A previous exact *unweighted* image-size formula does not supply the weight-conditioned distribution or the sharp minimum support law without additional analysis.

## Limitations

This is a theorem about one-step collisions on binary indexed finite rings only. It is not a theorem about Rule 30's central column, multiple updates, recovery complexity, practical cryptographic security, or the number of predecessor pairs when rotations are identified. The theorem establishes same-rule mathematical statements without claiming independent validation or historical-priority certification. A 2009 thesis by Edward Powley and parts of Jen's technical report could not be fully inspected through the accessible interfaces; an undiscovered equivalent earlier output-weight result remains a priority risk.

## References

- Erica Jen, *Rule matrices, degree vectors, and preimages for cellular automata*, Los Alamos report LA-UR-90-627, report cataloged as 1989, https://digital.library.unt.edu/ark:/67531/metadc1189848/ .
- Stephen Wolfram, *A New Kind of Science*, published May 14, 2002, chapter 10 notes on Rule 30 cryptography, https://www.wolframscience.com/nks/notes-10-10--cryptographic-properties-of-rule-30/ .
- *Global Reversibility of Cellular Automata*, MathPages, https://www.mathpages.com/home/kmath439/kmath439.htm (undated web discussion, date not used as the source anchor).
- Edward J. Powley and Susan Stepney, *Counting Preimages of Homogeneous Configurations in 1-Dimensional Cellular Automata*, Journal of Cellular Automata 5 (2010), 353–381, https://pure.york.ac.uk/portal/en/publications/counting-preimages-of-homogeneous-configurations-in-1-dimensional/ .
