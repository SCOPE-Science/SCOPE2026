# Every partial migration rate increases two-season growth on a directed three-patch cycle

## Finding
Consider exactly three habitat patches with unconditional clockwise migration. Suppose the patch growth matrices in consecutive seasons are reciprocal: \(D_1=D=\operatorname{diag}(x,y,z)\) and \(D_2=\kappa D^{-1}\), where \(x,y,z,\kappa>0\). Thus every patch has the same isolated two-season growth multiplier \(\kappa\). With clockwise permutation \(C e_1=e_2\), \(C e_2=e_3\), \(C e_3=e_1\), and migration fraction \(d\in[0,1]\), set \(M(d)=(1-d)I+dC\) and \(P(d)=M(d)D_2M(d)D_1\).

**Complete strict-growth classification:**
\[
\rho(P(0))=\rho(P(1))=\kappa,\qquad
\rho(P(d))>\kappa\quad\text{for every }0<d<1
\]
if and only if \(x,y,z\) are not all equal. If \(x=y=z\), then \(\rho(P(d))=\kappa\) for every \(d\in[0,1]\). In the heterogeneous case, every global optimizer of the period-two linear growth multiplier lies strictly in the interior \((0,1)\); existence follows by continuity. Uniqueness of that optimizer is not claimed.

The core all-parameter identity, with \(Q(d)=P(d)/\kappa\), is
\[
\det(I-Q(d))=-d^3(1-d)\left(
\frac{x}{y}+\frac{y}{x}+\frac{x}{z}+\frac{z}{x}
+\frac{y}{z}+\frac{z}{y}-6\right).
\]
It gives a necessary-and-sufficient heterogeneity condition for strict improvement at **each** partial migration fraction, rather than a counterexample at one arbitrarily chosen rate.

Among arbitrary nonnegative two-patch column-stochastic migration kernels with the same kernel in both seasons, no strictly intermediate fraction can beat both endpoints for positive two-season diagonal growth. Thus three patches are the smallest dimension admitting the strict-interior phenomenon. The two-patch boundary uses the standard symmetric-similarity/norm-convexity argument and is included for context rather than asserted as a separate novelty claim.

## Assumptions and scope
Population abundance is a nonnegative column vector immediately before reproduction. Each season consists of reproduction by its positive diagonal matrix followed by movement with the *same* column-stochastic \(M(d)\). Two seasons repeat indefinitely. Movement uses a single directed three-cycle with no migration mortality. The long-run growth factor per complete two-season period is the Perron spectral radius \(\rho(P(d))\), and the per-season factor is its positive square root. There are no density effects, extinction events, nonlinear demographic responses, changing dispersal fractions, or spatially variable migration costs. Every inequality holds for all real \(x,y,z,\kappa>0\) and all real \(d\) in the specified interval, without genericity assumptions beyond the explicit non-equality of the three growth values.

## Proof
Put \(a=1-d\), \(b=d\), and \(D=\operatorname{diag}(x,y,z)\). Factoring out \(\kappa\) leaves \(Q=M D^{-1}M D\). Direct multiplication yields the positive-entry representation
\[
Q=\begin{pmatrix}
 a^2 & b^2y/z & ab(1+z/x)\\
 ab(1+x/y) & a^2 & b^2z/x\\
 b^2x/y & ab(1+y/z) & a^2
\end{pmatrix}.
\]
For \(0<d<1\), all nine entries are strictly positive. Expanding the three-by-three determinant, inserting \(a+b=1\), and collecting reciprocal ratios gives
\[
\det(I-Q)=-d^3(1-d)H,\qquad
H=\sum_{\{u,v\}\subset\{x,y,z\}}
\left(\frac{u}{v}+\frac{v}{u}-2\right).
\]
Each summand is \((u-v)^2/(uv)\). Hence \(H\ge0\), with equality if and only if \(x=y=z\). For nonconstant \(D\) and \(0<d<1\), \(\det(I-Q)<0\). The real characteristic polynomial \(f(\lambda)=\det(\lambda I-Q)\) satisfies \(f(1)<0\) and \(f(\lambda)\to+\infty\) as \(\lambda\to+\infty\); therefore it has a real eigenvalue strictly greater than one. Since \(Q\) is nonnegative, \(\rho(Q)\) is at least the modulus of this eigenvalue, so \(\rho(Q)>1\).

At \(d=0\), \(Q=I\). At \(d=1\), \(Q=CD^{-1}CD\) is a positive weighted permutation for the cycle \(C^2\). The product of its three positive weights equals one, so its spectral radius is one. If \(D=xI\), then \(Q=M^2\); column stochasticity gives \(\rho(M)=1\) and therefore \(\rho(Q)=1\) for all \(d\). This proves the exact classification.

For the dimension boundary, let \(S\) be any nonnegative two-by-two column-stochastic kernel and \(M(d)=(1-d)I+dS\). If both off-diagonal entries are positive, a positive diagonal similarity symmetrizes \(S\). Since positive diagonal fitness matrices commute with this similarity, the two-season product is similar to a positive semidefinite symmetric product. Its square-root spectral radius becomes the Euclidean operator norm of a matrix affine in \(d\), and hence is convex in \(d\). A convex function on \([0,1]\) never exceeds its larger endpoint value. If one off-diagonal entry is zero, \(S\) and \(M(d)\) are triangular; the spectral radius of the period matrix is the maximum of two nonnegative diagonal terms of the form \((1-d+dS_{ii})^2(D_1)_{ii}(D_2)_{ii}\), each bounded by its value at \(d=0\). The one-patch case is immediate.

## Verification
A standalone standard-library verifier, `verify.py`, constructs the Laurent-polynomial ring with variables \(x,y,z,d\), multiplies the two-season matrices symbolically and checks the complete determinant identity coefficient-for-coefficient. Its exact symbolic difference is zero. It also checks 448 rational cases (300 strict cases and 148 boundary/homogeneous cases). The generated certificate is `certificate.json`.

For a compact independent example, take \(D_1=\operatorname{diag}(1,1,2)\), \(D_2=\operatorname{diag}(2,2,1)\), \(\kappa=2\), and \(d=1/2\). The period matrix is
\[
P(1/2)=\begin{pmatrix}1/2&1/4&3/2\\1&1/2&1\\1/2&3/4&1/2\end{pmatrix}.
\]
Its characteristic polynomial is \(\lambda^3-\tfrac32\lambda^2-\lambda-\tfrac12\), which is negative at \(\lambda=2\) and positive for all sufficiently large real \(\lambda\). Hence its Perron root is strictly greater than two, while both endpoint roots equal two. The universal theorem follows from the determinant proof, not this example or the finite tests.

## Relationship to prior work
Schreiber and Li (arXiv:1007.5267, 2010), model (2.1), study the same unconditional dispersal interpolation. Their Appendix A concluding remark **already exhibits** a three-cycle with one nonuniform growth diagonal and a growth advantage at \(d=1/2\). That example is prior art, not newly claimed. Their symmetrizable-migration results and the displayed example do not state or prove the classification of **every** positive reciprocal seasonal fitness profile at **every** intermediate fraction, nor the exact heterogeneity discriminant above. Thus the present result strengthens the isolated nonreversible example into an all-parameter, all-rate law. The overlapping special case is explicitly excluded from any novelty attribution.

Kleinhans and Jonsson (arXiv:1011.1109, 2010) study how asymmetry affects stochastic occupancy and extinction in spatial metapopulations; their dynamics and objective differ from the deterministic two-season monodromy. Artzy-Randrup and Stone (2010) analyze network cycles and persistence thresholds, but their main cycles analysis does not supply this reciprocal-fitness two-season spectral identity. A broader matrix-inequality or periodic-dispersal theorem not found in the searches could still imply this classification; independent literature review remains advisable.

## Limitations
The conclusion is confined to a directed three-cycle with phase-independent, lossless movement and exactly reciprocal seasonal diagonal fitnesses. It does not imply that all asymmetric dispersal, or all seasonally varying populations, benefit from every intermediate migration fraction. The result concerns deterministic low-density growth, not extinction probability, nonlinear persistence, or evolutionary stability in a resident-invader model. It guarantees an interior optimum but neither locates it nor claims it is unique. This is an analytical mathematical result with self-review only; no independent scientific audit has been performed.

## References
- Schreiber, S. J., and Li, C.-K., *Evolution of unconditional dispersal in periodic environments*, arXiv:1007.5267v1, first public 2010-07-29; Journal of Biological Dynamics 5 (2011), 120–134, DOI: 10.1080/17513758.2010.525667. Model §2, Theorem 2, Appendix A final remark.
- Artzy-Randrup, Y., and Stone, L., *Connectivity, Cycles, and Persistence Thresholds in Metapopulation Networks*, PLoS Computational Biology 6 (2010), e1000876, DOI: 10.1371/journal.pcbi.1000876, first public 2010-08-05. Sections on Cycles and Nonidentical Patches.
- Kleinhans, D., and Jonsson, P. R., *On the impact of dispersal asymmetry on metapopulation persistence*, arXiv:1011.1109, first public 2010-11-04. Sections 2–4.
