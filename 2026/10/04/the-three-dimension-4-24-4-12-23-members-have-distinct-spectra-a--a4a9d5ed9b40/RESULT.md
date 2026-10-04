# The three dimension-\(4\) \([24,4,12]_{23}\) members have distinct spectra and support hierarchies
## Finding

Specialize the cyclic-code construction displayed in Table 1 of Zhang–Cao–Luo to
\[
q=23,\qquad n=24.
\]
Let \(\beta\) be a primitive \(24\)-th root of unity in \(\mathbb F_{23^2}\), let \(M_i(x)\) denote the minimal polynomial of \(\beta^i\) over \(\mathbb F_{23}\), and put
\[
C_I=\left\langle
\left(\prod_{i\in I}M_i(x)\right)
\left(\prod_{j=4}^{11}M_j(x)\right)
\right\rangle
\subseteq \mathbb F_{23}[x]/(x^{24}-1).
\]
For the three two-element choices \(I=\{1,2\},\{1,3\},\{2,3\}\), the source table records the common parameters
\[
[24,4,12]_{23}.
\]

These three codes have different complete Hamming spectra:
\[
\begin{aligned}
W_{\{1,2\}}(z)
&=1+220z^{12}+352z^{15}+12408z^{18}+70576z^{21}+196284z^{24},\\
W_{\{1,3\}}(z)
&=1+44z^{12}+792z^{16}+792z^{18}+27060z^{20}+86064z^{22}+165088z^{24},\\
W_{\{2,3\}}(z)
&=1+44z^{12}+7920z^{20}+3168z^{21}+85800z^{22}+78672z^{23}+104236z^{24}.
\end{aligned}
\]
Their generalized Hamming weight hierarchies are, respectively,
\[
(12,18,21,24),\qquad(12,20,22,24),\qquad(12,22,23,24).
\]
Consequently the three parameter-identical codes are pairwise monomially inequivalent.

## Assumptions and scope

The specialization \(q=23,n=24\) is admissible because \(24\mid(23+1)\). The notation above fixes the exact finite objects independently of any choice of representation of the quadratic extension.

For reproducibility, use
\[
\mathbb F_{23^2}=\mathbb F_{23}(u),\qquad u^2=5,
\]
where \(5\) is a quadratic nonresidue modulo \(23\), and take
\[
\beta=4+7u.
\]
Then \(\beta\) has multiplicative order \(24\). Since \(\beta^{23}=\beta^{-1}\), each \(M_i\) is
\[
M_i(x)=(x-\beta^i)(x-\beta^{-i}).
\]
The resulting polynomials are
\[
\begin{array}{lll}
M_1=x^2+15x+1,&M_2=x^2+7x+1,&M_3=x^2+18x+1,\\
M_4=x^2+22x+1,&M_5=x^2+20x+1,&M_6=x^2+1,\\
M_7=x^2+3x+1,&M_8=x^2+x+1,&M_9=x^2+5x+1,\\
M_{10}=x^2+16x+1,&M_{11}=x^2+8x+1.&
\end{array}
\]

## Proof

Multiplying the indicated factors gives the three degree-\(20\) generator polynomials. Written from constant term upward, they are
\[
\begin{aligned}
g_{\{1,2\}}={}&(1,5,2,5,1,0,0,0,1,5,2,5,1,0,0,0,1,5,2,5,1),\\
g_{\{1,3\}}={}&(1,16,3,9,4,9,3,16,1,0,0,0,1,16,3,9,4,9,3,16,1),\\
g_{\{2,3\}}={}&(1,8,18,21,13,14,8,4,2,12,3,12,2,4,8,14,13,21,18,8,1).
\end{aligned}
\]
Each divides \(x^{24}-1\), so the four shifts \(g,xg,x^2g,x^3g\) form a generator matrix of rank \(4\).

There are \(23^4=279841\) messages for each code. Exhausting them gives exactly the three displayed weight enumerators. In every case the least nonzero weight is \(12\), agreeing with the source table.

For the generalized weights, let \(G\) be one of the \(4\times24\) generator matrices and regard its nonzero columns as a projective multiset in \(\mathrm{PG}(3,23)\). For an \([n,4]\) code,
\[
d_r=n-\max_U N(U),
\]
where \(U\) ranges over vector subspaces of dimension \(4-r\) and \(N(U)\) is the number of generator columns contained in \(U\), with multiplicity.

Exact column reduction gives the following projective data:
\[
\begin{array}{c|c|c|c}
I&\text{distinct projective points}&\text{point multiplicity}&
\text{largest line count}\\ \hline
\{1,2\}&8&3&6\\
\{1,3\}&12&2&4\\
\{2,3\}&24&1&2.
\end{array}
\]
The largest hyperplane count is \(12\) in all three cases, equivalently \(d_1=12\). Therefore
\[
\begin{aligned}
C_{\{1,2\}} &: (d_1,d_2,d_3,d_4)=(12,18,21,24),\\
C_{\{1,3\}} &: (d_1,d_2,d_3,d_4)=(12,20,22,24),\\
C_{\{2,3\}} &: (d_1,d_2,d_3,d_4)=(12,22,23,24).
\end{aligned}
\]
A monomial equivalence preserves the ordinary Hamming weight enumerator, so the three different enumerators prove pairwise monomial inequivalence.

## Verification

`artifacts/verify.py` uses only the Python standard library. It reconstructs \(\mathbb F_{23^2}\), checks that \(\beta=4+7u\) has order \(24\), reconstructs all eleven minimal polynomials, multiplies the three source-family generators, and verifies divisibility by \(x^{24}-1\).

For each of the three dimension-\(4\) codes it then exhausts all \(23^4\) messages and reproduces the complete weight distribution. Independently, it normalizes the \(24\) generator columns projectively, computes point multiplicities and all projective lines determined by column points, and derives the generalized Hamming hierarchy. Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Zhang, Cao, and Luo introduce a family of cyclic codes with increasing dimensions and fixed minimum distance \(n/2\). Their publicly visible Table 1 displays eight members of the \(n=24\) pattern, including the three two-index choices \(I=\{1,2\},\{1,3\},\{2,3\}\), all with \(k=4\) and \(d=12\). The table therefore identifies three codes with identical ordinary parameters but does not distinguish them by complete spectrum or higher support weights.

General literature on cyclic-code weight distributions does not make these invariants automatic from \([n,k,d]\). In particular, Yang–Xiong–Ding–Luo determine weight distributions for a broad class of cyclic codes with prescribed zero structure; their explicit \([24,4,12]\) example is over \(\mathbb F_7\), and their main equal-degree parity-check-factor hypotheses do not directly specialize to the present parity checks
\[
(x^2-1)M_j(x),
\]
which contain two linear factors and one quadratic factor.

The three exact spectra above are themselves a useful noncoverage check: despite identical \([24,4,12]_{23}\) parameters and membership in the same construction, the codes have three different generalized-support geometries.

## Limitations

The finding concerns the \(q=23,n=24\) specialization and the three dimension-\(4\) members only. It does not classify all \([24,4,12]_{23}\) cyclic codes or all specializations of the source family.

The publisher exposes the abstract, metadata, and Table 1, but the complete article text was not available through the lawful full-text routes checked here. Exact-title, exact-parameter, coefficient-level, and generalized-Hamming-weight searches found no prior statement of these three spectra or hierarchies, but an unindexed computation in inaccessible material remains a residual literature risk.

## References

1. Hanglong Zhang, Xiwang Cao, and Gaojun Luo, *A family of cyclic codes with increasing dimensions and fixed minimum distances*, Advances in Mathematics of Communications 23 (2026), 40–51, DOI 10.3934/amc.2026013, early access 2026-01-16.
2. Jing Yang, Maosheng Xiong, Cunsheng Ding, and Jinquan Luo, *Weight Distribution of a Class of Cyclic Codes With Arbitrary Number of Zeros*, IEEE Transactions on Information Theory 59 (2013), 5985–5993, DOI 10.1109/TIT.2013.2266731.
3. Victor K. Wei, *Generalized Hamming Weights for Linear Codes*, IEEE Transactions on Information Theory 37 (1991), 1412–1418.
