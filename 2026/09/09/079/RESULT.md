# Central-unipotent degree-7 Cayley lifts in SL(2,q): disconnected Borel family and an exact Ramanujan witness in SL(2,7)

## Definitions

For a prime \(q\ge 7\), let \(G_q=\mathrm{SL}(2,q)\), let \(z=-I\), and let \(U_q\) be the nonidentity trace-two unipotents. Let \(\mathcal C_q\) consist of symmetric seven-element sets of the form \(\{z\}\cup A\cup A^{-1}\) with three distinct representatives from \(U_q\). For such a set \(S\), write \(G(S)=\operatorname{Cay}(G_q,S)\) and \(X(S)\) for its bipartite double cover.

## Result

The class \(\mathcal C_q\) is mixed.

1. For every prime \(q\ge 7\), the set
\[
S_B=\{-I,u(\pm1),u(\pm2),u(\pm3)\},\qquad u(a)=\begin{pmatrix}1&a\\0&1\end{pmatrix},
\]
lies in \(\mathcal C_q\) and generates the order-\(2q\) subgroup \(\langle u(1)\rangle\times\langle -I\rangle\). Hence both the Cayley graph and its bipartite double cover are disconnected.

2. In \(\mathrm{SL}(2,7)\), let
\[
S_R=\{(6,0,0,6),(4,2,6,5),(2,4,5,0),(1,4,0,1),(5,5,1,4),(0,3,2,2),(1,3,0,1)\},
\]
with matrices written row-major modulo 7. This set lies in \(\mathcal C_7\), generates all 336 elements of \(\mathrm{SL}(2,7)\), and its 672-vertex bipartite double cover is 7-regular Ramanujan.

## Exact spectral certificate

Let \(A\) be the 336 by 336 adjacency matrix of \(G(S_R)\), and put \(\mu=4.89\). Exact fraction-free elimination on
\[
M_{\mathrm{lo}}=100A+489I
\]
and
\[
M_{\mathrm{up}}=16430400I-3360000A+21436J
\]
gives positive definiteness. The first matrix implies \(\lambda_{\min}(A)>-4.89\). For every vector perpendicular to the constants, the \(J\) term in the second matrix vanishes, so positive definiteness implies \(\lambda_2(A)<4.89\). Since \(4.89<2\sqrt6\), the bipartite double cover is Ramanujan.

A fully independent exact check reconstructs the same adjacency matrix, computes its characteristic polynomial, and factors it as
\[
(x-7)(x-2)^7(x-1)^7(x+2)^{24}(x^2+4x-3)^{24}(x^3-7x-2)^6
\]
\[
\cdot(x^4+x^3-11x^2-3x+16)^{24}(x^5-4x^4-12x^3+34x^2+27x+2)^7
\]
\[
\cdot(x^6-14x^4-4x^3+41x^2+12x-28)^6
\]
\[
\cdot(x^8-14x^7+63x^6-48x^5-365x^4+838x^3-223x^2-404x-52)^8.
\]
Rational root isolation places the largest nontrivial eigenvalue below \(15913/3256<4.89\) and the least eigenvalue above \(-4.89\).

The committed integer vector in `artifacts/rayleigh_vec.json` remains a useful exact cross-check: its Rayleigh quotient is \(55177273021248/11289966448320\approx4.8872840565\). Because a single test vector gives a lower bound on \(\lambda_2(A)\), not an upper bound, it is not used as the Ramanujan upper certificate.

## Reproducibility

- `python3 artifacts/verify.py` rebuilds the group, set membership, connectivity and numerical spectrum.
- `python3 artifacts/bareiss_cert.py lo` and `python3 artifacts/bareiss_cert.py up` rebuild the exact positive-definiteness certificates from the explicit witness set, without external scratch state.
- `python3 artifacts/exact_rayleigh.py` checks the committed integer Rayleigh vector and labels it correctly as a lower-bound cross-check.

## Scope

This is an existence/refutation result for a constrained generator class. It is not a census of \(\mathcal C_7\), and no spectral claim is made for primes greater than 7.
