# Solvable-subgroup rigidity of the free Burnside group B(2,665): every solvable subgroup is finite cyclic and the solvable radical is trivial

## Context

The free Burnside group $B(2,665)$ is the flagship Adian-bound torsion group: two
generators (minimal non-cyclic rank) and exponent $665 = 5\cdot 7\cdot 19$ (smallest
odd exponent with proved infiniteness, Adian). Its reduced group C*-algebra
$C^*_r(B(2,665))$ is a test case for the Elliott/Toms–Winter regularity,
Rosenberg–Ozawa unique-trace, and Brown–Ozawa programmes, where Powers
free-subgroup methods are unavailable. By Breuillard–Kalantar–Kennedy–Ozawa
(arXiv:1410.2518), unique trace of $C^*_r(G)$ is equivalent to triviality of the
amenable radical $\mathrm{Rad}(G)$. Olshanskii–Osin (arXiv:1401.7300) prove
C*-simplicity plus unique trace for $B(m,n)$ only for unspecified "sufficiently
large" odd $n$, leaving the Adian bound $n=665$ open. The result below closes the
solvable tier of that classification at exactly $n=665$ and certifies the boundary
of what remains open.

## Definitions

- $B(2,665) = \langle a_1,a_2 \mid X^{665} = 1\ \forall X\rangle$, the free group on
  two generators modulo all $665$-th powers.
- A subgroup is *solvable* if its derived series reaches $1$ in finitely many steps.
- The *solvable radical* is trivial if $B(2,665)$ has no nontrivial solvable normal
  subgroup.

## Result

**Theorem S.** Let $B = B(2,665)$. Every solvable subgroup $H \le B$ is cyclic of
order dividing $665$. In particular the solvable radical of $B$ is trivial: $B$ has
no nontrivial solvable normal subgroup.

**Corollary (finite-normal exclusion).** $B(2,665)$ has no nontrivial finite normal
subgroup, hence no nontrivial abelian normal subgroup.

## Proof / evidence

Pinned inputs, all valid at $n=665$:

- (I1) $B(2,665)$ is infinite of exponent $665$ (Adian).
- (I2) Every finite subgroup of $B(m,n)$ is cyclic for $m>1$, odd $n\ge 665$
  (Adian Ch. VII Thm 1.8; quoted as Cor. 1 of arXiv:1811.07167, scope $m>1$,
  odd $n\ge 665$).
- (I3) $Z(B(m,n)) = 1$ for $m>1$, odd $n\ge 665$ (arXiv:1811.07167 Lemma 2.1 via
  Adian Ch. VI Thm 3.4).
- (I4) $665 = 5\cdot 7\cdot 19$ is squarefree; for every $d\mid 665$,
  $\varphi(d)\in\{4,6,18,24,72,108,432\}$, so $\gcd(665,\varphi(d))=1$; CRT
  idempotents $e_5=266$, $e_7=190$, $e_{19}=210$ witness
  $\mathbf{Z}/665\cong\mathbf{F}_5\times\mathbf{F}_7\times\mathbf{F}_{19}$
  (machine-checked, ALL CHECKS PASSED).

**Lemma A.** Every abelian $A\le B(2,665)$ is cyclic of order dividing $665$.
*Proof.* Every f.g. subgroup of $A$ is finite, hence cyclic by (I2); $665A=0$ makes
$A$ a $\mathbf{Z}/665$-module, $A=A_5\oplus A_7\oplus A_{19}$ with $A_p$ an
$\mathbf{F}_p$-space. If $\dim A_p\ge 2$ then $C_p\times C_p\le A$ is finite
non-cyclic of order $p^2\nmid 665$, contradicting (I2). Hence $|A_p|\le p$ and
$|A|\mid 665$ squarefree, so $A$ is cyclic. ∎

**Lemma F.** $B(2,665)$ has no nontrivial finite normal subgroup. *Proof.* If
$1\ne N\triangleleft B$ is finite, (I2) gives $N=\langle g\rangle$ cyclic of order
$d\mid 665$, $d>1$. Conjugation $B\to\mathrm{Aut}(N)$ has image of order dividing
$\varphi(d)$ and exponent dividing $665$; by (I4) $\gcd(665,\varphi(d))=1$, so the
image is trivial, $N\le Z(B)=1$ by (I3), contradiction. ∎

**Finiteness theorem.** Every f.g. solvable torsion group is finite (induction on
derived length: last derived term is the normal closure of finitely many iterated
commutators, f.g. as a $\mathbf{Z}[Q]$-module over finite quotient $Q$, hence f.g.
abelian torsion, hence finite; so the extension is finite).

*Proof of Theorem S.* Let $H\le B$ be solvable. Every $\langle x,y\rangle\le H$ is
solvable f.g. torsion of exponent $665$, hence finite by the finiteness theorem,
hence cyclic by (I2); so $H$ is abelian, and Lemma A makes it cyclic of order
dividing $665$. A solvable normal $N$ is then finite cyclic, so $N=1$ by Lemma F. ∎

No "sufficiently large exponent" machinery is used.

## Limitations

Does NOT prove the preset fallback (triviality of the full amenable radical;
infinite amenable normals remain open at $665$) and does NOT prove C*-simplicity
or unique trace of $C^*_r(B(2,665))$. Uses Adian inputs (I1)–(I3) as cited black
boxes at $n\ge 665$ rather than re-deriving them. The single missing input for the
full radical is: every non-cyclic (equivalently, every amenable) subgroup of
$B(2,665)$ is non-amenable — proved in the literature only for $n\gg 665$
(Ivanov $n>10^{78}$; Olshanskii–Osin unspecified large $n$).

## Reproducibility

`output/artifacts/verify_target_inputs.py` (stdlib only):
`python3 output/artifacts/verify_target_inputs.py` exits 0, ALL CHECKS PASSED —
CRT idempotents, divisors/$\varphi$ values, abelianization order $665^2=442225$,
$\gcd(665,\varphi(d))=1$ for all $d\mid 665$.

## References

- S. I. Adian, *The Burnside problem and identities in groups* (1979): infiniteness
  at odd $n\ge 665$; finite subgroups cyclic (Ch. VII Thm 1.8); trivial center
  (Ch. VI Thm 3.4).
- S. I. Adian–V. S. Atabekyan, arXiv:1811.07167: scope-pinned ($m>1$, odd
  $n\ge 665$) statements of the above; presentation $\langle a_i\mid X^n=1\rangle$.
- E. Breuillard–M. Kalantar–M. Kennedy–N. Ozawa, arXiv:1410.2518: unique trace
  $\Leftrightarrow$ trivial amenable radical (Thm 1.3/Cor. 4.3).
- A. Yu. Olshanskii–D. V. Osin, arXiv:1401.7300: C*-simplicity + unique trace for
  $B(m,n)$ only for sufficiently large odd $n$ — not $665$.
- D. V. Osin, math/0404073: uniform non-amenability for large odd exponent.
- S. V. Ivanov, math/0210191: Q-subgroup theorem for $n>10^{78}$.
