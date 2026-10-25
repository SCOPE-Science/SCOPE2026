# Reflection orientation and quotient homology of two-row \(t\)-Young complexes

## Finding
For integers \(t,L\geq1\), let \(K_{L,t}=\Delta_t^{(L,L)}\) be the two-row \(t\)-Young complex with vertex labels \(1,\ldots,N\), \(N=L+t\). The order-reversing involution \(\rho(i)=N+1-i\) preserves this complex. Write \(L=(t+1)q+r\), where \(0\leq r\leq t\).

The previously known nonequivariant homotopy type and the new complete **integral orientation character** are
\[
\widetilde H_j(K_{L,t};\mathbb Z)=
\begin{cases}
\mathbb Z,&r\in\{0,1\},\ j=2q+r-1,\\
0,&\text{otherwise},
\end{cases}
\qquad
\rho_*\big|_{\widetilde H_{2q+r-1}}=(-1)^{q+r}
\quad(r\in\{0,1\}).
\]
Here \(L\geq1\) excludes the formal case \(q=r=0\); consequently the nonzero degree is always at least zero.

Equivalently, the **new reduced Lefschetz formula** is
\[
\widetilde\Lambda(\rho;K_{L,t})=
\begin{cases}
(-1)^{q+1},&r\in\{0,1\},\\
0,&2\leq r\leq t.
\end{cases}
\]
For each fixed \(t\), this has generating function
\[
\sum_{L\geq1}\widetilde\Lambda(\rho;K_{L,t})z^L
=-z+\frac{(1+z)z^{t+1}}{1+z^{t+1}}.
\]
As a quotient consequence, the reduced rational homology of \(|K_{L,t}|/\langle\rho\rangle\) is one-dimensional in degree \(2q+r-1\) exactly when \(r\in\{0,1\}\) and \(q+r\) is even; otherwise all its reduced rational homology vanishes. The Euler characteristic of the geometric fixed set is \(1+\widetilde\Lambda(\rho;K_{L,t})\).

## Assumptions and scope
The \(t\)-Young complex follows the definition of Navarra--Qureshi--Veer: two rows each of length \(L\), with entries \(j\) and \(t+j\) in column \(j\), and facets given by strictly increasing selections of one entry from each column. All parameters are arbitrary positive integers. Homology is reduced simplicial homology unless explicitly stated. A sign on \(\mathbb Z\) denotes its actual integral automorphism, not only a rational trace. The known homotopy type is used as an input, not claimed as new.

## Proof
**1. Facet model and symmetry.** An increasing column selection cannot have a top-row choice immediately followed by a bottom-row choice, because \(t+j\geq j+1\). Thus it consists of \(k\) bottom-row choices followed by \(L-k\) top-row choices, for a unique \(0\leq k\leq L\). Its vertex set is
\[
F_k=\{1,\ldots,k\}\cup\{t+k+1,\ldots,t+L\}
=[N]\setminus\{k+1,\ldots,k+t\}.
\]
The involution \(\rho\) carries \(F_k\) to \(F_{L-k}\), hence is a simplicial automorphism. Let \(I_{N,t}\) consist of all subsets of \([N]\) containing no run of \(t\) consecutive vertices. Then \(K_{L,t}=I_{N,t}^{\vee}\), its combinatorial Alexander dual: its facets are precisely the complements of minimal nonfaces of \(I_{N,t}\).

**2. Signed complement formula.** For any finite complex \(X\) on \([N]\) invariant under a permutation \(g\), let \(\varepsilon(g|_S)\) be the sign induced by \(g\) on an invariant subset \(S\), including the empty subset with sign \(+1\). The reduced simplicial Lefschetz number is the alternating trace on augmented simplicial chains:
\[
\widetilde\Lambda(g;X)=\sum_{S\in X,\ gS=S}(-1)^{|S|-1}\varepsilon(g|_S).
\]
The total sum of \((-1)^{|S|}\varepsilon(g|_S)\) over *all* invariant subsets of \([N]\) is zero: each cycle of \(g\) contributes a factor \(1-1\). If \(X=I_{N,t}^{\vee}\), complementing invariant subsets and using \(\varepsilon(g|_S)\varepsilon(g|_{[N]\setminus S})=\varepsilon(g)\) therefore gives
\[
\widetilde\Lambda(g;K_{L,t})
=(-1)^N\varepsilon(g)
\sum_{B\in I_{N,t},\ gB=B}(-1)^{|B|}\varepsilon(g|_B).
\]
This also verifies the reduced-degree convention at the empty face.

**3. Palindromic word computation.** For \(g=\rho\), invariant subsets correspond to palindromic binary words of length \(N\). If \(h=\lceil N/2\rceil\), specify a word by its first \(h\) bits, read toward the center. Every selected reflection orbit, whether a pair or the central singleton, contributes \(-1\) to \((-1)^{|B|}\varepsilon(\rho|_B)\). Hence the final sum above is the signed count \(A_{N,t}\) of binary half-words with no \(t\)-run in the full palindrome.

All runs of ones away from the center have length at most \(t-1\). The terminal run of ones in the half-word has length at most
\[
c=\begin{cases}
\lfloor(t-1)/2\rfloor,&N\text{ even},\\
\lfloor t/2\rfloor,&N\text{ odd}.
\end{cases}
\]
Decompose each half-word into zero-terminated blocks \(1^j0\), with \(0\leq j<t\), and a terminal block \(1^j\), with \(0\leq j\leq c\). With \(z\) marking length and each selected bit contributing \(-1\), these words have generating function
\[
G(z)=\frac{\sum_{j=0}^{c}(-z)^j}
{1-z\sum_{j=0}^{t-1}(-z)^j}
=\frac{1-(-z)^{c+1}}{1+(-1)^t z^{t+1}}.
\]
Here \(G(z)\) is the signed generating function for half-words with terminal-run bound \(c\), which depends on the parity of \(N\). Thus for the desired \(h\) and its corresponding \(c\),
\[
A_{N,t}=[z^h]G(z)=[z^h]\frac{1-(-z)^{c+1}}{1+(-1)^t z^{t+1}}.
\]
Put \(a=(-1)^{t+1}\). Expanding the denominator proves the exact coefficient rule
\[
A_{N,t}=\begin{cases}
a^u,&h=(t+1)u,\\
(-1)^c a^u,&h=(t+1)u+c+1,\\
0,&\text{otherwise},
\end{cases}\qquad u\geq0.
\]
The conditions are disjoint because \(0<c+1<t+1\). Using \(N=L+t\), \(L=(t+1)q+r\), \(\varepsilon(\rho)=(-1)^{\lfloor N/2\rfloor}\), and separating the two parities of \(N\) and of \(t\), the rule gives
\[
(-1)^{N+\lfloor N/2\rfloor}A_{N,t}
=\begin{cases}(-1)^{q+1},&r=0\text{ or }1,\\0,&2\leq r\leq t.\end{cases}
\]
For example, if \(t=2a+1\) is odd, \(N\) is odd when \(r=0\) and even when \(r=1\); the same \(h=(a+1)q+a+1\) and \(c=a\) occur for either residue. When \(q\) is even, the coefficient and permutation sign multiply to \(-1\); when \(q\) is odd, they multiply to \(+1\). For even \(t\), applying the same coefficient rule to the four combinations of \(q\bmod2\) and \(r\in\{0,1\}\) gives the identical signs. The remaining residues miss the two possible coefficient positions. This proves the new Lefschetz formula for every parameter, independently of finite enumeration.

**4. Integral orientation.** Theorem 3.6 of Navarra--Qureshi--Veer, specialized to one path and two equal rows, gives \(K_{L,t}\simeq S^{2q+r-1}\) if \(r=0,1\) and contractibility otherwise. In the sphere cases the only nonzero reduced integral homology is a free rank-one lattice. The Lefschetz number is \((-1)^{2q+r-1}\) times the trace on this lattice. Therefore that trace equals
\[
(-1)^{2q+r-1}(-1)^{q+1}=(-1)^{q+r}.
\]
The integral automorphism must be multiplication by this sign. Rational homology of a finite simplicial quotient by an involution is the invariant part of rational homology (use barycentric subdivision and averaging), proving the quotient statement. The fixed-point Euler characteristic follows from the Lefschetz fixed-point formula for the finite-order simplicial action. Expanding the geometric series in \(z^{t+1}\) gives the stated generating function.

## Verification
The companion standalone Python verifier builds the two-row complex independently from column choices and from complements of consecutive windows. It checks 60 exact facet identities, 60 complete reduced mod-two homology computations, 60 signed augmented-chain Lefschetz calculations, 255 independently enumerated palindromic half-word sums, and 67,500 algebraic parameter substitutions. All passed. The all-parameter proof is the signed-complement and rational-generating-function argument above, not extrapolation from the computations.

## Relationship to prior work
Navarra--Qureshi--Veer introduce \(t\)-Young complexes, identify the rectangular two-row case with the Alexander dual of one \(t\)-path ideal (Proposition 3.1), and compute its **nonequivariant** homotopy type (Theorem 3.6). Their full accessible article does not state a reflection action, integral orientation sign, quotient-homology classification, or equivariant Lefschetz series. The new formulas retain precisely those symmetry-sensitive invariants. Classical combinatorial Alexander duality and simplicial Lefschetz traces supply proof techniques, but their abstract statements do not determine this two-parameter character without the palindromic calculation.

## Limitations
The theorem concerns **two equal rows** and only the canonical label reversal, not arbitrary Young shapes or the entire automorphism group. It does not construct an equivariant sphere model or determine the homotopy type of fixed-point sets; it gives their Euler characteristics and the rational homology of the orbit spaces. The nonequivariant sphere classification is cited rather than reproved. Equivalent results outside the inspected literature cannot be excluded, and an independent scientific audit has not been performed.

## References
Navarra, F., Qureshi, A. A., and Veer, D., *\(t\)-Young complexes and squarefree powers of \(t\)-path ideals*, arXiv:2511.13477, first submitted 2025-11-17; version 3, 2026-09-30. In particular Definition in Section 2, Proposition 3.1, and Theorem 3.6.

Björner, A., and Tancer, M., *Combinatorial Alexander duality: a short and elementary proof*, Discrete Comput. Geom. 42 (2009), 586–593 (background; the signed complement identity needed here is proved explicitly above).
