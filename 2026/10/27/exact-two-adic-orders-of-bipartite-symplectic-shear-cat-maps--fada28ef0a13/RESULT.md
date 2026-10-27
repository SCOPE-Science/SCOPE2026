# Exact two-adic orders of bipartite symplectic shear cat maps

## Finding

Let \(a,b,s\ge1\) be integers, \(N=a+b\), and \(B\) the symmetric \(N\)-by-\(N\) adjacency matrix of the complete bipartite graph \(K_{a,b}\). On the finite torus \((\mathbb Z/2^s\mathbb Z)^{2N}\), consider the invertible symplectic transformation

\[
T_B=\begin{pmatrix}I_N&B\\ I_N&I_N+B\end{pmatrix},\qquad
P_{a,b}(s)=\min\{r\ge1:T_B^r\equiv I_{2N}\pmod{2^s}\}.
\]

The **exact global permutation order** is

\[
\boxed{P_{a,b}(s)=\begin{cases}
6\,2^{\max(0,s-2)}, & a=b=1,\\
3\,2^s, & a,b\text{ odd and }(a,b)\ne(1,1),\\
2^{s+1}, & a,b\text{ even},\\
2^{s+2}, & \text{one part odd and the even part divisible by }4,\\
8\,2^{\max(0,s-2)}, & \text{one part odd and the even part }\equiv2\pmod4.
\end{cases}}
\]

Thus complete bipartite graph coupling exhibits five exact modular-period regimes. In particular, the exceptional single-edge graph \(K_{1,1}\) has half the order of every larger odd-by-odd graph for \(s\ge2\), and changing the even part size from \(2\bmod4\) to \(0\bmod4\) changes the small-modulus lifting law.

## Assumptions and scope

The matrices and moduli are exactly those displayed. The two off-diagonal blocks of the graph adjacency matrix are all ones and the two diagonal blocks are zero; this is an unweighted simple complete bipartite graph. The map is the **composition of two integral symplectic shears**

\[
T_B=\begin{pmatrix}I_N&0\\I_N&I_N\end{pmatrix}
\begin{pmatrix}I_N&B\\0&I_N\end{pmatrix}.
\]

Because \(B\) is symmetric, the two factors are symplectic for the standard alternating form; their integer inverses also show that every reduction modulo \(2^s\) is a permutation. “Global order” means the least exponent fixing every state, not that every state has that primitive period. The theorem does not concern generic real torus orbit periods or different coupling matrices.

## Proof

**1. Graph adjacency algebra.** Order the two parts consecutively. Direct block multiplication gives

\[
B^2=\begin{pmatrix}bJ_a&0\\0&aJ_b\end{pmatrix},\qquad B^3=abB.
\]

Here \(J_c\) is the all-ones \(c\)-by-\(c\) matrix. Write \(t=ab\) and use the polynomial reduction \(z^3=tz\), which is valid on substitution \(z=B\). Define

\[
A(z)=\begin{pmatrix}1&z\\1&1+z\end{pmatrix},\quad
U_k(z)=(A(z)^k)_{11}-1,\quad V_k(z)=(A(z)^k)_{21}.
\]

For every \(k\ge1\), straightforward matrix multiplication, or the recurrence \(A(z)^{k+1}=A(z)^kA(z)\), yields

\[
T_B^k-I_{2N}=\begin{pmatrix}
U_k(B)&B V_k(B)\\ V_k(B)&U_k(B)+B V_k(B)
\end{pmatrix}.
\]

Thus exact divisibility of \(T_B^k-I\) is equivalent to exact divisibility of the two matrix entries \(U_k(B),V_k(B)\), rather than to a potentially lossy eigenvalue decomposition over a ring.

**2. Exact orders modulo two.** In characteristic two, \(B^2=0\) if both parts are even; \(B^3=0\) but \(B^2\ne0\) if exactly one is even; and \(B^3=B\) if both are odd. The identity above and the exact polynomials \(U_2=z\), \(U_3=3z+z^2\), \(U_4=6z+5z^2+z^3\), together with the corresponding \(V_k\), show directly that the respective least orders modulo two are

\[
m_0=4,\qquad m_0=8,\qquad m_0=6.
\]

Minimality can be checked without testing all exponents: for the first two cases, a power of two must occur since the reduced transformation is unipotent; the proper half-power is not the identity because its upper-left difference contains respectively \(B\) or \(B^2\). For the odd-odd case \(T_B^6=I\pmod2\), while \(T_B^2\ne I\) and \(T_B^3\ne I\) as \(B\ne0\) and \(B+B^2\ne0\) respectively. Hence the order is six.

**3. Exact first lifting valuations.** For an integer matrix \(H\), let \(v_2(H)\) be the minimum valuation of its entries. Reducing polynomials modulo \(z^3-tz\) gives, with \(t=ab\),

\[
\begin{aligned}
V_4(B)&=4I+(t+10)B+6B^2,\\
U_8(B)&=(t^3+66t^2+210t+28)B
 +(13t^2+165t+126)B^2,\\
V_8(B)&=8I+(t^3+78t^2+330t+84)B
 +(14t^2+220t+252)B^2,\\
V_6(B)&=6I+(t^2+36t+35)B+(10t+56)B^2.
\end{aligned}
\]

Because \(B\) has unit off-diagonal entries and \(B^2\) has entries \(a\) or \(b\) inside each part, these explicit identities imply:

| Part parities | \(m_0\) | \(v_2(T_B^{m_0}-I)\) | \(v_2(T_B^{2m_0}-I)\) when needed |
| --- | ---: | ---: | ---: |
| Both even | \(4\) | \(1\) | \(2\) |
| One odd, even part \(0\bmod4\) | \(8\) | \(1\) | \(2\) |
| One odd, even part \(2\bmod4\) | \(8\) | \(2\) | — |
| Both odd, except \(a=b=1\) | \(6\) | \(1\) | \(2\) |
| \(a=b=1\) | \(6\) | \(2\) | — |

Here are coefficient-level witnesses for every nontrivial row. If both parts are even, \(V_4\equiv2B\pmod4\) and \(V_8\equiv4B\pmod8\). If the even part is divisible by four, then \(U_8\equiv2B^2\pmod4\), and direct expansion of \(U_{16}\) gives \(U_{16}\equiv4B^2\pmod8\). Since the other part is odd, \(B^2\not\equiv0\pmod2\). If the even part is \(2\bmod4\), every block of \(T_B^8-I\) is divisible by four, whereas \(V_8\equiv4B^2\pmod8\). When both parts are odd, \(V_6\equiv2(I+B^2)\pmod4\) and \(V_{12}\equiv4(I+B^2)\pmod8\). The matrix \(I+B^2\) is nonzero modulo two unless \(a=b=1\); indeed, for any part of size at least three, it has a nonzero off-diagonal entry. At \(a=b=1\), \(B^2=I\), \(U_6=44B+44I\), and all blocks of \(T_B^6-I\) are divisible by four but not eight. Each congruence follows by reducing the displayed polynomial recurrence modulo eight; no sampling of graph sizes is required. In the rows with a first valuation of one, the asserted second valuation of two can alternatively be seen by the exact matrix square identity together with the explicitly established noncancellation modulo four or eight.

**4. Unique lifting and conclusion.** If \(H=I+2^rE\) for \(r\ge2\) with some odd entry in \(E\), then

\[
H^2-I=2^{r+1}(E+2^{r-1}E^2),
\]

and the parenthesized matrix still has an odd entry. Iteration gives \(v_2(H^{2^j}-I)=r+j\). When the first valuation is one, the explicit second valuation two above initiates exactly the same induction. The kernel of reduction from invertible matrices modulo \(2^{s+1}\) to those modulo \(2^s\) is a two-group, so a global order lifts only by successive factors of two. Starting with the proven least order \(m_0\) modulo two and the valuation table produces each displayed formula, with no missing odd factors. This establishes every claimed case.

## Verification

The standalone Python 3 script `verify.py` constructs the integer \(2N\)-by-\(2N\) matrix and computes its powers by exact modular arithmetic. It checks 476 period values: all \(1\le a,b\le8\), \(1\le s\le7\), plus seven larger bipartitions at four moduli; minimality is tested by the prime divisors two and three. It independently checks both base lifting valuations for all 64 small bipartitions. Its successful output is `VERIFY_OK: 476 exact matrix-order comparisons; base valuation and lifting comparisons for 64 bipartitions`. These finite tests corroborate, but cannot replace, the all-parameter coefficient and valuation argument.

## Relationship to prior work

Nance (2011) treats finite periods for the classical cat map and selected extensions to higher-dimensional maps; the present theorem instead uses symmetric adjacency coupling of two integral shears with distinct complete-bipartite parts. Axenides, Floratos and Nicolis (2022/2023) develop cat-map lattices and finite period methods, but the inspected full text does not state the five-case congruence classification here. Manolas and Floratos (2026) examine a general symmetric-circulant coupled system with matrix \(\bigl(\begin{smallmatrix}I&C\\C&I+C^2\end{smallmatrix}\bigr)\), including complete-graph specializations and numerical finite periods. That matrix and its complete-graph cases differ from both the shear ordering and complete-bipartite graph family treated here. Their general setting does not directly imply the present closed arithmetic classification, and no theorem giving it was located in their inspected text. General congruence-order lifting principles and matrix recurrences are prior mathematics, not claimed as new.

## Limitations

The theorem concerns global finite-torus permutation orders for exactly \(K_{a,b}\), integer unit graph weights and moduli \(2^s\). It does not determine the distribution of primitive state periods, extend to odd-prime powers or arbitrary graphs, or classify real-torus dynamics. A possible equivalent older specialization expressed via integer matrix recurrence rather than graph-coupled dynamics cannot be conclusively excluded; searches do not establish absolute historical priority. The finite verifier is a regression check, not an infinite proof.

## References

1. J. Nance, *Periods of the discretized Arnold's Cat Mapping and its extension to n-dimensions*, arXiv:1111.2984v1, first public November 13, 2011, https://arxiv.org/abs/1111.2984.
2. M. Axenides, E. Floratos, S. Nicolis, *Arnol'd cat map lattices*, arXiv:2208.03267, 2022; Physical Review E **107**, 064206 (2023), https://arxiv.org/abs/2208.03267.
3. K. Manolas, E. Floratos, *Coupled Arnol'd cat maps on circulant graphs*, arXiv:2605.00965, May 2026, https://arxiv.org/abs/2605.00965.
