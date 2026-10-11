# Sharp finite-dimensional eighth moment for fourth-root coordinate characters
## Finding
For every integer \(n\ge2\), let \(G_n=(\mathbb Z/4\mathbb Z)^n\) with normalized counting measure and coordinate characters
\[
r_j(x_1,\ldots,x_n)=i^{x_j}.
\]
For every \(a_1,\ldots,a_n\in\mathbb C\),
\[
\left\|\sum_{j=1}^n a_jr_j\right\|_8
\le
\left(24-\frac{72}{n}+\frac{83}{n^2}-\frac{34}{n^3}\right)^{1/8}
\left(\sum_{j=1}^n|a_j|^2\right)^{1/2}.
\]
The constant is exact. If the coefficient vector is nonzero, equality holds exactly when all coefficient moduli are equal and the fourth powers have a common argument. Equivalently,
\[
a_j=r e^{i\theta}\eta_j,\qquad r>0,\quad \eta_j\in\{1,i,-1,-i\},
\]
for a common \(r\) and \(\theta\).

## Assumptions and scope
The measure on \(G_n\) is normalized counting measure. The result concerns the coordinate character system, not arbitrary subsets of the dual group. Exponent \(8\) is the first even moment at which the order-four relation \(r_j^4=1\) produces a resonance not present for continuously distributed Steinhaus variables.

## Proof
Put
\[
F=\sum_{j=1}^n a_jr_j,\quad
S=\sum_j|a_j|^2,\quad
Q=\sum_j|a_j|^4,\quad
R=\sum_j|a_j|^6,\quad
U=\sum_j|a_j|^8,\quad
T=\sum_j a_j^4.
\]
Expand \(F^4\overline F^4\). A monomial indexed by \(\alpha,\beta\in\mathbb Z_{\ge0}^n\), with \(|\alpha|=|\beta|=4\), survives expectation exactly when
\[
\alpha_j\equiv\beta_j\pmod4
\]
for every \(j\). Since all entries lie between \(0\) and \(4\), the surviving terms are the diagonal terms \(\alpha=\beta\), together with transfers of four copies from one coordinate to another. Collecting the diagonal multinomial types and then those order-four transfers gives
\[
\|F\|_8^8
=
24S^4-72S^2Q+18Q^2+64SR-34U+|T|^2.
\]
Now
\[
|T|^2\le Q^2,
\]
with equality exactly when all nonzero \(a_j^4\) have a common argument. Thus
\[
\|F\|_8^8\le24S^4-72S^2Q+19Q^2+64SR-34U.
\]
By homogeneity set \(S=1\) and write \(x_j=|a_j|^2\). Let \(P_k=\sum_jx_j^k\). We must maximize
\[
\Phi(x)=24-72P_2+19P_2^2+64P_3-34P_4
\]
on the probability simplex.

Fix two coordinates \(x,y\), set \(u=x+y\), \(t=xy\), and let \(A\) be the sum of squares of all other coordinates. Holding \(u\) and the other coordinates fixed,
\[
\frac{d\Phi}{dt}=144-76A-192u+60u^2+16t.
\]
The remaining coordinates have total mass \(1-u\), hence \(A\le(1-u)^2\). Therefore
\[
\frac{d\Phi}{dt}
\ge68-40u-16u^2+16t
\ge12>0
\]
for \(0\le u\le1\). Replacing any unequal pair by its average strictly increases \(\Phi\), so the unique maximizer is
\[
x_1=\cdots=x_n=\frac1n.
\]
Substitution gives
\[
\max\Phi=24-\frac{72}{n}+\frac{83}{n^2}-\frac{34}{n^3}.
\]
Strict smoothing forces equal moduli at equality, while equality in \(|T|^2\le Q^2\) forces a common fourth-power phase. Conversely those conditions make every step sharp.

## Verification
A standalone exact-arithmetic checker expands the normalized eighth moment directly over all \(4^n\) points for selected coefficient vectors, verifies the exact moment identity on five cases, and verifies the sharp equality family for \(2\le n\le6\). It reports `VERIFY_OK identity_cases=5 extremizers=5 max_states=4096`. These finite checks corroborate the algebra; the proof above establishes the result for every \(n\ge2\).

## Relationship to prior work
Bourgain and Lewko place character systems in the Sidon, Rademacher-Sidon, and \(\psi_2\) framework; their paper is classified primarily under 43A46 and its first public preprint appeared on 2015-04-21. The present statement is a sharp finite-dimensional \(\Lambda(8)\)-type computation for a specific finite-order character system, including its equality class.

Nayar and Oleszkiewicz derive optimal even-moment Khinchine-type inequalities using ultra log-concavity, while König and Kwapień treat sums of independent rotationally invariant random vectors. Those frameworks motivate comparison with sharp moment inequalities but do not, in the inspected material, supply the discrete fourth-root resonance identity above. The term \(|\sum_j a_j^4|^2\) is the feature that determines the phase constraint here.

## Limitations
No assertion is made for other cyclic orders, other even exponents, or arbitrary character subsets. The closest harmonic-analysis source was inspected in open form; one broad Khinchine source was compared through its open abstract and metadata rather than a complete text, so an older equivalent probabilistic formulation remains a residual literature risk. Finite checker output is not a substitute for the analytic proof.

## References
1. J. Bourgain and M. Lewko, *Sidonicity and variants of Kaczmarz's problem*, arXiv:1504.05290, first submitted 2015-04-21; Annales de l'Institut Fourier 67 (2017), 1321-1352, DOI 10.5802/aif.3111.
2. P. Nayar and K. Oleszkiewicz, *Khinchine type inequalities with optimal constants via ultra log-concavity*, Positivity 16 (2012), 359-371, DOI 10.1007/s11117-011-0130-z.
3. H. König and S. Kwapień, *Best Khintchine type inequalities for sums of independent, rotationally invariant random vectors*, Positivity 5 (2001), 115-152, DOI 10.1023/A:1011434208929.
