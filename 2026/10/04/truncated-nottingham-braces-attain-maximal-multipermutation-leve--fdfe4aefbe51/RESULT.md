# Truncated Nottingham braces attain maximal multipermutation level at every odd prime
## Finding
Let \(K\) be a field of characteristic different from \(2\), and let \(N\ge 2\). Put
\[
B_N(K)=x^2K[x]/(x^{N+1}).
\]
The near-ring construction for the Nottingham group gives the right-brace product
\[
f\star g=g+f(x+g)\pmod{x^{N+1}}.
\]
Reverse the multiplicative law to obtain the associated left brace \(\widehat B_N(K)\), so that \(g\circ f=f\star g\). Its lambda action is
\[
\lambda_g(f)=f(x+g)\pmod{x^{N+1}}.
\]
For \(1\le r\le N-1\), its socle series is exactly
\[
\operatorname{Soc}_r(\widehat B_N(K))
 =\operatorname{span}_K\{x^{N-r+1},x^{N-r+2},\ldots,x^N\}.
\]
Consequently \(\widehat B_N(K)\) has multipermutation level exactly \(N-1\), and so does its associated set-theoretic Yang--Baxter solution.

For every odd prime \(p\), \(|\widehat B_N(\mathbb F_p)|=p^{N-1}\). Its level \(N-1\) is maximal among all finite braces of order \(p^{N-1}\) that have finite multipermutation level.
## Assumptions and scope
The statement concerns the natural finite truncations of the Nottingham right brace introduced through formal substitution, followed by the standard reversal of multiplicative order that converts a right brace into a left brace. The characteristic restriction is exactly the one used in the socle argument below: \(2\) must be nonzero in \(K\). No claim is made here in characteristic \(2\).

The multiplicative group of the original right brace is the natural degree-\(N\) quotient of the Nottingham substitution group. Reversing multiplication does not alter its abstract group isomorphism type, because every group is isomorphic to its opposite by inversion.
## Proof
For the reversed left brace, the lambda map is obtained directly from the right-brace law:
\[
\lambda_g(f)=-g+(g\circ f)=-g+(f\star g)=f(x+g).
\]
Because the additive group is abelian, the socle is the kernel of this lambda action.

Write a nonzero element as
\[
g=b_ex^e+b_{e+1}x^{e+1}+\cdots+b_Nx^N,
\qquad b_e\ne0,
\]
with \(2\le e\le N\). If \(e<N\), test the lambda action on \(f=x^2\). Then
\[
\lambda_g(x^2)-x^2=(x+g)^2-x^2=2xg+g^2.
\]
The lowest-degree term is \(2b_ex^{e+1}\), which is nonzero because \(\operatorname{char}K\ne2\) and \(e+1\le N\). Hence such a \(g\) is not in the socle.

If instead \(g=cx^N\), then every term of \(f(x+g)-f(x)\) containing \(g\) has degree at least \(N+1\), since every \(f\in B_N(K)\) has order at least \(2\). Thus \(\lambda_g(f)=f\) modulo \(x^{N+1}\) for every \(f\). Therefore
\[
\operatorname{Soc}(\widehat B_N(K))=Kx^N.
\]

Reduction modulo \(x^N\) is a brace epimorphism and identifies
\[
\widehat B_N(K)/(Kx^N)\cong \widehat B_{N-1}(K).
\]
Applying the preceding socle calculation inductively yields
\[
\operatorname{Soc}_r(\widehat B_N(K))
=\operatorname{span}_K\{x^{N-r+1},\ldots,x^N\}
\]
for every \(1\le r\le N-1\). The first term reaching the whole brace is therefore \(r=N-1\), proving that the multipermutation level is \(N-1\). The standard socle-series/retraction theorem for braces then gives the same level for the associated Yang--Baxter solution.

Finally let \(K=\mathbb F_p\) with \(p\) odd. The additive group has order \(p^{N-1}\). For any finite brace of order \(p^{N-1}\) whose socle series reaches the whole brace in \(m\) steps, every strict factor in that series is a nontrivial additive \(p\)-group and therefore has order at least \(p\). Hence \(p^m\le p^{N-1}\), so \(m\le N-1\). The present family attains equality.
## Verification
The proof is symbolic and valid for every field of characteristic different from \(2\). The accompanying script `artifacts/verify.py` independently enumerates the truncated braces for \((p,N)=(3,2),(3,3),(5,4)\), computes the lambda kernel directly, checks that it is exactly the top-degree line, and verifies that dropping the top coefficient intertwines the brace products. Its recorded output ends with `CHECK_OK`.

The finite computation is a regression check only; it is not used as an infinite proof.
## Relationship to prior work
Aragona, Gavioli, Iannaccone and Nozzi introduce the topological right skew brace on \(x^2D[[x]]\) and identify its multiplicative group with the Nottingham group. Their Nottingham construction supplies the operation used here, but the inspected Nottingham section does not state the finite-truncation socle series or its multipermutation level.

D'Alessandro and Szechtman study the same natural truncated substitution groups in positive characteristic and determine exponent data for their quotient subgroups. This is group-theoretic coverage of the multiplicative groups, not a computation of the brace socle or Yang--Baxter multipermutation level.

Ballester-Bolinches, Esteban-Romero and Pérez-Calabuig give the general socle-series characterization of multipermutation level for braces. Applying that theory to the Nottingham brace requires the explicit lambda-kernel computation above.
## Limitations
Characteristic \(2\) is excluded: the leading-term test with \(x^2\) degenerates there, and the socle can be larger. The result determines the socle filtration and multipermutation level, not the full ideal lattice or all Yang--Baxter invariants of these braces.

A residual literature risk is that an older paper on substitution groups or braces may encode the same filtration under different terminology. Targeted searches found group-theoretic analyses of Nottingham quotients and general brace results, but no statement implying this exact socle series.
## References
1. R. Aragona, N. Gavioli, M. Iannaccone, G. Nozzi, *Near-Rings and Skew Braces*, arXiv:2608.04874, first posted 5 August 2026.
2. A. D'Alessandro, F. Szechtman, *Substitution groups of formal power series*, arXiv:2606.11461, first posted 9 June 2026.
3. A. Ballester-Bolinches, R. Esteban-Romero, V. Pérez-Calabuig, *A Jordan--Hölder theorem for skew left braces and their applications to multipermutation solutions of the Yang--Baxter equation*, Proc. Royal Soc. Edinburgh A 154 (2024), 793--809, DOI 10.1017/prm.2023.37.
