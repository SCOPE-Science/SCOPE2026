# Orbit-equivalent affine and full symmetries of even direct-power dihedral quandles

## Finding
For integers \(k\ge2\) and \(d\ge2\), let \(A=(\mathbb Z/2^k\mathbb Z)^d\), and give \(Q=A\) the core-quandle operation \(x*y=2y-x\). Thus \(Q\cong R_{2^k}^{\,d}\), the direct product of \(d\) even dihedral quandles. Let \(F=\operatorname{Aut}(Q)\) and let \(H=A\rtimes\operatorname{GL}_d(\mathbb Z/2^k\mathbb Z)\) be the subgroup of affine transformations.

**Theorem.** The permutation groups \(H<F\) have exactly the same orbits on ordered pairs \(Q\times Q\): the diagonal and, for each \(0\le j<k\), the pairs whose difference belongs to \(2^jA\setminus2^{j+1}A\). Their common permutation rank is \(k+1\), but their index is
\[
[F:H]=2^{d(2^d-d-1)}.
\]
More precisely, the point stabilizer \(F_0\) admits a natural surjection onto \(\operatorname{GL}_d(\mathbb Z/2^{k-1}\mathbb Z)\) with kernel the elementary abelian group of all functions \(e:A/2A\to A[2]\) satisfying \(e(0)=0\); hence
\[
|F|=2^{kd+d(2^d-1)+d^2(k-2)}\prod_{i=0}^{d-1}(2^d-2^i).
\]
For \(k=d=2\), the full group has order \(6144\), its affine subgroup has order \(1536\), and their common point-stabilizer orbit sizes are \(1,3,12\).

## Assumptions and scope
The integers \(k,d\) satisfy \(k\ge2\), \(d\ge2\); the arithmetic is over the additive module \(A\). Write \(A[2]=\{a\in A:2a=0\}\). The ordered-pair orbits of a permutation group \(G\) are its orbits under the componentwise action on \(A\times A\). The canonical affine group \(H\) includes every translation and every additive-group automorphism of \(A\). The theorem describes \(F\) as a **permutation group**, rather than merely determining an abstract group isomorphism. It does not assert a splitting of the point-stabilizer exact sequence.

## Proof
**Step 1 (translation reduction).** For each \(b\in A\), the map \(T_b(x)=x+b\) satisfies \(T_b(x*y)=T_b(x)*T_b(y)\). Consequently \(F\) is transitive, and \(|F|=|A|\,|F_0|\).

**Step 2 (restriction to the doubled subgroup).** Let \(g\in F_0\). From \(g(2y-x)=2g(y)-g(x)\), putting \(y=0\) gives \(g(-x)=-g(x)\), and putting \(x=0\) gives \(g(2y)=2g(y)\). Replacing \(x\) by \(-x\) yields
\[
g(x+2y)=g(x)+2g(y)=g(x)+g(2y).
\]
Therefore \(h=g|_{2A}\) is a group homomorphism \(2A\to2A\), since \(g(2A)=2g(A)=2A\); injectivity of \(g\) makes \(h\) invertible. Thus restriction is a group homomorphism
\[
\rho:F_0\longrightarrow \operatorname{Aut}(2A)\cong\operatorname{GL}_d(\mathbb Z/2^{k-1}\mathbb Z).
\]
It is onto: every invertible matrix modulo \(2^{k-1}\) can be lifted to a matrix with odd determinant modulo \(2^k\), and this lifted matrix is an additive-group automorphism of \(A\), hence an element of \(F_0\).

**Step 3 (all kernel maps).** If \(g\in\ker\rho\), then \(g(x+t)=g(x)+t\) for all \(t\in2A\). Thus \(e([x])=g(x)-x\) depends only on \([x]\in A/2A\). Moreover \(2e([x])=g(2x)-2x=0\), and \(e(0)=0\). Conversely, for every function \(e:A/2A\to A[2]\) with \(e(0)=0\), define \(g_e(x)=x+e([x])\). As \(A[2]\subseteq2A\) when \(k\ge2\), this map acts as a translation within each parity coset and is bijective. The parity of \(2y-x\) is that of \(x\), so
\[
g_e(2y-x)=2y-x+e([x])=2g_e(y)-g_e(x)
\]
because \(2e([y])=0\) and \(-e([x])=e([x])\). Thus \(g_e\in F_0\). Composition in the kernel adds the functions pointwise; its order is \(|A[2]|^{|A/2A|-1}=2^{d(2^d-1)}\), and it is elementary abelian.

**Step 4 (exact order and strict index).** The reduction map \(\operatorname{GL}_d(\mathbb Z/2^r\mathbb Z)\to\operatorname{GL}_d(\mathbb F_2)\) is onto with kernel of order \(2^{d^2(r-1)}\) for every \(r\ge1\). Hence
\[
|F|=2^{kd}\,2^{d(2^d-1)}\,2^{d^2(k-2)}|\operatorname{GL}_d(\mathbb F_2)|,
\]
while
\[
|H|=2^{kd}\,2^{d^2(k-1)}|\operatorname{GL}_d(\mathbb F_2)|.
\]
Their ratio is the asserted index, strictly exceeding one for \(d\ge2\). An explicit nonaffine symmetry is \(g_e\) with \(e([x])=2^{k-1}e_1\) when the first two coordinates of \([x]\) are both \(1\), and \(e([x])=0\) otherwise. This \(g_e\) fixes \(0,e_1,e_2\) and moves \(e_1+e_2\); any additive map fixing \(e_1,e_2\) fixes their sum, so \(g_e\) is not affine.

**Step 5 (the identical ordered-pair orbitals).** For every \(g\in F_0\) and integer \(j\ge0\), repeated doubling gives \(g(2^jx)=2^jg(x)\). Hence \(g(2^jA)=2^jA\) and \(g\) preserves each valuation shell \(2^jA\setminus2^{j+1}A\). The affine point stabilizer \(\operatorname{GL}_d(\mathbb Z/2^k\mathbb Z)\) acts transitively on each such shell: any vector in it is \(2^j\) times a vector with at least one odd coordinate, and elementary invertible row operations take that primitive vector to \(e_1\). Since \(H\le F\), the \(F_0\)-orbits and the \(H_0\)-orbits coincide: \(\{0\}\) together with the \(k\) valuation shells. Translation of the first coordinate to zero identifies these with the claimed ordered-pair orbitals. The rank is therefore \(k+1\).

## Verification
The standalone Python 3 program `verify.py` enumerates all \(384\) identity-fixing automorphisms on \((\mathbb Z/4\mathbb Z)^2\) from the restriction/kernel parametrization and checks every defining quandle identity on all \(16^2\) ordered pairs for every map. It checks the stabilizer orbit sizes \(1,3,12\), the derived full-group order \(6144\), the affine index \(4\), and the explicit nonaffine automorphism. Run `python verify.py`; successful output ends with `VERIFY_OK`. Finite calculations corroborate but are not the proof for arbitrary \(k,d\).

## Relationship to prior work
Bardakov and Sangare, *Constructions and automorphisms of quandles* (arXiv:2610.18676v1, publicly submitted 2026-10-13), Question 3.5 explicitly asks about \(\operatorname{Aut}(R_n\times R_m)\) when either modulus is even. Their Section 3 treats the Latin/odd-modulus case, not the present non-Latin even direct powers. Hou, *Automorphism groups of Alexander quandles* (2011), studies **general** Alexander-quandle automorphism groups and is especially relevant prior structural work. The particular assertion here combines a canonical affine subgroup's ordered-pair orbit-equivalence with an exact exponentially growing index. Hou's general result may allow recovery of portions of this formula, so the theorem does not assert that no abstract automorphism-group description was previously possible. Bardakov, Dey and Singh's work on Takasaki quandles is stated for abelian groups without \(2\)-torsion; its quoted hypotheses exclude these groups.

## Limitations
The power-of-two homogeneous family is specified: mixed even moduli and arbitrary finite abelian groups are not classified. The exact sequence is not claimed to split. The 2011 Hou paper was identifiable by DOI and abstract, but its full text could not be inspected, leaving a substantive possibility that this orbital-equivalence property or the index is implicit in its general framework. This is a self-review, not independent validation.

## References
1. V. G. Bardakov and B. Sangare, *Constructions and automorphisms of quandles*, arXiv:2610.18676v1 (2026), Section 3 and Question 3.5. https://arxiv.org/abs/2610.18676
2. X.-D. Hou, *Automorphism groups of Alexander quandles*, Journal of Algebra (2011), DOI:10.1016/j.jalgebra.2011.06.027.
3. V. G. Bardakov, P. Dey and M. Singh, *Automorphism groups of quandles arising from groups*, arXiv:1608.05178 (2016).
4. M. Elhamdadi, J. Macquarrie and R. Restrepo, *Automorphism groups of quandles*, arXiv:1012.5291 (2010).
