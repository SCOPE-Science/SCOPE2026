# The 128 known rational conics form one automorphism orbit
## Finding
Let \(V_{\overline{\mathbf Q}}\subset \mathbf P^8\) be the surface parameterizing \(3\times3\) magic squares of squares, and let
\[
G=\operatorname{Aut}(V_{\overline{\mathbf Q}})\cong D_4\ltimes S,\qquad S=(\mu_2^9)/\mu_2.
\]
The 128 smooth rational conics that form the three-distinct-entry locus \(Z_3\) are a single \(G\)-orbit. Each of the two 64-conic diagonal families is a single \(S\)-orbit. Consequently, for any one of these conics \(C\),
\[
|\operatorname{Stab}_S(C)|=4,\qquad |\operatorname{Stab}_G(C)|=16.
\]

## Assumptions and scope
Work over \(\overline{\mathbf Q}\). Auel--Singer define \(V\) by the linear magic-square relations applied to the nine coordinate squares. Their Theorem 1 gives
\[
G\cong D_4\ltimes(\mu_2^9)/\mu_2
\]
of order \(2048\), with \(S=(\mu_2^9)/\mu_2\) acting by independent coordinate sign changes modulo global sign. Their Proposition 3.1 gives exactly 128 smooth geometrically connected rational conics in \(Z_3\), split in Section 3.1 into two collections of 64 according to the two diagonals.

Define the finite squaring morphism
\[
q:V\longrightarrow L_{\mathrm{ms}}\cong\mathbf P^2,
\qquad [A:\cdots:H]\longmapsto[A^2:\cdots:H^2],
\]
where \(L_{\mathrm{ms}}\) is the projective plane of \(3\times3\) magic squares. For a generic point of \(L_{\mathrm{ms}}\), all nine entries are nonzero, and there are \(2^9/2=256\) projective choices of square roots. Thus \(q\) has generic degree \(256=|S|\) and is the quotient by \(S\) at the function-field level.

## Proof
Let \(K=\overline{\mathbf Q}(V)\) and \(K_0=\overline{\mathbf Q}(L_{\mathrm{ms}})\). The subgroup \(S\) fixes every squared coordinate, so \(K_0\subseteq K^S\). The generic fiber count above gives
\[
[K:K_0]=256=|S|,
\]
hence \(K^S=K_0\). Therefore \(K/K_0\) is a finite Galois extension with group \(S\).

For the left-diagonal family, the squared entries have the cyclic form
\[
\begin{pmatrix}
x&y&z\\
z&x&y\\
y&z&x
\end{pmatrix},
\qquad y+z=2x.
\]
This is a prime line \(L_{\mathrm{left}}\subset L_{\mathrm{ms}}\). Auel--Singer show that its inverse image has exactly 64 irreducible components, all smooth rational conics. In a finite Galois extension of function fields, the Galois group acts transitively on the discrete valuations extending the valuation of any fixed prime divisor. Equivalently, the deck group acts transitively on the prime divisors lying above a fixed prime divisor of the quotient. It follows that these 64 conics form one \(S\)-orbit. The same argument applies to the right-diagonal line \(L_{\mathrm{right}}\), giving a second 64-element \(S\)-orbit.

It remains to compare the two lines. Auel--Singer's square reflection is
\[
\psi:[A:B:C:D:M:E:F:G:H]\longmapsto[C:B:A:E:M:D:H:G:F].
\]
Applied to the cyclic squared pattern above, it gives
\[
\begin{pmatrix}
z&y&x\\
y&x&z\\
x&z&y
\end{pmatrix},
\]
whose right diagonal has equal entries. Thus \(\psi(L_{\mathrm{left}})=L_{\mathrm{right}}\). Since \(\psi\in D_4\subset G\), the two 64-element \(S\)-orbits lie in one \(G\)-orbit. Auel--Singer's total count is 128, so this orbit is all of \(Z_3\)'s conics.

Finally, orbit--stabilizer gives
\[
|\operatorname{Stab}_S(C)|=256/64=4
\]
and
\[
|\operatorname{Stab}_G(C)|=2048/128=16.
\]

## Verification
The accompanying `verify_orbit.py` checks the two concrete finite combinatorial steps: the order computations \(2^9/2=256\) and \(8\cdot256=2048\), and the fact that Auel--Singer's reflection sends the left cyclic squared pattern to a pattern with equal right diagonal. It also checks the orbit--stabilizer orders \(256/64=4\) and \(2048/128=16\). The transitivity step is the standard theorem that a Galois group acts transitively on extensions of a discrete valuation, applied to the prime divisor of the quotient plane.

## Relationship to prior work
Auel--Singer compute the full geometric automorphism group, explicitly describe the sign-change subgroup and the square reflection, and prove that \(Z_3\) has exactly 128 rational conic components, presented as two families of 64. They do not state an orbit decomposition for those 128 conics; later they again refer to them as two families when studying their images on magic del Pezzo surfaces. Their final appendix remark leaves open whether the 128 known conics exhaust all conics on \(V\).

Bruin--Thomas--Várilly-Alvarado prove algebraic quasi-hyperbolicity of the same magic-square surface, which implies finiteness of low-genus curves but does not classify these conics or their automorphism orbits. Targeted searches for the exact orbit, stabilizer, quotient-divisor, and equivalent sign-change formulations did not locate a prior statement of the result above.

## Limitations
This finding classifies the automorphism orbit of the 128 already known conics only. It does not prove that no additional conics exist on \(V\); that completeness question remains open in Auel--Singer. It determines the orders of the stabilizers, not their abstract group structures. The originality search cannot exclude unindexed or inaccessible literature that states the same orbit decomposition.

## References
1. A. Auel and B. Singer, *The algebraic geometry of 3-by-3 magic squares of squares*, arXiv:2609.09351v1 (2026), especially Theorem 1, Section 3.1, Proposition 4.4, and Remark A.2.
2. N. Bruin, J. Thomas, and A. Várilly-Alvarado, *Explicit computation of symmetric differentials and its application to quasi-hyperbolicity*, Algebra & Number Theory 16 (2022), 1377--1405; arXiv:1912.08908.
