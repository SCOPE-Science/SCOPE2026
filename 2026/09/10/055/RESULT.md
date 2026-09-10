# H2-factor vacuity in the (1,3,5,3,1) Gorenstein cell: the Maeno–Watanabe second higher Hessian is constant, so no universal (H1,H2)-factor-pattern to Jordan-block lemma exists as stated

## Context

Codimension-3 Artinian Gorenstein algebras are studied via Macaulay duality (dual generator $F$), higher-Hessian Lefschetz criteria (Maeno–Watanabe), and Jordan-type stratification of multiplication by linear forms (Harima–Watanabe/Iarrobino school; Migliore–Nagel Lefschetz-locus program). The admitted target proposed a transferable lemma for the short-Hilbert cell $(1,3,5,3,1)$: the irreducible-factor pattern (degrees, multiplicities, incidence) of the two higher Hessian determinants $(H_1(F),H_2(F))$ determines the Jordan partition $P_\ell$ for every nonzero $\ell$, with a splitting pattern of $H_2(F)$ forcing one partition and a contrasting irreducible pattern forcing another.

## Definitions

Let $k$ be characteristic zero ($\mathbb{Q}$ for computation, stated over $\mathbb{C}$), $Q=k[x,y,z]$, $S=k[X,Y,Z]$ acting by differentiation, $A_F=Q/\mathrm{Ann}(F)$ with $F$ a quartic. Hilbert function $(1,3,5,3,1)$ means $\dim A_0=1,\dim A_1=3,\dim A_2=5,\dim A_3=3,\dim A_4=1$; length $13$, socle degree $4$. In Maeno–Watanabe indexing, $\mathrm{Hess}^{(k)}(F)$ is a $\dim A_k\times\dim A_k$ matrix of forms of degree $d-2k$ ($d=4$), and $H_k(F)=\det\mathrm{Hess}^{(k)}(F)$ has degree $(d-2k)\dim A_k$. Thus $H_1(F)$ is a sextic ($3\times 3$, degree $(4-2)\cdot 3=6$) and $H_2(F)$ is a $5\times 5$ determinant of degree $(4-4)\cdot 5=0$.

## Result

For every quartic dual generator $F$ with Hilbert function $(1,3,5,3,1)$, the Maeno–Watanabe second higher Hessian determinant $H_2(F)$ is a constant (degree $0$), hence admits no splitting/irreducible factor pattern (no degrees, multiplicities, or factor-incidence locus). Consequently the target universal lemma — that a stated splitting pattern of $H_2(F)$ forces one explicit non-SLP partition and a contrasting irreducible pattern forces another, with $(H_1,H_2)$ factor type determining $P_\ell$ for every $\ell$ — is impossible as stated: its $H_2$ hypothesis is unsatisfiable uniformly over the cell.

Certified witness: $F_0=X^4+X^3Y+Y^3Z+Z^4$ over $\mathbb{Q}$ has Hilbert function $(1,3,5,3,1)$ (length 13), $\mathrm{Ann}(F_0)_2=\mathrm{span}\{xz\}$,
$$H_1(F_0)=-a(2a^3c^2+2ab^4-16abc^3+b^5-8b^2c^3)/2,$$
a sextic splitting as linear $\times$ quintic (degrees $[1,5]$), and $H_2(F_0)=15116544$ (nonzero constant). Two further $(1,3,5,3,1)$ generators give the same constancy ($107495424$, $681836544$).

## Proof / Evidence

Structural proof (F-independent): by Maeno–Watanabe Definition 3.1, $\mathrm{Hess}^{(d)}(F)=\det(\alpha^{(d)}_i\alpha^{(d)}_jF)$ with entries homogeneous of degree $D-2d$; hence $\deg\det=(D-2d)\dim A_d$. For $D=4$, $d=2$, $\dim A_2=5$ by cell definition, degree $0$ for every such $F$ — a scalar, nonzero iff the $A_2$ pairing is nondegenerate (Gorenstein duality; $15116544\ne 0$ witnesses concretely). A scalar has no factor pattern; any lemma requiring one has unsatisfiable hypothesis.

Machine certificate (exact rational, sympy only): catalecticant ranks certify HF $(1,3,5,3,1)$; left nullspace of $6\times 6$ second catalecticant is 1-dimensional spanned by $XZ$; symbolic $\ell^2:A_1\to A_3$ determinant gives above $H_1$ sextic with `factor_list` degrees $[1,5]$; $5\times 5$ second-Hessian Gram determinant $=15116544$. Jordan partitions on $F_0$ (context, all summing to 13): $[5,3,3,1,1]$ generic ($x+y+z$), $[5,3,1,1,1,1,1]$ ($x$), $[4,4,2,2,1]$ ($y$), $[5,2,2,1,1,1,1]$ ($z$), $[5,3,2,2,1]$ ($y+z$), $[4,4,3,1,1]$ ($x-y+z$), with full kernel-dimension/rank tables in replay script — showing rich stratification none of which can be governed by factorization of constant $H_2$. Run `python3 output/artifacts/replay.py` → `VERIFY_OK`.

## Limitations

Refutes the target as stated/indexed (MW $H_1,H_2$). Does not claim Hessian data never constrains Jordan type: rank data does (Costa–Gondim Thm 4.7), and a repaired $(H_1,\mathrm{Hess}^0=F)$-factor criterion is left open (289-point scan consistent with per-$F$ determination). Does not address renaming some non-MW object "$H_2$". Characteristic zero only.

## Reproducibility

`python3 output/artifacts/replay.py` (stdlib+sympy; engine `output/artifacts/engine.py`) prints `VERIFY_OK` with `hf: [1, 3, 5, 3, 1] H1-degs: [1, 5] Hess2: 15116544`. All identities exact rational; factorizations are `sympy.factor_list` certificates. Independently reimplemented catalecticants confirm ranks, pivots, Gram dets, $H_1$, and Jordan kernel dims.

## References

- T. Maeno, J. Watanabe, Lefschetz elements of Artinian Gorenstein algebras and Hessians of homogeneous polynomials, arXiv:0903.3581 (Illinois J. Math. 53(2), 2009). — Def 3.1, Thm 3.1, Cor 3.1.
- B. Costa, R. Gondim, The Jordan type of graded Artinian Gorenstein algebras, arXiv:1811.02072. — rank-based (mixed-Hessian) Jordan determination, strictly finer than determinant factorization.
- N. Abdallah et al., Lefschetz properties of some codimension three Artinian Gorenstein algebras, arXiv:2203.01258. — SLP for Sperner $\le 6$ (generic type $[5,3,3,1,1]$).
- N. Altafi, Jordan types with small parts ..., arXiv:2008.02338; Altafi–Iarrobino–Macias Marques survey arXiv:2307.00957.
